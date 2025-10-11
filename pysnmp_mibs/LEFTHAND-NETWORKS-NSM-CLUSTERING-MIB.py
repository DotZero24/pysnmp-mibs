# SNMP MIB module (LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:53 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(lhnModules,
 lhnNsm) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    "lhnModules",
    "lhnNsm")

(lhnNsmClustering,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmClustering")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNsmClusteringModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12)
)
if mibBuilder.loadTexts:
    lhnNsmClusteringModule.setRevisions(
        ("2013-11-13 00:00",
         "2013-06-27 00:00",
         "2012-09-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClusPermissionBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("read", 0),
          ("write", 1),
          ("exclusive", 2))
    )


class ClusFeatureBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("multiNodeVirtualizationAndClustering", 0),
          ("managedSnapshot", 1),
          ("remoteCopy", 2),
          ("manualSnapshot", 3),
          ("multiSiteSan", 4))
    )


class ClusCreatorTypes(TextualConvention, Integer32):
    status = "current"
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
          ("manager", 1),
          ("gui", 2),
          ("script", 3),
          ("text", 4),
          ("api", 5),
          ("gateway", 6))
    )



class ClusReplicationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("faulty", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LhnNsmClusteringModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmClusteringModuleConformance = _LhnNsmClusteringModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12, 1)
)
_LhnNsmClusteringModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmClusteringModuleCompliances = _LhnNsmClusteringModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12, 1, 1)
)
_LhnNsmClusteringModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmClusteringModuleGroups = _LhnNsmClusteringModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12, 1, 2)
)
_ClusMgmtGroupName_Type = DisplayString
_ClusMgmtGroupName_Object = MibScalar
clusMgmtGroupName = _ClusMgmtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 1),
    _ClusMgmtGroupName_Type()
)
clusMgmtGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupName.setStatus("current")
_ClusMgmtGroupIsEnabled_Type = TruthValue
_ClusMgmtGroupIsEnabled_Object = MibScalar
clusMgmtGroupIsEnabled = _ClusMgmtGroupIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 2),
    _ClusMgmtGroupIsEnabled_Type()
)
clusMgmtGroupIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupIsEnabled.setStatus("current")
_ClusMgmtGroupQuorum_Type = Integer32
_ClusMgmtGroupQuorum_Object = MibScalar
clusMgmtGroupQuorum = _ClusMgmtGroupQuorum_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 3),
    _ClusMgmtGroupQuorum_Type()
)
clusMgmtGroupQuorum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupQuorum.setStatus("current")
_ClusMgmtGroupDescription_Type = DisplayString
_ClusMgmtGroupDescription_Object = MibScalar
clusMgmtGroupDescription = _ClusMgmtGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 4),
    _ClusMgmtGroupDescription_Type()
)
clusMgmtGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupDescription.setStatus("obsolete")
_ClusMgmtGroupActiveManagerCount_Type = Integer32
_ClusMgmtGroupActiveManagerCount_Object = MibScalar
clusMgmtGroupActiveManagerCount = _ClusMgmtGroupActiveManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 5),
    _ClusMgmtGroupActiveManagerCount_Type()
)
clusMgmtGroupActiveManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupActiveManagerCount.setStatus("current")
_ClusMgmtGroupManagerCount_Type = Integer32
_ClusMgmtGroupManagerCount_Object = MibScalar
clusMgmtGroupManagerCount = _ClusMgmtGroupManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 6),
    _ClusMgmtGroupManagerCount_Type()
)
clusMgmtGroupManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupManagerCount.setStatus("current")
_ClusMgmtGroupLicenseTimeRemaining_Type = DisplayString
_ClusMgmtGroupLicenseTimeRemaining_Object = MibScalar
clusMgmtGroupLicenseTimeRemaining = _ClusMgmtGroupLicenseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 43),
    _ClusMgmtGroupLicenseTimeRemaining_Type()
)
clusMgmtGroupLicenseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupLicenseTimeRemaining.setStatus("current")
_ClusManagerTable_Object = MibTable
clusManagerTable = _ClusManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44)
)
if mibBuilder.loadTexts:
    clusManagerTable.setStatus("current")
_ClusManagerEntry_Object = MibTableRow
clusManagerEntry = _ClusManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1)
)
clusManagerEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerIndex"),
)
if mibBuilder.loadTexts:
    clusManagerEntry.setStatus("current")
_ClusManagerIndex_Type = Unsigned32
_ClusManagerIndex_Object = MibTableColumn
clusManagerIndex = _ClusManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 1),
    _ClusManagerIndex_Type()
)
clusManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusManagerIndex.setStatus("current")
_ClusManagerName_Type = DisplayString
_ClusManagerName_Object = MibTableColumn
clusManagerName = _ClusManagerName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 2),
    _ClusManagerName_Type()
)
clusManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerName.setStatus("current")
_ClusManagerVersion_Type = DisplayString
_ClusManagerVersion_Object = MibTableColumn
clusManagerVersion = _ClusManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 3),
    _ClusManagerVersion_Type()
)
clusManagerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerVersion.setStatus("current")
_ClusManagerHostSerialNo_Type = DisplayString
_ClusManagerHostSerialNo_Object = MibTableColumn
clusManagerHostSerialNo = _ClusManagerHostSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 4),
    _ClusManagerHostSerialNo_Type()
)
clusManagerHostSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerHostSerialNo.setStatus("current")


class _ClusManagerStatus_Type(Integer32):
    """Custom type clusManagerStatus based on Integer32"""
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


_ClusManagerStatus_Type.__name__ = "Integer32"
_ClusManagerStatus_Object = MibTableColumn
clusManagerStatus = _ClusManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 5),
    _ClusManagerStatus_Type()
)
clusManagerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerStatus.setStatus("current")
_ClusManagerIsVirtual_Type = TruthValue
_ClusManagerIsVirtual_Object = MibTableColumn
clusManagerIsVirtual = _ClusManagerIsVirtual_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 7),
    _ClusManagerIsVirtual_Type()
)
clusManagerIsVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerIsVirtual.setStatus("current")
_ClusManagerIsFailover_Type = TruthValue
_ClusManagerIsFailover_Object = MibTableColumn
clusManagerIsFailover = _ClusManagerIsFailover_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 9),
    _ClusManagerIsFailover_Type()
)
clusManagerIsFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerIsFailover.setStatus("current")
_ClusManagerRowStatus_Type = RowStatus
_ClusManagerRowStatus_Object = MibTableColumn
clusManagerRowStatus = _ClusManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 44, 1, 10),
    _ClusManagerRowStatus_Type()
)
clusManagerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerRowStatus.setStatus("obsolete")
_ClusModuleCount_Type = Integer32
_ClusModuleCount_Object = MibScalar
clusModuleCount = _ClusModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 45),
    _ClusModuleCount_Type()
)
clusModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleCount.setStatus("current")
_ClusModuleTable_Object = MibTable
clusModuleTable = _ClusModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46)
)
if mibBuilder.loadTexts:
    clusModuleTable.setStatus("current")
_ClusModuleEntry_Object = MibTableRow
clusModuleEntry = _ClusModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1)
)
clusModuleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleIndex"),
)
if mibBuilder.loadTexts:
    clusModuleEntry.setStatus("current")
_ClusModuleIndex_Type = Unsigned32
_ClusModuleIndex_Object = MibTableColumn
clusModuleIndex = _ClusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 1),
    _ClusModuleIndex_Type()
)
clusModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusModuleIndex.setStatus("current")
_ClusModuleName_Type = DisplayString
_ClusModuleName_Object = MibTableColumn
clusModuleName = _ClusModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 2),
    _ClusModuleName_Type()
)
clusModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleName.setStatus("current")
_ClusModuleVersion_Type = DisplayString
_ClusModuleVersion_Object = MibTableColumn
clusModuleVersion = _ClusModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 3),
    _ClusModuleVersion_Type()
)
clusModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleVersion.setStatus("current")
_ClusModuleSerialNo_Type = DisplayString
_ClusModuleSerialNo_Object = MibTableColumn
clusModuleSerialNo = _ClusModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 4),
    _ClusModuleSerialNo_Type()
)
clusModuleSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleSerialNo.setStatus("current")
_ClusModuleUsableSpace_Type = CounterBasedGauge64
_ClusModuleUsableSpace_Object = MibTableColumn
clusModuleUsableSpace = _ClusModuleUsableSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 5),
    _ClusModuleUsableSpace_Type()
)
clusModuleUsableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleUsableSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleUsableSpace.setUnits("kB")
_ClusModuleAvailableSpace_Type = CounterBasedGauge64
_ClusModuleAvailableSpace_Object = MibTableColumn
clusModuleAvailableSpace = _ClusModuleAvailableSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 6),
    _ClusModuleAvailableSpace_Type()
)
clusModuleAvailableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleAvailableSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleAvailableSpace.setUnits("kB")
_ClusModuleIsManager_Type = TruthValue
_ClusModuleIsManager_Object = MibTableColumn
clusModuleIsManager = _ClusModuleIsManager_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 7),
    _ClusModuleIsManager_Type()
)
clusModuleIsManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleIsManager.setStatus("current")
_ClusModuleRaidConfiguration_Type = DisplayString
_ClusModuleRaidConfiguration_Object = MibTableColumn
clusModuleRaidConfiguration = _ClusModuleRaidConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 8),
    _ClusModuleRaidConfiguration_Type()
)
clusModuleRaidConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleRaidConfiguration.setStatus("current")
_ClusModuleStorageState_Type = DisplayString
_ClusModuleStorageState_Object = MibTableColumn
clusModuleStorageState = _ClusModuleStorageState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 9),
    _ClusModuleStorageState_Type()
)
clusModuleStorageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStorageState.setStatus("current")


class _ClusModuleStorageStatus_Type(Integer32):
    """Custom type clusModuleStorageStatus based on Integer32"""
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


_ClusModuleStorageStatus_Type.__name__ = "Integer32"
_ClusModuleStorageStatus_Object = MibTableColumn
clusModuleStorageStatus = _ClusModuleStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 10),
    _ClusModuleStorageStatus_Type()
)
clusModuleStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStorageStatus.setStatus("current")
_ClusModuleStorageIsReady_Type = TruthValue
_ClusModuleStorageIsReady_Object = MibTableColumn
clusModuleStorageIsReady = _ClusModuleStorageIsReady_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 11),
    _ClusModuleStorageIsReady_Type()
)
clusModuleStorageIsReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStorageIsReady.setStatus("current")
_ClusModuleCreationTime_Type = DateAndTime
_ClusModuleCreationTime_Object = MibTableColumn
clusModuleCreationTime = _ClusModuleCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 12),
    _ClusModuleCreationTime_Type()
)
clusModuleCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleCreationTime.setStatus("current")
_ClusModuleDescription_Type = DisplayString
_ClusModuleDescription_Object = MibTableColumn
clusModuleDescription = _ClusModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 13),
    _ClusModuleDescription_Type()
)
clusModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleDescription.setStatus("obsolete")
_ClusModuleClusterName_Type = DisplayString
_ClusModuleClusterName_Object = MibTableColumn
clusModuleClusterName = _ClusModuleClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 14),
    _ClusModuleClusterName_Type()
)
clusModuleClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleClusterName.setStatus("current")
_ClusModuleEnabledFeatures_Type = ClusFeatureBits
_ClusModuleEnabledFeatures_Object = MibTableColumn
clusModuleEnabledFeatures = _ClusModuleEnabledFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 16),
    _ClusModuleEnabledFeatures_Type()
)
clusModuleEnabledFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleEnabledFeatures.setStatus("current")
_ClusModuleFeatureKey_Type = DisplayString
_ClusModuleFeatureKey_Object = MibTableColumn
clusModuleFeatureKey = _ClusModuleFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 17),
    _ClusModuleFeatureKey_Type()
)
clusModuleFeatureKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleFeatureKey.setStatus("current")


class _ClusModuleStorageCondition_Type(Integer32):
    """Custom type clusModuleStorageCondition based on Integer32"""
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
        *(("notReady", 1),
          ("inoperable", 2),
          ("overloaded", 3),
          ("ready", 4))
    )


_ClusModuleStorageCondition_Type.__name__ = "Integer32"
_ClusModuleStorageCondition_Object = MibTableColumn
clusModuleStorageCondition = _ClusModuleStorageCondition_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 19),
    _ClusModuleStorageCondition_Type()
)
clusModuleStorageCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStorageCondition.setStatus("current")
_ClusModuleStatsIOsRead_Type = Counter64
_ClusModuleStatsIOsRead_Object = MibTableColumn
clusModuleStatsIOsRead = _ClusModuleStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 20),
    _ClusModuleStatsIOsRead_Type()
)
clusModuleStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsIOsRead.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsIOsRead.setUnits("operations")
_ClusModuleStatsIOsWrite_Type = Counter64
_ClusModuleStatsIOsWrite_Object = MibTableColumn
clusModuleStatsIOsWrite = _ClusModuleStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 21),
    _ClusModuleStatsIOsWrite_Type()
)
clusModuleStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsIOsWrite.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsIOsWrite.setUnits("operations")
_ClusModuleStatsKbytesRead_Type = Counter64
_ClusModuleStatsKbytesRead_Object = MibTableColumn
clusModuleStatsKbytesRead = _ClusModuleStatsKbytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 22),
    _ClusModuleStatsKbytesRead_Type()
)
clusModuleStatsKbytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsKbytesRead.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsKbytesRead.setUnits("Kbytes")
_ClusModuleStatsKbytesWrite_Type = Counter64
_ClusModuleStatsKbytesWrite_Object = MibTableColumn
clusModuleStatsKbytesWrite = _ClusModuleStatsKbytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 23),
    _ClusModuleStatsKbytesWrite_Type()
)
clusModuleStatsKbytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsKbytesWrite.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsKbytesWrite.setUnits("Kbytes")
_ClusModuleStatsQDepthTotal_Type = Gauge32
_ClusModuleStatsQDepthTotal_Object = MibTableColumn
clusModuleStatsQDepthTotal = _ClusModuleStatsQDepthTotal_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 24),
    _ClusModuleStatsQDepthTotal_Type()
)
clusModuleStatsQDepthTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsQDepthTotal.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsQDepthTotal.setUnits("operations")
_ClusModuleStatsIoLatencyRead_Type = Counter64
_ClusModuleStatsIoLatencyRead_Object = MibTableColumn
clusModuleStatsIoLatencyRead = _ClusModuleStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 25),
    _ClusModuleStatsIoLatencyRead_Type()
)
clusModuleStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsIoLatencyRead.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsIoLatencyRead.setUnits("ms")
_ClusModuleStatsIoLatencyWrite_Type = Counter64
_ClusModuleStatsIoLatencyWrite_Object = MibTableColumn
clusModuleStatsIoLatencyWrite = _ClusModuleStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 26),
    _ClusModuleStatsIoLatencyWrite_Type()
)
clusModuleStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsIoLatencyWrite.setStatus("obsolete")
if mibBuilder.loadTexts:
    clusModuleStatsIoLatencyWrite.setUnits("ms")
_ClusModuleStatsStoreLatencyTotal_Type = Counter64
_ClusModuleStatsStoreLatencyTotal_Object = MibTableColumn
clusModuleStatsStoreLatencyTotal = _ClusModuleStatsStoreLatencyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 27),
    _ClusModuleStatsStoreLatencyTotal_Type()
)
clusModuleStatsStoreLatencyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStatsStoreLatencyTotal.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleStatsStoreLatencyTotal.setUnits("ms")
_ClusModuleProvisionedSpace_Type = CounterBasedGauge64
_ClusModuleProvisionedSpace_Object = MibTableColumn
clusModuleProvisionedSpace = _ClusModuleProvisionedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 28),
    _ClusModuleProvisionedSpace_Type()
)
clusModuleProvisionedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleProvisionedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleProvisionedSpace.setUnits("kB")
_ClusModuleUsedSpace_Type = CounterBasedGauge64
_ClusModuleUsedSpace_Object = MibTableColumn
clusModuleUsedSpace = _ClusModuleUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 29),
    _ClusModuleUsedSpace_Type()
)
clusModuleUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleUsedSpace.setUnits("kB")
_ClusModuleRowStatus_Type = RowStatus
_ClusModuleRowStatus_Object = MibTableColumn
clusModuleRowStatus = _ClusModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 46, 1, 99),
    _ClusModuleRowStatus_Type()
)
clusModuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleRowStatus.setStatus("obsolete")
_ClusClusterCount_Type = Integer32
_ClusClusterCount_Object = MibScalar
clusClusterCount = _ClusClusterCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 47),
    _ClusClusterCount_Type()
)
clusClusterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterCount.setStatus("current")
_ClusClusterTable_Object = MibTable
clusClusterTable = _ClusClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48)
)
if mibBuilder.loadTexts:
    clusClusterTable.setStatus("current")
_ClusClusterEntry_Object = MibTableRow
clusClusterEntry = _ClusClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1)
)
clusClusterEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterIndex"),
)
if mibBuilder.loadTexts:
    clusClusterEntry.setStatus("current")
