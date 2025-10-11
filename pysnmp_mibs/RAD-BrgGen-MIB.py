# SNMP MIB module (RAD-BrgGen-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-BrgGen-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:17 2025
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

(BridgeId,
 Timeout,
 dot1dBasePortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePortEntry")

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBaseEntry,
 ieee8021BridgeBasePortEntry) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBaseEntry",
    "ieee8021BridgeBasePortEntry")

(ieee8021MstpDesignatedRoot,
 ieee8021MstpEntry,
 ieee8021MstpTopologyChanges) = mibBuilder.importSymbols(
    "IEEE8021-MSTP-MIB",
    "ieee8021MstpDesignatedRoot",
    "ieee8021MstpEntry",
    "ieee8021MstpTopologyChanges")

(ieee8021QBridgeVlanStaticEntry,) = mibBuilder.importSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    "ieee8021QBridgeVlanStaticEntry")

(IEEE8021BridgePortNumber,
 IEEE8021PbbComponentIdentifier,
 IEEE8021VlanIndex) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021VlanIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,
 VlanId,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "dot1qVlanStaticEntry")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(radBridges,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radBridges")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

genBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1)
)


# Types definitions



class GenAddress(OctetString):
    """Custom type GenAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12




# TEXTUAL-CONVENTIONS



class TagHandlingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("stacking", 3),
          ("stripping", 4))
    )



class BridgeTopology(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("eLAN", 3),
          ("eTree", 4))
    )



# MIB Managed Objects in the order of their OIDs

_GenBridgeEvents_ObjectIdentity = ObjectIdentity
genBridgeEvents = _GenBridgeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 0)
)


class _RadBridgeAction_Type(Integer32):
    """Custom type radBridgeAction based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("sendNetworkTab", 2),
          ("deleteNetworkTab", 3),
          ("sendRoutingTab", 4),
          ("deleteRoutinTab", 5),
          ("sendLanTab", 6),
          ("deleteLanTab", 7),
          ("deleteArpTab", 8),
          ("sendArpTab", 9),
          ("deleteRouteTab", 10),
          ("sendRouteTab", 11),
          ("deactivateAllMasks", 12),
          ("saveAllActiveMasks", 13),
          ("loadAndActivateAllMasksFromNVRAM", 14),
          ("clearAllMasksFromNVRAM", 15),
          ("defaultConfig", 16),
          ("resetNVRAM", 17),
          ("clearIPNVRAM", 18),
          ("noOp", 255))
    )


_RadBridgeAction_Type.__name__ = "Integer32"
_RadBridgeAction_Object = MibScalar
radBridgeAction = _RadBridgeAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 1),
    _RadBridgeAction_Type()
)
radBridgeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeAction.setStatus("current")
_RadBridgeInactiveArpTimeOut_Type = Integer32
_RadBridgeInactiveArpTimeOut_Object = MibScalar
radBridgeInactiveArpTimeOut = _RadBridgeInactiveArpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 2),
    _RadBridgeInactiveArpTimeOut_Type()
)
radBridgeInactiveArpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeInactiveArpTimeOut.setStatus("current")
_RadBridgeMaskTable_Object = MibTable
radBridgeMaskTable = _RadBridgeMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3)
)
if mibBuilder.loadTexts:
    radBridgeMaskTable.setStatus("current")
_RadBridgeMaskEntry_Object = MibTableRow
radBridgeMaskEntry = _RadBridgeMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1)
)
radBridgeMaskEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeMaskType"),
    (0, "RAD-BrgGen-MIB", "radBridgeMaskIfIndex"),
    (0, "RAD-BrgGen-MIB", "radBridgeMaskNum"),
)
if mibBuilder.loadTexts:
    radBridgeMaskEntry.setStatus("current")


class _RadBridgeMaskType_Type(Integer32):
    """Custom type radBridgeMaskType based on Integer32"""
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
        *(("tx", 1),
          ("rx", 2),
          ("compress", 3),
          ("priority", 4),
          ("loadSharing", 5),
          ("facs", 6),
          ("codConnect", 7),
          ("codDisconnect", 8))
    )


_RadBridgeMaskType_Type.__name__ = "Integer32"
_RadBridgeMaskType_Object = MibTableColumn
radBridgeMaskType = _RadBridgeMaskType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 1),
    _RadBridgeMaskType_Type()
)
radBridgeMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeMaskType.setStatus("current")
_RadBridgeMaskIfIndex_Type = Integer32
_RadBridgeMaskIfIndex_Object = MibTableColumn
radBridgeMaskIfIndex = _RadBridgeMaskIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 2),
    _RadBridgeMaskIfIndex_Type()
)
radBridgeMaskIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeMaskIfIndex.setStatus("current")
_RadBridgeMaskNum_Type = Integer32
_RadBridgeMaskNum_Object = MibTableColumn
radBridgeMaskNum = _RadBridgeMaskNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 3),
    _RadBridgeMaskNum_Type()
)
radBridgeMaskNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeMaskNum.setStatus("current")


class _RadBridgeMaskDest_Type(Integer32):
    """Custom type radBridgeMaskDest based on Integer32"""
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
        *(("unassigned-cond", 1),
          ("broadcast-msge", 2),
          ("multicast-msge", 3),
          ("all-msge", 4),
          ("none", 5))
    )


_RadBridgeMaskDest_Type.__name__ = "Integer32"
_RadBridgeMaskDest_Object = MibTableColumn
radBridgeMaskDest = _RadBridgeMaskDest_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 4),
    _RadBridgeMaskDest_Type()
)
radBridgeMaskDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskDest.setStatus("current")
_RadBridgeMaskPat1_Type = OctetString
_RadBridgeMaskPat1_Object = MibTableColumn
radBridgeMaskPat1 = _RadBridgeMaskPat1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 5),
    _RadBridgeMaskPat1_Type()
)
radBridgeMaskPat1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskPat1.setStatus("current")
_RadBridgeMaskActiveBit1_Type = OctetString
_RadBridgeMaskActiveBit1_Object = MibTableColumn
radBridgeMaskActiveBit1 = _RadBridgeMaskActiveBit1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 6),
    _RadBridgeMaskActiveBit1_Type()
)
radBridgeMaskActiveBit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskActiveBit1.setStatus("current")


class _RadBridgeMaskFrom1_Type(Integer32):
    """Custom type radBridgeMaskFrom1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("llc", 2),
          ("net", 3))
    )


_RadBridgeMaskFrom1_Type.__name__ = "Integer32"
_RadBridgeMaskFrom1_Object = MibTableColumn
radBridgeMaskFrom1 = _RadBridgeMaskFrom1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 7),
    _RadBridgeMaskFrom1_Type()
)
radBridgeMaskFrom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskFrom1.setStatus("current")
_RadBridgeMaskOffset1_Type = Integer32
_RadBridgeMaskOffset1_Object = MibTableColumn
radBridgeMaskOffset1 = _RadBridgeMaskOffset1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 8),
    _RadBridgeMaskOffset1_Type()
)
radBridgeMaskOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOffset1.setStatus("current")


class _RadBridgeMaskCond1_Type(Integer32):
    """Custom type radBridgeMaskCond1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RadBridgeMaskCond1_Type.__name__ = "Integer32"
_RadBridgeMaskCond1_Object = MibTableColumn
radBridgeMaskCond1 = _RadBridgeMaskCond1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 9),
    _RadBridgeMaskCond1_Type()
)
radBridgeMaskCond1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskCond1.setStatus("current")
_RadBridgeMaskPat2_Type = OctetString
_RadBridgeMaskPat2_Object = MibTableColumn
radBridgeMaskPat2 = _RadBridgeMaskPat2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 10),
    _RadBridgeMaskPat2_Type()
)
radBridgeMaskPat2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskPat2.setStatus("current")
_RadBridgeMaskActiveBit2_Type = OctetString
_RadBridgeMaskActiveBit2_Object = MibTableColumn
radBridgeMaskActiveBit2 = _RadBridgeMaskActiveBit2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 11),
    _RadBridgeMaskActiveBit2_Type()
)
radBridgeMaskActiveBit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskActiveBit2.setStatus("current")


class _RadBridgeMaskFrom2_Type(Integer32):
    """Custom type radBridgeMaskFrom2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("llc", 2),
          ("net", 3))
    )


_RadBridgeMaskFrom2_Type.__name__ = "Integer32"
_RadBridgeMaskFrom2_Object = MibTableColumn
radBridgeMaskFrom2 = _RadBridgeMaskFrom2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 12),
    _RadBridgeMaskFrom2_Type()
)
radBridgeMaskFrom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskFrom2.setStatus("current")
_RadBridgeMaskOffset2_Type = Integer32
_RadBridgeMaskOffset2_Object = MibTableColumn
radBridgeMaskOffset2 = _RadBridgeMaskOffset2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 13),
    _RadBridgeMaskOffset2_Type()
)
radBridgeMaskOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOffset2.setStatus("current")


class _RadBridgeMaskCond2_Type(Integer32):
    """Custom type radBridgeMaskCond2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RadBridgeMaskCond2_Type.__name__ = "Integer32"
_RadBridgeMaskCond2_Object = MibTableColumn
radBridgeMaskCond2 = _RadBridgeMaskCond2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 14),
    _RadBridgeMaskCond2_Type()
)
radBridgeMaskCond2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskCond2.setStatus("current")
_RadBridgeMaskPat3_Type = OctetString
_RadBridgeMaskPat3_Object = MibTableColumn
radBridgeMaskPat3 = _RadBridgeMaskPat3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 15),
    _RadBridgeMaskPat3_Type()
)
radBridgeMaskPat3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskPat3.setStatus("current")
_RadBridgeMaskActiveBit3_Type = OctetString
_RadBridgeMaskActiveBit3_Object = MibTableColumn
radBridgeMaskActiveBit3 = _RadBridgeMaskActiveBit3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 16),
    _RadBridgeMaskActiveBit3_Type()
)
radBridgeMaskActiveBit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskActiveBit3.setStatus("current")


class _RadBridgeMaskFrom3_Type(Integer32):
    """Custom type radBridgeMaskFrom3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("llc", 2),
          ("net", 3))
    )


_RadBridgeMaskFrom3_Type.__name__ = "Integer32"
_RadBridgeMaskFrom3_Object = MibTableColumn
radBridgeMaskFrom3 = _RadBridgeMaskFrom3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 17),
    _RadBridgeMaskFrom3_Type()
)
radBridgeMaskFrom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskFrom3.setStatus("current")
_RadBridgeMaskOffset3_Type = Integer32
_RadBridgeMaskOffset3_Object = MibTableColumn
radBridgeMaskOffset3 = _RadBridgeMaskOffset3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 18),
    _RadBridgeMaskOffset3_Type()
)
radBridgeMaskOffset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOffset3.setStatus("current")


class _RadBridgeMaskCond3_Type(Integer32):
    """Custom type radBridgeMaskCond3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RadBridgeMaskCond3_Type.__name__ = "Integer32"
_RadBridgeMaskCond3_Object = MibTableColumn
radBridgeMaskCond3 = _RadBridgeMaskCond3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 19),
    _RadBridgeMaskCond3_Type()
)
radBridgeMaskCond3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskCond3.setStatus("current")


class _RadBridgeMaskOper_Type(Integer32):
    """Custom type radBridgeMaskOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("route", 3),
          ("forward-route", 4),
          ("high-priority", 5),
          ("noOp", 6),
          ("delete", 7))
    )


_RadBridgeMaskOper_Type.__name__ = "Integer32"
_RadBridgeMaskOper_Object = MibTableColumn
radBridgeMaskOper = _RadBridgeMaskOper_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 20),
    _RadBridgeMaskOper_Type()
)
radBridgeMaskOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOper.setStatus("current")
_RadBridgeCOD_ObjectIdentity = ObjectIdentity
radBridgeCOD = _RadBridgeCOD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4)
)
_RadBridgeCODParamTable_Object = MibTable
radBridgeCODParamTable = _RadBridgeCODParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    radBridgeCODParamTable.setStatus("current")
_RadBridgeCODEntry_Object = MibTableRow
radBridgeCODEntry = _RadBridgeCODEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1)
)
radBridgeCODEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeCODIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeCODEntry.setStatus("current")
_RadBridgeCODIfIndex_Type = Integer32
_RadBridgeCODIfIndex_Object = MibTableColumn
radBridgeCODIfIndex = _RadBridgeCODIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 1),
    _RadBridgeCODIfIndex_Type()
)
radBridgeCODIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODIfIndex.setStatus("current")


class _RadBridgeCODManualConnect_Type(Integer32):
    """Custom type radBridgeCODManualConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2))
    )


_RadBridgeCODManualConnect_Type.__name__ = "Integer32"
_RadBridgeCODManualConnect_Object = MibTableColumn
radBridgeCODManualConnect = _RadBridgeCODManualConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 2),
    _RadBridgeCODManualConnect_Type()
)
radBridgeCODManualConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODManualConnect.setStatus("current")


class _RadBridgeCODMode_Type(Integer32):
    """Custom type radBridgeCODMode based on Integer32"""
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
        *(("answer", 1),
          ("originate", 2),
          ("disable", 3),
          ("answerAndOriginate", 4))
    )


_RadBridgeCODMode_Type.__name__ = "Integer32"
_RadBridgeCODMode_Object = MibTableColumn
radBridgeCODMode = _RadBridgeCODMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 3),
    _RadBridgeCODMode_Type()
)
radBridgeCODMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODMode.setStatus("current")
_RadBridgeCODConnectDelay_Type = Integer32
_RadBridgeCODConnectDelay_Object = MibTableColumn
radBridgeCODConnectDelay = _RadBridgeCODConnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 4),
    _RadBridgeCODConnectDelay_Type()
)
radBridgeCODConnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODConnectDelay.setStatus("current")
_RadBridgeCODisConnectDelay_Type = Integer32
_RadBridgeCODisConnectDelay_Object = MibTableColumn
radBridgeCODisConnectDelay = _RadBridgeCODisConnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 5),
    _RadBridgeCODisConnectDelay_Type()
)
radBridgeCODisConnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODisConnectDelay.setStatus("current")


class _RadBridgeCODImplicitSwitch_Type(Integer32):
    """Custom type radBridgeCODImplicitSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RadBridgeCODImplicitSwitch_Type.__name__ = "Integer32"
_RadBridgeCODImplicitSwitch_Object = MibTableColumn
radBridgeCODImplicitSwitch = _RadBridgeCODImplicitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 6),
    _RadBridgeCODImplicitSwitch_Type()
)
radBridgeCODImplicitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODImplicitSwitch.setStatus("current")
_RadBridgeCODNumAccess_Type = Counter32
_RadBridgeCODNumAccess_Object = MibTableColumn
radBridgeCODNumAccess = _RadBridgeCODNumAccess_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 7),
    _RadBridgeCODNumAccess_Type()
)
radBridgeCODNumAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODNumAccess.setStatus("current")
_RadBridgeCODTotalConnecTime_Type = Integer32
_RadBridgeCODTotalConnecTime_Object = MibTableColumn
radBridgeCODTotalConnecTime = _RadBridgeCODTotalConnecTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 8),
    _RadBridgeCODTotalConnecTime_Type()
)
radBridgeCODTotalConnecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODTotalConnecTime.setStatus("current")
_RadBridgeCODTimeTriggerTable_Object = MibTable
radBridgeCODTimeTriggerTable = _RadBridgeCODTimeTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerTable.setStatus("current")
_RadBridgeCODTimeTriggerEntry_Object = MibTableRow
radBridgeCODTimeTriggerEntry = _RadBridgeCODTimeTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1)
)
radBridgeCODTimeTriggerEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeCODTimeIfIndex"),
    (0, "RAD-BrgGen-MIB", "radBridgeCODDay"),
    (0, "RAD-BrgGen-MIB", "radBridgeCODTimeTriggerNum"),
)
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerEntry.setStatus("current")
_RadBridgeCODTimeIfIndex_Type = Integer32
_RadBridgeCODTimeIfIndex_Object = MibTableColumn
radBridgeCODTimeIfIndex = _RadBridgeCODTimeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 1),
    _RadBridgeCODTimeIfIndex_Type()
)
radBridgeCODTimeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODTimeIfIndex.setStatus("current")


class _RadBridgeCODDay_Type(Integer32):
    """Custom type radBridgeCODDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6),
          ("sun", 7))
    )


_RadBridgeCODDay_Type.__name__ = "Integer32"
_RadBridgeCODDay_Object = MibTableColumn
radBridgeCODDay = _RadBridgeCODDay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 2),
    _RadBridgeCODDay_Type()
)
radBridgeCODDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODDay.setStatus("current")


class _RadBridgeCODTimeTriggerNum_Type(Integer32):
    """Custom type radBridgeCODTimeTriggerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadBridgeCODTimeTriggerNum_Type.__name__ = "Integer32"
_RadBridgeCODTimeTriggerNum_Object = MibTableColumn
radBridgeCODTimeTriggerNum = _RadBridgeCODTimeTriggerNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 3),
    _RadBridgeCODTimeTriggerNum_Type()
)
radBridgeCODTimeTriggerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerNum.setStatus("current")
_RadBridgeCODTimeTriggerFrom_Type = DisplayString
_RadBridgeCODTimeTriggerFrom_Object = MibTableColumn
radBridgeCODTimeTriggerFrom = _RadBridgeCODTimeTriggerFrom_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 4),
    _RadBridgeCODTimeTriggerFrom_Type()
)
radBridgeCODTimeTriggerFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerFrom.setStatus("current")
_RadBridgeCODTimeTriggerTo_Type = DisplayString
_RadBridgeCODTimeTriggerTo_Object = MibTableColumn
radBridgeCODTimeTriggerTo = _RadBridgeCODTimeTriggerTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 5),
    _RadBridgeCODTimeTriggerTo_Type()
)
radBridgeCODTimeTriggerTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerTo.setStatus("current")


class _RadBridgeCODTimeTriggerStatus_Type(Integer32):
    """Custom type radBridgeCODTimeTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RadBridgeCODTimeTriggerStatus_Type.__name__ = "Integer32"
_RadBridgeCODTimeTriggerStatus_Object = MibTableColumn
radBridgeCODTimeTriggerStatus = _RadBridgeCODTimeTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 6),
    _RadBridgeCODTimeTriggerStatus_Type()
)
radBridgeCODTimeTriggerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerStatus.setStatus("current")
_RadBridgeCODTraffic_ObjectIdentity = ObjectIdentity
radBridgeCODTraffic = _RadBridgeCODTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3)
)
_RadBridgeCODTrafficTable_Object = MibTable
radBridgeCODTrafficTable = _RadBridgeCODTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    radBridgeCODTrafficTable.setStatus("current")
_RadBridgeCODTrafficEntry_Object = MibTableRow
radBridgeCODTrafficEntry = _RadBridgeCODTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1, 1)
)
radBridgeCODTrafficEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeCODProtocolType"),
)
if mibBuilder.loadTexts:
    radBridgeCODTrafficEntry.setStatus("current")


