# SNMP MIB module (AFFIRMED-TEMS-OBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsoft/AFFIRMED-TEMS-OBJECTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:39 2025
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

(affirmedSnmpObjects,) = mibBuilder.importSymbols(
    "AFFIRMED-TEMS-SNMP-MIB",
    "affirmedSnmpObjects")

(AlarmLevel,
 ResourceAdminStatus,
 ThresholdType) = mibBuilder.importSymbols(
    "AFFIRMED-TEMS-TC-MIB",
    "AlarmLevel",
    "ResourceAdminStatus",
    "ThresholdType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

affirmedTemsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1)
)
if mibBuilder.loadTexts:
    affirmedTemsObjects.setRevisions(
        ("2008-03-14 11:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TemsServerSystemGroup_ObjectIdentity = ObjectIdentity
temsServerSystemGroup = _TemsServerSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 1)
)
_TemsServerDetails_ObjectIdentity = ObjectIdentity
temsServerDetails = _TemsServerDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 1, 1)
)
_TemsServerId_Type = Unsigned32
_TemsServerId_Object = MibScalar
temsServerId = _TemsServerId_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 1, 1, 1),
    _TemsServerId_Type()
)
temsServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerId.setStatus("current")
_TemsServerName_Type = DisplayString
_TemsServerName_Object = MibScalar
temsServerName = _TemsServerName_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 1, 1, 2),
    _TemsServerName_Type()
)
temsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerName.setStatus("current")
_TemsServerRunningVersion_Type = DisplayString
_TemsServerRunningVersion_Object = MibScalar
temsServerRunningVersion = _TemsServerRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 1, 1, 3),
    _TemsServerRunningVersion_Type()
)
temsServerRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerRunningVersion.setStatus("current")
_TemsServerDeployedLocation_Type = DisplayString
_TemsServerDeployedLocation_Object = MibScalar
temsServerDeployedLocation = _TemsServerDeployedLocation_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 1, 1, 4),
    _TemsServerDeployedLocation_Type()
)
temsServerDeployedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerDeployedLocation.setStatus("current")
_TemsServerResourceGroup_ObjectIdentity = ObjectIdentity
temsServerResourceGroup = _TemsServerResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2)
)
_TemsServerResourceTypeTable_Object = MibTable
temsServerResourceTypeTable = _TemsServerResourceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    temsServerResourceTypeTable.setStatus("current")
_TemsServerResourceTypeEntry_Object = MibTableRow
temsServerResourceTypeEntry = _TemsServerResourceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 1, 1)
)
temsServerResourceTypeEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerResourceTypeIndex"),
)
if mibBuilder.loadTexts:
    temsServerResourceTypeEntry.setStatus("current")
_TemsServerResourceTypeIndex_Type = Unsigned32
_TemsServerResourceTypeIndex_Object = MibTableColumn
temsServerResourceTypeIndex = _TemsServerResourceTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 1, 1, 1),
    _TemsServerResourceTypeIndex_Type()
)
temsServerResourceTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temsServerResourceTypeIndex.setStatus("current")
_TemsServerResourceType_Type = DisplayString
_TemsServerResourceType_Object = MibTableColumn
temsServerResourceType = _TemsServerResourceType_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 1, 1, 2),
    _TemsServerResourceType_Type()
)
temsServerResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerResourceType.setStatus("current")
_TemsServerResourceTable_Object = MibTable
temsServerResourceTable = _TemsServerResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    temsServerResourceTable.setStatus("current")
_TemsServerResourceEntry_Object = MibTableRow
temsServerResourceEntry = _TemsServerResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2, 1)
)
temsServerResourceEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerResourceIndex"),
)
if mibBuilder.loadTexts:
    temsServerResourceEntry.setStatus("current")
