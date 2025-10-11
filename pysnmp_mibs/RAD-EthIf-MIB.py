# SNMP MIB module (RAD-EthIf-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-EthIf-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:18 2025
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

(dot3OamEntry,
 dot3OamLoopbackIgnoreRx,
 dot3OamLoopbackStatus,
 dot3OamOperStatus) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamEntry",
    "dot3OamLoopbackIgnoreRx",
    "dot3OamLoopbackStatus",
    "dot3OamOperStatus")

(InterfaceIndexOrZero,
 ifAlias,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifAlias",
    "ifDescr",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 prtTestCmdAndStatus) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "prtTestCmdAndStatus")

(diverseIfWanGen,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "diverseIfWanGen")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ethIf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthIfEvents_ObjectIdentity = ObjectIdentity
ethIfEvents = _EthIfEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0)
)
_EthIfTable_Object = MibTable
ethIfTable = _EthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ethIfTable.setStatus("current")
_EthIfEntry_Object = MibTableRow
ethIfEntry = _EthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1)
)
ethIfEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfIdx"),
)
if mibBuilder.loadTexts:
    ethIfEntry.setStatus("current")
_EthIfIdx_Type = Integer32
_EthIfIdx_Object = MibTableColumn
ethIfIdx = _EthIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 1),
    _EthIfIdx_Type()
)
ethIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIdx.setStatus("current")


class _EthMode_Type(Integer32):
    """Custom type ethMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2),
          ("notApplicable", 255))
    )


_EthMode_Type.__name__ = "Integer32"
_EthMode_Object = MibTableColumn
ethMode = _EthMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 2),
    _EthMode_Type()
)
ethMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMode.setStatus("current")


class _EthBridgingMode_Type(Integer32):
    """Custom type ethBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtered", 1),
          ("transparent", 2))
    )


_EthBridgingMode_Type.__name__ = "Integer32"
_EthBridgingMode_Object = MibTableColumn
ethBridgingMode = _EthBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 3),
    _EthBridgingMode_Type()
)
ethBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBridgingMode.setStatus("current")


class _EthEncapsulationCRCMode_Type(Integer32):
    """Custom type ethEncapsulationCRCMode based on Integer32"""
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
          ("withCRC", 2),
          ("withoutCRC", 3))
    )


_EthEncapsulationCRCMode_Type.__name__ = "Integer32"
_EthEncapsulationCRCMode_Object = MibTableColumn
ethEncapsulationCRCMode = _EthEncapsulationCRCMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 4),
    _EthEncapsulationCRCMode_Type()
)
ethEncapsulationCRCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethEncapsulationCRCMode.setStatus("current")


class _EthBackPressure_Type(Integer32):
    """Custom type ethBackPressure based on Integer32"""
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


_EthBackPressure_Type.__name__ = "Integer32"
_EthBackPressure_Object = MibTableColumn
ethBackPressure = _EthBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 5),
    _EthBackPressure_Type()
)
ethBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBackPressure.setStatus("current")


class _EthLimit4_Type(Integer32):
    """Custom type ethLimit4 based on Integer32"""
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


_EthLimit4_Type.__name__ = "Integer32"
_EthLimit4_Object = MibTableColumn
ethLimit4 = _EthLimit4_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 6),
    _EthLimit4_Type()
)
ethLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethLimit4.setStatus("current")


class _EthSkipInitReset_Type(Integer32):
    """Custom type ethSkipInitReset based on Integer32"""
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
          ("notSkip", 2),
          ("skip", 3))
    )


_EthSkipInitReset_Type.__name__ = "Integer32"
_EthSkipInitReset_Object = MibTableColumn
ethSkipInitReset = _EthSkipInitReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 7),
    _EthSkipInitReset_Type()
)
ethSkipInitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSkipInitReset.setStatus("current")


class _EthMulticastBlock_Type(Integer32):
    """Custom type ethMulticastBlock based on Integer32"""
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
          ("unBlock", 2),
          ("block", 3))
    )


_EthMulticastBlock_Type.__name__ = "Integer32"
_EthMulticastBlock_Object = MibTableColumn
ethMulticastBlock = _EthMulticastBlock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 8),
    _EthMulticastBlock_Type()
)
ethMulticastBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMulticastBlock.setStatus("current")


class _EthBroadcastBlock_Type(Integer32):
    """Custom type ethBroadcastBlock based on Integer32"""
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
          ("unBlock", 2),
          ("block", 3))
    )


_EthBroadcastBlock_Type.__name__ = "Integer32"
_EthBroadcastBlock_Object = MibTableColumn
ethBroadcastBlock = _EthBroadcastBlock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 9),
    _EthBroadcastBlock_Type()
)
ethBroadcastBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBroadcastBlock.setStatus("current")


class _EthSpeed_Type(Integer32):
    """Custom type ethSpeed based on Integer32"""
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
          ("s10Mbps", 2),
          ("s100Mbps", 3),
          ("s1Gbps", 4))
    )


_EthSpeed_Type.__name__ = "Integer32"
_EthSpeed_Object = MibTableColumn
ethSpeed = _EthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 10),
    _EthSpeed_Type()
)
ethSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSpeed.setStatus("current")


class _EthRip2_Type(Integer32):
    """Custom type ethRip2 based on Integer32"""
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


_EthRip2_Type.__name__ = "Integer32"
_EthRip2_Object = MibTableColumn
ethRip2 = _EthRip2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 11),
    _EthRip2_Type()
)
ethRip2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRip2.setStatus("current")


class _EthPortPriority_Type(Integer32):
    """Custom type ethPortPriority based on Integer32"""
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
          ("none", 2),
          ("fixed", 3))
    )


_EthPortPriority_Type.__name__ = "Integer32"
_EthPortPriority_Object = MibTableColumn
ethPortPriority = _EthPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 12),
    _EthPortPriority_Type()
)
ethPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortPriority.setStatus("current")


class _EthPortMngEnable_Type(Integer32):
    """Custom type ethPortMngEnable based on Integer32"""
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
          ("no", 2),
          ("yes", 3),
          ("localOnly", 4))
    )


_EthPortMngEnable_Type.__name__ = "Integer32"
_EthPortMngEnable_Object = MibTableColumn
ethPortMngEnable = _EthPortMngEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 13),
    _EthPortMngEnable_Type()
)
ethPortMngEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortMngEnable.setStatus("current")
_EthFlowCtrlMacAddress_Type = MacAddress
_EthFlowCtrlMacAddress_Object = MibTableColumn
ethFlowCtrlMacAddress = _EthFlowCtrlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 14),
    _EthFlowCtrlMacAddress_Type()
)
ethFlowCtrlMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFlowCtrlMacAddress.setStatus("current")
_EthRateLimit_Type = Integer32
_EthRateLimit_Object = MibTableColumn
ethRateLimit = _EthRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 15),
    _EthRateLimit_Type()
)
ethRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRateLimit.setStatus("current")


class _EthJumboFrameEnable_Type(Integer32):
    """Custom type ethJumboFrameEnable based on Integer32"""
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


_EthJumboFrameEnable_Type.__name__ = "Integer32"
_EthJumboFrameEnable_Object = MibTableColumn
ethJumboFrameEnable = _EthJumboFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 16),
    _EthJumboFrameEnable_Type()
)
ethJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethJumboFrameEnable.setStatus("current")


class _EthAutoMdiXEnable_Type(Integer32):
    """Custom type ethAutoMdiXEnable based on Integer32"""
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


_EthAutoMdiXEnable_Type.__name__ = "Integer32"
_EthAutoMdiXEnable_Object = MibTableColumn
ethAutoMdiXEnable = _EthAutoMdiXEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 17),
    _EthAutoMdiXEnable_Type()
)
ethAutoMdiXEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAutoMdiXEnable.setStatus("current")


class _EthPortDataEnable_Type(Integer32):
    """Custom type ethPortDataEnable based on Integer32"""
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


_EthPortDataEnable_Type.__name__ = "Integer32"
_EthPortDataEnable_Object = MibTableColumn
ethPortDataEnable = _EthPortDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 18),
    _EthPortDataEnable_Type()
)
ethPortDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortDataEnable.setStatus("current")
_EthIfUse_Type = Integer32
_EthIfUse_Object = MibTableColumn
ethIfUse = _EthIfUse_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 19),
    _EthIfUse_Type()
)
ethIfUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfUse.setStatus("current")


class _EthLineOam_Type(Integer32):
    """Custom type ethLineOam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("passive", 3))
    )


_EthLineOam_Type.__name__ = "Integer32"
_EthLineOam_Object = MibTableColumn
ethLineOam = _EthLineOam_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 20),
    _EthLineOam_Type()
)
ethLineOam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethLineOam.setStatus("current")


class _EthRoutingProtocol_Type(Integer32):
    """Custom type ethRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4),
          ("rip1and2", 6))
    )


_EthRoutingProtocol_Type.__name__ = "Integer32"
_EthRoutingProtocol_Object = MibTableColumn
ethRoutingProtocol = _EthRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 21),
    _EthRoutingProtocol_Type()
)
ethRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRoutingProtocol.setStatus("current")


class _EthMdiXManualSwitch_Type(Integer32):
    """Custom type ethMdiXManualSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossOver", 1),
          ("straightThrough", 2))
    )


_EthMdiXManualSwitch_Type.__name__ = "Integer32"
_EthMdiXManualSwitch_Object = MibTableColumn
ethMdiXManualSwitch = _EthMdiXManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 22),
    _EthMdiXManualSwitch_Type()
)
ethMdiXManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMdiXManualSwitch.setStatus("current")


class _EthDot1xEnable_Type(Integer32):
    """Custom type ethDot1xEnable based on Integer32"""
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


_EthDot1xEnable_Type.__name__ = "Integer32"
_EthDot1xEnable_Object = MibTableColumn
ethDot1xEnable = _EthDot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 23),
    _EthDot1xEnable_Type()
)
ethDot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot1xEnable.setStatus("current")


class _EthPartnerRateMode_Type(Integer32):
    """Custom type ethPartnerRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_EthPartnerRateMode_Type.__name__ = "Integer32"
_EthPartnerRateMode_Object = MibTableColumn
ethPartnerRateMode = _EthPartnerRateMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 24),
    _EthPartnerRateMode_Type()
)
ethPartnerRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPartnerRateMode.setStatus("current")


class _EthDot1xPortRole_Type(Integer32):
    """Custom type ethDot1xPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticator", 1),
          ("supplicant", 2))
    )


_EthDot1xPortRole_Type.__name__ = "Integer32"
_EthDot1xPortRole_Object = MibTableColumn
ethDot1xPortRole = _EthDot1xPortRole_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 25),
    _EthDot1xPortRole_Type()
)
ethDot1xPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot1xPortRole.setStatus("current")


class _EthDhcpRequest_Type(Integer32):
    """Custom type ethDhcpRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("never", 1),
          ("normal", 2),
          ("whenUp", 3))
    )


_EthDhcpRequest_Type.__name__ = "Integer32"
_EthDhcpRequest_Object = MibTableColumn
ethDhcpRequest = _EthDhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 26),
    _EthDhcpRequest_Type()
)
ethDhcpRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDhcpRequest.setStatus("current")


class _EthSfpCapabilities_Type(Bits):
    """Custom type ethSfpCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("speed10MFullAutoNegDisabled", 0),
          ("speed10MHalfAutoNegDisabled", 1),
          ("speed100MFullAutoNegDisabled", 2),
          ("speed100MHalfAutoNegDisabled", 3),
          ("speed1GFullAutoNegDisabled", 4),
          ("speed10GFullAutoNegDisabled", 5),
          ("autoNegConfigurable", 6),
          ("speed10MFullAutoNegEnabled", 7),
          ("speed10MHalfAutoNegEnabled", 8),
          ("speed100MFullAutoNegEnabled", 9),
          ("speed100MHalfAutoNegEnabled", 10),
          ("speed1GFullAutoNegEnabled", 11),
          ("speed10GFullAutoNegEnabled", 12),
          ("maxCapabilitiesAdvertised", 13),
          ("flowControlSupport", 14),
          ("sfpOpticInterface", 15))
    )

_EthSfpCapabilities_Type.__name__ = "Bits"
_EthSfpCapabilities_Object = MibTableColumn
ethSfpCapabilities = _EthSfpCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 1, 1, 27),
    _EthSfpCapabilities_Type()
)
ethSfpCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSfpCapabilities.setStatus("current")
_EthIfPerformance_ObjectIdentity = ObjectIdentity
ethIfPerformance = _EthIfPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2)
)
_EthIfCurrentTable_Object = MibTable
ethIfCurrentTable = _EthIfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ethIfCurrentTable.setStatus("current")
_EthIfCurrentEntry_Object = MibTableRow
ethIfCurrentEntry = _EthIfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1)
)
ethIfCurrentEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfCurrentIndex"),
)
if mibBuilder.loadTexts:
    ethIfCurrentEntry.setStatus("current")
_EthIfCurrentIndex_Type = Integer32
_EthIfCurrentIndex_Object = MibTableColumn
ethIfCurrentIndex = _EthIfCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 1),
    _EthIfCurrentIndex_Type()
)
ethIfCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentIndex.setStatus("current")


class _EthIfCurrentStatus_Type(OctetString):
    """Custom type ethIfCurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_EthIfCurrentStatus_Type.__name__ = "OctetString"
