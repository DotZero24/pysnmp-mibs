# SNMP MIB module (ALCATEL-ENT1-APP-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-APP-MON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:10 2025
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

(softentIND1AppMon,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1AppMon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alaAppMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1)
)
if mibBuilder.loadTexts:
    alaAppMonMIB.setRevisions(
        ("2014-01-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaAppMonMIBNotifications_ObjectIdentity = ObjectIdentity
alaAppMonMIBNotifications = _AlaAppMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 0)
)
_AlaAppMonMIBObjects_ObjectIdentity = ObjectIdentity
alaAppMonMIBObjects = _AlaAppMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1)
)
if mibBuilder.loadTexts:
    alaAppMonMIBObjects.setStatus("current")
_AlaAppMonCertConfig_ObjectIdentity = ObjectIdentity
alaAppMonCertConfig = _AlaAppMonCertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 1)
)


class _AlaAppMonUpdateSignatureFile_Type(Integer32):
    """Custom type alaAppMonUpdateSignatureFile based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("force", 2),
          ("autoCreat", 3),
          ("autoCreatForc", 4))
    )


_AlaAppMonUpdateSignatureFile_Type.__name__ = "Integer32"
_AlaAppMonUpdateSignatureFile_Object = MibScalar
alaAppMonUpdateSignatureFile = _AlaAppMonUpdateSignatureFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 1, 1),
    _AlaAppMonUpdateSignatureFile_Type()
)
alaAppMonUpdateSignatureFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonUpdateSignatureFile.setStatus("current")


class _AlaAppMonUpdateSignatureStatus_Type(Integer32):
    """Custom type alaAppMonUpdateSignatureStatus based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("failed", 4),
          ("timedOut", 5))
    )


_AlaAppMonUpdateSignatureStatus_Type.__name__ = "Integer32"
_AlaAppMonUpdateSignatureStatus_Object = MibScalar
alaAppMonUpdateSignatureStatus = _AlaAppMonUpdateSignatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 1, 2),
    _AlaAppMonUpdateSignatureStatus_Type()
)
alaAppMonUpdateSignatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonUpdateSignatureStatus.setStatus("current")
_AlaAppMonConfig_ObjectIdentity = ObjectIdentity
alaAppMonConfig = _AlaAppMonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2)
)


class _AlaAppMonAdminStatus_Type(Integer32):
    """Custom type alaAppMonAdminStatus based on Integer32"""
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


_AlaAppMonAdminStatus_Type.__name__ = "Integer32"
_AlaAppMonAdminStatus_Object = MibScalar
alaAppMonAdminStatus = _AlaAppMonAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 1),
    _AlaAppMonAdminStatus_Type()
)
alaAppMonAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAdminStatus.setStatus("current")


class _AlaAppMonUpdateAppList_Type(Integer32):
    """Custom type alaAppMonUpdateAppList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("apply", 2))
    )


_AlaAppMonUpdateAppList_Type.__name__ = "Integer32"
_AlaAppMonUpdateAppList_Object = MibScalar
alaAppMonUpdateAppList = _AlaAppMonUpdateAppList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 2),
    _AlaAppMonUpdateAppList_Type()
)
alaAppMonUpdateAppList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonUpdateAppList.setStatus("current")


class _AlaAppMonClearAppList_Type(Integer32):
    """Custom type alaAppMonClearAppList based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("clear", 2),
          ("enforcement", 3),
          ("monitor", 4))
    )


_AlaAppMonClearAppList_Type.__name__ = "Integer32"
_AlaAppMonClearAppList_Object = MibScalar
alaAppMonClearAppList = _AlaAppMonClearAppList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 3),
    _AlaAppMonClearAppList_Type()
)
alaAppMonClearAppList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonClearAppList.setStatus("current")


class _AlaAppMonFlowTableFlush_Type(Integer32):
    """Custom type alaAppMonFlowTableFlush based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("flush", 2),
          ("enforcement", 3),
          ("monitor", 4))
    )


_AlaAppMonFlowTableFlush_Type.__name__ = "Integer32"
_AlaAppMonFlowTableFlush_Object = MibScalar
alaAppMonFlowTableFlush = _AlaAppMonFlowTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 4),
    _AlaAppMonFlowTableFlush_Type()
)
alaAppMonFlowTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonFlowTableFlush.setStatus("current")


class _AlaAppMonAgingInterval_Type(Integer32):
    """Custom type alaAppMonAgingInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_AlaAppMonAgingInterval_Type.__name__ = "Integer32"
_AlaAppMonAgingInterval_Object = MibScalar
alaAppMonAgingInterval = _AlaAppMonAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 5),
    _AlaAppMonAgingInterval_Type()
)
alaAppMonAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAgingInterval.setStatus("current")
_AlaAppMonAppliedApplications_Type = Integer32
_AlaAppMonAppliedApplications_Object = MibScalar
alaAppMonAppliedApplications = _AlaAppMonAppliedApplications_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 6),
    _AlaAppMonAppliedApplications_Type()
)
alaAppMonAppliedApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppliedApplications.setStatus("current")
_AlaAppMonApplicationPoolApplications_Type = Integer32
_AlaAppMonApplicationPoolApplications_Object = MibScalar
alaAppMonApplicationPoolApplications = _AlaAppMonApplicationPoolApplications_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 7),
    _AlaAppMonApplicationPoolApplications_Type()
)
alaAppMonApplicationPoolApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonApplicationPoolApplications.setStatus("current")


class _AlaAppMonSignatureFileVersion_Type(SnmpAdminString):
    """Custom type alaAppMonSignatureFileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonSignatureFileVersion_Type.__name__ = "SnmpAdminString"
_AlaAppMonSignatureFileVersion_Object = MibScalar
alaAppMonSignatureFileVersion = _AlaAppMonSignatureFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 8),
    _AlaAppMonSignatureFileVersion_Type()
)
alaAppMonSignatureFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonSignatureFileVersion.setStatus("current")
_AlaAppMonSignatureFileAppCount_Type = Integer32
_AlaAppMonSignatureFileAppCount_Object = MibScalar
alaAppMonSignatureFileAppCount = _AlaAppMonSignatureFileAppCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 9),
    _AlaAppMonSignatureFileAppCount_Type()
)
alaAppMonSignatureFileAppCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonSignatureFileAppCount.setStatus("current")


class _AlaAppMonSignatureFileName_Type(SnmpAdminString):
    """Custom type alaAppMonSignatureFileName based on SnmpAdminString"""
    defaultValue = OctetString("/flash/UAppSig.upgrade_kit")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonSignatureFileName_Type.__name__ = "SnmpAdminString"
_AlaAppMonSignatureFileName_Object = MibScalar
alaAppMonSignatureFileName = _AlaAppMonSignatureFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 10),
    _AlaAppMonSignatureFileName_Type()
)
alaAppMonSignatureFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonSignatureFileName.setStatus("current")


class _AlaAppMonAppGrpFromAppName_Type(SnmpAdminString):
    """Custom type alaAppMonAppGrpFromAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonAppGrpFromAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppGrpFromAppName_Object = MibScalar
alaAppMonAppGrpFromAppName = _AlaAppMonAppGrpFromAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 11),
    _AlaAppMonAppGrpFromAppName_Type()
)
alaAppMonAppGrpFromAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAppGrpFromAppName.setStatus("current")


class _AlaAppMonAppGrpToAppName_Type(SnmpAdminString):
    """Custom type alaAppMonAppGrpToAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonAppGrpToAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppGrpToAppName_Object = MibScalar
alaAppMonAppGrpToAppName = _AlaAppMonAppGrpToAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 12),
    _AlaAppMonAppGrpToAppName_Type()
)
alaAppMonAppGrpToAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAppGrpToAppName.setStatus("current")


class _AlaAppMonAddAppGrpName_Type(SnmpAdminString):
    """Custom type alaAppMonAddAppGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonAddAppGrpName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAddAppGrpName_Object = MibScalar
alaAppMonAddAppGrpName = _AlaAppMonAddAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 13),
    _AlaAppMonAddAppGrpName_Type()
)
alaAppMonAddAppGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAddAppGrpName.setStatus("current")


class _AlaAppMonOperationalStatus_Type(Integer32):
    """Custom type alaAppMonOperationalStatus based on Integer32"""
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


_AlaAppMonOperationalStatus_Type.__name__ = "Integer32"
_AlaAppMonOperationalStatus_Object = MibScalar
alaAppMonOperationalStatus = _AlaAppMonOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 14),
    _AlaAppMonOperationalStatus_Type()
)
alaAppMonOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonOperationalStatus.setStatus("current")


class _AlaAppMonForceFlowSyncStatus_Type(Integer32):
    """Custom type alaAppMonForceFlowSyncStatus based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("sync", 2),
          ("enforcement", 3),
          ("monitor", 4))
    )


_AlaAppMonForceFlowSyncStatus_Type.__name__ = "Integer32"
_AlaAppMonForceFlowSyncStatus_Object = MibScalar
alaAppMonForceFlowSyncStatus = _AlaAppMonForceFlowSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 15),
    _AlaAppMonForceFlowSyncStatus_Type()
)
alaAppMonForceFlowSyncStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonForceFlowSyncStatus.setStatus("current")


class _AlaAppMonAutoGroupCreation_Type(Integer32):
    """Custom type alaAppMonAutoGroupCreation based on Integer32"""
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


_AlaAppMonAutoGroupCreation_Type.__name__ = "Integer32"
_AlaAppMonAutoGroupCreation_Object = MibScalar
alaAppMonAutoGroupCreation = _AlaAppMonAutoGroupCreation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 16),
    _AlaAppMonAutoGroupCreation_Type()
)
alaAppMonAutoGroupCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAutoGroupCreation.setStatus("current")


class _AlaAppMonLoggingThresholdFlows_Type(Integer32):
    """Custom type alaAppMonLoggingThresholdFlows based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 20000),
    )


_AlaAppMonLoggingThresholdFlows_Type.__name__ = "Integer32"
_AlaAppMonLoggingThresholdFlows_Object = MibScalar
alaAppMonLoggingThresholdFlows = _AlaAppMonLoggingThresholdFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 17),
    _AlaAppMonLoggingThresholdFlows_Type()
)
alaAppMonLoggingThresholdFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonLoggingThresholdFlows.setStatus("current")


class _AlaAppMonAddRemoveAppGrpName_Type(Integer32):
    """Custom type alaAppMonAddRemoveAppGrpName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_AlaAppMonAddRemoveAppGrpName_Type.__name__ = "Integer32"
_AlaAppMonAddRemoveAppGrpName_Object = MibScalar
alaAppMonAddRemoveAppGrpName = _AlaAppMonAddRemoveAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 18),
    _AlaAppMonAddRemoveAppGrpName_Type()
)
alaAppMonAddRemoveAppGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonAddRemoveAppGrpName.setStatus("current")
_AlaAppMonAOSCompatibilityVersion_Type = Integer32
_AlaAppMonAOSCompatibilityVersion_Object = MibScalar
alaAppMonAOSCompatibilityVersion = _AlaAppMonAOSCompatibilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 19),
    _AlaAppMonAOSCompatibilityVersion_Type()
)
alaAppMonAOSCompatibilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAOSCompatibilityVersion.setStatus("current")


class _AlaAppMonKitType_Type(Integer32):
    """Custom type alaAppMonKitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("production", 1),
          ("factory", 2))
    )


_AlaAppMonKitType_Type.__name__ = "Integer32"
_AlaAppMonKitType_Object = MibScalar
alaAppMonKitType = _AlaAppMonKitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 20),
    _AlaAppMonKitType_Type()
)
alaAppMonKitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonKitType.setStatus("current")


class _AlaAppMonUpgradedKitType_Type(Integer32):
    """Custom type alaAppMonUpgradedKitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("production", 1),
          ("factory", 2))
    )


_AlaAppMonUpgradedKitType_Type.__name__ = "Integer32"
_AlaAppMonUpgradedKitType_Object = MibScalar
alaAppMonUpgradedKitType = _AlaAppMonUpgradedKitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 21),
    _AlaAppMonUpgradedKitType_Type()
)
alaAppMonUpgradedKitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonUpgradedKitType.setStatus("current")


class _AlaAppMonUpgradedSignatureFileVersion_Type(SnmpAdminString):
    """Custom type alaAppMonUpgradedSignatureFileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonUpgradedSignatureFileVersion_Type.__name__ = "SnmpAdminString"
_AlaAppMonUpgradedSignatureFileVersion_Object = MibScalar
alaAppMonUpgradedSignatureFileVersion = _AlaAppMonUpgradedSignatureFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 22),
    _AlaAppMonUpgradedSignatureFileVersion_Type()
)
alaAppMonUpgradedSignatureFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonUpgradedSignatureFileVersion.setStatus("current")


class _AlaAppMonClearConfig_Type(Integer32):
    """Custom type alaAppMonClearConfig based on Integer32"""
    defaultValue = 2

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


_AlaAppMonClearConfig_Type.__name__ = "Integer32"
_AlaAppMonClearConfig_Object = MibScalar
alaAppMonClearConfig = _AlaAppMonClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 23),
    _AlaAppMonClearConfig_Type()
)
alaAppMonClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonClearConfig.setStatus("current")


class _AlaAppMonEnforcementIpv4_Type(Integer32):
    """Custom type alaAppMonEnforcementIpv4 based on Integer32"""
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


_AlaAppMonEnforcementIpv4_Type.__name__ = "Integer32"
_AlaAppMonEnforcementIpv4_Object = MibScalar
alaAppMonEnforcementIpv4 = _AlaAppMonEnforcementIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 24),
    _AlaAppMonEnforcementIpv4_Type()
)
alaAppMonEnforcementIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementIpv4.setStatus("current")


