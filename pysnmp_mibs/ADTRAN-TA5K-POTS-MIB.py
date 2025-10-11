# SNMP MIB module (ADTRAN-TA5K-POTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-POTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:04 2025
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

(adGenPortInfoIndex,
 adGenPortTrapIdentifier) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex",
    "adGenPortTrapIdentifier")

(adGenSlotAlarmStatus,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotAlarmStatus",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adMgmt",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adTA5kPotsID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 753)
)
if mibBuilder.loadTexts:
    adTA5kPotsID.setRevisions(
        ("2022-01-07 00:00",
         "2019-03-21 00:00",
         "2018-04-02 00:00",
         "2018-01-17 00:00",
         "2017-09-25 00:00",
         "2016-12-07 00:00",
         "2016-09-08 00:00",
         "2016-03-24 00:00",
         "2016-03-08 00:00",
         "2015-09-29 00:00",
         "2014-03-06 00:00",
         "2013-03-25 00:00",
         "2011-08-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTA5kPots_ObjectIdentity = ObjectIdentity
adTA5kPots = _AdTA5kPots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 753)
)
_AdTA5kPotsmg_ObjectIdentity = ObjectIdentity
adTA5kPotsmg = _AdTA5kPotsmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753)
)
_AdTA5kPotsProv_ObjectIdentity = ObjectIdentity
adTA5kPotsProv = _AdTA5kPotsProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1)
)
_AdTA5kPotsCardProv_ObjectIdentity = ObjectIdentity
adTA5kPotsCardProv = _AdTA5kPotsCardProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1)
)
_AdTA5kPotsCardProvTable_Object = MibTable
adTA5kPotsCardProvTable = _AdTA5kPotsCardProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsCardProvTable.setStatus("current")
_AdTA5kPotsCardProvEntry_Object = MibTableRow
adTA5kPotsCardProvEntry = _AdTA5kPotsCardProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1)
)
adTA5kPotsCardProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsCardProvEntry.setStatus("current")


class _AdTA5kPotsCardProvRestoreFactoryDefaults_Type(Integer32):
    """Custom type adTA5kPotsCardProvRestoreFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdTA5kPotsCardProvRestoreFactoryDefaults_Type.__name__ = "Integer32"
_AdTA5kPotsCardProvRestoreFactoryDefaults_Object = MibTableColumn
adTA5kPotsCardProvRestoreFactoryDefaults = _AdTA5kPotsCardProvRestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 1),
    _AdTA5kPotsCardProvRestoreFactoryDefaults_Type()
)
adTA5kPotsCardProvRestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardProvRestoreFactoryDefaults.setStatus("current")


class _AdTA5kPotsCardProvVoiceCallControl_Type(Integer32):
    """Custom type adTA5kPotsCardProvVoiceCallControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tunneledGR303", 1),
          ("ccSip", 2),
          ("mgcp", 3))
    )


_AdTA5kPotsCardProvVoiceCallControl_Type.__name__ = "Integer32"
_AdTA5kPotsCardProvVoiceCallControl_Object = MibTableColumn
adTA5kPotsCardProvVoiceCallControl = _AdTA5kPotsCardProvVoiceCallControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 2),
    _AdTA5kPotsCardProvVoiceCallControl_Type()
)
adTA5kPotsCardProvVoiceCallControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardProvVoiceCallControl.setStatus("current")


class _AdTA5kPotsCardReboot_Type(Integer32):
    """Custom type adTA5kPotsCardReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_AdTA5kPotsCardReboot_Type.__name__ = "Integer32"
_AdTA5kPotsCardReboot_Object = MibTableColumn
adTA5kPotsCardReboot = _AdTA5kPotsCardReboot_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 3),
    _AdTA5kPotsCardReboot_Type()
)
adTA5kPotsCardReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardReboot.setStatus("current")


class _AdTA5kPotsCardRemoveBatteryInOosUas_Type(Integer32):
    """Custom type adTA5kPotsCardRemoveBatteryInOosUas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdTA5kPotsCardRemoveBatteryInOosUas_Type.__name__ = "Integer32"
_AdTA5kPotsCardRemoveBatteryInOosUas_Object = MibTableColumn
adTA5kPotsCardRemoveBatteryInOosUas = _AdTA5kPotsCardRemoveBatteryInOosUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 4),
    _AdTA5kPotsCardRemoveBatteryInOosUas_Type()
)
adTA5kPotsCardRemoveBatteryInOosUas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardRemoveBatteryInOosUas.setStatus("current")


class _AdTA5kPotsCardProvLossOfTimingAlarm_Type(Integer32):
    """Custom type adTA5kPotsCardProvLossOfTimingAlarm based on Integer32"""
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


_AdTA5kPotsCardProvLossOfTimingAlarm_Type.__name__ = "Integer32"
_AdTA5kPotsCardProvLossOfTimingAlarm_Object = MibTableColumn
adTA5kPotsCardProvLossOfTimingAlarm = _AdTA5kPotsCardProvLossOfTimingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 5),
    _AdTA5kPotsCardProvLossOfTimingAlarm_Type()
)
adTA5kPotsCardProvLossOfTimingAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardProvLossOfTimingAlarm.setStatus("current")


class _AdTA5kPotsCardProvAllAlarms_Type(Integer32):
    """Custom type adTA5kPotsCardProvAllAlarms based on Integer32"""
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


_AdTA5kPotsCardProvAllAlarms_Type.__name__ = "Integer32"
_AdTA5kPotsCardProvAllAlarms_Object = MibTableColumn
adTA5kPotsCardProvAllAlarms = _AdTA5kPotsCardProvAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 6),
    _AdTA5kPotsCardProvAllAlarms_Type()
)
adTA5kPotsCardProvAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardProvAllAlarms.setStatus("current")


class _AdTA5kPotsCardLineTestScheduleEnable_Type(Integer32):
    """Custom type adTA5kPotsCardLineTestScheduleEnable based on Integer32"""
    defaultValue = 1

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


_AdTA5kPotsCardLineTestScheduleEnable_Type.__name__ = "Integer32"
_AdTA5kPotsCardLineTestScheduleEnable_Object = MibTableColumn
adTA5kPotsCardLineTestScheduleEnable = _AdTA5kPotsCardLineTestScheduleEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 7),
    _AdTA5kPotsCardLineTestScheduleEnable_Type()
)
adTA5kPotsCardLineTestScheduleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardLineTestScheduleEnable.setStatus("current")


class _AdTA5kPotsCardLoadCoilTestScheduleEnable_Type(Integer32):
    """Custom type adTA5kPotsCardLoadCoilTestScheduleEnable based on Integer32"""
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


_AdTA5kPotsCardLoadCoilTestScheduleEnable_Type.__name__ = "Integer32"
_AdTA5kPotsCardLoadCoilTestScheduleEnable_Object = MibTableColumn
adTA5kPotsCardLoadCoilTestScheduleEnable = _AdTA5kPotsCardLoadCoilTestScheduleEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 8),
    _AdTA5kPotsCardLoadCoilTestScheduleEnable_Type()
)
adTA5kPotsCardLoadCoilTestScheduleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardLoadCoilTestScheduleEnable.setStatus("current")


