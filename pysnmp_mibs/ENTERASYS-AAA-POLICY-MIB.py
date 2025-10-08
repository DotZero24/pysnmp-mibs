#
# PySNMP MIB module ENTERASYS-AAA-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-AAA-POLICY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysAAAPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51))
etsysAAAPolicyMIB.setRevisions(('2004-07-29 19:06',))
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setLastUpdated('200407291906Z')
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setOrganization('Enterasys Networks, Inc')
class AAAProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("any", 1), ("none", 2), ("radius", 3), ("tacacs", 4))

etsysAAAPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1))
etsysAAAPolicyMgmtAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1))
etsysAAAMgmtAccessTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1), )
if mibBuilder.loadTexts: etsysAAAMgmtAccessTable.setStatus('current')
etsysAAAMgmtAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtAccessProtocol"))
if mibBuilder.loadTexts: etsysAAAMgmtAccessEntry.setStatus('current')
etsysAAAMgmtAccessProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("allProtocols", 1))))
if mibBuilder.loadTexts: etsysAAAMgmtAccessProtocol.setStatus('current')
etsysAAAMgmtRemoteAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 2), AAAProtocol().clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAuthProtocol.setStatus('current')
etsysAAAMgmtRemoteAcctProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 3), AAAProtocol().clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAcctProtocol.setStatus('current')
etsysAAAPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2))
etsysAAAPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1))
etsysAAAPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2))
etsysAAAPolicyMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2, 1)).setObjects(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAuthProtocol"), ("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAcctProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAAAPolicyMgmtGroup = etsysAAAPolicyMgmtGroup.setStatus('current')
etsysAAAPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1, 1)).setObjects(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAPolicyMgmtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAAAPolicyMIBCompliance = etsysAAAPolicyMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-AAA-POLICY-MIB", etsysAAAPolicyMgmtGroup=etsysAAAPolicyMgmtGroup, etsysAAAPolicyMIBCompliances=etsysAAAPolicyMIBCompliances, AAAProtocol=AAAProtocol, etsysAAAPolicyMIBCompliance=etsysAAAPolicyMIBCompliance, etsysAAAMgmtAccessTable=etsysAAAMgmtAccessTable, etsysAAAMgmtAccessProtocol=etsysAAAMgmtAccessProtocol, PYSNMP_MODULE_ID=etsysAAAPolicyMIB, etsysAAAMgmtRemoteAcctProtocol=etsysAAAMgmtRemoteAcctProtocol, etsysAAAPolicyObjects=etsysAAAPolicyObjects, etsysAAAMgmtAccessEntry=etsysAAAMgmtAccessEntry, etsysAAAPolicyMgmtAccess=etsysAAAPolicyMgmtAccess, etsysAAAPolicyMIBConformance=etsysAAAPolicyMIBConformance, etsysAAAPolicyMIB=etsysAAAPolicyMIB, etsysAAAMgmtRemoteAuthProtocol=etsysAAAMgmtRemoteAuthProtocol, etsysAAAPolicyMIBGroups=etsysAAAPolicyMIBGroups)
