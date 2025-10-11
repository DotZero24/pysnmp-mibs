# SNMP MIB module (AT-ALMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied/AT-ALMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:39 2025
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

(DisplayStringUnsized,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized")

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "sysinfo")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atAlmMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26)
)
if mibBuilder.loadTexts:
    atAlmMon.setRevisions(
        ("2019-02-12 00:00",
         "2018-09-20 00:00",
         "2017-02-08 00:00",
         "2014-05-12 00:15",
         "2013-12-13 11:46")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtAlmMonAlarmType(TextualConvention, Integer32):
    status = "current"
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
        *(("externalPSU", 1),
          ("epsr", 2),
          ("contactInput", 3),
          ("portLinkDown", 4),
          ("loopDetect", 5),
          ("mainPse", 6),
          ("portPoeFailure", 7),
          ("temperature", 8),
          ("g8032", 9),
          ("ufo", 10))
    )



class AtAlmMonActionUseOutput(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("used", 2))
    )



class AtAlmMonAbnormalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )



class AtAlmMonActionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )



class AtAlmMonContactPosition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AtAlmMonActionTable_Object = MibTable
atAlmMonActionTable = _AtAlmMonActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1)
)
if mibBuilder.loadTexts:
    atAlmMonActionTable.setStatus("current")
_AtAlmMonActionEntry_Object = MibTableRow
atAlmMonActionEntry = _AtAlmMonActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1)
)
atAlmMonActionEntry.setIndexNames(
    (0, "AT-ALMMON-MIB", "atAlmMonActionStackMemberId"),
    (0, "AT-ALMMON-MIB", "atAlmMonActionIndex"),
)
if mibBuilder.loadTexts:
    atAlmMonActionEntry.setStatus("current")
_AtAlmMonActionStackMemberId_Type = Unsigned32
_AtAlmMonActionStackMemberId_Object = MibTableColumn
atAlmMonActionStackMemberId = _AtAlmMonActionStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 1),
    _AtAlmMonActionStackMemberId_Type()
)
atAlmMonActionStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionStackMemberId.setStatus("current")
_AtAlmMonActionIndex_Type = Unsigned32
_AtAlmMonActionIndex_Object = MibTableColumn
atAlmMonActionIndex = _AtAlmMonActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 2),
    _AtAlmMonActionIndex_Type()
)
atAlmMonActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionIndex.setStatus("current")
_AtAlmMonAlarmType_Type = AtAlmMonAlarmType
_AtAlmMonAlarmType_Object = MibTableColumn
atAlmMonAlarmType = _AtAlmMonAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 3),
    _AtAlmMonAlarmType_Type()
)
atAlmMonAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAlarmType.setStatus("current")
_AtAlmMonAlarmTypeSelection_Type = Unsigned32
_AtAlmMonAlarmTypeSelection_Object = MibTableColumn
atAlmMonAlarmTypeSelection = _AtAlmMonAlarmTypeSelection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 4),
    _AtAlmMonAlarmTypeSelection_Type()
)
atAlmMonAlarmTypeSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAlarmTypeSelection.setStatus("current")


