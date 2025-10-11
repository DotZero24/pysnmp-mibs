# SNMP MIB module (SUPERMICRO-OFC-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OFC-CFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:05:06 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsofc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81)
)
if mibBuilder.loadTexts:
    fsofc.setRevisions(
        ("2013-01-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


class INTEGER64(TextualConvention, Counter64):
    status = "current"
    displayHint = "d64"


class ActionString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255as"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ContextId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d32"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TableIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d32"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FlowIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d32"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_FsofcCfgGroup_ObjectIdentity = ObjectIdentity
fsofcCfgGroup = _FsofcCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1)
)
_FsofcCfgTable_Object = MibTable
fsofcCfgTable = _FsofcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1)
)
if mibBuilder.loadTexts:
    fsofcCfgTable.setStatus("current")
_FsofcCfgEntry_Object = MibTableRow
fsofcCfgEntry = _FsofcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1)
)
fsofcCfgEntry.setIndexNames(
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcContextId"),
)
if mibBuilder.loadTexts:
    fsofcCfgEntry.setStatus("current")
_FsofcContextId_Type = ContextId
_FsofcContextId_Object = MibTableColumn
fsofcContextId = _FsofcContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 1),
    _FsofcContextId_Type()
)
fsofcContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcContextId.setStatus("current")


class _FsofcModuleStatus_Type(Integer32):
    """Custom type fsofcModuleStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsofcModuleStatus_Type.__name__ = "Integer32"
_FsofcModuleStatus_Object = MibTableColumn
fsofcModuleStatus = _FsofcModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 2),
    _FsofcModuleStatus_Type()
)
fsofcModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcModuleStatus.setStatus("current")


class _FsofcSupportedVersion_Type(Integer32):
    """Custom type fsofcSupportedVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v100", 1),
          ("v131", 2))
    )


_FsofcSupportedVersion_Type.__name__ = "Integer32"
_FsofcSupportedVersion_Object = MibTableColumn
fsofcSupportedVersion = _FsofcSupportedVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 3),
    _FsofcSupportedVersion_Type()
)
fsofcSupportedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcSupportedVersion.setStatus("current")


class _FsofcDefaultFlowMissBehaviour_Type(Integer32):
    """Custom type fsofcDefaultFlowMissBehaviour based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("sendToController", 2))
    )


_FsofcDefaultFlowMissBehaviour_Type.__name__ = "Integer32"
_FsofcDefaultFlowMissBehaviour_Object = MibTableColumn
fsofcDefaultFlowMissBehaviour = _FsofcDefaultFlowMissBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 4),
    _FsofcDefaultFlowMissBehaviour_Type()
)
fsofcDefaultFlowMissBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcDefaultFlowMissBehaviour.setStatus("current")


class _FsofcControlPktBuffering_Type(Integer32):
    """Custom type fsofcControlPktBuffering based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsofcControlPktBuffering_Type.__name__ = "Integer32"
_FsofcControlPktBuffering_Object = MibTableColumn
fsofcControlPktBuffering = _FsofcControlPktBuffering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 5),
    _FsofcControlPktBuffering_Type()
)
fsofcControlPktBuffering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcControlPktBuffering.setStatus("current")


class _FsofcIpReassembleStatus_Type(Integer32):
    """Custom type fsofcIpReassembleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsofcIpReassembleStatus_Type.__name__ = "Integer32"
_FsofcIpReassembleStatus_Object = MibTableColumn
fsofcIpReassembleStatus = _FsofcIpReassembleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 6),
    _FsofcIpReassembleStatus_Type()
)
fsofcIpReassembleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcIpReassembleStatus.setStatus("current")


class _FsofcPortStpStatus_Type(Integer32):
    """Custom type fsofcPortStpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsofcPortStpStatus_Type.__name__ = "Integer32"
