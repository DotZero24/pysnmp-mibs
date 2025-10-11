# SNMP MIB module (RAISECOM-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-APS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:07 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

raisecomAps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomApsBaseGroup_ObjectIdentity = ObjectIdentity
raisecomApsBaseGroup = _RaisecomApsBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1)
)


class _RaisecomApsTrapEnable_Type(EnableVar):
    """Custom type raisecomApsTrapEnable based on EnableVar"""
    defaultValue = 2


_RaisecomApsTrapEnable_Type.__name__ = "EnableVar"
_RaisecomApsTrapEnable_Object = MibScalar
raisecomApsTrapEnable = _RaisecomApsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 1),
    _RaisecomApsTrapEnable_Type()
)
raisecomApsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsTrapEnable.setStatus("current")
_RaisecomApsCfgTable_Object = MibTable
raisecomApsCfgTable = _RaisecomApsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomApsCfgTable.setStatus("current")
_RaisecomApsCfgEntry_Object = MibTableRow
raisecomApsCfgEntry = _RaisecomApsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1)
)
raisecomApsCfgEntry.setIndexNames(
    (0, "RAISECOM-APS-MIB", "raisecomApsId"),
)
if mibBuilder.loadTexts:
    raisecomApsCfgEntry.setStatus("current")


class _RaisecomApsId_Type(Unsigned32):
    """Custom type raisecomApsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RaisecomApsId_Type.__name__ = "Unsigned32"
_RaisecomApsId_Object = MibTableColumn
raisecomApsId = _RaisecomApsId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 1),
    _RaisecomApsId_Type()
)
raisecomApsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomApsId.setStatus("current")


class _RaisecomApsName_Type(OctetString):
    """Custom type raisecomApsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomApsName_Type.__name__ = "OctetString"
_RaisecomApsName_Object = MibTableColumn
raisecomApsName = _RaisecomApsName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 2),
    _RaisecomApsName_Type()
)
raisecomApsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsName.setStatus("current")


class _RaisecomApsType_Type(Integer32):
    """Custom type raisecomApsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ether-aps", 1),
          ("mpls-aps", 2))
    )


_RaisecomApsType_Type.__name__ = "Integer32"
_RaisecomApsType_Object = MibTableColumn
raisecomApsType = _RaisecomApsType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 3),
    _RaisecomApsType_Type()
)
raisecomApsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsType.setStatus("current")
_RaisecomApsWorkingPort_Type = Integer32
_RaisecomApsWorkingPort_Object = MibTableColumn
raisecomApsWorkingPort = _RaisecomApsWorkingPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 4),
    _RaisecomApsWorkingPort_Type()
)
raisecomApsWorkingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsWorkingPort.setStatus("current")
_RaisecomApsWorkingBlockVlanlist_Type = Vlanset
_RaisecomApsWorkingBlockVlanlist_Object = MibTableColumn
raisecomApsWorkingBlockVlanlist = _RaisecomApsWorkingBlockVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 5),
    _RaisecomApsWorkingBlockVlanlist_Type()
)
raisecomApsWorkingBlockVlanlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsWorkingBlockVlanlist.setStatus("current")
_RaisecomApsProtectionPort_Type = Integer32
_RaisecomApsProtectionPort_Object = MibTableColumn
raisecomApsProtectionPort = _RaisecomApsProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 6),
    _RaisecomApsProtectionPort_Type()
)
raisecomApsProtectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsProtectionPort.setStatus("current")
_RaisecomApsProtectionBlockVlanlist_Type = Vlanset
_RaisecomApsProtectionBlockVlanlist_Object = MibTableColumn
raisecomApsProtectionBlockVlanlist = _RaisecomApsProtectionBlockVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 7),
    _RaisecomApsProtectionBlockVlanlist_Type()
)
raisecomApsProtectionBlockVlanlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsProtectionBlockVlanlist.setStatus("current")


class _RaisecomApsWorkingIngressAssociation_Type(OctetString):
    """Custom type raisecomApsWorkingIngressAssociation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomApsWorkingIngressAssociation_Type.__name__ = "OctetString"
