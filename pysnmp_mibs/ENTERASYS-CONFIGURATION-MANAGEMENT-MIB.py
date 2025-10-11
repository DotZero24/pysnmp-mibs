# SNMP MIB module (ENTERASYS-CONFIGURATION-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-CONFIGURATION-MANAGEMENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:28 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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

etsysConfigurationManagementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16)
)
if mibBuilder.loadTexts:
    etsysConfigurationManagementMIB.setRevisions(
        ("2013-02-04 16:00",
         "2008-12-05 14:13",
         "2002-10-03 20:21",
         "2002-09-30 17:02",
         "2001-12-03 19:49")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigMgmtOperations(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("resetHardware", 0),
          ("resetSoftware", 1),
          ("imageDownload", 2),
          ("imageDownloadNonPersistent", 3),
          ("configurationReset", 4),
          ("configurationUpload", 5),
          ("configurationDownload", 6),
          ("imageSetSelected", 7),
          ("imageGetSelected", 8),
          ("configurationActivate", 9),
          ("configurationAppend", 10),
          ("configurationPersist", 11),
          ("configurationParse", 12),
          ("validationMD5sum", 13),
          ("bootPromDownload", 14))
    )


# MIB Managed Objects in the order of their OIDs

_EtsysConfigMgmtNotifications_ObjectIdentity = ObjectIdentity
etsysConfigMgmtNotifications = _EtsysConfigMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 0)
)
_EtsysConfigMgmtStatus_ObjectIdentity = ObjectIdentity
etsysConfigMgmtStatus = _EtsysConfigMgmtStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1)
)


class _EtsysConfigMgmtCurrentImageURL_Type(DisplayString):
    """Custom type etsysConfigMgmtCurrentImageURL based on DisplayString"""
    defaultHexValue = ""


_EtsysConfigMgmtCurrentImageURL_Type.__name__ = "DisplayString"
_EtsysConfigMgmtCurrentImageURL_Object = MibScalar
etsysConfigMgmtCurrentImageURL = _EtsysConfigMgmtCurrentImageURL_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 1),
    _EtsysConfigMgmtCurrentImageURL_Type()
)
etsysConfigMgmtCurrentImageURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtCurrentImageURL.setStatus("current")


class _EtsysConfigMgmtCurrentConfigURL_Type(DisplayString):
    """Custom type etsysConfigMgmtCurrentConfigURL based on DisplayString"""
    defaultHexValue = ""


_EtsysConfigMgmtCurrentConfigURL_Type.__name__ = "DisplayString"
_EtsysConfigMgmtCurrentConfigURL_Object = MibScalar
etsysConfigMgmtCurrentConfigURL = _EtsysConfigMgmtCurrentConfigURL_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 2),
    _EtsysConfigMgmtCurrentConfigURL_Type()
)
etsysConfigMgmtCurrentConfigURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtCurrentConfigURL.setStatus("current")


class _EtsysConfigMgmtPersistentStorageStatus_Type(DisplayString):
    """Custom type etsysConfigMgmtPersistentStorageStatus based on DisplayString"""
    defaultHexValue = ""


_EtsysConfigMgmtPersistentStorageStatus_Type.__name__ = "DisplayString"
_EtsysConfigMgmtPersistentStorageStatus_Object = MibScalar
etsysConfigMgmtPersistentStorageStatus = _EtsysConfigMgmtPersistentStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 3),
    _EtsysConfigMgmtPersistentStorageStatus_Type()
)
etsysConfigMgmtPersistentStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtPersistentStorageStatus.setStatus("current")


class _EtsysConfigMgmtPersistentStorageCkSum_Type(DisplayString):
    """Custom type etsysConfigMgmtPersistentStorageCkSum based on DisplayString"""
    defaultHexValue = ""


_EtsysConfigMgmtPersistentStorageCkSum_Type.__name__ = "DisplayString"
_EtsysConfigMgmtPersistentStorageCkSum_Object = MibScalar
etsysConfigMgmtPersistentStorageCkSum = _EtsysConfigMgmtPersistentStorageCkSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 4),
    _EtsysConfigMgmtPersistentStorageCkSum_Type()
)
etsysConfigMgmtPersistentStorageCkSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtPersistentStorageCkSum.setStatus("current")
_EtsysConfigMgmtChange_ObjectIdentity = ObjectIdentity
etsysConfigMgmtChange = _EtsysConfigMgmtChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2)
)


