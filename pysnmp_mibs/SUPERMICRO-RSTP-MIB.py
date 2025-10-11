# SNMP MIB module (SUPERMICRO-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:10 2025
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
 dot1dBaseBridgeAddress,
 dot1dStpDesignatedRoot,
 dot1dStpPortState) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "dot1dBaseBridgeAddress",
    "dot1dStpDesignatedRoot",
    "dot1dStpPortState")

(dot1dStpVersion,) = mibBuilder.importSymbols(
    "RSTP-MIB",
    "dot1dStpVersion")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

futureRstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79)
)
if mibBuilder.loadTexts:
    futureRstMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_Dot1wFutureRst_ObjectIdentity = ObjectIdentity
dot1wFutureRst = _Dot1wFutureRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1)
)


class _FsRstSystemControl_Type(Integer32):
    """Custom type fsRstSystemControl based on Integer32"""
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


_FsRstSystemControl_Type.__name__ = "Integer32"
_FsRstSystemControl_Object = MibScalar
fsRstSystemControl = _FsRstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 1),
    _FsRstSystemControl_Type()
)
fsRstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstSystemControl.setStatus("current")
_FsRstModuleStatus_Type = EnabledStatus
_FsRstModuleStatus_Object = MibScalar
fsRstModuleStatus = _FsRstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 2),
    _FsRstModuleStatus_Type()
)
fsRstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstModuleStatus.setStatus("current")


class _FsRstTraceOption_Type(Integer32):
    """Custom type fsRstTraceOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRstTraceOption_Type.__name__ = "Integer32"
_FsRstTraceOption_Object = MibScalar
fsRstTraceOption = _FsRstTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 3),
    _FsRstTraceOption_Type()
)
fsRstTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstTraceOption.setStatus("current")


class _FsRstDebugOption_Type(Integer32):
    """Custom type fsRstDebugOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsRstDebugOption_Type.__name__ = "Integer32"
_FsRstDebugOption_Object = MibScalar
fsRstDebugOption = _FsRstDebugOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 4),
    _FsRstDebugOption_Type()
)
fsRstDebugOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstDebugOption.setStatus("current")
_FsRstRstpUpCount_Type = Counter32
_FsRstRstpUpCount_Object = MibScalar
fsRstRstpUpCount = _FsRstRstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 5),
    _FsRstRstpUpCount_Type()
)
fsRstRstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstRstpUpCount.setStatus("current")
_FsRstRstpDownCount_Type = Counter32
_FsRstRstpDownCount_Object = MibScalar
fsRstRstpDownCount = _FsRstRstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 6),
    _FsRstRstpDownCount_Type()
)
fsRstRstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstRstpDownCount.setStatus("current")
_FsRstBufferFailureCount_Type = Counter32
_FsRstBufferFailureCount_Object = MibScalar
fsRstBufferFailureCount = _FsRstBufferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 7),
    _FsRstBufferFailureCount_Type()
)
fsRstBufferFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstBufferFailureCount.setStatus("current")
_FsRstMemAllocFailureCount_Type = Counter32
_FsRstMemAllocFailureCount_Object = MibScalar
fsRstMemAllocFailureCount = _FsRstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 8),
    _FsRstMemAllocFailureCount_Type()
)
fsRstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstMemAllocFailureCount.setStatus("current")
_FsRstNewRootIdCount_Type = Counter32
_FsRstNewRootIdCount_Object = MibScalar
fsRstNewRootIdCount = _FsRstNewRootIdCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 9),
    _FsRstNewRootIdCount_Type()
)
fsRstNewRootIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstNewRootIdCount.setStatus("current")


class _FsRstPortRoleSelSmState_Type(Integer32):
    """Custom type fsRstPortRoleSelSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_FsRstPortRoleSelSmState_Type.__name__ = "Integer32"
_FsRstPortRoleSelSmState_Object = MibScalar
fsRstPortRoleSelSmState = _FsRstPortRoleSelSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 10),
    _FsRstPortRoleSelSmState_Type()
)
fsRstPortRoleSelSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRoleSelSmState.setStatus("current")
_FsRstOldDesignatedRoot_Type = BridgeId
_FsRstOldDesignatedRoot_Object = MibScalar
fsRstOldDesignatedRoot = _FsRstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 11),
    _FsRstOldDesignatedRoot_Type()
)
fsRstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstOldDesignatedRoot.setStatus("current")
_FsRstPortExtTable_Object = MibTable
fsRstPortExtTable = _FsRstPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12)
)
if mibBuilder.loadTexts:
    fsRstPortExtTable.setStatus("current")
_FsRstPortExtEntry_Object = MibTableRow
fsRstPortExtEntry = _FsRstPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1)
)
fsRstPortExtEntry.setIndexNames(
    (0, "SUPERMICRO-RSTP-MIB", "fsRstPort"),
)
if mibBuilder.loadTexts:
    fsRstPortExtEntry.setStatus("current")


class _FsRstPort_Type(Integer32):
    """Custom type fsRstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsRstPort_Type.__name__ = "Integer32"
