# SNMP MIB module (SUPERMICRO-RBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RBRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:13 2025
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

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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

fsrbridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66)
)
if mibBuilder.loadTexts:
    fsrbridgeMIB.setRevisions(
        ("2012-09-05 00:00",
         "2011-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RbridgeAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class RbridgeNickname(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65471),
    )



# MIB Managed Objects in the order of their OIDs

_FsrbridgeObjects_ObjectIdentity = ObjectIdentity
fsrbridgeObjects = _FsrbridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0)
)
_Fsrbridge_ObjectIdentity = ObjectIdentity
fsrbridge = _Fsrbridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1)
)
_FsrbridgeGlobalTrace_Type = Unsigned32
_FsrbridgeGlobalTrace_Object = MibScalar
fsrbridgeGlobalTrace = _FsrbridgeGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 1),
    _FsrbridgeGlobalTrace_Type()
)
fsrbridgeGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeGlobalTrace.setStatus("current")
_FsrbridgeGlobalTable_Object = MibTable
fsrbridgeGlobalTable = _FsrbridgeGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2)
)
if mibBuilder.loadTexts:
    fsrbridgeGlobalTable.setStatus("current")
_FsrbridgeGlobalEntry_Object = MibTableRow
fsrbridgeGlobalEntry = _FsrbridgeGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1)
)
fsrbridgeGlobalEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeContextId"),
)
if mibBuilder.loadTexts:
    fsrbridgeGlobalEntry.setStatus("current")
_FsrbridgeContextId_Type = Unsigned32
_FsrbridgeContextId_Object = MibTableColumn
fsrbridgeContextId = _FsrbridgeContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 1),
    _FsrbridgeContextId_Type()
)
fsrbridgeContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeContextId.setStatus("current")
_FsrbridgeTrillVersion_Type = Unsigned32
_FsrbridgeTrillVersion_Object = MibTableColumn
fsrbridgeTrillVersion = _FsrbridgeTrillVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 2),
    _FsrbridgeTrillVersion_Type()
)
fsrbridgeTrillVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgeTrillVersion.setStatus("current")
_FsrbridgeNumPorts_Type = Unsigned32
_FsrbridgeNumPorts_Object = MibTableColumn
fsrbridgeNumPorts = _FsrbridgeNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 3),
    _FsrbridgeNumPorts_Type()
)
fsrbridgeNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgeNumPorts.setStatus("current")
if mibBuilder.loadTexts:
    fsrbridgeNumPorts.setUnits("ports")
_FsrbridgeUniMultipathEnable_Type = TruthValue
_FsrbridgeUniMultipathEnable_Object = MibTableColumn
fsrbridgeUniMultipathEnable = _FsrbridgeUniMultipathEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 4),
    _FsrbridgeUniMultipathEnable_Type()
)
fsrbridgeUniMultipathEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeUniMultipathEnable.setStatus("current")
_FsrbridgeMultiMultipathEnable_Type = TruthValue
_FsrbridgeMultiMultipathEnable_Object = MibTableColumn
fsrbridgeMultiMultipathEnable = _FsrbridgeMultiMultipathEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 5),
    _FsrbridgeMultiMultipathEnable_Type()
)
fsrbridgeMultiMultipathEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeMultiMultipathEnable.setStatus("current")


class _FsrbridgeNicknameNumber_Type(Unsigned32):
    """Custom type fsrbridgeNicknameNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsrbridgeNicknameNumber_Type.__name__ = "Unsigned32"
_FsrbridgeNicknameNumber_Object = MibTableColumn
fsrbridgeNicknameNumber = _FsrbridgeNicknameNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 6),
    _FsrbridgeNicknameNumber_Type()
)
fsrbridgeNicknameNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeNicknameNumber.setStatus("current")


class _FsrbridgeSystemControl_Type(Integer32):
    """Custom type fsrbridgeSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsrbridgeSystemControl_Type.__name__ = "Integer32"
