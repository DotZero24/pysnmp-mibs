# SNMP MIB module (TIMETRA-SATELLITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-SATELLITE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:50:56 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxPhysChassisClass,
 TmnxPhysChassisIndex,
 TmnxPortAdminStatus,
 TmnxRefInState,
 TmnxSETSRefAlarm,
 TmnxSETSRefQualified,
 TmnxSETSStatus,
 TmnxSSMQualityLevel,
 tmnxHwClass,
 tmnxHwOperState) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxPhysChassisClass",
    "TmnxPhysChassisIndex",
    "TmnxPortAdminStatus",
    "TmnxRefInState",
    "TmnxSETSRefAlarm",
    "TmnxSETSRefQualified",
    "TmnxSETSStatus",
    "TmnxSSMQualityLevel",
    "tmnxHwClass",
    "tmnxHwOperState")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(ServiceOperStatus,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServiceOperStatus",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxPortID")


# MODULE-IDENTITY

timetraSatelliteMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 103)
)
if mibBuilder.loadTexts:
    timetraSatelliteMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2014-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxSatelliteType(TextualConvention, Unsigned32):
    status = "current"


class TmnxSatelliteConsoleAccessStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 1),
          ("requested", 2),
          ("enabled", 3),
          ("not-applicable", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSatelliteConformance_ObjectIdentity = ObjectIdentity
tmnxSatelliteConformance = _TmnxSatelliteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103)
)
_TmnxSatelliteCompliances_ObjectIdentity = ObjectIdentity
tmnxSatelliteCompliances = _TmnxSatelliteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 1)
)
_TmnxSatelliteGroups_ObjectIdentity = ObjectIdentity
tmnxSatelliteGroups = _TmnxSatelliteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2)
)
_TmnxSatelliteV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxSatelliteV14v0Groups = _TmnxSatelliteV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1)
)
_TmnxSatelliteV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxSatelliteV15v0Groups = _TmnxSatelliteV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2)
)
_TmnxSatelliteV16v0Groups_ObjectIdentity = ObjectIdentity
tmnxSatelliteV16v0Groups = _TmnxSatelliteV16v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 3)
)
_TmnxSatelliteV19v0Groups_ObjectIdentity = ObjectIdentity
tmnxSatelliteV19v0Groups = _TmnxSatelliteV19v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 4)
)
_TmnxSatellite20v0Groups_ObjectIdentity = ObjectIdentity
tmnxSatellite20v0Groups = _TmnxSatellite20v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 5)
)
_TmnxSatelliteObjs_ObjectIdentity = ObjectIdentity
tmnxSatelliteObjs = _TmnxSatelliteObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103)
)
_TmnxSatelliteConfigTimestamps_ObjectIdentity = ObjectIdentity
tmnxSatelliteConfigTimestamps = _TmnxSatelliteConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1)
)
_TmnxSatelliteTableLastChanged_Type = TimeStamp
_TmnxSatelliteTableLastChanged_Object = MibScalar
tmnxSatelliteTableLastChanged = _TmnxSatelliteTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 2),
    _TmnxSatelliteTableLastChanged_Type()
)
tmnxSatelliteTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatelliteTableLastChanged.setStatus("current")
_TmnxSatPortMapConfigTableLastChg_Type = TimeStamp
_TmnxSatPortMapConfigTableLastChg_Object = MibScalar
tmnxSatPortMapConfigTableLastChg = _TmnxSatPortMapConfigTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 3),
    _TmnxSatPortMapConfigTableLastChg_Type()
)
tmnxSatPortMapConfigTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatPortMapConfigTableLastChg.setStatus("current")
_TmnxSatPortTemplateTableLastChg_Type = TimeStamp
_TmnxSatPortTemplateTableLastChg_Object = MibScalar
tmnxSatPortTemplateTableLastChg = _TmnxSatPortTemplateTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 4),
    _TmnxSatPortTemplateTableLastChg_Type()
)
tmnxSatPortTemplateTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatPortTemplateTableLastChg.setStatus("current")
_TmnxSatPortTmplPortTableLastChg_Type = TimeStamp
_TmnxSatPortTmplPortTableLastChg_Object = MibScalar
tmnxSatPortTmplPortTableLastChg = _TmnxSatPortTmplPortTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 5),
    _TmnxSatPortTmplPortTableLastChg_Type()
)
tmnxSatPortTmplPortTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatPortTmplPortTableLastChg.setStatus("current")
_TmnxSatLocalForwardTableLastChg_Type = TimeStamp
_TmnxSatLocalForwardTableLastChg_Object = MibScalar
tmnxSatLocalForwardTableLastChg = _TmnxSatLocalForwardTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 6),
    _TmnxSatLocalForwardTableLastChg_Type()
)
tmnxSatLocalForwardTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardTableLastChg.setStatus("current")
_TmnxSatLocalFwdSapTableLastChg_Type = TimeStamp
_TmnxSatLocalFwdSapTableLastChg_Object = MibScalar
tmnxSatLocalFwdSapTableLastChg = _TmnxSatLocalFwdSapTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 7),
    _TmnxSatLocalFwdSapTableLastChg_Type()
)
tmnxSatLocalFwdSapTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLocalFwdSapTableLastChg.setStatus("current")
_TmnxSatFeaturesTableLastChange_Type = TimeStamp
_TmnxSatFeaturesTableLastChange_Object = MibScalar
tmnxSatFeaturesTableLastChange = _TmnxSatFeaturesTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 1, 8),
    _TmnxSatFeaturesTableLastChange_Type()
)
tmnxSatFeaturesTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatFeaturesTableLastChange.setStatus("current")
_TmnxSatelliteConfigurations_ObjectIdentity = ObjectIdentity
tmnxSatelliteConfigurations = _TmnxSatelliteConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2)
)
_TmnxSatelliteTable_Object = MibTable
tmnxSatelliteTable = _TmnxSatelliteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxSatelliteTable.setStatus("current")
_TmnxSatelliteEntry_Object = MibTableRow
tmnxSatelliteEntry = _TmnxSatelliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1)
)
tmnxSatelliteEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatClass"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatId"),
)
if mibBuilder.loadTexts:
    tmnxSatelliteEntry.setStatus("current")
_TmnxSatClass_Type = TmnxPhysChassisClass
_TmnxSatClass_Object = MibTableColumn
tmnxSatClass = _TmnxSatClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 1),
    _TmnxSatClass_Type()
)
tmnxSatClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatClass.setStatus("current")


class _TmnxSatId_Type(TmnxPhysChassisIndex):
    """Custom type tmnxSatId based on TmnxPhysChassisIndex"""
    subtypeSpec = TmnxPhysChassisIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxSatId_Type.__name__ = "TmnxPhysChassisIndex"
_TmnxSatId_Object = MibTableColumn
tmnxSatId = _TmnxSatId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 2),
    _TmnxSatId_Type()
)
tmnxSatId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatId.setStatus("current")
_TmnxSatRowStatus_Type = RowStatus
_TmnxSatRowStatus_Object = MibTableColumn
tmnxSatRowStatus = _TmnxSatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 3),
    _TmnxSatRowStatus_Type()
)
tmnxSatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatRowStatus.setStatus("current")
_TmnxSatLastChanged_Type = TimeStamp
_TmnxSatLastChanged_Object = MibTableColumn
tmnxSatLastChanged = _TmnxSatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 4),
    _TmnxSatLastChanged_Type()
)
tmnxSatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLastChanged.setStatus("current")


class _TmnxSatAssignedType_Type(TmnxSatelliteType):
    """Custom type tmnxSatAssignedType based on TmnxSatelliteType"""
    defaultValue = 1


_TmnxSatAssignedType_Type.__name__ = "TmnxSatelliteType"
_TmnxSatAssignedType_Object = MibTableColumn
tmnxSatAssignedType = _TmnxSatAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 5),
    _TmnxSatAssignedType_Type()
)
tmnxSatAssignedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatAssignedType.setStatus("current")
_TmnxSatEquippedType_Type = TmnxSatelliteType
_TmnxSatEquippedType_Object = MibTableColumn
tmnxSatEquippedType = _TmnxSatEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 6),
    _TmnxSatEquippedType_Type()
)
tmnxSatEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatEquippedType.setStatus("current")


class _TmnxSatMacAddress_Type(MacAddress):
    """Custom type tmnxSatMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxSatMacAddress_Type.__name__ = "MacAddress"
_TmnxSatMacAddress_Object = MibTableColumn
tmnxSatMacAddress = _TmnxSatMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 7),
    _TmnxSatMacAddress_Type()
)
tmnxSatMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatMacAddress.setStatus("current")


class _TmnxSatSoftwareRepository_Type(TNamedItemOrEmpty):
    """Custom type tmnxSatSoftwareRepository based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSatSoftwareRepository_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSatSoftwareRepository_Object = MibTableColumn