class _RadBridgeCODProtocolType_Type(Integer32):
    """Custom type radBridgeCODProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2),
          ("other", 3))
    )


_RadBridgeCODProtocolType_Type.__name__ = "Integer32"
_RadBridgeCODProtocolType_Object = MibTableColumn
radBridgeCODProtocolType = _RadBridgeCODProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1, 1, 1),
    _RadBridgeCODProtocolType_Type()
)
radBridgeCODProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODProtocolType.setStatus("current")


class _RadBridgeCODTrafficTriggerStatus_Type(Integer32):
    """Custom type radBridgeCODTrafficTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RadBridgeCODTrafficTriggerStatus_Type.__name__ = "Integer32"
_RadBridgeCODTrafficTriggerStatus_Object = MibTableColumn
radBridgeCODTrafficTriggerStatus = _RadBridgeCODTrafficTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1, 1, 2),
    _RadBridgeCODTrafficTriggerStatus_Type()
)
radBridgeCODTrafficTriggerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTrafficTriggerStatus.setStatus("current")
_RadBridgeCODRemoteIPAddr_Type = IpAddress
_RadBridgeCODRemoteIPAddr_Object = MibScalar
radBridgeCODRemoteIPAddr = _RadBridgeCODRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 2),
    _RadBridgeCODRemoteIPAddr_Type()
)
radBridgeCODRemoteIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODRemoteIPAddr.setStatus("current")
_RadBridgeCODIPMask_Type = IpAddress
_RadBridgeCODIPMask_Object = MibScalar
radBridgeCODIPMask = _RadBridgeCODIPMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 3),
    _RadBridgeCODIPMask_Type()
)
radBridgeCODIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODIPMask.setStatus("current")
_RadBridgeCODTrafficTriggerProtType_Type = OctetString
_RadBridgeCODTrafficTriggerProtType_Object = MibScalar
radBridgeCODTrafficTriggerProtType = _RadBridgeCODTrafficTriggerProtType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 4),
    _RadBridgeCODTrafficTriggerProtType_Type()
)
radBridgeCODTrafficTriggerProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTrafficTriggerProtType.setStatus("current")
_RadBridgeCODCondTable_Object = MibTable
radBridgeCODCondTable = _RadBridgeCODCondTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    radBridgeCODCondTable.setStatus("current")
_RadBridgeCODCondEntry_Object = MibTableRow
radBridgeCODCondEntry = _RadBridgeCODCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1)
)
radBridgeCODCondEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeCODCondIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeCODCondEntry.setStatus("current")
_RadBridgeCODCondIfIndex_Type = Integer32
_RadBridgeCODCondIfIndex_Object = MibTableColumn
radBridgeCODCondIfIndex = _RadBridgeCODCondIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 1),
    _RadBridgeCODCondIfIndex_Type()
)
radBridgeCODCondIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODCondIfIndex.setStatus("current")


class _RadBridgeCODOriginateConnectCondition_Type(Integer32):
    """Custom type radBridgeCODOriginateConnectCondition based on Integer32"""
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
        *(("onPowerOn", 1),
          ("whenAnyStationOnLan", 2),
          ("onTraffic", 3),
          ("onManualConnect", 4))
    )


_RadBridgeCODOriginateConnectCondition_Type.__name__ = "Integer32"
_RadBridgeCODOriginateConnectCondition_Object = MibTableColumn
radBridgeCODOriginateConnectCondition = _RadBridgeCODOriginateConnectCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 2),
    _RadBridgeCODOriginateConnectCondition_Type()
)
radBridgeCODOriginateConnectCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODOriginateConnectCondition.setStatus("current")


class _RadBridgeCODOriginateDisConnectCondition_Type(Integer32):
    """Custom type radBridgeCODOriginateDisConnectCondition based on Integer32"""
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
        *(("noStationOnLan", 1),
          ("onTraffic", 2),
          ("onDelayFromConnectionOnRequest", 3),
          ("onManualDisConnect", 4))
    )


_RadBridgeCODOriginateDisConnectCondition_Type.__name__ = "Integer32"
_RadBridgeCODOriginateDisConnectCondition_Object = MibTableColumn
radBridgeCODOriginateDisConnectCondition = _RadBridgeCODOriginateDisConnectCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 3),
    _RadBridgeCODOriginateDisConnectCondition_Type()
)
radBridgeCODOriginateDisConnectCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODOriginateDisConnectCondition.setStatus("current")
_RadBridgeCODOriginateDisConnectDelay_Type = Integer32
_RadBridgeCODOriginateDisConnectDelay_Object = MibTableColumn
radBridgeCODOriginateDisConnectDelay = _RadBridgeCODOriginateDisConnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 4),
    _RadBridgeCODOriginateDisConnectDelay_Type()
)
radBridgeCODOriginateDisConnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODOriginateDisConnectDelay.setStatus("current")


class _RadBridgeCODAnswerConnectCondition_Type(Integer32):
    """Custom type radBridgeCODAnswerConnectCondition based on Integer32"""
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
        *(("onPowerOn", 1),
          ("whenAnyStationOnLan", 2),
          ("onTraffic", 3),
          ("onManualConnect", 4))
    )


_RadBridgeCODAnswerConnectCondition_Type.__name__ = "Integer32"
_RadBridgeCODAnswerConnectCondition_Object = MibTableColumn
radBridgeCODAnswerConnectCondition = _RadBridgeCODAnswerConnectCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 5),
    _RadBridgeCODAnswerConnectCondition_Type()
)
radBridgeCODAnswerConnectCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODAnswerConnectCondition.setStatus("current")
_RadBridgeCODSpecificOnTrafficOIDCondition_Type = ObjectIdentifier
_RadBridgeCODSpecificOnTrafficOIDCondition_Object = MibTableColumn
radBridgeCODSpecificOnTrafficOIDCondition = _RadBridgeCODSpecificOnTrafficOIDCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 6),
    _RadBridgeCODSpecificOnTrafficOIDCondition_Type()
)
radBridgeCODSpecificOnTrafficOIDCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODSpecificOnTrafficOIDCondition.setStatus("current")
_RadBridgeCODDisConnectMinimunFramesNumber_Type = Integer32
_RadBridgeCODDisConnectMinimunFramesNumber_Object = MibTableColumn
radBridgeCODDisConnectMinimunFramesNumber = _RadBridgeCODDisConnectMinimunFramesNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 7),
    _RadBridgeCODDisConnectMinimunFramesNumber_Type()
)
radBridgeCODDisConnectMinimunFramesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODDisConnectMinimunFramesNumber.setStatus("current")
_RadBridgeIPX_ObjectIdentity = ObjectIdentity
radBridgeIPX = _RadBridgeIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5)
)
_RadBridgeIPXdriver_ObjectIdentity = ObjectIdentity
radBridgeIPXdriver = _RadBridgeIPXdriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 1)
)


class _RadBridgeIPXForwarding_Type(Integer32):
    """Custom type radBridgeIPXForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_RadBridgeIPXForwarding_Type.__name__ = "Integer32"
_RadBridgeIPXForwarding_Object = MibScalar
radBridgeIPXForwarding = _RadBridgeIPXForwarding_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 1, 1),
    _RadBridgeIPXForwarding_Type()
)
radBridgeIPXForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXForwarding.setStatus("current")
_RadBridgeIPXRip_ObjectIdentity = ObjectIdentity
radBridgeIPXRip = _RadBridgeIPXRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2)
)
_RadBridgeIPXRipOutPackets_Type = Counter32
_RadBridgeIPXRipOutPackets_Object = MibScalar
radBridgeIPXRipOutPackets = _RadBridgeIPXRipOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 1),
    _RadBridgeIPXRipOutPackets_Type()
)
radBridgeIPXRipOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipOutPackets.setStatus("current")
_RadBridgeIPXRipInPackets_Type = Counter32
_RadBridgeIPXRipInPackets_Object = MibScalar
radBridgeIPXRipInPackets = _RadBridgeIPXRipInPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 2),
    _RadBridgeIPXRipInPackets_Type()
)
radBridgeIPXRipInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipInPackets.setStatus("current")
_RadBridgeIPXRipInDiscards_Type = Counter32
_RadBridgeIPXRipInDiscards_Object = MibScalar
radBridgeIPXRipInDiscards = _RadBridgeIPXRipInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 3),
    _RadBridgeIPXRipInDiscards_Type()
)
radBridgeIPXRipInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipInDiscards.setStatus("current")
_RadBridgeIPXRipTblNoOfEntries_Type = Integer32
_RadBridgeIPXRipTblNoOfEntries_Object = MibScalar
radBridgeIPXRipTblNoOfEntries = _RadBridgeIPXRipTblNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 4),
    _RadBridgeIPXRipTblNoOfEntries_Type()
)
radBridgeIPXRipTblNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipTblNoOfEntries.setStatus("current")
_RadBridgeIPXRipTblBcastTrigUpdateInterval_Type = Integer32
_RadBridgeIPXRipTblBcastTrigUpdateInterval_Object = MibScalar
radBridgeIPXRipTblBcastTrigUpdateInterval = _RadBridgeIPXRipTblBcastTrigUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 5),
    _RadBridgeIPXRipTblBcastTrigUpdateInterval_Type()
)
radBridgeIPXRipTblBcastTrigUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipTblBcastTrigUpdateInterval.setStatus("current")
_RadBridgeIPXRipTable_Object = MibTable
radBridgeIPXRipTable = _RadBridgeIPXRipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    radBridgeIPXRipTable.setStatus("current")
_RadBridgeIPXRipTableEntry_Object = MibTableRow
radBridgeIPXRipTableEntry = _RadBridgeIPXRipTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1)
)
radBridgeIPXRipTableEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeIPXRipDestNetwork"),
    (0, "RAD-BrgGen-MIB", "radBridgeIPXRipPolicy"),
)
if mibBuilder.loadTexts:
    radBridgeIPXRipTableEntry.setStatus("current")


class _RadBridgeIPXRipDestNetwork_Type(OctetString):
    """Custom type radBridgeIPXRipDestNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RadBridgeIPXRipDestNetwork_Type.__name__ = "OctetString"
_RadBridgeIPXRipDestNetwork_Object = MibTableColumn
radBridgeIPXRipDestNetwork = _RadBridgeIPXRipDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 1),
    _RadBridgeIPXRipDestNetwork_Type()
)
radBridgeIPXRipDestNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipDestNetwork.setStatus("current")


class _RadBridgeIPXRipPolicy_Type(Integer32):
    """Custom type radBridgeIPXRipPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("alternate", 2))
    )


_RadBridgeIPXRipPolicy_Type.__name__ = "Integer32"
_RadBridgeIPXRipPolicy_Object = MibTableColumn
radBridgeIPXRipPolicy = _RadBridgeIPXRipPolicy_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 2),
    _RadBridgeIPXRipPolicy_Type()
)
radBridgeIPXRipPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipPolicy.setStatus("current")


class _RadBridgeIPXRipForwardingRouter_Type(OctetString):
    """Custom type radBridgeIPXRipForwardingRouter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RadBridgeIPXRipForwardingRouter_Type.__name__ = "OctetString"
_RadBridgeIPXRipForwardingRouter_Object = MibTableColumn
radBridgeIPXRipForwardingRouter = _RadBridgeIPXRipForwardingRouter_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 3),
    _RadBridgeIPXRipForwardingRouter_Type()
)
radBridgeIPXRipForwardingRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipForwardingRouter.setStatus("current")
_RadBridgeIPXRipNIC_Type = Integer32
_RadBridgeIPXRipNIC_Object = MibTableColumn
radBridgeIPXRipNIC = _RadBridgeIPXRipNIC_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 4),
    _RadBridgeIPXRipNIC_Type()
)
radBridgeIPXRipNIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipNIC.setStatus("current")
_RadBridgeIPXRipTickMetric_Type = Integer32
_RadBridgeIPXRipTickMetric_Object = MibTableColumn
radBridgeIPXRipTickMetric = _RadBridgeIPXRipTickMetric_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 5),
    _RadBridgeIPXRipTickMetric_Type()
)
radBridgeIPXRipTickMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipTickMetric.setStatus("current")
_RadBridgeIPXRipHopMetric_Type = Integer32
_RadBridgeIPXRipHopMetric_Object = MibTableColumn
radBridgeIPXRipHopMetric = _RadBridgeIPXRipHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 6),
    _RadBridgeIPXRipHopMetric_Type()
)
radBridgeIPXRipHopMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipHopMetric.setStatus("current")
_RadBridgeIPXRipAgingTime_Type = TimeTicks
_RadBridgeIPXRipAgingTime_Object = MibTableColumn
radBridgeIPXRipAgingTime = _RadBridgeIPXRipAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 7),
    _RadBridgeIPXRipAgingTime_Type()
)
radBridgeIPXRipAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipAgingTime.setStatus("current")


class _RadBridgeIPXRipValueStatus_Type(Integer32):
    """Custom type radBridgeIPXRipValueStatus based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("invalid", 3),
          ("semiDynamic", 4))
    )


_RadBridgeIPXRipValueStatus_Type.__name__ = "Integer32"
_RadBridgeIPXRipValueStatus_Object = MibTableColumn
radBridgeIPXRipValueStatus = _RadBridgeIPXRipValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 8),
    _RadBridgeIPXRipValueStatus_Type()
)
radBridgeIPXRipValueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipValueStatus.setStatus("current")


class _RadBridgeIPXRipForwardType_Type(Integer32):
    """Custom type radBridgeIPXRipForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("remote", 3))
    )


_RadBridgeIPXRipForwardType_Type.__name__ = "Integer32"
_RadBridgeIPXRipForwardType_Object = MibTableColumn
radBridgeIPXRipForwardType = _RadBridgeIPXRipForwardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 9),
    _RadBridgeIPXRipForwardType_Type()
)
radBridgeIPXRipForwardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipForwardType.setStatus("current")
_RadBridgeIPXRipInfTable_Object = MibTable
radBridgeIPXRipInfTable = _RadBridgeIPXRipInfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    radBridgeIPXRipInfTable.setStatus("current")
_RadBridgeIPXRipInfEntry_Object = MibTableRow
radBridgeIPXRipInfEntry = _RadBridgeIPXRipInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1)
)
radBridgeIPXRipInfEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeIPXRipInfIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeIPXRipInfEntry.setStatus("current")
_RadBridgeIPXRipInfIfIndex_Type = Integer32
_RadBridgeIPXRipInfIfIndex_Object = MibTableColumn
radBridgeIPXRipInfIfIndex = _RadBridgeIPXRipInfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1, 1),
    _RadBridgeIPXRipInfIfIndex_Type()
)
radBridgeIPXRipInfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipInfIfIndex.setStatus("current")
_RadBridgeIPXRipInfBcastUpdate_Type = Integer32
_RadBridgeIPXRipInfBcastUpdate_Object = MibTableColumn
radBridgeIPXRipInfBcastUpdate = _RadBridgeIPXRipInfBcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1, 2),
    _RadBridgeIPXRipInfBcastUpdate_Type()
)
radBridgeIPXRipInfBcastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipInfBcastUpdate.setStatus("current")
_RadBridgeIPXRipInfAgeMultiplier_Type = Integer32
_RadBridgeIPXRipInfAgeMultiplier_Object = MibTableColumn
radBridgeIPXRipInfAgeMultiplier = _RadBridgeIPXRipInfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1, 3),
    _RadBridgeIPXRipInfAgeMultiplier_Type()
)
radBridgeIPXRipInfAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipInfAgeMultiplier.setStatus("current")
_RadBridgeIPXSap_ObjectIdentity = ObjectIdentity
radBridgeIPXSap = _RadBridgeIPXSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3)
)
_RadBridgeIPXSapOutPackets_Type = Counter32
_RadBridgeIPXSapOutPackets_Object = MibScalar
radBridgeIPXSapOutPackets = _RadBridgeIPXSapOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 1),
    _RadBridgeIPXSapOutPackets_Type()
)
radBridgeIPXSapOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapOutPackets.setStatus("current")
_RadBridgeIPXSapInPackets_Type = Counter32
_RadBridgeIPXSapInPackets_Object = MibScalar
radBridgeIPXSapInPackets = _RadBridgeIPXSapInPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 2),
    _RadBridgeIPXSapInPackets_Type()
)
radBridgeIPXSapInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapInPackets.setStatus("current")
_RadBridgeIPXSapInDiscards_Type = Counter32
_RadBridgeIPXSapInDiscards_Object = MibScalar
radBridgeIPXSapInDiscards = _RadBridgeIPXSapInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 3),
    _RadBridgeIPXSapInDiscards_Type()
)
radBridgeIPXSapInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapInDiscards.setStatus("current")
_RadBridgeIPXSapTblNoOfEntries_Type = Integer32
_RadBridgeIPXSapTblNoOfEntries_Object = MibScalar
radBridgeIPXSapTblNoOfEntries = _RadBridgeIPXSapTblNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 4),
    _RadBridgeIPXSapTblNoOfEntries_Type()
)
radBridgeIPXSapTblNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapTblNoOfEntries.setStatus("current")
_RadBridgeIPXSapTblBcastTrigUpdateInterval_Type = Integer32
_RadBridgeIPXSapTblBcastTrigUpdateInterval_Object = MibScalar
radBridgeIPXSapTblBcastTrigUpdateInterval = _RadBridgeIPXSapTblBcastTrigUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 5),
    _RadBridgeIPXSapTblBcastTrigUpdateInterval_Type()
)
radBridgeIPXSapTblBcastTrigUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapTblBcastTrigUpdateInterval.setStatus("current")
_RadBridgeIPXSapTable_Object = MibTable
radBridgeIPXSapTable = _RadBridgeIPXSapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    radBridgeIPXSapTable.setStatus("current")
_RadBridgeIPXSapTableEntry_Object = MibTableRow
radBridgeIPXSapTableEntry = _RadBridgeIPXSapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1)
)
radBridgeIPXSapTableEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeIPXSapServerType"),
    (0, "RAD-BrgGen-MIB", "radBridgeIPXSapName"),
)
if mibBuilder.loadTexts:
    radBridgeIPXSapTableEntry.setStatus("current")
_RadBridgeIPXSapServerType_Type = Integer32
_RadBridgeIPXSapServerType_Object = MibTableColumn
radBridgeIPXSapServerType = _RadBridgeIPXSapServerType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 1),
    _RadBridgeIPXSapServerType_Type()
)
radBridgeIPXSapServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapServerType.setStatus("current")


