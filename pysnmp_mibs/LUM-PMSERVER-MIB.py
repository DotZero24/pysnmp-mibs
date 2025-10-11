# SNMP MIB module (LUM-PMSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-PMSERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:17 2025
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

(lumModules,
 lumPmServerMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumPmServerMIB")

(FaultStatus,) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatus")

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

lumPmServerMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 49)
)
if mibBuilder.loadTexts:
    lumPmServerMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2012-07-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumPmServerConfs_ObjectIdentity = ObjectIdentity
lumPmServerConfs = _LumPmServerConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 1)
)
_LumPmServerGroups_ObjectIdentity = ObjectIdentity
lumPmServerGroups = _LumPmServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 1)
)
_LumPmServerCompl_ObjectIdentity = ObjectIdentity
lumPmServerCompl = _LumPmServerCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 2)
)
_LumPmServerMIBObjects_ObjectIdentity = ObjectIdentity
lumPmServerMIBObjects = _LumPmServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2)
)
_PmServerGeneral_ObjectIdentity = ObjectIdentity
pmServerGeneral = _PmServerGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1)
)
_PmServerGeneralConfigLastChangeTime_Type = DateAndTime
_PmServerGeneralConfigLastChangeTime_Object = MibScalar
pmServerGeneralConfigLastChangeTime = _PmServerGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1, 1),
    _PmServerGeneralConfigLastChangeTime_Type()
)
pmServerGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmServerGeneralConfigLastChangeTime.setStatus("current")
_PmServerGeneralStateLastChangeTime_Type = DateAndTime
_PmServerGeneralStateLastChangeTime_Object = MibScalar
pmServerGeneralStateLastChangeTime = _PmServerGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1, 2),
    _PmServerGeneralStateLastChangeTime_Type()
)
pmServerGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmServerGeneralStateLastChangeTime.setStatus("current")
_PmServerGeneralStatusTableSize_Type = Unsigned32
_PmServerGeneralStatusTableSize_Object = MibScalar
pmServerGeneralStatusTableSize = _PmServerGeneralStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1, 3),
    _PmServerGeneralStatusTableSize_Type()
)
pmServerGeneralStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmServerGeneralStatusTableSize.setStatus("current")
_PmServerStatusList_ObjectIdentity = ObjectIdentity
pmServerStatusList = _PmServerStatusList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2)
)
_PmServerStatusTable_Object = MibTable
pmServerStatusTable = _PmServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pmServerStatusTable.setStatus("current")
_PmServerStatusEntry_Object = MibTableRow
pmServerStatusEntry = _PmServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1, 1)
)
pmServerStatusEntry.setIndexNames(
    (0, "LUM-PMSERVER-MIB", "pmServerStatusIndex"),
)
if mibBuilder.loadTexts:
    pmServerStatusEntry.setStatus("current")


class _PmServerStatusIndex_Type(Unsigned32):
    """Custom type pmServerStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmServerStatusIndex_Type.__name__ = "Unsigned32"
_PmServerStatusIndex_Object = MibTableColumn
pmServerStatusIndex = _PmServerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1, 1, 1),
    _PmServerStatusIndex_Type()
)
pmServerStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmServerStatusIndex.setStatus("current")
_PmServerStatusFaultyEduReportFilesExist_Type = FaultStatus
_PmServerStatusFaultyEduReportFilesExist_Object = MibTableColumn
pmServerStatusFaultyEduReportFilesExist = _PmServerStatusFaultyEduReportFilesExist_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1, 1, 2),
    _PmServerStatusFaultyEduReportFilesExist_Type()
)
pmServerStatusFaultyEduReportFilesExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmServerStatusFaultyEduReportFilesExist.setStatus("current")

# Managed Objects groups

pmServerGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 1, 1)
)
pmServerGeneralGroup.setObjects(
      *(("LUM-PMSERVER-MIB", "pmServerGeneralConfigLastChangeTime"),
        ("LUM-PMSERVER-MIB", "pmServerGeneralStateLastChangeTime"),
        ("LUM-PMSERVER-MIB", "pmServerGeneralStatusTableSize"))
)
if mibBuilder.loadTexts:
    pmServerGeneralGroup.setStatus("current")

pmServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 1, 2)
)
pmServerStatusGroup.setObjects(
      *(("LUM-PMSERVER-MIB", "pmServerStatusIndex"),
        ("LUM-PMSERVER-MIB", "pmServerStatusFaultyEduReportFilesExist"))
)
if mibBuilder.loadTexts:
    pmServerStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumPmServerBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 2, 1)
)
lumPmServerBasicComplV1.setObjects(
      *(("LUM-PMSERVER-MIB", "pmServerGeneralGroup"),
        ("LUM-PMSERVER-MIB", "pmServerStatusGroup"))
)
if mibBuilder.loadTexts:
    lumPmServerBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-PMSERVER-MIB",
    **{"lumPmServerMIBModule": lumPmServerMIBModule,
       "lumPmServerConfs": lumPmServerConfs,
       "lumPmServerGroups": lumPmServerGroups,
       "pmServerGeneralGroup": pmServerGeneralGroup,
       "pmServerStatusGroup": pmServerStatusGroup,
       "lumPmServerCompl": lumPmServerCompl,
       "lumPmServerBasicComplV1": lumPmServerBasicComplV1,
       "lumPmServerMIBObjects": lumPmServerMIBObjects,
       "pmServerGeneral": pmServerGeneral,
       "pmServerGeneralConfigLastChangeTime": pmServerGeneralConfigLastChangeTime,
       "pmServerGeneralStateLastChangeTime": pmServerGeneralStateLastChangeTime,
       "pmServerGeneralStatusTableSize": pmServerGeneralStatusTableSize,
       "pmServerStatusList": pmServerStatusList,
       "pmServerStatusTable": pmServerStatusTable,
       "pmServerStatusEntry": pmServerStatusEntry,
       "pmServerStatusIndex": pmServerStatusIndex,
       "pmServerStatusFaultyEduReportFilesExist": pmServerStatusFaultyEduReportFilesExist}
)