tmnxSatSoftwareRepository = _TmnxSatSoftwareRepository_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 8),
    _TmnxSatSoftwareRepository_Type()
)
tmnxSatSoftwareRepository.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatSoftwareRepository.setStatus("current")


class _TmnxSatDescription_Type(TItemDescription):
    """Custom type tmnxSatDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSatDescription_Type.__name__ = "TItemDescription"
_TmnxSatDescription_Object = MibTableColumn
tmnxSatDescription = _TmnxSatDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 9),
    _TmnxSatDescription_Type()
)
tmnxSatDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatDescription.setStatus("current")


class _TmnxSatReboot_Type(TmnxActionType):
    """Custom type tmnxSatReboot based on TmnxActionType"""
    defaultValue = 2


_TmnxSatReboot_Type.__name__ = "TmnxActionType"
_TmnxSatReboot_Object = MibTableColumn
tmnxSatReboot = _TmnxSatReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 10),
    _TmnxSatReboot_Type()
)
tmnxSatReboot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatReboot.setStatus("current")


class _TmnxSatUpgrade_Type(TmnxActionType):
    """Custom type tmnxSatUpgrade based on TmnxActionType"""
    defaultValue = 2


_TmnxSatUpgrade_Type.__name__ = "TmnxActionType"
_TmnxSatUpgrade_Object = MibTableColumn
tmnxSatUpgrade = _TmnxSatUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 11),
    _TmnxSatUpgrade_Type()
)
tmnxSatUpgrade.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatUpgrade.setStatus("current")


class _TmnxSatSyncBootEnv_Type(TmnxActionType):
    """Custom type tmnxSatSyncBootEnv based on TmnxActionType"""
    defaultValue = 2


_TmnxSatSyncBootEnv_Type.__name__ = "TmnxActionType"
_TmnxSatSyncBootEnv_Object = MibTableColumn
tmnxSatSyncBootEnv = _TmnxSatSyncBootEnv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 12),
    _TmnxSatSyncBootEnv_Type()
)
tmnxSatSyncBootEnv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatSyncBootEnv.setStatus("current")


class _TmnxSatSyncEEnabled_Type(TruthValue):
    """Custom type tmnxSatSyncEEnabled based on TruthValue"""
    defaultValue = 2


_TmnxSatSyncEEnabled_Type.__name__ = "TruthValue"
_TmnxSatSyncEEnabled_Object = MibTableColumn
tmnxSatSyncEEnabled = _TmnxSatSyncEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 13),
    _TmnxSatSyncEEnabled_Type()
)
tmnxSatSyncEEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatSyncEEnabled.setStatus("current")


class _TmnxSatPortTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxSatPortTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSatPortTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSatPortTemplate_Object = MibTableColumn
tmnxSatPortTemplate = _TmnxSatPortTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 14),
    _TmnxSatPortTemplate_Type()
)
tmnxSatPortTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatPortTemplate.setStatus("current")


class _TmnxSatPtpTc_Type(TruthValue):
    """Custom type tmnxSatPtpTc based on TruthValue"""
    defaultValue = 2


_TmnxSatPtpTc_Type.__name__ = "TruthValue"
_TmnxSatPtpTc_Object = MibTableColumn
tmnxSatPtpTc = _TmnxSatPtpTc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 15),
    _TmnxSatPtpTc_Type()
)
tmnxSatPtpTc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatPtpTc.setStatus("current")


class _TmnxSatClientDownDelay_Type(Integer32):
    """Custom type tmnxSatClientDownDelay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1800),
    )


_TmnxSatClientDownDelay_Type.__name__ = "Integer32"
_TmnxSatClientDownDelay_Object = MibTableColumn
tmnxSatClientDownDelay = _TmnxSatClientDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 16),
    _TmnxSatClientDownDelay_Type()
)
tmnxSatClientDownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatClientDownDelay.setStatus("current")


class _TmnxSatConsoleAccess_Type(TruthValue):
    """Custom type tmnxSatConsoleAccess based on TruthValue"""
    defaultValue = 2


_TmnxSatConsoleAccess_Type.__name__ = "TruthValue"
_TmnxSatConsoleAccess_Object = MibTableColumn
tmnxSatConsoleAccess = _TmnxSatConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 17),
    _TmnxSatConsoleAccess_Type()
)
tmnxSatConsoleAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatConsoleAccess.setStatus("current")


class _TmnxSatConsoleAccessStatus_Type(TmnxSatelliteConsoleAccessStatus):
    """Custom type tmnxSatConsoleAccessStatus based on TmnxSatelliteConsoleAccessStatus"""
    defaultValue = 1


_TmnxSatConsoleAccessStatus_Type.__name__ = "TmnxSatelliteConsoleAccessStatus"
_TmnxSatConsoleAccessStatus_Object = MibTableColumn
tmnxSatConsoleAccessStatus = _TmnxSatConsoleAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 2, 2, 1, 18),
    _TmnxSatConsoleAccessStatus_Type()
)
tmnxSatConsoleAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatConsoleAccessStatus.setStatus("current")
_TmnxSatelliteStatus_ObjectIdentity = ObjectIdentity
tmnxSatelliteStatus = _TmnxSatelliteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3)
)
_TmnxSatelliteTypeTable_Object = MibTable
tmnxSatelliteTypeTable = _TmnxSatelliteTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxSatelliteTypeTable.setStatus("current")
_TmnxSatelliteTypeEntry_Object = MibTableRow
tmnxSatelliteTypeEntry = _TmnxSatelliteTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 1, 1)
)
tmnxSatelliteTypeEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxSatelliteTypeEntry.setStatus("current")
_TmnxSatTypeIndex_Type = TmnxSatelliteType
_TmnxSatTypeIndex_Object = MibTableColumn
tmnxSatTypeIndex = _TmnxSatTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 1, 1, 1),
    _TmnxSatTypeIndex_Type()
)
tmnxSatTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatTypeIndex.setStatus("current")
_TmnxSatTypeClass_Type = TmnxPhysChassisClass
_TmnxSatTypeClass_Object = MibTableColumn
tmnxSatTypeClass = _TmnxSatTypeClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 1, 1, 2),
    _TmnxSatTypeClass_Type()
)
tmnxSatTypeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatTypeClass.setStatus("current")
_TmnxSatTypeName_Type = TNamedItem
_TmnxSatTypeName_Object = MibTableColumn
tmnxSatTypeName = _TmnxSatTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 1, 1, 3),
    _TmnxSatTypeName_Type()
)
tmnxSatTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatTypeName.setStatus("current")
_TmnxSatTypeDescription_Type = TItemDescription
_TmnxSatTypeDescription_Object = MibTableColumn
tmnxSatTypeDescription = _TmnxSatTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 1, 1, 4),
    _TmnxSatTypeDescription_Type()
)
tmnxSatTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatTypeDescription.setStatus("current")
_TmnxSatellitePortMapTable_Object = MibTable
tmnxSatellitePortMapTable = _TmnxSatellitePortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxSatellitePortMapTable.setStatus("current")
_TmnxSatellitePortMapEntry_Object = MibTableRow
tmnxSatellitePortMapEntry = _TmnxSatellitePortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2, 1)
)
tmnxSatellitePortMapEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatClass"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatId"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatClientPortId"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatUplinkId"),
)
if mibBuilder.loadTexts:
    tmnxSatellitePortMapEntry.setStatus("current")
_TmnxSatClientPortId_Type = TmnxPortID
_TmnxSatClientPortId_Object = MibTableColumn
tmnxSatClientPortId = _TmnxSatClientPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2, 1, 1),
    _TmnxSatClientPortId_Type()
)
tmnxSatClientPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatClientPortId.setStatus("current")