_FsRstPort_Object = MibTableColumn
fsRstPort = _FsRstPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 1),
    _FsRstPort_Type()
)
fsRstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRstPort.setStatus("current")


class _FsRstPortRole_Type(Integer32):
    """Custom type fsRstPortRole based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsRstPortRole_Type.__name__ = "Integer32"
_FsRstPortRole_Object = MibTableColumn
fsRstPortRole = _FsRstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 2),
    _FsRstPortRole_Type()
)
fsRstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRole.setStatus("current")


class _FsRstPortOperVersion_Type(Integer32):
    """Custom type fsRstPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2))
    )


_FsRstPortOperVersion_Type.__name__ = "Integer32"
_FsRstPortOperVersion_Object = MibTableColumn
fsRstPortOperVersion = _FsRstPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 3),
    _FsRstPortOperVersion_Type()
)
fsRstPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortOperVersion.setStatus("current")


class _FsRstPortInfoSmState_Type(Integer32):
    """Custom type fsRstPortInfoSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superior", 3),
          ("repeat", 4),
          ("notdesignated", 5),
          ("present", 6),
          ("receive", 7),
          ("inferiordesignated", 8))
    )


_FsRstPortInfoSmState_Type.__name__ = "Integer32"
_FsRstPortInfoSmState_Object = MibTableColumn
fsRstPortInfoSmState = _FsRstPortInfoSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 4),
    _FsRstPortInfoSmState_Type()
)
fsRstPortInfoSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortInfoSmState.setStatus("current")


class _FsRstPortMigSmState_Type(Integer32):
    """Custom type fsRstPortMigSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkingrstp", 0),
          ("selectingstp", 1),
          ("sensing", 2))
    )


_FsRstPortMigSmState_Type.__name__ = "Integer32"
_FsRstPortMigSmState_Object = MibTableColumn
fsRstPortMigSmState = _FsRstPortMigSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 5),
    _FsRstPortMigSmState_Type()
)
fsRstPortMigSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortMigSmState.setStatus("current")


class _FsRstPortRoleTransSmState_Type(Integer32):
    """Custom type fsRstPortRoleTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("init", 0),
          ("disableport", 1),
          ("disabledport", 2),
          ("rootport", 3),
          ("designatedport", 4),
          ("backupport", 5),
          ("rootproposed", 6),
          ("rootagreed", 7),
          ("reroot", 8),
          ("rootforward", 9),
          ("rootlearn", 10),
          ("rerooted", 11),
          ("designatedpropose", 12),
          ("designatedsynced", 13),
          ("designatedretired", 14),
          ("designatedforward", 15),
          ("designatedlearn", 16),
          ("designatedlisten", 17))
    )


_FsRstPortRoleTransSmState_Type.__name__ = "Integer32"
_FsRstPortRoleTransSmState_Object = MibTableColumn
fsRstPortRoleTransSmState = _FsRstPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 6),
    _FsRstPortRoleTransSmState_Type()
)
fsRstPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRoleTransSmState.setStatus("current")


class _FsRstPortStateTransSmState_Type(Integer32):
    """Custom type fsRstPortStateTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_FsRstPortStateTransSmState_Type.__name__ = "Integer32"
_FsRstPortStateTransSmState_Object = MibTableColumn
fsRstPortStateTransSmState = _FsRstPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 7),
    _FsRstPortStateTransSmState_Type()
)
fsRstPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortStateTransSmState.setStatus("current")


