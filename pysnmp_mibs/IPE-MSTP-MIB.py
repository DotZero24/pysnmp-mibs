# SNMP MIB module (IPE-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-MSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:52 2025
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableDisableValue(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )



class IpeBridgePriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )



class IpePortPathCost(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )



class IpePortPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )



class IpePortRole(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
          ("disabled", 1),
          ("alternate", 2),
          ("backup", 3),
          ("root", 4),
          ("designated", 5))
    )



class IpePortState(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("restricted", 8),
          ("guarded", 9))
    )



class IpeVlanList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsMstpGroup_ObjectIdentity = ObjectIdentity
asMstpGroup = _AsMstpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44)
)
_AsMstpBridgeCistTable_Object = MibTable
asMstpBridgeCistTable = _AsMstpBridgeCistTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1)
)
if mibBuilder.loadTexts:
    asMstpBridgeCistTable.setStatus("current")
_AsMstpBridgeCistEntry_Object = MibTableRow
asMstpBridgeCistEntry = _AsMstpBridgeCistEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1, 1)
)
asMstpBridgeCistEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "asMstpBridgeCistIndex"),
)
if mibBuilder.loadTexts:
    asMstpBridgeCistEntry.setStatus("current")


class _AsMstpBridgeCistIndex_Type(Integer32):
    """Custom type asMstpBridgeCistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AsMstpBridgeCistIndex_Type.__name__ = "Integer32"
_AsMstpBridgeCistIndex_Object = MibTableColumn
asMstpBridgeCistIndex = _AsMstpBridgeCistIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1, 1, 1),
    _AsMstpBridgeCistIndex_Type()
)
asMstpBridgeCistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpBridgeCistIndex.setStatus("current")
_AsMstpBridgeCistNEAddress_Type = IpAddress
_AsMstpBridgeCistNEAddress_Object = MibTableColumn
asMstpBridgeCistNEAddress = _AsMstpBridgeCistNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1, 1, 2),
    _AsMstpBridgeCistNEAddress_Type()
)
asMstpBridgeCistNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpBridgeCistNEAddress.setStatus("obsolete")
_AsMstpBridgeCistRegionalRoot_Type = BridgeId
_AsMstpBridgeCistRegionalRoot_Object = MibTableColumn
asMstpBridgeCistRegionalRoot = _AsMstpBridgeCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1, 1, 3),
    _AsMstpBridgeCistRegionalRoot_Type()
)
asMstpBridgeCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpBridgeCistRegionalRoot.setStatus("current")
_AsMstpBridgeCistTopChanges_Type = Counter32
_AsMstpBridgeCistTopChanges_Object = MibTableColumn
asMstpBridgeCistTopChanges = _AsMstpBridgeCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1, 1, 4),
    _AsMstpBridgeCistTopChanges_Type()
)
asMstpBridgeCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpBridgeCistTopChanges.setStatus("current")
_AsMstpBridgeCistRoot_Type = BridgeId
_AsMstpBridgeCistRoot_Object = MibTableColumn
asMstpBridgeCistRoot = _AsMstpBridgeCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 1, 1, 5),
    _AsMstpBridgeCistRoot_Type()
)
asMstpBridgeCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpBridgeCistRoot.setStatus("current")
_AsMstpBridgeMstTable_Object = MibTable
asMstpBridgeMstTable = _AsMstpBridgeMstTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 2)
)
if mibBuilder.loadTexts:
    asMstpBridgeMstTable.setStatus("current")
_AsMstpBridgeMstEntry_Object = MibTableRow
asMstpBridgeMstEntry = _AsMstpBridgeMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 2, 1)
)
asMstpBridgeMstEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "asMstpBridgeMstIndex"),
)
if mibBuilder.loadTexts:
    asMstpBridgeMstEntry.setStatus("current")


class _AsMstpBridgeMstIndex_Type(Integer32):
    """Custom type asMstpBridgeMstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AsMstpBridgeMstIndex_Type.__name__ = "Integer32"
_AsMstpBridgeMstIndex_Object = MibTableColumn
asMstpBridgeMstIndex = _AsMstpBridgeMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 2, 1, 1),
    _AsMstpBridgeMstIndex_Type()
)
asMstpBridgeMstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpBridgeMstIndex.setStatus("current")
_AsMstpBridgeMstNEAddress_Type = IpAddress
_AsMstpBridgeMstNEAddress_Object = MibTableColumn
asMstpBridgeMstNEAddress = _AsMstpBridgeMstNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 2, 1, 2),
    _AsMstpBridgeMstNEAddress_Type()
)
asMstpBridgeMstNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpBridgeMstNEAddress.setStatus("obsolete")
_AsMstpBridgeMstRegionalRoot_Type = BridgeId
_AsMstpBridgeMstRegionalRoot_Object = MibTableColumn
asMstpBridgeMstRegionalRoot = _AsMstpBridgeMstRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 2, 1, 3),
    _AsMstpBridgeMstRegionalRoot_Type()
)
asMstpBridgeMstRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpBridgeMstRegionalRoot.setStatus("current")
_AsMstpBridgeMstTopChanges_Type = Counter32
_AsMstpBridgeMstTopChanges_Object = MibTableColumn
asMstpBridgeMstTopChanges = _AsMstpBridgeMstTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 2, 1, 4),
    _AsMstpBridgeMstTopChanges_Type()
)
asMstpBridgeMstTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpBridgeMstTopChanges.setStatus("current")
_AsMstpPortCistTable_Object = MibTable
asMstpPortCistTable = _AsMstpPortCistTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3)
)
if mibBuilder.loadTexts:
    asMstpPortCistTable.setStatus("current")
