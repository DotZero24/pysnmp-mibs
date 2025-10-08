#
# PySNMP MIB module SYNOLOGY-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-SERVICES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synologyService = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 6))
synologyService.setRevisions(('2016-05-27 00:00',))
if mibBuilder.loadTexts: synologyService.setLastUpdated('201605270000Z')
if mibBuilder.loadTexts: synologyService.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
serviceTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 6, 1), )
if mibBuilder.loadTexts: serviceTable.setStatus('current')
serviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1), ).setIndexNames((0, "SYNOLOGY-SERVICES-MIB", "serviceInfoIndex"))
if mibBuilder.loadTexts: serviceEntry.setStatus('current')
serviceInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: serviceInfoIndex.setStatus('current')
serviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceName.setStatus('current')
serviceUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceUsers.setStatus('current')
synologyServiceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 6, 2))
synologyServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 6, 2, 1))
synologyServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 6, 2, 2))
synologyServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 6, 2, 1, 1)).setObjects(("SYNOLOGY-SERVICES-MIB", "synologyServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyServiceCompliance = synologyServiceCompliance.setStatus('current')
synologyServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 6, 2, 2, 1)).setObjects(("SYNOLOGY-SERVICES-MIB", "serviceName"), ("SYNOLOGY-SERVICES-MIB", "serviceUsers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyServiceGroup = synologyServiceGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-SERVICES-MIB", synologyServiceCompliance=synologyServiceCompliance, serviceEntry=serviceEntry, synology=synology, serviceTable=serviceTable, serviceUsers=serviceUsers, PYSNMP_MODULE_ID=synologyService, synologyService=synologyService, serviceInfoIndex=serviceInfoIndex, synologyServiceConformance=synologyServiceConformance, synologyServiceGroup=synologyServiceGroup, serviceName=serviceName, synologyServiceCompliances=synologyServiceCompliances, synologyServiceGroups=synologyServiceGroups)