_FsrbridgeSystemControl_Object = MibTableColumn
fsrbridgeSystemControl = _FsrbridgeSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 7),
    _FsrbridgeSystemControl_Type()
)
fsrbridgeSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeSystemControl.setStatus("current")


class _FsrbridgeModuleStatus_Type(Integer32):
    """Custom type fsrbridgeModuleStatus based on Integer32"""
    defaultValue = 2

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


_FsrbridgeModuleStatus_Type.__name__ = "Integer32"
_FsrbridgeModuleStatus_Object = MibTableColumn
fsrbridgeModuleStatus = _FsrbridgeModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 8),
    _FsrbridgeModuleStatus_Type()
)
fsrbridgeModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeModuleStatus.setStatus("current")
_FsrbridgeUnicastMultipathCount_Type = Unsigned32
_FsrbridgeUnicastMultipathCount_Object = MibTableColumn
fsrbridgeUnicastMultipathCount = _FsrbridgeUnicastMultipathCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 9),
    _FsrbridgeUnicastMultipathCount_Type()
)
fsrbridgeUnicastMultipathCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeUnicastMultipathCount.setStatus("current")
_FsrbridgeMulticastMultipathCount_Type = Unsigned32
_FsrbridgeMulticastMultipathCount_Object = MibTableColumn
fsrbridgeMulticastMultipathCount = _FsrbridgeMulticastMultipathCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 10),
    _FsrbridgeMulticastMultipathCount_Type()
)
fsrbridgeMulticastMultipathCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeMulticastMultipathCount.setStatus("current")


class _FsrbridgeClearCounters_Type(TruthValue):
    """Custom type fsrbridgeClearCounters based on TruthValue"""
    defaultValue = 2


_FsrbridgeClearCounters_Type.__name__ = "TruthValue"
_FsrbridgeClearCounters_Object = MibTableColumn
fsrbridgeClearCounters = _FsrbridgeClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 2, 1, 11),
    _FsrbridgeClearCounters_Type()
)
fsrbridgeClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeClearCounters.setStatus("current")
_FsrbridgeNicknameTable_Object = MibTable
fsrbridgeNicknameTable = _FsrbridgeNicknameTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 3)
)
if mibBuilder.loadTexts:
    fsrbridgeNicknameTable.setStatus("current")
_FsrbridgeNicknameEntry_Object = MibTableRow
fsrbridgeNicknameEntry = _FsrbridgeNicknameEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 3, 1)
)
fsrbridgeNicknameEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeContextId"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeNicknameName"),
)
if mibBuilder.loadTexts:
    fsrbridgeNicknameEntry.setStatus("current")
_FsrbridgeNicknameName_Type = RbridgeNickname
_FsrbridgeNicknameName_Object = MibTableColumn
fsrbridgeNicknameName = _FsrbridgeNicknameName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 3, 1, 1),
    _FsrbridgeNicknameName_Type()
)
fsrbridgeNicknameName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeNicknameName.setStatus("current")


class _FsrbridgeNicknamePriority_Type(Unsigned32):
    """Custom type fsrbridgeNicknamePriority based on Unsigned32"""
    defaultValue = 192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsrbridgeNicknamePriority_Type.__name__ = "Unsigned32"
_FsrbridgeNicknamePriority_Object = MibTableColumn
fsrbridgeNicknamePriority = _FsrbridgeNicknamePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 3, 1, 2),
    _FsrbridgeNicknamePriority_Type()
)
fsrbridgeNicknamePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgeNicknamePriority.setStatus("current")


class _FsrbridgeNicknameDtrPriority_Type(Unsigned32):
    """Custom type fsrbridgeNicknameDtrPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsrbridgeNicknameDtrPriority_Type.__name__ = "Unsigned32"
_FsrbridgeNicknameDtrPriority_Object = MibTableColumn
fsrbridgeNicknameDtrPriority = _FsrbridgeNicknameDtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 3, 1, 3),
    _FsrbridgeNicknameDtrPriority_Type()
)
fsrbridgeNicknameDtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgeNicknameDtrPriority.setStatus("current")


class _FsrbridgeNicknameStatus_Type(Integer32):
    """Custom type fsrbridgeNicknameStatus based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("invalid", 3))
    )


