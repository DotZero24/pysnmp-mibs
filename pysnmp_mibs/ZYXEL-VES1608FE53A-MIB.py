# SNMP MIB module (ZYXEL-VES1608FE53A-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-VES1608FE53A-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:01:07 2025
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
 MacAddress,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1dTrafficClass,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "dot1dTrafficClass")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

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

ves1608fe53a = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_VesSeries_ObjectIdentity = ObjectIdentity
vesSeries = _VesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12)
)
_Alarmconf_ObjectIdentity = ObjectIdentity
alarmconf = _Alarmconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2)
)
_AlarmOps_Type = Integer32
_AlarmOps_Object = MibScalar
alarmOps = _AlarmOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 1),
    _AlarmOps_Type()
)
alarmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOps.setStatus("current")
_AlarmConfTable_Object = MibTable
alarmConfTable = _AlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2)
)
if mibBuilder.loadTexts:
    alarmConfTable.setStatus("current")
_AlarmConfEntry_Object = MibTableRow
alarmConfEntry = _AlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2, 1)
)
alarmConfEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "alarmConfId"),
)
if mibBuilder.loadTexts:
    alarmConfEntry.setStatus("current")
_AlarmConfId_Type = Integer32
_AlarmConfId_Object = MibTableColumn
alarmConfId = _AlarmConfId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2, 1, 1),
    _AlarmConfId_Type()
)
alarmConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConfId.setStatus("current")


class _AlarmConfFacility_Type(Integer32):
    """Custom type alarmConfFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_AlarmConfFacility_Type.__name__ = "Integer32"
_AlarmConfFacility_Object = MibTableColumn
alarmConfFacility = _AlarmConfFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2, 1, 2),
    _AlarmConfFacility_Type()
)
alarmConfFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfFacility.setStatus("current")
_AlarmConfTarget_Type = Integer32
_AlarmConfTarget_Object = MibTableColumn
alarmConfTarget = _AlarmConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2, 1, 3),
    _AlarmConfTarget_Type()
)
alarmConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfTarget.setStatus("current")


class _AlarmConfSeverity_Type(Integer32):
    """Custom type alarmConfSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_AlarmConfSeverity_Type.__name__ = "Integer32"
_AlarmConfSeverity_Object = MibTableColumn
alarmConfSeverity = _AlarmConfSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2, 1, 4),
    _AlarmConfSeverity_Type()
)
alarmConfSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfSeverity.setStatus("current")


class _AlarmConfClearable_Type(Integer32):
    """Custom type alarmConfClearable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearable", 1),
          ("unclearable", 2))
    )


_AlarmConfClearable_Type.__name__ = "Integer32"
_AlarmConfClearable_Object = MibTableColumn
alarmConfClearable = _AlarmConfClearable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 2, 1, 5),
    _AlarmConfClearable_Type()
)
alarmConfClearable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfClearable.setStatus("current")
_AlarmCurrTable_Object = MibTable
alarmCurrTable = _AlarmCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3)
)
if mibBuilder.loadTexts:
    alarmCurrTable.setStatus("current")
_AlarmCurrEntry_Object = MibTableRow
alarmCurrEntry = _AlarmCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1)
)
alarmCurrEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "alarmCurrIndex"),
)
if mibBuilder.loadTexts:
    alarmCurrEntry.setStatus("current")
_AlarmCurrIndex_Type = Integer32
_AlarmCurrIndex_Object = MibTableColumn
alarmCurrIndex = _AlarmCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 1),
    _AlarmCurrIndex_Type()
)
alarmCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrIndex.setStatus("current")
_AlarmCurrOccurTime_Type = TimeTicks
_AlarmCurrOccurTime_Object = MibTableColumn
alarmCurrOccurTime = _AlarmCurrOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 2),
    _AlarmCurrOccurTime_Type()
)
alarmCurrOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrOccurTime.setStatus("current")
_AlarmCurrTrapOid_Type = ObjectIdentifier
_AlarmCurrTrapOid_Object = MibTableColumn
alarmCurrTrapOid = _AlarmCurrTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 3),
    _AlarmCurrTrapOid_Type()
)
alarmCurrTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTrapOid.setStatus("current")
_AlarmCurrParam1_Type = Integer32
_AlarmCurrParam1_Object = MibTableColumn
alarmCurrParam1 = _AlarmCurrParam1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 4),
    _AlarmCurrParam1_Type()
)
alarmCurrParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam1.setStatus("current")
_AlarmCurrParam2_Type = Integer32
_AlarmCurrParam2_Object = MibTableColumn
alarmCurrParam2 = _AlarmCurrParam2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 5),
    _AlarmCurrParam2_Type()
)
alarmCurrParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam2.setStatus("current")
_AlarmCurrParam3_Type = Integer32
_AlarmCurrParam3_Object = MibTableColumn
alarmCurrParam3 = _AlarmCurrParam3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 6),
    _AlarmCurrParam3_Type()
)
alarmCurrParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam3.setStatus("current")
_AlarmCurrParam4_Type = Integer32
_AlarmCurrParam4_Object = MibTableColumn
alarmCurrParam4 = _AlarmCurrParam4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 7),
    _AlarmCurrParam4_Type()
)
alarmCurrParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam4.setStatus("current")
_AlarmCurrParam5_Type = Integer32
_AlarmCurrParam5_Object = MibTableColumn
alarmCurrParam5 = _AlarmCurrParam5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 8),
    _AlarmCurrParam5_Type()
)
alarmCurrParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam5.setStatus("current")
_AlarmCurrParam6_Type = Integer32
_AlarmCurrParam6_Object = MibTableColumn
alarmCurrParam6 = _AlarmCurrParam6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 9),
    _AlarmCurrParam6_Type()
)
alarmCurrParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam6.setStatus("current")
_AlarmCurrParam7_Type = Integer32
_AlarmCurrParam7_Object = MibTableColumn
alarmCurrParam7 = _AlarmCurrParam7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 10),
    _AlarmCurrParam7_Type()
)
alarmCurrParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam7.setStatus("current")
_AlarmCurrParam8_Type = Integer32
_AlarmCurrParam8_Object = MibTableColumn
alarmCurrParam8 = _AlarmCurrParam8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 11),
    _AlarmCurrParam8_Type()
)
alarmCurrParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam8.setStatus("current")
_AlarmCurrTimeDescr_Type = DisplayString
_AlarmCurrTimeDescr_Object = MibTableColumn
alarmCurrTimeDescr = _AlarmCurrTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 12),
    _AlarmCurrTimeDescr_Type()
)
alarmCurrTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTimeDescr.setStatus("current")


class _AlarmCurrSeverity_Type(Integer32):
    """Custom type alarmCurrSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_AlarmCurrSeverity_Type.__name__ = "Integer32"
_AlarmCurrSeverity_Object = MibTableColumn
alarmCurrSeverity = _AlarmCurrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 13),
    _AlarmCurrSeverity_Type()
)
alarmCurrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrSeverity.setStatus("current")
_AlarmCurrDescr_Type = DisplayString
_AlarmCurrDescr_Object = MibTableColumn
alarmCurrDescr = _AlarmCurrDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 3, 1, 14),
    _AlarmCurrDescr_Type()
)
alarmCurrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrDescr.setStatus("current")
_AlarmSeverityPortTable_Object = MibTable
alarmSeverityPortTable = _AlarmSeverityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 4)
)
if mibBuilder.loadTexts:
    alarmSeverityPortTable.setStatus("current")
_AlarmSeverityPortEntry_Object = MibTableRow
alarmSeverityPortEntry = _AlarmSeverityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 4, 1)
)
alarmSeverityPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alarmSeverityPortEntry.setStatus("current")


class _SeverityThresh_Type(Integer32):
    """Custom type severityThresh based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_SeverityThresh_Type.__name__ = "Integer32"
_SeverityThresh_Object = MibTableColumn
severityThresh = _SeverityThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 2, 4, 1, 1),
    _SeverityThresh_Type()
)
severityThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityThresh.setStatus("current")
_Diagnostic_ObjectIdentity = ObjectIdentity
diagnostic = _Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4)
)
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3, 3),
    _SeltStatus_Type()
)
seltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltStatus.setStatus("current")


class _SeltCableType_Type(Integer32):
    """Custom type seltCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("awg24", 1),
          ("awg26", 2))
    )


_SeltCableType_Type.__name__ = "Integer32"
_SeltCableType_Object = MibScalar
seltCableType = _SeltCableType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3, 5),
    _SeltLoopEstimateLengthFt_Type()
)
seltLoopEstimateLengthFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setUnits("feet")
_SeltLoopEstimateLengthMeter_Type = Integer32
_SeltLoopEstimateLengthMeter_Object = MibScalar
seltLoopEstimateLengthMeter = _SeltLoopEstimateLengthMeter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 3, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")
_Ldm_ObjectIdentity = ObjectIdentity
ldm = _Ldm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4)
)
_LdmTarget_Type = Integer32
_LdmTarget_Object = MibScalar
ldmTarget = _LdmTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 1),
    _LdmTarget_Type()
)
ldmTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldmTarget.setStatus("current")
_LdmOps_Type = Integer32
_LdmOps_Object = MibScalar
ldmOps = _LdmOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 2),
    _LdmOps_Type()
)
ldmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldmOps.setStatus("current")
_LdmStatus_Type = DisplayString
_LdmStatus_Object = MibScalar
ldmStatus = _LdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 3),
    _LdmStatus_Type()
)
ldmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmStatus.setStatus("current")
_LdmXtucLoopAttenuation_Type = Integer32
_LdmXtucLoopAttenuation_Object = MibScalar
ldmXtucLoopAttenuation = _LdmXtucLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 4),
    _LdmXtucLoopAttenuation_Type()
)
ldmXtucLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucLoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucLoopAttenuation.setUnits("tenth dB")
_LdmXtucSignalAttenuation_Type = Integer32
_LdmXtucSignalAttenuation_Object = MibScalar
ldmXtucSignalAttenuation = _LdmXtucSignalAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 5),
    _LdmXtucSignalAttenuation_Type()
)
ldmXtucSignalAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSignalAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucSignalAttenuation.setUnits("tenth dB")
_LdmXtucSignalMargin_Type = Integer32
_LdmXtucSignalMargin_Object = MibScalar
ldmXtucSignalMargin = _LdmXtucSignalMargin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 6),
    _LdmXtucSignalMargin_Type()
)
ldmXtucSignalMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSignalMargin.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucSignalMargin.setUnits("tenth dB")
_LdmXtucAggregateTxPower_Type = Integer32
_LdmXtucAggregateTxPower_Object = MibScalar
ldmXtucAggregateTxPower = _LdmXtucAggregateTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 7),
    _LdmXtucAggregateTxPower_Type()
)
ldmXtucAggregateTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucAggregateTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucAggregateTxPower.setUnits("tenth dB")
_LdmXtucAttainableBitRate_Type = Unsigned32
_LdmXtucAttainableBitRate_Object = MibScalar
ldmXtucAttainableBitRate = _LdmXtucAttainableBitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 8),
    _LdmXtucAttainableBitRate_Type()
)
ldmXtucAttainableBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucAttainableBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucAttainableBitRate.setUnits("bits per second")
_LdmXturLoopAttenuation_Type = Integer32
_LdmXturLoopAttenuation_Object = MibScalar
ldmXturLoopAttenuation = _LdmXturLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 9),
    _LdmXturLoopAttenuation_Type()
)
ldmXturLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturLoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturLoopAttenuation.setUnits("tenth dB")
_LdmXturSignalAttenuation_Type = Integer32
_LdmXturSignalAttenuation_Object = MibScalar
ldmXturSignalAttenuation = _LdmXturSignalAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 10),
    _LdmXturSignalAttenuation_Type()
)
ldmXturSignalAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSignalAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturSignalAttenuation.setUnits("tenth dB")
_LdmXturSignalMargin_Type = Integer32
_LdmXturSignalMargin_Object = MibScalar
ldmXturSignalMargin = _LdmXturSignalMargin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 11),
    _LdmXturSignalMargin_Type()
)
ldmXturSignalMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSignalMargin.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturSignalMargin.setUnits("tenth dB")
_LdmXturAggregateTxPower_Type = Integer32
_LdmXturAggregateTxPower_Object = MibScalar
ldmXturAggregateTxPower = _LdmXturAggregateTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 12),
    _LdmXturAggregateTxPower_Type()
)
ldmXturAggregateTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturAggregateTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturAggregateTxPower.setUnits("tenth dB")
_LdmXturAttainableBitRate_Type = Unsigned32
_LdmXturAttainableBitRate_Object = MibScalar
ldmXturAttainableBitRate = _LdmXturAttainableBitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 13),
    _LdmXturAttainableBitRate_Type()
)
ldmXturAttainableBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturAttainableBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturAttainableBitRate.setUnits("bits per second")
_LdmXtucNumOfSubcarriersPerPort_Type = Integer32
_LdmXtucNumOfSubcarriersPerPort_Object = MibScalar
ldmXtucNumOfSubcarriersPerPort = _LdmXtucNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 14),
    _LdmXtucNumOfSubcarriersPerPort_Type()
)
ldmXtucNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucNumOfSubcarriersPerPort.setStatus("current")
_LdmXturNumOfSubcarriersPerPort_Type = Integer32
_LdmXturNumOfSubcarriersPerPort_Object = MibScalar
ldmXturNumOfSubcarriersPerPort = _LdmXturNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 15),
    _LdmXturNumOfSubcarriersPerPort_Type()
)
ldmXturNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturNumOfSubcarriersPerPort.setStatus("current")
_LdmXtucHlinScale_Type = Integer32
_LdmXtucHlinScale_Object = MibScalar
ldmXtucHlinScale = _LdmXtucHlinScale_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 16),
    _LdmXtucHlinScale_Type()
)
ldmXtucHlinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinScale.setStatus("current")
_LdmXtucHlinReal1_Type = OctetString
_LdmXtucHlinReal1_Object = MibScalar
ldmXtucHlinReal1 = _LdmXtucHlinReal1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 17),
    _LdmXtucHlinReal1_Type()
)
ldmXtucHlinReal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinReal1.setStatus("current")
_LdmXtucHlinReal2_Type = OctetString
_LdmXtucHlinReal2_Object = MibScalar
ldmXtucHlinReal2 = _LdmXtucHlinReal2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 18),
    _LdmXtucHlinReal2_Type()
)
ldmXtucHlinReal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinReal2.setStatus("current")
_LdmXtucHlinImage1_Type = OctetString
_LdmXtucHlinImage1_Object = MibScalar
ldmXtucHlinImage1 = _LdmXtucHlinImage1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 19),
    _LdmXtucHlinImage1_Type()
)
ldmXtucHlinImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinImage1.setStatus("current")
_LdmXtucHlinImage2_Type = OctetString
_LdmXtucHlinImage2_Object = MibScalar
ldmXtucHlinImage2 = _LdmXtucHlinImage2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 20),
    _LdmXtucHlinImage2_Type()
)
ldmXtucHlinImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinImage2.setStatus("current")
_LdmXtucHlog1_Type = OctetString
_LdmXtucHlog1_Object = MibScalar
ldmXtucHlog1 = _LdmXtucHlog1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 21),
    _LdmXtucHlog1_Type()
)
ldmXtucHlog1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlog1.setStatus("current")
_LdmXtucHlog2_Type = OctetString
_LdmXtucHlog2_Object = MibScalar
ldmXtucHlog2 = _LdmXtucHlog2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 22),
    _LdmXtucHlog2_Type()
)
ldmXtucHlog2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlog2.setStatus("current")
_LdmXtucQln1_Type = OctetString
_LdmXtucQln1_Object = MibScalar
ldmXtucQln1 = _LdmXtucQln1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 23),
    _LdmXtucQln1_Type()
)
ldmXtucQln1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucQln1.setStatus("current")
_LdmXtucQln2_Type = OctetString
_LdmXtucQln2_Object = MibScalar
ldmXtucQln2 = _LdmXtucQln2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 24),
    _LdmXtucQln2_Type()
)
ldmXtucQln2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucQln2.setStatus("current")
_LdmXtucSnr1_Type = OctetString
_LdmXtucSnr1_Object = MibScalar
ldmXtucSnr1 = _LdmXtucSnr1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 25),
    _LdmXtucSnr1_Type()
)
ldmXtucSnr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSnr1.setStatus("current")
_LdmXtucSnr2_Type = OctetString
_LdmXtucSnr2_Object = MibScalar
ldmXtucSnr2 = _LdmXtucSnr2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 26),
    _LdmXtucSnr2_Type()
)
ldmXtucSnr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSnr2.setStatus("current")
_LdmXturHlinScale_Type = Integer32
_LdmXturHlinScale_Object = MibScalar
ldmXturHlinScale = _LdmXturHlinScale_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 27),
    _LdmXturHlinScale_Type()
)
ldmXturHlinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlinScale.setStatus("current")
_LdmXturHlinReal_Type = OctetString
_LdmXturHlinReal_Object = MibScalar
ldmXturHlinReal = _LdmXturHlinReal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 28),
    _LdmXturHlinReal_Type()
)
ldmXturHlinReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlinReal.setStatus("current")
_LdmXturHlinImage_Type = OctetString
_LdmXturHlinImage_Object = MibScalar
ldmXturHlinImage = _LdmXturHlinImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 29),
    _LdmXturHlinImage_Type()
)
ldmXturHlinImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlinImage.setStatus("current")
_LdmXturHlog_Type = OctetString
_LdmXturHlog_Object = MibScalar
ldmXturHlog = _LdmXturHlog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 30),
    _LdmXturHlog_Type()
)
ldmXturHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlog.setStatus("current")
_LdmXturQln_Type = OctetString
_LdmXturQln_Object = MibScalar
ldmXturQln = _LdmXturQln_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 31),
    _LdmXturQln_Type()
)
ldmXturQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturQln.setStatus("current")
_LdmXturSnr_Type = OctetString
_LdmXturSnr_Object = MibScalar
ldmXturSnr = _LdmXturSnr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 4, 4, 32),
    _LdmXturSnr_Type()
)
ldmXturSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSnr.setStatus("current")
_Ipconf_ObjectIdentity = ObjectIdentity
ipconf = _Ipconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5)
)
_StaticRoute_ObjectIdentity = ObjectIdentity
staticRoute = _StaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1)
)
_MaxNumOfStaticRoutes_Type = Integer32
_MaxNumOfStaticRoutes_Object = MibScalar
maxNumOfStaticRoutes = _MaxNumOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 1),
    _MaxNumOfStaticRoutes_Type()
)
maxNumOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfStaticRoutes.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1)
)
staticRouteEntry.setIndexNames(
    (1, "ZYXEL-VES1608FE53A-MIB", "staticRouteName"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")


class _StaticRouteName_Type(DisplayString):
    """Custom type staticRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_StaticRouteName_Type.__name__ = "DisplayString"
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("current")
_StaticRouteDest_Type = IpAddress
_StaticRouteDest_Object = MibTableColumn
staticRouteDest = _StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1, 2),
    _StaticRouteDest_Type()
)
staticRouteDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteDest.setStatus("current")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("current")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("current")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("current")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 1, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 2)
)
_InbandIp_Type = IpAddress
_InbandIp_Object = MibScalar
inbandIp = _InbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 2, 1),
    _InbandIp_Type()
)
inbandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIp.setStatus("current")
_InbandIpSubnetMask_Type = IpAddress
_InbandIpSubnetMask_Object = MibScalar
inbandIpSubnetMask = _InbandIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 2, 2),
    _InbandIpSubnetMask_Type()
)
inbandIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpSubnetMask.setStatus("current")
_OutbandIp_Type = IpAddress
_OutbandIp_Object = MibScalar
outbandIp = _OutbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 2, 3),
    _OutbandIp_Type()
)
outbandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbandIp.setStatus("current")
_OutbandIpSubnetMask_Type = IpAddress
_OutbandIpSubnetMask_Object = MibScalar
outbandIpSubnetMask = _OutbandIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 2, 4),
    _OutbandIpSubnetMask_Type()
)
outbandIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbandIpSubnetMask.setStatus("current")
_DefaultGatewayIp_Type = IpAddress
_DefaultGatewayIp_Object = MibScalar
defaultGatewayIp = _DefaultGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 5, 2, 5),
    _DefaultGatewayIp_Type()
)
defaultGatewayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGatewayIp.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7)
)


class _IgmpEnable_Type(Integer32):
    """Custom type igmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableProxy", 1),
          ("enableSnooping", 2),
          ("disable", 3))
    )


_IgmpEnable_Type.__name__ = "Integer32"
_IgmpEnable_Object = MibScalar
igmpEnable = _IgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 1),
    _IgmpEnable_Type()
)
igmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnable.setStatus("current")
_StaticMulticast_ObjectIdentity = ObjectIdentity
staticMulticast = _StaticMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2)
)
_MaxNumberOfMcastGroups_Type = Integer32
_MaxNumberOfMcastGroups_Object = MibScalar
maxNumberOfMcastGroups = _MaxNumberOfMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 1),
    _MaxNumberOfMcastGroups_Type()
)
maxNumberOfMcastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMcastGroups.setStatus("current")
_MulticastGroupTable_Object = MibTable
multicastGroupTable = _MulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 2)
)
if mibBuilder.loadTexts:
    multicastGroupTable.setStatus("current")
_MulticastGroupEntry_Object = MibTableRow
multicastGroupEntry = _MulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 2, 1)
)
multicastGroupEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "multicastGroupVid"),
    (0, "ZYXEL-VES1608FE53A-MIB", "multicastGroupMacAddr"),
)
if mibBuilder.loadTexts:
    multicastGroupEntry.setStatus("current")
_MulticastGroupVid_Type = Integer32
_MulticastGroupVid_Object = MibTableColumn
multicastGroupVid = _MulticastGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 2, 1, 1),
    _MulticastGroupVid_Type()
)
multicastGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGroupVid.setStatus("current")
_MulticastGroupMacAddr_Type = PhysAddress
_MulticastGroupMacAddr_Object = MibTableColumn
multicastGroupMacAddr = _MulticastGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 2, 1, 2),
    _MulticastGroupMacAddr_Type()
)
multicastGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGroupMacAddr.setStatus("current")
_MulticastGroupPorts_Type = PortList
_MulticastGroupPorts_Object = MibTableColumn
multicastGroupPorts = _MulticastGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 2, 1, 3),
    _MulticastGroupPorts_Type()
)
multicastGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastGroupPorts.setStatus("current")
_MulticastGroupRowStatus_Type = RowStatus
_MulticastGroupRowStatus_Object = MibTableColumn
multicastGroupRowStatus = _MulticastGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 2, 2, 1, 4),
    _MulticastGroupRowStatus_Type()
)
multicastGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastGroupRowStatus.setStatus("current")
_IgmpFilter_ObjectIdentity = ObjectIdentity
igmpFilter = _IgmpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3)
)
_MaxNumOfIgmpFilters_Type = Integer32
_MaxNumOfIgmpFilters_Object = MibScalar
maxNumOfIgmpFilters = _MaxNumOfIgmpFilters_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 1),
    _MaxNumOfIgmpFilters_Type()
)
maxNumOfIgmpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfIgmpFilters.setStatus("current")
_IgmpFilterTable_Object = MibTable
igmpFilterTable = _IgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2)
)
if mibBuilder.loadTexts:
    igmpFilterTable.setStatus("current")
_IgmpFilterEntry_Object = MibTableRow
igmpFilterEntry = _IgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2, 1)
)
igmpFilterEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpFilterName"),
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpFilterIndex"),
)
if mibBuilder.loadTexts:
    igmpFilterEntry.setStatus("current")


class _IgmpFilterName_Type(DisplayString):
    """Custom type igmpFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpFilterName_Type.__name__ = "DisplayString"
_IgmpFilterName_Object = MibTableColumn
igmpFilterName = _IgmpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2, 1, 1),
    _IgmpFilterName_Type()
)
igmpFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilterName.setStatus("current")
_IgmpFilterIndex_Type = Integer32
_IgmpFilterIndex_Object = MibTableColumn
igmpFilterIndex = _IgmpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2, 1, 2),
    _IgmpFilterIndex_Type()
)
igmpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilterIndex.setStatus("current")
_IgmpFilterStartIp_Type = IpAddress
_IgmpFilterStartIp_Object = MibTableColumn
igmpFilterStartIp = _IgmpFilterStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2, 1, 3),
    _IgmpFilterStartIp_Type()
)
igmpFilterStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterStartIp.setStatus("current")
_IgmpFilterEndIp_Type = IpAddress
_IgmpFilterEndIp_Object = MibTableColumn
igmpFilterEndIp = _IgmpFilterEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2, 1, 4),
    _IgmpFilterEndIp_Type()
)
igmpFilterEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterEndIp.setStatus("current")
_IgmpFilterRowStatus_Type = RowStatus
_IgmpFilterRowStatus_Object = MibTableColumn
igmpFilterRowStatus = _IgmpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 2, 1, 5),
    _IgmpFilterRowStatus_Type()
)
igmpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterRowStatus.setStatus("current")
_IgmpFilterPortTable_Object = MibTable
igmpFilterPortTable = _IgmpFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 3)
)
if mibBuilder.loadTexts:
    igmpFilterPortTable.setStatus("current")
_IgmpFilterPortEntry_Object = MibTableRow
igmpFilterPortEntry = _IgmpFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 3, 1)
)
igmpFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpFilterPortEntry.setStatus("current")


class _IgmpFilterPortFilterName_Type(DisplayString):
    """Custom type igmpFilterPortFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpFilterPortFilterName_Type.__name__ = "DisplayString"
_IgmpFilterPortFilterName_Object = MibTableColumn
igmpFilterPortFilterName = _IgmpFilterPortFilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 3, 3, 1, 1),
    _IgmpFilterPortFilterName_Type()
)
igmpFilterPortFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpFilterPortFilterName.setStatus("current")
_McastBandwidth_ObjectIdentity = ObjectIdentity
mcastBandwidth = _McastBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4)
)


class _McastDefaultBandwidth_Type(Integer32):
    """Custom type mcastDefaultBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_McastDefaultBandwidth_Type.__name__ = "Integer32"
_McastDefaultBandwidth_Object = MibScalar
mcastDefaultBandwidth = _McastDefaultBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 1),
    _McastDefaultBandwidth_Type()
)
mcastDefaultBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastDefaultBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastDefaultBandwidth.setUnits("Kbps")
_MaxNumOfMcastBw_Type = Integer32
_MaxNumOfMcastBw_Object = MibScalar
maxNumOfMcastBw = _MaxNumOfMcastBw_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 2),
    _MaxNumOfMcastBw_Type()
)
maxNumOfMcastBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMcastBw.setStatus("current")
_McastBwTable_Object = MibTable
mcastBwTable = _McastBwTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3)
)
if mibBuilder.loadTexts:
    mcastBwTable.setStatus("current")
_McastBwEntry_Object = MibTableRow
mcastBwEntry = _McastBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3, 1)
)
mcastBwEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "mcastBwIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "mcastBwStartIp"),
    (0, "ZYXEL-VES1608FE53A-MIB", "mcastBwEndIp"),
)
if mibBuilder.loadTexts:
    mcastBwEntry.setStatus("current")
_McastBwIndex_Type = Integer32
_McastBwIndex_Object = MibTableColumn
mcastBwIndex = _McastBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3, 1, 1),
    _McastBwIndex_Type()
)
mcastBwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwIndex.setStatus("current")
_McastBwStartIp_Type = IpAddress
_McastBwStartIp_Object = MibTableColumn
mcastBwStartIp = _McastBwStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3, 1, 2),
    _McastBwStartIp_Type()
)
mcastBwStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwStartIp.setStatus("current")
_McastBwEndIp_Type = IpAddress
_McastBwEndIp_Object = MibTableColumn
mcastBwEndIp = _McastBwEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3, 1, 3),
    _McastBwEndIp_Type()
)
mcastBwEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwEndIp.setStatus("current")
_McastBwBandwidth_Type = Integer32
_McastBwBandwidth_Object = MibTableColumn
mcastBwBandwidth = _McastBwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3, 1, 4),
    _McastBwBandwidth_Type()
)
mcastBwBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwBandwidth.setUnits("Kbps")
_McastBwRowStatus_Type = RowStatus
_McastBwRowStatus_Object = MibTableColumn
mcastBwRowStatus = _McastBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 3, 1, 5),
    _McastBwRowStatus_Type()
)
mcastBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwRowStatus.setStatus("current")
_McastBwPortTable_Object = MibTable
mcastBwPortTable = _McastBwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mcastBwPortTable.setStatus("current")
_McastBwPortEntry_Object = MibTableRow
mcastBwPortEntry = _McastBwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 4, 1)
)
mcastBwPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mcastBwPortEntry.setStatus("current")


class _McastBwPortEnable_Type(Integer32):
    """Custom type mcastBwPortEnable based on Integer32"""
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


_McastBwPortEnable_Type.__name__ = "Integer32"
_McastBwPortEnable_Object = MibTableColumn
mcastBwPortEnable = _McastBwPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 4, 1, 1),
    _McastBwPortEnable_Type()
)
mcastBwPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortEnable.setStatus("current")
_McastBwPortBandwidth_Type = Integer32
_McastBwPortBandwidth_Object = MibTableColumn
mcastBwPortBandwidth = _McastBwPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 4, 4, 1, 2),
    _McastBwPortBandwidth_Type()
)
mcastBwPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setUnits("Kbps")
_IgmpCount_ObjectIdentity = ObjectIdentity
igmpCount = _IgmpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 5)
)
_IgmpCountPortTable_Object = MibTable
igmpCountPortTable = _IgmpCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 5, 1)
)
if mibBuilder.loadTexts:
    igmpCountPortTable.setStatus("current")
_IgmpCountPortEntry_Object = MibTableRow
igmpCountPortEntry = _IgmpCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 5, 1, 1)
)
igmpCountPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpCountPortEntry.setStatus("current")


class _IgmpCountPortEnable_Type(Integer32):
    """Custom type igmpCountPortEnable based on Integer32"""
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


_IgmpCountPortEnable_Type.__name__ = "Integer32"
_IgmpCountPortEnable_Object = MibTableColumn
igmpCountPortEnable = _IgmpCountPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 5, 1, 1, 1),
    _IgmpCountPortEnable_Type()
)
igmpCountPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortEnable.setStatus("current")


class _IgmpCountPortLimit_Type(Integer32):
    """Custom type igmpCountPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IgmpCountPortLimit_Type.__name__ = "Integer32"