_FsofcPortStpStatus_Object = MibTableColumn
fsofcPortStpStatus = _FsofcPortStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 7),
    _FsofcPortStpStatus_Type()
)
fsofcPortStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcPortStpStatus.setStatus("current")
_FsofcTraceEnable_Type = Unsigned32
_FsofcTraceEnable_Object = MibTableColumn
fsofcTraceEnable = _FsofcTraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 8),
    _FsofcTraceEnable_Type()
)
fsofcTraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcTraceEnable.setStatus("current")


class _FsofcSwitchModeOnConnFailure_Type(Integer32):
    """Custom type fsofcSwitchModeOnConnFailure based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failSecure", 1),
          ("failStandAlone", 2))
    )


_FsofcSwitchModeOnConnFailure_Type.__name__ = "Integer32"
_FsofcSwitchModeOnConnFailure_Object = MibTableColumn
fsofcSwitchModeOnConnFailure = _FsofcSwitchModeOnConnFailure_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 9),
    _FsofcSwitchModeOnConnFailure_Type()
)
fsofcSwitchModeOnConnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcSwitchModeOnConnFailure.setStatus("current")
_FsofcSwitchEntryStatus_Type = RowStatus
_FsofcSwitchEntryStatus_Object = MibTableColumn
fsofcSwitchEntryStatus = _FsofcSwitchEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 1, 1, 1, 10),
    _FsofcSwitchEntryStatus_Type()
)
fsofcSwitchEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcSwitchEntryStatus.setStatus("current")
_FsofcControllerCfgGroup_ObjectIdentity = ObjectIdentity
fsofcControllerCfgGroup = _FsofcControllerCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2)
)
_FsofcControllerConnTable_Object = MibTable
fsofcControllerConnTable = _FsofcControllerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1)
)
if mibBuilder.loadTexts:
    fsofcControllerConnTable.setStatus("current")
_FsofcControllerConnEntry_Object = MibTableRow
fsofcControllerConnEntry = _FsofcControllerConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1)
)
fsofcControllerConnEntry.setIndexNames(
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcContextId"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcControllerIpAddrType"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcControllerIpAddress"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcControllerConnAuxId"),
)
if mibBuilder.loadTexts:
    fsofcControllerConnEntry.setStatus("current")
_FsofcControllerIpAddrType_Type = InetAddressType
_FsofcControllerIpAddrType_Object = MibTableColumn
fsofcControllerIpAddrType = _FsofcControllerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 1),
    _FsofcControllerIpAddrType_Type()
)
fsofcControllerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcControllerIpAddrType.setStatus("current")
_FsofcControllerIpAddress_Type = InetAddress
_FsofcControllerIpAddress_Object = MibTableColumn
fsofcControllerIpAddress = _FsofcControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 2),
    _FsofcControllerIpAddress_Type()
)
fsofcControllerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcControllerIpAddress.setStatus("current")


class _FsofcControllerConnAuxId_Type(Integer32):
    """Custom type fsofcControllerConnAuxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FsofcControllerConnAuxId_Type.__name__ = "Integer32"
_FsofcControllerConnAuxId_Object = MibTableColumn
fsofcControllerConnAuxId = _FsofcControllerConnAuxId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 3),
    _FsofcControllerConnAuxId_Type()
)
fsofcControllerConnAuxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcControllerConnAuxId.setStatus("current")


class _FsofcControllerConnPort_Type(Integer32):
    """Custom type fsofcControllerConnPort based on Integer32"""
    defaultValue = 6633

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsofcControllerConnPort_Type.__name__ = "Integer32"
_FsofcControllerConnPort_Object = MibTableColumn
fsofcControllerConnPort = _FsofcControllerConnPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 4),
    _FsofcControllerConnPort_Type()
)
fsofcControllerConnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcControllerConnPort.setStatus("current")


