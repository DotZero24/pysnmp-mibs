# SNMP MIB module (ADTRAN-TA5000FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5000FAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:54 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
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

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

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

adTa5kFanModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 751)
)
if mibBuilder.loadTexts:
    adTa5kFanModuleIdentity.setRevisions(
        ("2014-10-22 21:00",
         "2011-10-28 21:00",
         "2011-06-20 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTA5kFanModule_ObjectIdentity = ObjectIdentity
adTA5kFanModule = _AdTA5kFanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 751)
)
_AdTa5kFanModuleEvents_ObjectIdentity = ObjectIdentity
adTa5kFanModuleEvents = _AdTa5kFanModuleEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0)
)
_AdTA5kFanModule19_ObjectIdentity = ObjectIdentity
adTA5kFanModule19 = _AdTA5kFanModule19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 860)
)
_AdTA5kFanmg_ObjectIdentity = ObjectIdentity
adTA5kFanmg = _AdTA5kFanmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 751)
)
_AdTA5kFanProvisioning_ObjectIdentity = ObjectIdentity
adTA5kFanProvisioning = _AdTA5kFanProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1)
)
_AdTA5kFanProvTable_Object = MibTable
adTA5kFanProvTable = _AdTA5kFanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1)
)
if mibBuilder.loadTexts:
    adTA5kFanProvTable.setStatus("current")
_AdTA5kFanProvEntry_Object = MibTableRow
adTA5kFanProvEntry = _AdTA5kFanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1)
)
adTA5kFanProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kFanProvEntry.setStatus("current")


class _AdTA5kFanProvFanSpeedMode_Type(Integer32):
    """Custom type adTA5kFanProvFanSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("max", 2))
    )


_AdTA5kFanProvFanSpeedMode_Type.__name__ = "Integer32"
_AdTA5kFanProvFanSpeedMode_Object = MibTableColumn
adTA5kFanProvFanSpeedMode = _AdTA5kFanProvFanSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1, 1),
    _AdTA5kFanProvFanSpeedMode_Type()
)
adTA5kFanProvFanSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kFanProvFanSpeedMode.setStatus("current")


class _AdTA5kFanProvTempThres_Type(Integer32):
    """Custom type adTA5kFanProvTempThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AdTA5kFanProvTempThres_Type.__name__ = "Integer32"
_AdTA5kFanProvTempThres_Object = MibTableColumn
adTA5kFanProvTempThres = _AdTA5kFanProvTempThres_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1, 2),
    _AdTA5kFanProvTempThres_Type()
)
adTA5kFanProvTempThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kFanProvTempThres.setStatus("current")


class _AdTA5kFanProvYellowAlarmEnable_Type(TruthValue):
    """Custom type adTA5kFanProvYellowAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTA5kFanProvYellowAlarmEnable_Type.__name__ = "TruthValue"
_AdTA5kFanProvYellowAlarmEnable_Object = MibTableColumn
adTA5kFanProvYellowAlarmEnable = _AdTA5kFanProvYellowAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1, 3),
    _AdTA5kFanProvYellowAlarmEnable_Type()
)
adTA5kFanProvYellowAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kFanProvYellowAlarmEnable.setStatus("current")


class _AdTA5kFanProvRedAlarmEnable_Type(TruthValue):
    """Custom type adTA5kFanProvRedAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTA5kFanProvRedAlarmEnable_Type.__name__ = "TruthValue"
_AdTA5kFanProvRedAlarmEnable_Object = MibTableColumn
adTA5kFanProvRedAlarmEnable = _AdTA5kFanProvRedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1, 4),
    _AdTA5kFanProvRedAlarmEnable_Type()
)
adTA5kFanProvRedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTA5kFanProvRedAlarmEnable.setStatus("current")


class _AdMultiFanAlarmSeverity_Type(Integer32):
    """Custom type adMultiFanAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("major", 5),
          ("critical", 6))
    )


_AdMultiFanAlarmSeverity_Type.__name__ = "Integer32"
_AdMultiFanAlarmSeverity_Object = MibTableColumn
adMultiFanAlarmSeverity = _AdMultiFanAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1, 5),
    _AdMultiFanAlarmSeverity_Type()
)
adMultiFanAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adMultiFanAlarmSeverity.setStatus("current")


class _AdFanTempThreshAlarmSeverity_Type(Integer32):
    """Custom type adFanTempThreshAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("major", 5),
          ("critical", 6))
    )