class _AlaAppMonEnforcementIpv6_Type(Integer32):
    """Custom type alaAppMonEnforcementIpv6 based on Integer32"""
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


_AlaAppMonEnforcementIpv6_Type.__name__ = "Integer32"
_AlaAppMonEnforcementIpv6_Object = MibScalar
alaAppMonEnforcementIpv6 = _AlaAppMonEnforcementIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 25),
    _AlaAppMonEnforcementIpv6_Type()
)
alaAppMonEnforcementIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementIpv6.setStatus("current")


class _AlaAppMonEnforcementFlowTableStatsAdminStatus_Type(Integer32):
    """Custom type alaAppMonEnforcementFlowTableStatsAdminStatus based on Integer32"""
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


_AlaAppMonEnforcementFlowTableStatsAdminStatus_Type.__name__ = "Integer32"
_AlaAppMonEnforcementFlowTableStatsAdminStatus_Object = MibScalar
alaAppMonEnforcementFlowTableStatsAdminStatus = _AlaAppMonEnforcementFlowTableStatsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 26),
    _AlaAppMonEnforcementFlowTableStatsAdminStatus_Type()
)
alaAppMonEnforcementFlowTableStatsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowTableStatsAdminStatus.setStatus("current")


class _AlaAppMonEnforcementStatsInterval_Type(Integer32):
    """Custom type alaAppMonEnforcementStatsInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 3600),
    )


_AlaAppMonEnforcementStatsInterval_Type.__name__ = "Integer32"
_AlaAppMonEnforcementStatsInterval_Object = MibScalar
alaAppMonEnforcementStatsInterval = _AlaAppMonEnforcementStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 27),
    _AlaAppMonEnforcementStatsInterval_Type()
)
alaAppMonEnforcementStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementStatsInterval.setStatus("deprecated")


class _AlaAppMonEnforcementLoggingThresholdFlows_Type(Integer32):
    """Custom type alaAppMonEnforcementLoggingThresholdFlows based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 60000),
    )


_AlaAppMonEnforcementLoggingThresholdFlows_Type.__name__ = "Integer32"
_AlaAppMonEnforcementLoggingThresholdFlows_Object = MibScalar
alaAppMonEnforcementLoggingThresholdFlows = _AlaAppMonEnforcementLoggingThresholdFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 28),
    _AlaAppMonEnforcementLoggingThresholdFlows_Type()
)
alaAppMonEnforcementLoggingThresholdFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementLoggingThresholdFlows.setStatus("current")


class _AlaAppMonFlowSyncEnforcementInterval_Type(Integer32):
    """Custom type alaAppMonFlowSyncEnforcementInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AlaAppMonFlowSyncEnforcementInterval_Type.__name__ = "Integer32"
_AlaAppMonFlowSyncEnforcementInterval_Object = MibScalar
alaAppMonFlowSyncEnforcementInterval = _AlaAppMonFlowSyncEnforcementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 29),
    _AlaAppMonFlowSyncEnforcementInterval_Type()
)
alaAppMonFlowSyncEnforcementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonFlowSyncEnforcementInterval.setStatus("current")


class _AlaAppMonFlowSyncMonitorInterval_Type(Integer32):
    """Custom type alaAppMonFlowSyncMonitorInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AlaAppMonFlowSyncMonitorInterval_Type.__name__ = "Integer32"
_AlaAppMonFlowSyncMonitorInterval_Object = MibScalar
alaAppMonFlowSyncMonitorInterval = _AlaAppMonFlowSyncMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 30),
    _AlaAppMonFlowSyncMonitorInterval_Type()
)
alaAppMonFlowSyncMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonFlowSyncMonitorInterval.setStatus("current")
_AlaAppMonEnforcementAppliedApplications_Type = Integer32
_AlaAppMonEnforcementAppliedApplications_Object = MibScalar
alaAppMonEnforcementAppliedApplications = _AlaAppMonEnforcementAppliedApplications_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 2, 31),
    _AlaAppMonEnforcementAppliedApplications_Type()
)
alaAppMonEnforcementAppliedApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppliedApplications.setStatus("current")
_AlaAppMonPortConfigTable_Object = MibTable
alaAppMonPortConfigTable = _AlaAppMonPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaAppMonPortConfigTable.setStatus("current")
_AlaAppMonPortConfigEntry_Object = MibTableRow
alaAppMonPortConfigEntry = _AlaAppMonPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3, 1)
)
alaAppMonPortConfigEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonPortConfigSlotPortIndex"),
)
if mibBuilder.loadTexts:
    alaAppMonPortConfigEntry.setStatus("current")
_AlaAppMonPortConfigSlotPortIndex_Type = InterfaceIndex
_AlaAppMonPortConfigSlotPortIndex_Object = MibTableColumn
alaAppMonPortConfigSlotPortIndex = _AlaAppMonPortConfigSlotPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3, 1, 1),
    _AlaAppMonPortConfigSlotPortIndex_Type()
)
alaAppMonPortConfigSlotPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonPortConfigSlotPortIndex.setStatus("current")


class _AlaAppMonPortConfigPortStatus_Type(Integer32):
    """Custom type alaAppMonPortConfigPortStatus based on Integer32"""
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


_AlaAppMonPortConfigPortStatus_Type.__name__ = "Integer32"
_AlaAppMonPortConfigPortStatus_Object = MibTableColumn
alaAppMonPortConfigPortStatus = _AlaAppMonPortConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3, 1, 2),
    _AlaAppMonPortConfigPortStatus_Type()
)
alaAppMonPortConfigPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonPortConfigPortStatus.setStatus("current")


class _AlaAppMonPortConfigOperStatus_Type(Integer32):
    """Custom type alaAppMonPortConfigOperStatus based on Integer32"""
    defaultValue = 2

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


_AlaAppMonPortConfigOperStatus_Type.__name__ = "Integer32"
_AlaAppMonPortConfigOperStatus_Object = MibTableColumn
alaAppMonPortConfigOperStatus = _AlaAppMonPortConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3, 1, 3),
    _AlaAppMonPortConfigOperStatus_Type()
)
alaAppMonPortConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonPortConfigOperStatus.setStatus("current")


class _AlaAppMonEnforcementPortConfigTcpStatus_Type(Integer32):
    """Custom type alaAppMonEnforcementPortConfigTcpStatus based on Integer32"""
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


_AlaAppMonEnforcementPortConfigTcpStatus_Type.__name__ = "Integer32"
_AlaAppMonEnforcementPortConfigTcpStatus_Object = MibTableColumn
alaAppMonEnforcementPortConfigTcpStatus = _AlaAppMonEnforcementPortConfigTcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3, 1, 4),
    _AlaAppMonEnforcementPortConfigTcpStatus_Type()
)
alaAppMonEnforcementPortConfigTcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementPortConfigTcpStatus.setStatus("current")


class _AlaAppMonEnforcementPortConfigUdpStatus_Type(Integer32):
    """Custom type alaAppMonEnforcementPortConfigUdpStatus based on Integer32"""
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


_AlaAppMonEnforcementPortConfigUdpStatus_Type.__name__ = "Integer32"
_AlaAppMonEnforcementPortConfigUdpStatus_Object = MibTableColumn
alaAppMonEnforcementPortConfigUdpStatus = _AlaAppMonEnforcementPortConfigUdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 3, 1, 5),
    _AlaAppMonEnforcementPortConfigUdpStatus_Type()
)
alaAppMonEnforcementPortConfigUdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementPortConfigUdpStatus.setStatus("current")
_AlaAppMonAppPoolTable_Object = MibTable
alaAppMonAppPoolTable = _AlaAppMonAppPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaAppMonAppPoolTable.setStatus("current")
_AlaAppMonAppPoolEntry_Object = MibTableRow
alaAppMonAppPoolEntry = _AlaAppMonAppPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4, 1)
)
alaAppMonAppPoolEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppPoolAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonAppPoolEntry.setStatus("current")


class _AlaAppMonAppPoolAppName_Type(SnmpAdminString):
    """Custom type alaAppMonAppPoolAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonAppPoolAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppPoolAppName_Object = MibTableColumn
alaAppMonAppPoolAppName = _AlaAppMonAppPoolAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4, 1, 1),
    _AlaAppMonAppPoolAppName_Type()
)
alaAppMonAppPoolAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonAppPoolAppName.setStatus("current")


class _AlaAppMonAppPoolCategory_Type(SnmpAdminString):
    """Custom type alaAppMonAppPoolCategory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonAppPoolCategory_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppPoolCategory_Object = MibTableColumn
alaAppMonAppPoolCategory = _AlaAppMonAppPoolCategory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4, 1, 2),
    _AlaAppMonAppPoolCategory_Type()
)
alaAppMonAppPoolCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppPoolCategory.setStatus("current")


class _AlaAppMonAppPoolRevision_Type(SnmpAdminString):
    """Custom type alaAppMonAppPoolRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AlaAppMonAppPoolRevision_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppPoolRevision_Object = MibTableColumn
alaAppMonAppPoolRevision = _AlaAppMonAppPoolRevision_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4, 1, 3),
    _AlaAppMonAppPoolRevision_Type()
)
alaAppMonAppPoolRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppPoolRevision.setStatus("current")


class _AlaAppMonAppPoolAppStatus_Type(Integer32):
    """Custom type alaAppMonAppPoolAppStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AlaAppMonAppPoolAppStatus_Type.__name__ = "Integer32"
_AlaAppMonAppPoolAppStatus_Object = MibTableColumn
alaAppMonAppPoolAppStatus = _AlaAppMonAppPoolAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4, 1, 4),
    _AlaAppMonAppPoolAppStatus_Type()
)
alaAppMonAppPoolAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppPoolAppStatus.setStatus("current")
_AlaAppMonEnforcementAppPoolAppID_Type = Integer32
_AlaAppMonEnforcementAppPoolAppID_Object = MibTableColumn
alaAppMonEnforcementAppPoolAppID = _AlaAppMonEnforcementAppPoolAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 4, 1, 5),
    _AlaAppMonEnforcementAppPoolAppID_Type()
)
alaAppMonEnforcementAppPoolAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppPoolAppID.setStatus("current")
_AlaAppMonAppGroupTable_Object = MibTable
alaAppMonAppGroupTable = _AlaAppMonAppGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaAppMonAppGroupTable.setStatus("current")
_AlaAppMonAppGroupEntry_Object = MibTableRow
alaAppMonAppGroupEntry = _AlaAppMonAppGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1)
)
alaAppMonAppGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupName"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupMember"),
)
if mibBuilder.loadTexts:
    alaAppMonAppGroupEntry.setStatus("current")


class _AlaAppMonAppGroupName_Type(SnmpAdminString):
    """Custom type alaAppMonAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppGroupName_Object = MibTableColumn
alaAppMonAppGroupName = _AlaAppMonAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 1),
    _AlaAppMonAppGroupName_Type()
)
alaAppMonAppGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonAppGroupName.setStatus("current")


class _AlaAppMonAppGroupMember_Type(SnmpAdminString):
    """Custom type alaAppMonAppGroupMember based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonAppGroupMember_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppGroupMember_Object = MibTableColumn
alaAppMonAppGroupMember = _AlaAppMonAppGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 2),
    _AlaAppMonAppGroupMember_Type()
)
alaAppMonAppGroupMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonAppGroupMember.setStatus("current")


class _AlaAppMonAppGroupBuiltIn_Type(Integer32):
    """Custom type alaAppMonAppGroupBuiltIn based on Integer32"""
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


_AlaAppMonAppGroupBuiltIn_Type.__name__ = "Integer32"
_AlaAppMonAppGroupBuiltIn_Object = MibTableColumn
alaAppMonAppGroupBuiltIn = _AlaAppMonAppGroupBuiltIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 3),
    _AlaAppMonAppGroupBuiltIn_Type()
)
alaAppMonAppGroupBuiltIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonAppGroupBuiltIn.setStatus("current")


class _AlaAppMonAppGroupCategoryName_Type(SnmpAdminString):
    """Custom type alaAppMonAppGroupCategoryName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonAppGroupCategoryName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppGroupCategoryName_Object = MibTableColumn
alaAppMonAppGroupCategoryName = _AlaAppMonAppGroupCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 4),
    _AlaAppMonAppGroupCategoryName_Type()
)
alaAppMonAppGroupCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppGroupCategoryName.setStatus("current")
_AlaAppMonAppGrpId_Type = Integer32
_AlaAppMonAppGrpId_Object = MibTableColumn
alaAppMonAppGrpId = _AlaAppMonAppGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 5),
    _AlaAppMonAppGrpId_Type()
)
alaAppMonAppGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppGrpId.setStatus("current")


class _AlaAppMonAppGroupAppStatus_Type(Integer32):
    """Custom type alaAppMonAppGroupAppStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AlaAppMonAppGroupAppStatus_Type.__name__ = "Integer32"
_AlaAppMonAppGroupAppStatus_Object = MibTableColumn
alaAppMonAppGroupAppStatus = _AlaAppMonAppGroupAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 6),
    _AlaAppMonAppGroupAppStatus_Type()
)
alaAppMonAppGroupAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppGroupAppStatus.setStatus("current")
_AlaAppMonAppGroupStatus_Type = RowStatus
_AlaAppMonAppGroupStatus_Object = MibTableColumn
alaAppMonAppGroupStatus = _AlaAppMonAppGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 5, 1, 7),
    _AlaAppMonAppGroupStatus_Type()
)
alaAppMonAppGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonAppGroupStatus.setStatus("current")
_AlaAppMonAppListTable_Object = MibTable
alaAppMonAppListTable = _AlaAppMonAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaAppMonAppListTable.setStatus("current")
_AlaAppMonAppListEntry_Object = MibTableRow
alaAppMonAppListEntry = _AlaAppMonAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6, 1)
)
alaAppMonAppListEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListMemberName"),
)
if mibBuilder.loadTexts:
    alaAppMonAppListEntry.setStatus("current")


