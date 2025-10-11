# SNMP MIB module (NEWTEC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:56 2025
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

(ntcEvent,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcEvent")

(NtcAlarmState,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcNotification = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ntcNotification.setRevisions(
        ("2012-06-28 12:00",
         "2012-05-16 12:35")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcNotifObjects_ObjectIdentity = ObjectIdentity
ntcNotifObjects = _NtcNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ntcNotifObjects.setStatus("current")
_NtcNotifReportList_ObjectIdentity = ObjectIdentity
ntcNotifReportList = _NtcNotifReportList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 0)
)
if mibBuilder.loadTexts:
    ntcNotifReportList.setStatus("current")
_NtcNotifField_ObjectIdentity = ObjectIdentity
ntcNotifField = _NtcNotifField_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntcNotifField.setStatus("current")
_NtcNotifFldSeqNbr_Type = Counter32
_NtcNotifFldSeqNbr_Object = MibScalar
ntcNotifFldSeqNbr = _NtcNotifFldSeqNbr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 1),
    _NtcNotifFldSeqNbr_Type()
)
ntcNotifFldSeqNbr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldSeqNbr.setStatus("current")
_NtcNotifFldSeverity_Type = DisplayString
_NtcNotifFldSeverity_Object = MibScalar
ntcNotifFldSeverity = _NtcNotifFldSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 2),
    _NtcNotifFldSeverity_Type()
)
ntcNotifFldSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldSeverity.setStatus("current")
_NtcNotifFldDevice_Type = DisplayString
_NtcNotifFldDevice_Object = MibScalar
ntcNotifFldDevice = _NtcNotifFldDevice_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 3),
    _NtcNotifFldDevice_Type()
)
ntcNotifFldDevice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldDevice.setStatus("current")
_NtcNotifFldFunctionName_Type = DisplayString
_NtcNotifFldFunctionName_Object = MibScalar
ntcNotifFldFunctionName = _NtcNotifFldFunctionName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 4),
    _NtcNotifFldFunctionName_Type()
)
ntcNotifFldFunctionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldFunctionName.setStatus("current")
_NtcNotifFldFunctionId_Type = ObjectIdentifier
_NtcNotifFldFunctionId_Object = MibScalar
ntcNotifFldFunctionId = _NtcNotifFldFunctionId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 5),
    _NtcNotifFldFunctionId_Type()
)
ntcNotifFldFunctionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldFunctionId.setStatus("current")
_NtcNotifFldObjectName_Type = DisplayString
_NtcNotifFldObjectName_Object = MibScalar
ntcNotifFldObjectName = _NtcNotifFldObjectName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 6),
    _NtcNotifFldObjectName_Type()
)
ntcNotifFldObjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldObjectName.setStatus("current")
_NtcNotifFldObjectId_Type = ObjectIdentifier
_NtcNotifFldObjectId_Object = MibScalar
ntcNotifFldObjectId = _NtcNotifFldObjectId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 7),
    _NtcNotifFldObjectId_Type()
)
ntcNotifFldObjectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldObjectId.setStatus("current")
_NtcNotifFldDescription_Type = DisplayString
_NtcNotifFldDescription_Object = MibScalar
ntcNotifFldDescription = _NtcNotifFldDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 8),
    _NtcNotifFldDescription_Type()
)
ntcNotifFldDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldDescription.setStatus("current")
_NtcNotifFldAlarmStatus_Type = NtcAlarmState
_NtcNotifFldAlarmStatus_Object = MibScalar
ntcNotifFldAlarmStatus = _NtcNotifFldAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 1, 9),
    _NtcNotifFldAlarmStatus_Type()
)
ntcNotifFldAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntcNotifFldAlarmStatus.setStatus("current")
_NtcNotifConformance_ObjectIdentity = ObjectIdentity
ntcNotifConformance = _NtcNotifConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ntcNotifConformance.setStatus("current")
_NtcNotifConfGroup_ObjectIdentity = ObjectIdentity
ntcNotifConfGroup = _NtcNotifConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ntcNotifConfGroup.setStatus("current")
_NtcNotifConfCompliance_ObjectIdentity = ObjectIdentity
ntcNotifConfCompliance = _NtcNotifConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ntcNotifConfCompliance.setStatus("current")

# Managed Objects groups

ntcNotifConfGrpFldV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 2, 1, 1)
)
ntcNotifConfGrpFldV1Standard.setObjects(
      *(("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldSeqNbr"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldSeverity"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldDevice"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldFunctionName"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldFunctionId"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldObjectName"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldObjectId"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldDescription"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldAlarmStatus"))
)
if mibBuilder.loadTexts:
    ntcNotifConfGrpFldV1Standard.setStatus("current")


# Notification objects

ntcNotifAlReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 1, 0, 1)
)
ntcNotifAlReport.setObjects(
      *(("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldSeqNbr"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldSeverity"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldDevice"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldFunctionName"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldFunctionId"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldObjectName"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldObjectId"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldDescription"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifFldAlarmStatus"))
)
if mibBuilder.loadTexts:
    ntcNotifAlReport.setStatus(
        "current"
    )


# Notifications groups

ntcNotifConfGrpRepV1Standard = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 2, 1, 2)
)
ntcNotifConfGrpRepV1Standard.setObjects(
    ("NEWTEC-NOTIFICATION-MIB", "ntcNotifAlReport")
)
if mibBuilder.loadTexts:
    ntcNotifConfGrpRepV1Standard.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ntcNotifConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3, 2, 2, 2, 1)
)
ntcNotifConfCompV1Standard.setObjects(
      *(("NEWTEC-NOTIFICATION-MIB", "ntcNotifConfGrpFldV1Standard"),
        ("NEWTEC-NOTIFICATION-MIB", "ntcNotifConfGrpRepV1Standard"))
)
if mibBuilder.loadTexts:
    ntcNotifConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-NOTIFICATION-MIB",
    **{"ntcNotification": ntcNotification,
       "ntcNotifObjects": ntcNotifObjects,
       "ntcNotifReportList": ntcNotifReportList,
       "ntcNotifAlReport": ntcNotifAlReport,
       "ntcNotifField": ntcNotifField,
       "ntcNotifFldSeqNbr": ntcNotifFldSeqNbr,
       "ntcNotifFldSeverity": ntcNotifFldSeverity,
       "ntcNotifFldDevice": ntcNotifFldDevice,
       "ntcNotifFldFunctionName": ntcNotifFldFunctionName,
       "ntcNotifFldFunctionId": ntcNotifFldFunctionId,
       "ntcNotifFldObjectName": ntcNotifFldObjectName,
       "ntcNotifFldObjectId": ntcNotifFldObjectId,
       "ntcNotifFldDescription": ntcNotifFldDescription,
       "ntcNotifFldAlarmStatus": ntcNotifFldAlarmStatus,
       "ntcNotifConformance": ntcNotifConformance,
       "ntcNotifConfGroup": ntcNotifConfGroup,
       "ntcNotifConfGrpFldV1Standard": ntcNotifConfGrpFldV1Standard,
       "ntcNotifConfGrpRepV1Standard": ntcNotifConfGrpRepV1Standard,
       "ntcNotifConfCompliance": ntcNotifConfCompliance,
       "ntcNotifConfCompV1Standard": ntcNotifConfCompV1Standard}
)