_ClusClusterIndex_Type = Unsigned32
_ClusClusterIndex_Object = MibTableColumn
clusClusterIndex = _ClusClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 1),
    _ClusClusterIndex_Type()
)
clusClusterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusClusterIndex.setStatus("current")
_ClusClusterName_Type = DisplayString
_ClusClusterName_Object = MibTableColumn
clusClusterName = _ClusClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 2),
    _ClusClusterName_Type()
)
clusClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterName.setStatus("current")
_ClusClusterModuleCount_Type = Gauge32
_ClusClusterModuleCount_Object = MibTableColumn
clusClusterModuleCount = _ClusClusterModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 3),
    _ClusClusterModuleCount_Type()
)
clusClusterModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterModuleCount.setStatus("current")
_ClusClusterVolumeCount_Type = Gauge32
_ClusClusterVolumeCount_Object = MibTableColumn
clusClusterVolumeCount = _ClusClusterVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 4),
    _ClusClusterVolumeCount_Type()
)
clusClusterVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterVolumeCount.setStatus("current")
_ClusClusterDescription_Type = DisplayString
_ClusClusterDescription_Object = MibTableColumn
clusClusterDescription = _ClusClusterDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 5),
    _ClusClusterDescription_Type()
)
clusClusterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterDescription.setStatus("current")
_ClusClusterHotSpareTimeout_Type = CounterBasedGauge64
_ClusClusterHotSpareTimeout_Object = MibTableColumn
clusClusterHotSpareTimeout = _ClusClusterHotSpareTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 7),
    _ClusClusterHotSpareTimeout_Type()
)
clusClusterHotSpareTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterHotSpareTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusClusterHotSpareTimeout.setUnits("seconds")
_ClusClusterISNSCount_Type = Gauge32
_ClusClusterISNSCount_Object = MibTableColumn
clusClusterISNSCount = _ClusClusterISNSCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 8),
    _ClusClusterISNSCount_Type()
)
clusClusterISNSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISNSCount.setStatus("current")
_ClusClusterISCSIVirtualIPCount_Type = Gauge32
_ClusClusterISCSIVirtualIPCount_Object = MibTableColumn
clusClusterISCSIVirtualIPCount = _ClusClusterISCSIVirtualIPCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 15),
    _ClusClusterISCSIVirtualIPCount_Type()
)
clusClusterISCSIVirtualIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPCount.setStatus("current")
_ClusClusterISCSIVirtualIPEnabled_Type = TruthValue
_ClusClusterISCSIVirtualIPEnabled_Object = MibTableColumn
clusClusterISCSIVirtualIPEnabled = _ClusClusterISCSIVirtualIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 16),
    _ClusClusterISCSIVirtualIPEnabled_Type()
)
clusClusterISCSIVirtualIPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPEnabled.setStatus("current")
_ClusClusterAvailableSpace_Type = CounterBasedGauge64
_ClusClusterAvailableSpace_Object = MibTableColumn
clusClusterAvailableSpace = _ClusClusterAvailableSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 17),
    _ClusClusterAvailableSpace_Type()
)
clusClusterAvailableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterAvailableSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterAvailableSpace.setUnits("kB")
_ClusClusterStatsIOsRead_Type = Counter64
_ClusClusterStatsIOsRead_Object = MibTableColumn
clusClusterStatsIOsRead = _ClusClusterStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 20),
    _ClusClusterStatsIOsRead_Type()
)
clusClusterStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsIOsRead.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsIOsRead.setUnits("operations")
_ClusClusterStatsIOsWrite_Type = Counter64
_ClusClusterStatsIOsWrite_Object = MibTableColumn
clusClusterStatsIOsWrite = _ClusClusterStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 21),
    _ClusClusterStatsIOsWrite_Type()
)
clusClusterStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsIOsWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsIOsWrite.setUnits("operations")
_ClusClusterStatsBytesRead_Type = Counter64
_ClusClusterStatsBytesRead_Object = MibTableColumn
clusClusterStatsBytesRead = _ClusClusterStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 22),
    _ClusClusterStatsBytesRead_Type()
)
clusClusterStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsBytesRead.setUnits("B")
_ClusClusterStatsBytesWrite_Type = Counter64
_ClusClusterStatsBytesWrite_Object = MibTableColumn
clusClusterStatsBytesWrite = _ClusClusterStatsBytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 23),
    _ClusClusterStatsBytesWrite_Type()
)
clusClusterStatsBytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsBytesWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsBytesWrite.setUnits("B")
_ClusClusterStatsQDepthRead_Type = Gauge32
_ClusClusterStatsQDepthRead_Object = MibTableColumn
clusClusterStatsQDepthRead = _ClusClusterStatsQDepthRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 24),
    _ClusClusterStatsQDepthRead_Type()
)
clusClusterStatsQDepthRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsQDepthRead.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsQDepthRead.setUnits("operations")
_ClusClusterStatsQDepthWrite_Type = Gauge32
_ClusClusterStatsQDepthWrite_Object = MibTableColumn
clusClusterStatsQDepthWrite = _ClusClusterStatsQDepthWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 25),
    _ClusClusterStatsQDepthWrite_Type()
)
clusClusterStatsQDepthWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsQDepthWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsQDepthWrite.setUnits("operations")
_ClusClusterStatsIoLatencyRead_Type = Counter64
_ClusClusterStatsIoLatencyRead_Object = MibTableColumn
clusClusterStatsIoLatencyRead = _ClusClusterStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 26),
    _ClusClusterStatsIoLatencyRead_Type()
)
clusClusterStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsIoLatencyRead.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsIoLatencyRead.setUnits("ms")
_ClusClusterStatsIoLatencyWrite_Type = Counter64
_ClusClusterStatsIoLatencyWrite_Object = MibTableColumn
clusClusterStatsIoLatencyWrite = _ClusClusterStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 27),
    _ClusClusterStatsIoLatencyWrite_Type()
)
clusClusterStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsIoLatencyWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsIoLatencyWrite.setUnits("ms")
_ClusClusterStatsCacheHits_Type = Counter64
_ClusClusterStatsCacheHits_Object = MibTableColumn
clusClusterStatsCacheHits = _ClusClusterStatsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 28),
    _ClusClusterStatsCacheHits_Type()
)
clusClusterStatsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterStatsCacheHits.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterStatsCacheHits.setUnits("operations")
_ClusClusterTotalSpace_Type = CounterBasedGauge64
_ClusClusterTotalSpace_Object = MibTableColumn
clusClusterTotalSpace = _ClusClusterTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 29),
    _ClusClusterTotalSpace_Type()
)
clusClusterTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterTotalSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterTotalSpace.setUnits("kB")
_ClusClusterProvisionedSpace_Type = CounterBasedGauge64
_ClusClusterProvisionedSpace_Object = MibTableColumn
clusClusterProvisionedSpace = _ClusClusterProvisionedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 30),
    _ClusClusterProvisionedSpace_Type()
)
clusClusterProvisionedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterProvisionedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterProvisionedSpace.setUnits("kB")
_ClusClusterUsedSpace_Type = CounterBasedGauge64
_ClusClusterUsedSpace_Object = MibTableColumn
clusClusterUsedSpace = _ClusClusterUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 31),
    _ClusClusterUsedSpace_Type()
)
clusClusterUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterUsedSpace.setUnits("kB")
_ClusClusterUtilization_Type = Gauge32
_ClusClusterUtilization_Object = MibTableColumn
clusClusterUtilization = _ClusClusterUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 32),
    _ClusClusterUtilization_Type()
)
clusClusterUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterUtilization.setStatus("current")
if mibBuilder.loadTexts:
    clusClusterUtilization.setUnits("%")
_ClusClusterRowStatus_Type = RowStatus
_ClusClusterRowStatus_Object = MibTableColumn
clusClusterRowStatus = _ClusClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 48, 1, 99),
    _ClusClusterRowStatus_Type()
)
clusClusterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterRowStatus.setStatus("obsolete")
_ClusClusterModuleTable_Object = MibTable
clusClusterModuleTable = _ClusClusterModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49)
)
if mibBuilder.loadTexts:
    clusClusterModuleTable.setStatus("current")
_ClusClusterModuleEntry_Object = MibTableRow
clusClusterModuleEntry = _ClusClusterModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49, 1)
)
clusClusterModuleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterModuleIndex"),
)
if mibBuilder.loadTexts:
    clusClusterModuleEntry.setStatus("current")
_ClusClusterModuleIndex_Type = Unsigned32
_ClusClusterModuleIndex_Object = MibTableColumn
clusClusterModuleIndex = _ClusClusterModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49, 1, 1),
    _ClusClusterModuleIndex_Type()
)
clusClusterModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusClusterModuleIndex.setStatus("current")
_ClusClusterModuleName_Type = DisplayString
_ClusClusterModuleName_Object = MibTableColumn
clusClusterModuleName = _ClusClusterModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49, 1, 2),
    _ClusClusterModuleName_Type()
)
clusClusterModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterModuleName.setStatus("current")
_ClusClusterModuleSerialNo_Type = DisplayString
_ClusClusterModuleSerialNo_Object = MibTableColumn
clusClusterModuleSerialNo = _ClusClusterModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49, 1, 3),
    _ClusClusterModuleSerialNo_Type()
)
clusClusterModuleSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterModuleSerialNo.setStatus("current")
_ClusClusterModuleIsHotSpare_Type = TruthValue
_ClusClusterModuleIsHotSpare_Object = MibTableColumn
clusClusterModuleIsHotSpare = _ClusClusterModuleIsHotSpare_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49, 1, 4),
    _ClusClusterModuleIsHotSpare_Type()
)
clusClusterModuleIsHotSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterModuleIsHotSpare.setStatus("deprecated")
_ClusClusterModuleRowStatus_Type = RowStatus
_ClusClusterModuleRowStatus_Object = MibTableColumn
clusClusterModuleRowStatus = _ClusClusterModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 49, 1, 5),
    _ClusClusterModuleRowStatus_Type()
)
clusClusterModuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterModuleRowStatus.setStatus("obsolete")
_ClusClusterISNSTable_Object = MibTable
clusClusterISNSTable = _ClusClusterISNSTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 50)
)
if mibBuilder.loadTexts:
    clusClusterISNSTable.setStatus("current")
_ClusClusterISNSEntry_Object = MibTableRow
clusClusterISNSEntry = _ClusClusterISNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 50, 1)
)
clusClusterISNSEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISNSIndex"),
)
if mibBuilder.loadTexts:
    clusClusterISNSEntry.setStatus("current")
_ClusClusterISNSIndex_Type = Unsigned32
_ClusClusterISNSIndex_Object = MibTableColumn
clusClusterISNSIndex = _ClusClusterISNSIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 50, 1, 1),
    _ClusClusterISNSIndex_Type()
)
clusClusterISNSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusClusterISNSIndex.setStatus("current")
_ClusClusterISNSHost_Type = DisplayString
_ClusClusterISNSHost_Object = MibTableColumn
clusClusterISNSHost = _ClusClusterISNSHost_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 50, 1, 2),
    _ClusClusterISNSHost_Type()
)
clusClusterISNSHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISNSHost.setStatus("current")
_ClusClusterISNSRowStatus_Type = RowStatus
_ClusClusterISNSRowStatus_Object = MibTableColumn
clusClusterISNSRowStatus = _ClusClusterISNSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 50, 1, 5),
    _ClusClusterISNSRowStatus_Type()
)
clusClusterISNSRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISNSRowStatus.setStatus("obsolete")
_ClusClusterISCSIVirtualIPTable_Object = MibTable
clusClusterISCSIVirtualIPTable = _ClusClusterISCSIVirtualIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95)
)
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPTable.setStatus("current")
_ClusClusterISCSIVirtualIPEntry_Object = MibTableRow
clusClusterISCSIVirtualIPEntry = _ClusClusterISCSIVirtualIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95, 1)
)
clusClusterISCSIVirtualIPEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPIndex"),
)
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPEntry.setStatus("current")
_ClusClusterISCSIVirtualIPIndex_Type = Unsigned32
_ClusClusterISCSIVirtualIPIndex_Object = MibTableColumn
clusClusterISCSIVirtualIPIndex = _ClusClusterISCSIVirtualIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95, 1, 1),
    _ClusClusterISCSIVirtualIPIndex_Type()
)
clusClusterISCSIVirtualIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPIndex.setStatus("current")
_ClusClusterISCSIVirtualIPAddress_Type = IpAddress
_ClusClusterISCSIVirtualIPAddress_Object = MibTableColumn
clusClusterISCSIVirtualIPAddress = _ClusClusterISCSIVirtualIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95, 1, 2),
    _ClusClusterISCSIVirtualIPAddress_Type()
)
clusClusterISCSIVirtualIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPAddress.setStatus("current")
_ClusClusterISCSIVirtualIPMask_Type = IpAddress
_ClusClusterISCSIVirtualIPMask_Object = MibTableColumn
clusClusterISCSIVirtualIPMask = _ClusClusterISCSIVirtualIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95, 1, 3),
    _ClusClusterISCSIVirtualIPMask_Type()
)
clusClusterISCSIVirtualIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPMask.setStatus("current")
_ClusClusterISCSIVirtualIPRoute_Type = IpAddress
_ClusClusterISCSIVirtualIPRoute_Object = MibTableColumn
clusClusterISCSIVirtualIPRoute = _ClusClusterISCSIVirtualIPRoute_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95, 1, 4),
    _ClusClusterISCSIVirtualIPRoute_Type()
)
clusClusterISCSIVirtualIPRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPRoute.setStatus("deprecated")
_ClusClusterISCSIVirtualIPRowStatus_Type = RowStatus
_ClusClusterISCSIVirtualIPRowStatus_Object = MibTableColumn
clusClusterISCSIVirtualIPRowStatus = _ClusClusterISCSIVirtualIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 95, 1, 5),
    _ClusClusterISCSIVirtualIPRowStatus_Type()
)
clusClusterISCSIVirtualIPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterISCSIVirtualIPRowStatus.setStatus("obsolete")
_ClusVolumeCount_Type = Integer32
_ClusVolumeCount_Object = MibScalar
clusVolumeCount = _ClusVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 96),
    _ClusVolumeCount_Type()
)
clusVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeCount.setStatus("current")
_ClusVolumeTable_Object = MibTable
clusVolumeTable = _ClusVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97)
)
if mibBuilder.loadTexts:
    clusVolumeTable.setStatus("current")