class _AtAlmMonActionDescription_Type(DisplayStringUnsized):
    """Custom type atAlmMonActionDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtAlmMonActionDescription_Type.__name__ = "DisplayStringUnsized"
_AtAlmMonActionDescription_Object = MibTableColumn
atAlmMonActionDescription = _AtAlmMonActionDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 5),
    _AtAlmMonActionDescription_Type()
)
atAlmMonActionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionDescription.setStatus("current")
_AtAlmMonActionUseRelay1_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay1_Object = MibTableColumn
atAlmMonActionUseRelay1 = _AtAlmMonActionUseRelay1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 6),
    _AtAlmMonActionUseRelay1_Type()
)
atAlmMonActionUseRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseRelay1.setStatus("current")
_AtAlmMonActionUseRelay2_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay2_Object = MibTableColumn
atAlmMonActionUseRelay2 = _AtAlmMonActionUseRelay2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 7),
    _AtAlmMonActionUseRelay2_Type()
)
atAlmMonActionUseRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseRelay2.setStatus("current")
_AtAlmMonActionUseRelay3_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay3_Object = MibTableColumn
atAlmMonActionUseRelay3 = _AtAlmMonActionUseRelay3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 8),
    _AtAlmMonActionUseRelay3_Type()
)
atAlmMonActionUseRelay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseRelay3.setStatus("current")
_AtAlmMonActionUseFaultLed_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseFaultLed_Object = MibTableColumn
atAlmMonActionUseFaultLed = _AtAlmMonActionUseFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 9),
    _AtAlmMonActionUseFaultLed_Type()
)
atAlmMonActionUseFaultLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseFaultLed.setStatus("current")
_AtAlmMonAbnormalState_Type = AtAlmMonAbnormalState
_AtAlmMonAbnormalState_Object = MibTableColumn
atAlmMonAbnormalState = _AtAlmMonAbnormalState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 10),
    _AtAlmMonAbnormalState_Type()
)
atAlmMonAbnormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonAbnormalState.setStatus("current")
_AtAlmMonActionState_Type = AtAlmMonActionState
_AtAlmMonActionState_Object = MibTableColumn
atAlmMonActionState = _AtAlmMonActionState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 11),
    _AtAlmMonActionState_Type()
)
atAlmMonActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionState.setStatus("current")
_AtAlmMonPerStackConfiguration_Type = TruthValue
_AtAlmMonPerStackConfiguration_Object = MibScalar
atAlmMonPerStackConfiguration = _AtAlmMonPerStackConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 2),
    _AtAlmMonPerStackConfiguration_Type()
)
atAlmMonPerStackConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonPerStackConfiguration.setStatus("current")
_AtAlmMonAvailableTable_Object = MibTable
atAlmMonAvailableTable = _AtAlmMonAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3)
)
if mibBuilder.loadTexts:
    atAlmMonAvailableTable.setStatus("current")
_AtAlmMonAvailableEntry_Object = MibTableRow
atAlmMonAvailableEntry = _AtAlmMonAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1)
)
atAlmMonAvailableEntry.setIndexNames(
    (0, "AT-ALMMON-MIB", "atAlmMonAvailableAlarmId"),
)
if mibBuilder.loadTexts:
    atAlmMonAvailableEntry.setStatus("current")
_AtAlmMonAvailableAlarmId_Type = Unsigned32
_AtAlmMonAvailableAlarmId_Object = MibTableColumn
atAlmMonAvailableAlarmId = _AtAlmMonAvailableAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1, 1),
    _AtAlmMonAvailableAlarmId_Type()
)
atAlmMonAvailableAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAvailableAlarmId.setStatus("current")
_AtAlmMonAvailableType_Type = AtAlmMonAlarmType
_AtAlmMonAvailableType_Object = MibTableColumn
atAlmMonAvailableType = _AtAlmMonAvailableType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1, 2),
    _AtAlmMonAvailableType_Type()
)
atAlmMonAvailableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAvailableType.setStatus("current")
_AtAlmMonAvailableTypeIndex_Type = Unsigned32
_AtAlmMonAvailableTypeIndex_Object = MibTableColumn
atAlmMonAvailableTypeIndex = _AtAlmMonAvailableTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1, 3),
    _AtAlmMonAvailableTypeIndex_Type()
)
atAlmMonAvailableTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAvailableTypeIndex.setStatus("current")
_AtAlmMonAvailableStkId_Type = Unsigned32
_AtAlmMonAvailableStkId_Object = MibTableColumn
atAlmMonAvailableStkId = _AtAlmMonAvailableStkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1, 4),
    _AtAlmMonAvailableStkId_Type()
)
atAlmMonAvailableStkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAvailableStkId.setStatus("current")


class _AtAlmMonAvailableIfName_Type(DisplayStringUnsized):
    """Custom type atAlmMonAvailableIfName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtAlmMonAvailableIfName_Type.__name__ = "DisplayStringUnsized"
_AtAlmMonAvailableIfName_Object = MibTableColumn
atAlmMonAvailableIfName = _AtAlmMonAvailableIfName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1, 5),
    _AtAlmMonAvailableIfName_Type()
)
atAlmMonAvailableIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAvailableIfName.setStatus("current")
_AtAlmMonAvailableState_Type = AtAlmMonActionState
_AtAlmMonAvailableState_Object = MibTableColumn
atAlmMonAvailableState = _AtAlmMonAvailableState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 3, 1, 6),
    _AtAlmMonAvailableState_Type()
)
atAlmMonAvailableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAvailableState.setStatus("current")
_AtAlmMonOutputRelayTable_Object = MibTable
atAlmMonOutputRelayTable = _AtAlmMonOutputRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 4)
)
if mibBuilder.loadTexts:
    atAlmMonOutputRelayTable.setStatus("current")
