# SNMP MIB module (RAISECOM-ELPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-ELPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:29 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "Vlanset")


# MODULE-IDENTITY

rcElps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcElpsBaseGroup_ObjectIdentity = ObjectIdentity
rcElpsBaseGroup = _RcElpsBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1)
)


class _RcElpsTrapEnable_Type(EnableVar):
    """Custom type rcElpsTrapEnable based on EnableVar"""
    defaultValue = 2


_RcElpsTrapEnable_Type.__name__ = "EnableVar"
_RcElpsTrapEnable_Object = MibScalar
rcElpsTrapEnable = _RcElpsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 1),
    _RcElpsTrapEnable_Type()
)
rcElpsTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsTrapEnable.setStatus("current")
_RcElpsCfgTable_Object = MibTable
rcElpsCfgTable = _RcElpsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2)
)
if mibBuilder.loadTexts:
    rcElpsCfgTable.setStatus("current")
_RcElpsCfgEntry_Object = MibTableRow
rcElpsCfgEntry = _RcElpsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1)
)
rcElpsCfgEntry.setIndexNames(
    (0, "RAISECOM-ELPS-MIB", "rcElpsId"),
)
if mibBuilder.loadTexts:
    rcElpsCfgEntry.setStatus("current")


class _RcElpsId_Type(Unsigned32):
    """Custom type rcElpsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcElpsId_Type.__name__ = "Unsigned32"
_RcElpsId_Object = MibTableColumn
rcElpsId = _RcElpsId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 1),
    _RcElpsId_Type()
)
rcElpsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcElpsId.setStatus("current")


class _RcElpsName_Type(OctetString):
    """Custom type rcElpsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RcElpsName_Type.__name__ = "OctetString"
_RcElpsName_Object = MibTableColumn
rcElpsName = _RcElpsName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 2),
    _RcElpsName_Type()
)
rcElpsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsName.setStatus("current")
_RcElpsWorkingPort_Type = Integer32
_RcElpsWorkingPort_Object = MibTableColumn
rcElpsWorkingPort = _RcElpsWorkingPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 3),
    _RcElpsWorkingPort_Type()
)
rcElpsWorkingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsWorkingPort.setStatus("current")
_RcElpsWorkingBlockVlanlist_Type = Vlanset
_RcElpsWorkingBlockVlanlist_Object = MibTableColumn
rcElpsWorkingBlockVlanlist = _RcElpsWorkingBlockVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 4),
    _RcElpsWorkingBlockVlanlist_Type()
)
rcElpsWorkingBlockVlanlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsWorkingBlockVlanlist.setStatus("current")
_RcElpsProtectionPort_Type = Integer32
_RcElpsProtectionPort_Object = MibTableColumn
rcElpsProtectionPort = _RcElpsProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 5),
    _RcElpsProtectionPort_Type()
)
rcElpsProtectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsProtectionPort.setStatus("current")
_RcElpsProtectionBlockVlanlist_Type = Vlanset
_RcElpsProtectionBlockVlanlist_Object = MibTableColumn
rcElpsProtectionBlockVlanlist = _RcElpsProtectionBlockVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 6),
    _RcElpsProtectionBlockVlanlist_Type()
)
rcElpsProtectionBlockVlanlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsProtectionBlockVlanlist.setStatus("current")


class _RcElpsProtectionTypeAdmin_Type(Unsigned32):
    """Custom type rcElpsProtectionTypeAdmin based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RcElpsProtectionTypeAdmin_Type.__name__ = "Unsigned32"
_RcElpsProtectionTypeAdmin_Object = MibTableColumn
rcElpsProtectionTypeAdmin = _RcElpsProtectionTypeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 7),
    _RcElpsProtectionTypeAdmin_Type()
)
rcElpsProtectionTypeAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsProtectionTypeAdmin.setStatus("current")


class _RcElpsProtectionTypeOper_Type(Unsigned32):
    """Custom type rcElpsProtectionTypeOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RcElpsProtectionTypeOper_Type.__name__ = "Unsigned32"
_RcElpsProtectionTypeOper_Object = MibTableColumn
rcElpsProtectionTypeOper = _RcElpsProtectionTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 8),
    _RcElpsProtectionTypeOper_Type()
)
rcElpsProtectionTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsProtectionTypeOper.setStatus("current")