_EthIfCurrentStatus_Object = MibTableColumn
ethIfCurrentStatus = _EthIfCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 2),
    _EthIfCurrentStatus_Type()
)
ethIfCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentStatus.setStatus("current")
_EthIfCurrentInFrames_Type = Gauge32
_EthIfCurrentInFrames_Object = MibTableColumn
ethIfCurrentInFrames = _EthIfCurrentInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 3),
    _EthIfCurrentInFrames_Type()
)
ethIfCurrentInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInFrames.setStatus("current")
_EthIfCurrentInOctets_Type = Gauge32
_EthIfCurrentInOctets_Object = MibTableColumn
ethIfCurrentInOctets = _EthIfCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 4),
    _EthIfCurrentInOctets_Type()
)
ethIfCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInOctets.setStatus("current")
_EthIfCurrentAlignmentErrors_Type = Gauge32
_EthIfCurrentAlignmentErrors_Object = MibTableColumn
ethIfCurrentAlignmentErrors = _EthIfCurrentAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 5),
    _EthIfCurrentAlignmentErrors_Type()
)
ethIfCurrentAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentAlignmentErrors.setStatus("current")
_EthIfCurrentFCSErrors_Type = Gauge32
_EthIfCurrentFCSErrors_Object = MibTableColumn
ethIfCurrentFCSErrors = _EthIfCurrentFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 6),
    _EthIfCurrentFCSErrors_Type()
)
ethIfCurrentFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentFCSErrors.setStatus("current")
_EthIfCurrentLengthError_Type = Gauge32
_EthIfCurrentLengthError_Object = MibTableColumn
ethIfCurrentLengthError = _EthIfCurrentLengthError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 7),
    _EthIfCurrentLengthError_Type()
)
ethIfCurrentLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentLengthError.setStatus("current")
_EthIfCurrentOutFrames_Type = Gauge32
_EthIfCurrentOutFrames_Object = MibTableColumn
ethIfCurrentOutFrames = _EthIfCurrentOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 8),
    _EthIfCurrentOutFrames_Type()
)
ethIfCurrentOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutFrames.setStatus("current")
_EthIfCurrentOutOctets_Type = Gauge32
_EthIfCurrentOutOctets_Object = MibTableColumn
ethIfCurrentOutOctets = _EthIfCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 9),
    _EthIfCurrentOutOctets_Type()
)
ethIfCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutOctets.setStatus("current")
_EthIfCurrentSingleCollisionFrames_Type = Gauge32
_EthIfCurrentSingleCollisionFrames_Object = MibTableColumn
ethIfCurrentSingleCollisionFrames = _EthIfCurrentSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 10),
    _EthIfCurrentSingleCollisionFrames_Type()
)
ethIfCurrentSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentSingleCollisionFrames.setStatus("current")
_EthIfCurrentMultipleCollisionFrames_Type = Gauge32
_EthIfCurrentMultipleCollisionFrames_Object = MibTableColumn
ethIfCurrentMultipleCollisionFrames = _EthIfCurrentMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 11),
    _EthIfCurrentMultipleCollisionFrames_Type()
)
ethIfCurrentMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentMultipleCollisionFrames.setStatus("current")
_EthIfCurrentDeferredTransmissions_Type = Gauge32
_EthIfCurrentDeferredTransmissions_Object = MibTableColumn
ethIfCurrentDeferredTransmissions = _EthIfCurrentDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 12),
    _EthIfCurrentDeferredTransmissions_Type()
)
ethIfCurrentDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentDeferredTransmissions.setStatus("current")
_EthIfCurrentLateCollisions_Type = Gauge32
_EthIfCurrentLateCollisions_Object = MibTableColumn
ethIfCurrentLateCollisions = _EthIfCurrentLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 13),
    _EthIfCurrentLateCollisions_Type()
)
ethIfCurrentLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentLateCollisions.setStatus("current")
_EthIfCurrentCarrierSenseErrors_Type = Gauge32
_EthIfCurrentCarrierSenseErrors_Object = MibTableColumn
ethIfCurrentCarrierSenseErrors = _EthIfCurrentCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 14),
    _EthIfCurrentCarrierSenseErrors_Type()
)
ethIfCurrentCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentCarrierSenseErrors.setStatus("current")
_EthIfCurrentInputCongestionDropped_Type = Gauge32
_EthIfCurrentInputCongestionDropped_Object = MibTableColumn
ethIfCurrentInputCongestionDropped = _EthIfCurrentInputCongestionDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 15),
    _EthIfCurrentInputCongestionDropped_Type()
)
ethIfCurrentInputCongestionDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInputCongestionDropped.setStatus("current")
_EthIfCurrentOutputCongestionDropped_Type = Gauge32
_EthIfCurrentOutputCongestionDropped_Object = MibTableColumn
ethIfCurrentOutputCongestionDropped = _EthIfCurrentOutputCongestionDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 16),
    _EthIfCurrentOutputCongestionDropped_Type()
)
ethIfCurrentOutputCongestionDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutputCongestionDropped.setStatus("current")
_EthIfCurrentOverflowInFrames_Type = Gauge32
_EthIfCurrentOverflowInFrames_Object = MibTableColumn
ethIfCurrentOverflowInFrames = _EthIfCurrentOverflowInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 17),
    _EthIfCurrentOverflowInFrames_Type()
)
ethIfCurrentOverflowInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInFrames.setStatus("current")
_EthIfCurrentOverflowInOctets_Type = Gauge32
_EthIfCurrentOverflowInOctets_Object = MibTableColumn
ethIfCurrentOverflowInOctets = _EthIfCurrentOverflowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 18),
    _EthIfCurrentOverflowInOctets_Type()
)
ethIfCurrentOverflowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInOctets.setStatus("current")
_EthIfCurrentOverflowFCSErrors_Type = Gauge32
_EthIfCurrentOverflowFCSErrors_Object = MibTableColumn
ethIfCurrentOverflowFCSErrors = _EthIfCurrentOverflowFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 19),
    _EthIfCurrentOverflowFCSErrors_Type()
)
ethIfCurrentOverflowFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowFCSErrors.setStatus("current")
_EthIfCurrentOverflowOutFrames_Type = Gauge32
_EthIfCurrentOverflowOutFrames_Object = MibTableColumn
ethIfCurrentOverflowOutFrames = _EthIfCurrentOverflowOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 20),
    _EthIfCurrentOverflowOutFrames_Type()
)
ethIfCurrentOverflowOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutFrames.setStatus("current")
_EthIfCurrentOverflowOutOctets_Type = Gauge32
_EthIfCurrentOverflowOutOctets_Object = MibTableColumn
ethIfCurrentOverflowOutOctets = _EthIfCurrentOverflowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 21),
    _EthIfCurrentOverflowOutOctets_Type()
)
ethIfCurrentOverflowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutOctets.setStatus("current")
_EthIfCurrentOverflowMultipleCollisionFrames_Type = Gauge32
_EthIfCurrentOverflowMultipleCollisionFrames_Object = MibTableColumn
ethIfCurrentOverflowMultipleCollisionFrames = _EthIfCurrentOverflowMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 22),
    _EthIfCurrentOverflowMultipleCollisionFrames_Type()
)
ethIfCurrentOverflowMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowMultipleCollisionFrames.setStatus("current")
_EthIfCurrentInUnicastFrames_Type = Gauge32
_EthIfCurrentInUnicastFrames_Object = MibTableColumn
ethIfCurrentInUnicastFrames = _EthIfCurrentInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 23),
    _EthIfCurrentInUnicastFrames_Type()
)
ethIfCurrentInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInUnicastFrames.setStatus("current")
_EthIfCurrentOutUnicastFrames_Type = Gauge32
_EthIfCurrentOutUnicastFrames_Object = MibTableColumn
ethIfCurrentOutUnicastFrames = _EthIfCurrentOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 24),
    _EthIfCurrentOutUnicastFrames_Type()
)
ethIfCurrentOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutUnicastFrames.setStatus("current")
_EthIfCurrentInMulticastFrames_Type = Gauge32
_EthIfCurrentInMulticastFrames_Object = MibTableColumn
ethIfCurrentInMulticastFrames = _EthIfCurrentInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 25),
    _EthIfCurrentInMulticastFrames_Type()
)
ethIfCurrentInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInMulticastFrames.setStatus("current")
_EthIfCurrentOutMulticastFrames_Type = Gauge32
_EthIfCurrentOutMulticastFrames_Object = MibTableColumn
ethIfCurrentOutMulticastFrames = _EthIfCurrentOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 26),
    _EthIfCurrentOutMulticastFrames_Type()
)
ethIfCurrentOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutMulticastFrames.setStatus("current")
_EthIfCurrentInBroadcastFrames_Type = Gauge32
_EthIfCurrentInBroadcastFrames_Object = MibTableColumn
ethIfCurrentInBroadcastFrames = _EthIfCurrentInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 27),
    _EthIfCurrentInBroadcastFrames_Type()
)
ethIfCurrentInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInBroadcastFrames.setStatus("current")
_EthIfCurrentOutBroadcastFrames_Type = Gauge32
_EthIfCurrentOutBroadcastFrames_Object = MibTableColumn
ethIfCurrentOutBroadcastFrames = _EthIfCurrentOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 28),
    _EthIfCurrentOutBroadcastFrames_Type()
)
ethIfCurrentOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutBroadcastFrames.setStatus("current")
_EthIfCurrentInDiscardFrames_Type = Gauge32
_EthIfCurrentInDiscardFrames_Object = MibTableColumn
ethIfCurrentInDiscardFrames = _EthIfCurrentInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 29),
    _EthIfCurrentInDiscardFrames_Type()
)
ethIfCurrentInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInDiscardFrames.setStatus("current")
_EthIfCurrentOutDiscardFrames_Type = Gauge32
_EthIfCurrentOutDiscardFrames_Object = MibTableColumn
ethIfCurrentOutDiscardFrames = _EthIfCurrentOutDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 30),
    _EthIfCurrentOutDiscardFrames_Type()
)
ethIfCurrentOutDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutDiscardFrames.setStatus("current")
_EthIfCurrentInPauseFrames_Type = Gauge32
_EthIfCurrentInPauseFrames_Object = MibTableColumn
ethIfCurrentInPauseFrames = _EthIfCurrentInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 31),
    _EthIfCurrentInPauseFrames_Type()
)
ethIfCurrentInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentInPauseFrames.setStatus("current")
_EthIfCurrentOutPauseFrames_Type = Gauge32
_EthIfCurrentOutPauseFrames_Object = MibTableColumn
ethIfCurrentOutPauseFrames = _EthIfCurrentOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 32),
    _EthIfCurrentOutPauseFrames_Type()
)
ethIfCurrentOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOutPauseFrames.setStatus("current")
_EthIfCurrentOverflowInUnicastFrames_Type = Gauge32
_EthIfCurrentOverflowInUnicastFrames_Object = MibTableColumn
ethIfCurrentOverflowInUnicastFrames = _EthIfCurrentOverflowInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 33),
    _EthIfCurrentOverflowInUnicastFrames_Type()
)
ethIfCurrentOverflowInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInUnicastFrames.setStatus("current")
_EthIfCurrentOverflowOutUnicastFrames_Type = Gauge32
_EthIfCurrentOverflowOutUnicastFrames_Object = MibTableColumn
ethIfCurrentOverflowOutUnicastFrames = _EthIfCurrentOverflowOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 34),
    _EthIfCurrentOverflowOutUnicastFrames_Type()
)
ethIfCurrentOverflowOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutUnicastFrames.setStatus("current")
_EthIfCurrentOverflowInMulticastFrames_Type = Gauge32
_EthIfCurrentOverflowInMulticastFrames_Object = MibTableColumn
ethIfCurrentOverflowInMulticastFrames = _EthIfCurrentOverflowInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 35),
    _EthIfCurrentOverflowInMulticastFrames_Type()
)
ethIfCurrentOverflowInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInMulticastFrames.setStatus("current")
_EthIfCurrentOverflowOutMulticastFrames_Type = Gauge32
_EthIfCurrentOverflowOutMulticastFrames_Object = MibTableColumn
ethIfCurrentOverflowOutMulticastFrames = _EthIfCurrentOverflowOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 36),
    _EthIfCurrentOverflowOutMulticastFrames_Type()
)
ethIfCurrentOverflowOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutMulticastFrames.setStatus("current")
_EthIfCurrentOverflowInBroadcastFrames_Type = Gauge32
_EthIfCurrentOverflowInBroadcastFrames_Object = MibTableColumn
ethIfCurrentOverflowInBroadcastFrames = _EthIfCurrentOverflowInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 37),
    _EthIfCurrentOverflowInBroadcastFrames_Type()
)
ethIfCurrentOverflowInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInBroadcastFrames.setStatus("current")
_EthIfCurrentOverflowOutBroadcastFrames_Type = Gauge32
_EthIfCurrentOverflowOutBroadcastFrames_Object = MibTableColumn
ethIfCurrentOverflowOutBroadcastFrames = _EthIfCurrentOverflowOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 38),
    _EthIfCurrentOverflowOutBroadcastFrames_Type()
)
ethIfCurrentOverflowOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutBroadcastFrames.setStatus("current")
_EthIfCurrentOverflowInDiscardFrames_Type = Gauge32
_EthIfCurrentOverflowInDiscardFrames_Object = MibTableColumn
ethIfCurrentOverflowInDiscardFrames = _EthIfCurrentOverflowInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 39),
    _EthIfCurrentOverflowInDiscardFrames_Type()
)
ethIfCurrentOverflowInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInDiscardFrames.setStatus("current")
_EthIfCurrentOverflowOutDiscardFrames_Type = Gauge32
_EthIfCurrentOverflowOutDiscardFrames_Object = MibTableColumn
ethIfCurrentOverflowOutDiscardFrames = _EthIfCurrentOverflowOutDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 40),
    _EthIfCurrentOverflowOutDiscardFrames_Type()
)
ethIfCurrentOverflowOutDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutDiscardFrames.setStatus("current")
_EthIfCurrentOverflowInPauseFrames_Type = Gauge32
_EthIfCurrentOverflowInPauseFrames_Object = MibTableColumn
ethIfCurrentOverflowInPauseFrames = _EthIfCurrentOverflowInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 41),
    _EthIfCurrentOverflowInPauseFrames_Type()
)
ethIfCurrentOverflowInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowInPauseFrames.setStatus("current")
_EthIfCurrentOverflowOutPauseFrames_Type = Gauge32
_EthIfCurrentOverflowOutPauseFrames_Object = MibTableColumn
ethIfCurrentOverflowOutPauseFrames = _EthIfCurrentOverflowOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 1, 1, 42),
    _EthIfCurrentOverflowOutPauseFrames_Type()
)
ethIfCurrentOverflowOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfCurrentOverflowOutPauseFrames.setStatus("current")
_EthIfIntervalTable_Object = MibTable
ethIfIntervalTable = _EthIfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ethIfIntervalTable.setStatus("current")
_EthIfIntervalEntry_Object = MibTableRow
ethIfIntervalEntry = _EthIfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1)
)
ethIfIntervalEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfIntervalIndex"),
    (0, "RAD-EthIf-MIB", "ethIfIntervalNumber"),
)
if mibBuilder.loadTexts:
    ethIfIntervalEntry.setStatus("current")
_EthIfIntervalIndex_Type = Integer32
_EthIfIntervalIndex_Object = MibTableColumn
ethIfIntervalIndex = _EthIfIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 1),
    _EthIfIntervalIndex_Type()
)
ethIfIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalIndex.setStatus("current")


class _EthIfIntervalNumber_Type(Integer32):
    """Custom type ethIfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EthIfIntervalNumber_Type.__name__ = "Integer32"
_EthIfIntervalNumber_Object = MibTableColumn
ethIfIntervalNumber = _EthIfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 2),
    _EthIfIntervalNumber_Type()
)
ethIfIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalNumber.setStatus("current")


class _EthIfIntervalStatus_Type(OctetString):
    """Custom type ethIfIntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_EthIfIntervalStatus_Type.__name__ = "OctetString"