_TemsServerResourceIndex_Type = Unsigned32
_TemsServerResourceIndex_Object = MibTableColumn
temsServerResourceIndex = _TemsServerResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2, 1, 1),
    _TemsServerResourceIndex_Type()
)
temsServerResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temsServerResourceIndex.setStatus("current")
_TemsServerResourceName_Type = DisplayString
_TemsServerResourceName_Object = MibTableColumn
temsServerResourceName = _TemsServerResourceName_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2, 1, 2),
    _TemsServerResourceName_Type()
)
temsServerResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerResourceName.setStatus("current")
_TemsServerResourceTypeId_Type = Unsigned32
_TemsServerResourceTypeId_Object = MibTableColumn
temsServerResourceTypeId = _TemsServerResourceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2, 1, 3),
    _TemsServerResourceTypeId_Type()
)
temsServerResourceTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerResourceTypeId.setStatus("current")
_TemsServerResourceIpAddress_Type = IpAddress
_TemsServerResourceIpAddress_Object = MibTableColumn
temsServerResourceIpAddress = _TemsServerResourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2, 1, 4),
    _TemsServerResourceIpAddress_Type()
)
temsServerResourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerResourceIpAddress.setStatus("current")
_TemsServerResourceAdminStatus_Type = ResourceAdminStatus
_TemsServerResourceAdminStatus_Object = MibTableColumn
temsServerResourceAdminStatus = _TemsServerResourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 2, 2, 1, 5),
    _TemsServerResourceAdminStatus_Type()
)
temsServerResourceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerResourceAdminStatus.setStatus("current")
_TemsServerAlarmGroup_ObjectIdentity = ObjectIdentity
temsServerAlarmGroup = _TemsServerAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3)
)
_TemsServerActiveAlarmTable_Object = MibTable
temsServerActiveAlarmTable = _TemsServerActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    temsServerActiveAlarmTable.setStatus("current")
_TemsServerActiveAlarmEntry_Object = MibTableRow
temsServerActiveAlarmEntry = _TemsServerActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1)
)
temsServerActiveAlarmEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerActiveAlarmIndex"),
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerResourceIndex"),
)
if mibBuilder.loadTexts:
    temsServerActiveAlarmEntry.setStatus("current")