class _AlaAppMonAppListMemberName_Type(SnmpAdminString):
    """Custom type alaAppMonAppListMemberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonAppListMemberName_Type.__name__ = "SnmpAdminString"
_AlaAppMonAppListMemberName_Object = MibTableColumn
alaAppMonAppListMemberName = _AlaAppMonAppListMemberName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6, 1, 1),
    _AlaAppMonAppListMemberName_Type()
)
alaAppMonAppListMemberName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonAppListMemberName.setStatus("current")


class _AlaAppMonAppListMemberType_Type(Integer32):
    """Custom type alaAppMonAppListMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("application", 1),
          ("applicationGroup", 2))
    )


_AlaAppMonAppListMemberType_Type.__name__ = "Integer32"
_AlaAppMonAppListMemberType_Object = MibTableColumn
alaAppMonAppListMemberType = _AlaAppMonAppListMemberType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6, 1, 2),
    _AlaAppMonAppListMemberType_Type()
)
alaAppMonAppListMemberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonAppListMemberType.setStatus("current")
_AlaAppMonAppListAppId_Type = Integer32
_AlaAppMonAppListAppId_Object = MibTableColumn
alaAppMonAppListAppId = _AlaAppMonAppListAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6, 1, 3),
    _AlaAppMonAppListAppId_Type()
)
alaAppMonAppListAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppListAppId.setStatus("current")


class _AlaAppMonAppListAppStatus_Type(Integer32):
    """Custom type alaAppMonAppListAppStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AlaAppMonAppListAppStatus_Type.__name__ = "Integer32"
_AlaAppMonAppListAppStatus_Object = MibTableColumn
alaAppMonAppListAppStatus = _AlaAppMonAppListAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6, 1, 4),
    _AlaAppMonAppListAppStatus_Type()
)
alaAppMonAppListAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppListAppStatus.setStatus("current")
_AlaAppMonAppListMemberStatus_Type = RowStatus
_AlaAppMonAppListMemberStatus_Object = MibTableColumn
alaAppMonAppListMemberStatus = _AlaAppMonAppListMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 6, 1, 5),
    _AlaAppMonAppListMemberStatus_Type()
)
alaAppMonAppListMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonAppListMemberStatus.setStatus("current")
_AlaAppMonActiveAppListTable_Object = MibTable
alaAppMonActiveAppListTable = _AlaAppMonActiveAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaAppMonActiveAppListTable.setStatus("current")
_AlaAppMonActiveAppListEntry_Object = MibTableRow
alaAppMonActiveAppListEntry = _AlaAppMonActiveAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7, 1)
)
alaAppMonActiveAppListEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonActiveAppListAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonActiveAppListEntry.setStatus("current")


class _AlaAppMonActiveAppListAppName_Type(SnmpAdminString):
    """Custom type alaAppMonActiveAppListAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonActiveAppListAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonActiveAppListAppName_Object = MibTableColumn
alaAppMonActiveAppListAppName = _AlaAppMonActiveAppListAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7, 1, 1),
    _AlaAppMonActiveAppListAppName_Type()
)
alaAppMonActiveAppListAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonActiveAppListAppName.setStatus("current")


class _AlaAppMonActiveAppListAppGroupName_Type(SnmpAdminString):
    """Custom type alaAppMonActiveAppListAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAppMonActiveAppListAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaAppMonActiveAppListAppGroupName_Object = MibTableColumn
alaAppMonActiveAppListAppGroupName = _AlaAppMonActiveAppListAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7, 1, 2),
    _AlaAppMonActiveAppListAppGroupName_Type()
)
alaAppMonActiveAppListAppGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonActiveAppListAppGroupName.setStatus("current")
_AlaAppMonActiveAppListActiveFlowCount_Type = Counter32
_AlaAppMonActiveAppListActiveFlowCount_Object = MibTableColumn
alaAppMonActiveAppListActiveFlowCount = _AlaAppMonActiveAppListActiveFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7, 1, 3),
    _AlaAppMonActiveAppListActiveFlowCount_Type()
)
alaAppMonActiveAppListActiveFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonActiveAppListActiveFlowCount.setStatus("current")
_AlaAppMonActiveAppListAppId_Type = Integer32
_AlaAppMonActiveAppListAppId_Object = MibTableColumn
alaAppMonActiveAppListAppId = _AlaAppMonActiveAppListAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7, 1, 4),
    _AlaAppMonActiveAppListAppId_Type()
)
alaAppMonActiveAppListAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonActiveAppListAppId.setStatus("current")


class _AlaAppMonActiveAppListAppStatus_Type(Integer32):
    """Custom type alaAppMonActiveAppListAppStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AlaAppMonActiveAppListAppStatus_Type.__name__ = "Integer32"
_AlaAppMonActiveAppListAppStatus_Object = MibTableColumn
alaAppMonActiveAppListAppStatus = _AlaAppMonActiveAppListAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 7, 1, 5),
    _AlaAppMonActiveAppListAppStatus_Type()
)
alaAppMonActiveAppListAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonActiveAppListAppStatus.setStatus("current")
_AlaAppMonSignatureFileTable_Object = MibTable
alaAppMonSignatureFileTable = _AlaAppMonSignatureFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaAppMonSignatureFileTable.setStatus("current")
_AlaAppMonSignatureFileEntry_Object = MibTableRow
alaAppMonSignatureFileEntry = _AlaAppMonSignatureFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 8, 1)
)
alaAppMonSignatureFileEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonSignatureFileAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonSignatureFileEntry.setStatus("current")


class _AlaAppMonSignatureFileAppName_Type(SnmpAdminString):
    """Custom type alaAppMonSignatureFileAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonSignatureFileAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonSignatureFileAppName_Object = MibTableColumn
alaAppMonSignatureFileAppName = _AlaAppMonSignatureFileAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 8, 1, 1),
    _AlaAppMonSignatureFileAppName_Type()
)
alaAppMonSignatureFileAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonSignatureFileAppName.setStatus("current")


class _AlaAppMonSignatureFileCategory_Type(SnmpAdminString):
    """Custom type alaAppMonSignatureFileCategory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonSignatureFileCategory_Type.__name__ = "SnmpAdminString"
_AlaAppMonSignatureFileCategory_Object = MibTableColumn
alaAppMonSignatureFileCategory = _AlaAppMonSignatureFileCategory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 8, 1, 2),
    _AlaAppMonSignatureFileCategory_Type()
)
alaAppMonSignatureFileCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonSignatureFileCategory.setStatus("current")
_AlaAppMonFlowTable_Object = MibTable
alaAppMonFlowTable = _AlaAppMonFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaAppMonFlowTable.setStatus("current")
_AlaAppMonFlowEntry_Object = MibTableRow
alaAppMonFlowEntry = _AlaAppMonFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1)
)
alaAppMonFlowEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowSourceIPType"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowSourceIP"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowSrcPort"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowDestIPType"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowDestIP"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowDestPort"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowProtocol"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonFlowEntry.setStatus("current")


class _AlaAppMonFlowSourceIPType_Type(InetAddressType):
    """Custom type alaAppMonFlowSourceIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaAppMonFlowSourceIPType_Type.__name__ = "InetAddressType"
_AlaAppMonFlowSourceIPType_Object = MibTableColumn
alaAppMonFlowSourceIPType = _AlaAppMonFlowSourceIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 1),
    _AlaAppMonFlowSourceIPType_Type()
)
alaAppMonFlowSourceIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowSourceIPType.setStatus("current")


class _AlaAppMonFlowSourceIP_Type(InetAddress):
    """Custom type alaAppMonFlowSourceIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaAppMonFlowSourceIP_Type.__name__ = "InetAddress"
_AlaAppMonFlowSourceIP_Object = MibTableColumn
alaAppMonFlowSourceIP = _AlaAppMonFlowSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 2),
    _AlaAppMonFlowSourceIP_Type()
)
alaAppMonFlowSourceIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowSourceIP.setStatus("current")


class _AlaAppMonFlowSrcPort_Type(Integer32):
    """Custom type alaAppMonFlowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaAppMonFlowSrcPort_Type.__name__ = "Integer32"
_AlaAppMonFlowSrcPort_Object = MibTableColumn
alaAppMonFlowSrcPort = _AlaAppMonFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 3),
    _AlaAppMonFlowSrcPort_Type()
)
alaAppMonFlowSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowSrcPort.setStatus("current")


class _AlaAppMonFlowDestIPType_Type(InetAddressType):
    """Custom type alaAppMonFlowDestIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaAppMonFlowDestIPType_Type.__name__ = "InetAddressType"
_AlaAppMonFlowDestIPType_Object = MibTableColumn
alaAppMonFlowDestIPType = _AlaAppMonFlowDestIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 4),
    _AlaAppMonFlowDestIPType_Type()
)
alaAppMonFlowDestIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowDestIPType.setStatus("current")


class _AlaAppMonFlowDestIP_Type(InetAddress):
    """Custom type alaAppMonFlowDestIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaAppMonFlowDestIP_Type.__name__ = "InetAddress"
_AlaAppMonFlowDestIP_Object = MibTableColumn
alaAppMonFlowDestIP = _AlaAppMonFlowDestIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 5),
    _AlaAppMonFlowDestIP_Type()
)
alaAppMonFlowDestIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowDestIP.setStatus("current")


class _AlaAppMonFlowDestPort_Type(Integer32):
    """Custom type alaAppMonFlowDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaAppMonFlowDestPort_Type.__name__ = "Integer32"
_AlaAppMonFlowDestPort_Object = MibTableColumn
alaAppMonFlowDestPort = _AlaAppMonFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 6),
    _AlaAppMonFlowDestPort_Type()
)
alaAppMonFlowDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowDestPort.setStatus("current")


class _AlaAppMonFlowProtocol_Type(Integer32):
    """Custom type alaAppMonFlowProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_AlaAppMonFlowProtocol_Type.__name__ = "Integer32"
_AlaAppMonFlowProtocol_Object = MibTableColumn
alaAppMonFlowProtocol = _AlaAppMonFlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 7),
    _AlaAppMonFlowProtocol_Type()
)
alaAppMonFlowProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowProtocol.setStatus("current")


class _AlaAppMonFlowAppName_Type(SnmpAdminString):
    """Custom type alaAppMonFlowAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonFlowAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonFlowAppName_Object = MibTableColumn
alaAppMonFlowAppName = _AlaAppMonFlowAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 8),
    _AlaAppMonFlowAppName_Type()
)
alaAppMonFlowAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonFlowAppName.setStatus("current")