_IgmpCountPortLimit_Object = MibTableColumn
igmpCountPortLimit = _IgmpCountPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 5, 1, 1, 2),
    _IgmpCountPortLimit_Type()
)
igmpCountPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortLimit.setStatus("current")
_Mvlan_ObjectIdentity = ObjectIdentity
mvlan = _Mvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6)
)
_MaxNumOfMvlan_Type = Integer32
_MaxNumOfMvlan_Object = MibScalar
maxNumOfMvlan = _MaxNumOfMvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 1),
    _MaxNumOfMvlan_Type()
)
maxNumOfMvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMvlan.setStatus("current")
_MvlanTable_Object = MibTable
mvlanTable = _MvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2)
)
if mibBuilder.loadTexts:
    mvlanTable.setStatus("current")
_MvlanEntry_Object = MibTableRow
mvlanEntry = _MvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2, 1)
)
mvlanEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "mvlanIndex"),
)
if mibBuilder.loadTexts:
    mvlanEntry.setStatus("current")
_MvlanIndex_Type = VlanIndex
_MvlanIndex_Object = MibTableColumn
mvlanIndex = _MvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2, 1, 1),
    _MvlanIndex_Type()
)
mvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanIndex.setStatus("current")


class _MvlanName_Type(DisplayString):
    """Custom type mvlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MvlanName_Type.__name__ = "DisplayString"
_MvlanName_Object = MibTableColumn
mvlanName = _MvlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2, 1, 2),
    _MvlanName_Type()
)
mvlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanName.setStatus("current")
_MvlanEgressPorts_Type = PortList
_MvlanEgressPorts_Object = MibTableColumn
mvlanEgressPorts = _MvlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2, 1, 3),
    _MvlanEgressPorts_Type()
)
mvlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanEgressPorts.setStatus("current")
_MvlanUntaggedPorts_Type = PortList
_MvlanUntaggedPorts_Object = MibTableColumn
mvlanUntaggedPorts = _MvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2, 1, 4),
    _MvlanUntaggedPorts_Type()
)
mvlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanUntaggedPorts.setStatus("current")
_MvlanRowStatus_Type = RowStatus
_MvlanRowStatus_Object = MibTableColumn
mvlanRowStatus = _MvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 2, 1, 5),
    _MvlanRowStatus_Type()
)
mvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanRowStatus.setStatus("current")
_MvlanTranslateTable_Object = MibTable
mvlanTranslateTable = _MvlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 3)
)
if mibBuilder.loadTexts:
    mvlanTranslateTable.setStatus("current")
_MvlanTranslateEntry_Object = MibTableRow
mvlanTranslateEntry = _MvlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 3, 1)
)
mvlanTranslateEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "mvlanTranslateIndex"),
)
if mibBuilder.loadTexts:
    mvlanTranslateEntry.setStatus("current")
_MvlanTranslateIndex_Type = Integer32
_MvlanTranslateIndex_Object = MibTableColumn
mvlanTranslateIndex = _MvlanTranslateIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 3, 1, 1),
    _MvlanTranslateIndex_Type()
)
mvlanTranslateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanTranslateIndex.setStatus("current")
_MvlanTranslateStartIp_Type = IpAddress
_MvlanTranslateStartIp_Object = MibTableColumn
mvlanTranslateStartIp = _MvlanTranslateStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 3, 1, 2),
    _MvlanTranslateStartIp_Type()
)
mvlanTranslateStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateStartIp.setStatus("current")
_MvlanTranslateEndIp_Type = IpAddress
_MvlanTranslateEndIp_Object = MibTableColumn
mvlanTranslateEndIp = _MvlanTranslateEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 6, 3, 1, 3),
    _MvlanTranslateEndIp_Type()
)
mvlanTranslateEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateEndIp.setStatus("current")
_QueryVid_ObjectIdentity = ObjectIdentity
queryVid = _QueryVid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7)
)
_MaxNumOfQryVid_Type = Integer32
_MaxNumOfQryVid_Object = MibScalar
maxNumOfQryVid = _MaxNumOfQryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 1),
    _MaxNumOfQryVid_Type()
)
maxNumOfQryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfQryVid.setStatus("current")
_QryVidConfTable_Object = MibTable
qryVidConfTable = _QryVidConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 2)
)
if mibBuilder.loadTexts:
    qryVidConfTable.setStatus("current")
_QryVidConfEntry_Object = MibTableRow
qryVidConfEntry = _QryVidConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 2, 1)
)
qryVidConfEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidConfEntry.setStatus("current")
_QryVid_Type = Integer32
_QryVid_Object = MibTableColumn
qryVid = _QryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 2, 1, 1),
    _QryVid_Type()
)
qryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVid.setStatus("current")
_QryVidRowStatus_Type = RowStatus
_QryVidRowStatus_Object = MibTableColumn
qryVidRowStatus = _QryVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 2, 1, 2),
    _QryVidRowStatus_Type()
)
qryVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qryVidRowStatus.setStatus("current")
_QryVidStatusTable_Object = MibTable
qryVidStatusTable = _QryVidStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 3)
)
if mibBuilder.loadTexts:
    qryVidStatusTable.setStatus("current")
_QryVidStatusEntry_Object = MibTableRow
qryVidStatusEntry = _QryVidStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 3, 1)
)
qryVidStatusEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidStatusEntry.setStatus("current")


class _QryVidType_Type(Integer32):
    """Custom type qryVidType based on Integer32"""
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


_QryVidType_Type.__name__ = "Integer32"
_QryVidType_Object = MibTableColumn
qryVidType = _QryVidType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 7, 3, 1, 1),
    _QryVidType_Type()
)
qryVidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVidType.setStatus("current")


class _IgmpVersion_Type(Integer32):
    """Custom type igmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2))
    )


_IgmpVersion_Type.__name__ = "Integer32"
_IgmpVersion_Object = MibScalar
igmpVersion = _IgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 7, 9),
    _IgmpVersion_Type()
)
igmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVersion.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8)
)
_SubrPortTable_Object = MibTable
subrPortTable = _SubrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 1)
)
if mibBuilder.loadTexts:
    subrPortTable.setStatus("current")
_SubrPortEntry_Object = MibTableRow
subrPortEntry = _SubrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 1, 1)
)
subrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subrPortEntry.setStatus("current")


class _SubrPortName_Type(DisplayString):
    """Custom type subrPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SubrPortName_Type.__name__ = "DisplayString"
_SubrPortName_Object = MibTableColumn
subrPortName = _SubrPortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 1, 1, 1),
    _SubrPortName_Type()
)
subrPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortName.setStatus("current")


class _SubrPortTel_Type(DisplayString):
    """Custom type subrPortTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SubrPortTel_Type.__name__ = "DisplayString"
_SubrPortTel_Object = MibTableColumn
subrPortTel = _SubrPortTel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 1, 1, 2),
    _SubrPortTel_Type()
)
subrPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortTel.setStatus("current")
_VdslPort_ObjectIdentity = ObjectIdentity
vdslPort = _VdslPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3)
)
_VdslLineConfTable_Object = MibTable
vdslLineConfTable = _VdslLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1)
)
if mibBuilder.loadTexts:
    vdslLineConfTable.setStatus("current")
_VdslLineConfEntry_Object = MibTableRow
vdslLineConfEntry = _VdslLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1)
)
vdslLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslLineConfEntry.setStatus("current")


class _VdslLineConfUpbo_Type(Integer32):
    """Custom type vdslLineConfUpbo based on Integer32"""
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


_VdslLineConfUpbo_Type.__name__ = "Integer32"
_VdslLineConfUpbo_Object = MibTableColumn
vdslLineConfUpbo = _VdslLineConfUpbo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 1),
    _VdslLineConfUpbo_Type()
)
vdslLineConfUpbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpbo.setStatus("current")


class _VdslLineConfVdslProfile_Type(Integer32):
    """Custom type vdslLineConfVdslProfile based on Integer32"""
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
        *(("vdsl_8a", 1),
          ("vdsl_8b", 2),
          ("vdsl_8c", 3),
          ("vdsl_8d", 4),
          ("vdsl_12a", 5),
          ("vdsl_12b", 6),
          ("vdsl_17a", 7),
          ("auto", 8),
          ("adsl2plus", 9),
          ("vdsl2", 10))
    )


_VdslLineConfVdslProfile_Type.__name__ = "Integer32"
_VdslLineConfVdslProfile_Object = MibTableColumn
vdslLineConfVdslProfile = _VdslLineConfVdslProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 2),
    _VdslLineConfVdslProfile_Type()
)
vdslLineConfVdslProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfVdslProfile.setStatus("current")


class _VdslLineConfRfiBand_Type(Integer32):
    """Custom type vdslLineConfRfiBand based on Integer32"""
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
        *(("disable", 1),
          ("ansi", 2),
          ("etsi", 3),
          ("custom", 4))
    )


_VdslLineConfRfiBand_Type.__name__ = "Integer32"
_VdslLineConfRfiBand_Object = MibTableColumn
vdslLineConfRfiBand = _VdslLineConfRfiBand_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 4),
    _VdslLineConfRfiBand_Type()
)
vdslLineConfRfiBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfRfiBand.setStatus("current")
_VdslLineConfIpqosProfile_Type = DisplayString
_VdslLineConfIpqosProfile_Object = MibTableColumn
vdslLineConfIpqosProfile = _VdslLineConfIpqosProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 5),
    _VdslLineConfIpqosProfile_Type()
)
vdslLineConfIpqosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfIpqosProfile.setStatus("current")


class _VdslLineConfVturInp_Type(Integer32):
    """Custom type vdslLineConfVturInp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslLineConfVturInp_Type.__name__ = "Integer32"
_VdslLineConfVturInp_Object = MibTableColumn
vdslLineConfVturInp = _VdslLineConfVturInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 6),
    _VdslLineConfVturInp_Type()
)
vdslLineConfVturInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfVturInp.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfVturInp.setUnits("0.1 DTM symbol")


class _VdslLineConfVtucInp_Type(Integer32):
    """Custom type vdslLineConfVtucInp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslLineConfVtucInp_Type.__name__ = "Integer32"
_VdslLineConfVtucInp_Object = MibTableColumn
vdslLineConfVtucInp = _VdslLineConfVtucInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 7),
    _VdslLineConfVtucInp_Type()
)
vdslLineConfVtucInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfVtucInp.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfVtucInp.setUnits("0.1 DTM symbol")
_VdslLineConfOptionMask_Type = Integer32
_VdslLineConfOptionMask_Object = MibTableColumn
vdslLineConfOptionMask = _VdslLineConfOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 8),
    _VdslLineConfOptionMask_Type()
)
vdslLineConfOptionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfOptionMask.setStatus("current")


class _VdslLineConfUpboForceLength_Type(Integer32):
    """Custom type vdslLineConfUpboForceLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
    )


_VdslLineConfUpboForceLength_Type.__name__ = "Integer32"
_VdslLineConfUpboForceLength_Object = MibTableColumn
vdslLineConfUpboForceLength = _VdslLineConfUpboForceLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 9),
    _VdslLineConfUpboForceLength_Type()
)
vdslLineConfUpboForceLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpboForceLength.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpboForceLength.setUnits("0.1dB")


class _VdslLineConfPsdShape_Type(Integer32):
    """Custom type vdslLineConfPsdShape based on Integer32"""
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("vdsl2_a_nus0", 1),
          ("vdsl2_a_eu32", 2),
          ("vdsl2_a_eu36", 3),
          ("vdsl2_a_eu40", 4),
          ("vdsl2_a_eu44", 5),
          ("vdsl2_a_eu48", 6),
          ("vdsl2_a_eu52", 7),
          ("vdsl2_a_eu56", 8),
          ("vdsl2_a_eu60", 9),
          ("vdsl2_a_eu64", 10),
          ("vdsl2_a_eu128", 11),
          ("vdsl1_fttex_ansi_m1", 12),
          ("vdsl1_fttex_ansi_m2", 13),
          ("vdsl1_fttcab_ansi_m1", 14),
          ("vdsl1_fttcab_ansi_m2", 15),
          ("vdsl1_fttex_ansi_m1_e", 16),
          ("vdsl1_fttex_ansi_m2_e", 17),
          ("vdsl_fttcab_ansi_m1_e", 18),
          ("vdsl_fttcab_ansi_m2_e", 19),
          ("vdsl2_a_ct", 20),
          ("vdsl2_b8_1", 21),
          ("vdsl2_b8_2", 22),
          ("vdsl2_b8_3", 23),
          ("vdsl2_b8_4", 24),
          ("vdsl2_b8_5", 25),
          ("vdsl2_b8_6", 26),
          ("vdsl2_b8_7", 27),
          ("vdsl2_b8_8", 28),
          ("vdsl2_b8_9", 29),
          ("vdsl2_b8_10", 30),
          ("vdsl2_b8_11", 31),
          ("vdsl2_b8_12", 32),
          ("vdsl2_b8_13", 33),
          ("vdsl2_b8_14", 34),
          ("vdsl2_b8_15", 35),
          ("vdsl2_b8_16", 36),
          ("vdsl2_b7_1", 37),
          ("vdsl2_b7_2", 38),
          ("vdsl2_b7_3", 39),
          ("vdsl2_b7_4", 40),
          ("vdsl2_b7_5", 41),
          ("vdsl2_b7_6", 42),
          ("vdsl2_b7_7", 43),
          ("vdsl2_b7_8", 44),
          ("vdsl2_b7_9", 45),
          ("vdsl2_b7_10", 46),
          ("vdsl2_bt_anfp", 47),
          ("vdsl2_c_138_b", 48),
          ("vdsl2_c_276_b", 49),
          ("vdsl2_c_138_co", 50),
          ("vdsl2_c_276_co", 51))
    )


_VdslLineConfPsdShape_Type.__name__ = "Integer32"
_VdslLineConfPsdShape_Object = MibTableColumn
vdslLineConfPsdShape = _VdslLineConfPsdShape_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 10),
    _VdslLineConfPsdShape_Type()
)
vdslLineConfPsdShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfPsdShape.setStatus("current")


class _VdslLineConfDpbo_Type(Integer32):
    """Custom type vdslLineConfDpbo based on Integer32"""
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


_VdslLineConfDpbo_Type.__name__ = "Integer32"
_VdslLineConfDpbo_Object = MibTableColumn
vdslLineConfDpbo = _VdslLineConfDpbo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 11),
    _VdslLineConfDpbo_Type()
)
vdslLineConfDpbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpbo.setStatus("current")


class _VdslLineConfDpboParamEsel_Type(Integer32):
    """Custom type vdslLineConfDpboParamEsel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_VdslLineConfDpboParamEsel_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEsel_Object = MibTableColumn
vdslLineConfDpboParamEsel = _VdslLineConfDpboParamEsel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 12),
    _VdslLineConfDpboParamEsel_Type()
)
vdslLineConfDpboParamEsel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEsel.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEsel.setUnits("0.5dB")


class _VdslLineConfDpboParamEscma_Type(Integer32):
    """Custom type vdslLineConfDpboParamEscma based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_VdslLineConfDpboParamEscma_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEscma_Object = MibTableColumn
vdslLineConfDpboParamEscma = _VdslLineConfDpboParamEscma_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 13),
    _VdslLineConfDpboParamEscma_Type()
)
vdslLineConfDpboParamEscma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEscma.setStatus("current")


class _VdslLineConfDpboParamEscmb_Type(Integer32):
    """Custom type vdslLineConfDpboParamEscmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_VdslLineConfDpboParamEscmb_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEscmb_Object = MibTableColumn
vdslLineConfDpboParamEscmb = _VdslLineConfDpboParamEscmb_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 14),
    _VdslLineConfDpboParamEscmb_Type()
)
vdslLineConfDpboParamEscmb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEscmb.setStatus("current")


class _VdslLineConfDpboParamEscmc_Type(Integer32):
    """Custom type vdslLineConfDpboParamEscmc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_VdslLineConfDpboParamEscmc_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEscmc_Object = MibTableColumn
vdslLineConfDpboParamEscmc = _VdslLineConfDpboParamEscmc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 15),
    _VdslLineConfDpboParamEscmc_Type()
)
vdslLineConfDpboParamEscmc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEscmc.setStatus("current")


class _VdslLineConfDpboParamMus_Type(Integer32):
    """Custom type vdslLineConfDpboParamMus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineConfDpboParamMus_Type.__name__ = "Integer32"
_VdslLineConfDpboParamMus_Object = MibTableColumn
vdslLineConfDpboParamMus = _VdslLineConfDpboParamMus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 16),
    _VdslLineConfDpboParamMus_Type()
)
vdslLineConfDpboParamMus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamMus.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamMus.setUnits("-0.5 dBm/Hz")


class _VdslLineConfDpboParamFmin_Type(Integer32):
    """Custom type vdslLineConfDpboParamFmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_VdslLineConfDpboParamFmin_Type.__name__ = "Integer32"
_VdslLineConfDpboParamFmin_Object = MibTableColumn
vdslLineConfDpboParamFmin = _VdslLineConfDpboParamFmin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 17),
    _VdslLineConfDpboParamFmin_Type()
)
vdslLineConfDpboParamFmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmin.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmin.setUnits("4.3125kHz")


class _VdslLineConfDpboParamFmax_Type(Integer32):
    """Custom type vdslLineConfDpboParamFmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6956),
    )


_VdslLineConfDpboParamFmax_Type.__name__ = "Integer32"
_VdslLineConfDpboParamFmax_Object = MibTableColumn
vdslLineConfDpboParamFmax = _VdslLineConfDpboParamFmax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 18),
    _VdslLineConfDpboParamFmax_Type()
)
vdslLineConfDpboParamFmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmax.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmax.setUnits("4.3125kHz")


class _VdslLineConfDpboParamPsdId_Type(Integer32):
    """Custom type vdslLineConfDpboParamPsdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("psd_co", 1),
          ("psd_flat", 2),
          ("psd_cab_ansi", 3),
          ("psd_cab_etsi", 4),
          ("psd_exch_etsi", 5),
          ("psd_exch_ansi", 6))
    )


_VdslLineConfDpboParamPsdId_Type.__name__ = "Integer32"
_VdslLineConfDpboParamPsdId_Object = MibTableColumn
vdslLineConfDpboParamPsdId = _VdslLineConfDpboParamPsdId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 19),
    _VdslLineConfDpboParamPsdId_Type()
)
vdslLineConfDpboParamPsdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamPsdId.setStatus("current")


class _VdslLineConfSraMode_Type(Integer32):
    """Custom type vdslLineConfSraMode based on Integer32"""
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


_VdslLineConfSraMode_Type.__name__ = "Integer32"
_VdslLineConfSraMode_Object = MibTableColumn
vdslLineConfSraMode = _VdslLineConfSraMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 1, 1, 20),
    _VdslLineConfSraMode_Type()
)
vdslLineConfSraMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfSraMode.setStatus("current")
_VdslVlan_ObjectIdentity = ObjectIdentity
vdslVlan = _VdslVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2)
)
_VdslPortConfTable_Object = MibTable
vdslPortConfTable = _VdslPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vdslPortConfTable.setStatus("current")
_VdslPortConfEntry_Object = MibTableRow
vdslPortConfEntry = _VdslPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1)
)
vdslPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslPortConfEntry.setStatus("current")


class _VdslPortConfTlsEnable_Type(Integer32):
    """Custom type vdslPortConfTlsEnable based on Integer32"""
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


_VdslPortConfTlsEnable_Type.__name__ = "Integer32"
_VdslPortConfTlsEnable_Object = MibTableColumn
vdslPortConfTlsEnable = _VdslPortConfTlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 4),
    _VdslPortConfTlsEnable_Type()
)
vdslPortConfTlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfTlsEnable.setStatus("current")
_VdslPortConfTlsVid_Type = VlanIndex
_VdslPortConfTlsVid_Object = MibTableColumn
vdslPortConfTlsVid = _VdslPortConfTlsVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 5),
    _VdslPortConfTlsVid_Type()
)
vdslPortConfTlsVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfTlsVid.setStatus("current")
_VdslPortConfTlsPriority_Type = Integer32
_VdslPortConfTlsPriority_Object = MibTableColumn
vdslPortConfTlsPriority = _VdslPortConfTlsPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 6),
    _VdslPortConfTlsPriority_Type()
)
vdslPortConfTlsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfTlsPriority.setStatus("current")


class _VdslPortConfDtEnable_Type(Integer32):
    """Custom type vdslPortConfDtEnable based on Integer32"""
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


_VdslPortConfDtEnable_Type.__name__ = "Integer32"
_VdslPortConfDtEnable_Object = MibTableColumn
vdslPortConfDtEnable = _VdslPortConfDtEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 7),
    _VdslPortConfDtEnable_Type()
)
vdslPortConfDtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtEnable.setStatus("current")
_VdslPortConfDtSVid_Type = VlanIndex
_VdslPortConfDtSVid_Object = MibTableColumn
vdslPortConfDtSVid = _VdslPortConfDtSVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 8),
    _VdslPortConfDtSVid_Type()
)
vdslPortConfDtSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtSVid.setStatus("current")
_VdslPortConfDtSPriority_Type = Integer32
_VdslPortConfDtSPriority_Object = MibTableColumn
vdslPortConfDtSPriority = _VdslPortConfDtSPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 9),
    _VdslPortConfDtSPriority_Type()
)
vdslPortConfDtSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtSPriority.setStatus("current")
_VdslPortConfDtCVid_Type = VlanIndex
_VdslPortConfDtCVid_Object = MibTableColumn
vdslPortConfDtCVid = _VdslPortConfDtCVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 10),
    _VdslPortConfDtCVid_Type()
)
vdslPortConfDtCVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtCVid.setStatus("current")
_VdslPortConfDtCPriority_Type = Integer32
_VdslPortConfDtCPriority_Object = MibTableColumn
vdslPortConfDtCPriority = _VdslPortConfDtCPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 1, 1, 11),
    _VdslPortConfDtCPriority_Type()
)
vdslPortConfDtCPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtCPriority.setStatus("current")
_VdslPortPvlanTable_Object = MibTable
vdslPortPvlanTable = _VdslPortPvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vdslPortPvlanTable.setStatus("current")
_VdslPortPvlanEntry_Object = MibTableRow
vdslPortPvlanEntry = _VdslPortPvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 4, 1)
)
vdslPortPvlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "vdslPortPvlanEtype"),
)
if mibBuilder.loadTexts:
    vdslPortPvlanEntry.setStatus("current")
_VdslPortPvlanEtype_Type = Unsigned32
_VdslPortPvlanEtype_Object = MibTableColumn
vdslPortPvlanEtype = _VdslPortPvlanEtype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 4, 1, 1),
    _VdslPortPvlanEtype_Type()
)
vdslPortPvlanEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortPvlanEtype.setStatus("current")
_VdslPortPvlanVid_Type = VlanIndex
_VdslPortPvlanVid_Object = MibTableColumn
vdslPortPvlanVid = _VdslPortPvlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 4, 1, 2),
    _VdslPortPvlanVid_Type()
)
vdslPortPvlanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortPvlanVid.setStatus("current")


class _VdslPortPvlanPriority_Type(Integer32):
    """Custom type vdslPortPvlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VdslPortPvlanPriority_Type.__name__ = "Integer32"
_VdslPortPvlanPriority_Object = MibTableColumn
vdslPortPvlanPriority = _VdslPortPvlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 4, 1, 3),
    _VdslPortPvlanPriority_Type()
)
vdslPortPvlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortPvlanPriority.setStatus("current")
_VdslPortPvlanRowStatus_Type = RowStatus
_VdslPortPvlanRowStatus_Object = MibTableColumn
vdslPortPvlanRowStatus = _VdslPortPvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 2, 4, 1, 4),
    _VdslPortPvlanRowStatus_Type()
)
vdslPortPvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortPvlanRowStatus.setStatus("current")
_VdslRfiCustomTable_Object = MibTable
vdslRfiCustomTable = _VdslRfiCustomTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 3)
)
if mibBuilder.loadTexts:
    vdslRfiCustomTable.setStatus("current")
_VdslRfiCustomEntry_Object = MibTableRow
vdslRfiCustomEntry = _VdslRfiCustomEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 3, 1)
)
vdslRfiCustomEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "vdslRfiCustomIndex"),
)
if mibBuilder.loadTexts:
    vdslRfiCustomEntry.setStatus("current")
_VdslRfiCustomIndex_Type = Integer32
_VdslRfiCustomIndex_Object = MibTableColumn
vdslRfiCustomIndex = _VdslRfiCustomIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 3, 1, 1),
    _VdslRfiCustomIndex_Type()
)
vdslRfiCustomIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslRfiCustomIndex.setStatus("current")
_VdslRfiCustomStartFreq_Type = Integer32
_VdslRfiCustomStartFreq_Object = MibTableColumn
vdslRfiCustomStartFreq = _VdslRfiCustomStartFreq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 3, 1, 2),
    _VdslRfiCustomStartFreq_Type()
)
vdslRfiCustomStartFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslRfiCustomStartFreq.setStatus("current")
if mibBuilder.loadTexts:
    vdslRfiCustomStartFreq.setUnits("KHz")
_VdslRfiCustomEndFreq_Type = Integer32
_VdslRfiCustomEndFreq_Object = MibTableColumn
vdslRfiCustomEndFreq = _VdslRfiCustomEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 3, 1, 3),
    _VdslRfiCustomEndFreq_Type()
)
vdslRfiCustomEndFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslRfiCustomEndFreq.setStatus("current")
if mibBuilder.loadTexts:
    vdslRfiCustomEndFreq.setUnits("KHz")


class _VdslRfiCustomEnable_Type(Integer32):
    """Custom type vdslRfiCustomEnable based on Integer32"""
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


_VdslRfiCustomEnable_Type.__name__ = "Integer32"
_VdslRfiCustomEnable_Object = MibTableColumn
vdslRfiCustomEnable = _VdslRfiCustomEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 3, 1, 4),
    _VdslRfiCustomEnable_Type()
)
vdslRfiCustomEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslRfiCustomEnable.setStatus("current")
_VdslLineConfUpboParamTable_Object = MibTable
vdslLineConfUpboParamTable = _VdslLineConfUpboParamTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 4)
)
if mibBuilder.loadTexts:
    vdslLineConfUpboParamTable.setStatus("current")
_VdslLineConfUpboParamEntry_Object = MibTableRow
vdslLineConfUpboParamEntry = _VdslLineConfUpboParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 4, 1)
)
vdslLineConfUpboParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "vdslLineConfUpboParamBand"),
)
if mibBuilder.loadTexts:
    vdslLineConfUpboParamEntry.setStatus("current")
_VdslLineConfUpboParamBand_Type = Integer32
_VdslLineConfUpboParamBand_Object = MibTableColumn
vdslLineConfUpboParamBand = _VdslLineConfUpboParamBand_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 4, 1, 1),
    _VdslLineConfUpboParamBand_Type()
)
vdslLineConfUpboParamBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamBand.setStatus("current")


class _VdslLineConfUpboParamA_Type(Integer32):
    """Custom type vdslLineConfUpboParamA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_VdslLineConfUpboParamA_Type.__name__ = "Integer32"
_VdslLineConfUpboParamA_Object = MibTableColumn
vdslLineConfUpboParamA = _VdslLineConfUpboParamA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 4, 1, 2),
    _VdslLineConfUpboParamA_Type()
)
vdslLineConfUpboParamA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamA.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamA.setUnits("0.01 dBm/Hz")


class _VdslLineConfUpboParamB_Type(Integer32):
    """Custom type vdslLineConfUpboParamB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VdslLineConfUpboParamB_Type.__name__ = "Integer32"
_VdslLineConfUpboParamB_Object = MibTableColumn
vdslLineConfUpboParamB = _VdslLineConfUpboParamB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 4, 1, 3),
    _VdslLineConfUpboParamB_Type()
)
vdslLineConfUpboParamB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamB.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamB.setUnits("0.01 dBm/Hz")
_VdslLineConfDpboTable_Object = MibTable
vdslLineConfDpboTable = _VdslLineConfDpboTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 5)
)
if mibBuilder.loadTexts:
    vdslLineConfDpboTable.setStatus("current")
_VdslLineConfDpboEntry_Object = MibTableRow
vdslLineConfDpboEntry = _VdslLineConfDpboEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 5, 1)
)
vdslLineConfDpboEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "vdslLineConfDpboIndex"),
)
if mibBuilder.loadTexts:
    vdslLineConfDpboEntry.setStatus("current")
_VdslLineConfDpboIndex_Type = Integer32
_VdslLineConfDpboIndex_Object = MibTableColumn
vdslLineConfDpboIndex = _VdslLineConfDpboIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 5, 1, 1),
    _VdslLineConfDpboIndex_Type()
)
vdslLineConfDpboIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineConfDpboIndex.setStatus("current")


class _VdslLineConfDpboTone_Type(Integer32):
    """Custom type vdslLineConfDpboTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_VdslLineConfDpboTone_Type.__name__ = "Integer32"
_VdslLineConfDpboTone_Object = MibTableColumn
vdslLineConfDpboTone = _VdslLineConfDpboTone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 5, 1, 2),
    _VdslLineConfDpboTone_Type()
)
vdslLineConfDpboTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboTone.setStatus("current")


class _VdslLineConfDpboPsd_Type(Integer32):
    """Custom type vdslLineConfDpboPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineConfDpboPsd_Type.__name__ = "Integer32"
_VdslLineConfDpboPsd_Object = MibTableColumn
vdslLineConfDpboPsd = _VdslLineConfDpboPsd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 5, 1, 3),
    _VdslLineConfDpboPsd_Type()
)
vdslLineConfDpboPsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboPsd.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboPsd.setUnits("-0.5dBm/Hz")
_VdslLineStatusTable_Object = MibTable
vdslLineStatusTable = _VdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 6)
)
if mibBuilder.loadTexts:
    vdslLineStatusTable.setStatus("current")
