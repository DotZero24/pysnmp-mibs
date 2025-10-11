# SNMP MIB module (RAD-License-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-License-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:27 2025
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

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 fileSystemObjName,
 fileSystemObjType,
 fileSystemPath) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "fileSystemObjName",
    "fileSystemObjType",
    "fileSystemPath")

(agnt,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "agnt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

agnLicense = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LicenseNotifications_ObjectIdentity = ObjectIdentity
licenseNotifications = _LicenseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 0)
)
_LicenseConfig_ObjectIdentity = ObjectIdentity
licenseConfig = _LicenseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1)
)
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 1)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 1, 1)
)
licenseEntry.setIndexNames(
    (0, "RAD-GEN-MIB", "fileSystemPath"),
    (0, "RAD-GEN-MIB", "fileSystemObjType"),
    (1, "RAD-GEN-MIB", "fileSystemObjName"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")
_LicenseId_Type = Unsigned32
_LicenseId_Object = MibTableColumn
licenseId = _LicenseId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 1, 1, 1),
    _LicenseId_Type()
)
licenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseId.setStatus("current")
_LicenseFeatureTable_Object = MibTable
licenseFeatureTable = _LicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2)
)
if mibBuilder.loadTexts:
    licenseFeatureTable.setStatus("current")
_LicenseFeatureEntry_Object = MibTableRow
licenseFeatureEntry = _LicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1)
)
licenseFeatureEntry.setIndexNames(
    (0, "RAD-License-MIB", "licenseId"),
    (0, "RAD-License-MIB", "licenseFeatureId"),
)
if mibBuilder.loadTexts:
    licenseFeatureEntry.setStatus("current")
_LicenseFeatureId_Type = Unsigned32
_LicenseFeatureId_Object = MibTableColumn
licenseFeatureId = _LicenseFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 1),
    _LicenseFeatureId_Type()
)
licenseFeatureId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseFeatureId.setStatus("current")


class _LicenseFeatureName_Type(SnmpAdminString):
    """Custom type licenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LicenseFeatureName_Type.__name__ = "SnmpAdminString"
_LicenseFeatureName_Object = MibTableColumn
licenseFeatureName = _LicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 2),
    _LicenseFeatureName_Type()
)
licenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureName.setStatus("current")


class _LicenseFeatureStatus_Type(Integer32):
    """Custom type licenseFeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("perpetual", 2),
          ("perpeutalAll", 3),
          ("temporary", 4),
          ("temporaryAll", 5),
          ("expired", 6))
    )


_LicenseFeatureStatus_Type.__name__ = "Integer32"
_LicenseFeatureStatus_Object = MibTableColumn
licenseFeatureStatus = _LicenseFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 3),
    _LicenseFeatureStatus_Type()
)
licenseFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureStatus.setStatus("current")
_LicenseFeatureMaxAvailableQuantity_Type = Unsigned32
_LicenseFeatureMaxAvailableQuantity_Object = MibTableColumn
licenseFeatureMaxAvailableQuantity = _LicenseFeatureMaxAvailableQuantity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 4),
    _LicenseFeatureMaxAvailableQuantity_Type()
)
licenseFeatureMaxAvailableQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureMaxAvailableQuantity.setStatus("current")
_LicenseFeatureAllowedQuantity_Type = Unsigned32
_LicenseFeatureAllowedQuantity_Object = MibTableColumn
licenseFeatureAllowedQuantity = _LicenseFeatureAllowedQuantity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 5),
    _LicenseFeatureAllowedQuantity_Type()
)
licenseFeatureAllowedQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureAllowedQuantity.setStatus("current")
_LicenseFeatureQuantityInUse_Type = Unsigned32
_LicenseFeatureQuantityInUse_Object = MibTableColumn
licenseFeatureQuantityInUse = _LicenseFeatureQuantityInUse_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 6),
    _LicenseFeatureQuantityInUse_Type()
)
licenseFeatureQuantityInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureQuantityInUse.setStatus("current")
_LicenseFeatureExpiration_Type = Unsigned32
_LicenseFeatureExpiration_Object = MibTableColumn
licenseFeatureExpiration = _LicenseFeatureExpiration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 7),
    _LicenseFeatureExpiration_Type()
)
licenseFeatureExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureExpiration.setStatus("current")


class _LicenseFeatureActivationCmd_Type(Integer32):
    """Custom type licenseFeatureActivationCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_LicenseFeatureActivationCmd_Type.__name__ = "Integer32"
_LicenseFeatureActivationCmd_Object = MibTableColumn
licenseFeatureActivationCmd = _LicenseFeatureActivationCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 1, 2, 1, 8),
    _LicenseFeatureActivationCmd_Type()
)
licenseFeatureActivationCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseFeatureActivationCmd.setStatus("current")

# Managed Objects groups


# Notification objects

systemLicenseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 0, 8)
)
systemLicenseEnabled.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-License-MIB", "licenseFeatureName"))
)
if mibBuilder.loadTexts:
    systemLicenseEnabled.setStatus(
        "current"
    )

systemLicenseDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 73, 0, 9)
)
systemLicenseDisabled.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-License-MIB", "licenseFeatureName"))
)
if mibBuilder.loadTexts:
    systemLicenseDisabled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-License-MIB",
    **{"agnLicense": agnLicense,
       "licenseNotifications": licenseNotifications,
       "systemLicenseEnabled": systemLicenseEnabled,
       "systemLicenseDisabled": systemLicenseDisabled,
       "licenseConfig": licenseConfig,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseId": licenseId,
       "licenseFeatureTable": licenseFeatureTable,
       "licenseFeatureEntry": licenseFeatureEntry,
       "licenseFeatureId": licenseFeatureId,
       "licenseFeatureName": licenseFeatureName,
       "licenseFeatureStatus": licenseFeatureStatus,
       "licenseFeatureMaxAvailableQuantity": licenseFeatureMaxAvailableQuantity,
       "licenseFeatureAllowedQuantity": licenseFeatureAllowedQuantity,
       "licenseFeatureQuantityInUse": licenseFeatureQuantityInUse,
       "licenseFeatureExpiration": licenseFeatureExpiration,
       "licenseFeatureActivationCmd": licenseFeatureActivationCmd}
)