class _AdTA5kPotsCardLineTestScheduleTimeString_Type(DisplayString):
    """Custom type adTA5kPotsCardLineTestScheduleTimeString based on DisplayString"""
    defaultValue = OctetString("02:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_AdTA5kPotsCardLineTestScheduleTimeString_Type.__name__ = "DisplayString"
_AdTA5kPotsCardLineTestScheduleTimeString_Object = MibTableColumn
adTA5kPotsCardLineTestScheduleTimeString = _AdTA5kPotsCardLineTestScheduleTimeString_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 1, 1, 1, 9),
    _AdTA5kPotsCardLineTestScheduleTimeString_Type()
)
adTA5kPotsCardLineTestScheduleTimeString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardLineTestScheduleTimeString.setStatus("current")
_AdTA5kPotsPortProv_ObjectIdentity = ObjectIdentity
adTA5kPotsPortProv = _AdTA5kPotsPortProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2)
)
_AdTA5kPotsPortProvTable_Object = MibTable
adTA5kPotsPortProvTable = _AdTA5kPotsPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsPortProvTable.setStatus("current")
_AdTA5kPotsPortProvEntry_Object = MibTableRow
adTA5kPotsPortProvEntry = _AdTA5kPotsPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1)
)
adTA5kPotsPortProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsPortProvEntry.setStatus("current")


class _AdTA5kPotsPortMode_Type(Integer32):
    """Custom type adTA5kPotsPortMode based on Integer32"""
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
        *(("loopStart", 1),
          ("groundStart", 2),
          ("tr08SingleParty", 3),
          ("tr08Uvg", 4))
    )


_AdTA5kPotsPortMode_Type.__name__ = "Integer32"
_AdTA5kPotsPortMode_Object = MibTableColumn
adTA5kPotsPortMode = _AdTA5kPotsPortMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 1),
    _AdTA5kPotsPortMode_Type()
)
adTA5kPotsPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortMode.setStatus("current")


class _AdTA5kPotsPortImpedance_Type(Integer32):
    """Custom type adTA5kPotsPortImpedance based on Integer32"""
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
        *(("ohm600", 1),
          ("ohm900", 2),
          ("ohm600Plus216uF", 3),
          ("ohm900Plus216uF", 4),
          ("ohmz1", 5),
          ("ohmz2", 6),
          ("ohmz3", 7),
          ("ohmz4", 8),
          ("ohmz5", 9),
          ("ohmz6", 10),
          ("ohmz7", 11),
          ("ohmz8", 12))
    )


_AdTA5kPotsPortImpedance_Type.__name__ = "Integer32"
_AdTA5kPotsPortImpedance_Object = MibTableColumn
adTA5kPotsPortImpedance = _AdTA5kPotsPortImpedance_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 2),
    _AdTA5kPotsPortImpedance_Type()
)
adTA5kPotsPortImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortImpedance.setStatus("current")


class _AdTA5kPotsPortTXTLPString_Type(DisplayString):
    """Custom type adTA5kPotsPortTXTLPString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AdTA5kPotsPortTXTLPString_Type.__name__ = "DisplayString"
_AdTA5kPotsPortTXTLPString_Object = MibTableColumn
adTA5kPotsPortTXTLPString = _AdTA5kPotsPortTXTLPString_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 3),
    _AdTA5kPotsPortTXTLPString_Type()
)
adTA5kPotsPortTXTLPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortTXTLPString.setStatus("current")


class _AdTA5kPotsPortRXTLPString_Type(DisplayString):
    """Custom type adTA5kPotsPortRXTLPString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AdTA5kPotsPortRXTLPString_Type.__name__ = "DisplayString"
_AdTA5kPotsPortRXTLPString_Object = MibTableColumn
adTA5kPotsPortRXTLPString = _AdTA5kPotsPortRXTLPString_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 4),
    _AdTA5kPotsPortRXTLPString_Type()
)
adTA5kPotsPortRXTLPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortRXTLPString.setStatus("current")


class _AdTA5kPotsPortOnHookMsg_Type(Integer32):
    """Custom type adTA5kPotsPortOnHookMsg based on Integer32"""
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


_AdTA5kPotsPortOnHookMsg_Type.__name__ = "Integer32"
_AdTA5kPotsPortOnHookMsg_Object = MibTableColumn
adTA5kPotsPortOnHookMsg = _AdTA5kPotsPortOnHookMsg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 5),
    _AdTA5kPotsPortOnHookMsg_Type()
)
adTA5kPotsPortOnHookMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortOnHookMsg.setStatus("current")


class _AdTA5kPotsPortTrunkConditioningAlarm_Type(Integer32):
    """Custom type adTA5kPotsPortTrunkConditioningAlarm based on Integer32"""
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


_AdTA5kPotsPortTrunkConditioningAlarm_Type.__name__ = "Integer32"
_AdTA5kPotsPortTrunkConditioningAlarm_Object = MibTableColumn
adTA5kPotsPortTrunkConditioningAlarm = _AdTA5kPotsPortTrunkConditioningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 6),
    _AdTA5kPotsPortTrunkConditioningAlarm_Type()
)
adTA5kPotsPortTrunkConditioningAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortTrunkConditioningAlarm.setStatus("current")


class _AdTA5kPotsPortLineShoweringAlarm_Type(Integer32):
    """Custom type adTA5kPotsPortLineShoweringAlarm based on Integer32"""
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


_AdTA5kPotsPortLineShoweringAlarm_Type.__name__ = "Integer32"
_AdTA5kPotsPortLineShoweringAlarm_Object = MibTableColumn
adTA5kPotsPortLineShoweringAlarm = _AdTA5kPotsPortLineShoweringAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 7),
    _AdTA5kPotsPortLineShoweringAlarm_Type()
)
adTA5kPotsPortLineShoweringAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortLineShoweringAlarm.setStatus("current")


class _AdTA5kPotsPortAutoImpedanceMode_Type(Integer32):
    """Custom type adTA5kPotsPortAutoImpedanceMode based on Integer32"""
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


_AdTA5kPotsPortAutoImpedanceMode_Type.__name__ = "Integer32"
_AdTA5kPotsPortAutoImpedanceMode_Object = MibTableColumn
adTA5kPotsPortAutoImpedanceMode = _AdTA5kPotsPortAutoImpedanceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 8),
    _AdTA5kPotsPortAutoImpedanceMode_Type()
)
adTA5kPotsPortAutoImpedanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortAutoImpedanceMode.setStatus("current")


class _AdTA5kPotsPortRingVoltage_Type(Integer32):
    """Custom type adTA5kPotsPortRingVoltage based on Integer32"""
    defaultValue = 3

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
        *(("fifty", 1),
          ("sixty", 2),
          ("seventy", 3),
          ("eighty", 4),
          ("eightyFive", 5),
          ("ninety", 6))
    )


_AdTA5kPotsPortRingVoltage_Type.__name__ = "Integer32"
_AdTA5kPotsPortRingVoltage_Object = MibTableColumn
adTA5kPotsPortRingVoltage = _AdTA5kPotsPortRingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 9),
    _AdTA5kPotsPortRingVoltage_Type()
)
adTA5kPotsPortRingVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortRingVoltage.setStatus("current")


class _AdTA5kPotsPortImpedanceByLoopLength_Type(Integer32):
    """Custom type adTA5kPotsPortImpedanceByLoopLength based on Integer32"""
    defaultValue = 2

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
        *(("loopLengthOther", 1),
          ("loopLengthShort", 2),
          ("loopLengthMedium", 3),
          ("loopLengthLong", 4))
    )