_VdslLineStatusEntry_Object = MibTableRow
vdslLineStatusEntry = _VdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 6, 1)
)
vdslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslLineStatusEntry.setStatus("current")
_VdslLineStatusVturInp_Type = Integer32
_VdslLineStatusVturInp_Object = MibTableColumn
vdslLineStatusVturInp = _VdslLineStatusVturInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 6, 1, 1),
    _VdslLineStatusVturInp_Type()
)
vdslLineStatusVturInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatusVturInp.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineStatusVturInp.setUnits("0.1 DTM symbol")
_VdslLineStatusVtucInp_Type = Integer32
_VdslLineStatusVtucInp_Object = MibTableColumn
vdslLineStatusVtucInp = _VdslLineStatusVtucInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 3, 6, 1, 2),
    _VdslLineStatusVtucInp_Type()
)
vdslLineStatusVtucInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatusVtucInp.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineStatusVtucInp.setUnits("0.1 DTM symbol")
_Pvc_ObjectIdentity = ObjectIdentity
pvc = _Pvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4)
)
_MaxNumOfPvcs_Type = Integer32
_MaxNumOfPvcs_Object = MibScalar
maxNumOfPvcs = _MaxNumOfPvcs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 1),
    _MaxNumOfPvcs_Type()
)
maxNumOfPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPvcs.setStatus("current")
_PvcTable_Object = MibTable
pvcTable = _PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2)
)
if mibBuilder.loadTexts:
    pvcTable.setStatus("current")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1)
)
pvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcPvid"),
)
if mibBuilder.loadTexts:
    pvcEntry.setStatus("current")


class _PvcVpi_Type(Integer32):
    """Custom type pvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcVpi_Type.__name__ = "Integer32"
_PvcVpi_Object = MibTableColumn
pvcVpi = _PvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 1),
    _PvcVpi_Type()
)
pvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVpi.setStatus("current")


class _PvcVci_Type(Integer32):
    """Custom type pvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcVci_Type.__name__ = "Integer32"
_PvcVci_Object = MibTableColumn
pvcVci = _PvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 2),
    _PvcVci_Type()
)
pvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVci.setStatus("current")
_PvcPvid_Type = VlanIndex
_PvcPvid_Object = MibTableColumn
pvcPvid = _PvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 3),
    _PvcPvid_Type()
)
pvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPvid.setStatus("current")


class _PvcPriority_Type(Integer32):
    """Custom type pvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvcPriority_Type.__name__ = "Integer32"
_PvcPriority_Object = MibTableColumn
pvcPriority = _PvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 5),
    _PvcPriority_Type()
)
pvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPriority.setStatus("current")


class _PvcProfile_Type(DisplayString):
    """Custom type pvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcProfile_Type.__name__ = "DisplayString"
_PvcProfile_Object = MibTableColumn
pvcProfile = _PvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 6),
    _PvcProfile_Type()
)
pvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfile.setStatus("current")


class _PvcEncap_Type(Integer32):
    """Custom type pvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_PvcEncap_Type.__name__ = "Integer32"
_PvcEncap_Object = MibTableColumn
pvcEncap = _PvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 7),
    _PvcEncap_Type()
)
pvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcEncap.setStatus("current")
_PvcRowStatus_Type = RowStatus
_PvcRowStatus_Object = MibTableColumn
pvcRowStatus = _PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 2, 1, 8),
    _PvcRowStatus_Type()
)
pvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcRowStatus.setStatus("current")
_PvcPvlanTable_Object = MibTable
pvcPvlanTable = _PvcPvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5)
)
if mibBuilder.loadTexts:
    pvcPvlanTable.setStatus("current")
_PvcPvlanEntry_Object = MibTableRow
pvcPvlanEntry = _PvcPvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1)
)
pvcPvlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcPvlanVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcPvlanVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcPvlanEtype"),
)
if mibBuilder.loadTexts:
    pvcPvlanEntry.setStatus("current")


class _PvcPvlanVpi_Type(Integer32):
    """Custom type pvcPvlanVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcPvlanVpi_Type.__name__ = "Integer32"
_PvcPvlanVpi_Object = MibTableColumn
pvcPvlanVpi = _PvcPvlanVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1, 1),
    _PvcPvlanVpi_Type()
)
pvcPvlanVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPvlanVpi.setStatus("current")


class _PvcPvlanVci_Type(Integer32):
    """Custom type pvcPvlanVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcPvlanVci_Type.__name__ = "Integer32"
_PvcPvlanVci_Object = MibTableColumn
pvcPvlanVci = _PvcPvlanVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1, 2),
    _PvcPvlanVci_Type()
)
pvcPvlanVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPvlanVci.setStatus("current")
_PvcPvlanEtype_Type = Unsigned32
_PvcPvlanEtype_Object = MibTableColumn
pvcPvlanEtype = _PvcPvlanEtype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1, 3),
    _PvcPvlanEtype_Type()
)
pvcPvlanEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPvlanEtype.setStatus("current")
_PvcPvlanVid_Type = VlanIndex
_PvcPvlanVid_Object = MibTableColumn
pvcPvlanVid = _PvcPvlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1, 4),
    _PvcPvlanVid_Type()
)
pvcPvlanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPvlanVid.setStatus("current")


class _PvcPvlanPriority_Type(Integer32):
    """Custom type pvcPvlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvcPvlanPriority_Type.__name__ = "Integer32"
_PvcPvlanPriority_Object = MibTableColumn
pvcPvlanPriority = _PvcPvlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1, 5),
    _PvcPvlanPriority_Type()
)
pvcPvlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPvlanPriority.setStatus("current")
_PvcPvlanRowStatus_Type = RowStatus
_PvcPvlanRowStatus_Object = MibTableColumn
pvcPvlanRowStatus = _PvcPvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 4, 5, 1, 6),
    _PvcPvlanRowStatus_Type()
)
pvcPvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPvlanRowStatus.setStatus("current")
_PvcStats_ObjectIdentity = ObjectIdentity
pvcStats = _PvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 7)
)
_PvcStatsTable_Object = MibTable
pvcStatsTable = _PvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 7, 1)
)
if mibBuilder.loadTexts:
    pvcStatsTable.setStatus("current")
_PvcStatsEntry_Object = MibTableRow
pvcStatsEntry = _PvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 7, 1, 1)
)
pvcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "pvcVci"),
)
if mibBuilder.loadTexts:
    pvcStatsEntry.setStatus("current")
_PvcStatsTxPackets_Type = Counter64
_PvcStatsTxPackets_Object = MibTableColumn
pvcStatsTxPackets = _PvcStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 7, 1, 1, 1),
    _PvcStatsTxPackets_Type()
)
pvcStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatsTxPackets.setStatus("current")
_PvcStatsRxPackets_Type = Counter64
_PvcStatsRxPackets_Object = MibTableColumn
pvcStatsRxPackets = _PvcStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 7, 1, 1, 2),
    _PvcStatsRxPackets_Type()
)
pvcStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatsRxPackets.setStatus("current")
_Rpvc_ObjectIdentity = ObjectIdentity
rpvc = _Rpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8)
)
_RpvcGatewayTable_Object = MibTable
rpvcGatewayTable = _RpvcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 1)
)
if mibBuilder.loadTexts:
    rpvcGatewayTable.setStatus("current")
_RpvcGatewayEntry_Object = MibTableRow
rpvcGatewayEntry = _RpvcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 1, 1)
)
rpvcGatewayEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcGatewayIp"),
)
if mibBuilder.loadTexts:
    rpvcGatewayEntry.setStatus("current")
_RpvcGatewayIp_Type = IpAddress
_RpvcGatewayIp_Object = MibTableColumn
rpvcGatewayIp = _RpvcGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 1, 1, 1),
    _RpvcGatewayIp_Type()
)
rpvcGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcGatewayIp.setStatus("current")
_RpvcGatewayVlanId_Type = VlanIndex
_RpvcGatewayVlanId_Object = MibTableColumn
rpvcGatewayVlanId = _RpvcGatewayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 1, 1, 2),
    _RpvcGatewayVlanId_Type()
)
rpvcGatewayVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayVlanId.setStatus("current")
_RpvcGatewayRowStatus_Type = RowStatus
_RpvcGatewayRowStatus_Object = MibTableColumn
rpvcGatewayRowStatus = _RpvcGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 1, 1, 3),
    _RpvcGatewayRowStatus_Type()
)
rpvcGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayRowStatus.setStatus("current")
_RpvcGatewayPriority_Type = Integer32
_RpvcGatewayPriority_Object = MibTableColumn
rpvcGatewayPriority = _RpvcGatewayPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 1, 1, 4),
    _RpvcGatewayPriority_Type()
)
rpvcGatewayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayPriority.setStatus("current")
_RpvcTable_Object = MibTable
rpvcTable = _RpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2)
)
if mibBuilder.loadTexts:
    rpvcTable.setStatus("current")
_RpvcEntry_Object = MibTableRow
rpvcEntry = _RpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1)
)
rpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcIp"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcNetmask"),
)
if mibBuilder.loadTexts:
    rpvcEntry.setStatus("current")


class _RpvcVpi_Type(Integer32):
    """Custom type rpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcVpi_Type.__name__ = "Integer32"
_RpvcVpi_Object = MibTableColumn
rpvcVpi = _RpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 1),
    _RpvcVpi_Type()
)
rpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVpi.setStatus("current")


class _RpvcVci_Type(Integer32):
    """Custom type rpvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpvcVci_Type.__name__ = "Integer32"
_RpvcVci_Object = MibTableColumn
rpvcVci = _RpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 2),
    _RpvcVci_Type()
)
rpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVci.setStatus("current")


class _RpvcEncap_Type(Integer32):
    """Custom type rpvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_RpvcEncap_Type.__name__ = "Integer32"
_RpvcEncap_Object = MibTableColumn
rpvcEncap = _RpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 3),
    _RpvcEncap_Type()
)
rpvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcEncap.setStatus("current")


class _RpvcProfile_Type(DisplayString):
    """Custom type rpvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RpvcProfile_Type.__name__ = "DisplayString"
_RpvcProfile_Object = MibTableColumn
rpvcProfile = _RpvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 4),
    _RpvcProfile_Type()
)
rpvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcProfile.setStatus("current")
_RpvcIp_Type = IpAddress
_RpvcIp_Object = MibTableColumn
rpvcIp = _RpvcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 5),
    _RpvcIp_Type()
)
rpvcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcIp.setStatus("current")
_RpvcNetmask_Type = IpAddress
_RpvcNetmask_Object = MibTableColumn
rpvcNetmask = _RpvcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 6),
    _RpvcNetmask_Type()
)
rpvcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcNetmask.setStatus("current")
_RpvcGatewayIpAddress_Type = IpAddress
_RpvcGatewayIpAddress_Object = MibTableColumn
rpvcGatewayIpAddress = _RpvcGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 7),
    _RpvcGatewayIpAddress_Type()
)
rpvcGatewayIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayIpAddress.setStatus("current")
_RpvcRowStatus_Type = RowStatus
_RpvcRowStatus_Object = MibTableColumn
rpvcRowStatus = _RpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 2, 1, 8),
    _RpvcRowStatus_Type()
)
rpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRowStatus.setStatus("current")
_RpvcRouteDomainTable_Object = MibTable
rpvcRouteDomainTable = _RpvcRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3)
)
if mibBuilder.loadTexts:
    rpvcRouteDomainTable.setStatus("current")
_RpvcRouteDomainEntry_Object = MibTableRow
rpvcRouteDomainEntry = _RpvcRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3, 1)
)
rpvcRouteDomainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcRouteDomainVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcRouteDomainVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcRouteDomainIp"),
    (0, "ZYXEL-VES1608FE53A-MIB", "rpvcRouteDomainNetmask"),
)
if mibBuilder.loadTexts:
    rpvcRouteDomainEntry.setStatus("current")


class _RpvcRouteDomainVpi_Type(Integer32):
    """Custom type rpvcRouteDomainVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcRouteDomainVpi_Type.__name__ = "Integer32"
_RpvcRouteDomainVpi_Object = MibTableColumn
rpvcRouteDomainVpi = _RpvcRouteDomainVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3, 1, 1),
    _RpvcRouteDomainVpi_Type()
)
rpvcRouteDomainVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVpi.setStatus("current")


class _RpvcRouteDomainVci_Type(Integer32):
    """Custom type rpvcRouteDomainVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpvcRouteDomainVci_Type.__name__ = "Integer32"
_RpvcRouteDomainVci_Object = MibTableColumn
rpvcRouteDomainVci = _RpvcRouteDomainVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3, 1, 2),
    _RpvcRouteDomainVci_Type()
)
rpvcRouteDomainVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVci.setStatus("current")
_RpvcRouteDomainIp_Type = IpAddress
_RpvcRouteDomainIp_Object = MibTableColumn
rpvcRouteDomainIp = _RpvcRouteDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3, 1, 3),
    _RpvcRouteDomainIp_Type()
)
rpvcRouteDomainIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainIp.setStatus("current")
_RpvcRouteDomainNetmask_Type = IpAddress
_RpvcRouteDomainNetmask_Object = MibTableColumn
rpvcRouteDomainNetmask = _RpvcRouteDomainNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3, 1, 4),
    _RpvcRouteDomainNetmask_Type()
)
rpvcRouteDomainNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainNetmask.setStatus("current")
_RpvcRouteDomainRowStatus_Type = RowStatus
_RpvcRouteDomainRowStatus_Object = MibTableColumn
rpvcRouteDomainRowStatus = _RpvcRouteDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 3, 1, 5),
    _RpvcRouteDomainRowStatus_Type()
)
rpvcRouteDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRouteDomainRowStatus.setStatus("current")
_RpvcArpAgingTime_Type = Integer32
_RpvcArpAgingTime_Object = MibScalar
rpvcArpAgingTime = _RpvcArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 4),
    _RpvcArpAgingTime_Type()
)
rpvcArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpAgingTime.setStatus("current")


class _RpvcArpFlush_Type(Integer32):
    """Custom type rpvcArpFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_RpvcArpFlush_Type.__name__ = "Integer32"
_RpvcArpFlush_Object = MibScalar
rpvcArpFlush = _RpvcArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 8, 5),
    _RpvcArpFlush_Type()
)
rpvcArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpFlush.setStatus("current")
_DsBcastDisableTable_Object = MibTable
dsBcastDisableTable = _DsBcastDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 9)
)
if mibBuilder.loadTexts:
    dsBcastDisableTable.setStatus("current")
_DsBcastDisableEntry_Object = MibTableRow
dsBcastDisableEntry = _DsBcastDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 9, 1)
)
dsBcastDisableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "dsBcastDisableVlanId"),
)
if mibBuilder.loadTexts:
    dsBcastDisableEntry.setStatus("current")
_DsBcastDisableVlanId_Type = Integer32
_DsBcastDisableVlanId_Object = MibTableColumn
dsBcastDisableVlanId = _DsBcastDisableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 9, 1, 1),
    _DsBcastDisableVlanId_Type()
)
dsBcastDisableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBcastDisableVlanId.setStatus("current")
_DsBcastDisableRowStatus_Type = RowStatus
_DsBcastDisableRowStatus_Object = MibTableColumn
dsBcastDisableRowStatus = _DsBcastDisableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 9, 1, 2),
    _DsBcastDisableRowStatus_Type()
)
dsBcastDisableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsBcastDisableRowStatus.setStatus("current")
_Paepvc_ObjectIdentity = ObjectIdentity
paepvc = _Paepvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10)
)
_PaepvcTable_Object = MibTable
paepvcTable = _PaepvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1)
)
if mibBuilder.loadTexts:
    paepvcTable.setStatus("current")
_PaepvcEntry_Object = MibTableRow
paepvcEntry = _PaepvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1)
)
paepvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcPvid"),
)
if mibBuilder.loadTexts:
    paepvcEntry.setStatus("current")


class _PaepvcVpi_Type(Integer32):
    """Custom type paepvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PaepvcVpi_Type.__name__ = "Integer32"
_PaepvcVpi_Object = MibTableColumn
paepvcVpi = _PaepvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 1),
    _PaepvcVpi_Type()
)
paepvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVpi.setStatus("current")


class _PaepvcVci_Type(Integer32):
    """Custom type paepvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PaepvcVci_Type.__name__ = "Integer32"
_PaepvcVci_Object = MibTableColumn
paepvcVci = _PaepvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 2),
    _PaepvcVci_Type()
)
paepvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVci.setStatus("current")
_PaepvcPvid_Type = VlanIndex
_PaepvcPvid_Object = MibTableColumn
paepvcPvid = _PaepvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 3),
    _PaepvcPvid_Type()
)
paepvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcPvid.setStatus("current")


class _PaepvcEncap_Type(Integer32):
    """Custom type paepvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_PaepvcEncap_Type.__name__ = "Integer32"
_PaepvcEncap_Object = MibTableColumn
paepvcEncap = _PaepvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 4),
    _PaepvcEncap_Type()
)
paepvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcEncap.setStatus("current")


class _PaepvcPriority_Type(Integer32):
    """Custom type paepvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PaepvcPriority_Type.__name__ = "Integer32"
_PaepvcPriority_Object = MibTableColumn
paepvcPriority = _PaepvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 5),
    _PaepvcPriority_Type()
)
paepvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcPriority.setStatus("current")


class _PaepvcProfile_Type(DisplayString):
    """Custom type paepvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PaepvcProfile_Type.__name__ = "DisplayString"
_PaepvcProfile_Object = MibTableColumn
paepvcProfile = _PaepvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 6),
    _PaepvcProfile_Type()
)
paepvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfile.setStatus("current")
_PaepvcAcName_Type = DisplayString
_PaepvcAcName_Object = MibTableColumn
paepvcAcName = _PaepvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 7),
    _PaepvcAcName_Type()
)
paepvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcAcName.setStatus("current")
_PaepvcServiceName_Type = DisplayString
_PaepvcServiceName_Object = MibTableColumn
paepvcServiceName = _PaepvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 8),
    _PaepvcServiceName_Type()
)
paepvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcServiceName.setStatus("current")
_PaepvcHelloTime_Type = Integer32
_PaepvcHelloTime_Object = MibTableColumn
paepvcHelloTime = _PaepvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 9),
    _PaepvcHelloTime_Type()
)
paepvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    paepvcHelloTime.setUnits("second")
_PaepvcRowStatus_Type = RowStatus
_PaepvcRowStatus_Object = MibTableColumn
paepvcRowStatus = _PaepvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 10, 1, 1, 10),
    _PaepvcRowStatus_Type()
)
paepvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcRowStatus.setStatus("current")
_Tlspvc_ObjectIdentity = ObjectIdentity
tlspvc = _Tlspvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11)
)
_TlspvcTable_Object = MibTable
tlspvcTable = _TlspvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1)
)
if mibBuilder.loadTexts:
    tlspvcTable.setStatus("current")
_TlspvcEntry_Object = MibTableRow
tlspvcEntry = _TlspvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1)
)
tlspvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "tlspvcVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "tlspvcVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "tlspvcSvid"),
)
if mibBuilder.loadTexts:
    tlspvcEntry.setStatus("current")


class _TlspvcVpi_Type(Integer32):
    """Custom type tlspvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TlspvcVpi_Type.__name__ = "Integer32"
_TlspvcVpi_Object = MibTableColumn
tlspvcVpi = _TlspvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 1),
    _TlspvcVpi_Type()
)
tlspvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVpi.setStatus("current")


class _TlspvcVci_Type(Integer32):
    """Custom type tlspvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlspvcVci_Type.__name__ = "Integer32"
_TlspvcVci_Object = MibTableColumn
tlspvcVci = _TlspvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 2),
    _TlspvcVci_Type()
)
tlspvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVci.setStatus("current")
_TlspvcSvid_Type = VlanIndex
_TlspvcSvid_Object = MibTableColumn
tlspvcSvid = _TlspvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 3),
    _TlspvcSvid_Type()
)
tlspvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcSvid.setStatus("current")


class _TlspvcEncap_Type(Integer32):
    """Custom type tlspvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_TlspvcEncap_Type.__name__ = "Integer32"
_TlspvcEncap_Object = MibTableColumn
tlspvcEncap = _TlspvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 4),
    _TlspvcEncap_Type()
)
tlspvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcEncap.setStatus("current")


class _TlspvcSpriority_Type(Integer32):
    """Custom type tlspvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TlspvcSpriority_Type.__name__ = "Integer32"
_TlspvcSpriority_Object = MibTableColumn
tlspvcSpriority = _TlspvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 5),
    _TlspvcSpriority_Type()
)
tlspvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcSpriority.setStatus("current")


class _TlspvcProfile_Type(DisplayString):
    """Custom type tlspvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TlspvcProfile_Type.__name__ = "DisplayString"
_TlspvcProfile_Object = MibTableColumn
tlspvcProfile = _TlspvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 6),
    _TlspvcProfile_Type()
)
tlspvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfile.setStatus("current")
_TlspvcRowStatus_Type = RowStatus
_TlspvcRowStatus_Object = MibTableColumn
tlspvcRowStatus = _TlspvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 11, 1, 1, 7),
    _TlspvcRowStatus_Type()
)
tlspvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcRowStatus.setStatus("current")
_Dtpvc_ObjectIdentity = ObjectIdentity
dtpvc = _Dtpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13)
)
_DtpvcTable_Object = MibTable
dtpvcTable = _DtpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1)
)
if mibBuilder.loadTexts:
    dtpvcTable.setStatus("current")
_DtpvcEntry_Object = MibTableRow
dtpvcEntry = _DtpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1)
)
dtpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "dtpvcVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "dtpvcVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "dtpvcSvid"),
)
if mibBuilder.loadTexts:
    dtpvcEntry.setStatus("current")


class _DtpvcVpi_Type(Integer32):
    """Custom type dtpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtpvcVpi_Type.__name__ = "Integer32"
_DtpvcVpi_Object = MibTableColumn
dtpvcVpi = _DtpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 1),
    _DtpvcVpi_Type()
)
dtpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcVpi.setStatus("current")


class _DtpvcVci_Type(Integer32):
    """Custom type dtpvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtpvcVci_Type.__name__ = "Integer32"
_DtpvcVci_Object = MibTableColumn
dtpvcVci = _DtpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 2),
    _DtpvcVci_Type()
)
dtpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcVci.setStatus("current")
_DtpvcSvid_Type = VlanIndex
_DtpvcSvid_Object = MibTableColumn
dtpvcSvid = _DtpvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 3),
    _DtpvcSvid_Type()
)
dtpvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcSvid.setStatus("current")


class _DtpvcSpriority_Type(Integer32):
    """Custom type dtpvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcSpriority_Type.__name__ = "Integer32"
_DtpvcSpriority_Object = MibTableColumn
dtpvcSpriority = _DtpvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 4),
    _DtpvcSpriority_Type()
)
dtpvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcSpriority.setStatus("current")
_DtpvcCvid_Type = VlanIndex
_DtpvcCvid_Object = MibTableColumn
dtpvcCvid = _DtpvcCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 5),
    _DtpvcCvid_Type()
)
dtpvcCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcCvid.setStatus("current")


class _DtpvcCpriority_Type(Integer32):
    """Custom type dtpvcCpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcCpriority_Type.__name__ = "Integer32"
_DtpvcCpriority_Object = MibTableColumn
dtpvcCpriority = _DtpvcCpriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 6),
    _DtpvcCpriority_Type()
)
dtpvcCpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcCpriority.setStatus("current")


class _DtpvcEncap_Type(Integer32):
    """Custom type dtpvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_DtpvcEncap_Type.__name__ = "Integer32"
_DtpvcEncap_Object = MibTableColumn
dtpvcEncap = _DtpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 7),
    _DtpvcEncap_Type()
)
dtpvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcEncap.setStatus("current")


class _DtpvcProfile_Type(DisplayString):
    """Custom type dtpvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcProfile_Type.__name__ = "DisplayString"
_DtpvcProfile_Object = MibTableColumn
dtpvcProfile = _DtpvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 8),
    _DtpvcProfile_Type()
)
dtpvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcProfile.setStatus("current")
_DtpvcRowStatus_Type = RowStatus
_DtpvcRowStatus_Object = MibTableColumn
dtpvcRowStatus = _DtpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 8, 13, 1, 1, 9),
    _DtpvcRowStatus_Type()
)
dtpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcRowStatus.setStatus("current")
_Profile_ObjectIdentity = ObjectIdentity
profile = _Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9)
)
_SraShiftMarginProfile_ObjectIdentity = ObjectIdentity
sraShiftMarginProfile = _SraShiftMarginProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1)
)
_SraShiftMarginProfileTable_Object = MibTable
sraShiftMarginProfileTable = _SraShiftMarginProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sraShiftMarginProfileTable.setStatus("current")
_SraShiftMarginProfileEntry_Object = MibTableRow
sraShiftMarginProfileEntry = _SraShiftMarginProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1)
)
sraShiftMarginProfileEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "sraShiftMarginProfileName"),
)
if mibBuilder.loadTexts:
    sraShiftMarginProfileEntry.setStatus("current")


class _SraShiftMarginProfileName_Type(DisplayString):
    """Custom type sraShiftMarginProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SraShiftMarginProfileName_Type.__name__ = "DisplayString"
_SraShiftMarginProfileName_Object = MibTableColumn
sraShiftMarginProfileName = _SraShiftMarginProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1, 1),
    _SraShiftMarginProfileName_Type()
)
sraShiftMarginProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraShiftMarginProfileName.setStatus("current")


class _XtucConfDownshiftSnrMgn_Type(Integer32):
    """Custom type xtucConfDownshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XtucConfDownshiftSnrMgn_Type.__name__ = "Integer32"
_XtucConfDownshiftSnrMgn_Object = MibTableColumn
xtucConfDownshiftSnrMgn = _XtucConfDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1, 2),
    _XtucConfDownshiftSnrMgn_Type()
)
xtucConfDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtucConfDownshiftSnrMgn.setStatus("current")


class _XtucConfUpshiftSnrMgn_Type(Integer32):
    """Custom type xtucConfUpshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XtucConfUpshiftSnrMgn_Type.__name__ = "Integer32"
_XtucConfUpshiftSnrMgn_Object = MibTableColumn
xtucConfUpshiftSnrMgn = _XtucConfUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1, 3),
    _XtucConfUpshiftSnrMgn_Type()
)
xtucConfUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtucConfUpshiftSnrMgn.setStatus("current")


class _XturConfDownshiftSnrMgn_Type(Integer32):
    """Custom type xturConfDownshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XturConfDownshiftSnrMgn_Type.__name__ = "Integer32"
_XturConfDownshiftSnrMgn_Object = MibTableColumn
xturConfDownshiftSnrMgn = _XturConfDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1, 6),
    _XturConfDownshiftSnrMgn_Type()
)
xturConfDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xturConfDownshiftSnrMgn.setStatus("current")


class _XturConfUpshiftSnrMgn_Type(Integer32):
    """Custom type xturConfUpshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XturConfUpshiftSnrMgn_Type.__name__ = "Integer32"
_XturConfUpshiftSnrMgn_Object = MibTableColumn
xturConfUpshiftSnrMgn = _XturConfUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1, 7),
    _XturConfUpshiftSnrMgn_Type()
)
xturConfUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xturConfUpshiftSnrMgn.setStatus("current")
_SraShiftMarginProfileStatus_Type = RowStatus
_SraShiftMarginProfileStatus_Object = MibTableColumn
sraShiftMarginProfileStatus = _SraShiftMarginProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 1, 1, 1, 10),
    _SraShiftMarginProfileStatus_Type()
)
sraShiftMarginProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sraShiftMarginProfileStatus.setStatus("current")
_IpqosProfile_ObjectIdentity = ObjectIdentity
ipqosProfile = _IpqosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8)
)
_MaxNumOfIpqosProfiles_Type = Integer32
_MaxNumOfIpqosProfiles_Object = MibScalar
maxNumOfIpqosProfiles = _MaxNumOfIpqosProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 1),
    _MaxNumOfIpqosProfiles_Type()
)
maxNumOfIpqosProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfIpqosProfiles.setStatus("current")
_IpqosProfileTable_Object = MibTable
ipqosProfileTable = _IpqosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 2)
)
if mibBuilder.loadTexts:
    ipqosProfileTable.setStatus("current")
_IpqosProfileEntry_Object = MibTableRow
ipqosProfileEntry = _IpqosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 2, 1)
)
ipqosProfileEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "ipqosProfileName"),
    (0, "ZYXEL-VES1608FE53A-MIB", "ipqosProfileNumOfQueue"),
)
if mibBuilder.loadTexts:
    ipqosProfileEntry.setStatus("current")


class _IpqosProfileName_Type(DisplayString):
    """Custom type ipqosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpqosProfileName_Type.__name__ = "DisplayString"
_IpqosProfileName_Object = MibTableColumn
ipqosProfileName = _IpqosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 2, 1, 1),
    _IpqosProfileName_Type()
)
ipqosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipqosProfileName.setStatus("current")


class _IpqosProfileNumOfQueue_Type(Integer32):
    """Custom type ipqosProfileNumOfQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IpqosProfileNumOfQueue_Type.__name__ = "Integer32"
_IpqosProfileNumOfQueue_Object = MibTableColumn
ipqosProfileNumOfQueue = _IpqosProfileNumOfQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 2, 1, 2),
    _IpqosProfileNumOfQueue_Type()
)
ipqosProfileNumOfQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipqosProfileNumOfQueue.setStatus("current")
_IpqosProfileRowStatus_Type = RowStatus
_IpqosProfileRowStatus_Object = MibTableColumn
ipqosProfileRowStatus = _IpqosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 2, 1, 3),
    _IpqosProfileRowStatus_Type()
)
ipqosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipqosProfileRowStatus.setStatus("current")
_IpqosProfileQueueTable_Object = MibTable
ipqosProfileQueueTable = _IpqosProfileQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3)
)
if mibBuilder.loadTexts:
    ipqosProfileQueueTable.setStatus("current")
_IpqosProfileQueueEntry_Object = MibTableRow
ipqosProfileQueueEntry = _IpqosProfileQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1)
)
ipqosProfileQueueEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "ipqosProfileName"),
    (0, "ZYXEL-VES1608FE53A-MIB", "ipqosProfileQueueIndex"),
)
if mibBuilder.loadTexts:
    ipqosProfileQueueEntry.setStatus("current")
_IpqosProfileQueueIndex_Type = Integer32
_IpqosProfileQueueIndex_Object = MibTableColumn
ipqosProfileQueueIndex = _IpqosProfileQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 1),
    _IpqosProfileQueueIndex_Type()
)
ipqosProfileQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipqosProfileQueueIndex.setStatus("current")


class _IpqosProfileQueuePIR_Type(Integer32):
    """Custom type ipqosProfileQueuePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 131072),
    )


_IpqosProfileQueuePIR_Type.__name__ = "Integer32"
_IpqosProfileQueuePIR_Object = MibTableColumn
ipqosProfileQueuePIR = _IpqosProfileQueuePIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 2),
    _IpqosProfileQueuePIR_Type()
)
ipqosProfileQueuePIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueuePIR.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueuePIR.setUnits("Kbps")


class _IpqosProfileQueueCIR_Type(Integer32):
    """Custom type ipqosProfileQueueCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65536),
    )


