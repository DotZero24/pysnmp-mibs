# SNMP MIB module (ALCATEL-ENT1-DPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-DPI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:16 2025
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

(softentIND1DPI,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1DPI")

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

alaDPIMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1)
)
if mibBuilder.loadTexts:
    alaDPIMIB.setRevisions(
        ("2012-05-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaDPIMIBNotifications_ObjectIdentity = ObjectIdentity
alaDPIMIBNotifications = _AlaDPIMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 0)
)
_AlaDPIMIBObjects_ObjectIdentity = ObjectIdentity
alaDPIMIBObjects = _AlaDPIMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1)
)
if mibBuilder.loadTexts:
    alaDPIMIBObjects.setStatus("current")
_AlaDPICertConfig_ObjectIdentity = ObjectIdentity
alaDPICertConfig = _AlaDPICertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 1)
)


class _AlaDPIUpdateSignatureFile_Type(Integer32):
    """Custom type alaDPIUpdateSignatureFile based on Integer32"""
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


_AlaDPIUpdateSignatureFile_Type.__name__ = "Integer32"
_AlaDPIUpdateSignatureFile_Object = MibScalar
alaDPIUpdateSignatureFile = _AlaDPIUpdateSignatureFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 1, 1),
    _AlaDPIUpdateSignatureFile_Type()
)
alaDPIUpdateSignatureFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIUpdateSignatureFile.setStatus("current")


class _AlaDPIUpdateSignatureStatus_Type(Integer32):
    """Custom type alaDPIUpdateSignatureStatus based on Integer32"""
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


_AlaDPIUpdateSignatureStatus_Type.__name__ = "Integer32"
_AlaDPIUpdateSignatureStatus_Object = MibScalar
alaDPIUpdateSignatureStatus = _AlaDPIUpdateSignatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 1, 2),
    _AlaDPIUpdateSignatureStatus_Type()
)
alaDPIUpdateSignatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIUpdateSignatureStatus.setStatus("current")
_AlaDPIConfig_ObjectIdentity = ObjectIdentity
alaDPIConfig = _AlaDPIConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2)
)


class _AlaDPIAdminStatus_Type(Integer32):
    """Custom type alaDPIAdminStatus based on Integer32"""
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


_AlaDPIAdminStatus_Type.__name__ = "Integer32"
_AlaDPIAdminStatus_Object = MibScalar
alaDPIAdminStatus = _AlaDPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 1),
    _AlaDPIAdminStatus_Type()
)
alaDPIAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAdminStatus.setStatus("current")


class _AlaDPIUpdateAppList_Type(Integer32):
    """Custom type alaDPIUpdateAppList based on Integer32"""
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


_AlaDPIUpdateAppList_Type.__name__ = "Integer32"
_AlaDPIUpdateAppList_Object = MibScalar
alaDPIUpdateAppList = _AlaDPIUpdateAppList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 2),
    _AlaDPIUpdateAppList_Type()
)
alaDPIUpdateAppList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIUpdateAppList.setStatus("current")


class _AlaDPIUpdateAppListStatus_Type(Integer32):
    """Custom type alaDPIUpdateAppListStatus based on Integer32"""
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
          ("successfullyUpdated", 3),
          ("failedToUpdate", 4),
          ("maximumAppCountExceeded", 5))
    )


_AlaDPIUpdateAppListStatus_Type.__name__ = "Integer32"
_AlaDPIUpdateAppListStatus_Object = MibScalar
alaDPIUpdateAppListStatus = _AlaDPIUpdateAppListStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 3),
    _AlaDPIUpdateAppListStatus_Type()
)
alaDPIUpdateAppListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIUpdateAppListStatus.setStatus("current")


class _AlaDPIClearAppList_Type(Integer32):
    """Custom type alaDPIClearAppList based on Integer32"""
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
          ("clear", 2))
    )


_AlaDPIClearAppList_Type.__name__ = "Integer32"
_AlaDPIClearAppList_Object = MibScalar
alaDPIClearAppList = _AlaDPIClearAppList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 4),
    _AlaDPIClearAppList_Type()
)
alaDPIClearAppList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIClearAppList.setStatus("current")


class _AlaDPIFlowTableFlush_Type(Integer32):
    """Custom type alaDPIFlowTableFlush based on Integer32"""
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
          ("flush", 2))
    )


_AlaDPIFlowTableFlush_Type.__name__ = "Integer32"
_AlaDPIFlowTableFlush_Object = MibScalar
alaDPIFlowTableFlush = _AlaDPIFlowTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 5),
    _AlaDPIFlowTableFlush_Type()
)
alaDPIFlowTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIFlowTableFlush.setStatus("current")


class _AlaDPIStatsInterval_Type(Integer32):
    """Custom type alaDPIStatsInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 3600),
    )


_AlaDPIStatsInterval_Type.__name__ = "Integer32"
_AlaDPIStatsInterval_Object = MibScalar
alaDPIStatsInterval = _AlaDPIStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 6),
    _AlaDPIStatsInterval_Type()
)
alaDPIStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIStatsInterval.setStatus("current")


class _AlaDPIClearStats_Type(Integer32):
    """Custom type alaDPIClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stats", 1)
    )


_AlaDPIClearStats_Type.__name__ = "Integer32"
_AlaDPIClearStats_Object = MibScalar
alaDPIClearStats = _AlaDPIClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 7),
    _AlaDPIClearStats_Type()
)
alaDPIClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIClearStats.setStatus("current")


class _AlaDPIIpv4_Type(Integer32):
    """Custom type alaDPIIpv4 based on Integer32"""
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


_AlaDPIIpv4_Type.__name__ = "Integer32"
_AlaDPIIpv4_Object = MibScalar
alaDPIIpv4 = _AlaDPIIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 8),
    _AlaDPIIpv4_Type()
)
alaDPIIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIIpv4.setStatus("current")


class _AlaDPIIpv6_Type(Integer32):
    """Custom type alaDPIIpv6 based on Integer32"""
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


_AlaDPIIpv6_Type.__name__ = "Integer32"
_AlaDPIIpv6_Object = MibScalar
alaDPIIpv6 = _AlaDPIIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 9),
    _AlaDPIIpv6_Type()
)
alaDPIIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIIpv6.setStatus("current")
_AlaDPIAppliedSignatures_Type = Integer32
_AlaDPIAppliedSignatures_Object = MibScalar
alaDPIAppliedSignatures = _AlaDPIAppliedSignatures_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 10),
    _AlaDPIAppliedSignatures_Type()
)
alaDPIAppliedSignatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppliedSignatures.setStatus("current")
_AlaDPIApplicationPoolSignatures_Type = Integer32
_AlaDPIApplicationPoolSignatures_Object = MibScalar
alaDPIApplicationPoolSignatures = _AlaDPIApplicationPoolSignatures_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 11),
    _AlaDPIApplicationPoolSignatures_Type()
)
alaDPIApplicationPoolSignatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIApplicationPoolSignatures.setStatus("current")


class _AlaDPISignatureFileVersion_Type(SnmpAdminString):
    """Custom type alaDPISignatureFileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPISignatureFileVersion_Type.__name__ = "SnmpAdminString"
_AlaDPISignatureFileVersion_Object = MibScalar
alaDPISignatureFileVersion = _AlaDPISignatureFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 12),
    _AlaDPISignatureFileVersion_Type()
)
alaDPISignatureFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPISignatureFileVersion.setStatus("current")
_AlaDPISignatureFileAppCount_Type = Integer32
_AlaDPISignatureFileAppCount_Object = MibScalar
alaDPISignatureFileAppCount = _AlaDPISignatureFileAppCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 13),
    _AlaDPISignatureFileAppCount_Type()
)
alaDPISignatureFileAppCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPISignatureFileAppCount.setStatus("current")


class _AlaDPISignatureFileName_Type(SnmpAdminString):
    """Custom type alaDPISignatureFileName based on SnmpAdminString"""
    defaultValue = OctetString("/flash/UAppSig.upgrade_kit")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPISignatureFileName_Type.__name__ = "SnmpAdminString"
_AlaDPISignatureFileName_Object = MibScalar
alaDPISignatureFileName = _AlaDPISignatureFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 14),
    _AlaDPISignatureFileName_Type()
)
alaDPISignatureFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPISignatureFileName.setStatus("current")


class _AlaDPIAppGrpFromAppName_Type(SnmpAdminString):
    """Custom type alaDPIAppGrpFromAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIAppGrpFromAppName_Type.__name__ = "SnmpAdminString"
_AlaDPIAppGrpFromAppName_Object = MibScalar
alaDPIAppGrpFromAppName = _AlaDPIAppGrpFromAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 15),
    _AlaDPIAppGrpFromAppName_Type()
)
alaDPIAppGrpFromAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAppGrpFromAppName.setStatus("current")