_AdTA5kPotsPortImpedanceByLoopLength_Type.__name__ = "Integer32"
_AdTA5kPotsPortImpedanceByLoopLength_Object = MibTableColumn
adTA5kPotsPortImpedanceByLoopLength = _AdTA5kPotsPortImpedanceByLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 10),
    _AdTA5kPotsPortImpedanceByLoopLength_Type()
)
adTA5kPotsPortImpedanceByLoopLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortImpedanceByLoopLength.setStatus("current")


class _AdTA5kPotsPortOverTempAlarmEnable_Type(Integer32):
    """Custom type adTA5kPotsPortOverTempAlarmEnable based on Integer32"""
    defaultValue = 1

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


_AdTA5kPotsPortOverTempAlarmEnable_Type.__name__ = "Integer32"
_AdTA5kPotsPortOverTempAlarmEnable_Object = MibTableColumn
adTA5kPotsPortOverTempAlarmEnable = _AdTA5kPotsPortOverTempAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 11),
    _AdTA5kPotsPortOverTempAlarmEnable_Type()
)
adTA5kPotsPortOverTempAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortOverTempAlarmEnable.setStatus("current")


class _AdTA5kPotsPortMwiType_Type(Integer32):
    """Custom type adTA5kPotsPortMwiType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwiTypeFsk", 1),
          ("mwiTypeNeon", 2))
    )


_AdTA5kPotsPortMwiType_Type.__name__ = "Integer32"
_AdTA5kPotsPortMwiType_Object = MibTableColumn
adTA5kPotsPortMwiType = _AdTA5kPotsPortMwiType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 12),
    _AdTA5kPotsPortMwiType_Type()
)
adTA5kPotsPortMwiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortMwiType.setStatus("current")


class _AdTA5kPotsPortNeonMwiCadence_Type(Integer32):
    """Custom type adTA5kPotsPortNeonMwiCadence based on Integer32"""
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
        *(("neonMwiCadence1000ms", 1),
          ("neonMwiCadence500ms", 2),
          ("neonMwiCadence250ms", 3))
    )


_AdTA5kPotsPortNeonMwiCadence_Type.__name__ = "Integer32"
_AdTA5kPotsPortNeonMwiCadence_Object = MibTableColumn
adTA5kPotsPortNeonMwiCadence = _AdTA5kPotsPortNeonMwiCadence_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 13),
    _AdTA5kPotsPortNeonMwiCadence_Type()
)
adTA5kPotsPortNeonMwiCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortNeonMwiCadence.setStatus("current")


class _AdTA5kPotsPortNeonMwiVoltage_Type(Integer32):
    """Custom type adTA5kPotsPortNeonMwiVoltage based on Integer32"""
    defaultValue = 2

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
        *(("neonMwiVoltage85volts", 1),
          ("neonMwiVoltage90volts", 2),
          ("neonMwiVoltage100volts", 3),
          ("neonMwiVoltage110volts", 4),
          ("neonMwiVoltage120volts", 5),
          ("neonMwiVoltage130volts", 6))
    )


_AdTA5kPotsPortNeonMwiVoltage_Type.__name__ = "Integer32"
_AdTA5kPotsPortNeonMwiVoltage_Object = MibTableColumn
adTA5kPotsPortNeonMwiVoltage = _AdTA5kPotsPortNeonMwiVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 14),
    _AdTA5kPotsPortNeonMwiVoltage_Type()
)
adTA5kPotsPortNeonMwiVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortNeonMwiVoltage.setStatus("current")


class _AdTA5kPotsPortVoiceCallJitterBufferDepth_Type(Integer32):
    """Custom type adTA5kPotsPortVoiceCallJitterBufferDepth based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_AdTA5kPotsPortVoiceCallJitterBufferDepth_Type.__name__ = "Integer32"
_AdTA5kPotsPortVoiceCallJitterBufferDepth_Object = MibTableColumn
adTA5kPotsPortVoiceCallJitterBufferDepth = _AdTA5kPotsPortVoiceCallJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 15),
    _AdTA5kPotsPortVoiceCallJitterBufferDepth_Type()
)
adTA5kPotsPortVoiceCallJitterBufferDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortVoiceCallJitterBufferDepth.setStatus("current")


class _AdTA5kPotsPortFaxModemCallJitterBufferDepth_Type(Integer32):
    """Custom type adTA5kPotsPortFaxModemCallJitterBufferDepth based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_AdTA5kPotsPortFaxModemCallJitterBufferDepth_Type.__name__ = "Integer32"
_AdTA5kPotsPortFaxModemCallJitterBufferDepth_Object = MibTableColumn
adTA5kPotsPortFaxModemCallJitterBufferDepth = _AdTA5kPotsPortFaxModemCallJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 16),
    _AdTA5kPotsPortFaxModemCallJitterBufferDepth_Type()
)
adTA5kPotsPortFaxModemCallJitterBufferDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortFaxModemCallJitterBufferDepth.setStatus("current")


class _AdTA5kPotsPortCircuitIdentifier_Type(DisplayString):
    """Custom type adTA5kPotsPortCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTA5kPotsPortCircuitIdentifier_Type.__name__ = "DisplayString"
_AdTA5kPotsPortCircuitIdentifier_Object = MibTableColumn
adTA5kPotsPortCircuitIdentifier = _AdTA5kPotsPortCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 17),
    _AdTA5kPotsPortCircuitIdentifier_Type()
)
adTA5kPotsPortCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortCircuitIdentifier.setStatus("current")


class _AdTA5kPotsPulseDigitDetectionEnable_Type(TruthValue):
    """Custom type adTA5kPotsPulseDigitDetectionEnable based on TruthValue"""
    defaultValue = 1


_AdTA5kPotsPulseDigitDetectionEnable_Type.__name__ = "TruthValue"
_AdTA5kPotsPulseDigitDetectionEnable_Object = MibTableColumn
adTA5kPotsPulseDigitDetectionEnable = _AdTA5kPotsPulseDigitDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 1, 2, 1, 1, 18),
    _AdTA5kPotsPulseDigitDetectionEnable_Type()
)
adTA5kPotsPulseDigitDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPulseDigitDetectionEnable.setStatus("current")
_AdTA5kPotsStat_ObjectIdentity = ObjectIdentity
adTA5kPotsStat = _AdTA5kPotsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2)
)
_AdTA5kPotsCardStat_ObjectIdentity = ObjectIdentity
adTA5kPotsCardStat = _AdTA5kPotsCardStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1)
)
_AdTA5kPotsCardStatTable_Object = MibTable
adTA5kPotsCardStatTable = _AdTA5kPotsCardStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsCardStatTable.setStatus("current")
_AdTA5kPotsCardStatEntry_Object = MibTableRow
adTA5kPotsCardStatEntry = _AdTA5kPotsCardStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1)
)
adTA5kPotsCardStatEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsCardStatEntry.setStatus("current")


class _AdTA5kPotsCardSelfTestFPGATest_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestFPGATest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestFPGATest_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestFPGATest_Object = MibTableColumn
adTA5kPotsCardSelfTestFPGATest = _AdTA5kPotsCardSelfTestFPGATest_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 1),
    _AdTA5kPotsCardSelfTestFPGATest_Type()
)
adTA5kPotsCardSelfTestFPGATest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestFPGATest.setStatus("current")


class _AdTA5kPotsCardSelfTestFlashTest_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestFlashTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestFlashTest_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestFlashTest_Object = MibTableColumn
adTA5kPotsCardSelfTestFlashTest = _AdTA5kPotsCardSelfTestFlashTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 2),
    _AdTA5kPotsCardSelfTestFlashTest_Type()
)
adTA5kPotsCardSelfTestFlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestFlashTest.setStatus("current")