class _TmnxSatUplinkId_Type(Unsigned32):
    """Custom type tmnxSatUplinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxSatUplinkId_Type.__name__ = "Unsigned32"
_TmnxSatUplinkId_Object = MibTableColumn
tmnxSatUplinkId = _TmnxSatUplinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2, 1, 2),
    _TmnxSatUplinkId_Type()
)
tmnxSatUplinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatUplinkId.setStatus("current")
_TmnxSatUplinkPortId_Type = TmnxPortID
_TmnxSatUplinkPortId_Object = MibTableColumn
tmnxSatUplinkPortId = _TmnxSatUplinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2, 1, 3),
    _TmnxSatUplinkPortId_Type()
)
tmnxSatUplinkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatUplinkPortId.setStatus("current")
_TmnxSatUplinkActive_Type = TruthValue
_TmnxSatUplinkActive_Object = MibTableColumn
tmnxSatUplinkActive = _TmnxSatUplinkActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2, 1, 4),
    _TmnxSatUplinkActive_Type()
)
tmnxSatUplinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatUplinkActive.setStatus("current")
_TmnxSatHostPortId_Type = TmnxPortID
_TmnxSatHostPortId_Object = MibTableColumn
tmnxSatHostPortId = _TmnxSatHostPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 2, 1, 5),
    _TmnxSatHostPortId_Type()
)
tmnxSatHostPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatHostPortId.setStatus("current")
_TmnxSatelliteSyncIfTimingTable_Object = MibTable
tmnxSatelliteSyncIfTimingTable = _TmnxSatelliteSyncIfTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxSatelliteSyncIfTimingTable.setStatus("current")
_TmnxSatelliteSyncIfTimingEntry_Object = MibTableRow
tmnxSatelliteSyncIfTimingEntry = _TmnxSatelliteSyncIfTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1)
)
tmnxSatelliteSyncIfTimingEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatClass"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatId"),
)
if mibBuilder.loadTexts:
    tmnxSatelliteSyncIfTimingEntry.setStatus("current")
_TmnxSatSyncIfTimingRef1SrcPort_Type = TmnxPortID
_TmnxSatSyncIfTimingRef1SrcPort_Object = MibTableColumn
tmnxSatSyncIfTimingRef1SrcPort = _TmnxSatSyncIfTimingRef1SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 1),
    _TmnxSatSyncIfTimingRef1SrcPort_Type()
)
tmnxSatSyncIfTimingRef1SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1SrcPort.setStatus("current")
_TmnxSatSyncIfTimingRef1AdmStatus_Type = TmnxPortAdminStatus
_TmnxSatSyncIfTimingRef1AdmStatus_Object = MibTableColumn
tmnxSatSyncIfTimingRef1AdmStatus = _TmnxSatSyncIfTimingRef1AdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 2),
    _TmnxSatSyncIfTimingRef1AdmStatus_Type()
)
tmnxSatSyncIfTimingRef1AdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1AdmStatus.setStatus("current")
_TmnxSatSyncIfTimingRef1InUse_Type = TruthValue
_TmnxSatSyncIfTimingRef1InUse_Object = MibTableColumn
tmnxSatSyncIfTimingRef1InUse = _TmnxSatSyncIfTimingRef1InUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 3),
    _TmnxSatSyncIfTimingRef1InUse_Type()
)
tmnxSatSyncIfTimingRef1InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1InUse.setStatus("current")
_TmnxSatSyncIfTimingRef1Qualified_Type = TmnxSETSRefQualified
_TmnxSatSyncIfTimingRef1Qualified_Object = MibTableColumn
tmnxSatSyncIfTimingRef1Qualified = _TmnxSatSyncIfTimingRef1Qualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 4),
    _TmnxSatSyncIfTimingRef1Qualified_Type()
)
tmnxSatSyncIfTimingRef1Qualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1Qualified.setStatus("current")
_TmnxSatSyncIfTimingRef1Alarm_Type = TmnxSETSRefAlarm
_TmnxSatSyncIfTimingRef1Alarm_Object = MibTableColumn
tmnxSatSyncIfTimingRef1Alarm = _TmnxSatSyncIfTimingRef1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 5),
    _TmnxSatSyncIfTimingRef1Alarm_Type()
)
tmnxSatSyncIfTimingRef1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1Alarm.setStatus("current")
_TmnxSatSyncIfTimingRef1RxQltyLvl_Type = TmnxSSMQualityLevel
_TmnxSatSyncIfTimingRef1RxQltyLvl_Object = MibTableColumn
tmnxSatSyncIfTimingRef1RxQltyLvl = _TmnxSatSyncIfTimingRef1RxQltyLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 6),
    _TmnxSatSyncIfTimingRef1RxQltyLvl_Type()
)
tmnxSatSyncIfTimingRef1RxQltyLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1RxQltyLvl.setStatus("current")
_TmnxSatSyncIfTimingRef1State_Type = TmnxRefInState
_TmnxSatSyncIfTimingRef1State_Object = MibTableColumn
tmnxSatSyncIfTimingRef1State = _TmnxSatSyncIfTimingRef1State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 7),
    _TmnxSatSyncIfTimingRef1State_Type()
)
tmnxSatSyncIfTimingRef1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef1State.setStatus("current")
_TmnxSatSyncIfTimingRef2SrcPort_Type = TmnxPortID
_TmnxSatSyncIfTimingRef2SrcPort_Object = MibTableColumn
tmnxSatSyncIfTimingRef2SrcPort = _TmnxSatSyncIfTimingRef2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 8),
    _TmnxSatSyncIfTimingRef2SrcPort_Type()
)
tmnxSatSyncIfTimingRef2SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2SrcPort.setStatus("current")
_TmnxSatSyncIfTimingRef2AdmStatus_Type = TmnxPortAdminStatus
_TmnxSatSyncIfTimingRef2AdmStatus_Object = MibTableColumn
tmnxSatSyncIfTimingRef2AdmStatus = _TmnxSatSyncIfTimingRef2AdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 9),
    _TmnxSatSyncIfTimingRef2AdmStatus_Type()
)
tmnxSatSyncIfTimingRef2AdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2AdmStatus.setStatus("current")
_TmnxSatSyncIfTimingRef2InUse_Type = TruthValue
_TmnxSatSyncIfTimingRef2InUse_Object = MibTableColumn
tmnxSatSyncIfTimingRef2InUse = _TmnxSatSyncIfTimingRef2InUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 10),
    _TmnxSatSyncIfTimingRef2InUse_Type()
)
tmnxSatSyncIfTimingRef2InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2InUse.setStatus("current")
_TmnxSatSyncIfTimingRef2Qualified_Type = TmnxSETSRefQualified
_TmnxSatSyncIfTimingRef2Qualified_Object = MibTableColumn
tmnxSatSyncIfTimingRef2Qualified = _TmnxSatSyncIfTimingRef2Qualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 11),
    _TmnxSatSyncIfTimingRef2Qualified_Type()
)
tmnxSatSyncIfTimingRef2Qualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2Qualified.setStatus("current")
_TmnxSatSyncIfTimingRef2Alarm_Type = TmnxSETSRefAlarm
_TmnxSatSyncIfTimingRef2Alarm_Object = MibTableColumn
tmnxSatSyncIfTimingRef2Alarm = _TmnxSatSyncIfTimingRef2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 12),
    _TmnxSatSyncIfTimingRef2Alarm_Type()
)
tmnxSatSyncIfTimingRef2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2Alarm.setStatus("current")
_TmnxSatSyncIfTimingRef2RxQltyLvl_Type = TmnxSSMQualityLevel
_TmnxSatSyncIfTimingRef2RxQltyLvl_Object = MibTableColumn
tmnxSatSyncIfTimingRef2RxQltyLvl = _TmnxSatSyncIfTimingRef2RxQltyLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 13),
    _TmnxSatSyncIfTimingRef2RxQltyLvl_Type()
)
tmnxSatSyncIfTimingRef2RxQltyLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2RxQltyLvl.setStatus("current")
_TmnxSatSyncIfTimingRef2State_Type = TmnxRefInState
_TmnxSatSyncIfTimingRef2State_Object = MibTableColumn
tmnxSatSyncIfTimingRef2State = _TmnxSatSyncIfTimingRef2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 14),
    _TmnxSatSyncIfTimingRef2State_Type()
)
tmnxSatSyncIfTimingRef2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingRef2State.setStatus("current")
_TmnxSatSyncIfTimingFreqOffset_Type = Integer32
_TmnxSatSyncIfTimingFreqOffset_Object = MibTableColumn
tmnxSatSyncIfTimingFreqOffset = _TmnxSatSyncIfTimingFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 15),
    _TmnxSatSyncIfTimingFreqOffset_Type()
)
tmnxSatSyncIfTimingFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingFreqOffset.setUnits("parts-per-million")
_TmnxSatSyncIfTimingStatus_Type = TmnxSETSStatus
_TmnxSatSyncIfTimingStatus_Object = MibTableColumn
tmnxSatSyncIfTimingStatus = _TmnxSatSyncIfTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 16),
    _TmnxSatSyncIfTimingStatus_Type()
)
tmnxSatSyncIfTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingStatus.setStatus("current")
_TmnxSatSyncIfTimingSystemQltyLvl_Type = TmnxSSMQualityLevel
_TmnxSatSyncIfTimingSystemQltyLvl_Object = MibTableColumn
tmnxSatSyncIfTimingSystemQltyLvl = _TmnxSatSyncIfTimingSystemQltyLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 3, 3, 1, 17),
    _TmnxSatSyncIfTimingSystemQltyLvl_Type()
)
tmnxSatSyncIfTimingSystemQltyLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimingSystemQltyLvl.setStatus("current")
_TmnxSatelliteStatistics_ObjectIdentity = ObjectIdentity
tmnxSatelliteStatistics = _TmnxSatelliteStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 4)
)
_TmnxSatelliteNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxSatelliteNotifyObjects = _TmnxSatelliteNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 5)
)
_TmnxSatNotifyFailureReason_Type = DisplayString
_TmnxSatNotifyFailureReason_Object = MibScalar
tmnxSatNotifyFailureReason = _TmnxSatNotifyFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 5, 1),
    _TmnxSatNotifyFailureReason_Type()
)
tmnxSatNotifyFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSatNotifyFailureReason.setStatus("current")


class _TmnxSatNotifySyncIfTimRefAlarm_Type(Integer32):
    """Custom type tmnxSatNotifySyncIfTimRefAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("los", 1),
          ("oof", 2),
          ("oopir", 3))
    )


