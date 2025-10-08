#
# PySNMP MIB module MX-BOOT-BEHAVIOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-BOOT-BEHAVIOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MX-BOOT-BEHAVIOR-MIB", bootBehaviorMIB=bootBehaviorMIB, checkTcpIpStackForSuccessfulBoot=checkTcpIpStackForSuccessfulBoot, bootBehaviorCompliances=bootBehaviorCompliances, bootBehaviorGroupVer1=bootBehaviorGroupVer1, bootBehaviorGroups=bootBehaviorGroups, PYSNMP_MODULE_ID=bootBehaviorMIB, bootBehaviorConformance=bootBehaviorConformance, bootBehaviorMIBObjects=bootBehaviorMIBObjects, bootBehaviorComplVer1=bootBehaviorComplVer1)