class _AdTA5kPotsCardSelfTestLasVegas1Prog_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestLasVegas1Prog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestLasVegas1Prog_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestLasVegas1Prog_Object = MibTableColumn
adTA5kPotsCardSelfTestLasVegas1Prog = _AdTA5kPotsCardSelfTestLasVegas1Prog_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 3),
    _AdTA5kPotsCardSelfTestLasVegas1Prog_Type()
)
adTA5kPotsCardSelfTestLasVegas1Prog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestLasVegas1Prog.setStatus("current")


class _AdTA5kPotsCardSelfTestLasVegas2Prog_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestLasVegas2Prog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestLasVegas2Prog_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestLasVegas2Prog_Object = MibTableColumn
adTA5kPotsCardSelfTestLasVegas2Prog = _AdTA5kPotsCardSelfTestLasVegas2Prog_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 4),
    _AdTA5kPotsCardSelfTestLasVegas2Prog_Type()
)
adTA5kPotsCardSelfTestLasVegas2Prog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestLasVegas2Prog.setStatus("current")


class _AdTA5kPotsCardSelfTestVineticCodecAProg_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestVineticCodecAProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestVineticCodecAProg_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestVineticCodecAProg_Object = MibTableColumn
adTA5kPotsCardSelfTestVineticCodecAProg = _AdTA5kPotsCardSelfTestVineticCodecAProg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 5),
    _AdTA5kPotsCardSelfTestVineticCodecAProg_Type()
)
adTA5kPotsCardSelfTestVineticCodecAProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestVineticCodecAProg.setStatus("current")


class _AdTA5kPotsCardSelfTestVineticCodecBProg_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestVineticCodecBProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestVineticCodecBProg_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestVineticCodecBProg_Object = MibTableColumn
adTA5kPotsCardSelfTestVineticCodecBProg = _AdTA5kPotsCardSelfTestVineticCodecBProg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 6),
    _AdTA5kPotsCardSelfTestVineticCodecBProg_Type()
)
adTA5kPotsCardSelfTestVineticCodecBProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestVineticCodecBProg.setStatus("current")


class _AdTA5kPotsCardSelfTestVineticCodecCProg_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestVineticCodecCProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestVineticCodecCProg_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestVineticCodecCProg_Object = MibTableColumn
adTA5kPotsCardSelfTestVineticCodecCProg = _AdTA5kPotsCardSelfTestVineticCodecCProg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 7),
    _AdTA5kPotsCardSelfTestVineticCodecCProg_Type()
)
adTA5kPotsCardSelfTestVineticCodecCProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestVineticCodecCProg.setStatus("current")


class _AdTA5kPotsCardSelfTestVineticCodecDProg_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestVineticCodecDProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestVineticCodecDProg_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestVineticCodecDProg_Object = MibTableColumn
adTA5kPotsCardSelfTestVineticCodecDProg = _AdTA5kPotsCardSelfTestVineticCodecDProg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 8),
    _AdTA5kPotsCardSelfTestVineticCodecDProg_Type()
)
adTA5kPotsCardSelfTestVineticCodecDProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestVineticCodecDProg.setStatus("current")


class _AdTA5kPotsCardSelfTestVineticCodecEProg_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestVineticCodecEProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestVineticCodecEProg_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestVineticCodecEProg_Object = MibTableColumn
adTA5kPotsCardSelfTestVineticCodecEProg = _AdTA5kPotsCardSelfTestVineticCodecEProg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 9),
    _AdTA5kPotsCardSelfTestVineticCodecEProg_Type()
)
adTA5kPotsCardSelfTestVineticCodecEProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestVineticCodecEProg.setStatus("current")


class _AdTA5kPotsCardSelfTestVineticCodecFProg_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestVineticCodecFProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestVineticCodecFProg_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestVineticCodecFProg_Object = MibTableColumn
adTA5kPotsCardSelfTestVineticCodecFProg = _AdTA5kPotsCardSelfTestVineticCodecFProg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 10),
    _AdTA5kPotsCardSelfTestVineticCodecFProg_Type()
)
adTA5kPotsCardSelfTestVineticCodecFProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestVineticCodecFProg.setStatus("current")


class _AdTA5kPotsCardSelfTestLasVegas3Prog_Type(Integer32):
    """Custom type adTA5kPotsCardSelfTestLasVegas3Prog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AdTA5kPotsCardSelfTestLasVegas3Prog_Type.__name__ = "Integer32"
_AdTA5kPotsCardSelfTestLasVegas3Prog_Object = MibTableColumn
adTA5kPotsCardSelfTestLasVegas3Prog = _AdTA5kPotsCardSelfTestLasVegas3Prog_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 1, 1, 1, 11),
    _AdTA5kPotsCardSelfTestLasVegas3Prog_Type()
)
adTA5kPotsCardSelfTestLasVegas3Prog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardSelfTestLasVegas3Prog.setStatus("current")
_AdTA5kPotsPortStat_ObjectIdentity = ObjectIdentity
adTA5kPotsPortStat = _AdTA5kPotsPortStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2)
)
_AdTA5kPotsPortStatTable_Object = MibTable
adTA5kPotsPortStatTable = _AdTA5kPotsPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsPortStatTable.setStatus("current")
_AdTA5kPotsPortStatEntry_Object = MibTableRow
adTA5kPotsPortStatEntry = _AdTA5kPotsPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1)
)
adTA5kPotsPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsPortStatEntry.setStatus("current")


class _AdTA5kPotsPortStatLineMode_Type(Integer32):
    """Custom type adTA5kPotsPortStatLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopStart", 1),
          ("groundStart", 2))
    )


_AdTA5kPotsPortStatLineMode_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatLineMode_Object = MibTableColumn
adTA5kPotsPortStatLineMode = _AdTA5kPotsPortStatLineMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 1),
    _AdTA5kPotsPortStatLineMode_Type()
)
adTA5kPotsPortStatLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatLineMode.setStatus("current")


class _AdTA5kPotsPortStatLineActive_Type(Integer32):
    """Custom type adTA5kPotsPortStatLineActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_AdTA5kPotsPortStatLineActive_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatLineActive_Object = MibTableColumn
adTA5kPotsPortStatLineActive = _AdTA5kPotsPortStatLineActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 2),
    _AdTA5kPotsPortStatLineActive_Type()
)
adTA5kPotsPortStatLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatLineActive.setStatus("current")


class _AdTA5kPotsPortStatLineCompression_Type(Integer32):
    """Custom type adTA5kPotsPortStatLineCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711", 1),
          ("g726", 2))
    )


_AdTA5kPotsPortStatLineCompression_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatLineCompression_Object = MibTableColumn
adTA5kPotsPortStatLineCompression = _AdTA5kPotsPortStatLineCompression_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 3),
    _AdTA5kPotsPortStatLineCompression_Type()
)
adTA5kPotsPortStatLineCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatLineCompression.setStatus("current")


class _AdTA5kPotsPortStatLoopFeed_Type(Integer32):
    """Custom type adTA5kPotsPortStatLoopFeed based on Integer32"""
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
        *(("lcf", 1),
          ("rlcf", 2),
          ("osi", 3),
          ("tipGround", 4),
          ("ringing", 5),
          ("powerDown", 6))
    )


_AdTA5kPotsPortStatLoopFeed_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatLoopFeed_Object = MibTableColumn
adTA5kPotsPortStatLoopFeed = _AdTA5kPotsPortStatLoopFeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 4),
    _AdTA5kPotsPortStatLoopFeed_Type()
)
adTA5kPotsPortStatLoopFeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatLoopFeed.setStatus("current")


