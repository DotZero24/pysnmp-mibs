#
# PySNMP MIB module STONESOFT-IPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/forcepoint/STONESOFT-IPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("STONESOFT-IPS-MIB", ipsSecurityPolicy=ipsSecurityPolicy, ipsPolicyTime=ipsPolicyTime, ipsEvents=ipsEvents, stonesoftIPSMibModule=stonesoftIPSMibModule, ipsCompliance1=ipsCompliance1, ipsGeneralNotificationsGroup=ipsGeneralNotificationsGroup, ipsCompliances=ipsCompliances, ipsConformance=ipsConformance, ipsGroups=ipsGroups, PYSNMP_MODULE_ID=stonesoftIPSMibModule, ipsGeneralInformationGroup=ipsGeneralInformationGroup, ipsPolicyInstall=ipsPolicyInstall, ipsEventsV2=ipsEventsV2, ipsSoftwareVersion=ipsSoftwareVersion, ipsObjects=ipsObjects)