_ClusVolumeEntry_Object = MibTableRow
clusVolumeEntry = _ClusVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1)
)
clusVolumeEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeEntry.setStatus("current")
_ClusVolumeIndex_Type = Unsigned32
_ClusVolumeIndex_Object = MibTableColumn
clusVolumeIndex = _ClusVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 1),
    _ClusVolumeIndex_Type()
)
clusVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusVolumeIndex.setStatus("current")
_ClusVolumeName_Type = DisplayString
_ClusVolumeName_Object = MibTableColumn
clusVolumeName = _ClusVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 2),
    _ClusVolumeName_Type()
)
clusVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeName.setStatus("current")
_ClusVolumeCreationTime_Type = DateAndTime
_ClusVolumeCreationTime_Object = MibTableColumn
clusVolumeCreationTime = _ClusVolumeCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 3),
    _ClusVolumeCreationTime_Type()
)
clusVolumeCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeCreationTime.setStatus("current")
_ClusVolumeDescription_Type = DisplayString
_ClusVolumeDescription_Object = MibTableColumn
clusVolumeDescription = _ClusVolumeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 4),
    _ClusVolumeDescription_Type()
)
clusVolumeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeDescription.setStatus("current")
_ClusVolumeSize_Type = CounterBasedGauge64
_ClusVolumeSize_Object = MibTableColumn
clusVolumeSize = _ClusVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 5),
    _ClusVolumeSize_Type()
)
clusVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSize.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSize.setUnits("kB")
_ClusVolumeSoftThreshold_Type = CounterBasedGauge64
_ClusVolumeSoftThreshold_Object = MibTableColumn
clusVolumeSoftThreshold = _ClusVolumeSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 6),
    _ClusVolumeSoftThreshold_Type()
)
clusVolumeSoftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSoftThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusVolumeSoftThreshold.setUnits("kB")
_ClusVolumeHardThreshold_Type = CounterBasedGauge64
_ClusVolumeHardThreshold_Object = MibTableColumn
clusVolumeHardThreshold = _ClusVolumeHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 7),
    _ClusVolumeHardThreshold_Type()
)
clusVolumeHardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeHardThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusVolumeHardThreshold.setUnits("kB")
_ClusVolumeReplicaCount_Type = Integer32
_ClusVolumeReplicaCount_Object = MibTableColumn
clusVolumeReplicaCount = _ClusVolumeReplicaCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 8),
    _ClusVolumeReplicaCount_Type()
)
clusVolumeReplicaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeReplicaCount.setStatus("current")
_ClusVolumeSnapshotCount_Type = Gauge32
_ClusVolumeSnapshotCount_Object = MibTableColumn
clusVolumeSnapshotCount = _ClusVolumeSnapshotCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 9),
    _ClusVolumeSnapshotCount_Type()
)
clusVolumeSnapshotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCount.setStatus("current")
_ClusVolumeACLCount_Type = Gauge32
_ClusVolumeACLCount_Object = MibTableColumn
clusVolumeACLCount = _ClusVolumeACLCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 10),
    _ClusVolumeACLCount_Type()
)
clusVolumeACLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeACLCount.setStatus("current")
_ClusVolumeClusterName_Type = DisplayString
_ClusVolumeClusterName_Object = MibTableColumn
clusVolumeClusterName = _ClusVolumeClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 11),
    _ClusVolumeClusterName_Type()
)
clusVolumeClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeClusterName.setStatus("current")
_ClusVolumeIsSoftThresholdExceeded_Type = TruthValue
_ClusVolumeIsSoftThresholdExceeded_Object = MibTableColumn
clusVolumeIsSoftThresholdExceeded = _ClusVolumeIsSoftThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 13),
    _ClusVolumeIsSoftThresholdExceeded_Type()
)
clusVolumeIsSoftThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsSoftThresholdExceeded.setStatus("deprecated")
_ClusVolumeIsHardThresholdExceeded_Type = TruthValue
_ClusVolumeIsHardThresholdExceeded_Object = MibTableColumn
clusVolumeIsHardThresholdExceeded = _ClusVolumeIsHardThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 14),
    _ClusVolumeIsHardThresholdExceeded_Type()
)
clusVolumeIsHardThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsHardThresholdExceeded.setStatus("deprecated")
_ClusVolumeReplicationStatus_Type = ClusReplicationStatus
_ClusVolumeReplicationStatus_Object = MibTableColumn
clusVolumeReplicationStatus = _ClusVolumeReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 15),
    _ClusVolumeReplicationStatus_Type()
)
clusVolumeReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeReplicationStatus.setStatus("current")
_ClusVolumeIsRemoteSnapshot_Type = TruthValue
_ClusVolumeIsRemoteSnapshot_Object = MibTableColumn
clusVolumeIsRemoteSnapshot = _ClusVolumeIsRemoteSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 16),
    _ClusVolumeIsRemoteSnapshot_Type()
)
clusVolumeIsRemoteSnapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsRemoteSnapshot.setStatus("current")
_ClusVolumeRemoteSnapshotFailureMessage_Type = DisplayString
_ClusVolumeRemoteSnapshotFailureMessage_Object = MibTableColumn
clusVolumeRemoteSnapshotFailureMessage = _ClusVolumeRemoteSnapshotFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 17),
    _ClusVolumeRemoteSnapshotFailureMessage_Type()
)
clusVolumeRemoteSnapshotFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeRemoteSnapshotFailureMessage.setStatus("current")
_ClusVolumeAccessType_Type = DisplayString
_ClusVolumeAccessType_Object = MibTableColumn
clusVolumeAccessType = _ClusVolumeAccessType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 19),
    _ClusVolumeAccessType_Type()
)
clusVolumeAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeAccessType.setStatus("obsolete")
_ClusVolumeMinimumReplication_Type = Gauge32
_ClusVolumeMinimumReplication_Object = MibTableColumn
clusVolumeMinimumReplication = _ClusVolumeMinimumReplication_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 20),
    _ClusVolumeMinimumReplication_Type()
)
clusVolumeMinimumReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeMinimumReplication.setStatus("current")
_ClusVolumeCreator_Type = ClusCreatorTypes
_ClusVolumeCreator_Object = MibTableColumn
clusVolumeCreator = _ClusVolumeCreator_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 22),
    _ClusVolumeCreator_Type()
)
clusVolumeCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeCreator.setStatus("current")
_ClusVolumeAutoGrowPages_Type = Integer32
_ClusVolumeAutoGrowPages_Object = MibTableColumn
clusVolumeAutoGrowPages = _ClusVolumeAutoGrowPages_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 24),
    _ClusVolumeAutoGrowPages_Type()
)
clusVolumeAutoGrowPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeAutoGrowPages.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusVolumeAutoGrowPages.setUnits("256K pages")
_ClusVolumeIscsiIqn_Type = DisplayString
_ClusVolumeIscsiIqn_Object = MibTableColumn
clusVolumeIscsiIqn = _ClusVolumeIscsiIqn_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 25),
    _ClusVolumeIscsiIqn_Type()
)
clusVolumeIscsiIqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIscsiIqn.setStatus("current")
_ClusVolumeFriendlyName_Type = DisplayString
_ClusVolumeFriendlyName_Object = MibTableColumn
clusVolumeFriendlyName = _ClusVolumeFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 27),
    _ClusVolumeFriendlyName_Type()
)
clusVolumeFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeFriendlyName.setStatus("deprecated")
_ClusVolumeInitiatorCount_Type = Gauge32
_ClusVolumeInitiatorCount_Object = MibTableColumn
clusVolumeInitiatorCount = _ClusVolumeInitiatorCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 30),
    _ClusVolumeInitiatorCount_Type()
)
clusVolumeInitiatorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorCount.setStatus("current")
_ClusVolumeUsedSpace_Type = CounterBasedGauge64
_ClusVolumeUsedSpace_Object = MibTableColumn
clusVolumeUsedSpace = _ClusVolumeUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 31),
    _ClusVolumeUsedSpace_Type()
)
clusVolumeUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeUsedSpace.setUnits("kB")
_ClusVolumeClusterUsedPercent_Type = Gauge32
_ClusVolumeClusterUsedPercent_Object = MibTableColumn
clusVolumeClusterUsedPercent = _ClusVolumeClusterUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 32),
    _ClusVolumeClusterUsedPercent_Type()
)
clusVolumeClusterUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeClusterUsedPercent.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeClusterUsedPercent.setUnits("%")
_ClusVolumeProvisionedSpace_Type = CounterBasedGauge64
_ClusVolumeProvisionedSpace_Object = MibTableColumn
clusVolumeProvisionedSpace = _ClusVolumeProvisionedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 33),
    _ClusVolumeProvisionedSpace_Type()
)
clusVolumeProvisionedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeProvisionedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeProvisionedSpace.setUnits("kB")
_ClusVolumeIsThinProvisioned_Type = TruthValue
_ClusVolumeIsThinProvisioned_Object = MibTableColumn
clusVolumeIsThinProvisioned = _ClusVolumeIsThinProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 34),
    _ClusVolumeIsThinProvisioned_Type()
)
clusVolumeIsThinProvisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsThinProvisioned.setStatus("current")
_ClusVolumeStatsIOsRead_Type = Counter64
_ClusVolumeStatsIOsRead_Object = MibTableColumn
clusVolumeStatsIOsRead = _ClusVolumeStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 36),
    _ClusVolumeStatsIOsRead_Type()
)
clusVolumeStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsIOsRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsIOsRead.setUnits("operations")
_ClusVolumeStatsIOsWrite_Type = Counter64
_ClusVolumeStatsIOsWrite_Object = MibTableColumn
clusVolumeStatsIOsWrite = _ClusVolumeStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 37),
    _ClusVolumeStatsIOsWrite_Type()
)
clusVolumeStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsIOsWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsIOsWrite.setUnits("operations")
_ClusVolumeStatsBytesRead_Type = Counter64
_ClusVolumeStatsBytesRead_Object = MibTableColumn
clusVolumeStatsBytesRead = _ClusVolumeStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 38),
    _ClusVolumeStatsBytesRead_Type()
)
clusVolumeStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsBytesRead.setUnits("B")
_ClusVolumeStatsBytesWrite_Type = Counter64
_ClusVolumeStatsBytesWrite_Object = MibTableColumn
clusVolumeStatsBytesWrite = _ClusVolumeStatsBytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 39),
    _ClusVolumeStatsBytesWrite_Type()
)
clusVolumeStatsBytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsBytesWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsBytesWrite.setUnits("B")
_ClusVolumeStatsQDepthRead_Type = Gauge32
_ClusVolumeStatsQDepthRead_Object = MibTableColumn
clusVolumeStatsQDepthRead = _ClusVolumeStatsQDepthRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 40),
    _ClusVolumeStatsQDepthRead_Type()
)
clusVolumeStatsQDepthRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsQDepthRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsQDepthRead.setUnits("operations")
_ClusVolumeStatsQDepthWrite_Type = Gauge32
_ClusVolumeStatsQDepthWrite_Object = MibTableColumn
clusVolumeStatsQDepthWrite = _ClusVolumeStatsQDepthWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 41),
    _ClusVolumeStatsQDepthWrite_Type()
)
clusVolumeStatsQDepthWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsQDepthWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsQDepthWrite.setUnits("operations")
_ClusVolumeStatsIoLatencyRead_Type = Counter64
_ClusVolumeStatsIoLatencyRead_Object = MibTableColumn
clusVolumeStatsIoLatencyRead = _ClusVolumeStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 42),
    _ClusVolumeStatsIoLatencyRead_Type()
)
clusVolumeStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsIoLatencyRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsIoLatencyRead.setUnits("ms")
_ClusVolumeStatsIoLatencyWrite_Type = Counter64
_ClusVolumeStatsIoLatencyWrite_Object = MibTableColumn
clusVolumeStatsIoLatencyWrite = _ClusVolumeStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 43),
    _ClusVolumeStatsIoLatencyWrite_Type()
)
clusVolumeStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsIoLatencyWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsIoLatencyWrite.setUnits("ms")
_ClusVolumeStatsCacheHits_Type = Counter64
_ClusVolumeStatsCacheHits_Object = MibTableColumn
clusVolumeStatsCacheHits = _ClusVolumeStatsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 44),
    _ClusVolumeStatsCacheHits_Type()
)
clusVolumeStatsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeStatsCacheHits.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeStatsCacheHits.setUnits("operations")
_ClusVolumeAutoGrowSecondsDefault_Type = Integer32
_ClusVolumeAutoGrowSecondsDefault_Object = MibTableColumn
clusVolumeAutoGrowSecondsDefault = _ClusVolumeAutoGrowSecondsDefault_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 45),
    _ClusVolumeAutoGrowSecondsDefault_Type()
)
clusVolumeAutoGrowSecondsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeAutoGrowSecondsDefault.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeAutoGrowSecondsDefault.setUnits("seconds")
_ClusVolumeAutoGrowSeconds_Type = Gauge32
_ClusVolumeAutoGrowSeconds_Object = MibTableColumn
clusVolumeAutoGrowSeconds = _ClusVolumeAutoGrowSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 46),
    _ClusVolumeAutoGrowSeconds_Type()
)
clusVolumeAutoGrowSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeAutoGrowSeconds.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeAutoGrowSeconds.setUnits("seconds")