_AsMstpPortCistEntry_Object = MibTableRow
asMstpPortCistEntry = _AsMstpPortCistEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1)
)
asMstpPortCistEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "asMstpPortCistIfIndex"),
)
if mibBuilder.loadTexts:
    asMstpPortCistEntry.setStatus("current")
_AsMstpPortCistIfIndex_Type = InterfaceIndex
_AsMstpPortCistIfIndex_Object = MibTableColumn
asMstpPortCistIfIndex = _AsMstpPortCistIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 1),
    _AsMstpPortCistIfIndex_Type()
)
asMstpPortCistIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpPortCistIfIndex.setStatus("current")
_AsMstpPortCistNEAddress_Type = IpAddress
_AsMstpPortCistNEAddress_Object = MibTableColumn
asMstpPortCistNEAddress = _AsMstpPortCistNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 2),
    _AsMstpPortCistNEAddress_Type()
)
asMstpPortCistNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpPortCistNEAddress.setStatus("obsolete")
_AsMstpPortCistRole_Type = IpePortRole
_AsMstpPortCistRole_Object = MibTableColumn
asMstpPortCistRole = _AsMstpPortCistRole_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 3),
    _AsMstpPortCistRole_Type()
)
asMstpPortCistRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistRole.setStatus("current")
_AsMstpPortCistState_Type = IpePortState
_AsMstpPortCistState_Object = MibTableColumn
asMstpPortCistState = _AsMstpPortCistState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 4),
    _AsMstpPortCistState_Type()
)
asMstpPortCistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistState.setStatus("current")
_AsMstpPortCistRegionalRoot_Type = BridgeId
_AsMstpPortCistRegionalRoot_Object = MibTableColumn
asMstpPortCistRegionalRoot = _AsMstpPortCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 5),
    _AsMstpPortCistRegionalRoot_Type()
)
asMstpPortCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistRegionalRoot.setStatus("current")


class _AsMstpPortCistProtoVersion_Type(Integer32):
    """Custom type asMstpPortCistProtoVersion based on Integer32"""
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
          ("stp", 1),
          ("rstp", 2),
          ("mstp", 3))
    )


_AsMstpPortCistProtoVersion_Type.__name__ = "Integer32"
_AsMstpPortCistProtoVersion_Object = MibTableColumn
asMstpPortCistProtoVersion = _AsMstpPortCistProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 6),
    _AsMstpPortCistProtoVersion_Type()
)
asMstpPortCistProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistProtoVersion.setStatus("current")
_AsMstpPortCistPathCost_Type = Integer32
_AsMstpPortCistPathCost_Object = MibTableColumn
asMstpPortCistPathCost = _AsMstpPortCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 7),
    _AsMstpPortCistPathCost_Type()
)
asMstpPortCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistPathCost.setStatus("current")


class _AsMstpPortCistInvalidBpdu_Type(Integer32):
    """Custom type asMstpPortCistInvalidBpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("invalid", 0)
    )


_AsMstpPortCistInvalidBpdu_Type.__name__ = "Integer32"
_AsMstpPortCistInvalidBpdu_Object = MibTableColumn
asMstpPortCistInvalidBpdu = _AsMstpPortCistInvalidBpdu_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 8),
    _AsMstpPortCistInvalidBpdu_Type()
)
asMstpPortCistInvalidBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistInvalidBpdu.setStatus("current")
_AsMstpPortCistDesignatedPathCost_Type = Integer32
_AsMstpPortCistDesignatedPathCost_Object = MibTableColumn
asMstpPortCistDesignatedPathCost = _AsMstpPortCistDesignatedPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 9),
    _AsMstpPortCistDesignatedPathCost_Type()
)
asMstpPortCistDesignatedPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistDesignatedPathCost.setStatus("current")
_AsMstpPortCistDesignatedBridge_Type = BridgeId
_AsMstpPortCistDesignatedBridge_Object = MibTableColumn
asMstpPortCistDesignatedBridge = _AsMstpPortCistDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 10),
    _AsMstpPortCistDesignatedBridge_Type()
)
asMstpPortCistDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistDesignatedBridge.setStatus("current")
_AsMstpPortCistDesignatedPort_Type = OctetString
_AsMstpPortCistDesignatedPort_Object = MibTableColumn
asMstpPortCistDesignatedPort = _AsMstpPortCistDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 11),
    _AsMstpPortCistDesignatedPort_Type()
)
asMstpPortCistDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistDesignatedPort.setStatus("current")
_AsMstpPortCistForwardTransitions_Type = Counter32
_AsMstpPortCistForwardTransitions_Object = MibTableColumn
asMstpPortCistForwardTransitions = _AsMstpPortCistForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 12),
    _AsMstpPortCistForwardTransitions_Type()
)
asMstpPortCistForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistForwardTransitions.setStatus("current")


class _AsMstpPortCistOperEdgePort_Type(Integer32):
    """Custom type asMstpPortCistOperEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOff", 0),
          ("alarmOn", 1))
    )


_AsMstpPortCistOperEdgePort_Type.__name__ = "Integer32"
_AsMstpPortCistOperEdgePort_Object = MibTableColumn
asMstpPortCistOperEdgePort = _AsMstpPortCistOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 3, 1, 13),
    _AsMstpPortCistOperEdgePort_Type()
)
asMstpPortCistOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortCistOperEdgePort.setStatus("current")
_AsMstpPortMstTable_Object = MibTable
asMstpPortMstTable = _AsMstpPortMstTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4)
)
if mibBuilder.loadTexts:
    asMstpPortMstTable.setStatus("current")