_IpqosProfileQueueCIR_Type.__name__ = "Integer32"
_IpqosProfileQueueCIR_Object = MibTableColumn
ipqosProfileQueueCIR = _IpqosProfileQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 3),
    _IpqosProfileQueueCIR_Type()
)
ipqosProfileQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueCIR.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueCIR.setUnits("Kbps")


class _IpqosProfileQueuePBS_Type(Integer32):
    """Custom type ipqosProfileQueuePBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3072, 65536),
    )


_IpqosProfileQueuePBS_Type.__name__ = "Integer32"
_IpqosProfileQueuePBS_Object = MibTableColumn
ipqosProfileQueuePBS = _IpqosProfileQueuePBS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 4),
    _IpqosProfileQueuePBS_Type()
)
ipqosProfileQueuePBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueuePBS.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueuePBS.setUnits("byte")


class _IpqosProfileQueueCBS_Type(Integer32):
    """Custom type ipqosProfileQueueCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3072, 65536),
    )


_IpqosProfileQueueCBS_Type.__name__ = "Integer32"
_IpqosProfileQueueCBS_Object = MibTableColumn
ipqosProfileQueueCBS = _IpqosProfileQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 5),
    _IpqosProfileQueueCBS_Type()
)
ipqosProfileQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueCBS.setUnits("byts")


class _IpqosProfileQueueLevel_Type(Integer32):
    """Custom type ipqosProfileQueueLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpqosProfileQueueLevel_Type.__name__ = "Integer32"
_IpqosProfileQueueLevel_Object = MibTableColumn
ipqosProfileQueueLevel = _IpqosProfileQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 6),
    _IpqosProfileQueueLevel_Type()
)
ipqosProfileQueueLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueLevel.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueLevel.setUnits("byts")


class _IpqosProfileQueueWeight_Type(Integer32):
    """Custom type ipqosProfileQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_IpqosProfileQueueWeight_Type.__name__ = "Integer32"
_IpqosProfileQueueWeight_Object = MibTableColumn
ipqosProfileQueueWeight = _IpqosProfileQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 9, 8, 3, 1, 7),
    _IpqosProfileQueueWeight_Type()
)
ipqosProfileQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueWeight.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueWeight.setUnits("byts")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10)
)
_ManagementVLANId_Type = VlanIndex
_ManagementVLANId_Object = MibScalar
managementVLANId = _ManagementVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 1),
    _ManagementVLANId_Type()
)
managementVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVLANId.setStatus("current")
_MaxNumOfStaticVlans_Type = Integer32
_MaxNumOfStaticVlans_Object = MibScalar
maxNumOfStaticVlans = _MaxNumOfStaticVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 2),
    _MaxNumOfStaticVlans_Type()
)
maxNumOfStaticVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfStaticVlans.setStatus("current")
_Pktfilter_ObjectIdentity = ObjectIdentity
pktfilter = _Pktfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 4)
)
_PktFilterPortTable_Object = MibTable
pktFilterPortTable = _PktFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 4, 1)
)
if mibBuilder.loadTexts:
    pktFilterPortTable.setStatus("current")
_PktFilterPortEntry_Object = MibTableRow
pktFilterPortEntry = _PktFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 4, 1, 1)
)
pktFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktFilterPortEntry.setStatus("current")
_PktFilter_Type = Integer32
_PktFilter_Object = MibTableColumn
pktFilter = _PktFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 4, 1, 1, 1),
    _PktFilter_Type()
)
pktFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktFilter.setStatus("current")
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5)
)
_MaxNumberOfRadiusServers_Type = Integer32
_MaxNumberOfRadiusServers_Object = MibScalar
maxNumberOfRadiusServers = _MaxNumberOfRadiusServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 1),
    _MaxNumberOfRadiusServers_Type()
)
maxNumberOfRadiusServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfRadiusServers.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2, 1)
)
radiusServerEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")
_RadiusServerIndex_Type = Integer32
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerIp_Type = IpAddress
_RadiusServerIp_Object = MibTableColumn
radiusServerIp = _RadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2, 1, 2),
    _RadiusServerIp_Type()
)
radiusServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerIp.setStatus("current")
_RadiusServerPort_Type = Integer32
_RadiusServerPort_Object = MibTableColumn
radiusServerPort = _RadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2, 1, 3),
    _RadiusServerPort_Type()
)
radiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerPort.setStatus("current")
_RadiusSharedSecret_Type = DisplayString
_RadiusSharedSecret_Object = MibTableColumn
radiusSharedSecret = _RadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2, 1, 4),
    _RadiusSharedSecret_Type()
)
radiusSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusSharedSecret.setStatus("current")
_RadiusServerRowStatus_Type = RowStatus
_RadiusServerRowStatus_Object = MibTableColumn
radiusServerRowStatus = _RadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 2, 1, 5),
    _RadiusServerRowStatus_Type()
)
radiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerRowStatus.setStatus("current")


class _Dot1xEnable_Type(Integer32):
    """Custom type dot1xEnable based on Integer32"""
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


_Dot1xEnable_Type.__name__ = "Integer32"
_Dot1xEnable_Object = MibScalar
dot1xEnable = _Dot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 3),
    _Dot1xEnable_Type()
)
dot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xEnable.setStatus("current")
_Dot1xPortTable_Object = MibTable
dot1xPortTable = _Dot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 4)
)
if mibBuilder.loadTexts:
    dot1xPortTable.setStatus("current")
_Dot1xPortEntry_Object = MibTableRow
dot1xPortEntry = _Dot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 4, 1)
)
dot1xPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot1xPortEntry.setStatus("current")


class _Dot1xPortEnable_Type(Integer32):
    """Custom type dot1xPortEnable based on Integer32"""
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


_Dot1xPortEnable_Type.__name__ = "Integer32"
_Dot1xPortEnable_Object = MibTableColumn
dot1xPortEnable = _Dot1xPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 4, 1, 1),
    _Dot1xPortEnable_Type()
)
dot1xPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortEnable.setStatus("current")


class _Dot1xPortControl_Type(Integer32):
    """Custom type dot1xPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnAuth", 3))
    )


_Dot1xPortControl_Type.__name__ = "Integer32"
_Dot1xPortControl_Object = MibTableColumn
dot1xPortControl = _Dot1xPortControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 4, 1, 2),
    _Dot1xPortControl_Type()
)
dot1xPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortControl.setStatus("current")


class _Dot1xPortReAuthEnable_Type(Integer32):
    """Custom type dot1xPortReAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Dot1xPortReAuthEnable_Type.__name__ = "Integer32"
_Dot1xPortReAuthEnable_Object = MibTableColumn
dot1xPortReAuthEnable = _Dot1xPortReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 4, 1, 3),
    _Dot1xPortReAuthEnable_Type()
)
dot1xPortReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortReAuthEnable.setStatus("current")
_Dot1xPortReAuthPeriod_Type = Integer32
_Dot1xPortReAuthPeriod_Object = MibTableColumn
dot1xPortReAuthPeriod = _Dot1xPortReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 4, 1, 4),
    _Dot1xPortReAuthPeriod_Type()
)
dot1xPortReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortReAuthPeriod.setStatus("current")


class _RadiusMode_Type(Integer32):
    """Custom type radiusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authentication_server", 1),
          ("local_user_profile", 2))
    )


_RadiusMode_Type.__name__ = "Integer32"
_RadiusMode_Object = MibScalar
radiusMode = _RadiusMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 5),
    _RadiusMode_Type()
)
radiusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMode.setStatus("current")
_MaxNumberOfRadiusUserProfiles_Type = Integer32
_MaxNumberOfRadiusUserProfiles_Object = MibScalar
maxNumberOfRadiusUserProfiles = _MaxNumberOfRadiusUserProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 6),
    _MaxNumberOfRadiusUserProfiles_Type()
)
maxNumberOfRadiusUserProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfRadiusUserProfiles.setStatus("current")
_RadiusUserProfileTable_Object = MibTable
radiusUserProfileTable = _RadiusUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 7)
)
if mibBuilder.loadTexts:
    radiusUserProfileTable.setStatus("current")
_RadiusUserProfileEntry_Object = MibTableRow
radiusUserProfileEntry = _RadiusUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 7, 1)
)
radiusUserProfileEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "radiusUserProfileUserName"),
)
if mibBuilder.loadTexts:
    radiusUserProfileEntry.setStatus("current")
_RadiusUserProfileUserName_Type = DisplayString
_RadiusUserProfileUserName_Object = MibTableColumn
radiusUserProfileUserName = _RadiusUserProfileUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 7, 1, 1),
    _RadiusUserProfileUserName_Type()
)
radiusUserProfileUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusUserProfileUserName.setStatus("current")
_RadiusUserProfileUserPassword_Type = DisplayString
_RadiusUserProfileUserPassword_Object = MibTableColumn
radiusUserProfileUserPassword = _RadiusUserProfileUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 7, 1, 2),
    _RadiusUserProfileUserPassword_Type()
)
radiusUserProfileUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusUserProfileUserPassword.setStatus("current")
_RadiusUserProfileRowStatus_Type = RowStatus
_RadiusUserProfileRowStatus_Object = MibTableColumn
radiusUserProfileRowStatus = _RadiusUserProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 5, 7, 1, 3),
    _RadiusUserProfileRowStatus_Type()
)
radiusUserProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusUserProfileRowStatus.setStatus("current")
_Dot3ad_ObjectIdentity = ObjectIdentity
dot3ad = _Dot3ad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6)
)
_Dot3adTable_Object = MibTable
dot3adTable = _Dot3adTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 1)
)
if mibBuilder.loadTexts:
    dot3adTable.setStatus("current")
_Dot3adEntry_Object = MibTableRow
dot3adEntry = _Dot3adEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 1, 1)
)
dot3adEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "dot3adGroupId"),
)
if mibBuilder.loadTexts:
    dot3adEntry.setStatus("current")
_Dot3adGroupId_Type = Integer32
_Dot3adGroupId_Object = MibTableColumn
dot3adGroupId = _Dot3adGroupId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 1, 1, 1),
    _Dot3adGroupId_Type()
)
dot3adGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adGroupId.setStatus("current")


class _Dot3adEnable_Type(Integer32):
    """Custom type dot3adEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("enableWithLacp", 2),
          ("disable", 3))
    )


_Dot3adEnable_Type.__name__ = "Integer32"
_Dot3adEnable_Object = MibTableColumn
dot3adEnable = _Dot3adEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 1, 1, 2),
    _Dot3adEnable_Type()
)
dot3adEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adEnable.setStatus("current")


class _LacpPriority_Type(Integer32):
    """Custom type lacpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LacpPriority_Type.__name__ = "Integer32"
_LacpPriority_Object = MibScalar
lacpPriority = _LacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 2),
    _LacpPriority_Type()
)
lacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPriority.setStatus("current")


class _LacpTimeout_Type(Integer32):
    """Custom type lacpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shorttimeout", 1),
          ("longtimeout", 2))
    )


_LacpTimeout_Type.__name__ = "Integer32"
_LacpTimeout_Object = MibScalar
lacpTimeout = _LacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 3),
    _LacpTimeout_Type()
)
lacpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpTimeout.setStatus("current")
_PortTrunkingTable_Object = MibTable
portTrunkingTable = _PortTrunkingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 4)
)
if mibBuilder.loadTexts:
    portTrunkingTable.setStatus("current")
_PortTrunkingEntry_Object = MibTableRow
portTrunkingEntry = _PortTrunkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 4, 1)
)
portTrunkingEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "portTrunkingGroupId"),
)
if mibBuilder.loadTexts:
    portTrunkingEntry.setStatus("current")
_PortTrunkingGroupId_Type = Integer32
_PortTrunkingGroupId_Object = MibTableColumn
portTrunkingGroupId = _PortTrunkingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 4, 1, 1),
    _PortTrunkingGroupId_Type()
)
portTrunkingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkingGroupId.setStatus("current")


class _PortTrunkingStatus_Type(Integer32):
    """Custom type portTrunkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PortTrunkingStatus_Type.__name__ = "Integer32"
_PortTrunkingStatus_Object = MibTableColumn
portTrunkingStatus = _PortTrunkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 4, 1, 2),
    _PortTrunkingStatus_Type()
)
portTrunkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkingStatus.setStatus("current")
_PortTrunkingPortList_Type = PortList
_PortTrunkingPortList_Object = MibTableColumn
portTrunkingPortList = _PortTrunkingPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 6, 4, 1, 3),
    _PortTrunkingPortList_Type()
)
portTrunkingPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkingPortList.setStatus("current")
_PortIsolation_ObjectIdentity = ObjectIdentity
portIsolation = _PortIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 9)
)


class _PortIsolationEnable_Type(Integer32):
    """Custom type portIsolationEnable based on Integer32"""
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


_PortIsolationEnable_Type.__name__ = "Integer32"
_PortIsolationEnable_Object = MibScalar
portIsolationEnable = _PortIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 9, 1),
    _PortIsolationEnable_Type()
)
portIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIsolationEnable.setStatus("current")
_Dscp_ObjectIdentity = ObjectIdentity
dscp = _Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "dscpSrcCodePoint"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpSrcCodePoint_Type = Integer32
_DscpSrcCodePoint_Object = MibTableColumn
dscpSrcCodePoint = _DscpSrcCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 1, 1, 1),
    _DscpSrcCodePoint_Type()
)
dscpSrcCodePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpSrcCodePoint.setStatus("current")


class _DscpMapPriority_Type(Integer32):
    """Custom type dscpMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DscpMapPriority_Type.__name__ = "Integer32"
_DscpMapPriority_Object = MibTableColumn
dscpMapPriority = _DscpMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 1, 1, 3),
    _DscpMapPriority_Type()
)
dscpMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMapPriority.setStatus("current")
_DscpPortTable_Object = MibTable
dscpPortTable = _DscpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 2)
)
if mibBuilder.loadTexts:
    dscpPortTable.setStatus("current")
_DscpPortEntry_Object = MibTableRow
dscpPortEntry = _DscpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 2, 1)
)
dscpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dscpPortEntry.setStatus("current")


class _DscpStatusEnable_Type(Integer32):
    """Custom type dscpStatusEnable based on Integer32"""
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


_DscpStatusEnable_Type.__name__ = "Integer32"
_DscpStatusEnable_Object = MibTableColumn
dscpStatusEnable = _DscpStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 10, 2, 1, 1),
    _DscpStatusEnable_Type()
)
dscpStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpStatusEnable.setStatus("current")
_Rstp_ObjectIdentity = ObjectIdentity
rstp = _Rstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 11)
)


class _RstpEnable_Type(Integer32):
    """Custom type rstpEnable based on Integer32"""
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


_RstpEnable_Type.__name__ = "Integer32"
_RstpEnable_Object = MibScalar
rstpEnable = _RstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 11, 1),
    _RstpEnable_Type()
)
rstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpEnable.setStatus("current")
_VlanIsolation_ObjectIdentity = ObjectIdentity
vlanIsolation = _VlanIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 12)
)
_VlanIsolationTable_Object = MibTable
vlanIsolationTable = _VlanIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 12, 1)
)
if mibBuilder.loadTexts:
    vlanIsolationTable.setStatus("current")
_VlanIsolationEntry_Object = MibTableRow
vlanIsolationEntry = _VlanIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 12, 1, 1)
)
vlanIsolationEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanIsolationEntry.setStatus("current")
_VlanIsolationRowStatus_Type = RowStatus
_VlanIsolationRowStatus_Object = MibTableColumn
vlanIsolationRowStatus = _VlanIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 12, 1, 1, 1),
    _VlanIsolationRowStatus_Type()
)
vlanIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIsolationRowStatus.setStatus("current")
_EnetMtu_ObjectIdentity = ObjectIdentity
enetMtu = _EnetMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 13)
)
_EnetMtuEntry_Type = Integer32
_EnetMtuEntry_Object = MibScalar
enetMtuEntry = _EnetMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 13, 1),
    _EnetMtuEntry_Type()
)
enetMtuEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetMtuEntry.setStatus("current")
_Tpid_ObjectIdentity = ObjectIdentity
tpid = _Tpid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 14)
)
_TpidEntry_Type = Unsigned32
_TpidEntry_Object = MibScalar
tpidEntry = _TpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 14, 1),
    _TpidEntry_Type()
)
tpidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpidEntry.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51)
)


class _DhcpRelayEnable_Type(Integer32):
    """Custom type dhcpRelayEnable based on Integer32"""
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


_DhcpRelayEnable_Type.__name__ = "Integer32"
_DhcpRelayEnable_Object = MibScalar
dhcpRelayEnable = _DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 1),
    _DhcpRelayEnable_Type()
)
dhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnable.setStatus("current")
_DhcpRelay82Table_Object = MibTable
dhcpRelay82Table = _DhcpRelay82Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2)
)
if mibBuilder.loadTexts:
    dhcpRelay82Table.setStatus("current")
_DhcpRelay82Entry_Object = MibTableRow
dhcpRelay82Entry = _DhcpRelay82Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1)
)
dhcpRelay82Entry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelay82Entry.setStatus("current")
_DhcpRelay82PrimaryServer_Type = IpAddress
_DhcpRelay82PrimaryServer_Object = MibTableColumn
dhcpRelay82PrimaryServer = _DhcpRelay82PrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 1),
    _DhcpRelay82PrimaryServer_Type()
)
dhcpRelay82PrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82PrimaryServer.setStatus("current")
_DhcpRelay82SecondaryServer_Type = IpAddress
_DhcpRelay82SecondaryServer_Object = MibTableColumn
dhcpRelay82SecondaryServer = _DhcpRelay82SecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 2),
    _DhcpRelay82SecondaryServer_Type()
)
dhcpRelay82SecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82SecondaryServer.setStatus("current")


class _DhcpRelay82ActiveServer_Type(Integer32):
    """Custom type dhcpRelay82ActiveServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("none", 3))
    )


_DhcpRelay82ActiveServer_Type.__name__ = "Integer32"
_DhcpRelay82ActiveServer_Object = MibTableColumn
dhcpRelay82ActiveServer = _DhcpRelay82ActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 3),
    _DhcpRelay82ActiveServer_Type()
)
dhcpRelay82ActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82ActiveServer.setStatus("current")


class _DhcpRelay82Enable_Type(Integer32):
    """Custom type dhcpRelay82Enable based on Integer32"""
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


_DhcpRelay82Enable_Type.__name__ = "Integer32"
_DhcpRelay82Enable_Object = MibTableColumn
dhcpRelay82Enable = _DhcpRelay82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 4),
    _DhcpRelay82Enable_Type()
)
dhcpRelay82Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Enable.setStatus("current")


class _DhcpRelay82Info_Type(DisplayString):
    """Custom type dhcpRelay82Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelay82Info_Type.__name__ = "DisplayString"
_DhcpRelay82Info_Object = MibTableColumn
dhcpRelay82Info = _DhcpRelay82Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 5),
    _DhcpRelay82Info_Type()
)
dhcpRelay82Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Info.setStatus("current")


class _DhcpRelay82RelayMode_Type(Integer32):
    """Custom type dhcpRelay82RelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("both", 2))
    )


_DhcpRelay82RelayMode_Type.__name__ = "Integer32"
_DhcpRelay82RelayMode_Object = MibTableColumn
dhcpRelay82RelayMode = _DhcpRelay82RelayMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 6),
    _DhcpRelay82RelayMode_Type()
)
dhcpRelay82RelayMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82RelayMode.setStatus("current")
_DhcpRelay82RowStatus_Type = RowStatus
_DhcpRelay82RowStatus_Object = MibTableColumn
dhcpRelay82RowStatus = _DhcpRelay82RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 7),
    _DhcpRelay82RowStatus_Type()
)
dhcpRelay82RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82RowStatus.setStatus("current")


class _DhcpRelay82Suboption2Enable_Type(Integer32):
    """Custom type dhcpRelay82Suboption2Enable based on Integer32"""
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


_DhcpRelay82Suboption2Enable_Type.__name__ = "Integer32"
_DhcpRelay82Suboption2Enable_Object = MibTableColumn
dhcpRelay82Suboption2Enable = _DhcpRelay82Suboption2Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 8),
    _DhcpRelay82Suboption2Enable_Type()
)
dhcpRelay82Suboption2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Enable.setStatus("current")
_DhcpRelay82Suboption2Info_Type = DisplayString
_DhcpRelay82Suboption2Info_Object = MibTableColumn
dhcpRelay82Suboption2Info = _DhcpRelay82Suboption2Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 9),
    _DhcpRelay82Suboption2Info_Type()
)
dhcpRelay82Suboption2Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Info.setStatus("current")


class _DhcpRelay82EntryEnable_Type(Integer32):
    """Custom type dhcpRelay82EntryEnable based on Integer32"""
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


_DhcpRelay82EntryEnable_Type.__name__ = "Integer32"
_DhcpRelay82EntryEnable_Object = MibTableColumn
dhcpRelay82EntryEnable = _DhcpRelay82EntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 10),
    _DhcpRelay82EntryEnable_Type()
)
dhcpRelay82EntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryEnable.setStatus("current")


class _DhcpRelay82EntryOptionMode_Type(Integer32):
    """Custom type dhcpRelay82EntryOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2))
    )


_DhcpRelay82EntryOptionMode_Type.__name__ = "Integer32"
_DhcpRelay82EntryOptionMode_Object = MibTableColumn
dhcpRelay82EntryOptionMode = _DhcpRelay82EntryOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 2, 1, 11),
    _DhcpRelay82EntryOptionMode_Type()
)
dhcpRelay82EntryOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryOptionMode.setStatus("current")


class _DhcpRelayOption82Sub1Info_Type(DisplayString):
    """Custom type dhcpRelayOption82Sub1Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelayOption82Sub1Info_Type.__name__ = "DisplayString"
_DhcpRelayOption82Sub1Info_Object = MibScalar
dhcpRelayOption82Sub1Info = _DhcpRelayOption82Sub1Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 3),
    _DhcpRelayOption82Sub1Info_Type()
)
dhcpRelayOption82Sub1Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub1Info.setStatus("current")
_MaxNumOfDhcpRelay82Conf_Type = Integer32
_MaxNumOfDhcpRelay82Conf_Object = MibScalar
maxNumOfDhcpRelay82Conf = _MaxNumOfDhcpRelay82Conf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 4),
    _MaxNumOfDhcpRelay82Conf_Type()
)
maxNumOfDhcpRelay82Conf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDhcpRelay82Conf.setStatus("current")


class _DhcpRelayOption82Sub1Enable_Type(Integer32):
    """Custom type dhcpRelayOption82Sub1Enable based on Integer32"""
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


_DhcpRelayOption82Sub1Enable_Type.__name__ = "Integer32"
_DhcpRelayOption82Sub1Enable_Object = MibScalar
dhcpRelayOption82Sub1Enable = _DhcpRelayOption82Sub1Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 5),
    _DhcpRelayOption82Sub1Enable_Type()
)
dhcpRelayOption82Sub1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub1Enable.setStatus("current")


class _DhcpRelayOption82Sub2Info_Type(DisplayString):
    """Custom type dhcpRelayOption82Sub2Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelayOption82Sub2Info_Type.__name__ = "DisplayString"
_DhcpRelayOption82Sub2Info_Object = MibScalar
dhcpRelayOption82Sub2Info = _DhcpRelayOption82Sub2Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 6),
    _DhcpRelayOption82Sub2Info_Type()
)
dhcpRelayOption82Sub2Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub2Info.setStatus("current")


class _DhcpRelayOption82Sub2Enable_Type(Integer32):
    """Custom type dhcpRelayOption82Sub2Enable based on Integer32"""
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


_DhcpRelayOption82Sub2Enable_Type.__name__ = "Integer32"
_DhcpRelayOption82Sub2Enable_Object = MibScalar
dhcpRelayOption82Sub2Enable = _DhcpRelayOption82Sub2Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 51, 7),
    _DhcpRelayOption82Sub2Enable_Type()
)
dhcpRelayOption82Sub2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub2Enable.setStatus("current")
_Macfilter_ObjectIdentity = ObjectIdentity
macfilter = _Macfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53)
)
_MacFilterPortTable_Object = MibTable
macFilterPortTable = _MacFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 1)
)
if mibBuilder.loadTexts:
    macFilterPortTable.setStatus("current")
_MacFilterPortEntry_Object = MibTableRow
macFilterPortEntry = _MacFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 1, 1)
)
macFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    macFilterPortEntry.setStatus("current")


class _MacFilterPortEnable_Type(Integer32):
    """Custom type macFilterPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("enableMacFilter", 1),
          ("enableMacCount", 2),
          ("disable", 4),
          ("enableMacFilterAndMacCount", 5))
    )


_MacFilterPortEnable_Type.__name__ = "Integer32"
_MacFilterPortEnable_Object = MibTableColumn
macFilterPortEnable = _MacFilterPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 1, 1, 1),
    _MacFilterPortEnable_Type()
)
macFilterPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortEnable.setStatus("current")


class _MacFilterPortMacCount_Type(Integer32):
    """Custom type macFilterPortMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MacFilterPortMacCount_Type.__name__ = "Integer32"
_MacFilterPortMacCount_Object = MibTableColumn
macFilterPortMacCount = _MacFilterPortMacCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 1, 1, 2),
    _MacFilterPortMacCount_Type()
)
macFilterPortMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortMacCount.setStatus("current")


class _MacFilterPortFilterMode_Type(Integer32):
    """Custom type macFilterPortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MacFilterPortFilterMode_Type.__name__ = "Integer32"
_MacFilterPortFilterMode_Object = MibTableColumn
macFilterPortFilterMode = _MacFilterPortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 1, 1, 3),
    _MacFilterPortFilterMode_Type()
)
macFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortFilterMode.setStatus("current")
_MaxNumOfMacFiltersInSystem_Type = Integer32
_MaxNumOfMacFiltersInSystem_Object = MibScalar
maxNumOfMacFiltersInSystem = _MaxNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 2),
    _MaxNumOfMacFiltersInSystem_Type()
)
maxNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersInSystem.setStatus("current")
_MaxNumOfMacFiltersPerPort_Type = Integer32
_MaxNumOfMacFiltersPerPort_Object = MibScalar
maxNumOfMacFiltersPerPort = _MaxNumOfMacFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 3),
    _MaxNumOfMacFiltersPerPort_Type()
)
maxNumOfMacFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersPerPort.setStatus("current")
_CurrNumOfMacFiltersInSystem_Type = Integer32
_CurrNumOfMacFiltersInSystem_Object = MibScalar
currNumOfMacFiltersInSystem = _CurrNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 4),
    _CurrNumOfMacFiltersInSystem_Type()
)
currNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currNumOfMacFiltersInSystem.setStatus("current")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 5)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("current")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 5, 1)
)
macFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "macFilterAddr"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("current")
_MacFilterAddr_Type = PhysAddress
_MacFilterAddr_Object = MibTableColumn
macFilterAddr = _MacFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 5, 1, 1),
    _MacFilterAddr_Type()
)
macFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterAddr.setStatus("current")
_MacFilterRowStatus_Type = RowStatus
_MacFilterRowStatus_Object = MibTableColumn
macFilterRowStatus = _MacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 5, 1, 2),
    _MacFilterRowStatus_Type()
)
macFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterRowStatus.setStatus("current")
_MacfilterBatchSet_ObjectIdentity = ObjectIdentity
macfilterBatchSet = _MacfilterBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 6)
)
_MacfilterTarget_Type = OctetString
_MacfilterTarget_Object = MibScalar
macfilterTarget = _MacfilterTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 6, 1),
    _MacfilterTarget_Type()
)
macfilterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterTarget.setStatus("current")
_MacfilterOps_Type = Integer32
_MacfilterOps_Object = MibScalar
macfilterOps = _MacfilterOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 6, 2),
    _MacfilterOps_Type()
)
macfilterOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterOps.setStatus("current")


class _MacFilterMacCountForBatchSet_Type(Integer32):
    """Custom type macFilterMacCountForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MacFilterMacCountForBatchSet_Type.__name__ = "Integer32"
_MacFilterMacCountForBatchSet_Object = MibScalar
macFilterMacCountForBatchSet = _MacFilterMacCountForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 6, 3),
    _MacFilterMacCountForBatchSet_Type()
)
macFilterMacCountForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMacCountForBatchSet.setStatus("current")
_OuiFilterTable_Object = MibTable
ouiFilterTable = _OuiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 7)
)
if mibBuilder.loadTexts:
    ouiFilterTable.setStatus("current")
_OuiFilterEntry_Object = MibTableRow
ouiFilterEntry = _OuiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 7, 1)
)
ouiFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "ouiFilterAddr"),
)
if mibBuilder.loadTexts:
    ouiFilterEntry.setStatus("current")
_OuiFilterAddr_Type = OctetString
_OuiFilterAddr_Object = MibTableColumn
ouiFilterAddr = _OuiFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 7, 1, 1),
    _OuiFilterAddr_Type()
)
ouiFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ouiFilterAddr.setStatus("current")
_OuiFilterRowStatus_Type = RowStatus
_OuiFilterRowStatus_Object = MibTableColumn
ouiFilterRowStatus = _OuiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 7, 1, 2),
    _OuiFilterRowStatus_Type()
)
ouiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ouiFilterRowStatus.setStatus("current")
_MaxNumOfOuiFiltersPerPort_Type = Integer32
_MaxNumOfOuiFiltersPerPort_Object = MibScalar
maxNumOfOuiFiltersPerPort = _MaxNumOfOuiFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 8),
    _MaxNumOfOuiFiltersPerPort_Type()
)
maxNumOfOuiFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersPerPort.setStatus("current")
_OuiFilterPortTable_Object = MibTable
ouiFilterPortTable = _OuiFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 9)
)
if mibBuilder.loadTexts:
    ouiFilterPortTable.setStatus("current")
_OuiFilterPortEntry_Object = MibTableRow
ouiFilterPortEntry = _OuiFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 9, 1)
)
ouiFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ouiFilterPortEntry.setStatus("current")