class _FsofcControllerConnProtocol_Type(Integer32):
    """Custom type fsofcControllerConnProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("ssl", 2))
    )


_FsofcControllerConnProtocol_Type.__name__ = "Integer32"
_FsofcControllerConnProtocol_Object = MibTableColumn
fsofcControllerConnProtocol = _FsofcControllerConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 5),
    _FsofcControllerConnProtocol_Type()
)
fsofcControllerConnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcControllerConnProtocol.setStatus("current")


class _FsofcControllerRole_Type(Integer32):
    """Custom type fsofcControllerRole based on Integer32"""
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
        *(("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_FsofcControllerRole_Type.__name__ = "Integer32"
_FsofcControllerRole_Object = MibTableColumn
fsofcControllerRole = _FsofcControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 6),
    _FsofcControllerRole_Type()
)
fsofcControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcControllerRole.setStatus("current")


class _FsofcControllerConnState_Type(Integer32):
    """Custom type fsofcControllerConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2),
          ("connInProgress", 3))
    )


_FsofcControllerConnState_Type.__name__ = "Integer32"
_FsofcControllerConnState_Object = MibTableColumn
fsofcControllerConnState = _FsofcControllerConnState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 7),
    _FsofcControllerConnState_Type()
)
fsofcControllerConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcControllerConnState.setStatus("current")


class _FsofcControllerConnEchoReqCount_Type(Integer32):
    """Custom type fsofcControllerConnEchoReqCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsofcControllerConnEchoReqCount_Type.__name__ = "Integer32"
_FsofcControllerConnEchoReqCount_Object = MibTableColumn
fsofcControllerConnEchoReqCount = _FsofcControllerConnEchoReqCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 8),
    _FsofcControllerConnEchoReqCount_Type()
)
fsofcControllerConnEchoReqCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcControllerConnEchoReqCount.setStatus("current")


class _FsofcControllerConnEchoReplyCount_Type(Integer32):
    """Custom type fsofcControllerConnEchoReplyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsofcControllerConnEchoReplyCount_Type.__name__ = "Integer32"
_FsofcControllerConnEchoReplyCount_Object = MibTableColumn
fsofcControllerConnEchoReplyCount = _FsofcControllerConnEchoReplyCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 9),
    _FsofcControllerConnEchoReplyCount_Type()
)
fsofcControllerConnEchoReplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcControllerConnEchoReplyCount.setStatus("current")
_FsofcControllerConnEntryStatus_Type = RowStatus
_FsofcControllerConnEntryStatus_Object = MibTableColumn
fsofcControllerConnEntryStatus = _FsofcControllerConnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 2, 1, 1, 10),
    _FsofcControllerConnEntryStatus_Type()
)
fsofcControllerConnEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcControllerConnEntryStatus.setStatus("current")
_FsofcInterfaceGroup_ObjectIdentity = ObjectIdentity
fsofcInterfaceGroup = _FsofcInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3)
)
_FsofcIfTable_Object = MibTable
fsofcIfTable = _FsofcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1)
)
if mibBuilder.loadTexts:
    fsofcIfTable.setStatus("current")
_FsofcIfEntry_Object = MibTableRow
fsofcIfEntry = _FsofcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1)
)
fsofcIfEntry.setIndexNames(
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcContextId"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcIfIndex"),
)
if mibBuilder.loadTexts:
    fsofcIfEntry.setStatus("current")
_FsofcIfIndex_Type = InterfaceIndex
_FsofcIfIndex_Object = MibTableColumn
fsofcIfIndex = _FsofcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 1),
    _FsofcIfIndex_Type()
)
fsofcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcIfIndex.setStatus("current")


class _FsofcIfType_Type(Integer32):
    """Custom type fsofcIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("logical", 2),
          ("reserved", 3))
    )


_FsofcIfType_Type.__name__ = "Integer32"
_FsofcIfType_Object = MibTableColumn
fsofcIfType = _FsofcIfType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 2),
    _FsofcIfType_Type()
)
fsofcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcIfType.setStatus("current")


class _FsofcIfAlias_Type(DisplayString):
    """Custom type fsofcIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsofcIfAlias_Type.__name__ = "DisplayString"
_FsofcIfAlias_Object = MibTableColumn
fsofcIfAlias = _FsofcIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 3),
    _FsofcIfAlias_Type()
)
fsofcIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcIfAlias.setStatus("current")