_FsrbridgeNicknameStatus_Type.__name__ = "Integer32"
_FsrbridgeNicknameStatus_Object = MibTableColumn
fsrbridgeNicknameStatus = _FsrbridgeNicknameStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 3, 1, 4),
    _FsrbridgeNicknameStatus_Type()
)
fsrbridgeNicknameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgeNicknameStatus.setStatus("current")
_FsrbridgePortTable_Object = MibTable
fsrbridgePortTable = _FsrbridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4)
)
if mibBuilder.loadTexts:
    fsrbridgePortTable.setStatus("current")
_FsrbridgePortEntry_Object = MibTableRow
fsrbridgePortEntry = _FsrbridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1)
)
fsrbridgePortEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgePortIfIndex"),
)
if mibBuilder.loadTexts:
    fsrbridgePortEntry.setStatus("current")
_FsrbridgePortIfIndex_Type = InterfaceIndex
_FsrbridgePortIfIndex_Object = MibTableColumn
fsrbridgePortIfIndex = _FsrbridgePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 1),
    _FsrbridgePortIfIndex_Type()
)
fsrbridgePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgePortIfIndex.setStatus("current")


class _FsrbridgePortDisable_Type(TruthValue):
    """Custom type fsrbridgePortDisable based on TruthValue"""
    defaultValue = 2


_FsrbridgePortDisable_Type.__name__ = "TruthValue"
_FsrbridgePortDisable_Object = MibTableColumn
fsrbridgePortDisable = _FsrbridgePortDisable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 2),
    _FsrbridgePortDisable_Type()
)
fsrbridgePortDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgePortDisable.setStatus("current")


class _FsrbridgePortTrunkPort_Type(TruthValue):
    """Custom type fsrbridgePortTrunkPort based on TruthValue"""
    defaultValue = 2


_FsrbridgePortTrunkPort_Type.__name__ = "TruthValue"
_FsrbridgePortTrunkPort_Object = MibTableColumn
fsrbridgePortTrunkPort = _FsrbridgePortTrunkPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 3),
    _FsrbridgePortTrunkPort_Type()
)
fsrbridgePortTrunkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgePortTrunkPort.setStatus("current")


class _FsrbridgePortAccessPort_Type(TruthValue):
    """Custom type fsrbridgePortAccessPort based on TruthValue"""
    defaultValue = 2


_FsrbridgePortAccessPort_Type.__name__ = "TruthValue"
_FsrbridgePortAccessPort_Object = MibTableColumn
fsrbridgePortAccessPort = _FsrbridgePortAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 4),
    _FsrbridgePortAccessPort_Type()
)
fsrbridgePortAccessPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgePortAccessPort.setStatus("current")


class _FsrbridgePortState_Type(Integer32):
    """Custom type fsrbridgePortState based on Integer32"""
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
        *(("uninhibited", 1),
          ("portInhibited", 2),
          ("vlanInhibited", 3),
          ("disabled", 4),
          ("broken", 5))
    )


_FsrbridgePortState_Type.__name__ = "Integer32"
_FsrbridgePortState_Object = MibTableColumn
fsrbridgePortState = _FsrbridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 5),
    _FsrbridgePortState_Type()
)
fsrbridgePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortState.setStatus("current")


class _FsrbridgePortDisableLearning_Type(TruthValue):
    """Custom type fsrbridgePortDisableLearning based on TruthValue"""
    defaultValue = 2