class _EtsysConfigMgmtChangeLimit_Type(Unsigned32):
    """Custom type etsysConfigMgmtChangeLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysConfigMgmtChangeLimit_Type.__name__ = "Unsigned32"
_EtsysConfigMgmtChangeLimit_Object = MibScalar
etsysConfigMgmtChangeLimit = _EtsysConfigMgmtChangeLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 1),
    _EtsysConfigMgmtChangeLimit_Type()
)
etsysConfigMgmtChangeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeLimit.setStatus("current")
_EtsysConfigMgmtChangeCurrent_Type = Gauge32
_EtsysConfigMgmtChangeCurrent_Object = MibScalar
etsysConfigMgmtChangeCurrent = _EtsysConfigMgmtChangeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 2),
    _EtsysConfigMgmtChangeCurrent_Type()
)
etsysConfigMgmtChangeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeCurrent.setStatus("current")
_EtsysConfigMgmtChangeCompleted_Type = Counter32
_EtsysConfigMgmtChangeCompleted_Object = MibScalar
etsysConfigMgmtChangeCompleted = _EtsysConfigMgmtChangeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 3),
    _EtsysConfigMgmtChangeCompleted_Type()
)
etsysConfigMgmtChangeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeCompleted.setStatus("current")


class _EtsysConfigMgmtChangeSupportedURLs_Type(Bits):
    """Custom type etsysConfigMgmtChangeSupportedURLs based on Bits"""
    namedValues = NamedValues(
        *(("etsysConfigMgmtFtp", 0),
          ("etsysConfigMgmtRcp", 1),
          ("etsysConfigMgmtHttp", 2),
          ("etsysConfigMgmtTftp", 3),
          ("etsysConfigMgmtFile", 4),
          ("etsysConfigMgmtBootP", 5),
          ("etsysConfigMgmtScp", 6))
    )

_EtsysConfigMgmtChangeSupportedURLs_Type.__name__ = "Bits"
_EtsysConfigMgmtChangeSupportedURLs_Object = MibScalar
etsysConfigMgmtChangeSupportedURLs = _EtsysConfigMgmtChangeSupportedURLs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 4),
    _EtsysConfigMgmtChangeSupportedURLs_Type()
)
etsysConfigMgmtChangeSupportedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeSupportedURLs.setStatus("current")
_EtsysConfigMgmtChangeSupportedOperations_Type = ConfigMgmtOperations
_EtsysConfigMgmtChangeSupportedOperations_Object = MibScalar
etsysConfigMgmtChangeSupportedOperations = _EtsysConfigMgmtChangeSupportedOperations_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 5),
    _EtsysConfigMgmtChangeSupportedOperations_Type()
)
etsysConfigMgmtChangeSupportedOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeSupportedOperations.setStatus("current")


class _EtsysConfigMgmtChangeNextAvailableIndex_Type(Unsigned32):
    """Custom type etsysConfigMgmtChangeNextAvailableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysConfigMgmtChangeNextAvailableIndex_Type.__name__ = "Unsigned32"
_EtsysConfigMgmtChangeNextAvailableIndex_Object = MibScalar
etsysConfigMgmtChangeNextAvailableIndex = _EtsysConfigMgmtChangeNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 6),
    _EtsysConfigMgmtChangeNextAvailableIndex_Type()
)
etsysConfigMgmtChangeNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeNextAvailableIndex.setStatus("current")
_EtsysConfigMgmtChangeTable_Object = MibTable
etsysConfigMgmtChangeTable = _EtsysConfigMgmtChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7)
)
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeTable.setStatus("current")
_EtsysConfigMgmtChangeEntry_Object = MibTableRow
etsysConfigMgmtChangeEntry = _EtsysConfigMgmtChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1)
)
etsysConfigMgmtChangeEntry.setIndexNames(
    (0, "ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeIndex"),
)
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeEntry.setStatus("current")