class _OuiFilterPortEnable_Type(Integer32):
    """Custom type ouiFilterPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableOuiFilter", 1),
          ("disable", 2))
    )


_OuiFilterPortEnable_Type.__name__ = "Integer32"
_OuiFilterPortEnable_Object = MibTableColumn
ouiFilterPortEnable = _OuiFilterPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 9, 1, 1),
    _OuiFilterPortEnable_Type()
)
ouiFilterPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortEnable.setStatus("current")


class _OuiFilterPortFilterMode_Type(Integer32):
    """Custom type ouiFilterPortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_OuiFilterPortFilterMode_Type.__name__ = "Integer32"
_OuiFilterPortFilterMode_Object = MibTableColumn
ouiFilterPortFilterMode = _OuiFilterPortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 53, 9, 1, 2),
    _OuiFilterPortFilterMode_Type()
)
ouiFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortFilterMode.setStatus("current")
_DhcpSnoop_ObjectIdentity = ObjectIdentity
dhcpSnoop = _DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55)
)
_DhcpSnoopPortTable_Object = MibTable
dhcpSnoopPortTable = _DhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortTable.setStatus("current")
_DhcpSnoopPortEntry_Object = MibTableRow
dhcpSnoopPortEntry = _DhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 1, 1)
)
dhcpSnoopPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortEntry.setStatus("current")


class _DhcpSnoopEnable_Type(Integer32):
    """Custom type dhcpSnoopEnable based on Integer32"""
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


_DhcpSnoopEnable_Type.__name__ = "Integer32"
_DhcpSnoopEnable_Object = MibTableColumn
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 1, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopTarget_Type = OctetString
_DhcpSnoopTarget_Object = MibScalar
dhcpSnoopTarget = _DhcpSnoopTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 2),
    _DhcpSnoopTarget_Type()
)
dhcpSnoopTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopTarget.setStatus("current")
_DhcpSnoopOps_Type = Integer32
_DhcpSnoopOps_Object = MibScalar
dhcpSnoopOps = _DhcpSnoopOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 3),
    _DhcpSnoopOps_Type()
)
dhcpSnoopOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOps.setStatus("current")
_DhcpStaticTable_Object = MibTable
dhcpStaticTable = _DhcpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 4)
)
if mibBuilder.loadTexts:
    dhcpStaticTable.setStatus("current")
_DhcpStaticEntry_Object = MibTableRow
dhcpStaticEntry = _DhcpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 4, 1)
)
dhcpStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "dhcpStaticIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpStaticEntry.setStatus("current")
_DhcpStaticIpAddr_Type = IpAddress
_DhcpStaticIpAddr_Object = MibTableColumn
dhcpStaticIpAddr = _DhcpStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 4, 1, 1),
    _DhcpStaticIpAddr_Type()
)
dhcpStaticIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIpAddr.setStatus("current")
_DhcpStaticRowStatus_Type = RowStatus
_DhcpStaticRowStatus_Object = MibTableColumn
dhcpStaticRowStatus = _DhcpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 4, 1, 2),
    _DhcpStaticRowStatus_Type()
)
dhcpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticRowStatus.setStatus("current")
_MaxNumOfDhcpStaticIp_Type = Integer32
_MaxNumOfDhcpStaticIp_Object = MibScalar
maxNumOfDhcpStaticIp = _MaxNumOfDhcpStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 55, 5),
    _MaxNumOfDhcpStaticIp_Type()
)
maxNumOfDhcpStaticIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDhcpStaticIp.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56)
)
_AclSetTable_Object = MibTable
aclSetTable = _AclSetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 1)
)
if mibBuilder.loadTexts:
    aclSetTable.setStatus("current")
_AclSetEntry_Object = MibTableRow
aclSetEntry = _AclSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 1, 1)
)
aclSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "aclSetVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "aclSetVci"),
    (0, "ZYXEL-VES1608FE53A-MIB", "aclSetProfileName"),
)
if mibBuilder.loadTexts:
    aclSetEntry.setStatus("current")
_AclSetVpi_Type = Integer32
_AclSetVpi_Object = MibTableColumn
aclSetVpi = _AclSetVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 1, 1, 1),
    _AclSetVpi_Type()
)
aclSetVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVpi.setStatus("current")
_AclSetVci_Type = Integer32
_AclSetVci_Object = MibTableColumn
aclSetVci = _AclSetVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 1, 1, 2),
    _AclSetVci_Type()
)
aclSetVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVci.setStatus("current")
_AclSetProfileName_Type = DisplayString
_AclSetProfileName_Object = MibTableColumn
aclSetProfileName = _AclSetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 1, 1, 3),
    _AclSetProfileName_Type()
)
aclSetProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetProfileName.setStatus("current")
_AclSetRowStatus_Type = RowStatus
_AclSetRowStatus_Object = MibTableColumn
aclSetRowStatus = _AclSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 1, 1, 4),
    _AclSetRowStatus_Type()
)
aclSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSetRowStatus.setStatus("current")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "aclProfileRuleName"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")
_AclProfileRuleName_Type = DisplayString
_AclProfileRuleName_Object = MibTableColumn
aclProfileRuleName = _AclProfileRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 1),
    _AclProfileRuleName_Type()
)
aclProfileRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleName.setStatus("current")
_AclProfileRuleNumber_Type = Integer32
_AclProfileRuleNumber_Object = MibTableColumn
aclProfileRuleNumber = _AclProfileRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 2),
    _AclProfileRuleNumber_Type()
)
aclProfileRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleNumber.setStatus("current")
_AclProfileActionNumber_Type = Integer32
_AclProfileActionNumber_Object = MibTableColumn
aclProfileActionNumber = _AclProfileActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 3),
    _AclProfileActionNumber_Type()
)
aclProfileActionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionNumber.setStatus("current")
_AclProfileRuleParamMask_Type = Integer32
_AclProfileRuleParamMask_Object = MibTableColumn
aclProfileRuleParamMask = _AclProfileRuleParamMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 4),
    _AclProfileRuleParamMask_Type()
)
aclProfileRuleParamMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleParamMask.setStatus("current")


class _AclProfileRuleEtype_Type(Integer32):
    """Custom type aclProfileRuleEtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleEtype_Type.__name__ = "Integer32"
_AclProfileRuleEtype_Object = MibTableColumn
aclProfileRuleEtype = _AclProfileRuleEtype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 5),
    _AclProfileRuleEtype_Type()
)
aclProfileRuleEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleEtype.setStatus("current")


class _AclProfileRuleVid_Type(Integer32):
    """Custom type aclProfileRuleVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclProfileRuleVid_Type.__name__ = "Integer32"
_AclProfileRuleVid_Object = MibTableColumn
aclProfileRuleVid = _AclProfileRuleVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 6),
    _AclProfileRuleVid_Type()
)
aclProfileRuleVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleVid.setStatus("current")
_AclProfileRuleSmac_Type = PhysAddress
_AclProfileRuleSmac_Object = MibTableColumn
aclProfileRuleSmac = _AclProfileRuleSmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 7),
    _AclProfileRuleSmac_Type()
)
aclProfileRuleSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSmac.setStatus("current")
_AclProfileRuleDmac_Type = PhysAddress
_AclProfileRuleDmac_Object = MibTableColumn
aclProfileRuleDmac = _AclProfileRuleDmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 8),
    _AclProfileRuleDmac_Type()
)
aclProfileRuleDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDmac.setStatus("current")


class _AclProfileRulePriority_Type(Integer32):
    """Custom type aclProfileRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileRulePriority_Type.__name__ = "Integer32"
_AclProfileRulePriority_Object = MibTableColumn
aclProfileRulePriority = _AclProfileRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 9),
    _AclProfileRulePriority_Type()
)
aclProfileRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRulePriority.setStatus("current")


class _AclProfileRuleProtocol_Type(Integer32):
    """Custom type aclProfileRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleProtocol_Type.__name__ = "Integer32"
_AclProfileRuleProtocol_Object = MibTableColumn
aclProfileRuleProtocol = _AclProfileRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 10),
    _AclProfileRuleProtocol_Type()
)
aclProfileRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleProtocol.setStatus("current")


class _AclProfileActionRate_Type(Integer32):
    """Custom type aclProfileActionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65472),
    )


_AclProfileActionRate_Type.__name__ = "Integer32"
_AclProfileActionRate_Object = MibTableColumn
aclProfileActionRate = _AclProfileActionRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 21),
    _AclProfileActionRate_Type()
)
aclProfileActionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionRate.setStatus("current")


class _AclProfileActionrvlan_Type(Integer32):
    """Custom type aclProfileActionrvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclProfileActionrvlan_Type.__name__ = "Integer32"
_AclProfileActionrvlan_Object = MibTableColumn
aclProfileActionrvlan = _AclProfileActionrvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 22),
    _AclProfileActionrvlan_Type()
)
aclProfileActionrvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrvlan.setStatus("current")


class _AclProfileActionrpri_Type(Integer32):
    """Custom type aclProfileActionrpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileActionrpri_Type.__name__ = "Integer32"
_AclProfileActionrpri_Object = MibTableColumn
aclProfileActionrpri = _AclProfileActionrpri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 23),
    _AclProfileActionrpri_Type()
)
aclProfileActionrpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrpri.setStatus("current")
_AclProfileRowStatus_Type = RowStatus
_AclProfileRowStatus_Object = MibTableColumn
aclProfileRowStatus = _AclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 24),
    _AclProfileRowStatus_Type()
)
aclProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRowStatus.setStatus("current")
_AclProfileRuleSip_Type = IpAddress
_AclProfileRuleSip_Object = MibTableColumn
aclProfileRuleSip = _AclProfileRuleSip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 25),
    _AclProfileRuleSip_Type()
)
aclProfileRuleSip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSip.setStatus("current")
_AclProfileRuleDip_Type = IpAddress
_AclProfileRuleDip_Object = MibTableColumn
aclProfileRuleDip = _AclProfileRuleDip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 26),
    _AclProfileRuleDip_Type()
)
aclProfileRuleDip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDip.setStatus("current")


class _AclProfileRuleSport_Type(Integer32):
    """Custom type aclProfileRuleSport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSport_Type.__name__ = "Integer32"
_AclProfileRuleSport_Object = MibTableColumn
aclProfileRuleSport = _AclProfileRuleSport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 27),
    _AclProfileRuleSport_Type()
)
aclProfileRuleSport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSport.setStatus("current")


class _AclProfileRuleDport_Type(Integer32):
    """Custom type aclProfileRuleDport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDport_Type.__name__ = "Integer32"
_AclProfileRuleDport_Object = MibTableColumn
aclProfileRuleDport = _AclProfileRuleDport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 56, 2, 1, 28),
    _AclProfileRuleDport_Type()
)
aclProfileRuleDport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDport.setStatus("current")
_PppoeAgent_ObjectIdentity = ObjectIdentity
pppoeAgent = _PppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57)
)
_PppoeAgentTable_Object = MibTable
pppoeAgentTable = _PppoeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 1)
)
if mibBuilder.loadTexts:
    pppoeAgentTable.setStatus("current")
_PppoeAgentEntry_Object = MibTableRow
pppoeAgentEntry = _PppoeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 1, 1)
)
pppoeAgentEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    pppoeAgentEntry.setStatus("current")


class _PppoeAgentEnable_Type(Integer32):
    """Custom type pppoeAgentEnable based on Integer32"""
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


_PppoeAgentEnable_Type.__name__ = "Integer32"
_PppoeAgentEnable_Object = MibTableColumn
pppoeAgentEnable = _PppoeAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 1, 1, 1),
    _PppoeAgentEnable_Type()
)
pppoeAgentEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentEnable.setStatus("current")


class _PppoeAgentInfo_Type(DisplayString):
    """Custom type pppoeAgentInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_PppoeAgentInfo_Type.__name__ = "DisplayString"
_PppoeAgentInfo_Object = MibTableColumn
pppoeAgentInfo = _PppoeAgentInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 1, 1, 2),
    _PppoeAgentInfo_Type()
)
pppoeAgentInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentInfo.setStatus("current")
_PppoeAgentRowStatus_Type = RowStatus
_PppoeAgentRowStatus_Object = MibTableColumn
pppoeAgentRowStatus = _PppoeAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 1, 1, 3),
    _PppoeAgentRowStatus_Type()
)
pppoeAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentRowStatus.setStatus("current")


class _PppoeAgentOptionMode_Type(Integer32):
    """Custom type pppoeAgentOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2))
    )


_PppoeAgentOptionMode_Type.__name__ = "Integer32"
_PppoeAgentOptionMode_Object = MibTableColumn
pppoeAgentOptionMode = _PppoeAgentOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 1, 1, 4),
    _PppoeAgentOptionMode_Type()
)
pppoeAgentOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentOptionMode.setStatus("current")
_MaxNumOfPppoeDhcpRelay82Conf_Type = Integer32
_MaxNumOfPppoeDhcpRelay82Conf_Object = MibScalar
maxNumOfPppoeDhcpRelay82Conf = _MaxNumOfPppoeDhcpRelay82Conf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 57, 2),
    _MaxNumOfPppoeDhcpRelay82Conf_Type()
)
maxNumOfPppoeDhcpRelay82Conf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPppoeDhcpRelay82Conf.setStatus("current")
_N1mac_ObjectIdentity = ObjectIdentity
n1mac = _N1mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 58)
)
_N1macReplaceMac_Type = MacAddress
_N1macReplaceMac_Object = MibScalar
n1macReplaceMac = _N1macReplaceMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 58, 1),
    _N1macReplaceMac_Type()
)
n1macReplaceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macReplaceMac.setStatus("current")
_N1macPortTable_Object = MibTable
n1macPortTable = _N1macPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 58, 2)
)
if mibBuilder.loadTexts:
    n1macPortTable.setStatus("current")
_N1macPortEntry_Object = MibTableRow
n1macPortEntry = _N1macPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 58, 2, 1)
)
n1macPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    n1macPortEntry.setStatus("current")


class _N1macStatusEnable_Type(Integer32):
    """Custom type n1macStatusEnable based on Integer32"""
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


_N1macStatusEnable_Type.__name__ = "Integer32"
_N1macStatusEnable_Object = MibTableColumn
n1macStatusEnable = _N1macStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 58, 2, 1, 1),
    _N1macStatusEnable_Type()
)
n1macStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n1macStatusEnable.setStatus("current")
_EnetPort_ObjectIdentity = ObjectIdentity
enetPort = _EnetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59)
)
_EnetPortConfTable_Object = MibTable
enetPortConfTable = _EnetPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59, 1)
)
if mibBuilder.loadTexts:
    enetPortConfTable.setStatus("current")
_EnetPortConfEntry_Object = MibTableRow
enetPortConfEntry = _EnetPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59, 1, 1)
)
enetPortConfEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "enetPortId"),
)
if mibBuilder.loadTexts:
    enetPortConfEntry.setStatus("current")
_EnetPortId_Type = Integer32
_EnetPortId_Object = MibTableColumn
enetPortId = _EnetPortId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59, 1, 1, 1),
    _EnetPortId_Type()
)
enetPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortId.setStatus("current")


class _EnetPortType_Type(Integer32):
    """Custom type enetPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("e1000BaseT", 2),
          ("e1000BaseLX", 3),
          ("e1000BaseSX", 4),
          ("e100BaseFX", 5),
          ("e100BaseTX", 6),
          ("e1000BaseGBIC", 7))
    )


_EnetPortType_Type.__name__ = "Integer32"
_EnetPortType_Object = MibTableColumn
enetPortType = _EnetPortType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59, 1, 1, 2),
    _EnetPortType_Type()
)
enetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortType.setStatus("current")
_EnetPortIfIndex_Type = Integer32
_EnetPortIfIndex_Object = MibTableColumn
enetPortIfIndex = _EnetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59, 1, 1, 3),
    _EnetPortIfIndex_Type()
)
enetPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortIfIndex.setStatus("current")


class _EnetPortSpeed_Type(Integer32):
    """Custom type enetPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("e1000M", 2),
          ("e100M", 3))
    )


_EnetPortSpeed_Type.__name__ = "Integer32"
_EnetPortSpeed_Object = MibTableColumn
enetPortSpeed = _EnetPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 59, 1, 1, 4),
    _EnetPortSpeed_Type()
)
enetPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetPortSpeed.setStatus("current")
_Macff_ObjectIdentity = ObjectIdentity
macff = _Macff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60)
)
_MacFfTable_Object = MibTable
macFfTable = _MacFfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1)
)
if mibBuilder.loadTexts:
    macFfTable.setStatus("current")
_MacFfEntry_Object = MibTableRow
macFfEntry = _MacFfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1)
)
macFfEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "macFfIndex"),
)
if mibBuilder.loadTexts:
    macFfEntry.setStatus("current")
_MacFfIndex_Type = Integer32
_MacFfIndex_Object = MibTableColumn
macFfIndex = _MacFfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 1),
    _MacFfIndex_Type()
)
macFfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfIndex.setStatus("current")
_MacFfVid_Type = Integer32
_MacFfVid_Object = MibTableColumn
macFfVid = _MacFfVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 2),
    _MacFfVid_Type()
)
macFfVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfVid.setStatus("current")
_MacFfArIP_Type = IpAddress
_MacFfArIP_Object = MibTableColumn
macFfArIP = _MacFfArIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 3),
    _MacFfArIP_Type()
)
macFfArIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArIP.setStatus("current")
_MacFfSrcIP_Type = IpAddress
_MacFfSrcIP_Object = MibTableColumn
macFfSrcIP = _MacFfSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 4),
    _MacFfSrcIP_Type()
)
macFfSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfSrcIP.setStatus("current")
_MacFfSrcMask_Type = Integer32
_MacFfSrcMask_Object = MibTableColumn
macFfSrcMask = _MacFfSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 5),
    _MacFfSrcMask_Type()
)
macFfSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfSrcMask.setStatus("current")
_MacFfArMac_Type = PhysAddress
_MacFfArMac_Object = MibTableColumn
macFfArMac = _MacFfArMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 6),
    _MacFfArMac_Type()
)
macFfArMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArMac.setStatus("current")
_MacFfRowStatus_Type = RowStatus
_MacFfRowStatus_Object = MibTableColumn
macFfRowStatus = _MacFfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 1, 1, 7),
    _MacFfRowStatus_Type()
)
macFfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfRowStatus.setStatus("current")
_MacFfArpAgingTime_Type = Integer32
_MacFfArpAgingTime_Object = MibScalar
macFfArpAgingTime = _MacFfArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 2),
    _MacFfArpAgingTime_Type()
)
macFfArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArpAgingTime.setStatus("current")
_MacFfArpFlush_Type = Integer32
_MacFfArpFlush_Object = MibScalar
macFfArpFlush = _MacFfArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 60, 3),
    _MacFfArpFlush_Type()
)
macFfArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArpFlush.setStatus("current")


class _ManagementPriority_Type(Integer32):
    """Custom type managementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ManagementPriority_Type.__name__ = "Integer32"
_ManagementPriority_Object = MibScalar
managementPriority = _ManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 61),
    _ManagementPriority_Type()
)
managementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementPriority.setStatus("current")
_MacAntiSpoof_ObjectIdentity = ObjectIdentity
macAntiSpoof = _MacAntiSpoof_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 62)
)


class _MacAntiSpoofEnable_Type(Integer32):
    """Custom type macAntiSpoofEnable based on Integer32"""
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


_MacAntiSpoofEnable_Type.__name__ = "Integer32"
_MacAntiSpoofEnable_Object = MibScalar
macAntiSpoofEnable = _MacAntiSpoofEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 10, 62, 1),
    _MacAntiSpoofEnable_Type()
)
macAntiSpoofEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAntiSpoofEnable.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11)
)
_SysState_ObjectIdentity = ObjectIdentity
sysState = _SysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 1)
)
_SystemStatus_Type = Integer32
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 1, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_ProblemCause_Type = DisplayString
_ProblemCause_Object = MibScalar
problemCause = _ProblemCause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 1, 2),
    _ProblemCause_Type()
)
problemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    problemCause.setStatus("current")
_HwMonitor_ObjectIdentity = ObjectIdentity
hwMonitor = _HwMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3)
)
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1)
)
voltageEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 2),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageCurValue.setUnits("milli-voltage")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 3),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageMaxValue.setUnits("milli-voltage")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 4),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageMinValue.setUnits("milli-voltage")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 5),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageNominalValue.setUnits("milli-voltage")
_VoltageLowThresh_Type = Integer32
_VoltageLowThresh_Object = MibTableColumn
voltageLowThresh = _VoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 6),
    _VoltageLowThresh_Type()
)
voltageLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    voltageLowThresh.setUnits("milli-voltage")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 2, 1, 7),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("current")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1)
)
temperatureEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("current")
_TemperatureIndex_Type = Integer32
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")
_TemperatureCurValue_Type = Integer32
_TemperatureCurValue_Object = MibTableColumn
temperatureCurValue = _TemperatureCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1, 2),
    _TemperatureCurValue_Type()
)
temperatureCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCurValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCurValue.setUnits("Celsius")
_TemperatureMaxValue_Type = Integer32
_TemperatureMaxValue_Object = MibTableColumn
temperatureMaxValue = _TemperatureMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1, 3),
    _TemperatureMaxValue_Type()
)
temperatureMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureMaxValue.setUnits("Celsius")
_TemperatureMinValue_Type = Integer32
_TemperatureMinValue_Object = MibTableColumn
temperatureMinValue = _TemperatureMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1, 4),
    _TemperatureMinValue_Type()
)
temperatureMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMinValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureMinValue.setUnits("Celsius")
_TemperatureHighThresh_Type = Integer32
_TemperatureHighThresh_Object = MibTableColumn
temperatureHighThresh = _TemperatureHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1, 5),
    _TemperatureHighThresh_Type()
)
temperatureHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    temperatureHighThresh.setUnits("Celsius")
_TemperatureDescr_Type = DisplayString
_TemperatureDescr_Object = MibTableColumn
temperatureDescr = _TemperatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 3, 3, 1, 6),
    _TemperatureDescr_Type()
)
temperatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDescr.setStatus("current")
_TimeSetup_ObjectIdentity = ObjectIdentity
timeSetup = _TimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4)
)


class _TimeServerMode_Type(Integer32):
    """Custom type timeServerMode based on Integer32"""
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
          ("daytime", 2),
          ("time", 3),
          ("ntp", 4))
    )


_TimeServerMode_Type.__name__ = "Integer32"
_TimeServerMode_Object = MibScalar
timeServerMode = _TimeServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 1),
    _TimeServerMode_Type()
)
timeServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerMode.setStatus("current")
_TimeServerIP_Type = IpAddress
_TimeServerIP_Object = MibScalar
timeServerIP = _TimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 2),
    _TimeServerIP_Type()
)
timeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerIP.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 3),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemDate_Type = DisplayString
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 4),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")


class _SystemTimeZone_Type(Integer32):
    """Custom type systemTimeZone based on Integer32"""
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
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("utc_minus_1200", 1),
          ("utc_minus_1100", 2),
          ("utc_minus_1000", 3),
          ("utc_minus_0900", 4),
          ("utc_minus_0800", 5),
          ("utc_minus_0700", 6),
          ("utc_minus_0600", 7),
          ("utc_minus_0500", 8),
          ("utc_minus_0400", 9),
          ("utc_minus_0300", 10),
          ("utc_minus_0200", 11),
          ("utc_minus_0100", 12),
          ("utc", 13),
          ("utc_plus_0100", 14),
          ("utc_plus_0200", 15),
          ("utc_plus_0300", 16),
          ("utc_plus_0400", 17),
          ("utc_plus_0500", 18),
          ("utc_plus_0600", 19),
          ("utc_plus_0700", 20),
          ("utc_plus_0800", 21),
          ("utc_plus_0900", 22),
          ("utc_plus_1000", 23),
          ("utc_plus_1100", 24),
          ("utc_plus_1200", 25))
    )


_SystemTimeZone_Type.__name__ = "Integer32"
_SystemTimeZone_Object = MibScalar
systemTimeZone = _SystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 5),
    _SystemTimeZone_Type()
)
systemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeZone.setStatus("current")
_TimeServerSync_Type = Integer32
_TimeServerSync_Object = MibScalar
timeServerSync = _TimeServerSync_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 6),
    _TimeServerSync_Type()
)
timeServerSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerSync.setStatus("current")


class _TimeServerSyncStatus_Type(Integer32):
    """Custom type timeServerSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2),
          ("onGoing", 3))
    )


_TimeServerSyncStatus_Type.__name__ = "Integer32"
_TimeServerSyncStatus_Object = MibScalar
timeServerSyncStatus = _TimeServerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 4, 7),
    _TimeServerSyncStatus_Type()
)
timeServerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerSyncStatus.setStatus("current")
_AccessCtrl_ObjectIdentity = ObjectIdentity
accessCtrl = _AccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5)
)
_AccessCtrlTable_Object = MibTable
accessCtrlTable = _AccessCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 1)
)
if mibBuilder.loadTexts:
    accessCtrlTable.setStatus("current")
_AccessCtrlEntry_Object = MibTableRow
accessCtrlEntry = _AccessCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 1, 1)
)
accessCtrlEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "accessCtrlService"),
)
if mibBuilder.loadTexts:
    accessCtrlEntry.setStatus("current")


class _AccessCtrlService_Type(Integer32):
    """Custom type accessCtrlService based on Integer32"""
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
        *(("telnet", 1),
          ("ftp", 2),
          ("web", 3),
          ("icmp", 4))
    )


_AccessCtrlService_Type.__name__ = "Integer32"
_AccessCtrlService_Object = MibTableColumn
accessCtrlService = _AccessCtrlService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 1, 1, 1),
    _AccessCtrlService_Type()
)
accessCtrlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtrlService.setStatus("current")


class _AccessCtrlEnable_Type(Integer32):
    """Custom type accessCtrlEnable based on Integer32"""
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


_AccessCtrlEnable_Type.__name__ = "Integer32"
_AccessCtrlEnable_Object = MibTableColumn
accessCtrlEnable = _AccessCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 1, 1, 2),
    _AccessCtrlEnable_Type()
)
accessCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtrlEnable.setStatus("current")
_AccessCtrlPort_Type = Integer32
_AccessCtrlPort_Object = MibTableColumn
accessCtrlPort = _AccessCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 1, 1, 3),
    _AccessCtrlPort_Type()
)
accessCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtrlPort.setStatus("current")
_MaxNumOfSecuredClients_Type = Integer32
_MaxNumOfSecuredClients_Object = MibScalar
maxNumOfSecuredClients = _MaxNumOfSecuredClients_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 2),
    _MaxNumOfSecuredClients_Type()
)
maxNumOfSecuredClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSecuredClients.setStatus("current")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3, 1, 2),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3, 1, 3),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")
_SecuredClientService_Type = Integer32
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3, 1, 4),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("current")


class _SecuredClientEnable_Type(Integer32):
    """Custom type securedClientEnable based on Integer32"""
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


_SecuredClientEnable_Type.__name__ = "Integer32"
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 5, 3, 1, 5),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 6)
)
_SysLogEnable_Type = Integer32
_SysLogEnable_Object = MibScalar
sysLogEnable = _SysLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 6, 1),
    _SysLogEnable_Type()
)
sysLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogEnable.setStatus("current")
_SysLogServer_Type = IpAddress
_SysLogServer_Object = MibScalar
sysLogServer = _SysLogServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 6, 2),
    _SysLogServer_Type()
)
sysLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServer.setStatus("current")


class _SysLogFacility_Type(Integer32):
    """Custom type sysLogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_SysLogFacility_Type.__name__ = "Integer32"
_SysLogFacility_Object = MibScalar
sysLogFacility = _SysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 6, 3),
    _SysLogFacility_Type()
)
sysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFacility.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7)
)
_MaxNumberOfTrapDestinations_Type = Integer32
_MaxNumberOfTrapDestinations_Object = MibScalar
maxNumberOfTrapDestinations = _MaxNumberOfTrapDestinations_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 1),
    _MaxNumberOfTrapDestinations_Type()
)
maxNumberOfTrapDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfTrapDestinations.setStatus("current")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 2)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("current")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 2, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "trapDestIp"),
    (0, "ZYXEL-VES1608FE53A-MIB", "trapDestPort"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("current")
_TrapDestIp_Type = IpAddress
_TrapDestIp_Object = MibTableColumn
trapDestIp = _TrapDestIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 2, 1, 1),
    _TrapDestIp_Type()
)
trapDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestIp.setStatus("current")
_TrapDestPort_Type = Integer32
_TrapDestPort_Object = MibTableColumn
trapDestPort = _TrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 2, 1, 2),
    _TrapDestPort_Type()
)
trapDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestPort.setStatus("current")
_TrapDestRowStatus_Type = RowStatus
_TrapDestRowStatus_Object = MibTableColumn
trapDestRowStatus = _TrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 2, 1, 3),
    _TrapDestRowStatus_Type()
)
trapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestRowStatus.setStatus("current")
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 3),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("current")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 4),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 7, 5),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_ExtAlarm_ObjectIdentity = ObjectIdentity
extAlarm = _ExtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 8)
)
_ExtAlarmTable_Object = MibTable
extAlarmTable = _ExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 8, 1)
)
if mibBuilder.loadTexts:
    extAlarmTable.setStatus("current")
_ExtAlarmEntry_Object = MibTableRow
extAlarmEntry = _ExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 8, 1, 1)
)
extAlarmEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "extAlarmIndex"),
)
if mibBuilder.loadTexts:
    extAlarmEntry.setStatus("current")
_ExtAlarmIndex_Type = Integer32
_ExtAlarmIndex_Object = MibTableColumn
extAlarmIndex = _ExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 8, 1, 1, 1),
    _ExtAlarmIndex_Type()
)
extAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmIndex.setStatus("current")


class _ExtAlarmName_Type(DisplayString):
    """Custom type extAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmName_Type.__name__ = "DisplayString"
_ExtAlarmName_Object = MibTableColumn
extAlarmName = _ExtAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 8, 1, 1, 2),
    _ExtAlarmName_Type()
)
extAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extAlarmName.setStatus("current")


class _ExtAlarmStatus_Type(DisplayString):
    """Custom type extAlarmStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmStatus_Type.__name__ = "DisplayString"
_ExtAlarmStatus_Object = MibTableColumn
extAlarmStatus = _ExtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 8, 1, 1, 3),
    _ExtAlarmStatus_Type()
)
extAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmStatus.setStatus("current")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9)
)