_FsrbridgePortDisableLearning_Type.__name__ = "TruthValue"
_FsrbridgePortDisableLearning_Object = MibTableColumn
fsrbridgePortDisableLearning = _FsrbridgePortDisableLearning_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 6),
    _FsrbridgePortDisableLearning_Type()
)
fsrbridgePortDisableLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsrbridgePortDisableLearning.setStatus("current")
_FsrbridgePortDesigVlan_Type = VlanId
_FsrbridgePortDesigVlan_Object = MibTableColumn
fsrbridgePortDesigVlan = _FsrbridgePortDesigVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 7),
    _FsrbridgePortDesigVlan_Type()
)
fsrbridgePortDesigVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgePortDesigVlan.setStatus("current")


class _FsrbridgePortClearCounters_Type(TruthValue):
    """Custom type fsrbridgePortClearCounters based on TruthValue"""
    defaultValue = 2


_FsrbridgePortClearCounters_Type.__name__ = "TruthValue"
_FsrbridgePortClearCounters_Object = MibTableColumn
fsrbridgePortClearCounters = _FsrbridgePortClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 8),
    _FsrbridgePortClearCounters_Type()
)
fsrbridgePortClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgePortClearCounters.setStatus("current")
_FsrbridgePortMac_Type = MacAddress
_FsrbridgePortMac_Object = MibTableColumn
fsrbridgePortMac = _FsrbridgePortMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 1, 4, 1, 9),
    _FsrbridgePortMac_Type()
)
fsrbridgePortMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortMac.setStatus("current")
_FsrbridgeFdb_ObjectIdentity = ObjectIdentity
fsrbridgeFdb = _FsrbridgeFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2)
)
_FsrbridgeUniFdbTable_Object = MibTable
fsrbridgeUniFdbTable = _FsrbridgeUniFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1)
)
if mibBuilder.loadTexts:
    fsrbridgeUniFdbTable.setStatus("current")
_FsrbridgeUniFdbEntry_Object = MibTableRow
fsrbridgeUniFdbEntry = _FsrbridgeUniFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1)
)
fsrbridgeUniFdbEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeContextId"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeFdbId"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeUniFdbAddr"),
)
if mibBuilder.loadTexts:
    fsrbridgeUniFdbEntry.setStatus("current")


class _FsrbridgeFdbId_Type(Unsigned32):
    """Custom type fsrbridgeFdbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsrbridgeFdbId_Type.__name__ = "Unsigned32"
_FsrbridgeFdbId_Object = MibTableColumn
fsrbridgeFdbId = _FsrbridgeFdbId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 1),
    _FsrbridgeFdbId_Type()
)
fsrbridgeFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeFdbId.setStatus("current")
_FsrbridgeUniFdbAddr_Type = MacAddress
_FsrbridgeUniFdbAddr_Object = MibTableColumn
fsrbridgeUniFdbAddr = _FsrbridgeUniFdbAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 2),
    _FsrbridgeUniFdbAddr_Type()
)
fsrbridgeUniFdbAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeUniFdbAddr.setStatus("current")


class _FsrbridgeUniFdbPort_Type(Integer32):
    """Custom type fsrbridgeUniFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsrbridgeUniFdbPort_Type.__name__ = "Integer32"
_FsrbridgeUniFdbPort_Object = MibTableColumn
fsrbridgeUniFdbPort = _FsrbridgeUniFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 3),
    _FsrbridgeUniFdbPort_Type()
)
fsrbridgeUniFdbPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeUniFdbPort.setStatus("current")
_FsrbridgeUniFdbNick_Type = RbridgeNickname
_FsrbridgeUniFdbNick_Object = MibTableColumn
fsrbridgeUniFdbNick = _FsrbridgeUniFdbNick_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 4),
    _FsrbridgeUniFdbNick_Type()
)
fsrbridgeUniFdbNick.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeUniFdbNick.setStatus("current")


