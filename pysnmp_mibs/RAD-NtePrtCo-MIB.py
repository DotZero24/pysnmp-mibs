# SNMP MIB module (RAD-NtePrtCo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-NtePrtCo-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:09 2025
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

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rad,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "rad")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

radAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmNte_ObjectIdentity = ObjectIdentity
atmNte = _AtmNte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3)
)
_AtmNteEvents_ObjectIdentity = ObjectIdentity
atmNteEvents = _AtmNteEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 0)
)
if mibBuilder.loadTexts:
    atmNteEvents.setStatus("current")
_AtmNtePrt_ObjectIdentity = ObjectIdentity
atmNtePrt = _AtmNtePrt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2)
)
_AtmNtePrtConfig_ObjectIdentity = ObjectIdentity
atmNtePrtConfig = _AtmNtePrtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1)
)
_AtmNteConfIfTable_Object = MibTable
atmNteConfIfTable = _AtmNteConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmNteConfIfTable.setStatus("current")
_AtmNteConfIfEntry_Object = MibTableRow
atmNteConfIfEntry = _AtmNteConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1)
)
atmNteConfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmNteConfIfEntry.setStatus("current")


class _AtmConfIfTransmitClk_Type(Integer32):
    """Custom type atmConfIfTransmitClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("external", 3),
          ("loopback", 4),
          ("adaptive", 5))
    )


_AtmConfIfTransmitClk_Type.__name__ = "Integer32"
_AtmConfIfTransmitClk_Object = MibTableColumn
atmConfIfTransmitClk = _AtmConfIfTransmitClk_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 1),
    _AtmConfIfTransmitClk_Type()
)
atmConfIfTransmitClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfTransmitClk.setStatus("current")


class _AtmConfIfLoopback_Type(Integer32):
    """Custom type atmConfIfLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("external", 3),
          ("disable", 4))
    )


_AtmConfIfLoopback_Type.__name__ = "Integer32"
_AtmConfIfLoopback_Object = MibTableColumn
atmConfIfLoopback = _AtmConfIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 2),
    _AtmConfIfLoopback_Type()
)
atmConfIfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfLoopback.setStatus("current")


class _AtmConfIfFrameType_Type(Integer32):
    """Custom type atmConfIfFrameType based on Integer32"""
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
        *(("other", 1),
          ("sonet", 2),
          ("sdh", 3),
          ("direct", 4),
          ("plcpInternal", 5),
          ("plcpExternal", 6),
          ("e3", 7),
          ("ethCrcTrans", 8),
          ("ethCrcNotTrans", 9),
          ("directNoScrmbling", 10),
          ("plcpInternalNoScrmbling", 11),
          ("plcpExternalNoScrmbling", 12))
    )


_AtmConfIfFrameType_Type.__name__ = "Integer32"
_AtmConfIfFrameType_Object = MibTableColumn
atmConfIfFrameType = _AtmConfIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 3),
    _AtmConfIfFrameType_Type()
)
atmConfIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfFrameType.setStatus("current")


class _AtmConfIfCardType_Type(Integer32):
    """Custom type atmConfIfCardType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sc13m-155", 2),
          ("st13s-155", 3),
          ("st13l-155", 4),
          ("utp-155", 5),
          ("cx-bnc-155", 6),
          ("e3", 7),
          ("t3", 8),
          ("e1", 9),
          ("e1-ltu", 10),
          ("fc13l-155", 11),
          ("fc13lh-155", 12),
          ("fc15lh-155", 13),
          ("fc13l-e3", 14),
          ("fc13lh-e3", 15),
          ("fc15lh-e3", 16),
          ("fc13l-t3", 17),
          ("fc13lh-t3", 18),
          ("fc15lh-t3", 19))
    )


_AtmConfIfCardType_Type.__name__ = "Integer32"
_AtmConfIfCardType_Object = MibTableColumn
atmConfIfCardType = _AtmConfIfCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 4),
    _AtmConfIfCardType_Type()
)
atmConfIfCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfIfCardType.setStatus("deprecated")


class _AtmConfAtmIfVpiVciLimit_Type(Integer32):
    """Custom type atmConfAtmIfVpiVciLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits15", 2),
          ("bits17", 3))
    )


_AtmConfAtmIfVpiVciLimit_Type.__name__ = "Integer32"
_AtmConfAtmIfVpiVciLimit_Object = MibTableColumn
atmConfAtmIfVpiVciLimit = _AtmConfAtmIfVpiVciLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 5),
    _AtmConfAtmIfVpiVciLimit_Type()
)
atmConfAtmIfVpiVciLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfAtmIfVpiVciLimit.setStatus("current")


