# SNMP MIB module (LUM-LINKLOSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-LINKLOSS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:37 2025
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

(lumLinkLossMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumLinkLossMIB",
    "lumModules")

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

lumLinkLossMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 45)
)
if mibBuilder.loadTexts:
    lumLinkLossMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2012-03-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumLinkLossConfs_ObjectIdentity = ObjectIdentity
lumLinkLossConfs = _LumLinkLossConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 1)
)
_LumLinkLossGroups_ObjectIdentity = ObjectIdentity
lumLinkLossGroups = _LumLinkLossGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 1, 1)
)
_LumLinkLossCompl_ObjectIdentity = ObjectIdentity
lumLinkLossCompl = _LumLinkLossCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 1, 2)
)
_LumLinkLossMIBObjects_ObjectIdentity = ObjectIdentity
lumLinkLossMIBObjects = _LumLinkLossMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2)
)
_LinkLossGeneral_ObjectIdentity = ObjectIdentity
linkLossGeneral = _LinkLossGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 1)
)
_LinkLossGeneralConfigLastChangeTime_Type = DateAndTime
_LinkLossGeneralConfigLastChangeTime_Object = MibScalar
linkLossGeneralConfigLastChangeTime = _LinkLossGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 1, 1),
    _LinkLossGeneralConfigLastChangeTime_Type()
)
linkLossGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossGeneralConfigLastChangeTime.setStatus("current")
_LinkLossGeneralStateLastChangeTime_Type = DateAndTime
_LinkLossGeneralStateLastChangeTime_Object = MibScalar
linkLossGeneralStateLastChangeTime = _LinkLossGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 1, 2),
    _LinkLossGeneralStateLastChangeTime_Type()
)
linkLossGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossGeneralStateLastChangeTime.setStatus("current")
_LinkLossGeneralStatusTableSize_Type = Unsigned32
_LinkLossGeneralStatusTableSize_Object = MibScalar
linkLossGeneralStatusTableSize = _LinkLossGeneralStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 1, 3),
    _LinkLossGeneralStatusTableSize_Type()
)
linkLossGeneralStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossGeneralStatusTableSize.setStatus("current")
_LinkLossStatusList_ObjectIdentity = ObjectIdentity
linkLossStatusList = _LinkLossStatusList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2)
)
_LinkLossStatusTable_Object = MibTable
linkLossStatusTable = _LinkLossStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1)
)
if mibBuilder.loadTexts:
    linkLossStatusTable.setStatus("current")
_LinkLossStatusEntry_Object = MibTableRow
linkLossStatusEntry = _LinkLossStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1, 1)
)
linkLossStatusEntry.setIndexNames(
    (0, "LUM-LINKLOSS-MIB", "linkLossStatusIndex"),
)
if mibBuilder.loadTexts:
    linkLossStatusEntry.setStatus("current")