class _AlaAppMonFlowAppGrpName_Type(SnmpAdminString):
    """Custom type alaAppMonFlowAppGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonFlowAppGrpName_Type.__name__ = "SnmpAdminString"
_AlaAppMonFlowAppGrpName_Object = MibTableColumn
alaAppMonFlowAppGrpName = _AlaAppMonFlowAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 9, 1, 9),
    _AlaAppMonFlowAppGrpName_Type()
)
alaAppMonFlowAppGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonFlowAppGrpName.setStatus("current")
_AlaAppMonCurrentHourTable_Object = MibTable
alaAppMonCurrentHourTable = _AlaAppMonCurrentHourTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaAppMonCurrentHourTable.setStatus("current")
_AlaAppMonCurrentHourEntry_Object = MibTableRow
alaAppMonCurrentHourEntry = _AlaAppMonCurrentHourEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1)
)
alaAppMonCurrentHourEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHourAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonCurrentHourEntry.setStatus("current")
_AlaAppMonCurrentHourAppName_Type = SnmpAdminString
_AlaAppMonCurrentHourAppName_Object = MibTableColumn
alaAppMonCurrentHourAppName = _AlaAppMonCurrentHourAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1, 1),
    _AlaAppMonCurrentHourAppName_Type()
)
alaAppMonCurrentHourAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonCurrentHourAppName.setStatus("current")
_AlaAppMonCurrentHourAppGroupName_Type = SnmpAdminString
_AlaAppMonCurrentHourAppGroupName_Object = MibTableColumn
alaAppMonCurrentHourAppGroupName = _AlaAppMonCurrentHourAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1, 2),
    _AlaAppMonCurrentHourAppGroupName_Type()
)
alaAppMonCurrentHourAppGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonCurrentHourAppGroupName.setStatus("current")
_AlaAppMonCurrentHrStatsMinActiveFlow_Type = Counter32
_AlaAppMonCurrentHrStatsMinActiveFlow_Object = MibTableColumn
alaAppMonCurrentHrStatsMinActiveFlow = _AlaAppMonCurrentHrStatsMinActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1, 3),
    _AlaAppMonCurrentHrStatsMinActiveFlow_Type()
)
alaAppMonCurrentHrStatsMinActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonCurrentHrStatsMinActiveFlow.setStatus("current")
_AlaAppMonCurrentHrStatsMaxActiveFlow_Type = Counter32
_AlaAppMonCurrentHrStatsMaxActiveFlow_Object = MibTableColumn
alaAppMonCurrentHrStatsMaxActiveFlow = _AlaAppMonCurrentHrStatsMaxActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1, 4),
    _AlaAppMonCurrentHrStatsMaxActiveFlow_Type()
)
alaAppMonCurrentHrStatsMaxActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonCurrentHrStatsMaxActiveFlow.setStatus("current")
_AlaAppMonCurrentHrStatsAvgActiveFlow_Type = Counter32
_AlaAppMonCurrentHrStatsAvgActiveFlow_Object = MibTableColumn
alaAppMonCurrentHrStatsAvgActiveFlow = _AlaAppMonCurrentHrStatsAvgActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1, 5),
    _AlaAppMonCurrentHrStatsAvgActiveFlow_Type()
)
alaAppMonCurrentHrStatsAvgActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonCurrentHrStatsAvgActiveFlow.setStatus("current")
_AlaAppMonCurrentHrStatsTotalFlow_Type = Counter32
_AlaAppMonCurrentHrStatsTotalFlow_Object = MibTableColumn
alaAppMonCurrentHrStatsTotalFlow = _AlaAppMonCurrentHrStatsTotalFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 10, 1, 6),
    _AlaAppMonCurrentHrStatsTotalFlow_Type()
)
alaAppMonCurrentHrStatsTotalFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonCurrentHrStatsTotalFlow.setStatus("current")
_AlaAppMon24HourTable_Object = MibTable
alaAppMon24HourTable = _AlaAppMon24HourTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaAppMon24HourTable.setStatus("current")
_AlaAppMon24HourEntry_Object = MibTableRow
alaAppMon24HourEntry = _AlaAppMon24HourEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11, 1)
)
alaAppMon24HourEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMon24HourAppName"),
)
if mibBuilder.loadTexts:
    alaAppMon24HourEntry.setStatus("current")
_AlaAppMon24HourAppName_Type = SnmpAdminString
_AlaAppMon24HourAppName_Object = MibTableColumn
alaAppMon24HourAppName = _AlaAppMon24HourAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11, 1, 1),
    _AlaAppMon24HourAppName_Type()
)
alaAppMon24HourAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMon24HourAppName.setStatus("current")
_AlaAppMon24HrStatsMinActiveFlow_Type = Counter32
_AlaAppMon24HrStatsMinActiveFlow_Object = MibTableColumn
alaAppMon24HrStatsMinActiveFlow = _AlaAppMon24HrStatsMinActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11, 1, 2),
    _AlaAppMon24HrStatsMinActiveFlow_Type()
)
alaAppMon24HrStatsMinActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMon24HrStatsMinActiveFlow.setStatus("current")
_AlaAppMon24HrStatsMaxActiveFlow_Type = Counter32
_AlaAppMon24HrStatsMaxActiveFlow_Object = MibTableColumn
alaAppMon24HrStatsMaxActiveFlow = _AlaAppMon24HrStatsMaxActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11, 1, 3),
    _AlaAppMon24HrStatsMaxActiveFlow_Type()
)
alaAppMon24HrStatsMaxActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMon24HrStatsMaxActiveFlow.setStatus("current")
_AlaAppMon24HrStatsAvgActiveFlow_Type = Counter32
_AlaAppMon24HrStatsAvgActiveFlow_Object = MibTableColumn
alaAppMon24HrStatsAvgActiveFlow = _AlaAppMon24HrStatsAvgActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11, 1, 4),
    _AlaAppMon24HrStatsAvgActiveFlow_Type()
)
alaAppMon24HrStatsAvgActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMon24HrStatsAvgActiveFlow.setStatus("current")
_AlaAppMon24HrStatsTotalFlow_Type = Counter32
_AlaAppMon24HrStatsTotalFlow_Object = MibTableColumn
alaAppMon24HrStatsTotalFlow = _AlaAppMon24HrStatsTotalFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 11, 1, 5),
    _AlaAppMon24HrStatsTotalFlow_Type()
)
alaAppMon24HrStatsTotalFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMon24HrStatsTotalFlow.setStatus("current")
_AlaAppMonHourlyTable_Object = MibTable
alaAppMonHourlyTable = _AlaAppMonHourlyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaAppMonHourlyTable.setStatus("current")
_AlaAppMonHourlyEntry_Object = MibTableRow
alaAppMonHourlyEntry = _AlaAppMonHourlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1)
)
alaAppMonHourlyEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyAppName"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHour"),
)
if mibBuilder.loadTexts:
    alaAppMonHourlyEntry.setStatus("current")
_AlaAppMonHourlyAppName_Type = SnmpAdminString
_AlaAppMonHourlyAppName_Object = MibTableColumn
alaAppMonHourlyAppName = _AlaAppMonHourlyAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 1),
    _AlaAppMonHourlyAppName_Type()
)
alaAppMonHourlyAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonHourlyAppName.setStatus("current")


class _AlaAppMonHour_Type(Integer32):
    """Custom type alaAppMonHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AlaAppMonHour_Type.__name__ = "Integer32"
_AlaAppMonHour_Object = MibTableColumn
alaAppMonHour = _AlaAppMonHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 2),
    _AlaAppMonHour_Type()
)
alaAppMonHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonHour.setStatus("current")
_AlaAppMonHourlyAppGroupName_Type = SnmpAdminString
_AlaAppMonHourlyAppGroupName_Object = MibTableColumn
alaAppMonHourlyAppGroupName = _AlaAppMonHourlyAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 3),
    _AlaAppMonHourlyAppGroupName_Type()
)
alaAppMonHourlyAppGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyAppGroupName.setStatus("current")
_AlaAppMonHourlyStatsMinActiveFlow_Type = Counter32
_AlaAppMonHourlyStatsMinActiveFlow_Object = MibTableColumn
alaAppMonHourlyStatsMinActiveFlow = _AlaAppMonHourlyStatsMinActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 4),
    _AlaAppMonHourlyStatsMinActiveFlow_Type()
)
alaAppMonHourlyStatsMinActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyStatsMinActiveFlow.setStatus("current")
_AlaAppMonHourlyStatsMaxActiveFlow_Type = Counter32
_AlaAppMonHourlyStatsMaxActiveFlow_Object = MibTableColumn
alaAppMonHourlyStatsMaxActiveFlow = _AlaAppMonHourlyStatsMaxActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 5),
    _AlaAppMonHourlyStatsMaxActiveFlow_Type()
)
alaAppMonHourlyStatsMaxActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyStatsMaxActiveFlow.setStatus("current")
_AlaAppMonHourlyStatsAvgActiveFlow_Type = Counter32
_AlaAppMonHourlyStatsAvgActiveFlow_Object = MibTableColumn
alaAppMonHourlyStatsAvgActiveFlow = _AlaAppMonHourlyStatsAvgActiveFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 6),
    _AlaAppMonHourlyStatsAvgActiveFlow_Type()
)
alaAppMonHourlyStatsAvgActiveFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyStatsAvgActiveFlow.setStatus("current")
_AlaAppMonHourlyStatsTotalFlow_Type = Counter32
_AlaAppMonHourlyStatsTotalFlow_Object = MibTableColumn
alaAppMonHourlyStatsTotalFlow = _AlaAppMonHourlyStatsTotalFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 7),
    _AlaAppMonHourlyStatsTotalFlow_Type()
)
alaAppMonHourlyStatsTotalFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyStatsTotalFlow.setStatus("current")
_AlaAppMonHourlyTimeInterval_Type = DateAndTime
_AlaAppMonHourlyTimeInterval_Object = MibTableColumn
alaAppMonHourlyTimeInterval = _AlaAppMonHourlyTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 8),
    _AlaAppMonHourlyTimeInterval_Type()
)
alaAppMonHourlyTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyTimeInterval.setStatus("current")
_AlaAppMonHourlyTimeIntervalUTC_Type = DateAndTime
_AlaAppMonHourlyTimeIntervalUTC_Object = MibTableColumn
alaAppMonHourlyTimeIntervalUTC = _AlaAppMonHourlyTimeIntervalUTC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 12, 1, 9),
    _AlaAppMonHourlyTimeIntervalUTC_Type()
)
alaAppMonHourlyTimeIntervalUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonHourlyTimeIntervalUTC.setStatus("current")
_AlaAppMonAppListConflictTable_Object = MibTable
alaAppMonAppListConflictTable = _AlaAppMonAppListConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaAppMonAppListConflictTable.setStatus("current")
_AlaAppMonAppListConflictEntry_Object = MibTableRow
alaAppMonAppListConflictEntry = _AlaAppMonAppListConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13, 1)
)
alaAppMonAppListConflictEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListConflictIndex"),
)
if mibBuilder.loadTexts:
    alaAppMonAppListConflictEntry.setStatus("current")
_AlaAppMonAppListConflictIndex_Type = Unsigned32
_AlaAppMonAppListConflictIndex_Object = MibTableColumn
alaAppMonAppListConflictIndex = _AlaAppMonAppListConflictIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13, 1, 1),
    _AlaAppMonAppListConflictIndex_Type()
)
alaAppMonAppListConflictIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonAppListConflictIndex.setStatus("current")
_AlaAppMonAppListConflictAppID_Type = Integer32
_AlaAppMonAppListConflictAppID_Object = MibTableColumn
alaAppMonAppListConflictAppID = _AlaAppMonAppListConflictAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13, 1, 2),
    _AlaAppMonAppListConflictAppID_Type()
)
alaAppMonAppListConflictAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppListConflictAppID.setStatus("current")
_AlaAppMonAppListConflictAppName_Type = SnmpAdminString
_AlaAppMonAppListConflictAppName_Object = MibTableColumn
alaAppMonAppListConflictAppName = _AlaAppMonAppListConflictAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13, 1, 3),
    _AlaAppMonAppListConflictAppName_Type()
)
alaAppMonAppListConflictAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppListConflictAppName.setStatus("current")
_AlaAppMonAppListConflictAppGrpName_Type = SnmpAdminString
_AlaAppMonAppListConflictAppGrpName_Object = MibTableColumn
alaAppMonAppListConflictAppGrpName = _AlaAppMonAppListConflictAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13, 1, 4),
    _AlaAppMonAppListConflictAppGrpName_Type()
)
alaAppMonAppListConflictAppGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppListConflictAppGrpName.setStatus("current")


class _AlaAppMonAppListConflictAppErrorType_Type(Integer32):
    """Custom type alaAppMonAppListConflictAppErrorType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplicate", 1),
          ("notInUse", 2))
    )


_AlaAppMonAppListConflictAppErrorType_Type.__name__ = "Integer32"
_AlaAppMonAppListConflictAppErrorType_Object = MibTableColumn
alaAppMonAppListConflictAppErrorType = _AlaAppMonAppListConflictAppErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 13, 1, 5),
    _AlaAppMonAppListConflictAppErrorType_Type()
)
alaAppMonAppListConflictAppErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonAppListConflictAppErrorType.setStatus("current")
_AlaAppMonEnforcementAppListTable_Object = MibTable
alaAppMonEnforcementAppListTable = _AlaAppMonEnforcementAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListTable.setStatus("current")
_AlaAppMonEnforcementAppListEntry_Object = MibTableRow
alaAppMonEnforcementAppListEntry = _AlaAppMonEnforcementAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14, 1)
)
alaAppMonEnforcementAppListEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListMemberName"),
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListEntry.setStatus("current")


class _AlaAppMonEnforcementAppListMemberName_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementAppListMemberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonEnforcementAppListMemberName_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementAppListMemberName_Object = MibTableColumn
alaAppMonEnforcementAppListMemberName = _AlaAppMonEnforcementAppListMemberName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14, 1, 1),
    _AlaAppMonEnforcementAppListMemberName_Type()
)
alaAppMonEnforcementAppListMemberName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListMemberName.setStatus("current")


class _AlaAppMonEnforcementAppListMemberType_Type(Integer32):
    """Custom type alaAppMonEnforcementAppListMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("application", 1),
          ("applicationGroup", 2))
    )


_AlaAppMonEnforcementAppListMemberType_Type.__name__ = "Integer32"
_AlaAppMonEnforcementAppListMemberType_Object = MibTableColumn
alaAppMonEnforcementAppListMemberType = _AlaAppMonEnforcementAppListMemberType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14, 1, 2),
    _AlaAppMonEnforcementAppListMemberType_Type()
)
alaAppMonEnforcementAppListMemberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListMemberType.setStatus("current")
_AlaAppMonEnforcementAppListAppOrGroupID_Type = Integer32
_AlaAppMonEnforcementAppListAppOrGroupID_Object = MibTableColumn
alaAppMonEnforcementAppListAppOrGroupID = _AlaAppMonEnforcementAppListAppOrGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14, 1, 3),
    _AlaAppMonEnforcementAppListAppOrGroupID_Type()
)
alaAppMonEnforcementAppListAppOrGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListAppOrGroupID.setStatus("current")


class _AlaAppMonEnforcementAppListAppStatus_Type(Integer32):
    """Custom type alaAppMonEnforcementAppListAppStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AlaAppMonEnforcementAppListAppStatus_Type.__name__ = "Integer32"
_AlaAppMonEnforcementAppListAppStatus_Object = MibTableColumn
alaAppMonEnforcementAppListAppStatus = _AlaAppMonEnforcementAppListAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14, 1, 4),
    _AlaAppMonEnforcementAppListAppStatus_Type()
)
alaAppMonEnforcementAppListAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListAppStatus.setStatus("current")
_AlaAppMonEnforcementAppListMemberStatus_Type = RowStatus
_AlaAppMonEnforcementAppListMemberStatus_Object = MibTableColumn
alaAppMonEnforcementAppListMemberStatus = _AlaAppMonEnforcementAppListMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 14, 1, 5),
    _AlaAppMonEnforcementAppListMemberStatus_Type()
)
alaAppMonEnforcementAppListMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListMemberStatus.setStatus("current")
_AlaAppMonEnforcementFlowTable_Object = MibTable
alaAppMonEnforcementFlowTable = _AlaAppMonEnforcementFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowTable.setStatus("current")
_AlaAppMonEnforcementFlowEntry_Object = MibTableRow
alaAppMonEnforcementFlowEntry = _AlaAppMonEnforcementFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1)
)
alaAppMonEnforcementFlowEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowSourceIPType"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowSourceIP"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowDestIPType"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowDestIP"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowSrcPort"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowDestPort"),
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowProtocol"),
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowEntry.setStatus("current")


class _AlaAppMonEnforcementFlowSourceIPType_Type(InetAddressType):
    """Custom type alaAppMonEnforcementFlowSourceIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaAppMonEnforcementFlowSourceIPType_Type.__name__ = "InetAddressType"
