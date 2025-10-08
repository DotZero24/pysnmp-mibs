#
# PySNMP MIB module ENTERASYS-NETFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-NETFLOW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysNetflowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61))
etsysNetflowMIB.setRevisions(('2007-02-07 19:49', '2006-03-22 21:36',))
if mibBuilder.loadTexts: etsysNetflowMIB.setLastUpdated('200702071949Z')
if mibBuilder.loadTexts: etsysNetflowMIB.setOrganization('Enterasys Networks, Inc.')
etsysNetflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1))
etsysNetflowInterfaceMap = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1))
etsysNetflowExportIntfMapTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1), )
if mibBuilder.loadTexts: etsysNetflowExportIntfMapTable.setStatus('current')
etsysNetflowExportIntfMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-NETFLOW-MIB", "etsysNetflowExportIntf"))
if mibBuilder.loadTexts: etsysNetflowExportIntfMapEntry.setStatus('current')
etsysNetflowExportIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: etsysNetflowExportIntf.setStatus('current')
etsysNetflowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysNetflowIfIndex.setStatus('current')
etsysNetflowIfIndexMapTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2), )
if mibBuilder.loadTexts: etsysNetflowIfIndexMapTable.setStatus('current')
etsysNetflowIfIndexMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysNetflowIfIndexMapEntry.setStatus('current')
etsysNetflowExportInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysNetflowExportInterface.setStatus('current')
etsysNetflowConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2))
etsysNetflowGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 1))
etsysNetflowCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 2))
etsysNetflowIntfMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 1, 1)).setObjects(("ENTERASYS-NETFLOW-MIB", "etsysNetflowExportIntf"), ("ENTERASYS-NETFLOW-MIB", "etsysNetflowIfIndex"), ("ENTERASYS-NETFLOW-MIB", "etsysNetflowExportInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysNetflowIntfMapGroup = etsysNetflowIntfMapGroup.setStatus('current')
etsysNetflowIntfMapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 2, 1)).setObjects(("ENTERASYS-NETFLOW-MIB", "etsysNetflowIntfMapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysNetflowIntfMapCompliance = etsysNetflowIntfMapCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-NETFLOW-MIB", etsysNetflowIfIndexMapEntry=etsysNetflowIfIndexMapEntry, etsysNetflowIfIndexMapTable=etsysNetflowIfIndexMapTable, PYSNMP_MODULE_ID=etsysNetflowMIB, etsysNetflowMIB=etsysNetflowMIB, etsysNetflowExportIntf=etsysNetflowExportIntf, etsysNetflowInterfaceMap=etsysNetflowInterfaceMap, etsysNetflowIfIndex=etsysNetflowIfIndex, etsysNetflowExportIntfMapTable=etsysNetflowExportIntfMapTable, etsysNetflowExportInterface=etsysNetflowExportInterface, etsysNetflowGroups=etsysNetflowGroups, etsysNetflowIntfMapCompliance=etsysNetflowIntfMapCompliance, etsysNetflowObjects=etsysNetflowObjects, etsysNetflowExportIntfMapEntry=etsysNetflowExportIntfMapEntry, etsysNetflowConformance=etsysNetflowConformance, etsysNetflowIntfMapGroup=etsysNetflowIntfMapGroup, etsysNetflowCompliances=etsysNetflowCompliances)
