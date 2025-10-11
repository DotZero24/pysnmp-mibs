# SNMP MIB module (MX-SECURITY-CERTIFICATES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SECURITY-CERTIFICATES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:45 2025
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

(mediatrixMgmt,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixMgmt")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

securityCertificatesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200)
)
if mibBuilder.loadTexts:
    securityCertificatesMIB.setRevisions(
        ("2005-04-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SecurityCertificatesMIBObjects_ObjectIdentity = ObjectIdentity
securityCertificatesMIBObjects = _SecurityCertificatesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 1)
)
_CertificateTable_Object = MibTable
certificateTable = _CertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500)
)
if mibBuilder.loadTexts:
    certificateTable.setStatus("current")
_CertificateEntry_Object = MibTableRow
certificateEntry = _CertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50)
)
certificateEntry.setIndexNames(
    (0, "MX-SECURITY-CERTIFICATES-MIB", "certificateName"),
)
if mibBuilder.loadTexts:
    certificateEntry.setStatus("current")


class _CertificateName_Type(OctetString):
    """Custom type certificateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CertificateName_Type.__name__ = "OctetString"
_CertificateName_Object = MibTableColumn
certificateName = _CertificateName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50, 50),
    _CertificateName_Type()
)
certificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateName.setStatus("current")


class _CertificateSubjectCommonName_Type(OctetString):
    """Custom type certificateSubjectCommonName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CertificateSubjectCommonName_Type.__name__ = "OctetString"
_CertificateSubjectCommonName_Object = MibTableColumn
certificateSubjectCommonName = _CertificateSubjectCommonName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50, 100),
    _CertificateSubjectCommonName_Type()
)
certificateSubjectCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSubjectCommonName.setStatus("current")


class _CertificateExpirationDate_Type(OctetString):
    """Custom type certificateExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_CertificateExpirationDate_Type.__name__ = "OctetString"
_CertificateExpirationDate_Object = MibTableColumn
certificateExpirationDate = _CertificateExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50, 150),
    _CertificateExpirationDate_Type()
)
certificateExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateExpirationDate.setStatus("current")
_SecurityCertificatesConformance_ObjectIdentity = ObjectIdentity
securityCertificatesConformance = _SecurityCertificatesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 5)
)
_SecurityCertificatesCompliances_ObjectIdentity = ObjectIdentity
securityCertificatesCompliances = _SecurityCertificatesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 1)
)
_SecurityCertificatesGroups_ObjectIdentity = ObjectIdentity
securityCertificatesGroups = _SecurityCertificatesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 5)
)

# Managed Objects groups

securityCertificatesVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 5, 10)
)
securityCertificatesVer1.setObjects(
      *(("MX-SECURITY-CERTIFICATES-MIB", "certificateSubjectCommonName"),
        ("MX-SECURITY-CERTIFICATES-MIB", "certificateExpirationDate"))
)
if mibBuilder.loadTexts:
    securityCertificatesVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

securityCertificatesComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 1, 1)
)
securityCertificatesComplVer1.setObjects(
    ("MX-SECURITY-CERTIFICATES-MIB", "securityCertificatesVer1")
)
if mibBuilder.loadTexts:
    securityCertificatesComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SECURITY-CERTIFICATES-MIB",
    **{"securityCertificatesMIB": securityCertificatesMIB,
       "securityCertificatesMIBObjects": securityCertificatesMIBObjects,
       "certificateTable": certificateTable,
       "certificateEntry": certificateEntry,
       "certificateName": certificateName,
       "certificateSubjectCommonName": certificateSubjectCommonName,
       "certificateExpirationDate": certificateExpirationDate,
       "securityCertificatesConformance": securityCertificatesConformance,
       "securityCertificatesCompliances": securityCertificatesCompliances,
       "securityCertificatesComplVer1": securityCertificatesComplVer1,
       "securityCertificatesGroups": securityCertificatesGroups,
       "securityCertificatesVer1": securityCertificatesVer1}
)