class _RcElpsForceSwitch_Type(TruthValue):
    """Custom type rcElpsForceSwitch based on TruthValue"""
    defaultValue = 2


_RcElpsForceSwitch_Type.__name__ = "TruthValue"
_RcElpsForceSwitch_Object = MibTableColumn
rcElpsForceSwitch = _RcElpsForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 9),
    _RcElpsForceSwitch_Type()
)
rcElpsForceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsForceSwitch.setStatus("current")


class _RcElpsManualSwitch_Type(TruthValue):
    """Custom type rcElpsManualSwitch based on TruthValue"""
    defaultValue = 2


_RcElpsManualSwitch_Type.__name__ = "TruthValue"
_RcElpsManualSwitch_Object = MibTableColumn
rcElpsManualSwitch = _RcElpsManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 10),
    _RcElpsManualSwitch_Type()
)
rcElpsManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsManualSwitch.setStatus("current")


class _RcElpsManualSwitchtoWork_Type(TruthValue):
    """Custom type rcElpsManualSwitchtoWork based on TruthValue"""
    defaultValue = 2


_RcElpsManualSwitchtoWork_Type.__name__ = "TruthValue"
_RcElpsManualSwitchtoWork_Object = MibTableColumn
rcElpsManualSwitchtoWork = _RcElpsManualSwitchtoWork_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 11),
    _RcElpsManualSwitchtoWork_Type()
)
rcElpsManualSwitchtoWork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsManualSwitchtoWork.setStatus("current")


class _RcElpsLockout_Type(TruthValue):
    """Custom type rcElpsLockout based on TruthValue"""
    defaultValue = 2


_RcElpsLockout_Type.__name__ = "TruthValue"
_RcElpsLockout_Object = MibTableColumn
rcElpsLockout = _RcElpsLockout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 12),
    _RcElpsLockout_Type()
)
rcElpsLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsLockout.setStatus("current")


class _RcElpsClear_Type(TruthValue):
    """Custom type rcElpsClear based on TruthValue"""
    defaultValue = 2


_RcElpsClear_Type.__name__ = "TruthValue"
_RcElpsClear_Object = MibTableColumn
rcElpsClear = _RcElpsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 13),
    _RcElpsClear_Type()
)
rcElpsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsClear.setStatus("current")


class _RcElpsWtrTimer_Type(Unsigned32):
    """Custom type rcElpsWtrTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RcElpsWtrTimer_Type.__name__ = "Unsigned32"
_RcElpsWtrTimer_Object = MibTableColumn
rcElpsWtrTimer = _RcElpsWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 14),
    _RcElpsWtrTimer_Type()
)
rcElpsWtrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsWtrTimer.setStatus("current")


class _RcElpsHoldOffTimer_Type(Unsigned32):
    """Custom type rcElpsHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RcElpsHoldOffTimer_Type.__name__ = "Unsigned32"
_RcElpsHoldOffTimer_Object = MibTableColumn
rcElpsHoldOffTimer = _RcElpsHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 15),
    _RcElpsHoldOffTimer_Type()
)
rcElpsHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsHoldOffTimer.setStatus("current")


