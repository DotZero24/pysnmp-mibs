#
# PySNMP MIB module ENTERASYS-NETFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-NETFLOW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-NETFLOW-MIB", etsysNetflowInterfaceMap=etsysNetflowInterfaceMap, etsysNetflowCompliances=etsysNetflowCompliances, etsysNetflowObjects=etsysNetflowObjects, etsysNetflowExportIntfMapEntry=etsysNetflowExportIntfMapEntry, etsysNetflowIntfMapCompliance=etsysNetflowIntfMapCompliance, etsysNetflowExportIntfMapTable=etsysNetflowExportIntfMapTable, etsysNetflowGroups=etsysNetflowGroups, etsysNetflowExportIntf=etsysNetflowExportIntf, etsysNetflowIfIndexMapTable=etsysNetflowIfIndexMapTable, etsysNetflowExportInterface=etsysNetflowExportInterface, etsysNetflowConformance=etsysNetflowConformance, etsysNetflowMIB=etsysNetflowMIB, PYSNMP_MODULE_ID=etsysNetflowMIB, etsysNetflowIfIndex=etsysNetflowIfIndex, etsysNetflowIntfMapGroup=etsysNetflowIntfMapGroup, etsysNetflowIfIndexMapEntry=etsysNetflowIfIndexMapEntry)