class _AlaDPIAppGrpToAppName_Type(SnmpAdminString):
    """Custom type alaDPIAppGrpToAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIAppGrpToAppName_Type.__name__ = "SnmpAdminString"
_AlaDPIAppGrpToAppName_Object = MibScalar
alaDPIAppGrpToAppName = _AlaDPIAppGrpToAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 16),
    _AlaDPIAppGrpToAppName_Type()
)
alaDPIAppGrpToAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAppGrpToAppName.setStatus("current")


class _AlaDPIAddAppGrpName_Type(SnmpAdminString):
    """Custom type alaDPIAddAppGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPIAddAppGrpName_Type.__name__ = "SnmpAdminString"
_AlaDPIAddAppGrpName_Object = MibScalar
alaDPIAddAppGrpName = _AlaDPIAddAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 17),
    _AlaDPIAddAppGrpName_Type()
)
alaDPIAddAppGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAddAppGrpName.setStatus("current")


class _AlaDPIAutoGroupCreation_Type(Integer32):
    """Custom type alaDPIAutoGroupCreation based on Integer32"""
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


_AlaDPIAutoGroupCreation_Type.__name__ = "Integer32"
_AlaDPIAutoGroupCreation_Object = MibScalar
alaDPIAutoGroupCreation = _AlaDPIAutoGroupCreation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 18),
    _AlaDPIAutoGroupCreation_Type()
)
alaDPIAutoGroupCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAutoGroupCreation.setStatus("current")


class _AlaDPIAddRemoveAppGrpName_Type(Integer32):
    """Custom type alaDPIAddRemoveAppGrpName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addGroup", 1),
          ("removeGroup", 2))
    )


_AlaDPIAddRemoveAppGrpName_Type.__name__ = "Integer32"
_AlaDPIAddRemoveAppGrpName_Object = MibScalar
alaDPIAddRemoveAppGrpName = _AlaDPIAddRemoveAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 19),
    _AlaDPIAddRemoveAppGrpName_Type()
)
alaDPIAddRemoveAppGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAddRemoveAppGrpName.setStatus("current")
_AlaDPIAOSCompatibilityVersion_Type = Integer32
_AlaDPIAOSCompatibilityVersion_Object = MibScalar
alaDPIAOSCompatibilityVersion = _AlaDPIAOSCompatibilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 20),
    _AlaDPIAOSCompatibilityVersion_Type()
)
alaDPIAOSCompatibilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAOSCompatibilityVersion.setStatus("current")


class _AlaDPIKitType_Type(Integer32):
    """Custom type alaDPIKitType based on Integer32"""
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


_AlaDPIKitType_Type.__name__ = "Integer32"
_AlaDPIKitType_Object = MibScalar
alaDPIKitType = _AlaDPIKitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 21),
    _AlaDPIKitType_Type()
)
alaDPIKitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIKitType.setStatus("current")


class _AlaDPIUpgradedKitType_Type(Integer32):
    """Custom type alaDPIUpgradedKitType based on Integer32"""
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


_AlaDPIUpgradedKitType_Type.__name__ = "Integer32"
_AlaDPIUpgradedKitType_Object = MibScalar
alaDPIUpgradedKitType = _AlaDPIUpgradedKitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 22),
    _AlaDPIUpgradedKitType_Type()
)
alaDPIUpgradedKitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIUpgradedKitType.setStatus("current")


class _AlaDPIUpgradedSignatureFileVersion_Type(SnmpAdminString):
    """Custom type alaDPIUpgradedSignatureFileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPIUpgradedSignatureFileVersion_Type.__name__ = "SnmpAdminString"
_AlaDPIUpgradedSignatureFileVersion_Object = MibScalar
alaDPIUpgradedSignatureFileVersion = _AlaDPIUpgradedSignatureFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 23),
    _AlaDPIUpgradedSignatureFileVersion_Type()
)
alaDPIUpgradedSignatureFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIUpgradedSignatureFileVersion.setStatus("current")


class _AlaDPILoggingThresholdFlows_Type(Integer32):
    """Custom type alaDPILoggingThresholdFlows based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 600000),
    )


_AlaDPILoggingThresholdFlows_Type.__name__ = "Integer32"
_AlaDPILoggingThresholdFlows_Object = MibScalar
alaDPILoggingThresholdFlows = _AlaDPILoggingThresholdFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 24),
    _AlaDPILoggingThresholdFlows_Type()
)
alaDPILoggingThresholdFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPILoggingThresholdFlows.setStatus("current")


class _AlaDPIClearConfig_Type(Integer32):
    """Custom type alaDPIClearConfig based on Integer32"""
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


_AlaDPIClearConfig_Type.__name__ = "Integer32"
_AlaDPIClearConfig_Object = MibScalar
alaDPIClearConfig = _AlaDPIClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 25),
    _AlaDPIClearConfig_Type()
)
alaDPIClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIClearConfig.setStatus("current")


class _AlaDPIProxyServerDefaultPort1_Type(Integer32):
    """Custom type alaDPIProxyServerDefaultPort1 based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerDefaultPort1_Type.__name__ = "Integer32"
_AlaDPIProxyServerDefaultPort1_Object = MibScalar
alaDPIProxyServerDefaultPort1 = _AlaDPIProxyServerDefaultPort1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 26),
    _AlaDPIProxyServerDefaultPort1_Type()
)
alaDPIProxyServerDefaultPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerDefaultPort1.setStatus("current")


class _AlaDPIProxyServerDefaultPort2_Type(Integer32):
    """Custom type alaDPIProxyServerDefaultPort2 based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerDefaultPort2_Type.__name__ = "Integer32"
_AlaDPIProxyServerDefaultPort2_Object = MibScalar
alaDPIProxyServerDefaultPort2 = _AlaDPIProxyServerDefaultPort2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 27),
    _AlaDPIProxyServerDefaultPort2_Type()
)
alaDPIProxyServerDefaultPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerDefaultPort2.setStatus("current")


class _AlaDPIProxyServerPort1_Type(Integer32):
    """Custom type alaDPIProxyServerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort1_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort1_Object = MibScalar
alaDPIProxyServerPort1 = _AlaDPIProxyServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 28),
    _AlaDPIProxyServerPort1_Type()
)
alaDPIProxyServerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort1.setStatus("current")


class _AlaDPIProxyServerPort2_Type(Integer32):
    """Custom type alaDPIProxyServerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort2_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort2_Object = MibScalar
alaDPIProxyServerPort2 = _AlaDPIProxyServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 29),
    _AlaDPIProxyServerPort2_Type()
)
alaDPIProxyServerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort2.setStatus("current")


class _AlaDPIProxyServerPort3_Type(Integer32):
    """Custom type alaDPIProxyServerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort3_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort3_Object = MibScalar
alaDPIProxyServerPort3 = _AlaDPIProxyServerPort3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 30),
    _AlaDPIProxyServerPort3_Type()
)
alaDPIProxyServerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort3.setStatus("current")


class _AlaDPIProxyServerPort4_Type(Integer32):
    """Custom type alaDPIProxyServerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort4_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort4_Object = MibScalar
alaDPIProxyServerPort4 = _AlaDPIProxyServerPort4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 31),
    _AlaDPIProxyServerPort4_Type()
)
alaDPIProxyServerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort4.setStatus("current")


class _AlaDPIProxyServerPort5_Type(Integer32):
    """Custom type alaDPIProxyServerPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort5_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort5_Object = MibScalar
alaDPIProxyServerPort5 = _AlaDPIProxyServerPort5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 32),
    _AlaDPIProxyServerPort5_Type()
)
alaDPIProxyServerPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort5.setStatus("current")


class _AlaDPIProxyServerPort6_Type(Integer32):
    """Custom type alaDPIProxyServerPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort6_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort6_Object = MibScalar
alaDPIProxyServerPort6 = _AlaDPIProxyServerPort6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 33),
    _AlaDPIProxyServerPort6_Type()
)
alaDPIProxyServerPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort6.setStatus("current")


class _AlaDPIProxyServerPort7_Type(Integer32):
    """Custom type alaDPIProxyServerPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort7_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort7_Object = MibScalar
alaDPIProxyServerPort7 = _AlaDPIProxyServerPort7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 34),
    _AlaDPIProxyServerPort7_Type()
)
alaDPIProxyServerPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort7.setStatus("current")


class _AlaDPIProxyServerPort8_Type(Integer32):
    """Custom type alaDPIProxyServerPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIProxyServerPort8_Type.__name__ = "Integer32"
_AlaDPIProxyServerPort8_Object = MibScalar
alaDPIProxyServerPort8 = _AlaDPIProxyServerPort8_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 35),
    _AlaDPIProxyServerPort8_Type()
)
alaDPIProxyServerPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIProxyServerPort8.setStatus("current")


class _AlaDPIAddRemoveProxyServerPort_Type(Integer32):
    """Custom type alaDPIAddRemoveProxyServerPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addPort", 1),
          ("removePort", 2))
    )