class _AdTA5kPotsPortStatLoopState_Type(Integer32):
    """Custom type adTA5kPotsPortStatLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopOpen", 1),
          ("loopClosed", 2),
          ("ringGround", 3))
    )


_AdTA5kPotsPortStatLoopState_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatLoopState_Object = MibTableColumn
adTA5kPotsPortStatLoopState = _AdTA5kPotsPortStatLoopState_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 5),
    _AdTA5kPotsPortStatLoopState_Type()
)
adTA5kPotsPortStatLoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatLoopState.setStatus("current")


class _AdTA5kPotsPortStatTestActive_Type(Integer32):
    """Custom type adTA5kPotsPortStatTestActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdTA5kPotsPortStatTestActive_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatTestActive_Object = MibTableColumn
adTA5kPotsPortStatTestActive = _AdTA5kPotsPortStatTestActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 6),
    _AdTA5kPotsPortStatTestActive_Type()
)
adTA5kPotsPortStatTestActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatTestActive.setStatus("current")


class _AdTA5kPotsPortStatServiceState_Type(Integer32):
    """Custom type adTA5kPotsPortStatServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oosUAS", 2),
          ("oosMA", 3))
    )


_AdTA5kPotsPortStatServiceState_Type.__name__ = "Integer32"
_AdTA5kPotsPortStatServiceState_Object = MibTableColumn
adTA5kPotsPortStatServiceState = _AdTA5kPotsPortStatServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 7),
    _AdTA5kPotsPortStatServiceState_Type()
)
adTA5kPotsPortStatServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortStatServiceState.setStatus("current")


class _AdTA5kPotsPortMwiStatus_Type(Integer32):
    """Custom type adTA5kPotsPortMwiStatus based on Integer32"""
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
          ("indicatorOff", 2),
          ("indicatorOn", 3),
          ("indicatorOffForced", 4),
          ("indicatorOnForced", 5))
    )


_AdTA5kPotsPortMwiStatus_Type.__name__ = "Integer32"
_AdTA5kPotsPortMwiStatus_Object = MibTableColumn
adTA5kPotsPortMwiStatus = _AdTA5kPotsPortMwiStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 2, 1, 1, 8),
    _AdTA5kPotsPortMwiStatus_Type()
)
adTA5kPotsPortMwiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortMwiStatus.setStatus("current")
_AdTA5kPotsStatistics_ObjectIdentity = ObjectIdentity
adTA5kPotsStatistics = _AdTA5kPotsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3)
)
_AdTA5kPotscardStatistics_ObjectIdentity = ObjectIdentity
adTA5kPotscardStatistics = _AdTA5kPotscardStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1)
)
_AdTA5kPotscardStatisticsTable_Object = MibTable
adTA5kPotscardStatisticsTable = _AdTA5kPotscardStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotscardStatisticsTable.setStatus("current")
_AdTA5kPotscardStatisticsEntry_Object = MibTableRow
adTA5kPotscardStatisticsEntry = _AdTA5kPotscardStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1, 1)
)
adTA5kPotscardStatisticsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotscardStatisticsEntry.setStatus("current")
_AdTA5kPotsCardRXEthernetPkts_Type = Integer32
_AdTA5kPotsCardRXEthernetPkts_Object = MibTableColumn
adTA5kPotsCardRXEthernetPkts = _AdTA5kPotsCardRXEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1, 1, 1),
    _AdTA5kPotsCardRXEthernetPkts_Type()
)
adTA5kPotsCardRXEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardRXEthernetPkts.setStatus("current")
_AdTA5kPotsCardTXEthernetPkts_Type = Integer32
_AdTA5kPotsCardTXEthernetPkts_Object = MibTableColumn
adTA5kPotsCardTXEthernetPkts = _AdTA5kPotsCardTXEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1, 1, 2),
    _AdTA5kPotsCardTXEthernetPkts_Type()
)
adTA5kPotsCardTXEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardTXEthernetPkts.setStatus("current")
_AdTA5kPotsCardVoiceGatewayTimeouts_Type = Integer32
_AdTA5kPotsCardVoiceGatewayTimeouts_Object = MibTableColumn
adTA5kPotsCardVoiceGatewayTimeouts = _AdTA5kPotsCardVoiceGatewayTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1, 1, 3),
    _AdTA5kPotsCardVoiceGatewayTimeouts_Type()
)
adTA5kPotsCardVoiceGatewayTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsCardVoiceGatewayTimeouts.setStatus("current")
_AdTA5kPotsCardClearStatistics_Type = Integer32
_AdTA5kPotsCardClearStatistics_Object = MibTableColumn
adTA5kPotsCardClearStatistics = _AdTA5kPotsCardClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1, 1, 4),
    _AdTA5kPotsCardClearStatistics_Type()
)
adTA5kPotsCardClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardClearStatistics.setStatus("current")
_AdTA5kPotsPortClearStatistics_Type = Integer32
_AdTA5kPotsPortClearStatistics_Object = MibTableColumn
adTA5kPotsPortClearStatistics = _AdTA5kPotsPortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 1, 1, 1, 5),
    _AdTA5kPotsPortClearStatistics_Type()
)
adTA5kPotsPortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortClearStatistics.setStatus("current")
_AdTA5kPotsPortStatistics_ObjectIdentity = ObjectIdentity
adTA5kPotsPortStatistics = _AdTA5kPotsPortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2)
)
_AdTA5kPotsPortStatisticsTable_Object = MibTable
adTA5kPotsPortStatisticsTable = _AdTA5kPotsPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsPortStatisticsTable.setStatus("current")
_AdTA5kPotsPortStatisticsEntry_Object = MibTableRow
adTA5kPotsPortStatisticsEntry = _AdTA5kPotsPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2, 1, 1)
)
adTA5kPotsPortStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsPortStatisticsEntry.setStatus("current")
_AdTA5kPotsPortRXVoicePkts_Type = Integer32
_AdTA5kPotsPortRXVoicePkts_Object = MibTableColumn
adTA5kPotsPortRXVoicePkts = _AdTA5kPotsPortRXVoicePkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2, 1, 1, 1),
    _AdTA5kPotsPortRXVoicePkts_Type()
)
adTA5kPotsPortRXVoicePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortRXVoicePkts.setStatus("current")
_AdTA5kPotsPortTXVoicePkts_Type = Integer32
_AdTA5kPotsPortTXVoicePkts_Object = MibTableColumn
adTA5kPotsPortTXVoicePkts = _AdTA5kPotsPortTXVoicePkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2, 1, 1, 2),
    _AdTA5kPotsPortTXVoicePkts_Type()
)
adTA5kPotsPortTXVoicePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortTXVoicePkts.setStatus("current")
_AdTA5kPotsPortRXSignalPkts_Type = Integer32
_AdTA5kPotsPortRXSignalPkts_Object = MibTableColumn
adTA5kPotsPortRXSignalPkts = _AdTA5kPotsPortRXSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2, 1, 1, 3),
    _AdTA5kPotsPortRXSignalPkts_Type()
)
adTA5kPotsPortRXSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortRXSignalPkts.setStatus("current")
_AdTA5kPotsPortTXSignalPkts_Type = Integer32
_AdTA5kPotsPortTXSignalPkts_Object = MibTableColumn
adTA5kPotsPortTXSignalPkts = _AdTA5kPotsPortTXSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 2, 3, 2, 1, 1, 4),
    _AdTA5kPotsPortTXSignalPkts_Type()
)
adTA5kPotsPortTXSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kPotsPortTXSignalPkts.setStatus("current")
_AdTA5kPotsTest_ObjectIdentity = ObjectIdentity
adTA5kPotsTest = _AdTA5kPotsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3)
)
_AdTA5kPotsCardTest_ObjectIdentity = ObjectIdentity
adTA5kPotsCardTest = _AdTA5kPotsCardTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 1)
)
_AdTA5kPotsCardTestTable_Object = MibTable
adTA5kPotsCardTestTable = _AdTA5kPotsCardTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 1, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsCardTestTable.setStatus("current")
_AdTA5kPotsCardTestEntry_Object = MibTableRow
adTA5kPotsCardTestEntry = _AdTA5kPotsCardTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 1, 1, 1)
)
adTA5kPotsCardTestEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsCardTestEntry.setStatus("current")


class _AdTA5kPotsCardTestLpbkPotsLine_Type(Integer32):
    """Custom type adTA5kPotsCardTestLpbkPotsLine based on Integer32"""
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


_AdTA5kPotsCardTestLpbkPotsLine_Type.__name__ = "Integer32"
_AdTA5kPotsCardTestLpbkPotsLine_Object = MibTableColumn
adTA5kPotsCardTestLpbkPotsLine = _AdTA5kPotsCardTestLpbkPotsLine_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 1, 1, 1, 1),
    _AdTA5kPotsCardTestLpbkPotsLine_Type()
)
adTA5kPotsCardTestLpbkPotsLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardTestLpbkPotsLine.setStatus("current")


class _AdTA5kPotsCardTestLpbkPotsPayload_Type(Integer32):
    """Custom type adTA5kPotsCardTestLpbkPotsPayload based on Integer32"""
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


_AdTA5kPotsCardTestLpbkPotsPayload_Type.__name__ = "Integer32"
_AdTA5kPotsCardTestLpbkPotsPayload_Object = MibTableColumn
adTA5kPotsCardTestLpbkPotsPayload = _AdTA5kPotsCardTestLpbkPotsPayload_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 1, 1, 1, 2),
    _AdTA5kPotsCardTestLpbkPotsPayload_Type()
)
adTA5kPotsCardTestLpbkPotsPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsCardTestLpbkPotsPayload.setStatus("current")
_AdTA5kPotsLineTest_ObjectIdentity = ObjectIdentity
adTA5kPotsLineTest = _AdTA5kPotsLineTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2)
)
_AdTA5kPotsLineTestTable_Object = MibTable
adTA5kPotsLineTestTable = _AdTA5kPotsLineTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1)
)
if mibBuilder.loadTexts:
    adTA5kPotsLineTestTable.setStatus("current")
_AdTA5kPotsLineTestEntry_Object = MibTableRow
adTA5kPotsLineTestEntry = _AdTA5kPotsLineTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1)
)
adTA5kPotsLineTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTA5kPotsLineTestEntry.setStatus("current")


class _AdTA5kPotsLineTest1004HzTone_Type(Integer32):
    """Custom type adTA5kPotsLineTest1004HzTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("toLoop", 1),
          ("toNetwork", 2),
          ("disable", 3))
    )