_EthIfIntervalStatus_Object = MibTableColumn
ethIfIntervalStatus = _EthIfIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 3),
    _EthIfIntervalStatus_Type()
)
ethIfIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalStatus.setStatus("current")
_EthIfIntervalInFrames_Type = Gauge32
_EthIfIntervalInFrames_Object = MibTableColumn
ethIfIntervalInFrames = _EthIfIntervalInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 4),
    _EthIfIntervalInFrames_Type()
)
ethIfIntervalInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInFrames.setStatus("current")
_EthIfIntervalInOctets_Type = Gauge32
_EthIfIntervalInOctets_Object = MibTableColumn
ethIfIntervalInOctets = _EthIfIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 5),
    _EthIfIntervalInOctets_Type()
)
ethIfIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInOctets.setStatus("current")
_EthIfIntervalAlignmentErrors_Type = Gauge32
_EthIfIntervalAlignmentErrors_Object = MibTableColumn
ethIfIntervalAlignmentErrors = _EthIfIntervalAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 6),
    _EthIfIntervalAlignmentErrors_Type()
)
ethIfIntervalAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalAlignmentErrors.setStatus("current")
_EthIfIntervalFCSErrors_Type = Gauge32
_EthIfIntervalFCSErrors_Object = MibTableColumn
ethIfIntervalFCSErrors = _EthIfIntervalFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 7),
    _EthIfIntervalFCSErrors_Type()
)
ethIfIntervalFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalFCSErrors.setStatus("current")
_EthIfIntervalLengthError_Type = Gauge32
_EthIfIntervalLengthError_Object = MibTableColumn
ethIfIntervalLengthError = _EthIfIntervalLengthError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 8),
    _EthIfIntervalLengthError_Type()
)
ethIfIntervalLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalLengthError.setStatus("current")
_EthIfIntervalOutFrames_Type = Gauge32
_EthIfIntervalOutFrames_Object = MibTableColumn
ethIfIntervalOutFrames = _EthIfIntervalOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 9),
    _EthIfIntervalOutFrames_Type()
)
ethIfIntervalOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutFrames.setStatus("current")
_EthIfIntervalOutOctets_Type = Gauge32
_EthIfIntervalOutOctets_Object = MibTableColumn
ethIfIntervalOutOctets = _EthIfIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 10),
    _EthIfIntervalOutOctets_Type()
)
ethIfIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutOctets.setStatus("current")
_EthIfIntervalSingleCollisionFrames_Type = Gauge32
_EthIfIntervalSingleCollisionFrames_Object = MibTableColumn
ethIfIntervalSingleCollisionFrames = _EthIfIntervalSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 11),
    _EthIfIntervalSingleCollisionFrames_Type()
)
ethIfIntervalSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalSingleCollisionFrames.setStatus("current")
_EthIfIntervalMultipleCollisionFrames_Type = Gauge32
_EthIfIntervalMultipleCollisionFrames_Object = MibTableColumn
ethIfIntervalMultipleCollisionFrames = _EthIfIntervalMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 12),
    _EthIfIntervalMultipleCollisionFrames_Type()
)
ethIfIntervalMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalMultipleCollisionFrames.setStatus("current")
_EthIfIntervalDeferredTransmissions_Type = Gauge32
_EthIfIntervalDeferredTransmissions_Object = MibTableColumn
ethIfIntervalDeferredTransmissions = _EthIfIntervalDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 13),
    _EthIfIntervalDeferredTransmissions_Type()
)
ethIfIntervalDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalDeferredTransmissions.setStatus("current")
_EthIfIntervalLateCollisions_Type = Gauge32
_EthIfIntervalLateCollisions_Object = MibTableColumn
ethIfIntervalLateCollisions = _EthIfIntervalLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 14),
    _EthIfIntervalLateCollisions_Type()
)
ethIfIntervalLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalLateCollisions.setStatus("current")
_EthIfIntervalCarrierSenseErrors_Type = Gauge32
_EthIfIntervalCarrierSenseErrors_Object = MibTableColumn
ethIfIntervalCarrierSenseErrors = _EthIfIntervalCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 15),
    _EthIfIntervalCarrierSenseErrors_Type()
)
ethIfIntervalCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalCarrierSenseErrors.setStatus("current")
_EthIfIntervalInputCongestionDropped_Type = Gauge32
_EthIfIntervalInputCongestionDropped_Object = MibTableColumn
ethIfIntervalInputCongestionDropped = _EthIfIntervalInputCongestionDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 16),
    _EthIfIntervalInputCongestionDropped_Type()
)
ethIfIntervalInputCongestionDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInputCongestionDropped.setStatus("current")
_EthIfIntervalOutputCongestionDropped_Type = Gauge32
_EthIfIntervalOutputCongestionDropped_Object = MibTableColumn
ethIfIntervalOutputCongestionDropped = _EthIfIntervalOutputCongestionDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 17),
    _EthIfIntervalOutputCongestionDropped_Type()
)
ethIfIntervalOutputCongestionDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutputCongestionDropped.setStatus("current")
_EthIfIntervalOverflowInFrames_Type = Gauge32
_EthIfIntervalOverflowInFrames_Object = MibTableColumn
ethIfIntervalOverflowInFrames = _EthIfIntervalOverflowInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 18),
    _EthIfIntervalOverflowInFrames_Type()
)
ethIfIntervalOverflowInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInFrames.setStatus("current")
_EthIfIntervalOverflowInOctets_Type = Gauge32
_EthIfIntervalOverflowInOctets_Object = MibTableColumn
ethIfIntervalOverflowInOctets = _EthIfIntervalOverflowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 19),
    _EthIfIntervalOverflowInOctets_Type()
)
ethIfIntervalOverflowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInOctets.setStatus("current")
_EthIfIntervalOverflowFCSErrors_Type = Gauge32
_EthIfIntervalOverflowFCSErrors_Object = MibTableColumn
ethIfIntervalOverflowFCSErrors = _EthIfIntervalOverflowFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 20),
    _EthIfIntervalOverflowFCSErrors_Type()
)
ethIfIntervalOverflowFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowFCSErrors.setStatus("current")
_EthIfIntervalOverflowOutFrames_Type = Gauge32
_EthIfIntervalOverflowOutFrames_Object = MibTableColumn
ethIfIntervalOverflowOutFrames = _EthIfIntervalOverflowOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 21),
    _EthIfIntervalOverflowOutFrames_Type()
)
ethIfIntervalOverflowOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutFrames.setStatus("current")
_EthIfIntervalOverflowOutOctets_Type = Gauge32
_EthIfIntervalOverflowOutOctets_Object = MibTableColumn
ethIfIntervalOverflowOutOctets = _EthIfIntervalOverflowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 22),
    _EthIfIntervalOverflowOutOctets_Type()
)
ethIfIntervalOverflowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutOctets.setStatus("current")
_EthIfIntervalOverflowMultipleCollisionFrames_Type = Gauge32
_EthIfIntervalOverflowMultipleCollisionFrames_Object = MibTableColumn
ethIfIntervalOverflowMultipleCollisionFrames = _EthIfIntervalOverflowMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 23),
    _EthIfIntervalOverflowMultipleCollisionFrames_Type()
)
ethIfIntervalOverflowMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowMultipleCollisionFrames.setStatus("current")
_EthIfIntervalInUnicastFrames_Type = Gauge32
_EthIfIntervalInUnicastFrames_Object = MibTableColumn
ethIfIntervalInUnicastFrames = _EthIfIntervalInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 24),
    _EthIfIntervalInUnicastFrames_Type()
)
ethIfIntervalInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInUnicastFrames.setStatus("current")
_EthIfIntervalOutUnicastFrames_Type = Gauge32
_EthIfIntervalOutUnicastFrames_Object = MibTableColumn
ethIfIntervalOutUnicastFrames = _EthIfIntervalOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 25),
    _EthIfIntervalOutUnicastFrames_Type()
)
ethIfIntervalOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutUnicastFrames.setStatus("current")
_EthIfIntervalInMulticastFrames_Type = Gauge32
_EthIfIntervalInMulticastFrames_Object = MibTableColumn
ethIfIntervalInMulticastFrames = _EthIfIntervalInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 26),
    _EthIfIntervalInMulticastFrames_Type()
)
ethIfIntervalInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInMulticastFrames.setStatus("current")
_EthIfIntervalOutMulticastFrames_Type = Gauge32
_EthIfIntervalOutMulticastFrames_Object = MibTableColumn
ethIfIntervalOutMulticastFrames = _EthIfIntervalOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 27),
    _EthIfIntervalOutMulticastFrames_Type()
)
ethIfIntervalOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutMulticastFrames.setStatus("current")
_EthIfIntervalInBroadcastFrames_Type = Gauge32
_EthIfIntervalInBroadcastFrames_Object = MibTableColumn
ethIfIntervalInBroadcastFrames = _EthIfIntervalInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 28),
    _EthIfIntervalInBroadcastFrames_Type()
)
ethIfIntervalInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInBroadcastFrames.setStatus("current")
_EthIfIntervalOutBroadcastFrames_Type = Gauge32
_EthIfIntervalOutBroadcastFrames_Object = MibTableColumn
ethIfIntervalOutBroadcastFrames = _EthIfIntervalOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 29),
    _EthIfIntervalOutBroadcastFrames_Type()
)
ethIfIntervalOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutBroadcastFrames.setStatus("current")
_EthIfIntervalInDiscardFrames_Type = Gauge32
_EthIfIntervalInDiscardFrames_Object = MibTableColumn
ethIfIntervalInDiscardFrames = _EthIfIntervalInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 30),
    _EthIfIntervalInDiscardFrames_Type()
)
ethIfIntervalInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInDiscardFrames.setStatus("current")
_EthIfIntervalOutDiscardFrames_Type = Gauge32
_EthIfIntervalOutDiscardFrames_Object = MibTableColumn
ethIfIntervalOutDiscardFrames = _EthIfIntervalOutDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 31),
    _EthIfIntervalOutDiscardFrames_Type()
)
ethIfIntervalOutDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutDiscardFrames.setStatus("current")
_EthIfIntervalInPauseFrames_Type = Gauge32
_EthIfIntervalInPauseFrames_Object = MibTableColumn
ethIfIntervalInPauseFrames = _EthIfIntervalInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 32),
    _EthIfIntervalInPauseFrames_Type()
)
ethIfIntervalInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalInPauseFrames.setStatus("current")
_EthIfIntervalOutPauseFrames_Type = Gauge32
_EthIfIntervalOutPauseFrames_Object = MibTableColumn
ethIfIntervalOutPauseFrames = _EthIfIntervalOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 33),
    _EthIfIntervalOutPauseFrames_Type()
)
ethIfIntervalOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOutPauseFrames.setStatus("current")
_EthIfIntervalOverflowInUnicastFrames_Type = Gauge32
_EthIfIntervalOverflowInUnicastFrames_Object = MibTableColumn
ethIfIntervalOverflowInUnicastFrames = _EthIfIntervalOverflowInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 34),
    _EthIfIntervalOverflowInUnicastFrames_Type()
)
ethIfIntervalOverflowInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInUnicastFrames.setStatus("current")
_EthIfIntervalOverflowOutUnicastFrames_Type = Gauge32
_EthIfIntervalOverflowOutUnicastFrames_Object = MibTableColumn
ethIfIntervalOverflowOutUnicastFrames = _EthIfIntervalOverflowOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 35),
    _EthIfIntervalOverflowOutUnicastFrames_Type()
)
ethIfIntervalOverflowOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutUnicastFrames.setStatus("current")
_EthIfIntervalOverflowInMulticastFrames_Type = Gauge32
_EthIfIntervalOverflowInMulticastFrames_Object = MibTableColumn
ethIfIntervalOverflowInMulticastFrames = _EthIfIntervalOverflowInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 36),
    _EthIfIntervalOverflowInMulticastFrames_Type()
)
ethIfIntervalOverflowInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInMulticastFrames.setStatus("current")
_EthIfIntervalOverflowOutMulticastFrames_Type = Gauge32
_EthIfIntervalOverflowOutMulticastFrames_Object = MibTableColumn
ethIfIntervalOverflowOutMulticastFrames = _EthIfIntervalOverflowOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 37),
    _EthIfIntervalOverflowOutMulticastFrames_Type()
)
ethIfIntervalOverflowOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutMulticastFrames.setStatus("current")
_EthIfIntervalOverflowInBroadcastFrames_Type = Gauge32
_EthIfIntervalOverflowInBroadcastFrames_Object = MibTableColumn
ethIfIntervalOverflowInBroadcastFrames = _EthIfIntervalOverflowInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 38),
    _EthIfIntervalOverflowInBroadcastFrames_Type()
)
ethIfIntervalOverflowInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInBroadcastFrames.setStatus("current")
_EthIfIntervalOverflowOutBroadcastFrames_Type = Gauge32
_EthIfIntervalOverflowOutBroadcastFrames_Object = MibTableColumn
ethIfIntervalOverflowOutBroadcastFrames = _EthIfIntervalOverflowOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 39),
    _EthIfIntervalOverflowOutBroadcastFrames_Type()
)
ethIfIntervalOverflowOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutBroadcastFrames.setStatus("current")
_EthIfIntervalOverflowInDiscardFrames_Type = Gauge32
_EthIfIntervalOverflowInDiscardFrames_Object = MibTableColumn
ethIfIntervalOverflowInDiscardFrames = _EthIfIntervalOverflowInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 40),
    _EthIfIntervalOverflowInDiscardFrames_Type()
)
ethIfIntervalOverflowInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInDiscardFrames.setStatus("current")
_EthIfIntervalOverflowOutDiscardFrames_Type = Gauge32
_EthIfIntervalOverflowOutDiscardFrames_Object = MibTableColumn
ethIfIntervalOverflowOutDiscardFrames = _EthIfIntervalOverflowOutDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 41),
    _EthIfIntervalOverflowOutDiscardFrames_Type()
)
ethIfIntervalOverflowOutDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutDiscardFrames.setStatus("current")
_EthIfIntervalOverflowInPauseFrames_Type = Gauge32
_EthIfIntervalOverflowInPauseFrames_Object = MibTableColumn
ethIfIntervalOverflowInPauseFrames = _EthIfIntervalOverflowInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 42),
    _EthIfIntervalOverflowInPauseFrames_Type()
)
ethIfIntervalOverflowInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowInPauseFrames.setStatus("current")
_EthIfIntervalOverflowOutPauseFrames_Type = Gauge32
_EthIfIntervalOverflowOutPauseFrames_Object = MibTableColumn
ethIfIntervalOverflowOutPauseFrames = _EthIfIntervalOverflowOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 2, 1, 43),
    _EthIfIntervalOverflowOutPauseFrames_Type()
)
ethIfIntervalOverflowOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIntervalOverflowOutPauseFrames.setStatus("current")


class _EthPerformanceMode_Type(Integer32):
    """Custom type ethPerformanceMode based on Integer32"""
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
          ("countOK", 2),
          ("countFail", 3))
    )


_EthPerformanceMode_Type.__name__ = "Integer32"
_EthPerformanceMode_Object = MibScalar
ethPerformanceMode = _EthPerformanceMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 3),
    _EthPerformanceMode_Type()
)
ethPerformanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPerformanceMode.setStatus("current")
_EthIfPerfTable_Object = MibTable
ethIfPerfTable = _EthIfPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ethIfPerfTable.setStatus("current")
_EthIfPerfEntry_Object = MibTableRow
ethIfPerfEntry = _EthIfPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 4, 1)
)
ethIfPerfEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfIdx"),
)
if mibBuilder.loadTexts:
    ethIfPerfEntry.setStatus("current")