_AlaAppMonEnforcementFlowSourceIPType_Object = MibTableColumn
alaAppMonEnforcementFlowSourceIPType = _AlaAppMonEnforcementFlowSourceIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 1),
    _AlaAppMonEnforcementFlowSourceIPType_Type()
)
alaAppMonEnforcementFlowSourceIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowSourceIPType.setStatus("current")


class _AlaAppMonEnforcementFlowSourceIP_Type(InetAddress):
    """Custom type alaAppMonEnforcementFlowSourceIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaAppMonEnforcementFlowSourceIP_Type.__name__ = "InetAddress"
_AlaAppMonEnforcementFlowSourceIP_Object = MibTableColumn
alaAppMonEnforcementFlowSourceIP = _AlaAppMonEnforcementFlowSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 2),
    _AlaAppMonEnforcementFlowSourceIP_Type()
)
alaAppMonEnforcementFlowSourceIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowSourceIP.setStatus("current")


class _AlaAppMonEnforcementFlowDestIPType_Type(InetAddressType):
    """Custom type alaAppMonEnforcementFlowDestIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaAppMonEnforcementFlowDestIPType_Type.__name__ = "InetAddressType"
_AlaAppMonEnforcementFlowDestIPType_Object = MibTableColumn
alaAppMonEnforcementFlowDestIPType = _AlaAppMonEnforcementFlowDestIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 3),
    _AlaAppMonEnforcementFlowDestIPType_Type()
)
alaAppMonEnforcementFlowDestIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowDestIPType.setStatus("current")


class _AlaAppMonEnforcementFlowDestIP_Type(InetAddress):
    """Custom type alaAppMonEnforcementFlowDestIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaAppMonEnforcementFlowDestIP_Type.__name__ = "InetAddress"
_AlaAppMonEnforcementFlowDestIP_Object = MibTableColumn
alaAppMonEnforcementFlowDestIP = _AlaAppMonEnforcementFlowDestIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 4),
    _AlaAppMonEnforcementFlowDestIP_Type()
)
alaAppMonEnforcementFlowDestIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowDestIP.setStatus("current")


class _AlaAppMonEnforcementFlowSrcPort_Type(Integer32):
    """Custom type alaAppMonEnforcementFlowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaAppMonEnforcementFlowSrcPort_Type.__name__ = "Integer32"
_AlaAppMonEnforcementFlowSrcPort_Object = MibTableColumn
alaAppMonEnforcementFlowSrcPort = _AlaAppMonEnforcementFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 5),
    _AlaAppMonEnforcementFlowSrcPort_Type()
)
alaAppMonEnforcementFlowSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowSrcPort.setStatus("current")


class _AlaAppMonEnforcementFlowDestPort_Type(Integer32):
    """Custom type alaAppMonEnforcementFlowDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaAppMonEnforcementFlowDestPort_Type.__name__ = "Integer32"
_AlaAppMonEnforcementFlowDestPort_Object = MibTableColumn
alaAppMonEnforcementFlowDestPort = _AlaAppMonEnforcementFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 6),
    _AlaAppMonEnforcementFlowDestPort_Type()
)
alaAppMonEnforcementFlowDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowDestPort.setStatus("current")


class _AlaAppMonEnforcementFlowProtocol_Type(Integer32):
    """Custom type alaAppMonEnforcementFlowProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_AlaAppMonEnforcementFlowProtocol_Type.__name__ = "Integer32"
_AlaAppMonEnforcementFlowProtocol_Object = MibTableColumn
alaAppMonEnforcementFlowProtocol = _AlaAppMonEnforcementFlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 7),
    _AlaAppMonEnforcementFlowProtocol_Type()
)
alaAppMonEnforcementFlowProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowProtocol.setStatus("current")


class _AlaAppMonEnforcementFlowAppName_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementFlowAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonEnforcementFlowAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementFlowAppName_Object = MibTableColumn
alaAppMonEnforcementFlowAppName = _AlaAppMonEnforcementFlowAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 8),
    _AlaAppMonEnforcementFlowAppName_Type()
)
alaAppMonEnforcementFlowAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowAppName.setStatus("current")


class _AlaAppMonEnforcementFlowAppGrpName_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementFlowAppGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonEnforcementFlowAppGrpName_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementFlowAppGrpName_Object = MibTableColumn
alaAppMonEnforcementFlowAppGrpName = _AlaAppMonEnforcementFlowAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 9),
    _AlaAppMonEnforcementFlowAppGrpName_Type()
)
alaAppMonEnforcementFlowAppGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowAppGrpName.setStatus("current")


class _AlaAppMonEnforcementFlowPolicyRule_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementFlowPolicyRule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAppMonEnforcementFlowPolicyRule_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementFlowPolicyRule_Object = MibTableColumn
alaAppMonEnforcementFlowPolicyRule = _AlaAppMonEnforcementFlowPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 10),
    _AlaAppMonEnforcementFlowPolicyRule_Type()
)
alaAppMonEnforcementFlowPolicyRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowPolicyRule.setStatus("current")
_AlaAppMonEnforcementFlowStartTime_Type = DateAndTime
_AlaAppMonEnforcementFlowStartTime_Object = MibTableColumn
alaAppMonEnforcementFlowStartTime = _AlaAppMonEnforcementFlowStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 11),
    _AlaAppMonEnforcementFlowStartTime_Type()
)
alaAppMonEnforcementFlowStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowStartTime.setStatus("current")
_AlaAppMonEnforcementFlowPktCount_Type = Counter64
_AlaAppMonEnforcementFlowPktCount_Object = MibTableColumn
alaAppMonEnforcementFlowPktCount = _AlaAppMonEnforcementFlowPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 12),
    _AlaAppMonEnforcementFlowPktCount_Type()
)
alaAppMonEnforcementFlowPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowPktCount.setStatus("current")
_AlaAppMonEnforcementFlowByteCount_Type = Counter64
_AlaAppMonEnforcementFlowByteCount_Object = MibTableColumn
alaAppMonEnforcementFlowByteCount = _AlaAppMonEnforcementFlowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 15, 1, 13),
    _AlaAppMonEnforcementFlowByteCount_Type()
)
alaAppMonEnforcementFlowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowByteCount.setStatus("current")
_AlaAppMonEnforcementL4PortRangeTable_Object = MibTable
alaAppMonEnforcementL4PortRangeTable = _AlaAppMonEnforcementL4PortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortRangeTable.setStatus("current")
_AlaAppMonEnforcementL4PortRangeEntry_Object = MibTableRow
alaAppMonEnforcementL4PortRangeEntry = _AlaAppMonEnforcementL4PortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16, 1)
)
alaAppMonEnforcementL4PortRangeEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementL4PortRangeID"),
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortRangeEntry.setStatus("current")


class _AlaAppMonEnforcementL4PortRangeID_Type(Integer32):
    """Custom type alaAppMonEnforcementL4PortRangeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaAppMonEnforcementL4PortRangeID_Type.__name__ = "Integer32"
_AlaAppMonEnforcementL4PortRangeID_Object = MibTableColumn
alaAppMonEnforcementL4PortRangeID = _AlaAppMonEnforcementL4PortRangeID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16, 1, 1),
    _AlaAppMonEnforcementL4PortRangeID_Type()
)
alaAppMonEnforcementL4PortRangeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortRangeID.setStatus("current")


class _AlaAppMonEnforcementL4PortRangeStart_Type(Integer32):
    """Custom type alaAppMonEnforcementL4PortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaAppMonEnforcementL4PortRangeStart_Type.__name__ = "Integer32"
_AlaAppMonEnforcementL4PortRangeStart_Object = MibTableColumn
alaAppMonEnforcementL4PortRangeStart = _AlaAppMonEnforcementL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16, 1, 2),
    _AlaAppMonEnforcementL4PortRangeStart_Type()
)
alaAppMonEnforcementL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortRangeStart.setStatus("current")


class _AlaAppMonEnforcementL4PortRangeEnd_Type(Integer32):
    """Custom type alaAppMonEnforcementL4PortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaAppMonEnforcementL4PortRangeEnd_Type.__name__ = "Integer32"
_AlaAppMonEnforcementL4PortRangeEnd_Object = MibTableColumn
alaAppMonEnforcementL4PortRangeEnd = _AlaAppMonEnforcementL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16, 1, 3),
    _AlaAppMonEnforcementL4PortRangeEnd_Type()
)
alaAppMonEnforcementL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortRangeEnd.setStatus("current")


class _AlaAppMonEnforcementL4PortType_Type(Integer32):
    """Custom type alaAppMonEnforcementL4PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcpServicePort", 1),
          ("udpPort", 2))
    )


_AlaAppMonEnforcementL4PortType_Type.__name__ = "Integer32"
_AlaAppMonEnforcementL4PortType_Object = MibTableColumn
alaAppMonEnforcementL4PortType = _AlaAppMonEnforcementL4PortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16, 1, 4),
    _AlaAppMonEnforcementL4PortType_Type()
)
alaAppMonEnforcementL4PortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortType.setStatus("current")
_AlaAppMonEnforcementL4PortStatus_Type = RowStatus
_AlaAppMonEnforcementL4PortStatus_Object = MibTableColumn
alaAppMonEnforcementL4PortStatus = _AlaAppMonEnforcementL4PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 16, 1, 5),
    _AlaAppMonEnforcementL4PortStatus_Type()
)
alaAppMonEnforcementL4PortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortStatus.setStatus("current")
_AlaAppMonEnforcementActiveAppListTable_Object = MibTable
alaAppMonEnforcementActiveAppListTable = _AlaAppMonEnforcementActiveAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListTable.setStatus("current")
_AlaAppMonEnforcementActiveAppListEntry_Object = MibTableRow
alaAppMonEnforcementActiveAppListEntry = _AlaAppMonEnforcementActiveAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1)
)
alaAppMonEnforcementActiveAppListEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListEntry.setStatus("current")


class _AlaAppMonEnforcementActiveAppListAppName_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementActiveAppListAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonEnforcementActiveAppListAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementActiveAppListAppName_Object = MibTableColumn
alaAppMonEnforcementActiveAppListAppName = _AlaAppMonEnforcementActiveAppListAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 1),
    _AlaAppMonEnforcementActiveAppListAppName_Type()
)
alaAppMonEnforcementActiveAppListAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListAppName.setStatus("current")


class _AlaAppMonEnforcementActiveAppListAppGroupName_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementActiveAppListAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAppMonEnforcementActiveAppListAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementActiveAppListAppGroupName_Object = MibTableColumn
alaAppMonEnforcementActiveAppListAppGroupName = _AlaAppMonEnforcementActiveAppListAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 2),
    _AlaAppMonEnforcementActiveAppListAppGroupName_Type()
)
alaAppMonEnforcementActiveAppListAppGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListAppGroupName.setStatus("current")
_AlaAppMonEnforcementActiveAppListActiveMatchedFlows_Type = Integer32
_AlaAppMonEnforcementActiveAppListActiveMatchedFlows_Object = MibTableColumn
alaAppMonEnforcementActiveAppListActiveMatchedFlows = _AlaAppMonEnforcementActiveAppListActiveMatchedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 3),
    _AlaAppMonEnforcementActiveAppListActiveMatchedFlows_Type()
)
alaAppMonEnforcementActiveAppListActiveMatchedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListActiveMatchedFlows.setStatus("current")
_AlaAppMonEnforcementActiveAppListTotalMatchedFlows_Type = Integer32
_AlaAppMonEnforcementActiveAppListTotalMatchedFlows_Object = MibTableColumn
alaAppMonEnforcementActiveAppListTotalMatchedFlows = _AlaAppMonEnforcementActiveAppListTotalMatchedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 4),
    _AlaAppMonEnforcementActiveAppListTotalMatchedFlows_Type()
)
alaAppMonEnforcementActiveAppListTotalMatchedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListTotalMatchedFlows.setStatus("current")
_AlaAppMonEnforcementActiveAppListAppID_Type = Integer32
_AlaAppMonEnforcementActiveAppListAppID_Object = MibTableColumn
alaAppMonEnforcementActiveAppListAppID = _AlaAppMonEnforcementActiveAppListAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 5),
    _AlaAppMonEnforcementActiveAppListAppID_Type()
)
alaAppMonEnforcementActiveAppListAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListAppID.setStatus("current")