class _ClusVolumeType_Type(Integer32):
    """Custom type clusVolumeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mr", 1),
          ("pbnr", 2))
    )


_ClusVolumeType_Type.__name__ = "Integer32"
_ClusVolumeType_Object = MibTableColumn
clusVolumeType = _ClusVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 47),
    _ClusVolumeType_Type()
)
clusVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeType.setStatus("current")
_ClusVolumeDataProtectionLevel_Type = DisplayString
_ClusVolumeDataProtectionLevel_Object = MibTableColumn
clusVolumeDataProtectionLevel = _ClusVolumeDataProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 48),
    _ClusVolumeDataProtectionLevel_Type()
)
clusVolumeDataProtectionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeDataProtectionLevel.setStatus("current")
_ClusVolumePBNRStripes_Type = Gauge32
_ClusVolumePBNRStripes_Object = MibTableColumn
clusVolumePBNRStripes = _ClusVolumePBNRStripes_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 49),
    _ClusVolumePBNRStripes_Type()
)
clusVolumePBNRStripes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumePBNRStripes.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumePBNRStripes.setUnits("pages")
_ClusVolumePBNRParity_Type = Gauge32
_ClusVolumePBNRParity_Object = MibTableColumn
clusVolumePBNRParity = _ClusVolumePBNRParity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 50),
    _ClusVolumePBNRParity_Type()
)
clusVolumePBNRParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumePBNRParity.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumePBNRParity.setUnits("pages")
_ClusVolumeAvailableSpace_Type = CounterBasedGauge64
_ClusVolumeAvailableSpace_Object = MibTableColumn
clusVolumeAvailableSpace = _ClusVolumeAvailableSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 51),
    _ClusVolumeAvailableSpace_Type()
)
clusVolumeAvailableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeAvailableSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeAvailableSpace.setUnits("kB")
_ClusVolumeUsedPercent_Type = Gauge32
_ClusVolumeUsedPercent_Object = MibTableColumn
clusVolumeUsedPercent = _ClusVolumeUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 52),
    _ClusVolumeUsedPercent_Type()
)
clusVolumeUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeUsedPercent.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeUsedPercent.setUnits("%")
_ClusVolumeIsFull_Type = TruthValue
_ClusVolumeIsFull_Object = MibTableColumn
clusVolumeIsFull = _ClusVolumeIsFull_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 53),
    _ClusVolumeIsFull_Type()
)
clusVolumeIsFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsFull.setStatus("current")
_ClusVolumeIsDeleting_Type = TruthValue
_ClusVolumeIsDeleting_Object = MibTableColumn
clusVolumeIsDeleting = _ClusVolumeIsDeleting_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 54),
    _ClusVolumeIsDeleting_Type()
)
clusVolumeIsDeleting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsDeleting.setStatus("current")
_ClusVolumeIsAvailable_Type = TruthValue
_ClusVolumeIsAvailable_Object = MibTableColumn
clusVolumeIsAvailable = _ClusVolumeIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 55),
    _ClusVolumeIsAvailable_Type()
)
clusVolumeIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsAvailable.setStatus("current")
_ClusVolumeLunIsAvailable_Type = TruthValue
_ClusVolumeLunIsAvailable_Object = MibTableColumn
clusVolumeLunIsAvailable = _ClusVolumeLunIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 56),
    _ClusVolumeLunIsAvailable_Type()
)
clusVolumeLunIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeLunIsAvailable.setStatus("current")
_ClusVolumeReplicationState_Type = Integer32
_ClusVolumeReplicationState_Object = MibTableColumn
clusVolumeReplicationState = _ClusVolumeReplicationState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 57),
    _ClusVolumeReplicationState_Type()
)
clusVolumeReplicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeReplicationState.setStatus("current")
_ClusVolumeResyncPercent_Type = Gauge32
_ClusVolumeResyncPercent_Object = MibTableColumn
clusVolumeResyncPercent = _ClusVolumeResyncPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 58),
    _ClusVolumeResyncPercent_Type()
)
clusVolumeResyncPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeResyncPercent.setStatus("current")
_ClusVolumeRestripePending_Type = TruthValue
_ClusVolumeRestripePending_Object = MibTableColumn
clusVolumeRestripePending = _ClusVolumeRestripePending_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 59),
    _ClusVolumeRestripePending_Type()
)
clusVolumeRestripePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeRestripePending.setStatus("current")
_ClusVolumeIsMigrating_Type = TruthValue
_ClusVolumeIsMigrating_Object = MibTableColumn
clusVolumeIsMigrating = _ClusVolumeIsMigrating_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 60),
    _ClusVolumeIsMigrating_Type()
)
clusVolumeIsMigrating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsMigrating.setStatus("current")
_ClusVolumeMigrationPercent_Type = Gauge32
_ClusVolumeMigrationPercent_Object = MibTableColumn
clusVolumeMigrationPercent = _ClusVolumeMigrationPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 61),
    _ClusVolumeMigrationPercent_Type()
)
clusVolumeMigrationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeMigrationPercent.setStatus("current")
_ClusVolumeRowStatus_Type = RowStatus
_ClusVolumeRowStatus_Object = MibTableColumn
clusVolumeRowStatus = _ClusVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 97, 1, 99),
    _ClusVolumeRowStatus_Type()
)
clusVolumeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeRowStatus.setStatus("obsolete")
_ClusVolumeACLTable_Object = MibTable
clusVolumeACLTable = _ClusVolumeACLTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 98)
)
if mibBuilder.loadTexts:
    clusVolumeACLTable.setStatus("current")
_ClusVolumeACLEntry_Object = MibTableRow
clusVolumeACLEntry = _ClusVolumeACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 98, 1)
)
clusVolumeACLEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeACLIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeACLEntry.setStatus("current")
_ClusVolumeACLIndex_Type = Unsigned32
_ClusVolumeACLIndex_Object = MibTableColumn
clusVolumeACLIndex = _ClusVolumeACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 98, 1, 1),
    _ClusVolumeACLIndex_Type()
)
clusVolumeACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusVolumeACLIndex.setStatus("current")
_ClusVolumeACLServer_Type = DisplayString
_ClusVolumeACLServer_Object = MibTableColumn
clusVolumeACLServer = _ClusVolumeACLServer_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 98, 1, 2),
    _ClusVolumeACLServer_Type()
)
clusVolumeACLServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeACLServer.setStatus("current")
_ClusVolumeACLPermissions_Type = ClusPermissionBits
_ClusVolumeACLPermissions_Object = MibTableColumn
clusVolumeACLPermissions = _ClusVolumeACLPermissions_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 98, 1, 3),
    _ClusVolumeACLPermissions_Type()
)
clusVolumeACLPermissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeACLPermissions.setStatus("current")
_ClusVolumeACLRowStatus_Type = RowStatus
_ClusVolumeACLRowStatus_Object = MibTableColumn
clusVolumeACLRowStatus = _ClusVolumeACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 98, 1, 6),
    _ClusVolumeACLRowStatus_Type()
)
clusVolumeACLRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeACLRowStatus.setStatus("obsolete")
_ClusVolumeInitiatorTable_Object = MibTable
clusVolumeInitiatorTable = _ClusVolumeInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99)
)
if mibBuilder.loadTexts:
    clusVolumeInitiatorTable.setStatus("current")
_ClusVolumeInitiatorEntry_Object = MibTableRow
clusVolumeInitiatorEntry = _ClusVolumeInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1)
)
clusVolumeInitiatorEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeInitiatorEntry.setStatus("current")
_ClusVolumeInitiatorIndex_Type = Unsigned32
_ClusVolumeInitiatorIndex_Object = MibTableColumn
clusVolumeInitiatorIndex = _ClusVolumeInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 1),
    _ClusVolumeInitiatorIndex_Type()
)
clusVolumeInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusVolumeInitiatorIndex.setStatus("current")
_ClusVolumeInitiatorIqn_Type = DisplayString
_ClusVolumeInitiatorIqn_Object = MibTableColumn
clusVolumeInitiatorIqn = _ClusVolumeInitiatorIqn_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 2),
    _ClusVolumeInitiatorIqn_Type()
)
clusVolumeInitiatorIqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorIqn.setStatus("current")
_ClusVolumeInitiatorAddress_Type = IpAddress
_ClusVolumeInitiatorAddress_Object = MibTableColumn
clusVolumeInitiatorAddress = _ClusVolumeInitiatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 3),
    _ClusVolumeInitiatorAddress_Type()
)
clusVolumeInitiatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorAddress.setStatus("current")
_ClusVolumeInitiatorPort_Type = Unsigned32
_ClusVolumeInitiatorPort_Object = MibTableColumn
clusVolumeInitiatorPort = _ClusVolumeInitiatorPort_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 4),
    _ClusVolumeInitiatorPort_Type()
)
clusVolumeInitiatorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorPort.setStatus("current")
_ClusVolumeInitiatorStatus_Type = DisplayString
_ClusVolumeInitiatorStatus_Object = MibTableColumn
clusVolumeInitiatorStatus = _ClusVolumeInitiatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 5),
    _ClusVolumeInitiatorStatus_Type()
)
clusVolumeInitiatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatus.setStatus("current")
_ClusVolumeInitiatorStatsIOsRead_Type = Counter64
_ClusVolumeInitiatorStatsIOsRead_Object = MibTableColumn
clusVolumeInitiatorStatsIOsRead = _ClusVolumeInitiatorStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 6),
    _ClusVolumeInitiatorStatsIOsRead_Type()
)
clusVolumeInitiatorStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIOsRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIOsRead.setUnits("operations")
_ClusVolumeInitiatorStatsIOsWrite_Type = Counter64
_ClusVolumeInitiatorStatsIOsWrite_Object = MibTableColumn
clusVolumeInitiatorStatsIOsWrite = _ClusVolumeInitiatorStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 7),
    _ClusVolumeInitiatorStatsIOsWrite_Type()
)
clusVolumeInitiatorStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIOsWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIOsWrite.setUnits("operations")
_ClusVolumeInitiatorStatsBytesRead_Type = Counter64
_ClusVolumeInitiatorStatsBytesRead_Object = MibTableColumn
clusVolumeInitiatorStatsBytesRead = _ClusVolumeInitiatorStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 8),
    _ClusVolumeInitiatorStatsBytesRead_Type()
)
clusVolumeInitiatorStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsBytesRead.setUnits("B")
_ClusVolumeInitiatorStatsBytesWrite_Type = Counter64
_ClusVolumeInitiatorStatsBytesWrite_Object = MibTableColumn
clusVolumeInitiatorStatsBytesWrite = _ClusVolumeInitiatorStatsBytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 9),
    _ClusVolumeInitiatorStatsBytesWrite_Type()
)
clusVolumeInitiatorStatsBytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsBytesWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsBytesWrite.setUnits("B")
_ClusVolumeInitiatorStatsQDepthRead_Type = Gauge32
_ClusVolumeInitiatorStatsQDepthRead_Object = MibTableColumn
clusVolumeInitiatorStatsQDepthRead = _ClusVolumeInitiatorStatsQDepthRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 10),
    _ClusVolumeInitiatorStatsQDepthRead_Type()
)
clusVolumeInitiatorStatsQDepthRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsQDepthRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsQDepthRead.setUnits("operations")
_ClusVolumeInitiatorStatsQDepthWrite_Type = Gauge32
_ClusVolumeInitiatorStatsQDepthWrite_Object = MibTableColumn
clusVolumeInitiatorStatsQDepthWrite = _ClusVolumeInitiatorStatsQDepthWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 11),
    _ClusVolumeInitiatorStatsQDepthWrite_Type()
)
clusVolumeInitiatorStatsQDepthWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsQDepthWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsQDepthWrite.setUnits("operations")
_ClusVolumeInitiatorStatsIoLatencyRead_Type = Counter64
_ClusVolumeInitiatorStatsIoLatencyRead_Object = MibTableColumn
clusVolumeInitiatorStatsIoLatencyRead = _ClusVolumeInitiatorStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 12),
    _ClusVolumeInitiatorStatsIoLatencyRead_Type()
)
clusVolumeInitiatorStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIoLatencyRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIoLatencyRead.setUnits("ms")
_ClusVolumeInitiatorStatsIoLatencyWrite_Type = Counter64
_ClusVolumeInitiatorStatsIoLatencyWrite_Object = MibTableColumn
clusVolumeInitiatorStatsIoLatencyWrite = _ClusVolumeInitiatorStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 13),
    _ClusVolumeInitiatorStatsIoLatencyWrite_Type()
)
clusVolumeInitiatorStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIoLatencyWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsIoLatencyWrite.setUnits("ms")
_ClusVolumeInitiatorStatsCacheHits_Type = Counter64
_ClusVolumeInitiatorStatsCacheHits_Object = MibTableColumn
clusVolumeInitiatorStatsCacheHits = _ClusVolumeInitiatorStatsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 14),
    _ClusVolumeInitiatorStatsCacheHits_Type()
)
clusVolumeInitiatorStatsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsCacheHits.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeInitiatorStatsCacheHits.setUnits("operations")
_ClusVolumeInitiatorState_Type = DisplayString
_ClusVolumeInitiatorState_Object = MibTableColumn
clusVolumeInitiatorState = _ClusVolumeInitiatorState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 15),
    _ClusVolumeInitiatorState_Type()
)
clusVolumeInitiatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorState.setStatus("current")
_ClusVolumeInitiatorRowStatus_Type = RowStatus
_ClusVolumeInitiatorRowStatus_Object = MibTableColumn
clusVolumeInitiatorRowStatus = _ClusVolumeInitiatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 99, 1, 99),
    _ClusVolumeInitiatorRowStatus_Type()
)
clusVolumeInitiatorRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeInitiatorRowStatus.setStatus("obsolete")
_ClusClusterVolumeTable_Object = MibTable
clusClusterVolumeTable = _ClusClusterVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 100)
)
if mibBuilder.loadTexts:
    clusClusterVolumeTable.setStatus("current")
_ClusClusterVolumeEntry_Object = MibTableRow
clusClusterVolumeEntry = _ClusClusterVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 100, 1)
)
clusClusterVolumeEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterVolumeIndex"),
)
if mibBuilder.loadTexts:
    clusClusterVolumeEntry.setStatus("current")
_ClusClusterVolumeIndex_Type = Unsigned32
_ClusClusterVolumeIndex_Object = MibTableColumn
clusClusterVolumeIndex = _ClusClusterVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 100, 1, 1),
    _ClusClusterVolumeIndex_Type()
)
clusClusterVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusClusterVolumeIndex.setStatus("current")
_ClusClusterVolumeName_Type = DisplayString
_ClusClusterVolumeName_Object = MibTableColumn
clusClusterVolumeName = _ClusClusterVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 100, 1, 2),
    _ClusClusterVolumeName_Type()
)
clusClusterVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterVolumeName.setStatus("current")
_ClusClusterVolumeRowStatus_Type = RowStatus
_ClusClusterVolumeRowStatus_Object = MibTableColumn
clusClusterVolumeRowStatus = _ClusClusterVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 100, 1, 3),
    _ClusClusterVolumeRowStatus_Type()
)
clusClusterVolumeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterVolumeRowStatus.setStatus("obsolete")
_ClusVolumeSnapshotTable_Object = MibTable
clusVolumeSnapshotTable = _ClusVolumeSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101)
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotTable.setStatus("current")
_ClusVolumeSnapshotEntry_Object = MibTableRow
clusVolumeSnapshotEntry = _ClusVolumeSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1)
)
clusVolumeSnapshotEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotEntry.setStatus("current")
_ClusVolumeSnapshotIndex_Type = Unsigned32
_ClusVolumeSnapshotIndex_Object = MibTableColumn
clusVolumeSnapshotIndex = _ClusVolumeSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 1),
    _ClusVolumeSnapshotIndex_Type()
)
clusVolumeSnapshotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIndex.setStatus("current")
_ClusVolumeSnapshotName_Type = DisplayString
_ClusVolumeSnapshotName_Object = MibTableColumn
clusVolumeSnapshotName = _ClusVolumeSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 2),
    _ClusVolumeSnapshotName_Type()
)
clusVolumeSnapshotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotName.setStatus("current")
_ClusVolumeSnapshotCreationTime_Type = DateAndTime
_ClusVolumeSnapshotCreationTime_Object = MibTableColumn
clusVolumeSnapshotCreationTime = _ClusVolumeSnapshotCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 3),
    _ClusVolumeSnapshotCreationTime_Type()
)
clusVolumeSnapshotCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCreationTime.setStatus("current")
_ClusVolumeSnapshotDescription_Type = DisplayString
_ClusVolumeSnapshotDescription_Object = MibTableColumn
clusVolumeSnapshotDescription = _ClusVolumeSnapshotDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 4),
    _ClusVolumeSnapshotDescription_Type()
)
clusVolumeSnapshotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotDescription.setStatus("current")
_ClusVolumeSnapshotSize_Type = CounterBasedGauge64
_ClusVolumeSnapshotSize_Object = MibTableColumn
clusVolumeSnapshotSize = _ClusVolumeSnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 5),
    _ClusVolumeSnapshotSize_Type()
)
clusVolumeSnapshotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSize.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSize.setUnits("kB")
_ClusVolumeSnapshotSoftThreshold_Type = CounterBasedGauge64
_ClusVolumeSnapshotSoftThreshold_Object = MibTableColumn
clusVolumeSnapshotSoftThreshold = _ClusVolumeSnapshotSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 6),
    _ClusVolumeSnapshotSoftThreshold_Type()
)
clusVolumeSnapshotSoftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSoftThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSoftThreshold.setUnits("kB")
_ClusVolumeSnapshotHardThreshold_Type = CounterBasedGauge64
_ClusVolumeSnapshotHardThreshold_Object = MibTableColumn
clusVolumeSnapshotHardThreshold = _ClusVolumeSnapshotHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 7),
    _ClusVolumeSnapshotHardThreshold_Type()
)
clusVolumeSnapshotHardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotHardThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusVolumeSnapshotHardThreshold.setUnits("kB")
_ClusVolumeSnapshotACLCount_Type = Gauge32
_ClusVolumeSnapshotACLCount_Object = MibTableColumn
clusVolumeSnapshotACLCount = _ClusVolumeSnapshotACLCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 8),
    _ClusVolumeSnapshotACLCount_Type()
)
clusVolumeSnapshotACLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLCount.setStatus("current")
_ClusVolumeSnapshotScheduleName_Type = DisplayString
_ClusVolumeSnapshotScheduleName_Object = MibTableColumn
clusVolumeSnapshotScheduleName = _ClusVolumeSnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 10),
    _ClusVolumeSnapshotScheduleName_Type()
)
clusVolumeSnapshotScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotScheduleName.setStatus("current")
_ClusVolumeSnapshotIsSoftThresholdExceeded_Type = TruthValue
_ClusVolumeSnapshotIsSoftThresholdExceeded_Object = MibTableColumn
clusVolumeSnapshotIsSoftThresholdExceeded = _ClusVolumeSnapshotIsSoftThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 12),
    _ClusVolumeSnapshotIsSoftThresholdExceeded_Type()
)
clusVolumeSnapshotIsSoftThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsSoftThresholdExceeded.setStatus("deprecated")
_ClusVolumeSnapshotIsHardThresholdExceeded_Type = TruthValue
_ClusVolumeSnapshotIsHardThresholdExceeded_Object = MibTableColumn
clusVolumeSnapshotIsHardThresholdExceeded = _ClusVolumeSnapshotIsHardThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 13),
    _ClusVolumeSnapshotIsHardThresholdExceeded_Type()
)
clusVolumeSnapshotIsHardThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsHardThresholdExceeded.setStatus("deprecated")
_ClusVolumeSnapshotReplicationStatus_Type = ClusReplicationStatus
_ClusVolumeSnapshotReplicationStatus_Object = MibTableColumn
clusVolumeSnapshotReplicationStatus = _ClusVolumeSnapshotReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 14),
    _ClusVolumeSnapshotReplicationStatus_Type()
)
clusVolumeSnapshotReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotReplicationStatus.setStatus("current")


class _ClusVolumeSnapshotType_Type(Integer32):
    """Custom type clusVolumeSnapshotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("remote", 2))
    )


_ClusVolumeSnapshotType_Type.__name__ = "Integer32"
_ClusVolumeSnapshotType_Object = MibTableColumn
clusVolumeSnapshotType = _ClusVolumeSnapshotType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 15),
    _ClusVolumeSnapshotType_Type()
)
clusVolumeSnapshotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotType.setStatus("current")