_AlaDPIAddRemoveProxyServerPort_Type.__name__ = "Integer32"
_AlaDPIAddRemoveProxyServerPort_Object = MibScalar
alaDPIAddRemoveProxyServerPort = _AlaDPIAddRemoveProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 36),
    _AlaDPIAddRemoveProxyServerPort_Type()
)
alaDPIAddRemoveProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAddRemoveProxyServerPort.setStatus("current")


class _AlaDPIFlowTableStatsAdminStatus_Type(Integer32):
    """Custom type alaDPIFlowTableStatsAdminStatus based on Integer32"""
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


_AlaDPIFlowTableStatsAdminStatus_Type.__name__ = "Integer32"
_AlaDPIFlowTableStatsAdminStatus_Object = MibScalar
alaDPIFlowTableStatsAdminStatus = _AlaDPIFlowTableStatsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 2, 37),
    _AlaDPIFlowTableStatsAdminStatus_Type()
)
alaDPIFlowTableStatsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIFlowTableStatsAdminStatus.setStatus("current")
_AlaDPIPortConfigTable_Object = MibTable
alaDPIPortConfigTable = _AlaDPIPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaDPIPortConfigTable.setStatus("current")
_AlaDPIPortConfigEntry_Object = MibTableRow
alaDPIPortConfigEntry = _AlaDPIPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1)
)
alaDPIPortConfigEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigSlotPortIndex"),
)
if mibBuilder.loadTexts:
    alaDPIPortConfigEntry.setStatus("current")
_AlaDPIPortConfigSlotPortIndex_Type = InterfaceIndex
_AlaDPIPortConfigSlotPortIndex_Object = MibTableColumn
alaDPIPortConfigSlotPortIndex = _AlaDPIPortConfigSlotPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1, 1),
    _AlaDPIPortConfigSlotPortIndex_Type()
)
alaDPIPortConfigSlotPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIPortConfigSlotPortIndex.setStatus("current")


class _AlaDPIPortConfigPortStatus_Type(Integer32):
    """Custom type alaDPIPortConfigPortStatus based on Integer32"""
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


_AlaDPIPortConfigPortStatus_Type.__name__ = "Integer32"
_AlaDPIPortConfigPortStatus_Object = MibTableColumn
alaDPIPortConfigPortStatus = _AlaDPIPortConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1, 2),
    _AlaDPIPortConfigPortStatus_Type()
)
alaDPIPortConfigPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIPortConfigPortStatus.setStatus("current")


class _AlaDPIPortConfigTcpStatus_Type(Integer32):
    """Custom type alaDPIPortConfigTcpStatus based on Integer32"""
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


_AlaDPIPortConfigTcpStatus_Type.__name__ = "Integer32"
_AlaDPIPortConfigTcpStatus_Object = MibTableColumn
alaDPIPortConfigTcpStatus = _AlaDPIPortConfigTcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1, 3),
    _AlaDPIPortConfigTcpStatus_Type()
)
alaDPIPortConfigTcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIPortConfigTcpStatus.setStatus("current")


class _AlaDPIPortConfigUdpStatus_Type(Integer32):
    """Custom type alaDPIPortConfigUdpStatus based on Integer32"""
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


_AlaDPIPortConfigUdpStatus_Type.__name__ = "Integer32"
_AlaDPIPortConfigUdpStatus_Object = MibTableColumn
alaDPIPortConfigUdpStatus = _AlaDPIPortConfigUdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1, 4),
    _AlaDPIPortConfigUdpStatus_Type()
)
alaDPIPortConfigUdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIPortConfigUdpStatus.setStatus("current")


class _AlaDPIPortConfigPortTypeStatus_Type(Integer32):
    """Custom type alaDPIPortConfigPortTypeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonUplink", 1),
          ("uplink", 2))
    )


_AlaDPIPortConfigPortTypeStatus_Type.__name__ = "Integer32"
_AlaDPIPortConfigPortTypeStatus_Object = MibTableColumn
alaDPIPortConfigPortTypeStatus = _AlaDPIPortConfigPortTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1, 5),
    _AlaDPIPortConfigPortTypeStatus_Type()
)
alaDPIPortConfigPortTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIPortConfigPortTypeStatus.setStatus("current")


class _AlaDPIPortConfigOperStatus_Type(Integer32):
    """Custom type alaDPIPortConfigOperStatus based on Integer32"""
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


_AlaDPIPortConfigOperStatus_Type.__name__ = "Integer32"
_AlaDPIPortConfigOperStatus_Object = MibTableColumn
alaDPIPortConfigOperStatus = _AlaDPIPortConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 3, 1, 6),
    _AlaDPIPortConfigOperStatus_Type()
)
alaDPIPortConfigOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIPortConfigOperStatus.setStatus("current")
_AlaDPIAppPoolTable_Object = MibTable
alaDPIAppPoolTable = _AlaDPIAppPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDPIAppPoolTable.setStatus("current")
_AlaDPIAppPoolEntry_Object = MibTableRow
alaDPIAppPoolEntry = _AlaDPIAppPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4, 1)
)
alaDPIAppPoolEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIAppPoolAppName"),
)
if mibBuilder.loadTexts:
    alaDPIAppPoolEntry.setStatus("current")


class _AlaDPIAppPoolAppName_Type(SnmpAdminString):
    """Custom type alaDPIAppPoolAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIAppPoolAppName_Type.__name__ = "SnmpAdminString"
_AlaDPIAppPoolAppName_Object = MibTableColumn
alaDPIAppPoolAppName = _AlaDPIAppPoolAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4, 1, 1),
    _AlaDPIAppPoolAppName_Type()
)
alaDPIAppPoolAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIAppPoolAppName.setStatus("current")


class _AlaDPIAppPoolCategory_Type(SnmpAdminString):
    """Custom type alaDPIAppPoolCategory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPIAppPoolCategory_Type.__name__ = "SnmpAdminString"
_AlaDPIAppPoolCategory_Object = MibTableColumn
alaDPIAppPoolCategory = _AlaDPIAppPoolCategory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4, 1, 2),
    _AlaDPIAppPoolCategory_Type()
)
alaDPIAppPoolCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppPoolCategory.setStatus("current")


class _AlaDPIAppPoolRevision_Type(SnmpAdminString):
    """Custom type alaDPIAppPoolRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AlaDPIAppPoolRevision_Type.__name__ = "SnmpAdminString"
_AlaDPIAppPoolRevision_Object = MibTableColumn
alaDPIAppPoolRevision = _AlaDPIAppPoolRevision_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4, 1, 3),
    _AlaDPIAppPoolRevision_Type()
)
alaDPIAppPoolRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppPoolRevision.setStatus("current")
_AlaDPIAppPoolAppID_Type = Integer32
_AlaDPIAppPoolAppID_Object = MibTableColumn
alaDPIAppPoolAppID = _AlaDPIAppPoolAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4, 1, 4),
    _AlaDPIAppPoolAppID_Type()
)
alaDPIAppPoolAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppPoolAppID.setStatus("current")


class _AlaDPIAppPoolAppStatus_Type(Integer32):
    """Custom type alaDPIAppPoolAppStatus based on Integer32"""
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


_AlaDPIAppPoolAppStatus_Type.__name__ = "Integer32"
_AlaDPIAppPoolAppStatus_Object = MibTableColumn
alaDPIAppPoolAppStatus = _AlaDPIAppPoolAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 4, 1, 5),
    _AlaDPIAppPoolAppStatus_Type()
)
alaDPIAppPoolAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppPoolAppStatus.setStatus("current")
_AlaDPIAppGroupTable_Object = MibTable
alaDPIAppGroupTable = _AlaDPIAppGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaDPIAppGroupTable.setStatus("current")
_AlaDPIAppGroupEntry_Object = MibTableRow
alaDPIAppGroupEntry = _AlaDPIAppGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1)
)
alaDPIAppGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupName"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupMember"),
)
if mibBuilder.loadTexts:
    alaDPIAppGroupEntry.setStatus("current")


class _AlaDPIAppGroupName_Type(SnmpAdminString):
    """Custom type alaDPIAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AlaDPIAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaDPIAppGroupName_Object = MibTableColumn
alaDPIAppGroupName = _AlaDPIAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 1),
    _AlaDPIAppGroupName_Type()
)
alaDPIAppGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIAppGroupName.setStatus("current")


class _AlaDPIAppGroupMember_Type(SnmpAdminString):
    """Custom type alaDPIAppGroupMember based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIAppGroupMember_Type.__name__ = "SnmpAdminString"
_AlaDPIAppGroupMember_Object = MibTableColumn
alaDPIAppGroupMember = _AlaDPIAppGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 2),
    _AlaDPIAppGroupMember_Type()
)
alaDPIAppGroupMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIAppGroupMember.setStatus("current")