class _AtmConfIfHwFeatures_Type(Integer32):
    """Custom type atmConfIfHwFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtmConfIfHwFeatures_Type.__name__ = "Integer32"
_AtmConfIfHwFeatures_Object = MibTableColumn
atmConfIfHwFeatures = _AtmConfIfHwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 6),
    _AtmConfIfHwFeatures_Type()
)
atmConfIfHwFeatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfHwFeatures.setStatus("current")
_AtmConfIfOutputRate_Type = Integer32
_AtmConfIfOutputRate_Object = MibTableColumn
atmConfIfOutputRate = _AtmConfIfOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 7),
    _AtmConfIfOutputRate_Type()
)
atmConfIfOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfOutputRate.setStatus("current")
_AtmConfIfInputRate_Type = Integer32
_AtmConfIfInputRate_Object = MibTableColumn
atmConfIfInputRate = _AtmConfIfInputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 8),
    _AtmConfIfInputRate_Type()
)
atmConfIfInputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfInputRate.setStatus("current")


class _AtmConfAlarmForwarding_Type(Integer32):
    """Custom type atmConfAlarmForwarding based on Integer32"""
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


_AtmConfAlarmForwarding_Type.__name__ = "Integer32"
_AtmConfAlarmForwarding_Object = MibTableColumn
atmConfAlarmForwarding = _AtmConfAlarmForwarding_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 9),
    _AtmConfAlarmForwarding_Type()
)
atmConfAlarmForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfAlarmForwarding.setStatus("current")
_AtmConfIfAllocatedBw_Type = Integer32
_AtmConfIfAllocatedBw_Object = MibTableColumn
atmConfIfAllocatedBw = _AtmConfIfAllocatedBw_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 10),
    _AtmConfIfAllocatedBw_Type()
)
atmConfIfAllocatedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfIfAllocatedBw.setStatus("current")
_AtmConfIfLowerVpi_Type = Integer32
_AtmConfIfLowerVpi_Object = MibTableColumn
atmConfIfLowerVpi = _AtmConfIfLowerVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 11),
    _AtmConfIfLowerVpi_Type()
)
atmConfIfLowerVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfLowerVpi.setStatus("current")


class _AtmConfIfOamMode_Type(Integer32):
    """Custom type atmConfIfOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("segmentTermination", 2),
          ("endToEndTermination", 3))
    )


_AtmConfIfOamMode_Type.__name__ = "Integer32"
_AtmConfIfOamMode_Object = MibTableColumn
atmConfIfOamMode = _AtmConfIfOamMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 12),
    _AtmConfIfOamMode_Type()
)
atmConfIfOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfOamMode.setStatus("current")