class _RadBridgeIPXSapName_Type(DisplayString):
    """Custom type radBridgeIPXSapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48


_RadBridgeIPXSapName_Type.__name__ = "DisplayString"
_RadBridgeIPXSapName_Object = MibTableColumn
radBridgeIPXSapName = _RadBridgeIPXSapName_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 2),
    _RadBridgeIPXSapName_Type()
)
radBridgeIPXSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapName.setStatus("current")


class _RadBridgeIPXSapNetwork_Type(OctetString):
    """Custom type radBridgeIPXSapNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RadBridgeIPXSapNetwork_Type.__name__ = "OctetString"
_RadBridgeIPXSapNetwork_Object = MibTableColumn
radBridgeIPXSapNetwork = _RadBridgeIPXSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 3),
    _RadBridgeIPXSapNetwork_Type()
)
radBridgeIPXSapNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapNetwork.setStatus("current")


class _RadBridgeIPXSapNode_Type(OctetString):
    """Custom type radBridgeIPXSapNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RadBridgeIPXSapNode_Type.__name__ = "OctetString"
_RadBridgeIPXSapNode_Object = MibTableColumn
radBridgeIPXSapNode = _RadBridgeIPXSapNode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 4),
    _RadBridgeIPXSapNode_Type()
)
radBridgeIPXSapNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapNode.setStatus("current")
_RadBridgeIPXSapSocket_Type = Integer32
_RadBridgeIPXSapSocket_Object = MibTableColumn
radBridgeIPXSapSocket = _RadBridgeIPXSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 5),
    _RadBridgeIPXSapSocket_Type()
)
radBridgeIPXSapSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapSocket.setStatus("current")


class _RadBridgeIPXSapHopsToServer_Type(Integer32):
    """Custom type radBridgeIPXSapHopsToServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RadBridgeIPXSapHopsToServer_Type.__name__ = "Integer32"
_RadBridgeIPXSapHopsToServer_Object = MibTableColumn
radBridgeIPXSapHopsToServer = _RadBridgeIPXSapHopsToServer_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 6),
    _RadBridgeIPXSapHopsToServer_Type()
)
radBridgeIPXSapHopsToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapHopsToServer.setStatus("current")
_RadBridgeIPXSapNIC_Type = Integer32
_RadBridgeIPXSapNIC_Object = MibTableColumn
radBridgeIPXSapNIC = _RadBridgeIPXSapNIC_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 7),
    _RadBridgeIPXSapNIC_Type()
)
radBridgeIPXSapNIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapNIC.setStatus("current")
_RadBridgeIPXSapAgingTime_Type = TimeTicks
_RadBridgeIPXSapAgingTime_Object = MibTableColumn
radBridgeIPXSapAgingTime = _RadBridgeIPXSapAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 8),
    _RadBridgeIPXSapAgingTime_Type()
)
radBridgeIPXSapAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapAgingTime.setStatus("current")


class _RadBridgeIPXSapStatus_Type(Integer32):
    """Custom type radBridgeIPXSapStatus based on Integer32"""
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
        *(("permanent", 1),
          ("dynamic", 2),
          ("invalid", 3),
          ("semiDynamic", 4))
    )


_RadBridgeIPXSapStatus_Type.__name__ = "Integer32"
_RadBridgeIPXSapStatus_Object = MibTableColumn
radBridgeIPXSapStatus = _RadBridgeIPXSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 9),
    _RadBridgeIPXSapStatus_Type()
)
radBridgeIPXSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapStatus.setStatus("current")
_RadBridgeIPXSapInfTable_Object = MibTable
radBridgeIPXSapInfTable = _RadBridgeIPXSapInfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    radBridgeIPXSapInfTable.setStatus("current")
_RadBridgeIPXSapInfEntry_Object = MibTableRow
radBridgeIPXSapInfEntry = _RadBridgeIPXSapInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1)
)
radBridgeIPXSapInfEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeIPXSapInfIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeIPXSapInfEntry.setStatus("current")
_RadBridgeIPXSapInfIfIndex_Type = Integer32
_RadBridgeIPXSapInfIfIndex_Object = MibTableColumn
radBridgeIPXSapInfIfIndex = _RadBridgeIPXSapInfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1, 1),
    _RadBridgeIPXSapInfIfIndex_Type()
)
radBridgeIPXSapInfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapInfIfIndex.setStatus("current")
_RadBridgeIPXSapInfBcastUpdate_Type = Integer32
_RadBridgeIPXSapInfBcastUpdate_Object = MibTableColumn
radBridgeIPXSapInfBcastUpdate = _RadBridgeIPXSapInfBcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1, 2),
    _RadBridgeIPXSapInfBcastUpdate_Type()
)
radBridgeIPXSapInfBcastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapInfBcastUpdate.setStatus("current")
_RadBridgeIPXSapInfAgeMultiplier_Type = Integer32
_RadBridgeIPXSapInfAgeMultiplier_Object = MibTableColumn
radBridgeIPXSapInfAgeMultiplier = _RadBridgeIPXSapInfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1, 3),
    _RadBridgeIPXSapInfAgeMultiplier_Type()
)
radBridgeIPXSapInfAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapInfAgeMultiplier.setStatus("current")
_NewMasking_ObjectIdentity = ObjectIdentity
newMasking = _NewMasking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6)
)
_MaskingMaxEntries_Type = Integer32
_MaskingMaxEntries_Object = MibScalar
maskingMaxEntries = _MaskingMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 1),
    _MaskingMaxEntries_Type()
)
maskingMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingMaxEntries.setStatus("current")
_MaskingCurrentEntries_Type = Integer32
_MaskingCurrentEntries_Object = MibScalar
maskingCurrentEntries = _MaskingCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 2),
    _MaskingCurrentEntries_Type()
)
maskingCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingCurrentEntries.setStatus("current")
_MaskingTable_Object = MibTable
maskingTable = _MaskingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    maskingTable.setStatus("current")
_MaskingEntry_Object = MibTableRow
maskingEntry = _MaskingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1)
)
maskingEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "maskingType"),
    (0, "RAD-BrgGen-MIB", "maskingIfIndex"),
    (0, "RAD-BrgGen-MIB", "maskingIndex"),
)
if mibBuilder.loadTexts:
    maskingEntry.setStatus("current")


class _MaskingType_Type(Integer32):
    """Custom type maskingType based on Integer32"""
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
        *(("tx", 1),
          ("rx", 2),
          ("compress", 3),
          ("priority", 4),
          ("loadSharing", 5),
          ("facs", 6),
          ("codConnect", 7),
          ("codDisconnect", 8))
    )


_MaskingType_Type.__name__ = "Integer32"
_MaskingType_Object = MibTableColumn
maskingType = _MaskingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 1),
    _MaskingType_Type()
)
maskingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingType.setStatus("current")
_MaskingIfIndex_Type = Integer32
_MaskingIfIndex_Object = MibTableColumn
maskingIfIndex = _MaskingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 2),
    _MaskingIfIndex_Type()
)
maskingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingIfIndex.setStatus("current")
_MaskingIndex_Type = Integer32
_MaskingIndex_Object = MibTableColumn
maskingIndex = _MaskingIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 3),
    _MaskingIndex_Type()
)
maskingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingIndex.setStatus("current")


class _MaskingProtocolType_Type(Integer32):
    """Custom type maskingProtocolType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ip", 2),
          ("ipx", 3),
          ("sna", 4),
          ("netbios", 5),
          ("apple", 6),
          ("dec", 7),
          ("all", 255))
    )


_MaskingProtocolType_Type.__name__ = "Integer32"
_MaskingProtocolType_Object = MibTableColumn
maskingProtocolType = _MaskingProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 4),
    _MaskingProtocolType_Type()
)
maskingProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingProtocolType.setStatus("current")
_MaskingSmartMaskOID_Type = ObjectIdentifier
_MaskingSmartMaskOID_Object = MibTableColumn
maskingSmartMaskOID = _MaskingSmartMaskOID_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 5),
    _MaskingSmartMaskOID_Type()
)
maskingSmartMaskOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingSmartMaskOID.setStatus("current")


class _MaskingFrameType_Type(Integer32):
    """Custom type maskingFrameType based on Integer32"""
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
          ("all", 2),
          ("broadcast", 3),
          ("multicast", 4))
    )


_MaskingFrameType_Type.__name__ = "Integer32"
_MaskingFrameType_Object = MibTableColumn
maskingFrameType = _MaskingFrameType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 6),
    _MaskingFrameType_Type()
)
maskingFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingFrameType.setStatus("current")


class _MaskingFrameTypeCondition_Type(Integer32):
    """Custom type maskingFrameTypeCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingFrameTypeCondition_Type.__name__ = "Integer32"
_MaskingFrameTypeCondition_Object = MibTableColumn
maskingFrameTypeCondition = _MaskingFrameTypeCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 7),
    _MaskingFrameTypeCondition_Type()
)
maskingFrameTypeCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingFrameTypeCondition.setStatus("current")
_MaskingSourceAddress_Type = GenAddress
_MaskingSourceAddress_Object = MibTableColumn
maskingSourceAddress = _MaskingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 8),
    _MaskingSourceAddress_Type()
)
maskingSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceAddress.setStatus("current")
_MaskingSourceActiveBits_Type = GenAddress
_MaskingSourceActiveBits_Object = MibTableColumn
maskingSourceActiveBits = _MaskingSourceActiveBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 9),
    _MaskingSourceActiveBits_Type()
)
maskingSourceActiveBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceActiveBits.setStatus("current")


class _MaskingSourceMacOrNet_Type(Integer32):
    """Custom type maskingSourceMacOrNet based on Integer32"""
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
        *(("macAddress", 1),
          ("netAddress", 2),
          ("ipRange", 3),
          ("appleAddress", 4))
    )


_MaskingSourceMacOrNet_Type.__name__ = "Integer32"
_MaskingSourceMacOrNet_Object = MibTableColumn
maskingSourceMacOrNet = _MaskingSourceMacOrNet_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 10),
    _MaskingSourceMacOrNet_Type()
)
maskingSourceMacOrNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceMacOrNet.setStatus("current")


class _MaskingSourceCondition_Type(Integer32):
    """Custom type maskingSourceCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingSourceCondition_Type.__name__ = "Integer32"
_MaskingSourceCondition_Object = MibTableColumn
maskingSourceCondition = _MaskingSourceCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 11),
    _MaskingSourceCondition_Type()
)
maskingSourceCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceCondition.setStatus("current")
_MaskingDestAddress_Type = GenAddress
_MaskingDestAddress_Object = MibTableColumn
maskingDestAddress = _MaskingDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 12),
    _MaskingDestAddress_Type()
)
maskingDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestAddress.setStatus("current")
_MaskingDestActiveBits_Type = GenAddress
_MaskingDestActiveBits_Object = MibTableColumn
maskingDestActiveBits = _MaskingDestActiveBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 13),
    _MaskingDestActiveBits_Type()
)
maskingDestActiveBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestActiveBits.setStatus("current")


class _MaskingDestMacOrNet_Type(Integer32):
    """Custom type maskingDestMacOrNet based on Integer32"""
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
        *(("macAddress", 1),
          ("netAddress", 2),
          ("ipRange", 3),
          ("appleAddress", 4))
    )


_MaskingDestMacOrNet_Type.__name__ = "Integer32"
_MaskingDestMacOrNet_Object = MibTableColumn
maskingDestMacOrNet = _MaskingDestMacOrNet_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 14),
    _MaskingDestMacOrNet_Type()
)
maskingDestMacOrNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestMacOrNet.setStatus("current")


class _MaskingDestCondition_Type(Integer32):
    """Custom type maskingDestCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingDestCondition_Type.__name__ = "Integer32"
_MaskingDestCondition_Object = MibTableColumn
maskingDestCondition = _MaskingDestCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 15),
    _MaskingDestCondition_Type()
)
maskingDestCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestCondition.setStatus("current")


class _MaskingLowLevelProt_Type(Integer32):
    """Custom type maskingLowLevelProt based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ipxRip", 2),
          ("ipxSap", 3),
          ("ipxSpx", 4),
          ("ipUdp", 5),
          ("ipTcp", 6),
          ("ipIcmp", 7),
          ("ipxNcp", 8),
          ("ipxWan", 9),
          ("ipxEco", 10),
          ("ipxErr", 11),
          ("ipxPep", 12))
    )


_MaskingLowLevelProt_Type.__name__ = "Integer32"
_MaskingLowLevelProt_Object = MibTableColumn
maskingLowLevelProt = _MaskingLowLevelProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 16),
    _MaskingLowLevelProt_Type()
)
maskingLowLevelProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingLowLevelProt.setStatus("current")


class _MaskingLowLevelProtCondition_Type(Integer32):
    """Custom type maskingLowLevelProtCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingLowLevelProtCondition_Type.__name__ = "Integer32"
_MaskingLowLevelProtCondition_Object = MibTableColumn
maskingLowLevelProtCondition = _MaskingLowLevelProtCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 17),
    _MaskingLowLevelProtCondition_Type()
)
maskingLowLevelProtCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingLowLevelProtCondition.setStatus("current")
_MaskingHighLevelProt_Type = Integer32
_MaskingHighLevelProt_Object = MibTableColumn
maskingHighLevelProt = _MaskingHighLevelProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 18),
    _MaskingHighLevelProt_Type()
)
maskingHighLevelProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingHighLevelProt.setStatus("current")


class _MaskingHighLevelProtCondition_Type(Integer32):
    """Custom type maskingHighLevelProtCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingHighLevelProtCondition_Type.__name__ = "Integer32"
_MaskingHighLevelProtCondition_Object = MibTableColumn
maskingHighLevelProtCondition = _MaskingHighLevelProtCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 19),
    _MaskingHighLevelProtCondition_Type()
)
maskingHighLevelProtCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingHighLevelProtCondition.setStatus("current")
_MaskingPortNum_Type = Integer32
_MaskingPortNum_Object = MibTableColumn
maskingPortNum = _MaskingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 20),
    _MaskingPortNum_Type()
)
maskingPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingPortNum.setStatus("current")


class _MaskingPortNumCondition_Type(Integer32):
    """Custom type maskingPortNumCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingPortNumCondition_Type.__name__ = "Integer32"
_MaskingPortNumCondition_Object = MibTableColumn
maskingPortNumCondition = _MaskingPortNumCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 21),
    _MaskingPortNumCondition_Type()
)
maskingPortNumCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingPortNumCondition.setStatus("current")


class _MaskingOperation_Type(Integer32):
    """Custom type maskingOperation based on Integer32"""
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
        *(("block", 1),
          ("forward", 2),
          ("route", 3),
          ("forward-route", 4),
          ("high-priority", 5),
          ("noOp", 6),
          ("delete", 7),
          ("smartMask", 8))
    )


_MaskingOperation_Type.__name__ = "Integer32"
_MaskingOperation_Object = MibTableColumn
maskingOperation = _MaskingOperation_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 22),
    _MaskingOperation_Type()
)
maskingOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingOperation.setStatus("current")
_MaskingSrcPortNum_Type = Integer32
_MaskingSrcPortNum_Object = MibTableColumn
maskingSrcPortNum = _MaskingSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 23),
    _MaskingSrcPortNum_Type()
)
maskingSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSrcPortNum.setStatus("current")


