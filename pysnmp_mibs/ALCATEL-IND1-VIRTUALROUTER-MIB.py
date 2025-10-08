#
# PySNMP MIB module ALCATEL-IND1-VIRTUALROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-VIRTUALROUTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
routingIND1Vrf, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Vrf")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUALROUTER-MIB", alaVirtualRouterNameIndex=alaVirtualRouterNameIndex, alcatelIND1VirtualRouterMIBCompliances=alcatelIND1VirtualRouterMIBCompliances, alaVirtualRouterNameTable=alaVirtualRouterNameTable, alaVirtualRouterName=alaVirtualRouterName, alaVirtualRouterNameEntry=alaVirtualRouterNameEntry, alaVirtualRouterCompliance=alaVirtualRouterCompliance, PYSNMP_MODULE_ID=alcatelIND1VirtualRouterMIB, alaVirtualRouterConfig=alaVirtualRouterConfig, alcatelIND1VirtualRouterMIBObjects=alcatelIND1VirtualRouterMIBObjects, alaVirtualRouterNameRowStatus=alaVirtualRouterNameRowStatus, alcatelIND1VirtualRouterMIBConformance=alcatelIND1VirtualRouterMIBConformance, alcatelIND1VirtualRouterMIBGroups=alcatelIND1VirtualRouterMIBGroups, alaVirtualRouterConfigMIBGroup=alaVirtualRouterConfigMIBGroup, alcatelIND1VirtualRouterMIB=alcatelIND1VirtualRouterMIB)