class _AtmConfIfOamFailureInd_Type(Integer32):
    """Custom type atmConfIfOamFailureInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ais", 3),
          ("rdi", 4),
          ("aisAndRdi", 5))
    )


_AtmConfIfOamFailureInd_Type.__name__ = "Integer32"
_AtmConfIfOamFailureInd_Object = MibTableColumn
atmConfIfOamFailureInd = _AtmConfIfOamFailureInd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 13),
    _AtmConfIfOamFailureInd_Type()
)
atmConfIfOamFailureInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfOamFailureInd.setStatus("current")
_AtmNteAlarmIfTable_Object = MibTable
atmNteAlarmIfTable = _AtmNteAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmNteAlarmIfTable.setStatus("current")
_AtmNteAlarmIfEntry_Object = MibTableRow
atmNteAlarmIfEntry = _AtmNteAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1)
)
atmNteAlarmIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmNteAlarmIfEntry.setStatus("current")
_AtmInterfaceActiveAlarms_Type = Integer32
_AtmInterfaceActiveAlarms_Object = MibTableColumn
atmInterfaceActiveAlarms = _AtmInterfaceActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 1),
    _AtmInterfaceActiveAlarms_Type()
)
atmInterfaceActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceActiveAlarms.setStatus("current")
_AtmThresholdSectionBIP_Type = Integer32
_AtmThresholdSectionBIP_Object = MibTableColumn
atmThresholdSectionBIP = _AtmThresholdSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 2),
    _AtmThresholdSectionBIP_Type()
)
atmThresholdSectionBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdSectionBIP.setStatus("current")
_AtmThresholdLineBIP_Type = Integer32
_AtmThresholdLineBIP_Object = MibTableColumn
atmThresholdLineBIP = _AtmThresholdLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 3),
    _AtmThresholdLineBIP_Type()
)
atmThresholdLineBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdLineBIP.setStatus("current")
_AtmThresholdLineFEBE_Type = Integer32
_AtmThresholdLineFEBE_Object = MibTableColumn
atmThresholdLineFEBE = _AtmThresholdLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 4),
    _AtmThresholdLineFEBE_Type()
)
atmThresholdLineFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdLineFEBE.setStatus("current")
_AtmThresholdPathBIP_Type = Integer32
_AtmThresholdPathBIP_Object = MibTableColumn
atmThresholdPathBIP = _AtmThresholdPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 5),
    _AtmThresholdPathBIP_Type()
)
atmThresholdPathBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdPathBIP.setStatus("current")
_AtmThresholdPathFEBE_Type = Integer32
_AtmThresholdPathFEBE_Object = MibTableColumn
atmThresholdPathFEBE = _AtmThresholdPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 6),
    _AtmThresholdPathFEBE_Type()
)
atmThresholdPathFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdPathFEBE.setStatus("current")
_AtmThresholdErroredCells_Type = Integer32
_AtmThresholdErroredCells_Object = MibTableColumn
atmThresholdErroredCells = _AtmThresholdErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 7),
    _AtmThresholdErroredCells_Type()
)
atmThresholdErroredCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdErroredCells.setStatus("current")
_AtmThresholdLostCells_Type = Integer32
_AtmThresholdLostCells_Object = MibTableColumn
atmThresholdLostCells = _AtmThresholdLostCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 8),
    _AtmThresholdLostCells_Type()
)
atmThresholdLostCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdLostCells.setStatus("current")
_AtmThresholdMisinsertedCells_Type = Integer32
_AtmThresholdMisinsertedCells_Object = MibTableColumn
atmThresholdMisinsertedCells = _AtmThresholdMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 9),
    _AtmThresholdMisinsertedCells_Type()
)
atmThresholdMisinsertedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdMisinsertedCells.setStatus("current")


class _AtmInterfaceAlarmStatus_Type(Integer32):
    """Custom type atmInterfaceAlarmStatus based on Integer32"""
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


_AtmInterfaceAlarmStatus_Type.__name__ = "Integer32"
_AtmInterfaceAlarmStatus_Object = MibTableColumn
atmInterfaceAlarmStatus = _AtmInterfaceAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 10),
    _AtmInterfaceAlarmStatus_Type()
)
atmInterfaceAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceAlarmStatus.setStatus("current")
_AtmInterfaceMaskAlarms_Type = Integer32
_AtmInterfaceMaskAlarms_Object = MibTableColumn
atmInterfaceMaskAlarms = _AtmInterfaceMaskAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 11),
    _AtmInterfaceMaskAlarms_Type()
)
atmInterfaceMaskAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaskAlarms.setStatus("current")
_AtmNteConfVpTable_Object = MibTable
atmNteConfVpTable = _AtmNteConfVpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmNteConfVpTable.setStatus("current")
_AtmNteConfVpEntry_Object = MibTableRow
atmNteConfVpEntry = _AtmNteConfVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1)
)
atmNteConfVpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmNteConfVpEntry.setStatus("current")


class _AtmConfVpPolicing_Type(Integer32):
    """Custom type atmConfVpPolicing based on Integer32"""
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
          ("police", 2),
          ("monitor", 3),
          ("shaping", 4),
          ("policingAndShaping", 5))
    )


_AtmConfVpPolicing_Type.__name__ = "Integer32"
_AtmConfVpPolicing_Object = MibTableColumn
atmConfVpPolicing = _AtmConfVpPolicing_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 1),
    _AtmConfVpPolicing_Type()
)
atmConfVpPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpPolicing.setStatus("current")


class _AtmConfVpCCAdminStatus_Type(Integer32):
    """Custom type atmConfVpCCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("source", 4),
          ("sink", 5),
          ("listenToActivationCells", 6),
          ("originateActivationCells", 7))
    )


_AtmConfVpCCAdminStatus_Type.__name__ = "Integer32"
_AtmConfVpCCAdminStatus_Object = MibTableColumn
atmConfVpCCAdminStatus = _AtmConfVpCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 2),
    _AtmConfVpCCAdminStatus_Type()
)
atmConfVpCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpCCAdminStatus.setStatus("current")


class _AtmConfVpLoopbackAdminStatus_Type(Integer32):
    """Custom type atmConfVpLoopbackAdminStatus based on Integer32"""
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
        *(("up", 2),
          ("down", 3),
          ("llid", 4),
          ("segment", 5),
          ("endToEnd", 6),
          ("segmentLlid", 7),
          ("endToEndLlid", 8))
    )


_AtmConfVpLoopbackAdminStatus_Type.__name__ = "Integer32"
_AtmConfVpLoopbackAdminStatus_Object = MibTableColumn
atmConfVpLoopbackAdminStatus = _AtmConfVpLoopbackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 3),
    _AtmConfVpLoopbackAdminStatus_Type()
)
atmConfVpLoopbackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackAdminStatus.setStatus("current")