class _MaskingSrcPortNumCondition_Type(Integer32):
    """Custom type maskingSrcPortNumCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingSrcPortNumCondition_Type.__name__ = "Integer32"
_MaskingSrcPortNumCondition_Object = MibTableColumn
maskingSrcPortNumCondition = _MaskingSrcPortNumCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 24),
    _MaskingSrcPortNumCondition_Type()
)
maskingSrcPortNumCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSrcPortNumCondition.setStatus("current")
_RadBridgePerformance_ObjectIdentity = ObjectIdentity
radBridgePerformance = _RadBridgePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7)
)
_RadBridgeCurrentTable_Object = MibTable
radBridgeCurrentTable = _RadBridgeCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    radBridgeCurrentTable.setStatus("current")
_RadBridgeCurrentEntry_Object = MibTableRow
radBridgeCurrentEntry = _RadBridgeCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1)
)
radBridgeCurrentEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeCurrentIndex"),
)
if mibBuilder.loadTexts:
    radBridgeCurrentEntry.setStatus("current")
_RadBridgeCurrentIndex_Type = Integer32
_RadBridgeCurrentIndex_Object = MibTableColumn
radBridgeCurrentIndex = _RadBridgeCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 1),
    _RadBridgeCurrentIndex_Type()
)
radBridgeCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentIndex.setStatus("current")
_RadBridgeCurrentIngressFilteringDiscardedFrames_Type = Gauge32
_RadBridgeCurrentIngressFilteringDiscardedFrames_Object = MibTableColumn
radBridgeCurrentIngressFilteringDiscardedFrames = _RadBridgeCurrentIngressFilteringDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 2),
    _RadBridgeCurrentIngressFilteringDiscardedFrames_Type()
)
radBridgeCurrentIngressFilteringDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentIngressFilteringDiscardedFrames.setStatus("current")
_RadBridgeCurrentFrameTypeDiscardedFrames_Type = Gauge32
_RadBridgeCurrentFrameTypeDiscardedFrames_Object = MibTableColumn
radBridgeCurrentFrameTypeDiscardedFrames = _RadBridgeCurrentFrameTypeDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 3),
    _RadBridgeCurrentFrameTypeDiscardedFrames_Type()
)
radBridgeCurrentFrameTypeDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentFrameTypeDiscardedFrames.setStatus("current")
_RadBridgeCurrentRxCorrectFrames_Type = Gauge32
_RadBridgeCurrentRxCorrectFrames_Object = MibTableColumn
radBridgeCurrentRxCorrectFrames = _RadBridgeCurrentRxCorrectFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 4),
    _RadBridgeCurrentRxCorrectFrames_Type()
)
radBridgeCurrentRxCorrectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentRxCorrectFrames.setStatus("current")
_RadBridgeCurrentRxCorrectBytes_Type = Gauge32
_RadBridgeCurrentRxCorrectBytes_Object = MibTableColumn
radBridgeCurrentRxCorrectBytes = _RadBridgeCurrentRxCorrectBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 5),
    _RadBridgeCurrentRxCorrectBytes_Type()
)
radBridgeCurrentRxCorrectBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentRxCorrectBytes.setStatus("current")
_RadBridgeCurrentRxCorrectBytesHCOverflow_Type = Gauge32
_RadBridgeCurrentRxCorrectBytesHCOverflow_Object = MibTableColumn
radBridgeCurrentRxCorrectBytesHCOverflow = _RadBridgeCurrentRxCorrectBytesHCOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 6),
    _RadBridgeCurrentRxCorrectBytesHCOverflow_Type()
)
radBridgeCurrentRxCorrectBytesHCOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentRxCorrectBytesHCOverflow.setStatus("current")
_RadBridgeCurrentRxBcastFrames_Type = Gauge32
_RadBridgeCurrentRxBcastFrames_Object = MibTableColumn
radBridgeCurrentRxBcastFrames = _RadBridgeCurrentRxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 7),
    _RadBridgeCurrentRxBcastFrames_Type()
)
radBridgeCurrentRxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentRxBcastFrames.setStatus("current")
_RadBridgeCurrentRxMcastFrames_Type = Gauge32
_RadBridgeCurrentRxMcastFrames_Object = MibTableColumn
radBridgeCurrentRxMcastFrames = _RadBridgeCurrentRxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 8),
    _RadBridgeCurrentRxMcastFrames_Type()
)
radBridgeCurrentRxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentRxMcastFrames.setStatus("current")
_RadBridgeCurrentTxCorrectFrames_Type = Gauge32
_RadBridgeCurrentTxCorrectFrames_Object = MibTableColumn
radBridgeCurrentTxCorrectFrames = _RadBridgeCurrentTxCorrectFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 9),
    _RadBridgeCurrentTxCorrectFrames_Type()
)
radBridgeCurrentTxCorrectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentTxCorrectFrames.setStatus("current")
_RadBridgeCurrentTxCorrectBytes_Type = Gauge32
_RadBridgeCurrentTxCorrectBytes_Object = MibTableColumn
radBridgeCurrentTxCorrectBytes = _RadBridgeCurrentTxCorrectBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 10),
    _RadBridgeCurrentTxCorrectBytes_Type()
)
radBridgeCurrentTxCorrectBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentTxCorrectBytes.setStatus("current")
_RadBridgeCurrentTxCorrectBytesHCOverflow_Type = Gauge32
_RadBridgeCurrentTxCorrectBytesHCOverflow_Object = MibTableColumn
radBridgeCurrentTxCorrectBytesHCOverflow = _RadBridgeCurrentTxCorrectBytesHCOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 11),
    _RadBridgeCurrentTxCorrectBytesHCOverflow_Type()
)
radBridgeCurrentTxCorrectBytesHCOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentTxCorrectBytesHCOverflow.setStatus("current")
_RadBridgeCurrentTxBcastFrames_Type = Gauge32
_RadBridgeCurrentTxBcastFrames_Object = MibTableColumn
radBridgeCurrentTxBcastFrames = _RadBridgeCurrentTxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 12),
    _RadBridgeCurrentTxBcastFrames_Type()
)
radBridgeCurrentTxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentTxBcastFrames.setStatus("current")
_RadBridgeCurrentTxMcastFrames_Type = Gauge32
_RadBridgeCurrentTxMcastFrames_Object = MibTableColumn
radBridgeCurrentTxMcastFrames = _RadBridgeCurrentTxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 13),
    _RadBridgeCurrentTxMcastFrames_Type()
)
radBridgeCurrentTxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentTxMcastFrames.setStatus("current")
_RadBridgeCurrentTxDropFrames_Type = Gauge32
_RadBridgeCurrentTxDropFrames_Object = MibTableColumn
radBridgeCurrentTxDropFrames = _RadBridgeCurrentTxDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 1, 1, 14),
    _RadBridgeCurrentTxDropFrames_Type()
)
radBridgeCurrentTxDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCurrentTxDropFrames.setStatus("current")
_RadBridgeIntervalTable_Object = MibTable
radBridgeIntervalTable = _RadBridgeIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2)
)
if mibBuilder.loadTexts:
    radBridgeIntervalTable.setStatus("current")
_RadBridgeIntervalEntry_Object = MibTableRow
radBridgeIntervalEntry = _RadBridgeIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1)
)
radBridgeIntervalEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeIntervalIndex"),
    (0, "RAD-BrgGen-MIB", "radBridgeIntervalNumber"),
)
if mibBuilder.loadTexts:
    radBridgeIntervalEntry.setStatus("current")
_RadBridgeIntervalIndex_Type = Integer32
_RadBridgeIntervalIndex_Object = MibTableColumn
radBridgeIntervalIndex = _RadBridgeIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 1),
    _RadBridgeIntervalIndex_Type()
)
radBridgeIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalIndex.setStatus("current")


class _RadBridgeIntervalNumber_Type(Integer32):
    """Custom type radBridgeIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RadBridgeIntervalNumber_Type.__name__ = "Integer32"
_RadBridgeIntervalNumber_Object = MibTableColumn
radBridgeIntervalNumber = _RadBridgeIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 2),
    _RadBridgeIntervalNumber_Type()
)
radBridgeIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalNumber.setStatus("current")
_RadBridgeIntervalIngressFilteringDiscardedFrames_Type = Gauge32
_RadBridgeIntervalIngressFilteringDiscardedFrames_Object = MibTableColumn
radBridgeIntervalIngressFilteringDiscardedFrames = _RadBridgeIntervalIngressFilteringDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 3),
    _RadBridgeIntervalIngressFilteringDiscardedFrames_Type()
)
radBridgeIntervalIngressFilteringDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalIngressFilteringDiscardedFrames.setStatus("current")
_RadBridgeIntervalFrameTypeDiscardedFrames_Type = Gauge32
_RadBridgeIntervalFrameTypeDiscardedFrames_Object = MibTableColumn
radBridgeIntervalFrameTypeDiscardedFrames = _RadBridgeIntervalFrameTypeDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 4),
    _RadBridgeIntervalFrameTypeDiscardedFrames_Type()
)
radBridgeIntervalFrameTypeDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalFrameTypeDiscardedFrames.setStatus("current")
_RadBridgeIntervalRxCorrectFrames_Type = Gauge32
_RadBridgeIntervalRxCorrectFrames_Object = MibTableColumn
radBridgeIntervalRxCorrectFrames = _RadBridgeIntervalRxCorrectFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 5),
    _RadBridgeIntervalRxCorrectFrames_Type()
)
radBridgeIntervalRxCorrectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalRxCorrectFrames.setStatus("current")
_RadBridgeIntervalRxCorrectBytes_Type = Gauge32
_RadBridgeIntervalRxCorrectBytes_Object = MibTableColumn
radBridgeIntervalRxCorrectBytes = _RadBridgeIntervalRxCorrectBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 6),
    _RadBridgeIntervalRxCorrectBytes_Type()
)
radBridgeIntervalRxCorrectBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalRxCorrectBytes.setStatus("current")
_RadBridgeIntervalRxCorrectBytesHCOverflow_Type = Gauge32
_RadBridgeIntervalRxCorrectBytesHCOverflow_Object = MibTableColumn
radBridgeIntervalRxCorrectBytesHCOverflow = _RadBridgeIntervalRxCorrectBytesHCOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 7),
    _RadBridgeIntervalRxCorrectBytesHCOverflow_Type()
)
radBridgeIntervalRxCorrectBytesHCOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalRxCorrectBytesHCOverflow.setStatus("current")
_RadBridgeIntervalRxBcastFrames_Type = Gauge32
_RadBridgeIntervalRxBcastFrames_Object = MibTableColumn
radBridgeIntervalRxBcastFrames = _RadBridgeIntervalRxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 8),
    _RadBridgeIntervalRxBcastFrames_Type()
)
radBridgeIntervalRxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalRxBcastFrames.setStatus("current")
_RadBridgeIntervalRxMcastFrames_Type = Gauge32
_RadBridgeIntervalRxMcastFrames_Object = MibTableColumn
radBridgeIntervalRxMcastFrames = _RadBridgeIntervalRxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 9),
    _RadBridgeIntervalRxMcastFrames_Type()
)
radBridgeIntervalRxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalRxMcastFrames.setStatus("current")
_RadBridgeIntervalTxCorrectFrames_Type = Gauge32
_RadBridgeIntervalTxCorrectFrames_Object = MibTableColumn
radBridgeIntervalTxCorrectFrames = _RadBridgeIntervalTxCorrectFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 10),
    _RadBridgeIntervalTxCorrectFrames_Type()
)
radBridgeIntervalTxCorrectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalTxCorrectFrames.setStatus("current")
_RadBridgeIntervalTxCorrectBytes_Type = Gauge32
_RadBridgeIntervalTxCorrectBytes_Object = MibTableColumn
radBridgeIntervalTxCorrectBytes = _RadBridgeIntervalTxCorrectBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 11),
    _RadBridgeIntervalTxCorrectBytes_Type()
)
radBridgeIntervalTxCorrectBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalTxCorrectBytes.setStatus("current")
_RadBridgeIntervalTxCorrectBytesHCOverflow_Type = Gauge32
_RadBridgeIntervalTxCorrectBytesHCOverflow_Object = MibTableColumn
radBridgeIntervalTxCorrectBytesHCOverflow = _RadBridgeIntervalTxCorrectBytesHCOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 12),
    _RadBridgeIntervalTxCorrectBytesHCOverflow_Type()
)
radBridgeIntervalTxCorrectBytesHCOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalTxCorrectBytesHCOverflow.setStatus("current")
_RadBridgeIntervalTxBcastFrames_Type = Gauge32
_RadBridgeIntervalTxBcastFrames_Object = MibTableColumn
radBridgeIntervalTxBcastFrames = _RadBridgeIntervalTxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 13),
    _RadBridgeIntervalTxBcastFrames_Type()
)
radBridgeIntervalTxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalTxBcastFrames.setStatus("current")
_RadBridgeIntervalTxMcastFrames_Type = Gauge32
_RadBridgeIntervalTxMcastFrames_Object = MibTableColumn
radBridgeIntervalTxMcastFrames = _RadBridgeIntervalTxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 14),
    _RadBridgeIntervalTxMcastFrames_Type()
)
radBridgeIntervalTxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalTxMcastFrames.setStatus("current")
_RadBridgeIntervalTxDropFrames_Type = Gauge32
_RadBridgeIntervalTxDropFrames_Object = MibTableColumn
radBridgeIntervalTxDropFrames = _RadBridgeIntervalTxDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 7, 2, 1, 15),
    _RadBridgeIntervalTxDropFrames_Type()
)
radBridgeIntervalTxDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIntervalTxDropFrames.setStatus("current")
_RadBridgePortBaseVlan_ObjectIdentity = ObjectIdentity
radBridgePortBaseVlan = _RadBridgePortBaseVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8)
)
_RadBridgePortBaseVlanTable_Object = MibTable
radBridgePortBaseVlanTable = _RadBridgePortBaseVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    radBridgePortBaseVlanTable.setStatus("current")
_RadBridgePortBaseVlanEntry_Object = MibTableRow
radBridgePortBaseVlanEntry = _RadBridgePortBaseVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1)
)
radBridgePortBaseVlanEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgePortBaseVlanCnfgIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgePortBaseVlanIdx"),
)
if mibBuilder.loadTexts:
    radBridgePortBaseVlanEntry.setStatus("current")


class _RadBridgePortBaseVlanCnfgIdx_Type(Integer32):
    """Custom type radBridgePortBaseVlanCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RadBridgePortBaseVlanCnfgIdx_Type.__name__ = "Integer32"
_RadBridgePortBaseVlanCnfgIdx_Object = MibTableColumn
radBridgePortBaseVlanCnfgIdx = _RadBridgePortBaseVlanCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 1),
    _RadBridgePortBaseVlanCnfgIdx_Type()
)
radBridgePortBaseVlanCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanCnfgIdx.setStatus("current")
_RadBridgePortBaseVlanIdx_Type = Integer32
_RadBridgePortBaseVlanIdx_Object = MibTableColumn
radBridgePortBaseVlanIdx = _RadBridgePortBaseVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 2),
    _RadBridgePortBaseVlanIdx_Type()
)
radBridgePortBaseVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanIdx.setStatus("current")


class _RadBridgePortBaseVlanName_Type(SnmpAdminString):
    """Custom type radBridgePortBaseVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadBridgePortBaseVlanName_Type.__name__ = "SnmpAdminString"
_RadBridgePortBaseVlanName_Object = MibTableColumn
radBridgePortBaseVlanName = _RadBridgePortBaseVlanName_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 3),
    _RadBridgePortBaseVlanName_Type()
)
radBridgePortBaseVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanName.setStatus("current")
_RadBridgePortBaseVlanEgressPorts_Type = PortList
_RadBridgePortBaseVlanEgressPorts_Object = MibTableColumn
radBridgePortBaseVlanEgressPorts = _RadBridgePortBaseVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 4),
    _RadBridgePortBaseVlanEgressPorts_Type()
)
radBridgePortBaseVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanEgressPorts.setStatus("current")
_RadBridgePortBaseVlanVirtualGroups_Type = PortList
_RadBridgePortBaseVlanVirtualGroups_Object = MibTableColumn
radBridgePortBaseVlanVirtualGroups = _RadBridgePortBaseVlanVirtualGroups_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 5),
    _RadBridgePortBaseVlanVirtualGroups_Type()
)
radBridgePortBaseVlanVirtualGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanVirtualGroups.setStatus("current")
_RadBridgePortBaseVlanRowStatus_Type = RowStatus
_RadBridgePortBaseVlanRowStatus_Object = MibTableColumn
radBridgePortBaseVlanRowStatus = _RadBridgePortBaseVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 6),
    _RadBridgePortBaseVlanRowStatus_Type()
)
radBridgePortBaseVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanRowStatus.setStatus("current")


class _RadBridgePortBaseVlanMng_Type(Integer32):
    """Custom type radBridgePortBaseVlanMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_RadBridgePortBaseVlanMng_Type.__name__ = "Integer32"
_RadBridgePortBaseVlanMng_Object = MibTableColumn
radBridgePortBaseVlanMng = _RadBridgePortBaseVlanMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 1, 1, 7),
    _RadBridgePortBaseVlanMng_Type()
)
radBridgePortBaseVlanMng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortBaseVlanMng.setStatus("current")
_RadBridgePortVlanMemberTable_Object = MibTable
radBridgePortVlanMemberTable = _RadBridgePortVlanMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 2)
)
if mibBuilder.loadTexts:
    radBridgePortVlanMemberTable.setStatus("current")
_RadBridgePortVlanMemberEntry_Object = MibTableRow
radBridgePortVlanMemberEntry = _RadBridgePortVlanMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 2, 1)
)
radBridgePortVlanMemberEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgePortVlanMemberBridgeIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgePortVlanMemberPortIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgePortVlanMemberVlanId"),
)
if mibBuilder.loadTexts:
    radBridgePortVlanMemberEntry.setStatus("current")
_RadBridgePortVlanMemberBridgeIdx_Type = Integer32
_RadBridgePortVlanMemberBridgeIdx_Object = MibTableColumn
radBridgePortVlanMemberBridgeIdx = _RadBridgePortVlanMemberBridgeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 2, 1, 1),
    _RadBridgePortVlanMemberBridgeIdx_Type()
)
radBridgePortVlanMemberBridgeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgePortVlanMemberBridgeIdx.setStatus("current")
_RadBridgePortVlanMemberPortIdx_Type = Integer32
_RadBridgePortVlanMemberPortIdx_Object = MibTableColumn
radBridgePortVlanMemberPortIdx = _RadBridgePortVlanMemberPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 2, 1, 2),
    _RadBridgePortVlanMemberPortIdx_Type()
)
radBridgePortVlanMemberPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgePortVlanMemberPortIdx.setStatus("current")
_RadBridgePortVlanMemberVlanId_Type = Integer32
_RadBridgePortVlanMemberVlanId_Object = MibTableColumn
radBridgePortVlanMemberVlanId = _RadBridgePortVlanMemberVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 2, 1, 3),
    _RadBridgePortVlanMemberVlanId_Type()
)
radBridgePortVlanMemberVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgePortVlanMemberVlanId.setStatus("current")
_RadBridgePortVlanMemberRowStatus_Type = RowStatus
_RadBridgePortVlanMemberRowStatus_Object = MibTableColumn
radBridgePortVlanMemberRowStatus = _RadBridgePortVlanMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 8, 2, 1, 4),
    _RadBridgePortVlanMemberRowStatus_Type()
)
radBridgePortVlanMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortVlanMemberRowStatus.setStatus("current")
_RadBridgeGenCnfg_ObjectIdentity = ObjectIdentity
radBridgeGenCnfg = _RadBridgeGenCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9)
)
_RadBridgeGenFlowTable_Object = MibTable
radBridgeGenFlowTable = _RadBridgeGenFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    radBridgeGenFlowTable.setStatus("current")
_RadBridgeGenFlowEntry_Object = MibTableRow
radBridgeGenFlowEntry = _RadBridgeGenFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1)
)
radBridgeGenFlowEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeGenFlowCnfgIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgeGenFlowIdx"),
)
if mibBuilder.loadTexts:
    radBridgeGenFlowEntry.setStatus("current")


class _RadBridgeGenFlowCnfgIdx_Type(Integer32):
    """Custom type radBridgeGenFlowCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadBridgeGenFlowCnfgIdx_Type.__name__ = "Integer32"
_RadBridgeGenFlowCnfgIdx_Object = MibTableColumn
radBridgeGenFlowCnfgIdx = _RadBridgeGenFlowCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 1),
    _RadBridgeGenFlowCnfgIdx_Type()
)
radBridgeGenFlowCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeGenFlowCnfgIdx.setStatus("current")
_RadBridgeGenFlowIdx_Type = Integer32
_RadBridgeGenFlowIdx_Object = MibTableColumn
radBridgeGenFlowIdx = _RadBridgeGenFlowIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 2),
    _RadBridgeGenFlowIdx_Type()
)
radBridgeGenFlowIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeGenFlowIdx.setStatus("current")
_RadBridgeGenFlowRowStatus_Type = RowStatus
_RadBridgeGenFlowRowStatus_Object = MibTableColumn
radBridgeGenFlowRowStatus = _RadBridgeGenFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 3),
    _RadBridgeGenFlowRowStatus_Type()
)
radBridgeGenFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowRowStatus.setStatus("current")
_RadBridgeGenFlowFloodOrBcastMaxRate_Type = Integer32
_RadBridgeGenFlowFloodOrBcastMaxRate_Object = MibTableColumn
radBridgeGenFlowFloodOrBcastMaxRate = _RadBridgeGenFlowFloodOrBcastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 4),
    _RadBridgeGenFlowFloodOrBcastMaxRate_Type()
)
radBridgeGenFlowFloodOrBcastMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowFloodOrBcastMaxRate.setStatus("current")