class _FsrbridgeUniFdbConfidence_Type(Unsigned32):
    """Custom type fsrbridgeUniFdbConfidence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_FsrbridgeUniFdbConfidence_Type.__name__ = "Unsigned32"
_FsrbridgeUniFdbConfidence_Object = MibTableColumn
fsrbridgeUniFdbConfidence = _FsrbridgeUniFdbConfidence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 5),
    _FsrbridgeUniFdbConfidence_Type()
)
fsrbridgeUniFdbConfidence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeUniFdbConfidence.setStatus("current")


class _FsrbridgeUniFdbStatus_Type(Integer32):
    """Custom type fsrbridgeUniFdbStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5),
          ("esadi", 6))
    )


_FsrbridgeUniFdbStatus_Type.__name__ = "Integer32"
_FsrbridgeUniFdbStatus_Object = MibTableColumn
fsrbridgeUniFdbStatus = _FsrbridgeUniFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 6),
    _FsrbridgeUniFdbStatus_Type()
)
fsrbridgeUniFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgeUniFdbStatus.setStatus("current")
_FsrbridgeUniFdbRowStatus_Type = RowStatus
_FsrbridgeUniFdbRowStatus_Object = MibTableColumn
fsrbridgeUniFdbRowStatus = _FsrbridgeUniFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 1, 1, 7),
    _FsrbridgeUniFdbRowStatus_Type()
)
fsrbridgeUniFdbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeUniFdbRowStatus.setStatus("current")
_FsrbridgeUniFibTable_Object = MibTable
fsrbridgeUniFibTable = _FsrbridgeUniFibTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2)
)
if mibBuilder.loadTexts:
    fsrbridgeUniFibTable.setStatus("current")
_FsrbridgeUniFibEntry_Object = MibTableRow
fsrbridgeUniFibEntry = _FsrbridgeUniFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1)
)
fsrbridgeUniFibEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeContextId"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeFibNickname"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeFibPort"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeFibNextHopRBridge"),
)
if mibBuilder.loadTexts:
    fsrbridgeUniFibEntry.setStatus("current")
_FsrbridgeFibNickname_Type = RbridgeNickname
_FsrbridgeFibNickname_Object = MibTableColumn
fsrbridgeFibNickname = _FsrbridgeFibNickname_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 1),
    _FsrbridgeFibNickname_Type()
)
fsrbridgeFibNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeFibNickname.setStatus("current")


class _FsrbridgeFibPort_Type(Integer32):
    """Custom type fsrbridgeFibPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsrbridgeFibPort_Type.__name__ = "Integer32"
_FsrbridgeFibPort_Object = MibTableColumn
fsrbridgeFibPort = _FsrbridgeFibPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 2),
    _FsrbridgeFibPort_Type()
)
fsrbridgeFibPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeFibPort.setStatus("current")
_FsrbridgeFibNextHopRBridge_Type = RbridgeNickname
_FsrbridgeFibNextHopRBridge_Object = MibTableColumn
fsrbridgeFibNextHopRBridge = _FsrbridgeFibNextHopRBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 3),
    _FsrbridgeFibNextHopRBridge_Type()
)
fsrbridgeFibNextHopRBridge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeFibNextHopRBridge.setStatus("current")
_FsrbridgeFibMacAddress_Type = RbridgeAddress
_FsrbridgeFibMacAddress_Object = MibTableColumn
fsrbridgeFibMacAddress = _FsrbridgeFibMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 4),
    _FsrbridgeFibMacAddress_Type()
)
fsrbridgeFibMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeFibMacAddress.setStatus("current")


class _FsrbridgeFibMtuDesired_Type(Unsigned32):
    """Custom type fsrbridgeFibMtuDesired based on Unsigned32"""
    defaultValue = 1470


_FsrbridgeFibMtuDesired_Type.__name__ = "Unsigned32"
_FsrbridgeFibMtuDesired_Object = MibTableColumn
fsrbridgeFibMtuDesired = _FsrbridgeFibMtuDesired_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 5),
    _FsrbridgeFibMtuDesired_Type()
)
fsrbridgeFibMtuDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeFibMtuDesired.setStatus("current")


class _FsrbridgeFibHopCount_Type(Unsigned32):
    """Custom type fsrbridgeFibHopCount based on Unsigned32"""
    defaultValue = 10


_FsrbridgeFibHopCount_Type.__name__ = "Unsigned32"
_FsrbridgeFibHopCount_Object = MibTableColumn
fsrbridgeFibHopCount = _FsrbridgeFibHopCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 6),
    _FsrbridgeFibHopCount_Type()
)
fsrbridgeFibHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeFibHopCount.setStatus("current")


class _FsrbridgeFibStatus_Type(Integer32):
    """Custom type fsrbridgeFibStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_FsrbridgeFibStatus_Type.__name__ = "Integer32"