class _ClusVolumeSnapshotCopyProgress_Type(Gauge32):
    """Custom type clusVolumeSnapshotCopyProgress based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClusVolumeSnapshotCopyProgress_Type.__name__ = "Gauge32"
_ClusVolumeSnapshotCopyProgress_Object = MibTableColumn
clusVolumeSnapshotCopyProgress = _ClusVolumeSnapshotCopyProgress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 16),
    _ClusVolumeSnapshotCopyProgress_Type()
)
clusVolumeSnapshotCopyProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCopyProgress.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCopyProgress.setUnits("%")
_ClusVolumeSnapshotAccessType_Type = DisplayString
_ClusVolumeSnapshotAccessType_Object = MibTableColumn
clusVolumeSnapshotAccessType = _ClusVolumeSnapshotAccessType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 18),
    _ClusVolumeSnapshotAccessType_Type()
)
clusVolumeSnapshotAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotAccessType.setStatus("obsolete")
_ClusVolumeSnapshotCreator_Type = ClusCreatorTypes
_ClusVolumeSnapshotCreator_Object = MibTableColumn
clusVolumeSnapshotCreator = _ClusVolumeSnapshotCreator_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 20),
    _ClusVolumeSnapshotCreator_Type()
)
clusVolumeSnapshotCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCreator.setStatus("current")
_ClusVolumeSnapshotIscsiIqn_Type = DisplayString
_ClusVolumeSnapshotIscsiIqn_Object = MibTableColumn
clusVolumeSnapshotIscsiIqn = _ClusVolumeSnapshotIscsiIqn_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 22),
    _ClusVolumeSnapshotIscsiIqn_Type()
)
clusVolumeSnapshotIscsiIqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIscsiIqn.setStatus("current")
_ClusVolumeSnapshotFriendlyName_Type = DisplayString
_ClusVolumeSnapshotFriendlyName_Object = MibTableColumn
clusVolumeSnapshotFriendlyName = _ClusVolumeSnapshotFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 24),
    _ClusVolumeSnapshotFriendlyName_Type()
)
clusVolumeSnapshotFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotFriendlyName.setStatus("deprecated")
_ClusVolumeSnapshotOriginalVolume_Type = DisplayString
_ClusVolumeSnapshotOriginalVolume_Object = MibTableColumn
clusVolumeSnapshotOriginalVolume = _ClusVolumeSnapshotOriginalVolume_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 25),
    _ClusVolumeSnapshotOriginalVolume_Type()
)
clusVolumeSnapshotOriginalVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotOriginalVolume.setStatus("current")
_ClusVolumeSnapshotOriginalMgmtGroup_Type = DisplayString
_ClusVolumeSnapshotOriginalMgmtGroup_Object = MibTableColumn
clusVolumeSnapshotOriginalMgmtGroup = _ClusVolumeSnapshotOriginalMgmtGroup_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 26),
    _ClusVolumeSnapshotOriginalMgmtGroup_Type()
)
clusVolumeSnapshotOriginalMgmtGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotOriginalMgmtGroup.setStatus("current")
_ClusVolumeSnapshotInitiatorCount_Type = Gauge32
_ClusVolumeSnapshotInitiatorCount_Object = MibTableColumn
clusVolumeSnapshotInitiatorCount = _ClusVolumeSnapshotInitiatorCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 27),
    _ClusVolumeSnapshotInitiatorCount_Type()
)
clusVolumeSnapshotInitiatorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorCount.setStatus("current")
_ClusVolumeSnapshotUsedSpace_Type = CounterBasedGauge64
_ClusVolumeSnapshotUsedSpace_Object = MibTableColumn
clusVolumeSnapshotUsedSpace = _ClusVolumeSnapshotUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 28),
    _ClusVolumeSnapshotUsedSpace_Type()
)
clusVolumeSnapshotUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotUsedSpace.setUnits("kB")
_ClusVolumeSnapshotWritableProvisionedSpace_Type = CounterBasedGauge64
_ClusVolumeSnapshotWritableProvisionedSpace_Object = MibTableColumn
clusVolumeSnapshotWritableProvisionedSpace = _ClusVolumeSnapshotWritableProvisionedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 29),
    _ClusVolumeSnapshotWritableProvisionedSpace_Type()
)
clusVolumeSnapshotWritableProvisionedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotWritableProvisionedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotWritableProvisionedSpace.setUnits("kB")
_ClusVolumeSnapshotClusterUsedPercent_Type = Gauge32
_ClusVolumeSnapshotClusterUsedPercent_Object = MibTableColumn
clusVolumeSnapshotClusterUsedPercent = _ClusVolumeSnapshotClusterUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 31),
    _ClusVolumeSnapshotClusterUsedPercent_Type()
)
clusVolumeSnapshotClusterUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotClusterUsedPercent.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotClusterUsedPercent.setUnits("%")
_ClusVolumeSnapshotProvisionedSpace_Type = CounterBasedGauge64
_ClusVolumeSnapshotProvisionedSpace_Object = MibTableColumn
clusVolumeSnapshotProvisionedSpace = _ClusVolumeSnapshotProvisionedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 32),
    _ClusVolumeSnapshotProvisionedSpace_Type()
)
clusVolumeSnapshotProvisionedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotProvisionedSpace.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotProvisionedSpace.setUnits("kB")
_ClusVolumeSnapshotStatsIOsRead_Type = Counter64
_ClusVolumeSnapshotStatsIOsRead_Object = MibTableColumn
clusVolumeSnapshotStatsIOsRead = _ClusVolumeSnapshotStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 36),
    _ClusVolumeSnapshotStatsIOsRead_Type()
)
clusVolumeSnapshotStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIOsRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIOsRead.setUnits("operations")
_ClusVolumeSnapshotStatsIOsWrite_Type = Counter64
_ClusVolumeSnapshotStatsIOsWrite_Object = MibTableColumn
clusVolumeSnapshotStatsIOsWrite = _ClusVolumeSnapshotStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 37),
    _ClusVolumeSnapshotStatsIOsWrite_Type()
)
clusVolumeSnapshotStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIOsWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIOsWrite.setUnits("operations")
_ClusVolumeSnapshotStatsBytesRead_Type = Counter64
_ClusVolumeSnapshotStatsBytesRead_Object = MibTableColumn
clusVolumeSnapshotStatsBytesRead = _ClusVolumeSnapshotStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 38),
    _ClusVolumeSnapshotStatsBytesRead_Type()
)
clusVolumeSnapshotStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsBytesRead.setUnits("B")
_ClusVolumeSnapshotStatsBytesWrite_Type = Counter64
_ClusVolumeSnapshotStatsBytesWrite_Object = MibTableColumn
clusVolumeSnapshotStatsBytesWrite = _ClusVolumeSnapshotStatsBytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 39),
    _ClusVolumeSnapshotStatsBytesWrite_Type()
)
clusVolumeSnapshotStatsBytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsBytesWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsBytesWrite.setUnits("B")
_ClusVolumeSnapshotStatsQDepthRead_Type = Gauge32
_ClusVolumeSnapshotStatsQDepthRead_Object = MibTableColumn
clusVolumeSnapshotStatsQDepthRead = _ClusVolumeSnapshotStatsQDepthRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 40),
    _ClusVolumeSnapshotStatsQDepthRead_Type()
)
clusVolumeSnapshotStatsQDepthRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsQDepthRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsQDepthRead.setUnits("operations")
_ClusVolumeSnapshotStatsQDepthWrite_Type = Gauge32
_ClusVolumeSnapshotStatsQDepthWrite_Object = MibTableColumn
clusVolumeSnapshotStatsQDepthWrite = _ClusVolumeSnapshotStatsQDepthWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 41),
    _ClusVolumeSnapshotStatsQDepthWrite_Type()
)
clusVolumeSnapshotStatsQDepthWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsQDepthWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsQDepthWrite.setUnits("operations")
_ClusVolumeSnapshotStatsIoLatencyRead_Type = Counter64
_ClusVolumeSnapshotStatsIoLatencyRead_Object = MibTableColumn
clusVolumeSnapshotStatsIoLatencyRead = _ClusVolumeSnapshotStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 42),
    _ClusVolumeSnapshotStatsIoLatencyRead_Type()
)
clusVolumeSnapshotStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIoLatencyRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIoLatencyRead.setUnits("ms")
_ClusVolumeSnapshotStatsIoLatencyWrite_Type = Counter64
_ClusVolumeSnapshotStatsIoLatencyWrite_Object = MibTableColumn
clusVolumeSnapshotStatsIoLatencyWrite = _ClusVolumeSnapshotStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 43),
    _ClusVolumeSnapshotStatsIoLatencyWrite_Type()
)
clusVolumeSnapshotStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIoLatencyWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsIoLatencyWrite.setUnits("ms")
_ClusVolumeSnapshotStatsCacheHits_Type = Counter64
_ClusVolumeSnapshotStatsCacheHits_Object = MibTableColumn
clusVolumeSnapshotStatsCacheHits = _ClusVolumeSnapshotStatsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 44),
    _ClusVolumeSnapshotStatsCacheHits_Type()
)
clusVolumeSnapshotStatsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsCacheHits.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotStatsCacheHits.setUnits("operations")
_ClusVolumeSnapshotIsDeleting_Type = TruthValue
_ClusVolumeSnapshotIsDeleting_Object = MibTableColumn
clusVolumeSnapshotIsDeleting = _ClusVolumeSnapshotIsDeleting_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 45),
    _ClusVolumeSnapshotIsDeleting_Type()
)
clusVolumeSnapshotIsDeleting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsDeleting.setStatus("current")
_ClusVolumeSnapshotIsAvailable_Type = TruthValue
_ClusVolumeSnapshotIsAvailable_Object = MibTableColumn
clusVolumeSnapshotIsAvailable = _ClusVolumeSnapshotIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 46),
    _ClusVolumeSnapshotIsAvailable_Type()
)
clusVolumeSnapshotIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsAvailable.setStatus("current")
_ClusVolumeSnapshotLunIsAvailable_Type = TruthValue
_ClusVolumeSnapshotLunIsAvailable_Object = MibTableColumn
clusVolumeSnapshotLunIsAvailable = _ClusVolumeSnapshotLunIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 47),
    _ClusVolumeSnapshotLunIsAvailable_Type()
)
clusVolumeSnapshotLunIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotLunIsAvailable.setStatus("current")
_ClusVolumeSnapshotReplicationState_Type = Integer32
_ClusVolumeSnapshotReplicationState_Object = MibTableColumn
clusVolumeSnapshotReplicationState = _ClusVolumeSnapshotReplicationState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 48),
    _ClusVolumeSnapshotReplicationState_Type()
)
clusVolumeSnapshotReplicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotReplicationState.setStatus("current")
_ClusVolumeSnapshotResyncPercent_Type = Gauge32
_ClusVolumeSnapshotResyncPercent_Object = MibTableColumn
clusVolumeSnapshotResyncPercent = _ClusVolumeSnapshotResyncPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 49),
    _ClusVolumeSnapshotResyncPercent_Type()
)
clusVolumeSnapshotResyncPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotResyncPercent.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotResyncPercent.setUnits("%")
_ClusVolumeSnapshotRestripePending_Type = TruthValue
_ClusVolumeSnapshotRestripePending_Object = MibTableColumn
clusVolumeSnapshotRestripePending = _ClusVolumeSnapshotRestripePending_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 50),
    _ClusVolumeSnapshotRestripePending_Type()
)
clusVolumeSnapshotRestripePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotRestripePending.setStatus("current")
_ClusVolumeSnapshotIsMigrating_Type = TruthValue
_ClusVolumeSnapshotIsMigrating_Object = MibTableColumn
clusVolumeSnapshotIsMigrating = _ClusVolumeSnapshotIsMigrating_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 51),
    _ClusVolumeSnapshotIsMigrating_Type()
)
clusVolumeSnapshotIsMigrating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsMigrating.setStatus("current")
_ClusVolumeSnapshotMigrationPercent_Type = Gauge32
_ClusVolumeSnapshotMigrationPercent_Object = MibTableColumn
clusVolumeSnapshotMigrationPercent = _ClusVolumeSnapshotMigrationPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 52),
    _ClusVolumeSnapshotMigrationPercent_Type()
)
clusVolumeSnapshotMigrationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotMigrationPercent.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotMigrationPercent.setUnits("%")
_ClusVolumeSnapshotRowStatus_Type = RowStatus
_ClusVolumeSnapshotRowStatus_Object = MibTableColumn
clusVolumeSnapshotRowStatus = _ClusVolumeSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 101, 1, 99),
    _ClusVolumeSnapshotRowStatus_Type()
)
clusVolumeSnapshotRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotRowStatus.setStatus("obsolete")
_ClusVolumeSnapshotACLTable_Object = MibTable
clusVolumeSnapshotACLTable = _ClusVolumeSnapshotACLTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 102)
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLTable.setStatus("current")
_ClusVolumeSnapshotACLEntry_Object = MibTableRow
clusVolumeSnapshotACLEntry = _ClusVolumeSnapshotACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 102, 1)
)
clusVolumeSnapshotACLEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotACLIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLEntry.setStatus("current")
_ClusVolumeSnapshotACLIndex_Type = Unsigned32
_ClusVolumeSnapshotACLIndex_Object = MibTableColumn
clusVolumeSnapshotACLIndex = _ClusVolumeSnapshotACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 102, 1, 1),
    _ClusVolumeSnapshotACLIndex_Type()
)
clusVolumeSnapshotACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLIndex.setStatus("current")
_ClusVolumeSnapshotACLServer_Type = DisplayString
_ClusVolumeSnapshotACLServer_Object = MibTableColumn
clusVolumeSnapshotACLServer = _ClusVolumeSnapshotACLServer_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 102, 1, 2),
    _ClusVolumeSnapshotACLServer_Type()
)
clusVolumeSnapshotACLServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLServer.setStatus("current")
_ClusVolumeSnapshotACLPermissions_Type = ClusPermissionBits
_ClusVolumeSnapshotACLPermissions_Object = MibTableColumn
clusVolumeSnapshotACLPermissions = _ClusVolumeSnapshotACLPermissions_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 102, 1, 3),
    _ClusVolumeSnapshotACLPermissions_Type()
)
clusVolumeSnapshotACLPermissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLPermissions.setStatus("current")
_ClusVolumeSnapshotACLRowStatus_Type = RowStatus
_ClusVolumeSnapshotACLRowStatus_Object = MibTableColumn
clusVolumeSnapshotACLRowStatus = _ClusVolumeSnapshotACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 102, 1, 6),
    _ClusVolumeSnapshotACLRowStatus_Type()
)
clusVolumeSnapshotACLRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLRowStatus.setStatus("obsolete")
_ClusVolumeSnapshotInitiatorTable_Object = MibTable
clusVolumeSnapshotInitiatorTable = _ClusVolumeSnapshotInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103)
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorTable.setStatus("current")
_ClusVolumeSnapshotInitiatorEntry_Object = MibTableRow
clusVolumeSnapshotInitiatorEntry = _ClusVolumeSnapshotInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1)
)
clusVolumeSnapshotInitiatorEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorEntry.setStatus("current")
_ClusVolumeSnapshotInitiatorIndex_Type = Unsigned32
_ClusVolumeSnapshotInitiatorIndex_Object = MibTableColumn
clusVolumeSnapshotInitiatorIndex = _ClusVolumeSnapshotInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 1),
    _ClusVolumeSnapshotInitiatorIndex_Type()
)
clusVolumeSnapshotInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorIndex.setStatus("current")
_ClusVolumeSnapshotInitiatorIqn_Type = DisplayString
_ClusVolumeSnapshotInitiatorIqn_Object = MibTableColumn
clusVolumeSnapshotInitiatorIqn = _ClusVolumeSnapshotInitiatorIqn_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 2),
    _ClusVolumeSnapshotInitiatorIqn_Type()
)
clusVolumeSnapshotInitiatorIqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorIqn.setStatus("current")
_ClusVolumeSnapshotInitiatorAddress_Type = IpAddress
_ClusVolumeSnapshotInitiatorAddress_Object = MibTableColumn
clusVolumeSnapshotInitiatorAddress = _ClusVolumeSnapshotInitiatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 3),
    _ClusVolumeSnapshotInitiatorAddress_Type()
)
clusVolumeSnapshotInitiatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorAddress.setStatus("current")
_ClusVolumeSnapshotInitiatorPort_Type = Unsigned32
_ClusVolumeSnapshotInitiatorPort_Object = MibTableColumn
clusVolumeSnapshotInitiatorPort = _ClusVolumeSnapshotInitiatorPort_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 4),
    _ClusVolumeSnapshotInitiatorPort_Type()
)
clusVolumeSnapshotInitiatorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorPort.setStatus("current")
_ClusVolumeSnapshotInitiatorStatus_Type = DisplayString
_ClusVolumeSnapshotInitiatorStatus_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatus = _ClusVolumeSnapshotInitiatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 5),
    _ClusVolumeSnapshotInitiatorStatus_Type()
)
clusVolumeSnapshotInitiatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatus.setStatus("current")
_ClusVolumeSnapshotInitiatorStatsIOsRead_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsIOsRead_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsIOsRead = _ClusVolumeSnapshotInitiatorStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 6),
    _ClusVolumeSnapshotInitiatorStatsIOsRead_Type()
)
clusVolumeSnapshotInitiatorStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIOsRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIOsRead.setUnits("operations")
_ClusVolumeSnapshotInitiatorStatsIOsWrite_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsIOsWrite_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsIOsWrite = _ClusVolumeSnapshotInitiatorStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 7),
    _ClusVolumeSnapshotInitiatorStatsIOsWrite_Type()
)
clusVolumeSnapshotInitiatorStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIOsWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIOsWrite.setUnits("operations")
_ClusVolumeSnapshotInitiatorStatsBytesRead_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsBytesRead_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsBytesRead = _ClusVolumeSnapshotInitiatorStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 8),
    _ClusVolumeSnapshotInitiatorStatsBytesRead_Type()
)
clusVolumeSnapshotInitiatorStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsBytesRead.setUnits("B")
_ClusVolumeSnapshotInitiatorStatsBytesWrite_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsBytesWrite_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsBytesWrite = _ClusVolumeSnapshotInitiatorStatsBytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 9),
    _ClusVolumeSnapshotInitiatorStatsBytesWrite_Type()
)
clusVolumeSnapshotInitiatorStatsBytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsBytesWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsBytesWrite.setUnits("B")
_ClusVolumeSnapshotInitiatorStatsQDepthRead_Type = Gauge32
_ClusVolumeSnapshotInitiatorStatsQDepthRead_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsQDepthRead = _ClusVolumeSnapshotInitiatorStatsQDepthRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 10),
    _ClusVolumeSnapshotInitiatorStatsQDepthRead_Type()
)
clusVolumeSnapshotInitiatorStatsQDepthRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsQDepthRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsQDepthRead.setUnits("operations")
_ClusVolumeSnapshotInitiatorStatsQDepthWrite_Type = Gauge32
_ClusVolumeSnapshotInitiatorStatsQDepthWrite_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsQDepthWrite = _ClusVolumeSnapshotInitiatorStatsQDepthWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 11),
    _ClusVolumeSnapshotInitiatorStatsQDepthWrite_Type()
)
clusVolumeSnapshotInitiatorStatsQDepthWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsQDepthWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsQDepthWrite.setUnits("operations")
_ClusVolumeSnapshotInitiatorStatsIoLatencyRead_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsIoLatencyRead_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsIoLatencyRead = _ClusVolumeSnapshotInitiatorStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 12),
    _ClusVolumeSnapshotInitiatorStatsIoLatencyRead_Type()
)
clusVolumeSnapshotInitiatorStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIoLatencyRead.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIoLatencyRead.setUnits("ms")
_ClusVolumeSnapshotInitiatorStatsIoLatencyWrite_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsIoLatencyWrite_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsIoLatencyWrite = _ClusVolumeSnapshotInitiatorStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 13),
    _ClusVolumeSnapshotInitiatorStatsIoLatencyWrite_Type()
)
clusVolumeSnapshotInitiatorStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIoLatencyWrite.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsIoLatencyWrite.setUnits("ms")
_ClusVolumeSnapshotInitiatorStatsCacheHits_Type = Counter64
_ClusVolumeSnapshotInitiatorStatsCacheHits_Object = MibTableColumn
clusVolumeSnapshotInitiatorStatsCacheHits = _ClusVolumeSnapshotInitiatorStatsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 14),
    _ClusVolumeSnapshotInitiatorStatsCacheHits_Type()
)
clusVolumeSnapshotInitiatorStatsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsCacheHits.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorStatsCacheHits.setUnits("operations")
_ClusVolumeSnapshotInitiatorState_Type = DisplayString
_ClusVolumeSnapshotInitiatorState_Object = MibTableColumn
clusVolumeSnapshotInitiatorState = _ClusVolumeSnapshotInitiatorState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 15),
    _ClusVolumeSnapshotInitiatorState_Type()
)
clusVolumeSnapshotInitiatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorState.setStatus("current")
_ClusVolumeSnapshotInitiatorRowStatus_Type = RowStatus
_ClusVolumeSnapshotInitiatorRowStatus_Object = MibTableColumn
clusVolumeSnapshotInitiatorRowStatus = _ClusVolumeSnapshotInitiatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 103, 1, 99),
    _ClusVolumeSnapshotInitiatorRowStatus_Type()
)
clusVolumeSnapshotInitiatorRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotInitiatorRowStatus.setStatus("obsolete")
_ClusServerCount_Type = Integer32
_ClusServerCount_Object = MibScalar
clusServerCount = _ClusServerCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 104),
    _ClusServerCount_Type()
)
clusServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerCount.setStatus("current")
_ClusServerTable_Object = MibTable
clusServerTable = _ClusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105)
)
if mibBuilder.loadTexts:
    clusServerTable.setStatus("current")
_ClusServerEntry_Object = MibTableRow
clusServerEntry = _ClusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1)
)
clusServerEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIndex"),
)
if mibBuilder.loadTexts:
    clusServerEntry.setStatus("current")
_ClusServerIndex_Type = Unsigned32
_ClusServerIndex_Object = MibTableColumn
clusServerIndex = _ClusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 1),
    _ClusServerIndex_Type()
)
clusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusServerIndex.setStatus("current")
_ClusServerName_Type = DisplayString
_ClusServerName_Object = MibTableColumn
clusServerName = _ClusServerName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 2),
    _ClusServerName_Type()
)
clusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerName.setStatus("current")
_ClusServerDescription_Type = DisplayString
_ClusServerDescription_Object = MibTableColumn
clusServerDescription = _ClusServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 3),
    _ClusServerDescription_Type()
)
clusServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerDescription.setStatus("current")
_ClusServerIscsiEnabled_Type = TruthValue
_ClusServerIscsiEnabled_Object = MibTableColumn
clusServerIscsiEnabled = _ClusServerIscsiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 22),
    _ClusServerIscsiEnabled_Type()
)
clusServerIscsiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerIscsiEnabled.setStatus("current")
_ClusServerIscsiChapAuthRequired_Type = TruthValue
_ClusServerIscsiChapAuthRequired_Object = MibTableColumn
clusServerIscsiChapAuthRequired = _ClusServerIscsiChapAuthRequired_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 23),
    _ClusServerIscsiChapAuthRequired_Type()
)
clusServerIscsiChapAuthRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerIscsiChapAuthRequired.setStatus("current")
_ClusServerIscsiInitiatorCount_Type = Gauge32
_ClusServerIscsiInitiatorCount_Object = MibTableColumn
clusServerIscsiInitiatorCount = _ClusServerIscsiInitiatorCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 25),
    _ClusServerIscsiInitiatorCount_Type()
)
clusServerIscsiInitiatorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorCount.setStatus("current")
_ClusServerVolumeACLCount_Type = Gauge32
_ClusServerVolumeACLCount_Object = MibTableColumn
clusServerVolumeACLCount = _ClusServerVolumeACLCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 30),
    _ClusServerVolumeACLCount_Type()
)
clusServerVolumeACLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerVolumeACLCount.setStatus("current")
_ClusServerRowStatus_Type = RowStatus
_ClusServerRowStatus_Object = MibTableColumn
clusServerRowStatus = _ClusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 105, 1, 99),
    _ClusServerRowStatus_Type()
)
clusServerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerRowStatus.setStatus("obsolete")
_ClusServerSubnetTable_Object = MibTable
clusServerSubnetTable = _ClusServerSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 106)
)
if mibBuilder.loadTexts:
    clusServerSubnetTable.setStatus("current")
_ClusServerSubnetEntry_Object = MibTableRow
clusServerSubnetEntry = _ClusServerSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 106, 1)
)
clusServerSubnetEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerSubnetIndex"),
)
if mibBuilder.loadTexts:
    clusServerSubnetEntry.setStatus("current")
_ClusServerSubnetIndex_Type = Unsigned32
_ClusServerSubnetIndex_Object = MibTableColumn
clusServerSubnetIndex = _ClusServerSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 106, 1, 1),
    _ClusServerSubnetIndex_Type()
)
clusServerSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusServerSubnetIndex.setStatus("current")
_ClusServerSubnetAddress_Type = IpAddress
_ClusServerSubnetAddress_Object = MibTableColumn
clusServerSubnetAddress = _ClusServerSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 106, 1, 2),
    _ClusServerSubnetAddress_Type()
)
clusServerSubnetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerSubnetAddress.setStatus("deprecated")
_ClusServerSubnetMask_Type = IpAddress
_ClusServerSubnetMask_Object = MibTableColumn
clusServerSubnetMask = _ClusServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 106, 1, 3),
    _ClusServerSubnetMask_Type()
)
clusServerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerSubnetMask.setStatus("deprecated")
_ClusServerSubnetRowStatus_Type = RowStatus
_ClusServerSubnetRowStatus_Object = MibTableColumn
clusServerSubnetRowStatus = _ClusServerSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 106, 1, 4),
    _ClusServerSubnetRowStatus_Type()
)
clusServerSubnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerSubnetRowStatus.setStatus("obsolete")
_ClusServerIscsiInitiatorTable_Object = MibTable
clusServerIscsiInitiatorTable = _ClusServerIscsiInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 107)
)
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorTable.setStatus("current")
_ClusServerIscsiInitiatorEntry_Object = MibTableRow
clusServerIscsiInitiatorEntry = _ClusServerIscsiInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 107, 1)
)
clusServerIscsiInitiatorEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiInitiatorIndex"),
)
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorEntry.setStatus("current")
_ClusServerIscsiInitiatorIndex_Type = Unsigned32
_ClusServerIscsiInitiatorIndex_Object = MibTableColumn
clusServerIscsiInitiatorIndex = _ClusServerIscsiInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 107, 1, 1),
    _ClusServerIscsiInitiatorIndex_Type()
)
clusServerIscsiInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorIndex.setStatus("current")
_ClusServerIscsiInitiatorIqn_Type = DisplayString
_ClusServerIscsiInitiatorIqn_Object = MibTableColumn
clusServerIscsiInitiatorIqn = _ClusServerIscsiInitiatorIqn_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 107, 1, 5),
    _ClusServerIscsiInitiatorIqn_Type()
)
clusServerIscsiInitiatorIqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorIqn.setStatus("current")
_ClusServerIscsiInitiatorChapName_Type = DisplayString
_ClusServerIscsiInitiatorChapName_Object = MibTableColumn
clusServerIscsiInitiatorChapName = _ClusServerIscsiInitiatorChapName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 107, 1, 6),
    _ClusServerIscsiInitiatorChapName_Type()
)
clusServerIscsiInitiatorChapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorChapName.setStatus("current")
_ClusServerIscsiInitiatorRowStatus_Type = RowStatus
_ClusServerIscsiInitiatorRowStatus_Object = MibTableColumn
clusServerIscsiInitiatorRowStatus = _ClusServerIscsiInitiatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 107, 1, 7),
    _ClusServerIscsiInitiatorRowStatus_Type()
)
clusServerIscsiInitiatorRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerIscsiInitiatorRowStatus.setStatus("obsolete")


class _ClusCommunicationMode_Type(Integer32):
    """Custom type clusCommunicationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2),
          ("multicastAndUnicast", 3))
    )