class _RadBridgeGenFlowQosMode_Type(Integer32):
    """Custom type radBridgeGenFlowQosMode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("vlanTag", 2),
          ("dscp", 3),
          ("dscpAndVlanTag", 4),
          ("vlanTagAndDscp", 5),
          ("none", 6),
          ("tos", 7),
          ("perPort", 8),
          ("ipPrecedence", 9),
          ("dsField", 10),
          ("vlanTagAndTos", 11),
          ("tosAndVlanTag", 12),
          ("vlanTagAndIpPrecedence", 13),
          ("ipPrecedenceAndVlanTag", 14),
          ("vlanTagAndDsField", 15),
          ("dsFieldAndVlanTag", 16),
          ("vlanId", 17))
    )


_RadBridgeGenFlowQosMode_Type.__name__ = "Integer32"
_RadBridgeGenFlowQosMode_Object = MibTableColumn
radBridgeGenFlowQosMode = _RadBridgeGenFlowQosMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 5),
    _RadBridgeGenFlowQosMode_Type()
)
radBridgeGenFlowQosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowQosMode.setStatus("current")


class _RadBridgeGenFlowSchedulingMode_Type(Integer32):
    """Custom type radBridgeGenFlowSchedulingMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("wfq", 2),
          ("sp", 3),
          ("atmCos", 4),
          ("wrr", 5),
          ("hqpAndWrr", 6),
          ("spAndWrr", 7))
    )


_RadBridgeGenFlowSchedulingMode_Type.__name__ = "Integer32"
_RadBridgeGenFlowSchedulingMode_Object = MibTableColumn
radBridgeGenFlowSchedulingMode = _RadBridgeGenFlowSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 6),
    _RadBridgeGenFlowSchedulingMode_Type()
)
radBridgeGenFlowSchedulingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowSchedulingMode.setStatus("current")


class _RadBridgeGenFlowBasicClassification_Type(Integer32):
    """Custom type radBridgeGenFlowBasicClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("port", 3))
    )


_RadBridgeGenFlowBasicClassification_Type.__name__ = "Integer32"
_RadBridgeGenFlowBasicClassification_Object = MibTableColumn
radBridgeGenFlowBasicClassification = _RadBridgeGenFlowBasicClassification_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 7),
    _RadBridgeGenFlowBasicClassification_Type()
)
radBridgeGenFlowBasicClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowBasicClassification.setStatus("current")
_RadBridgeGenFlowMulticastTrafficClass_Type = Integer32
_RadBridgeGenFlowMulticastTrafficClass_Object = MibTableColumn
radBridgeGenFlowMulticastTrafficClass = _RadBridgeGenFlowMulticastTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 8),
    _RadBridgeGenFlowMulticastTrafficClass_Type()
)
radBridgeGenFlowMulticastTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowMulticastTrafficClass.setStatus("current")
_RadBridgeGenFlowBroadcastTrafficClass_Type = Integer32
_RadBridgeGenFlowBroadcastTrafficClass_Object = MibTableColumn
radBridgeGenFlowBroadcastTrafficClass = _RadBridgeGenFlowBroadcastTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 9),
    _RadBridgeGenFlowBroadcastTrafficClass_Type()
)
radBridgeGenFlowBroadcastTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowBroadcastTrafficClass.setStatus("current")
_RadBridgeGenFlowUnkownUnicastTrafficClass_Type = Integer32
_RadBridgeGenFlowUnkownUnicastTrafficClass_Object = MibTableColumn
radBridgeGenFlowUnkownUnicastTrafficClass = _RadBridgeGenFlowUnkownUnicastTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 1, 1, 10),
    _RadBridgeGenFlowUnkownUnicastTrafficClass_Type()
)
radBridgeGenFlowUnkownUnicastTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeGenFlowUnkownUnicastTrafficClass.setStatus("current")
_RadBridgeDot1qVlanStaticTable_Object = MibTable
radBridgeDot1qVlanStaticTable = _RadBridgeDot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 2)
)
if mibBuilder.loadTexts:
    radBridgeDot1qVlanStaticTable.setStatus("current")
_RadBridgeDot1qVlanStaticEntry_Object = MibTableRow
radBridgeDot1qVlanStaticEntry = _RadBridgeDot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    radBridgeDot1qVlanStaticEntry.setStatus("current")
_RadBridgeDot1qVlanTaggedPorts_Type = PortList
_RadBridgeDot1qVlanTaggedPorts_Object = MibTableColumn
radBridgeDot1qVlanTaggedPorts = _RadBridgeDot1qVlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 2, 1, 1),
    _RadBridgeDot1qVlanTaggedPorts_Type()
)
radBridgeDot1qVlanTaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeDot1qVlanTaggedPorts.setStatus("current")
_RadBridgeDot1qVlanUnmodifiedPorts_Type = PortList
_RadBridgeDot1qVlanUnmodifiedPorts_Object = MibTableColumn
radBridgeDot1qVlanUnmodifiedPorts = _RadBridgeDot1qVlanUnmodifiedPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 2, 1, 2),
    _RadBridgeDot1qVlanUnmodifiedPorts_Type()
)
radBridgeDot1qVlanUnmodifiedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeDot1qVlanUnmodifiedPorts.setStatus("current")


class _RadBridgeDot1qVlanSplitHorizon_Type(Integer32):
    """Custom type radBridgeDot1qVlanSplitHorizon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_RadBridgeDot1qVlanSplitHorizon_Type.__name__ = "Integer32"
_RadBridgeDot1qVlanSplitHorizon_Object = MibTableColumn
radBridgeDot1qVlanSplitHorizon = _RadBridgeDot1qVlanSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 2, 1, 3),
    _RadBridgeDot1qVlanSplitHorizon_Type()
)
radBridgeDot1qVlanSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeDot1qVlanSplitHorizon.setStatus("current")


class _RadBridgeDot1qVlanRingMembers_Type(Bits):
    """Custom type radBridgeDot1qVlanRingMembers based on Bits"""
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ring1", 1),
          ("ring2", 2),
          ("ring3", 3),
          ("ring4", 4),
          ("ring5", 5))
    )

_RadBridgeDot1qVlanRingMembers_Type.__name__ = "Bits"
_RadBridgeDot1qVlanRingMembers_Object = MibTableColumn
radBridgeDot1qVlanRingMembers = _RadBridgeDot1qVlanRingMembers_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 2, 1, 4),
    _RadBridgeDot1qVlanRingMembers_Type()
)
radBridgeDot1qVlanRingMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgeDot1qVlanRingMembers.setStatus("current")
_RadDot1qPortVlanTable_Object = MibTable
radDot1qPortVlanTable = _RadDot1qPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3)
)
if mibBuilder.loadTexts:
    radDot1qPortVlanTable.setStatus("current")
_RadDot1qPortVlanEntry_Object = MibTableRow
radDot1qPortVlanEntry = _RadDot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    radDot1qPortVlanEntry.setStatus("current")


class _RadDot1qPortStacking_Type(Integer32):
    """Custom type radDot1qPortStacking based on Integer32"""
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
        *(("notApplicable", 1),
          ("unmodify", 2),
          ("tag", 3),
          ("stack", 4))
    )


_RadDot1qPortStacking_Type.__name__ = "Integer32"
_RadDot1qPortStacking_Object = MibTableColumn
radDot1qPortStacking = _RadDot1qPortStacking_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 1),
    _RadDot1qPortStacking_Type()
)
radDot1qPortStacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortStacking.setStatus("current")


class _RadDot1qPortCopyOriginVlanPriority_Type(Integer32):
    """Custom type radDot1qPortCopyOriginVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_RadDot1qPortCopyOriginVlanPriority_Type.__name__ = "Integer32"
_RadDot1qPortCopyOriginVlanPriority_Object = MibTableColumn
radDot1qPortCopyOriginVlanPriority = _RadDot1qPortCopyOriginVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 2),
    _RadDot1qPortCopyOriginVlanPriority_Type()
)
radDot1qPortCopyOriginVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortCopyOriginVlanPriority.setStatus("current")
_RadDot1qPortDefaultVlanPriority_Type = Integer32
_RadDot1qPortDefaultVlanPriority_Object = MibTableColumn
radDot1qPortDefaultVlanPriority = _RadDot1qPortDefaultVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 3),
    _RadDot1qPortDefaultVlanPriority_Type()
)
radDot1qPortDefaultVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortDefaultVlanPriority.setStatus("current")


class _RadDot1qPortTagStripping_Type(Integer32):
    """Custom type radDot1qPortTagStripping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_RadDot1qPortTagStripping_Type.__name__ = "Integer32"
_RadDot1qPortTagStripping_Object = MibTableColumn
radDot1qPortTagStripping = _RadDot1qPortTagStripping_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 4),
    _RadDot1qPortTagStripping_Type()
)
radDot1qPortTagStripping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortTagStripping.setStatus("current")


class _RadDot1qPortEgressTagHandling_Type(Integer32):
    """Custom type radDot1qPortEgressTagHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("stacking", 3),
          ("stripping", 4))
    )


_RadDot1qPortEgressTagHandling_Type.__name__ = "Integer32"
_RadDot1qPortEgressTagHandling_Object = MibTableColumn
radDot1qPortEgressTagHandling = _RadDot1qPortEgressTagHandling_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 5),
    _RadDot1qPortEgressTagHandling_Type()
)
radDot1qPortEgressTagHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortEgressTagHandling.setStatus("current")


class _RadDot1qPortIngressTagHandling_Type(Integer32):
    """Custom type radDot1qPortIngressTagHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("stacking", 3),
          ("stripping", 4))
    )


_RadDot1qPortIngressTagHandling_Type.__name__ = "Integer32"
_RadDot1qPortIngressTagHandling_Object = MibTableColumn
radDot1qPortIngressTagHandling = _RadDot1qPortIngressTagHandling_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 6),
    _RadDot1qPortIngressTagHandling_Type()
)
radDot1qPortIngressTagHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortIngressTagHandling.setStatus("current")


class _RadDot1qPortReplaceVlanPriority_Type(Integer32):
    """Custom type radDot1qPortReplaceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_RadDot1qPortReplaceVlanPriority_Type.__name__ = "Integer32"
_RadDot1qPortReplaceVlanPriority_Object = MibTableColumn
radDot1qPortReplaceVlanPriority = _RadDot1qPortReplaceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 7),
    _RadDot1qPortReplaceVlanPriority_Type()
)
radDot1qPortReplaceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortReplaceVlanPriority.setStatus("current")
_RadDot1qPortVlanEthType_Type = Unsigned32
_RadDot1qPortVlanEthType_Object = MibTableColumn
radDot1qPortVlanEthType = _RadDot1qPortVlanEthType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 8),
    _RadDot1qPortVlanEthType_Type()
)
radDot1qPortVlanEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortVlanEthType.setStatus("current")


class _RadDot1qPortVlanCnodeLevel1Agent_Type(Integer32):
    """Custom type radDot1qPortVlanCnodeLevel1Agent based on Integer32"""
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


_RadDot1qPortVlanCnodeLevel1Agent_Type.__name__ = "Integer32"
_RadDot1qPortVlanCnodeLevel1Agent_Object = MibTableColumn
radDot1qPortVlanCnodeLevel1Agent = _RadDot1qPortVlanCnodeLevel1Agent_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 3, 1, 9),
    _RadDot1qPortVlanCnodeLevel1Agent_Type()
)
radDot1qPortVlanCnodeLevel1Agent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radDot1qPortVlanCnodeLevel1Agent.setStatus("current")
_RadBridgeGenCfgTable_Object = MibTable
radBridgeGenCfgTable = _RadBridgeGenCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4)
)
if mibBuilder.loadTexts:
    radBridgeGenCfgTable.setStatus("current")
_RadBridgeGenCfgEntry_Object = MibTableRow
radBridgeGenCfgEntry = _RadBridgeGenCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1)
)
radBridgeGenCfgEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeGenCfgIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgeGenCfgIdx2"),
)
if mibBuilder.loadTexts:
    radBridgeGenCfgEntry.setStatus("current")


class _RadBridgeGenCfgIdx_Type(Integer32):
    """Custom type radBridgeGenCfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RadBridgeGenCfgIdx_Type.__name__ = "Integer32"
_RadBridgeGenCfgIdx_Object = MibTableColumn
radBridgeGenCfgIdx = _RadBridgeGenCfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 1),
    _RadBridgeGenCfgIdx_Type()
)
radBridgeGenCfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeGenCfgIdx.setStatus("current")
_RadBridgeGenCfgIdx2_Type = Integer32
_RadBridgeGenCfgIdx2_Object = MibTableColumn
radBridgeGenCfgIdx2 = _RadBridgeGenCfgIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 2),
    _RadBridgeGenCfgIdx2_Type()
)
radBridgeGenCfgIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeGenCfgIdx2.setStatus("current")


class _RadBridgeGenCfgBridgeAction_Type(Integer32):
    """Custom type radBridgeGenCfgBridgeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deleteLanTab", 7),
          ("noOp", 255))
    )


_RadBridgeGenCfgBridgeAction_Type.__name__ = "Integer32"
_RadBridgeGenCfgBridgeAction_Object = MibTableColumn
radBridgeGenCfgBridgeAction = _RadBridgeGenCfgBridgeAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 3),
    _RadBridgeGenCfgBridgeAction_Type()
)
radBridgeGenCfgBridgeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeGenCfgBridgeAction.setStatus("current")


class _RadBridgeAgingTimeSec_Type(Integer32):
    """Custom type radBridgeAgingTimeSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_RadBridgeAgingTimeSec_Type.__name__ = "Integer32"
_RadBridgeAgingTimeSec_Object = MibTableColumn
radBridgeAgingTimeSec = _RadBridgeAgingTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 4),
    _RadBridgeAgingTimeSec_Type()
)
radBridgeAgingTimeSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeAgingTimeSec.setStatus("current")
_RadBridgeMngVlanId_Type = Unsigned32
_RadBridgeMngVlanId_Object = MibTableColumn
radBridgeMngVlanId = _RadBridgeMngVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 5),
    _RadBridgeMngVlanId_Type()
)
radBridgeMngVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMngVlanId.setStatus("current")
_RadBridgeLoopDetectVlanId_Type = Unsigned32
_RadBridgeLoopDetectVlanId_Object = MibTableColumn
radBridgeLoopDetectVlanId = _RadBridgeLoopDetectVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 6),
    _RadBridgeLoopDetectVlanId_Type()
)
radBridgeLoopDetectVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeLoopDetectVlanId.setStatus("current")


class _RadBridgeSplitHorizon_Type(Integer32):
    """Custom type radBridgeSplitHorizon based on Integer32"""
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
        *(("notApplicable", 1),
          ("disable", 2),
          ("enabled", 3),
          ("vlanBased", 4))
    )


_RadBridgeSplitHorizon_Type.__name__ = "Integer32"
_RadBridgeSplitHorizon_Object = MibTableColumn
radBridgeSplitHorizon = _RadBridgeSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 7),
    _RadBridgeSplitHorizon_Type()
)
radBridgeSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeSplitHorizon.setStatus("current")
_RadBridgeEthType_Type = Unsigned32
_RadBridgeEthType_Object = MibTableColumn
radBridgeEthType = _RadBridgeEthType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 8),
    _RadBridgeEthType_Type()
)
radBridgeEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeEthType.setStatus("current")
_RadBridgeTopology_Type = BridgeTopology
_RadBridgeTopology_Object = MibTableColumn
radBridgeTopology = _RadBridgeTopology_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 4, 1, 9),
    _RadBridgeTopology_Type()
)
radBridgeTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeTopology.setStatus("current")


class _RadBridgeAgingTime_Type(Integer32):
    """Custom type radBridgeAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("infinite", 2),
          ("finite", 3))
    )


_RadBridgeAgingTime_Type.__name__ = "Integer32"
_RadBridgeAgingTime_Object = MibScalar
radBridgeAgingTime = _RadBridgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 5),
    _RadBridgeAgingTime_Type()
)
radBridgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeAgingTime.setStatus("current")


class _RadBridgeMngFlow_Type(Integer32):
    """Custom type radBridgeMngFlow based on Integer32"""
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


_RadBridgeMngFlow_Type.__name__ = "Integer32"
_RadBridgeMngFlow_Object = MibScalar
radBridgeMngFlow = _RadBridgeMngFlow_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 6),
    _RadBridgeMngFlow_Type()
)
radBridgeMngFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMngFlow.setStatus("current")
_Ieee8021QBridgeVlanStaticXTable_Object = MibTable
ieee8021QBridgeVlanStaticXTable = _Ieee8021QBridgeVlanStaticXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 7)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticXTable.setStatus("current")
_Ieee8021QBridgeVlanStaticXEntry_Object = MibTableRow
ieee8021QBridgeVlanStaticXEntry = _Ieee8021QBridgeVlanStaticXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 7, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticXEntry.setStatus("current")


class _Ieee8021QBridgeVlanStaticXSplitHorizon_Type(Integer32):
    """Custom type ieee8021QBridgeVlanStaticXSplitHorizon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ieee8021QBridgeVlanStaticXSplitHorizon_Type.__name__ = "Integer32"
_Ieee8021QBridgeVlanStaticXSplitHorizon_Object = MibTableColumn
ieee8021QBridgeVlanStaticXSplitHorizon = _Ieee8021QBridgeVlanStaticXSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 7, 1, 3),
    _Ieee8021QBridgeVlanStaticXSplitHorizon_Type()
)
ieee8021QBridgeVlanStaticXSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticXSplitHorizon.setStatus("current")
_Ieee8021QBridgeVlanStaticXRingMembers_Type = OctetString
_Ieee8021QBridgeVlanStaticXRingMembers_Object = MibTableColumn
ieee8021QBridgeVlanStaticXRingMembers = _Ieee8021QBridgeVlanStaticXRingMembers_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 7, 1, 4),
    _Ieee8021QBridgeVlanStaticXRingMembers_Type()
)
ieee8021QBridgeVlanStaticXRingMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticXRingMembers.setStatus("current")
_Ieee8021QBridgeVlanStaticXMaxMacAddr_Type = Unsigned32
_Ieee8021QBridgeVlanStaticXMaxMacAddr_Object = MibTableColumn
ieee8021QBridgeVlanStaticXMaxMacAddr = _Ieee8021QBridgeVlanStaticXMaxMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 7, 1, 8),
    _Ieee8021QBridgeVlanStaticXMaxMacAddr_Type()
)
ieee8021QBridgeVlanStaticXMaxMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticXMaxMacAddr.setStatus("current")
_Ieee8021QBridgeVlanStaticXTopology_Type = BridgeTopology
_Ieee8021QBridgeVlanStaticXTopology_Object = MibTableColumn
ieee8021QBridgeVlanStaticXTopology = _Ieee8021QBridgeVlanStaticXTopology_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 7, 1, 9),
    _Ieee8021QBridgeVlanStaticXTopology_Type()
)
ieee8021QBridgeVlanStaticXTopology.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticXTopology.setStatus("current")
_RadBridgePortVlanTable_Object = MibTable
radBridgePortVlanTable = _RadBridgePortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9)
)
if mibBuilder.loadTexts:
    radBridgePortVlanTable.setStatus("current")