class _AtmConfVpLoopbackSinkAddress_Type(OctetString):
    """Custom type atmConfVpLoopbackSinkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmConfVpLoopbackSinkAddress_Type.__name__ = "OctetString"
_AtmConfVpLoopbackSinkAddress_Object = MibTableColumn
atmConfVpLoopbackSinkAddress = _AtmConfVpLoopbackSinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 4),
    _AtmConfVpLoopbackSinkAddress_Type()
)
atmConfVpLoopbackSinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackSinkAddress.setStatus("current")
_AtmConfVpCongestionControl_Type = OctetString
_AtmConfVpCongestionControl_Object = MibTableColumn
atmConfVpCongestionControl = _AtmConfVpCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 5),
    _AtmConfVpCongestionControl_Type()
)
atmConfVpCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpCongestionControl.setStatus("current")


class _AtmConfVpCCDirection_Type(Integer32):
    """Custom type atmConfVpCCDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("source", 4),
          ("sink", 5))
    )


_AtmConfVpCCDirection_Type.__name__ = "Integer32"
_AtmConfVpCCDirection_Object = MibTableColumn
atmConfVpCCDirection = _AtmConfVpCCDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 6),
    _AtmConfVpCCDirection_Type()
)
atmConfVpCCDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpCCDirection.setStatus("current")
_AtmConfVpCreationTime_Type = DateAndTime
_AtmConfVpCreationTime_Object = MibTableColumn
atmConfVpCreationTime = _AtmConfVpCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 7),
    _AtmConfVpCreationTime_Type()
)
atmConfVpCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVpCreationTime.setStatus("current")


class _AtmConfVpOamSupport_Type(Integer32):
    """Custom type atmConfVpOamSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("segmentTermination", 2),
          ("endToEndTermination", 3))
    )


_AtmConfVpOamSupport_Type.__name__ = "Integer32"
_AtmConfVpOamSupport_Object = MibTableColumn
atmConfVpOamSupport = _AtmConfVpOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 8),
    _AtmConfVpOamSupport_Type()
)
atmConfVpOamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpOamSupport.setStatus("current")


class _AtmConfVpCCOperStatus_Type(Integer32):
    """Custom type atmConfVpCCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("source", 4),
          ("sink", 5),
          ("both", 8),
          ("timeout", 9),
          ("denied", 10),
          ("conflict", 11),
          ("manual", 12))
    )


_AtmConfVpCCOperStatus_Type.__name__ = "Integer32"
_AtmConfVpCCOperStatus_Object = MibTableColumn
atmConfVpCCOperStatus = _AtmConfVpCCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 9),
    _AtmConfVpCCOperStatus_Type()
)
atmConfVpCCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVpCCOperStatus.setStatus("current")


class _AtmConfVpLoopbackTraffic_Type(Integer32):
    """Custom type atmConfVpLoopbackTraffic based on Integer32"""
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


_AtmConfVpLoopbackTraffic_Type.__name__ = "Integer32"
_AtmConfVpLoopbackTraffic_Object = MibTableColumn
atmConfVpLoopbackTraffic = _AtmConfVpLoopbackTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 10),
    _AtmConfVpLoopbackTraffic_Type()
)
atmConfVpLoopbackTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackTraffic.setStatus("current")


class _AtmConfVpLoopbackFailureInd_Type(Integer32):
    """Custom type atmConfVpLoopbackFailureInd based on Integer32"""
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
        *(("disabled", 2),
          ("segmentAis", 3),
          ("segmentRdi", 4),
          ("segmentAisAndRdi", 5),
          ("endToEndAis", 6),
          ("endToEndRdi", 7),
          ("endToEndAisAndRdi", 8))
    )


_AtmConfVpLoopbackFailureInd_Type.__name__ = "Integer32"
_AtmConfVpLoopbackFailureInd_Object = MibTableColumn
atmConfVpLoopbackFailureInd = _AtmConfVpLoopbackFailureInd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 11),
    _AtmConfVpLoopbackFailureInd_Type()
)
atmConfVpLoopbackFailureInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackFailureInd.setStatus("current")
_AtmConfVpLoopbackFailureThreshold_Type = Integer32
_AtmConfVpLoopbackFailureThreshold_Object = MibTableColumn
atmConfVpLoopbackFailureThreshold = _AtmConfVpLoopbackFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 12),
    _AtmConfVpLoopbackFailureThreshold_Type()
)
atmConfVpLoopbackFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackFailureThreshold.setStatus("current")


class _AtmConfVpOamDirection_Type(Integer32):
    """Custom type atmConfVpOamDirection based on Integer32"""
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
          ("downStream", 2),
          ("upStream", 3))
    )


_AtmConfVpOamDirection_Type.__name__ = "Integer32"
_AtmConfVpOamDirection_Object = MibTableColumn
atmConfVpOamDirection = _AtmConfVpOamDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 13),
    _AtmConfVpOamDirection_Type()
)
atmConfVpOamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpOamDirection.setStatus("current")
_AtmConfVpOamDescrIndex_Type = Integer32
_AtmConfVpOamDescrIndex_Object = MibTableColumn
atmConfVpOamDescrIndex = _AtmConfVpOamDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 14),
    _AtmConfVpOamDescrIndex_Type()
)
atmConfVpOamDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpOamDescrIndex.setStatus("current")