_AsMstpPortMstEntry_Object = MibTableRow
asMstpPortMstEntry = _AsMstpPortMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1)
)
asMstpPortMstEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "asMstpPortMstIfIndex"),
    (0, "IPE-MSTP-MIB", "asMstpPortMstIndex"),
)
if mibBuilder.loadTexts:
    asMstpPortMstEntry.setStatus("current")
_AsMstpPortMstIfIndex_Type = InterfaceIndex
_AsMstpPortMstIfIndex_Object = MibTableColumn
asMstpPortMstIfIndex = _AsMstpPortMstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 1),
    _AsMstpPortMstIfIndex_Type()
)
asMstpPortMstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpPortMstIfIndex.setStatus("current")


class _AsMstpPortMstIndex_Type(Integer32):
    """Custom type asMstpPortMstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AsMstpPortMstIndex_Type.__name__ = "Integer32"
_AsMstpPortMstIndex_Object = MibTableColumn
asMstpPortMstIndex = _AsMstpPortMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 2),
    _AsMstpPortMstIndex_Type()
)
asMstpPortMstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpPortMstIndex.setStatus("current")
_AsMstpPortMstNEAddress_Type = IpAddress
_AsMstpPortMstNEAddress_Object = MibTableColumn
asMstpPortMstNEAddress = _AsMstpPortMstNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 3),
    _AsMstpPortMstNEAddress_Type()
)
asMstpPortMstNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMstpPortMstNEAddress.setStatus("obsolete")
_AsMstpPortMstRole_Type = IpePortRole
_AsMstpPortMstRole_Object = MibTableColumn
asMstpPortMstRole = _AsMstpPortMstRole_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 4),
    _AsMstpPortMstRole_Type()
)
asMstpPortMstRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstRole.setStatus("current")
_AsMstpPortMstState_Type = IpePortState
_AsMstpPortMstState_Object = MibTableColumn
asMstpPortMstState = _AsMstpPortMstState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 5),
    _AsMstpPortMstState_Type()
)
asMstpPortMstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstState.setStatus("current")
_AsMstpPortMstRegionalRoot_Type = BridgeId
_AsMstpPortMstRegionalRoot_Object = MibTableColumn
asMstpPortMstRegionalRoot = _AsMstpPortMstRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 6),
    _AsMstpPortMstRegionalRoot_Type()
)
asMstpPortMstRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstRegionalRoot.setStatus("current")
_AsMstpPortMstPathCost_Type = Integer32
_AsMstpPortMstPathCost_Object = MibTableColumn
asMstpPortMstPathCost = _AsMstpPortMstPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 7),
    _AsMstpPortMstPathCost_Type()
)
asMstpPortMstPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstPathCost.setStatus("current")
_AsMstpPortMstDesignatedPathCost_Type = Integer32
_AsMstpPortMstDesignatedPathCost_Object = MibTableColumn
asMstpPortMstDesignatedPathCost = _AsMstpPortMstDesignatedPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 8),
    _AsMstpPortMstDesignatedPathCost_Type()
)
asMstpPortMstDesignatedPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstDesignatedPathCost.setStatus("current")
_AsMstpPortMstDesignatedBridge_Type = BridgeId
_AsMstpPortMstDesignatedBridge_Object = MibTableColumn
asMstpPortMstDesignatedBridge = _AsMstpPortMstDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 9),
    _AsMstpPortMstDesignatedBridge_Type()
)
asMstpPortMstDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstDesignatedBridge.setStatus("current")
_AsMstpPortMstDesignatedPort_Type = OctetString
_AsMstpPortMstDesignatedPort_Object = MibTableColumn
asMstpPortMstDesignatedPort = _AsMstpPortMstDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 44, 4, 1, 10),
    _AsMstpPortMstDesignatedPort_Type()
)
asMstpPortMstDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMstpPortMstDesignatedPort.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvMstpGroup_ObjectIdentity = ObjectIdentity
provMstpGroup = _ProvMstpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44)
)
_ProvMstpBridgeTable_Object = MibTable
provMstpBridgeTable = _ProvMstpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1)
)
if mibBuilder.loadTexts:
    provMstpBridgeTable.setStatus("current")
_ProvMstpBridgeEntry_Object = MibTableRow
provMstpBridgeEntry = _ProvMstpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1)
)
provMstpBridgeEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "provMstpBridgeIndex"),
)
if mibBuilder.loadTexts:
    provMstpBridgeEntry.setStatus("current")


class _ProvMstpBridgeIndex_Type(Integer32):
    """Custom type provMstpBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ProvMstpBridgeIndex_Type.__name__ = "Integer32"
_ProvMstpBridgeIndex_Object = MibTableColumn
provMstpBridgeIndex = _ProvMstpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 1),
    _ProvMstpBridgeIndex_Type()
)
provMstpBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpBridgeIndex.setStatus("current")
_ProvMstpBridgeNEAddress_Type = IpAddress
_ProvMstpBridgeNEAddress_Object = MibTableColumn
provMstpBridgeNEAddress = _ProvMstpBridgeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 2),
    _ProvMstpBridgeNEAddress_Type()
)
provMstpBridgeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpBridgeNEAddress.setStatus("current")