_RadBridgePortVlanEntry_Object = MibTableRow
radBridgePortVlanEntry = _RadBridgePortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9, 1)
)
radBridgePortVlanEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgePortVlanBridgeIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgePortVlanIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgePortVlanPrtIdx"),
)
if mibBuilder.loadTexts:
    radBridgePortVlanEntry.setStatus("current")
_RadBridgePortVlanBridgeIdx_Type = IEEE8021PbbComponentIdentifier
_RadBridgePortVlanBridgeIdx_Object = MibTableColumn
radBridgePortVlanBridgeIdx = _RadBridgePortVlanBridgeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9, 1, 1),
    _RadBridgePortVlanBridgeIdx_Type()
)
radBridgePortVlanBridgeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortVlanBridgeIdx.setStatus("current")
_RadBridgePortVlanIdx_Type = IEEE8021VlanIndex
_RadBridgePortVlanIdx_Object = MibTableColumn
radBridgePortVlanIdx = _RadBridgePortVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9, 1, 2),
    _RadBridgePortVlanIdx_Type()
)
radBridgePortVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortVlanIdx.setStatus("current")
_RadBridgePortVlanPrtIdx_Type = IEEE8021BridgePortNumber
_RadBridgePortVlanPrtIdx_Object = MibTableColumn
radBridgePortVlanPrtIdx = _RadBridgePortVlanPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9, 1, 3),
    _RadBridgePortVlanPrtIdx_Type()
)
radBridgePortVlanPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortVlanPrtIdx.setStatus("current")
_RadBridgePortVlanRowStatus_Type = RowStatus
_RadBridgePortVlanRowStatus_Object = MibTableColumn
radBridgePortVlanRowStatus = _RadBridgePortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9, 1, 4),
    _RadBridgePortVlanRowStatus_Type()
)
radBridgePortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortVlanRowStatus.setStatus("current")


class _RadBridgePortVlanIsRoot_Type(Integer32):
    """Custom type radBridgePortVlanIsRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 2),
          ("no", 3))
    )


_RadBridgePortVlanIsRoot_Type.__name__ = "Integer32"
_RadBridgePortVlanIsRoot_Object = MibTableColumn
radBridgePortVlanIsRoot = _RadBridgePortVlanIsRoot_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 9, 9, 1, 5),
    _RadBridgePortVlanIsRoot_Type()
)
radBridgePortVlanIsRoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radBridgePortVlanIsRoot.setStatus("current")
_RadBridgeStatus_ObjectIdentity = ObjectIdentity
radBridgeStatus = _RadBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10)
)
_RadBridgeInvBasePortTable_Object = MibTable
radBridgeInvBasePortTable = _RadBridgeInvBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    radBridgeInvBasePortTable.setStatus("current")
_RadBridgeInvBasePortEntry_Object = MibTableRow
radBridgeInvBasePortEntry = _RadBridgeInvBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 1, 1)
)
radBridgeInvBasePortEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeInvBasePortIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeInvBasePortEntry.setStatus("current")
_RadBridgeInvBasePortIfIndex_Type = Integer32
_RadBridgeInvBasePortIfIndex_Object = MibTableColumn
radBridgeInvBasePortIfIndex = _RadBridgeInvBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 1, 1, 1),
    _RadBridgeInvBasePortIfIndex_Type()
)
radBridgeInvBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeInvBasePortIfIndex.setStatus("current")
_RadBridgeInvBasePort_Type = Integer32
_RadBridgeInvBasePort_Object = MibTableColumn
radBridgeInvBasePort = _RadBridgeInvBasePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 1, 1, 2),
    _RadBridgeInvBasePort_Type()
)
radBridgeInvBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeInvBasePort.setStatus("current")
_BridgeMacSearchTable_Object = MibTable
bridgeMacSearchTable = _BridgeMacSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2)
)
if mibBuilder.loadTexts:
    bridgeMacSearchTable.setStatus("current")
_BridgeMacSearchEntry_Object = MibTableRow
bridgeMacSearchEntry = _BridgeMacSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1)
)
bridgeMacSearchEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "bridgeMacSearchIdx"),
)
if mibBuilder.loadTexts:
    bridgeMacSearchEntry.setStatus("current")
_BridgeMacSearchIdx_Type = Unsigned32
_BridgeMacSearchIdx_Object = MibTableColumn
bridgeMacSearchIdx = _BridgeMacSearchIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1, 1),
    _BridgeMacSearchIdx_Type()
)
bridgeMacSearchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacSearchIdx.setStatus("current")
_BridgeMacSearchBridgeComponentId_Type = Unsigned32
_BridgeMacSearchBridgeComponentId_Object = MibTableColumn
bridgeMacSearchBridgeComponentId = _BridgeMacSearchBridgeComponentId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1, 2),
    _BridgeMacSearchBridgeComponentId_Type()
)
bridgeMacSearchBridgeComponentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMacSearchBridgeComponentId.setStatus("current")
_BridgeMacSearchAddress_Type = MacAddress
_BridgeMacSearchAddress_Object = MibTableColumn
bridgeMacSearchAddress = _BridgeMacSearchAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1, 3),
    _BridgeMacSearchAddress_Type()
)
bridgeMacSearchAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMacSearchAddress.setStatus("current")
_BridgeMacSearchVlan_Type = Unsigned32
_BridgeMacSearchVlan_Object = MibTableColumn
bridgeMacSearchVlan = _BridgeMacSearchVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1, 4),
    _BridgeMacSearchVlan_Type()
)
bridgeMacSearchVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMacSearchVlan.setStatus("current")
_BridgeMacSearchPort_Type = Unsigned32
_BridgeMacSearchPort_Object = MibTableColumn
bridgeMacSearchPort = _BridgeMacSearchPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1, 5),
    _BridgeMacSearchPort_Type()
)
bridgeMacSearchPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMacSearchPort.setStatus("current")


class _BridgeMacSearchCmdStatus_Type(Integer32):
    """Custom type bridgeMacSearchCmdStatus based on Integer32"""
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
        *(("notApplicable", 1),
          ("startSearch", 2),
          ("macSearching", 3),
          ("macFound", 4),
          ("macNoFound", 5),
          ("failed", 6))
    )


_BridgeMacSearchCmdStatus_Type.__name__ = "Integer32"
_BridgeMacSearchCmdStatus_Object = MibTableColumn
bridgeMacSearchCmdStatus = _BridgeMacSearchCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 2, 1, 6),
    _BridgeMacSearchCmdStatus_Type()
)
bridgeMacSearchCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMacSearchCmdStatus.setStatus("current")
_BridgeMacResultTable_Object = MibTable
bridgeMacResultTable = _BridgeMacResultTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3)
)
if mibBuilder.loadTexts:
    bridgeMacResultTable.setStatus("current")
_BridgeMacResultEntry_Object = MibTableRow
bridgeMacResultEntry = _BridgeMacResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3, 1)
)
bridgeMacResultEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "bridgeMacResultBridgeIdx"),
    (0, "RAD-BrgGen-MIB", "bridgeMacResultVlan"),
    (0, "RAD-BrgGen-MIB", "bridgeMacResultMacAddress"),
)
if mibBuilder.loadTexts:
    bridgeMacResultEntry.setStatus("current")
_BridgeMacResultBridgeIdx_Type = Unsigned32
_BridgeMacResultBridgeIdx_Object = MibTableColumn
bridgeMacResultBridgeIdx = _BridgeMacResultBridgeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3, 1, 1),
    _BridgeMacResultBridgeIdx_Type()
)
bridgeMacResultBridgeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacResultBridgeIdx.setStatus("current")
_BridgeMacResultVlan_Type = Unsigned32
_BridgeMacResultVlan_Object = MibTableColumn
bridgeMacResultVlan = _BridgeMacResultVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3, 1, 2),
    _BridgeMacResultVlan_Type()
)
bridgeMacResultVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacResultVlan.setStatus("current")
_BridgeMacResultMacAddress_Type = MacAddress
_BridgeMacResultMacAddress_Object = MibTableColumn
bridgeMacResultMacAddress = _BridgeMacResultMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3, 1, 3),
    _BridgeMacResultMacAddress_Type()
)
bridgeMacResultMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacResultMacAddress.setStatus("current")
_BridgeMacResultPort_Type = Unsigned32
_BridgeMacResultPort_Object = MibTableColumn
bridgeMacResultPort = _BridgeMacResultPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3, 1, 4),
    _BridgeMacResultPort_Type()
)
bridgeMacResultPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacResultPort.setStatus("current")


class _BridgeMacResultCmdStatus_Type(Integer32):
    """Custom type bridgeMacResultCmdStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_BridgeMacResultCmdStatus_Type.__name__ = "Integer32"
_BridgeMacResultCmdStatus_Object = MibTableColumn
bridgeMacResultCmdStatus = _BridgeMacResultCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 10, 3, 1, 5),
    _BridgeMacResultCmdStatus_Type()
)
bridgeMacResultCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacResultCmdStatus.setStatus("current")
_RadBridgeStp_ObjectIdentity = ObjectIdentity
radBridgeStp = _RadBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11)
)
_RadBridgeStpCnfgTable_Object = MibTable
radBridgeStpCnfgTable = _RadBridgeStpCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    radBridgeStpCnfgTable.setStatus("current")
_RadBridgeStpCnfgEntry_Object = MibTableRow
radBridgeStpCnfgEntry = _RadBridgeStpCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1)
)
radBridgeStpCnfgEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeStpCnfgIdx1"),
    (0, "RAD-BrgGen-MIB", "radBridgeStpCnfgIdx2"),
)
if mibBuilder.loadTexts:
    radBridgeStpCnfgEntry.setStatus("current")


class _RadBridgeStpCnfgIdx1_Type(Integer32):
    """Custom type radBridgeStpCnfgIdx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RadBridgeStpCnfgIdx1_Type.__name__ = "Integer32"
_RadBridgeStpCnfgIdx1_Object = MibTableColumn
radBridgeStpCnfgIdx1 = _RadBridgeStpCnfgIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 1),
    _RadBridgeStpCnfgIdx1_Type()
)
radBridgeStpCnfgIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeStpCnfgIdx1.setStatus("current")
_RadBridgeStpCnfgIdx2_Type = Integer32
_RadBridgeStpCnfgIdx2_Object = MibTableColumn
radBridgeStpCnfgIdx2 = _RadBridgeStpCnfgIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 2),
    _RadBridgeStpCnfgIdx2_Type()
)
radBridgeStpCnfgIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeStpCnfgIdx2.setStatus("current")


class _RadBridgeStpCnfgForwardDelay_Type(Timeout):
    """Custom type radBridgeStpCnfgForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_RadBridgeStpCnfgForwardDelay_Type.__name__ = "Timeout"
_RadBridgeStpCnfgForwardDelay_Object = MibTableColumn
radBridgeStpCnfgForwardDelay = _RadBridgeStpCnfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 3),
    _RadBridgeStpCnfgForwardDelay_Type()
)
radBridgeStpCnfgForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeStpCnfgForwardDelay.setStatus("current")


class _RadBridgeStpCnfgMaxAge_Type(Timeout):
    """Custom type radBridgeStpCnfgMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_RadBridgeStpCnfgMaxAge_Type.__name__ = "Timeout"
_RadBridgeStpCnfgMaxAge_Object = MibTableColumn
radBridgeStpCnfgMaxAge = _RadBridgeStpCnfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 4),
    _RadBridgeStpCnfgMaxAge_Type()
)
radBridgeStpCnfgMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeStpCnfgMaxAge.setStatus("current")


class _RadBridgeStpCnfgHelloTime_Type(Timeout):
    """Custom type radBridgeStpCnfgHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_RadBridgeStpCnfgHelloTime_Type.__name__ = "Timeout"
_RadBridgeStpCnfgHelloTime_Object = MibTableColumn
radBridgeStpCnfgHelloTime = _RadBridgeStpCnfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 5),
    _RadBridgeStpCnfgHelloTime_Type()
)
radBridgeStpCnfgHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeStpCnfgHelloTime.setStatus("current")


class _RadBridgeStpCnfgPriority_Type(Integer32):
    """Custom type radBridgeStpCnfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadBridgeStpCnfgPriority_Type.__name__ = "Integer32"
_RadBridgeStpCnfgPriority_Object = MibTableColumn
radBridgeStpCnfgPriority = _RadBridgeStpCnfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 6),
    _RadBridgeStpCnfgPriority_Type()
)
radBridgeStpCnfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeStpCnfgPriority.setStatus("current")


class _RadBridgeStpCnfgStpVersion_Type(Integer32):
    """Custom type radBridgeStpCnfgStpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("stp", 2),
          ("rstp", 3))
    )


_RadBridgeStpCnfgStpVersion_Type.__name__ = "Integer32"
_RadBridgeStpCnfgStpVersion_Object = MibTableColumn
radBridgeStpCnfgStpVersion = _RadBridgeStpCnfgStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 1, 1, 7),
    _RadBridgeStpCnfgStpVersion_Type()
)
radBridgeStpCnfgStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeStpCnfgStpVersion.setStatus("current")
_RadBridgeStpStatTable_Object = MibTable
radBridgeStpStatTable = _RadBridgeStpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2)
)
if mibBuilder.loadTexts:
    radBridgeStpStatTable.setStatus("current")
_RadBridgeStpStatEntry_Object = MibTableRow
radBridgeStpStatEntry = _RadBridgeStpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1)
)
radBridgeStpStatEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgeStpStatIdx"),
)
if mibBuilder.loadTexts:
    radBridgeStpStatEntry.setStatus("current")
_RadBridgeStpStatIdx_Type = Integer32
_RadBridgeStpStatIdx_Object = MibTableColumn
radBridgeStpStatIdx = _RadBridgeStpStatIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1, 1),
    _RadBridgeStpStatIdx_Type()
)
radBridgeStpStatIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgeStpStatIdx.setStatus("current")
_RadBridgeStpStatForwardDelay_Type = Timeout
_RadBridgeStpStatForwardDelay_Object = MibTableColumn
radBridgeStpStatForwardDelay = _RadBridgeStpStatForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1, 2),
    _RadBridgeStpStatForwardDelay_Type()
)
radBridgeStpStatForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeStpStatForwardDelay.setStatus("current")
_RadBridgeStpStatMaxAge_Type = Timeout
_RadBridgeStpStatMaxAge_Object = MibTableColumn
radBridgeStpStatMaxAge = _RadBridgeStpStatMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1, 3),
    _RadBridgeStpStatMaxAge_Type()
)
radBridgeStpStatMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeStpStatMaxAge.setStatus("current")
_RadBridgeStpStatHelloTime_Type = Timeout
_RadBridgeStpStatHelloTime_Object = MibTableColumn
radBridgeStpStatHelloTime = _RadBridgeStpStatHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1, 4),
    _RadBridgeStpStatHelloTime_Type()
)
radBridgeStpStatHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeStpStatHelloTime.setStatus("current")
_RadBridgeStpStatDesignatedRoot_Type = BridgeId
_RadBridgeStpStatDesignatedRoot_Object = MibTableColumn
radBridgeStpStatDesignatedRoot = _RadBridgeStpStatDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1, 5),
    _RadBridgeStpStatDesignatedRoot_Type()
)
radBridgeStpStatDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeStpStatDesignatedRoot.setStatus("current")
_RadBridgeStpStatRootCost_Type = Integer32
_RadBridgeStpStatRootCost_Object = MibTableColumn
radBridgeStpStatRootCost = _RadBridgeStpStatRootCost_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 2, 1, 6),
    _RadBridgeStpStatRootCost_Type()
)
radBridgeStpStatRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeStpStatRootCost.setStatus("current")
_Ieee8021MstpXTable_Object = MibTable
ieee8021MstpXTable = _Ieee8021MstpXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 3)
)
if mibBuilder.loadTexts:
    ieee8021MstpXTable.setStatus("current")
_Ieee8021MstpXEntry_Object = MibTableRow
ieee8021MstpXEntry = _Ieee8021MstpXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021MstpXEntry.setStatus("current")


class _Ieee8021MstpXVids0_Type(OctetString):
    """Custom type ieee8021MstpXVids0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_Ieee8021MstpXVids0_Type.__name__ = "OctetString"
_Ieee8021MstpXVids0_Object = MibTableColumn
ieee8021MstpXVids0 = _Ieee8021MstpXVids0_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 3, 1, 1),
    _Ieee8021MstpXVids0_Type()
)
ieee8021MstpXVids0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MstpXVids0.setStatus("current")


class _Ieee8021MstpXVids1_Type(OctetString):
    """Custom type ieee8021MstpXVids1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_Ieee8021MstpXVids1_Type.__name__ = "OctetString"
_Ieee8021MstpXVids1_Object = MibTableColumn
ieee8021MstpXVids1 = _Ieee8021MstpXVids1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 3, 1, 2),
    _Ieee8021MstpXVids1_Type()
)
ieee8021MstpXVids1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MstpXVids1.setStatus("current")


class _Ieee8021MstpXVids2_Type(OctetString):
    """Custom type ieee8021MstpXVids2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_Ieee8021MstpXVids2_Type.__name__ = "OctetString"
_Ieee8021MstpXVids2_Object = MibTableColumn
ieee8021MstpXVids2 = _Ieee8021MstpXVids2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 3, 1, 3),
    _Ieee8021MstpXVids2_Type()
)
ieee8021MstpXVids2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MstpXVids2.setStatus("current")


class _Ieee8021MstpXVids3_Type(OctetString):
    """Custom type ieee8021MstpXVids3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_Ieee8021MstpXVids3_Type.__name__ = "OctetString"
_Ieee8021MstpXVids3_Object = MibTableColumn
ieee8021MstpXVids3 = _Ieee8021MstpXVids3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 11, 3, 1, 4),
    _Ieee8021MstpXVids3_Type()
)
ieee8021MstpXVids3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MstpXVids3.setStatus("current")