class _AlaDPIAppGroupMemberType_Type(Integer32):
    """Custom type alaDPIAppGroupMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("app", 1),
          ("category", 2))
    )


_AlaDPIAppGroupMemberType_Type.__name__ = "Integer32"
_AlaDPIAppGroupMemberType_Object = MibTableColumn
alaDPIAppGroupMemberType = _AlaDPIAppGroupMemberType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 3),
    _AlaDPIAppGroupMemberType_Type()
)
alaDPIAppGroupMemberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIAppGroupMemberType.setStatus("current")


class _AlaDPIAppGroupCategoryName_Type(SnmpAdminString):
    """Custom type alaDPIAppGroupCategoryName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPIAppGroupCategoryName_Type.__name__ = "SnmpAdminString"
_AlaDPIAppGroupCategoryName_Object = MibTableColumn
alaDPIAppGroupCategoryName = _AlaDPIAppGroupCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 4),
    _AlaDPIAppGroupCategoryName_Type()
)
alaDPIAppGroupCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppGroupCategoryName.setStatus("current")
_AlaDPIAppGroupID_Type = Integer32
_AlaDPIAppGroupID_Object = MibTableColumn
alaDPIAppGroupID = _AlaDPIAppGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 5),
    _AlaDPIAppGroupID_Type()
)
alaDPIAppGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppGroupID.setStatus("current")


class _AlaDPIAppGroupAppStatus_Type(Integer32):
    """Custom type alaDPIAppGroupAppStatus based on Integer32"""
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


_AlaDPIAppGroupAppStatus_Type.__name__ = "Integer32"
_AlaDPIAppGroupAppStatus_Object = MibTableColumn
alaDPIAppGroupAppStatus = _AlaDPIAppGroupAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 6),
    _AlaDPIAppGroupAppStatus_Type()
)
alaDPIAppGroupAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppGroupAppStatus.setStatus("current")
_AlaDPIAppGroupStatus_Type = RowStatus
_AlaDPIAppGroupStatus_Object = MibTableColumn
alaDPIAppGroupStatus = _AlaDPIAppGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 5, 1, 7),
    _AlaDPIAppGroupStatus_Type()
)
alaDPIAppGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIAppGroupStatus.setStatus("current")
_AlaDPIAppListTable_Object = MibTable
alaDPIAppListTable = _AlaDPIAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaDPIAppListTable.setStatus("current")
_AlaDPIAppListEntry_Object = MibTableRow
alaDPIAppListEntry = _AlaDPIAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6, 1)
)
alaDPIAppListEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIAppListMemberName"),
)
if mibBuilder.loadTexts:
    alaDPIAppListEntry.setStatus("current")


class _AlaDPIAppListMemberName_Type(SnmpAdminString):
    """Custom type alaDPIAppListMemberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIAppListMemberName_Type.__name__ = "SnmpAdminString"
_AlaDPIAppListMemberName_Object = MibTableColumn
alaDPIAppListMemberName = _AlaDPIAppListMemberName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6, 1, 1),
    _AlaDPIAppListMemberName_Type()
)
alaDPIAppListMemberName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIAppListMemberName.setStatus("current")


class _AlaDPIAppListMemberType_Type(Integer32):
    """Custom type alaDPIAppListMemberType based on Integer32"""
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


_AlaDPIAppListMemberType_Type.__name__ = "Integer32"
_AlaDPIAppListMemberType_Object = MibTableColumn
alaDPIAppListMemberType = _AlaDPIAppListMemberType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6, 1, 2),
    _AlaDPIAppListMemberType_Type()
)
alaDPIAppListMemberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIAppListMemberType.setStatus("current")
_AlaDPIAppListAppOrGroupID_Type = Integer32
_AlaDPIAppListAppOrGroupID_Object = MibTableColumn
alaDPIAppListAppOrGroupID = _AlaDPIAppListAppOrGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6, 1, 3),
    _AlaDPIAppListAppOrGroupID_Type()
)
alaDPIAppListAppOrGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppListAppOrGroupID.setStatus("current")


class _AlaDPIAppListAppStatus_Type(Integer32):
    """Custom type alaDPIAppListAppStatus based on Integer32"""
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


_AlaDPIAppListAppStatus_Type.__name__ = "Integer32"
_AlaDPIAppListAppStatus_Object = MibTableColumn
alaDPIAppListAppStatus = _AlaDPIAppListAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6, 1, 4),
    _AlaDPIAppListAppStatus_Type()
)
alaDPIAppListAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppListAppStatus.setStatus("current")
_AlaDPIAppListMemberStatus_Type = RowStatus
_AlaDPIAppListMemberStatus_Object = MibTableColumn
alaDPIAppListMemberStatus = _AlaDPIAppListMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 6, 1, 5),
    _AlaDPIAppListMemberStatus_Type()
)
alaDPIAppListMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIAppListMemberStatus.setStatus("current")
_AlaDPIFlowTable_Object = MibTable
alaDPIFlowTable = _AlaDPIFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaDPIFlowTable.setStatus("current")
_AlaDPIFlowEntry_Object = MibTableRow
alaDPIFlowEntry = _AlaDPIFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1)
)
alaDPIFlowEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowSourceIPType"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowSourceIP"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowDestIPType"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowDestIP"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowSrcPort"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowDestPort"),
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIFlowProtocol"),
)
if mibBuilder.loadTexts:
    alaDPIFlowEntry.setStatus("current")


class _AlaDPIFlowSourceIPType_Type(InetAddressType):
    """Custom type alaDPIFlowSourceIPType based on InetAddressType"""
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


_AlaDPIFlowSourceIPType_Type.__name__ = "InetAddressType"
_AlaDPIFlowSourceIPType_Object = MibTableColumn
alaDPIFlowSourceIPType = _AlaDPIFlowSourceIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 1),
    _AlaDPIFlowSourceIPType_Type()
)
alaDPIFlowSourceIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowSourceIPType.setStatus("current")


class _AlaDPIFlowSourceIP_Type(InetAddress):
    """Custom type alaDPIFlowSourceIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDPIFlowSourceIP_Type.__name__ = "InetAddress"
_AlaDPIFlowSourceIP_Object = MibTableColumn
alaDPIFlowSourceIP = _AlaDPIFlowSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 2),
    _AlaDPIFlowSourceIP_Type()
)
alaDPIFlowSourceIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowSourceIP.setStatus("current")


class _AlaDPIFlowDestIPType_Type(InetAddressType):
    """Custom type alaDPIFlowDestIPType based on InetAddressType"""
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


_AlaDPIFlowDestIPType_Type.__name__ = "InetAddressType"
_AlaDPIFlowDestIPType_Object = MibTableColumn
alaDPIFlowDestIPType = _AlaDPIFlowDestIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 3),
    _AlaDPIFlowDestIPType_Type()
)
alaDPIFlowDestIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowDestIPType.setStatus("current")


class _AlaDPIFlowDestIP_Type(InetAddress):
    """Custom type alaDPIFlowDestIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDPIFlowDestIP_Type.__name__ = "InetAddress"
_AlaDPIFlowDestIP_Object = MibTableColumn
alaDPIFlowDestIP = _AlaDPIFlowDestIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 4),
    _AlaDPIFlowDestIP_Type()
)
alaDPIFlowDestIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowDestIP.setStatus("current")


class _AlaDPIFlowSrcPort_Type(Integer32):
    """Custom type alaDPIFlowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaDPIFlowSrcPort_Type.__name__ = "Integer32"
_AlaDPIFlowSrcPort_Object = MibTableColumn
alaDPIFlowSrcPort = _AlaDPIFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 5),
    _AlaDPIFlowSrcPort_Type()
)
alaDPIFlowSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowSrcPort.setStatus("current")


class _AlaDPIFlowDestPort_Type(Integer32):
    """Custom type alaDPIFlowDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaDPIFlowDestPort_Type.__name__ = "Integer32"
_AlaDPIFlowDestPort_Object = MibTableColumn
alaDPIFlowDestPort = _AlaDPIFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 6),
    _AlaDPIFlowDestPort_Type()
)
alaDPIFlowDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowDestPort.setStatus("current")


class _AlaDPIFlowProtocol_Type(Integer32):
    """Custom type alaDPIFlowProtocol based on Integer32"""
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


_AlaDPIFlowProtocol_Type.__name__ = "Integer32"
_AlaDPIFlowProtocol_Object = MibTableColumn
alaDPIFlowProtocol = _AlaDPIFlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 7),
    _AlaDPIFlowProtocol_Type()
)
alaDPIFlowProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIFlowProtocol.setStatus("current")


class _AlaDPIFlowAppName_Type(SnmpAdminString):
    """Custom type alaDPIFlowAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIFlowAppName_Type.__name__ = "SnmpAdminString"