_AtAlmMonOutputRelayEntry_Object = MibTableRow
atAlmMonOutputRelayEntry = _AtAlmMonOutputRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 4, 1)
)
atAlmMonOutputRelayEntry.setIndexNames(
    (0, "AT-ALMMON-MIB", "atAlmMonOutputRelayStkId"),
    (0, "AT-ALMMON-MIB", "atAlmMonOutputRelayNumber"),
    (0, "AT-ALMMON-MIB", "atAlmMonOutputRelayAlarmId"),
)
if mibBuilder.loadTexts:
    atAlmMonOutputRelayEntry.setStatus("current")
_AtAlmMonOutputRelayStkId_Type = Unsigned32
_AtAlmMonOutputRelayStkId_Object = MibTableColumn
atAlmMonOutputRelayStkId = _AtAlmMonOutputRelayStkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 4, 1, 1),
    _AtAlmMonOutputRelayStkId_Type()
)
atAlmMonOutputRelayStkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonOutputRelayStkId.setStatus("current")
_AtAlmMonOutputRelayNumber_Type = Unsigned32
_AtAlmMonOutputRelayNumber_Object = MibTableColumn
atAlmMonOutputRelayNumber = _AtAlmMonOutputRelayNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 4, 1, 2),
    _AtAlmMonOutputRelayNumber_Type()
)
atAlmMonOutputRelayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonOutputRelayNumber.setStatus("current")
_AtAlmMonOutputRelayAlarmId_Type = Unsigned32
_AtAlmMonOutputRelayAlarmId_Object = MibTableColumn
atAlmMonOutputRelayAlarmId = _AtAlmMonOutputRelayAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 4, 1, 3),
    _AtAlmMonOutputRelayAlarmId_Type()
)
atAlmMonOutputRelayAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonOutputRelayAlarmId.setStatus("current")
_AtAlmMonOutputRelayUsage_Type = AtAlmMonActionUseOutput
_AtAlmMonOutputRelayUsage_Object = MibTableColumn
atAlmMonOutputRelayUsage = _AtAlmMonOutputRelayUsage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 4, 1, 4),
    _AtAlmMonOutputRelayUsage_Type()
)
atAlmMonOutputRelayUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonOutputRelayUsage.setStatus("current")
_AtAlmMonOutputLedTable_Object = MibTable
atAlmMonOutputLedTable = _AtAlmMonOutputLedTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 5)
)
if mibBuilder.loadTexts:
    atAlmMonOutputLedTable.setStatus("current")
_AtAlmMonOutputLedEntry_Object = MibTableRow
atAlmMonOutputLedEntry = _AtAlmMonOutputLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 5, 1)
)
atAlmMonOutputLedEntry.setIndexNames(
    (0, "AT-ALMMON-MIB", "atAlmMonOutputRelayStkId"),
    (0, "AT-ALMMON-MIB", "atAlmMonOutputRelayAlarmId"),
)
if mibBuilder.loadTexts:
    atAlmMonOutputLedEntry.setStatus("current")
_AtAlmMonOutputLedStkId_Type = Unsigned32
_AtAlmMonOutputLedStkId_Object = MibTableColumn
atAlmMonOutputLedStkId = _AtAlmMonOutputLedStkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 5, 1, 1),
    _AtAlmMonOutputLedStkId_Type()
)
atAlmMonOutputLedStkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonOutputLedStkId.setStatus("current")
_AtAlmMonOutputLedAlarmId_Type = Unsigned32
_AtAlmMonOutputLedAlarmId_Object = MibTableColumn
atAlmMonOutputLedAlarmId = _AtAlmMonOutputLedAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 5, 1, 2),
    _AtAlmMonOutputLedAlarmId_Type()
)
atAlmMonOutputLedAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonOutputLedAlarmId.setStatus("current")
_AtAlmMonOutputLedUsage_Type = AtAlmMonActionUseOutput
_AtAlmMonOutputLedUsage_Object = MibTableColumn
atAlmMonOutputLedUsage = _AtAlmMonOutputLedUsage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 5, 1, 3),
    _AtAlmMonOutputLedUsage_Type()
)
atAlmMonOutputLedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonOutputLedUsage.setStatus("current")
_AtAlmMonInputContactTable_Object = MibTable
atAlmMonInputContactTable = _AtAlmMonInputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 6)
)
if mibBuilder.loadTexts:
    atAlmMonInputContactTable.setStatus("current")
_AtAlmMonInputContactEntry_Object = MibTableRow
atAlmMonInputContactEntry = _AtAlmMonInputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 6, 1)
)
atAlmMonInputContactEntry.setIndexNames(
    (0, "AT-ALMMON-MIB", "atAlmMonInputContactStkId"),
    (0, "AT-ALMMON-MIB", "atAlmMonInputContactNumber"),
)
if mibBuilder.loadTexts:
    atAlmMonInputContactEntry.setStatus("current")