_EthIfPerfInOkFrames_Type = Gauge32
_EthIfPerfInOkFrames_Object = MibTableColumn
ethIfPerfInOkFrames = _EthIfPerfInOkFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 4, 1, 1),
    _EthIfPerfInOkFrames_Type()
)
ethIfPerfInOkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfPerfInOkFrames.setStatus("current")
_EthIfPerfOutOkFrames_Type = Gauge32
_EthIfPerfOutOkFrames_Object = MibTableColumn
ethIfPerfOutOkFrames = _EthIfPerfOutOkFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 4, 1, 2),
    _EthIfPerfOutOkFrames_Type()
)
ethIfPerfOutOkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfPerfOutOkFrames.setStatus("current")
_EthIfPerfTotalCollisions_Type = Gauge32
_EthIfPerfTotalCollisions_Object = MibTableColumn
ethIfPerfTotalCollisions = _EthIfPerfTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 4, 1, 3),
    _EthIfPerfTotalCollisions_Type()
)
ethIfPerfTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfPerfTotalCollisions.setStatus("current")
_EthIfPerfInOkOctets_Type = Gauge32
_EthIfPerfInOkOctets_Object = MibTableColumn
ethIfPerfInOkOctets = _EthIfPerfInOkOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 4, 1, 4),
    _EthIfPerfInOkOctets_Type()
)
ethIfPerfInOkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfPerfInOkOctets.setStatus("current")
_EthIfStatsTable_Object = MibTable
ethIfStatsTable = _EthIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ethIfStatsTable.setStatus("current")
_EthIfStatsEntry_Object = MibTableRow
ethIfStatsEntry = _EthIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1)
)
ethIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethIfStatsEntry.setStatus("current")
_EthIfStatsInOctets_Type = Counter64
_EthIfStatsInOctets_Object = MibTableColumn
ethIfStatsInOctets = _EthIfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 1),
    _EthIfStatsInOctets_Type()
)
ethIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInOctets.setStatus("current")
_EthIfStatsInPkts_Type = Counter64
_EthIfStatsInPkts_Object = MibTableColumn
ethIfStatsInPkts = _EthIfStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 2),
    _EthIfStatsInPkts_Type()
)
ethIfStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts.setStatus("current")
_EthIfStatsInUcastPkts_Type = Counter64
_EthIfStatsInUcastPkts_Object = MibTableColumn
ethIfStatsInUcastPkts = _EthIfStatsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 3),
    _EthIfStatsInUcastPkts_Type()
)
ethIfStatsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInUcastPkts.setStatus("current")
_EthIfStatsInMulticastPkts_Type = Counter64
_EthIfStatsInMulticastPkts_Object = MibTableColumn
ethIfStatsInMulticastPkts = _EthIfStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 4),
    _EthIfStatsInMulticastPkts_Type()
)
ethIfStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInMulticastPkts.setStatus("current")
_EthIfStatsInBroadcastPkts_Type = Counter64
_EthIfStatsInBroadcastPkts_Object = MibTableColumn
ethIfStatsInBroadcastPkts = _EthIfStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 5),
    _EthIfStatsInBroadcastPkts_Type()
)
ethIfStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInBroadcastPkts.setStatus("current")
_EthIfStatsInJabberPkts_Type = Counter64
_EthIfStatsInJabberPkts_Object = MibTableColumn
ethIfStatsInJabberPkts = _EthIfStatsInJabberPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 6),
    _EthIfStatsInJabberPkts_Type()
)
ethIfStatsInJabberPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInJabberPkts.setStatus("current")
_EthIfStatsInL2CPDiscardPkts_Type = Counter64
_EthIfStatsInL2CPDiscardPkts_Object = MibTableColumn
ethIfStatsInL2CPDiscardPkts = _EthIfStatsInL2CPDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 7),
    _EthIfStatsInL2CPDiscardPkts_Type()
)
ethIfStatsInL2CPDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInL2CPDiscardPkts.setStatus("current")
_EthIfStatsInCFMDiscardPkts_Type = Counter64
_EthIfStatsInCFMDiscardPkts_Object = MibTableColumn
ethIfStatsInCFMDiscardPkts = _EthIfStatsInCFMDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 8),
    _EthIfStatsInCFMDiscardPkts_Type()
)
ethIfStatsInCFMDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInCFMDiscardPkts.setStatus("current")
_EthIfStatsInACLDiscardPkts_Type = Counter64
_EthIfStatsInACLDiscardPkts_Object = MibTableColumn
ethIfStatsInACLDiscardPkts = _EthIfStatsInACLDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 9),
    _EthIfStatsInACLDiscardPkts_Type()
)
ethIfStatsInACLDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInACLDiscardPkts.setStatus("current")
_EthIfStatsInFCSErrorPkts_Type = Counter64
_EthIfStatsInFCSErrorPkts_Object = MibTableColumn
ethIfStatsInFCSErrorPkts = _EthIfStatsInFCSErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 10),
    _EthIfStatsInFCSErrorPkts_Type()
)
ethIfStatsInFCSErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInFCSErrorPkts.setStatus("current")
_EthIfStatsInMacOverflowPkts_Type = Counter64
_EthIfStatsInMacOverflowPkts_Object = MibTableColumn
ethIfStatsInMacOverflowPkts = _EthIfStatsInMacOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 11),
    _EthIfStatsInMacOverflowPkts_Type()
)
ethIfStatsInMacOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInMacOverflowPkts.setStatus("current")
_EthIfStatsInternalMacReceiveErrors_Type = Counter64
_EthIfStatsInternalMacReceiveErrors_Object = MibTableColumn
ethIfStatsInternalMacReceiveErrors = _EthIfStatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 12),
    _EthIfStatsInternalMacReceiveErrors_Type()
)
ethIfStatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInternalMacReceiveErrors.setStatus("current")
_EthIfStatsInUndersizePkts_Type = Counter64
_EthIfStatsInUndersizePkts_Object = MibTableColumn
ethIfStatsInUndersizePkts = _EthIfStatsInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 13),
    _EthIfStatsInUndersizePkts_Type()
)
ethIfStatsInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInUndersizePkts.setStatus("current")
_EthIfStatsInPkts64Octets_Type = Counter64
_EthIfStatsInPkts64Octets_Object = MibTableColumn
ethIfStatsInPkts64Octets = _EthIfStatsInPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 14),
    _EthIfStatsInPkts64Octets_Type()
)
ethIfStatsInPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts64Octets.setStatus("current")
_EthIfStatsInPkts65to127Octets_Type = Counter64
_EthIfStatsInPkts65to127Octets_Object = MibTableColumn
ethIfStatsInPkts65to127Octets = _EthIfStatsInPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 15),
    _EthIfStatsInPkts65to127Octets_Type()
)
ethIfStatsInPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts65to127Octets.setStatus("current")
_EthIfStatsInPkts128to255Octets_Type = Counter64
_EthIfStatsInPkts128to255Octets_Object = MibTableColumn
ethIfStatsInPkts128to255Octets = _EthIfStatsInPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 16),
    _EthIfStatsInPkts128to255Octets_Type()
)
ethIfStatsInPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts128to255Octets.setStatus("current")
_EthIfStatsInPkts256to511Octets_Type = Counter64
_EthIfStatsInPkts256to511Octets_Object = MibTableColumn
ethIfStatsInPkts256to511Octets = _EthIfStatsInPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 17),
    _EthIfStatsInPkts256to511Octets_Type()
)
ethIfStatsInPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts256to511Octets.setStatus("current")
_EthIfStatsInPkts512to1023Octets_Type = Counter64
_EthIfStatsInPkts512to1023Octets_Object = MibTableColumn
ethIfStatsInPkts512to1023Octets = _EthIfStatsInPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 18),
    _EthIfStatsInPkts512to1023Octets_Type()
)
ethIfStatsInPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts512to1023Octets.setStatus("current")
_EthIfStatsInPkts1024to1518Octets_Type = Counter64
_EthIfStatsInPkts1024to1518Octets_Object = MibTableColumn
ethIfStatsInPkts1024to1518Octets = _EthIfStatsInPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 19),
    _EthIfStatsInPkts1024to1518Octets_Type()
)
ethIfStatsInPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts1024to1518Octets.setStatus("current")
_EthIfStatsInPkts1519to2047Octets_Type = Counter64
_EthIfStatsInPkts1519to2047Octets_Object = MibTableColumn
ethIfStatsInPkts1519to2047Octets = _EthIfStatsInPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 20),
    _EthIfStatsInPkts1519to2047Octets_Type()
)
ethIfStatsInPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts1519to2047Octets.setStatus("current")
_EthIfStatsInPkts1519toMaxOctets_Type = Counter64
_EthIfStatsInPkts1519toMaxOctets_Object = MibTableColumn
ethIfStatsInPkts1519toMaxOctets = _EthIfStatsInPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 21),
    _EthIfStatsInPkts1519toMaxOctets_Type()
)
ethIfStatsInPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts1519toMaxOctets.setStatus("current")
_EthIfStatsInPkts2048toMaxOctets_Type = Counter64
_EthIfStatsInPkts2048toMaxOctets_Object = MibTableColumn
ethIfStatsInPkts2048toMaxOctets = _EthIfStatsInPkts2048toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 22),
    _EthIfStatsInPkts2048toMaxOctets_Type()
)
ethIfStatsInPkts2048toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInPkts2048toMaxOctets.setStatus("current")
_EthIfStatsInOversizePkts_Type = Counter64
_EthIfStatsInOversizePkts_Object = MibTableColumn
ethIfStatsInOversizePkts = _EthIfStatsInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 23),
    _EthIfStatsInOversizePkts_Type()
)
ethIfStatsInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInOversizePkts.setStatus("current")
_EthIfStatsInErrorPkts_Type = Counter64
_EthIfStatsInErrorPkts_Object = MibTableColumn
ethIfStatsInErrorPkts = _EthIfStatsInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 24),
    _EthIfStatsInErrorPkts_Type()
)
ethIfStatsInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInErrorPkts.setStatus("current")
_EthIfStatsOutOctets_Type = Counter64
_EthIfStatsOutOctets_Object = MibTableColumn
ethIfStatsOutOctets = _EthIfStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 25),
    _EthIfStatsOutOctets_Type()
)
ethIfStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutOctets.setStatus("current")
_EthIfStatsOutPkts_Type = Counter64
_EthIfStatsOutPkts_Object = MibTableColumn
ethIfStatsOutPkts = _EthIfStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 26),
    _EthIfStatsOutPkts_Type()
)
ethIfStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts.setStatus("current")
_EthIfStatsOutUcastPkts_Type = Counter64
_EthIfStatsOutUcastPkts_Object = MibTableColumn
ethIfStatsOutUcastPkts = _EthIfStatsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 27),
    _EthIfStatsOutUcastPkts_Type()
)
ethIfStatsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutUcastPkts.setStatus("current")
_EthIfStatsOutMulticastPkts_Type = Counter64
_EthIfStatsOutMulticastPkts_Object = MibTableColumn
ethIfStatsOutMulticastPkts = _EthIfStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 28),
    _EthIfStatsOutMulticastPkts_Type()
)
ethIfStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutMulticastPkts.setStatus("current")
_EthIfStatsOutBroadcastPkts_Type = Counter64
_EthIfStatsOutBroadcastPkts_Object = MibTableColumn
ethIfStatsOutBroadcastPkts = _EthIfStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 29),
    _EthIfStatsOutBroadcastPkts_Type()
)
ethIfStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutBroadcastPkts.setStatus("current")
_EthIfStatsOutDiscardPkts_Type = Counter64
_EthIfStatsOutDiscardPkts_Object = MibTableColumn
ethIfStatsOutDiscardPkts = _EthIfStatsOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 30),
    _EthIfStatsOutDiscardPkts_Type()
)
ethIfStatsOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutDiscardPkts.setStatus("current")
_EthIfStatsOutPkts64Octets_Type = Counter64
_EthIfStatsOutPkts64Octets_Object = MibTableColumn
ethIfStatsOutPkts64Octets = _EthIfStatsOutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 31),
    _EthIfStatsOutPkts64Octets_Type()
)
ethIfStatsOutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts64Octets.setStatus("current")
_EthIfStatsOutPkts65to127Octets_Type = Counter64
_EthIfStatsOutPkts65to127Octets_Object = MibTableColumn
ethIfStatsOutPkts65to127Octets = _EthIfStatsOutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 32),
    _EthIfStatsOutPkts65to127Octets_Type()
)
ethIfStatsOutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts65to127Octets.setStatus("current")
_EthIfStatsOutPkts128to255Octets_Type = Counter64
_EthIfStatsOutPkts128to255Octets_Object = MibTableColumn
ethIfStatsOutPkts128to255Octets = _EthIfStatsOutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 33),
    _EthIfStatsOutPkts128to255Octets_Type()
)
ethIfStatsOutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts128to255Octets.setStatus("current")
_EthIfStatsOutPkts256to511Octets_Type = Counter64
_EthIfStatsOutPkts256to511Octets_Object = MibTableColumn
ethIfStatsOutPkts256to511Octets = _EthIfStatsOutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 34),
    _EthIfStatsOutPkts256to511Octets_Type()
)
ethIfStatsOutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts256to511Octets.setStatus("current")
_EthIfStatsOutPkts512to1023Octets_Type = Counter64
_EthIfStatsOutPkts512to1023Octets_Object = MibTableColumn
ethIfStatsOutPkts512to1023Octets = _EthIfStatsOutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 35),
    _EthIfStatsOutPkts512to1023Octets_Type()
)
ethIfStatsOutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts512to1023Octets.setStatus("current")
_EthIfStatsOutPkts1024to1518Octets_Type = Counter64
_EthIfStatsOutPkts1024to1518Octets_Object = MibTableColumn
ethIfStatsOutPkts1024to1518Octets = _EthIfStatsOutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 36),
    _EthIfStatsOutPkts1024to1518Octets_Type()
)
ethIfStatsOutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts1024to1518Octets.setStatus("current")
_EthIfStatsOutPkts1519to2047Octets_Type = Counter64
_EthIfStatsOutPkts1519to2047Octets_Object = MibTableColumn
ethIfStatsOutPkts1519to2047Octets = _EthIfStatsOutPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 37),
    _EthIfStatsOutPkts1519to2047Octets_Type()
)
ethIfStatsOutPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts1519to2047Octets.setStatus("current")
_EthIfStatsOutPkts2048toMaxOctets_Type = Counter64
_EthIfStatsOutPkts2048toMaxOctets_Object = MibTableColumn
ethIfStatsOutPkts2048toMaxOctets = _EthIfStatsOutPkts2048toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 38),
    _EthIfStatsOutPkts2048toMaxOctets_Type()
)
ethIfStatsOutPkts2048toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutPkts2048toMaxOctets.setStatus("current")
_EthIfStatsOutOversizePkts_Type = Counter64
_EthIfStatsOutOversizePkts_Object = MibTableColumn
ethIfStatsOutOversizePkts = _EthIfStatsOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 39),
    _EthIfStatsOutOversizePkts_Type()
)
ethIfStatsOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsOutOversizePkts.setStatus("current")
_EthIfStatsInUnMappedCosFrames_Type = Counter64
_EthIfStatsInUnMappedCosFrames_Object = MibTableColumn
ethIfStatsInUnMappedCosFrames = _EthIfStatsInUnMappedCosFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 40),
    _EthIfStatsInUnMappedCosFrames_Type()
)
ethIfStatsInUnMappedCosFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsInUnMappedCosFrames.setStatus("current")
_EthIfStatsEgressMTUDiscarded_Type = Counter64
_EthIfStatsEgressMTUDiscarded_Object = MibTableColumn
ethIfStatsEgressMTUDiscarded = _EthIfStatsEgressMTUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 42),
    _EthIfStatsEgressMTUDiscarded_Type()
)
ethIfStatsEgressMTUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsEgressMTUDiscarded.setStatus("current")
_EthIfStatsLastEgressMTUDiscardingFlow_Type = RowPointer
_EthIfStatsLastEgressMTUDiscardingFlow_Object = MibTableColumn
ethIfStatsLastEgressMTUDiscardingFlow = _EthIfStatsLastEgressMTUDiscardingFlow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 2, 5, 1, 43),
    _EthIfStatsLastEgressMTUDiscardingFlow_Type()
)
ethIfStatsLastEgressMTUDiscardingFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatsLastEgressMTUDiscardingFlow.setStatus("current")
_EthIfRing_ObjectIdentity = ObjectIdentity
ethIfRing = _EthIfRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4)
)
_EthIfRingEvents_ObjectIdentity = ObjectIdentity
ethIfRingEvents = _EthIfRingEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 0)
)
_EthIfRingTable_Object = MibTable
ethIfRingTable = _EthIfRingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ethIfRingTable.setStatus("current")
_EthIfRingEntry_Object = MibTableRow
ethIfRingEntry = _EthIfRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1)
)
ethIfRingEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfRingIdx"),
)
if mibBuilder.loadTexts:
    ethIfRingEntry.setStatus("current")
_EthIfRingIdx_Type = Unsigned32
_EthIfRingIdx_Object = MibTableColumn
ethIfRingIdx = _EthIfRingIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 1),
    _EthIfRingIdx_Type()
)
ethIfRingIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfRingIdx.setStatus("current")


class _EthIfRingAdminStatus_Type(Integer32):
    """Custom type ethIfRingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 3))
    )


_EthIfRingAdminStatus_Type.__name__ = "Integer32"
_EthIfRingAdminStatus_Object = MibTableColumn
ethIfRingAdminStatus = _EthIfRingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 2),
    _EthIfRingAdminStatus_Type()
)
ethIfRingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingAdminStatus.setStatus("current")
_EthIfRingPorts_Type = PortList
_EthIfRingPorts_Object = MibTableColumn
ethIfRingPorts = _EthIfRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 3),
    _EthIfRingPorts_Type()
)
ethIfRingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingPorts.setStatus("current")


class _EthIfRingOperStatus_Type(Integer32):
    """Custom type ethIfRingOperStatus based on Integer32"""
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
          ("open", 2),
          ("close", 3))
    )


_EthIfRingOperStatus_Type.__name__ = "Integer32"
_EthIfRingOperStatus_Object = MibTableColumn
ethIfRingOperStatus = _EthIfRingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 4),
    _EthIfRingOperStatus_Type()
)
ethIfRingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRingOperStatus.setStatus("current")
_EthIfRingKeepAliveInterval_Type = Unsigned32
_EthIfRingKeepAliveInterval_Object = MibTableColumn
ethIfRingKeepAliveInterval = _EthIfRingKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 5),
    _EthIfRingKeepAliveInterval_Type()
)
ethIfRingKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingKeepAliveInterval.setStatus("current")
_EthIfRingKeepAliveThresh_Type = Unsigned32
_EthIfRingKeepAliveThresh_Object = MibTableColumn
ethIfRingKeepAliveThresh = _EthIfRingKeepAliveThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 6),
    _EthIfRingKeepAliveThresh_Type()
)
ethIfRingKeepAliveThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingKeepAliveThresh.setStatus("current")
_EthIfRingKeepAliveVlanId_Type = Unsigned32
_EthIfRingKeepAliveVlanId_Object = MibTableColumn
ethIfRingKeepAliveVlanId = _EthIfRingKeepAliveVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 7),
    _EthIfRingKeepAliveVlanId_Type()
)
ethIfRingKeepAliveVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingKeepAliveVlanId.setStatus("current")
_EthIfRingMultiCastVlanId_Type = Unsigned32
_EthIfRingMultiCastVlanId_Object = MibTableColumn
ethIfRingMultiCastVlanId = _EthIfRingMultiCastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 8),
    _EthIfRingMultiCastVlanId_Type()
)
ethIfRingMultiCastVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingMultiCastVlanId.setStatus("current")


class _EthIfRingRowStatus_Type(Integer32):
    """Custom type ethIfRingRowStatus based on Integer32"""
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


_EthIfRingRowStatus_Type.__name__ = "Integer32"
_EthIfRingRowStatus_Object = MibTableColumn
ethIfRingRowStatus = _EthIfRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 1, 1, 9),
    _EthIfRingRowStatus_Type()
)
ethIfRingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRingRowStatus.setStatus("current")
_Erp_ObjectIdentity = ObjectIdentity
erp = _Erp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2)
)
_ErpTable_Object = MibTable
erpTable = _ErpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    erpTable.setStatus("current")
_ErpEntry_Object = MibTableRow
erpEntry = _ErpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1)
)
erpEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "erpIdx"),
)
if mibBuilder.loadTexts:
    erpEntry.setStatus("current")


class _ErpIdx_Type(Unsigned32):
    """Custom type erpIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ErpIdx_Type.__name__ = "Unsigned32"
_ErpIdx_Object = MibTableColumn
erpIdx = _ErpIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 1),
    _ErpIdx_Type()
)
erpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpIdx.setStatus("current")
_ErpRowStatus_Type = RowStatus
_ErpRowStatus_Object = MibTableColumn
erpRowStatus = _ErpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 2),
    _ErpRowStatus_Type()
)
erpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpRowStatus.setStatus("current")


class _ErpAdminStatus_Type(Integer32):
    """Custom type erpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 3))
    )


_ErpAdminStatus_Type.__name__ = "Integer32"
_ErpAdminStatus_Object = MibTableColumn
erpAdminStatus = _ErpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 3),
    _ErpAdminStatus_Type()
)
erpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpAdminStatus.setStatus("current")


class _ErpNodeState_Type(Integer32):
    """Custom type erpNodeState based on Integer32"""
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
        *(("init", 1),
          ("idle", 2),
          ("protected", 3),
          ("manualSwitch", 4),
          ("forcedSwitch", 5),
          ("pending", 6))
    )


_ErpNodeState_Type.__name__ = "Integer32"
_ErpNodeState_Object = MibTableColumn
erpNodeState = _ErpNodeState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 4),
    _ErpNodeState_Type()
)
erpNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpNodeState.setStatus("current")
_ErpBridgeNum_Type = Unsigned32
_ErpBridgeNum_Object = MibTableColumn
erpBridgeNum = _ErpBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 5),
    _ErpBridgeNum_Type()
)
erpBridgeNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpBridgeNum.setStatus("current")
_ErpEastPort_Type = Integer32
_ErpEastPort_Object = MibTableColumn
erpEastPort = _ErpEastPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 6),
    _ErpEastPort_Type()
)
erpEastPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpEastPort.setStatus("current")
_ErpWestPort_Type = Integer32
_ErpWestPort_Object = MibTableColumn
erpWestPort = _ErpWestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 7),
    _ErpWestPort_Type()
)
erpWestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpWestPort.setStatus("current")


class _ErpRplPort_Type(Integer32):
    """Custom type erpRplPort based on Integer32"""
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
          ("east", 2),
          ("west", 3))
    )


_ErpRplPort_Type.__name__ = "Integer32"
_ErpRplPort_Object = MibTableColumn
erpRplPort = _ErpRplPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 8),
    _ErpRplPort_Type()
)
erpRplPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpRplPort.setStatus("current")


class _ErpRapsVlanId_Type(Unsigned32):
    """Custom type erpRapsVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ErpRapsVlanId_Type.__name__ = "Unsigned32"
_ErpRapsVlanId_Object = MibTableColumn
erpRapsVlanId = _ErpRapsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 9),
    _ErpRapsVlanId_Type()
)
erpRapsVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpRapsVlanId.setStatus("current")


class _ErpOamCfmMel_Type(Unsigned32):
    """Custom type erpOamCfmMel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ErpOamCfmMel_Type.__name__ = "Unsigned32"
_ErpOamCfmMel_Object = MibTableColumn
erpOamCfmMel = _ErpOamCfmMel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 10),
    _ErpOamCfmMel_Type()
)
erpOamCfmMel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpOamCfmMel.setStatus("current")
_ErpWTR_Type = Unsigned32
_ErpWTR_Object = MibTableColumn
erpWTR = _ErpWTR_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 11),
    _ErpWTR_Type()
)
erpWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpWTR.setStatus("current")
_ErpWTRStatus_Type = Unsigned32
_ErpWTRStatus_Object = MibTableColumn
erpWTRStatus = _ErpWTRStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 12),
    _ErpWTRStatus_Type()
)
erpWTRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpWTRStatus.setStatus("current")
_ErpGuardTimer_Type = Unsigned32
_ErpGuardTimer_Object = MibTableColumn
erpGuardTimer = _ErpGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 13),
    _ErpGuardTimer_Type()
)
erpGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpGuardTimer.setStatus("current")
_ErpHoldoffTimer_Type = Unsigned32
_ErpHoldoffTimer_Object = MibTableColumn
erpHoldoffTimer = _ErpHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 14),
    _ErpHoldoffTimer_Type()
)
erpHoldoffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpHoldoffTimer.setStatus("current")


class _ErpForceSfCmd_Type(Integer32):
    """Custom type erpForceSfCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("eastOn", 3),
          ("westOn", 4),
          ("eastClear", 5),
          ("westClear", 6))
    )