class _ProvMstpBridgeEnable_Type(EnableDisableValue):
    """Custom type provMstpBridgeEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpBridgeEnable_Type.__name__ = "EnableDisableValue"
_ProvMstpBridgeEnable_Object = MibTableColumn
provMstpBridgeEnable = _ProvMstpBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 3),
    _ProvMstpBridgeEnable_Type()
)
provMstpBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeEnable.setStatus("current")


class _ProvMstpBridgeMaxAge_Type(Integer32):
    """Custom type provMstpBridgeMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_ProvMstpBridgeMaxAge_Type.__name__ = "Integer32"
_ProvMstpBridgeMaxAge_Object = MibTableColumn
provMstpBridgeMaxAge = _ProvMstpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 4),
    _ProvMstpBridgeMaxAge_Type()
)
provMstpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    provMstpBridgeMaxAge.setUnits("seconds")


class _ProvMstpBridgeHelloTime_Type(Integer32):
    """Custom type provMstpBridgeHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ProvMstpBridgeHelloTime_Type.__name__ = "Integer32"
_ProvMstpBridgeHelloTime_Object = MibTableColumn
provMstpBridgeHelloTime = _ProvMstpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 5),
    _ProvMstpBridgeHelloTime_Type()
)
provMstpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    provMstpBridgeHelloTime.setUnits("seconds")


class _ProvMstpBridgeForwardDelay_Type(Integer32):
    """Custom type provMstpBridgeForwardDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_ProvMstpBridgeForwardDelay_Type.__name__ = "Integer32"
_ProvMstpBridgeForwardDelay_Object = MibTableColumn
provMstpBridgeForwardDelay = _ProvMstpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 6),
    _ProvMstpBridgeForwardDelay_Type()
)
provMstpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    provMstpBridgeForwardDelay.setUnits("seconds")


class _ProvMstpBridgeTxHoldCount_Type(Integer32):
    """Custom type provMstpBridgeTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ProvMstpBridgeTxHoldCount_Type.__name__ = "Integer32"
_ProvMstpBridgeTxHoldCount_Object = MibTableColumn
provMstpBridgeTxHoldCount = _ProvMstpBridgeTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 7),
    _ProvMstpBridgeTxHoldCount_Type()
)
provMstpBridgeTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeTxHoldCount.setStatus("current")


class _ProvMstpBridgeMaxHopCount_Type(Integer32):
    """Custom type provMstpBridgeMaxHopCount based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_ProvMstpBridgeMaxHopCount_Type.__name__ = "Integer32"
_ProvMstpBridgeMaxHopCount_Object = MibTableColumn
provMstpBridgeMaxHopCount = _ProvMstpBridgeMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 12),
    _ProvMstpBridgeMaxHopCount_Type()
)
provMstpBridgeMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeMaxHopCount.setStatus("current")


class _ProvMstpBridgeRegionName_Type(DisplayString):
    """Custom type provMstpBridgeRegionName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMstpBridgeRegionName_Type.__name__ = "DisplayString"
_ProvMstpBridgeRegionName_Object = MibTableColumn
provMstpBridgeRegionName = _ProvMstpBridgeRegionName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 13),
    _ProvMstpBridgeRegionName_Type()
)
provMstpBridgeRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeRegionName.setStatus("current")


class _ProvMstpBridgeRevisionNum_Type(Integer32):
    """Custom type provMstpBridgeRevisionNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ProvMstpBridgeRevisionNum_Type.__name__ = "Integer32"
_ProvMstpBridgeRevisionNum_Object = MibTableColumn
provMstpBridgeRevisionNum = _ProvMstpBridgeRevisionNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 14),
    _ProvMstpBridgeRevisionNum_Type()
)
provMstpBridgeRevisionNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeRevisionNum.setStatus("current")


class _ProvMstpBridgeBpduFilter_Type(EnableDisableValue):
    """Custom type provMstpBridgeBpduFilter based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpBridgeBpduFilter_Type.__name__ = "EnableDisableValue"
_ProvMstpBridgeBpduFilter_Object = MibTableColumn
provMstpBridgeBpduFilter = _ProvMstpBridgeBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 15),
    _ProvMstpBridgeBpduFilter_Type()
)
provMstpBridgeBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeBpduFilter.setStatus("current")


class _ProvMstpBridgeBpduGuardTimer_Type(Integer32):
    """Custom type provMstpBridgeBpduGuardTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_ProvMstpBridgeBpduGuardTimer_Type.__name__ = "Integer32"
_ProvMstpBridgeBpduGuardTimer_Object = MibTableColumn
provMstpBridgeBpduGuardTimer = _ProvMstpBridgeBpduGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 1, 1, 16),
    _ProvMstpBridgeBpduGuardTimer_Type()
)
provMstpBridgeBpduGuardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeBpduGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    provMstpBridgeBpduGuardTimer.setUnits("seconds")
_ProvMstpBridgeCistTable_Object = MibTable
provMstpBridgeCistTable = _ProvMstpBridgeCistTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 2)
)
if mibBuilder.loadTexts:
    provMstpBridgeCistTable.setStatus("current")
_ProvMstpBridgeCistEntry_Object = MibTableRow
provMstpBridgeCistEntry = _ProvMstpBridgeCistEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 2, 1)
)
provMstpBridgeCistEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "provMstpBridgeCistIndex"),
)
if mibBuilder.loadTexts:
    provMstpBridgeCistEntry.setStatus("current")