class _FsofcIfOperStatus_Type(Integer32):
    """Custom type fsofcIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("others", 3))
    )


_FsofcIfOperStatus_Type.__name__ = "Integer32"
_FsofcIfOperStatus_Object = MibTableColumn
fsofcIfOperStatus = _FsofcIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 4),
    _FsofcIfOperStatus_Type()
)
fsofcIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcIfOperStatus.setStatus("current")
_FsofcVlanEgressPorts_Type = PortList
_FsofcVlanEgressPorts_Object = MibTableColumn
fsofcVlanEgressPorts = _FsofcVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 5),
    _FsofcVlanEgressPorts_Type()
)
fsofcVlanEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcVlanEgressPorts.setStatus("current")
_FsofcVlanUntaggedPorts_Type = PortList
_FsofcVlanUntaggedPorts_Object = MibTableColumn
fsofcVlanUntaggedPorts = _FsofcVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 6),
    _FsofcVlanUntaggedPorts_Type()
)
fsofcVlanUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsofcVlanUntaggedPorts.setStatus("current")
_FsofcVlanInFrames_Type = Counter32
_FsofcVlanInFrames_Object = MibTableColumn
fsofcVlanInFrames = _FsofcVlanInFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 7),
    _FsofcVlanInFrames_Type()
)
fsofcVlanInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcVlanInFrames.setStatus("current")
_FsofcVlanOutFrames_Type = Counter32
_FsofcVlanOutFrames_Object = MibTableColumn
fsofcVlanOutFrames = _FsofcVlanOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 3, 1, 1, 8),
    _FsofcVlanOutFrames_Type()
)
fsofcVlanOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcVlanOutFrames.setStatus("current")
_FsofcFlowGroup_ObjectIdentity = ObjectIdentity
fsofcFlowGroup = _FsofcFlowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4)
)
_FsofcFlowTable_Object = MibTable
fsofcFlowTable = _FsofcFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1)
)
if mibBuilder.loadTexts:
    fsofcFlowTable.setStatus("current")
_FsofcFlowEntry_Object = MibTableRow
fsofcFlowEntry = _FsofcFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1)
)
fsofcFlowEntry.setIndexNames(
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcContextId"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcTableIndex"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcFlowIndex"),
)
if mibBuilder.loadTexts:
    fsofcFlowEntry.setStatus("current")
_FsofcTableIndex_Type = TableIndex
_FsofcTableIndex_Object = MibTableColumn
fsofcTableIndex = _FsofcTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 1),
    _FsofcTableIndex_Type()
)
fsofcTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcTableIndex.setStatus("current")
_FsofcFlowIndex_Type = FlowIndex
_FsofcFlowIndex_Object = MibTableColumn
fsofcFlowIndex = _FsofcFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 2),
    _FsofcFlowIndex_Type()
)
fsofcFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcFlowIndex.setStatus("current")


class _FsofcFlowMatchField_Type(DisplayString):
    """Custom type fsofcFlowMatchField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FsofcFlowMatchField_Type.__name__ = "DisplayString"
_FsofcFlowMatchField_Object = MibTableColumn
fsofcFlowMatchField = _FsofcFlowMatchField_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 3),
    _FsofcFlowMatchField_Type()
)
fsofcFlowMatchField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowMatchField.setStatus("current")