_TemsServerActiveAlarmIndex_Type = Unsigned32
_TemsServerActiveAlarmIndex_Object = MibTableColumn
temsServerActiveAlarmIndex = _TemsServerActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 1),
    _TemsServerActiveAlarmIndex_Type()
)
temsServerActiveAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temsServerActiveAlarmIndex.setStatus("current")
_TemsServerActiveAlarmSource_Type = DisplayString
_TemsServerActiveAlarmSource_Object = MibTableColumn
temsServerActiveAlarmSource = _TemsServerActiveAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 2),
    _TemsServerActiveAlarmSource_Type()
)
temsServerActiveAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmSource.setStatus("current")
_TemsServerActiveAlarmCategory_Type = DisplayString
_TemsServerActiveAlarmCategory_Object = MibTableColumn
temsServerActiveAlarmCategory = _TemsServerActiveAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 3),
    _TemsServerActiveAlarmCategory_Type()
)
temsServerActiveAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmCategory.setStatus("current")
_TemsServerActiveAlarmSeverity_Type = AlarmLevel
_TemsServerActiveAlarmSeverity_Object = MibTableColumn
temsServerActiveAlarmSeverity = _TemsServerActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 4),
    _TemsServerActiveAlarmSeverity_Type()
)
temsServerActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmSeverity.setStatus("current")
_TemsServerActiveAlarmMessage_Type = DisplayString
_TemsServerActiveAlarmMessage_Object = MibTableColumn
temsServerActiveAlarmMessage = _TemsServerActiveAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 5),
    _TemsServerActiveAlarmMessage_Type()
)
temsServerActiveAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmMessage.setStatus("current")
_TemsServerActiveAlarmRemedy_Type = DisplayString
_TemsServerActiveAlarmRemedy_Object = MibTableColumn
temsServerActiveAlarmRemedy = _TemsServerActiveAlarmRemedy_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 6),
    _TemsServerActiveAlarmRemedy_Type()
)
temsServerActiveAlarmRemedy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmRemedy.setStatus("current")
_TemsServerActiveAlarmOwner_Type = DisplayString
_TemsServerActiveAlarmOwner_Object = MibTableColumn
temsServerActiveAlarmOwner = _TemsServerActiveAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 7),
    _TemsServerActiveAlarmOwner_Type()
)
temsServerActiveAlarmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmOwner.setStatus("current")
_TemsServerActiveAlarmCreatedTime_Type = DateAndTime
_TemsServerActiveAlarmCreatedTime_Object = MibTableColumn
temsServerActiveAlarmCreatedTime = _TemsServerActiveAlarmCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 8),
    _TemsServerActiveAlarmCreatedTime_Type()
)
temsServerActiveAlarmCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmCreatedTime.setStatus("current")
_TemsServerActiveAlarmUpdatedTime_Type = DateAndTime
_TemsServerActiveAlarmUpdatedTime_Object = MibTableColumn
temsServerActiveAlarmUpdatedTime = _TemsServerActiveAlarmUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 9),
    _TemsServerActiveAlarmUpdatedTime_Type()
)
temsServerActiveAlarmUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmUpdatedTime.setStatus("current")
_TemsServerActiveAlarmClearedTime_Type = DateAndTime
_TemsServerActiveAlarmClearedTime_Object = MibTableColumn
temsServerActiveAlarmClearedTime = _TemsServerActiveAlarmClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 10),
    _TemsServerActiveAlarmClearedTime_Type()
)
temsServerActiveAlarmClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmClearedTime.setStatus("current")
_TemsServerActiveAlarmAckStatus_Type = TruthValue
_TemsServerActiveAlarmAckStatus_Object = MibTableColumn
temsServerActiveAlarmAckStatus = _TemsServerActiveAlarmAckStatus_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 11),
    _TemsServerActiveAlarmAckStatus_Type()
)
temsServerActiveAlarmAckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmAckStatus.setStatus("current")
_TemsServerActiveAlarmAckTime_Type = DateAndTime
_TemsServerActiveAlarmAckTime_Object = MibTableColumn
temsServerActiveAlarmAckTime = _TemsServerActiveAlarmAckTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 12),
    _TemsServerActiveAlarmAckTime_Type()
)
temsServerActiveAlarmAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmAckTime.setStatus("current")
_TemsServerActiveAlarmAdditionalInfo_Type = DisplayString
_TemsServerActiveAlarmAdditionalInfo_Object = MibTableColumn
temsServerActiveAlarmAdditionalInfo = _TemsServerActiveAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 13),
    _TemsServerActiveAlarmAdditionalInfo_Type()
)
temsServerActiveAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmAdditionalInfo.setStatus("current")
_TemsServerActiveAlarmNEIndex_Type = Unsigned32
_TemsServerActiveAlarmNEIndex_Object = MibTableColumn
temsServerActiveAlarmNEIndex = _TemsServerActiveAlarmNEIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 14),
    _TemsServerActiveAlarmNEIndex_Type()
)
temsServerActiveAlarmNEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmNEIndex.setStatus("current")
_TemsServerActiveAlarmNESeqNumber_Type = Unsigned32
_TemsServerActiveAlarmNESeqNumber_Object = MibTableColumn
temsServerActiveAlarmNESeqNumber = _TemsServerActiveAlarmNESeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 15),
    _TemsServerActiveAlarmNESeqNumber_Type()
)
temsServerActiveAlarmNESeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmNESeqNumber.setStatus("current")
_TemsServerActiveAlarmTrapOid_Type = DisplayString
_TemsServerActiveAlarmTrapOid_Object = MibTableColumn
temsServerActiveAlarmTrapOid = _TemsServerActiveAlarmTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 3, 2, 1, 16),
    _TemsServerActiveAlarmTrapOid_Type()
)
temsServerActiveAlarmTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerActiveAlarmTrapOid.setStatus("current")
_TemsServerStatsGroup_ObjectIdentity = ObjectIdentity
temsServerStatsGroup = _TemsServerStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4)
)
_TemsServerPerfMetricsTable_Object = MibTable
temsServerPerfMetricsTable = _TemsServerPerfMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    temsServerPerfMetricsTable.setStatus("current")
_TemsServerPerfMetricsEntry_Object = MibTableRow
temsServerPerfMetricsEntry = _TemsServerPerfMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 1, 1)
)
temsServerPerfMetricsEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerPerfMetricsIndex"),
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerResourceTypeIndex"),
)
if mibBuilder.loadTexts:
    temsServerPerfMetricsEntry.setStatus("current")