class _ProvMstpBridgeCistIndex_Type(Integer32):
    """Custom type provMstpBridgeCistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ProvMstpBridgeCistIndex_Type.__name__ = "Integer32"
_ProvMstpBridgeCistIndex_Object = MibTableColumn
provMstpBridgeCistIndex = _ProvMstpBridgeCistIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 2, 1, 1),
    _ProvMstpBridgeCistIndex_Type()
)
provMstpBridgeCistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpBridgeCistIndex.setStatus("current")
_ProvMstpBridgeCistNEAddress_Type = IpAddress
_ProvMstpBridgeCistNEAddress_Object = MibTableColumn
provMstpBridgeCistNEAddress = _ProvMstpBridgeCistNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 2, 1, 2),
    _ProvMstpBridgeCistNEAddress_Type()
)
provMstpBridgeCistNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpBridgeCistNEAddress.setStatus("current")


class _ProvMstpBridgeCistPriority_Type(IpeBridgePriority):
    """Custom type provMstpBridgeCistPriority based on IpeBridgePriority"""
    defaultValue = 32768


_ProvMstpBridgeCistPriority_Type.__name__ = "IpeBridgePriority"
_ProvMstpBridgeCistPriority_Object = MibTableColumn
provMstpBridgeCistPriority = _ProvMstpBridgeCistPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 2, 1, 3),
    _ProvMstpBridgeCistPriority_Type()
)
provMstpBridgeCistPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeCistPriority.setStatus("current")
_ProvMstpBridgeCistVlanList_Type = IpeVlanList
_ProvMstpBridgeCistVlanList_Object = MibTableColumn
provMstpBridgeCistVlanList = _ProvMstpBridgeCistVlanList_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 2, 1, 4),
    _ProvMstpBridgeCistVlanList_Type()
)
provMstpBridgeCistVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpBridgeCistVlanList.setStatus("current")
_ProvMstpBridgeMstTable_Object = MibTable
provMstpBridgeMstTable = _ProvMstpBridgeMstTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3)
)
if mibBuilder.loadTexts:
    provMstpBridgeMstTable.setStatus("current")
_ProvMstpBridgeMstEntry_Object = MibTableRow
provMstpBridgeMstEntry = _ProvMstpBridgeMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1)
)
provMstpBridgeMstEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "provMstpBridgeMstIndex"),
)
if mibBuilder.loadTexts:
    provMstpBridgeMstEntry.setStatus("current")


class _ProvMstpBridgeMstIndex_Type(Integer32):
    """Custom type provMstpBridgeMstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ProvMstpBridgeMstIndex_Type.__name__ = "Integer32"
_ProvMstpBridgeMstIndex_Object = MibTableColumn
provMstpBridgeMstIndex = _ProvMstpBridgeMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1, 1),
    _ProvMstpBridgeMstIndex_Type()
)
provMstpBridgeMstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpBridgeMstIndex.setStatus("current")
_ProvMstpBridgeMstNEAddress_Type = IpAddress
_ProvMstpBridgeMstNEAddress_Object = MibTableColumn
provMstpBridgeMstNEAddress = _ProvMstpBridgeMstNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1, 2),
    _ProvMstpBridgeMstNEAddress_Type()
)
provMstpBridgeMstNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpBridgeMstNEAddress.setStatus("obsolete")


class _ProvMstpBridgeMstPriority_Type(IpeBridgePriority):
    """Custom type provMstpBridgeMstPriority based on IpeBridgePriority"""
    defaultValue = 32768


_ProvMstpBridgeMstPriority_Type.__name__ = "IpeBridgePriority"
_ProvMstpBridgeMstPriority_Object = MibTableColumn
provMstpBridgeMstPriority = _ProvMstpBridgeMstPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1, 3),
    _ProvMstpBridgeMstPriority_Type()
)
provMstpBridgeMstPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provMstpBridgeMstPriority.setStatus("current")
_ProvMstpBridgeMstVlanList_Type = IpeVlanList
_ProvMstpBridgeMstVlanList_Object = MibTableColumn
provMstpBridgeMstVlanList = _ProvMstpBridgeMstVlanList_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1, 4),
    _ProvMstpBridgeMstVlanList_Type()
)
provMstpBridgeMstVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provMstpBridgeMstVlanList.setStatus("current")