_TmnxSatNotifySyncIfTimRefAlarm_Type.__name__ = "Integer32"
_TmnxSatNotifySyncIfTimRefAlarm_Object = MibScalar
tmnxSatNotifySyncIfTimRefAlarm = _TmnxSatNotifySyncIfTimRefAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 5, 2),
    _TmnxSatNotifySyncIfTimRefAlarm_Type()
)
tmnxSatNotifySyncIfTimRefAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSatNotifySyncIfTimRefAlarm.setStatus("current")
_TmnxSatellitePortMapConfigTable_Object = MibTable
tmnxSatellitePortMapConfigTable = _TmnxSatellitePortMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 6)
)
if mibBuilder.loadTexts:
    tmnxSatellitePortMapConfigTable.setStatus("current")
_TmnxSatellitePortMapConfigEntry_Object = MibTableRow
tmnxSatellitePortMapConfigEntry = _TmnxSatellitePortMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 6, 1)
)
tmnxSatellitePortMapConfigEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatClass"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatId"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatClientPortId"),
)
if mibBuilder.loadTexts:
    tmnxSatellitePortMapConfigEntry.setStatus("current")
_TmnxSatPortMapConfigEntryLastChg_Type = TimeStamp
_TmnxSatPortMapConfigEntryLastChg_Object = MibTableColumn
tmnxSatPortMapConfigEntryLastChg = _TmnxSatPortMapConfigEntryLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 6, 1, 1),
    _TmnxSatPortMapConfigEntryLastChg_Type()
)
tmnxSatPortMapConfigEntryLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatPortMapConfigEntryLastChg.setStatus("current")
_TmnxSatPrimaryUplinkPortId_Type = TmnxPortID
_TmnxSatPrimaryUplinkPortId_Object = MibTableColumn
tmnxSatPrimaryUplinkPortId = _TmnxSatPrimaryUplinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 6, 1, 2),
    _TmnxSatPrimaryUplinkPortId_Type()
)
tmnxSatPrimaryUplinkPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatPrimaryUplinkPortId.setStatus("current")
_TmnxSatSecondaryUplinkPortId_Type = TmnxPortID
_TmnxSatSecondaryUplinkPortId_Object = MibTableColumn
tmnxSatSecondaryUplinkPortId = _TmnxSatSecondaryUplinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 6, 1, 3),
    _TmnxSatSecondaryUplinkPortId_Type()
)
tmnxSatSecondaryUplinkPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatSecondaryUplinkPortId.setStatus("current")
_TmnxSatellitePortTemplateTable_Object = MibTable
tmnxSatellitePortTemplateTable = _TmnxSatellitePortTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7)
)
if mibBuilder.loadTexts:
    tmnxSatellitePortTemplateTable.setStatus("current")
_TmnxSatellitePortTemplateEntry_Object = MibTableRow
tmnxSatellitePortTemplateEntry = _TmnxSatellitePortTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1)
)
tmnxSatellitePortTemplateEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatellitePortTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxSatellitePortTemplateEntry.setStatus("current")
_TmnxSatellitePortTemplateName_Type = TNamedItem
_TmnxSatellitePortTemplateName_Object = MibTableColumn
tmnxSatellitePortTemplateName = _TmnxSatellitePortTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1, 1),
    _TmnxSatellitePortTemplateName_Type()
)
tmnxSatellitePortTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatellitePortTemplateName.setStatus("current")
_TmnxSatPortTemplateRowStatus_Type = RowStatus
_TmnxSatPortTemplateRowStatus_Object = MibTableColumn
tmnxSatPortTemplateRowStatus = _TmnxSatPortTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1, 2),
    _TmnxSatPortTemplateRowStatus_Type()
)
tmnxSatPortTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatPortTemplateRowStatus.setStatus("current")
_TmnxSatPortTemplateEntryLastChg_Type = TimeStamp
_TmnxSatPortTemplateEntryLastChg_Object = MibTableColumn
tmnxSatPortTemplateEntryLastChg = _TmnxSatPortTemplateEntryLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1, 3),
    _TmnxSatPortTemplateEntryLastChg_Type()
)
tmnxSatPortTemplateEntryLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatPortTemplateEntryLastChg.setStatus("current")
_TmnxSatPortTemplateSatType_Type = TmnxSatelliteType
_TmnxSatPortTemplateSatType_Object = MibTableColumn
tmnxSatPortTemplateSatType = _TmnxSatPortTemplateSatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1, 4),
    _TmnxSatPortTemplateSatType_Type()
)
tmnxSatPortTemplateSatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatPortTemplateSatType.setStatus("current")


class _TmnxSatPortTemplateAdminState_Type(TmnxAdminState):
    """Custom type tmnxSatPortTemplateAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSatPortTemplateAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSatPortTemplateAdminState_Object = MibTableColumn
tmnxSatPortTemplateAdminState = _TmnxSatPortTemplateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1, 5),
    _TmnxSatPortTemplateAdminState_Type()
)
tmnxSatPortTemplateAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatPortTemplateAdminState.setStatus("current")


class _TmnxSatPortTemplateDescription_Type(TItemDescription):
    """Custom type tmnxSatPortTemplateDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSatPortTemplateDescription_Type.__name__ = "TItemDescription"
_TmnxSatPortTemplateDescription_Object = MibTableColumn
tmnxSatPortTemplateDescription = _TmnxSatPortTemplateDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 7, 1, 6),
    _TmnxSatPortTemplateDescription_Type()
)
tmnxSatPortTemplateDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatPortTemplateDescription.setStatus("current")
_TmnxSatPortTemplatePortTable_Object = MibTable
tmnxSatPortTemplatePortTable = _TmnxSatPortTemplatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 8)
)
if mibBuilder.loadTexts:
    tmnxSatPortTemplatePortTable.setStatus("current")
_TmnxSatPortTemplatePortEntry_Object = MibTableRow
tmnxSatPortTemplatePortEntry = _TmnxSatPortTemplatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 8, 1)
)
tmnxSatPortTemplatePortEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatellitePortTemplateName"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatPhysPortId"),
)
if mibBuilder.loadTexts:
    tmnxSatPortTemplatePortEntry.setStatus("current")
_TmnxSatPhysPortId_Type = TmnxPortID
_TmnxSatPhysPortId_Object = MibTableColumn
tmnxSatPhysPortId = _TmnxSatPhysPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 8, 1, 1),
    _TmnxSatPhysPortId_Type()
)
tmnxSatPhysPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatPhysPortId.setStatus("current")
_TmnxSatPortTmplPortEntryLastChg_Type = TimeStamp
_TmnxSatPortTmplPortEntryLastChg_Object = MibTableColumn
tmnxSatPortTmplPortEntryLastChg = _TmnxSatPortTmplPortEntryLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 8, 1, 2),
    _TmnxSatPortTmplPortEntryLastChg_Type()
)
tmnxSatPortTmplPortEntryLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatPortTmplPortEntryLastChg.setStatus("current")


class _TmnxSatPortTemplatePortRole_Type(Integer32):
    """Custom type tmnxSatPortTemplatePortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("uplink", 1),
          ("client", 2))
    )


_TmnxSatPortTemplatePortRole_Type.__name__ = "Integer32"
_TmnxSatPortTemplatePortRole_Object = MibTableColumn
tmnxSatPortTemplatePortRole = _TmnxSatPortTemplatePortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 8, 1, 3),
    _TmnxSatPortTemplatePortRole_Type()
)
tmnxSatPortTemplatePortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatPortTemplatePortRole.setStatus("current")
_TmnxSatPortTemplatePortUplink_Type = TmnxPortID
_TmnxSatPortTemplatePortUplink_Object = MibTableColumn
tmnxSatPortTemplatePortUplink = _TmnxSatPortTemplatePortUplink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 8, 1, 4),
    _TmnxSatPortTemplatePortUplink_Type()
)
tmnxSatPortTemplatePortUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatPortTemplatePortUplink.setStatus("current")
_TmnxSatelliteLocalForwardTable_Object = MibTable
tmnxSatelliteLocalForwardTable = _TmnxSatelliteLocalForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9)
)
if mibBuilder.loadTexts:
    tmnxSatelliteLocalForwardTable.setStatus("current")
_TmnxSatelliteLocalForwardEntry_Object = MibTableRow
tmnxSatelliteLocalForwardEntry = _TmnxSatelliteLocalForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1)
)
tmnxSatelliteLocalForwardEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardId"),
)
if mibBuilder.loadTexts:
    tmnxSatelliteLocalForwardEntry.setStatus("current")


class _TmnxSatLocalForwardId_Type(Unsigned32):
    """Custom type tmnxSatLocalForwardId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )


_TmnxSatLocalForwardId_Type.__name__ = "Unsigned32"
_TmnxSatLocalForwardId_Object = MibTableColumn
tmnxSatLocalForwardId = _TmnxSatLocalForwardId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1, 1),
    _TmnxSatLocalForwardId_Type()
)
tmnxSatLocalForwardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardId.setStatus("current")
_TmnxSatLocalForwardRowStatus_Type = RowStatus
_TmnxSatLocalForwardRowStatus_Object = MibTableColumn
tmnxSatLocalForwardRowStatus = _TmnxSatLocalForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1, 2),
    _TmnxSatLocalForwardRowStatus_Type()
)
tmnxSatLocalForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardRowStatus.setStatus("current")
_TmnxSatLocalForwardEntryLastChg_Type = TimeStamp
_TmnxSatLocalForwardEntryLastChg_Object = MibTableColumn
tmnxSatLocalForwardEntryLastChg = _TmnxSatLocalForwardEntryLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1, 3),
    _TmnxSatLocalForwardEntryLastChg_Type()
)
tmnxSatLocalForwardEntryLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardEntryLastChg.setStatus("current")


class _TmnxSatLocalForwardAdminState_Type(TmnxAdminState):
    """Custom type tmnxSatLocalForwardAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSatLocalForwardAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSatLocalForwardAdminState_Object = MibTableColumn
tmnxSatLocalForwardAdminState = _TmnxSatLocalForwardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1, 4),
    _TmnxSatLocalForwardAdminState_Type()
)
tmnxSatLocalForwardAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardAdminState.setStatus("current")


class _TmnxSatLocalForwardDescription_Type(TItemDescription):
    """Custom type tmnxSatLocalForwardDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSatLocalForwardDescription_Type.__name__ = "TItemDescription"
_TmnxSatLocalForwardDescription_Object = MibTableColumn
tmnxSatLocalForwardDescription = _TmnxSatLocalForwardDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1, 5),
    _TmnxSatLocalForwardDescription_Type()
)
tmnxSatLocalForwardDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardDescription.setStatus("current")
_TmnxSatLocalForwardOperState_Type = ServiceOperStatus
_TmnxSatLocalForwardOperState_Object = MibTableColumn
tmnxSatLocalForwardOperState = _TmnxSatLocalForwardOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 9, 1, 6),
    _TmnxSatLocalForwardOperState_Type()
)
tmnxSatLocalForwardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardOperState.setStatus("current")
_TmnxSatLocalForwardSapTable_Object = MibTable
tmnxSatLocalForwardSapTable = _TmnxSatLocalForwardSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10)
)
if mibBuilder.loadTexts:
    tmnxSatLocalForwardSapTable.setStatus("current")
_TmnxSatLocalForwardSapEntry_Object = MibTableRow
tmnxSatLocalForwardSapEntry = _TmnxSatLocalForwardSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1)
)
tmnxSatLocalForwardSapEntry.setIndexNames(
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardId"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatPortId"),
    (0, "TIMETRA-SATELLITE-MIB", "tmnxSatEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxSatLocalForwardSapEntry.setStatus("current")
_TmnxSatPortId_Type = TmnxPortID
_TmnxSatPortId_Object = MibTableColumn
tmnxSatPortId = _TmnxSatPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 1),
    _TmnxSatPortId_Type()
)
tmnxSatPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatPortId.setStatus("current")


class _TmnxSatEncapValue_Type(Unsigned32):
    """Custom type tmnxSatEncapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TmnxSatEncapValue_Type.__name__ = "Unsigned32"
_TmnxSatEncapValue_Object = MibTableColumn
tmnxSatEncapValue = _TmnxSatEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 2),
    _TmnxSatEncapValue_Type()
)
tmnxSatEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSatEncapValue.setStatus("current")
_TmnxSatLocalForwardSapRowStatus_Type = RowStatus
_TmnxSatLocalForwardSapRowStatus_Object = MibTableColumn
tmnxSatLocalForwardSapRowStatus = _TmnxSatLocalForwardSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 3),
    _TmnxSatLocalForwardSapRowStatus_Type()
)
tmnxSatLocalForwardSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardSapRowStatus.setStatus("current")
_TmnxSatLocalFwdSapEntryLastChg_Type = TimeStamp
_TmnxSatLocalFwdSapEntryLastChg_Object = MibTableColumn
tmnxSatLocalFwdSapEntryLastChg = _TmnxSatLocalFwdSapEntryLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 4),
    _TmnxSatLocalFwdSapEntryLastChg_Type()
)
tmnxSatLocalFwdSapEntryLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLocalFwdSapEntryLastChg.setStatus("current")


class _TmnxSatLocalForwardSapAdminState_Type(TmnxAdminState):
    """Custom type tmnxSatLocalForwardSapAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSatLocalForwardSapAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSatLocalForwardSapAdminState_Object = MibTableColumn
tmnxSatLocalForwardSapAdminState = _TmnxSatLocalForwardSapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 5),
    _TmnxSatLocalForwardSapAdminState_Type()
)
tmnxSatLocalForwardSapAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardSapAdminState.setStatus("current")


class _TmnxSatLocalFwdSapDescription_Type(TItemDescription):
    """Custom type tmnxSatLocalFwdSapDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSatLocalFwdSapDescription_Type.__name__ = "TItemDescription"
_TmnxSatLocalFwdSapDescription_Object = MibTableColumn
tmnxSatLocalFwdSapDescription = _TmnxSatLocalFwdSapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 6),
    _TmnxSatLocalFwdSapDescription_Type()
)
tmnxSatLocalFwdSapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSatLocalFwdSapDescription.setStatus("current")


class _TmnxSatLocalForwardSapOperState_Type(Integer32):
    """Custom type tmnxSatLocalForwardSapOperState based on Integer32"""
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


_TmnxSatLocalForwardSapOperState_Type.__name__ = "Integer32"
_TmnxSatLocalForwardSapOperState_Object = MibTableColumn
tmnxSatLocalForwardSapOperState = _TmnxSatLocalForwardSapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 10, 1, 7),
    _TmnxSatLocalForwardSapOperState_Type()
)
tmnxSatLocalForwardSapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatLocalForwardSapOperState.setStatus("current")
_TmnxSatelliteFeaturesTable_Object = MibTable
tmnxSatelliteFeaturesTable = _TmnxSatelliteFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 11)
)
if mibBuilder.loadTexts:
    tmnxSatelliteFeaturesTable.setStatus("current")
_TmnxSatelliteFeaturesEntry_Object = MibTableRow
tmnxSatelliteFeaturesEntry = _TmnxSatelliteFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxSatelliteFeaturesEntry.setStatus("current")
_TmnxSatFeaturesEntryLastChange_Type = TimeStamp
_TmnxSatFeaturesEntryLastChange_Object = MibTableColumn
tmnxSatFeaturesEntryLastChange = _TmnxSatFeaturesEntryLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 11, 1, 1),
    _TmnxSatFeaturesEntryLastChange_Type()
)
tmnxSatFeaturesEntryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSatFeaturesEntryLastChange.setStatus("current")


class _TmnxSatFeatureLocalForward_Type(TmnxEnabledDisabled):
    """Custom type tmnxSatFeatureLocalForward based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxSatFeatureLocalForward_Type.__name__ = "TmnxEnabledDisabled"
_TmnxSatFeatureLocalForward_Object = MibTableColumn
tmnxSatFeatureLocalForward = _TmnxSatFeatureLocalForward_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 11, 1, 2),
    _TmnxSatFeatureLocalForward_Type()
)
tmnxSatFeatureLocalForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatFeatureLocalForward.setStatus("current")