class _UserAuthMode_Type(Integer32):
    """Custom type userAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("localThenRadius", 3))
    )


_UserAuthMode_Type.__name__ = "Integer32"
_UserAuthMode_Object = MibScalar
userAuthMode = _UserAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 1),
    _UserAuthMode_Type()
)
userAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthMode.setStatus("current")
_UserAuthServerIp_Type = IpAddress
_UserAuthServerIp_Object = MibScalar
userAuthServerIp = _UserAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 2),
    _UserAuthServerIp_Type()
)
userAuthServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerIp.setStatus("current")
_UserAuthServerPort_Type = Integer32
_UserAuthServerPort_Object = MibScalar
userAuthServerPort = _UserAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 3),
    _UserAuthServerPort_Type()
)
userAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerPort.setStatus("current")
_UserAuthServerSecret_Type = OctetString
_UserAuthServerSecret_Object = MibScalar
userAuthServerSecret = _UserAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 4),
    _UserAuthServerSecret_Type()
)
userAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerSecret.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 5)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 5, 1)
)
userEntry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 5, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 5, 1, 2),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")


class _UserPriviledge_Type(Integer32):
    """Custom type userPriviledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("middle", 2),
          ("low", 3))
    )


_UserPriviledge_Type.__name__ = "Integer32"
_UserPriviledge_Object = MibTableColumn
userPriviledge = _UserPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 5, 1, 3),
    _UserPriviledge_Type()
)
userPriviledge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPriviledge.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 5, 1, 4),
    _UserRowStatus_Type()
)
userRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userRowStatus.setStatus("current")


class _UserAuthDefaultPriviledge_Type(Integer32):
    """Custom type userAuthDefaultPriviledge based on Integer32"""
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
        *(("high", 1),
          ("middle", 2),
          ("low", 3),
          ("deny", 4))
    )


_UserAuthDefaultPriviledge_Type.__name__ = "Integer32"
_UserAuthDefaultPriviledge_Object = MibScalar
userAuthDefaultPriviledge = _UserAuthDefaultPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 9, 6),
    _UserAuthDefaultPriviledge_Type()
)
userAuthDefaultPriviledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthDefaultPriviledge.setStatus("current")
_UsbCastCtrl_ObjectIdentity = ObjectIdentity
usbCastCtrl = _UsbCastCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 10)
)


class _UsBcastCtrlEnable_Type(Integer32):
    """Custom type usBcastCtrlEnable based on Integer32"""
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


_UsBcastCtrlEnable_Type.__name__ = "Integer32"
_UsBcastCtrlEnable_Object = MibScalar
usBcastCtrlEnable = _UsBcastCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 10, 1),
    _UsBcastCtrlEnable_Type()
)
usBcastCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usBcastCtrlEnable.setStatus("current")
_UsBcastCtrlRate_Type = Integer32
_UsBcastCtrlRate_Object = MibScalar
usBcastCtrlRate = _UsBcastCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 10, 2),
    _UsBcastCtrlRate_Type()
)
usBcastCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usBcastCtrlRate.setStatus("current")
if mibBuilder.loadTexts:
    usBcastCtrlRate.setUnits("Kbps")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 11)
)
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 11, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_ModuleDescr_Type = DisplayString
_ModuleDescr_Object = MibScalar
moduleDescr = _ModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 11, 2),
    _ModuleDescr_Type()
)
moduleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescr.setStatus("current")
_FWVersion_Type = DisplayString
_FWVersion_Object = MibScalar
fWVersion = _FWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 11, 3),
    _FWVersion_Type()
)
fWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fWVersion.setStatus("current")
_DriverVersion_Type = DisplayString
_DriverVersion_Object = MibScalar
driverVersion = _DriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 11, 4),
    _DriverVersion_Type()
)
driverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverVersion.setStatus("current")
_ModemCodeVersion_Type = DisplayString
_ModemCodeVersion_Object = MibScalar
modemCodeVersion = _ModemCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 11, 5),
    _ModemCodeVersion_Type()
)
modemCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCodeVersion.setStatus("current")
_SysMaintain_ObjectIdentity = ObjectIdentity
sysMaintain = _SysMaintain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90)
)
_MaintenanceOps_Type = Integer32
_MaintenanceOps_Object = MibScalar
maintenanceOps = _MaintenanceOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 1),
    _MaintenanceOps_Type()
)
maintenanceOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceOps.setStatus("current")


class _MaintenanceTarget_Type(Integer32):
    """Custom type maintenanceTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_MaintenanceTarget_Type.__name__ = "Integer32"
_MaintenanceTarget_Object = MibScalar
maintenanceTarget = _MaintenanceTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 2),
    _MaintenanceTarget_Type()
)
maintenanceTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceTarget.setStatus("current")
_MaintenanceDSLConfOps_Type = Integer32
_MaintenanceDSLConfOps_Object = MibScalar
maintenanceDSLConfOps = _MaintenanceDSLConfOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 3),
    _MaintenanceDSLConfOps_Type()
)
maintenanceDSLConfOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfOps.setStatus("current")
_MaintenanceDSLConfTarget_Type = OctetString
_MaintenanceDSLConfTarget_Object = MibScalar
maintenanceDSLConfTarget = _MaintenanceDSLConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 4),
    _MaintenanceDSLConfTarget_Type()
)
maintenanceDSLConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfTarget.setStatus("current")


class _MaintenanceDSLConfProfileName_Type(DisplayString):
    """Custom type maintenanceDSLConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_MaintenanceDSLConfProfileName_Type.__name__ = "DisplayString"
_MaintenanceDSLConfProfileName_Object = MibScalar
maintenanceDSLConfProfileName = _MaintenanceDSLConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 5),
    _MaintenanceDSLConfProfileName_Type()
)
maintenanceDSLConfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfProfileName.setStatus("current")
_MaintenanceDSLConfMode_Type = Integer32
_MaintenanceDSLConfMode_Object = MibScalar
maintenanceDSLConfMode = _MaintenanceDSLConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 6),
    _MaintenanceDSLConfMode_Type()
)
maintenanceDSLConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfMode.setStatus("current")
_MaintenanceDSLConfPktFilter_Type = Integer32
_MaintenanceDSLConfPktFilter_Object = MibScalar
maintenanceDSLConfPktFilter = _MaintenanceDSLConfPktFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 7),
    _MaintenanceDSLConfPktFilter_Type()
)
maintenanceDSLConfPktFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfPktFilter.setStatus("current")


class _MaintenanceDSLConfDot1xControl_Type(Integer32):
    """Custom type maintenanceDSLConfDot1xControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnAuth", 3))
    )


_MaintenanceDSLConfDot1xControl_Type.__name__ = "Integer32"
_MaintenanceDSLConfDot1xControl_Object = MibScalar
maintenanceDSLConfDot1xControl = _MaintenanceDSLConfDot1xControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 8),
    _MaintenanceDSLConfDot1xControl_Type()
)
maintenanceDSLConfDot1xControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfDot1xControl.setStatus("current")
_MaintenanceDSLConfDot1xReauthPeriod_Type = Integer32
_MaintenanceDSLConfDot1xReauthPeriod_Object = MibScalar
maintenanceDSLConfDot1xReauthPeriod = _MaintenanceDSLConfDot1xReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 9),
    _MaintenanceDSLConfDot1xReauthPeriod_Type()
)
maintenanceDSLConfDot1xReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfDot1xReauthPeriod.setStatus("current")
_MaintenanceDSLConfMacCount_Type = Integer32
_MaintenanceDSLConfMacCount_Object = MibScalar
maintenanceDSLConfMacCount = _MaintenanceDSLConfMacCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 10),
    _MaintenanceDSLConfMacCount_Type()
)
maintenanceDSLConfMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfMacCount.setStatus("current")


class _MaintenanceVpi_Type(Integer32):
    """Custom type maintenanceVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaintenanceVpi_Type.__name__ = "Integer32"
_MaintenanceVpi_Object = MibScalar
maintenanceVpi = _MaintenanceVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 11),
    _MaintenanceVpi_Type()
)
maintenanceVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceVpi.setStatus("current")


class _MaintenanceVci_Type(Integer32):
    """Custom type maintenanceVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MaintenanceVci_Type.__name__ = "Integer32"
_MaintenanceVci_Object = MibScalar
maintenanceVci = _MaintenanceVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 12),
    _MaintenanceVci_Type()
)
maintenanceVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceVci.setStatus("current")


class _MaintenanceDSLConfAlarmProfileName_Type(OctetString):
    """Custom type maintenanceDSLConfAlarmProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_MaintenanceDSLConfAlarmProfileName_Type.__name__ = "OctetString"
_MaintenanceDSLConfAlarmProfileName_Object = MibScalar
maintenanceDSLConfAlarmProfileName = _MaintenanceDSLConfAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 13),
    _MaintenanceDSLConfAlarmProfileName_Type()
)
maintenanceDSLConfAlarmProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfAlarmProfileName.setStatus("current")


class _MaintenanceDSLConfAnnexL_Type(Integer32):
    """Custom type maintenanceDSLConfAnnexL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableNarrowMode", 1),
          ("enableWideMode", 2),
          ("disable", 3))
    )


_MaintenanceDSLConfAnnexL_Type.__name__ = "Integer32"
_MaintenanceDSLConfAnnexL_Object = MibScalar
maintenanceDSLConfAnnexL = _MaintenanceDSLConfAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 14),
    _MaintenanceDSLConfAnnexL_Type()
)
maintenanceDSLConfAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfAnnexL.setStatus("current")


class _MaintenanceDSLConfPmMode_Type(Integer32):
    """Custom type maintenanceDSLConfPmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableL2Mode", 1),
          ("enableL3Mode", 2),
          ("disable", 3))
    )


_MaintenanceDSLConfPmMode_Type.__name__ = "Integer32"
_MaintenanceDSLConfPmMode_Object = MibScalar
maintenanceDSLConfPmMode = _MaintenanceDSLConfPmMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 15),
    _MaintenanceDSLConfPmMode_Type()
)
maintenanceDSLConfPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfPmMode.setStatus("current")


class _MaintenanceDSLConfRateMode_Type(Integer32):
    """Custom type maintenanceDSLConfRateMode based on Integer32"""
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


_MaintenanceDSLConfRateMode_Type.__name__ = "Integer32"
_MaintenanceDSLConfRateMode_Object = MibScalar
maintenanceDSLConfRateMode = _MaintenanceDSLConfRateMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 16),
    _MaintenanceDSLConfRateMode_Type()
)
maintenanceDSLConfRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfRateMode.setStatus("current")


class _MaintenanceDSLConfIgmpFilter_Type(OctetString):
    """Custom type maintenanceDSLConfIgmpFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_MaintenanceDSLConfIgmpFilter_Type.__name__ = "OctetString"
_MaintenanceDSLConfIgmpFilter_Object = MibScalar
maintenanceDSLConfIgmpFilter = _MaintenanceDSLConfIgmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 11, 90, 17),
    _MaintenanceDSLConfIgmpFilter_Type()
)
maintenanceDSLConfIgmpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceDSLConfIgmpFilter.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12)
)
_Object_ObjectIdentity = ObjectIdentity
object = _Object_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 1)
)
_EqptAlarmInputIndex_Type = Integer32
_EqptAlarmInputIndex_Object = MibScalar
eqptAlarmInputIndex = _EqptAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 1, 2),
    _EqptAlarmInputIndex_Type()
)
eqptAlarmInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputIndex.setStatus("current")
_EqptAlarmInputName_Type = DisplayString
_EqptAlarmInputName_Object = MibScalar
eqptAlarmInputName = _EqptAlarmInputName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 1, 8),
    _EqptAlarmInputName_Type()
)
eqptAlarmInputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputName.setStatus("current")
_SysMacAntiSpoofOrig_Type = Integer32
_SysMacAntiSpoofOrig_Object = MibScalar
sysMacAntiSpoofOrig = _SysMacAntiSpoofOrig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 1, 9),
    _SysMacAntiSpoofOrig_Type()
)
sysMacAntiSpoofOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofOrig.setStatus("current")
_SysMacAntiSpoofNew_Type = Integer32
_SysMacAntiSpoofNew_Object = MibScalar
sysMacAntiSpoofNew = _SysMacAntiSpoofNew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 1, 10),
    _SysMacAntiSpoofNew_Type()
)
sysMacAntiSpoofNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofNew.setStatus("current")
_SysMacAntiSpoofMAC_Type = DisplayString
_SysMacAntiSpoofMAC_Object = MibScalar
sysMacAntiSpoofMAC = _SysMacAntiSpoofMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 1, 11),
    _SysMacAntiSpoofMAC_Type()
)
sysMacAntiSpoofMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofMAC.setStatus("current")
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3)
)
_Systrap_ObjectIdentity = ObjectIdentity
systrap = _Systrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 4)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13)
)
_IgmpStats_ObjectIdentity = ObjectIdentity
igmpStats = _IgmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2)
)
_IgmpQueryCntTotal_Type = Counter32
_IgmpQueryCntTotal_Object = MibScalar
igmpQueryCntTotal = _IgmpQueryCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 1),
    _IgmpQueryCntTotal_Type()
)
igmpQueryCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQueryCntTotal.setStatus("current")
_IgmpReportCntTotal_Type = Counter32
_IgmpReportCntTotal_Object = MibScalar
igmpReportCntTotal = _IgmpReportCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 2),
    _IgmpReportCntTotal_Type()
)
igmpReportCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpReportCntTotal.setStatus("current")
_IgmpLeaveCntTotal_Type = Counter32
_IgmpLeaveCntTotal_Object = MibScalar
igmpLeaveCntTotal = _IgmpLeaveCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 3),
    _IgmpLeaveCntTotal_Type()
)
igmpLeaveCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpLeaveCntTotal.setStatus("current")
_IgmpNumOfActiveGroups_Type = Integer32
_IgmpNumOfActiveGroups_Object = MibScalar
igmpNumOfActiveGroups = _IgmpNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 4),
    _IgmpNumOfActiveGroups_Type()
)
igmpNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpNumOfActiveGroups.setStatus("current")
_IgmpGroupV2Table_Object = MibTable
igmpGroupV2Table = _IgmpGroupV2Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 7)
)
if mibBuilder.loadTexts:
    igmpGroupV2Table.setStatus("current")
_IgmpGroupV2Entry_Object = MibTableRow
igmpGroupV2Entry = _IgmpGroupV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 7, 1)
)
igmpGroupV2Entry.setIndexNames(
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpGroupV2Vid"),
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpGroupV2Ip"),
)
if mibBuilder.loadTexts:
    igmpGroupV2Entry.setStatus("current")
_IgmpGroupV2Vid_Type = VlanIndex
_IgmpGroupV2Vid_Object = MibTableColumn
igmpGroupV2Vid = _IgmpGroupV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 7, 1, 1),
    _IgmpGroupV2Vid_Type()
)
igmpGroupV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Vid.setStatus("current")
_IgmpGroupV2Ip_Type = IpAddress
_IgmpGroupV2Ip_Object = MibTableColumn
igmpGroupV2Ip = _IgmpGroupV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 7, 1, 2),
    _IgmpGroupV2Ip_Type()
)
igmpGroupV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Ip.setStatus("current")
_IgmpGroupV2NumOfMembers_Type = Integer32
_IgmpGroupV2NumOfMembers_Object = MibTableColumn
igmpGroupV2NumOfMembers = _IgmpGroupV2NumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 7, 1, 3),
    _IgmpGroupV2NumOfMembers_Type()
)
igmpGroupV2NumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2NumOfMembers.setStatus("current")
_IgmpGroupV2MemberPorts_Type = PortList
_IgmpGroupV2MemberPorts_Object = MibTableColumn
igmpGroupV2MemberPorts = _IgmpGroupV2MemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 7, 1, 4),
    _IgmpGroupV2MemberPorts_Type()
)
igmpGroupV2MemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2MemberPorts.setStatus("current")
_IgmpGroupPortV2Table_Object = MibTable
igmpGroupPortV2Table = _IgmpGroupPortV2Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 8)
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Table.setStatus("current")
_IgmpGroupPortV2Entry_Object = MibTableRow
igmpGroupPortV2Entry = _IgmpGroupPortV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 8, 1)
)
igmpGroupPortV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpGroupPortV2Vid"),
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpGroupPortV2Ip"),
    (0, "ZYXEL-VES1608FE53A-MIB", "igmpGroupPortV2SourceIp"),
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Entry.setStatus("current")
_IgmpGroupPortV2Vid_Type = VlanIndex
_IgmpGroupPortV2Vid_Object = MibTableColumn
igmpGroupPortV2Vid = _IgmpGroupPortV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 8, 1, 1),
    _IgmpGroupPortV2Vid_Type()
)
igmpGroupPortV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Vid.setStatus("current")
_IgmpGroupPortV2Ip_Type = IpAddress
_IgmpGroupPortV2Ip_Object = MibTableColumn
igmpGroupPortV2Ip = _IgmpGroupPortV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 8, 1, 2),
    _IgmpGroupPortV2Ip_Type()
)
igmpGroupPortV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Ip.setStatus("current")
_IgmpGroupPortV2SourceIp_Type = IpAddress
_IgmpGroupPortV2SourceIp_Object = MibTableColumn
igmpGroupPortV2SourceIp = _IgmpGroupPortV2SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 8, 1, 3),
    _IgmpGroupPortV2SourceIp_Type()
)
igmpGroupPortV2SourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2SourceIp.setStatus("current")
_IgmpPortCtrlPduTable_Object = MibTable
igmpPortCtrlPduTable = _IgmpPortCtrlPduTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 9)
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduTable.setStatus("current")
_IgmpPortCtrlPduEntry_Object = MibTableRow
igmpPortCtrlPduEntry = _IgmpPortCtrlPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 9, 1)
)
igmpPortCtrlPduEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduEntry.setStatus("current")
_IgmpPortCtrlPduQueryCnt_Type = Counter32
_IgmpPortCtrlPduQueryCnt_Object = MibTableColumn
igmpPortCtrlPduQueryCnt = _IgmpPortCtrlPduQueryCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 9, 1, 1),
    _IgmpPortCtrlPduQueryCnt_Type()
)
igmpPortCtrlPduQueryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduQueryCnt.setStatus("current")
_IgmpPortCtrlPduReportCnt_Type = Counter32
_IgmpPortCtrlPduReportCnt_Object = MibTableColumn
igmpPortCtrlPduReportCnt = _IgmpPortCtrlPduReportCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 9, 1, 2),
    _IgmpPortCtrlPduReportCnt_Type()
)
igmpPortCtrlPduReportCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduReportCnt.setStatus("current")
_IgmpPortCtrlPduLeaveCnt_Type = Counter32
_IgmpPortCtrlPduLeaveCnt_Object = MibTableColumn
igmpPortCtrlPduLeaveCnt = _IgmpPortCtrlPduLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 9, 1, 3),
    _IgmpPortCtrlPduLeaveCnt_Type()
)
igmpPortCtrlPduLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduLeaveCnt.setStatus("current")
_IgmpPortNumOfActiveGroups_Type = Integer32
_IgmpPortNumOfActiveGroups_Object = MibTableColumn
igmpPortNumOfActiveGroups = _IgmpPortNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 2, 9, 1, 4),
    _IgmpPortNumOfActiveGroups_Type()
)
igmpPortNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortNumOfActiveGroups.setStatus("current")
_VdslStats_ObjectIdentity = ObjectIdentity
vdslStats = _VdslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8)
)
_VdslLineStatsTable_Object = MibTable
vdslLineStatsTable = _VdslLineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2)
)
if mibBuilder.loadTexts:
    vdslLineStatsTable.setStatus("current")
_VdslLineStatsEntry_Object = MibTableRow
vdslLineStatsEntry = _VdslLineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1)
)
vdslLineStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslLineStatsEntry.setStatus("current")
_VdslLineStatsVtucBits1_Type = OctetString
_VdslLineStatsVtucBits1_Object = MibTableColumn
vdslLineStatsVtucBits1 = _VdslLineStatsVtucBits1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 1),
    _VdslLineStatsVtucBits1_Type()
)
vdslLineStatsVtucBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits1.setStatus("current")
_VdslLineStatsVtucBits2_Type = OctetString
_VdslLineStatsVtucBits2_Object = MibTableColumn
vdslLineStatsVtucBits2 = _VdslLineStatsVtucBits2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 2),
    _VdslLineStatsVtucBits2_Type()
)
vdslLineStatsVtucBits2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits2.setStatus("current")
_VdslLineStatsVtucBits3_Type = OctetString
_VdslLineStatsVtucBits3_Object = MibTableColumn
vdslLineStatsVtucBits3 = _VdslLineStatsVtucBits3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 3),
    _VdslLineStatsVtucBits3_Type()
)
vdslLineStatsVtucBits3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits3.setStatus("current")
_VdslLineStatsVtucBits4_Type = OctetString
_VdslLineStatsVtucBits4_Object = MibTableColumn
vdslLineStatsVtucBits4 = _VdslLineStatsVtucBits4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 4),
    _VdslLineStatsVtucBits4_Type()
)
vdslLineStatsVtucBits4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits4.setStatus("current")
_VdslLineStatsVturBits1_Type = OctetString
_VdslLineStatsVturBits1_Object = MibTableColumn
vdslLineStatsVturBits1 = _VdslLineStatsVturBits1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 5),
    _VdslLineStatsVturBits1_Type()
)
vdslLineStatsVturBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits1.setStatus("current")
_VdslLineStatsVturBits2_Type = OctetString
_VdslLineStatsVturBits2_Object = MibTableColumn
vdslLineStatsVturBits2 = _VdslLineStatsVturBits2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 6),
    _VdslLineStatsVturBits2_Type()
)
vdslLineStatsVturBits2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits2.setStatus("current")
_VdslLineStatsVturBits3_Type = OctetString
_VdslLineStatsVturBits3_Object = MibTableColumn
vdslLineStatsVturBits3 = _VdslLineStatsVturBits3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 7),
    _VdslLineStatsVturBits3_Type()
)
vdslLineStatsVturBits3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits3.setStatus("current")
_VdslLineStatsVturBits4_Type = OctetString
_VdslLineStatsVturBits4_Object = MibTableColumn
vdslLineStatsVturBits4 = _VdslLineStatsVturBits4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 8),
    _VdslLineStatsVturBits4_Type()
)
vdslLineStatsVturBits4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits4.setStatus("current")
_VdslLineStatsVtucGain1_Type = OctetString
_VdslLineStatsVtucGain1_Object = MibTableColumn
vdslLineStatsVtucGain1 = _VdslLineStatsVtucGain1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 9),
    _VdslLineStatsVtucGain1_Type()
)
vdslLineStatsVtucGain1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain1.setStatus("current")
_VdslLineStatsVtucGain2_Type = OctetString
_VdslLineStatsVtucGain2_Object = MibTableColumn
vdslLineStatsVtucGain2 = _VdslLineStatsVtucGain2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 10),
    _VdslLineStatsVtucGain2_Type()
)
vdslLineStatsVtucGain2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain2.setStatus("current")
_VdslLineStatsVtucGain3_Type = OctetString
_VdslLineStatsVtucGain3_Object = MibTableColumn
vdslLineStatsVtucGain3 = _VdslLineStatsVtucGain3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 11),
    _VdslLineStatsVtucGain3_Type()
)
vdslLineStatsVtucGain3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain3.setStatus("current")
_VdslLineStatsVtucGain4_Type = OctetString
_VdslLineStatsVtucGain4_Object = MibTableColumn
vdslLineStatsVtucGain4 = _VdslLineStatsVtucGain4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 12),
    _VdslLineStatsVtucGain4_Type()
)
vdslLineStatsVtucGain4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain4.setStatus("current")
_VdslLineStatsVtucGain5_Type = OctetString
_VdslLineStatsVtucGain5_Object = MibTableColumn
vdslLineStatsVtucGain5 = _VdslLineStatsVtucGain5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 13),
    _VdslLineStatsVtucGain5_Type()
)
vdslLineStatsVtucGain5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain5.setStatus("current")
_VdslLineStatsVtucGain6_Type = OctetString
_VdslLineStatsVtucGain6_Object = MibTableColumn
vdslLineStatsVtucGain6 = _VdslLineStatsVtucGain6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 14),
    _VdslLineStatsVtucGain6_Type()
)
vdslLineStatsVtucGain6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain6.setStatus("current")
_VdslLineStatsVtucGain7_Type = OctetString
_VdslLineStatsVtucGain7_Object = MibTableColumn
vdslLineStatsVtucGain7 = _VdslLineStatsVtucGain7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 15),
    _VdslLineStatsVtucGain7_Type()
)
vdslLineStatsVtucGain7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain7.setStatus("current")
_VdslLineStatsVtucGain8_Type = OctetString
_VdslLineStatsVtucGain8_Object = MibTableColumn
vdslLineStatsVtucGain8 = _VdslLineStatsVtucGain8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 16),
    _VdslLineStatsVtucGain8_Type()
)
vdslLineStatsVtucGain8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain8.setStatus("current")
_VdslLineStatsVturGain1_Type = OctetString
_VdslLineStatsVturGain1_Object = MibTableColumn
vdslLineStatsVturGain1 = _VdslLineStatsVturGain1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 17),
    _VdslLineStatsVturGain1_Type()
)
vdslLineStatsVturGain1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain1.setStatus("current")
_VdslLineStatsVturGain2_Type = OctetString
_VdslLineStatsVturGain2_Object = MibTableColumn
vdslLineStatsVturGain2 = _VdslLineStatsVturGain2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 18),
    _VdslLineStatsVturGain2_Type()
)
vdslLineStatsVturGain2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain2.setStatus("current")
_VdslLineStatsVturGain3_Type = OctetString
_VdslLineStatsVturGain3_Object = MibTableColumn
vdslLineStatsVturGain3 = _VdslLineStatsVturGain3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 19),
    _VdslLineStatsVturGain3_Type()
)
vdslLineStatsVturGain3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain3.setStatus("current")
_VdslLineStatsVturGain4_Type = OctetString
_VdslLineStatsVturGain4_Object = MibTableColumn
vdslLineStatsVturGain4 = _VdslLineStatsVturGain4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 20),
    _VdslLineStatsVturGain4_Type()
)
vdslLineStatsVturGain4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain4.setStatus("current")
_VdslLineStatsVturGain5_Type = OctetString
_VdslLineStatsVturGain5_Object = MibTableColumn
vdslLineStatsVturGain5 = _VdslLineStatsVturGain5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 21),
    _VdslLineStatsVturGain5_Type()
)
vdslLineStatsVturGain5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain5.setStatus("current")
_VdslLineStatsVturGain6_Type = OctetString
_VdslLineStatsVturGain6_Object = MibTableColumn
vdslLineStatsVturGain6 = _VdslLineStatsVturGain6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 22),
    _VdslLineStatsVturGain6_Type()
)
vdslLineStatsVturGain6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain6.setStatus("current")
_VdslLineStatsVturGain7_Type = OctetString
_VdslLineStatsVturGain7_Object = MibTableColumn
vdslLineStatsVturGain7 = _VdslLineStatsVturGain7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 23),
    _VdslLineStatsVturGain7_Type()
)
vdslLineStatsVturGain7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain7.setStatus("current")
_VdslLineStatsVturGain8_Type = OctetString
_VdslLineStatsVturGain8_Object = MibTableColumn
vdslLineStatsVturGain8 = _VdslLineStatsVturGain8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 24),
    _VdslLineStatsVturGain8_Type()
)
vdslLineStatsVturGain8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain8.setStatus("current")
_VdslLineStatsVtucHlog_Type = OctetString
_VdslLineStatsVtucHlog_Object = MibTableColumn
vdslLineStatsVtucHlog = _VdslLineStatsVtucHlog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 25),
    _VdslLineStatsVtucHlog_Type()
)
vdslLineStatsVtucHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucHlog.setStatus("current")
_VdslLineStatsVturHlog_Type = OctetString
_VdslLineStatsVturHlog_Object = MibTableColumn
vdslLineStatsVturHlog = _VdslLineStatsVturHlog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 26),
    _VdslLineStatsVturHlog_Type()
)
vdslLineStatsVturHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturHlog.setStatus("current")
_VdslLineStatsVtucQln_Type = OctetString
_VdslLineStatsVtucQln_Object = MibTableColumn
vdslLineStatsVtucQln = _VdslLineStatsVtucQln_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 27),
    _VdslLineStatsVtucQln_Type()
)
vdslLineStatsVtucQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucQln.setStatus("current")
_VdslLineStatsVturQln_Type = OctetString
_VdslLineStatsVturQln_Object = MibTableColumn
vdslLineStatsVturQln = _VdslLineStatsVturQln_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 28),
    _VdslLineStatsVturQln_Type()
)
vdslLineStatsVturQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturQln.setStatus("current")
_VdslLineStatsVtucSnr_Type = OctetString
_VdslLineStatsVtucSnr_Object = MibTableColumn
vdslLineStatsVtucSnr = _VdslLineStatsVtucSnr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 29),
    _VdslLineStatsVtucSnr_Type()
)
vdslLineStatsVtucSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucSnr.setStatus("current")
_VdslLineStatsVturSnr_Type = OctetString
_VdslLineStatsVturSnr_Object = MibTableColumn
vdslLineStatsVturSnr = _VdslLineStatsVturSnr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 30),
    _VdslLineStatsVturSnr_Type()
)
vdslLineStatsVturSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturSnr.setStatus("current")
_VdslLineStatsVtucTssi_Type = OctetString
_VdslLineStatsVtucTssi_Object = MibTableColumn
vdslLineStatsVtucTssi = _VdslLineStatsVtucTssi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 31),
    _VdslLineStatsVtucTssi_Type()
)
vdslLineStatsVtucTssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucTssi.setStatus("current")
_VdslLineStatsVturTssi_Type = OctetString
_VdslLineStatsVturTssi_Object = MibTableColumn
vdslLineStatsVturTssi = _VdslLineStatsVturTssi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 32),
    _VdslLineStatsVturTssi_Type()
)
vdslLineStatsVturTssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturTssi.setStatus("current")


class _VdslLineStatsProtocol_Type(Integer32):
    """Custom type vdslLineStatsProtocol based on Integer32"""
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
        *(("none", 1),
          ("vdsl_8a", 2),
          ("vdsl_8b", 3),
          ("vdsl_8c", 4),
          ("vdsl_8d", 5),
          ("vdsl_12a", 6),
          ("vdsl_12b", 7),
          ("vdsl_17a", 8),
          ("vdsl_30a", 9),
          ("adsl2plus", 10))
    )


_VdslLineStatsProtocol_Type.__name__ = "Integer32"
_VdslLineStatsProtocol_Object = MibTableColumn
vdslLineStatsProtocol = _VdslLineStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 8, 2, 1, 33),
    _VdslLineStatsProtocol_Type()
)
vdslLineStatsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsProtocol.setStatus("current")
_DhcpStats_ObjectIdentity = ObjectIdentity
dhcpStats = _DhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11)
)
_DhcpSnoopIpTable_Object = MibTable
dhcpSnoopIpTable = _DhcpSnoopIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopIpTable.setStatus("current")
_DhcpSnoopIpEntry_Object = MibTableRow
dhcpSnoopIpEntry = _DhcpSnoopIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 1, 1)
)
dhcpSnoopIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "dhcpSnoopIp"),
)
if mibBuilder.loadTexts:
    dhcpSnoopIpEntry.setStatus("current")
_DhcpSnoopIp_Type = IpAddress
_DhcpSnoopIp_Object = MibTableColumn
dhcpSnoopIp = _DhcpSnoopIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 1, 1, 1),
    _DhcpSnoopIp_Type()
)
dhcpSnoopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopIp.setStatus("current")
_DhcpSnoopMac_Type = PhysAddress
_DhcpSnoopMac_Object = MibTableColumn
dhcpSnoopMac = _DhcpSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 1, 1, 2),
    _DhcpSnoopMac_Type()
)
dhcpSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMac.setStatus("current")
_DhcpSnoopVid_Type = VlanIndex
_DhcpSnoopVid_Object = MibTableColumn
dhcpSnoopVid = _DhcpSnoopVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 1, 1, 3),
    _DhcpSnoopVid_Type()
)
dhcpSnoopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopVid.setStatus("current")
_DhcpSnoopCounterTable_Object = MibTable
dhcpSnoopCounterTable = _DhcpSnoopCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterTable.setStatus("current")
_DhcpSnoopCounterEntry_Object = MibTableRow
dhcpSnoopCounterEntry = _DhcpSnoopCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2, 1)
)
dhcpSnoopCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterEntry.setStatus("current")
_DhcpDiscovery_Type = Counter64
_DhcpDiscovery_Object = MibTableColumn
dhcpDiscovery = _DhcpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2, 1, 1),
    _DhcpDiscovery_Type()
)
dhcpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDiscovery.setStatus("current")
_DhcpOffer_Type = Counter64
_DhcpOffer_Object = MibTableColumn
dhcpOffer = _DhcpOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2, 1, 2),
    _DhcpOffer_Type()
)
dhcpOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOffer.setStatus("current")
_DhcpRequest_Type = Counter64
_DhcpRequest_Object = MibTableColumn
dhcpRequest = _DhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2, 1, 3),
    _DhcpRequest_Type()
)
dhcpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequest.setStatus("current")
_DhcpAck_Type = Counter64
_DhcpAck_Object = MibTableColumn
dhcpAck = _DhcpAck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2, 1, 4),
    _DhcpAck_Type()
)
dhcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAck.setStatus("current")
_DhcpAckBySnoopFull_Type = Counter64
_DhcpAckBySnoopFull_Object = MibTableColumn
dhcpAckBySnoopFull = _DhcpAckBySnoopFull_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 11, 2, 1, 5),
    _DhcpAckBySnoopFull_Type()
)
dhcpAckBySnoopFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAckBySnoopFull.setStatus("current")
_PaepvcStats_ObjectIdentity = ObjectIdentity
paepvcStats = _PaepvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12)
)
_PaepvcSessionTable_Object = MibTable
paepvcSessionTable = _PaepvcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1)
)
if mibBuilder.loadTexts:
    paepvcSessionTable.setStatus("current")
_PaepvcSessionEntry_Object = MibTableRow
paepvcSessionEntry = _PaepvcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1)
)
paepvcSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcSessionVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcSessionVci"),
)
if mibBuilder.loadTexts:
    paepvcSessionEntry.setStatus("current")
_PaepvcSessionVpi_Type = Integer32
_PaepvcSessionVpi_Object = MibTableColumn
paepvcSessionVpi = _PaepvcSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 1),
    _PaepvcSessionVpi_Type()
)
paepvcSessionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVpi.setStatus("current")
_PaepvcSessionVci_Type = Integer32
_PaepvcSessionVci_Object = MibTableColumn
paepvcSessionVci = _PaepvcSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 2),
    _PaepvcSessionVci_Type()
)
paepvcSessionVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVci.setStatus("current")


class _PaepvcSessionState_Type(Integer32):
    """Custom type paepvcSessionState based on Integer32"""
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
        *(("down", 1),
          ("pppoe", 2),
          ("ppp", 3),
          ("up", 4))
    )


_PaepvcSessionState_Type.__name__ = "Integer32"
_PaepvcSessionState_Object = MibTableColumn
paepvcSessionState = _PaepvcSessionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 3),
    _PaepvcSessionState_Type()
)
paepvcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionState.setStatus("current")
_PaepvcSessionId_Type = Integer32
_PaepvcSessionId_Object = MibTableColumn
paepvcSessionId = _PaepvcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 4),
    _PaepvcSessionId_Type()
)
paepvcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionId.setStatus("current")
_PaepvcSessionUptime_Type = Unsigned32
_PaepvcSessionUptime_Object = MibTableColumn
paepvcSessionUptime = _PaepvcSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 5),
    _PaepvcSessionUptime_Type()
)
paepvcSessionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionUptime.setStatus("current")
if mibBuilder.loadTexts:
    paepvcSessionUptime.setUnits("second")
_PaepvcSessionacname_Type = DisplayString
_PaepvcSessionacname_Object = MibTableColumn
paepvcSessionacname = _PaepvcSessionacname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 6),
    _PaepvcSessionacname_Type()
)
paepvcSessionacname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionacname.setStatus("current")
_PaepvcSessionsrvcname_Type = DisplayString
_PaepvcSessionsrvcname_Object = MibTableColumn
paepvcSessionsrvcname = _PaepvcSessionsrvcname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 1, 1, 7),
    _PaepvcSessionsrvcname_Type()
)
paepvcSessionsrvcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionsrvcname.setStatus("current")
_PaepvcCountTable_Object = MibTable
paepvcCountTable = _PaepvcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2)
)
if mibBuilder.loadTexts:
    paepvcCountTable.setStatus("current")
_PaepvcCountEntry_Object = MibTableRow
paepvcCountEntry = _PaepvcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1)
)
paepvcCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcCountVpi"),
    (0, "ZYXEL-VES1608FE53A-MIB", "paepvcCountVci"),
)
if mibBuilder.loadTexts:
    paepvcCountEntry.setStatus("current")
_PaepvcCountVpi_Type = Integer32
_PaepvcCountVpi_Object = MibTableColumn
paepvcCountVpi = _PaepvcCountVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 1),
    _PaepvcCountVpi_Type()
)
paepvcCountVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVpi.setStatus("current")
_PaepvcCountVci_Type = Integer32
_PaepvcCountVci_Object = MibTableColumn
paepvcCountVci = _PaepvcCountVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 2),
    _PaepvcCountVci_Type()
)
paepvcCountVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVci.setStatus("current")
_PaepvcCountPppLcpCfgReqRx_Type = Unsigned32
_PaepvcCountPppLcpCfgReqRx_Object = MibTableColumn
paepvcCountPppLcpCfgReqRx = _PaepvcCountPppLcpCfgReqRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 3),
    _PaepvcCountPppLcpCfgReqRx_Type()
)
paepvcCountPppLcpCfgReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpCfgReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReqRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReqRx_Object = MibTableColumn
paepvcCountPppLcpEchoReqRx = _PaepvcCountPppLcpEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 4),
    _PaepvcCountPppLcpEchoReqRx_Type()
)
paepvcCountPppLcpEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReplyRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReplyRx_Object = MibTableColumn
paepvcCountPppLcpEchoReplyRx = _PaepvcCountPppLcpEchoReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 5),
    _PaepvcCountPppLcpEchoReplyRx_Type()
)
paepvcCountPppLcpEchoReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReplyRx.setStatus("current")
_PaepvcCountPadiTx_Type = Unsigned32
_PaepvcCountPadiTx_Object = MibTableColumn
paepvcCountPadiTx = _PaepvcCountPadiTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 6),
    _PaepvcCountPadiTx_Type()
)
paepvcCountPadiTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadiTx.setStatus("current")
_PaepvcCountPadoRx_Type = Unsigned32
_PaepvcCountPadoRx_Object = MibTableColumn
paepvcCountPadoRx = _PaepvcCountPadoRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 7),
    _PaepvcCountPadoRx_Type()
)
paepvcCountPadoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadoRx.setStatus("current")
_PaepvcCountPadrTx_Type = Unsigned32
_PaepvcCountPadrTx_Object = MibTableColumn
paepvcCountPadrTx = _PaepvcCountPadrTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 8),
    _PaepvcCountPadrTx_Type()
)
paepvcCountPadrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadrTx.setStatus("current")
_PaepvcCountPadsRx_Type = Unsigned32
_PaepvcCountPadsRx_Object = MibTableColumn
paepvcCountPadsRx = _PaepvcCountPadsRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 9),
    _PaepvcCountPadsRx_Type()
)
paepvcCountPadsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadsRx.setStatus("current")
_PaepvcCountPadtTx_Type = Unsigned32
_PaepvcCountPadtTx_Object = MibTableColumn
paepvcCountPadtTx = _PaepvcCountPadtTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 10),
    _PaepvcCountPadtTx_Type()
)
paepvcCountPadtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtTx.setStatus("current")
_PaepvcCountPadtRx_Type = Unsigned32
_PaepvcCountPadtRx_Object = MibTableColumn
paepvcCountPadtRx = _PaepvcCountPadtRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 11),
    _PaepvcCountPadtRx_Type()
)
paepvcCountPadtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtRx.setStatus("current")
_PaepvcCountSrvcnameErrRx_Type = Unsigned32
_PaepvcCountSrvcnameErrRx_Object = MibTableColumn
paepvcCountSrvcnameErrRx = _PaepvcCountSrvcnameErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 12),
    _PaepvcCountSrvcnameErrRx_Type()
)
paepvcCountSrvcnameErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountSrvcnameErrRx.setStatus("current")
_PaepvcCountAcSystemErrRx_Type = Unsigned32
_PaepvcCountAcSystemErrRx_Object = MibTableColumn
paepvcCountAcSystemErrRx = _PaepvcCountAcSystemErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 13),
    _PaepvcCountAcSystemErrRx_Type()
)
paepvcCountAcSystemErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountAcSystemErrRx.setStatus("current")
_PaepvcCountGenericErrTx_Type = Unsigned32
_PaepvcCountGenericErrTx_Object = MibTableColumn
paepvcCountGenericErrTx = _PaepvcCountGenericErrTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 14),
    _PaepvcCountGenericErrTx_Type()
)
paepvcCountGenericErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrTx.setStatus("current")
_PaepvcCountGenericErrRx_Type = Unsigned32
_PaepvcCountGenericErrRx_Object = MibTableColumn
paepvcCountGenericErrRx = _PaepvcCountGenericErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 12, 2, 1, 15),
    _PaepvcCountGenericErrRx_Type()
)
paepvcCountGenericErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrRx.setStatus("current")
_MacStats_ObjectIdentity = ObjectIdentity
macStats = _MacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13)
)
_MacDisplayTarget_Type = Integer32
_MacDisplayTarget_Object = MibScalar
macDisplayTarget = _MacDisplayTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 1),
    _MacDisplayTarget_Type()
)
macDisplayTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macDisplayTarget.setStatus("current")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 2, 1)
)
macEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "macAddress"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 2, 1, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacPort_Type = Integer32
_MacPort_Object = MibTableColumn
macPort = _MacPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 2, 1, 2),
    _MacPort_Type()
)
macPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macPort.setStatus("current")


class _MacStatus_Type(Integer32):
    """Custom type macStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_MacStatus_Type.__name__ = "Integer32"