class _RcElpsProtocolVlan_Type(Integer32):
    """Custom type rcElpsProtocolVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcElpsProtocolVlan_Type.__name__ = "Integer32"
_RcElpsProtocolVlan_Object = MibTableColumn
rcElpsProtocolVlan = _RcElpsProtocolVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 16),
    _RcElpsProtocolVlan_Type()
)
rcElpsProtocolVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsProtocolVlan.setStatus("current")


class _RcElpsStatus_Type(Integer32):
    """Custom type rcElpsStatus based on Integer32"""
    defaultValue = 1

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("nr-w", 1),
          ("nr-p", 2),
          ("lo", 3),
          ("fs", 4),
          ("sf-w", 5),
          ("sf-p", 6),
          ("ms", 7),
          ("ms-w", 8),
          ("wtr", 9),
          ("dnr", 10))
    )


_RcElpsStatus_Type.__name__ = "Integer32"
_RcElpsStatus_Object = MibTableColumn
rcElpsStatus = _RcElpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 17),
    _RcElpsStatus_Type()
)
rcElpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatus.setStatus("current")


class _RcElpsDfopStatus_Type(Integer32):
    """Custom type rcElpsDfopStatus based on Integer32"""
    defaultValue = 1

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
        *(("normal", 1),
          ("dFOP-CM", 2),
          ("dFOP-PM", 3),
          ("dFOP-NR", 4))
    )


_RcElpsDfopStatus_Type.__name__ = "Integer32"
_RcElpsDfopStatus_Object = MibTableColumn
rcElpsDfopStatus = _RcElpsDfopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 18),
    _RcElpsDfopStatus_Type()
)
rcElpsDfopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsDfopStatus.setStatus("current")
_RcElpsRowStatus_Type = RowStatus
_RcElpsRowStatus_Object = MibTableColumn
rcElpsRowStatus = _RcElpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 2, 1, 19),
    _RcElpsRowStatus_Type()
)
rcElpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcElpsRowStatus.setStatus("current")
_RcElpsStatisticsTable_Object = MibTable
rcElpsStatisticsTable = _RcElpsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3)
)
if mibBuilder.loadTexts:
    rcElpsStatisticsTable.setStatus("current")
_RcElpsStatisticsEntry_Object = MibTableRow
rcElpsStatisticsEntry = _RcElpsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1)
)
rcElpsStatisticsEntry.setIndexNames(
    (0, "RAISECOM-ELPS-MIB", "rcElpsId"),
)
if mibBuilder.loadTexts:
    rcElpsStatisticsEntry.setStatus("current")
_RcElpsStatisticsSwitchCounts_Type = Unsigned32
_RcElpsStatisticsSwitchCounts_Object = MibTableColumn
rcElpsStatisticsSwitchCounts = _RcElpsStatisticsSwitchCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 1),
    _RcElpsStatisticsSwitchCounts_Type()
)
rcElpsStatisticsSwitchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatisticsSwitchCounts.setStatus("current")
_RcElpsStatisticsApsTx_Type = Unsigned32
_RcElpsStatisticsApsTx_Object = MibTableColumn
rcElpsStatisticsApsTx = _RcElpsStatisticsApsTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 2),
    _RcElpsStatisticsApsTx_Type()
)
rcElpsStatisticsApsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatisticsApsTx.setStatus("current")
_RcElpsStatisticsApsRx_Type = Unsigned32
_RcElpsStatisticsApsRx_Object = MibTableColumn
rcElpsStatisticsApsRx = _RcElpsStatisticsApsRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 3),
    _RcElpsStatisticsApsRx_Type()
)
rcElpsStatisticsApsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatisticsApsRx.setStatus("current")
_RcElpsStatisticsLastStatusOccur_Type = TimeTicks
_RcElpsStatisticsLastStatusOccur_Object = MibTableColumn
rcElpsStatisticsLastStatusOccur = _RcElpsStatisticsLastStatusOccur_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 4),
    _RcElpsStatisticsLastStatusOccur_Type()
)
rcElpsStatisticsLastStatusOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatisticsLastStatusOccur.setStatus("current")
_RcElpsStatisticsLastSwitchOccur_Type = TimeTicks
_RcElpsStatisticsLastSwitchOccur_Object = MibTableColumn
rcElpsStatisticsLastSwitchOccur = _RcElpsStatisticsLastSwitchOccur_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 5),
    _RcElpsStatisticsLastSwitchOccur_Type()
)
rcElpsStatisticsLastSwitchOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatisticsLastSwitchOccur.setStatus("current")
_RcElpsStatisticsLastDfop_Type = TimeTicks
_RcElpsStatisticsLastDfop_Object = MibTableColumn
rcElpsStatisticsLastDfop = _RcElpsStatisticsLastDfop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 6),
    _RcElpsStatisticsLastDfop_Type()
)
rcElpsStatisticsLastDfop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsStatisticsLastDfop.setStatus("current")


class _RcElpsStatisticsClear_Type(EnableVar):
    """Custom type rcElpsStatisticsClear based on EnableVar"""
    defaultValue = 2


_RcElpsStatisticsClear_Type.__name__ = "EnableVar"
_RcElpsStatisticsClear_Object = MibTableColumn
rcElpsStatisticsClear = _RcElpsStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 3, 1, 7),
    _RcElpsStatisticsClear_Type()
)
rcElpsStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsStatisticsClear.setStatus("current")
_RcElpsPeerTable_Object = MibTable
rcElpsPeerTable = _RcElpsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 4)
)
if mibBuilder.loadTexts:
    rcElpsPeerTable.setStatus("current")
_RcElpsPeerEntry_Object = MibTableRow
rcElpsPeerEntry = _RcElpsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 4, 1)
)
rcElpsPeerEntry.setIndexNames(
    (0, "RAISECOM-ELPS-MIB", "rcElpsId"),
)
if mibBuilder.loadTexts:
    rcElpsPeerEntry.setStatus("current")


class _RcElpsPeerProtectionType_Type(Unsigned32):
    """Custom type rcElpsPeerProtectionType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 15),
    )