class _ProvMstpBridgeMstInstanceNum_Type(Integer32):
    """Custom type provMstpBridgeMstInstanceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_ProvMstpBridgeMstInstanceNum_Type.__name__ = "Integer32"
_ProvMstpBridgeMstInstanceNum_Object = MibTableColumn
provMstpBridgeMstInstanceNum = _ProvMstpBridgeMstInstanceNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1, 5),
    _ProvMstpBridgeMstInstanceNum_Type()
)
provMstpBridgeMstInstanceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provMstpBridgeMstInstanceNum.setStatus("current")
_ProvMstpBridgeMstRowStatus_Type = RowStatus
_ProvMstpBridgeMstRowStatus_Object = MibTableColumn
provMstpBridgeMstRowStatus = _ProvMstpBridgeMstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 3, 1, 6),
    _ProvMstpBridgeMstRowStatus_Type()
)
provMstpBridgeMstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provMstpBridgeMstRowStatus.setStatus("current")
_ProvMstpPortCistTable_Object = MibTable
provMstpPortCistTable = _ProvMstpPortCistTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4)
)
if mibBuilder.loadTexts:
    provMstpPortCistTable.setStatus("current")
_ProvMstpPortCistEntry_Object = MibTableRow
provMstpPortCistEntry = _ProvMstpPortCistEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1)
)
provMstpPortCistEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "provMstpPortCistIfIndex"),
)
if mibBuilder.loadTexts:
    provMstpPortCistEntry.setStatus("current")
_ProvMstpPortCistIfIndex_Type = InterfaceIndex
_ProvMstpPortCistIfIndex_Object = MibTableColumn
provMstpPortCistIfIndex = _ProvMstpPortCistIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 1),
    _ProvMstpPortCistIfIndex_Type()
)
provMstpPortCistIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpPortCistIfIndex.setStatus("current")
_ProvMstpPortCistNEAddress_Type = IpAddress
_ProvMstpPortCistNEAddress_Object = MibTableColumn
provMstpPortCistNEAddress = _ProvMstpPortCistNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 2),
    _ProvMstpPortCistNEAddress_Type()
)
provMstpPortCistNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpPortCistNEAddress.setStatus("obsolete")


class _ProvMstpPortCistPriority_Type(IpePortPriority):
    """Custom type provMstpPortCistPriority based on IpePortPriority"""
    defaultValue = 0


_ProvMstpPortCistPriority_Type.__name__ = "IpePortPriority"
_ProvMstpPortCistPriority_Object = MibTableColumn
provMstpPortCistPriority = _ProvMstpPortCistPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 3),
    _ProvMstpPortCistPriority_Type()
)
provMstpPortCistPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortCistPriority.setStatus("current")


class _ProvMstpPortCistEnable_Type(EnableDisableValue):
    """Custom type provMstpPortCistEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpPortCistEnable_Type.__name__ = "EnableDisableValue"
_ProvMstpPortCistEnable_Object = MibTableColumn
provMstpPortCistEnable = _ProvMstpPortCistEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 4),
    _ProvMstpPortCistEnable_Type()
)
provMstpPortCistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortCistEnable.setStatus("current")


class _ProvMstpPortCistEdgePort_Type(EnableDisableValue):
    """Custom type provMstpPortCistEdgePort based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpPortCistEdgePort_Type.__name__ = "EnableDisableValue"
_ProvMstpPortCistEdgePort_Object = MibTableColumn
provMstpPortCistEdgePort = _ProvMstpPortCistEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 5),
    _ProvMstpPortCistEdgePort_Type()
)
provMstpPortCistEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortCistEdgePort.setStatus("current")
_ProvMstpPortCistPathCost_Type = IpePortPathCost
_ProvMstpPortCistPathCost_Object = MibTableColumn
provMstpPortCistPathCost = _ProvMstpPortCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 6),
    _ProvMstpPortCistPathCost_Type()
)
provMstpPortCistPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortCistPathCost.setStatus("current")


class _ProvMstpPortCistBpduGuard_Type(EnableDisableValue):
    """Custom type provMstpPortCistBpduGuard based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpPortCistBpduGuard_Type.__name__ = "EnableDisableValue"
_ProvMstpPortCistBpduGuard_Object = MibTableColumn
provMstpPortCistBpduGuard = _ProvMstpPortCistBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 7),
    _ProvMstpPortCistBpduGuard_Type()
)
provMstpPortCistBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortCistBpduGuard.setStatus("current")


class _ProvMstpPortCistRestrictRole_Type(EnableDisableValue):
    """Custom type provMstpPortCistRestrictRole based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpPortCistRestrictRole_Type.__name__ = "EnableDisableValue"
_ProvMstpPortCistRestrictRole_Object = MibTableColumn
provMstpPortCistRestrictRole = _ProvMstpPortCistRestrictRole_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 4, 1, 8),
    _ProvMstpPortCistRestrictRole_Type()
)
provMstpPortCistRestrictRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortCistRestrictRole.setStatus("current")
_ProvMstpPortMstTable_Object = MibTable
provMstpPortMstTable = _ProvMstpPortMstTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5)
)
if mibBuilder.loadTexts:
    provMstpPortMstTable.setStatus("current")
_ProvMstpPortMstEntry_Object = MibTableRow
provMstpPortMstEntry = _ProvMstpPortMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1)
)
provMstpPortMstEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "provMstpPortMstIfIndex"),
    (0, "IPE-MSTP-MIB", "provMstpPortMstIndex"),
)
if mibBuilder.loadTexts:
    provMstpPortMstEntry.setStatus("current")
_ProvMstpPortMstIfIndex_Type = InterfaceIndex
_ProvMstpPortMstIfIndex_Object = MibTableColumn
provMstpPortMstIfIndex = _ProvMstpPortMstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1, 1),
    _ProvMstpPortMstIfIndex_Type()
)
provMstpPortMstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpPortMstIfIndex.setStatus("current")


class _ProvMstpPortMstIndex_Type(Integer32):
    """Custom type provMstpPortMstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ProvMstpPortMstIndex_Type.__name__ = "Integer32"
_ProvMstpPortMstIndex_Object = MibTableColumn
provMstpPortMstIndex = _ProvMstpPortMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1, 2),
    _ProvMstpPortMstIndex_Type()
)
provMstpPortMstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpPortMstIndex.setStatus("current")
_ProvMstpPortMstNEAddress_Type = IpAddress
_ProvMstpPortMstNEAddress_Object = MibTableColumn
provMstpPortMstNEAddress = _ProvMstpPortMstNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1, 3),
    _ProvMstpPortMstNEAddress_Type()
)
provMstpPortMstNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMstpPortMstNEAddress.setStatus("obsolete")


class _ProvMstpPortMstPriority_Type(IpePortPriority):
    """Custom type provMstpPortMstPriority based on IpePortPriority"""
    defaultValue = 0


