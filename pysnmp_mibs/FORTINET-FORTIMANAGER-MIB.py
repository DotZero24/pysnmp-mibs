#
# PySNMP MIB module FORTINET-FORTIMANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fortinet/FORTINET-FORTIMANAGER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fnSysSerial, fortinet = mibBuilder.importSymbols("FORTINET-CORE-MIB", "fnSysSerial", "fortinet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FORTINET-FORTIMANAGER-MIB", PYSNMP_MODULE_ID=fnFortiManagerMib, fmTrapObject=fmTrapObject, fmTrapsComplianceGroup=fmTrapsComplianceGroup, fmg400A=fmg400A, fmMIBCompliance=fmMIBCompliance, fmModel=fmModel, fmTrapHASwitch=fmTrapHASwitch, fmTrapPrefix=fmTrapPrefix, fmg2000XL=fmg2000XL, fmg100=fmg100, fmg3000=fmg3000, fmg3000B=fmg3000B, fmMIBConformance=fmMIBConformance, fmTraps=fmTraps, fnFortiManagerMib=fnFortiManagerMib, fmg400=fmg400)