class _TmnxSatFeaturePtpTc_Type(TmnxEnabledDisabled):
    """Custom type tmnxSatFeaturePtpTc based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxSatFeaturePtpTc_Type.__name__ = "TmnxEnabledDisabled"
_TmnxSatFeaturePtpTc_Object = MibTableColumn
tmnxSatFeaturePtpTc = _TmnxSatFeaturePtpTc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 11, 1, 3),
    _TmnxSatFeaturePtpTc_Type()
)
tmnxSatFeaturePtpTc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatFeaturePtpTc.setStatus("current")
_TmnxSatelliteSecurityObjs_ObjectIdentity = ObjectIdentity
tmnxSatelliteSecurityObjs = _TmnxSatelliteSecurityObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 12)
)


class _TmnxSatFileTransferFtp_Type(TmnxEnabledDisabled):
    """Custom type tmnxSatFileTransferFtp based on TmnxEnabledDisabled"""
    defaultValue = 1


_TmnxSatFileTransferFtp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxSatFileTransferFtp_Object = MibScalar
tmnxSatFileTransferFtp = _TmnxSatFileTransferFtp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 12, 1),
    _TmnxSatFileTransferFtp_Type()
)
tmnxSatFileTransferFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatFileTransferFtp.setStatus("current")


class _TmnxSatFileTransferScp_Type(TmnxEnabledDisabled):
    """Custom type tmnxSatFileTransferScp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxSatFileTransferScp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxSatFileTransferScp_Object = MibScalar
tmnxSatFileTransferScp = _TmnxSatFileTransferScp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 103, 12, 2),
    _TmnxSatFileTransferScp_Type()
)
tmnxSatFileTransferScp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSatFileTransferScp.setStatus("current")
_TmnxSatelliteNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSatelliteNotifyPrefix = _TmnxSatelliteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103)
)
_TmnxSatelliteNotifications_ObjectIdentity = ObjectIdentity
tmnxSatelliteNotifications = _TmnxSatelliteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0)
)
tmnxSatelliteEntry.registerAugmentions(
    ("TIMETRA-SATELLITE-MIB",
     "tmnxSatelliteFeaturesEntry")
)
tmnxSatelliteFeaturesEntry.setIndexNames(*tmnxSatelliteEntry.getIndexNames())

# Managed Objects groups

tmnxSatelliteGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1, 1)
)
tmnxSatelliteGroupV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatelliteTableLastChanged"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatRowStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLastChanged"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatAssignedType"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatEquippedType"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatMacAddress"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSoftwareRepository"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatDescription"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatReboot"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatUpgrade"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncBootEnv"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncEEnabled"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteGroupV14v0.setStatus("current")

tmnxSatelliteTypeGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1, 2)
)
tmnxSatelliteTypeGroupV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatTypeClass"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatTypeName"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatTypeDescription"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteTypeGroupV14v0.setStatus("current")

tmnxSatellitePortMapGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1, 3)
)
tmnxSatellitePortMapGroupV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatUplinkPortId"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatUplinkActive"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatHostPortId"))
)
if mibBuilder.loadTexts:
    tmnxSatellitePortMapGroupV14v0.setStatus("current")

tmnxSatelliteSyncIfTimGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1, 4)
)
tmnxSatelliteSyncIfTimGroupV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1SrcPort"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1AdmStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1InUse"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1Qualified"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1Alarm"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2SrcPort"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2AdmStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2InUse"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2Qualified"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2Alarm"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingFreqOffset"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1RxQltyLvl"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2RxQltyLvl"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1State"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2State"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingSystemQltyLvl"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteSyncIfTimGroupV14v0.setStatus("current")

tmnxSatelliteNotifyObjsGrpV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1, 6)
)
tmnxSatelliteNotifyObjsGrpV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatNotifyFailureReason"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatNotifySyncIfTimRefAlarm"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteNotifyObjsGrpV14v0.setStatus("current")

tmnxSatPortMapGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2, 1)
)
tmnxSatPortMapGroupV15v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatPortMapConfigTableLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortMapConfigEntryLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPrimaryUplinkPortId"))
)
if mibBuilder.loadTexts:
    tmnxSatPortMapGroupV15v0.setStatus("current")

tmnxSatResiliencyGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2, 2)
)
tmnxSatResiliencyGroupV15v0.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatSecondaryUplinkPortId")
)
if mibBuilder.loadTexts:
    tmnxSatResiliencyGroupV15v0.setStatus("current")

tmnxSatPortTemplateGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2, 3)
)
tmnxSatPortTemplateGroupV15v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplate"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateTableLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateRowStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateEntryLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateSatType"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateAdminState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateDescription"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTmplPortTableLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTmplPortEntryLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplatePortRole"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplatePortUplink"))
)
if mibBuilder.loadTexts:
    tmnxSatPortTemplateGroupV15v0.setStatus("current")

tmnxSatLocalForwardGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2, 4)
)
tmnxSatLocalForwardGroupV15v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardTableLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardRowStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardEntryLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardAdminState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardDescription"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardOperState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalFwdSapTableLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardSapRowStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalFwdSapEntryLastChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardSapAdminState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalFwdSapDescription"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardSapOperState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatFeatureLocalForward"))
)
if mibBuilder.loadTexts:
    tmnxSatLocalForwardGroupV15v0.setStatus("current")

tmnxSatFeaturesGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2, 5)
)
tmnxSatFeaturesGroupV15v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatFeaturesTableLastChange"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatFeaturesEntryLastChange"))
)
if mibBuilder.loadTexts:
    tmnxSatFeaturesGroupV15v0.setStatus("current")

tmnxSatPtpTcGroupV16v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 3, 1)
)
tmnxSatPtpTcGroupV16v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatPtpTc"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatFeaturePtpTc"))
)
if mibBuilder.loadTexts:
    tmnxSatPtpTcGroupV16v0.setStatus("current")

tmnxSatClientDownDelayGroupV19v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 4, 1)
)
tmnxSatClientDownDelayGroupV19v0.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatClientDownDelay")
)
if mibBuilder.loadTexts:
    tmnxSatClientDownDelayGroupV19v0.setStatus("current")

tmnxSatConsoleAccessGroupV20v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 5, 1)
)
tmnxSatConsoleAccessGroupV20v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatConsoleAccess"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatConsoleAccessStatus"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatFileTransferFtp"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatFileTransferScp"))
)
if mibBuilder.loadTexts:
    tmnxSatConsoleAccessGroupV20v0.setStatus("current")


# Notification objects

tmnxSatelliteOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 1)
)
tmnxSatelliteOperStateChange.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatNotifyFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteOperStateChange.setStatus(
        "current"
    )

tmnxSatSyncIfTimRefSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 2)
)
tmnxSatSyncIfTimRefSwitch.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1InUse"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2InUse"))
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRefSwitch.setStatus(
        "current"
    )

tmnxSatSyncIfTimSystemQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 3)
)
tmnxSatSyncIfTimSystemQuality.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingSystemQltyLvl")
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimSystemQuality.setStatus(
        "current"
    )

tmnxSatSyncIfTimRef1Quality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 4)
)
tmnxSatSyncIfTimRef1Quality.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef1RxQltyLvl")
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRef1Quality.setStatus(
        "current"
    )

tmnxSatSyncIfTimRef2Quality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 5)
)
tmnxSatSyncIfTimRef2Quality.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimingRef2RxQltyLvl")
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRef2Quality.setStatus(
        "current"
    )

tmnxSatSyncIfTimHoldover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 6)
)
tmnxSatSyncIfTimHoldover.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimHoldover.setStatus(
        "current"
    )

tmnxSatSyncIfTimHoldoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 7)
)
tmnxSatSyncIfTimHoldoverClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimHoldoverClear.setStatus(
        "current"
    )

tmnxSatSyncIfTimRef1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 8)
)
tmnxSatSyncIfTimRef1Alarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatNotifySyncIfTimRefAlarm"))
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRef1Alarm.setStatus(
        "current"
    )

tmnxSatSyncIfTimRef1AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 9)
)
tmnxSatSyncIfTimRef1AlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatNotifySyncIfTimRefAlarm"))
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRef1AlarmClear.setStatus(
        "current"
    )

tmnxSatSyncIfTimRef2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 10)
)
tmnxSatSyncIfTimRef2Alarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatNotifySyncIfTimRefAlarm"))
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRef2Alarm.setStatus(
        "current"
    )

tmnxSatSyncIfTimRef2AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 11)
)
tmnxSatSyncIfTimRef2AlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatNotifySyncIfTimRefAlarm"))
)
if mibBuilder.loadTexts:
    tmnxSatSyncIfTimRef2AlarmClear.setStatus(
        "current"
    )

tmnxSatLocalForwardStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 16)
)
tmnxSatLocalForwardStateChg.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardAdminState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardOperState"))
)
if mibBuilder.loadTexts:
    tmnxSatLocalForwardStateChg.setStatus(
        "current"
    )

tmnxSatLocalForwardSapStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 103, 0, 17)
)
tmnxSatLocalForwardSapStateChg.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardSapAdminState"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardSapOperState"))
)
if mibBuilder.loadTexts:
    tmnxSatLocalForwardSapStateChg.setStatus(
        "current"
    )


# Notifications groups

tmnxSatelliteNotifGroupV14v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 1, 5)
)
tmnxSatelliteNotifGroupV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatelliteOperStateChange"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRefSwitch"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimSystemQuality"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRef1Quality"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRef2Quality"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimHoldover"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimHoldoverClear"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRef1Alarm"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRef1AlarmClear"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRef2Alarm"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatSyncIfTimRef2AlarmClear"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteNotifGroupV14v0.setStatus(
        "current"
    )

tmnxSatelliteNotifGroupV15v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 2, 2, 6)
)
tmnxSatelliteNotifGroupV15v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardStateChg"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardSapStateChg"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteNotifGroupV15v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSatelliteComplianceV14v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 1, 1)
)
tmnxSatelliteComplianceV14v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatelliteGroupV14v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatelliteTypeGroupV14v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatellitePortMapGroupV14v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatelliteSyncIfTimGroupV14v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatelliteNotifGroupV14v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatelliteNotifyObjsGrpV14v0"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteComplianceV14v0.setStatus(
        "current"
    )

tmnxSatelliteComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 1, 2)
)
tmnxSatelliteComplianceV15v0.setObjects(
      *(("TIMETRA-SATELLITE-MIB", "tmnxSatPortMapGroupV15v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatResiliencyGroupV15v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatPortTemplateGroupV15v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatLocalForwardGroupV15v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatFeaturesGroupV15v0"),
        ("TIMETRA-SATELLITE-MIB", "tmnxSatelliteNotifGroupV15v0"))
)
if mibBuilder.loadTexts:
    tmnxSatelliteComplianceV15v0.setStatus(
        "current"
    )

tmnxSatelliteComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 1, 3)
)
tmnxSatelliteComplianceV16v0.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatPtpTcGroupV16v0")
)
if mibBuilder.loadTexts:
    tmnxSatelliteComplianceV16v0.setStatus(
        "current"
    )

tmnxSatelliteComplianceV19v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 1, 4)
)
tmnxSatelliteComplianceV19v0.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatClientDownDelayGroupV19v0")
)
if mibBuilder.loadTexts:
    tmnxSatelliteComplianceV19v0.setStatus(
        "current"
    )