_ProvMstpPortMstPriority_Type.__name__ = "IpePortPriority"
_ProvMstpPortMstPriority_Object = MibTableColumn
provMstpPortMstPriority = _ProvMstpPortMstPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1, 4),
    _ProvMstpPortMstPriority_Type()
)
provMstpPortMstPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortMstPriority.setStatus("current")


class _ProvMstpPortMstEnable_Type(EnableDisableValue):
    """Custom type provMstpPortMstEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvMstpPortMstEnable_Type.__name__ = "EnableDisableValue"
_ProvMstpPortMstEnable_Object = MibTableColumn
provMstpPortMstEnable = _ProvMstpPortMstEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1, 5),
    _ProvMstpPortMstEnable_Type()
)
provMstpPortMstEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortMstEnable.setStatus("current")
_ProvMstpPortMstPathCost_Type = IpePortPathCost
_ProvMstpPortMstPathCost_Object = MibTableColumn
provMstpPortMstPathCost = _ProvMstpPortMstPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 44, 5, 1, 6),
    _ProvMstpPortMstPathCost_Type()
)
provMstpPortMstPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMstpPortMstPathCost.setStatus("current")
_MaintenanceGroup_ObjectIdentity = ObjectIdentity
maintenanceGroup = _MaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6)
)
_MaintMstpGroup_ObjectIdentity = ObjectIdentity
maintMstpGroup = _MaintMstpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 44)
)
_MaintMstpBridgeTable_Object = MibTable
maintMstpBridgeTable = _MaintMstpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 44, 1)
)
if mibBuilder.loadTexts:
    maintMstpBridgeTable.setStatus("current")
_MaintMstpBridgeEntry_Object = MibTableRow
maintMstpBridgeEntry = _MaintMstpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 44, 1, 1)
)
maintMstpBridgeEntry.setIndexNames(
    (0, "IPE-MSTP-MIB", "maintMstpBridgeIndex"),
)
if mibBuilder.loadTexts:
    maintMstpBridgeEntry.setStatus("current")


class _MaintMstpBridgeIndex_Type(Integer32):
    """Custom type maintMstpBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MaintMstpBridgeIndex_Type.__name__ = "Integer32"
_MaintMstpBridgeIndex_Object = MibTableColumn
maintMstpBridgeIndex = _MaintMstpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 44, 1, 1, 1),
    _MaintMstpBridgeIndex_Type()
)
maintMstpBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintMstpBridgeIndex.setStatus("current")
_MaintMstpBridgeNEAddress_Type = IpAddress
_MaintMstpBridgeNEAddress_Object = MibTableColumn
maintMstpBridgeNEAddress = _MaintMstpBridgeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 44, 1, 1, 2),
    _MaintMstpBridgeNEAddress_Type()
)
maintMstpBridgeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintMstpBridgeNEAddress.setStatus("current")


