# SNMP MIB module (CERTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/kemp/CERTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:31 2025
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

(one4net,) = mibBuilder.importSymbols(
    "ONE4NET-MIB",
    "one4net")

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

certs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 14)
)
if mibBuilder.loadTexts:
    certs.setRevisions(
        ("2018-12-07 03:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CertsTable_Object = MibTable
certsTable = _CertsTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1)
)
if mibBuilder.loadTexts:
    certsTable.setStatus("current")
_CertEntry_Object = MibTableRow
certEntry = _CertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1)
)
certEntry.setIndexNames(
    (0, "CERTS-MIB", "certIdx"),
)
if mibBuilder.loadTexts:
    certEntry.setStatus("current")


class _CertIdx_Type(Integer32):
    """Custom type certIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CertIdx_Type.__name__ = "Integer32"
_CertIdx_Object = MibTableColumn
certIdx = _CertIdx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 1),
    _CertIdx_Type()
)
certIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIdx.setStatus("current")


class _CertFileName_Type(OctetString):
    """Custom type certFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CertFileName_Type.__name__ = "OctetString"
_CertFileName_Object = MibTableColumn
certFileName = _CertFileName_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 2),
    _CertFileName_Type()
)
certFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certFileName.setStatus("current")


class _CertSubjectName_Type(OctetString):
    """Custom type certSubjectName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CertSubjectName_Type.__name__ = "OctetString"
_CertSubjectName_Object = MibTableColumn
certSubjectName = _CertSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 3),
    _CertSubjectName_Type()
)
certSubjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSubjectName.setStatus("current")


class _CertSerialNumber_Type(OctetString):
    """Custom type certSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CertSerialNumber_Type.__name__ = "OctetString"
_CertSerialNumber_Object = MibTableColumn
certSerialNumber = _CertSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 4),
    _CertSerialNumber_Type()
)
certSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSerialNumber.setStatus("current")
_CertStartDate_Type = DateAndTime
_CertStartDate_Object = MibTableColumn
certStartDate = _CertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 5),
    _CertStartDate_Type()
)
certStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certStartDate.setStatus("current")
_CertEndDate_Type = DateAndTime
_CertEndDate_Object = MibTableColumn
certEndDate = _CertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 6),
    _CertEndDate_Type()
)
certEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certEndDate.setStatus("current")


class _CertIssuer_Type(OctetString):
    """Custom type certIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CertIssuer_Type.__name__ = "OctetString"
_CertIssuer_Object = MibTableColumn
certIssuer = _CertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 12196, 14, 1, 1, 7),
    _CertIssuer_Type()
)
certIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIssuer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERTS-MIB",
    **{"certs": certs,
       "certsTable": certsTable,
       "certEntry": certEntry,
       "certIdx": certIdx,
       "certFileName": certFileName,
       "certSubjectName": certSubjectName,
       "certSerialNumber": certSerialNumber,
       "certStartDate": certStartDate,
       "certEndDate": certEndDate,
       "certIssuer": certIssuer}
)