class _FsofcFlowOutputAction_Type(DisplayString):
    """Custom type fsofcFlowOutputAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FsofcFlowOutputAction_Type.__name__ = "DisplayString"
_FsofcFlowOutputAction_Object = MibTableColumn
fsofcFlowOutputAction = _FsofcFlowOutputAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 4),
    _FsofcFlowOutputAction_Type()
)
fsofcFlowOutputAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowOutputAction.setStatus("current")
_FsofcFlowIdleTimeout_Type = Unsigned32
_FsofcFlowIdleTimeout_Object = MibTableColumn
fsofcFlowIdleTimeout = _FsofcFlowIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 5),
    _FsofcFlowIdleTimeout_Type()
)
fsofcFlowIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowIdleTimeout.setStatus("current")
_FsofcFlowHardTimeout_Type = Unsigned32
_FsofcFlowHardTimeout_Object = MibTableColumn
fsofcFlowHardTimeout = _FsofcFlowHardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 6),
    _FsofcFlowHardTimeout_Type()
)
fsofcFlowHardTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowHardTimeout.setStatus("current")
_FsofcFlowPacketCount_Type = INTEGER64
_FsofcFlowPacketCount_Object = MibTableColumn
fsofcFlowPacketCount = _FsofcFlowPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 7),
    _FsofcFlowPacketCount_Type()
)
fsofcFlowPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowPacketCount.setStatus("current")
_FsofcFlowByteCount_Type = INTEGER64
_FsofcFlowByteCount_Object = MibTableColumn
fsofcFlowByteCount = _FsofcFlowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 8),
    _FsofcFlowByteCount_Type()
)
fsofcFlowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowByteCount.setStatus("current")
_FsofcFlowDurationSec_Type = Unsigned32
_FsofcFlowDurationSec_Object = MibTableColumn
fsofcFlowDurationSec = _FsofcFlowDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 4, 1, 1, 9),
    _FsofcFlowDurationSec_Type()
)
fsofcFlowDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcFlowDurationSec.setStatus("current")
_FsofcGrpGroup_ObjectIdentity = ObjectIdentity
fsofcGrpGroup = _FsofcGrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5)
)
_FsofcGroupTable_Object = MibTable
fsofcGroupTable = _FsofcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1)
)
if mibBuilder.loadTexts:
    fsofcGroupTable.setStatus("current")
_FsofcGroupEntry_Object = MibTableRow
fsofcGroupEntry = _FsofcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1)
)
fsofcGroupEntry.setIndexNames(
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcContextId"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcGroupIndex"),
)
if mibBuilder.loadTexts:
    fsofcGroupEntry.setStatus("current")


class _FsofcGroupIndex_Type(Unsigned32):
    """Custom type fsofcGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsofcGroupIndex_Type.__name__ = "Unsigned32"
_FsofcGroupIndex_Object = MibTableColumn
fsofcGroupIndex = _FsofcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1, 1),
    _FsofcGroupIndex_Type()
)
fsofcGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcGroupIndex.setStatus("current")


class _FsofcGroupType_Type(Integer32):
    """Custom type fsofcGroupType based on Integer32"""
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
        *(("all", 0),
          ("select", 1),
          ("indirect", 2),
          ("fastfailover", 3))
    )


_FsofcGroupType_Type.__name__ = "Integer32"
_FsofcGroupType_Object = MibTableColumn
fsofcGroupType = _FsofcGroupType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1, 2),
    _FsofcGroupType_Type()
)
fsofcGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcGroupType.setStatus("current")
_FsofcGroupActionBuckets_Type = ActionString
_FsofcGroupActionBuckets_Object = MibTableColumn
fsofcGroupActionBuckets = _FsofcGroupActionBuckets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1, 3),
    _FsofcGroupActionBuckets_Type()
)
fsofcGroupActionBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcGroupActionBuckets.setStatus("current")
_FsofcGroupPacketCount_Type = INTEGER64
_FsofcGroupPacketCount_Object = MibTableColumn
fsofcGroupPacketCount = _FsofcGroupPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1, 5),
    _FsofcGroupPacketCount_Type()
)
fsofcGroupPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcGroupPacketCount.setStatus("current")
_FsofcGroupByteCount_Type = INTEGER64
_FsofcGroupByteCount_Object = MibTableColumn
fsofcGroupByteCount = _FsofcGroupByteCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1, 6),
    _FsofcGroupByteCount_Type()
)
fsofcGroupByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcGroupByteCount.setStatus("current")
_FsofcGroupDurationSec_Type = Unsigned32
_FsofcGroupDurationSec_Object = MibTableColumn
fsofcGroupDurationSec = _FsofcGroupDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 5, 1, 1, 7),
    _FsofcGroupDurationSec_Type()
)
fsofcGroupDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcGroupDurationSec.setStatus("current")
_FsofcMeterGroup_ObjectIdentity = ObjectIdentity
fsofcMeterGroup = _FsofcMeterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6)
)
_FsofcMeterTable_Object = MibTable
fsofcMeterTable = _FsofcMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1)
)
if mibBuilder.loadTexts:
    fsofcMeterTable.setStatus("current")