_RaisecomApsWorkingIngressAssociation_Object = MibTableColumn
raisecomApsWorkingIngressAssociation = _RaisecomApsWorkingIngressAssociation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 8),
    _RaisecomApsWorkingIngressAssociation_Type()
)
raisecomApsWorkingIngressAssociation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsWorkingIngressAssociation.setStatus("current")


class _RaisecomApsWorkingEgressAssociation_Type(OctetString):
    """Custom type raisecomApsWorkingEgressAssociation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomApsWorkingEgressAssociation_Type.__name__ = "OctetString"
_RaisecomApsWorkingEgressAssociation_Object = MibTableColumn
raisecomApsWorkingEgressAssociation = _RaisecomApsWorkingEgressAssociation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 9),
    _RaisecomApsWorkingEgressAssociation_Type()
)
raisecomApsWorkingEgressAssociation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsWorkingEgressAssociation.setStatus("current")


class _RaisecomApsProtectionIngressAssociation_Type(OctetString):
    """Custom type raisecomApsProtectionIngressAssociation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomApsProtectionIngressAssociation_Type.__name__ = "OctetString"
_RaisecomApsProtectionIngressAssociation_Object = MibTableColumn
raisecomApsProtectionIngressAssociation = _RaisecomApsProtectionIngressAssociation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 10),
    _RaisecomApsProtectionIngressAssociation_Type()
)
raisecomApsProtectionIngressAssociation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsProtectionIngressAssociation.setStatus("current")


class _RaisecomApsProtectionEgressAssociation_Type(OctetString):
    """Custom type raisecomApsProtectionEgressAssociation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomApsProtectionEgressAssociation_Type.__name__ = "OctetString"
_RaisecomApsProtectionEgressAssociation_Object = MibTableColumn
raisecomApsProtectionEgressAssociation = _RaisecomApsProtectionEgressAssociation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 11),
    _RaisecomApsProtectionEgressAssociation_Type()
)
raisecomApsProtectionEgressAssociation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsProtectionEgressAssociation.setStatus("current")


class _RaisecomApsProtectionTypeAdmin_Type(Unsigned32):
    """Custom type raisecomApsProtectionTypeAdmin based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RaisecomApsProtectionTypeAdmin_Type.__name__ = "Unsigned32"
_RaisecomApsProtectionTypeAdmin_Object = MibTableColumn
raisecomApsProtectionTypeAdmin = _RaisecomApsProtectionTypeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 12),
    _RaisecomApsProtectionTypeAdmin_Type()
)
raisecomApsProtectionTypeAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsProtectionTypeAdmin.setStatus("current")


class _RaisecomApsProtectionTypeOper_Type(Unsigned32):
    """Custom type raisecomApsProtectionTypeOper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RaisecomApsProtectionTypeOper_Type.__name__ = "Unsigned32"
_RaisecomApsProtectionTypeOper_Object = MibTableColumn
raisecomApsProtectionTypeOper = _RaisecomApsProtectionTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 13),
    _RaisecomApsProtectionTypeOper_Type()
)
raisecomApsProtectionTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsProtectionTypeOper.setStatus("current")


class _RaisecomApsForceSwitch_Type(TruthValue):
    """Custom type raisecomApsForceSwitch based on TruthValue"""
    defaultValue = 2


_RaisecomApsForceSwitch_Type.__name__ = "TruthValue"
_RaisecomApsForceSwitch_Object = MibTableColumn
raisecomApsForceSwitch = _RaisecomApsForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 14),
    _RaisecomApsForceSwitch_Type()
)
raisecomApsForceSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsForceSwitch.setStatus("current")


class _RaisecomApsManualSwitch_Type(TruthValue):
    """Custom type raisecomApsManualSwitch based on TruthValue"""
    defaultValue = 2


_RaisecomApsManualSwitch_Type.__name__ = "TruthValue"
_RaisecomApsManualSwitch_Object = MibTableColumn
raisecomApsManualSwitch = _RaisecomApsManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 15),
    _RaisecomApsManualSwitch_Type()
)
raisecomApsManualSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsManualSwitch.setStatus("current")


class _RaisecomApsManualSwitchtoWork_Type(TruthValue):
    """Custom type raisecomApsManualSwitchtoWork based on TruthValue"""
    defaultValue = 2


_RaisecomApsManualSwitchtoWork_Type.__name__ = "TruthValue"
_RaisecomApsManualSwitchtoWork_Object = MibTableColumn
raisecomApsManualSwitchtoWork = _RaisecomApsManualSwitchtoWork_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 16),
    _RaisecomApsManualSwitchtoWork_Type()
)
raisecomApsManualSwitchtoWork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsManualSwitchtoWork.setStatus("current")


class _RaisecomApsLockout_Type(TruthValue):
    """Custom type raisecomApsLockout based on TruthValue"""
    defaultValue = 2


_RaisecomApsLockout_Type.__name__ = "TruthValue"
_RaisecomApsLockout_Object = MibTableColumn
raisecomApsLockout = _RaisecomApsLockout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 17),
    _RaisecomApsLockout_Type()
)
raisecomApsLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsLockout.setStatus("current")


class _RaisecomApsClear_Type(EnableVar):
    """Custom type raisecomApsClear based on EnableVar"""
    defaultValue = 2


_RaisecomApsClear_Type.__name__ = "EnableVar"
_RaisecomApsClear_Object = MibTableColumn
raisecomApsClear = _RaisecomApsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 18),
    _RaisecomApsClear_Type()
)
raisecomApsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsClear.setStatus("current")


class _RaisecomApsWtrTimer_Type(Unsigned32):
    """Custom type raisecomApsWtrTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RaisecomApsWtrTimer_Type.__name__ = "Unsigned32"
