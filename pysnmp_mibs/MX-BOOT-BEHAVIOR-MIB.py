#
# PySNMP MIB module MX-BOOT-BEHAVIOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-BOOT-BEHAVIOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bootBehaviorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 70))
bootBehaviorMIB.setRevisions(('2004-08-12 00:00',))
if mibBuilder.loadTexts: bootBehaviorMIB.setLastUpdated('200408120000Z')
if mibBuilder.loadTexts: bootBehaviorMIB.setOrganization('Mediatrix Telecom, Inc.')
bootBehaviorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 70, 1))
bootBehaviorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 70, 2))
checkTcpIpStackForSuccessfulBoot = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 70, 1, 1), MxEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: checkTcpIpStackForSuccessfulBoot.setStatus('current')
bootBehaviorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 1))
bootBehaviorComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 1, 10)).setObjects(("MX-BOOT-BEHAVIOR-MIB", "bootBehaviorGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bootBehaviorComplVer1 = bootBehaviorComplVer1.setStatus('current')
bootBehaviorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 2))
bootBehaviorGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 2, 10)).setObjects(("MX-BOOT-BEHAVIOR-MIB", "checkTcpIpStackForSuccessfulBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bootBehaviorGroupVer1 = bootBehaviorGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-BOOT-BEHAVIOR-MIB", bootBehaviorCompliances=bootBehaviorCompliances, checkTcpIpStackForSuccessfulBoot=checkTcpIpStackForSuccessfulBoot, bootBehaviorGroupVer1=bootBehaviorGroupVer1, bootBehaviorMIBObjects=bootBehaviorMIBObjects, bootBehaviorGroups=bootBehaviorGroups, PYSNMP_MODULE_ID=bootBehaviorMIB, bootBehaviorMIB=bootBehaviorMIB, bootBehaviorConformance=bootBehaviorConformance, bootBehaviorComplVer1=bootBehaviorComplVer1)