_FsofcMeterEntry_Object = MibTableRow
fsofcMeterEntry = _FsofcMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1)
)
fsofcMeterEntry.setIndexNames(
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcContextId"),
    (0, "SUPERMICRO-OFC-CFG-MIB", "fsofcMeterIndex"),
)
if mibBuilder.loadTexts:
    fsofcMeterEntry.setStatus("current")


class _FsofcMeterIndex_Type(Unsigned32):
    """Custom type fsofcMeterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsofcMeterIndex_Type.__name__ = "Unsigned32"
_FsofcMeterIndex_Object = MibTableColumn
fsofcMeterIndex = _FsofcMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1, 1),
    _FsofcMeterIndex_Type()
)
fsofcMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsofcMeterIndex.setStatus("current")


class _FsofcMeterBandInfo_Type(DisplayString):
    """Custom type fsofcMeterBandInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsofcMeterBandInfo_Type.__name__ = "DisplayString"
_FsofcMeterBandInfo_Object = MibTableColumn
fsofcMeterBandInfo = _FsofcMeterBandInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1, 2),
    _FsofcMeterBandInfo_Type()
)
fsofcMeterBandInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcMeterBandInfo.setStatus("current")
_FsofcMeterFlowCount_Type = Counter32
_FsofcMeterFlowCount_Object = MibTableColumn
fsofcMeterFlowCount = _FsofcMeterFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1, 3),
    _FsofcMeterFlowCount_Type()
)
fsofcMeterFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcMeterFlowCount.setStatus("current")
_FsofcMeterPacketInCount_Type = INTEGER64
_FsofcMeterPacketInCount_Object = MibTableColumn
fsofcMeterPacketInCount = _FsofcMeterPacketInCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1, 4),
    _FsofcMeterPacketInCount_Type()
)
fsofcMeterPacketInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcMeterPacketInCount.setStatus("current")
_FsofcMeterByteInCount_Type = INTEGER64
_FsofcMeterByteInCount_Object = MibTableColumn
fsofcMeterByteInCount = _FsofcMeterByteInCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1, 5),
    _FsofcMeterByteInCount_Type()
)
fsofcMeterByteInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcMeterByteInCount.setStatus("current")
_FsofcMeterDurationSec_Type = Unsigned32
_FsofcMeterDurationSec_Object = MibTableColumn
fsofcMeterDurationSec = _FsofcMeterDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 81, 6, 1, 1, 6),
    _FsofcMeterDurationSec_Type()
)
fsofcMeterDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsofcMeterDurationSec.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OFC-CFG-MIB",
    **{"PortList": PortList,
       "INTEGER64": INTEGER64,
       "ActionString": ActionString,
       "ContextId": ContextId,
       "TableIndex": TableIndex,
       "FlowIndex": FlowIndex,
       "fsofc": fsofc,
       "fsofcCfgGroup": fsofcCfgGroup,
       "fsofcCfgTable": fsofcCfgTable,
       "fsofcCfgEntry": fsofcCfgEntry,
       "fsofcContextId": fsofcContextId,
       "fsofcModuleStatus": fsofcModuleStatus,
       "fsofcSupportedVersion": fsofcSupportedVersion,
       "fsofcDefaultFlowMissBehaviour": fsofcDefaultFlowMissBehaviour,
       "fsofcControlPktBuffering": fsofcControlPktBuffering,
       "fsofcIpReassembleStatus": fsofcIpReassembleStatus,
       "fsofcPortStpStatus": fsofcPortStpStatus,
       "fsofcTraceEnable": fsofcTraceEnable,
       "fsofcSwitchModeOnConnFailure": fsofcSwitchModeOnConnFailure,
       "fsofcSwitchEntryStatus": fsofcSwitchEntryStatus,
       "fsofcControllerCfgGroup": fsofcControllerCfgGroup,
       "fsofcControllerConnTable": fsofcControllerConnTable,
       "fsofcControllerConnEntry": fsofcControllerConnEntry,
       "fsofcControllerIpAddrType": fsofcControllerIpAddrType,
       "fsofcControllerIpAddress": fsofcControllerIpAddress,
       "fsofcControllerConnAuxId": fsofcControllerConnAuxId,
       "fsofcControllerConnPort": fsofcControllerConnPort,
       "fsofcControllerConnProtocol": fsofcControllerConnProtocol,
       "fsofcControllerRole": fsofcControllerRole,
       "fsofcControllerConnState": fsofcControllerConnState,
       "fsofcControllerConnEchoReqCount": fsofcControllerConnEchoReqCount,
       "fsofcControllerConnEchoReplyCount": fsofcControllerConnEchoReplyCount,
       "fsofcControllerConnEntryStatus": fsofcControllerConnEntryStatus,
       "fsofcInterfaceGroup": fsofcInterfaceGroup,
       "fsofcIfTable": fsofcIfTable,
       "fsofcIfEntry": fsofcIfEntry,
       "fsofcIfIndex": fsofcIfIndex,
       "fsofcIfType": fsofcIfType,
       "fsofcIfAlias": fsofcIfAlias,
       "fsofcIfOperStatus": fsofcIfOperStatus,
       "fsofcVlanEgressPorts": fsofcVlanEgressPorts,
       "fsofcVlanUntaggedPorts": fsofcVlanUntaggedPorts,
       "fsofcVlanInFrames": fsofcVlanInFrames,
       "fsofcVlanOutFrames": fsofcVlanOutFrames,
       "fsofcFlowGroup": fsofcFlowGroup,
       "fsofcFlowTable": fsofcFlowTable,
       "fsofcFlowEntry": fsofcFlowEntry,
       "fsofcTableIndex": fsofcTableIndex,
       "fsofcFlowIndex": fsofcFlowIndex,
       "fsofcFlowMatchField": fsofcFlowMatchField,
       "fsofcFlowOutputAction": fsofcFlowOutputAction,
       "fsofcFlowIdleTimeout": fsofcFlowIdleTimeout,
       "fsofcFlowHardTimeout": fsofcFlowHardTimeout,
       "fsofcFlowPacketCount": fsofcFlowPacketCount,
       "fsofcFlowByteCount": fsofcFlowByteCount,
       "fsofcFlowDurationSec": fsofcFlowDurationSec,
       "fsofcGrpGroup": fsofcGrpGroup,
       "fsofcGroupTable": fsofcGroupTable,
       "fsofcGroupEntry": fsofcGroupEntry,
       "fsofcGroupIndex": fsofcGroupIndex,
       "fsofcGroupType": fsofcGroupType,
       "fsofcGroupActionBuckets": fsofcGroupActionBuckets,
       "fsofcGroupPacketCount": fsofcGroupPacketCount,
       "fsofcGroupByteCount": fsofcGroupByteCount,
       "fsofcGroupDurationSec": fsofcGroupDurationSec,
       "fsofcMeterGroup": fsofcMeterGroup,
       "fsofcMeterTable": fsofcMeterTable,
       "fsofcMeterEntry": fsofcMeterEntry,
       "fsofcMeterIndex": fsofcMeterIndex,
       "fsofcMeterBandInfo": fsofcMeterBandInfo,
       "fsofcMeterFlowCount": fsofcMeterFlowCount,
       "fsofcMeterPacketInCount": fsofcMeterPacketInCount,
       "fsofcMeterByteInCount": fsofcMeterByteInCount,
       "fsofcMeterDurationSec": fsofcMeterDurationSec}
)