_RaisecomApsWtrTimer_Object = MibTableColumn
raisecomApsWtrTimer = _RaisecomApsWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 19),
    _RaisecomApsWtrTimer_Type()
)
raisecomApsWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsWtrTimer.setStatus("current")


class _RaisecomApsHoldOffTimer_Type(Unsigned32):
    """Custom type raisecomApsHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomApsHoldOffTimer_Type.__name__ = "Unsigned32"
_RaisecomApsHoldOffTimer_Object = MibTableColumn
raisecomApsHoldOffTimer = _RaisecomApsHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 20),
    _RaisecomApsHoldOffTimer_Type()
)
raisecomApsHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsHoldOffTimer.setStatus("current")


class _RaisecomApsProtocolVlan_Type(Integer32):
    """Custom type raisecomApsProtocolVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomApsProtocolVlan_Type.__name__ = "Integer32"
_RaisecomApsProtocolVlan_Object = MibTableColumn
raisecomApsProtocolVlan = _RaisecomApsProtocolVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 21),
    _RaisecomApsProtocolVlan_Type()
)
raisecomApsProtocolVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsProtocolVlan.setStatus("current")


class _RaisecomApsStatus_Type(Integer32):
    """Custom type raisecomApsStatus based on Integer32"""
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


_RaisecomApsStatus_Type.__name__ = "Integer32"
_RaisecomApsStatus_Object = MibTableColumn
raisecomApsStatus = _RaisecomApsStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 22),
    _RaisecomApsStatus_Type()
)
raisecomApsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatus.setStatus("current")


class _RaisecomApsDfopStatus_Type(Integer32):
    """Custom type raisecomApsDfopStatus based on Integer32"""
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


_RaisecomApsDfopStatus_Type.__name__ = "Integer32"
_RaisecomApsDfopStatus_Object = MibTableColumn
raisecomApsDfopStatus = _RaisecomApsDfopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 23),
    _RaisecomApsDfopStatus_Type()
)
raisecomApsDfopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsDfopStatus.setStatus("current")
_RaisecomApsRowStatus_Type = RowStatus
_RaisecomApsRowStatus_Object = MibTableColumn
raisecomApsRowStatus = _RaisecomApsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 2, 1, 24),
    _RaisecomApsRowStatus_Type()
)
raisecomApsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsRowStatus.setStatus("current")
_RaisecomApsStatisticsTable_Object = MibTable
raisecomApsStatisticsTable = _RaisecomApsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomApsStatisticsTable.setStatus("current")
_RaisecomApsStatisticsEntry_Object = MibTableRow
raisecomApsStatisticsEntry = _RaisecomApsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1)
)
raisecomApsStatisticsEntry.setIndexNames(
    (0, "RAISECOM-APS-MIB", "raisecomApsId"),
)
if mibBuilder.loadTexts:
    raisecomApsStatisticsEntry.setStatus("current")


