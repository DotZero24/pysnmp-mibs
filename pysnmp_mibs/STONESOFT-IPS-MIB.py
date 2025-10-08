#
# PySNMP MIB module STONESOFT-IPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/forcepoint/STONESOFT-IPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
stonesoftModules, stonesoftIPS = mibBuilder.importSymbols("STONESOFT-SMI-MIB", "stonesoftModules", "stonesoftIPS")
stonesoftIPSMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1369, 3, 3))
stonesoftIPSMibModule.setRevisions(('2007-01-04 00:00',))
if mibBuilder.loadTexts: stonesoftIPSMibModule.setLastUpdated('200701040000Z')
if mibBuilder.loadTexts: stonesoftIPSMibModule.setOrganization('Stonesoft Corp')
ipsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5, 1))
ipsEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5, 2))
ipsEventsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5, 2, 0))
ipsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5, 3))
ipsSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 5, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsSoftwareVersion.setStatus('current')
ipsSecurityPolicy = MibScalar((1, 3, 6, 1, 4, 1, 1369, 5, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsSecurityPolicy.setStatus('current')
ipsPolicyTime = MibScalar((1, 3, 6, 1, 4, 1, 1369, 5, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsPolicyTime.setStatus('current')
ipsPolicyInstall = NotificationType((1, 3, 6, 1, 4, 1, 1369, 5, 5, 2, 0, 1)).setObjects(("STONESOFT-IPS-MIB", "ipsSecurityPolicy"))
if mibBuilder.loadTexts: ipsPolicyInstall.setStatus('current')
ipsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 1))
ipsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 2))
ipsCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 2, 1)).setObjects(("STONESOFT-IPS-MIB", "ipsGeneralInformationGroup"), ("STONESOFT-IPS-MIB", "ipsGeneralNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsCompliance1 = ipsCompliance1.setStatus('current')
ipsGeneralInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 1, 1)).setObjects(("STONESOFT-IPS-MIB", "ipsSoftwareVersion"), ("STONESOFT-IPS-MIB", "ipsSecurityPolicy"), ("STONESOFT-IPS-MIB", "ipsPolicyTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsGeneralInformationGroup = ipsGeneralInformationGroup.setStatus('current')
ipsGeneralNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 1, 2)).setObjects(("STONESOFT-IPS-MIB", "ipsPolicyInstall"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsGeneralNotificationsGroup = ipsGeneralNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("STONESOFT-IPS-MIB", ipsPolicyInstall=ipsPolicyInstall, ipsCompliance1=ipsCompliance1, stonesoftIPSMibModule=stonesoftIPSMibModule, ipsConformance=ipsConformance, ipsGroups=ipsGroups, ipsEventsV2=ipsEventsV2, ipsSecurityPolicy=ipsSecurityPolicy, ipsEvents=ipsEvents, ipsSoftwareVersion=ipsSoftwareVersion, ipsPolicyTime=ipsPolicyTime, ipsObjects=ipsObjects, ipsGeneralInformationGroup=ipsGeneralInformationGroup, ipsCompliances=ipsCompliances, ipsGeneralNotificationsGroup=ipsGeneralNotificationsGroup, PYSNMP_MODULE_ID=stonesoftIPSMibModule)