_ErpForceSfCmd_Type.__name__ = "Integer32"
_ErpForceSfCmd_Object = MibTableColumn
erpForceSfCmd = _ErpForceSfCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 15),
    _ErpForceSfCmd_Type()
)
erpForceSfCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpForceSfCmd.setStatus("current")


class _ErpClearStatistics_Type(Bits):
    """Custom type erpClearStatistics based on Bits"""
    namedValues = NamedValues(
        *(("east", 0),
          ("west", 1))
    )

_ErpClearStatistics_Type.__name__ = "Bits"
_ErpClearStatistics_Object = MibTableColumn
erpClearStatistics = _ErpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 16),
    _ErpClearStatistics_Type()
)
erpClearStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpClearStatistics.setStatus("current")
_ErpRapsVlanPriority_Type = Unsigned32
_ErpRapsVlanPriority_Object = MibTableColumn
erpRapsVlanPriority = _ErpRapsVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 17),
    _ErpRapsVlanPriority_Type()
)
erpRapsVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpRapsVlanPriority.setStatus("current")


class _ErpDescr_Type(SnmpAdminString):
    """Custom type erpDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ErpDescr_Type.__name__ = "SnmpAdminString"
_ErpDescr_Object = MibTableColumn
erpDescr = _ErpDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 18),
    _ErpDescr_Type()
)
erpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpDescr.setStatus("current")


class _ErpRingType_Type(Integer32):
    """Custom type erpRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 1),
          ("subRing", 2))
    )


_ErpRingType_Type.__name__ = "Integer32"
_ErpRingType_Object = MibTableColumn
erpRingType = _ErpRingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 19),
    _ErpRingType_Type()
)
erpRingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpRingType.setStatus("current")
_ErpWTBStatus_Type = Unsigned32
_ErpWTBStatus_Object = MibTableColumn
erpWTBStatus = _ErpWTBStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 20),
    _ErpWTBStatus_Type()
)
erpWTBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpWTBStatus.setStatus("current")


class _ErpRevertiveMode_Type(Integer32):
    """Custom type erpRevertiveMode based on Integer32"""
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


_ErpRevertiveMode_Type.__name__ = "Integer32"
_ErpRevertiveMode_Object = MibTableColumn
erpRevertiveMode = _ErpRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 21),
    _ErpRevertiveMode_Type()
)
erpRevertiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpRevertiveMode.setStatus("current")
_ErpBackwardCompatibility_Type = TruthValue
_ErpBackwardCompatibility_Object = MibTableColumn
erpBackwardCompatibility = _ErpBackwardCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 22),
    _ErpBackwardCompatibility_Type()
)
erpBackwardCompatibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpBackwardCompatibility.setStatus("current")


class _ErpTopologyChangepropogation_Type(Integer32):
    """Custom type erpTopologyChangepropogation based on Integer32"""
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


_ErpTopologyChangepropogation_Type.__name__ = "Integer32"
_ErpTopologyChangepropogation_Object = MibTableColumn
erpTopologyChangepropogation = _ErpTopologyChangepropogation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 23),
    _ErpTopologyChangepropogation_Type()
)
erpTopologyChangepropogation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpTopologyChangepropogation.setStatus("current")
_ErpInterconnectionNode_Type = TruthValue
_ErpInterconnectionNode_Object = MibTableColumn
erpInterconnectionNode = _ErpInterconnectionNode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 24),
    _ErpInterconnectionNode_Type()
)
erpInterconnectionNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpInterconnectionNode.setStatus("current")


class _ErpCommand_Type(Integer32):
    """Custom type erpCommand based on Integer32"""
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
        *(("force", 1),
          ("manual", 2),
          ("clear", 3),
          ("noCommand", 4))
    )


_ErpCommand_Type.__name__ = "Integer32"
_ErpCommand_Object = MibTableColumn
erpCommand = _ErpCommand_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 25),
    _ErpCommand_Type()
)
erpCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpCommand.setStatus("current")


class _ErpCommandParam_Type(Integer32):
    """Custom type erpCommandParam based on Integer32"""
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
          ("eastPort", 2),
          ("westPort", 3))
    )


_ErpCommandParam_Type.__name__ = "Integer32"
_ErpCommandParam_Object = MibTableColumn
erpCommandParam = _ErpCommandParam_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 26),
    _ErpCommandParam_Type()
)
erpCommandParam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpCommandParam.setStatus("current")
_ErpEastPhyPort_Type = Unsigned32
_ErpEastPhyPort_Object = MibTableColumn
erpEastPhyPort = _ErpEastPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 27),
    _ErpEastPhyPort_Type()
)
erpEastPhyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpEastPhyPort.setStatus("current")
_ErpWestPhyPort_Type = Unsigned32
_ErpWestPhyPort_Object = MibTableColumn
erpWestPhyPort = _ErpWestPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 28),
    _ErpWestPhyPort_Type()
)
erpWestPhyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpWestPhyPort.setStatus("current")
_ErpCosMapProfile_Type = Unsigned32
_ErpCosMapProfile_Object = MibTableColumn
erpCosMapProfile = _ErpCosMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 29),
    _ErpCosMapProfile_Type()
)
erpCosMapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpCosMapProfile.setStatus("current")


class _ErpVirtualChannel_Type(Integer32):
    """Custom type erpVirtualChannel based on Integer32"""
    defaultValue = 3

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


_ErpVirtualChannel_Type.__name__ = "Integer32"
_ErpVirtualChannel_Object = MibTableColumn
erpVirtualChannel = _ErpVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 30),
    _ErpVirtualChannel_Type()
)
erpVirtualChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVirtualChannel.setStatus("current")


class _ErpPassthroughVids_Type(OctetString):
    """Custom type erpPassthroughVids based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_ErpPassthroughVids_Type.__name__ = "OctetString"
_ErpPassthroughVids_Object = MibTableColumn
erpPassthroughVids = _ErpPassthroughVids_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 31),
    _ErpPassthroughVids_Type()
)
erpPassthroughVids.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpPassthroughVids.setStatus("current")


class _ErpColorMapProfile_Type(Unsigned32):
    """Custom type erpColorMapProfile based on Unsigned32"""
    defaultValue = 0


_ErpColorMapProfile_Type.__name__ = "Unsigned32"
_ErpColorMapProfile_Object = MibTableColumn
erpColorMapProfile = _ErpColorMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 32),
    _ErpColorMapProfile_Type()
)
erpColorMapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpColorMapProfile.setStatus("current")
_ErpPassthroughQueueBlockEast_Type = RowPointer
_ErpPassthroughQueueBlockEast_Object = MibTableColumn
erpPassthroughQueueBlockEast = _ErpPassthroughQueueBlockEast_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 33),
    _ErpPassthroughQueueBlockEast_Type()
)
erpPassthroughQueueBlockEast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpPassthroughQueueBlockEast.setStatus("current")
_ErpPassthroughQueueBlockWest_Type = RowPointer
_ErpPassthroughQueueBlockWest_Object = MibTableColumn
erpPassthroughQueueBlockWest = _ErpPassthroughQueueBlockWest_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 1, 1, 34),
    _ErpPassthroughQueueBlockWest_Type()
)
erpPassthroughQueueBlockWest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpPassthroughQueueBlockWest.setStatus("current")
_ErpPortTable_Object = MibTable
erpPortTable = _ErpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    erpPortTable.setStatus("current")
_ErpPortEntry_Object = MibTableRow
erpPortEntry = _ErpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1)
)
erpPortEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "erpIdx"),
    (0, "RAD-EthIf-MIB", "erpPortIdx"),
)
if mibBuilder.loadTexts:
    erpPortEntry.setStatus("current")


class _ErpPortIdx_Type(Integer32):
    """Custom type erpPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 2))
    )


_ErpPortIdx_Type.__name__ = "Integer32"
_ErpPortIdx_Object = MibTableColumn
erpPortIdx = _ErpPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 1),
    _ErpPortIdx_Type()
)
erpPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpPortIdx.setStatus("current")
_ErpPortOamCfmMdId_Type = Unsigned32
_ErpPortOamCfmMdId_Object = MibTableColumn
erpPortOamCfmMdId = _ErpPortOamCfmMdId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 2),
    _ErpPortOamCfmMdId_Type()
)
erpPortOamCfmMdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpPortOamCfmMdId.setStatus("current")
_ErpPortOamCfmMaId_Type = Unsigned32
_ErpPortOamCfmMaId_Object = MibTableColumn
erpPortOamCfmMaId = _ErpPortOamCfmMaId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 3),
    _ErpPortOamCfmMaId_Type()
)
erpPortOamCfmMaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpPortOamCfmMaId.setStatus("current")
_ErpPortOamCfmMepId_Type = Unsigned32
_ErpPortOamCfmMepId_Object = MibTableColumn
erpPortOamCfmMepId = _ErpPortOamCfmMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 4),
    _ErpPortOamCfmMepId_Type()
)
erpPortOamCfmMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpPortOamCfmMepId.setStatus("current")


class _ErpPortState_Type(Integer32):
    """Custom type erpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("forwarding", 3),
          ("rAPSAndDataChannelBlocked", 4))
    )


_ErpPortState_Type.__name__ = "Integer32"
_ErpPortState_Object = MibTableColumn
erpPortState = _ErpPortState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 5),
    _ErpPortState_Type()
)
erpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortState.setStatus("current")


class _ErpPortLocalSfSource_Type(Integer32):
    """Custom type erpPortLocalSfSource based on Integer32"""
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
          ("serverLayer", 2),
          ("oamCfm", 3),
          ("forced", 4))
    )


_ErpPortLocalSfSource_Type.__name__ = "Integer32"
_ErpPortLocalSfSource_Object = MibTableColumn
erpPortLocalSfSource = _ErpPortLocalSfSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 6),
    _ErpPortLocalSfSource_Type()
)
erpPortLocalSfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortLocalSfSource.setStatus("current")
_ErpPortRapsRxValidMsg_Type = Counter32
_ErpPortRapsRxValidMsg_Object = MibTableColumn
erpPortRapsRxValidMsg = _ErpPortRapsRxValidMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 7),
    _ErpPortRapsRxValidMsg_Type()
)
erpPortRapsRxValidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxValidMsg.setStatus("current")
_ErpPortRapsRxInvalidMsg_Type = Counter32
_ErpPortRapsRxInvalidMsg_Object = MibTableColumn
erpPortRapsRxInvalidMsg = _ErpPortRapsRxInvalidMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 8),
    _ErpPortRapsRxInvalidMsg_Type()
)
erpPortRapsRxInvalidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxInvalidMsg.setStatus("current")
_ErpPortRapsRxSfMsg_Type = Counter32
_ErpPortRapsRxSfMsg_Object = MibTableColumn
erpPortRapsRxSfMsg = _ErpPortRapsRxSfMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 9),
    _ErpPortRapsRxSfMsg_Type()
)
erpPortRapsRxSfMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxSfMsg.setStatus("current")
_ErpPortRapsRxNrMsg_Type = Counter32
_ErpPortRapsRxNrMsg_Object = MibTableColumn
erpPortRapsRxNrMsg = _ErpPortRapsRxNrMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 10),
    _ErpPortRapsRxNrMsg_Type()
)
erpPortRapsRxNrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxNrMsg.setStatus("current")
_ErpPortRapsRxNrrbMsg_Type = Counter32
_ErpPortRapsRxNrrbMsg_Object = MibTableColumn
erpPortRapsRxNrrbMsg = _ErpPortRapsRxNrrbMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 11),
    _ErpPortRapsRxNrrbMsg_Type()
)
erpPortRapsRxNrrbMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxNrrbMsg.setStatus("current")
_ErpPortRapsTxValidMsg_Type = Counter32
_ErpPortRapsTxValidMsg_Object = MibTableColumn
erpPortRapsTxValidMsg = _ErpPortRapsTxValidMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 12),
    _ErpPortRapsTxValidMsg_Type()
)
erpPortRapsTxValidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxValidMsg.setStatus("current")
_ErpPortRapsTxInvalidMsg_Type = Counter32
_ErpPortRapsTxInvalidMsg_Object = MibTableColumn
erpPortRapsTxInvalidMsg = _ErpPortRapsTxInvalidMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 13),
    _ErpPortRapsTxInvalidMsg_Type()
)
erpPortRapsTxInvalidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxInvalidMsg.setStatus("current")
_ErpPortRapsTxSfMsg_Type = Counter32
_ErpPortRapsTxSfMsg_Object = MibTableColumn
erpPortRapsTxSfMsg = _ErpPortRapsTxSfMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 14),
    _ErpPortRapsTxSfMsg_Type()
)
erpPortRapsTxSfMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxSfMsg.setStatus("current")
_ErpPortRapsTxNrMsg_Type = Counter32
_ErpPortRapsTxNrMsg_Object = MibTableColumn
erpPortRapsTxNrMsg = _ErpPortRapsTxNrMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 15),
    _ErpPortRapsTxNrMsg_Type()
)
erpPortRapsTxNrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxNrMsg.setStatus("current")
_ErpPortRapsTxNrrbMsg_Type = Counter32
_ErpPortRapsTxNrrbMsg_Object = MibTableColumn
erpPortRapsTxNrrbMsg = _ErpPortRapsTxNrrbMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 16),
    _ErpPortRapsTxNrrbMsg_Type()
)
erpPortRapsTxNrrbMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxNrrbMsg.setStatus("current")


class _ErpPortDescr_Type(SnmpAdminString):
    """Custom type erpPortDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ErpPortDescr_Type.__name__ = "SnmpAdminString"
_ErpPortDescr_Object = MibTableColumn
erpPortDescr = _ErpPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 17),
    _ErpPortDescr_Type()
)
erpPortDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpPortDescr.setStatus("current")
_ErpPortRapsRxFsMsg_Type = Counter32
_ErpPortRapsRxFsMsg_Object = MibTableColumn
erpPortRapsRxFsMsg = _ErpPortRapsRxFsMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 18),
    _ErpPortRapsRxFsMsg_Type()
)
erpPortRapsRxFsMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxFsMsg.setStatus("current")
_ErpPortRapsRxMsMsg_Type = Counter32
_ErpPortRapsRxMsMsg_Object = MibTableColumn
erpPortRapsRxMsMsg = _ErpPortRapsRxMsMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 19),
    _ErpPortRapsRxMsMsg_Type()
)
erpPortRapsRxMsMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxMsMsg.setStatus("current")
_ErpPortRapsRxDnfMsg_Type = Counter32
_ErpPortRapsRxDnfMsg_Object = MibTableColumn
erpPortRapsRxDnfMsg = _ErpPortRapsRxDnfMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 20),
    _ErpPortRapsRxDnfMsg_Type()
)
erpPortRapsRxDnfMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxDnfMsg.setStatus("current")
_ErpPortRapsRxEvtMsg_Type = Counter32
_ErpPortRapsRxEvtMsg_Object = MibTableColumn
erpPortRapsRxEvtMsg = _ErpPortRapsRxEvtMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 21),
    _ErpPortRapsRxEvtMsg_Type()
)
erpPortRapsRxEvtMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsRxEvtMsg.setStatus("current")
_ErpPortRapsTxFsMsg_Type = Counter32
_ErpPortRapsTxFsMsg_Object = MibTableColumn
erpPortRapsTxFsMsg = _ErpPortRapsTxFsMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 22),
    _ErpPortRapsTxFsMsg_Type()
)
erpPortRapsTxFsMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxFsMsg.setStatus("current")
_ErpPortRapsTxMsMsg_Type = Counter32
_ErpPortRapsTxMsMsg_Object = MibTableColumn
erpPortRapsTxMsMsg = _ErpPortRapsTxMsMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 23),
    _ErpPortRapsTxMsMsg_Type()
)
erpPortRapsTxMsMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxMsMsg.setStatus("current")
_ErpPortRapsTxDnfMsg_Type = Counter32
_ErpPortRapsTxDnfMsg_Object = MibTableColumn
erpPortRapsTxDnfMsg = _ErpPortRapsTxDnfMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 24),
    _ErpPortRapsTxDnfMsg_Type()
)
erpPortRapsTxDnfMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxDnfMsg.setStatus("current")
_ErpPortRapsTxEvtMsg_Type = Counter32
_ErpPortRapsTxEvtMsg_Object = MibTableColumn
erpPortRapsTxEvtMsg = _ErpPortRapsTxEvtMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 25),
    _ErpPortRapsTxEvtMsg_Type()
)
erpPortRapsTxEvtMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpPortRapsTxEvtMsg.setStatus("current")


class _ErpPortType_Type(Integer32):
    """Custom type erpPortType based on Integer32"""
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
        *(("nodePort", 1),
          ("rpl", 2),
          ("neighbor", 3),
          ("nextNeighbor", 4))
    )


_ErpPortType_Type.__name__ = "Integer32"
_ErpPortType_Object = MibTableColumn
erpPortType = _ErpPortType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 2, 1, 26),
    _ErpPortType_Type()
)
erpPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpPortType.setStatus("current")
_ErpSubRingTable_Object = MibTable
erpSubRingTable = _ErpSubRingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    erpSubRingTable.setStatus("current")
_ErpSubRingEntry_Object = MibTableRow
erpSubRingEntry = _ErpSubRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1)
)
erpSubRingEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "erpSubRingMajorRingIndex"),
    (0, "RAD-EthIf-MIB", "erpSubRingSubRingIndex"),
)
if mibBuilder.loadTexts:
    erpSubRingEntry.setStatus("current")