_MacStatus_Object = MibTableColumn
macStatus = _MacStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 2, 1, 3),
    _MacStatus_Type()
)
macStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macStatus.setStatus("current")
_MacVid_Type = VlanIndex
_MacVid_Object = MibTableColumn
macVid = _MacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 2, 1, 4),
    _MacVid_Type()
)
macVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVid.setStatus("current")
_MacFlush_Type = Integer32
_MacFlush_Object = MibScalar
macFlush = _MacFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 13, 3),
    _MacFlush_Type()
)
macFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFlush.setStatus("current")
_N1macStats_ObjectIdentity = ObjectIdentity
n1macStats = _N1macStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 15)
)
_N1macTable_Object = MibTable
n1macTable = _N1macTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 15, 1)
)
if mibBuilder.loadTexts:
    n1macTable.setStatus("current")
_N1macEntry_Object = MibTableRow
n1macEntry = _N1macEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 15, 1, 1)
)
n1macEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VES1608FE53A-MIB", "n1macProtoVal"),
)
if mibBuilder.loadTexts:
    n1macEntry.setStatus("current")
_N1macProtoVal_Type = Unsigned32
_N1macProtoVal_Object = MibTableColumn
n1macProtoVal = _N1macProtoVal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 15, 1, 1, 1),
    _N1macProtoVal_Type()
)
n1macProtoVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macProtoVal.setStatus("current")


class _N1macProtoType_Type(Integer32):
    """Custom type n1macProtoType based on Integer32"""
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
          ("ipoe", 2),
          ("ipoaoe", 3),
          ("pppoe", 4),
          ("pppoaoe", 5))
    )


_N1macProtoType_Type.__name__ = "Integer32"
_N1macProtoType_Object = MibTableColumn
n1macProtoType = _N1macProtoType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 15, 1, 1, 2),
    _N1macProtoType_Type()
)
n1macProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macProtoType.setStatus("current")
_N1macMacAddr_Type = MacAddress
_N1macMacAddr_Object = MibTableColumn
n1macMacAddr = _N1macMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 15, 1, 1, 3),
    _N1macMacAddr_Type()
)
n1macMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macMacAddr.setStatus("current")
_EnetStats_ObjectIdentity = ObjectIdentity
enetStats = _EnetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 16)
)
_EnetPrimaryPort_Type = Integer32
_EnetPrimaryPort_Object = MibScalar
enetPrimaryPort = _EnetPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 13, 16, 1),
    _EnetPrimaryPort_Type()
)
enetPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPrimaryPort.setStatus("current")
_Clear_ObjectIdentity = ObjectIdentity
clear = _Clear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 14)
)
_CounterClearTarget_Type = OctetString
_CounterClearTarget_Object = MibScalar
counterClearTarget = _CounterClearTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 14, 1),
    _CounterClearTarget_Type()
)
counterClearTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearTarget.setStatus("current")
_CounterClearOps_Type = Integer32
_CounterClearOps_Object = MibScalar
counterClearOps = _CounterClearOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 14, 2),
    _CounterClearOps_Type()
)
counterClearOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearOps.setStatus("current")


class _CounterClearVpi_Type(Integer32):
    """Custom type counterClearVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CounterClearVpi_Type.__name__ = "Integer32"
_CounterClearVpi_Object = MibScalar
counterClearVpi = _CounterClearVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 14, 3),
    _CounterClearVpi_Type()
)
counterClearVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVpi.setStatus("current")


class _CounterClearVci_Type(Integer32):
    """Custom type counterClearVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CounterClearVci_Type.__name__ = "Integer32"
_CounterClearVci_Object = MibScalar
counterClearVci = _CounterClearVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 14, 4),
    _CounterClearVci_Type()
)
counterClearVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVci.setStatus("current")

# Managed Objects groups


# Notification objects

eqptVoltageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 1)
)
eqptVoltageError.setObjects(
      *(("ZYXEL-VES1608FE53A-MIB", "voltageIndex"),
        ("ZYXEL-VES1608FE53A-MIB", "voltageCurValue"),
        ("ZYXEL-VES1608FE53A-MIB", "voltageLowThresh"))
)
if mibBuilder.loadTexts:
    eqptVoltageError.setStatus(
        "current"
    )

eqptVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 2)
)
eqptVoltageNormal.setObjects(
    ("ZYXEL-VES1608FE53A-MIB", "voltageIndex")
)
if mibBuilder.loadTexts:
    eqptVoltageNormal.setStatus(
        "current"
    )

eqptTempError = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 3)
)
eqptTempError.setObjects(
      *(("ZYXEL-VES1608FE53A-MIB", "temperatureIndex"),
        ("ZYXEL-VES1608FE53A-MIB", "temperatureCurValue"),
        ("ZYXEL-VES1608FE53A-MIB", "temperatureHighThresh"))
)
if mibBuilder.loadTexts:
    eqptTempError.setStatus(
        "current"
    )

eqptTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 4)
)
eqptTempNormal.setObjects(
    ("ZYXEL-VES1608FE53A-MIB", "temperatureIndex")
)
if mibBuilder.loadTexts:
    eqptTempNormal.setStatus(
        "current"
    )

eqptHWMonitorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 7)
)
if mibBuilder.loadTexts:
    eqptHWMonitorFailure.setStatus(
        "current"
    )

eqptExternalAlarmInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 8)
)
eqptExternalAlarmInput.setObjects(
      *(("ZYXEL-VES1608FE53A-MIB", "extAlarmIndex"),
        ("ZYXEL-VES1608FE53A-MIB", "extAlarmName"))
)
if mibBuilder.loadTexts:
    eqptExternalAlarmInput.setStatus(
        "current"
    )

eqptExternalAlarmInputRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 3, 9)
)
eqptExternalAlarmInputRelease.setObjects(
      *(("ZYXEL-VES1608FE53A-MIB", "extAlarmIndex"),
        ("ZYXEL-VES1608FE53A-MIB", "extAlarmName"))
)
if mibBuilder.loadTexts:
    eqptExternalAlarmInputRelease.setStatus(
        "current"
    )

sysReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 4, 1)
)
if mibBuilder.loadTexts:
    sysReboot.setStatus(
        "current"
    )

sysMacAntiSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42, 12, 4, 2)
)
sysMacAntiSpoofing.setObjects(
      *(("ZYXEL-VES1608FE53A-MIB", "sysMacAntiSpoofOrig"),
        ("ZYXEL-VES1608FE53A-MIB", "sysMacAntiSpoofNew"),
        ("ZYXEL-VES1608FE53A-MIB", "sysMacAntiSpoofMAC"))
)
if mibBuilder.loadTexts:
    sysMacAntiSpoofing.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VES1608FE53A-MIB",
    **{"zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "vesSeries": vesSeries,
       "ves1608fe53a": ves1608fe53a,
       "alarmconf": alarmconf,
       "alarmOps": alarmOps,
       "alarmConfTable": alarmConfTable,
       "alarmConfEntry": alarmConfEntry,
       "alarmConfId": alarmConfId,
       "alarmConfFacility": alarmConfFacility,
       "alarmConfTarget": alarmConfTarget,
       "alarmConfSeverity": alarmConfSeverity,
       "alarmConfClearable": alarmConfClearable,
       "alarmCurrTable": alarmCurrTable,
       "alarmCurrEntry": alarmCurrEntry,
       "alarmCurrIndex": alarmCurrIndex,
       "alarmCurrOccurTime": alarmCurrOccurTime,
       "alarmCurrTrapOid": alarmCurrTrapOid,
       "alarmCurrParam1": alarmCurrParam1,
       "alarmCurrParam2": alarmCurrParam2,
       "alarmCurrParam3": alarmCurrParam3,
       "alarmCurrParam4": alarmCurrParam4,
       "alarmCurrParam5": alarmCurrParam5,
       "alarmCurrParam6": alarmCurrParam6,
       "alarmCurrParam7": alarmCurrParam7,
       "alarmCurrParam8": alarmCurrParam8,
       "alarmCurrTimeDescr": alarmCurrTimeDescr,
       "alarmCurrSeverity": alarmCurrSeverity,
       "alarmCurrDescr": alarmCurrDescr,
       "alarmSeverityPortTable": alarmSeverityPortTable,
       "alarmSeverityPortEntry": alarmSeverityPortEntry,
       "severityThresh": severityThresh,
       "diagnostic": diagnostic,
       "selt": selt,
       "seltTarget": seltTarget,
       "seltOps": seltOps,
       "seltStatus": seltStatus,
       "seltCableType": seltCableType,
       "seltLoopEstimateLengthFt": seltLoopEstimateLengthFt,
       "seltLoopEstimateLengthMeter": seltLoopEstimateLengthMeter,
       "ldm": ldm,
       "ldmTarget": ldmTarget,
       "ldmOps": ldmOps,
       "ldmStatus": ldmStatus,
       "ldmXtucLoopAttenuation": ldmXtucLoopAttenuation,
       "ldmXtucSignalAttenuation": ldmXtucSignalAttenuation,
       "ldmXtucSignalMargin": ldmXtucSignalMargin,
       "ldmXtucAggregateTxPower": ldmXtucAggregateTxPower,
       "ldmXtucAttainableBitRate": ldmXtucAttainableBitRate,
       "ldmXturLoopAttenuation": ldmXturLoopAttenuation,
       "ldmXturSignalAttenuation": ldmXturSignalAttenuation,
       "ldmXturSignalMargin": ldmXturSignalMargin,
       "ldmXturAggregateTxPower": ldmXturAggregateTxPower,
       "ldmXturAttainableBitRate": ldmXturAttainableBitRate,
       "ldmXtucNumOfSubcarriersPerPort": ldmXtucNumOfSubcarriersPerPort,
       "ldmXturNumOfSubcarriersPerPort": ldmXturNumOfSubcarriersPerPort,
       "ldmXtucHlinScale": ldmXtucHlinScale,
       "ldmXtucHlinReal1": ldmXtucHlinReal1,
       "ldmXtucHlinReal2": ldmXtucHlinReal2,
       "ldmXtucHlinImage1": ldmXtucHlinImage1,
       "ldmXtucHlinImage2": ldmXtucHlinImage2,
       "ldmXtucHlog1": ldmXtucHlog1,
       "ldmXtucHlog2": ldmXtucHlog2,
       "ldmXtucQln1": ldmXtucQln1,
       "ldmXtucQln2": ldmXtucQln2,
       "ldmXtucSnr1": ldmXtucSnr1,
       "ldmXtucSnr2": ldmXtucSnr2,
       "ldmXturHlinScale": ldmXturHlinScale,
       "ldmXturHlinReal": ldmXturHlinReal,
       "ldmXturHlinImage": ldmXturHlinImage,
       "ldmXturHlog": ldmXturHlog,
       "ldmXturQln": ldmXturQln,
       "ldmXturSnr": ldmXturSnr,
       "ipconf": ipconf,
       "staticRoute": staticRoute,
       "maxNumOfStaticRoutes": maxNumOfStaticRoutes,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteName": staticRouteName,
       "staticRouteDest": staticRouteDest,
       "staticRouteMask": staticRouteMask,
       "staticRouteGateway": staticRouteGateway,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteRowStatus": staticRouteRowStatus,
       "ipSetup": ipSetup,
       "inbandIp": inbandIp,
       "inbandIpSubnetMask": inbandIpSubnetMask,
       "outbandIp": outbandIp,
       "outbandIpSubnetMask": outbandIpSubnetMask,
       "defaultGatewayIp": defaultGatewayIp,
       "multicast": multicast,
       "igmpEnable": igmpEnable,
       "staticMulticast": staticMulticast,
       "maxNumberOfMcastGroups": maxNumberOfMcastGroups,
       "multicastGroupTable": multicastGroupTable,
       "multicastGroupEntry": multicastGroupEntry,
       "multicastGroupVid": multicastGroupVid,
       "multicastGroupMacAddr": multicastGroupMacAddr,
       "multicastGroupPorts": multicastGroupPorts,
       "multicastGroupRowStatus": multicastGroupRowStatus,
       "igmpFilter": igmpFilter,
       "maxNumOfIgmpFilters": maxNumOfIgmpFilters,
       "igmpFilterTable": igmpFilterTable,
       "igmpFilterEntry": igmpFilterEntry,
       "igmpFilterName": igmpFilterName,
       "igmpFilterIndex": igmpFilterIndex,
       "igmpFilterStartIp": igmpFilterStartIp,
       "igmpFilterEndIp": igmpFilterEndIp,
       "igmpFilterRowStatus": igmpFilterRowStatus,
       "igmpFilterPortTable": igmpFilterPortTable,
       "igmpFilterPortEntry": igmpFilterPortEntry,
       "igmpFilterPortFilterName": igmpFilterPortFilterName,
       "mcastBandwidth": mcastBandwidth,
       "mcastDefaultBandwidth": mcastDefaultBandwidth,
       "maxNumOfMcastBw": maxNumOfMcastBw,
       "mcastBwTable": mcastBwTable,
       "mcastBwEntry": mcastBwEntry,
       "mcastBwIndex": mcastBwIndex,
       "mcastBwStartIp": mcastBwStartIp,
       "mcastBwEndIp": mcastBwEndIp,
       "mcastBwBandwidth": mcastBwBandwidth,
       "mcastBwRowStatus": mcastBwRowStatus,
       "mcastBwPortTable": mcastBwPortTable,
       "mcastBwPortEntry": mcastBwPortEntry,
       "mcastBwPortEnable": mcastBwPortEnable,
       "mcastBwPortBandwidth": mcastBwPortBandwidth,
       "igmpCount": igmpCount,
       "igmpCountPortTable": igmpCountPortTable,
       "igmpCountPortEntry": igmpCountPortEntry,
       "igmpCountPortEnable": igmpCountPortEnable,
       "igmpCountPortLimit": igmpCountPortLimit,
       "mvlan": mvlan,
       "maxNumOfMvlan": maxNumOfMvlan,
       "mvlanTable": mvlanTable,
       "mvlanEntry": mvlanEntry,
       "mvlanIndex": mvlanIndex,
       "mvlanName": mvlanName,
       "mvlanEgressPorts": mvlanEgressPorts,
       "mvlanUntaggedPorts": mvlanUntaggedPorts,
       "mvlanRowStatus": mvlanRowStatus,
       "mvlanTranslateTable": mvlanTranslateTable,
       "mvlanTranslateEntry": mvlanTranslateEntry,
       "mvlanTranslateIndex": mvlanTranslateIndex,
       "mvlanTranslateStartIp": mvlanTranslateStartIp,
       "mvlanTranslateEndIp": mvlanTranslateEndIp,
       "queryVid": queryVid,
       "maxNumOfQryVid": maxNumOfQryVid,
       "qryVidConfTable": qryVidConfTable,
       "qryVidConfEntry": qryVidConfEntry,
       "qryVid": qryVid,
       "qryVidRowStatus": qryVidRowStatus,
       "qryVidStatusTable": qryVidStatusTable,
       "qryVidStatusEntry": qryVidStatusEntry,
       "qryVidType": qryVidType,
       "igmpVersion": igmpVersion,
       "port": port,
       "subrPortTable": subrPortTable,
       "subrPortEntry": subrPortEntry,
       "subrPortName": subrPortName,
       "subrPortTel": subrPortTel,
       "vdslPort": vdslPort,
       "vdslLineConfTable": vdslLineConfTable,
       "vdslLineConfEntry": vdslLineConfEntry,
       "vdslLineConfUpbo": vdslLineConfUpbo,
       "vdslLineConfVdslProfile": vdslLineConfVdslProfile,
       "vdslLineConfRfiBand": vdslLineConfRfiBand,
       "vdslLineConfIpqosProfile": vdslLineConfIpqosProfile,
       "vdslLineConfVturInp": vdslLineConfVturInp,
       "vdslLineConfVtucInp": vdslLineConfVtucInp,
       "vdslLineConfOptionMask": vdslLineConfOptionMask,
       "vdslLineConfUpboForceLength": vdslLineConfUpboForceLength,
       "vdslLineConfPsdShape": vdslLineConfPsdShape,
       "vdslLineConfDpbo": vdslLineConfDpbo,
       "vdslLineConfDpboParamEsel": vdslLineConfDpboParamEsel,
       "vdslLineConfDpboParamEscma": vdslLineConfDpboParamEscma,
       "vdslLineConfDpboParamEscmb": vdslLineConfDpboParamEscmb,
       "vdslLineConfDpboParamEscmc": vdslLineConfDpboParamEscmc,
       "vdslLineConfDpboParamMus": vdslLineConfDpboParamMus,
       "vdslLineConfDpboParamFmin": vdslLineConfDpboParamFmin,
       "vdslLineConfDpboParamFmax": vdslLineConfDpboParamFmax,
       "vdslLineConfDpboParamPsdId": vdslLineConfDpboParamPsdId,
       "vdslLineConfSraMode": vdslLineConfSraMode,
       "vdslVlan": vdslVlan,
       "vdslPortConfTable": vdslPortConfTable,
       "vdslPortConfEntry": vdslPortConfEntry,
       "vdslPortConfTlsEnable": vdslPortConfTlsEnable,
       "vdslPortConfTlsVid": vdslPortConfTlsVid,
       "vdslPortConfTlsPriority": vdslPortConfTlsPriority,
       "vdslPortConfDtEnable": vdslPortConfDtEnable,
       "vdslPortConfDtSVid": vdslPortConfDtSVid,
       "vdslPortConfDtSPriority": vdslPortConfDtSPriority,
       "vdslPortConfDtCVid": vdslPortConfDtCVid,
       "vdslPortConfDtCPriority": vdslPortConfDtCPriority,
       "vdslPortPvlanTable": vdslPortPvlanTable,
       "vdslPortPvlanEntry": vdslPortPvlanEntry,
       "vdslPortPvlanEtype": vdslPortPvlanEtype,
       "vdslPortPvlanVid": vdslPortPvlanVid,
       "vdslPortPvlanPriority": vdslPortPvlanPriority,
       "vdslPortPvlanRowStatus": vdslPortPvlanRowStatus,
       "vdslRfiCustomTable": vdslRfiCustomTable,
       "vdslRfiCustomEntry": vdslRfiCustomEntry,
       "vdslRfiCustomIndex": vdslRfiCustomIndex,
       "vdslRfiCustomStartFreq": vdslRfiCustomStartFreq,
       "vdslRfiCustomEndFreq": vdslRfiCustomEndFreq,
       "vdslRfiCustomEnable": vdslRfiCustomEnable,
       "vdslLineConfUpboParamTable": vdslLineConfUpboParamTable,
       "vdslLineConfUpboParamEntry": vdslLineConfUpboParamEntry,
       "vdslLineConfUpboParamBand": vdslLineConfUpboParamBand,
       "vdslLineConfUpboParamA": vdslLineConfUpboParamA,
       "vdslLineConfUpboParamB": vdslLineConfUpboParamB,
       "vdslLineConfDpboTable": vdslLineConfDpboTable,
       "vdslLineConfDpboEntry": vdslLineConfDpboEntry,
       "vdslLineConfDpboIndex": vdslLineConfDpboIndex,
       "vdslLineConfDpboTone": vdslLineConfDpboTone,
       "vdslLineConfDpboPsd": vdslLineConfDpboPsd,
       "vdslLineStatusTable": vdslLineStatusTable,
       "vdslLineStatusEntry": vdslLineStatusEntry,
       "vdslLineStatusVturInp": vdslLineStatusVturInp,
       "vdslLineStatusVtucInp": vdslLineStatusVtucInp,
       "pvc": pvc,
       "maxNumOfPvcs": maxNumOfPvcs,
       "pvcTable": pvcTable,
       "pvcEntry": pvcEntry,
       "pvcVpi": pvcVpi,
       "pvcVci": pvcVci,
       "pvcPvid": pvcPvid,
       "pvcPriority": pvcPriority,
       "pvcProfile": pvcProfile,
       "pvcEncap": pvcEncap,
       "pvcRowStatus": pvcRowStatus,
       "pvcPvlanTable": pvcPvlanTable,
       "pvcPvlanEntry": pvcPvlanEntry,
       "pvcPvlanVpi": pvcPvlanVpi,
       "pvcPvlanVci": pvcPvlanVci,
       "pvcPvlanEtype": pvcPvlanEtype,
       "pvcPvlanVid": pvcPvlanVid,
       "pvcPvlanPriority": pvcPvlanPriority,
       "pvcPvlanRowStatus": pvcPvlanRowStatus,
       "pvcStats": pvcStats,
       "pvcStatsTable": pvcStatsTable,
       "pvcStatsEntry": pvcStatsEntry,
       "pvcStatsTxPackets": pvcStatsTxPackets,
       "pvcStatsRxPackets": pvcStatsRxPackets,
       "rpvc": rpvc,
       "rpvcGatewayTable": rpvcGatewayTable,
       "rpvcGatewayEntry": rpvcGatewayEntry,
       "rpvcGatewayIp": rpvcGatewayIp,
       "rpvcGatewayVlanId": rpvcGatewayVlanId,
       "rpvcGatewayRowStatus": rpvcGatewayRowStatus,
       "rpvcGatewayPriority": rpvcGatewayPriority,
       "rpvcTable": rpvcTable,
       "rpvcEntry": rpvcEntry,
       "rpvcVpi": rpvcVpi,
       "rpvcVci": rpvcVci,
       "rpvcEncap": rpvcEncap,
       "rpvcProfile": rpvcProfile,
       "rpvcIp": rpvcIp,
       "rpvcNetmask": rpvcNetmask,
       "rpvcGatewayIpAddress": rpvcGatewayIpAddress,
       "rpvcRowStatus": rpvcRowStatus,
       "rpvcRouteDomainTable": rpvcRouteDomainTable,
       "rpvcRouteDomainEntry": rpvcRouteDomainEntry,
       "rpvcRouteDomainVpi": rpvcRouteDomainVpi,
       "rpvcRouteDomainVci": rpvcRouteDomainVci,
       "rpvcRouteDomainIp": rpvcRouteDomainIp,
       "rpvcRouteDomainNetmask": rpvcRouteDomainNetmask,
       "rpvcRouteDomainRowStatus": rpvcRouteDomainRowStatus,
       "rpvcArpAgingTime": rpvcArpAgingTime,
       "rpvcArpFlush": rpvcArpFlush,
       "dsBcastDisableTable": dsBcastDisableTable,
       "dsBcastDisableEntry": dsBcastDisableEntry,
       "dsBcastDisableVlanId": dsBcastDisableVlanId,
       "dsBcastDisableRowStatus": dsBcastDisableRowStatus,
       "paepvc": paepvc,
       "paepvcTable": paepvcTable,
       "paepvcEntry": paepvcEntry,
       "paepvcVpi": paepvcVpi,
       "paepvcVci": paepvcVci,
       "paepvcPvid": paepvcPvid,
       "paepvcEncap": paepvcEncap,
       "paepvcPriority": paepvcPriority,
       "paepvcProfile": paepvcProfile,
       "paepvcAcName": paepvcAcName,
       "paepvcServiceName": paepvcServiceName,
       "paepvcHelloTime": paepvcHelloTime,
       "paepvcRowStatus": paepvcRowStatus,
       "tlspvc": tlspvc,
       "tlspvcTable": tlspvcTable,
       "tlspvcEntry": tlspvcEntry,
       "tlspvcVpi": tlspvcVpi,
       "tlspvcVci": tlspvcVci,
       "tlspvcSvid": tlspvcSvid,
       "tlspvcEncap": tlspvcEncap,
       "tlspvcSpriority": tlspvcSpriority,
       "tlspvcProfile": tlspvcProfile,
       "tlspvcRowStatus": tlspvcRowStatus,
       "dtpvc": dtpvc,
       "dtpvcTable": dtpvcTable,
       "dtpvcEntry": dtpvcEntry,
       "dtpvcVpi": dtpvcVpi,
       "dtpvcVci": dtpvcVci,
       "dtpvcSvid": dtpvcSvid,
       "dtpvcSpriority": dtpvcSpriority,
       "dtpvcCvid": dtpvcCvid,
       "dtpvcCpriority": dtpvcCpriority,
       "dtpvcEncap": dtpvcEncap,
       "dtpvcProfile": dtpvcProfile,
       "dtpvcRowStatus": dtpvcRowStatus,
       "profile": profile,
       "sraShiftMarginProfile": sraShiftMarginProfile,
       "sraShiftMarginProfileTable": sraShiftMarginProfileTable,
       "sraShiftMarginProfileEntry": sraShiftMarginProfileEntry,
       "sraShiftMarginProfileName": sraShiftMarginProfileName,
       "xtucConfDownshiftSnrMgn": xtucConfDownshiftSnrMgn,
       "xtucConfUpshiftSnrMgn": xtucConfUpshiftSnrMgn,
       "xturConfDownshiftSnrMgn": xturConfDownshiftSnrMgn,
       "xturConfUpshiftSnrMgn": xturConfUpshiftSnrMgn,
       "sraShiftMarginProfileStatus": sraShiftMarginProfileStatus,
       "ipqosProfile": ipqosProfile,
       "maxNumOfIpqosProfiles": maxNumOfIpqosProfiles,
       "ipqosProfileTable": ipqosProfileTable,
       "ipqosProfileEntry": ipqosProfileEntry,
       "ipqosProfileName": ipqosProfileName,
       "ipqosProfileNumOfQueue": ipqosProfileNumOfQueue,
       "ipqosProfileRowStatus": ipqosProfileRowStatus,
       "ipqosProfileQueueTable": ipqosProfileQueueTable,
       "ipqosProfileQueueEntry": ipqosProfileQueueEntry,
       "ipqosProfileQueueIndex": ipqosProfileQueueIndex,
       "ipqosProfileQueuePIR": ipqosProfileQueuePIR,
       "ipqosProfileQueueCIR": ipqosProfileQueueCIR,
       "ipqosProfileQueuePBS": ipqosProfileQueuePBS,
       "ipqosProfileQueueCBS": ipqosProfileQueueCBS,
       "ipqosProfileQueueLevel": ipqosProfileQueueLevel,
       "ipqosProfileQueueWeight": ipqosProfileQueueWeight,
       "switch": switch,
       "managementVLANId": managementVLANId,
       "maxNumOfStaticVlans": maxNumOfStaticVlans,
       "pktfilter": pktfilter,
       "pktFilterPortTable": pktFilterPortTable,
       "pktFilterPortEntry": pktFilterPortEntry,
       "pktFilter": pktFilter,
       "dot1x": dot1x,
       "maxNumberOfRadiusServers": maxNumberOfRadiusServers,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerIp": radiusServerIp,
       "radiusServerPort": radiusServerPort,
       "radiusSharedSecret": radiusSharedSecret,
       "radiusServerRowStatus": radiusServerRowStatus,
       "dot1xEnable": dot1xEnable,
       "dot1xPortTable": dot1xPortTable,
       "dot1xPortEntry": dot1xPortEntry,
       "dot1xPortEnable": dot1xPortEnable,
       "dot1xPortControl": dot1xPortControl,
       "dot1xPortReAuthEnable": dot1xPortReAuthEnable,
       "dot1xPortReAuthPeriod": dot1xPortReAuthPeriod,
       "radiusMode": radiusMode,
       "maxNumberOfRadiusUserProfiles": maxNumberOfRadiusUserProfiles,
       "radiusUserProfileTable": radiusUserProfileTable,
       "radiusUserProfileEntry": radiusUserProfileEntry,
       "radiusUserProfileUserName": radiusUserProfileUserName,
       "radiusUserProfileUserPassword": radiusUserProfileUserPassword,
       "radiusUserProfileRowStatus": radiusUserProfileRowStatus,
       "dot3ad": dot3ad,
       "dot3adTable": dot3adTable,
       "dot3adEntry": dot3adEntry,
       "dot3adGroupId": dot3adGroupId,
       "dot3adEnable": dot3adEnable,
       "lacpPriority": lacpPriority,
       "lacpTimeout": lacpTimeout,
       "portTrunkingTable": portTrunkingTable,
       "portTrunkingEntry": portTrunkingEntry,
       "portTrunkingGroupId": portTrunkingGroupId,
       "portTrunkingStatus": portTrunkingStatus,
       "portTrunkingPortList": portTrunkingPortList,
       "portIsolation": portIsolation,
       "portIsolationEnable": portIsolationEnable,
       "dscp": dscp,
       "dscpMappingTable": dscpMappingTable,
       "dscpMappingEntry": dscpMappingEntry,
       "dscpSrcCodePoint": dscpSrcCodePoint,
       "dscpMapPriority": dscpMapPriority,
       "dscpPortTable": dscpPortTable,
       "dscpPortEntry": dscpPortEntry,
       "dscpStatusEnable": dscpStatusEnable,
       "rstp": rstp,
       "rstpEnable": rstpEnable,
       "vlanIsolation": vlanIsolation,
       "vlanIsolationTable": vlanIsolationTable,
       "vlanIsolationEntry": vlanIsolationEntry,
       "vlanIsolationRowStatus": vlanIsolationRowStatus,
       "enetMtu": enetMtu,
       "enetMtuEntry": enetMtuEntry,
       "tpid": tpid,
       "tpidEntry": tpidEntry,
       "dhcp": dhcp,
       "dhcpRelayEnable": dhcpRelayEnable,
       "dhcpRelay82Table": dhcpRelay82Table,
       "dhcpRelay82Entry": dhcpRelay82Entry,
       "dhcpRelay82PrimaryServer": dhcpRelay82PrimaryServer,
       "dhcpRelay82SecondaryServer": dhcpRelay82SecondaryServer,
       "dhcpRelay82ActiveServer": dhcpRelay82ActiveServer,
       "dhcpRelay82Enable": dhcpRelay82Enable,
       "dhcpRelay82Info": dhcpRelay82Info,
       "dhcpRelay82RelayMode": dhcpRelay82RelayMode,
       "dhcpRelay82RowStatus": dhcpRelay82RowStatus,
       "dhcpRelay82Suboption2Enable": dhcpRelay82Suboption2Enable,
       "dhcpRelay82Suboption2Info": dhcpRelay82Suboption2Info,
       "dhcpRelay82EntryEnable": dhcpRelay82EntryEnable,
       "dhcpRelay82EntryOptionMode": dhcpRelay82EntryOptionMode,
       "dhcpRelayOption82Sub1Info": dhcpRelayOption82Sub1Info,
       "maxNumOfDhcpRelay82Conf": maxNumOfDhcpRelay82Conf,
       "dhcpRelayOption82Sub1Enable": dhcpRelayOption82Sub1Enable,
       "dhcpRelayOption82Sub2Info": dhcpRelayOption82Sub2Info,
       "dhcpRelayOption82Sub2Enable": dhcpRelayOption82Sub2Enable,
       "macfilter": macfilter,
       "macFilterPortTable": macFilterPortTable,
       "macFilterPortEntry": macFilterPortEntry,
       "macFilterPortEnable": macFilterPortEnable,
       "macFilterPortMacCount": macFilterPortMacCount,
       "macFilterPortFilterMode": macFilterPortFilterMode,
       "maxNumOfMacFiltersInSystem": maxNumOfMacFiltersInSystem,
       "maxNumOfMacFiltersPerPort": maxNumOfMacFiltersPerPort,
       "currNumOfMacFiltersInSystem": currNumOfMacFiltersInSystem,
       "macFilterTable": macFilterTable,
       "macFilterEntry": macFilterEntry,
       "macFilterAddr": macFilterAddr,
       "macFilterRowStatus": macFilterRowStatus,
       "macfilterBatchSet": macfilterBatchSet,
       "macfilterTarget": macfilterTarget,
       "macfilterOps": macfilterOps,
       "macFilterMacCountForBatchSet": macFilterMacCountForBatchSet,
       "ouiFilterTable": ouiFilterTable,
       "ouiFilterEntry": ouiFilterEntry,
       "ouiFilterAddr": ouiFilterAddr,
       "ouiFilterRowStatus": ouiFilterRowStatus,
       "maxNumOfOuiFiltersPerPort": maxNumOfOuiFiltersPerPort,
       "ouiFilterPortTable": ouiFilterPortTable,
       "ouiFilterPortEntry": ouiFilterPortEntry,
       "ouiFilterPortEnable": ouiFilterPortEnable,
       "ouiFilterPortFilterMode": ouiFilterPortFilterMode,
       "dhcpSnoop": dhcpSnoop,
       "dhcpSnoopPortTable": dhcpSnoopPortTable,
       "dhcpSnoopPortEntry": dhcpSnoopPortEntry,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopTarget": dhcpSnoopTarget,
       "dhcpSnoopOps": dhcpSnoopOps,
       "dhcpStaticTable": dhcpStaticTable,
       "dhcpStaticEntry": dhcpStaticEntry,
       "dhcpStaticIpAddr": dhcpStaticIpAddr,
       "dhcpStaticRowStatus": dhcpStaticRowStatus,
       "maxNumOfDhcpStaticIp": maxNumOfDhcpStaticIp,
       "acl": acl,
       "aclSetTable": aclSetTable,
       "aclSetEntry": aclSetEntry,
       "aclSetVpi": aclSetVpi,
       "aclSetVci": aclSetVci,
       "aclSetProfileName": aclSetProfileName,
       "aclSetRowStatus": aclSetRowStatus,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileRuleName": aclProfileRuleName,
       "aclProfileRuleNumber": aclProfileRuleNumber,
       "aclProfileActionNumber": aclProfileActionNumber,
       "aclProfileRuleParamMask": aclProfileRuleParamMask,
       "aclProfileRuleEtype": aclProfileRuleEtype,
       "aclProfileRuleVid": aclProfileRuleVid,
       "aclProfileRuleSmac": aclProfileRuleSmac,
       "aclProfileRuleDmac": aclProfileRuleDmac,
       "aclProfileRulePriority": aclProfileRulePriority,
       "aclProfileRuleProtocol": aclProfileRuleProtocol,
       "aclProfileActionRate": aclProfileActionRate,
       "aclProfileActionrvlan": aclProfileActionrvlan,
       "aclProfileActionrpri": aclProfileActionrpri,
       "aclProfileRowStatus": aclProfileRowStatus,
       "aclProfileRuleSip": aclProfileRuleSip,
       "aclProfileRuleDip": aclProfileRuleDip,
       "aclProfileRuleSport": aclProfileRuleSport,
       "aclProfileRuleDport": aclProfileRuleDport,
       "pppoeAgent": pppoeAgent,
       "pppoeAgentTable": pppoeAgentTable,
       "pppoeAgentEntry": pppoeAgentEntry,
       "pppoeAgentEnable": pppoeAgentEnable,
       "pppoeAgentInfo": pppoeAgentInfo,
       "pppoeAgentRowStatus": pppoeAgentRowStatus,
       "pppoeAgentOptionMode": pppoeAgentOptionMode,
       "maxNumOfPppoeDhcpRelay82Conf": maxNumOfPppoeDhcpRelay82Conf,
       "n1mac": n1mac,
       "n1macReplaceMac": n1macReplaceMac,
       "n1macPortTable": n1macPortTable,
       "n1macPortEntry": n1macPortEntry,
       "n1macStatusEnable": n1macStatusEnable,
       "enetPort": enetPort,
       "enetPortConfTable": enetPortConfTable,
       "enetPortConfEntry": enetPortConfEntry,
       "enetPortId": enetPortId,
       "enetPortType": enetPortType,
       "enetPortIfIndex": enetPortIfIndex,
       "enetPortSpeed": enetPortSpeed,
       "macff": macff,
       "macFfTable": macFfTable,
       "macFfEntry": macFfEntry,
       "macFfIndex": macFfIndex,
       "macFfVid": macFfVid,
       "macFfArIP": macFfArIP,
       "macFfSrcIP": macFfSrcIP,
       "macFfSrcMask": macFfSrcMask,
       "macFfArMac": macFfArMac,
       "macFfRowStatus": macFfRowStatus,
       "macFfArpAgingTime": macFfArpAgingTime,
       "macFfArpFlush": macFfArpFlush,
       "managementPriority": managementPriority,
       "macAntiSpoof": macAntiSpoof,
       "macAntiSpoofEnable": macAntiSpoofEnable,
       "sys": sys,
       "sysState": sysState,
       "systemStatus": systemStatus,
       "problemCause": problemCause,
       "hwMonitor": hwMonitor,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageCurValue": voltageCurValue,
       "voltageMaxValue": voltageMaxValue,
       "voltageMinValue": voltageMinValue,
       "voltageNominalValue": voltageNominalValue,
       "voltageLowThresh": voltageLowThresh,
       "voltageDescr": voltageDescr,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureCurValue": temperatureCurValue,
       "temperatureMaxValue": temperatureMaxValue,
       "temperatureMinValue": temperatureMinValue,
       "temperatureHighThresh": temperatureHighThresh,
       "temperatureDescr": temperatureDescr,
       "timeSetup": timeSetup,
       "timeServerMode": timeServerMode,
       "timeServerIP": timeServerIP,
       "systemTime": systemTime,
       "systemDate": systemDate,
       "systemTimeZone": systemTimeZone,
       "timeServerSync": timeServerSync,
       "timeServerSyncStatus": timeServerSyncStatus,
       "accessCtrl": accessCtrl,
       "accessCtrlTable": accessCtrlTable,
       "accessCtrlEntry": accessCtrlEntry,
       "accessCtrlService": accessCtrlService,
       "accessCtrlEnable": accessCtrlEnable,
       "accessCtrlPort": accessCtrlPort,
       "maxNumOfSecuredClients": maxNumOfSecuredClients,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "securedClientEnable": securedClientEnable,
       "syslog": syslog,
       "sysLogEnable": sysLogEnable,
       "sysLogServer": sysLogServer,
       "sysLogFacility": sysLogFacility,
       "snmp": snmp,
       "maxNumberOfTrapDestinations": maxNumberOfTrapDestinations,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestEntry": snmpTrapDestEntry,
       "trapDestIp": trapDestIp,
       "trapDestPort": trapDestPort,
       "trapDestRowStatus": trapDestRowStatus,
       "snmpGetCommunity": snmpGetCommunity,
       "snmpSetCommunity": snmpSetCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "extAlarm": extAlarm,
       "extAlarmTable": extAlarmTable,
       "extAlarmEntry": extAlarmEntry,
       "extAlarmIndex": extAlarmIndex,
       "extAlarmName": extAlarmName,
       "extAlarmStatus": extAlarmStatus,
       "user": user,
       "userAuthMode": userAuthMode,
       "userAuthServerIp": userAuthServerIp,
       "userAuthServerPort": userAuthServerPort,
       "userAuthServerSecret": userAuthServerSecret,
       "userTable": userTable,
       "userEntry": userEntry,
       "userName": userName,
       "userPassword": userPassword,
       "userPriviledge": userPriviledge,
       "userRowStatus": userRowStatus,
       "userAuthDefaultPriviledge": userAuthDefaultPriviledge,
       "usbCastCtrl": usbCastCtrl,
       "usBcastCtrlEnable": usBcastCtrlEnable,
       "usBcastCtrlRate": usBcastCtrlRate,
       "info": info,
       "serialNumber": serialNumber,
       "moduleDescr": moduleDescr,
       "fWVersion": fWVersion,
       "driverVersion": driverVersion,
       "modemCodeVersion": modemCodeVersion,
       "sysMaintain": sysMaintain,
       "maintenanceOps": maintenanceOps,
       "maintenanceTarget": maintenanceTarget,
       "maintenanceDSLConfOps": maintenanceDSLConfOps,
       "maintenanceDSLConfTarget": maintenanceDSLConfTarget,
       "maintenanceDSLConfProfileName": maintenanceDSLConfProfileName,
       "maintenanceDSLConfMode": maintenanceDSLConfMode,
       "maintenanceDSLConfPktFilter": maintenanceDSLConfPktFilter,
       "maintenanceDSLConfDot1xControl": maintenanceDSLConfDot1xControl,
       "maintenanceDSLConfDot1xReauthPeriod": maintenanceDSLConfDot1xReauthPeriod,
       "maintenanceDSLConfMacCount": maintenanceDSLConfMacCount,
       "maintenanceVpi": maintenanceVpi,
       "maintenanceVci": maintenanceVci,
       "maintenanceDSLConfAlarmProfileName": maintenanceDSLConfAlarmProfileName,
       "maintenanceDSLConfAnnexL": maintenanceDSLConfAnnexL,
       "maintenanceDSLConfPmMode": maintenanceDSLConfPmMode,
       "maintenanceDSLConfRateMode": maintenanceDSLConfRateMode,
       "maintenanceDSLConfIgmpFilter": maintenanceDSLConfIgmpFilter,
       "trap": trap,
       "object": object,
       "eqptAlarmInputIndex": eqptAlarmInputIndex,
       "eqptAlarmInputName": eqptAlarmInputName,
       "sysMacAntiSpoofOrig": sysMacAntiSpoofOrig,
       "sysMacAntiSpoofNew": sysMacAntiSpoofNew,
       "sysMacAntiSpoofMAC": sysMacAntiSpoofMAC,
       "equipment": equipment,
       "eqptVoltageError": eqptVoltageError,
       "eqptVoltageNormal": eqptVoltageNormal,
       "eqptTempError": eqptTempError,
       "eqptTempNormal": eqptTempNormal,
       "eqptHWMonitorFailure": eqptHWMonitorFailure,
       "eqptExternalAlarmInput": eqptExternalAlarmInput,
       "eqptExternalAlarmInputRelease": eqptExternalAlarmInputRelease,
       "systrap": systrap,
       "sysReboot": sysReboot,
       "sysMacAntiSpoofing": sysMacAntiSpoofing,
       "statistics": statistics,
       "igmpStats": igmpStats,
       "igmpQueryCntTotal": igmpQueryCntTotal,
       "igmpReportCntTotal": igmpReportCntTotal,
       "igmpLeaveCntTotal": igmpLeaveCntTotal,
       "igmpNumOfActiveGroups": igmpNumOfActiveGroups,
       "igmpGroupV2Table": igmpGroupV2Table,
       "igmpGroupV2Entry": igmpGroupV2Entry,
       "igmpGroupV2Vid": igmpGroupV2Vid,
       "igmpGroupV2Ip": igmpGroupV2Ip,
       "igmpGroupV2NumOfMembers": igmpGroupV2NumOfMembers,
       "igmpGroupV2MemberPorts": igmpGroupV2MemberPorts,
       "igmpGroupPortV2Table": igmpGroupPortV2Table,
       "igmpGroupPortV2Entry": igmpGroupPortV2Entry,
       "igmpGroupPortV2Vid": igmpGroupPortV2Vid,
       "igmpGroupPortV2Ip": igmpGroupPortV2Ip,
       "igmpGroupPortV2SourceIp": igmpGroupPortV2SourceIp,
       "igmpPortCtrlPduTable": igmpPortCtrlPduTable,
       "igmpPortCtrlPduEntry": igmpPortCtrlPduEntry,
       "igmpPortCtrlPduQueryCnt": igmpPortCtrlPduQueryCnt,
       "igmpPortCtrlPduReportCnt": igmpPortCtrlPduReportCnt,
       "igmpPortCtrlPduLeaveCnt": igmpPortCtrlPduLeaveCnt,
       "igmpPortNumOfActiveGroups": igmpPortNumOfActiveGroups,
       "vdslStats": vdslStats,
       "vdslLineStatsTable": vdslLineStatsTable,
       "vdslLineStatsEntry": vdslLineStatsEntry,
       "vdslLineStatsVtucBits1": vdslLineStatsVtucBits1,
       "vdslLineStatsVtucBits2": vdslLineStatsVtucBits2,
       "vdslLineStatsVtucBits3": vdslLineStatsVtucBits3,
       "vdslLineStatsVtucBits4": vdslLineStatsVtucBits4,
       "vdslLineStatsVturBits1": vdslLineStatsVturBits1,
       "vdslLineStatsVturBits2": vdslLineStatsVturBits2,
       "vdslLineStatsVturBits3": vdslLineStatsVturBits3,
       "vdslLineStatsVturBits4": vdslLineStatsVturBits4,
       "vdslLineStatsVtucGain1": vdslLineStatsVtucGain1,
       "vdslLineStatsVtucGain2": vdslLineStatsVtucGain2,
       "vdslLineStatsVtucGain3": vdslLineStatsVtucGain3,
       "vdslLineStatsVtucGain4": vdslLineStatsVtucGain4,
       "vdslLineStatsVtucGain5": vdslLineStatsVtucGain5,
       "vdslLineStatsVtucGain6": vdslLineStatsVtucGain6,
       "vdslLineStatsVtucGain7": vdslLineStatsVtucGain7,
       "vdslLineStatsVtucGain8": vdslLineStatsVtucGain8,
       "vdslLineStatsVturGain1": vdslLineStatsVturGain1,
       "vdslLineStatsVturGain2": vdslLineStatsVturGain2,
       "vdslLineStatsVturGain3": vdslLineStatsVturGain3,
       "vdslLineStatsVturGain4": vdslLineStatsVturGain4,
       "vdslLineStatsVturGain5": vdslLineStatsVturGain5,
       "vdslLineStatsVturGain6": vdslLineStatsVturGain6,
       "vdslLineStatsVturGain7": vdslLineStatsVturGain7,
       "vdslLineStatsVturGain8": vdslLineStatsVturGain8,
       "vdslLineStatsVtucHlog": vdslLineStatsVtucHlog,
       "vdslLineStatsVturHlog": vdslLineStatsVturHlog,
       "vdslLineStatsVtucQln": vdslLineStatsVtucQln,
       "vdslLineStatsVturQln": vdslLineStatsVturQln,
       "vdslLineStatsVtucSnr": vdslLineStatsVtucSnr,
       "vdslLineStatsVturSnr": vdslLineStatsVturSnr,
       "vdslLineStatsVtucTssi": vdslLineStatsVtucTssi,
       "vdslLineStatsVturTssi": vdslLineStatsVturTssi,
       "vdslLineStatsProtocol": vdslLineStatsProtocol,
       "dhcpStats": dhcpStats,
       "dhcpSnoopIpTable": dhcpSnoopIpTable,
       "dhcpSnoopIpEntry": dhcpSnoopIpEntry,
       "dhcpSnoopIp": dhcpSnoopIp,
       "dhcpSnoopMac": dhcpSnoopMac,
       "dhcpSnoopVid": dhcpSnoopVid,
       "dhcpSnoopCounterTable": dhcpSnoopCounterTable,
       "dhcpSnoopCounterEntry": dhcpSnoopCounterEntry,
       "dhcpDiscovery": dhcpDiscovery,
       "dhcpOffer": dhcpOffer,
       "dhcpRequest": dhcpRequest,
       "dhcpAck": dhcpAck,
       "dhcpAckBySnoopFull": dhcpAckBySnoopFull,
       "paepvcStats": paepvcStats,
       "paepvcSessionTable": paepvcSessionTable,
       "paepvcSessionEntry": paepvcSessionEntry,
       "paepvcSessionVpi": paepvcSessionVpi,
       "paepvcSessionVci": paepvcSessionVci,
       "paepvcSessionState": paepvcSessionState,
       "paepvcSessionId": paepvcSessionId,
       "paepvcSessionUptime": paepvcSessionUptime,
       "paepvcSessionacname": paepvcSessionacname,
       "paepvcSessionsrvcname": paepvcSessionsrvcname,
       "paepvcCountTable": paepvcCountTable,
       "paepvcCountEntry": paepvcCountEntry,
       "paepvcCountVpi": paepvcCountVpi,
       "paepvcCountVci": paepvcCountVci,
       "paepvcCountPppLcpCfgReqRx": paepvcCountPppLcpCfgReqRx,
       "paepvcCountPppLcpEchoReqRx": paepvcCountPppLcpEchoReqRx,
       "paepvcCountPppLcpEchoReplyRx": paepvcCountPppLcpEchoReplyRx,
       "paepvcCountPadiTx": paepvcCountPadiTx,
       "paepvcCountPadoRx": paepvcCountPadoRx,
       "paepvcCountPadrTx": paepvcCountPadrTx,
       "paepvcCountPadsRx": paepvcCountPadsRx,
       "paepvcCountPadtTx": paepvcCountPadtTx,
       "paepvcCountPadtRx": paepvcCountPadtRx,
       "paepvcCountSrvcnameErrRx": paepvcCountSrvcnameErrRx,
       "paepvcCountAcSystemErrRx": paepvcCountAcSystemErrRx,
       "paepvcCountGenericErrTx": paepvcCountGenericErrTx,
       "paepvcCountGenericErrRx": paepvcCountGenericErrRx,
       "macStats": macStats,
       "macDisplayTarget": macDisplayTarget,
       "macTable": macTable,
       "macEntry": macEntry,
       "macAddress": macAddress,
       "macPort": macPort,
       "macStatus": macStatus,
       "macVid": macVid,
       "macFlush": macFlush,
       "n1macStats": n1macStats,
       "n1macTable": n1macTable,
       "n1macEntry": n1macEntry,
       "n1macProtoVal": n1macProtoVal,
       "n1macProtoType": n1macProtoType,
       "n1macMacAddr": n1macMacAddr,
       "enetStats": enetStats,
       "enetPrimaryPort": enetPrimaryPort,
       "clear": clear,
       "counterClearTarget": counterClearTarget,
       "counterClearOps": counterClearOps,
       "counterClearVpi": counterClearVpi,
       "counterClearVci": counterClearVci}
)