_AtAlmMonInputContactStkId_Type = Unsigned32
_AtAlmMonInputContactStkId_Object = MibTableColumn
atAlmMonInputContactStkId = _AtAlmMonInputContactStkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 6, 1, 1),
    _AtAlmMonInputContactStkId_Type()
)
atAlmMonInputContactStkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonInputContactStkId.setStatus("current")
_AtAlmMonInputContactNumber_Type = Unsigned32
_AtAlmMonInputContactNumber_Object = MibTableColumn
atAlmMonInputContactNumber = _AtAlmMonInputContactNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 6, 1, 2),
    _AtAlmMonInputContactNumber_Type()
)
atAlmMonInputContactNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonInputContactNumber.setStatus("current")
_AtAlmMonInputContactPosition_Type = AtAlmMonContactPosition
_AtAlmMonInputContactPosition_Object = MibTableColumn
atAlmMonInputContactPosition = _AtAlmMonInputContactPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 6, 1, 3),
    _AtAlmMonInputContactPosition_Type()
)
atAlmMonInputContactPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonInputContactPosition.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ALMMON-MIB",
    **{"AtAlmMonAlarmType": AtAlmMonAlarmType,
       "AtAlmMonActionUseOutput": AtAlmMonActionUseOutput,
       "AtAlmMonAbnormalState": AtAlmMonAbnormalState,
       "AtAlmMonActionState": AtAlmMonActionState,
       "AtAlmMonContactPosition": AtAlmMonContactPosition,
       "atAlmMon": atAlmMon,
       "atAlmMonActionTable": atAlmMonActionTable,
       "atAlmMonActionEntry": atAlmMonActionEntry,
       "atAlmMonActionStackMemberId": atAlmMonActionStackMemberId,
       "atAlmMonActionIndex": atAlmMonActionIndex,
       "atAlmMonAlarmType": atAlmMonAlarmType,
       "atAlmMonAlarmTypeSelection": atAlmMonAlarmTypeSelection,
       "atAlmMonActionDescription": atAlmMonActionDescription,
       "atAlmMonActionUseRelay1": atAlmMonActionUseRelay1,
       "atAlmMonActionUseRelay2": atAlmMonActionUseRelay2,
       "atAlmMonActionUseRelay3": atAlmMonActionUseRelay3,
       "atAlmMonActionUseFaultLed": atAlmMonActionUseFaultLed,
       "atAlmMonAbnormalState": atAlmMonAbnormalState,
       "atAlmMonActionState": atAlmMonActionState,
       "atAlmMonPerStackConfiguration": atAlmMonPerStackConfiguration,
       "atAlmMonAvailableTable": atAlmMonAvailableTable,
       "atAlmMonAvailableEntry": atAlmMonAvailableEntry,
       "atAlmMonAvailableAlarmId": atAlmMonAvailableAlarmId,
       "atAlmMonAvailableType": atAlmMonAvailableType,
       "atAlmMonAvailableTypeIndex": atAlmMonAvailableTypeIndex,
       "atAlmMonAvailableStkId": atAlmMonAvailableStkId,
       "atAlmMonAvailableIfName": atAlmMonAvailableIfName,
       "atAlmMonAvailableState": atAlmMonAvailableState,
       "atAlmMonOutputRelayTable": atAlmMonOutputRelayTable,
       "atAlmMonOutputRelayEntry": atAlmMonOutputRelayEntry,
       "atAlmMonOutputRelayStkId": atAlmMonOutputRelayStkId,
       "atAlmMonOutputRelayNumber": atAlmMonOutputRelayNumber,
       "atAlmMonOutputRelayAlarmId": atAlmMonOutputRelayAlarmId,
       "atAlmMonOutputRelayUsage": atAlmMonOutputRelayUsage,
       "atAlmMonOutputLedTable": atAlmMonOutputLedTable,
       "atAlmMonOutputLedEntry": atAlmMonOutputLedEntry,
       "atAlmMonOutputLedStkId": atAlmMonOutputLedStkId,
       "atAlmMonOutputLedAlarmId": atAlmMonOutputLedAlarmId,
       "atAlmMonOutputLedUsage": atAlmMonOutputLedUsage,
       "atAlmMonInputContactTable": atAlmMonInputContactTable,
       "atAlmMonInputContactEntry": atAlmMonInputContactEntry,
       "atAlmMonInputContactStkId": atAlmMonInputContactStkId,
       "atAlmMonInputContactNumber": atAlmMonInputContactNumber,
       "atAlmMonInputContactPosition": atAlmMonInputContactPosition}
)
