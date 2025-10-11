# SNMP MIB module (AFFIRMED-MME-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsoft/AFFIRMED-MME-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:32 2025
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

(alarmActiveDateAndTime,
 alarmActiveIndex,
 alarmListName,
 alarmModelIndex,
 alarmModelState) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmActiveDateAndTime",
    "alarmActiveIndex",
    "alarmListName",
    "alarmModelIndex",
    "alarmModelState")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

affirmedSnmpMmeTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6)
)
if mibBuilder.loadTexts:
    affirmedSnmpMmeTraps.setRevisions(
        ("2016-09-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AnMmeTrapAlarms_ObjectIdentity = ObjectIdentity
anMmeTrapAlarms = _AnMmeTrapAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1)
)
_AnMmeTrapEvents_ObjectIdentity = ObjectIdentity
anMmeTrapEvents = _AnMmeTrapEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2)
)
_AnMmeNotificationVars_ObjectIdentity = ObjectIdentity
anMmeNotificationVars = _AnMmeNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3)
)


class _AnMmeAlarmState_Type(SnmpAdminString):
    """Custom type anMmeAlarmState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AnMmeAlarmState_Type.__name__ = "SnmpAdminString"
_AnMmeAlarmState_Object = MibScalar
anMmeAlarmState = _AnMmeAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 1),
    _AnMmeAlarmState_Type()
)
anMmeAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeAlarmState.setStatus("current")
_AnMmeAlarmSeverity_Type = ItuPerceivedSeverity
_AnMmeAlarmSeverity_Object = MibScalar
anMmeAlarmSeverity = _AnMmeAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 2),
    _AnMmeAlarmSeverity_Type()
)
anMmeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeAlarmSeverity.setStatus("current")


class _AnMmeEntityTag_Type(SnmpAdminString):
    """Custom type anMmeEntityTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeEntityTag_Type.__name__ = "SnmpAdminString"
_AnMmeEntityTag_Object = MibScalar
anMmeEntityTag = _AnMmeEntityTag_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 3),
    _AnMmeEntityTag_Type()
)
anMmeEntityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeEntityTag.setStatus("current")


class _AnMmeSubentityInfo_Type(SnmpAdminString):
    """Custom type anMmeSubentityInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeSubentityInfo_Type.__name__ = "SnmpAdminString"
_AnMmeSubentityInfo_Object = MibScalar
anMmeSubentityInfo = _AnMmeSubentityInfo_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 4),
    _AnMmeSubentityInfo_Type()
)
anMmeSubentityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeSubentityInfo.setStatus("current")


class _AnMmeLocationGateway_Type(SnmpAdminString):
    """Custom type anMmeLocationGateway based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeLocationGateway_Type.__name__ = "SnmpAdminString"
_AnMmeLocationGateway_Object = MibScalar
anMmeLocationGateway = _AnMmeLocationGateway_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 5),
    _AnMmeLocationGateway_Type()
)
anMmeLocationGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeLocationGateway.setStatus("deprecated")


class _AnMmeReason_Type(SnmpAdminString):
    """Custom type anMmeReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeReason_Type.__name__ = "SnmpAdminString"
_AnMmeReason_Object = MibScalar
anMmeReason = _AnMmeReason_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 6),
    _AnMmeReason_Type()
)
anMmeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeReason.setStatus("current")
_AnMmeAlarmDateAndTime_Type = DateAndTime
_AnMmeAlarmDateAndTime_Object = MibScalar
anMmeAlarmDateAndTime = _AnMmeAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 7),
    _AnMmeAlarmDateAndTime_Type()
)
anMmeAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeAlarmDateAndTime.setStatus("current")


class _AnMmeGroupKey_Type(SnmpAdminString):
    """Custom type anMmeGroupKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeGroupKey_Type.__name__ = "SnmpAdminString"
_AnMmeGroupKey_Object = MibScalar
anMmeGroupKey = _AnMmeGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 8),
    _AnMmeGroupKey_Type()
)
anMmeGroupKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeGroupKey.setStatus("current")
_AnMmeSequenceNumber_Type = Unsigned32
_AnMmeSequenceNumber_Object = MibScalar
anMmeSequenceNumber = _AnMmeSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 9),
    _AnMmeSequenceNumber_Type()
)
anMmeSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeSequenceNumber.setStatus("current")
_AnMmeFirstEvent_Type = DateAndTime
_AnMmeFirstEvent_Object = MibScalar
anMmeFirstEvent = _AnMmeFirstEvent_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 10),
    _AnMmeFirstEvent_Type()
)
anMmeFirstEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeFirstEvent.setStatus("current")
_AnMmeLastEvent_Type = DateAndTime
_AnMmeLastEvent_Object = MibScalar
anMmeLastEvent = _AnMmeLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 11),
    _AnMmeLastEvent_Type()
)
anMmeLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeLastEvent.setStatus("current")


class _AnMmeLocation_Type(SnmpAdminString):
    """Custom type anMmeLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeLocation_Type.__name__ = "SnmpAdminString"
_AnMmeLocation_Object = MibScalar
anMmeLocation = _AnMmeLocation_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 12),
    _AnMmeLocation_Type()
)
anMmeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeLocation.setStatus("current")


class _AnMmeService_Type(SnmpAdminString):
    """Custom type anMmeService based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AnMmeService_Type.__name__ = "SnmpAdminString"
_AnMmeService_Object = MibScalar
anMmeService = _AnMmeService_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 13),
    _AnMmeService_Type()
)
anMmeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeService.setStatus("current")
_AnMmeAlarmIndex_Type = Unsigned32
_AnMmeAlarmIndex_Object = MibScalar
anMmeAlarmIndex = _AnMmeAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 3, 14),
    _AnMmeAlarmIndex_Type()
)
anMmeAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anMmeAlarmIndex.setStatus("current")

# Managed Objects groups


# Notification objects

anMmeTrapAlarmNm1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 65536001)
)
anMmeTrapAlarmNm1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmNm1300.setStatus(
        "current"
    )

anMmeTrapAlarmNm1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 65536002)
)
anMmeTrapAlarmNm1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmNm1301.setStatus(
        "current"
    )

anMmeTrapAlarmNm1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 65536003)
)
anMmeTrapAlarmNm1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmNm1302.setStatus(
        "current"
    )

anMmeTrapAlarmNm1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 65536099)
)
anMmeTrapAlarmNm1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmNm1399.setStatus(
        "current"
    )

anMmeTrapAlarmResmon1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 66191361)
)
anMmeTrapAlarmResmon1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmResmon1301.setStatus(
        "current"
    )

anMmeTrapAlarmResmon1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 66191459)
)
anMmeTrapAlarmResmon1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmResmon1399.setStatus(
        "current"
    )

anMmeTrapAlarmGaBilling1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133693441)
)
anMmeTrapAlarmGaBilling1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmGaBilling1300.setStatus(
        "current"
    )

anMmeTrapAlarmGaBilling1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133693443)
)
anMmeTrapAlarmGaBilling1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmGaBilling1301.setStatus(
        "current"
    )

anMmeTrapAlarmGaBilling1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133693539)
)
anMmeTrapAlarmGaBilling1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmGaBilling1399.setStatus(
        "current"
    )

anMmeTrapAlarmLi1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758977)
)
anMmeTrapAlarmLi1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1300.setStatus(
        "current"
    )

anMmeTrapAlarmLi1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758978)
)
anMmeTrapAlarmLi1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1301.setStatus(
        "current"
    )

anMmeTrapAlarmLi1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758979)
)
anMmeTrapAlarmLi1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1302.setStatus(
        "current"
    )

anMmeTrapAlarmLi1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758980)
)
anMmeTrapAlarmLi1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1303.setStatus(
        "current"
    )

anMmeTrapAlarmLi1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758981)
)
anMmeTrapAlarmLi1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1304.setStatus(
        "current"
    )

anMmeTrapAlarmLi1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758982)
)
anMmeTrapAlarmLi1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1305.setStatus(
        "current"
    )

anMmeTrapAlarmLi1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758983)
)
anMmeTrapAlarmLi1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1306.setStatus(
        "current"
    )