class _AlaAppMonEnforcementActiveAppListAppStatus_Type(Integer32):
    """Custom type alaAppMonEnforcementActiveAppListAppStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AlaAppMonEnforcementActiveAppListAppStatus_Type.__name__ = "Integer32"
_AlaAppMonEnforcementActiveAppListAppStatus_Object = MibTableColumn
alaAppMonEnforcementActiveAppListAppStatus = _AlaAppMonEnforcementActiveAppListAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 6),
    _AlaAppMonEnforcementActiveAppListAppStatus_Type()
)
alaAppMonEnforcementActiveAppListAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListAppStatus.setStatus("current")
_AlaAppMonEnforcementActiveAppListActivePktCount_Type = Counter64
_AlaAppMonEnforcementActiveAppListActivePktCount_Object = MibTableColumn
alaAppMonEnforcementActiveAppListActivePktCount = _AlaAppMonEnforcementActiveAppListActivePktCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 7),
    _AlaAppMonEnforcementActiveAppListActivePktCount_Type()
)
alaAppMonEnforcementActiveAppListActivePktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListActivePktCount.setStatus("current")
_AlaAppMonEnforcementActiveAppListActiveByteCount_Type = Counter64
_AlaAppMonEnforcementActiveAppListActiveByteCount_Object = MibTableColumn
alaAppMonEnforcementActiveAppListActiveByteCount = _AlaAppMonEnforcementActiveAppListActiveByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 8),
    _AlaAppMonEnforcementActiveAppListActiveByteCount_Type()
)
alaAppMonEnforcementActiveAppListActiveByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListActiveByteCount.setStatus("current")
_AlaAppMonEnforcementActiveAppListGrossPktCount_Type = Counter64
_AlaAppMonEnforcementActiveAppListGrossPktCount_Object = MibTableColumn
alaAppMonEnforcementActiveAppListGrossPktCount = _AlaAppMonEnforcementActiveAppListGrossPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 9),
    _AlaAppMonEnforcementActiveAppListGrossPktCount_Type()
)
alaAppMonEnforcementActiveAppListGrossPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListGrossPktCount.setStatus("current")
_AlaAppMonEnforcementActiveAppListGrossByteCount_Type = Counter64
_AlaAppMonEnforcementActiveAppListGrossByteCount_Object = MibTableColumn
alaAppMonEnforcementActiveAppListGrossByteCount = _AlaAppMonEnforcementActiveAppListGrossByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 17, 1, 10),
    _AlaAppMonEnforcementActiveAppListGrossByteCount_Type()
)
alaAppMonEnforcementActiveAppListGrossByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveAppListGrossByteCount.setStatus("current")
_AlaAppMonEnforcementAppListConflictTable_Object = MibTable
alaAppMonEnforcementAppListConflictTable = _AlaAppMonEnforcementAppListConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictTable.setStatus("current")
_AlaAppMonEnforcementAppListConflictEntry_Object = MibTableRow
alaAppMonEnforcementAppListConflictEntry = _AlaAppMonEnforcementAppListConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18, 1)
)
alaAppMonEnforcementAppListConflictEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListConflictIndex"),
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictEntry.setStatus("current")
_AlaAppMonEnforcementAppListConflictIndex_Type = Unsigned32
_AlaAppMonEnforcementAppListConflictIndex_Object = MibTableColumn
alaAppMonEnforcementAppListConflictIndex = _AlaAppMonEnforcementAppListConflictIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18, 1, 1),
    _AlaAppMonEnforcementAppListConflictIndex_Type()
)
alaAppMonEnforcementAppListConflictIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictIndex.setStatus("current")
_AlaAppMonEnforcementAppListConflictAppID_Type = Integer32
_AlaAppMonEnforcementAppListConflictAppID_Object = MibTableColumn
alaAppMonEnforcementAppListConflictAppID = _AlaAppMonEnforcementAppListConflictAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18, 1, 2),
    _AlaAppMonEnforcementAppListConflictAppID_Type()
)
alaAppMonEnforcementAppListConflictAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictAppID.setStatus("current")
_AlaAppMonEnforcementAppListConflictAppName_Type = SnmpAdminString
_AlaAppMonEnforcementAppListConflictAppName_Object = MibTableColumn
alaAppMonEnforcementAppListConflictAppName = _AlaAppMonEnforcementAppListConflictAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18, 1, 3),
    _AlaAppMonEnforcementAppListConflictAppName_Type()
)
alaAppMonEnforcementAppListConflictAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictAppName.setStatus("current")
_AlaAppMonEnforcementAppListConflictAppGrpName_Type = SnmpAdminString
_AlaAppMonEnforcementAppListConflictAppGrpName_Object = MibTableColumn
alaAppMonEnforcementAppListConflictAppGrpName = _AlaAppMonEnforcementAppListConflictAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18, 1, 4),
    _AlaAppMonEnforcementAppListConflictAppGrpName_Type()
)
alaAppMonEnforcementAppListConflictAppGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictAppGrpName.setStatus("current")


class _AlaAppMonEnforcementAppListConflictAppErrorType_Type(Integer32):
    """Custom type alaAppMonEnforcementAppListConflictAppErrorType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplicate", 1),
          ("notInUse", 2))
    )


_AlaAppMonEnforcementAppListConflictAppErrorType_Type.__name__ = "Integer32"
_AlaAppMonEnforcementAppListConflictAppErrorType_Object = MibTableColumn
alaAppMonEnforcementAppListConflictAppErrorType = _AlaAppMonEnforcementAppListConflictAppErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 18, 1, 5),
    _AlaAppMonEnforcementAppListConflictAppErrorType_Type()
)
alaAppMonEnforcementAppListConflictAppErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListConflictAppErrorType.setStatus("current")
_AlaAppMonEnforcementAgingTimerTable_Object = MibTable
alaAppMonEnforcementAgingTimerTable = _AlaAppMonEnforcementAgingTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 19)
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAgingTimerTable.setStatus("current")
_AlaAppMonEnforcementAgingTimerEntry_Object = MibTableRow
alaAppMonEnforcementAgingTimerEntry = _AlaAppMonEnforcementAgingTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 19, 1)
)
alaAppMonEnforcementAgingTimerEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAgingTimerAppName"),
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAgingTimerEntry.setStatus("current")


class _AlaAppMonEnforcementAgingTimerAppName_Type(SnmpAdminString):
    """Custom type alaAppMonEnforcementAgingTimerAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaAppMonEnforcementAgingTimerAppName_Type.__name__ = "SnmpAdminString"
_AlaAppMonEnforcementAgingTimerAppName_Object = MibTableColumn
alaAppMonEnforcementAgingTimerAppName = _AlaAppMonEnforcementAgingTimerAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 19, 1, 1),
    _AlaAppMonEnforcementAgingTimerAppName_Type()
)
alaAppMonEnforcementAgingTimerAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonEnforcementAgingTimerAppName.setStatus("current")


class _AlaAppMonEnforcementTcpAgingTimerValue_Type(Integer32):
    """Custom type alaAppMonEnforcementTcpAgingTimerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(120, 120),
    )


_AlaAppMonEnforcementTcpAgingTimerValue_Type.__name__ = "Integer32"
_AlaAppMonEnforcementTcpAgingTimerValue_Object = MibTableColumn
alaAppMonEnforcementTcpAgingTimerValue = _AlaAppMonEnforcementTcpAgingTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 19, 1, 2),
    _AlaAppMonEnforcementTcpAgingTimerValue_Type()
)
alaAppMonEnforcementTcpAgingTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementTcpAgingTimerValue.setStatus("current")


class _AlaAppMonEnforcementUdpAgingTimerValue_Type(Integer32):
    """Custom type alaAppMonEnforcementUdpAgingTimerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(120, 120),
    )


_AlaAppMonEnforcementUdpAgingTimerValue_Type.__name__ = "Integer32"
_AlaAppMonEnforcementUdpAgingTimerValue_Object = MibTableColumn
alaAppMonEnforcementUdpAgingTimerValue = _AlaAppMonEnforcementUdpAgingTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 19, 1, 3),
    _AlaAppMonEnforcementUdpAgingTimerValue_Type()
)
alaAppMonEnforcementUdpAgingTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppMonEnforcementUdpAgingTimerValue.setStatus("current")
_AlaAppMonStatisticsTable_Object = MibTable
alaAppMonStatisticsTable = _AlaAppMonStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20)
)
if mibBuilder.loadTexts:
    alaAppMonStatisticsTable.setStatus("current")
_AlaAppMonStatisticsEntry_Object = MibTableRow
alaAppMonStatisticsEntry = _AlaAppMonStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20, 1)
)
alaAppMonStatisticsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonStatsSlotIndex"),
)
if mibBuilder.loadTexts:
    alaAppMonStatisticsEntry.setStatus("current")
_AlaAppMonStatsSlotIndex_Type = InterfaceIndex
_AlaAppMonStatsSlotIndex_Object = MibTableColumn
alaAppMonStatsSlotIndex = _AlaAppMonStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20, 1, 1),
    _AlaAppMonStatsSlotIndex_Type()
)
alaAppMonStatsSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonStatsSlotIndex.setStatus("current")
_AlaAppMonTotalEnforcementActiveFlows_Type = Counter32
_AlaAppMonTotalEnforcementActiveFlows_Object = MibTableColumn
alaAppMonTotalEnforcementActiveFlows = _AlaAppMonTotalEnforcementActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20, 1, 2),
    _AlaAppMonTotalEnforcementActiveFlows_Type()
)
alaAppMonTotalEnforcementActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonTotalEnforcementActiveFlows.setStatus("current")
_AlaAppMonTotalFlowTableInUseFlows_Type = Counter32
_AlaAppMonTotalFlowTableInUseFlows_Object = MibTableColumn
alaAppMonTotalFlowTableInUseFlows = _AlaAppMonTotalFlowTableInUseFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20, 1, 3),
    _AlaAppMonTotalFlowTableInUseFlows_Type()
)
alaAppMonTotalFlowTableInUseFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonTotalFlowTableInUseFlows.setStatus("current")
_AlaAppMonTCPOverflowFlows_Type = Counter32
_AlaAppMonTCPOverflowFlows_Object = MibTableColumn
alaAppMonTCPOverflowFlows = _AlaAppMonTCPOverflowFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20, 1, 4),
    _AlaAppMonTCPOverflowFlows_Type()
)
alaAppMonTCPOverflowFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonTCPOverflowFlows.setStatus("current")
_AlaAppMonUDPOverflowPackets_Type = Counter32
_AlaAppMonUDPOverflowPackets_Object = MibTableColumn
alaAppMonUDPOverflowPackets = _AlaAppMonUDPOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 20, 1, 5),
    _AlaAppMonUDPOverflowPackets_Type()
)
alaAppMonUDPOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonUDPOverflowPackets.setStatus("current")
_AlaAppMonVCTopologyTable_Object = MibTable
alaAppMonVCTopologyTable = _AlaAppMonVCTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 21)
)
if mibBuilder.loadTexts:
    alaAppMonVCTopologyTable.setStatus("current")
_AlaAppMonVCTopologyEntry_Object = MibTableRow
alaAppMonVCTopologyEntry = _AlaAppMonVCTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 21, 1)
)
alaAppMonVCTopologyEntry.setIndexNames(
    (0, "ALCATEL-ENT1-APP-MON-MIB", "alaAppMonVCTopologyChassisIndex"),
)
if mibBuilder.loadTexts:
    alaAppMonVCTopologyEntry.setStatus("current")
_AlaAppMonVCTopologyChassisIndex_Type = InterfaceIndex
_AlaAppMonVCTopologyChassisIndex_Object = MibTableColumn
alaAppMonVCTopologyChassisIndex = _AlaAppMonVCTopologyChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 21, 1, 1),
    _AlaAppMonVCTopologyChassisIndex_Type()
)
alaAppMonVCTopologyChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppMonVCTopologyChassisIndex.setStatus("current")


class _AlaAppMonVCTopologyChassisType_Type(Integer32):
    """Custom type alaAppMonVCTopologyChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("os6860", 1),
          ("os6860E", 2))
    )


_AlaAppMonVCTopologyChassisType_Type.__name__ = "Integer32"
_AlaAppMonVCTopologyChassisType_Object = MibTableColumn
alaAppMonVCTopologyChassisType = _AlaAppMonVCTopologyChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 21, 1, 2),
    _AlaAppMonVCTopologyChassisType_Type()
)
alaAppMonVCTopologyChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonVCTopologyChassisType.setStatus("current")
_AlaAppMonVCTopologyDesignatedChassisIndex_Type = InterfaceIndex
_AlaAppMonVCTopologyDesignatedChassisIndex_Object = MibTableColumn
alaAppMonVCTopologyDesignatedChassisIndex = _AlaAppMonVCTopologyDesignatedChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 1, 21, 1, 3),
    _AlaAppMonVCTopologyDesignatedChassisIndex_Type()
)
alaAppMonVCTopologyDesignatedChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppMonVCTopologyDesignatedChassisIndex.setStatus("current")
_AlaAppMonMIBConformance_ObjectIdentity = ObjectIdentity
alaAppMonMIBConformance = _AlaAppMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2)
)
if mibBuilder.loadTexts:
    alaAppMonMIBConformance.setStatus("current")
_AlaAppMonMIBGroups_ObjectIdentity = ObjectIdentity
alaAppMonMIBGroups = _AlaAppMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaAppMonMIBGroups.setStatus("current")
_AlaAppMonMIBCompliances_ObjectIdentity = ObjectIdentity
alaAppMonMIBCompliances = _AlaAppMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaAppMonMIBCompliances.setStatus("current")

# Managed Objects groups

alaAppMonPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 1)
)
alaAppMonPortConfigGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonPortConfigPortStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonPortConfigOperStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementPortConfigTcpStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementPortConfigUdpStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonPortConfigGroup.setStatus("current")

alaAppMonAppPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 2)
)
alaAppMonAppPoolGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppPoolCategory"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppPoolRevision"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppPoolAppStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppPoolAppID"))
)
if mibBuilder.loadTexts:
    alaAppMonAppPoolGroup.setStatus("current")

alaAppMonAppGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 3)
)
alaAppMonAppGroupsGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupBuiltIn"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupCategoryName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGrpId"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupAppStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonAppGroupsGroup.setStatus("current")

alaAppMonAppListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 4)
)
alaAppMonAppListGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListMemberType"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListAppId"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListAppStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListMemberStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonAppListGroup.setStatus("current")

alaAppMonConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 7)
)
alaAppMonConfigGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAdminStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonUpdateAppList"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonClearAppList"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowTableFlush"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAgingInterval"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppliedApplications"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonApplicationPoolApplications"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonSignatureFileVersion"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonSignatureFileName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonSignatureFileAppCount"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGrpFromAppName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGrpToAppName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAddAppGrpName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonOperationalStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonForceFlowSyncStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAutoGroupCreation"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonLoggingThresholdFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAddRemoveAppGrpName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAOSCompatibilityVersion"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonKitType"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonUpgradedKitType"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonUpgradedSignatureFileVersion"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonClearConfig"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementIpv4"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementIpv6"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowTableStatsAdminStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementStatsInterval"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementLoggingThresholdFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowSyncEnforcementInterval"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowSyncMonitorInterval"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppliedApplications"))
)
if mibBuilder.loadTexts:
    alaAppMonConfigGroup.setStatus("current")

alaAppMonActiveAppListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 8)
)
alaAppMonActiveAppListGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonActiveAppListAppGroupName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonActiveAppListActiveFlowCount"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonActiveAppListAppId"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonActiveAppListAppStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonActiveAppListGroup.setStatus("current")

alaAppMonSignatureFileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 9)
)
alaAppMonSignatureFileTableGroup.setObjects(
    ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonSignatureFileCategory")
)
if mibBuilder.loadTexts:
    alaAppMonSignatureFileTableGroup.setStatus("current")

alaAppMonFlowTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 10)
)
alaAppMonFlowTableGroup.setObjects(
    ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowAppGrpName")
)
if mibBuilder.loadTexts:
    alaAppMonFlowTableGroup.setStatus("current")

alaAppMonCurrentHourGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 11)
)
alaAppMonCurrentHourGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHourAppGroupName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHrStatsMinActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHrStatsMaxActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHrStatsAvgActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHrStatsTotalFlow"))
)
if mibBuilder.loadTexts:
    alaAppMonCurrentHourGroup.setStatus("current")

alaAppMon24HourGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 12)
)
alaAppMon24HourGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMon24HrStatsMinActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMon24HrStatsMaxActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMon24HrStatsAvgActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMon24HrStatsTotalFlow"))
)
if mibBuilder.loadTexts:
    alaAppMon24HourGroup.setStatus("current")

alaAppMonHourlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 13)
)
alaAppMonHourlyGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyAppGroupName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyStatsMinActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyStatsMaxActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyStatsAvgActiveFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyStatsTotalFlow"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyTimeInterval"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyTimeIntervalUTC"))
)
if mibBuilder.loadTexts:
    alaAppMonHourlyGroup.setStatus("current")

alaAppMonAppListConflictGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 15)
)
alaAppMonAppListConflictGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListConflictAppID"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListConflictAppName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListConflictAppGrpName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListConflictAppErrorType"))
)
if mibBuilder.loadTexts:
    alaAppMonAppListConflictGroup.setStatus("current")

alaAppMonCertConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 16)
)
alaAppMonCertConfigGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonUpdateSignatureFile"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonUpdateSignatureStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonCertConfigGroup.setStatus("current")

alaAppMonEnforcementAppListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 17)
)
alaAppMonEnforcementAppListGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListMemberType"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListAppOrGroupID"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListAppStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListMemberStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAppListGroup.setStatus("current")

alaAppMonEnforcementFlowTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 18)
)
alaAppMonEnforcementFlowTableGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowAppName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowAppGrpName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowPolicyRule"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowStartTime"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowPktCount"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowByteCount"))
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementFlowTableGroup.setStatus("current")

alaAppMonEnforcementL4PortRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 19)
)
alaAppMonEnforcementL4PortRangeGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementL4PortRangeStart"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementL4PortRangeEnd"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementL4PortType"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementL4PortStatus"))
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementL4PortRangeGroup.setStatus("current")

alaAppMonEnforcementActiveApplistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 20)
)
alaAppMonEnforcementActiveApplistGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListAppGroupName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListActiveMatchedFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListTotalMatchedFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListAppID"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListAppStatus"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListActivePktCount"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListActiveByteCount"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListGrossPktCount"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveAppListGrossByteCount"))
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementActiveApplistGroup.setStatus("current")

alaAppMonEnforcementConflictGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 21)
)
alaAppMonEnforcementConflictGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListConflictAppID"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListConflictAppName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListConflictAppGrpName"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListConflictAppErrorType"))
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementConflictGroup.setStatus("current")

alaAppMonEnforcementAgingTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 22)
)
alaAppMonEnforcementAgingTimerGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementTcpAgingTimerValue"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementUdpAgingTimerValue"))
)
if mibBuilder.loadTexts:
    alaAppMonEnforcementAgingTimerGroup.setStatus("current")

alaAppMonStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 23)
)
alaAppMonStatisticsGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonTotalEnforcementActiveFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonTotalFlowTableInUseFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonTCPOverflowFlows"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonUDPOverflowPackets"))
)
if mibBuilder.loadTexts:
    alaAppMonStatisticsGroup.setStatus("current")

alaAppMonVCTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 24)
)
alaAppMonVCTopologyGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonVCTopologyChassisType"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonVCTopologyDesignatedChassisIndex"))
)
if mibBuilder.loadTexts:
    alaAppMonVCTopologyGroup.setStatus("current")


# Notification objects

alaAppMonAppRecordFileCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 0, 1)
)
if mibBuilder.loadTexts:
    alaAppMonAppRecordFileCreated.setStatus(
        "current"
    )

alaAppMonFlowRecordFileCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 0, 2)
)
if mibBuilder.loadTexts:
    alaAppMonFlowRecordFileCreated.setStatus(
        "current"
    )


# Notifications groups

alaAppMonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 1, 14)
)
alaAppMonNotificationGroup.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppRecordFileCreated"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowRecordFileCreated"))
)
if mibBuilder.loadTexts:
    alaAppMonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaAppMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 81, 1, 2, 2, 1)
)
alaAppMonMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonConfigGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonPortConfigGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppPoolGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppGroupsGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonActiveAppListGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonSignatureFileTableGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonFlowTableGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCurrentHourGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMon24HourGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonHourlyGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonNotificationGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonAppListConflictGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonCertConfigGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAppListGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementFlowTableGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementL4PortRangeGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementActiveApplistGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementConflictGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonEnforcementAgingTimerGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonStatisticsGroup"),
        ("ALCATEL-ENT1-APP-MON-MIB", "alaAppMonVCTopologyGroup"))
)
if mibBuilder.loadTexts:
    alaAppMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-APP-MON-MIB",
    **{"alaAppMonMIB": alaAppMonMIB,
       "alaAppMonMIBNotifications": alaAppMonMIBNotifications,
       "alaAppMonAppRecordFileCreated": alaAppMonAppRecordFileCreated,
       "alaAppMonFlowRecordFileCreated": alaAppMonFlowRecordFileCreated,
       "alaAppMonMIBObjects": alaAppMonMIBObjects,
       "alaAppMonCertConfig": alaAppMonCertConfig,
       "alaAppMonUpdateSignatureFile": alaAppMonUpdateSignatureFile,
       "alaAppMonUpdateSignatureStatus": alaAppMonUpdateSignatureStatus,
       "alaAppMonConfig": alaAppMonConfig,
       "alaAppMonAdminStatus": alaAppMonAdminStatus,
       "alaAppMonUpdateAppList": alaAppMonUpdateAppList,
       "alaAppMonClearAppList": alaAppMonClearAppList,
       "alaAppMonFlowTableFlush": alaAppMonFlowTableFlush,
       "alaAppMonAgingInterval": alaAppMonAgingInterval,
       "alaAppMonAppliedApplications": alaAppMonAppliedApplications,
       "alaAppMonApplicationPoolApplications": alaAppMonApplicationPoolApplications,
       "alaAppMonSignatureFileVersion": alaAppMonSignatureFileVersion,
       "alaAppMonSignatureFileAppCount": alaAppMonSignatureFileAppCount,
       "alaAppMonSignatureFileName": alaAppMonSignatureFileName,
       "alaAppMonAppGrpFromAppName": alaAppMonAppGrpFromAppName,
       "alaAppMonAppGrpToAppName": alaAppMonAppGrpToAppName,
       "alaAppMonAddAppGrpName": alaAppMonAddAppGrpName,
       "alaAppMonOperationalStatus": alaAppMonOperationalStatus,
       "alaAppMonForceFlowSyncStatus": alaAppMonForceFlowSyncStatus,
       "alaAppMonAutoGroupCreation": alaAppMonAutoGroupCreation,
       "alaAppMonLoggingThresholdFlows": alaAppMonLoggingThresholdFlows,
       "alaAppMonAddRemoveAppGrpName": alaAppMonAddRemoveAppGrpName,
       "alaAppMonAOSCompatibilityVersion": alaAppMonAOSCompatibilityVersion,
       "alaAppMonKitType": alaAppMonKitType,
       "alaAppMonUpgradedKitType": alaAppMonUpgradedKitType,
       "alaAppMonUpgradedSignatureFileVersion": alaAppMonUpgradedSignatureFileVersion,
       "alaAppMonClearConfig": alaAppMonClearConfig,
       "alaAppMonEnforcementIpv4": alaAppMonEnforcementIpv4,
       "alaAppMonEnforcementIpv6": alaAppMonEnforcementIpv6,
       "alaAppMonEnforcementFlowTableStatsAdminStatus": alaAppMonEnforcementFlowTableStatsAdminStatus,
       "alaAppMonEnforcementStatsInterval": alaAppMonEnforcementStatsInterval,
       "alaAppMonEnforcementLoggingThresholdFlows": alaAppMonEnforcementLoggingThresholdFlows,
       "alaAppMonFlowSyncEnforcementInterval": alaAppMonFlowSyncEnforcementInterval,
       "alaAppMonFlowSyncMonitorInterval": alaAppMonFlowSyncMonitorInterval,
       "alaAppMonEnforcementAppliedApplications": alaAppMonEnforcementAppliedApplications,
       "alaAppMonPortConfigTable": alaAppMonPortConfigTable,
       "alaAppMonPortConfigEntry": alaAppMonPortConfigEntry,
       "alaAppMonPortConfigSlotPortIndex": alaAppMonPortConfigSlotPortIndex,
       "alaAppMonPortConfigPortStatus": alaAppMonPortConfigPortStatus,
       "alaAppMonPortConfigOperStatus": alaAppMonPortConfigOperStatus,
       "alaAppMonEnforcementPortConfigTcpStatus": alaAppMonEnforcementPortConfigTcpStatus,
       "alaAppMonEnforcementPortConfigUdpStatus": alaAppMonEnforcementPortConfigUdpStatus,
       "alaAppMonAppPoolTable": alaAppMonAppPoolTable,
       "alaAppMonAppPoolEntry": alaAppMonAppPoolEntry,
       "alaAppMonAppPoolAppName": alaAppMonAppPoolAppName,
       "alaAppMonAppPoolCategory": alaAppMonAppPoolCategory,
       "alaAppMonAppPoolRevision": alaAppMonAppPoolRevision,
       "alaAppMonAppPoolAppStatus": alaAppMonAppPoolAppStatus,
       "alaAppMonEnforcementAppPoolAppID": alaAppMonEnforcementAppPoolAppID,
       "alaAppMonAppGroupTable": alaAppMonAppGroupTable,
       "alaAppMonAppGroupEntry": alaAppMonAppGroupEntry,
       "alaAppMonAppGroupName": alaAppMonAppGroupName,
       "alaAppMonAppGroupMember": alaAppMonAppGroupMember,
       "alaAppMonAppGroupBuiltIn": alaAppMonAppGroupBuiltIn,
       "alaAppMonAppGroupCategoryName": alaAppMonAppGroupCategoryName,
       "alaAppMonAppGrpId": alaAppMonAppGrpId,
       "alaAppMonAppGroupAppStatus": alaAppMonAppGroupAppStatus,
       "alaAppMonAppGroupStatus": alaAppMonAppGroupStatus,
       "alaAppMonAppListTable": alaAppMonAppListTable,
       "alaAppMonAppListEntry": alaAppMonAppListEntry,
       "alaAppMonAppListMemberName": alaAppMonAppListMemberName,
       "alaAppMonAppListMemberType": alaAppMonAppListMemberType,
       "alaAppMonAppListAppId": alaAppMonAppListAppId,
       "alaAppMonAppListAppStatus": alaAppMonAppListAppStatus,
       "alaAppMonAppListMemberStatus": alaAppMonAppListMemberStatus,
       "alaAppMonActiveAppListTable": alaAppMonActiveAppListTable,
       "alaAppMonActiveAppListEntry": alaAppMonActiveAppListEntry,
       "alaAppMonActiveAppListAppName": alaAppMonActiveAppListAppName,
       "alaAppMonActiveAppListAppGroupName": alaAppMonActiveAppListAppGroupName,
       "alaAppMonActiveAppListActiveFlowCount": alaAppMonActiveAppListActiveFlowCount,
       "alaAppMonActiveAppListAppId": alaAppMonActiveAppListAppId,
       "alaAppMonActiveAppListAppStatus": alaAppMonActiveAppListAppStatus,
       "alaAppMonSignatureFileTable": alaAppMonSignatureFileTable,
       "alaAppMonSignatureFileEntry": alaAppMonSignatureFileEntry,
       "alaAppMonSignatureFileAppName": alaAppMonSignatureFileAppName,
       "alaAppMonSignatureFileCategory": alaAppMonSignatureFileCategory,
       "alaAppMonFlowTable": alaAppMonFlowTable,
       "alaAppMonFlowEntry": alaAppMonFlowEntry,
       "alaAppMonFlowSourceIPType": alaAppMonFlowSourceIPType,
       "alaAppMonFlowSourceIP": alaAppMonFlowSourceIP,
       "alaAppMonFlowSrcPort": alaAppMonFlowSrcPort,
       "alaAppMonFlowDestIPType": alaAppMonFlowDestIPType,
       "alaAppMonFlowDestIP": alaAppMonFlowDestIP,
       "alaAppMonFlowDestPort": alaAppMonFlowDestPort,
       "alaAppMonFlowProtocol": alaAppMonFlowProtocol,
       "alaAppMonFlowAppName": alaAppMonFlowAppName,
       "alaAppMonFlowAppGrpName": alaAppMonFlowAppGrpName,
       "alaAppMonCurrentHourTable": alaAppMonCurrentHourTable,
       "alaAppMonCurrentHourEntry": alaAppMonCurrentHourEntry,
       "alaAppMonCurrentHourAppName": alaAppMonCurrentHourAppName,
       "alaAppMonCurrentHourAppGroupName": alaAppMonCurrentHourAppGroupName,
       "alaAppMonCurrentHrStatsMinActiveFlow": alaAppMonCurrentHrStatsMinActiveFlow,
       "alaAppMonCurrentHrStatsMaxActiveFlow": alaAppMonCurrentHrStatsMaxActiveFlow,
       "alaAppMonCurrentHrStatsAvgActiveFlow": alaAppMonCurrentHrStatsAvgActiveFlow,
       "alaAppMonCurrentHrStatsTotalFlow": alaAppMonCurrentHrStatsTotalFlow,
       "alaAppMon24HourTable": alaAppMon24HourTable,
       "alaAppMon24HourEntry": alaAppMon24HourEntry,
       "alaAppMon24HourAppName": alaAppMon24HourAppName,
       "alaAppMon24HrStatsMinActiveFlow": alaAppMon24HrStatsMinActiveFlow,
       "alaAppMon24HrStatsMaxActiveFlow": alaAppMon24HrStatsMaxActiveFlow,
       "alaAppMon24HrStatsAvgActiveFlow": alaAppMon24HrStatsAvgActiveFlow,
       "alaAppMon24HrStatsTotalFlow": alaAppMon24HrStatsTotalFlow,
       "alaAppMonHourlyTable": alaAppMonHourlyTable,
       "alaAppMonHourlyEntry": alaAppMonHourlyEntry,
       "alaAppMonHourlyAppName": alaAppMonHourlyAppName,
       "alaAppMonHour": alaAppMonHour,
       "alaAppMonHourlyAppGroupName": alaAppMonHourlyAppGroupName,
       "alaAppMonHourlyStatsMinActiveFlow": alaAppMonHourlyStatsMinActiveFlow,
       "alaAppMonHourlyStatsMaxActiveFlow": alaAppMonHourlyStatsMaxActiveFlow,
       "alaAppMonHourlyStatsAvgActiveFlow": alaAppMonHourlyStatsAvgActiveFlow,
       "alaAppMonHourlyStatsTotalFlow": alaAppMonHourlyStatsTotalFlow,
       "alaAppMonHourlyTimeInterval": alaAppMonHourlyTimeInterval,
       "alaAppMonHourlyTimeIntervalUTC": alaAppMonHourlyTimeIntervalUTC,
       "alaAppMonAppListConflictTable": alaAppMonAppListConflictTable,
       "alaAppMonAppListConflictEntry": alaAppMonAppListConflictEntry,
       "alaAppMonAppListConflictIndex": alaAppMonAppListConflictIndex,
       "alaAppMonAppListConflictAppID": alaAppMonAppListConflictAppID,
       "alaAppMonAppListConflictAppName": alaAppMonAppListConflictAppName,
       "alaAppMonAppListConflictAppGrpName": alaAppMonAppListConflictAppGrpName,
       "alaAppMonAppListConflictAppErrorType": alaAppMonAppListConflictAppErrorType,
       "alaAppMonEnforcementAppListTable": alaAppMonEnforcementAppListTable,
       "alaAppMonEnforcementAppListEntry": alaAppMonEnforcementAppListEntry,
       "alaAppMonEnforcementAppListMemberName": alaAppMonEnforcementAppListMemberName,
       "alaAppMonEnforcementAppListMemberType": alaAppMonEnforcementAppListMemberType,
       "alaAppMonEnforcementAppListAppOrGroupID": alaAppMonEnforcementAppListAppOrGroupID,
       "alaAppMonEnforcementAppListAppStatus": alaAppMonEnforcementAppListAppStatus,
       "alaAppMonEnforcementAppListMemberStatus": alaAppMonEnforcementAppListMemberStatus,
       "alaAppMonEnforcementFlowTable": alaAppMonEnforcementFlowTable,
       "alaAppMonEnforcementFlowEntry": alaAppMonEnforcementFlowEntry,
       "alaAppMonEnforcementFlowSourceIPType": alaAppMonEnforcementFlowSourceIPType,
       "alaAppMonEnforcementFlowSourceIP": alaAppMonEnforcementFlowSourceIP,
       "alaAppMonEnforcementFlowDestIPType": alaAppMonEnforcementFlowDestIPType,
       "alaAppMonEnforcementFlowDestIP": alaAppMonEnforcementFlowDestIP,
       "alaAppMonEnforcementFlowSrcPort": alaAppMonEnforcementFlowSrcPort,
       "alaAppMonEnforcementFlowDestPort": alaAppMonEnforcementFlowDestPort,
       "alaAppMonEnforcementFlowProtocol": alaAppMonEnforcementFlowProtocol,
       "alaAppMonEnforcementFlowAppName": alaAppMonEnforcementFlowAppName,
       "alaAppMonEnforcementFlowAppGrpName": alaAppMonEnforcementFlowAppGrpName,
       "alaAppMonEnforcementFlowPolicyRule": alaAppMonEnforcementFlowPolicyRule,
       "alaAppMonEnforcementFlowStartTime": alaAppMonEnforcementFlowStartTime,
       "alaAppMonEnforcementFlowPktCount": alaAppMonEnforcementFlowPktCount,
       "alaAppMonEnforcementFlowByteCount": alaAppMonEnforcementFlowByteCount,
       "alaAppMonEnforcementL4PortRangeTable": alaAppMonEnforcementL4PortRangeTable,
       "alaAppMonEnforcementL4PortRangeEntry": alaAppMonEnforcementL4PortRangeEntry,
       "alaAppMonEnforcementL4PortRangeID": alaAppMonEnforcementL4PortRangeID,
       "alaAppMonEnforcementL4PortRangeStart": alaAppMonEnforcementL4PortRangeStart,
       "alaAppMonEnforcementL4PortRangeEnd": alaAppMonEnforcementL4PortRangeEnd,
       "alaAppMonEnforcementL4PortType": alaAppMonEnforcementL4PortType,
       "alaAppMonEnforcementL4PortStatus": alaAppMonEnforcementL4PortStatus,
       "alaAppMonEnforcementActiveAppListTable": alaAppMonEnforcementActiveAppListTable,
       "alaAppMonEnforcementActiveAppListEntry": alaAppMonEnforcementActiveAppListEntry,
       "alaAppMonEnforcementActiveAppListAppName": alaAppMonEnforcementActiveAppListAppName,
       "alaAppMonEnforcementActiveAppListAppGroupName": alaAppMonEnforcementActiveAppListAppGroupName,
       "alaAppMonEnforcementActiveAppListActiveMatchedFlows": alaAppMonEnforcementActiveAppListActiveMatchedFlows,
       "alaAppMonEnforcementActiveAppListTotalMatchedFlows": alaAppMonEnforcementActiveAppListTotalMatchedFlows,
       "alaAppMonEnforcementActiveAppListAppID": alaAppMonEnforcementActiveAppListAppID,
       "alaAppMonEnforcementActiveAppListAppStatus": alaAppMonEnforcementActiveAppListAppStatus,
       "alaAppMonEnforcementActiveAppListActivePktCount": alaAppMonEnforcementActiveAppListActivePktCount,
       "alaAppMonEnforcementActiveAppListActiveByteCount": alaAppMonEnforcementActiveAppListActiveByteCount,
       "alaAppMonEnforcementActiveAppListGrossPktCount": alaAppMonEnforcementActiveAppListGrossPktCount,
       "alaAppMonEnforcementActiveAppListGrossByteCount": alaAppMonEnforcementActiveAppListGrossByteCount,
       "alaAppMonEnforcementAppListConflictTable": alaAppMonEnforcementAppListConflictTable,
       "alaAppMonEnforcementAppListConflictEntry": alaAppMonEnforcementAppListConflictEntry,
       "alaAppMonEnforcementAppListConflictIndex": alaAppMonEnforcementAppListConflictIndex,
       "alaAppMonEnforcementAppListConflictAppID": alaAppMonEnforcementAppListConflictAppID,
       "alaAppMonEnforcementAppListConflictAppName": alaAppMonEnforcementAppListConflictAppName,
       "alaAppMonEnforcementAppListConflictAppGrpName": alaAppMonEnforcementAppListConflictAppGrpName,
       "alaAppMonEnforcementAppListConflictAppErrorType": alaAppMonEnforcementAppListConflictAppErrorType,
       "alaAppMonEnforcementAgingTimerTable": alaAppMonEnforcementAgingTimerTable,
       "alaAppMonEnforcementAgingTimerEntry": alaAppMonEnforcementAgingTimerEntry,
       "alaAppMonEnforcementAgingTimerAppName": alaAppMonEnforcementAgingTimerAppName,
       "alaAppMonEnforcementTcpAgingTimerValue": alaAppMonEnforcementTcpAgingTimerValue,
       "alaAppMonEnforcementUdpAgingTimerValue": alaAppMonEnforcementUdpAgingTimerValue,
       "alaAppMonStatisticsTable": alaAppMonStatisticsTable,
       "alaAppMonStatisticsEntry": alaAppMonStatisticsEntry,
       "alaAppMonStatsSlotIndex": alaAppMonStatsSlotIndex,
       "alaAppMonTotalEnforcementActiveFlows": alaAppMonTotalEnforcementActiveFlows,
       "alaAppMonTotalFlowTableInUseFlows": alaAppMonTotalFlowTableInUseFlows,
       "alaAppMonTCPOverflowFlows": alaAppMonTCPOverflowFlows,
       "alaAppMonUDPOverflowPackets": alaAppMonUDPOverflowPackets,
       "alaAppMonVCTopologyTable": alaAppMonVCTopologyTable,
       "alaAppMonVCTopologyEntry": alaAppMonVCTopologyEntry,
       "alaAppMonVCTopologyChassisIndex": alaAppMonVCTopologyChassisIndex,
       "alaAppMonVCTopologyChassisType": alaAppMonVCTopologyChassisType,
       "alaAppMonVCTopologyDesignatedChassisIndex": alaAppMonVCTopologyDesignatedChassisIndex,
       "alaAppMonMIBConformance": alaAppMonMIBConformance,
       "alaAppMonMIBGroups": alaAppMonMIBGroups,
       "alaAppMonPortConfigGroup": alaAppMonPortConfigGroup,
       "alaAppMonAppPoolGroup": alaAppMonAppPoolGroup,
       "alaAppMonAppGroupsGroup": alaAppMonAppGroupsGroup,
       "alaAppMonAppListGroup": alaAppMonAppListGroup,
       "alaAppMonConfigGroup": alaAppMonConfigGroup,
       "alaAppMonActiveAppListGroup": alaAppMonActiveAppListGroup,
       "alaAppMonSignatureFileTableGroup": alaAppMonSignatureFileTableGroup,
       "alaAppMonFlowTableGroup": alaAppMonFlowTableGroup,
       "alaAppMonCurrentHourGroup": alaAppMonCurrentHourGroup,
       "alaAppMon24HourGroup": alaAppMon24HourGroup,
       "alaAppMonHourlyGroup": alaAppMonHourlyGroup,
       "alaAppMonNotificationGroup": alaAppMonNotificationGroup,
       "alaAppMonAppListConflictGroup": alaAppMonAppListConflictGroup,
       "alaAppMonCertConfigGroup": alaAppMonCertConfigGroup,
       "alaAppMonEnforcementAppListGroup": alaAppMonEnforcementAppListGroup,
       "alaAppMonEnforcementFlowTableGroup": alaAppMonEnforcementFlowTableGroup,
       "alaAppMonEnforcementL4PortRangeGroup": alaAppMonEnforcementL4PortRangeGroup,
       "alaAppMonEnforcementActiveApplistGroup": alaAppMonEnforcementActiveApplistGroup,
       "alaAppMonEnforcementConflictGroup": alaAppMonEnforcementConflictGroup,
       "alaAppMonEnforcementAgingTimerGroup": alaAppMonEnforcementAgingTimerGroup,
       "alaAppMonStatisticsGroup": alaAppMonStatisticsGroup,
       "alaAppMonVCTopologyGroup": alaAppMonVCTopologyGroup,
       "alaAppMonMIBCompliances": alaAppMonMIBCompliances,
       "alaAppMonMIBCompliance": alaAppMonMIBCompliance}
)