_AlaDPIFlowAppName_Object = MibTableColumn
alaDPIFlowAppName = _AlaDPIFlowAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 8),
    _AlaDPIFlowAppName_Type()
)
alaDPIFlowAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIFlowAppName.setStatus("current")


class _AlaDPIFlowAppGrpName_Type(SnmpAdminString):
    """Custom type alaDPIFlowAppGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPIFlowAppGrpName_Type.__name__ = "SnmpAdminString"
_AlaDPIFlowAppGrpName_Object = MibTableColumn
alaDPIFlowAppGrpName = _AlaDPIFlowAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 9),
    _AlaDPIFlowAppGrpName_Type()
)
alaDPIFlowAppGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIFlowAppGrpName.setStatus("current")


class _AlaDPIFlowPolicyRule_Type(SnmpAdminString):
    """Custom type alaDPIFlowPolicyRule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPIFlowPolicyRule_Type.__name__ = "SnmpAdminString"
_AlaDPIFlowPolicyRule_Object = MibTableColumn
alaDPIFlowPolicyRule = _AlaDPIFlowPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 10),
    _AlaDPIFlowPolicyRule_Type()
)
alaDPIFlowPolicyRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIFlowPolicyRule.setStatus("current")
_AlaDPIFlowStartTime_Type = DateAndTime
_AlaDPIFlowStartTime_Object = MibTableColumn
alaDPIFlowStartTime = _AlaDPIFlowStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 11),
    _AlaDPIFlowStartTime_Type()
)
alaDPIFlowStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIFlowStartTime.setStatus("current")
_AlaDPIFlowPktCount_Type = Counter64
_AlaDPIFlowPktCount_Object = MibTableColumn
alaDPIFlowPktCount = _AlaDPIFlowPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 12),
    _AlaDPIFlowPktCount_Type()
)
alaDPIFlowPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIFlowPktCount.setStatus("current")
_AlaDPIFlowByteCount_Type = Counter64
_AlaDPIFlowByteCount_Object = MibTableColumn
alaDPIFlowByteCount = _AlaDPIFlowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 7, 1, 13),
    _AlaDPIFlowByteCount_Type()
)
alaDPIFlowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIFlowByteCount.setStatus("current")
_AlaDPIL4PortRangeTable_Object = MibTable
alaDPIL4PortRangeTable = _AlaDPIL4PortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaDPIL4PortRangeTable.setStatus("current")
_AlaDPIL4PortRangeEntry_Object = MibTableRow
alaDPIL4PortRangeEntry = _AlaDPIL4PortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8, 1)
)
alaDPIL4PortRangeEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIL4PortRangeId"),
)
if mibBuilder.loadTexts:
    alaDPIL4PortRangeEntry.setStatus("current")


class _AlaDPIL4PortRangeId_Type(Integer32):
    """Custom type alaDPIL4PortRangeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaDPIL4PortRangeId_Type.__name__ = "Integer32"
_AlaDPIL4PortRangeId_Object = MibTableColumn
alaDPIL4PortRangeId = _AlaDPIL4PortRangeId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8, 1, 1),
    _AlaDPIL4PortRangeId_Type()
)
alaDPIL4PortRangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIL4PortRangeId.setStatus("current")


class _AlaDPIL4PortRangeStart_Type(Integer32):
    """Custom type alaDPIL4PortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIL4PortRangeStart_Type.__name__ = "Integer32"
_AlaDPIL4PortRangeStart_Object = MibTableColumn
alaDPIL4PortRangeStart = _AlaDPIL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8, 1, 2),
    _AlaDPIL4PortRangeStart_Type()
)
alaDPIL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIL4PortRangeStart.setStatus("current")


class _AlaDPIL4PortRangeEnd_Type(Integer32):
    """Custom type alaDPIL4PortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDPIL4PortRangeEnd_Type.__name__ = "Integer32"
_AlaDPIL4PortRangeEnd_Object = MibTableColumn
alaDPIL4PortRangeEnd = _AlaDPIL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8, 1, 3),
    _AlaDPIL4PortRangeEnd_Type()
)
alaDPIL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIL4PortRangeEnd.setStatus("current")


class _AlaDPIL4PortType_Type(Integer32):
    """Custom type alaDPIL4PortType based on Integer32"""
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


_AlaDPIL4PortType_Type.__name__ = "Integer32"
_AlaDPIL4PortType_Object = MibTableColumn
alaDPIL4PortType = _AlaDPIL4PortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8, 1, 4),
    _AlaDPIL4PortType_Type()
)
alaDPIL4PortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIL4PortType.setStatus("current")
_AlaDPIL4PortStatus_Type = RowStatus
_AlaDPIL4PortStatus_Object = MibTableColumn
alaDPIL4PortStatus = _AlaDPIL4PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 8, 1, 5),
    _AlaDPIL4PortStatus_Type()
)
alaDPIL4PortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDPIL4PortStatus.setStatus("current")
_AlaDPIActiveAppListTable_Object = MibTable
alaDPIActiveAppListTable = _AlaDPIActiveAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaDPIActiveAppListTable.setStatus("current")
_AlaDPIActiveAppListEntry_Object = MibTableRow
alaDPIActiveAppListEntry = _AlaDPIActiveAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1)
)
alaDPIActiveAppListEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListAppName"),
)
if mibBuilder.loadTexts:
    alaDPIActiveAppListEntry.setStatus("current")


class _AlaDPIActiveAppListAppName_Type(SnmpAdminString):
    """Custom type alaDPIActiveAppListAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIActiveAppListAppName_Type.__name__ = "SnmpAdminString"
_AlaDPIActiveAppListAppName_Object = MibTableColumn
alaDPIActiveAppListAppName = _AlaDPIActiveAppListAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 1),
    _AlaDPIActiveAppListAppName_Type()
)
alaDPIActiveAppListAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIActiveAppListAppName.setStatus("current")


class _AlaDPIActiveAppListAppGroupName_Type(SnmpAdminString):
    """Custom type alaDPIActiveAppListAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDPIActiveAppListAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaDPIActiveAppListAppGroupName_Object = MibTableColumn
alaDPIActiveAppListAppGroupName = _AlaDPIActiveAppListAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 2),
    _AlaDPIActiveAppListAppGroupName_Type()
)
alaDPIActiveAppListAppGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListAppGroupName.setStatus("current")
_AlaDPIActiveAppListActiveMatchedFlows_Type = Integer32
_AlaDPIActiveAppListActiveMatchedFlows_Object = MibTableColumn
alaDPIActiveAppListActiveMatchedFlows = _AlaDPIActiveAppListActiveMatchedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 3),
    _AlaDPIActiveAppListActiveMatchedFlows_Type()
)
alaDPIActiveAppListActiveMatchedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListActiveMatchedFlows.setStatus("current")
_AlaDPIActiveAppListTotalMatchedFlows_Type = Integer32
_AlaDPIActiveAppListTotalMatchedFlows_Object = MibTableColumn
alaDPIActiveAppListTotalMatchedFlows = _AlaDPIActiveAppListTotalMatchedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 4),
    _AlaDPIActiveAppListTotalMatchedFlows_Type()
)
alaDPIActiveAppListTotalMatchedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListTotalMatchedFlows.setStatus("current")
_AlaDPIActiveAppListAppID_Type = Integer32
_AlaDPIActiveAppListAppID_Object = MibTableColumn
alaDPIActiveAppListAppID = _AlaDPIActiveAppListAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 5),
    _AlaDPIActiveAppListAppID_Type()
)
alaDPIActiveAppListAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListAppID.setStatus("current")


class _AlaDPIActiveAppListAppStatus_Type(Integer32):
    """Custom type alaDPIActiveAppListAppStatus based on Integer32"""
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


_AlaDPIActiveAppListAppStatus_Type.__name__ = "Integer32"
_AlaDPIActiveAppListAppStatus_Object = MibTableColumn
alaDPIActiveAppListAppStatus = _AlaDPIActiveAppListAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 6),
    _AlaDPIActiveAppListAppStatus_Type()
)
alaDPIActiveAppListAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListAppStatus.setStatus("current")
_AlaDPIActiveAppListActivePktCount_Type = Counter64
_AlaDPIActiveAppListActivePktCount_Object = MibTableColumn
alaDPIActiveAppListActivePktCount = _AlaDPIActiveAppListActivePktCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 7),
    _AlaDPIActiveAppListActivePktCount_Type()
)
alaDPIActiveAppListActivePktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListActivePktCount.setStatus("current")
_AlaDPIActiveAppListActiveByteCount_Type = Counter64
_AlaDPIActiveAppListActiveByteCount_Object = MibTableColumn
alaDPIActiveAppListActiveByteCount = _AlaDPIActiveAppListActiveByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 8),
    _AlaDPIActiveAppListActiveByteCount_Type()
)
alaDPIActiveAppListActiveByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListActiveByteCount.setStatus("current")
_AlaDPIActiveAppListGrossPktCount_Type = Counter64
_AlaDPIActiveAppListGrossPktCount_Object = MibTableColumn
alaDPIActiveAppListGrossPktCount = _AlaDPIActiveAppListGrossPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 9),
    _AlaDPIActiveAppListGrossPktCount_Type()
)
alaDPIActiveAppListGrossPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListGrossPktCount.setStatus("current")
_AlaDPIActiveAppListGrossByteCount_Type = Counter64
_AlaDPIActiveAppListGrossByteCount_Object = MibTableColumn
alaDPIActiveAppListGrossByteCount = _AlaDPIActiveAppListGrossByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 9, 1, 10),
    _AlaDPIActiveAppListGrossByteCount_Type()
)
alaDPIActiveAppListGrossByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIActiveAppListGrossByteCount.setStatus("current")
_AlaDPISignatureFileTable_Object = MibTable
alaDPISignatureFileTable = _AlaDPISignatureFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaDPISignatureFileTable.setStatus("current")
_AlaDPISignatureFileEntry_Object = MibTableRow
alaDPISignatureFileEntry = _AlaDPISignatureFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 10, 1)
)
alaDPISignatureFileEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPISignatureFileAppName"),
)
if mibBuilder.loadTexts:
    alaDPISignatureFileEntry.setStatus("current")


class _AlaDPISignatureFileAppName_Type(SnmpAdminString):
    """Custom type alaDPISignatureFileAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPISignatureFileAppName_Type.__name__ = "SnmpAdminString"
