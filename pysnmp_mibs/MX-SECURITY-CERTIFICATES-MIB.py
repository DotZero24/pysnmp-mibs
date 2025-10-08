#
# PySNMP MIB module MX-SECURITY-CERTIFICATES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-SECURITY-CERTIFICATES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixMgmt, = mibBuilder.importSymbols("MX-SMI", "mediatrixMgmt")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-SECURITY-CERTIFICATES-MIB", certificateName=certificateName, certificateTable=certificateTable, securityCertificatesVer1=securityCertificatesVer1, certificateSubjectCommonName=certificateSubjectCommonName, securityCertificatesGroups=securityCertificatesGroups, securityCertificatesCompliances=securityCertificatesCompliances, securityCertificatesMIBObjects=securityCertificatesMIBObjects, securityCertificatesMIB=securityCertificatesMIB, securityCertificatesComplVer1=securityCertificatesComplVer1, PYSNMP_MODULE_ID=securityCertificatesMIB, certificateExpirationDate=certificateExpirationDate, certificateEntry=certificateEntry, securityCertificatesConformance=securityCertificatesConformance)
