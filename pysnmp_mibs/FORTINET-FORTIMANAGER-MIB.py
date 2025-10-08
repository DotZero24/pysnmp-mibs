#
# PySNMP MIB module FORTINET-FORTIMANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fortinet/FORTINET-FORTIMANAGER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fortinet, fnSysSerial = mibBuilder.importSymbols("FORTINET-CORE-MIB", "fortinet", "fnSysSerial")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fnFortiManagerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356, 103))
fnFortiManagerMib.setRevisions(('2008-07-18 00:00', '2008-06-26 00:00', '2008-06-16 00:00', '2008-06-10 00:00',))
if mibBuilder.loadTexts: fnFortiManagerMib.setLastUpdated('200807180000Z')
if mibBuilder.loadTexts: fnFortiManagerMib.setOrganization('Fortinet Technologies, Inc.')
fmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 0))
fmTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 0, 0))
fmTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 0, 1))
fmModel = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1))
fmg100 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 1000))
fmg400 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 4000))
fmg400A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 4001))
fmg2000XL = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 20000))
fmg3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 30000))
fmg3000B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 30002))
fmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 10))
fmTrapHASwitch = NotificationType((1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 401)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fmTrapHASwitch.setStatus('current')
fmTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 103, 10, 1)).setObjects(("FORTINET-FORTIMANAGER-MIB", "fmTrapHASwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmTrapsComplianceGroup = fmTrapsComplianceGroup.setStatus('current')
fmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 103, 10, 100)).setObjects(("FORTINET-FORTIMANAGER-MIB", "fmTrapsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmMIBCompliance = fmMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("FORTINET-FORTIMANAGER-MIB", fmMIBConformance=fmMIBConformance, fmg400A=fmg400A, fmg3000B=fmg3000B, fmModel=fmModel, fmg100=fmg100, fmg3000=fmg3000, PYSNMP_MODULE_ID=fnFortiManagerMib, fnFortiManagerMib=fnFortiManagerMib, fmMIBCompliance=fmMIBCompliance, fmg2000XL=fmg2000XL, fmTrapHASwitch=fmTrapHASwitch, fmg400=fmg400, fmTrapObject=fmTrapObject, fmTrapPrefix=fmTrapPrefix, fmTrapsComplianceGroup=fmTrapsComplianceGroup, fmTraps=fmTraps)