_AlaDPISignatureFileAppName_Object = MibTableColumn
alaDPISignatureFileAppName = _AlaDPISignatureFileAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 10, 1, 1),
    _AlaDPISignatureFileAppName_Type()
)
alaDPISignatureFileAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPISignatureFileAppName.setStatus("current")


class _AlaDPISignatureFileCategory_Type(SnmpAdminString):
    """Custom type alaDPISignatureFileCategory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDPISignatureFileCategory_Type.__name__ = "SnmpAdminString"
_AlaDPISignatureFileCategory_Object = MibTableColumn
alaDPISignatureFileCategory = _AlaDPISignatureFileCategory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 10, 1, 2),
    _AlaDPISignatureFileCategory_Type()
)
alaDPISignatureFileCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPISignatureFileCategory.setStatus("current")
_AlaDPIStatisticsTable_Object = MibTable
alaDPIStatisticsTable = _AlaDPIStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaDPIStatisticsTable.setStatus("current")
_AlaDPIStatisticsEntry_Object = MibTableRow
alaDPIStatisticsEntry = _AlaDPIStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 11, 1)
)
alaDPIStatisticsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIStatsSlotIndex"),
)
if mibBuilder.loadTexts:
    alaDPIStatisticsEntry.setStatus("current")
_AlaDPIStatsSlotIndex_Type = InterfaceIndex
_AlaDPIStatsSlotIndex_Object = MibTableColumn
alaDPIStatsSlotIndex = _AlaDPIStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 11, 1, 1),
    _AlaDPIStatsSlotIndex_Type()
)
alaDPIStatsSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIStatsSlotIndex.setStatus("current")
_AlaDPITotalMatchedFlows_Type = Counter32
_AlaDPITotalMatchedFlows_Object = MibTableColumn
alaDPITotalMatchedFlows = _AlaDPITotalMatchedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 11, 1, 2),
    _AlaDPITotalMatchedFlows_Type()
)
alaDPITotalMatchedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPITotalMatchedFlows.setStatus("current")
_AlaDPITotalUnmatchedFlows_Type = Counter32
_AlaDPITotalUnmatchedFlows_Object = MibTableColumn
alaDPITotalUnmatchedFlows = _AlaDPITotalUnmatchedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 11, 1, 3),
    _AlaDPITotalUnmatchedFlows_Type()
)
alaDPITotalUnmatchedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPITotalUnmatchedFlows.setStatus("current")
_AlaDPITotalMissedFlows_Type = Counter64
_AlaDPITotalMissedFlows_Object = MibTableColumn
alaDPITotalMissedFlows = _AlaDPITotalMissedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 11, 1, 4),
    _AlaDPITotalMissedFlows_Type()
)
alaDPITotalMissedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPITotalMissedFlows.setStatus("current")
_AlaDPIAppListConflictTable_Object = MibTable
alaDPIAppListConflictTable = _AlaDPIAppListConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaDPIAppListConflictTable.setStatus("current")
_AlaDPIAppListConflictEntry_Object = MibTableRow
alaDPIAppListConflictEntry = _AlaDPIAppListConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12, 1)
)
alaDPIAppListConflictEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIAppListConflictIndex"),
)
if mibBuilder.loadTexts:
    alaDPIAppListConflictEntry.setStatus("current")
_AlaDPIAppListConflictIndex_Type = Unsigned32
_AlaDPIAppListConflictIndex_Object = MibTableColumn
alaDPIAppListConflictIndex = _AlaDPIAppListConflictIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12, 1, 1),
    _AlaDPIAppListConflictIndex_Type()
)
alaDPIAppListConflictIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIAppListConflictIndex.setStatus("current")
_AlaDPIAppListConflictAppID_Type = Integer32
_AlaDPIAppListConflictAppID_Object = MibTableColumn
alaDPIAppListConflictAppID = _AlaDPIAppListConflictAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12, 1, 2),
    _AlaDPIAppListConflictAppID_Type()
)
alaDPIAppListConflictAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppListConflictAppID.setStatus("current")
_AlaDPIAppListConflictAppName_Type = SnmpAdminString
_AlaDPIAppListConflictAppName_Object = MibTableColumn
alaDPIAppListConflictAppName = _AlaDPIAppListConflictAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12, 1, 3),
    _AlaDPIAppListConflictAppName_Type()
)
alaDPIAppListConflictAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppListConflictAppName.setStatus("current")
_AlaDPIAppListConflictAppGrpName_Type = SnmpAdminString
_AlaDPIAppListConflictAppGrpName_Object = MibTableColumn
alaDPIAppListConflictAppGrpName = _AlaDPIAppListConflictAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12, 1, 4),
    _AlaDPIAppListConflictAppGrpName_Type()
)
alaDPIAppListConflictAppGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppListConflictAppGrpName.setStatus("current")


class _AlaDPIAppListConflictAppErrorType_Type(Integer32):
    """Custom type alaDPIAppListConflictAppErrorType based on Integer32"""
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


_AlaDPIAppListConflictAppErrorType_Type.__name__ = "Integer32"
_AlaDPIAppListConflictAppErrorType_Object = MibTableColumn
alaDPIAppListConflictAppErrorType = _AlaDPIAppListConflictAppErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 12, 1, 5),
    _AlaDPIAppListConflictAppErrorType_Type()
)
alaDPIAppListConflictAppErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDPIAppListConflictAppErrorType.setStatus("current")
_AlaDPINotificationObjects_ObjectIdentity = ObjectIdentity
alaDPINotificationObjects = _AlaDPINotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 13)
)
_AlaDPIAgingTimerTable_Object = MibTable
alaDPIAgingTimerTable = _AlaDPIAgingTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaDPIAgingTimerTable.setStatus("current")
_AlaDPIAgingTimerEntry_Object = MibTableRow
alaDPIAgingTimerEntry = _AlaDPIAgingTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 14, 1)
)
alaDPIAgingTimerEntry.setIndexNames(
    (0, "ALCATEL-ENT1-DPI-MIB", "alaDPIAgingTimerAppName"),
)
if mibBuilder.loadTexts:
    alaDPIAgingTimerEntry.setStatus("current")


class _AlaDPIAgingTimerAppName_Type(SnmpAdminString):
    """Custom type alaDPIAgingTimerAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDPIAgingTimerAppName_Type.__name__ = "SnmpAdminString"
_AlaDPIAgingTimerAppName_Object = MibTableColumn
alaDPIAgingTimerAppName = _AlaDPIAgingTimerAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 14, 1, 1),
    _AlaDPIAgingTimerAppName_Type()
)
alaDPIAgingTimerAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDPIAgingTimerAppName.setStatus("current")