_AdTA5kPotsLineTest1004HzTone_Type.__name__ = "Integer32"
_AdTA5kPotsLineTest1004HzTone_Object = MibTableColumn
adTA5kPotsLineTest1004HzTone = _AdTA5kPotsLineTest1004HzTone_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 1),
    _AdTA5kPotsLineTest1004HzTone_Type()
)
adTA5kPotsLineTest1004HzTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTest1004HzTone.setStatus("current")


class _AdTA5kPotsLineTestRingCadence_Type(Integer32):
    """Custom type adTA5kPotsLineTestRingCadence based on Integer32"""
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


_AdTA5kPotsLineTestRingCadence_Type.__name__ = "Integer32"
_AdTA5kPotsLineTestRingCadence_Object = MibTableColumn
adTA5kPotsLineTestRingCadence = _AdTA5kPotsLineTestRingCadence_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 2),
    _AdTA5kPotsLineTestRingCadence_Type()
)
adTA5kPotsLineTestRingCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTestRingCadence.setStatus("current")


class _AdTA5kPotsLineTestLoopState_Type(Integer32):
    """Custom type adTA5kPotsLineTestLoopState based on Integer32"""
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
        *(("disable", 1),
          ("activeHigh", 2),
          ("activeLow", 3),
          ("reverseActiveHigh", 4),
          ("reverseActiveLow", 5),
          ("powerDownActive", 6),
          ("powerDownResistive", 7),
          ("tipGround", 8),
          ("activeTest", 9),
          ("tipOpen", 10))
    )


_AdTA5kPotsLineTestLoopState_Type.__name__ = "Integer32"
_AdTA5kPotsLineTestLoopState_Object = MibTableColumn
adTA5kPotsLineTestLoopState = _AdTA5kPotsLineTestLoopState_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 3),
    _AdTA5kPotsLineTestLoopState_Type()
)
adTA5kPotsLineTestLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTestLoopState.setStatus("current")


class _AdTA5kPotsLineClearTest_Type(Integer32):
    """Custom type adTA5kPotsLineClearTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdTA5kPotsLineClearTest_Type.__name__ = "Integer32"
_AdTA5kPotsLineClearTest_Object = MibTableColumn
adTA5kPotsLineClearTest = _AdTA5kPotsLineClearTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 4),
    _AdTA5kPotsLineClearTest_Type()
)
adTA5kPotsLineClearTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineClearTest.setStatus("current")


class _AdTA5kPotsLineTestWarbleTone_Type(Integer32):
    """Custom type adTA5kPotsLineTestWarbleTone based on Integer32"""
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


_AdTA5kPotsLineTestWarbleTone_Type.__name__ = "Integer32"
_AdTA5kPotsLineTestWarbleTone_Object = MibTableColumn
adTA5kPotsLineTestWarbleTone = _AdTA5kPotsLineTestWarbleTone_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 5),
    _AdTA5kPotsLineTestWarbleTone_Type()
)
adTA5kPotsLineTestWarbleTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTestWarbleTone.setStatus("current")


class _AdTA5kPotsLineTestWarbleToneFreq1_Type(Integer32):
    """Custom type adTA5kPotsLineTestWarbleToneFreq1 based on Integer32"""
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
        *(("silence", 1),
          ("tone1004hz", 2),
          ("tone1400hz", 3),
          ("tone2040hz", 4))
    )


_AdTA5kPotsLineTestWarbleToneFreq1_Type.__name__ = "Integer32"
_AdTA5kPotsLineTestWarbleToneFreq1_Object = MibTableColumn
adTA5kPotsLineTestWarbleToneFreq1 = _AdTA5kPotsLineTestWarbleToneFreq1_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 6),
    _AdTA5kPotsLineTestWarbleToneFreq1_Type()
)
adTA5kPotsLineTestWarbleToneFreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTestWarbleToneFreq1.setStatus("current")


class _AdTA5kPotsLineTestWarbleToneFreq2_Type(Integer32):
    """Custom type adTA5kPotsLineTestWarbleToneFreq2 based on Integer32"""
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
        *(("silence", 1),
          ("tone1004hz", 2),
          ("tone1400hz", 3),
          ("tone2040hz", 4))
    )


_AdTA5kPotsLineTestWarbleToneFreq2_Type.__name__ = "Integer32"
_AdTA5kPotsLineTestWarbleToneFreq2_Object = MibTableColumn
adTA5kPotsLineTestWarbleToneFreq2 = _AdTA5kPotsLineTestWarbleToneFreq2_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 7),
    _AdTA5kPotsLineTestWarbleToneFreq2_Type()
)
adTA5kPotsLineTestWarbleToneFreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTestWarbleToneFreq2.setStatus("current")


class _AdTA5kPotsLineTestWarbleToneCadence_Type(Integer32):
    """Custom type adTA5kPotsLineTestWarbleToneCadence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("time100ms", 1),
          ("time250ms", 2),
          ("time500ms", 3))
    )