_FsrbridgeFibStatus_Object = MibTableColumn
fsrbridgeFibStatus = _FsrbridgeFibStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 7),
    _FsrbridgeFibStatus_Type()
)
fsrbridgeFibStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgeFibStatus.setStatus("current")
_FsrbridgeFibRowstatus_Type = RowStatus
_FsrbridgeFibRowstatus_Object = MibTableColumn
fsrbridgeFibRowstatus = _FsrbridgeFibRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 2, 1, 8),
    _FsrbridgeFibRowstatus_Type()
)
fsrbridgeFibRowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeFibRowstatus.setStatus("current")
_FsrbridgeMultiFibTable_Object = MibTable
fsrbridgeMultiFibTable = _FsrbridgeMultiFibTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 4)
)
if mibBuilder.loadTexts:
    fsrbridgeMultiFibTable.setStatus("current")
_FsrbridgeMultiFibEntry_Object = MibTableRow
fsrbridgeMultiFibEntry = _FsrbridgeMultiFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 4, 1)
)
fsrbridgeMultiFibEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeContextId"),
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgeMultiFibNickname"),
)
if mibBuilder.loadTexts:
    fsrbridgeMultiFibEntry.setStatus("current")
_FsrbridgeMultiFibNickname_Type = RbridgeNickname
_FsrbridgeMultiFibNickname_Object = MibTableColumn
fsrbridgeMultiFibNickname = _FsrbridgeMultiFibNickname_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 4, 1, 1),
    _FsrbridgeMultiFibNickname_Type()
)
fsrbridgeMultiFibNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrbridgeMultiFibNickname.setStatus("current")
_FsrbridgeMultiFibPorts_Type = PortList
_FsrbridgeMultiFibPorts_Object = MibTableColumn
fsrbridgeMultiFibPorts = _FsrbridgeMultiFibPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 4, 1, 2),
    _FsrbridgeMultiFibPorts_Type()
)
fsrbridgeMultiFibPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeMultiFibPorts.setStatus("current")