class _FsRstPortTopoChSmState_Type(Integer32):
    """Custom type fsRstPortTopoChSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("learning", 1),
          ("detected", 2),
          ("active", 3),
          ("notifiedtcn", 4),
          ("notifiedtc", 5),
          ("propagating", 6),
          ("acknowledged", 7))
    )


_FsRstPortTopoChSmState_Type.__name__ = "Integer32"
_FsRstPortTopoChSmState_Object = MibTableColumn
fsRstPortTopoChSmState = _FsRstPortTopoChSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 8),
    _FsRstPortTopoChSmState_Type()
)
fsRstPortTopoChSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortTopoChSmState.setStatus("current")


class _FsRstPortTxSmState_Type(Integer32):
    """Custom type fsRstPortTxSmState based on Integer32"""
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
        *(("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitconfig", 2),
          ("transmittcn", 3),
          ("transmitrstp", 4),
          ("idle", 5))
    )


_FsRstPortTxSmState_Type.__name__ = "Integer32"
_FsRstPortTxSmState_Object = MibTableColumn
fsRstPortTxSmState = _FsRstPortTxSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 9),
    _FsRstPortTxSmState_Type()
)
fsRstPortTxSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortTxSmState.setStatus("current")
_FsRstPortRxRstBpduCount_Type = Counter32
_FsRstPortRxRstBpduCount_Object = MibTableColumn
fsRstPortRxRstBpduCount = _FsRstPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 10),
    _FsRstPortRxRstBpduCount_Type()
)
fsRstPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRxRstBpduCount.setStatus("current")
_FsRstPortRxConfigBpduCount_Type = Counter32
_FsRstPortRxConfigBpduCount_Object = MibTableColumn
fsRstPortRxConfigBpduCount = _FsRstPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 11),
    _FsRstPortRxConfigBpduCount_Type()
)
fsRstPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRxConfigBpduCount.setStatus("current")
_FsRstPortRxTcnBpduCount_Type = Counter32
_FsRstPortRxTcnBpduCount_Object = MibTableColumn
fsRstPortRxTcnBpduCount = _FsRstPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 12),
    _FsRstPortRxTcnBpduCount_Type()
)
fsRstPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRxTcnBpduCount.setStatus("current")
_FsRstPortTxRstBpduCount_Type = Counter32
_FsRstPortTxRstBpduCount_Object = MibTableColumn
fsRstPortTxRstBpduCount = _FsRstPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 13),
    _FsRstPortTxRstBpduCount_Type()
)
fsRstPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortTxRstBpduCount.setStatus("current")
_FsRstPortTxConfigBpduCount_Type = Counter32
_FsRstPortTxConfigBpduCount_Object = MibTableColumn
fsRstPortTxConfigBpduCount = _FsRstPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 14),
    _FsRstPortTxConfigBpduCount_Type()
)
fsRstPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortTxConfigBpduCount.setStatus("current")
_FsRstPortTxTcnBpduCount_Type = Counter32
_FsRstPortTxTcnBpduCount_Object = MibTableColumn
fsRstPortTxTcnBpduCount = _FsRstPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 15),
    _FsRstPortTxTcnBpduCount_Type()
)
fsRstPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortTxTcnBpduCount.setStatus("current")
_FsRstPortInvalidRstBpduRxCount_Type = Counter32
_FsRstPortInvalidRstBpduRxCount_Object = MibTableColumn
fsRstPortInvalidRstBpduRxCount = _FsRstPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 16),
    _FsRstPortInvalidRstBpduRxCount_Type()
)
fsRstPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortInvalidRstBpduRxCount.setStatus("current")
_FsRstPortInvalidConfigBpduRxCount_Type = Counter32
_FsRstPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsRstPortInvalidConfigBpduRxCount = _FsRstPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 17),
    _FsRstPortInvalidConfigBpduRxCount_Type()
)
fsRstPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortInvalidConfigBpduRxCount.setStatus("current")
_FsRstPortInvalidTcnBpduRxCount_Type = Counter32
_FsRstPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsRstPortInvalidTcnBpduRxCount = _FsRstPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 18),
    _FsRstPortInvalidTcnBpduRxCount_Type()
)
fsRstPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortInvalidTcnBpduRxCount.setStatus("current")
_FsRstPortProtocolMigrationCount_Type = Counter32
_FsRstPortProtocolMigrationCount_Object = MibTableColumn
fsRstPortProtocolMigrationCount = _FsRstPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 19),
    _FsRstPortProtocolMigrationCount_Type()
)
fsRstPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortProtocolMigrationCount.setStatus("current")
_FsRstPortEffectivePortState_Type = TruthValue
_FsRstPortEffectivePortState_Object = MibTableColumn
fsRstPortEffectivePortState = _FsRstPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 20),
    _FsRstPortEffectivePortState_Type()
)
fsRstPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortEffectivePortState.setStatus("current")
_FsRstPortAutoEdge_Type = TruthValue
_FsRstPortAutoEdge_Object = MibTableColumn
fsRstPortAutoEdge = _FsRstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 21),
    _FsRstPortAutoEdge_Type()
)
fsRstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortAutoEdge.setStatus("current")
_FsRstPortRestrictedRole_Type = TruthValue
_FsRstPortRestrictedRole_Object = MibTableColumn
fsRstPortRestrictedRole = _FsRstPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 22),
    _FsRstPortRestrictedRole_Type()
)
fsRstPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortRestrictedRole.setStatus("current")
_FsRstPortRestrictedTCN_Type = TruthValue
_FsRstPortRestrictedTCN_Object = MibTableColumn
fsRstPortRestrictedTCN = _FsRstPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 23),
    _FsRstPortRestrictedTCN_Type()
)
fsRstPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortRestrictedTCN.setStatus("current")


class _FsRstPortEnableBPDURx_Type(TruthValue):
    """Custom type fsRstPortEnableBPDURx based on TruthValue"""
    defaultValue = 1


_FsRstPortEnableBPDURx_Type.__name__ = "TruthValue"
_FsRstPortEnableBPDURx_Object = MibTableColumn
fsRstPortEnableBPDURx = _FsRstPortEnableBPDURx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 24),
    _FsRstPortEnableBPDURx_Type()
)
fsRstPortEnableBPDURx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortEnableBPDURx.setStatus("current")


class _FsRstPortEnableBPDUTx_Type(TruthValue):
    """Custom type fsRstPortEnableBPDUTx based on TruthValue"""
    defaultValue = 1


_FsRstPortEnableBPDUTx_Type.__name__ = "TruthValue"
_FsRstPortEnableBPDUTx_Object = MibTableColumn
fsRstPortEnableBPDUTx = _FsRstPortEnableBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 25),
    _FsRstPortEnableBPDUTx_Type()
)
fsRstPortEnableBPDUTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortEnableBPDUTx.setStatus("current")
_FsRstPortPseudoRootId_Type = BridgeId
_FsRstPortPseudoRootId_Object = MibTableColumn
fsRstPortPseudoRootId = _FsRstPortPseudoRootId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 26),
    _FsRstPortPseudoRootId_Type()
)
fsRstPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortPseudoRootId.setStatus("current")


class _FsRstPortIsL2Gp_Type(TruthValue):
    """Custom type fsRstPortIsL2Gp based on TruthValue"""
    defaultValue = 2


_FsRstPortIsL2Gp_Type.__name__ = "TruthValue"
_FsRstPortIsL2Gp_Object = MibTableColumn
fsRstPortIsL2Gp = _FsRstPortIsL2Gp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 27),
    _FsRstPortIsL2Gp_Type()
)
fsRstPortIsL2Gp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortIsL2Gp.setStatus("current")


class _FsRstPortLoopGuard_Type(TruthValue):
    """Custom type fsRstPortLoopGuard based on TruthValue"""
    defaultValue = 2


_FsRstPortLoopGuard_Type.__name__ = "TruthValue"
_FsRstPortLoopGuard_Object = MibTableColumn
fsRstPortLoopGuard = _FsRstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 28),
    _FsRstPortLoopGuard_Type()
)
fsRstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortLoopGuard.setStatus("current")


class _FsRstPortRcvdEvent_Type(Integer32):
    """Custom type fsRstPortRcvdEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationEvent", 1),
          ("bpduEvent", 2),
          ("timerExpiryEvent", 3))
    )


