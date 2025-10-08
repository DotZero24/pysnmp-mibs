#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-L2L3-INTERFACE-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 151))
ciscoL2L3IfConfigMIB.setRevisions(('2000-05-10 19:00',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setLastUpdated('200005101900Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setOrganization('Cisco Systems, Inc.')
ciscoL2L3IfConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1))
cL2L3IfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1))
class CL2L3InterfaceMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("routed", 1), ("switchport", 2))

cL2L3IfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1), )
if mibBuilder.loadTexts: cL2L3IfTable.setStatus('current')
cL2L3IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cL2L3IfEntry.setStatus('current')
cL2L3IfModeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 1), CL2L3InterfaceMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cL2L3IfModeAdmin.setStatus('current')
cL2L3IfModeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 2), CL2L3InterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cL2L3IfModeOper.setStatus('current')
ciscoL2L3IfConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3))
ciscoL2L3IfConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1))
ciscoL2L3IfConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2))
ciscoL2L3IfConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "ciscoL2L3IfConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBCompliance = ciscoL2L3IfConfigMIBCompliance.setStatus('current')
ciscoL2L3IfConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeAdmin"), ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBGroup = ciscoL2L3IfConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-MIB", cL2L3IfConfig=cL2L3IfConfig, cL2L3IfModeOper=cL2L3IfModeOper, ciscoL2L3IfConfigMIBCompliances=ciscoL2L3IfConfigMIBCompliances, ciscoL2L3IfConfigMIB=ciscoL2L3IfConfigMIB, cL2L3IfTable=cL2L3IfTable, ciscoL2L3IfConfigMIBGroups=ciscoL2L3IfConfigMIBGroups, ciscoL2L3IfConfigMIBGroup=ciscoL2L3IfConfigMIBGroup, cL2L3IfEntry=cL2L3IfEntry, cL2L3IfModeAdmin=cL2L3IfModeAdmin, ciscoL2L3IfConfigMIBCompliance=ciscoL2L3IfConfigMIBCompliance, ciscoL2L3IfConfigMIBObjects=ciscoL2L3IfConfigMIBObjects, PYSNMP_MODULE_ID=ciscoL2L3IfConfigMIB, CL2L3InterfaceMode=CL2L3InterfaceMode, ciscoL2L3IfConfigMIBConformance=ciscoL2L3IfConfigMIBConformance)