_TemsServerPerfMetricsIndex_Type = Unsigned32
_TemsServerPerfMetricsIndex_Object = MibTableColumn
temsServerPerfMetricsIndex = _TemsServerPerfMetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 1, 1, 1),
    _TemsServerPerfMetricsIndex_Type()
)
temsServerPerfMetricsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temsServerPerfMetricsIndex.setStatus("current")
_TemsServerPerfMetric_Type = DisplayString
_TemsServerPerfMetric_Object = MibTableColumn
temsServerPerfMetric = _TemsServerPerfMetric_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 1, 1, 2),
    _TemsServerPerfMetric_Type()
)
temsServerPerfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerPerfMetric.setStatus("current")
_TemsServerPerfMetricPollingInterval_Type = Unsigned32
_TemsServerPerfMetricPollingInterval_Object = MibTableColumn
temsServerPerfMetricPollingInterval = _TemsServerPerfMetricPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 1, 1, 3),
    _TemsServerPerfMetricPollingInterval_Type()
)
temsServerPerfMetricPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerPerfMetricPollingInterval.setStatus("current")
_TemsServerPerfStatsTable_Object = MibTable
temsServerPerfStatsTable = _TemsServerPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    temsServerPerfStatsTable.setStatus("current")
_TemsServerPerfStatsEntry_Object = MibTableRow
temsServerPerfStatsEntry = _TemsServerPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 2, 1)
)
temsServerPerfStatsEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerPerfMetricsIndex"),
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerResourceIndex"),
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerPerfStatsIndex"),
)
if mibBuilder.loadTexts:
    temsServerPerfStatsEntry.setStatus("current")
_TemsServerPerfStatsIndex_Type = Unsigned32
_TemsServerPerfStatsIndex_Object = MibTableColumn
temsServerPerfStatsIndex = _TemsServerPerfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 2, 1, 1),
    _TemsServerPerfStatsIndex_Type()
)
temsServerPerfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temsServerPerfStatsIndex.setStatus("current")
_TemsServerPerfMetricCollectedTime_Type = DateAndTime
_TemsServerPerfMetricCollectedTime_Object = MibTableColumn
temsServerPerfMetricCollectedTime = _TemsServerPerfMetricCollectedTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 2, 1, 2),
    _TemsServerPerfMetricCollectedTime_Type()
)
temsServerPerfMetricCollectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerPerfMetricCollectedTime.setStatus("current")
_TemsServerPerfMetricCollectedValue_Type = Integer32
_TemsServerPerfMetricCollectedValue_Object = MibTableColumn
temsServerPerfMetricCollectedValue = _TemsServerPerfMetricCollectedValue_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 4, 2, 1, 3),
    _TemsServerPerfMetricCollectedValue_Type()
)
temsServerPerfMetricCollectedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temsServerPerfMetricCollectedValue.setStatus("current")
_TemsServerConfigGroup_ObjectIdentity = ObjectIdentity
temsServerConfigGroup = _TemsServerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5)
)
_TemsServerSnmpManagerTable_Object = MibTable
temsServerSnmpManagerTable = _TemsServerSnmpManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    temsServerSnmpManagerTable.setStatus("current")
_TemsServerSnmpManagerEntry_Object = MibTableRow
temsServerSnmpManagerEntry = _TemsServerSnmpManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1, 1)
)
temsServerSnmpManagerEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerSnmpManagerIndex"),
)
if mibBuilder.loadTexts:
    temsServerSnmpManagerEntry.setStatus("current")