_FsRstPortRcvdEvent_Type.__name__ = "Integer32"
_FsRstPortRcvdEvent_Object = MibTableColumn
fsRstPortRcvdEvent = _FsRstPortRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 29),
    _FsRstPortRcvdEvent_Type()
)
fsRstPortRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRcvdEvent.setStatus("current")
_FsRstPortRcvdEventSubType_Type = Integer32
_FsRstPortRcvdEventSubType_Object = MibTableColumn
fsRstPortRcvdEventSubType = _FsRstPortRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 30),
    _FsRstPortRcvdEventSubType_Type()
)
fsRstPortRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRcvdEventSubType.setStatus("current")
_FsRstPortRcvdEventTimeStamp_Type = Unsigned32
_FsRstPortRcvdEventTimeStamp_Object = MibTableColumn
fsRstPortRcvdEventTimeStamp = _FsRstPortRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 31),
    _FsRstPortRcvdEventTimeStamp_Type()
)
fsRstPortRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRcvdEventTimeStamp.setStatus("current")
_FsRstPortStateChangeTimeStamp_Type = Unsigned32
_FsRstPortStateChangeTimeStamp_Object = MibTableColumn
fsRstPortStateChangeTimeStamp = _FsRstPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 32),
    _FsRstPortStateChangeTimeStamp_Type()
)
fsRstPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortStateChangeTimeStamp.setStatus("current")
_FsRstPortRowStatus_Type = RowStatus
_FsRstPortRowStatus_Object = MibTableColumn
fsRstPortRowStatus = _FsRstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 33),
    _FsRstPortRowStatus_Type()
)
fsRstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRstPortRowStatus.setStatus("current")