_AdFanTempThreshAlarmSeverity_Type.__name__ = "Integer32"
_AdFanTempThreshAlarmSeverity_Object = MibTableColumn
adFanTempThreshAlarmSeverity = _AdFanTempThreshAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 1, 1, 1, 6),
    _AdFanTempThreshAlarmSeverity_Type()
)
adFanTempThreshAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adFanTempThreshAlarmSeverity.setStatus("current")
_AdTA5kFanStatus_ObjectIdentity = ObjectIdentity
adTA5kFanStatus = _AdTA5kFanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2)
)
_AdTA5kFanStatusTable_Object = MibTable
adTA5kFanStatusTable = _AdTA5kFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1)
)
if mibBuilder.loadTexts:
    adTA5kFanStatusTable.setStatus("current")
_AdTA5kFanStatusEntry_Object = MibTableRow
adTA5kFanStatusEntry = _AdTA5kFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1)
)
adTA5kFanStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kFanStatusEntry.setStatus("current")
_AdTA5kFanStatusFan1Speed_Type = DisplayString
_AdTA5kFanStatusFan1Speed_Object = MibTableColumn
adTA5kFanStatusFan1Speed = _AdTA5kFanStatusFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 1),
    _AdTA5kFanStatusFan1Speed_Type()
)
adTA5kFanStatusFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan1Speed.setStatus("current")
_AdTA5kFanStatusFan2Speed_Type = DisplayString
_AdTA5kFanStatusFan2Speed_Object = MibTableColumn
adTA5kFanStatusFan2Speed = _AdTA5kFanStatusFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 2),
    _AdTA5kFanStatusFan2Speed_Type()
)
adTA5kFanStatusFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan2Speed.setStatus("current")
_AdTA5kFanStatusFan3Speed_Type = DisplayString
_AdTA5kFanStatusFan3Speed_Object = MibTableColumn
adTA5kFanStatusFan3Speed = _AdTA5kFanStatusFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 3),
    _AdTA5kFanStatusFan3Speed_Type()
)
adTA5kFanStatusFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan3Speed.setStatus("current")
_AdTA5kFanStatusFan4Speed_Type = DisplayString
_AdTA5kFanStatusFan4Speed_Object = MibTableColumn
adTA5kFanStatusFan4Speed = _AdTA5kFanStatusFan4Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 4),
    _AdTA5kFanStatusFan4Speed_Type()
)
adTA5kFanStatusFan4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan4Speed.setStatus("current")
_AdTA5kFanStatusVoltage_Type = DisplayString
_AdTA5kFanStatusVoltage_Object = MibTableColumn
adTA5kFanStatusVoltage = _AdTA5kFanStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 5),
    _AdTA5kFanStatusVoltage_Type()
)
adTA5kFanStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusVoltage.setStatus("current")
_AdTA5kFanStatusTemp_Type = DisplayString
_AdTA5kFanStatusTemp_Object = MibTableColumn
adTA5kFanStatusTemp = _AdTA5kFanStatusTemp_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 6),
    _AdTA5kFanStatusTemp_Type()
)
adTA5kFanStatusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusTemp.setStatus("current")
_AdTA5kFanStatusVoltageAux_Type = DisplayString
_AdTA5kFanStatusVoltageAux_Object = MibTableColumn
adTA5kFanStatusVoltageAux = _AdTA5kFanStatusVoltageAux_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 7),
    _AdTA5kFanStatusVoltageAux_Type()
)
adTA5kFanStatusVoltageAux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusVoltageAux.setStatus("current")
_AdTA5kFanStatusFan5Speed_Type = DisplayString
_AdTA5kFanStatusFan5Speed_Object = MibTableColumn
adTA5kFanStatusFan5Speed = _AdTA5kFanStatusFan5Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 8),
    _AdTA5kFanStatusFan5Speed_Type()
)
adTA5kFanStatusFan5Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan5Speed.setStatus("current")
_AdTA5kFanStatusFan6Speed_Type = DisplayString
_AdTA5kFanStatusFan6Speed_Object = MibTableColumn
adTA5kFanStatusFan6Speed = _AdTA5kFanStatusFan6Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 9),
    _AdTA5kFanStatusFan6Speed_Type()
)
adTA5kFanStatusFan6Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan6Speed.setStatus("current")
_AdTA5kFanStatusFan7Speed_Type = DisplayString
_AdTA5kFanStatusFan7Speed_Object = MibTableColumn
adTA5kFanStatusFan7Speed = _AdTA5kFanStatusFan7Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 10),
    _AdTA5kFanStatusFan7Speed_Type()
)
adTA5kFanStatusFan7Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan7Speed.setStatus("current")
_AdTA5kFanStatusFan8Speed_Type = DisplayString
_AdTA5kFanStatusFan8Speed_Object = MibTableColumn
adTA5kFanStatusFan8Speed = _AdTA5kFanStatusFan8Speed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 11),
    _AdTA5kFanStatusFan8Speed_Type()
)
adTA5kFanStatusFan8Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kFanStatusFan8Speed.setStatus("current")
_AdTA5kMultiFansInAlarm_Type = Integer32
_AdTA5kMultiFansInAlarm_Object = MibTableColumn
adTA5kMultiFansInAlarm = _AdTA5kMultiFansInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 751, 2, 1, 1, 12),
    _AdTA5kMultiFansInAlarm_Type()
)
adTA5kMultiFansInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kMultiFansInAlarm.setStatus("current")