_RcElpsPeerProtectionType_Type.__name__ = "Unsigned32"
_RcElpsPeerProtectionType_Object = MibTableColumn
rcElpsPeerProtectionType = _RcElpsPeerProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 4, 1, 1),
    _RcElpsPeerProtectionType_Type()
)
rcElpsPeerProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsPeerProtectionType.setStatus("current")


class _RcElpsPeerStatus_Type(Integer32):
    """Custom type rcElpsPeerStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("nr-w", 1),
          ("nr-p", 2),
          ("lo", 3),
          ("fs", 4),
          ("sf-w", 5),
          ("sf-p", 6),
          ("ms", 7),
          ("ms-w", 8),
          ("wtr", 9),
          ("dnr", 10),
          ("sd", 11),
          ("exer", 12),
          ("rr", 13))
    )


_RcElpsPeerStatus_Type.__name__ = "Integer32"
_RcElpsPeerStatus_Object = MibTableColumn
rcElpsPeerStatus = _RcElpsPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 4, 1, 2),
    _RcElpsPeerStatus_Type()
)
rcElpsPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsPeerStatus.setStatus("current")


class _RcElpsRequestSignal_Type(Integer32):
    """Custom type rcElpsRequestSignal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("normal-traffic-signal", 1))
    )


_RcElpsRequestSignal_Type.__name__ = "Integer32"
_RcElpsRequestSignal_Object = MibTableColumn
rcElpsRequestSignal = _RcElpsRequestSignal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 4, 1, 3),
    _RcElpsRequestSignal_Type()
)
rcElpsRequestSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsRequestSignal.setStatus("current")


class _RcElpsBridgedSignal_Type(Integer32):
    """Custom type rcElpsBridgedSignal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("normal-traffic-signal", 1))
    )


_RcElpsBridgedSignal_Type.__name__ = "Integer32"
_RcElpsBridgedSignal_Object = MibTableColumn
rcElpsBridgedSignal = _RcElpsBridgedSignal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 4, 1, 4),
    _RcElpsBridgedSignal_Type()
)
rcElpsBridgedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsBridgedSignal.setStatus("current")
_RcElpsNotifications_ObjectIdentity = ObjectIdentity
rcElpsNotifications = _RcElpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 5)
)
_RcElpsFailureDetGroup_ObjectIdentity = ObjectIdentity
rcElpsFailureDetGroup = _RcElpsFailureDetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2)
)
_RcElpsFailureDetTable_Object = MibTable
rcElpsFailureDetTable = _RcElpsFailureDetTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1)
)
if mibBuilder.loadTexts:
    rcElpsFailureDetTable.setStatus("current")
_RcElpsFailureDetEntry_Object = MibTableRow
rcElpsFailureDetEntry = _RcElpsFailureDetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1)
)
rcElpsFailureDetEntry.setIndexNames(
    (0, "RAISECOM-ELPS-MIB", "rcElpsId"),
    (0, "RAISECOM-ELPS-MIB", "rcElpsFdLink"),
)
if mibBuilder.loadTexts:
    rcElpsFailureDetEntry.setStatus("current")


class _RcElpsFdLink_Type(Integer32):
    """Custom type rcElpsFdLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protection", 2))
    )


_RcElpsFdLink_Type.__name__ = "Integer32"
_RcElpsFdLink_Object = MibTableColumn
rcElpsFdLink = _RcElpsFdLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 1),
    _RcElpsFdLink_Type()
)
rcElpsFdLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcElpsFdLink.setStatus("current")