class _RadBridgeForwardingMode_Type(Integer32):
    """Custom type radBridgeForwardingMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("transparent", 2),
          ("filter", 3),
          ("filterTagged", 4),
          ("transparentTagged", 5))
    )


_RadBridgeForwardingMode_Type.__name__ = "Integer32"
_RadBridgeForwardingMode_Object = MibScalar
radBridgeForwardingMode = _RadBridgeForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 12),
    _RadBridgeForwardingMode_Type()
)
radBridgeForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeForwardingMode.setStatus("current")
_RadBridgePort_ObjectIdentity = ObjectIdentity
radBridgePort = _RadBridgePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13)
)
_RadBridgePortCnfgTable_Object = MibTable
radBridgePortCnfgTable = _RadBridgePortCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    radBridgePortCnfgTable.setStatus("current")
_RadBridgePortCnfgEntry_Object = MibTableRow
radBridgePortCnfgEntry = _RadBridgePortCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1)
)
radBridgePortCnfgEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "radBridgePortCnfgIdx"),
    (0, "RAD-BrgGen-MIB", "radBridgePortCnfgPrtIdx"),
)
if mibBuilder.loadTexts:
    radBridgePortCnfgEntry.setStatus("current")
_RadBridgePortCnfgIdx_Type = Integer32
_RadBridgePortCnfgIdx_Object = MibTableColumn
radBridgePortCnfgIdx = _RadBridgePortCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 1),
    _RadBridgePortCnfgIdx_Type()
)
radBridgePortCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortCnfgIdx.setStatus("current")
_RadBridgePortCnfgPrtIdx_Type = Integer32
_RadBridgePortCnfgPrtIdx_Object = MibTableColumn
radBridgePortCnfgPrtIdx = _RadBridgePortCnfgPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 2),
    _RadBridgePortCnfgPrtIdx_Type()
)
radBridgePortCnfgPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radBridgePortCnfgPrtIdx.setStatus("current")
_RadBridgePortCnfgMaxMacAddr_Type = Integer32
_RadBridgePortCnfgMaxMacAddr_Object = MibTableColumn
radBridgePortCnfgMaxMacAddr = _RadBridgePortCnfgMaxMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 3),
    _RadBridgePortCnfgMaxMacAddr_Type()
)
radBridgePortCnfgMaxMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgMaxMacAddr.setStatus("current")


class _RadBridgePortCnfgMngFlow_Type(Integer32):
    """Custom type radBridgePortCnfgMngFlow based on Integer32"""
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


_RadBridgePortCnfgMngFlow_Type.__name__ = "Integer32"
_RadBridgePortCnfgMngFlow_Object = MibTableColumn
radBridgePortCnfgMngFlow = _RadBridgePortCnfgMngFlow_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 4),
    _RadBridgePortCnfgMngFlow_Type()
)
radBridgePortCnfgMngFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgMngFlow.setStatus("current")


class _RadBridgePortCnfgMcastMode_Type(Integer32):
    """Custom type radBridgePortCnfgMcastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("forwarding", 2))
    )


_RadBridgePortCnfgMcastMode_Type.__name__ = "Integer32"
_RadBridgePortCnfgMcastMode_Object = MibTableColumn
radBridgePortCnfgMcastMode = _RadBridgePortCnfgMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 5),
    _RadBridgePortCnfgMcastMode_Type()
)
radBridgePortCnfgMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgMcastMode.setStatus("current")
_RadBridgePortCnfgDefaultVpi_Type = Integer32
_RadBridgePortCnfgDefaultVpi_Object = MibTableColumn
radBridgePortCnfgDefaultVpi = _RadBridgePortCnfgDefaultVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 6),
    _RadBridgePortCnfgDefaultVpi_Type()
)
radBridgePortCnfgDefaultVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgDefaultVpi.setStatus("current")
_RadBridgePortCnfgDefaultVci_Type = Integer32
_RadBridgePortCnfgDefaultVci_Object = MibTableColumn
radBridgePortCnfgDefaultVci = _RadBridgePortCnfgDefaultVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 7),
    _RadBridgePortCnfgDefaultVci_Type()
)
radBridgePortCnfgDefaultVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgDefaultVci.setStatus("current")
_RadBridgePortCnfgStatVlanId_Type = Integer32
_RadBridgePortCnfgStatVlanId_Object = MibTableColumn
radBridgePortCnfgStatVlanId = _RadBridgePortCnfgStatVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 8),
    _RadBridgePortCnfgStatVlanId_Type()
)
radBridgePortCnfgStatVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgStatVlanId.setStatus("current")
_RadBridgePortCnfgIngressMtu_Type = Integer32
_RadBridgePortCnfgIngressMtu_Object = MibTableColumn
radBridgePortCnfgIngressMtu = _RadBridgePortCnfgIngressMtu_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 9),
    _RadBridgePortCnfgIngressMtu_Type()
)
radBridgePortCnfgIngressMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgIngressMtu.setStatus("current")
_RadBridgePortCnfgEgressMtu_Type = Integer32
_RadBridgePortCnfgEgressMtu_Object = MibTableColumn
radBridgePortCnfgEgressMtu = _RadBridgePortCnfgEgressMtu_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 10),
    _RadBridgePortCnfgEgressMtu_Type()
)
radBridgePortCnfgEgressMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgEgressMtu.setStatus("current")


class _RadBridgePortCnfgDot1x_Type(Integer32):
    """Custom type radBridgePortCnfgDot1x based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_RadBridgePortCnfgDot1x_Type.__name__ = "Integer32"
_RadBridgePortCnfgDot1x_Object = MibTableColumn
radBridgePortCnfgDot1x = _RadBridgePortCnfgDot1x_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 11),
    _RadBridgePortCnfgDot1x_Type()
)
radBridgePortCnfgDot1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgDot1x.setStatus("current")
_RadBridgePortCnfgMappingProfile_Type = Integer32
_RadBridgePortCnfgMappingProfile_Object = MibTableColumn
radBridgePortCnfgMappingProfile = _RadBridgePortCnfgMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 13, 1, 1, 12),
    _RadBridgePortCnfgMappingProfile_Type()
)
radBridgePortCnfgMappingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgePortCnfgMappingProfile.setStatus("current")
_Ieee8021BridgeBaseXTable_Object = MibTable
ieee8021BridgeBaseXTable = _Ieee8021BridgeBaseXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 14)
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseXTable.setStatus("current")
_Ieee8021BridgeBaseXEntry_Object = MibTableRow
ieee8021BridgeBaseXEntry = _Ieee8021BridgeBaseXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseXEntry.setStatus("current")


class _Ieee8021BridgeBaseXForwardingMode_Type(Integer32):
    """Custom type ieee8021BridgeBaseXForwardingMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("transparent", 2),
          ("filter", 3),
          ("filterTagged", 4),
          ("transparentTagged", 5))
    )


_Ieee8021BridgeBaseXForwardingMode_Type.__name__ = "Integer32"
_Ieee8021BridgeBaseXForwardingMode_Object = MibTableColumn
ieee8021BridgeBaseXForwardingMode = _Ieee8021BridgeBaseXForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 14, 1, 1),
    _Ieee8021BridgeBaseXForwardingMode_Type()
)
ieee8021BridgeBaseXForwardingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseXForwardingMode.setStatus("current")