class _RaisecomApsStatisticsSwitchCounts_Type(Unsigned32):
    """Custom type raisecomApsStatisticsSwitchCounts based on Unsigned32"""
    defaultValue = 0


_RaisecomApsStatisticsSwitchCounts_Type.__name__ = "Unsigned32"
_RaisecomApsStatisticsSwitchCounts_Object = MibTableColumn
raisecomApsStatisticsSwitchCounts = _RaisecomApsStatisticsSwitchCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 1),
    _RaisecomApsStatisticsSwitchCounts_Type()
)
raisecomApsStatisticsSwitchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatisticsSwitchCounts.setStatus("current")


class _RaisecomApsStatisticsApsTx_Type(Unsigned32):
    """Custom type raisecomApsStatisticsApsTx based on Unsigned32"""
    defaultValue = 0


_RaisecomApsStatisticsApsTx_Type.__name__ = "Unsigned32"
_RaisecomApsStatisticsApsTx_Object = MibTableColumn
raisecomApsStatisticsApsTx = _RaisecomApsStatisticsApsTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 2),
    _RaisecomApsStatisticsApsTx_Type()
)
raisecomApsStatisticsApsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatisticsApsTx.setStatus("current")


class _RaisecomApsStatisticsApsRx_Type(Unsigned32):
    """Custom type raisecomApsStatisticsApsRx based on Unsigned32"""
    defaultValue = 0


_RaisecomApsStatisticsApsRx_Type.__name__ = "Unsigned32"
_RaisecomApsStatisticsApsRx_Object = MibTableColumn
raisecomApsStatisticsApsRx = _RaisecomApsStatisticsApsRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 3),
    _RaisecomApsStatisticsApsRx_Type()
)
raisecomApsStatisticsApsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatisticsApsRx.setStatus("current")
_RaisecomApsStatisticsLastStatusOccur_Type = TimeTicks
_RaisecomApsStatisticsLastStatusOccur_Object = MibTableColumn
raisecomApsStatisticsLastStatusOccur = _RaisecomApsStatisticsLastStatusOccur_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 4),
    _RaisecomApsStatisticsLastStatusOccur_Type()
)
raisecomApsStatisticsLastStatusOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatisticsLastStatusOccur.setStatus("current")
_RaisecomApsStatisticsLastSwitchOccur_Type = TimeTicks
_RaisecomApsStatisticsLastSwitchOccur_Object = MibTableColumn
raisecomApsStatisticsLastSwitchOccur = _RaisecomApsStatisticsLastSwitchOccur_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 5),
    _RaisecomApsStatisticsLastSwitchOccur_Type()
)
raisecomApsStatisticsLastSwitchOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatisticsLastSwitchOccur.setStatus("current")
_RaisecomApsStatisticsLastDfop_Type = TimeTicks
_RaisecomApsStatisticsLastDfop_Object = MibTableColumn
raisecomApsStatisticsLastDfop = _RaisecomApsStatisticsLastDfop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 6),
    _RaisecomApsStatisticsLastDfop_Type()
)
raisecomApsStatisticsLastDfop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsStatisticsLastDfop.setStatus("current")


class _RaisecomApsStatisticsClear_Type(EnableVar):
    """Custom type raisecomApsStatisticsClear based on EnableVar"""
    defaultValue = 2


_RaisecomApsStatisticsClear_Type.__name__ = "EnableVar"
_RaisecomApsStatisticsClear_Object = MibTableColumn
raisecomApsStatisticsClear = _RaisecomApsStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 3, 1, 7),
    _RaisecomApsStatisticsClear_Type()
)
raisecomApsStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsStatisticsClear.setStatus("current")
_RaisecomApsPeerTable_Object = MibTable
raisecomApsPeerTable = _RaisecomApsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomApsPeerTable.setStatus("current")
_RaisecomApsPeerEntry_Object = MibTableRow
raisecomApsPeerEntry = _RaisecomApsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 4, 1)
)
raisecomApsPeerEntry.setIndexNames(
    (0, "RAISECOM-APS-MIB", "raisecomApsId"),
)
if mibBuilder.loadTexts:
    raisecomApsPeerEntry.setStatus("current")