anMmeTrapAlarmLi1307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758984)
)
anMmeTrapAlarmLi1307.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1307.setStatus(
        "current"
    )

anMmeTrapAlarmLi1308 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758985)
)
anMmeTrapAlarmLi1308.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1308.setStatus(
        "current"
    )

anMmeTrapAlarmLi1309 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758986)
)
anMmeTrapAlarmLi1309.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1309.setStatus(
        "current"
    )

anMmeTrapAlarmLi1310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133758987)
)
anMmeTrapAlarmLi1310.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1310.setStatus(
        "current"
    )

anMmeTrapAlarmLi1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133759075)
)
anMmeTrapAlarmLi1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLi1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeRm1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133824513)
)
anMmeTrapAlarmMmeRm1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeRm1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeRm1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133824514)
)
anMmeTrapAlarmMmeRm1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeRm1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeRm1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133824515)
)
anMmeTrapAlarmMmeRm1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeRm1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeRm1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133824516)
)
anMmeTrapAlarmMmeRm1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeRm1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeRm1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133824611)
)
anMmeTrapAlarmMmeRm1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeRm1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890051)
)
anMmeTrapAlarmMmeS1M1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890052)
)
anMmeTrapAlarmMmeS1M1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890053)
)
anMmeTrapAlarmMmeS1M1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890054)
)
anMmeTrapAlarmMmeS1M1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890055)
)
anMmeTrapAlarmMmeS1M1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1306.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890056)
)
anMmeTrapAlarmMmeS1M1307.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1307.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1308 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890057)
)
anMmeTrapAlarmMmeS1M1308.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1308.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1309 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890058)
)
anMmeTrapAlarmMmeS1M1309.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1309.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890059)
)
anMmeTrapAlarmMmeS1M1310.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1310.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1311 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890060)
)
anMmeTrapAlarmMmeS1M1311.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1311.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1M1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133890147)
)
anMmeTrapAlarmMmeS1M1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1M1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955585)
)
anMmeTrapAlarmMmeUpsm1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955587)
)
anMmeTrapAlarmMmeUpsm1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955588)
)
anMmeTrapAlarmMmeUpsm1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955589)
)
anMmeTrapAlarmMmeUpsm1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955590)
)
anMmeTrapAlarmMmeUpsm1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955591)
)
anMmeTrapAlarmMmeUpsm1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1306.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955592)
)
anMmeTrapAlarmMmeUpsm1307.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1307.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1308 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955593)
)
anMmeTrapAlarmMmeUpsm1308.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1308.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1309 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955594)
)
anMmeTrapAlarmMmeUpsm1309.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1309.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955595)
)
anMmeTrapAlarmMmeUpsm1310.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1310.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpsm1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 133955683)
)
anMmeTrapAlarmMmeUpsm1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpsm1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeIlf1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134021121)
)
anMmeTrapAlarmMmeIlf1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeIlf1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeIlf1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134021122)
)
anMmeTrapAlarmMmeIlf1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeIlf1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeIlf1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134021219)
)
anMmeTrapAlarmMmeIlf1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeIlf1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1Server1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134086657)
)
anMmeTrapAlarmMmeS1Server1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1Server1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1Server1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134086658)
)
anMmeTrapAlarmMmeS1Server1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1Server1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1Server1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134086755)
)
anMmeTrapAlarmMmeS1Server1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1Server1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1Enb1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134152193)
)
anMmeTrapAlarmMmeS1Enb1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1Enb1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeS1Enb1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134152291)
)
anMmeTrapAlarmMmeS1Enb1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeS1Enb1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217729)
)
anMmeTrapAlarmMmeDc1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217730)
)
anMmeTrapAlarmMmeDc1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217731)
)
anMmeTrapAlarmMmeDc1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217732)
)
anMmeTrapAlarmMmeDc1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217733)
)
anMmeTrapAlarmMmeDc1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217734)
)
anMmeTrapAlarmMmeDc1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217735)
)
anMmeTrapAlarmMmeDc1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1306.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217736)
)
anMmeTrapAlarmMmeDc1307.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1307.setStatus(
        "current"
    )

anMmeTrapAlarmMmeDc1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134217827)
)
anMmeTrapAlarmMmeDc1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeDc1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283266)
)
anMmeTrapAlarmMmeSc1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283267)
)
anMmeTrapAlarmMmeSc1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283268)
)
anMmeTrapAlarmMmeSc1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283269)
)
anMmeTrapAlarmMmeSc1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283270)
)
anMmeTrapAlarmMmeSc1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283271)
)
anMmeTrapAlarmMmeSc1310.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1310.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1311 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283272)
)
anMmeTrapAlarmMmeSc1311.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1311.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283273)
)
anMmeTrapAlarmMmeSc1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1306.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283274)
)
anMmeTrapAlarmMmeSc1307.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1307.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1308 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283275)
)
anMmeTrapAlarmMmeSc1308.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1308.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1309 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283276)
)
anMmeTrapAlarmMmeSc1309.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1309.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1320 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283277)
)
anMmeTrapAlarmMmeSc1320.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1320.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1312 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283278)
)
anMmeTrapAlarmMmeSc1312.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1312.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1313 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283279)
)
anMmeTrapAlarmMmeSc1313.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1313.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1314 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283280)
)
anMmeTrapAlarmMmeSc1314.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1314.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1315 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283281)
)
anMmeTrapAlarmMmeSc1315.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1315.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1316 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283282)
)
anMmeTrapAlarmMmeSc1316.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1316.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1317 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283283)
)
anMmeTrapAlarmMmeSc1317.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1317.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1318 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283284)
)
anMmeTrapAlarmMmeSc1318.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1318.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1321 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283288)
)
anMmeTrapAlarmMmeSc1321.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1321.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1322 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283289)
)
anMmeTrapAlarmMmeSc1322.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1322.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1323 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283290)
)
anMmeTrapAlarmMmeSc1323.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1323.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1324 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283291)
)
anMmeTrapAlarmMmeSc1324.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1324.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1325 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283292)
)
anMmeTrapAlarmMmeSc1325.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1325.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSc1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134283363)
)
anMmeTrapAlarmMmeSc1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSc1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpm1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134545409)
)
anMmeTrapAlarmMmeUpm1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpm1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpm1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134545410)
)
anMmeTrapAlarmMmeUpm1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpm1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpm1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134545411)
)
anMmeTrapAlarmMmeUpm1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpm1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpm1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134545412)
)
anMmeTrapAlarmMmeUpm1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpm1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpm1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134545413)
)
anMmeTrapAlarmMmeUpm1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpm1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeUpm1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 134545507)
)
anMmeTrapAlarmMmeUpm1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeUpm1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593985)
)
anMmeTrapAlarmMmeSigtran1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593986)
)
anMmeTrapAlarmMmeSigtran1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593987)
)
anMmeTrapAlarmMmeSigtran1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593988)
)
anMmeTrapAlarmMmeSigtran1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593989)
)
anMmeTrapAlarmMmeSigtran1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593990)
)
anMmeTrapAlarmMmeSigtran1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593991)
)
anMmeTrapAlarmMmeSigtran1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1306.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593992)
)
anMmeTrapAlarmMmeSigtran1307.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1307.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1308 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135593993)
)
anMmeTrapAlarmMmeSigtran1308.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1308.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSigtran1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135594083)
)
anMmeTrapAlarmMmeSigtran1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSigtran1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeTcap1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135659521)
)
anMmeTrapAlarmMmeTcap1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeTcap1303.setStatus(
        "current"
    )

anMmeTrapAlarmMmeTcap1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135659522)
)
anMmeTrapAlarmMmeTcap1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeTcap1304.setStatus(
        "current"
    )

anMmeTrapAlarmMmeTcap1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135659523)
)
anMmeTrapAlarmMmeTcap1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeTcap1305.setStatus(
        "current"
    )

anMmeTrapAlarmMmeTcap1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135659524)
)
anMmeTrapAlarmMmeTcap1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeTcap1306.setStatus(
        "current"
    )