class _FsRstPortBpduGuard_Type(Integer32):
    """Custom type fsRstPortBpduGuard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_FsRstPortBpduGuard_Type.__name__ = "Integer32"
_FsRstPortBpduGuard_Object = MibTableColumn
fsRstPortBpduGuard = _FsRstPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 12, 1, 34),
    _FsRstPortBpduGuard_Type()
)
fsRstPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstPortBpduGuard.setStatus("current")


class _FsRstDynamicPathcostCalculation_Type(TruthValue):
    """Custom type fsRstDynamicPathcostCalculation based on TruthValue"""
    defaultValue = 2


_FsRstDynamicPathcostCalculation_Type.__name__ = "TruthValue"
_FsRstDynamicPathcostCalculation_Object = MibScalar
fsRstDynamicPathcostCalculation = _FsRstDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 13),
    _FsRstDynamicPathcostCalculation_Type()
)
fsRstDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstDynamicPathcostCalculation.setStatus("current")


class _FsRstCalcPortPathCostOnSpeedChg_Type(TruthValue):
    """Custom type fsRstCalcPortPathCostOnSpeedChg based on TruthValue"""
    defaultValue = 2


_FsRstCalcPortPathCostOnSpeedChg_Type.__name__ = "TruthValue"
_FsRstCalcPortPathCostOnSpeedChg_Object = MibScalar
fsRstCalcPortPathCostOnSpeedChg = _FsRstCalcPortPathCostOnSpeedChg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 14),
    _FsRstCalcPortPathCostOnSpeedChg_Type()
)
fsRstCalcPortPathCostOnSpeedChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstCalcPortPathCostOnSpeedChg.setStatus("current")


class _FsRstRcvdEvent_Type(Integer32):
    """Custom type fsRstRcvdEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationEvent", 1),
          ("bpduEvent", 2),
          ("timerExpiryEvent", 3))
    )


_FsRstRcvdEvent_Type.__name__ = "Integer32"
_FsRstRcvdEvent_Object = MibScalar
fsRstRcvdEvent = _FsRstRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 15),
    _FsRstRcvdEvent_Type()
)
fsRstRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstRcvdEvent.setStatus("current")
_FsRstRcvdEventSubType_Type = Integer32
_FsRstRcvdEventSubType_Object = MibScalar
fsRstRcvdEventSubType = _FsRstRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 16),
    _FsRstRcvdEventSubType_Type()
)
fsRstRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstRcvdEventSubType.setStatus("current")
_FsRstRcvdEventTimeStamp_Type = Unsigned32
_FsRstRcvdEventTimeStamp_Object = MibScalar
fsRstRcvdEventTimeStamp = _FsRstRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 17),
    _FsRstRcvdEventTimeStamp_Type()
)
fsRstRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstRcvdEventTimeStamp.setStatus("current")
_FsRstRcvdPortStateChangeTimeStamp_Type = Unsigned32
_FsRstRcvdPortStateChangeTimeStamp_Object = MibScalar
fsRstRcvdPortStateChangeTimeStamp = _FsRstRcvdPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 18),
    _FsRstRcvdPortStateChangeTimeStamp_Type()
)
fsRstRcvdPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstRcvdPortStateChangeTimeStamp.setStatus("current")


class _FsRstBpduGuard_Type(Integer32):
    """Custom type fsRstBpduGuard based on Integer32"""
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


