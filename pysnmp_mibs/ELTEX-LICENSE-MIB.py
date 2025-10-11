# SNMP MIB module (ELTEX-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-LICENSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:47 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49)
)
if mibBuilder.loadTexts:
    eltexLicenseMIB.setRevisions(
        ("2018-07-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexLicenseStatus(TextualConvention, Integer32):
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
        *(("active", 1),
          ("activeAfterReboot", 2),
          ("inactiveAfterReboot", 3),
          ("deviceMismatching", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltexLicenseMIBObjects_ObjectIdentity = ObjectIdentity
eltexLicenseMIBObjects = _EltexLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1)
)
_EltexLicenseGeneral_ObjectIdentity = ObjectIdentity
eltexLicenseGeneral = _EltexLicenseGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 1)
)
_EltexLicenseInformation_ObjectIdentity = ObjectIdentity
eltexLicenseInformation = _EltexLicenseInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2)
)
_EltexLicenseInfoTable_Object = MibTable
eltexLicenseInfoTable = _EltexLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexLicenseInfoTable.setStatus("current")
_EltexLicenseInfoEntry_Object = MibTableRow
eltexLicenseInfoEntry = _EltexLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1)
)
eltexLicenseInfoEntry.setIndexNames(
    (0, "ELTEX-LICENSE-MIB", "eltexLicenseInfoId"),
)
if mibBuilder.loadTexts:
    eltexLicenseInfoEntry.setStatus("current")
_EltexLicenseInfoId_Type = Unsigned32
_EltexLicenseInfoId_Object = MibTableColumn
eltexLicenseInfoId = _EltexLicenseInfoId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 1),
    _EltexLicenseInfoId_Type()
)
eltexLicenseInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexLicenseInfoId.setStatus("current")
_EltexLicenseInfoFileName_Type = DisplayString
_EltexLicenseInfoFileName_Object = MibTableColumn
eltexLicenseInfoFileName = _EltexLicenseInfoFileName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 2),
    _EltexLicenseInfoFileName_Type()
)
eltexLicenseInfoFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoFileName.setStatus("current")
_EltexLicenseInfoVersion_Type = Unsigned32
_EltexLicenseInfoVersion_Object = MibTableColumn
eltexLicenseInfoVersion = _EltexLicenseInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 3),
    _EltexLicenseInfoVersion_Type()
)
eltexLicenseInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoVersion.setStatus("current")
_EltexLicenseInfoStatus_Type = EltexLicenseStatus
_EltexLicenseInfoStatus_Object = MibTableColumn
eltexLicenseInfoStatus = _EltexLicenseInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 4),
    _EltexLicenseInfoStatus_Type()
)
eltexLicenseInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoStatus.setStatus("current")
_EltexLicenseInfoSerialNumber_Type = DisplayString
_EltexLicenseInfoSerialNumber_Object = MibTableColumn
eltexLicenseInfoSerialNumber = _EltexLicenseInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 5),
    _EltexLicenseInfoSerialNumber_Type()
)
eltexLicenseInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoSerialNumber.setStatus("current")
_EltexLicenseInfoMacAddress_Type = MacAddress
_EltexLicenseInfoMacAddress_Object = MibTableColumn
eltexLicenseInfoMacAddress = _EltexLicenseInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 6),
    _EltexLicenseInfoMacAddress_Type()
)
eltexLicenseInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoMacAddress.setStatus("current")
_EltexLicenseInfoVendorName_Type = DisplayString
_EltexLicenseInfoVendorName_Object = MibTableColumn
eltexLicenseInfoVendorName = _EltexLicenseInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 7),
    _EltexLicenseInfoVendorName_Type()
)
eltexLicenseInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoVendorName.setStatus("current")
_EltexLicenseInfoDeviceName_Type = DisplayString
_EltexLicenseInfoDeviceName_Object = MibTableColumn
eltexLicenseInfoDeviceName = _EltexLicenseInfoDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 2, 1, 1, 8),
    _EltexLicenseInfoDeviceName_Type()
)
eltexLicenseInfoDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseInfoDeviceName.setStatus("current")
_EltexLicenseFeature_ObjectIdentity = ObjectIdentity
eltexLicenseFeature = _EltexLicenseFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3)
)
_EltexLicenseFeatureTable_Object = MibTable
eltexLicenseFeatureTable = _EltexLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexLicenseFeatureTable.setStatus("current")
_EltexLicenseFeatureEntry_Object = MibTableRow
eltexLicenseFeatureEntry = _EltexLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1, 1)
)
eltexLicenseFeatureEntry.setIndexNames(
    (0, "ELTEX-LICENSE-MIB", "eltexLicenseFeatureName"),
)
if mibBuilder.loadTexts:
    eltexLicenseFeatureEntry.setStatus("current")