anMmeTrapAlarmMmeTcap1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 135659619)
)
anMmeTrapAlarmMmeTcap1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeTcap1399.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIu1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136314881)
)
anMmeTrapAlarmSgsnIu1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIu1300.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIu1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136314882)
)
anMmeTrapAlarmSgsnIu1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIu1301.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIu1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136314883)
)
anMmeTrapAlarmSgsnIu1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIu1303.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIu1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136314884)
)
anMmeTrapAlarmSgsnIu1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIu1304.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIu1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136314979)
)
anMmeTrapAlarmSgsnIu1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIu1399.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIpSp1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136380417)
)
anMmeTrapAlarmSgsnIpSp1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIpSp1300.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIpSp1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136380418)
)
anMmeTrapAlarmSgsnIpSp1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIpSp1301.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIpSp1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136380419)
)
anMmeTrapAlarmSgsnIpSp1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIpSp1302.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIpSp1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136380420)
)
anMmeTrapAlarmSgsnIpSp1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIpSp1303.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIpSp1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136380421)
)
anMmeTrapAlarmSgsnIpSp1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIpSp1304.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnIpSp1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136380515)
)
anMmeTrapAlarmSgsnIpSp1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnIpSp1399.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnSd1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136445953)
)
anMmeTrapAlarmSgsnSd1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnSd1300.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnSd1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136445954)
)
anMmeTrapAlarmSgsnSd1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnSd1301.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnSd1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136445955)
)
anMmeTrapAlarmSgsnSd1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnSd1302.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnSd1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136446051)
)
anMmeTrapAlarmSgsnSd1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnSd1399.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511489)
)
anMmeTrapAlarmSgsnGb1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1300.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511490)
)
anMmeTrapAlarmSgsnGb1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1301.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511491)
)
anMmeTrapAlarmSgsnGb1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1302.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511492)
)
anMmeTrapAlarmSgsnGb1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1303.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511493)
)
anMmeTrapAlarmSgsnGb1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1304.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511494)
)
anMmeTrapAlarmSgsnGb1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1305.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511495)
)
anMmeTrapAlarmSgsnGb1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1306.setStatus(
        "current"
    )

anMmeTrapAlarmSgsnGb1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136511587)
)
anMmeTrapAlarmSgsnGb1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmSgsnGb1399.setStatus(
        "current"
    )

anMmeTrapAlarmCsl1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136642561)
)
anMmeTrapAlarmCsl1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmCsl1300.setStatus(
        "current"
    )

anMmeTrapAlarmCsl1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136642562)
)
anMmeTrapAlarmCsl1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmCsl1301.setStatus(
        "current"
    )

anMmeTrapAlarmCsl1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136642563)
)
anMmeTrapAlarmCsl1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmCsl1302.setStatus(
        "current"
    )

anMmeTrapAlarmCsl1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136642564)
)
anMmeTrapAlarmCsl1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmCsl1303.setStatus(
        "current"
    )

anMmeTrapAlarmCsl1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136642565)
)
anMmeTrapAlarmCsl1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmCsl1304.setStatus(
        "current"
    )

anMmeTrapAlarmCsl1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 136642659)
)
anMmeTrapAlarmCsl1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmCsl1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSbc1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137232385)
)
anMmeTrapAlarmMmeSbc1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSbc1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSbc1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137232386)
)
anMmeTrapAlarmMmeSbc1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSbc1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSbc1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137232483)
)
anMmeTrapAlarmMmeSbc1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSbc1399.setStatus(
        "current"
    )

anMmeTrapAlarmDns1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137297921)
)
anMmeTrapAlarmDns1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmDns1300.setStatus(
        "current"
    )

anMmeTrapAlarmDns1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137297922)
)
anMmeTrapAlarmDns1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmDns1301.setStatus(
        "current"
    )

anMmeTrapAlarmDns1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137297923)
)
anMmeTrapAlarmDns1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmDns1302.setStatus(
        "current"
    )

anMmeTrapAlarmDns1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137298019)
)
anMmeTrapAlarmDns1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmDns1399.setStatus(
        "current"
    )

anMmeTrapAlarmTrace1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137494529)
)
anMmeTrapAlarmTrace1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmTrace1300.setStatus(
        "current"
    )

anMmeTrapAlarmTrace1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 137494627)
)
anMmeTrapAlarmTrace1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmTrace1399.setStatus(
        "current"
    )

anMmeTrapAlarmOverload1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138412033)
)
anMmeTrapAlarmOverload1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmOverload1300.setStatus(
        "current"
    )

anMmeTrapAlarmOverload1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138412034)
)
anMmeTrapAlarmOverload1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmOverload1301.setStatus(
        "current"
    )

anMmeTrapAlarmOverload1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138412131)
)
anMmeTrapAlarmOverload1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmOverload1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSgs1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138477569)
)
anMmeTrapAlarmMmeSgs1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSgs1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSgs1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138477570)
)
anMmeTrapAlarmMmeSgs1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSgs1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSgs1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138477667)
)
anMmeTrapAlarmMmeSgs1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSgs1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeAtam1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138739713)
)
anMmeTrapAlarmMmeAtam1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeAtam1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeAtam1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 138739811)
)
anMmeTrapAlarmMmeAtam1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeAtam1399.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Mme1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 140771329)
)
anMmeTrapAlarmFgwS1Mme1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Mme1300.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Mme1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 140771330)
)
anMmeTrapAlarmFgwS1Mme1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Mme1301.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Mme1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 140771427)
)
anMmeTrapAlarmFgwS1Mme1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Mme1399.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344193)
)
anMmeTrapAlarmFgwSc1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1300.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344194)
)
anMmeTrapAlarmFgwSc1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1301.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344195)
)
anMmeTrapAlarmFgwSc1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1302.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344196)
)
anMmeTrapAlarmFgwSc1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1303.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344197)
)
anMmeTrapAlarmFgwSc1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1304.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344198)
)
anMmeTrapAlarmFgwSc1305.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1305.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344199)
)
anMmeTrapAlarmFgwSc1306.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1306.setStatus(
        "current"
    )

anMmeTrapAlarmFgwSc1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142344291)
)
anMmeTrapAlarmFgwSc1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwSc1399.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Enb1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142409729)
)
anMmeTrapAlarmFgwS1Enb1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Enb1301.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Enb1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142409827)
)
anMmeTrapAlarmFgwS1Enb1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Enb1399.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Server1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142475265)
)
anMmeTrapAlarmFgwS1Server1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Server1300.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Server1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142475266)
)
anMmeTrapAlarmFgwS1Server1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Server1301.setStatus(
        "current"
    )

anMmeTrapAlarmFgwS1Server1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 142475363)
)
anMmeTrapAlarmFgwS1Server1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmFgwS1Server1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSls1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143392769)
)
anMmeTrapAlarmMmeSls1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSls1300.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSls1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143392770)
)
anMmeTrapAlarmMmeSls1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSls1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSls1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143392771)
)
anMmeTrapAlarmMmeSls1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSls1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeSls1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143392867)
)
anMmeTrapAlarmMmeSls1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeSls1399.setStatus(
        "current"
    )

anMmeTrapAlarmPathMon1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143917057)
)
anMmeTrapAlarmPathMon1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmPathMon1300.setStatus(
        "current"
    )

anMmeTrapAlarmPathMon1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143917058)
)
anMmeTrapAlarmPathMon1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmPathMon1301.setStatus(
        "current"
    )

anMmeTrapAlarmPathMon1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143917059)
)
anMmeTrapAlarmPathMon1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmPathMon1302.setStatus(
        "current"
    )

anMmeTrapAlarmPathMon1303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143917060)
)
anMmeTrapAlarmPathMon1303.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmPathMon1303.setStatus(
        "current"
    )

anMmeTrapAlarmPathMon1304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143917061)
)
anMmeTrapAlarmPathMon1304.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmPathMon1304.setStatus(
        "current"
    )

anMmeTrapAlarmPathMon1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 143917155)
)
anMmeTrapAlarmPathMon1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmPathMon1399.setStatus(
        "current"
    )