class _RcElpsFdType_Type(Integer32):
    """Custom type rcElpsFdType based on Integer32"""
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
        *(("physical-link", 1),
          ("cc", 2),
          ("both", 3))
    )


_RcElpsFdType_Type.__name__ = "Integer32"
_RcElpsFdType_Object = MibTableColumn
rcElpsFdType = _RcElpsFdType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 2),
    _RcElpsFdType_Type()
)
rcElpsFdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsFdType.setStatus("current")


class _RcElpsFdLinkStatus_Type(Integer32):
    """Custom type rcElpsFdLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("sf", 2))
    )


_RcElpsFdLinkStatus_Type.__name__ = "Integer32"
_RcElpsFdLinkStatus_Object = MibTableColumn
rcElpsFdLinkStatus = _RcElpsFdLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 3),
    _RcElpsFdLinkStatus_Type()
)
rcElpsFdLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsFdLinkStatus.setStatus("current")


class _RcElpsFdSfType_Type(Integer32):
    """Custom type rcElpsFdSfType based on Integer32"""
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
        *(("none", 1),
          ("physical-link", 2),
          ("cc", 3),
          ("both", 4))
    )


_RcElpsFdSfType_Type.__name__ = "Integer32"
_RcElpsFdSfType_Object = MibTableColumn
rcElpsFdSfType = _RcElpsFdSfType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 4),
    _RcElpsFdSfType_Type()
)
rcElpsFdSfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcElpsFdSfType.setStatus("current")


class _RcElpsFdMdName_Type(OctetString):
    """Custom type rcElpsFdMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcElpsFdMdName_Type.__name__ = "OctetString"
_RcElpsFdMdName_Object = MibTableColumn
rcElpsFdMdName = _RcElpsFdMdName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 5),
    _RcElpsFdMdName_Type()
)
rcElpsFdMdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsFdMdName.setStatus("current")


class _RcElpsFdMaName_Type(OctetString):
    """Custom type rcElpsFdMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_RcElpsFdMaName_Type.__name__ = "OctetString"
_RcElpsFdMaName_Object = MibTableColumn
rcElpsFdMaName = _RcElpsFdMaName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 6),
    _RcElpsFdMaName_Type()
)
rcElpsFdMaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsFdMaName.setStatus("current")


class _RcElpsFdLocalMep_Type(Integer32):
    """Custom type rcElpsFdLocalMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RcElpsFdLocalMep_Type.__name__ = "Integer32"
_RcElpsFdLocalMep_Object = MibTableColumn
rcElpsFdLocalMep = _RcElpsFdLocalMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 7),
    _RcElpsFdLocalMep_Type()
)
rcElpsFdLocalMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsFdLocalMep.setStatus("current")


class _RcElpsFdRemoteMep_Type(Integer32):
    """Custom type rcElpsFdRemoteMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RcElpsFdRemoteMep_Type.__name__ = "Integer32"
_RcElpsFdRemoteMep_Object = MibTableColumn
rcElpsFdRemoteMep = _RcElpsFdRemoteMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 8),
    _RcElpsFdRemoteMep_Type()
)
rcElpsFdRemoteMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsFdRemoteMep.setStatus("current")


class _RcElpsMdLevel_Type(Integer32):
    """Custom type rcElpsMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcElpsMdLevel_Type.__name__ = "Integer32"
_RcElpsMdLevel_Object = MibTableColumn
rcElpsMdLevel = _RcElpsMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 2, 1, 1, 9),
    _RcElpsMdLevel_Type()
)
rcElpsMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcElpsMdLevel.setStatus("current")

# Managed Objects groups


# Notification objects

rcElpsDfopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 5, 1)
)
rcElpsDfopTrap.setObjects(
    ("RAISECOM-ELPS-MIB", "rcElpsStatisticsLastDfop")
)
if mibBuilder.loadTexts:
    rcElpsDfopTrap.setStatus(
        "current"
    )

rcElpsDfopClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 5, 2)
)
rcElpsDfopClearTrap.setObjects(
    ("RAISECOM-ELPS-MIB", "rcElpsStatisticsLastDfop")
)
if mibBuilder.loadTexts:
    rcElpsDfopClearTrap.setStatus(
        "current"
    )

rcElpsSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 54, 1, 5, 3)
)
rcElpsSwitchTrap.setObjects(
    ("RAISECOM-ELPS-MIB", "rcElpsStatus")
)
if mibBuilder.loadTexts:
    rcElpsSwitchTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-ELPS-MIB",
    **{"rcElps": rcElps,
       "rcElpsBaseGroup": rcElpsBaseGroup,
       "rcElpsTrapEnable": rcElpsTrapEnable,
       "rcElpsCfgTable": rcElpsCfgTable,
       "rcElpsCfgEntry": rcElpsCfgEntry,
       "rcElpsId": rcElpsId,
       "rcElpsName": rcElpsName,
       "rcElpsWorkingPort": rcElpsWorkingPort,
       "rcElpsWorkingBlockVlanlist": rcElpsWorkingBlockVlanlist,
       "rcElpsProtectionPort": rcElpsProtectionPort,
       "rcElpsProtectionBlockVlanlist": rcElpsProtectionBlockVlanlist,
       "rcElpsProtectionTypeAdmin": rcElpsProtectionTypeAdmin,
       "rcElpsProtectionTypeOper": rcElpsProtectionTypeOper,
       "rcElpsForceSwitch": rcElpsForceSwitch,
       "rcElpsManualSwitch": rcElpsManualSwitch,
       "rcElpsManualSwitchtoWork": rcElpsManualSwitchtoWork,
       "rcElpsLockout": rcElpsLockout,
       "rcElpsClear": rcElpsClear,
       "rcElpsWtrTimer": rcElpsWtrTimer,
       "rcElpsHoldOffTimer": rcElpsHoldOffTimer,
       "rcElpsProtocolVlan": rcElpsProtocolVlan,
       "rcElpsStatus": rcElpsStatus,
       "rcElpsDfopStatus": rcElpsDfopStatus,
       "rcElpsRowStatus": rcElpsRowStatus,
       "rcElpsStatisticsTable": rcElpsStatisticsTable,
       "rcElpsStatisticsEntry": rcElpsStatisticsEntry,
       "rcElpsStatisticsSwitchCounts": rcElpsStatisticsSwitchCounts,
       "rcElpsStatisticsApsTx": rcElpsStatisticsApsTx,
       "rcElpsStatisticsApsRx": rcElpsStatisticsApsRx,
       "rcElpsStatisticsLastStatusOccur": rcElpsStatisticsLastStatusOccur,
       "rcElpsStatisticsLastSwitchOccur": rcElpsStatisticsLastSwitchOccur,
       "rcElpsStatisticsLastDfop": rcElpsStatisticsLastDfop,
       "rcElpsStatisticsClear": rcElpsStatisticsClear,
       "rcElpsPeerTable": rcElpsPeerTable,
       "rcElpsPeerEntry": rcElpsPeerEntry,
       "rcElpsPeerProtectionType": rcElpsPeerProtectionType,
       "rcElpsPeerStatus": rcElpsPeerStatus,
       "rcElpsRequestSignal": rcElpsRequestSignal,
       "rcElpsBridgedSignal": rcElpsBridgedSignal,
       "rcElpsNotifications": rcElpsNotifications,
       "rcElpsDfopTrap": rcElpsDfopTrap,
       "rcElpsDfopClearTrap": rcElpsDfopClearTrap,
       "rcElpsSwitchTrap": rcElpsSwitchTrap,
       "rcElpsFailureDetGroup": rcElpsFailureDetGroup,
       "rcElpsFailureDetTable": rcElpsFailureDetTable,
       "rcElpsFailureDetEntry": rcElpsFailureDetEntry,
       "rcElpsFdLink": rcElpsFdLink,
       "rcElpsFdType": rcElpsFdType,
       "rcElpsFdLinkStatus": rcElpsFdLinkStatus,
       "rcElpsFdSfType": rcElpsFdSfType,
       "rcElpsFdMdName": rcElpsFdMdName,
       "rcElpsFdMaName": rcElpsFdMaName,
       "rcElpsFdLocalMep": rcElpsFdLocalMep,
       "rcElpsFdRemoteMep": rcElpsFdRemoteMep,
       "rcElpsMdLevel": rcElpsMdLevel}
)