class _RaisecomApsPeerProtectionType_Type(Unsigned32):
    """Custom type raisecomApsPeerProtectionType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RaisecomApsPeerProtectionType_Type.__name__ = "Unsigned32"
_RaisecomApsPeerProtectionType_Object = MibTableColumn
raisecomApsPeerProtectionType = _RaisecomApsPeerProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 4, 1, 1),
    _RaisecomApsPeerProtectionType_Type()
)
raisecomApsPeerProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsPeerProtectionType.setStatus("current")


class _RaisecomApsPeerStatus_Type(Integer32):
    """Custom type raisecomApsPeerStatus based on Integer32"""
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


_RaisecomApsPeerStatus_Type.__name__ = "Integer32"
_RaisecomApsPeerStatus_Object = MibTableColumn
raisecomApsPeerStatus = _RaisecomApsPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 4, 1, 2),
    _RaisecomApsPeerStatus_Type()
)
raisecomApsPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsPeerStatus.setStatus("current")


class _RaisecomApsRequestSignal_Type(Integer32):
    """Custom type raisecomApsRequestSignal based on Integer32"""
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


_RaisecomApsRequestSignal_Type.__name__ = "Integer32"
_RaisecomApsRequestSignal_Object = MibTableColumn
raisecomApsRequestSignal = _RaisecomApsRequestSignal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 4, 1, 3),
    _RaisecomApsRequestSignal_Type()
)
raisecomApsRequestSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsRequestSignal.setStatus("current")


class _RaisecomApsBridgedSignal_Type(Integer32):
    """Custom type raisecomApsBridgedSignal based on Integer32"""
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


_RaisecomApsBridgedSignal_Type.__name__ = "Integer32"
_RaisecomApsBridgedSignal_Object = MibTableColumn
raisecomApsBridgedSignal = _RaisecomApsBridgedSignal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 1, 4, 1, 4),
    _RaisecomApsBridgedSignal_Type()
)
raisecomApsBridgedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsBridgedSignal.setStatus("current")
_RaisecomApsAssociationGroup_ObjectIdentity = ObjectIdentity
raisecomApsAssociationGroup = _RaisecomApsAssociationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2)
)
_RaisecomApsAssociationTable_Object = MibTable
raisecomApsAssociationTable = _RaisecomApsAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomApsAssociationTable.setStatus("current")
_RaisecomApsAssociationEntry_Object = MibTableRow
raisecomApsAssociationEntry = _RaisecomApsAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1, 1)
)
raisecomApsAssociationEntry.setIndexNames(
    (0, "RAISECOM-APS-MIB", "raisecomApsAssociationName"),
)
if mibBuilder.loadTexts:
    raisecomApsAssociationEntry.setStatus("current")


class _RaisecomApsAssociationName_Type(OctetString):
    """Custom type raisecomApsAssociationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomApsAssociationName_Type.__name__ = "OctetString"
_RaisecomApsAssociationName_Object = MibTableColumn
raisecomApsAssociationName = _RaisecomApsAssociationName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1, 1, 1),
    _RaisecomApsAssociationName_Type()
)
raisecomApsAssociationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomApsAssociationName.setStatus("current")


class _RaisecomApsAssociationMdName_Type(OctetString):
    """Custom type raisecomApsAssociationMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RaisecomApsAssociationMdName_Type.__name__ = "OctetString"
_RaisecomApsAssociationMdName_Object = MibTableColumn
raisecomApsAssociationMdName = _RaisecomApsAssociationMdName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1, 1, 2),
    _RaisecomApsAssociationMdName_Type()
)
raisecomApsAssociationMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsAssociationMdName.setStatus("current")
_RaisecomApsAssociationMdLevel_Type = Integer32
_RaisecomApsAssociationMdLevel_Object = MibTableColumn
raisecomApsAssociationMdLevel = _RaisecomApsAssociationMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1, 1, 3),
    _RaisecomApsAssociationMdLevel_Type()
)
raisecomApsAssociationMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsAssociationMdLevel.setStatus("current")


class _RaisecomApsAssociationMaName_Type(OctetString):
    """Custom type raisecomApsAssociationMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_RaisecomApsAssociationMaName_Type.__name__ = "OctetString"