anMmeTrapAlarmLbCtrl1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 144113665)
)
anMmeTrapAlarmLbCtrl1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLbCtrl1300.setStatus(
        "current"
    )

anMmeTrapAlarmLbCtrl1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 144113763)
)
anMmeTrapAlarmLbCtrl1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmLbCtrl1399.setStatus(
        "current"
    )

anMmeTrapAlarmEdp1300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 144179201)
)
anMmeTrapAlarmEdp1300.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmEdp1300.setStatus(
        "current"
    )

anMmeTrapAlarmEdp1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 144179299)
)
anMmeTrapAlarmEdp1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmEdp1399.setStatus(
        "current"
    )

anMmeTrapAlarmMmeMbms1301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 196673537)
)
anMmeTrapAlarmMmeMbms1301.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeMbms1301.setStatus(
        "current"
    )

anMmeTrapAlarmMmeMbms1302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 196673538)
)
anMmeTrapAlarmMmeMbms1302.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeMbms1302.setStatus(
        "current"
    )

anMmeTrapAlarmMmeMbms1399 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 1, 196673635)
)
anMmeTrapAlarmMmeMbms1399.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeFirstEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLastEvent"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmIndex"))
)
if mibBuilder.loadTexts:
    anMmeTrapAlarmMmeMbms1399.setStatus(
        "current"
    )

anMmeTrapEventNm1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 65536100)
)
anMmeTrapEventNm1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventNm1400.setStatus(
        "current"
    )

anMmeTrapEventNm1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 65536101)
)
anMmeTrapEventNm1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventNm1401.setStatus(
        "current"
    )

anMmeTrapEventLi1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133759076)
)
anMmeTrapEventLi1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLi1400.setStatus(
        "current"
    )

anMmeTrapEventLi1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133759077)
)
anMmeTrapEventLi1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLi1401.setStatus(
        "current"
    )

anMmeTrapEventLi1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133759078)
)
anMmeTrapEventLi1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLi1402.setStatus(
        "current"
    )

anMmeTrapEventMmeRm1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133824612)
)
anMmeTrapEventMmeRm1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeRm1400.setStatus(
        "current"
    )

anMmeTrapEventMmeRm1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133824613)
)
anMmeTrapEventMmeRm1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeRm1401.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890148)
)
anMmeTrapEventMmeS1M1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1400.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890149)
)
anMmeTrapEventMmeS1M1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1401.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890150)
)
anMmeTrapEventMmeS1M1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1402.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890151)
)
anMmeTrapEventMmeS1M1403.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1403.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1404 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890152)
)
anMmeTrapEventMmeS1M1404.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1404.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1405 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890153)
)
anMmeTrapEventMmeS1M1405.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1405.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1406 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890154)
)
anMmeTrapEventMmeS1M1406.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1406.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1407 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890155)
)
anMmeTrapEventMmeS1M1407.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1407.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1408 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890156)
)
anMmeTrapEventMmeS1M1408.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1408.setStatus(
        "current"
    )

anMmeTrapEventMmeS1M1409 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133890157)
)
anMmeTrapEventMmeS1M1409.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1M1409.setStatus(
        "current"
    )

anMmeTrapEventMmeUpsm1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 133955684)
)
anMmeTrapEventMmeUpsm1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeUpsm1400.setStatus(
        "current"
    )

anMmeTrapEventMmeIlf1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134021220)
)
anMmeTrapEventMmeIlf1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeIlf1400.setStatus(
        "current"
    )

anMmeTrapEventMmeIlf1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134021221)
)
anMmeTrapEventMmeIlf1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeIlf1401.setStatus(
        "current"
    )

anMmeTrapEventMmeS1Enb1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134152292)
)
anMmeTrapEventMmeS1Enb1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1Enb1400.setStatus(
        "current"
    )

anMmeTrapEventMmeS1Enb1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134152293)
)
anMmeTrapEventMmeS1Enb1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeS1Enb1401.setStatus(
        "current"
    )

anMmeTrapEventMmeDc1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134217828)
)
anMmeTrapEventMmeDc1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeDc1400.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283364)
)
anMmeTrapEventMmeSc1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1400.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283365)
)
anMmeTrapEventMmeSc1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1401.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283366)
)
anMmeTrapEventMmeSc1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1402.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283367)
)
anMmeTrapEventMmeSc1403.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1403.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1404 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283368)
)
anMmeTrapEventMmeSc1404.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1404.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1405 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283369)
)
anMmeTrapEventMmeSc1405.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1405.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1406 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283370)
)
anMmeTrapEventMmeSc1406.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1406.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1407 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283371)
)
anMmeTrapEventMmeSc1407.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1407.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1408 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283372)
)
anMmeTrapEventMmeSc1408.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1408.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1409 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283373)
)
anMmeTrapEventMmeSc1409.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1409.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1410 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283374)
)
anMmeTrapEventMmeSc1410.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1410.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1411 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283375)
)
anMmeTrapEventMmeSc1411.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1411.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1412 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283376)
)
anMmeTrapEventMmeSc1412.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1412.setStatus(
        "current"
    )

anMmeTrapEventMmeSc1413 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134283377)
)
anMmeTrapEventMmeSc1413.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSc1413.setStatus(
        "current"
    )

anMmeTrapEventMmeUpm1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 134545508)
)
anMmeTrapEventMmeUpm1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeUpm1400.setStatus(
        "current"
    )

anMmeTrapEventMmeSigtran1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 135594085)
)
anMmeTrapEventMmeSigtran1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSigtran1400.setStatus(
        "current"
    )

anMmeTrapEventMmeSigtran1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 135594086)
)
anMmeTrapEventMmeSigtran1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSigtran1401.setStatus(
        "current"
    )

anMmeTrapEventMmeTcap1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 135659621)
)
anMmeTrapEventMmeTcap1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeTcap1400.setStatus(
        "current"
    )

anMmeTrapEventSgsnIu1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136314980)
)
anMmeTrapEventSgsnIu1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnIu1400.setStatus(
        "current"
    )

anMmeTrapEventSgsnIu1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136314981)
)
anMmeTrapEventSgsnIu1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnIu1401.setStatus(
        "current"
    )

anMmeTrapEventSgsnIpSp1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136380516)
)
anMmeTrapEventSgsnIpSp1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnIpSp1400.setStatus(
        "current"
    )

anMmeTrapEventSgsnIpSp1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136380517)
)
anMmeTrapEventSgsnIpSp1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnIpSp1401.setStatus(
        "current"
    )

anMmeTrapEventSgsnSd1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136446052)
)
anMmeTrapEventSgsnSd1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnSd1400.setStatus(
        "current"
    )

anMmeTrapEventSgsnSd1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136446053)
)
anMmeTrapEventSgsnSd1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnSd1401.setStatus(
        "current"
    )

anMmeTrapEventSgsnSd1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136446054)
)
anMmeTrapEventSgsnSd1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnSd1402.setStatus(
        "current"
    )

anMmeTrapEventSgsnSd1403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136446055)
)
anMmeTrapEventSgsnSd1403.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnSd1403.setStatus(
        "current"
    )

anMmeTrapEventSgsnSd1404 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136446056)
)
anMmeTrapEventSgsnSd1404.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnSd1404.setStatus(
        "current"
    )

anMmeTrapEventSgsnGb1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136511588)
)
anMmeTrapEventSgsnGb1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnGb1400.setStatus(
        "current"
    )

anMmeTrapEventSgsnGb1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136511589)
)
anMmeTrapEventSgsnGb1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnGb1401.setStatus(
        "current"
    )

anMmeTrapEventSgsnGb1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136511590)
)
anMmeTrapEventSgsnGb1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnGb1402.setStatus(
        "current"
    )

anMmeTrapEventSgsnGb1403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136511591)
)
anMmeTrapEventSgsnGb1403.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnGb1403.setStatus(
        "current"
    )

anMmeTrapEventSgsnGb1404 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136511592)
)
anMmeTrapEventSgsnGb1404.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnGb1404.setStatus(
        "current"
    )

anMmeTrapEventSgsnGb1405 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 136511593)
)
anMmeTrapEventSgsnGb1405.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventSgsnGb1405.setStatus(
        "current"
    )

