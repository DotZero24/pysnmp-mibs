#
# PySNMP MIB module BASIS-ONLINE-DIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/BASIS-ONLINE-DIAG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisOnlineDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 80))
basisOnlineDiagMIB.setRevisions(('2003-06-11 00:00',))
if mibBuilder.loadTexts: basisOnlineDiagMIB.setLastUpdated('200306110000Z')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setOrganization('Cisco Systems, Inc.')
onlineDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 3))
diagType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("post", 1), ("onlinediag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagType.setStatus('current')
diagResult = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagResult.setStatus('current')
diagTestId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagTestId.setStatus('current')
boDiagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2))
boDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1))
boDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2))
boDiagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "boDiagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagCompliance = boDiagCompliance.setStatus('current')
boDiagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "diagType"), ("BASIS-ONLINE-DIAG-MIB", "diagResult"), ("BASIS-ONLINE-DIAG-MIB", "diagTestId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagGroup = boDiagGroup.setStatus('current')
mibBuilder.exportSymbols("BASIS-ONLINE-DIAG-MIB", boDiagMIBGroups=boDiagMIBGroups, diagType=diagType, onlineDiagnostics=onlineDiagnostics, basisOnlineDiagMIB=basisOnlineDiagMIB, PYSNMP_MODULE_ID=basisOnlineDiagMIB, boDiagMIBCompliances=boDiagMIBCompliances, boDiagGroup=boDiagGroup, boDiagMIBConformance=boDiagMIBConformance, boDiagCompliance=boDiagCompliance, diagTestId=diagTestId, diagResult=diagResult)