# Managed Objects groups


# Notification objects

adTA5kFanYellowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0, 1)
)
adTA5kFanYellowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kFanYellowActive.setStatus(
        "current"
    )

adTA5kFanYellowInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0, 2)
)
adTA5kFanYellowInActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kFanYellowInActive.setStatus(
        "current"
    )

adTA5kFanRedActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0, 3)
)
adTA5kFanRedActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-TA5000FAN-MIB", "adTA5kMultiFansInAlarm"))
)
if mibBuilder.loadTexts:
    adTA5kFanRedActive.setStatus(
        "current"
    )

adTA5kFanRedInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0, 4)
)
adTA5kFanRedInActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-TA5000FAN-MIB", "adTA5kMultiFansInAlarm"))
)
if mibBuilder.loadTexts:
    adTA5kFanRedInActive.setStatus(
        "current"
    )

adTA5kFanTempThresExceedActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0, 5)
)
adTA5kFanTempThresExceedActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTA5kFanTempThresExceedActive.setStatus(
        "current"
    )

adTA5kFanTempThresExceedInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 751, 0, 6)
)
adTA5kFanTempThresExceedInactive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTA5kFanTempThresExceedInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5000FAN-MIB",
    **{"adTA5kFanModule": adTA5kFanModule,
       "adTa5kFanModuleEvents": adTa5kFanModuleEvents,
       "adTA5kFanYellowActive": adTA5kFanYellowActive,
       "adTA5kFanYellowInActive": adTA5kFanYellowInActive,
       "adTA5kFanRedActive": adTA5kFanRedActive,
       "adTA5kFanRedInActive": adTA5kFanRedInActive,
       "adTA5kFanTempThresExceedActive": adTA5kFanTempThresExceedActive,
       "adTA5kFanTempThresExceedInactive": adTA5kFanTempThresExceedInactive,
       "adTA5kFanModule19": adTA5kFanModule19,
       "adTA5kFanmg": adTA5kFanmg,
       "adTA5kFanProvisioning": adTA5kFanProvisioning,
       "adTA5kFanProvTable": adTA5kFanProvTable,
       "adTA5kFanProvEntry": adTA5kFanProvEntry,
       "adTA5kFanProvFanSpeedMode": adTA5kFanProvFanSpeedMode,
       "adTA5kFanProvTempThres": adTA5kFanProvTempThres,
       "adTA5kFanProvYellowAlarmEnable": adTA5kFanProvYellowAlarmEnable,
       "adTA5kFanProvRedAlarmEnable": adTA5kFanProvRedAlarmEnable,
       "adMultiFanAlarmSeverity": adMultiFanAlarmSeverity,
       "adFanTempThreshAlarmSeverity": adFanTempThreshAlarmSeverity,
       "adTA5kFanStatus": adTA5kFanStatus,
       "adTA5kFanStatusTable": adTA5kFanStatusTable,
       "adTA5kFanStatusEntry": adTA5kFanStatusEntry,
       "adTA5kFanStatusFan1Speed": adTA5kFanStatusFan1Speed,
       "adTA5kFanStatusFan2Speed": adTA5kFanStatusFan2Speed,
       "adTA5kFanStatusFan3Speed": adTA5kFanStatusFan3Speed,
       "adTA5kFanStatusFan4Speed": adTA5kFanStatusFan4Speed,
       "adTA5kFanStatusVoltage": adTA5kFanStatusVoltage,
       "adTA5kFanStatusTemp": adTA5kFanStatusTemp,
       "adTA5kFanStatusVoltageAux": adTA5kFanStatusVoltageAux,
       "adTA5kFanStatusFan5Speed": adTA5kFanStatusFan5Speed,
       "adTA5kFanStatusFan6Speed": adTA5kFanStatusFan6Speed,
       "adTA5kFanStatusFan7Speed": adTA5kFanStatusFan7Speed,
       "adTA5kFanStatusFan8Speed": adTA5kFanStatusFan8Speed,
       "adTA5kMultiFansInAlarm": adTA5kMultiFansInAlarm,
       "adTa5kFanModuleIdentity": adTa5kFanModuleIdentity}
)
