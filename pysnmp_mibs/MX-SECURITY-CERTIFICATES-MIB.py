#
# PySNMP MIB module MX-SECURITY-CERTIFICATES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-SECURITY-CERTIFICATES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixMgmt, = mibBuilder.importSymbols("MX-SMI", "mediatrixMgmt")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
securityCertificatesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 10, 200))
securityCertificatesMIB.setRevisions(('2005-04-21 00:00',))
if mibBuilder.loadTexts: securityCertificatesMIB.setLastUpdated('200504210000Z')
if mibBuilder.loadTexts: securityCertificatesMIB.setOrganization('Mediatrix Telecom, Inc.')
securityCertificatesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 200, 1))
securityCertificatesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 200, 5))
certificateTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500), )
if mibBuilder.loadTexts: certificateTable.setStatus('current')
certificateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50), ).setIndexNames((0, "MX-SECURITY-CERTIFICATES-MIB", "certificateName"))
if mibBuilder.loadTexts: certificateEntry.setStatus('current')
certificateName = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50, 50), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: certificateName.setStatus('current')
certificateSubjectCommonName = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50, 100), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: certificateSubjectCommonName.setStatus('current')
certificateExpirationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 10, 200, 1, 500, 50, 150), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: certificateExpirationDate.setStatus('current')
securityCertificatesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 1))
securityCertificatesComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 1, 1)).setObjects(("MX-SECURITY-CERTIFICATES-MIB", "securityCertificatesVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    securityCertificatesComplVer1 = securityCertificatesComplVer1.setStatus('current')
securityCertificatesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 5))
securityCertificatesVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 10, 200, 5, 5, 10)).setObjects(("MX-SECURITY-CERTIFICATES-MIB", "certificateSubjectCommonName"), ("MX-SECURITY-CERTIFICATES-MIB", "certificateExpirationDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    securityCertificatesVer1 = securityCertificatesVer1.setStatus('current')
mibBuilder.exportSymbols("MX-SECURITY-CERTIFICATES-MIB", certificateName=certificateName, securityCertificatesComplVer1=securityCertificatesComplVer1, PYSNMP_MODULE_ID=securityCertificatesMIB, certificateSubjectCommonName=certificateSubjectCommonName, securityCertificatesMIBObjects=securityCertificatesMIBObjects, certificateTable=certificateTable, securityCertificatesConformance=securityCertificatesConformance, securityCertificatesMIB=securityCertificatesMIB, certificateEntry=certificateEntry, securityCertificatesCompliances=securityCertificatesCompliances, securityCertificatesGroups=securityCertificatesGroups, certificateExpirationDate=certificateExpirationDate, securityCertificatesVer1=securityCertificatesVer1)