_AdTA5kPotsLineTestWarbleToneCadence_Type.__name__ = "Integer32"
_AdTA5kPotsLineTestWarbleToneCadence_Object = MibTableColumn
adTA5kPotsLineTestWarbleToneCadence = _AdTA5kPotsLineTestWarbleToneCadence_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 8),
    _AdTA5kPotsLineTestWarbleToneCadence_Type()
)
adTA5kPotsLineTestWarbleToneCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsLineTestWarbleToneCadence.setStatus("current")


class _AdTA5kPotsPortForceMwiOffEvent_Type(Integer32):
    """Custom type adTA5kPotsPortForceMwiOffEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("indicatorOff", 1)
    )


_AdTA5kPotsPortForceMwiOffEvent_Type.__name__ = "Integer32"
_AdTA5kPotsPortForceMwiOffEvent_Object = MibTableColumn
adTA5kPotsPortForceMwiOffEvent = _AdTA5kPotsPortForceMwiOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 9),
    _AdTA5kPotsPortForceMwiOffEvent_Type()
)
adTA5kPotsPortForceMwiOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortForceMwiOffEvent.setStatus("current")


class _AdTA5kPotsPortForceMwiOnEvent_Type(Integer32):
    """Custom type adTA5kPotsPortForceMwiOnEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("indicatorOn", 1)
    )


_AdTA5kPotsPortForceMwiOnEvent_Type.__name__ = "Integer32"
_AdTA5kPotsPortForceMwiOnEvent_Object = MibTableColumn
adTA5kPotsPortForceMwiOnEvent = _AdTA5kPotsPortForceMwiOnEvent_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 3, 2, 1, 1, 10),
    _AdTA5kPotsPortForceMwiOnEvent_Type()
)
adTA5kPotsPortForceMwiOnEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kPotsPortForceMwiOnEvent.setStatus("current")
_AdTA5kPotsAlarm_ObjectIdentity = ObjectIdentity
adTA5kPotsAlarm = _AdTA5kPotsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4)
)
_AdTA5kPotsAlarmEvents_ObjectIdentity = ObjectIdentity
adTA5kPotsAlarmEvents = _AdTA5kPotsAlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0)
)

# Managed Objects groups


# Notification objects

adTa5kPotsTrunkConditioningTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 2)
)
adTa5kPotsTrunkConditioningTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsTrunkConditioningTrapClear.setStatus(
        "current"
    )

adTa5kPotsTrunkConditioningTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 3)
)
adTa5kPotsTrunkConditioningTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsTrunkConditioningTrapActive.setStatus(
        "current"
    )

adTa5kPotsLineShoweringTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 4)
)
adTa5kPotsLineShoweringTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsLineShoweringTrapClear.setStatus(
        "current"
    )

adTa5kPotsLineShoweringTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 5)
)
adTa5kPotsLineShoweringTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsLineShoweringTrapActive.setStatus(
        "current"
    )

adTa5kPotsBackplaneTimingTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 6)
)
adTa5kPotsBackplaneTimingTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsBackplaneTimingTrapClear.setStatus(
        "current"
    )

adTa5kPotsBackplaneTimingTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 7)
)
adTa5kPotsBackplaneTimingTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsBackplaneTimingTrapActive.setStatus(
        "current"
    )

adTa5kPotsOverTempTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 8)
)
adTa5kPotsOverTempTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsOverTempTrapClear.setStatus(
        "current"
    )