_FsRstBpduGuard_Type.__name__ = "Integer32"
_FsRstBpduGuard_Object = MibScalar
fsRstBpduGuard = _FsRstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 1, 19),
    _FsRstBpduGuard_Type()
)
fsRstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstBpduGuard.setStatus("current")
_Dot1wFsRstTrapsControl_ObjectIdentity = ObjectIdentity
dot1wFsRstTrapsControl = _Dot1wFsRstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2)
)


class _FsRstSetTraps_Type(Integer32):
    """Custom type fsRstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRstSetTraps_Type.__name__ = "Integer32"
_FsRstSetTraps_Object = MibScalar
fsRstSetTraps = _FsRstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 1),
    _FsRstSetTraps_Type()
)
fsRstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRstSetTraps.setStatus("current")


class _FsRstGenTrapType_Type(Integer32):
    """Custom type fsRstGenTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("up", 1),
          ("down", 2))
    )


_FsRstGenTrapType_Type.__name__ = "Integer32"
_FsRstGenTrapType_Object = MibScalar
fsRstGenTrapType = _FsRstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 2),
    _FsRstGenTrapType_Type()
)
fsRstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstGenTrapType.setStatus("current")


class _FsRstErrTrapType_Type(Integer32):
    """Custom type fsRstErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("memfail", 1),
          ("bufffail", 2))
    )


_FsRstErrTrapType_Type.__name__ = "Integer32"
_FsRstErrTrapType_Object = MibScalar
fsRstErrTrapType = _FsRstErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 3),
    _FsRstErrTrapType_Type()
)
fsRstErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstErrTrapType.setStatus("current")
_FsRstPortTrapNotificationTable_Object = MibTable
fsRstPortTrapNotificationTable = _FsRstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4)
)
if mibBuilder.loadTexts:
    fsRstPortTrapNotificationTable.setStatus("current")
_FsRstPortTrapNotificationEntry_Object = MibTableRow
fsRstPortTrapNotificationEntry = _FsRstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1)
)
fsRstPortTrapNotificationEntry.setIndexNames(
    (0, "SUPERMICRO-RSTP-MIB", "fsRstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsRstPortTrapNotificationEntry.setStatus("current")


class _FsRstPortTrapIndex_Type(Integer32):
    """Custom type fsRstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsRstPortTrapIndex_Type.__name__ = "Integer32"
_FsRstPortTrapIndex_Object = MibTableColumn
fsRstPortTrapIndex = _FsRstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1, 1),
    _FsRstPortTrapIndex_Type()
)
fsRstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRstPortTrapIndex.setStatus("current")


class _FsRstPortMigrationType_Type(Integer32):
    """Custom type fsRstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendstp", 0),
          ("sendrstp", 1))
    )


_FsRstPortMigrationType_Type.__name__ = "Integer32"
_FsRstPortMigrationType_Object = MibTableColumn
fsRstPortMigrationType = _FsRstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1, 2),
    _FsRstPortMigrationType_Type()
)
fsRstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortMigrationType.setStatus("current")


class _FsRstPktErrType_Type(Integer32):
    """Custom type fsRstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("protocolIdErr", 0),
          ("invalidBpdu", 1),
          ("configLengthErr", 2),
          ("tcnLengthErr", 3),
          ("rstpLengthErr", 4),
          ("maxAgeErr", 5),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7))
    )


_FsRstPktErrType_Type.__name__ = "Integer32"
_FsRstPktErrType_Object = MibTableColumn
fsRstPktErrType = _FsRstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1, 3),
    _FsRstPktErrType_Type()
)
fsRstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPktErrType.setStatus("current")
_FsRstPktErrVal_Type = Integer32
_FsRstPktErrVal_Object = MibTableColumn
fsRstPktErrVal = _FsRstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1, 4),
    _FsRstPktErrVal_Type()
)
fsRstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPktErrVal.setStatus("current")


class _FsRstPortRoleType_Type(Integer32):
    """Custom type fsRstPortRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsRstPortRoleType_Type.__name__ = "Integer32"
_FsRstPortRoleType_Object = MibTableColumn
fsRstPortRoleType = _FsRstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1, 5),
    _FsRstPortRoleType_Type()
)
fsRstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstPortRoleType.setStatus("current")


class _FsRstOldRoleType_Type(Integer32):
    """Custom type fsRstOldRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsRstOldRoleType_Type.__name__ = "Integer32"