anMmeTrapEventMmeSbc1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 137232485)
)
anMmeTrapEventMmeSbc1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSbc1401.setStatus(
        "current"
    )

anMmeTrapEventMmeSbc1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 137232486)
)
anMmeTrapEventMmeSbc1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSbc1402.setStatus(
        "current"
    )

anMmeTrapEventTrace1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 137494628)
)
anMmeTrapEventTrace1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventTrace1400.setStatus(
        "current"
    )

anMmeTrapEventTrace1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 137494629)
)
anMmeTrapEventTrace1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventTrace1401.setStatus(
        "current"
    )

anMmeTrapEventTrace1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 137494630)
)
anMmeTrapEventTrace1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventTrace1402.setStatus(
        "current"
    )

anMmeTrapEventMmeSgs1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 138477668)
)
anMmeTrapEventMmeSgs1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSgs1400.setStatus(
        "current"
    )

anMmeTrapEventMmeSgs1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 138477669)
)
anMmeTrapEventMmeSgs1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeSgs1401.setStatus(
        "current"
    )

anMmeTrapEventMME1600 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 140640356)
)
anMmeTrapEventMME1600.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMME1600.setStatus(
        "current"
    )

anMmeTrapEventMME1601 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 140640357)
)
anMmeTrapEventMME1601.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMME1601.setStatus(
        "current"
    )

anMmeTrapEventMME1602 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 140640358)
)
anMmeTrapEventMME1602.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMME1602.setStatus(
        "current"
    )

anMmeTrapEventMME1603 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 140640359)
)
anMmeTrapEventMME1603.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMME1603.setStatus(
        "current"
    )

anMmeTrapEventMME1604 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 140640360)
)
anMmeTrapEventMME1604.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMME1604.setStatus(
        "current"
    )

anMmeTrapEventFgwSc1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 142344292)
)
anMmeTrapEventFgwSc1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventFgwSc1400.setStatus(
        "current"
    )

anMmeTrapEventFgwSc1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 142344293)
)
anMmeTrapEventFgwSc1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventFgwSc1401.setStatus(
        "current"
    )

anMmeTrapEventFgwSc1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 142344294)
)
anMmeTrapEventFgwSc1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventFgwSc1402.setStatus(
        "current"
    )

anMmeTrapEventFgwSc1403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 142344295)
)
anMmeTrapEventFgwSc1403.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventFgwSc1403.setStatus(
        "current"
    )

anMmeTrapEventFgwSc1404 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 142344296)
)
anMmeTrapEventFgwSc1404.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventFgwSc1404.setStatus(
        "current"
    )

anMmeTrapEventLbCtrl1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 144113764)
)
anMmeTrapEventLbCtrl1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLbCtrl1400.setStatus(
        "current"
    )

anMmeTrapEventLbCtrl1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 144113765)
)
anMmeTrapEventLbCtrl1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLbCtrl1401.setStatus(
        "current"
    )

anMmeTrapEventLbCtrl1402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 144113766)
)
anMmeTrapEventLbCtrl1402.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLbCtrl1402.setStatus(
        "current"
    )

anMmeTrapEventLbCtrl1403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 144113767)
)
anMmeTrapEventLbCtrl1403.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventLbCtrl1403.setStatus(
        "current"
    )

anMmeTrapEventEdp1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 144179300)
)
anMmeTrapEventEdp1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventEdp1400.setStatus(
        "current"
    )

anMmeTrapEventMmeMbms1400 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 196673636)
)
anMmeTrapEventMmeMbms1400.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeMbms1400.setStatus(
        "current"
    )

