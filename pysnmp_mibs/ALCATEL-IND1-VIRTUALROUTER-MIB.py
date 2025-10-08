#
# PySNMP MIB module ALCATEL-IND1-VIRTUALROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-VIRTUALROUTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
routingIND1Vrf, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Vrf")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1VirtualRouterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1))
alcatelIND1VirtualRouterMIB.setRevisions(('2008-03-17 00:00',))
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setOrganization('Alcatel-Lucent')
alcatelIND1VirtualRouterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1))
alaVirtualRouterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1))
alaVirtualRouterNameTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setStatus('current')
alaVirtualRouterNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"))
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setStatus('current')
alaVirtualRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: alaVirtualRouterName.setStatus('current')
alaVirtualRouterNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setStatus('current')
alaVirtualRouterNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setStatus('current')
alcatelIND1VirtualRouterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2))
alcatelIND1VirtualRouterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1))
alcatelIND1VirtualRouterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2))
alaVirtualRouterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterCompliance = alaVirtualRouterCompliance.setStatus('current')
alaVirtualRouterConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterConfigMIBGroup = alaVirtualRouterConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUALROUTER-MIB", alaVirtualRouterNameIndex=alaVirtualRouterNameIndex, alaVirtualRouterCompliance=alaVirtualRouterCompliance, alaVirtualRouterNameEntry=alaVirtualRouterNameEntry, alcatelIND1VirtualRouterMIBObjects=alcatelIND1VirtualRouterMIBObjects, alaVirtualRouterNameRowStatus=alaVirtualRouterNameRowStatus, alaVirtualRouterNameTable=alaVirtualRouterNameTable, alaVirtualRouterName=alaVirtualRouterName, alcatelIND1VirtualRouterMIB=alcatelIND1VirtualRouterMIB, PYSNMP_MODULE_ID=alcatelIND1VirtualRouterMIB, alcatelIND1VirtualRouterMIBCompliances=alcatelIND1VirtualRouterMIBCompliances, alaVirtualRouterConfig=alaVirtualRouterConfig, alcatelIND1VirtualRouterMIBConformance=alcatelIND1VirtualRouterMIBConformance, alaVirtualRouterConfigMIBGroup=alaVirtualRouterConfigMIBGroup, alcatelIND1VirtualRouterMIBGroups=alcatelIND1VirtualRouterMIBGroups)
