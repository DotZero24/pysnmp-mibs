#
# PySNMP MIB module ENTERASYS-PKI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-PKI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-PKI-MIB", etsysPkiCertificateGroup=etsysPkiCertificateGroup, etsysPkiCertStartDate=etsysPkiCertStartDate, etsysPkiCertNearingExpirationNotification=etsysPkiCertNearingExpirationNotification, etsysPkiMIB=etsysPkiMIB, etsysPkiCompliance=etsysPkiCompliance, etsysPkiCertificateBranch=etsysPkiCertificateBranch, etsysPkiConformance=etsysPkiConformance, etsysPkiCertListName=etsysPkiCertListName, etsysPkiCompliances=etsysPkiCompliances, etsysPkiCertEndDate=etsysPkiCertEndDate, etsysPkiNotificationBranch=etsysPkiNotificationBranch, etsysPkiCertIssuerName=etsysPkiCertIssuerName, etsysPkiCertSubjectName=etsysPkiCertSubjectName, etsysPkiObjects=etsysPkiObjects, etsysPkiCertFingerprint=etsysPkiCertFingerprint, etsysPkiGroups=etsysPkiGroups, PYSNMP_MODULE_ID=etsysPkiMIB, etsysPkiNotificationGroup=etsysPkiNotificationGroup)
