#
# PySNMP MIB module SYNOLOGY-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-SERVICES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SYNOLOGY-SERVICES-MIB", serviceTable=serviceTable, synologyServiceCompliance=synologyServiceCompliance, PYSNMP_MODULE_ID=synologyService, synologyService=synologyService, serviceName=serviceName, serviceUsers=serviceUsers, serviceInfoIndex=serviceInfoIndex, synologyServiceCompliances=synologyServiceCompliances, synologyServiceGroups=synologyServiceGroups, serviceEntry=serviceEntry, synologyServiceGroup=synologyServiceGroup, synology=synology, synologyServiceConformance=synologyServiceConformance)