class _TemsServerSnmpManagerIndex_Type(Unsigned32):
    """Custom type temsServerSnmpManagerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TemsServerSnmpManagerIndex_Type.__name__ = "Unsigned32"
_TemsServerSnmpManagerIndex_Object = MibTableColumn
temsServerSnmpManagerIndex = _TemsServerSnmpManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1, 1, 1),
    _TemsServerSnmpManagerIndex_Type()
)
temsServerSnmpManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temsServerSnmpManagerIndex.setStatus("current")
_TemsServerSnmpManagerIpAddress_Type = IpAddress
_TemsServerSnmpManagerIpAddress_Object = MibTableColumn
temsServerSnmpManagerIpAddress = _TemsServerSnmpManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1, 1, 2),
    _TemsServerSnmpManagerIpAddress_Type()
)
temsServerSnmpManagerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temsServerSnmpManagerIpAddress.setStatus("current")


class _TemsServerSnmpManagerTrapPort_Type(Unsigned32):
    """Custom type temsServerSnmpManagerTrapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65327),
    )


_TemsServerSnmpManagerTrapPort_Type.__name__ = "Unsigned32"
_TemsServerSnmpManagerTrapPort_Object = MibTableColumn
temsServerSnmpManagerTrapPort = _TemsServerSnmpManagerTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1, 1, 3),
    _TemsServerSnmpManagerTrapPort_Type()
)
temsServerSnmpManagerTrapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temsServerSnmpManagerTrapPort.setStatus("current")
_TemsServerSnmpManagerTrapCommunity_Type = DisplayString
_TemsServerSnmpManagerTrapCommunity_Object = MibTableColumn
temsServerSnmpManagerTrapCommunity = _TemsServerSnmpManagerTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1, 1, 4),
    _TemsServerSnmpManagerTrapCommunity_Type()
)
temsServerSnmpManagerTrapCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temsServerSnmpManagerTrapCommunity.setStatus("current")
_TemsServerSnmpManagerRowStatus_Type = RowStatus
_TemsServerSnmpManagerRowStatus_Object = MibTableColumn
temsServerSnmpManagerRowStatus = _TemsServerSnmpManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 1, 1, 5),
    _TemsServerSnmpManagerRowStatus_Type()
)
temsServerSnmpManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temsServerSnmpManagerRowStatus.setStatus("current")
_PerfMetricThresholdTable_Object = MibTable
perfMetricThresholdTable = _PerfMetricThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    perfMetricThresholdTable.setStatus("current")
_PerfMetricThresholdEntry_Object = MibTableRow
perfMetricThresholdEntry = _PerfMetricThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1)
)
perfMetricThresholdEntry.setIndexNames(
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "temsServerPerfMetricsIndex"),
    (0, "AFFIRMED-TEMS-OBJECTS-MIB", "perfMetricThresholdIndex"),
)
if mibBuilder.loadTexts:
    perfMetricThresholdEntry.setStatus("current")