adTa5kPotsOverTempTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 753, 4, 0, 9)
)
adTa5kPotsOverTempTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kPotsOverTempTrapActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-POTS-MIB",
    **{"adTA5kPots": adTA5kPots,
       "adTA5kPotsmg": adTA5kPotsmg,
       "adTA5kPotsProv": adTA5kPotsProv,
       "adTA5kPotsCardProv": adTA5kPotsCardProv,
       "adTA5kPotsCardProvTable": adTA5kPotsCardProvTable,
       "adTA5kPotsCardProvEntry": adTA5kPotsCardProvEntry,
       "adTA5kPotsCardProvRestoreFactoryDefaults": adTA5kPotsCardProvRestoreFactoryDefaults,
       "adTA5kPotsCardProvVoiceCallControl": adTA5kPotsCardProvVoiceCallControl,
       "adTA5kPotsCardReboot": adTA5kPotsCardReboot,
       "adTA5kPotsCardRemoveBatteryInOosUas": adTA5kPotsCardRemoveBatteryInOosUas,
       "adTA5kPotsCardProvLossOfTimingAlarm": adTA5kPotsCardProvLossOfTimingAlarm,
       "adTA5kPotsCardProvAllAlarms": adTA5kPotsCardProvAllAlarms,
       "adTA5kPotsCardLineTestScheduleEnable": adTA5kPotsCardLineTestScheduleEnable,
       "adTA5kPotsCardLoadCoilTestScheduleEnable": adTA5kPotsCardLoadCoilTestScheduleEnable,
       "adTA5kPotsCardLineTestScheduleTimeString": adTA5kPotsCardLineTestScheduleTimeString,
       "adTA5kPotsPortProv": adTA5kPotsPortProv,
       "adTA5kPotsPortProvTable": adTA5kPotsPortProvTable,
       "adTA5kPotsPortProvEntry": adTA5kPotsPortProvEntry,
       "adTA5kPotsPortMode": adTA5kPotsPortMode,
       "adTA5kPotsPortImpedance": adTA5kPotsPortImpedance,
       "adTA5kPotsPortTXTLPString": adTA5kPotsPortTXTLPString,
       "adTA5kPotsPortRXTLPString": adTA5kPotsPortRXTLPString,
       "adTA5kPotsPortOnHookMsg": adTA5kPotsPortOnHookMsg,
       "adTA5kPotsPortTrunkConditioningAlarm": adTA5kPotsPortTrunkConditioningAlarm,
       "adTA5kPotsPortLineShoweringAlarm": adTA5kPotsPortLineShoweringAlarm,
       "adTA5kPotsPortAutoImpedanceMode": adTA5kPotsPortAutoImpedanceMode,
       "adTA5kPotsPortRingVoltage": adTA5kPotsPortRingVoltage,
       "adTA5kPotsPortImpedanceByLoopLength": adTA5kPotsPortImpedanceByLoopLength,
       "adTA5kPotsPortOverTempAlarmEnable": adTA5kPotsPortOverTempAlarmEnable,
       "adTA5kPotsPortMwiType": adTA5kPotsPortMwiType,
       "adTA5kPotsPortNeonMwiCadence": adTA5kPotsPortNeonMwiCadence,
       "adTA5kPotsPortNeonMwiVoltage": adTA5kPotsPortNeonMwiVoltage,
       "adTA5kPotsPortVoiceCallJitterBufferDepth": adTA5kPotsPortVoiceCallJitterBufferDepth,
       "adTA5kPotsPortFaxModemCallJitterBufferDepth": adTA5kPotsPortFaxModemCallJitterBufferDepth,
       "adTA5kPotsPortCircuitIdentifier": adTA5kPotsPortCircuitIdentifier,
       "adTA5kPotsPulseDigitDetectionEnable": adTA5kPotsPulseDigitDetectionEnable,
       "adTA5kPotsStat": adTA5kPotsStat,
       "adTA5kPotsCardStat": adTA5kPotsCardStat,
       "adTA5kPotsCardStatTable": adTA5kPotsCardStatTable,
       "adTA5kPotsCardStatEntry": adTA5kPotsCardStatEntry,
       "adTA5kPotsCardSelfTestFPGATest": adTA5kPotsCardSelfTestFPGATest,
       "adTA5kPotsCardSelfTestFlashTest": adTA5kPotsCardSelfTestFlashTest,
       "adTA5kPotsCardSelfTestLasVegas1Prog": adTA5kPotsCardSelfTestLasVegas1Prog,
       "adTA5kPotsCardSelfTestLasVegas2Prog": adTA5kPotsCardSelfTestLasVegas2Prog,
       "adTA5kPotsCardSelfTestVineticCodecAProg": adTA5kPotsCardSelfTestVineticCodecAProg,
       "adTA5kPotsCardSelfTestVineticCodecBProg": adTA5kPotsCardSelfTestVineticCodecBProg,
       "adTA5kPotsCardSelfTestVineticCodecCProg": adTA5kPotsCardSelfTestVineticCodecCProg,
       "adTA5kPotsCardSelfTestVineticCodecDProg": adTA5kPotsCardSelfTestVineticCodecDProg,
       "adTA5kPotsCardSelfTestVineticCodecEProg": adTA5kPotsCardSelfTestVineticCodecEProg,
       "adTA5kPotsCardSelfTestVineticCodecFProg": adTA5kPotsCardSelfTestVineticCodecFProg,
       "adTA5kPotsCardSelfTestLasVegas3Prog": adTA5kPotsCardSelfTestLasVegas3Prog,
       "adTA5kPotsPortStat": adTA5kPotsPortStat,
       "adTA5kPotsPortStatTable": adTA5kPotsPortStatTable,
       "adTA5kPotsPortStatEntry": adTA5kPotsPortStatEntry,
       "adTA5kPotsPortStatLineMode": adTA5kPotsPortStatLineMode,
       "adTA5kPotsPortStatLineActive": adTA5kPotsPortStatLineActive,
       "adTA5kPotsPortStatLineCompression": adTA5kPotsPortStatLineCompression,
       "adTA5kPotsPortStatLoopFeed": adTA5kPotsPortStatLoopFeed,
       "adTA5kPotsPortStatLoopState": adTA5kPotsPortStatLoopState,
       "adTA5kPotsPortStatTestActive": adTA5kPotsPortStatTestActive,
       "adTA5kPotsPortStatServiceState": adTA5kPotsPortStatServiceState,
       "adTA5kPotsPortMwiStatus": adTA5kPotsPortMwiStatus,
       "adTA5kPotsStatistics": adTA5kPotsStatistics,
       "adTA5kPotscardStatistics": adTA5kPotscardStatistics,
       "adTA5kPotscardStatisticsTable": adTA5kPotscardStatisticsTable,
       "adTA5kPotscardStatisticsEntry": adTA5kPotscardStatisticsEntry,
       "adTA5kPotsCardRXEthernetPkts": adTA5kPotsCardRXEthernetPkts,
       "adTA5kPotsCardTXEthernetPkts": adTA5kPotsCardTXEthernetPkts,
       "adTA5kPotsCardVoiceGatewayTimeouts": adTA5kPotsCardVoiceGatewayTimeouts,
       "adTA5kPotsCardClearStatistics": adTA5kPotsCardClearStatistics,
       "adTA5kPotsPortClearStatistics": adTA5kPotsPortClearStatistics,
       "adTA5kPotsPortStatistics": adTA5kPotsPortStatistics,
       "adTA5kPotsPortStatisticsTable": adTA5kPotsPortStatisticsTable,
       "adTA5kPotsPortStatisticsEntry": adTA5kPotsPortStatisticsEntry,
       "adTA5kPotsPortRXVoicePkts": adTA5kPotsPortRXVoicePkts,
       "adTA5kPotsPortTXVoicePkts": adTA5kPotsPortTXVoicePkts,
       "adTA5kPotsPortRXSignalPkts": adTA5kPotsPortRXSignalPkts,
       "adTA5kPotsPortTXSignalPkts": adTA5kPotsPortTXSignalPkts,
       "adTA5kPotsTest": adTA5kPotsTest,
       "adTA5kPotsCardTest": adTA5kPotsCardTest,
       "adTA5kPotsCardTestTable": adTA5kPotsCardTestTable,
       "adTA5kPotsCardTestEntry": adTA5kPotsCardTestEntry,
       "adTA5kPotsCardTestLpbkPotsLine": adTA5kPotsCardTestLpbkPotsLine,
       "adTA5kPotsCardTestLpbkPotsPayload": adTA5kPotsCardTestLpbkPotsPayload,
       "adTA5kPotsLineTest": adTA5kPotsLineTest,
       "adTA5kPotsLineTestTable": adTA5kPotsLineTestTable,
       "adTA5kPotsLineTestEntry": adTA5kPotsLineTestEntry,
       "adTA5kPotsLineTest1004HzTone": adTA5kPotsLineTest1004HzTone,
       "adTA5kPotsLineTestRingCadence": adTA5kPotsLineTestRingCadence,
       "adTA5kPotsLineTestLoopState": adTA5kPotsLineTestLoopState,
       "adTA5kPotsLineClearTest": adTA5kPotsLineClearTest,
       "adTA5kPotsLineTestWarbleTone": adTA5kPotsLineTestWarbleTone,
       "adTA5kPotsLineTestWarbleToneFreq1": adTA5kPotsLineTestWarbleToneFreq1,
       "adTA5kPotsLineTestWarbleToneFreq2": adTA5kPotsLineTestWarbleToneFreq2,
       "adTA5kPotsLineTestWarbleToneCadence": adTA5kPotsLineTestWarbleToneCadence,
       "adTA5kPotsPortForceMwiOffEvent": adTA5kPotsPortForceMwiOffEvent,
       "adTA5kPotsPortForceMwiOnEvent": adTA5kPotsPortForceMwiOnEvent,
       "adTA5kPotsAlarm": adTA5kPotsAlarm,
       "adTA5kPotsAlarmEvents": adTA5kPotsAlarmEvents,
       "adTa5kPotsTrunkConditioningTrapClear": adTa5kPotsTrunkConditioningTrapClear,
       "adTa5kPotsTrunkConditioningTrapActive": adTa5kPotsTrunkConditioningTrapActive,
       "adTa5kPotsLineShoweringTrapClear": adTa5kPotsLineShoweringTrapClear,
       "adTa5kPotsLineShoweringTrapActive": adTa5kPotsLineShoweringTrapActive,
       "adTa5kPotsBackplaneTimingTrapClear": adTa5kPotsBackplaneTimingTrapClear,
       "adTa5kPotsBackplaneTimingTrapActive": adTa5kPotsBackplaneTimingTrapActive,
       "adTa5kPotsOverTempTrapClear": adTa5kPotsOverTempTrapClear,
       "adTa5kPotsOverTempTrapActive": adTa5kPotsOverTempTrapActive,
       "adTA5kPotsID": adTA5kPotsID}
)
