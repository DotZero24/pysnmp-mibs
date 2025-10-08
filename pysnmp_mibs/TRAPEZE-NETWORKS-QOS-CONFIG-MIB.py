#
# PySNMP MIB module TRAPEZE-NETWORKS-QOS-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-QOS-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzQosConfigMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 20))
trpzQosConfigMib.setRevisions(('2011-02-24 00:11',))
if mibBuilder.loadTexts: trpzQosConfigMib.setLastUpdated('201102240011Z')
if mibBuilder.loadTexts: trpzQosConfigMib.setOrganization('Trapeze Networks')
trpzQosConfigMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1))
trpzQosConfQosProfileConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1), )
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigTable.setStatus('current')
trpzQosConfQosProfileConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfProfileName"))
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigEntry.setStatus('current')
trpzQosConfQosProfConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: trpzQosConfQosProfConfProfileName.setStatus('current')
trpzQosConfQosProfConfMaxBandwidthKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trpzQosConfQosProfConfMaxBandwidthKbps.setStatus('current')
trpzQosConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2))
trpzQosConfigCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1))
trpzQosConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2))
trpzQosConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfileConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzQosConfigCompliance = trpzQosConfigCompliance.setStatus('current')
trpzQosConfQosProfileConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfMaxBandwidthKbps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzQosConfQosProfileConfigGroup = trpzQosConfQosProfileConfigGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", trpzQosConfQosProfileConfigEntry=trpzQosConfQosProfileConfigEntry, trpzQosConfQosProfileConfigGroup=trpzQosConfQosProfileConfigGroup, trpzQosConfigGroups=trpzQosConfigGroups, trpzQosConfigMib=trpzQosConfigMib, PYSNMP_MODULE_ID=trpzQosConfigMib, trpzQosConfQosProfConfProfileName=trpzQosConfQosProfConfProfileName, trpzQosConfigCompliances=trpzQosConfigCompliances, trpzQosConfigMibObjects=trpzQosConfigMibObjects, trpzQosConfigCompliance=trpzQosConfigCompliance, trpzQosConfigConformance=trpzQosConfigConformance, trpzQosConfQosProfConfMaxBandwidthKbps=trpzQosConfQosProfConfMaxBandwidthKbps, trpzQosConfQosProfileConfigTable=trpzQosConfQosProfileConfigTable)