class _AlaDPIAgingTimerValue_Type(Integer32):
    """Custom type alaDPIAgingTimerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(120, 120),
    )


_AlaDPIAgingTimerValue_Type.__name__ = "Integer32"
_AlaDPIAgingTimerValue_Object = MibTableColumn
alaDPIAgingTimerValue = _AlaDPIAgingTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 1, 14, 1, 2),
    _AlaDPIAgingTimerValue_Type()
)
alaDPIAgingTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDPIAgingTimerValue.setStatus("current")
_AlaDPIMIBConformance_ObjectIdentity = ObjectIdentity
alaDPIMIBConformance = _AlaDPIMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2)
)
if mibBuilder.loadTexts:
    alaDPIMIBConformance.setStatus("current")
_AlaDPIMIBGroups_ObjectIdentity = ObjectIdentity
alaDPIMIBGroups = _AlaDPIMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaDPIMIBGroups.setStatus("current")
_AlaDPIMIBCompliances_ObjectIdentity = ObjectIdentity
alaDPIMIBCompliances = _AlaDPIMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaDPIMIBCompliances.setStatus("current")

# Managed Objects groups

alaDPIPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 1)
)
alaDPIPortConfigGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigPortStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigTcpStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigUdpStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigPortTypeStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigOperStatus"))
)
if mibBuilder.loadTexts:
    alaDPIPortConfigGroup.setStatus("current")

alaDPIAppPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 2)
)
alaDPIAppPoolGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIAppPoolCategory"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppPoolRevision"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppPoolAppID"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppPoolAppStatus"))
)
if mibBuilder.loadTexts:
    alaDPIAppPoolGroup.setStatus("current")

alaDPIAppGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 3)
)
alaDPIAppGroupsGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupMemberType"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupCategoryName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupID"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupAppStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupStatus"))
)
if mibBuilder.loadTexts:
    alaDPIAppGroupsGroup.setStatus("current")

alaDPIAppListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 4)
)
alaDPIAppListGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListMemberType"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListAppOrGroupID"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListAppStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListMemberStatus"))
)
if mibBuilder.loadTexts:
    alaDPIAppListGroup.setStatus("current")

alaDPIFlowTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 5)
)
alaDPIFlowTableGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowAppName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowAppGrpName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowPolicyRule"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowStartTime"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowPktCount"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowByteCount"))
)
if mibBuilder.loadTexts:
    alaDPIFlowTableGroup.setStatus("current")

alaDPIRangeDetailsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 6)
)
alaDPIRangeDetailsGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIL4PortRangeStart"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIL4PortRangeEnd"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIL4PortType"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIL4PortStatus"))
)
if mibBuilder.loadTexts:
    alaDPIRangeDetailsGroup.setStatus("current")

alaDPIConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 7)
)
alaDPIConfigGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIAdminStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIUpdateAppList"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIUpdateAppListStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIClearAppList"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowTableFlush"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIStatsInterval"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIClearStats"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIIpv4"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIIpv6"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppliedSignatures"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIApplicationPoolSignatures"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPISignatureFileVersion"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPISignatureFileName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPISignatureFileAppCount"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGrpFromAppName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGrpToAppName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAddAppGrpName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAutoGroupCreation"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAddRemoveAppGrpName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAOSCompatibilityVersion"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIKitType"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIUpgradedKitType"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIUpgradedSignatureFileVersion"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPILoggingThresholdFlows"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIClearConfig"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerDefaultPort1"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerDefaultPort2"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort1"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort2"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort3"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort4"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort5"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort6"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort7"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIProxyServerPort8"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAddRemoveProxyServerPort"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowTableStatsAdminStatus"))
)
if mibBuilder.loadTexts:
    alaDPIConfigGroup.setStatus("current")

alaDPIActiveListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 8)
)
alaDPIActiveListGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListAppGroupName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListActiveMatchedFlows"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListTotalMatchedFlows"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListAppID"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListAppStatus"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListActivePktCount"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListActiveByteCount"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListGrossPktCount"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveAppListGrossByteCount"))
)
if mibBuilder.loadTexts:
    alaDPIActiveListGroup.setStatus("current")

alaDPISignatureFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 9)
)
alaDPISignatureFileGroup.setObjects(
    ("ALCATEL-ENT1-DPI-MIB", "alaDPISignatureFileCategory")
)
if mibBuilder.loadTexts:
    alaDPISignatureFileGroup.setStatus("current")

alaDPIStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 10)
)
alaDPIStatisticsGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPITotalMatchedFlows"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPITotalUnmatchedFlows"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPITotalMissedFlows"))
)
if mibBuilder.loadTexts:
    alaDPIStatisticsGroup.setStatus("current")

alaDPIAppListConflictGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 11)
)
alaDPIAppListConflictGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListConflictAppID"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListConflictAppName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListConflictAppGrpName"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListConflictAppErrorType"))
)
if mibBuilder.loadTexts:
    alaDPIAppListConflictGroup.setStatus("current")

alaDPIAgingTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 13)
)
alaDPIAgingTimerGroup.setObjects(
    ("ALCATEL-ENT1-DPI-MIB", "alaDPIAgingTimerValue")
)
if mibBuilder.loadTexts:
    alaDPIAgingTimerGroup.setStatus("current")

alaDPICertConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 14)
)
alaDPICertConfigGroup.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIUpdateSignatureFile"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIUpdateSignatureStatus"))
)
if mibBuilder.loadTexts:
    alaDPICertConfigGroup.setStatus("current")


# Notification objects

alaDPIFlowRecordFileCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 0, 1)
)
if mibBuilder.loadTexts:
    alaDPIFlowRecordFileCreated.setStatus(
        "current"
    )


# Notifications groups

alaDPINotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 1, 12)
)
alaDPINotificationGroup.setObjects(
    ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowRecordFileCreated")
)
if mibBuilder.loadTexts:
    alaDPINotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaDPIMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78, 1, 2, 2, 1)
)
alaDPIMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-DPI-MIB", "alaDPIPortConfigGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppPoolGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppGroupsGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIFlowTableGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIConfigGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIRangeDetailsGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIActiveListGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPISignatureFileGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIStatisticsGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAppListConflictGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPINotificationGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPIAgingTimerGroup"),
        ("ALCATEL-ENT1-DPI-MIB", "alaDPICertConfigGroup"))
)
if mibBuilder.loadTexts:
    alaDPIMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-DPI-MIB",
    **{"alaDPIMIB": alaDPIMIB,
       "alaDPIMIBNotifications": alaDPIMIBNotifications,
       "alaDPIFlowRecordFileCreated": alaDPIFlowRecordFileCreated,
       "alaDPIMIBObjects": alaDPIMIBObjects,
       "alaDPICertConfig": alaDPICertConfig,
       "alaDPIUpdateSignatureFile": alaDPIUpdateSignatureFile,
       "alaDPIUpdateSignatureStatus": alaDPIUpdateSignatureStatus,
       "alaDPIConfig": alaDPIConfig,
       "alaDPIAdminStatus": alaDPIAdminStatus,
       "alaDPIUpdateAppList": alaDPIUpdateAppList,
       "alaDPIUpdateAppListStatus": alaDPIUpdateAppListStatus,
       "alaDPIClearAppList": alaDPIClearAppList,
       "alaDPIFlowTableFlush": alaDPIFlowTableFlush,
       "alaDPIStatsInterval": alaDPIStatsInterval,
       "alaDPIClearStats": alaDPIClearStats,
       "alaDPIIpv4": alaDPIIpv4,
       "alaDPIIpv6": alaDPIIpv6,
       "alaDPIAppliedSignatures": alaDPIAppliedSignatures,
       "alaDPIApplicationPoolSignatures": alaDPIApplicationPoolSignatures,
       "alaDPISignatureFileVersion": alaDPISignatureFileVersion,
       "alaDPISignatureFileAppCount": alaDPISignatureFileAppCount,
       "alaDPISignatureFileName": alaDPISignatureFileName,
       "alaDPIAppGrpFromAppName": alaDPIAppGrpFromAppName,
       "alaDPIAppGrpToAppName": alaDPIAppGrpToAppName,
       "alaDPIAddAppGrpName": alaDPIAddAppGrpName,
       "alaDPIAutoGroupCreation": alaDPIAutoGroupCreation,
       "alaDPIAddRemoveAppGrpName": alaDPIAddRemoveAppGrpName,
       "alaDPIAOSCompatibilityVersion": alaDPIAOSCompatibilityVersion,
       "alaDPIKitType": alaDPIKitType,
       "alaDPIUpgradedKitType": alaDPIUpgradedKitType,
       "alaDPIUpgradedSignatureFileVersion": alaDPIUpgradedSignatureFileVersion,
       "alaDPILoggingThresholdFlows": alaDPILoggingThresholdFlows,
       "alaDPIClearConfig": alaDPIClearConfig,
       "alaDPIProxyServerDefaultPort1": alaDPIProxyServerDefaultPort1,
       "alaDPIProxyServerDefaultPort2": alaDPIProxyServerDefaultPort2,
       "alaDPIProxyServerPort1": alaDPIProxyServerPort1,
       "alaDPIProxyServerPort2": alaDPIProxyServerPort2,
       "alaDPIProxyServerPort3": alaDPIProxyServerPort3,
       "alaDPIProxyServerPort4": alaDPIProxyServerPort4,
       "alaDPIProxyServerPort5": alaDPIProxyServerPort5,
       "alaDPIProxyServerPort6": alaDPIProxyServerPort6,
       "alaDPIProxyServerPort7": alaDPIProxyServerPort7,
       "alaDPIProxyServerPort8": alaDPIProxyServerPort8,
       "alaDPIAddRemoveProxyServerPort": alaDPIAddRemoveProxyServerPort,
       "alaDPIFlowTableStatsAdminStatus": alaDPIFlowTableStatsAdminStatus,
       "alaDPIPortConfigTable": alaDPIPortConfigTable,
       "alaDPIPortConfigEntry": alaDPIPortConfigEntry,
       "alaDPIPortConfigSlotPortIndex": alaDPIPortConfigSlotPortIndex,
       "alaDPIPortConfigPortStatus": alaDPIPortConfigPortStatus,
       "alaDPIPortConfigTcpStatus": alaDPIPortConfigTcpStatus,
       "alaDPIPortConfigUdpStatus": alaDPIPortConfigUdpStatus,
       "alaDPIPortConfigPortTypeStatus": alaDPIPortConfigPortTypeStatus,
       "alaDPIPortConfigOperStatus": alaDPIPortConfigOperStatus,
       "alaDPIAppPoolTable": alaDPIAppPoolTable,
       "alaDPIAppPoolEntry": alaDPIAppPoolEntry,
       "alaDPIAppPoolAppName": alaDPIAppPoolAppName,
       "alaDPIAppPoolCategory": alaDPIAppPoolCategory,
       "alaDPIAppPoolRevision": alaDPIAppPoolRevision,
       "alaDPIAppPoolAppID": alaDPIAppPoolAppID,
       "alaDPIAppPoolAppStatus": alaDPIAppPoolAppStatus,
       "alaDPIAppGroupTable": alaDPIAppGroupTable,
       "alaDPIAppGroupEntry": alaDPIAppGroupEntry,
       "alaDPIAppGroupName": alaDPIAppGroupName,
       "alaDPIAppGroupMember": alaDPIAppGroupMember,
       "alaDPIAppGroupMemberType": alaDPIAppGroupMemberType,
       "alaDPIAppGroupCategoryName": alaDPIAppGroupCategoryName,
       "alaDPIAppGroupID": alaDPIAppGroupID,
       "alaDPIAppGroupAppStatus": alaDPIAppGroupAppStatus,
       "alaDPIAppGroupStatus": alaDPIAppGroupStatus,
       "alaDPIAppListTable": alaDPIAppListTable,
       "alaDPIAppListEntry": alaDPIAppListEntry,
       "alaDPIAppListMemberName": alaDPIAppListMemberName,
       "alaDPIAppListMemberType": alaDPIAppListMemberType,
       "alaDPIAppListAppOrGroupID": alaDPIAppListAppOrGroupID,
       "alaDPIAppListAppStatus": alaDPIAppListAppStatus,
       "alaDPIAppListMemberStatus": alaDPIAppListMemberStatus,
       "alaDPIFlowTable": alaDPIFlowTable,
       "alaDPIFlowEntry": alaDPIFlowEntry,
       "alaDPIFlowSourceIPType": alaDPIFlowSourceIPType,
       "alaDPIFlowSourceIP": alaDPIFlowSourceIP,
       "alaDPIFlowDestIPType": alaDPIFlowDestIPType,
       "alaDPIFlowDestIP": alaDPIFlowDestIP,
       "alaDPIFlowSrcPort": alaDPIFlowSrcPort,
       "alaDPIFlowDestPort": alaDPIFlowDestPort,
       "alaDPIFlowProtocol": alaDPIFlowProtocol,
       "alaDPIFlowAppName": alaDPIFlowAppName,
       "alaDPIFlowAppGrpName": alaDPIFlowAppGrpName,
       "alaDPIFlowPolicyRule": alaDPIFlowPolicyRule,
       "alaDPIFlowStartTime": alaDPIFlowStartTime,
       "alaDPIFlowPktCount": alaDPIFlowPktCount,
       "alaDPIFlowByteCount": alaDPIFlowByteCount,
       "alaDPIL4PortRangeTable": alaDPIL4PortRangeTable,
       "alaDPIL4PortRangeEntry": alaDPIL4PortRangeEntry,
       "alaDPIL4PortRangeId": alaDPIL4PortRangeId,
       "alaDPIL4PortRangeStart": alaDPIL4PortRangeStart,
       "alaDPIL4PortRangeEnd": alaDPIL4PortRangeEnd,
       "alaDPIL4PortType": alaDPIL4PortType,
       "alaDPIL4PortStatus": alaDPIL4PortStatus,
       "alaDPIActiveAppListTable": alaDPIActiveAppListTable,
       "alaDPIActiveAppListEntry": alaDPIActiveAppListEntry,
       "alaDPIActiveAppListAppName": alaDPIActiveAppListAppName,
       "alaDPIActiveAppListAppGroupName": alaDPIActiveAppListAppGroupName,
       "alaDPIActiveAppListActiveMatchedFlows": alaDPIActiveAppListActiveMatchedFlows,
       "alaDPIActiveAppListTotalMatchedFlows": alaDPIActiveAppListTotalMatchedFlows,
       "alaDPIActiveAppListAppID": alaDPIActiveAppListAppID,
       "alaDPIActiveAppListAppStatus": alaDPIActiveAppListAppStatus,
       "alaDPIActiveAppListActivePktCount": alaDPIActiveAppListActivePktCount,
       "alaDPIActiveAppListActiveByteCount": alaDPIActiveAppListActiveByteCount,
       "alaDPIActiveAppListGrossPktCount": alaDPIActiveAppListGrossPktCount,
       "alaDPIActiveAppListGrossByteCount": alaDPIActiveAppListGrossByteCount,
       "alaDPISignatureFileTable": alaDPISignatureFileTable,
       "alaDPISignatureFileEntry": alaDPISignatureFileEntry,
       "alaDPISignatureFileAppName": alaDPISignatureFileAppName,
       "alaDPISignatureFileCategory": alaDPISignatureFileCategory,
       "alaDPIStatisticsTable": alaDPIStatisticsTable,
       "alaDPIStatisticsEntry": alaDPIStatisticsEntry,
       "alaDPIStatsSlotIndex": alaDPIStatsSlotIndex,
       "alaDPITotalMatchedFlows": alaDPITotalMatchedFlows,
       "alaDPITotalUnmatchedFlows": alaDPITotalUnmatchedFlows,
       "alaDPITotalMissedFlows": alaDPITotalMissedFlows,
       "alaDPIAppListConflictTable": alaDPIAppListConflictTable,
       "alaDPIAppListConflictEntry": alaDPIAppListConflictEntry,
       "alaDPIAppListConflictIndex": alaDPIAppListConflictIndex,
       "alaDPIAppListConflictAppID": alaDPIAppListConflictAppID,
       "alaDPIAppListConflictAppName": alaDPIAppListConflictAppName,
       "alaDPIAppListConflictAppGrpName": alaDPIAppListConflictAppGrpName,
       "alaDPIAppListConflictAppErrorType": alaDPIAppListConflictAppErrorType,
       "alaDPINotificationObjects": alaDPINotificationObjects,
       "alaDPIAgingTimerTable": alaDPIAgingTimerTable,
       "alaDPIAgingTimerEntry": alaDPIAgingTimerEntry,
       "alaDPIAgingTimerAppName": alaDPIAgingTimerAppName,
       "alaDPIAgingTimerValue": alaDPIAgingTimerValue,
       "alaDPIMIBConformance": alaDPIMIBConformance,
       "alaDPIMIBGroups": alaDPIMIBGroups,
       "alaDPIPortConfigGroup": alaDPIPortConfigGroup,
       "alaDPIAppPoolGroup": alaDPIAppPoolGroup,
       "alaDPIAppGroupsGroup": alaDPIAppGroupsGroup,
       "alaDPIAppListGroup": alaDPIAppListGroup,
       "alaDPIFlowTableGroup": alaDPIFlowTableGroup,
       "alaDPIRangeDetailsGroup": alaDPIRangeDetailsGroup,
       "alaDPIConfigGroup": alaDPIConfigGroup,
       "alaDPIActiveListGroup": alaDPIActiveListGroup,
       "alaDPISignatureFileGroup": alaDPISignatureFileGroup,
       "alaDPIStatisticsGroup": alaDPIStatisticsGroup,
       "alaDPIAppListConflictGroup": alaDPIAppListConflictGroup,
       "alaDPINotificationGroup": alaDPINotificationGroup,
       "alaDPIAgingTimerGroup": alaDPIAgingTimerGroup,
       "alaDPICertConfigGroup": alaDPICertConfigGroup,
       "alaDPIMIBCompliances": alaDPIMIBCompliances,
       "alaDPIMIBCompliance": alaDPIMIBCompliance}
)