class _FsrbridgeMultiFibStatus_Type(Integer32):
    """Custom type fsrbridgeMultiFibStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_FsrbridgeMultiFibStatus_Type.__name__ = "Integer32"
_FsrbridgeMultiFibStatus_Object = MibTableColumn
fsrbridgeMultiFibStatus = _FsrbridgeMultiFibStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 4, 1, 3),
    _FsrbridgeMultiFibStatus_Type()
)
fsrbridgeMultiFibStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgeMultiFibStatus.setStatus("current")
_FsrbridgeMultiFibRowStatus_Type = RowStatus
_FsrbridgeMultiFibRowStatus_Object = MibTableColumn
fsrbridgeMultiFibRowStatus = _FsrbridgeMultiFibRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 2, 4, 1, 4),
    _FsrbridgeMultiFibRowStatus_Type()
)
fsrbridgeMultiFibRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrbridgeMultiFibRowStatus.setStatus("current")
_FsrbridgeCounter_ObjectIdentity = ObjectIdentity
fsrbridgeCounter = _FsrbridgeCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3)
)
_FsrbridgePortCounterTable_Object = MibTable
fsrbridgePortCounterTable = _FsrbridgePortCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1)
)
if mibBuilder.loadTexts:
    fsrbridgePortCounterTable.setStatus("current")
_FsrbridgePortCounterEntry_Object = MibTableRow
fsrbridgePortCounterEntry = _FsrbridgePortCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1, 1)
)
fsrbridgePortCounterEntry.setIndexNames(
    (0, "SUPERMICRO-RBRIDGE-MIB", "fsrbridgePortIfIndex"),
)
if mibBuilder.loadTexts:
    fsrbridgePortCounterEntry.setStatus("current")
_FsrbridgePortRpfChecksFailed_Type = Counter32
_FsrbridgePortRpfChecksFailed_Object = MibTableColumn
fsrbridgePortRpfChecksFailed = _FsrbridgePortRpfChecksFailed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1, 1, 1),
    _FsrbridgePortRpfChecksFailed_Type()
)
fsrbridgePortRpfChecksFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortRpfChecksFailed.setStatus("current")
_FsrbridgePortHopCountsExceeded_Type = Counter32
_FsrbridgePortHopCountsExceeded_Object = MibTableColumn
fsrbridgePortHopCountsExceeded = _FsrbridgePortHopCountsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1, 1, 2),
    _FsrbridgePortHopCountsExceeded_Type()
)
fsrbridgePortHopCountsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortHopCountsExceeded.setStatus("current")
_FsrbridgePortOptions_Type = Counter32
_FsrbridgePortOptions_Object = MibTableColumn
fsrbridgePortOptions = _FsrbridgePortOptions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1, 1, 3),
    _FsrbridgePortOptions_Type()
)
fsrbridgePortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortOptions.setStatus("current")
_FsrbridgePortTrillInFrames_Type = Counter64
_FsrbridgePortTrillInFrames_Object = MibTableColumn
fsrbridgePortTrillInFrames = _FsrbridgePortTrillInFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1, 1, 4),
    _FsrbridgePortTrillInFrames_Type()
)
fsrbridgePortTrillInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortTrillInFrames.setStatus("current")
_FsrbridgePortTrillOutFrames_Type = Counter64
_FsrbridgePortTrillOutFrames_Object = MibTableColumn
fsrbridgePortTrillOutFrames = _FsrbridgePortTrillOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 0, 3, 1, 1, 5),
    _FsrbridgePortTrillOutFrames_Type()
)
fsrbridgePortTrillOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrbridgePortTrillOutFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RBRIDGE-MIB",
    **{"RbridgeAddress": RbridgeAddress,
       "RbridgeNickname": RbridgeNickname,
       "fsrbridgeMIB": fsrbridgeMIB,
       "fsrbridgeObjects": fsrbridgeObjects,
       "fsrbridge": fsrbridge,
       "fsrbridgeGlobalTrace": fsrbridgeGlobalTrace,
       "fsrbridgeGlobalTable": fsrbridgeGlobalTable,
       "fsrbridgeGlobalEntry": fsrbridgeGlobalEntry,
       "fsrbridgeContextId": fsrbridgeContextId,
       "fsrbridgeTrillVersion": fsrbridgeTrillVersion,
       "fsrbridgeNumPorts": fsrbridgeNumPorts,
       "fsrbridgeUniMultipathEnable": fsrbridgeUniMultipathEnable,
       "fsrbridgeMultiMultipathEnable": fsrbridgeMultiMultipathEnable,
       "fsrbridgeNicknameNumber": fsrbridgeNicknameNumber,
       "fsrbridgeSystemControl": fsrbridgeSystemControl,
       "fsrbridgeModuleStatus": fsrbridgeModuleStatus,
       "fsrbridgeUnicastMultipathCount": fsrbridgeUnicastMultipathCount,
       "fsrbridgeMulticastMultipathCount": fsrbridgeMulticastMultipathCount,
       "fsrbridgeClearCounters": fsrbridgeClearCounters,
       "fsrbridgeNicknameTable": fsrbridgeNicknameTable,
       "fsrbridgeNicknameEntry": fsrbridgeNicknameEntry,
       "fsrbridgeNicknameName": fsrbridgeNicknameName,
       "fsrbridgeNicknamePriority": fsrbridgeNicknamePriority,
       "fsrbridgeNicknameDtrPriority": fsrbridgeNicknameDtrPriority,
       "fsrbridgeNicknameStatus": fsrbridgeNicknameStatus,
       "fsrbridgePortTable": fsrbridgePortTable,
       "fsrbridgePortEntry": fsrbridgePortEntry,
       "fsrbridgePortIfIndex": fsrbridgePortIfIndex,
       "fsrbridgePortDisable": fsrbridgePortDisable,
       "fsrbridgePortTrunkPort": fsrbridgePortTrunkPort,
       "fsrbridgePortAccessPort": fsrbridgePortAccessPort,
       "fsrbridgePortState": fsrbridgePortState,
       "fsrbridgePortDisableLearning": fsrbridgePortDisableLearning,
       "fsrbridgePortDesigVlan": fsrbridgePortDesigVlan,
       "fsrbridgePortClearCounters": fsrbridgePortClearCounters,
       "fsrbridgePortMac": fsrbridgePortMac,
       "fsrbridgeFdb": fsrbridgeFdb,
       "fsrbridgeUniFdbTable": fsrbridgeUniFdbTable,
       "fsrbridgeUniFdbEntry": fsrbridgeUniFdbEntry,
       "fsrbridgeFdbId": fsrbridgeFdbId,
       "fsrbridgeUniFdbAddr": fsrbridgeUniFdbAddr,
       "fsrbridgeUniFdbPort": fsrbridgeUniFdbPort,
       "fsrbridgeUniFdbNick": fsrbridgeUniFdbNick,
       "fsrbridgeUniFdbConfidence": fsrbridgeUniFdbConfidence,
       "fsrbridgeUniFdbStatus": fsrbridgeUniFdbStatus,
       "fsrbridgeUniFdbRowStatus": fsrbridgeUniFdbRowStatus,
       "fsrbridgeUniFibTable": fsrbridgeUniFibTable,
       "fsrbridgeUniFibEntry": fsrbridgeUniFibEntry,
       "fsrbridgeFibNickname": fsrbridgeFibNickname,
       "fsrbridgeFibPort": fsrbridgeFibPort,
       "fsrbridgeFibNextHopRBridge": fsrbridgeFibNextHopRBridge,
       "fsrbridgeFibMacAddress": fsrbridgeFibMacAddress,
       "fsrbridgeFibMtuDesired": fsrbridgeFibMtuDesired,
       "fsrbridgeFibHopCount": fsrbridgeFibHopCount,
       "fsrbridgeFibStatus": fsrbridgeFibStatus,
       "fsrbridgeFibRowstatus": fsrbridgeFibRowstatus,
       "fsrbridgeMultiFibTable": fsrbridgeMultiFibTable,
       "fsrbridgeMultiFibEntry": fsrbridgeMultiFibEntry,
       "fsrbridgeMultiFibNickname": fsrbridgeMultiFibNickname,
       "fsrbridgeMultiFibPorts": fsrbridgeMultiFibPorts,
       "fsrbridgeMultiFibStatus": fsrbridgeMultiFibStatus,
       "fsrbridgeMultiFibRowStatus": fsrbridgeMultiFibRowStatus,
       "fsrbridgeCounter": fsrbridgeCounter,
       "fsrbridgePortCounterTable": fsrbridgePortCounterTable,
       "fsrbridgePortCounterEntry": fsrbridgePortCounterEntry,
       "fsrbridgePortRpfChecksFailed": fsrbridgePortRpfChecksFailed,
       "fsrbridgePortHopCountsExceeded": fsrbridgePortHopCountsExceeded,
       "fsrbridgePortOptions": fsrbridgePortOptions,
       "fsrbridgePortTrillInFrames": fsrbridgePortTrillInFrames,
       "fsrbridgePortTrillOutFrames": fsrbridgePortTrillOutFrames}
)