class _EtsysConfigMgmtChangeIndex_Type(Unsigned32):
    """Custom type etsysConfigMgmtChangeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysConfigMgmtChangeIndex_Type.__name__ = "Unsigned32"
_EtsysConfigMgmtChangeIndex_Object = MibTableColumn
etsysConfigMgmtChangeIndex = _EtsysConfigMgmtChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 1),
    _EtsysConfigMgmtChangeIndex_Type()
)
etsysConfigMgmtChangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeIndex.setStatus("current")


class _EtsysConfigMgmtChangeURL_Type(DisplayString):
    """Custom type etsysConfigMgmtChangeURL based on DisplayString"""
    defaultHexValue = ""


_EtsysConfigMgmtChangeURL_Type.__name__ = "DisplayString"
_EtsysConfigMgmtChangeURL_Object = MibTableColumn
etsysConfigMgmtChangeURL = _EtsysConfigMgmtChangeURL_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 2),
    _EtsysConfigMgmtChangeURL_Type()
)
etsysConfigMgmtChangeURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeURL.setStatus("current")
_EtsysConfigMgmtChangeOperation_Type = ConfigMgmtOperations
_EtsysConfigMgmtChangeOperation_Object = MibTableColumn
etsysConfigMgmtChangeOperation = _EtsysConfigMgmtChangeOperation_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 3),
    _EtsysConfigMgmtChangeOperation_Type()
)
etsysConfigMgmtChangeOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeOperation.setStatus("current")


class _EtsysConfigMgmtChangeOperStatus_Type(Integer32):
    """Custom type etsysConfigMgmtChangeOperStatus based on Integer32"""
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
        *(("inactive", 1),
          ("pending", 2),
          ("running", 3),
          ("success", 4),
          ("failure", 5))
    )


_EtsysConfigMgmtChangeOperStatus_Type.__name__ = "Integer32"
_EtsysConfigMgmtChangeOperStatus_Object = MibTableColumn
etsysConfigMgmtChangeOperStatus = _EtsysConfigMgmtChangeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 4),
    _EtsysConfigMgmtChangeOperStatus_Type()
)
etsysConfigMgmtChangeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeOperStatus.setStatus("current")


class _EtsysConfigMgmtChangeDelayTime_Type(Unsigned32):
    """Custom type etsysConfigMgmtChangeDelayTime based on Unsigned32"""
    defaultValue = 0


_EtsysConfigMgmtChangeDelayTime_Type.__name__ = "Unsigned32"
_EtsysConfigMgmtChangeDelayTime_Object = MibTableColumn
etsysConfigMgmtChangeDelayTime = _EtsysConfigMgmtChangeDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 5),
    _EtsysConfigMgmtChangeDelayTime_Type()
)
etsysConfigMgmtChangeDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeDelayTime.setUnits("seconds")


class _EtsysConfigMgmtChangeEnqueuedTime_Type(DateAndTime):
    """Custom type etsysConfigMgmtChangeEnqueuedTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_EtsysConfigMgmtChangeEnqueuedTime_Type.__name__ = "DateAndTime"
_EtsysConfigMgmtChangeEnqueuedTime_Object = MibTableColumn
etsysConfigMgmtChangeEnqueuedTime = _EtsysConfigMgmtChangeEnqueuedTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 6),
    _EtsysConfigMgmtChangeEnqueuedTime_Type()
)
etsysConfigMgmtChangeEnqueuedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeEnqueuedTime.setStatus("current")