tmnxSatelliteComplianceV20v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 103, 1, 5)
)
tmnxSatelliteComplianceV20v0.setObjects(
    ("TIMETRA-SATELLITE-MIB", "tmnxSatConsoleAccessGroupV20v0")
)
if mibBuilder.loadTexts:
    tmnxSatelliteComplianceV20v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SATELLITE-MIB",
    **{"TmnxSatelliteType": TmnxSatelliteType,
       "TmnxSatelliteConsoleAccessStatus": TmnxSatelliteConsoleAccessStatus,
       "timetraSatelliteMIBModule": timetraSatelliteMIBModule,
       "tmnxSatelliteConformance": tmnxSatelliteConformance,
       "tmnxSatelliteCompliances": tmnxSatelliteCompliances,
       "tmnxSatelliteComplianceV14v0": tmnxSatelliteComplianceV14v0,
       "tmnxSatelliteComplianceV15v0": tmnxSatelliteComplianceV15v0,
       "tmnxSatelliteComplianceV16v0": tmnxSatelliteComplianceV16v0,
       "tmnxSatelliteComplianceV19v0": tmnxSatelliteComplianceV19v0,
       "tmnxSatelliteComplianceV20v0": tmnxSatelliteComplianceV20v0,
       "tmnxSatelliteGroups": tmnxSatelliteGroups,
       "tmnxSatelliteV14v0Groups": tmnxSatelliteV14v0Groups,
       "tmnxSatelliteGroupV14v0": tmnxSatelliteGroupV14v0,
       "tmnxSatelliteTypeGroupV14v0": tmnxSatelliteTypeGroupV14v0,
       "tmnxSatellitePortMapGroupV14v0": tmnxSatellitePortMapGroupV14v0,
       "tmnxSatelliteSyncIfTimGroupV14v0": tmnxSatelliteSyncIfTimGroupV14v0,
       "tmnxSatelliteNotifGroupV14v0": tmnxSatelliteNotifGroupV14v0,
       "tmnxSatelliteNotifyObjsGrpV14v0": tmnxSatelliteNotifyObjsGrpV14v0,
       "tmnxSatelliteV15v0Groups": tmnxSatelliteV15v0Groups,
       "tmnxSatPortMapGroupV15v0": tmnxSatPortMapGroupV15v0,
       "tmnxSatResiliencyGroupV15v0": tmnxSatResiliencyGroupV15v0,
       "tmnxSatPortTemplateGroupV15v0": tmnxSatPortTemplateGroupV15v0,
       "tmnxSatLocalForwardGroupV15v0": tmnxSatLocalForwardGroupV15v0,
       "tmnxSatFeaturesGroupV15v0": tmnxSatFeaturesGroupV15v0,
       "tmnxSatelliteNotifGroupV15v0": tmnxSatelliteNotifGroupV15v0,
       "tmnxSatelliteV16v0Groups": tmnxSatelliteV16v0Groups,
       "tmnxSatPtpTcGroupV16v0": tmnxSatPtpTcGroupV16v0,
       "tmnxSatelliteV19v0Groups": tmnxSatelliteV19v0Groups,
       "tmnxSatClientDownDelayGroupV19v0": tmnxSatClientDownDelayGroupV19v0,
       "tmnxSatellite20v0Groups": tmnxSatellite20v0Groups,
       "tmnxSatConsoleAccessGroupV20v0": tmnxSatConsoleAccessGroupV20v0,
       "tmnxSatelliteObjs": tmnxSatelliteObjs,
       "tmnxSatelliteConfigTimestamps": tmnxSatelliteConfigTimestamps,
       "tmnxSatelliteTableLastChanged": tmnxSatelliteTableLastChanged,
       "tmnxSatPortMapConfigTableLastChg": tmnxSatPortMapConfigTableLastChg,
       "tmnxSatPortTemplateTableLastChg": tmnxSatPortTemplateTableLastChg,
       "tmnxSatPortTmplPortTableLastChg": tmnxSatPortTmplPortTableLastChg,
       "tmnxSatLocalForwardTableLastChg": tmnxSatLocalForwardTableLastChg,
       "tmnxSatLocalFwdSapTableLastChg": tmnxSatLocalFwdSapTableLastChg,
       "tmnxSatFeaturesTableLastChange": tmnxSatFeaturesTableLastChange,
       "tmnxSatelliteConfigurations": tmnxSatelliteConfigurations,
       "tmnxSatelliteTable": tmnxSatelliteTable,
       "tmnxSatelliteEntry": tmnxSatelliteEntry,
       "tmnxSatClass": tmnxSatClass,
       "tmnxSatId": tmnxSatId,
       "tmnxSatRowStatus": tmnxSatRowStatus,
       "tmnxSatLastChanged": tmnxSatLastChanged,
       "tmnxSatAssignedType": tmnxSatAssignedType,
       "tmnxSatEquippedType": tmnxSatEquippedType,
       "tmnxSatMacAddress": tmnxSatMacAddress,
       "tmnxSatSoftwareRepository": tmnxSatSoftwareRepository,
       "tmnxSatDescription": tmnxSatDescription,
       "tmnxSatReboot": tmnxSatReboot,
       "tmnxSatUpgrade": tmnxSatUpgrade,
       "tmnxSatSyncBootEnv": tmnxSatSyncBootEnv,
       "tmnxSatSyncEEnabled": tmnxSatSyncEEnabled,
       "tmnxSatPortTemplate": tmnxSatPortTemplate,
       "tmnxSatPtpTc": tmnxSatPtpTc,
       "tmnxSatClientDownDelay": tmnxSatClientDownDelay,
       "tmnxSatConsoleAccess": tmnxSatConsoleAccess,
       "tmnxSatConsoleAccessStatus": tmnxSatConsoleAccessStatus,
       "tmnxSatelliteStatus": tmnxSatelliteStatus,
       "tmnxSatelliteTypeTable": tmnxSatelliteTypeTable,
       "tmnxSatelliteTypeEntry": tmnxSatelliteTypeEntry,
       "tmnxSatTypeIndex": tmnxSatTypeIndex,
       "tmnxSatTypeClass": tmnxSatTypeClass,
       "tmnxSatTypeName": tmnxSatTypeName,
       "tmnxSatTypeDescription": tmnxSatTypeDescription,
       "tmnxSatellitePortMapTable": tmnxSatellitePortMapTable,
       "tmnxSatellitePortMapEntry": tmnxSatellitePortMapEntry,
       "tmnxSatClientPortId": tmnxSatClientPortId,
       "tmnxSatUplinkId": tmnxSatUplinkId,
       "tmnxSatUplinkPortId": tmnxSatUplinkPortId,
       "tmnxSatUplinkActive": tmnxSatUplinkActive,
       "tmnxSatHostPortId": tmnxSatHostPortId,
       "tmnxSatelliteSyncIfTimingTable": tmnxSatelliteSyncIfTimingTable,
       "tmnxSatelliteSyncIfTimingEntry": tmnxSatelliteSyncIfTimingEntry,
       "tmnxSatSyncIfTimingRef1SrcPort": tmnxSatSyncIfTimingRef1SrcPort,
       "tmnxSatSyncIfTimingRef1AdmStatus": tmnxSatSyncIfTimingRef1AdmStatus,
       "tmnxSatSyncIfTimingRef1InUse": tmnxSatSyncIfTimingRef1InUse,
       "tmnxSatSyncIfTimingRef1Qualified": tmnxSatSyncIfTimingRef1Qualified,
       "tmnxSatSyncIfTimingRef1Alarm": tmnxSatSyncIfTimingRef1Alarm,
       "tmnxSatSyncIfTimingRef1RxQltyLvl": tmnxSatSyncIfTimingRef1RxQltyLvl,
       "tmnxSatSyncIfTimingRef1State": tmnxSatSyncIfTimingRef1State,
       "tmnxSatSyncIfTimingRef2SrcPort": tmnxSatSyncIfTimingRef2SrcPort,
       "tmnxSatSyncIfTimingRef2AdmStatus": tmnxSatSyncIfTimingRef2AdmStatus,
       "tmnxSatSyncIfTimingRef2InUse": tmnxSatSyncIfTimingRef2InUse,
       "tmnxSatSyncIfTimingRef2Qualified": tmnxSatSyncIfTimingRef2Qualified,
       "tmnxSatSyncIfTimingRef2Alarm": tmnxSatSyncIfTimingRef2Alarm,
       "tmnxSatSyncIfTimingRef2RxQltyLvl": tmnxSatSyncIfTimingRef2RxQltyLvl,
       "tmnxSatSyncIfTimingRef2State": tmnxSatSyncIfTimingRef2State,
       "tmnxSatSyncIfTimingFreqOffset": tmnxSatSyncIfTimingFreqOffset,
       "tmnxSatSyncIfTimingStatus": tmnxSatSyncIfTimingStatus,
       "tmnxSatSyncIfTimingSystemQltyLvl": tmnxSatSyncIfTimingSystemQltyLvl,
       "tmnxSatelliteStatistics": tmnxSatelliteStatistics,
       "tmnxSatelliteNotifyObjects": tmnxSatelliteNotifyObjects,
       "tmnxSatNotifyFailureReason": tmnxSatNotifyFailureReason,
       "tmnxSatNotifySyncIfTimRefAlarm": tmnxSatNotifySyncIfTimRefAlarm,
       "tmnxSatellitePortMapConfigTable": tmnxSatellitePortMapConfigTable,
       "tmnxSatellitePortMapConfigEntry": tmnxSatellitePortMapConfigEntry,
       "tmnxSatPortMapConfigEntryLastChg": tmnxSatPortMapConfigEntryLastChg,
       "tmnxSatPrimaryUplinkPortId": tmnxSatPrimaryUplinkPortId,
       "tmnxSatSecondaryUplinkPortId": tmnxSatSecondaryUplinkPortId,
       "tmnxSatellitePortTemplateTable": tmnxSatellitePortTemplateTable,
       "tmnxSatellitePortTemplateEntry": tmnxSatellitePortTemplateEntry,
       "tmnxSatellitePortTemplateName": tmnxSatellitePortTemplateName,
       "tmnxSatPortTemplateRowStatus": tmnxSatPortTemplateRowStatus,
       "tmnxSatPortTemplateEntryLastChg": tmnxSatPortTemplateEntryLastChg,
       "tmnxSatPortTemplateSatType": tmnxSatPortTemplateSatType,
       "tmnxSatPortTemplateAdminState": tmnxSatPortTemplateAdminState,
       "tmnxSatPortTemplateDescription": tmnxSatPortTemplateDescription,
       "tmnxSatPortTemplatePortTable": tmnxSatPortTemplatePortTable,
       "tmnxSatPortTemplatePortEntry": tmnxSatPortTemplatePortEntry,
       "tmnxSatPhysPortId": tmnxSatPhysPortId,
       "tmnxSatPortTmplPortEntryLastChg": tmnxSatPortTmplPortEntryLastChg,
       "tmnxSatPortTemplatePortRole": tmnxSatPortTemplatePortRole,
       "tmnxSatPortTemplatePortUplink": tmnxSatPortTemplatePortUplink,
       "tmnxSatelliteLocalForwardTable": tmnxSatelliteLocalForwardTable,
       "tmnxSatelliteLocalForwardEntry": tmnxSatelliteLocalForwardEntry,
       "tmnxSatLocalForwardId": tmnxSatLocalForwardId,
       "tmnxSatLocalForwardRowStatus": tmnxSatLocalForwardRowStatus,
       "tmnxSatLocalForwardEntryLastChg": tmnxSatLocalForwardEntryLastChg,
       "tmnxSatLocalForwardAdminState": tmnxSatLocalForwardAdminState,
       "tmnxSatLocalForwardDescription": tmnxSatLocalForwardDescription,
       "tmnxSatLocalForwardOperState": tmnxSatLocalForwardOperState,
       "tmnxSatLocalForwardSapTable": tmnxSatLocalForwardSapTable,
       "tmnxSatLocalForwardSapEntry": tmnxSatLocalForwardSapEntry,
       "tmnxSatPortId": tmnxSatPortId,
       "tmnxSatEncapValue": tmnxSatEncapValue,
       "tmnxSatLocalForwardSapRowStatus": tmnxSatLocalForwardSapRowStatus,
       "tmnxSatLocalFwdSapEntryLastChg": tmnxSatLocalFwdSapEntryLastChg,
       "tmnxSatLocalForwardSapAdminState": tmnxSatLocalForwardSapAdminState,
       "tmnxSatLocalFwdSapDescription": tmnxSatLocalFwdSapDescription,
       "tmnxSatLocalForwardSapOperState": tmnxSatLocalForwardSapOperState,
       "tmnxSatelliteFeaturesTable": tmnxSatelliteFeaturesTable,
       "tmnxSatelliteFeaturesEntry": tmnxSatelliteFeaturesEntry,
       "tmnxSatFeaturesEntryLastChange": tmnxSatFeaturesEntryLastChange,
       "tmnxSatFeatureLocalForward": tmnxSatFeatureLocalForward,
       "tmnxSatFeaturePtpTc": tmnxSatFeaturePtpTc,
       "tmnxSatelliteSecurityObjs": tmnxSatelliteSecurityObjs,
       "tmnxSatFileTransferFtp": tmnxSatFileTransferFtp,
       "tmnxSatFileTransferScp": tmnxSatFileTransferScp,
       "tmnxSatelliteNotifyPrefix": tmnxSatelliteNotifyPrefix,
       "tmnxSatelliteNotifications": tmnxSatelliteNotifications,
       "tmnxSatelliteOperStateChange": tmnxSatelliteOperStateChange,
       "tmnxSatSyncIfTimRefSwitch": tmnxSatSyncIfTimRefSwitch,
       "tmnxSatSyncIfTimSystemQuality": tmnxSatSyncIfTimSystemQuality,
       "tmnxSatSyncIfTimRef1Quality": tmnxSatSyncIfTimRef1Quality,
       "tmnxSatSyncIfTimRef2Quality": tmnxSatSyncIfTimRef2Quality,
       "tmnxSatSyncIfTimHoldover": tmnxSatSyncIfTimHoldover,
       "tmnxSatSyncIfTimHoldoverClear": tmnxSatSyncIfTimHoldoverClear,
       "tmnxSatSyncIfTimRef1Alarm": tmnxSatSyncIfTimRef1Alarm,
       "tmnxSatSyncIfTimRef1AlarmClear": tmnxSatSyncIfTimRef1AlarmClear,
       "tmnxSatSyncIfTimRef2Alarm": tmnxSatSyncIfTimRef2Alarm,
       "tmnxSatSyncIfTimRef2AlarmClear": tmnxSatSyncIfTimRef2AlarmClear,
       "tmnxSatLocalForwardStateChg": tmnxSatLocalForwardStateChg,
       "tmnxSatLocalForwardSapStateChg": tmnxSatLocalForwardSapStateChg}
)