class _ErpSubRingMajorRingIndex_Type(Unsigned32):
    """Custom type erpSubRingMajorRingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ErpSubRingMajorRingIndex_Type.__name__ = "Unsigned32"
_ErpSubRingMajorRingIndex_Object = MibTableColumn
erpSubRingMajorRingIndex = _ErpSubRingMajorRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1, 1),
    _ErpSubRingMajorRingIndex_Type()
)
erpSubRingMajorRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpSubRingMajorRingIndex.setStatus("current")


class _ErpSubRingSubRingIndex_Type(Unsigned32):
    """Custom type erpSubRingSubRingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ErpSubRingSubRingIndex_Type.__name__ = "Unsigned32"
_ErpSubRingSubRingIndex_Object = MibTableColumn
erpSubRingSubRingIndex = _ErpSubRingSubRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1, 2),
    _ErpSubRingSubRingIndex_Type()
)
erpSubRingSubRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpSubRingSubRingIndex.setStatus("current")
_ErpSubRingRowStatus_Type = RowStatus
_ErpSubRingRowStatus_Object = MibTableColumn
erpSubRingRowStatus = _ErpSubRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1, 3),
    _ErpSubRingRowStatus_Type()
)
erpSubRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpSubRingRowStatus.setStatus("current")


class _ErpSubRingVirtualChannel_Type(Integer32):
    """Custom type erpSubRingVirtualChannel based on Integer32"""
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


_ErpSubRingVirtualChannel_Type.__name__ = "Integer32"
_ErpSubRingVirtualChannel_Object = MibTableColumn
erpSubRingVirtualChannel = _ErpSubRingVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1, 4),
    _ErpSubRingVirtualChannel_Type()
)
erpSubRingVirtualChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpSubRingVirtualChannel.setStatus("deprecated")


class _ErpSubRingRAPSVlanId_Type(Unsigned32):
    """Custom type erpSubRingRAPSVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ErpSubRingRAPSVlanId_Type.__name__ = "Unsigned32"
_ErpSubRingRAPSVlanId_Object = MibTableColumn
erpSubRingRAPSVlanId = _ErpSubRingRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1, 5),
    _ErpSubRingRAPSVlanId_Type()
)
erpSubRingRAPSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpSubRingRAPSVlanId.setStatus("current")
_ErpSubRingRAPSVlanPriority_Type = Unsigned32
_ErpSubRingRAPSVlanPriority_Object = MibTableColumn
erpSubRingRAPSVlanPriority = _ErpSubRingRAPSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 4, 1, 6),
    _ErpSubRingRAPSVlanPriority_Type()
)
erpSubRingRAPSVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpSubRingRAPSVlanPriority.setStatus("current")
_ErpVlanTable_Object = MibTable
erpVlanTable = _ErpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    erpVlanTable.setStatus("current")
_ErpVlanEntry_Object = MibTableRow
erpVlanEntry = _ErpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1)
)
erpVlanEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "erpIdx"),
    (0, "RAD-EthIf-MIB", "erpVlanIdx"),
)
if mibBuilder.loadTexts:
    erpVlanEntry.setStatus("current")


class _ErpVlanIdx_Type(Unsigned32):
    """Custom type erpVlanIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ErpVlanIdx_Type.__name__ = "Unsigned32"
_ErpVlanIdx_Object = MibTableColumn
erpVlanIdx = _ErpVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 1),
    _ErpVlanIdx_Type()
)
erpVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpVlanIdx.setStatus("current")
_ErpVlanRowStatus_Type = RowStatus
_ErpVlanRowStatus_Object = MibTableColumn
erpVlanRowStatus = _ErpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 2),
    _ErpVlanRowStatus_Type()
)
erpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVlanRowStatus.setStatus("current")
_ErpVlanEastQblock_Type = ObjectIdentifier
_ErpVlanEastQblock_Object = MibTableColumn
erpVlanEastQblock = _ErpVlanEastQblock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 3),
    _ErpVlanEastQblock_Type()
)
erpVlanEastQblock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVlanEastQblock.setStatus("current")
_ErpVlanWestQblock_Type = ObjectIdentifier
_ErpVlanWestQblock_Object = MibTableColumn
erpVlanWestQblock = _ErpVlanWestQblock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 4),
    _ErpVlanWestQblock_Type()
)
erpVlanWestQblock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVlanWestQblock.setStatus("current")
_ErpVlanServiceIdName_Type = SnmpAdminString
_ErpVlanServiceIdName_Object = MibTableColumn
erpVlanServiceIdName = _ErpVlanServiceIdName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 5),
    _ErpVlanServiceIdName_Type()
)
erpVlanServiceIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVlanServiceIdName.setStatus("current")
_ErpVlanMajorEastQblock_Type = ObjectIdentifier
_ErpVlanMajorEastQblock_Object = MibTableColumn
erpVlanMajorEastQblock = _ErpVlanMajorEastQblock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 6),
    _ErpVlanMajorEastQblock_Type()
)
erpVlanMajorEastQblock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVlanMajorEastQblock.setStatus("current")
_ErpVlanMajorWestQblock_Type = ObjectIdentifier
_ErpVlanMajorWestQblock_Object = MibTableColumn
erpVlanMajorWestQblock = _ErpVlanMajorWestQblock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 2, 5, 1, 7),
    _ErpVlanMajorWestQblock_Type()
)
erpVlanMajorWestQblock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpVlanMajorWestQblock.setStatus("current")
_EthIfStorming_ObjectIdentity = ObjectIdentity
ethIfStorming = _EthIfStorming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5)
)
_EthIfStormTable_Object = MibTable
ethIfStormTable = _EthIfStormTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ethIfStormTable.setStatus("current")
_EthIfStormEntry_Object = MibTableRow
ethIfStormEntry = _EthIfStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1)
)
ethIfStormEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfStormCnfgIdx"),
    (0, "RAD-EthIf-MIB", "ethIfStormIfIdx"),
    (0, "RAD-EthIf-MIB", "ethIfStormDirection"),
    (0, "RAD-EthIf-MIB", "ethIfStormPacketType"),
)
if mibBuilder.loadTexts:
    ethIfStormEntry.setStatus("current")


class _EthIfStormCnfgIdx_Type(Unsigned32):
    """Custom type ethIfStormCnfgIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthIfStormCnfgIdx_Type.__name__ = "Unsigned32"
_EthIfStormCnfgIdx_Object = MibTableColumn
ethIfStormCnfgIdx = _EthIfStormCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1, 1),
    _EthIfStormCnfgIdx_Type()
)
ethIfStormCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfStormCnfgIdx.setStatus("current")
_EthIfStormIfIdx_Type = Unsigned32
_EthIfStormIfIdx_Object = MibTableColumn
ethIfStormIfIdx = _EthIfStormIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1, 2),
    _EthIfStormIfIdx_Type()
)
ethIfStormIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfStormIfIdx.setStatus("current")


class _EthIfStormDirection_Type(Integer32):
    """Custom type ethIfStormDirection based on Integer32"""
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


_EthIfStormDirection_Type.__name__ = "Integer32"
_EthIfStormDirection_Object = MibTableColumn
ethIfStormDirection = _EthIfStormDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1, 3),
    _EthIfStormDirection_Type()
)
ethIfStormDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfStormDirection.setStatus("current")


class _EthIfStormPacketType_Type(Bits):
    """Custom type ethIfStormPacketType based on Bits"""
    namedValues = NamedValues(
        *(("unknownUnicast", 0),
          ("broadcast", 1),
          ("multicast", 2))
    )

_EthIfStormPacketType_Type.__name__ = "Bits"
_EthIfStormPacketType_Object = MibTableColumn
ethIfStormPacketType = _EthIfStormPacketType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1, 4),
    _EthIfStormPacketType_Type()
)
ethIfStormPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfStormPacketType.setStatus("current")


class _EthIfStormCtrlEnable_Type(Integer32):
    """Custom type ethIfStormCtrlEnable based on Integer32"""
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


_EthIfStormCtrlEnable_Type.__name__ = "Integer32"
_EthIfStormCtrlEnable_Object = MibTableColumn
ethIfStormCtrlEnable = _EthIfStormCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1, 5),
    _EthIfStormCtrlEnable_Type()
)
ethIfStormCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfStormCtrlEnable.setStatus("current")
_EthIfStormMaxRate_Type = Unsigned32
_EthIfStormMaxRate_Object = MibTableColumn
ethIfStormMaxRate = _EthIfStormMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 5, 1, 1, 6),
    _EthIfStormMaxRate_Type()
)
ethIfStormMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfStormMaxRate.setStatus("current")
_EthIfOamEfm_ObjectIdentity = ObjectIdentity
ethIfOamEfm = _EthIfOamEfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6)
)
_Dot3OamEvents_ObjectIdentity = ObjectIdentity
dot3OamEvents = _Dot3OamEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 0)
)
_Dot3OamDescrTable_Object = MibTable
dot3OamDescrTable = _Dot3OamDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dot3OamDescrTable.setStatus("current")
_Dot3OamDescrEntry_Object = MibTableRow
dot3OamDescrEntry = _Dot3OamDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1, 1)
)
dot3OamDescrEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "dot3OamDescrId"),
)
if mibBuilder.loadTexts:
    dot3OamDescrEntry.setStatus("current")


class _Dot3OamDescrId_Type(Unsigned32):
    """Custom type dot3OamDescrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot3OamDescrId_Type.__name__ = "Unsigned32"
_Dot3OamDescrId_Object = MibTableColumn
dot3OamDescrId = _Dot3OamDescrId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1, 1, 1),
    _Dot3OamDescrId_Type()
)
dot3OamDescrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3OamDescrId.setStatus("current")
_Dot3OamDescrRowStatus_Type = RowStatus
_Dot3OamDescrRowStatus_Object = MibTableColumn
dot3OamDescrRowStatus = _Dot3OamDescrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1, 1, 2),
    _Dot3OamDescrRowStatus_Type()
)
dot3OamDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot3OamDescrRowStatus.setStatus("current")


class _Dot3OamDescrMode_Type(Integer32):
    """Custom type dot3OamDescrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_Dot3OamDescrMode_Type.__name__ = "Integer32"
_Dot3OamDescrMode_Object = MibTableColumn
dot3OamDescrMode = _Dot3OamDescrMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1, 1, 3),
    _Dot3OamDescrMode_Type()
)
dot3OamDescrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot3OamDescrMode.setStatus("current")


class _Dot3OamDescrLbRxOperation_Type(Integer32):
    """Custom type dot3OamDescrLbRxOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_Dot3OamDescrLbRxOperation_Type.__name__ = "Integer32"
_Dot3OamDescrLbRxOperation_Object = MibTableColumn
dot3OamDescrLbRxOperation = _Dot3OamDescrLbRxOperation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1, 1, 4),
    _Dot3OamDescrLbRxOperation_Type()
)
dot3OamDescrLbRxOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot3OamDescrLbRxOperation.setStatus("current")
_Dot3OamDescrRateLimit_Type = Unsigned32
_Dot3OamDescrRateLimit_Object = MibTableColumn
dot3OamDescrRateLimit = _Dot3OamDescrRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 1, 1, 5),
    _Dot3OamDescrRateLimit_Type()
)
dot3OamDescrRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot3OamDescrRateLimit.setStatus("current")
_Dot3OamXTable_Object = MibTable
dot3OamXTable = _Dot3OamXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dot3OamXTable.setStatus("current")
_Dot3OamXEntry_Object = MibTableRow
dot3OamXEntry = _Dot3OamXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    dot3OamXEntry.setStatus("current")


class _Dot3OamXDescrId_Type(Unsigned32):
    """Custom type dot3OamXDescrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dot3OamXDescrId_Type.__name__ = "Unsigned32"
_Dot3OamXDescrId_Object = MibTableColumn
dot3OamXDescrId = _Dot3OamXDescrId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 2, 1, 1),
    _Dot3OamXDescrId_Type()
)
dot3OamXDescrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamXDescrId.setStatus("current")


class _Dot3OamXPeerState_Type(Integer32):
    """Custom type dot3OamXPeerState based on Integer32"""
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
        *(("unknown", 1),
          ("operational", 2),
          ("linkFault", 3),
          ("dyingGasp", 4),
          ("criticalEvent", 5))
    )


_Dot3OamXPeerState_Type.__name__ = "Integer32"
_Dot3OamXPeerState_Object = MibTableColumn
dot3OamXPeerState = _Dot3OamXPeerState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 2, 1, 2),
    _Dot3OamXPeerState_Type()
)
dot3OamXPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamXPeerState.setStatus("current")
_EthIfMacLayer_ObjectIdentity = ObjectIdentity
ethIfMacLayer = _EthIfMacLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7)
)
_EthIfMacLayerEvents_ObjectIdentity = ObjectIdentity
ethIfMacLayerEvents = _EthIfMacLayerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 0)
)
_EthIfSrcMacCtrlTable_Object = MibTable
ethIfSrcMacCtrlTable = _EthIfSrcMacCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlTable.setStatus("current")
_EthIfSrcMacCtrlEntry_Object = MibTableRow
ethIfSrcMacCtrlEntry = _EthIfSrcMacCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1)
)
ethIfSrcMacCtrlEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfSrcMacCtrlIndex"),
    (0, "RAD-EthIf-MIB", "ethIfSrcMacCtrlIdx2"),
)
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlEntry.setStatus("current")
_EthIfSrcMacCtrlIndex_Type = Unsigned32
_EthIfSrcMacCtrlIndex_Object = MibTableColumn
ethIfSrcMacCtrlIndex = _EthIfSrcMacCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 1),
    _EthIfSrcMacCtrlIndex_Type()
)
ethIfSrcMacCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlIndex.setStatus("current")
_EthIfSrcMacCtrlIdx2_Type = Unsigned32
_EthIfSrcMacCtrlIdx2_Object = MibTableColumn
ethIfSrcMacCtrlIdx2 = _EthIfSrcMacCtrlIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 2),
    _EthIfSrcMacCtrlIdx2_Type()
)
ethIfSrcMacCtrlIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlIdx2.setStatus("current")


class _EthIfSrcMacCtrl_Type(Integer32):
    """Custom type ethIfSrcMacCtrl based on Integer32"""
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


_EthIfSrcMacCtrl_Type.__name__ = "Integer32"
_EthIfSrcMacCtrl_Object = MibTableColumn
ethIfSrcMacCtrl = _EthIfSrcMacCtrl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 3),
    _EthIfSrcMacCtrl_Type()
)
ethIfSrcMacCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrl.setStatus("current")
_EthIfSrcMacCtrlMaxPermitAddr_Type = Unsigned32
_EthIfSrcMacCtrlMaxPermitAddr_Object = MibTableColumn
ethIfSrcMacCtrlMaxPermitAddr = _EthIfSrcMacCtrlMaxPermitAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 4),
    _EthIfSrcMacCtrlMaxPermitAddr_Type()
)
ethIfSrcMacCtrlMaxPermitAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlMaxPermitAddr.setStatus("current")
_EthIfSrcMacCtrlCurNumPermitAddr_Type = Unsigned32
_EthIfSrcMacCtrlCurNumPermitAddr_Object = MibTableColumn
ethIfSrcMacCtrlCurNumPermitAddr = _EthIfSrcMacCtrlCurNumPermitAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 5),
    _EthIfSrcMacCtrlCurNumPermitAddr_Type()
)
ethIfSrcMacCtrlCurNumPermitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlCurNumPermitAddr.setStatus("current")


class _EthIfSrcMacCtrlFlushAddrCmd_Type(Integer32):
    """Custom type ethIfSrcMacCtrlFlushAddrCmd based on Integer32"""
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


_EthIfSrcMacCtrlFlushAddrCmd_Type.__name__ = "Integer32"
_EthIfSrcMacCtrlFlushAddrCmd_Object = MibTableColumn
ethIfSrcMacCtrlFlushAddrCmd = _EthIfSrcMacCtrlFlushAddrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 6),
    _EthIfSrcMacCtrlFlushAddrCmd_Type()
)
ethIfSrcMacCtrlFlushAddrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlFlushAddrCmd.setStatus("current")
_EthIfSrcMacCtrlAging_Type = Unsigned32
_EthIfSrcMacCtrlAging_Object = MibTableColumn
ethIfSrcMacCtrlAging = _EthIfSrcMacCtrlAging_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 7),
    _EthIfSrcMacCtrlAging_Type()
)
ethIfSrcMacCtrlAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAging.setStatus("current")


class _EthIfSrcMacCtrlLocking_Type(Integer32):
    """Custom type ethIfSrcMacCtrlLocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 2),
          ("lock", 3))
    )


_EthIfSrcMacCtrlLocking_Type.__name__ = "Integer32"
_EthIfSrcMacCtrlLocking_Object = MibTableColumn
ethIfSrcMacCtrlLocking = _EthIfSrcMacCtrlLocking_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 8),
    _EthIfSrcMacCtrlLocking_Type()
)
ethIfSrcMacCtrlLocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlLocking.setStatus("current")


class _EthIfSrcMacCtrlViolationAction_Type(Integer32):
    """Custom type ethIfSrcMacCtrlViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("dropNotify", 3),
          ("shutdown", 4))
    )


_EthIfSrcMacCtrlViolationAction_Type.__name__ = "Integer32"
_EthIfSrcMacCtrlViolationAction_Object = MibTableColumn
ethIfSrcMacCtrlViolationAction = _EthIfSrcMacCtrlViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 9),
    _EthIfSrcMacCtrlViolationAction_Type()
)
ethIfSrcMacCtrlViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlViolationAction.setStatus("current")
_EthIfSrcMacCtrlLastViolatingAddr_Type = MacAddress
_EthIfSrcMacCtrlLastViolatingAddr_Object = MibTableColumn
ethIfSrcMacCtrlLastViolatingAddr = _EthIfSrcMacCtrlLastViolatingAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 10),
    _EthIfSrcMacCtrlLastViolatingAddr_Type()
)
ethIfSrcMacCtrlLastViolatingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlLastViolatingAddr.setStatus("current")


class _EthIfSrcMacCtrlPortStatus_Type(Integer32):
    """Custom type ethIfSrcMacCtrlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("secureActive", 3),
          ("secureInactive", 4))
    )