_RaisecomApsAssociationMaName_Object = MibTableColumn
raisecomApsAssociationMaName = _RaisecomApsAssociationMaName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1, 1, 4),
    _RaisecomApsAssociationMaName_Type()
)
raisecomApsAssociationMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsAssociationMaName.setStatus("current")
_RaisecomApsAssociationRowStatus_Type = RowStatus
_RaisecomApsAssociationRowStatus_Object = MibTableColumn
raisecomApsAssociationRowStatus = _RaisecomApsAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 2, 1, 1, 5),
    _RaisecomApsAssociationRowStatus_Type()
)
raisecomApsAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomApsAssociationRowStatus.setStatus("current")
_RaisecomApsFailureDetGroup_ObjectIdentity = ObjectIdentity
raisecomApsFailureDetGroup = _RaisecomApsFailureDetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3)
)
_RaisecomApsFailureDetTable_Object = MibTable
raisecomApsFailureDetTable = _RaisecomApsFailureDetTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1)
)
if mibBuilder.loadTexts:
    raisecomApsFailureDetTable.setStatus("current")
_RaisecomApsFailureDetEntry_Object = MibTableRow
raisecomApsFailureDetEntry = _RaisecomApsFailureDetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1)
)
raisecomApsFailureDetEntry.setIndexNames(
    (0, "RAISECOM-APS-MIB", "raisecomApsId"),
    (0, "RAISECOM-APS-MIB", "raisecomApsFdLink"),
)
if mibBuilder.loadTexts:
    raisecomApsFailureDetEntry.setStatus("current")


class _RaisecomApsFdLink_Type(Integer32):
    """Custom type raisecomApsFdLink based on Integer32"""
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


_RaisecomApsFdLink_Type.__name__ = "Integer32"
_RaisecomApsFdLink_Object = MibTableColumn
raisecomApsFdLink = _RaisecomApsFdLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 1),
    _RaisecomApsFdLink_Type()
)
raisecomApsFdLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomApsFdLink.setStatus("current")


class _RaisecomApsFdType_Type(Integer32):
    """Custom type raisecomApsFdType based on Integer32"""
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


_RaisecomApsFdType_Type.__name__ = "Integer32"
_RaisecomApsFdType_Object = MibTableColumn
raisecomApsFdType = _RaisecomApsFdType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 2),
    _RaisecomApsFdType_Type()
)
raisecomApsFdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsFdType.setStatus("current")


class _RaisecomApsFdLinkStatus_Type(Integer32):
    """Custom type raisecomApsFdLinkStatus based on Integer32"""
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


_RaisecomApsFdLinkStatus_Type.__name__ = "Integer32"
_RaisecomApsFdLinkStatus_Object = MibTableColumn
raisecomApsFdLinkStatus = _RaisecomApsFdLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 3),
    _RaisecomApsFdLinkStatus_Type()
)
raisecomApsFdLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsFdLinkStatus.setStatus("current")


class _RaisecomApsFdSfType_Type(Integer32):
    """Custom type raisecomApsFdSfType based on Integer32"""
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


_RaisecomApsFdSfType_Type.__name__ = "Integer32"
_RaisecomApsFdSfType_Object = MibTableColumn
raisecomApsFdSfType = _RaisecomApsFdSfType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 4),
    _RaisecomApsFdSfType_Type()
)
raisecomApsFdSfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomApsFdSfType.setStatus("current")


class _RaisecomApsFdMdName_Type(OctetString):
    """Custom type raisecomApsFdMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RaisecomApsFdMdName_Type.__name__ = "OctetString"
_RaisecomApsFdMdName_Object = MibTableColumn
raisecomApsFdMdName = _RaisecomApsFdMdName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 5),
    _RaisecomApsFdMdName_Type()
)
raisecomApsFdMdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsFdMdName.setStatus("current")


class _RaisecomApsFdMaName_Type(OctetString):
    """Custom type raisecomApsFdMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_RaisecomApsFdMaName_Type.__name__ = "OctetString"