_ClusCommunicationMode_Type.__name__ = "Integer32"
_ClusCommunicationMode_Object = MibScalar
clusCommunicationMode = _ClusCommunicationMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 109),
    _ClusCommunicationMode_Type()
)
clusCommunicationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusCommunicationMode.setStatus("current")
_ClusUnicastHostCount_Type = Integer32
_ClusUnicastHostCount_Object = MibScalar
clusUnicastHostCount = _ClusUnicastHostCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 110),
    _ClusUnicastHostCount_Type()
)
clusUnicastHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusUnicastHostCount.setStatus("current")
_ClusUnicastHostTable_Object = MibTable
clusUnicastHostTable = _ClusUnicastHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 111)
)
if mibBuilder.loadTexts:
    clusUnicastHostTable.setStatus("current")
_ClusUnicastHostEntry_Object = MibTableRow
clusUnicastHostEntry = _ClusUnicastHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 111, 1)
)
clusUnicastHostEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusUnicastHostIndex"),
)
if mibBuilder.loadTexts:
    clusUnicastHostEntry.setStatus("current")
_ClusUnicastHostIndex_Type = Unsigned32
_ClusUnicastHostIndex_Object = MibTableColumn
clusUnicastHostIndex = _ClusUnicastHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 111, 1, 1),
    _ClusUnicastHostIndex_Type()
)
clusUnicastHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusUnicastHostIndex.setStatus("current")
_ClusUnicastHostName_Type = DisplayString
_ClusUnicastHostName_Object = MibTableColumn
clusUnicastHostName = _ClusUnicastHostName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 111, 1, 2),
    _ClusUnicastHostName_Type()
)
clusUnicastHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusUnicastHostName.setStatus("current")
_ClusUnicastHostRowStatus_Type = RowStatus
_ClusUnicastHostRowStatus_Object = MibTableColumn
clusUnicastHostRowStatus = _ClusUnicastHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 111, 1, 3),
    _ClusUnicastHostRowStatus_Type()
)
clusUnicastHostRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusUnicastHostRowStatus.setStatus("obsolete")
_ClusSnapshotScheduleCount_Type = Integer32
_ClusSnapshotScheduleCount_Object = MibScalar
clusSnapshotScheduleCount = _ClusSnapshotScheduleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 112),
    _ClusSnapshotScheduleCount_Type()
)
clusSnapshotScheduleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleCount.setStatus("current")
_ClusSnapshotScheduleTable_Object = MibTable
clusSnapshotScheduleTable = _ClusSnapshotScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113)
)
if mibBuilder.loadTexts:
    clusSnapshotScheduleTable.setStatus("current")
_ClusSnapshotScheduleEntry_Object = MibTableRow
clusSnapshotScheduleEntry = _ClusSnapshotScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1)
)
clusSnapshotScheduleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleIndex"),
)
if mibBuilder.loadTexts:
    clusSnapshotScheduleEntry.setStatus("current")
_ClusSnapshotScheduleIndex_Type = Unsigned32
_ClusSnapshotScheduleIndex_Object = MibTableColumn
clusSnapshotScheduleIndex = _ClusSnapshotScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 1),
    _ClusSnapshotScheduleIndex_Type()
)
clusSnapshotScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusSnapshotScheduleIndex.setStatus("current")
_ClusSnapshotScheduleName_Type = DisplayString
_ClusSnapshotScheduleName_Object = MibTableColumn
clusSnapshotScheduleName = _ClusSnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 2),
    _ClusSnapshotScheduleName_Type()
)
clusSnapshotScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleName.setStatus("current")
_ClusSnapshotScheduleDescription_Type = DisplayString
_ClusSnapshotScheduleDescription_Object = MibTableColumn
clusSnapshotScheduleDescription = _ClusSnapshotScheduleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 3),
    _ClusSnapshotScheduleDescription_Type()
)
clusSnapshotScheduleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleDescription.setStatus("current")
_ClusSnapshotScheduleSoftThreshold_Type = CounterBasedGauge64
_ClusSnapshotScheduleSoftThreshold_Object = MibTableColumn
clusSnapshotScheduleSoftThreshold = _ClusSnapshotScheduleSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 4),
    _ClusSnapshotScheduleSoftThreshold_Type()
)
clusSnapshotScheduleSoftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleSoftThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusSnapshotScheduleSoftThreshold.setUnits("kB")
_ClusSnapshotScheduleHardThreshold_Type = CounterBasedGauge64
_ClusSnapshotScheduleHardThreshold_Object = MibTableColumn
clusSnapshotScheduleHardThreshold = _ClusSnapshotScheduleHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 5),
    _ClusSnapshotScheduleHardThreshold_Type()
)
clusSnapshotScheduleHardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleHardThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clusSnapshotScheduleHardThreshold.setUnits("kB")
_ClusSnapshotScheduleFirstCreationTime_Type = DateAndTime
_ClusSnapshotScheduleFirstCreationTime_Object = MibTableColumn
clusSnapshotScheduleFirstCreationTime = _ClusSnapshotScheduleFirstCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 6),
    _ClusSnapshotScheduleFirstCreationTime_Type()
)
clusSnapshotScheduleFirstCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFirstCreationTime.setStatus("current")
_ClusSnapshotScheduleFrequency_Type = Gauge32
_ClusSnapshotScheduleFrequency_Object = MibTableColumn
clusSnapshotScheduleFrequency = _ClusSnapshotScheduleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 7),
    _ClusSnapshotScheduleFrequency_Type()
)
clusSnapshotScheduleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFrequency.setStatus("current")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFrequency.setUnits("seconds")
_ClusSnapshotScheduleVolumeName_Type = DisplayString
_ClusSnapshotScheduleVolumeName_Object = MibTableColumn
clusSnapshotScheduleVolumeName = _ClusSnapshotScheduleVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 8),
    _ClusSnapshotScheduleVolumeName_Type()
)
clusSnapshotScheduleVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleVolumeName.setStatus("current")


class _ClusSnapshotScheduleRetainType_Type(Integer32):
    """Custom type clusSnapshotScheduleRetainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byTime", 1),
          ("byNumber", 2))
    )


_ClusSnapshotScheduleRetainType_Type.__name__ = "Integer32"
_ClusSnapshotScheduleRetainType_Object = MibTableColumn
clusSnapshotScheduleRetainType = _ClusSnapshotScheduleRetainType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 9),
    _ClusSnapshotScheduleRetainType_Type()
)
clusSnapshotScheduleRetainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainType.setStatus("current")
_ClusSnapshotScheduleRetainCount_Type = Gauge32
_ClusSnapshotScheduleRetainCount_Object = MibTableColumn
clusSnapshotScheduleRetainCount = _ClusSnapshotScheduleRetainCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 10),
    _ClusSnapshotScheduleRetainCount_Type()
)
clusSnapshotScheduleRetainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainCount.setStatus("current")
_ClusSnapshotScheduleRetainTime_Type = Gauge32
_ClusSnapshotScheduleRetainTime_Object = MibTableColumn
clusSnapshotScheduleRetainTime = _ClusSnapshotScheduleRetainTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 11),
    _ClusSnapshotScheduleRetainTime_Type()
)
clusSnapshotScheduleRetainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainTime.setStatus("current")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainTime.setUnits("seconds")


class _ClusSnapshotScheduleType_Type(Integer32):
    """Custom type clusSnapshotScheduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("primary", 2),
          ("remote", 3))
    )


_ClusSnapshotScheduleType_Type.__name__ = "Integer32"
_ClusSnapshotScheduleType_Object = MibTableColumn
clusSnapshotScheduleType = _ClusSnapshotScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 13),
    _ClusSnapshotScheduleType_Type()
)
clusSnapshotScheduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleType.setStatus("current")
_ClusSnapshotScheduleFailureMessage_Type = DisplayString
_ClusSnapshotScheduleFailureMessage_Object = MibTableColumn
clusSnapshotScheduleFailureMessage = _ClusSnapshotScheduleFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 14),
    _ClusSnapshotScheduleFailureMessage_Type()
)
clusSnapshotScheduleFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFailureMessage.setStatus("current")
_ClusSnapshotScheduleRowStatus_Type = RowStatus
_ClusSnapshotScheduleRowStatus_Object = MibTableColumn
clusSnapshotScheduleRowStatus = _ClusSnapshotScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 113, 1, 15),
    _ClusSnapshotScheduleRowStatus_Type()
)
clusSnapshotScheduleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRowStatus.setStatus("obsolete")
_ClusMgmtGroupSiteCount_Type = Integer32
_ClusMgmtGroupSiteCount_Object = MibScalar
clusMgmtGroupSiteCount = _ClusMgmtGroupSiteCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 118),
    _ClusMgmtGroupSiteCount_Type()
)
clusMgmtGroupSiteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupSiteCount.setStatus("current")
_ClusSiteTable_Object = MibTable
clusSiteTable = _ClusSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119)
)
if mibBuilder.loadTexts:
    clusSiteTable.setStatus("current")
_ClusSiteEntry_Object = MibTableRow
clusSiteEntry = _ClusSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1)
)
clusSiteEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteIndex"),
)
if mibBuilder.loadTexts:
    clusSiteEntry.setStatus("current")
_ClusSiteIndex_Type = Unsigned32
_ClusSiteIndex_Object = MibTableColumn
clusSiteIndex = _ClusSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 1),
    _ClusSiteIndex_Type()
)
clusSiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusSiteIndex.setStatus("current")
_ClusSiteName_Type = DisplayString
_ClusSiteName_Object = MibTableColumn
clusSiteName = _ClusSiteName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 2),
    _ClusSiteName_Type()
)
clusSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteName.setStatus("current")
_ClusSiteDescription_Type = DisplayString
_ClusSiteDescription_Object = MibTableColumn
clusSiteDescription = _ClusSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 3),
    _ClusSiteDescription_Type()
)
clusSiteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteDescription.setStatus("current")
_ClusSiteIsPrimary_Type = TruthValue
_ClusSiteIsPrimary_Object = MibTableColumn
clusSiteIsPrimary = _ClusSiteIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 4),
    _ClusSiteIsPrimary_Type()
)
clusSiteIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteIsPrimary.setStatus("current")
_ClusSiteFailoverManager_Type = DisplayString
_ClusSiteFailoverManager_Object = MibTableColumn
clusSiteFailoverManager = _ClusSiteFailoverManager_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 5),
    _ClusSiteFailoverManager_Type()
)
clusSiteFailoverManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteFailoverManager.setStatus("current")
_ClusSiteModuleCount_Type = Gauge32
_ClusSiteModuleCount_Object = MibTableColumn
clusSiteModuleCount = _ClusSiteModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 6),
    _ClusSiteModuleCount_Type()
)
clusSiteModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteModuleCount.setStatus("current")
_ClusSiteRowStatus_Type = RowStatus
_ClusSiteRowStatus_Object = MibTableColumn
clusSiteRowStatus = _ClusSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 119, 1, 7),
    _ClusSiteRowStatus_Type()
)
clusSiteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteRowStatus.setStatus("obsolete")
_ClusSiteModuleTable_Object = MibTable
clusSiteModuleTable = _ClusSiteModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 120)
)
if mibBuilder.loadTexts:
    clusSiteModuleTable.setStatus("current")