_EthIfSrcMacCtrlPortStatus_Type.__name__ = "Integer32"
_EthIfSrcMacCtrlPortStatus_Object = MibTableColumn
ethIfSrcMacCtrlPortStatus = _EthIfSrcMacCtrlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 1, 1, 11),
    _EthIfSrcMacCtrlPortStatus_Type()
)
ethIfSrcMacCtrlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlPortStatus.setStatus("current")
_EthIfSrcMacCtrlAddrTable_Object = MibTable
ethIfSrcMacCtrlAddrTable = _EthIfSrcMacCtrlAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddrTable.setStatus("current")
_EthIfSrcMacCtrlAddrEntry_Object = MibTableRow
ethIfSrcMacCtrlAddrEntry = _EthIfSrcMacCtrlAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2, 1)
)
ethIfSrcMacCtrlAddrEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfSrcMacCtrlAddrIndex"),
    (0, "RAD-EthIf-MIB", "ethIfSrcMacCtrlAddr"),
    (0, "RAD-EthIf-MIB", "ethIfSrcMacCtrlAddrIdx3"),
)
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddrEntry.setStatus("current")
_EthIfSrcMacCtrlAddrIndex_Type = Unsigned32
_EthIfSrcMacCtrlAddrIndex_Object = MibTableColumn
ethIfSrcMacCtrlAddrIndex = _EthIfSrcMacCtrlAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2, 1, 1),
    _EthIfSrcMacCtrlAddrIndex_Type()
)
ethIfSrcMacCtrlAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddrIndex.setStatus("current")
_EthIfSrcMacCtrlAddr_Type = MacAddress
_EthIfSrcMacCtrlAddr_Object = MibTableColumn
ethIfSrcMacCtrlAddr = _EthIfSrcMacCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2, 1, 2),
    _EthIfSrcMacCtrlAddr_Type()
)
ethIfSrcMacCtrlAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddr.setStatus("current")
_EthIfSrcMacCtrlAddrIdx3_Type = Unsigned32
_EthIfSrcMacCtrlAddrIdx3_Object = MibTableColumn
ethIfSrcMacCtrlAddrIdx3 = _EthIfSrcMacCtrlAddrIdx3_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2, 1, 3),
    _EthIfSrcMacCtrlAddrIdx3_Type()
)
ethIfSrcMacCtrlAddrIdx3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddrIdx3.setStatus("current")


class _EthIfSrcMacCtrlAddrRowStatus_Type(Integer32):
    """Custom type ethIfSrcMacCtrlAddrRowStatus based on Integer32"""
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


_EthIfSrcMacCtrlAddrRowStatus_Type.__name__ = "Integer32"
_EthIfSrcMacCtrlAddrRowStatus_Object = MibTableColumn
ethIfSrcMacCtrlAddrRowStatus = _EthIfSrcMacCtrlAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2, 1, 4),
    _EthIfSrcMacCtrlAddrRowStatus_Type()
)
ethIfSrcMacCtrlAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddrRowStatus.setStatus("current")