_FsRstOldRoleType_Object = MibTableColumn
fsRstOldRoleType = _FsRstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 2, 4, 1, 6),
    _FsRstOldRoleType_Type()
)
fsRstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstOldRoleType.setStatus("current")
_Dot1wFutureRstTraps_ObjectIdentity = ObjectIdentity
dot1wFutureRstTraps = _Dot1wFutureRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3)
)
_FsRstTraps_ObjectIdentity = ObjectIdentity
fsRstTraps = _FsRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0)
)

# Managed Objects groups


# Notification objects

fsRstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 1)
)
fsRstGenTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("SUPERMICRO-RSTP-MIB", "fsRstGenTrapType"))
)
if mibBuilder.loadTexts:
    fsRstGenTrap.setStatus(
        "current"
    )

fsRstErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 2)
)
fsRstErrTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("SUPERMICRO-RSTP-MIB", "fsRstErrTrapType"))
)
if mibBuilder.loadTexts:
    fsRstErrTrap.setStatus(
        "current"
    )

fsRstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 3)
)
fsRstNewRootTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("SUPERMICRO-RSTP-MIB", "fsRstOldDesignatedRoot"),
        ("BRIDGE-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    fsRstNewRootTrap.setStatus(
        "current"
    )

fsRstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 4)
)
fsRstTopologyChgTrap.setObjects(
    ("BRIDGE-MIB", "dot1dBaseBridgeAddress")
)
if mibBuilder.loadTexts:
    fsRstTopologyChgTrap.setStatus(
        "current"
    )

fsRstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 5)
)
fsRstProtocolMigrationTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("RSTP-MIB", "dot1dStpVersion"),
        ("SUPERMICRO-RSTP-MIB", "fsRstPortMigrationType"))
)
if mibBuilder.loadTexts:
    fsRstProtocolMigrationTrap.setStatus(
        "current"
    )

fsRstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 6)
)
fsRstInvalidBpduRxdTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("SUPERMICRO-RSTP-MIB", "fsRstPktErrType"),
        ("SUPERMICRO-RSTP-MIB", "fsRstPktErrVal"))
)
if mibBuilder.loadTexts:
    fsRstInvalidBpduRxdTrap.setStatus(
        "current"
    )

fsRstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 7)
)
fsRstNewPortRoleTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("SUPERMICRO-RSTP-MIB", "fsRstPortRoleType"),
        ("SUPERMICRO-RSTP-MIB", "fsRstOldRoleType"))
)
if mibBuilder.loadTexts:
    fsRstNewPortRoleTrap.setStatus(
        "current"
    )

fsRstHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 79, 3, 0, 8)
)
fsRstHwFailureTrap.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("BRIDGE-MIB", "dot1dStpPortState"))
)
if mibBuilder.loadTexts:
    fsRstHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "futureRstMIB": futureRstMIB,
       "dot1wFutureRst": dot1wFutureRst,
       "fsRstSystemControl": fsRstSystemControl,
       "fsRstModuleStatus": fsRstModuleStatus,
       "fsRstTraceOption": fsRstTraceOption,
       "fsRstDebugOption": fsRstDebugOption,
       "fsRstRstpUpCount": fsRstRstpUpCount,
       "fsRstRstpDownCount": fsRstRstpDownCount,
       "fsRstBufferFailureCount": fsRstBufferFailureCount,
       "fsRstMemAllocFailureCount": fsRstMemAllocFailureCount,
       "fsRstNewRootIdCount": fsRstNewRootIdCount,
       "fsRstPortRoleSelSmState": fsRstPortRoleSelSmState,
       "fsRstOldDesignatedRoot": fsRstOldDesignatedRoot,
       "fsRstPortExtTable": fsRstPortExtTable,
       "fsRstPortExtEntry": fsRstPortExtEntry,
       "fsRstPort": fsRstPort,
       "fsRstPortRole": fsRstPortRole,
       "fsRstPortOperVersion": fsRstPortOperVersion,
       "fsRstPortInfoSmState": fsRstPortInfoSmState,
       "fsRstPortMigSmState": fsRstPortMigSmState,
       "fsRstPortRoleTransSmState": fsRstPortRoleTransSmState,
       "fsRstPortStateTransSmState": fsRstPortStateTransSmState,
       "fsRstPortTopoChSmState": fsRstPortTopoChSmState,
       "fsRstPortTxSmState": fsRstPortTxSmState,
       "fsRstPortRxRstBpduCount": fsRstPortRxRstBpduCount,
       "fsRstPortRxConfigBpduCount": fsRstPortRxConfigBpduCount,
       "fsRstPortRxTcnBpduCount": fsRstPortRxTcnBpduCount,
       "fsRstPortTxRstBpduCount": fsRstPortTxRstBpduCount,
       "fsRstPortTxConfigBpduCount": fsRstPortTxConfigBpduCount,
       "fsRstPortTxTcnBpduCount": fsRstPortTxTcnBpduCount,
       "fsRstPortInvalidRstBpduRxCount": fsRstPortInvalidRstBpduRxCount,
       "fsRstPortInvalidConfigBpduRxCount": fsRstPortInvalidConfigBpduRxCount,
       "fsRstPortInvalidTcnBpduRxCount": fsRstPortInvalidTcnBpduRxCount,
       "fsRstPortProtocolMigrationCount": fsRstPortProtocolMigrationCount,
       "fsRstPortEffectivePortState": fsRstPortEffectivePortState,
       "fsRstPortAutoEdge": fsRstPortAutoEdge,
       "fsRstPortRestrictedRole": fsRstPortRestrictedRole,
       "fsRstPortRestrictedTCN": fsRstPortRestrictedTCN,
       "fsRstPortEnableBPDURx": fsRstPortEnableBPDURx,
       "fsRstPortEnableBPDUTx": fsRstPortEnableBPDUTx,
       "fsRstPortPseudoRootId": fsRstPortPseudoRootId,
       "fsRstPortIsL2Gp": fsRstPortIsL2Gp,
       "fsRstPortLoopGuard": fsRstPortLoopGuard,
       "fsRstPortRcvdEvent": fsRstPortRcvdEvent,
       "fsRstPortRcvdEventSubType": fsRstPortRcvdEventSubType,
       "fsRstPortRcvdEventTimeStamp": fsRstPortRcvdEventTimeStamp,
       "fsRstPortStateChangeTimeStamp": fsRstPortStateChangeTimeStamp,
       "fsRstPortRowStatus": fsRstPortRowStatus,
       "fsRstPortBpduGuard": fsRstPortBpduGuard,
       "fsRstDynamicPathcostCalculation": fsRstDynamicPathcostCalculation,
       "fsRstCalcPortPathCostOnSpeedChg": fsRstCalcPortPathCostOnSpeedChg,
       "fsRstRcvdEvent": fsRstRcvdEvent,
       "fsRstRcvdEventSubType": fsRstRcvdEventSubType,
       "fsRstRcvdEventTimeStamp": fsRstRcvdEventTimeStamp,
       "fsRstRcvdPortStateChangeTimeStamp": fsRstRcvdPortStateChangeTimeStamp,
       "fsRstBpduGuard": fsRstBpduGuard,
       "dot1wFsRstTrapsControl": dot1wFsRstTrapsControl,
       "fsRstSetTraps": fsRstSetTraps,
       "fsRstGenTrapType": fsRstGenTrapType,
       "fsRstErrTrapType": fsRstErrTrapType,
       "fsRstPortTrapNotificationTable": fsRstPortTrapNotificationTable,
       "fsRstPortTrapNotificationEntry": fsRstPortTrapNotificationEntry,
       "fsRstPortTrapIndex": fsRstPortTrapIndex,
       "fsRstPortMigrationType": fsRstPortMigrationType,
       "fsRstPktErrType": fsRstPktErrType,
       "fsRstPktErrVal": fsRstPktErrVal,
       "fsRstPortRoleType": fsRstPortRoleType,
       "fsRstOldRoleType": fsRstOldRoleType,
       "dot1wFutureRstTraps": dot1wFutureRstTraps,
       "fsRstTraps": fsRstTraps,
       "fsRstGenTrap": fsRstGenTrap,
       "fsRstErrTrap": fsRstErrTrap,
       "fsRstNewRootTrap": fsRstNewRootTrap,
       "fsRstTopologyChgTrap": fsRstTopologyChgTrap,
       "fsRstProtocolMigrationTrap": fsRstProtocolMigrationTrap,
       "fsRstInvalidBpduRxdTrap": fsRstInvalidBpduRxdTrap,
       "fsRstNewPortRoleTrap": fsRstNewPortRoleTrap,
       "fsRstHwFailureTrap": fsRstHwFailureTrap}
)