class _AtmConfVpConnected_Type(Integer32):
    """Custom type atmConfVpConnected based on Integer32"""
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
        *(("notConnected", 1),
          ("mng", 2),
          ("bridgePort", 3),
          ("ds0Bundle", 4),
          ("atm", 5),
          ("pw", 6))
    )


_AtmConfVpConnected_Type.__name__ = "Integer32"
_AtmConfVpConnected_Object = MibTableColumn
atmConfVpConnected = _AtmConfVpConnected_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 15),
    _AtmConfVpConnected_Type()
)
atmConfVpConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpConnected.setStatus("current")
_AtmNteConfVcTable_Object = MibTable
atmNteConfVcTable = _AtmNteConfVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    atmNteConfVcTable.setStatus("current")
_AtmNteConfVcEntry_Object = MibTableRow
atmNteConfVcEntry = _AtmNteConfVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1)
)
atmNteConfVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmNteConfVcEntry.setStatus("current")


class _AtmConfVcPolicing_Type(Integer32):
    """Custom type atmConfVcPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("police", 2),
          ("monitor", 3),
          ("shaping", 4),
          ("policingAndShaping", 5),
          ("notApplicable", 255))
    )


_AtmConfVcPolicing_Type.__name__ = "Integer32"
_AtmConfVcPolicing_Object = MibTableColumn
atmConfVcPolicing = _AtmConfVcPolicing_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 1),
    _AtmConfVcPolicing_Type()
)
atmConfVcPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcPolicing.setStatus("current")


class _AtmConfVcCCAdminStatus_Type(Integer32):
    """Custom type atmConfVcCCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("source", 4),
          ("sink", 5),
          ("listenToActivationCells", 6),
          ("originateActivationCells", 7))
    )


_AtmConfVcCCAdminStatus_Type.__name__ = "Integer32"
_AtmConfVcCCAdminStatus_Object = MibTableColumn
atmConfVcCCAdminStatus = _AtmConfVcCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 2),
    _AtmConfVcCCAdminStatus_Type()
)
atmConfVcCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCCAdminStatus.setStatus("current")


class _AtmConfVcLoopbackAdminStatus_Type(Integer32):
    """Custom type atmConfVcLoopbackAdminStatus based on Integer32"""
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
        *(("up", 2),
          ("down", 3),
          ("llid", 4),
          ("segment", 5),
          ("endToEnd", 6),
          ("segmentLlid", 7),
          ("endToEndLlid", 8))
    )


_AtmConfVcLoopbackAdminStatus_Type.__name__ = "Integer32"
_AtmConfVcLoopbackAdminStatus_Object = MibTableColumn
atmConfVcLoopbackAdminStatus = _AtmConfVcLoopbackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 3),
    _AtmConfVcLoopbackAdminStatus_Type()
)
atmConfVcLoopbackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackAdminStatus.setStatus("current")


class _AtmConfVcLoopbackSinkAddress_Type(OctetString):
    """Custom type atmConfVcLoopbackSinkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )


_AtmConfVcLoopbackSinkAddress_Type.__name__ = "OctetString"
_AtmConfVcLoopbackSinkAddress_Object = MibTableColumn
atmConfVcLoopbackSinkAddress = _AtmConfVcLoopbackSinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 4),
    _AtmConfVcLoopbackSinkAddress_Type()
)
atmConfVcLoopbackSinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackSinkAddress.setStatus("current")
_AtmConfVcCongestionControl_Type = OctetString
_AtmConfVcCongestionControl_Object = MibTableColumn
atmConfVcCongestionControl = _AtmConfVcCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 5),
    _AtmConfVcCongestionControl_Type()
)
atmConfVcCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCongestionControl.setStatus("current")


class _AtmConfVcCCDirection_Type(Integer32):
    """Custom type atmConfVcCCDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("none", 3),
          ("source", 4),
          ("sink", 5))
    )


_AtmConfVcCCDirection_Type.__name__ = "Integer32"
_AtmConfVcCCDirection_Object = MibTableColumn
atmConfVcCCDirection = _AtmConfVcCCDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 6),
    _AtmConfVcCCDirection_Type()
)
atmConfVcCCDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCCDirection.setStatus("current")
_AtmConfVcCreationTime_Type = DateAndTime
_AtmConfVcCreationTime_Object = MibTableColumn
atmConfVcCreationTime = _AtmConfVcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 7),
    _AtmConfVcCreationTime_Type()
)
atmConfVcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVcCreationTime.setStatus("current")