class _EthIfSrcMacCtrlAddrStatus_Type(Integer32):
    """Custom type ethIfSrcMacCtrlAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5))
    )


_EthIfSrcMacCtrlAddrStatus_Type.__name__ = "Integer32"
_EthIfSrcMacCtrlAddrStatus_Object = MibTableColumn
ethIfSrcMacCtrlAddrStatus = _EthIfSrcMacCtrlAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 2, 1, 5),
    _EthIfSrcMacCtrlAddrStatus_Type()
)
ethIfSrcMacCtrlAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSrcMacCtrlAddrStatus.setStatus("current")
_EthIfSysConfig_ObjectIdentity = ObjectIdentity
ethIfSysConfig = _EthIfSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 11)
)
_EthIfSysValidEtherTypeTable_Object = MibTable
ethIfSysValidEtherTypeTable = _EthIfSysValidEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ethIfSysValidEtherTypeTable.setStatus("current")
_EthIfSysValidEtherTypeEntry_Object = MibTableRow
ethIfSysValidEtherTypeEntry = _EthIfSysValidEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 11, 1, 1)
)
ethIfSysValidEtherTypeEntry.setIndexNames(
    (0, "RAD-EthIf-MIB", "ethIfSysValidEtherTypeIdx"),
)
if mibBuilder.loadTexts:
    ethIfSysValidEtherTypeEntry.setStatus("current")
_EthIfSysValidEtherTypeIdx_Type = Unsigned32
_EthIfSysValidEtherTypeIdx_Object = MibTableColumn
ethIfSysValidEtherTypeIdx = _EthIfSysValidEtherTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 11, 1, 1, 1),
    _EthIfSysValidEtherTypeIdx_Type()
)
ethIfSysValidEtherTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfSysValidEtherTypeIdx.setStatus("current")
_EthIfSysValidEtherTypeRowStatus_Type = RowStatus
_EthIfSysValidEtherTypeRowStatus_Object = MibTableColumn
ethIfSysValidEtherTypeRowStatus = _EthIfSysValidEtherTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 11, 1, 1, 2),
    _EthIfSysValidEtherTypeRowStatus_Type()
)
ethIfSysValidEtherTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfSysValidEtherTypeRowStatus.setStatus("current")
_EthIfSysValidEtherTypeCode_Type = Unsigned32
_EthIfSysValidEtherTypeCode_Object = MibTableColumn
ethIfSysValidEtherTypeCode = _EthIfSysValidEtherTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 11, 1, 1, 3),
    _EthIfSysValidEtherTypeCode_Type()
)
ethIfSysValidEtherTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfSysValidEtherTypeCode.setStatus("current")
dot3OamEntry.registerAugmentions(
    ("RAD-EthIf-MIB",
     "dot3OamXEntry")
)
dot3OamXEntry.setIndexNames(*dot3OamEntry.getIndexNames())

# Managed Objects groups


# Notification objects

ethLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 1)
)
ethLos.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ethLos.setStatus(
        "current"
    )

erpStateProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 4)
)
erpStateProtected.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-EthIf-MIB", "erpDescr"))
)
if mibBuilder.loadTexts:
    erpStateProtected.setStatus(
        "current"
    )

erpPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 5)
)
erpPortStateChange.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-EthIf-MIB", "erpPortDescr"),
        ("RAD-EthIf-MIB", "erpPortState"))
)
if mibBuilder.loadTexts:
    erpPortStateChange.setStatus(
        "current"
    )

oamEfmRemoteLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 17)
)
oamEfmRemoteLoopback.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DOT3-OAM-MIB", "dot3OamLoopbackStatus"),
        ("DOT3-OAM-MIB", "dot3OamLoopbackIgnoreRx"))
)
if mibBuilder.loadTexts:
    oamEfmRemoteLoopback.setStatus(
        "current"
    )

oamEfmRemoteLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 19)
)
oamEfmRemoteLoopbackOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmRemoteLoopbackOff.setStatus(
        "current"
    )

oamEfmLinkFaultIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 20)
)
oamEfmLinkFaultIndication.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmLinkFaultIndication.setStatus(
        "current"
    )

oamEfmFeLinkFaultIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 21)
)
oamEfmFeLinkFaultIndication.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmFeLinkFaultIndication.setStatus(
        "current"
    )

oamEfmCriticalLinkIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 22)
)
oamEfmCriticalLinkIndication.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmCriticalLinkIndication.setStatus(
        "current"
    )

oamEfmFeCriticalLinkIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 23)
)
oamEfmFeCriticalLinkIndication.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmFeCriticalLinkIndication.setStatus(
        "current"
    )

oamEfmDyingGaspIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 24)
)
oamEfmDyingGaspIndication.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmDyingGaspIndication.setStatus(
        "current"
    )

oamEfmFeDyingGaspIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 25)
)
oamEfmFeDyingGaspIndication.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    oamEfmFeDyingGaspIndication.setStatus(
        "current"
    )

pcsLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 0, 26)
)
pcsLinkDown.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    pcsLinkDown.setStatus(
        "current"
    )

ethIfRingStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 4, 0, 1)
)
ethIfRingStatusChange.setObjects(
    ("RAD-EthIf-MIB", "ethIfRingOperStatus")
)
if mibBuilder.loadTexts:
    ethIfRingStatusChange.setStatus(
        "current"
    )

dot3OamOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 0, 1)
)
dot3OamOperStatusChange.setObjects(
    ("DOT3-OAM-MIB", "dot3OamOperStatus")
)
if mibBuilder.loadTexts:
    dot3OamOperStatusChange.setStatus(
        "current"
    )

dot3OamPeerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 6, 0, 2)
)
dot3OamPeerEvent.setObjects(
    ("RAD-EthIf-MIB", "dot3OamXPeerState")
)
if mibBuilder.loadTexts:
    dot3OamPeerEvent.setStatus(
        "current"
    )

ethIfMacAccessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 7, 0, 1)
)
ethIfMacAccessViolation.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("RAD-EthIf-MIB", "ethIfSrcMacCtrlLastViolatingAddr"))
)
if mibBuilder.loadTexts:
    ethIfMacAccessViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-EthIf-MIB",
    **{"ethIf": ethIf,
       "ethIfEvents": ethIfEvents,
       "ethLos": ethLos,
       "erpStateProtected": erpStateProtected,
       "erpPortStateChange": erpPortStateChange,
       "oamEfmRemoteLoopback": oamEfmRemoteLoopback,
       "oamEfmRemoteLoopbackOff": oamEfmRemoteLoopbackOff,
       "oamEfmLinkFaultIndication": oamEfmLinkFaultIndication,
       "oamEfmFeLinkFaultIndication": oamEfmFeLinkFaultIndication,
       "oamEfmCriticalLinkIndication": oamEfmCriticalLinkIndication,
       "oamEfmFeCriticalLinkIndication": oamEfmFeCriticalLinkIndication,
       "oamEfmDyingGaspIndication": oamEfmDyingGaspIndication,
       "oamEfmFeDyingGaspIndication": oamEfmFeDyingGaspIndication,
       "pcsLinkDown": pcsLinkDown,
       "ethIfTable": ethIfTable,
       "ethIfEntry": ethIfEntry,
       "ethIfIdx": ethIfIdx,
       "ethMode": ethMode,
       "ethBridgingMode": ethBridgingMode,
       "ethEncapsulationCRCMode": ethEncapsulationCRCMode,
       "ethBackPressure": ethBackPressure,
       "ethLimit4": ethLimit4,
       "ethSkipInitReset": ethSkipInitReset,
       "ethMulticastBlock": ethMulticastBlock,
       "ethBroadcastBlock": ethBroadcastBlock,
       "ethSpeed": ethSpeed,
       "ethRip2": ethRip2,
       "ethPortPriority": ethPortPriority,
       "ethPortMngEnable": ethPortMngEnable,
       "ethFlowCtrlMacAddress": ethFlowCtrlMacAddress,
       "ethRateLimit": ethRateLimit,
       "ethJumboFrameEnable": ethJumboFrameEnable,
       "ethAutoMdiXEnable": ethAutoMdiXEnable,
       "ethPortDataEnable": ethPortDataEnable,
       "ethIfUse": ethIfUse,
       "ethLineOam": ethLineOam,
       "ethRoutingProtocol": ethRoutingProtocol,
       "ethMdiXManualSwitch": ethMdiXManualSwitch,
       "ethDot1xEnable": ethDot1xEnable,
       "ethPartnerRateMode": ethPartnerRateMode,
       "ethDot1xPortRole": ethDot1xPortRole,
       "ethDhcpRequest": ethDhcpRequest,
       "ethSfpCapabilities": ethSfpCapabilities,
       "ethIfPerformance": ethIfPerformance,
       "ethIfCurrentTable": ethIfCurrentTable,
       "ethIfCurrentEntry": ethIfCurrentEntry,
       "ethIfCurrentIndex": ethIfCurrentIndex,
       "ethIfCurrentStatus": ethIfCurrentStatus,
       "ethIfCurrentInFrames": ethIfCurrentInFrames,
       "ethIfCurrentInOctets": ethIfCurrentInOctets,
       "ethIfCurrentAlignmentErrors": ethIfCurrentAlignmentErrors,
       "ethIfCurrentFCSErrors": ethIfCurrentFCSErrors,
       "ethIfCurrentLengthError": ethIfCurrentLengthError,
       "ethIfCurrentOutFrames": ethIfCurrentOutFrames,
       "ethIfCurrentOutOctets": ethIfCurrentOutOctets,
       "ethIfCurrentSingleCollisionFrames": ethIfCurrentSingleCollisionFrames,
       "ethIfCurrentMultipleCollisionFrames": ethIfCurrentMultipleCollisionFrames,
       "ethIfCurrentDeferredTransmissions": ethIfCurrentDeferredTransmissions,
       "ethIfCurrentLateCollisions": ethIfCurrentLateCollisions,
       "ethIfCurrentCarrierSenseErrors": ethIfCurrentCarrierSenseErrors,
       "ethIfCurrentInputCongestionDropped": ethIfCurrentInputCongestionDropped,
       "ethIfCurrentOutputCongestionDropped": ethIfCurrentOutputCongestionDropped,
       "ethIfCurrentOverflowInFrames": ethIfCurrentOverflowInFrames,
       "ethIfCurrentOverflowInOctets": ethIfCurrentOverflowInOctets,
       "ethIfCurrentOverflowFCSErrors": ethIfCurrentOverflowFCSErrors,
       "ethIfCurrentOverflowOutFrames": ethIfCurrentOverflowOutFrames,
       "ethIfCurrentOverflowOutOctets": ethIfCurrentOverflowOutOctets,
       "ethIfCurrentOverflowMultipleCollisionFrames": ethIfCurrentOverflowMultipleCollisionFrames,
       "ethIfCurrentInUnicastFrames": ethIfCurrentInUnicastFrames,
       "ethIfCurrentOutUnicastFrames": ethIfCurrentOutUnicastFrames,
       "ethIfCurrentInMulticastFrames": ethIfCurrentInMulticastFrames,
       "ethIfCurrentOutMulticastFrames": ethIfCurrentOutMulticastFrames,
       "ethIfCurrentInBroadcastFrames": ethIfCurrentInBroadcastFrames,
       "ethIfCurrentOutBroadcastFrames": ethIfCurrentOutBroadcastFrames,
       "ethIfCurrentInDiscardFrames": ethIfCurrentInDiscardFrames,
       "ethIfCurrentOutDiscardFrames": ethIfCurrentOutDiscardFrames,
       "ethIfCurrentInPauseFrames": ethIfCurrentInPauseFrames,
       "ethIfCurrentOutPauseFrames": ethIfCurrentOutPauseFrames,
       "ethIfCurrentOverflowInUnicastFrames": ethIfCurrentOverflowInUnicastFrames,
       "ethIfCurrentOverflowOutUnicastFrames": ethIfCurrentOverflowOutUnicastFrames,
       "ethIfCurrentOverflowInMulticastFrames": ethIfCurrentOverflowInMulticastFrames,
       "ethIfCurrentOverflowOutMulticastFrames": ethIfCurrentOverflowOutMulticastFrames,
       "ethIfCurrentOverflowInBroadcastFrames": ethIfCurrentOverflowInBroadcastFrames,
       "ethIfCurrentOverflowOutBroadcastFrames": ethIfCurrentOverflowOutBroadcastFrames,
       "ethIfCurrentOverflowInDiscardFrames": ethIfCurrentOverflowInDiscardFrames,
       "ethIfCurrentOverflowOutDiscardFrames": ethIfCurrentOverflowOutDiscardFrames,
       "ethIfCurrentOverflowInPauseFrames": ethIfCurrentOverflowInPauseFrames,
       "ethIfCurrentOverflowOutPauseFrames": ethIfCurrentOverflowOutPauseFrames,
       "ethIfIntervalTable": ethIfIntervalTable,
       "ethIfIntervalEntry": ethIfIntervalEntry,
       "ethIfIntervalIndex": ethIfIntervalIndex,
       "ethIfIntervalNumber": ethIfIntervalNumber,
       "ethIfIntervalStatus": ethIfIntervalStatus,
       "ethIfIntervalInFrames": ethIfIntervalInFrames,
       "ethIfIntervalInOctets": ethIfIntervalInOctets,
       "ethIfIntervalAlignmentErrors": ethIfIntervalAlignmentErrors,
       "ethIfIntervalFCSErrors": ethIfIntervalFCSErrors,
       "ethIfIntervalLengthError": ethIfIntervalLengthError,
       "ethIfIntervalOutFrames": ethIfIntervalOutFrames,
       "ethIfIntervalOutOctets": ethIfIntervalOutOctets,
       "ethIfIntervalSingleCollisionFrames": ethIfIntervalSingleCollisionFrames,
       "ethIfIntervalMultipleCollisionFrames": ethIfIntervalMultipleCollisionFrames,
       "ethIfIntervalDeferredTransmissions": ethIfIntervalDeferredTransmissions,
       "ethIfIntervalLateCollisions": ethIfIntervalLateCollisions,
       "ethIfIntervalCarrierSenseErrors": ethIfIntervalCarrierSenseErrors,
       "ethIfIntervalInputCongestionDropped": ethIfIntervalInputCongestionDropped,
       "ethIfIntervalOutputCongestionDropped": ethIfIntervalOutputCongestionDropped,
       "ethIfIntervalOverflowInFrames": ethIfIntervalOverflowInFrames,
       "ethIfIntervalOverflowInOctets": ethIfIntervalOverflowInOctets,
       "ethIfIntervalOverflowFCSErrors": ethIfIntervalOverflowFCSErrors,
       "ethIfIntervalOverflowOutFrames": ethIfIntervalOverflowOutFrames,
       "ethIfIntervalOverflowOutOctets": ethIfIntervalOverflowOutOctets,
       "ethIfIntervalOverflowMultipleCollisionFrames": ethIfIntervalOverflowMultipleCollisionFrames,
       "ethIfIntervalInUnicastFrames": ethIfIntervalInUnicastFrames,
       "ethIfIntervalOutUnicastFrames": ethIfIntervalOutUnicastFrames,
       "ethIfIntervalInMulticastFrames": ethIfIntervalInMulticastFrames,
       "ethIfIntervalOutMulticastFrames": ethIfIntervalOutMulticastFrames,
       "ethIfIntervalInBroadcastFrames": ethIfIntervalInBroadcastFrames,
       "ethIfIntervalOutBroadcastFrames": ethIfIntervalOutBroadcastFrames,
       "ethIfIntervalInDiscardFrames": ethIfIntervalInDiscardFrames,
       "ethIfIntervalOutDiscardFrames": ethIfIntervalOutDiscardFrames,
       "ethIfIntervalInPauseFrames": ethIfIntervalInPauseFrames,
       "ethIfIntervalOutPauseFrames": ethIfIntervalOutPauseFrames,
       "ethIfIntervalOverflowInUnicastFrames": ethIfIntervalOverflowInUnicastFrames,
       "ethIfIntervalOverflowOutUnicastFrames": ethIfIntervalOverflowOutUnicastFrames,
       "ethIfIntervalOverflowInMulticastFrames": ethIfIntervalOverflowInMulticastFrames,
       "ethIfIntervalOverflowOutMulticastFrames": ethIfIntervalOverflowOutMulticastFrames,
       "ethIfIntervalOverflowInBroadcastFrames": ethIfIntervalOverflowInBroadcastFrames,
       "ethIfIntervalOverflowOutBroadcastFrames": ethIfIntervalOverflowOutBroadcastFrames,
       "ethIfIntervalOverflowInDiscardFrames": ethIfIntervalOverflowInDiscardFrames,
       "ethIfIntervalOverflowOutDiscardFrames": ethIfIntervalOverflowOutDiscardFrames,
       "ethIfIntervalOverflowInPauseFrames": ethIfIntervalOverflowInPauseFrames,
       "ethIfIntervalOverflowOutPauseFrames": ethIfIntervalOverflowOutPauseFrames,
       "ethPerformanceMode": ethPerformanceMode,
       "ethIfPerfTable": ethIfPerfTable,
       "ethIfPerfEntry": ethIfPerfEntry,
       "ethIfPerfInOkFrames": ethIfPerfInOkFrames,
       "ethIfPerfOutOkFrames": ethIfPerfOutOkFrames,
       "ethIfPerfTotalCollisions": ethIfPerfTotalCollisions,
       "ethIfPerfInOkOctets": ethIfPerfInOkOctets,
       "ethIfStatsTable": ethIfStatsTable,
       "ethIfStatsEntry": ethIfStatsEntry,
       "ethIfStatsInOctets": ethIfStatsInOctets,
       "ethIfStatsInPkts": ethIfStatsInPkts,
       "ethIfStatsInUcastPkts": ethIfStatsInUcastPkts,
       "ethIfStatsInMulticastPkts": ethIfStatsInMulticastPkts,
       "ethIfStatsInBroadcastPkts": ethIfStatsInBroadcastPkts,
       "ethIfStatsInJabberPkts": ethIfStatsInJabberPkts,
       "ethIfStatsInL2CPDiscardPkts": ethIfStatsInL2CPDiscardPkts,
       "ethIfStatsInCFMDiscardPkts": ethIfStatsInCFMDiscardPkts,
       "ethIfStatsInACLDiscardPkts": ethIfStatsInACLDiscardPkts,
       "ethIfStatsInFCSErrorPkts": ethIfStatsInFCSErrorPkts,
       "ethIfStatsInMacOverflowPkts": ethIfStatsInMacOverflowPkts,
       "ethIfStatsInternalMacReceiveErrors": ethIfStatsInternalMacReceiveErrors,
       "ethIfStatsInUndersizePkts": ethIfStatsInUndersizePkts,
       "ethIfStatsInPkts64Octets": ethIfStatsInPkts64Octets,
       "ethIfStatsInPkts65to127Octets": ethIfStatsInPkts65to127Octets,
       "ethIfStatsInPkts128to255Octets": ethIfStatsInPkts128to255Octets,
       "ethIfStatsInPkts256to511Octets": ethIfStatsInPkts256to511Octets,
       "ethIfStatsInPkts512to1023Octets": ethIfStatsInPkts512to1023Octets,
       "ethIfStatsInPkts1024to1518Octets": ethIfStatsInPkts1024to1518Octets,
       "ethIfStatsInPkts1519to2047Octets": ethIfStatsInPkts1519to2047Octets,
       "ethIfStatsInPkts1519toMaxOctets": ethIfStatsInPkts1519toMaxOctets,
       "ethIfStatsInPkts2048toMaxOctets": ethIfStatsInPkts2048toMaxOctets,
       "ethIfStatsInOversizePkts": ethIfStatsInOversizePkts,
       "ethIfStatsInErrorPkts": ethIfStatsInErrorPkts,
       "ethIfStatsOutOctets": ethIfStatsOutOctets,
       "ethIfStatsOutPkts": ethIfStatsOutPkts,
       "ethIfStatsOutUcastPkts": ethIfStatsOutUcastPkts,
       "ethIfStatsOutMulticastPkts": ethIfStatsOutMulticastPkts,
       "ethIfStatsOutBroadcastPkts": ethIfStatsOutBroadcastPkts,
       "ethIfStatsOutDiscardPkts": ethIfStatsOutDiscardPkts,
       "ethIfStatsOutPkts64Octets": ethIfStatsOutPkts64Octets,
       "ethIfStatsOutPkts65to127Octets": ethIfStatsOutPkts65to127Octets,
       "ethIfStatsOutPkts128to255Octets": ethIfStatsOutPkts128to255Octets,
       "ethIfStatsOutPkts256to511Octets": ethIfStatsOutPkts256to511Octets,
       "ethIfStatsOutPkts512to1023Octets": ethIfStatsOutPkts512to1023Octets,
       "ethIfStatsOutPkts1024to1518Octets": ethIfStatsOutPkts1024to1518Octets,
       "ethIfStatsOutPkts1519to2047Octets": ethIfStatsOutPkts1519to2047Octets,
       "ethIfStatsOutPkts2048toMaxOctets": ethIfStatsOutPkts2048toMaxOctets,
       "ethIfStatsOutOversizePkts": ethIfStatsOutOversizePkts,
       "ethIfStatsInUnMappedCosFrames": ethIfStatsInUnMappedCosFrames,
       "ethIfStatsEgressMTUDiscarded": ethIfStatsEgressMTUDiscarded,
       "ethIfStatsLastEgressMTUDiscardingFlow": ethIfStatsLastEgressMTUDiscardingFlow,
       "ethIfRing": ethIfRing,
       "ethIfRingEvents": ethIfRingEvents,
       "ethIfRingStatusChange": ethIfRingStatusChange,
       "ethIfRingTable": ethIfRingTable,
       "ethIfRingEntry": ethIfRingEntry,
       "ethIfRingIdx": ethIfRingIdx,
       "ethIfRingAdminStatus": ethIfRingAdminStatus,
       "ethIfRingPorts": ethIfRingPorts,
       "ethIfRingOperStatus": ethIfRingOperStatus,
       "ethIfRingKeepAliveInterval": ethIfRingKeepAliveInterval,
       "ethIfRingKeepAliveThresh": ethIfRingKeepAliveThresh,
       "ethIfRingKeepAliveVlanId": ethIfRingKeepAliveVlanId,
       "ethIfRingMultiCastVlanId": ethIfRingMultiCastVlanId,
       "ethIfRingRowStatus": ethIfRingRowStatus,
       "erp": erp,
       "erpTable": erpTable,
       "erpEntry": erpEntry,
       "erpIdx": erpIdx,
       "erpRowStatus": erpRowStatus,
       "erpAdminStatus": erpAdminStatus,
       "erpNodeState": erpNodeState,
       "erpBridgeNum": erpBridgeNum,
       "erpEastPort": erpEastPort,
       "erpWestPort": erpWestPort,
       "erpRplPort": erpRplPort,
       "erpRapsVlanId": erpRapsVlanId,
       "erpOamCfmMel": erpOamCfmMel,
       "erpWTR": erpWTR,
       "erpWTRStatus": erpWTRStatus,
       "erpGuardTimer": erpGuardTimer,
       "erpHoldoffTimer": erpHoldoffTimer,
       "erpForceSfCmd": erpForceSfCmd,
       "erpClearStatistics": erpClearStatistics,
       "erpRapsVlanPriority": erpRapsVlanPriority,
       "erpDescr": erpDescr,
       "erpRingType": erpRingType,
       "erpWTBStatus": erpWTBStatus,
       "erpRevertiveMode": erpRevertiveMode,
       "erpBackwardCompatibility": erpBackwardCompatibility,
       "erpTopologyChangepropogation": erpTopologyChangepropogation,
       "erpInterconnectionNode": erpInterconnectionNode,
       "erpCommand": erpCommand,
       "erpCommandParam": erpCommandParam,
       "erpEastPhyPort": erpEastPhyPort,
       "erpWestPhyPort": erpWestPhyPort,
       "erpCosMapProfile": erpCosMapProfile,
       "erpVirtualChannel": erpVirtualChannel,
       "erpPassthroughVids": erpPassthroughVids,
       "erpColorMapProfile": erpColorMapProfile,
       "erpPassthroughQueueBlockEast": erpPassthroughQueueBlockEast,
       "erpPassthroughQueueBlockWest": erpPassthroughQueueBlockWest,
       "erpPortTable": erpPortTable,
       "erpPortEntry": erpPortEntry,
       "erpPortIdx": erpPortIdx,
       "erpPortOamCfmMdId": erpPortOamCfmMdId,
       "erpPortOamCfmMaId": erpPortOamCfmMaId,
       "erpPortOamCfmMepId": erpPortOamCfmMepId,
       "erpPortState": erpPortState,
       "erpPortLocalSfSource": erpPortLocalSfSource,
       "erpPortRapsRxValidMsg": erpPortRapsRxValidMsg,
       "erpPortRapsRxInvalidMsg": erpPortRapsRxInvalidMsg,
       "erpPortRapsRxSfMsg": erpPortRapsRxSfMsg,
       "erpPortRapsRxNrMsg": erpPortRapsRxNrMsg,
       "erpPortRapsRxNrrbMsg": erpPortRapsRxNrrbMsg,
       "erpPortRapsTxValidMsg": erpPortRapsTxValidMsg,
       "erpPortRapsTxInvalidMsg": erpPortRapsTxInvalidMsg,
       "erpPortRapsTxSfMsg": erpPortRapsTxSfMsg,
       "erpPortRapsTxNrMsg": erpPortRapsTxNrMsg,
       "erpPortRapsTxNrrbMsg": erpPortRapsTxNrrbMsg,
       "erpPortDescr": erpPortDescr,
       "erpPortRapsRxFsMsg": erpPortRapsRxFsMsg,
       "erpPortRapsRxMsMsg": erpPortRapsRxMsMsg,
       "erpPortRapsRxDnfMsg": erpPortRapsRxDnfMsg,
       "erpPortRapsRxEvtMsg": erpPortRapsRxEvtMsg,
       "erpPortRapsTxFsMsg": erpPortRapsTxFsMsg,
       "erpPortRapsTxMsMsg": erpPortRapsTxMsMsg,
       "erpPortRapsTxDnfMsg": erpPortRapsTxDnfMsg,
       "erpPortRapsTxEvtMsg": erpPortRapsTxEvtMsg,
       "erpPortType": erpPortType,
       "erpSubRingTable": erpSubRingTable,
       "erpSubRingEntry": erpSubRingEntry,
       "erpSubRingMajorRingIndex": erpSubRingMajorRingIndex,
       "erpSubRingSubRingIndex": erpSubRingSubRingIndex,
       "erpSubRingRowStatus": erpSubRingRowStatus,
       "erpSubRingVirtualChannel": erpSubRingVirtualChannel,
       "erpSubRingRAPSVlanId": erpSubRingRAPSVlanId,
       "erpSubRingRAPSVlanPriority": erpSubRingRAPSVlanPriority,
       "erpVlanTable": erpVlanTable,
       "erpVlanEntry": erpVlanEntry,
       "erpVlanIdx": erpVlanIdx,
       "erpVlanRowStatus": erpVlanRowStatus,
       "erpVlanEastQblock": erpVlanEastQblock,
       "erpVlanWestQblock": erpVlanWestQblock,
       "erpVlanServiceIdName": erpVlanServiceIdName,
       "erpVlanMajorEastQblock": erpVlanMajorEastQblock,
       "erpVlanMajorWestQblock": erpVlanMajorWestQblock,
       "ethIfStorming": ethIfStorming,
       "ethIfStormTable": ethIfStormTable,
       "ethIfStormEntry": ethIfStormEntry,
       "ethIfStormCnfgIdx": ethIfStormCnfgIdx,
       "ethIfStormIfIdx": ethIfStormIfIdx,
       "ethIfStormDirection": ethIfStormDirection,
       "ethIfStormPacketType": ethIfStormPacketType,
       "ethIfStormCtrlEnable": ethIfStormCtrlEnable,
       "ethIfStormMaxRate": ethIfStormMaxRate,
       "ethIfOamEfm": ethIfOamEfm,
       "dot3OamEvents": dot3OamEvents,
       "dot3OamOperStatusChange": dot3OamOperStatusChange,
       "dot3OamPeerEvent": dot3OamPeerEvent,
       "dot3OamDescrTable": dot3OamDescrTable,
       "dot3OamDescrEntry": dot3OamDescrEntry,
       "dot3OamDescrId": dot3OamDescrId,
       "dot3OamDescrRowStatus": dot3OamDescrRowStatus,
       "dot3OamDescrMode": dot3OamDescrMode,
       "dot3OamDescrLbRxOperation": dot3OamDescrLbRxOperation,
       "dot3OamDescrRateLimit": dot3OamDescrRateLimit,
       "dot3OamXTable": dot3OamXTable,
       "dot3OamXEntry": dot3OamXEntry,
       "dot3OamXDescrId": dot3OamXDescrId,
       "dot3OamXPeerState": dot3OamXPeerState,
       "ethIfMacLayer": ethIfMacLayer,
       "ethIfMacLayerEvents": ethIfMacLayerEvents,
       "ethIfMacAccessViolation": ethIfMacAccessViolation,
       "ethIfSrcMacCtrlTable": ethIfSrcMacCtrlTable,
       "ethIfSrcMacCtrlEntry": ethIfSrcMacCtrlEntry,
       "ethIfSrcMacCtrlIndex": ethIfSrcMacCtrlIndex,
       "ethIfSrcMacCtrlIdx2": ethIfSrcMacCtrlIdx2,
       "ethIfSrcMacCtrl": ethIfSrcMacCtrl,
       "ethIfSrcMacCtrlMaxPermitAddr": ethIfSrcMacCtrlMaxPermitAddr,
       "ethIfSrcMacCtrlCurNumPermitAddr": ethIfSrcMacCtrlCurNumPermitAddr,
       "ethIfSrcMacCtrlFlushAddrCmd": ethIfSrcMacCtrlFlushAddrCmd,
       "ethIfSrcMacCtrlAging": ethIfSrcMacCtrlAging,
       "ethIfSrcMacCtrlLocking": ethIfSrcMacCtrlLocking,
       "ethIfSrcMacCtrlViolationAction": ethIfSrcMacCtrlViolationAction,
       "ethIfSrcMacCtrlLastViolatingAddr": ethIfSrcMacCtrlLastViolatingAddr,
       "ethIfSrcMacCtrlPortStatus": ethIfSrcMacCtrlPortStatus,
       "ethIfSrcMacCtrlAddrTable": ethIfSrcMacCtrlAddrTable,
       "ethIfSrcMacCtrlAddrEntry": ethIfSrcMacCtrlAddrEntry,
       "ethIfSrcMacCtrlAddrIndex": ethIfSrcMacCtrlAddrIndex,
       "ethIfSrcMacCtrlAddr": ethIfSrcMacCtrlAddr,
       "ethIfSrcMacCtrlAddrIdx3": ethIfSrcMacCtrlAddrIdx3,
       "ethIfSrcMacCtrlAddrRowStatus": ethIfSrcMacCtrlAddrRowStatus,
       "ethIfSrcMacCtrlAddrStatus": ethIfSrcMacCtrlAddrStatus,
       "ethIfSysConfig": ethIfSysConfig,
       "ethIfSysValidEtherTypeTable": ethIfSysValidEtherTypeTable,
       "ethIfSysValidEtherTypeEntry": ethIfSysValidEtherTypeEntry,
       "ethIfSysValidEtherTypeIdx": ethIfSysValidEtherTypeIdx,
       "ethIfSysValidEtherTypeRowStatus": ethIfSysValidEtherTypeRowStatus,
       "ethIfSysValidEtherTypeCode": ethIfSysValidEtherTypeCode}
)