class _LinkLossStatusIndex_Type(Unsigned32):
    """Custom type linkLossStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LinkLossStatusIndex_Type.__name__ = "Unsigned32"
_LinkLossStatusIndex_Object = MibTableColumn
linkLossStatusIndex = _LinkLossStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1, 1, 1),
    _LinkLossStatusIndex_Type()
)
linkLossStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossStatusIndex.setStatus("current")
_LinkLossStatusThresholdExceeded_Type = FaultStatus
_LinkLossStatusThresholdExceeded_Object = MibTableColumn
linkLossStatusThresholdExceeded = _LinkLossStatusThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1, 1, 2),
    _LinkLossStatusThresholdExceeded_Type()
)
linkLossStatusThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossStatusThresholdExceeded.setStatus("current")
_LinkLossStatusMeasurementFailed_Type = FaultStatus
_LinkLossStatusMeasurementFailed_Object = MibTableColumn
linkLossStatusMeasurementFailed = _LinkLossStatusMeasurementFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1, 1, 3),
    _LinkLossStatusMeasurementFailed_Type()
)
linkLossStatusMeasurementFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossStatusMeasurementFailed.setStatus("current")
_LinkLossStatusMeasurementFailedOneDb_Type = FaultStatus
_LinkLossStatusMeasurementFailedOneDb_Object = MibTableColumn
linkLossStatusMeasurementFailedOneDb = _LinkLossStatusMeasurementFailedOneDb_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1, 1, 4),
    _LinkLossStatusMeasurementFailedOneDb_Type()
)
linkLossStatusMeasurementFailedOneDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossStatusMeasurementFailedOneDb.setStatus("current")
_LinkLossStatusMeasurementFailedFiveSec_Type = FaultStatus
_LinkLossStatusMeasurementFailedFiveSec_Object = MibTableColumn
linkLossStatusMeasurementFailedFiveSec = _LinkLossStatusMeasurementFailedFiveSec_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 2, 2, 1, 1, 5),
    _LinkLossStatusMeasurementFailedFiveSec_Type()
)
linkLossStatusMeasurementFailedFiveSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossStatusMeasurementFailedFiveSec.setStatus("current")

# Managed Objects groups

linkLossGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 1, 1, 1)
)
linkLossGeneralGroup.setObjects(
      *(("LUM-LINKLOSS-MIB", "linkLossGeneralConfigLastChangeTime"),
        ("LUM-LINKLOSS-MIB", "linkLossGeneralStateLastChangeTime"),
        ("LUM-LINKLOSS-MIB", "linkLossGeneralStatusTableSize"))
)
if mibBuilder.loadTexts:
    linkLossGeneralGroup.setStatus("current")

linkLossStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 1, 1, 2)
)
linkLossStatusGroup.setObjects(
      *(("LUM-LINKLOSS-MIB", "linkLossStatusIndex"),
        ("LUM-LINKLOSS-MIB", "linkLossStatusThresholdExceeded"),
        ("LUM-LINKLOSS-MIB", "linkLossStatusMeasurementFailed"),
        ("LUM-LINKLOSS-MIB", "linkLossStatusMeasurementFailedOneDb"),
        ("LUM-LINKLOSS-MIB", "linkLossStatusMeasurementFailedFiveSec"))
)
if mibBuilder.loadTexts:
    linkLossStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumLinkLossBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45, 1, 2, 1)
)
lumLinkLossBasicComplV1.setObjects(
      *(("LUM-LINKLOSS-MIB", "linkLossGeneralGroup"),
        ("LUM-LINKLOSS-MIB", "linkLossStatusGroup"))
)
if mibBuilder.loadTexts:
    lumLinkLossBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-LINKLOSS-MIB",
    **{"lumLinkLossMIBModule": lumLinkLossMIBModule,
       "lumLinkLossConfs": lumLinkLossConfs,
       "lumLinkLossGroups": lumLinkLossGroups,
       "linkLossGeneralGroup": linkLossGeneralGroup,
       "linkLossStatusGroup": linkLossStatusGroup,
       "lumLinkLossCompl": lumLinkLossCompl,
       "lumLinkLossBasicComplV1": lumLinkLossBasicComplV1,
       "lumLinkLossMIBObjects": lumLinkLossMIBObjects,
       "linkLossGeneral": linkLossGeneral,
       "linkLossGeneralConfigLastChangeTime": linkLossGeneralConfigLastChangeTime,
       "linkLossGeneralStateLastChangeTime": linkLossGeneralStateLastChangeTime,
       "linkLossGeneralStatusTableSize": linkLossGeneralStatusTableSize,
       "linkLossStatusList": linkLossStatusList,
       "linkLossStatusTable": linkLossStatusTable,
       "linkLossStatusEntry": linkLossStatusEntry,
       "linkLossStatusIndex": linkLossStatusIndex,
       "linkLossStatusThresholdExceeded": linkLossStatusThresholdExceeded,
       "linkLossStatusMeasurementFailed": linkLossStatusMeasurementFailed,
       "linkLossStatusMeasurementFailedOneDb": linkLossStatusMeasurementFailedOneDb,
       "linkLossStatusMeasurementFailedFiveSec": linkLossStatusMeasurementFailedFiveSec}
)