_PerfMetricThresholdIndex_Type = Unsigned32
_PerfMetricThresholdIndex_Object = MibTableColumn
perfMetricThresholdIndex = _PerfMetricThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 1),
    _PerfMetricThresholdIndex_Type()
)
perfMetricThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfMetricThresholdIndex.setStatus("current")
_PerfMetricThresholdType_Type = ThresholdType
_PerfMetricThresholdType_Object = MibTableColumn
perfMetricThresholdType = _PerfMetricThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 2),
    _PerfMetricThresholdType_Type()
)
perfMetricThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricThresholdType.setStatus("current")
_PerfMetricCriticalThreshold_Type = Integer32
_PerfMetricCriticalThreshold_Object = MibTableColumn
perfMetricCriticalThreshold = _PerfMetricCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 3),
    _PerfMetricCriticalThreshold_Type()
)
perfMetricCriticalThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricCriticalThreshold.setStatus("current")
_PerfMetricMajorThreshold_Type = Integer32
_PerfMetricMajorThreshold_Object = MibTableColumn
perfMetricMajorThreshold = _PerfMetricMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 4),
    _PerfMetricMajorThreshold_Type()
)
perfMetricMajorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricMajorThreshold.setStatus("current")
_PerfMetricMinorThreshold_Type = Integer32
_PerfMetricMinorThreshold_Object = MibTableColumn
perfMetricMinorThreshold = _PerfMetricMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 5),
    _PerfMetricMinorThreshold_Type()
)
perfMetricMinorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricMinorThreshold.setStatus("current")
_PerfMetricCriticalRearm_Type = Integer32
_PerfMetricCriticalRearm_Object = MibTableColumn
perfMetricCriticalRearm = _PerfMetricCriticalRearm_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 6),
    _PerfMetricCriticalRearm_Type()
)
perfMetricCriticalRearm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricCriticalRearm.setStatus("current")
_PerfMetricMajorRearm_Type = Integer32
_PerfMetricMajorRearm_Object = MibTableColumn
perfMetricMajorRearm = _PerfMetricMajorRearm_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 7),
    _PerfMetricMajorRearm_Type()
)
perfMetricMajorRearm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricMajorRearm.setStatus("current")
_PerfMetricMinorRearm_Type = Integer32
_PerfMetricMinorRearm_Object = MibTableColumn
perfMetricMinorRearm = _PerfMetricMinorRearm_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 8),
    _PerfMetricMinorRearm_Type()
)
perfMetricMinorRearm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricMinorRearm.setStatus("current")
_PerfMetricClearThreshold_Type = Integer32
_PerfMetricClearThreshold_Object = MibTableColumn
perfMetricClearThreshold = _PerfMetricClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 9),
    _PerfMetricClearThreshold_Type()
)
perfMetricClearThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricClearThreshold.setStatus("current")
_PerfMetricThresholdRowStatus_Type = RowStatus
_PerfMetricThresholdRowStatus_Object = MibTableColumn
perfMetricThresholdRowStatus = _PerfMetricThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37963, 6, 2, 1, 5, 2, 1, 10),
    _PerfMetricThresholdRowStatus_Type()
)
perfMetricThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfMetricThresholdRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AFFIRMED-TEMS-OBJECTS-MIB",
    **{"affirmedTemsObjects": affirmedTemsObjects,
       "temsServerSystemGroup": temsServerSystemGroup,
       "temsServerDetails": temsServerDetails,
       "temsServerId": temsServerId,
       "temsServerName": temsServerName,
       "temsServerRunningVersion": temsServerRunningVersion,
       "temsServerDeployedLocation": temsServerDeployedLocation,
       "temsServerResourceGroup": temsServerResourceGroup,
       "temsServerResourceTypeTable": temsServerResourceTypeTable,
       "temsServerResourceTypeEntry": temsServerResourceTypeEntry,
       "temsServerResourceTypeIndex": temsServerResourceTypeIndex,
       "temsServerResourceType": temsServerResourceType,
       "temsServerResourceTable": temsServerResourceTable,
       "temsServerResourceEntry": temsServerResourceEntry,
       "temsServerResourceIndex": temsServerResourceIndex,
       "temsServerResourceName": temsServerResourceName,
       "temsServerResourceTypeId": temsServerResourceTypeId,
       "temsServerResourceIpAddress": temsServerResourceIpAddress,
       "temsServerResourceAdminStatus": temsServerResourceAdminStatus,
       "temsServerAlarmGroup": temsServerAlarmGroup,
       "temsServerActiveAlarmTable": temsServerActiveAlarmTable,
       "temsServerActiveAlarmEntry": temsServerActiveAlarmEntry,
       "temsServerActiveAlarmIndex": temsServerActiveAlarmIndex,
       "temsServerActiveAlarmSource": temsServerActiveAlarmSource,
       "temsServerActiveAlarmCategory": temsServerActiveAlarmCategory,
       "temsServerActiveAlarmSeverity": temsServerActiveAlarmSeverity,
       "temsServerActiveAlarmMessage": temsServerActiveAlarmMessage,
       "temsServerActiveAlarmRemedy": temsServerActiveAlarmRemedy,
       "temsServerActiveAlarmOwner": temsServerActiveAlarmOwner,
       "temsServerActiveAlarmCreatedTime": temsServerActiveAlarmCreatedTime,
       "temsServerActiveAlarmUpdatedTime": temsServerActiveAlarmUpdatedTime,
       "temsServerActiveAlarmClearedTime": temsServerActiveAlarmClearedTime,
       "temsServerActiveAlarmAckStatus": temsServerActiveAlarmAckStatus,
       "temsServerActiveAlarmAckTime": temsServerActiveAlarmAckTime,
       "temsServerActiveAlarmAdditionalInfo": temsServerActiveAlarmAdditionalInfo,
       "temsServerActiveAlarmNEIndex": temsServerActiveAlarmNEIndex,
       "temsServerActiveAlarmNESeqNumber": temsServerActiveAlarmNESeqNumber,
       "temsServerActiveAlarmTrapOid": temsServerActiveAlarmTrapOid,
       "temsServerStatsGroup": temsServerStatsGroup,
       "temsServerPerfMetricsTable": temsServerPerfMetricsTable,
       "temsServerPerfMetricsEntry": temsServerPerfMetricsEntry,
       "temsServerPerfMetricsIndex": temsServerPerfMetricsIndex,
       "temsServerPerfMetric": temsServerPerfMetric,
       "temsServerPerfMetricPollingInterval": temsServerPerfMetricPollingInterval,
       "temsServerPerfStatsTable": temsServerPerfStatsTable,
       "temsServerPerfStatsEntry": temsServerPerfStatsEntry,
       "temsServerPerfStatsIndex": temsServerPerfStatsIndex,
       "temsServerPerfMetricCollectedTime": temsServerPerfMetricCollectedTime,
       "temsServerPerfMetricCollectedValue": temsServerPerfMetricCollectedValue,
       "temsServerConfigGroup": temsServerConfigGroup,
       "temsServerSnmpManagerTable": temsServerSnmpManagerTable,
       "temsServerSnmpManagerEntry": temsServerSnmpManagerEntry,
       "temsServerSnmpManagerIndex": temsServerSnmpManagerIndex,
       "temsServerSnmpManagerIpAddress": temsServerSnmpManagerIpAddress,
       "temsServerSnmpManagerTrapPort": temsServerSnmpManagerTrapPort,
       "temsServerSnmpManagerTrapCommunity": temsServerSnmpManagerTrapCommunity,
       "temsServerSnmpManagerRowStatus": temsServerSnmpManagerRowStatus,
       "perfMetricThresholdTable": perfMetricThresholdTable,
       "perfMetricThresholdEntry": perfMetricThresholdEntry,
       "perfMetricThresholdIndex": perfMetricThresholdIndex,
       "perfMetricThresholdType": perfMetricThresholdType,
       "perfMetricCriticalThreshold": perfMetricCriticalThreshold,
       "perfMetricMajorThreshold": perfMetricMajorThreshold,
       "perfMetricMinorThreshold": perfMetricMinorThreshold,
       "perfMetricCriticalRearm": perfMetricCriticalRearm,
       "perfMetricMajorRearm": perfMetricMajorRearm,
       "perfMetricMinorRearm": perfMetricMinorRearm,
       "perfMetricClearThreshold": perfMetricClearThreshold,
       "perfMetricThresholdRowStatus": perfMetricThresholdRowStatus}
)