class _AtmConfVcOamSupport_Type(Integer32):
    """Custom type atmConfVcOamSupport based on Integer32"""
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
        *(("intermediate", 1),
          ("segmentTermination", 2),
          ("endToEndTermination", 3),
          ("endToEndAndSegment", 4))
    )


_AtmConfVcOamSupport_Type.__name__ = "Integer32"
_AtmConfVcOamSupport_Object = MibTableColumn
atmConfVcOamSupport = _AtmConfVcOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 8),
    _AtmConfVcOamSupport_Type()
)
atmConfVcOamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcOamSupport.setStatus("current")


class _AtmConfVcCCActivationCtrl_Type(Integer32):
    """Custom type atmConfVcCCActivationCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("activator", 2),
          ("listener", 3))
    )


_AtmConfVcCCActivationCtrl_Type.__name__ = "Integer32"
_AtmConfVcCCActivationCtrl_Object = MibTableColumn
atmConfVcCCActivationCtrl = _AtmConfVcCCActivationCtrl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 9),
    _AtmConfVcCCActivationCtrl_Type()
)
atmConfVcCCActivationCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCCActivationCtrl.setStatus("current")


class _AtmConfVcCCOperStatus_Type(Integer32):
    """Custom type atmConfVcCCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("up", 2),
          ("down", 3),
          ("source", 4),
          ("sink", 5),
          ("both", 8),
          ("timeout", 9),
          ("denied", 10),
          ("conflict", 11),
          ("manual", 12))
    )


_AtmConfVcCCOperStatus_Type.__name__ = "Integer32"
_AtmConfVcCCOperStatus_Object = MibTableColumn
atmConfVcCCOperStatus = _AtmConfVcCCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 10),
    _AtmConfVcCCOperStatus_Type()
)
atmConfVcCCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVcCCOperStatus.setStatus("current")


class _AtmConfVcLoopbackTraffic_Type(Integer32):
    """Custom type atmConfVcLoopbackTraffic based on Integer32"""
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


_AtmConfVcLoopbackTraffic_Type.__name__ = "Integer32"
_AtmConfVcLoopbackTraffic_Object = MibTableColumn
atmConfVcLoopbackTraffic = _AtmConfVcLoopbackTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 11),
    _AtmConfVcLoopbackTraffic_Type()
)
atmConfVcLoopbackTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackTraffic.setStatus("current")


class _AtmConfVcLoopbackFailureInd_Type(Integer32):
    """Custom type atmConfVcLoopbackFailureInd based on Integer32"""
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
        *(("disabled", 2),
          ("segmentAis", 3),
          ("segmentRdi", 4),
          ("segmentAisAndRdi", 5),
          ("endToEndAis", 6),
          ("endToEndRdi", 7),
          ("endToEndAisAndRdi", 8))
    )


_AtmConfVcLoopbackFailureInd_Type.__name__ = "Integer32"
_AtmConfVcLoopbackFailureInd_Object = MibTableColumn
atmConfVcLoopbackFailureInd = _AtmConfVcLoopbackFailureInd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 12),
    _AtmConfVcLoopbackFailureInd_Type()
)
atmConfVcLoopbackFailureInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackFailureInd.setStatus("current")
_AtmConfVcLoopbackFailureThreshold_Type = Integer32
_AtmConfVcLoopbackFailureThreshold_Object = MibTableColumn
atmConfVcLoopbackFailureThreshold = _AtmConfVcLoopbackFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 13),
    _AtmConfVcLoopbackFailureThreshold_Type()
)
atmConfVcLoopbackFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackFailureThreshold.setStatus("current")


class _AtmConfVcOamDirection_Type(Integer32):
    """Custom type atmConfVcOamDirection based on Integer32"""
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
          ("downStream", 2),
          ("upStream", 3))
    )


_AtmConfVcOamDirection_Type.__name__ = "Integer32"
_AtmConfVcOamDirection_Object = MibTableColumn
atmConfVcOamDirection = _AtmConfVcOamDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 14),
    _AtmConfVcOamDirection_Type()
)
atmConfVcOamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcOamDirection.setStatus("current")
_AtmConfVcName_Type = DisplayString
_AtmConfVcName_Object = MibTableColumn
atmConfVcName = _AtmConfVcName_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 15),
    _AtmConfVcName_Type()
)
atmConfVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcName.setStatus("current")


