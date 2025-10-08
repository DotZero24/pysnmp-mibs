#
# PySNMP MIB module ENTERASYS-PKI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-PKI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
etsysPkiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101))
etsysPkiMIB.setRevisions(('2013-03-27 11:08',))
if mibBuilder.loadTexts: etsysPkiMIB.setLastUpdated('201303271108Z')
if mibBuilder.loadTexts: etsysPkiMIB.setOrganization('Enterasys Networks, Inc')
etsysPkiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1))
etsysPkiNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 0))
etsysPkiCertificateBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1))
etsysPkiCertListName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysPkiCertListName.setStatus('current')
etsysPkiCertFingerprint = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysPkiCertFingerprint.setStatus('current')
etsysPkiCertIssuerName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysPkiCertIssuerName.setStatus('current')
etsysPkiCertSubjectName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysPkiCertSubjectName.setStatus('current')
etsysPkiCertStartDate = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysPkiCertStartDate.setStatus('current')
etsysPkiCertEndDate = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 1, 6), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysPkiCertEndDate.setStatus('current')
etsysPkiCertNearingExpirationNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 1, 0, 1)).setObjects(("ENTERASYS-PKI-MIB", "etsysPkiCertListName"), ("ENTERASYS-PKI-MIB", "etsysPkiCertFingerprint"), ("ENTERASYS-PKI-MIB", "etsysPkiCertIssuerName"), ("ENTERASYS-PKI-MIB", "etsysPkiCertSubjectName"), ("ENTERASYS-PKI-MIB", "etsysPkiCertStartDate"), ("ENTERASYS-PKI-MIB", "etsysPkiCertEndDate"))
if mibBuilder.loadTexts: etsysPkiCertNearingExpirationNotification.setStatus('current')
etsysPkiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2))
etsysPkiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 1))
etsysPkiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 2))
etsysPkiCertificateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 1, 1)).setObjects(("ENTERASYS-PKI-MIB", "etsysPkiCertListName"), ("ENTERASYS-PKI-MIB", "etsysPkiCertFingerprint"), ("ENTERASYS-PKI-MIB", "etsysPkiCertIssuerName"), ("ENTERASYS-PKI-MIB", "etsysPkiCertSubjectName"), ("ENTERASYS-PKI-MIB", "etsysPkiCertStartDate"), ("ENTERASYS-PKI-MIB", "etsysPkiCertEndDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPkiCertificateGroup = etsysPkiCertificateGroup.setStatus('current')
etsysPkiNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 1, 2)).setObjects(("ENTERASYS-PKI-MIB", "etsysPkiCertNearingExpirationNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPkiNotificationGroup = etsysPkiNotificationGroup.setStatus('current')
etsysPkiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 101, 2, 2, 1)).setObjects(("ENTERASYS-PKI-MIB", "etsysPkiCertificateGroup"), ("ENTERASYS-PKI-MIB", "etsysPkiNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPkiCompliance = etsysPkiCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-PKI-MIB", etsysPkiCompliances=etsysPkiCompliances, etsysPkiConformance=etsysPkiConformance, etsysPkiCertificateBranch=etsysPkiCertificateBranch, etsysPkiCertStartDate=etsysPkiCertStartDate, etsysPkiCertEndDate=etsysPkiCertEndDate, etsysPkiCertificateGroup=etsysPkiCertificateGroup, etsysPkiCompliance=etsysPkiCompliance, etsysPkiCertFingerprint=etsysPkiCertFingerprint, etsysPkiCertNearingExpirationNotification=etsysPkiCertNearingExpirationNotification, PYSNMP_MODULE_ID=etsysPkiMIB, etsysPkiCertIssuerName=etsysPkiCertIssuerName, etsysPkiGroups=etsysPkiGroups, etsysPkiCertSubjectName=etsysPkiCertSubjectName, etsysPkiObjects=etsysPkiObjects, etsysPkiNotificationBranch=etsysPkiNotificationBranch, etsysPkiNotificationGroup=etsysPkiNotificationGroup, etsysPkiCertListName=etsysPkiCertListName, etsysPkiMIB=etsysPkiMIB)