class _Ieee8021BridgeBaseXName_Type(SnmpAdminString):
    """Custom type ieee8021BridgeBaseXName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Ieee8021BridgeBaseXName_Type.__name__ = "SnmpAdminString"
_Ieee8021BridgeBaseXName_Object = MibTableColumn
ieee8021BridgeBaseXName = _Ieee8021BridgeBaseXName_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 14, 1, 2),
    _Ieee8021BridgeBaseXName_Type()
)
ieee8021BridgeBaseXName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseXName.setStatus("current")
_Invieee8021QBridgeVlanCurrentTable_Object = MibTable
invieee8021QBridgeVlanCurrentTable = _Invieee8021QBridgeVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 15)
)
if mibBuilder.loadTexts:
    invieee8021QBridgeVlanCurrentTable.setStatus("current")
_Invieee8021QBridgeVlanCurrentEntry_Object = MibTableRow
invieee8021QBridgeVlanCurrentEntry = _Invieee8021QBridgeVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 15, 1)
)
invieee8021QBridgeVlanCurrentEntry.setIndexNames(
    (0, "RAD-BrgGen-MIB", "invieee8021QBridgeVlanCurrentComponentId"),
    (0, "RAD-BrgGen-MIB", "invieee8021QBridgeVlanFdbId"),
    (0, "RAD-BrgGen-MIB", "invieee8021QBridgeVlanTimeMark"),
)
if mibBuilder.loadTexts:
    invieee8021QBridgeVlanCurrentEntry.setStatus("current")
_Invieee8021QBridgeVlanCurrentComponentId_Type = IEEE8021PbbComponentIdentifier
_Invieee8021QBridgeVlanCurrentComponentId_Object = MibTableColumn
invieee8021QBridgeVlanCurrentComponentId = _Invieee8021QBridgeVlanCurrentComponentId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 15, 1, 1),
    _Invieee8021QBridgeVlanCurrentComponentId_Type()
)
invieee8021QBridgeVlanCurrentComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invieee8021QBridgeVlanCurrentComponentId.setStatus("current")
_Invieee8021QBridgeVlanFdbId_Type = Unsigned32
_Invieee8021QBridgeVlanFdbId_Object = MibTableColumn
invieee8021QBridgeVlanFdbId = _Invieee8021QBridgeVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 15, 1, 2),
    _Invieee8021QBridgeVlanFdbId_Type()
)
invieee8021QBridgeVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invieee8021QBridgeVlanFdbId.setStatus("current")
_Invieee8021QBridgeVlanTimeMark_Type = TimeFilter
_Invieee8021QBridgeVlanTimeMark_Object = MibTableColumn
invieee8021QBridgeVlanTimeMark = _Invieee8021QBridgeVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 15, 1, 3),
    _Invieee8021QBridgeVlanTimeMark_Type()
)
invieee8021QBridgeVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invieee8021QBridgeVlanTimeMark.setStatus("current")
_Invieee8021QBridgeVlanIndex_Type = IEEE8021VlanIndex
_Invieee8021QBridgeVlanIndex_Object = MibTableColumn
invieee8021QBridgeVlanIndex = _Invieee8021QBridgeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 15, 1, 4),
    _Invieee8021QBridgeVlanIndex_Type()
)
invieee8021QBridgeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invieee8021QBridgeVlanIndex.setStatus("current")
dot1qVlanStaticEntry.registerAugmentions(
    ("RAD-BrgGen-MIB",
     "radBridgeDot1qVlanStaticEntry")
)
radBridgeDot1qVlanStaticEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("RAD-BrgGen-MIB",
     "radDot1qPortVlanEntry")
)
radDot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
ieee8021QBridgeVlanStaticEntry.registerAugmentions(
    ("RAD-BrgGen-MIB",
     "ieee8021QBridgeVlanStaticXEntry")
)
ieee8021QBridgeVlanStaticXEntry.setIndexNames(*ieee8021QBridgeVlanStaticEntry.getIndexNames())
ieee8021MstpEntry.registerAugmentions(
    ("RAD-BrgGen-MIB",
     "ieee8021MstpXEntry")
)
ieee8021MstpXEntry.setIndexNames(*ieee8021MstpEntry.getIndexNames())
ieee8021BridgeBaseEntry.registerAugmentions(
    ("RAD-BrgGen-MIB",
     "ieee8021BridgeBaseXEntry")
)
ieee8021BridgeBaseXEntry.setIndexNames(*ieee8021BridgeBaseEntry.getIndexNames())

# Managed Objects groups


# Notification objects

bridgeSpanningTreeNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 4, 0, 1)
)
bridgeSpanningTreeNewRoot.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-BrgGen-MIB", "ieee8021BridgeBaseXName"))
)
if mibBuilder.loadTexts:
    bridgeSpanningTreeNewRoot.setStatus(
        "current"
    )

bridgeSpanningTreeTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 4, 0, 2)
)
bridgeSpanningTreeTopologyChange.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-BrgGen-MIB", "ieee8021BridgeBaseXName"))
)
if mibBuilder.loadTexts:
    bridgeSpanningTreeTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-BrgGen-MIB",
    **{"TagHandlingType": TagHandlingType,
       "BridgeTopology": BridgeTopology,
       "GenAddress": GenAddress,
       "genBridgeEvents": genBridgeEvents,
       "bridgeSpanningTreeNewRoot": bridgeSpanningTreeNewRoot,
       "bridgeSpanningTreeTopologyChange": bridgeSpanningTreeTopologyChange,
       "genBridge": genBridge,
       "radBridgeAction": radBridgeAction,
       "radBridgeInactiveArpTimeOut": radBridgeInactiveArpTimeOut,
       "radBridgeMaskTable": radBridgeMaskTable,
       "radBridgeMaskEntry": radBridgeMaskEntry,
       "radBridgeMaskType": radBridgeMaskType,
       "radBridgeMaskIfIndex": radBridgeMaskIfIndex,
       "radBridgeMaskNum": radBridgeMaskNum,
       "radBridgeMaskDest": radBridgeMaskDest,
       "radBridgeMaskPat1": radBridgeMaskPat1,
       "radBridgeMaskActiveBit1": radBridgeMaskActiveBit1,
       "radBridgeMaskFrom1": radBridgeMaskFrom1,
       "radBridgeMaskOffset1": radBridgeMaskOffset1,
       "radBridgeMaskCond1": radBridgeMaskCond1,
       "radBridgeMaskPat2": radBridgeMaskPat2,
       "radBridgeMaskActiveBit2": radBridgeMaskActiveBit2,
       "radBridgeMaskFrom2": radBridgeMaskFrom2,
       "radBridgeMaskOffset2": radBridgeMaskOffset2,
       "radBridgeMaskCond2": radBridgeMaskCond2,
       "radBridgeMaskPat3": radBridgeMaskPat3,
       "radBridgeMaskActiveBit3": radBridgeMaskActiveBit3,
       "radBridgeMaskFrom3": radBridgeMaskFrom3,
       "radBridgeMaskOffset3": radBridgeMaskOffset3,
       "radBridgeMaskCond3": radBridgeMaskCond3,
       "radBridgeMaskOper": radBridgeMaskOper,
       "radBridgeCOD": radBridgeCOD,
       "radBridgeCODParamTable": radBridgeCODParamTable,
       "radBridgeCODEntry": radBridgeCODEntry,
       "radBridgeCODIfIndex": radBridgeCODIfIndex,
       "radBridgeCODManualConnect": radBridgeCODManualConnect,
       "radBridgeCODMode": radBridgeCODMode,
       "radBridgeCODConnectDelay": radBridgeCODConnectDelay,
       "radBridgeCODisConnectDelay": radBridgeCODisConnectDelay,
       "radBridgeCODImplicitSwitch": radBridgeCODImplicitSwitch,
       "radBridgeCODNumAccess": radBridgeCODNumAccess,
       "radBridgeCODTotalConnecTime": radBridgeCODTotalConnecTime,
       "radBridgeCODTimeTriggerTable": radBridgeCODTimeTriggerTable,
       "radBridgeCODTimeTriggerEntry": radBridgeCODTimeTriggerEntry,
       "radBridgeCODTimeIfIndex": radBridgeCODTimeIfIndex,
       "radBridgeCODDay": radBridgeCODDay,
       "radBridgeCODTimeTriggerNum": radBridgeCODTimeTriggerNum,
       "radBridgeCODTimeTriggerFrom": radBridgeCODTimeTriggerFrom,
       "radBridgeCODTimeTriggerTo": radBridgeCODTimeTriggerTo,
       "radBridgeCODTimeTriggerStatus": radBridgeCODTimeTriggerStatus,
       "radBridgeCODTraffic": radBridgeCODTraffic,
       "radBridgeCODTrafficTable": radBridgeCODTrafficTable,
       "radBridgeCODTrafficEntry": radBridgeCODTrafficEntry,
       "radBridgeCODProtocolType": radBridgeCODProtocolType,
       "radBridgeCODTrafficTriggerStatus": radBridgeCODTrafficTriggerStatus,
       "radBridgeCODRemoteIPAddr": radBridgeCODRemoteIPAddr,
       "radBridgeCODIPMask": radBridgeCODIPMask,
       "radBridgeCODTrafficTriggerProtType": radBridgeCODTrafficTriggerProtType,
       "radBridgeCODCondTable": radBridgeCODCondTable,
       "radBridgeCODCondEntry": radBridgeCODCondEntry,
       "radBridgeCODCondIfIndex": radBridgeCODCondIfIndex,
       "radBridgeCODOriginateConnectCondition": radBridgeCODOriginateConnectCondition,
       "radBridgeCODOriginateDisConnectCondition": radBridgeCODOriginateDisConnectCondition,
       "radBridgeCODOriginateDisConnectDelay": radBridgeCODOriginateDisConnectDelay,
       "radBridgeCODAnswerConnectCondition": radBridgeCODAnswerConnectCondition,
       "radBridgeCODSpecificOnTrafficOIDCondition": radBridgeCODSpecificOnTrafficOIDCondition,
       "radBridgeCODDisConnectMinimunFramesNumber": radBridgeCODDisConnectMinimunFramesNumber,
       "radBridgeIPX": radBridgeIPX,
       "radBridgeIPXdriver": radBridgeIPXdriver,
       "radBridgeIPXForwarding": radBridgeIPXForwarding,
       "radBridgeIPXRip": radBridgeIPXRip,
       "radBridgeIPXRipOutPackets": radBridgeIPXRipOutPackets,
       "radBridgeIPXRipInPackets": radBridgeIPXRipInPackets,
       "radBridgeIPXRipInDiscards": radBridgeIPXRipInDiscards,
       "radBridgeIPXRipTblNoOfEntries": radBridgeIPXRipTblNoOfEntries,
       "radBridgeIPXRipTblBcastTrigUpdateInterval": radBridgeIPXRipTblBcastTrigUpdateInterval,
       "radBridgeIPXRipTable": radBridgeIPXRipTable,
       "radBridgeIPXRipTableEntry": radBridgeIPXRipTableEntry,
       "radBridgeIPXRipDestNetwork": radBridgeIPXRipDestNetwork,
       "radBridgeIPXRipPolicy": radBridgeIPXRipPolicy,
       "radBridgeIPXRipForwardingRouter": radBridgeIPXRipForwardingRouter,
       "radBridgeIPXRipNIC": radBridgeIPXRipNIC,
       "radBridgeIPXRipTickMetric": radBridgeIPXRipTickMetric,
       "radBridgeIPXRipHopMetric": radBridgeIPXRipHopMetric,
       "radBridgeIPXRipAgingTime": radBridgeIPXRipAgingTime,
       "radBridgeIPXRipValueStatus": radBridgeIPXRipValueStatus,
       "radBridgeIPXRipForwardType": radBridgeIPXRipForwardType,
       "radBridgeIPXRipInfTable": radBridgeIPXRipInfTable,
       "radBridgeIPXRipInfEntry": radBridgeIPXRipInfEntry,
       "radBridgeIPXRipInfIfIndex": radBridgeIPXRipInfIfIndex,
       "radBridgeIPXRipInfBcastUpdate": radBridgeIPXRipInfBcastUpdate,
       "radBridgeIPXRipInfAgeMultiplier": radBridgeIPXRipInfAgeMultiplier,
       "radBridgeIPXSap": radBridgeIPXSap,
       "radBridgeIPXSapOutPackets": radBridgeIPXSapOutPackets,
       "radBridgeIPXSapInPackets": radBridgeIPXSapInPackets,
       "radBridgeIPXSapInDiscards": radBridgeIPXSapInDiscards,
       "radBridgeIPXSapTblNoOfEntries": radBridgeIPXSapTblNoOfEntries,
       "radBridgeIPXSapTblBcastTrigUpdateInterval": radBridgeIPXSapTblBcastTrigUpdateInterval,
       "radBridgeIPXSapTable": radBridgeIPXSapTable,
       "radBridgeIPXSapTableEntry": radBridgeIPXSapTableEntry,
       "radBridgeIPXSapServerType": radBridgeIPXSapServerType,
       "radBridgeIPXSapName": radBridgeIPXSapName,
       "radBridgeIPXSapNetwork": radBridgeIPXSapNetwork,
       "radBridgeIPXSapNode": radBridgeIPXSapNode,
       "radBridgeIPXSapSocket": radBridgeIPXSapSocket,
       "radBridgeIPXSapHopsToServer": radBridgeIPXSapHopsToServer,
       "radBridgeIPXSapNIC": radBridgeIPXSapNIC,
       "radBridgeIPXSapAgingTime": radBridgeIPXSapAgingTime,
       "radBridgeIPXSapStatus": radBridgeIPXSapStatus,
       "radBridgeIPXSapInfTable": radBridgeIPXSapInfTable,
       "radBridgeIPXSapInfEntry": radBridgeIPXSapInfEntry,
       "radBridgeIPXSapInfIfIndex": radBridgeIPXSapInfIfIndex,
       "radBridgeIPXSapInfBcastUpdate": radBridgeIPXSapInfBcastUpdate,
       "radBridgeIPXSapInfAgeMultiplier": radBridgeIPXSapInfAgeMultiplier,
       "newMasking": newMasking,
       "maskingMaxEntries": maskingMaxEntries,
       "maskingCurrentEntries": maskingCurrentEntries,
       "maskingTable": maskingTable,
       "maskingEntry": maskingEntry,
       "maskingType": maskingType,
       "maskingIfIndex": maskingIfIndex,
       "maskingIndex": maskingIndex,
       "maskingProtocolType": maskingProtocolType,
       "maskingSmartMaskOID": maskingSmartMaskOID,
       "maskingFrameType": maskingFrameType,
       "maskingFrameTypeCondition": maskingFrameTypeCondition,
       "maskingSourceAddress": maskingSourceAddress,
       "maskingSourceActiveBits": maskingSourceActiveBits,
       "maskingSourceMacOrNet": maskingSourceMacOrNet,
       "maskingSourceCondition": maskingSourceCondition,
       "maskingDestAddress": maskingDestAddress,
       "maskingDestActiveBits": maskingDestActiveBits,
       "maskingDestMacOrNet": maskingDestMacOrNet,
       "maskingDestCondition": maskingDestCondition,
       "maskingLowLevelProt": maskingLowLevelProt,
       "maskingLowLevelProtCondition": maskingLowLevelProtCondition,
       "maskingHighLevelProt": maskingHighLevelProt,
       "maskingHighLevelProtCondition": maskingHighLevelProtCondition,
       "maskingPortNum": maskingPortNum,
       "maskingPortNumCondition": maskingPortNumCondition,
       "maskingOperation": maskingOperation,
       "maskingSrcPortNum": maskingSrcPortNum,
       "maskingSrcPortNumCondition": maskingSrcPortNumCondition,
       "radBridgePerformance": radBridgePerformance,
       "radBridgeCurrentTable": radBridgeCurrentTable,
       "radBridgeCurrentEntry": radBridgeCurrentEntry,
       "radBridgeCurrentIndex": radBridgeCurrentIndex,
       "radBridgeCurrentIngressFilteringDiscardedFrames": radBridgeCurrentIngressFilteringDiscardedFrames,
       "radBridgeCurrentFrameTypeDiscardedFrames": radBridgeCurrentFrameTypeDiscardedFrames,
       "radBridgeCurrentRxCorrectFrames": radBridgeCurrentRxCorrectFrames,
       "radBridgeCurrentRxCorrectBytes": radBridgeCurrentRxCorrectBytes,
       "radBridgeCurrentRxCorrectBytesHCOverflow": radBridgeCurrentRxCorrectBytesHCOverflow,
       "radBridgeCurrentRxBcastFrames": radBridgeCurrentRxBcastFrames,
       "radBridgeCurrentRxMcastFrames": radBridgeCurrentRxMcastFrames,
       "radBridgeCurrentTxCorrectFrames": radBridgeCurrentTxCorrectFrames,
       "radBridgeCurrentTxCorrectBytes": radBridgeCurrentTxCorrectBytes,
       "radBridgeCurrentTxCorrectBytesHCOverflow": radBridgeCurrentTxCorrectBytesHCOverflow,
       "radBridgeCurrentTxBcastFrames": radBridgeCurrentTxBcastFrames,
       "radBridgeCurrentTxMcastFrames": radBridgeCurrentTxMcastFrames,
       "radBridgeCurrentTxDropFrames": radBridgeCurrentTxDropFrames,
       "radBridgeIntervalTable": radBridgeIntervalTable,
       "radBridgeIntervalEntry": radBridgeIntervalEntry,
       "radBridgeIntervalIndex": radBridgeIntervalIndex,
       "radBridgeIntervalNumber": radBridgeIntervalNumber,
       "radBridgeIntervalIngressFilteringDiscardedFrames": radBridgeIntervalIngressFilteringDiscardedFrames,
       "radBridgeIntervalFrameTypeDiscardedFrames": radBridgeIntervalFrameTypeDiscardedFrames,
       "radBridgeIntervalRxCorrectFrames": radBridgeIntervalRxCorrectFrames,
       "radBridgeIntervalRxCorrectBytes": radBridgeIntervalRxCorrectBytes,
       "radBridgeIntervalRxCorrectBytesHCOverflow": radBridgeIntervalRxCorrectBytesHCOverflow,
       "radBridgeIntervalRxBcastFrames": radBridgeIntervalRxBcastFrames,
       "radBridgeIntervalRxMcastFrames": radBridgeIntervalRxMcastFrames,
       "radBridgeIntervalTxCorrectFrames": radBridgeIntervalTxCorrectFrames,
       "radBridgeIntervalTxCorrectBytes": radBridgeIntervalTxCorrectBytes,
       "radBridgeIntervalTxCorrectBytesHCOverflow": radBridgeIntervalTxCorrectBytesHCOverflow,
       "radBridgeIntervalTxBcastFrames": radBridgeIntervalTxBcastFrames,
       "radBridgeIntervalTxMcastFrames": radBridgeIntervalTxMcastFrames,
       "radBridgeIntervalTxDropFrames": radBridgeIntervalTxDropFrames,
       "radBridgePortBaseVlan": radBridgePortBaseVlan,
       "radBridgePortBaseVlanTable": radBridgePortBaseVlanTable,
       "radBridgePortBaseVlanEntry": radBridgePortBaseVlanEntry,
       "radBridgePortBaseVlanCnfgIdx": radBridgePortBaseVlanCnfgIdx,
       "radBridgePortBaseVlanIdx": radBridgePortBaseVlanIdx,
       "radBridgePortBaseVlanName": radBridgePortBaseVlanName,
       "radBridgePortBaseVlanEgressPorts": radBridgePortBaseVlanEgressPorts,
       "radBridgePortBaseVlanVirtualGroups": radBridgePortBaseVlanVirtualGroups,
       "radBridgePortBaseVlanRowStatus": radBridgePortBaseVlanRowStatus,
       "radBridgePortBaseVlanMng": radBridgePortBaseVlanMng,
       "radBridgePortVlanMemberTable": radBridgePortVlanMemberTable,
       "radBridgePortVlanMemberEntry": radBridgePortVlanMemberEntry,
       "radBridgePortVlanMemberBridgeIdx": radBridgePortVlanMemberBridgeIdx,
       "radBridgePortVlanMemberPortIdx": radBridgePortVlanMemberPortIdx,
       "radBridgePortVlanMemberVlanId": radBridgePortVlanMemberVlanId,
       "radBridgePortVlanMemberRowStatus": radBridgePortVlanMemberRowStatus,
       "radBridgeGenCnfg": radBridgeGenCnfg,
       "radBridgeGenFlowTable": radBridgeGenFlowTable,
       "radBridgeGenFlowEntry": radBridgeGenFlowEntry,
       "radBridgeGenFlowCnfgIdx": radBridgeGenFlowCnfgIdx,
       "radBridgeGenFlowIdx": radBridgeGenFlowIdx,
       "radBridgeGenFlowRowStatus": radBridgeGenFlowRowStatus,
       "radBridgeGenFlowFloodOrBcastMaxRate": radBridgeGenFlowFloodOrBcastMaxRate,
       "radBridgeGenFlowQosMode": radBridgeGenFlowQosMode,
       "radBridgeGenFlowSchedulingMode": radBridgeGenFlowSchedulingMode,
       "radBridgeGenFlowBasicClassification": radBridgeGenFlowBasicClassification,
       "radBridgeGenFlowMulticastTrafficClass": radBridgeGenFlowMulticastTrafficClass,
       "radBridgeGenFlowBroadcastTrafficClass": radBridgeGenFlowBroadcastTrafficClass,
       "radBridgeGenFlowUnkownUnicastTrafficClass": radBridgeGenFlowUnkownUnicastTrafficClass,
       "radBridgeDot1qVlanStaticTable": radBridgeDot1qVlanStaticTable,
       "radBridgeDot1qVlanStaticEntry": radBridgeDot1qVlanStaticEntry,
       "radBridgeDot1qVlanTaggedPorts": radBridgeDot1qVlanTaggedPorts,
       "radBridgeDot1qVlanUnmodifiedPorts": radBridgeDot1qVlanUnmodifiedPorts,
       "radBridgeDot1qVlanSplitHorizon": radBridgeDot1qVlanSplitHorizon,
       "radBridgeDot1qVlanRingMembers": radBridgeDot1qVlanRingMembers,
       "radDot1qPortVlanTable": radDot1qPortVlanTable,
       "radDot1qPortVlanEntry": radDot1qPortVlanEntry,
       "radDot1qPortStacking": radDot1qPortStacking,
       "radDot1qPortCopyOriginVlanPriority": radDot1qPortCopyOriginVlanPriority,
       "radDot1qPortDefaultVlanPriority": radDot1qPortDefaultVlanPriority,
       "radDot1qPortTagStripping": radDot1qPortTagStripping,
       "radDot1qPortEgressTagHandling": radDot1qPortEgressTagHandling,
       "radDot1qPortIngressTagHandling": radDot1qPortIngressTagHandling,
       "radDot1qPortReplaceVlanPriority": radDot1qPortReplaceVlanPriority,
       "radDot1qPortVlanEthType": radDot1qPortVlanEthType,
       "radDot1qPortVlanCnodeLevel1Agent": radDot1qPortVlanCnodeLevel1Agent,
       "radBridgeGenCfgTable": radBridgeGenCfgTable,
       "radBridgeGenCfgEntry": radBridgeGenCfgEntry,
       "radBridgeGenCfgIdx": radBridgeGenCfgIdx,
       "radBridgeGenCfgIdx2": radBridgeGenCfgIdx2,
       "radBridgeGenCfgBridgeAction": radBridgeGenCfgBridgeAction,
       "radBridgeAgingTimeSec": radBridgeAgingTimeSec,
       "radBridgeMngVlanId": radBridgeMngVlanId,
       "radBridgeLoopDetectVlanId": radBridgeLoopDetectVlanId,
       "radBridgeSplitHorizon": radBridgeSplitHorizon,
       "radBridgeEthType": radBridgeEthType,
       "radBridgeTopology": radBridgeTopology,
       "radBridgeAgingTime": radBridgeAgingTime,
       "radBridgeMngFlow": radBridgeMngFlow,
       "ieee8021QBridgeVlanStaticXTable": ieee8021QBridgeVlanStaticXTable,
       "ieee8021QBridgeVlanStaticXEntry": ieee8021QBridgeVlanStaticXEntry,
       "ieee8021QBridgeVlanStaticXSplitHorizon": ieee8021QBridgeVlanStaticXSplitHorizon,
       "ieee8021QBridgeVlanStaticXRingMembers": ieee8021QBridgeVlanStaticXRingMembers,
       "ieee8021QBridgeVlanStaticXMaxMacAddr": ieee8021QBridgeVlanStaticXMaxMacAddr,
       "ieee8021QBridgeVlanStaticXTopology": ieee8021QBridgeVlanStaticXTopology,
       "radBridgePortVlanTable": radBridgePortVlanTable,
       "radBridgePortVlanEntry": radBridgePortVlanEntry,
       "radBridgePortVlanBridgeIdx": radBridgePortVlanBridgeIdx,
       "radBridgePortVlanIdx": radBridgePortVlanIdx,
       "radBridgePortVlanPrtIdx": radBridgePortVlanPrtIdx,
       "radBridgePortVlanRowStatus": radBridgePortVlanRowStatus,
       "radBridgePortVlanIsRoot": radBridgePortVlanIsRoot,
       "radBridgeStatus": radBridgeStatus,
       "radBridgeInvBasePortTable": radBridgeInvBasePortTable,
       "radBridgeInvBasePortEntry": radBridgeInvBasePortEntry,
       "radBridgeInvBasePortIfIndex": radBridgeInvBasePortIfIndex,
       "radBridgeInvBasePort": radBridgeInvBasePort,
       "bridgeMacSearchTable": bridgeMacSearchTable,
       "bridgeMacSearchEntry": bridgeMacSearchEntry,
       "bridgeMacSearchIdx": bridgeMacSearchIdx,
       "bridgeMacSearchBridgeComponentId": bridgeMacSearchBridgeComponentId,
       "bridgeMacSearchAddress": bridgeMacSearchAddress,
       "bridgeMacSearchVlan": bridgeMacSearchVlan,
       "bridgeMacSearchPort": bridgeMacSearchPort,
       "bridgeMacSearchCmdStatus": bridgeMacSearchCmdStatus,
       "bridgeMacResultTable": bridgeMacResultTable,
       "bridgeMacResultEntry": bridgeMacResultEntry,
       "bridgeMacResultBridgeIdx": bridgeMacResultBridgeIdx,
       "bridgeMacResultVlan": bridgeMacResultVlan,
       "bridgeMacResultMacAddress": bridgeMacResultMacAddress,
       "bridgeMacResultPort": bridgeMacResultPort,
       "bridgeMacResultCmdStatus": bridgeMacResultCmdStatus,
       "radBridgeStp": radBridgeStp,
       "radBridgeStpCnfgTable": radBridgeStpCnfgTable,
       "radBridgeStpCnfgEntry": radBridgeStpCnfgEntry,
       "radBridgeStpCnfgIdx1": radBridgeStpCnfgIdx1,
       "radBridgeStpCnfgIdx2": radBridgeStpCnfgIdx2,
       "radBridgeStpCnfgForwardDelay": radBridgeStpCnfgForwardDelay,
       "radBridgeStpCnfgMaxAge": radBridgeStpCnfgMaxAge,
       "radBridgeStpCnfgHelloTime": radBridgeStpCnfgHelloTime,
       "radBridgeStpCnfgPriority": radBridgeStpCnfgPriority,
       "radBridgeStpCnfgStpVersion": radBridgeStpCnfgStpVersion,
       "radBridgeStpStatTable": radBridgeStpStatTable,
       "radBridgeStpStatEntry": radBridgeStpStatEntry,
       "radBridgeStpStatIdx": radBridgeStpStatIdx,
       "radBridgeStpStatForwardDelay": radBridgeStpStatForwardDelay,
       "radBridgeStpStatMaxAge": radBridgeStpStatMaxAge,
       "radBridgeStpStatHelloTime": radBridgeStpStatHelloTime,
       "radBridgeStpStatDesignatedRoot": radBridgeStpStatDesignatedRoot,
       "radBridgeStpStatRootCost": radBridgeStpStatRootCost,
       "ieee8021MstpXTable": ieee8021MstpXTable,
       "ieee8021MstpXEntry": ieee8021MstpXEntry,
       "ieee8021MstpXVids0": ieee8021MstpXVids0,
       "ieee8021MstpXVids1": ieee8021MstpXVids1,
       "ieee8021MstpXVids2": ieee8021MstpXVids2,
       "ieee8021MstpXVids3": ieee8021MstpXVids3,
       "radBridgeForwardingMode": radBridgeForwardingMode,
       "radBridgePort": radBridgePort,
       "radBridgePortCnfgTable": radBridgePortCnfgTable,
       "radBridgePortCnfgEntry": radBridgePortCnfgEntry,
       "radBridgePortCnfgIdx": radBridgePortCnfgIdx,
       "radBridgePortCnfgPrtIdx": radBridgePortCnfgPrtIdx,
       "radBridgePortCnfgMaxMacAddr": radBridgePortCnfgMaxMacAddr,
       "radBridgePortCnfgMngFlow": radBridgePortCnfgMngFlow,
       "radBridgePortCnfgMcastMode": radBridgePortCnfgMcastMode,
       "radBridgePortCnfgDefaultVpi": radBridgePortCnfgDefaultVpi,
       "radBridgePortCnfgDefaultVci": radBridgePortCnfgDefaultVci,
       "radBridgePortCnfgStatVlanId": radBridgePortCnfgStatVlanId,
       "radBridgePortCnfgIngressMtu": radBridgePortCnfgIngressMtu,
       "radBridgePortCnfgEgressMtu": radBridgePortCnfgEgressMtu,
       "radBridgePortCnfgDot1x": radBridgePortCnfgDot1x,
       "radBridgePortCnfgMappingProfile": radBridgePortCnfgMappingProfile,
       "ieee8021BridgeBaseXTable": ieee8021BridgeBaseXTable,
       "ieee8021BridgeBaseXEntry": ieee8021BridgeBaseXEntry,
       "ieee8021BridgeBaseXForwardingMode": ieee8021BridgeBaseXForwardingMode,
       "ieee8021BridgeBaseXName": ieee8021BridgeBaseXName,
       "invieee8021QBridgeVlanCurrentTable": invieee8021QBridgeVlanCurrentTable,
       "invieee8021QBridgeVlanCurrentEntry": invieee8021QBridgeVlanCurrentEntry,
       "invieee8021QBridgeVlanCurrentComponentId": invieee8021QBridgeVlanCurrentComponentId,
       "invieee8021QBridgeVlanFdbId": invieee8021QBridgeVlanFdbId,
       "invieee8021QBridgeVlanTimeMark": invieee8021QBridgeVlanTimeMark,
       "invieee8021QBridgeVlanIndex": invieee8021QBridgeVlanIndex}
)