class _AtmConfVcConnected_Type(Integer32):
    """Custom type atmConfVcConnected based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("mng", 2),
          ("bridgePort", 3),
          ("ds0Bundle", 4),
          ("atm", 5),
          ("pw", 6),
          ("routerInterface", 7),
          ("qos", 8),
          ("other", 9),
          ("logicalMac", 10),
          ("atmAal2", 11))
    )


_AtmConfVcConnected_Type.__name__ = "Integer32"
_AtmConfVcConnected_Object = MibTableColumn
atmConfVcConnected = _AtmConfVcConnected_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 16),
    _AtmConfVcConnected_Type()
)
atmConfVcConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcConnected.setStatus("current")
_AtmConfVcOamDescrIndex_Type = Integer32
_AtmConfVcOamDescrIndex_Object = MibTableColumn
atmConfVcOamDescrIndex = _AtmConfVcOamDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 17),
    _AtmConfVcOamDescrIndex_Type()
)
atmConfVcOamDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcOamDescrIndex.setStatus("current")
_AtmConfVcNoOfUsages_Type = Unsigned32
_AtmConfVcNoOfUsages_Object = MibTableColumn
atmConfVcNoOfUsages = _AtmConfVcNoOfUsages_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 18),
    _AtmConfVcNoOfUsages_Type()
)
atmConfVcNoOfUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVcNoOfUsages.setStatus("current")
_AtmNteAlarmVpTable_Object = MibTable
atmNteAlarmVpTable = _AtmNteAlarmVpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    atmNteAlarmVpTable.setStatus("current")
_AtmNteAlarmVpEntry_Object = MibTableRow
atmNteAlarmVpEntry = _AtmNteAlarmVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5, 1)
)
atmNteAlarmVpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-NtePrtCo-MIB", "atmNteVpAlarmVpi"),
)
if mibBuilder.loadTexts:
    atmNteAlarmVpEntry.setStatus("current")
_AtmNteVpAlarmVpi_Type = Integer32
_AtmNteVpAlarmVpi_Object = MibTableColumn
atmNteVpAlarmVpi = _AtmNteVpAlarmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5, 1, 1),
    _AtmNteVpAlarmVpi_Type()
)
atmNteVpAlarmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVpAlarmVpi.setStatus("current")
_AtmNteVpActiveAlarms_Type = Integer32
_AtmNteVpActiveAlarms_Object = MibTableColumn
atmNteVpActiveAlarms = _AtmNteVpActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5, 1, 2),
    _AtmNteVpActiveAlarms_Type()
)
atmNteVpActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVpActiveAlarms.setStatus("current")
_AtmNteAlarmVcTable_Object = MibTable
atmNteAlarmVcTable = _AtmNteAlarmVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    atmNteAlarmVcTable.setStatus("current")
_AtmNteAlarmVcEntry_Object = MibTableRow
atmNteAlarmVcEntry = _AtmNteAlarmVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1)
)
atmNteAlarmVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-NtePrtCo-MIB", "atmNteVcAlarmVpi"),
    (0, "RAD-NtePrtCo-MIB", "atmNteVcAlarmVci"),
)
if mibBuilder.loadTexts:
    atmNteAlarmVcEntry.setStatus("current")
_AtmNteVcAlarmVpi_Type = Integer32
_AtmNteVcAlarmVpi_Object = MibTableColumn
atmNteVcAlarmVpi = _AtmNteVcAlarmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1, 1),
    _AtmNteVcAlarmVpi_Type()
)
atmNteVcAlarmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVcAlarmVpi.setStatus("current")
_AtmNteVcAlarmVci_Type = Integer32
_AtmNteVcAlarmVci_Object = MibTableColumn
atmNteVcAlarmVci = _AtmNteVcAlarmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1, 2),
    _AtmNteVcAlarmVci_Type()
)
atmNteVcAlarmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVcAlarmVci.setStatus("current")
_AtmNteVcActiveAlarms_Type = Integer32
_AtmNteVcActiveAlarms_Object = MibTableColumn
atmNteVcActiveAlarms = _AtmNteVcActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1, 3),
    _AtmNteVcActiveAlarms_Type()
)
atmNteVcActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVcActiveAlarms.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-NtePrtCo-MIB",
    **{"radAtm": radAtm,
       "atmNte": atmNte,
       "atmNteEvents": atmNteEvents,
       "atmNtePrt": atmNtePrt,
       "atmNtePrtConfig": atmNtePrtConfig,
       "atmNteConfIfTable": atmNteConfIfTable,
       "atmNteConfIfEntry": atmNteConfIfEntry,
       "atmConfIfTransmitClk": atmConfIfTransmitClk,
       "atmConfIfLoopback": atmConfIfLoopback,
       "atmConfIfFrameType": atmConfIfFrameType,
       "atmConfIfCardType": atmConfIfCardType,
       "atmConfAtmIfVpiVciLimit": atmConfAtmIfVpiVciLimit,
       "atmConfIfHwFeatures": atmConfIfHwFeatures,
       "atmConfIfOutputRate": atmConfIfOutputRate,
       "atmConfIfInputRate": atmConfIfInputRate,
       "atmConfAlarmForwarding": atmConfAlarmForwarding,
       "atmConfIfAllocatedBw": atmConfIfAllocatedBw,
       "atmConfIfLowerVpi": atmConfIfLowerVpi,
       "atmConfIfOamMode": atmConfIfOamMode,
       "atmConfIfOamFailureInd": atmConfIfOamFailureInd,
       "atmNteAlarmIfTable": atmNteAlarmIfTable,
       "atmNteAlarmIfEntry": atmNteAlarmIfEntry,
       "atmInterfaceActiveAlarms": atmInterfaceActiveAlarms,
       "atmThresholdSectionBIP": atmThresholdSectionBIP,
       "atmThresholdLineBIP": atmThresholdLineBIP,
       "atmThresholdLineFEBE": atmThresholdLineFEBE,
       "atmThresholdPathBIP": atmThresholdPathBIP,
       "atmThresholdPathFEBE": atmThresholdPathFEBE,
       "atmThresholdErroredCells": atmThresholdErroredCells,
       "atmThresholdLostCells": atmThresholdLostCells,
       "atmThresholdMisinsertedCells": atmThresholdMisinsertedCells,
       "atmInterfaceAlarmStatus": atmInterfaceAlarmStatus,
       "atmInterfaceMaskAlarms": atmInterfaceMaskAlarms,
       "atmNteConfVpTable": atmNteConfVpTable,
       "atmNteConfVpEntry": atmNteConfVpEntry,
       "atmConfVpPolicing": atmConfVpPolicing,
       "atmConfVpCCAdminStatus": atmConfVpCCAdminStatus,
       "atmConfVpLoopbackAdminStatus": atmConfVpLoopbackAdminStatus,
       "atmConfVpLoopbackSinkAddress": atmConfVpLoopbackSinkAddress,
       "atmConfVpCongestionControl": atmConfVpCongestionControl,
       "atmConfVpCCDirection": atmConfVpCCDirection,
       "atmConfVpCreationTime": atmConfVpCreationTime,
       "atmConfVpOamSupport": atmConfVpOamSupport,
       "atmConfVpCCOperStatus": atmConfVpCCOperStatus,
       "atmConfVpLoopbackTraffic": atmConfVpLoopbackTraffic,
       "atmConfVpLoopbackFailureInd": atmConfVpLoopbackFailureInd,
       "atmConfVpLoopbackFailureThreshold": atmConfVpLoopbackFailureThreshold,
       "atmConfVpOamDirection": atmConfVpOamDirection,
       "atmConfVpOamDescrIndex": atmConfVpOamDescrIndex,
       "atmConfVpConnected": atmConfVpConnected,
       "atmNteConfVcTable": atmNteConfVcTable,
       "atmNteConfVcEntry": atmNteConfVcEntry,
       "atmConfVcPolicing": atmConfVcPolicing,
       "atmConfVcCCAdminStatus": atmConfVcCCAdminStatus,
       "atmConfVcLoopbackAdminStatus": atmConfVcLoopbackAdminStatus,
       "atmConfVcLoopbackSinkAddress": atmConfVcLoopbackSinkAddress,
       "atmConfVcCongestionControl": atmConfVcCongestionControl,
       "atmConfVcCCDirection": atmConfVcCCDirection,
       "atmConfVcCreationTime": atmConfVcCreationTime,
       "atmConfVcOamSupport": atmConfVcOamSupport,
       "atmConfVcCCActivationCtrl": atmConfVcCCActivationCtrl,
       "atmConfVcCCOperStatus": atmConfVcCCOperStatus,
       "atmConfVcLoopbackTraffic": atmConfVcLoopbackTraffic,
       "atmConfVcLoopbackFailureInd": atmConfVcLoopbackFailureInd,
       "atmConfVcLoopbackFailureThreshold": atmConfVcLoopbackFailureThreshold,
       "atmConfVcOamDirection": atmConfVcOamDirection,
       "atmConfVcName": atmConfVcName,
       "atmConfVcConnected": atmConfVcConnected,
       "atmConfVcOamDescrIndex": atmConfVcOamDescrIndex,
       "atmConfVcNoOfUsages": atmConfVcNoOfUsages,
       "atmNteAlarmVpTable": atmNteAlarmVpTable,
       "atmNteAlarmVpEntry": atmNteAlarmVpEntry,
       "atmNteVpAlarmVpi": atmNteVpAlarmVpi,
       "atmNteVpActiveAlarms": atmNteVpActiveAlarms,
       "atmNteAlarmVcTable": atmNteAlarmVcTable,
       "atmNteAlarmVcEntry": atmNteAlarmVcEntry,
       "atmNteVcAlarmVpi": atmNteVcAlarmVpi,
       "atmNteVcAlarmVci": atmNteVcAlarmVci,
       "atmNteVcActiveAlarms": atmNteVcActiveAlarms}
)
