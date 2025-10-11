# SNMP MIB module (ENTERASYS-PKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-PKI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:16 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

etsysPkiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101)
)
if mibBuilder.loadTexts:
    etsysPkiMIB.setRevisions(
        ("2013-03-27 11:08",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysPkiObjects_ObjectIdentity = ObjectIdentity
etsysPkiObjects = _EtsysPkiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1)
)
_EtsysPkiNotificationBranch_ObjectIdentity = ObjectIdentity
etsysPkiNotificationBranch = _EtsysPkiNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 0)
)
_EtsysPkiCertificateBranch_ObjectIdentity = ObjectIdentity
etsysPkiCertificateBranch = _EtsysPkiCertificateBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1)
)


class _EtsysPkiCertListName_Type(SnmpAdminString):
    """Custom type etsysPkiCertListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysPkiCertListName_Type.__name__ = "SnmpAdminString"
_EtsysPkiCertListName_Object = MibScalar
etsysPkiCertListName = _EtsysPkiCertListName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 1),
    _EtsysPkiCertListName_Type()
)
etsysPkiCertListName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysPkiCertListName.setStatus("current")


class _EtsysPkiCertFingerprint_Type(OctetString):
    """Custom type etsysPkiCertFingerprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_EtsysPkiCertFingerprint_Type.__name__ = "OctetString"
_EtsysPkiCertFingerprint_Object = MibScalar
etsysPkiCertFingerprint = _EtsysPkiCertFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 2),
    _EtsysPkiCertFingerprint_Type()
)
etsysPkiCertFingerprint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysPkiCertFingerprint.setStatus("current")


class _EtsysPkiCertIssuerName_Type(SnmpAdminString):
    """Custom type etsysPkiCertIssuerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EtsysPkiCertIssuerName_Type.__name__ = "SnmpAdminString"
_EtsysPkiCertIssuerName_Object = MibScalar
etsysPkiCertIssuerName = _EtsysPkiCertIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 3),
    _EtsysPkiCertIssuerName_Type()
)
etsysPkiCertIssuerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysPkiCertIssuerName.setStatus("current")


class _EtsysPkiCertSubjectName_Type(SnmpAdminString):
    """Custom type etsysPkiCertSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EtsysPkiCertSubjectName_Type.__name__ = "SnmpAdminString"
_EtsysPkiCertSubjectName_Object = MibScalar
etsysPkiCertSubjectName = _EtsysPkiCertSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 4),
    _EtsysPkiCertSubjectName_Type()
)
etsysPkiCertSubjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysPkiCertSubjectName.setStatus("current")
_EtsysPkiCertStartDate_Type = DateAndTime
_EtsysPkiCertStartDate_Object = MibScalar
etsysPkiCertStartDate = _EtsysPkiCertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 5),
    _EtsysPkiCertStartDate_Type()
)
etsysPkiCertStartDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysPkiCertStartDate.setStatus("current")
_EtsysPkiCertEndDate_Type = DateAndTime
_EtsysPkiCertEndDate_Object = MibScalar
etsysPkiCertEndDate = _EtsysPkiCertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 6),
    _EtsysPkiCertEndDate_Type()
)
etsysPkiCertEndDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysPkiCertEndDate.setStatus("current")
_EtsysPkiConformance_ObjectIdentity = ObjectIdentity
etsysPkiConformance = _EtsysPkiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2)
)
_EtsysPkiGroups_ObjectIdentity = ObjectIdentity
etsysPkiGroups = _EtsysPkiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 1)
)
_EtsysPkiCompliances_ObjectIdentity = ObjectIdentity
etsysPkiCompliances = _EtsysPkiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 2)
)

# Managed Objects groups

etsysPkiCertificateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 1, 1)
)
etsysPkiCertificateGroup.setObjects(
      *(("ENTERASYS-PKI-MIB", "etsysPkiCertListName"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertFingerprint"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertIssuerName"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertSubjectName"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertStartDate"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertEndDate"))
)
if mibBuilder.loadTexts:
    etsysPkiCertificateGroup.setStatus("current")


# Notification objects

etsysPkiCertNearingExpirationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 0, 1)
)
etsysPkiCertNearingExpirationNotification.setObjects(
      *(("ENTERASYS-PKI-MIB", "etsysPkiCertListName"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertFingerprint"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertIssuerName"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertSubjectName"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertStartDate"),
        ("ENTERASYS-PKI-MIB", "etsysPkiCertEndDate"))
)
if mibBuilder.loadTexts:
    etsysPkiCertNearingExpirationNotification.setStatus(
        "current"
    )


# Notifications groups

etsysPkiNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 1, 2)
)
etsysPkiNotificationGroup.setObjects(
    ("ENTERASYS-PKI-MIB", "etsysPkiCertNearingExpirationNotification")
)
if mibBuilder.loadTexts:
    etsysPkiNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysPkiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 2, 1)
)
etsysPkiCompliance.setObjects(
      *(("ENTERASYS-PKI-MIB", "etsysPkiCertificateGroup"),
        ("ENTERASYS-PKI-MIB", "etsysPkiNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPkiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-PKI-MIB",
    **{"etsysPkiMIB": etsysPkiMIB,
       "etsysPkiObjects": etsysPkiObjects,
       "etsysPkiNotificationBranch": etsysPkiNotificationBranch,
       "etsysPkiCertNearingExpirationNotification": etsysPkiCertNearingExpirationNotification,
       "etsysPkiCertificateBranch": etsysPkiCertificateBranch,
       "etsysPkiCertListName": etsysPkiCertListName,
       "etsysPkiCertFingerprint": etsysPkiCertFingerprint,
       "etsysPkiCertIssuerName": etsysPkiCertIssuerName,
       "etsysPkiCertSubjectName": etsysPkiCertSubjectName,
       "etsysPkiCertStartDate": etsysPkiCertStartDate,
       "etsysPkiCertEndDate": etsysPkiCertEndDate,
       "etsysPkiConformance": etsysPkiConformance,
       "etsysPkiGroups": etsysPkiGroups,
       "etsysPkiCertificateGroup": etsysPkiCertificateGroup,
       "etsysPkiNotificationGroup": etsysPkiNotificationGroup,
       "etsysPkiCompliances": etsysPkiCompliances,
       "etsysPkiCompliance": etsysPkiCompliance}
)