_ClusSiteModuleEntry_Object = MibTableRow
clusSiteModuleEntry = _ClusSiteModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 120, 1)
)
clusSiteModuleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteModuleIndex"),
)
if mibBuilder.loadTexts:
    clusSiteModuleEntry.setStatus("current")
_ClusSiteModuleIndex_Type = Unsigned32
_ClusSiteModuleIndex_Object = MibTableColumn
clusSiteModuleIndex = _ClusSiteModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 120, 1, 1),
    _ClusSiteModuleIndex_Type()
)
clusSiteModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusSiteModuleIndex.setStatus("current")
_ClusSiteModuleName_Type = DisplayString
_ClusSiteModuleName_Object = MibTableColumn
clusSiteModuleName = _ClusSiteModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 120, 1, 2),
    _ClusSiteModuleName_Type()
)
clusSiteModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteModuleName.setStatus("current")
_ClusSiteModuleRowStatus_Type = RowStatus
_ClusSiteModuleRowStatus_Object = MibTableColumn
clusSiteModuleRowStatus = _ClusSiteModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 120, 1, 3),
    _ClusSiteModuleRowStatus_Type()
)
clusSiteModuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSiteModuleRowStatus.setStatus("obsolete")
_ClusServerVolumeACLTable_Object = MibTable
clusServerVolumeACLTable = _ClusServerVolumeACLTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 121)
)
if mibBuilder.loadTexts:
    clusServerVolumeACLTable.setStatus("current")
_ClusServerVolumeACLEntry_Object = MibTableRow
clusServerVolumeACLEntry = _ClusServerVolumeACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 121, 1)
)
clusServerVolumeACLEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerVolumeACLIndex"),
)
if mibBuilder.loadTexts:
    clusServerVolumeACLEntry.setStatus("current")
_ClusServerVolumeACLIndex_Type = Unsigned32
_ClusServerVolumeACLIndex_Object = MibTableColumn
clusServerVolumeACLIndex = _ClusServerVolumeACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 121, 1, 1),
    _ClusServerVolumeACLIndex_Type()
)
clusServerVolumeACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusServerVolumeACLIndex.setStatus("current")
_ClusServerVolumeACLVolume_Type = DisplayString
_ClusServerVolumeACLVolume_Object = MibTableColumn
clusServerVolumeACLVolume = _ClusServerVolumeACLVolume_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 121, 1, 2),
    _ClusServerVolumeACLVolume_Type()
)
clusServerVolumeACLVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerVolumeACLVolume.setStatus("current")
_ClusServerVolumeACLPermissions_Type = ClusPermissionBits
_ClusServerVolumeACLPermissions_Object = MibTableColumn
clusServerVolumeACLPermissions = _ClusServerVolumeACLPermissions_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 121, 1, 3),
    _ClusServerVolumeACLPermissions_Type()
)
clusServerVolumeACLPermissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerVolumeACLPermissions.setStatus("current")
_ClusServerVolumeACLRowStatus_Type = RowStatus
_ClusServerVolumeACLRowStatus_Object = MibTableColumn
clusServerVolumeACLRowStatus = _ClusServerVolumeACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 121, 1, 5),
    _ClusServerVolumeACLRowStatus_Type()
)
clusServerVolumeACLRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusServerVolumeACLRowStatus.setStatus("obsolete")

# Managed Objects groups

lefthandNetworksNsmClusteringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12, 1, 2, 1)
)
lefthandNetworksNsmClusteringGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupIsEnabled"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupQuorum"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupActiveManagerCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupManagerCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupLicenseTimeRemaining"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusCommunicationMode"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusUnicastHostCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupSiteCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerVersion"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerHostSerialNo"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerIsVirtual"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerIsFailover"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleVersion"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleSerialNo"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleUsableSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleAvailableSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleIsManager"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleRaidConfiguration"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStorageState"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStorageStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStorageIsReady"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleCreationTime"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleClusterName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleEnabledFeatures"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleFeatureKey"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStorageCondition"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsStoreLatencyTotal"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleProvisionedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleUsedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterModuleCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterVolumeCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISNSCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPEnabled"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterAvailableSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsBytesRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsBytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsQDepthRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsQDepthWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterStatsCacheHits"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterTotalSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterProvisionedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterUsedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterUtilization"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterModuleName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterModuleSerialNo"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISNSHost"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPAddress"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPMask"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeCreationTime"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSize"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeReplicaCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeACLCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeClusterName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeReplicationStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsRemoteSnapshot"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeRemoteSnapshotFailureMessage"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeMinimumReplication"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeCreator"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIscsiIqn"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeUsedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeClusterUsedPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeProvisionedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsThinProvisioned"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsBytesRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsBytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsQDepthRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsQDepthWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeStatsCacheHits"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeAutoGrowSecondsDefault"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeAutoGrowSeconds"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeType"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeDataProtectionLevel"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumePBNRStripes"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumePBNRParity"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeAvailableSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeUsedPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsFull"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsDeleting"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsAvailable"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeLunIsAvailable"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeReplicationState"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeResyncPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeRestripePending"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsMigrating"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeMigrationPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeACLServer"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeACLPermissions"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorIqn"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorAddress"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorPort"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsBytesRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsBytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsQDepthRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsQDepthWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorStatsCacheHits"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorState"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterVolumeName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotCreationTime"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotSize"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotACLCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotScheduleName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotReplicationStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotType"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotCopyProgress"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotCreator"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIscsiIqn"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotFriendlyName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotOriginalVolume"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotOriginalMgmtGroup"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotUsedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotWritableProvisionedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotClusterUsedPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotProvisionedSpace"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsBytesRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsBytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsQDepthRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsQDepthWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotStatsCacheHits"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIsDeleting"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIsAvailable"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotLunIsAvailable"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotReplicationState"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotResyncPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotRestripePending"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIsMigrating"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotMigrationPercent"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotACLServer"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotACLPermissions"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorIqn"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorAddress"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorPort"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsBytesRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsBytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsQDepthRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsQDepthWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorStatsCacheHits"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorState"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusUnicastHostName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleFirstCreationTime"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleFrequency"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleVolumeName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleRetainType"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleRetainCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleRetainTime"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleType"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleFailureMessage"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteIsPrimary"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteFailoverManager"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteModuleCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteModuleName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiEnabled"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiChapAuthRequired"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiInitiatorCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerVolumeACLCount"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiInitiatorIqn"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiInitiatorChapName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerVolumeACLVolume"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerVolumeACLPermissions"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmClusteringGroup.setStatus("current")

lefthandNetworksNsmClusteringGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12, 1, 2, 2)
)
lefthandNetworksNsmClusteringGroupObsolete.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusMgmtGroupDescription"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterHotSpareTimeout"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterModuleIsHotSpare"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeAutoGrowPages"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSoftThreshold"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeHardThreshold"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsSoftThresholdExceeded"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeIsHardThresholdExceeded"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeFriendlyName"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleSoftThreshold"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleHardThreshold"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotSoftThreshold"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotHardThreshold"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIsSoftThresholdExceeded"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotIsHardThresholdExceeded"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusManagerRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsKbytesRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsKbytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsQDepthTotal"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusModuleRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterModuleRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISNSRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPRoute"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterISCSIVirtualIPRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeACLRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeInitiatorRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusClusterVolumeRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotACLRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotInitiatorRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusUnicastHostRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSnapshotScheduleRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusSiteModuleRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerSubnetAddress"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerSubnetMask"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerSubnetRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerIscsiInitiatorRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusServerVolumeACLRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeAccessType"),
        ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "clusVolumeSnapshotAccessType"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmClusteringGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmClusteringMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 12, 1, 1, 1)
)
lefthandNetworksNsmClusteringMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB", "lefthandNetworksNsmClusteringGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmClusteringMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-CLUSTERING-MIB",
    **{"ClusPermissionBits": ClusPermissionBits,
       "ClusFeatureBits": ClusFeatureBits,
       "ClusCreatorTypes": ClusCreatorTypes,
       "ClusReplicationStatus": ClusReplicationStatus,
       "lhnNsmClusteringModule": lhnNsmClusteringModule,
       "lhnNsmClusteringModuleConformance": lhnNsmClusteringModuleConformance,
       "lhnNsmClusteringModuleCompliances": lhnNsmClusteringModuleCompliances,
       "lefthandNetworksNsmClusteringMibCompliance": lefthandNetworksNsmClusteringMibCompliance,
       "lhnNsmClusteringModuleGroups": lhnNsmClusteringModuleGroups,
       "lefthandNetworksNsmClusteringGroup": lefthandNetworksNsmClusteringGroup,
       "lefthandNetworksNsmClusteringGroupObsolete": lefthandNetworksNsmClusteringGroupObsolete,
       "clusMgmtGroupName": clusMgmtGroupName,
       "clusMgmtGroupIsEnabled": clusMgmtGroupIsEnabled,
       "clusMgmtGroupQuorum": clusMgmtGroupQuorum,
       "clusMgmtGroupDescription": clusMgmtGroupDescription,
       "clusMgmtGroupActiveManagerCount": clusMgmtGroupActiveManagerCount,
       "clusMgmtGroupManagerCount": clusMgmtGroupManagerCount,
       "clusMgmtGroupLicenseTimeRemaining": clusMgmtGroupLicenseTimeRemaining,
       "clusManagerTable": clusManagerTable,
       "clusManagerEntry": clusManagerEntry,
       "clusManagerIndex": clusManagerIndex,
       "clusManagerName": clusManagerName,
       "clusManagerVersion": clusManagerVersion,
       "clusManagerHostSerialNo": clusManagerHostSerialNo,
       "clusManagerStatus": clusManagerStatus,
       "clusManagerIsVirtual": clusManagerIsVirtual,
       "clusManagerIsFailover": clusManagerIsFailover,
       "clusManagerRowStatus": clusManagerRowStatus,
       "clusModuleCount": clusModuleCount,
       "clusModuleTable": clusModuleTable,
       "clusModuleEntry": clusModuleEntry,
       "clusModuleIndex": clusModuleIndex,
       "clusModuleName": clusModuleName,
       "clusModuleVersion": clusModuleVersion,
       "clusModuleSerialNo": clusModuleSerialNo,
       "clusModuleUsableSpace": clusModuleUsableSpace,
       "clusModuleAvailableSpace": clusModuleAvailableSpace,
       "clusModuleIsManager": clusModuleIsManager,
       "clusModuleRaidConfiguration": clusModuleRaidConfiguration,
       "clusModuleStorageState": clusModuleStorageState,
       "clusModuleStorageStatus": clusModuleStorageStatus,
       "clusModuleStorageIsReady": clusModuleStorageIsReady,
       "clusModuleCreationTime": clusModuleCreationTime,
       "clusModuleDescription": clusModuleDescription,
       "clusModuleClusterName": clusModuleClusterName,
       "clusModuleEnabledFeatures": clusModuleEnabledFeatures,
       "clusModuleFeatureKey": clusModuleFeatureKey,
       "clusModuleStorageCondition": clusModuleStorageCondition,
       "clusModuleStatsIOsRead": clusModuleStatsIOsRead,
       "clusModuleStatsIOsWrite": clusModuleStatsIOsWrite,
       "clusModuleStatsKbytesRead": clusModuleStatsKbytesRead,
       "clusModuleStatsKbytesWrite": clusModuleStatsKbytesWrite,
       "clusModuleStatsQDepthTotal": clusModuleStatsQDepthTotal,
       "clusModuleStatsIoLatencyRead": clusModuleStatsIoLatencyRead,
       "clusModuleStatsIoLatencyWrite": clusModuleStatsIoLatencyWrite,
       "clusModuleStatsStoreLatencyTotal": clusModuleStatsStoreLatencyTotal,
       "clusModuleProvisionedSpace": clusModuleProvisionedSpace,
       "clusModuleUsedSpace": clusModuleUsedSpace,
       "clusModuleRowStatus": clusModuleRowStatus,
       "clusClusterCount": clusClusterCount,
       "clusClusterTable": clusClusterTable,
       "clusClusterEntry": clusClusterEntry,
       "clusClusterIndex": clusClusterIndex,
       "clusClusterName": clusClusterName,
       "clusClusterModuleCount": clusClusterModuleCount,
       "clusClusterVolumeCount": clusClusterVolumeCount,
       "clusClusterDescription": clusClusterDescription,
       "clusClusterHotSpareTimeout": clusClusterHotSpareTimeout,
       "clusClusterISNSCount": clusClusterISNSCount,
       "clusClusterISCSIVirtualIPCount": clusClusterISCSIVirtualIPCount,
       "clusClusterISCSIVirtualIPEnabled": clusClusterISCSIVirtualIPEnabled,
       "clusClusterAvailableSpace": clusClusterAvailableSpace,
       "clusClusterStatsIOsRead": clusClusterStatsIOsRead,
       "clusClusterStatsIOsWrite": clusClusterStatsIOsWrite,
       "clusClusterStatsBytesRead": clusClusterStatsBytesRead,
       "clusClusterStatsBytesWrite": clusClusterStatsBytesWrite,
       "clusClusterStatsQDepthRead": clusClusterStatsQDepthRead,
       "clusClusterStatsQDepthWrite": clusClusterStatsQDepthWrite,
       "clusClusterStatsIoLatencyRead": clusClusterStatsIoLatencyRead,
       "clusClusterStatsIoLatencyWrite": clusClusterStatsIoLatencyWrite,
       "clusClusterStatsCacheHits": clusClusterStatsCacheHits,
       "clusClusterTotalSpace": clusClusterTotalSpace,
       "clusClusterProvisionedSpace": clusClusterProvisionedSpace,
       "clusClusterUsedSpace": clusClusterUsedSpace,
       "clusClusterUtilization": clusClusterUtilization,
       "clusClusterRowStatus": clusClusterRowStatus,
       "clusClusterModuleTable": clusClusterModuleTable,
       "clusClusterModuleEntry": clusClusterModuleEntry,
       "clusClusterModuleIndex": clusClusterModuleIndex,
       "clusClusterModuleName": clusClusterModuleName,
       "clusClusterModuleSerialNo": clusClusterModuleSerialNo,
       "clusClusterModuleIsHotSpare": clusClusterModuleIsHotSpare,
       "clusClusterModuleRowStatus": clusClusterModuleRowStatus,
       "clusClusterISNSTable": clusClusterISNSTable,
       "clusClusterISNSEntry": clusClusterISNSEntry,
       "clusClusterISNSIndex": clusClusterISNSIndex,
       "clusClusterISNSHost": clusClusterISNSHost,
       "clusClusterISNSRowStatus": clusClusterISNSRowStatus,
       "clusClusterISCSIVirtualIPTable": clusClusterISCSIVirtualIPTable,
       "clusClusterISCSIVirtualIPEntry": clusClusterISCSIVirtualIPEntry,
       "clusClusterISCSIVirtualIPIndex": clusClusterISCSIVirtualIPIndex,
       "clusClusterISCSIVirtualIPAddress": clusClusterISCSIVirtualIPAddress,
       "clusClusterISCSIVirtualIPMask": clusClusterISCSIVirtualIPMask,
       "clusClusterISCSIVirtualIPRoute": clusClusterISCSIVirtualIPRoute,
       "clusClusterISCSIVirtualIPRowStatus": clusClusterISCSIVirtualIPRowStatus,
       "clusVolumeCount": clusVolumeCount,
       "clusVolumeTable": clusVolumeTable,
       "clusVolumeEntry": clusVolumeEntry,
       "clusVolumeIndex": clusVolumeIndex,
       "clusVolumeName": clusVolumeName,
       "clusVolumeCreationTime": clusVolumeCreationTime,
       "clusVolumeDescription": clusVolumeDescription,
       "clusVolumeSize": clusVolumeSize,
       "clusVolumeSoftThreshold": clusVolumeSoftThreshold,
       "clusVolumeHardThreshold": clusVolumeHardThreshold,
       "clusVolumeReplicaCount": clusVolumeReplicaCount,
       "clusVolumeSnapshotCount": clusVolumeSnapshotCount,
       "clusVolumeACLCount": clusVolumeACLCount,
       "clusVolumeClusterName": clusVolumeClusterName,
       "clusVolumeIsSoftThresholdExceeded": clusVolumeIsSoftThresholdExceeded,
       "clusVolumeIsHardThresholdExceeded": clusVolumeIsHardThresholdExceeded,
       "clusVolumeReplicationStatus": clusVolumeReplicationStatus,
       "clusVolumeIsRemoteSnapshot": clusVolumeIsRemoteSnapshot,
       "clusVolumeRemoteSnapshotFailureMessage": clusVolumeRemoteSnapshotFailureMessage,
       "clusVolumeAccessType": clusVolumeAccessType,
       "clusVolumeMinimumReplication": clusVolumeMinimumReplication,
       "clusVolumeCreator": clusVolumeCreator,
       "clusVolumeAutoGrowPages": clusVolumeAutoGrowPages,
       "clusVolumeIscsiIqn": clusVolumeIscsiIqn,
       "clusVolumeFriendlyName": clusVolumeFriendlyName,
       "clusVolumeInitiatorCount": clusVolumeInitiatorCount,
       "clusVolumeUsedSpace": clusVolumeUsedSpace,
       "clusVolumeClusterUsedPercent": clusVolumeClusterUsedPercent,
       "clusVolumeProvisionedSpace": clusVolumeProvisionedSpace,
       "clusVolumeIsThinProvisioned": clusVolumeIsThinProvisioned,
       "clusVolumeStatsIOsRead": clusVolumeStatsIOsRead,
       "clusVolumeStatsIOsWrite": clusVolumeStatsIOsWrite,
       "clusVolumeStatsBytesRead": clusVolumeStatsBytesRead,
       "clusVolumeStatsBytesWrite": clusVolumeStatsBytesWrite,
       "clusVolumeStatsQDepthRead": clusVolumeStatsQDepthRead,
       "clusVolumeStatsQDepthWrite": clusVolumeStatsQDepthWrite,
       "clusVolumeStatsIoLatencyRead": clusVolumeStatsIoLatencyRead,
       "clusVolumeStatsIoLatencyWrite": clusVolumeStatsIoLatencyWrite,
       "clusVolumeStatsCacheHits": clusVolumeStatsCacheHits,
       "clusVolumeAutoGrowSecondsDefault": clusVolumeAutoGrowSecondsDefault,
       "clusVolumeAutoGrowSeconds": clusVolumeAutoGrowSeconds,
       "clusVolumeType": clusVolumeType,
       "clusVolumeDataProtectionLevel": clusVolumeDataProtectionLevel,
       "clusVolumePBNRStripes": clusVolumePBNRStripes,
       "clusVolumePBNRParity": clusVolumePBNRParity,
       "clusVolumeAvailableSpace": clusVolumeAvailableSpace,
       "clusVolumeUsedPercent": clusVolumeUsedPercent,
       "clusVolumeIsFull": clusVolumeIsFull,
       "clusVolumeIsDeleting": clusVolumeIsDeleting,
       "clusVolumeIsAvailable": clusVolumeIsAvailable,
       "clusVolumeLunIsAvailable": clusVolumeLunIsAvailable,
       "clusVolumeReplicationState": clusVolumeReplicationState,
       "clusVolumeResyncPercent": clusVolumeResyncPercent,
       "clusVolumeRestripePending": clusVolumeRestripePending,
       "clusVolumeIsMigrating": clusVolumeIsMigrating,
       "clusVolumeMigrationPercent": clusVolumeMigrationPercent,
       "clusVolumeRowStatus": clusVolumeRowStatus,
       "clusVolumeACLTable": clusVolumeACLTable,
       "clusVolumeACLEntry": clusVolumeACLEntry,
       "clusVolumeACLIndex": clusVolumeACLIndex,
       "clusVolumeACLServer": clusVolumeACLServer,
       "clusVolumeACLPermissions": clusVolumeACLPermissions,
       "clusVolumeACLRowStatus": clusVolumeACLRowStatus,
       "clusVolumeInitiatorTable": clusVolumeInitiatorTable,
       "clusVolumeInitiatorEntry": clusVolumeInitiatorEntry,
       "clusVolumeInitiatorIndex": clusVolumeInitiatorIndex,
       "clusVolumeInitiatorIqn": clusVolumeInitiatorIqn,
       "clusVolumeInitiatorAddress": clusVolumeInitiatorAddress,
       "clusVolumeInitiatorPort": clusVolumeInitiatorPort,
       "clusVolumeInitiatorStatus": clusVolumeInitiatorStatus,
       "clusVolumeInitiatorStatsIOsRead": clusVolumeInitiatorStatsIOsRead,
       "clusVolumeInitiatorStatsIOsWrite": clusVolumeInitiatorStatsIOsWrite,
       "clusVolumeInitiatorStatsBytesRead": clusVolumeInitiatorStatsBytesRead,
       "clusVolumeInitiatorStatsBytesWrite": clusVolumeInitiatorStatsBytesWrite,
       "clusVolumeInitiatorStatsQDepthRead": clusVolumeInitiatorStatsQDepthRead,
       "clusVolumeInitiatorStatsQDepthWrite": clusVolumeInitiatorStatsQDepthWrite,
       "clusVolumeInitiatorStatsIoLatencyRead": clusVolumeInitiatorStatsIoLatencyRead,
       "clusVolumeInitiatorStatsIoLatencyWrite": clusVolumeInitiatorStatsIoLatencyWrite,
       "clusVolumeInitiatorStatsCacheHits": clusVolumeInitiatorStatsCacheHits,
       "clusVolumeInitiatorState": clusVolumeInitiatorState,
       "clusVolumeInitiatorRowStatus": clusVolumeInitiatorRowStatus,
       "clusClusterVolumeTable": clusClusterVolumeTable,
       "clusClusterVolumeEntry": clusClusterVolumeEntry,
       "clusClusterVolumeIndex": clusClusterVolumeIndex,
       "clusClusterVolumeName": clusClusterVolumeName,
       "clusClusterVolumeRowStatus": clusClusterVolumeRowStatus,
       "clusVolumeSnapshotTable": clusVolumeSnapshotTable,
       "clusVolumeSnapshotEntry": clusVolumeSnapshotEntry,
       "clusVolumeSnapshotIndex": clusVolumeSnapshotIndex,
       "clusVolumeSnapshotName": clusVolumeSnapshotName,
       "clusVolumeSnapshotCreationTime": clusVolumeSnapshotCreationTime,
       "clusVolumeSnapshotDescription": clusVolumeSnapshotDescription,
       "clusVolumeSnapshotSize": clusVolumeSnapshotSize,
       "clusVolumeSnapshotSoftThreshold": clusVolumeSnapshotSoftThreshold,
       "clusVolumeSnapshotHardThreshold": clusVolumeSnapshotHardThreshold,
       "clusVolumeSnapshotACLCount": clusVolumeSnapshotACLCount,
       "clusVolumeSnapshotScheduleName": clusVolumeSnapshotScheduleName,
       "clusVolumeSnapshotIsSoftThresholdExceeded": clusVolumeSnapshotIsSoftThresholdExceeded,
       "clusVolumeSnapshotIsHardThresholdExceeded": clusVolumeSnapshotIsHardThresholdExceeded,
       "clusVolumeSnapshotReplicationStatus": clusVolumeSnapshotReplicationStatus,
       "clusVolumeSnapshotType": clusVolumeSnapshotType,
       "clusVolumeSnapshotCopyProgress": clusVolumeSnapshotCopyProgress,
       "clusVolumeSnapshotAccessType": clusVolumeSnapshotAccessType,
       "clusVolumeSnapshotCreator": clusVolumeSnapshotCreator,
       "clusVolumeSnapshotIscsiIqn": clusVolumeSnapshotIscsiIqn,
       "clusVolumeSnapshotFriendlyName": clusVolumeSnapshotFriendlyName,
       "clusVolumeSnapshotOriginalVolume": clusVolumeSnapshotOriginalVolume,
       "clusVolumeSnapshotOriginalMgmtGroup": clusVolumeSnapshotOriginalMgmtGroup,
       "clusVolumeSnapshotInitiatorCount": clusVolumeSnapshotInitiatorCount,
       "clusVolumeSnapshotUsedSpace": clusVolumeSnapshotUsedSpace,
       "clusVolumeSnapshotWritableProvisionedSpace": clusVolumeSnapshotWritableProvisionedSpace,
       "clusVolumeSnapshotClusterUsedPercent": clusVolumeSnapshotClusterUsedPercent,
       "clusVolumeSnapshotProvisionedSpace": clusVolumeSnapshotProvisionedSpace,
       "clusVolumeSnapshotStatsIOsRead": clusVolumeSnapshotStatsIOsRead,
       "clusVolumeSnapshotStatsIOsWrite": clusVolumeSnapshotStatsIOsWrite,
       "clusVolumeSnapshotStatsBytesRead": clusVolumeSnapshotStatsBytesRead,
       "clusVolumeSnapshotStatsBytesWrite": clusVolumeSnapshotStatsBytesWrite,
       "clusVolumeSnapshotStatsQDepthRead": clusVolumeSnapshotStatsQDepthRead,
       "clusVolumeSnapshotStatsQDepthWrite": clusVolumeSnapshotStatsQDepthWrite,
       "clusVolumeSnapshotStatsIoLatencyRead": clusVolumeSnapshotStatsIoLatencyRead,
       "clusVolumeSnapshotStatsIoLatencyWrite": clusVolumeSnapshotStatsIoLatencyWrite,
       "clusVolumeSnapshotStatsCacheHits": clusVolumeSnapshotStatsCacheHits,
       "clusVolumeSnapshotIsDeleting": clusVolumeSnapshotIsDeleting,
       "clusVolumeSnapshotIsAvailable": clusVolumeSnapshotIsAvailable,
       "clusVolumeSnapshotLunIsAvailable": clusVolumeSnapshotLunIsAvailable,
       "clusVolumeSnapshotReplicationState": clusVolumeSnapshotReplicationState,
       "clusVolumeSnapshotResyncPercent": clusVolumeSnapshotResyncPercent,
       "clusVolumeSnapshotRestripePending": clusVolumeSnapshotRestripePending,
       "clusVolumeSnapshotIsMigrating": clusVolumeSnapshotIsMigrating,
       "clusVolumeSnapshotMigrationPercent": clusVolumeSnapshotMigrationPercent,
       "clusVolumeSnapshotRowStatus": clusVolumeSnapshotRowStatus,
       "clusVolumeSnapshotACLTable": clusVolumeSnapshotACLTable,
       "clusVolumeSnapshotACLEntry": clusVolumeSnapshotACLEntry,
       "clusVolumeSnapshotACLIndex": clusVolumeSnapshotACLIndex,
       "clusVolumeSnapshotACLServer": clusVolumeSnapshotACLServer,
       "clusVolumeSnapshotACLPermissions": clusVolumeSnapshotACLPermissions,
       "clusVolumeSnapshotACLRowStatus": clusVolumeSnapshotACLRowStatus,
       "clusVolumeSnapshotInitiatorTable": clusVolumeSnapshotInitiatorTable,
       "clusVolumeSnapshotInitiatorEntry": clusVolumeSnapshotInitiatorEntry,
       "clusVolumeSnapshotInitiatorIndex": clusVolumeSnapshotInitiatorIndex,
       "clusVolumeSnapshotInitiatorIqn": clusVolumeSnapshotInitiatorIqn,
       "clusVolumeSnapshotInitiatorAddress": clusVolumeSnapshotInitiatorAddress,
       "clusVolumeSnapshotInitiatorPort": clusVolumeSnapshotInitiatorPort,
       "clusVolumeSnapshotInitiatorStatus": clusVolumeSnapshotInitiatorStatus,
       "clusVolumeSnapshotInitiatorStatsIOsRead": clusVolumeSnapshotInitiatorStatsIOsRead,
       "clusVolumeSnapshotInitiatorStatsIOsWrite": clusVolumeSnapshotInitiatorStatsIOsWrite,
       "clusVolumeSnapshotInitiatorStatsBytesRead": clusVolumeSnapshotInitiatorStatsBytesRead,
       "clusVolumeSnapshotInitiatorStatsBytesWrite": clusVolumeSnapshotInitiatorStatsBytesWrite,
       "clusVolumeSnapshotInitiatorStatsQDepthRead": clusVolumeSnapshotInitiatorStatsQDepthRead,
       "clusVolumeSnapshotInitiatorStatsQDepthWrite": clusVolumeSnapshotInitiatorStatsQDepthWrite,
       "clusVolumeSnapshotInitiatorStatsIoLatencyRead": clusVolumeSnapshotInitiatorStatsIoLatencyRead,
       "clusVolumeSnapshotInitiatorStatsIoLatencyWrite": clusVolumeSnapshotInitiatorStatsIoLatencyWrite,
       "clusVolumeSnapshotInitiatorStatsCacheHits": clusVolumeSnapshotInitiatorStatsCacheHits,
       "clusVolumeSnapshotInitiatorState": clusVolumeSnapshotInitiatorState,
       "clusVolumeSnapshotInitiatorRowStatus": clusVolumeSnapshotInitiatorRowStatus,
       "clusServerCount": clusServerCount,
       "clusServerTable": clusServerTable,
       "clusServerEntry": clusServerEntry,
       "clusServerIndex": clusServerIndex,
       "clusServerName": clusServerName,
       "clusServerDescription": clusServerDescription,
       "clusServerIscsiEnabled": clusServerIscsiEnabled,
       "clusServerIscsiChapAuthRequired": clusServerIscsiChapAuthRequired,
       "clusServerIscsiInitiatorCount": clusServerIscsiInitiatorCount,
       "clusServerVolumeACLCount": clusServerVolumeACLCount,
       "clusServerRowStatus": clusServerRowStatus,
       "clusServerSubnetTable": clusServerSubnetTable,
       "clusServerSubnetEntry": clusServerSubnetEntry,
       "clusServerSubnetIndex": clusServerSubnetIndex,
       "clusServerSubnetAddress": clusServerSubnetAddress,
       "clusServerSubnetMask": clusServerSubnetMask,
       "clusServerSubnetRowStatus": clusServerSubnetRowStatus,
       "clusServerIscsiInitiatorTable": clusServerIscsiInitiatorTable,
       "clusServerIscsiInitiatorEntry": clusServerIscsiInitiatorEntry,
       "clusServerIscsiInitiatorIndex": clusServerIscsiInitiatorIndex,
       "clusServerIscsiInitiatorIqn": clusServerIscsiInitiatorIqn,
       "clusServerIscsiInitiatorChapName": clusServerIscsiInitiatorChapName,
       "clusServerIscsiInitiatorRowStatus": clusServerIscsiInitiatorRowStatus,
       "clusCommunicationMode": clusCommunicationMode,
       "clusUnicastHostCount": clusUnicastHostCount,
       "clusUnicastHostTable": clusUnicastHostTable,
       "clusUnicastHostEntry": clusUnicastHostEntry,
       "clusUnicastHostIndex": clusUnicastHostIndex,
       "clusUnicastHostName": clusUnicastHostName,
       "clusUnicastHostRowStatus": clusUnicastHostRowStatus,
       "clusSnapshotScheduleCount": clusSnapshotScheduleCount,
       "clusSnapshotScheduleTable": clusSnapshotScheduleTable,
       "clusSnapshotScheduleEntry": clusSnapshotScheduleEntry,
       "clusSnapshotScheduleIndex": clusSnapshotScheduleIndex,
       "clusSnapshotScheduleName": clusSnapshotScheduleName,
       "clusSnapshotScheduleDescription": clusSnapshotScheduleDescription,
       "clusSnapshotScheduleSoftThreshold": clusSnapshotScheduleSoftThreshold,
       "clusSnapshotScheduleHardThreshold": clusSnapshotScheduleHardThreshold,
       "clusSnapshotScheduleFirstCreationTime": clusSnapshotScheduleFirstCreationTime,
       "clusSnapshotScheduleFrequency": clusSnapshotScheduleFrequency,
       "clusSnapshotScheduleVolumeName": clusSnapshotScheduleVolumeName,
       "clusSnapshotScheduleRetainType": clusSnapshotScheduleRetainType,
       "clusSnapshotScheduleRetainCount": clusSnapshotScheduleRetainCount,
       "clusSnapshotScheduleRetainTime": clusSnapshotScheduleRetainTime,
       "clusSnapshotScheduleType": clusSnapshotScheduleType,
       "clusSnapshotScheduleFailureMessage": clusSnapshotScheduleFailureMessage,
       "clusSnapshotScheduleRowStatus": clusSnapshotScheduleRowStatus,
       "clusMgmtGroupSiteCount": clusMgmtGroupSiteCount,
       "clusSiteTable": clusSiteTable,
       "clusSiteEntry": clusSiteEntry,
       "clusSiteIndex": clusSiteIndex,
       "clusSiteName": clusSiteName,
       "clusSiteDescription": clusSiteDescription,
       "clusSiteIsPrimary": clusSiteIsPrimary,
       "clusSiteFailoverManager": clusSiteFailoverManager,
       "clusSiteModuleCount": clusSiteModuleCount,
       "clusSiteRowStatus": clusSiteRowStatus,
       "clusSiteModuleTable": clusSiteModuleTable,
       "clusSiteModuleEntry": clusSiteModuleEntry,
       "clusSiteModuleIndex": clusSiteModuleIndex,
       "clusSiteModuleName": clusSiteModuleName,
       "clusSiteModuleRowStatus": clusSiteModuleRowStatus,
       "clusServerVolumeACLTable": clusServerVolumeACLTable,
       "clusServerVolumeACLEntry": clusServerVolumeACLEntry,
       "clusServerVolumeACLIndex": clusServerVolumeACLIndex,
       "clusServerVolumeACLVolume": clusServerVolumeACLVolume,
       "clusServerVolumeACLPermissions": clusServerVolumeACLPermissions,
       "clusServerVolumeACLRowStatus": clusServerVolumeACLRowStatus}
)