_EltexLicenseFeatureName_Type = DisplayString
_EltexLicenseFeatureName_Object = MibTableColumn
eltexLicenseFeatureName = _EltexLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1, 1, 1),
    _EltexLicenseFeatureName_Type()
)
eltexLicenseFeatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexLicenseFeatureName.setStatus("current")
_EltexLicenseFeatureActive_Type = TruthValue
_EltexLicenseFeatureActive_Object = MibTableColumn
eltexLicenseFeatureActive = _EltexLicenseFeatureActive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1, 1, 2),
    _EltexLicenseFeatureActive_Type()
)
eltexLicenseFeatureActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseFeatureActive.setStatus("current")
_EltexLicenseFeatureCountable_Type = TruthValue
_EltexLicenseFeatureCountable_Object = MibTableColumn
eltexLicenseFeatureCountable = _EltexLicenseFeatureCountable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1, 1, 3),
    _EltexLicenseFeatureCountable_Type()
)
eltexLicenseFeatureCountable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseFeatureCountable.setStatus("current")
_EltexLicenseFeatureLicensesInstalled_Type = Unsigned32
_EltexLicenseFeatureLicensesInstalled_Object = MibTableColumn
eltexLicenseFeatureLicensesInstalled = _EltexLicenseFeatureLicensesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1, 1, 4),
    _EltexLicenseFeatureLicensesInstalled_Type()
)
eltexLicenseFeatureLicensesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseFeatureLicensesInstalled.setStatus("current")
_EltexLicenseFeatureLicensesUsed_Type = Unsigned32
_EltexLicenseFeatureLicensesUsed_Object = MibTableColumn
eltexLicenseFeatureLicensesUsed = _EltexLicenseFeatureLicensesUsed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 1, 1, 5),
    _EltexLicenseFeatureLicensesUsed_Type()
)
eltexLicenseFeatureLicensesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseFeatureLicensesUsed.setStatus("current")
_EltexLicenseFeatureListTable_Object = MibTable
eltexLicenseFeatureListTable = _EltexLicenseFeatureListTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexLicenseFeatureListTable.setStatus("current")
_EltexLicenseFeatureListEntry_Object = MibTableRow
eltexLicenseFeatureListEntry = _EltexLicenseFeatureListEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 2, 1)
)
eltexLicenseFeatureListEntry.setIndexNames(
    (0, "ELTEX-LICENSE-MIB", "eltexLicenseInfoId"),
    (0, "ELTEX-LICENSE-MIB", "eltexLicenseFeatureName"),
)
if mibBuilder.loadTexts:
    eltexLicenseFeatureListEntry.setStatus("current")
_EltexLicenseFeatureListCount_Type = Unsigned32
_EltexLicenseFeatureListCount_Object = MibTableColumn
eltexLicenseFeatureListCount = _EltexLicenseFeatureListCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 49, 1, 3, 2, 1, 1),
    _EltexLicenseFeatureListCount_Type()
)
eltexLicenseFeatureListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLicenseFeatureListCount.setStatus("current")
_EltexLicenseMIBNotifications_ObjectIdentity = ObjectIdentity
eltexLicenseMIBNotifications = _EltexLicenseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 2)
)
_EltexLicenseMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltexLicenseMIBNotificationsPrefix = _EltexLicenseMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 2, 0)
)
_EltexLicenseMIBConformance_ObjectIdentity = ObjectIdentity
eltexLicenseMIBConformance = _EltexLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 49, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-LICENSE-MIB",
    **{"EltexLicenseStatus": EltexLicenseStatus,
       "eltexLicenseMIB": eltexLicenseMIB,
       "eltexLicenseMIBObjects": eltexLicenseMIBObjects,
       "eltexLicenseGeneral": eltexLicenseGeneral,
       "eltexLicenseInformation": eltexLicenseInformation,
       "eltexLicenseInfoTable": eltexLicenseInfoTable,
       "eltexLicenseInfoEntry": eltexLicenseInfoEntry,
       "eltexLicenseInfoId": eltexLicenseInfoId,
       "eltexLicenseInfoFileName": eltexLicenseInfoFileName,
       "eltexLicenseInfoVersion": eltexLicenseInfoVersion,
       "eltexLicenseInfoStatus": eltexLicenseInfoStatus,
       "eltexLicenseInfoSerialNumber": eltexLicenseInfoSerialNumber,
       "eltexLicenseInfoMacAddress": eltexLicenseInfoMacAddress,
       "eltexLicenseInfoVendorName": eltexLicenseInfoVendorName,
       "eltexLicenseInfoDeviceName": eltexLicenseInfoDeviceName,
       "eltexLicenseFeature": eltexLicenseFeature,
       "eltexLicenseFeatureTable": eltexLicenseFeatureTable,
       "eltexLicenseFeatureEntry": eltexLicenseFeatureEntry,
       "eltexLicenseFeatureName": eltexLicenseFeatureName,
       "eltexLicenseFeatureActive": eltexLicenseFeatureActive,
       "eltexLicenseFeatureCountable": eltexLicenseFeatureCountable,
       "eltexLicenseFeatureLicensesInstalled": eltexLicenseFeatureLicensesInstalled,
       "eltexLicenseFeatureLicensesUsed": eltexLicenseFeatureLicensesUsed,
       "eltexLicenseFeatureListTable": eltexLicenseFeatureListTable,
       "eltexLicenseFeatureListEntry": eltexLicenseFeatureListEntry,
       "eltexLicenseFeatureListCount": eltexLicenseFeatureListCount,
       "eltexLicenseMIBNotifications": eltexLicenseMIBNotifications,
       "eltexLicenseMIBNotificationsPrefix": eltexLicenseMIBNotificationsPrefix,
       "eltexLicenseMIBConformance": eltexLicenseMIBConformance}
)