class _EtsysConfigMgmtChangeCompletionTime_Type(DateAndTime):
    """Custom type etsysConfigMgmtChangeCompletionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_EtsysConfigMgmtChangeCompletionTime_Type.__name__ = "DateAndTime"
_EtsysConfigMgmtChangeCompletionTime_Object = MibTableColumn
etsysConfigMgmtChangeCompletionTime = _EtsysConfigMgmtChangeCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 7),
    _EtsysConfigMgmtChangeCompletionTime_Type()
)
etsysConfigMgmtChangeCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeCompletionTime.setStatus("current")


class _EtsysConfigMgmtChangeBytesTransferred_Type(Integer32):
    """Custom type etsysConfigMgmtChangeBytesTransferred based on Integer32"""
    defaultValue = 0


_EtsysConfigMgmtChangeBytesTransferred_Type.__name__ = "Integer32"
_EtsysConfigMgmtChangeBytesTransferred_Object = MibTableColumn
etsysConfigMgmtChangeBytesTransferred = _EtsysConfigMgmtChangeBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 8),
    _EtsysConfigMgmtChangeBytesTransferred_Type()
)
etsysConfigMgmtChangeBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeBytesTransferred.setStatus("current")


class _EtsysConfigMgmtChangeValidationString_Type(DisplayString):
    """Custom type etsysConfigMgmtChangeValidationString based on DisplayString"""
    defaultHexValue = ""


_EtsysConfigMgmtChangeValidationString_Type.__name__ = "DisplayString"
_EtsysConfigMgmtChangeValidationString_Object = MibTableColumn
etsysConfigMgmtChangeValidationString = _EtsysConfigMgmtChangeValidationString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 9),
    _EtsysConfigMgmtChangeValidationString_Type()
)
etsysConfigMgmtChangeValidationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeValidationString.setStatus("current")


class _EtsysConfigMgmtChangeErrorDescription_Type(SnmpAdminString):
    """Custom type etsysConfigMgmtChangeErrorDescription based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysConfigMgmtChangeErrorDescription_Type.__name__ = "SnmpAdminString"
_EtsysConfigMgmtChangeErrorDescription_Object = MibTableColumn
etsysConfigMgmtChangeErrorDescription = _EtsysConfigMgmtChangeErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 10),
    _EtsysConfigMgmtChangeErrorDescription_Type()
)
etsysConfigMgmtChangeErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeErrorDescription.setStatus("current")
_EtsysConfigMgmtChangeRowStatus_Type = RowStatus
_EtsysConfigMgmtChangeRowStatus_Object = MibTableColumn
etsysConfigMgmtChangeRowStatus = _EtsysConfigMgmtChangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 11),
    _EtsysConfigMgmtChangeRowStatus_Type()
)
etsysConfigMgmtChangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeRowStatus.setStatus("current")
_EtsysConfigMgmtConformance_ObjectIdentity = ObjectIdentity
etsysConfigMgmtConformance = _EtsysConfigMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3)
)
_EtsysConfigMgmtGroups_ObjectIdentity = ObjectIdentity
etsysConfigMgmtGroups = _EtsysConfigMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1)
)
_EtsysConfigMgmtCompliances_ObjectIdentity = ObjectIdentity
etsysConfigMgmtCompliances = _EtsysConfigMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2)
)

# Managed Objects groups

etsysConfigMgmtStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 1)
)
etsysConfigMgmtStatusGroup.setObjects(
      *(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtCurrentImageURL"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtCurrentConfigURL"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtPersistentStorageStatus"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtPersistentStorageCkSum"))
)
if mibBuilder.loadTexts:
    etsysConfigMgmtStatusGroup.setStatus("current")

etsysConfigMgmtChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 2)
)
etsysConfigMgmtChangeGroup.setObjects(
      *(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeLimit"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCurrent"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCompleted"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeSupportedURLs"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeSupportedOperations"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeNextAvailableIndex"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeURL"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeOperation"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeOperStatus"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeDelayTime"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeEnqueuedTime"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCompletionTime"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeBytesTransferred"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeValidationString"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeErrorDescription"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeRowStatus"))
)
if mibBuilder.loadTexts:
    etsysConfigMgmtChangeGroup.setStatus("current")


# Notification objects

etsysConfigMgmtReadyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 0, 1)
)
if mibBuilder.loadTexts:
    etsysConfigMgmtReadyNotification.setStatus(
        "current"
    )


# Notifications groups

etsysConfigMgmtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 3)
)
etsysConfigMgmtNotificationsGroup.setObjects(
    ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtReadyNotification")
)
if mibBuilder.loadTexts:
    etsysConfigMgmtNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysConfigMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2, 1)
)
etsysConfigMgmtCompliance.setObjects(
      *(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtStatusGroup"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeGroup"))
)
if mibBuilder.loadTexts:
    etsysConfigMgmtCompliance.setStatus(
        "deprecated"
    )

etsysConfigMgmtCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2, 2)
)
etsysConfigMgmtCompliance2.setObjects(
      *(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtStatusGroup"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeGroup"),
        ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtNotificationsGroup"))
)
if mibBuilder.loadTexts:
    etsysConfigMgmtCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-CONFIGURATION-MANAGEMENT-MIB",
    **{"ConfigMgmtOperations": ConfigMgmtOperations,
       "etsysConfigurationManagementMIB": etsysConfigurationManagementMIB,
       "etsysConfigMgmtNotifications": etsysConfigMgmtNotifications,
       "etsysConfigMgmtReadyNotification": etsysConfigMgmtReadyNotification,
       "etsysConfigMgmtStatus": etsysConfigMgmtStatus,
       "etsysConfigMgmtCurrentImageURL": etsysConfigMgmtCurrentImageURL,
       "etsysConfigMgmtCurrentConfigURL": etsysConfigMgmtCurrentConfigURL,
       "etsysConfigMgmtPersistentStorageStatus": etsysConfigMgmtPersistentStorageStatus,
       "etsysConfigMgmtPersistentStorageCkSum": etsysConfigMgmtPersistentStorageCkSum,
       "etsysConfigMgmtChange": etsysConfigMgmtChange,
       "etsysConfigMgmtChangeLimit": etsysConfigMgmtChangeLimit,
       "etsysConfigMgmtChangeCurrent": etsysConfigMgmtChangeCurrent,
       "etsysConfigMgmtChangeCompleted": etsysConfigMgmtChangeCompleted,
       "etsysConfigMgmtChangeSupportedURLs": etsysConfigMgmtChangeSupportedURLs,
       "etsysConfigMgmtChangeSupportedOperations": etsysConfigMgmtChangeSupportedOperations,
       "etsysConfigMgmtChangeNextAvailableIndex": etsysConfigMgmtChangeNextAvailableIndex,
       "etsysConfigMgmtChangeTable": etsysConfigMgmtChangeTable,
       "etsysConfigMgmtChangeEntry": etsysConfigMgmtChangeEntry,
       "etsysConfigMgmtChangeIndex": etsysConfigMgmtChangeIndex,
       "etsysConfigMgmtChangeURL": etsysConfigMgmtChangeURL,
       "etsysConfigMgmtChangeOperation": etsysConfigMgmtChangeOperation,
       "etsysConfigMgmtChangeOperStatus": etsysConfigMgmtChangeOperStatus,
       "etsysConfigMgmtChangeDelayTime": etsysConfigMgmtChangeDelayTime,
       "etsysConfigMgmtChangeEnqueuedTime": etsysConfigMgmtChangeEnqueuedTime,
       "etsysConfigMgmtChangeCompletionTime": etsysConfigMgmtChangeCompletionTime,
       "etsysConfigMgmtChangeBytesTransferred": etsysConfigMgmtChangeBytesTransferred,
       "etsysConfigMgmtChangeValidationString": etsysConfigMgmtChangeValidationString,
       "etsysConfigMgmtChangeErrorDescription": etsysConfigMgmtChangeErrorDescription,
       "etsysConfigMgmtChangeRowStatus": etsysConfigMgmtChangeRowStatus,
       "etsysConfigMgmtConformance": etsysConfigMgmtConformance,
       "etsysConfigMgmtGroups": etsysConfigMgmtGroups,
       "etsysConfigMgmtStatusGroup": etsysConfigMgmtStatusGroup,
       "etsysConfigMgmtChangeGroup": etsysConfigMgmtChangeGroup,
       "etsysConfigMgmtNotificationsGroup": etsysConfigMgmtNotificationsGroup,
       "etsysConfigMgmtCompliances": etsysConfigMgmtCompliances,
       "etsysConfigMgmtCompliance": etsysConfigMgmtCompliance,
       "etsysConfigMgmtCompliance2": etsysConfigMgmtCompliance2}
)