anMmeTrapEventMmeMbms1401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 6, 2, 196673637)
)
anMmeTrapEventMmeMbms1401.setObjects(
      *(("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmState"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmSeverity"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeEntityTag"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSubentityInfo"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocationGateway"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeReason"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeAlarmDateAndTime"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeGroupKey"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeSequenceNumber"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeLocation"),
        ("AFFIRMED-MME-TRAPS-MIB", "anMmeService"))
)
if mibBuilder.loadTexts:
    anMmeTrapEventMmeMbms1401.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AFFIRMED-MME-TRAPS-MIB",
    **{"affirmedSnmpMmeTraps": affirmedSnmpMmeTraps,
       "anMmeTrapAlarms": anMmeTrapAlarms,
       "anMmeTrapAlarmNm1300": anMmeTrapAlarmNm1300,
       "anMmeTrapAlarmNm1301": anMmeTrapAlarmNm1301,
       "anMmeTrapAlarmNm1302": anMmeTrapAlarmNm1302,
       "anMmeTrapAlarmNm1399": anMmeTrapAlarmNm1399,
       "anMmeTrapAlarmResmon1301": anMmeTrapAlarmResmon1301,
       "anMmeTrapAlarmResmon1399": anMmeTrapAlarmResmon1399,
       "anMmeTrapAlarmGaBilling1300": anMmeTrapAlarmGaBilling1300,
       "anMmeTrapAlarmGaBilling1301": anMmeTrapAlarmGaBilling1301,
       "anMmeTrapAlarmGaBilling1399": anMmeTrapAlarmGaBilling1399,
       "anMmeTrapAlarmLi1300": anMmeTrapAlarmLi1300,
       "anMmeTrapAlarmLi1301": anMmeTrapAlarmLi1301,
       "anMmeTrapAlarmLi1302": anMmeTrapAlarmLi1302,
       "anMmeTrapAlarmLi1303": anMmeTrapAlarmLi1303,
       "anMmeTrapAlarmLi1304": anMmeTrapAlarmLi1304,
       "anMmeTrapAlarmLi1305": anMmeTrapAlarmLi1305,
       "anMmeTrapAlarmLi1306": anMmeTrapAlarmLi1306,
       "anMmeTrapAlarmLi1307": anMmeTrapAlarmLi1307,
       "anMmeTrapAlarmLi1308": anMmeTrapAlarmLi1308,
       "anMmeTrapAlarmLi1309": anMmeTrapAlarmLi1309,
       "anMmeTrapAlarmLi1310": anMmeTrapAlarmLi1310,
       "anMmeTrapAlarmLi1399": anMmeTrapAlarmLi1399,
       "anMmeTrapAlarmMmeRm1301": anMmeTrapAlarmMmeRm1301,
       "anMmeTrapAlarmMmeRm1302": anMmeTrapAlarmMmeRm1302,
       "anMmeTrapAlarmMmeRm1303": anMmeTrapAlarmMmeRm1303,
       "anMmeTrapAlarmMmeRm1304": anMmeTrapAlarmMmeRm1304,
       "anMmeTrapAlarmMmeRm1399": anMmeTrapAlarmMmeRm1399,
       "anMmeTrapAlarmMmeS1M1302": anMmeTrapAlarmMmeS1M1302,
       "anMmeTrapAlarmMmeS1M1303": anMmeTrapAlarmMmeS1M1303,
       "anMmeTrapAlarmMmeS1M1304": anMmeTrapAlarmMmeS1M1304,
       "anMmeTrapAlarmMmeS1M1305": anMmeTrapAlarmMmeS1M1305,
       "anMmeTrapAlarmMmeS1M1306": anMmeTrapAlarmMmeS1M1306,
       "anMmeTrapAlarmMmeS1M1307": anMmeTrapAlarmMmeS1M1307,
       "anMmeTrapAlarmMmeS1M1308": anMmeTrapAlarmMmeS1M1308,
       "anMmeTrapAlarmMmeS1M1309": anMmeTrapAlarmMmeS1M1309,
       "anMmeTrapAlarmMmeS1M1310": anMmeTrapAlarmMmeS1M1310,
       "anMmeTrapAlarmMmeS1M1311": anMmeTrapAlarmMmeS1M1311,
       "anMmeTrapAlarmMmeS1M1399": anMmeTrapAlarmMmeS1M1399,
       "anMmeTrapAlarmMmeUpsm1300": anMmeTrapAlarmMmeUpsm1300,
       "anMmeTrapAlarmMmeUpsm1302": anMmeTrapAlarmMmeUpsm1302,
       "anMmeTrapAlarmMmeUpsm1303": anMmeTrapAlarmMmeUpsm1303,
       "anMmeTrapAlarmMmeUpsm1304": anMmeTrapAlarmMmeUpsm1304,
       "anMmeTrapAlarmMmeUpsm1305": anMmeTrapAlarmMmeUpsm1305,
       "anMmeTrapAlarmMmeUpsm1306": anMmeTrapAlarmMmeUpsm1306,
       "anMmeTrapAlarmMmeUpsm1307": anMmeTrapAlarmMmeUpsm1307,
       "anMmeTrapAlarmMmeUpsm1308": anMmeTrapAlarmMmeUpsm1308,
       "anMmeTrapAlarmMmeUpsm1309": anMmeTrapAlarmMmeUpsm1309,
       "anMmeTrapAlarmMmeUpsm1310": anMmeTrapAlarmMmeUpsm1310,
       "anMmeTrapAlarmMmeUpsm1399": anMmeTrapAlarmMmeUpsm1399,
       "anMmeTrapAlarmMmeIlf1300": anMmeTrapAlarmMmeIlf1300,
       "anMmeTrapAlarmMmeIlf1301": anMmeTrapAlarmMmeIlf1301,
       "anMmeTrapAlarmMmeIlf1399": anMmeTrapAlarmMmeIlf1399,
       "anMmeTrapAlarmMmeS1Server1300": anMmeTrapAlarmMmeS1Server1300,
       "anMmeTrapAlarmMmeS1Server1301": anMmeTrapAlarmMmeS1Server1301,
       "anMmeTrapAlarmMmeS1Server1399": anMmeTrapAlarmMmeS1Server1399,
       "anMmeTrapAlarmMmeS1Enb1301": anMmeTrapAlarmMmeS1Enb1301,
       "anMmeTrapAlarmMmeS1Enb1399": anMmeTrapAlarmMmeS1Enb1399,
       "anMmeTrapAlarmMmeDc1300": anMmeTrapAlarmMmeDc1300,
       "anMmeTrapAlarmMmeDc1301": anMmeTrapAlarmMmeDc1301,
       "anMmeTrapAlarmMmeDc1302": anMmeTrapAlarmMmeDc1302,
       "anMmeTrapAlarmMmeDc1303": anMmeTrapAlarmMmeDc1303,
       "anMmeTrapAlarmMmeDc1304": anMmeTrapAlarmMmeDc1304,
       "anMmeTrapAlarmMmeDc1305": anMmeTrapAlarmMmeDc1305,
       "anMmeTrapAlarmMmeDc1306": anMmeTrapAlarmMmeDc1306,
       "anMmeTrapAlarmMmeDc1307": anMmeTrapAlarmMmeDc1307,
       "anMmeTrapAlarmMmeDc1399": anMmeTrapAlarmMmeDc1399,
       "anMmeTrapAlarmMmeSc1301": anMmeTrapAlarmMmeSc1301,
       "anMmeTrapAlarmMmeSc1302": anMmeTrapAlarmMmeSc1302,
       "anMmeTrapAlarmMmeSc1303": anMmeTrapAlarmMmeSc1303,
       "anMmeTrapAlarmMmeSc1304": anMmeTrapAlarmMmeSc1304,
       "anMmeTrapAlarmMmeSc1305": anMmeTrapAlarmMmeSc1305,
       "anMmeTrapAlarmMmeSc1310": anMmeTrapAlarmMmeSc1310,
       "anMmeTrapAlarmMmeSc1311": anMmeTrapAlarmMmeSc1311,
       "anMmeTrapAlarmMmeSc1306": anMmeTrapAlarmMmeSc1306,
       "anMmeTrapAlarmMmeSc1307": anMmeTrapAlarmMmeSc1307,
       "anMmeTrapAlarmMmeSc1308": anMmeTrapAlarmMmeSc1308,
       "anMmeTrapAlarmMmeSc1309": anMmeTrapAlarmMmeSc1309,
       "anMmeTrapAlarmMmeSc1320": anMmeTrapAlarmMmeSc1320,
       "anMmeTrapAlarmMmeSc1312": anMmeTrapAlarmMmeSc1312,
       "anMmeTrapAlarmMmeSc1313": anMmeTrapAlarmMmeSc1313,
       "anMmeTrapAlarmMmeSc1314": anMmeTrapAlarmMmeSc1314,
       "anMmeTrapAlarmMmeSc1315": anMmeTrapAlarmMmeSc1315,
       "anMmeTrapAlarmMmeSc1316": anMmeTrapAlarmMmeSc1316,
       "anMmeTrapAlarmMmeSc1317": anMmeTrapAlarmMmeSc1317,
       "anMmeTrapAlarmMmeSc1318": anMmeTrapAlarmMmeSc1318,
       "anMmeTrapAlarmMmeSc1321": anMmeTrapAlarmMmeSc1321,
       "anMmeTrapAlarmMmeSc1322": anMmeTrapAlarmMmeSc1322,
       "anMmeTrapAlarmMmeSc1323": anMmeTrapAlarmMmeSc1323,
       "anMmeTrapAlarmMmeSc1324": anMmeTrapAlarmMmeSc1324,
       "anMmeTrapAlarmMmeSc1325": anMmeTrapAlarmMmeSc1325,
       "anMmeTrapAlarmMmeSc1399": anMmeTrapAlarmMmeSc1399,
       "anMmeTrapAlarmMmeUpm1303": anMmeTrapAlarmMmeUpm1303,
       "anMmeTrapAlarmMmeUpm1301": anMmeTrapAlarmMmeUpm1301,
       "anMmeTrapAlarmMmeUpm1304": anMmeTrapAlarmMmeUpm1304,
       "anMmeTrapAlarmMmeUpm1302": anMmeTrapAlarmMmeUpm1302,
       "anMmeTrapAlarmMmeUpm1305": anMmeTrapAlarmMmeUpm1305,
       "anMmeTrapAlarmMmeUpm1399": anMmeTrapAlarmMmeUpm1399,
       "anMmeTrapAlarmMmeSigtran1300": anMmeTrapAlarmMmeSigtran1300,
       "anMmeTrapAlarmMmeSigtran1301": anMmeTrapAlarmMmeSigtran1301,
       "anMmeTrapAlarmMmeSigtran1302": anMmeTrapAlarmMmeSigtran1302,
       "anMmeTrapAlarmMmeSigtran1303": anMmeTrapAlarmMmeSigtran1303,
       "anMmeTrapAlarmMmeSigtran1304": anMmeTrapAlarmMmeSigtran1304,
       "anMmeTrapAlarmMmeSigtran1305": anMmeTrapAlarmMmeSigtran1305,
       "anMmeTrapAlarmMmeSigtran1306": anMmeTrapAlarmMmeSigtran1306,
       "anMmeTrapAlarmMmeSigtran1307": anMmeTrapAlarmMmeSigtran1307,
       "anMmeTrapAlarmMmeSigtran1308": anMmeTrapAlarmMmeSigtran1308,
       "anMmeTrapAlarmMmeSigtran1399": anMmeTrapAlarmMmeSigtran1399,
       "anMmeTrapAlarmMmeTcap1303": anMmeTrapAlarmMmeTcap1303,
       "anMmeTrapAlarmMmeTcap1304": anMmeTrapAlarmMmeTcap1304,
       "anMmeTrapAlarmMmeTcap1305": anMmeTrapAlarmMmeTcap1305,
       "anMmeTrapAlarmMmeTcap1306": anMmeTrapAlarmMmeTcap1306,
       "anMmeTrapAlarmMmeTcap1399": anMmeTrapAlarmMmeTcap1399,
       "anMmeTrapAlarmSgsnIu1300": anMmeTrapAlarmSgsnIu1300,
       "anMmeTrapAlarmSgsnIu1301": anMmeTrapAlarmSgsnIu1301,
       "anMmeTrapAlarmSgsnIu1303": anMmeTrapAlarmSgsnIu1303,
       "anMmeTrapAlarmSgsnIu1304": anMmeTrapAlarmSgsnIu1304,
       "anMmeTrapAlarmSgsnIu1399": anMmeTrapAlarmSgsnIu1399,
       "anMmeTrapAlarmSgsnIpSp1300": anMmeTrapAlarmSgsnIpSp1300,
       "anMmeTrapAlarmSgsnIpSp1301": anMmeTrapAlarmSgsnIpSp1301,
       "anMmeTrapAlarmSgsnIpSp1302": anMmeTrapAlarmSgsnIpSp1302,
       "anMmeTrapAlarmSgsnIpSp1303": anMmeTrapAlarmSgsnIpSp1303,
       "anMmeTrapAlarmSgsnIpSp1304": anMmeTrapAlarmSgsnIpSp1304,
       "anMmeTrapAlarmSgsnIpSp1399": anMmeTrapAlarmSgsnIpSp1399,
       "anMmeTrapAlarmSgsnSd1300": anMmeTrapAlarmSgsnSd1300,
       "anMmeTrapAlarmSgsnSd1301": anMmeTrapAlarmSgsnSd1301,
       "anMmeTrapAlarmSgsnSd1302": anMmeTrapAlarmSgsnSd1302,
       "anMmeTrapAlarmSgsnSd1399": anMmeTrapAlarmSgsnSd1399,
       "anMmeTrapAlarmSgsnGb1300": anMmeTrapAlarmSgsnGb1300,
       "anMmeTrapAlarmSgsnGb1301": anMmeTrapAlarmSgsnGb1301,
       "anMmeTrapAlarmSgsnGb1302": anMmeTrapAlarmSgsnGb1302,
       "anMmeTrapAlarmSgsnGb1303": anMmeTrapAlarmSgsnGb1303,
       "anMmeTrapAlarmSgsnGb1304": anMmeTrapAlarmSgsnGb1304,
       "anMmeTrapAlarmSgsnGb1305": anMmeTrapAlarmSgsnGb1305,
       "anMmeTrapAlarmSgsnGb1306": anMmeTrapAlarmSgsnGb1306,
       "anMmeTrapAlarmSgsnGb1399": anMmeTrapAlarmSgsnGb1399,
       "anMmeTrapAlarmCsl1300": anMmeTrapAlarmCsl1300,
       "anMmeTrapAlarmCsl1301": anMmeTrapAlarmCsl1301,
       "anMmeTrapAlarmCsl1302": anMmeTrapAlarmCsl1302,
       "anMmeTrapAlarmCsl1303": anMmeTrapAlarmCsl1303,
       "anMmeTrapAlarmCsl1304": anMmeTrapAlarmCsl1304,
       "anMmeTrapAlarmCsl1399": anMmeTrapAlarmCsl1399,
       "anMmeTrapAlarmMmeSbc1300": anMmeTrapAlarmMmeSbc1300,
       "anMmeTrapAlarmMmeSbc1301": anMmeTrapAlarmMmeSbc1301,
       "anMmeTrapAlarmMmeSbc1399": anMmeTrapAlarmMmeSbc1399,
       "anMmeTrapAlarmDns1300": anMmeTrapAlarmDns1300,
       "anMmeTrapAlarmDns1301": anMmeTrapAlarmDns1301,
       "anMmeTrapAlarmDns1302": anMmeTrapAlarmDns1302,
       "anMmeTrapAlarmDns1399": anMmeTrapAlarmDns1399,
       "anMmeTrapAlarmTrace1300": anMmeTrapAlarmTrace1300,
       "anMmeTrapAlarmTrace1399": anMmeTrapAlarmTrace1399,
       "anMmeTrapAlarmOverload1300": anMmeTrapAlarmOverload1300,
       "anMmeTrapAlarmOverload1301": anMmeTrapAlarmOverload1301,
       "anMmeTrapAlarmOverload1399": anMmeTrapAlarmOverload1399,
       "anMmeTrapAlarmMmeSgs1300": anMmeTrapAlarmMmeSgs1300,
       "anMmeTrapAlarmMmeSgs1301": anMmeTrapAlarmMmeSgs1301,
       "anMmeTrapAlarmMmeSgs1399": anMmeTrapAlarmMmeSgs1399,
       "anMmeTrapAlarmMmeAtam1300": anMmeTrapAlarmMmeAtam1300,
       "anMmeTrapAlarmMmeAtam1399": anMmeTrapAlarmMmeAtam1399,
       "anMmeTrapAlarmFgwS1Mme1300": anMmeTrapAlarmFgwS1Mme1300,
       "anMmeTrapAlarmFgwS1Mme1301": anMmeTrapAlarmFgwS1Mme1301,
       "anMmeTrapAlarmFgwS1Mme1399": anMmeTrapAlarmFgwS1Mme1399,
       "anMmeTrapAlarmFgwSc1300": anMmeTrapAlarmFgwSc1300,
       "anMmeTrapAlarmFgwSc1301": anMmeTrapAlarmFgwSc1301,
       "anMmeTrapAlarmFgwSc1302": anMmeTrapAlarmFgwSc1302,
       "anMmeTrapAlarmFgwSc1303": anMmeTrapAlarmFgwSc1303,
       "anMmeTrapAlarmFgwSc1304": anMmeTrapAlarmFgwSc1304,
       "anMmeTrapAlarmFgwSc1305": anMmeTrapAlarmFgwSc1305,
       "anMmeTrapAlarmFgwSc1306": anMmeTrapAlarmFgwSc1306,
       "anMmeTrapAlarmFgwSc1399": anMmeTrapAlarmFgwSc1399,
       "anMmeTrapAlarmFgwS1Enb1301": anMmeTrapAlarmFgwS1Enb1301,
       "anMmeTrapAlarmFgwS1Enb1399": anMmeTrapAlarmFgwS1Enb1399,
       "anMmeTrapAlarmFgwS1Server1300": anMmeTrapAlarmFgwS1Server1300,
       "anMmeTrapAlarmFgwS1Server1301": anMmeTrapAlarmFgwS1Server1301,
       "anMmeTrapAlarmFgwS1Server1399": anMmeTrapAlarmFgwS1Server1399,
       "anMmeTrapAlarmMmeSls1300": anMmeTrapAlarmMmeSls1300,
       "anMmeTrapAlarmMmeSls1301": anMmeTrapAlarmMmeSls1301,
       "anMmeTrapAlarmMmeSls1302": anMmeTrapAlarmMmeSls1302,
       "anMmeTrapAlarmMmeSls1399": anMmeTrapAlarmMmeSls1399,
       "anMmeTrapAlarmPathMon1300": anMmeTrapAlarmPathMon1300,
       "anMmeTrapAlarmPathMon1301": anMmeTrapAlarmPathMon1301,
       "anMmeTrapAlarmPathMon1302": anMmeTrapAlarmPathMon1302,
       "anMmeTrapAlarmPathMon1303": anMmeTrapAlarmPathMon1303,
       "anMmeTrapAlarmPathMon1304": anMmeTrapAlarmPathMon1304,
       "anMmeTrapAlarmPathMon1399": anMmeTrapAlarmPathMon1399,
       "anMmeTrapAlarmLbCtrl1300": anMmeTrapAlarmLbCtrl1300,
       "anMmeTrapAlarmLbCtrl1399": anMmeTrapAlarmLbCtrl1399,
       "anMmeTrapAlarmEdp1300": anMmeTrapAlarmEdp1300,
       "anMmeTrapAlarmEdp1399": anMmeTrapAlarmEdp1399,
       "anMmeTrapAlarmMmeMbms1301": anMmeTrapAlarmMmeMbms1301,
       "anMmeTrapAlarmMmeMbms1302": anMmeTrapAlarmMmeMbms1302,
       "anMmeTrapAlarmMmeMbms1399": anMmeTrapAlarmMmeMbms1399,
       "anMmeTrapEvents": anMmeTrapEvents,
       "anMmeTrapEventNm1400": anMmeTrapEventNm1400,
       "anMmeTrapEventNm1401": anMmeTrapEventNm1401,
       "anMmeTrapEventLi1400": anMmeTrapEventLi1400,
       "anMmeTrapEventLi1401": anMmeTrapEventLi1401,
       "anMmeTrapEventLi1402": anMmeTrapEventLi1402,
       "anMmeTrapEventMmeRm1400": anMmeTrapEventMmeRm1400,
       "anMmeTrapEventMmeRm1401": anMmeTrapEventMmeRm1401,
       "anMmeTrapEventMmeS1M1400": anMmeTrapEventMmeS1M1400,
       "anMmeTrapEventMmeS1M1401": anMmeTrapEventMmeS1M1401,
       "anMmeTrapEventMmeS1M1402": anMmeTrapEventMmeS1M1402,
       "anMmeTrapEventMmeS1M1403": anMmeTrapEventMmeS1M1403,
       "anMmeTrapEventMmeS1M1404": anMmeTrapEventMmeS1M1404,
       "anMmeTrapEventMmeS1M1405": anMmeTrapEventMmeS1M1405,
       "anMmeTrapEventMmeS1M1406": anMmeTrapEventMmeS1M1406,
       "anMmeTrapEventMmeS1M1407": anMmeTrapEventMmeS1M1407,
       "anMmeTrapEventMmeS1M1408": anMmeTrapEventMmeS1M1408,
       "anMmeTrapEventMmeS1M1409": anMmeTrapEventMmeS1M1409,
       "anMmeTrapEventMmeUpsm1400": anMmeTrapEventMmeUpsm1400,
       "anMmeTrapEventMmeIlf1400": anMmeTrapEventMmeIlf1400,
       "anMmeTrapEventMmeIlf1401": anMmeTrapEventMmeIlf1401,
       "anMmeTrapEventMmeS1Enb1400": anMmeTrapEventMmeS1Enb1400,
       "anMmeTrapEventMmeS1Enb1401": anMmeTrapEventMmeS1Enb1401,
       "anMmeTrapEventMmeDc1400": anMmeTrapEventMmeDc1400,
       "anMmeTrapEventMmeSc1400": anMmeTrapEventMmeSc1400,
       "anMmeTrapEventMmeSc1401": anMmeTrapEventMmeSc1401,
       "anMmeTrapEventMmeSc1402": anMmeTrapEventMmeSc1402,
       "anMmeTrapEventMmeSc1403": anMmeTrapEventMmeSc1403,
       "anMmeTrapEventMmeSc1404": anMmeTrapEventMmeSc1404,
       "anMmeTrapEventMmeSc1405": anMmeTrapEventMmeSc1405,
       "anMmeTrapEventMmeSc1406": anMmeTrapEventMmeSc1406,
       "anMmeTrapEventMmeSc1407": anMmeTrapEventMmeSc1407,
       "anMmeTrapEventMmeSc1408": anMmeTrapEventMmeSc1408,
       "anMmeTrapEventMmeSc1409": anMmeTrapEventMmeSc1409,
       "anMmeTrapEventMmeSc1410": anMmeTrapEventMmeSc1410,
       "anMmeTrapEventMmeSc1411": anMmeTrapEventMmeSc1411,
       "anMmeTrapEventMmeSc1412": anMmeTrapEventMmeSc1412,
       "anMmeTrapEventMmeSc1413": anMmeTrapEventMmeSc1413,
       "anMmeTrapEventMmeUpm1400": anMmeTrapEventMmeUpm1400,
       "anMmeTrapEventMmeSigtran1400": anMmeTrapEventMmeSigtran1400,
       "anMmeTrapEventMmeSigtran1401": anMmeTrapEventMmeSigtran1401,
       "anMmeTrapEventMmeTcap1400": anMmeTrapEventMmeTcap1400,
       "anMmeTrapEventSgsnIu1400": anMmeTrapEventSgsnIu1400,
       "anMmeTrapEventSgsnIu1401": anMmeTrapEventSgsnIu1401,
       "anMmeTrapEventSgsnIpSp1400": anMmeTrapEventSgsnIpSp1400,
       "anMmeTrapEventSgsnIpSp1401": anMmeTrapEventSgsnIpSp1401,
       "anMmeTrapEventSgsnSd1400": anMmeTrapEventSgsnSd1400,
       "anMmeTrapEventSgsnSd1401": anMmeTrapEventSgsnSd1401,
       "anMmeTrapEventSgsnSd1402": anMmeTrapEventSgsnSd1402,
       "anMmeTrapEventSgsnSd1403": anMmeTrapEventSgsnSd1403,
       "anMmeTrapEventSgsnSd1404": anMmeTrapEventSgsnSd1404,
       "anMmeTrapEventSgsnGb1400": anMmeTrapEventSgsnGb1400,
       "anMmeTrapEventSgsnGb1401": anMmeTrapEventSgsnGb1401,
       "anMmeTrapEventSgsnGb1402": anMmeTrapEventSgsnGb1402,
       "anMmeTrapEventSgsnGb1403": anMmeTrapEventSgsnGb1403,
       "anMmeTrapEventSgsnGb1404": anMmeTrapEventSgsnGb1404,
       "anMmeTrapEventSgsnGb1405": anMmeTrapEventSgsnGb1405,
       "anMmeTrapEventMmeSbc1401": anMmeTrapEventMmeSbc1401,
       "anMmeTrapEventMmeSbc1402": anMmeTrapEventMmeSbc1402,
       "anMmeTrapEventTrace1400": anMmeTrapEventTrace1400,
       "anMmeTrapEventTrace1401": anMmeTrapEventTrace1401,
       "anMmeTrapEventTrace1402": anMmeTrapEventTrace1402,
       "anMmeTrapEventMmeSgs1400": anMmeTrapEventMmeSgs1400,
       "anMmeTrapEventMmeSgs1401": anMmeTrapEventMmeSgs1401,
       "anMmeTrapEventMME1600": anMmeTrapEventMME1600,
       "anMmeTrapEventMME1601": anMmeTrapEventMME1601,
       "anMmeTrapEventMME1602": anMmeTrapEventMME1602,
       "anMmeTrapEventMME1603": anMmeTrapEventMME1603,
       "anMmeTrapEventMME1604": anMmeTrapEventMME1604,
       "anMmeTrapEventFgwSc1400": anMmeTrapEventFgwSc1400,
       "anMmeTrapEventFgwSc1401": anMmeTrapEventFgwSc1401,
       "anMmeTrapEventFgwSc1402": anMmeTrapEventFgwSc1402,
       "anMmeTrapEventFgwSc1403": anMmeTrapEventFgwSc1403,
       "anMmeTrapEventFgwSc1404": anMmeTrapEventFgwSc1404,
       "anMmeTrapEventLbCtrl1400": anMmeTrapEventLbCtrl1400,
       "anMmeTrapEventLbCtrl1401": anMmeTrapEventLbCtrl1401,
       "anMmeTrapEventLbCtrl1402": anMmeTrapEventLbCtrl1402,
       "anMmeTrapEventLbCtrl1403": anMmeTrapEventLbCtrl1403,
       "anMmeTrapEventEdp1400": anMmeTrapEventEdp1400,
       "anMmeTrapEventMmeMbms1400": anMmeTrapEventMmeMbms1400,
       "anMmeTrapEventMmeMbms1401": anMmeTrapEventMmeMbms1401,
       "anMmeNotificationVars": anMmeNotificationVars,
       "anMmeAlarmState": anMmeAlarmState,
       "anMmeAlarmSeverity": anMmeAlarmSeverity,
       "anMmeEntityTag": anMmeEntityTag,
       "anMmeSubentityInfo": anMmeSubentityInfo,
       "anMmeLocationGateway": anMmeLocationGateway,
       "anMmeReason": anMmeReason,
       "anMmeAlarmDateAndTime": anMmeAlarmDateAndTime,
       "anMmeGroupKey": anMmeGroupKey,
       "anMmeSequenceNumber": anMmeSequenceNumber,
       "anMmeFirstEvent": anMmeFirstEvent,
       "anMmeLastEvent": anMmeLastEvent,
       "anMmeLocation": anMmeLocation,
       "anMmeService": anMmeService,
       "anMmeAlarmIndex": anMmeAlarmIndex}
)