class _MaintMstpBridgeModeClear_Type(Integer32):
    """Custom type maintMstpBridgeModeClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_MaintMstpBridgeModeClear_Type.__name__ = "Integer32"
_MaintMstpBridgeModeClear_Object = MibTableColumn
maintMstpBridgeModeClear = _MaintMstpBridgeModeClear_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 44, 1, 1, 3),
    _MaintMstpBridgeModeClear_Type()
)
maintMstpBridgeModeClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintMstpBridgeModeClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-MSTP-MIB",
    **{"EnableDisableValue": EnableDisableValue,
       "IpeBridgePriority": IpeBridgePriority,
       "IpePortPathCost": IpePortPathCost,
       "IpePortPriority": IpePortPriority,
       "IpePortRole": IpePortRole,
       "IpePortState": IpePortState,
       "IpeVlanList": IpeVlanList,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asMstpGroup": asMstpGroup,
       "asMstpBridgeCistTable": asMstpBridgeCistTable,
       "asMstpBridgeCistEntry": asMstpBridgeCistEntry,
       "asMstpBridgeCistIndex": asMstpBridgeCistIndex,
       "asMstpBridgeCistNEAddress": asMstpBridgeCistNEAddress,
       "asMstpBridgeCistRegionalRoot": asMstpBridgeCistRegionalRoot,
       "asMstpBridgeCistTopChanges": asMstpBridgeCistTopChanges,
       "asMstpBridgeCistRoot": asMstpBridgeCistRoot,
       "asMstpBridgeMstTable": asMstpBridgeMstTable,
       "asMstpBridgeMstEntry": asMstpBridgeMstEntry,
       "asMstpBridgeMstIndex": asMstpBridgeMstIndex,
       "asMstpBridgeMstNEAddress": asMstpBridgeMstNEAddress,
       "asMstpBridgeMstRegionalRoot": asMstpBridgeMstRegionalRoot,
       "asMstpBridgeMstTopChanges": asMstpBridgeMstTopChanges,
       "asMstpPortCistTable": asMstpPortCistTable,
       "asMstpPortCistEntry": asMstpPortCistEntry,
       "asMstpPortCistIfIndex": asMstpPortCistIfIndex,
       "asMstpPortCistNEAddress": asMstpPortCistNEAddress,
       "asMstpPortCistRole": asMstpPortCistRole,
       "asMstpPortCistState": asMstpPortCistState,
       "asMstpPortCistRegionalRoot": asMstpPortCistRegionalRoot,
       "asMstpPortCistProtoVersion": asMstpPortCistProtoVersion,
       "asMstpPortCistPathCost": asMstpPortCistPathCost,
       "asMstpPortCistInvalidBpdu": asMstpPortCistInvalidBpdu,
       "asMstpPortCistDesignatedPathCost": asMstpPortCistDesignatedPathCost,
       "asMstpPortCistDesignatedBridge": asMstpPortCistDesignatedBridge,
       "asMstpPortCistDesignatedPort": asMstpPortCistDesignatedPort,
       "asMstpPortCistForwardTransitions": asMstpPortCistForwardTransitions,
       "asMstpPortCistOperEdgePort": asMstpPortCistOperEdgePort,
       "asMstpPortMstTable": asMstpPortMstTable,
       "asMstpPortMstEntry": asMstpPortMstEntry,
       "asMstpPortMstIfIndex": asMstpPortMstIfIndex,
       "asMstpPortMstIndex": asMstpPortMstIndex,
       "asMstpPortMstNEAddress": asMstpPortMstNEAddress,
       "asMstpPortMstRole": asMstpPortMstRole,
       "asMstpPortMstState": asMstpPortMstState,
       "asMstpPortMstRegionalRoot": asMstpPortMstRegionalRoot,
       "asMstpPortMstPathCost": asMstpPortMstPathCost,
       "asMstpPortMstDesignatedPathCost": asMstpPortMstDesignatedPathCost,
       "asMstpPortMstDesignatedBridge": asMstpPortMstDesignatedBridge,
       "asMstpPortMstDesignatedPort": asMstpPortMstDesignatedPort,
       "provisioningGroup": provisioningGroup,
       "provMstpGroup": provMstpGroup,
       "provMstpBridgeTable": provMstpBridgeTable,
       "provMstpBridgeEntry": provMstpBridgeEntry,
       "provMstpBridgeIndex": provMstpBridgeIndex,
       "provMstpBridgeNEAddress": provMstpBridgeNEAddress,
       "provMstpBridgeEnable": provMstpBridgeEnable,
       "provMstpBridgeMaxAge": provMstpBridgeMaxAge,
       "provMstpBridgeHelloTime": provMstpBridgeHelloTime,
       "provMstpBridgeForwardDelay": provMstpBridgeForwardDelay,
       "provMstpBridgeTxHoldCount": provMstpBridgeTxHoldCount,
       "provMstpBridgeMaxHopCount": provMstpBridgeMaxHopCount,
       "provMstpBridgeRegionName": provMstpBridgeRegionName,
       "provMstpBridgeRevisionNum": provMstpBridgeRevisionNum,
       "provMstpBridgeBpduFilter": provMstpBridgeBpduFilter,
       "provMstpBridgeBpduGuardTimer": provMstpBridgeBpduGuardTimer,
       "provMstpBridgeCistTable": provMstpBridgeCistTable,
       "provMstpBridgeCistEntry": provMstpBridgeCistEntry,
       "provMstpBridgeCistIndex": provMstpBridgeCistIndex,
       "provMstpBridgeCistNEAddress": provMstpBridgeCistNEAddress,
       "provMstpBridgeCistPriority": provMstpBridgeCistPriority,
       "provMstpBridgeCistVlanList": provMstpBridgeCistVlanList,
       "provMstpBridgeMstTable": provMstpBridgeMstTable,
       "provMstpBridgeMstEntry": provMstpBridgeMstEntry,
       "provMstpBridgeMstIndex": provMstpBridgeMstIndex,
       "provMstpBridgeMstNEAddress": provMstpBridgeMstNEAddress,
       "provMstpBridgeMstPriority": provMstpBridgeMstPriority,
       "provMstpBridgeMstVlanList": provMstpBridgeMstVlanList,
       "provMstpBridgeMstInstanceNum": provMstpBridgeMstInstanceNum,
       "provMstpBridgeMstRowStatus": provMstpBridgeMstRowStatus,
       "provMstpPortCistTable": provMstpPortCistTable,
       "provMstpPortCistEntry": provMstpPortCistEntry,
       "provMstpPortCistIfIndex": provMstpPortCistIfIndex,
       "provMstpPortCistNEAddress": provMstpPortCistNEAddress,
       "provMstpPortCistPriority": provMstpPortCistPriority,
       "provMstpPortCistEnable": provMstpPortCistEnable,
       "provMstpPortCistEdgePort": provMstpPortCistEdgePort,
       "provMstpPortCistPathCost": provMstpPortCistPathCost,
       "provMstpPortCistBpduGuard": provMstpPortCistBpduGuard,
       "provMstpPortCistRestrictRole": provMstpPortCistRestrictRole,
       "provMstpPortMstTable": provMstpPortMstTable,
       "provMstpPortMstEntry": provMstpPortMstEntry,
       "provMstpPortMstIfIndex": provMstpPortMstIfIndex,
       "provMstpPortMstIndex": provMstpPortMstIndex,
       "provMstpPortMstNEAddress": provMstpPortMstNEAddress,
       "provMstpPortMstPriority": provMstpPortMstPriority,
       "provMstpPortMstEnable": provMstpPortMstEnable,
       "provMstpPortMstPathCost": provMstpPortMstPathCost,
       "maintenanceGroup": maintenanceGroup,
       "maintMstpGroup": maintMstpGroup,
       "maintMstpBridgeTable": maintMstpBridgeTable,
       "maintMstpBridgeEntry": maintMstpBridgeEntry,
       "maintMstpBridgeIndex": maintMstpBridgeIndex,
       "maintMstpBridgeNEAddress": maintMstpBridgeNEAddress,
       "maintMstpBridgeModeClear": maintMstpBridgeModeClear}
)