_RaisecomApsFdMaName_Object = MibTableColumn
raisecomApsFdMaName = _RaisecomApsFdMaName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 6),
    _RaisecomApsFdMaName_Type()
)
raisecomApsFdMaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsFdMaName.setStatus("current")


class _RaisecomApsFdLocalMep_Type(Integer32):
    """Custom type raisecomApsFdLocalMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RaisecomApsFdLocalMep_Type.__name__ = "Integer32"
_RaisecomApsFdLocalMep_Object = MibTableColumn
raisecomApsFdLocalMep = _RaisecomApsFdLocalMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 7),
    _RaisecomApsFdLocalMep_Type()
)
raisecomApsFdLocalMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsFdLocalMep.setStatus("current")


class _RaisecomApsFdRemoteMep_Type(Integer32):
    """Custom type raisecomApsFdRemoteMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RaisecomApsFdRemoteMep_Type.__name__ = "Integer32"
_RaisecomApsFdRemoteMep_Object = MibTableColumn
raisecomApsFdRemoteMep = _RaisecomApsFdRemoteMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 8),
    _RaisecomApsFdRemoteMep_Type()
)
raisecomApsFdRemoteMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsFdRemoteMep.setStatus("current")


class _RaisecomApsMdLevel_Type(Integer32):
    """Custom type raisecomApsMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomApsMdLevel_Type.__name__ = "Integer32"
_RaisecomApsMdLevel_Object = MibTableColumn
raisecomApsMdLevel = _RaisecomApsMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 3, 1, 1, 9),
    _RaisecomApsMdLevel_Type()
)
raisecomApsMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomApsMdLevel.setStatus("current")
_RaisecomApsNotifications_ObjectIdentity = ObjectIdentity
raisecomApsNotifications = _RaisecomApsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 4)
)

# Managed Objects groups


# Notification objects

raisecomApsDfopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 4, 1)
)
raisecomApsDfopTrap.setObjects(
    ("RAISECOM-APS-MIB", "raisecomApsStatisticsLastDfop")
)
if mibBuilder.loadTexts:
    raisecomApsDfopTrap.setStatus(
        "current"
    )

raisecomApsDfopClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 4, 2)
)
raisecomApsDfopClearTrap.setObjects(
    ("RAISECOM-APS-MIB", "raisecomApsStatisticsLastDfop")
)
if mibBuilder.loadTexts:
    raisecomApsDfopClearTrap.setStatus(
        "current"
    )

raisecomApsSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 37, 4, 3)
)
raisecomApsSwitchTrap.setObjects(
    ("RAISECOM-APS-MIB", "raisecomApsStatus")
)
if mibBuilder.loadTexts:
    raisecomApsSwitchTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-APS-MIB",
    **{"raisecomAps": raisecomAps,
       "raisecomApsBaseGroup": raisecomApsBaseGroup,
       "raisecomApsTrapEnable": raisecomApsTrapEnable,
       "raisecomApsCfgTable": raisecomApsCfgTable,
       "raisecomApsCfgEntry": raisecomApsCfgEntry,
       "raisecomApsId": raisecomApsId,
       "raisecomApsName": raisecomApsName,
       "raisecomApsType": raisecomApsType,
       "raisecomApsWorkingPort": raisecomApsWorkingPort,
       "raisecomApsWorkingBlockVlanlist": raisecomApsWorkingBlockVlanlist,
       "raisecomApsProtectionPort": raisecomApsProtectionPort,
       "raisecomApsProtectionBlockVlanlist": raisecomApsProtectionBlockVlanlist,
       "raisecomApsWorkingIngressAssociation": raisecomApsWorkingIngressAssociation,
       "raisecomApsWorkingEgressAssociation": raisecomApsWorkingEgressAssociation,
       "raisecomApsProtectionIngressAssociation": raisecomApsProtectionIngressAssociation,
       "raisecomApsProtectionEgressAssociation": raisecomApsProtectionEgressAssociation,
       "raisecomApsProtectionTypeAdmin": raisecomApsProtectionTypeAdmin,
       "raisecomApsProtectionTypeOper": raisecomApsProtectionTypeOper,
       "raisecomApsForceSwitch": raisecomApsForceSwitch,
       "raisecomApsManualSwitch": raisecomApsManualSwitch,
       "raisecomApsManualSwitchtoWork": raisecomApsManualSwitchtoWork,
       "raisecomApsLockout": raisecomApsLockout,
       "raisecomApsClear": raisecomApsClear,
       "raisecomApsWtrTimer": raisecomApsWtrTimer,
       "raisecomApsHoldOffTimer": raisecomApsHoldOffTimer,
       "raisecomApsProtocolVlan": raisecomApsProtocolVlan,
       "raisecomApsStatus": raisecomApsStatus,
       "raisecomApsDfopStatus": raisecomApsDfopStatus,
       "raisecomApsRowStatus": raisecomApsRowStatus,
       "raisecomApsStatisticsTable": raisecomApsStatisticsTable,
       "raisecomApsStatisticsEntry": raisecomApsStatisticsEntry,
       "raisecomApsStatisticsSwitchCounts": raisecomApsStatisticsSwitchCounts,
       "raisecomApsStatisticsApsTx": raisecomApsStatisticsApsTx,
       "raisecomApsStatisticsApsRx": raisecomApsStatisticsApsRx,
       "raisecomApsStatisticsLastStatusOccur": raisecomApsStatisticsLastStatusOccur,
       "raisecomApsStatisticsLastSwitchOccur": raisecomApsStatisticsLastSwitchOccur,
       "raisecomApsStatisticsLastDfop": raisecomApsStatisticsLastDfop,
       "raisecomApsStatisticsClear": raisecomApsStatisticsClear,
       "raisecomApsPeerTable": raisecomApsPeerTable,
       "raisecomApsPeerEntry": raisecomApsPeerEntry,
       "raisecomApsPeerProtectionType": raisecomApsPeerProtectionType,
       "raisecomApsPeerStatus": raisecomApsPeerStatus,
       "raisecomApsRequestSignal": raisecomApsRequestSignal,
       "raisecomApsBridgedSignal": raisecomApsBridgedSignal,
       "raisecomApsAssociationGroup": raisecomApsAssociationGroup,
       "raisecomApsAssociationTable": raisecomApsAssociationTable,
       "raisecomApsAssociationEntry": raisecomApsAssociationEntry,
       "raisecomApsAssociationName": raisecomApsAssociationName,
       "raisecomApsAssociationMdName": raisecomApsAssociationMdName,
       "raisecomApsAssociationMdLevel": raisecomApsAssociationMdLevel,
       "raisecomApsAssociationMaName": raisecomApsAssociationMaName,
       "raisecomApsAssociationRowStatus": raisecomApsAssociationRowStatus,
       "raisecomApsFailureDetGroup": raisecomApsFailureDetGroup,
       "raisecomApsFailureDetTable": raisecomApsFailureDetTable,
       "raisecomApsFailureDetEntry": raisecomApsFailureDetEntry,
       "raisecomApsFdLink": raisecomApsFdLink,
       "raisecomApsFdType": raisecomApsFdType,
       "raisecomApsFdLinkStatus": raisecomApsFdLinkStatus,
       "raisecomApsFdSfType": raisecomApsFdSfType,
       "raisecomApsFdMdName": raisecomApsFdMdName,
       "raisecomApsFdMaName": raisecomApsFdMaName,
       "raisecomApsFdLocalMep": raisecomApsFdLocalMep,
       "raisecomApsFdRemoteMep": raisecomApsFdRemoteMep,
       "raisecomApsMdLevel": raisecomApsMdLevel,
       "raisecomApsNotifications": raisecomApsNotifications,
       "raisecomApsDfopTrap": raisecomApsDfopTrap,
       "raisecomApsDfopClearTrap": raisecomApsDfopClearTrap,
       "raisecomApsSwitchTrap": raisecomApsSwitchTrap}
)
