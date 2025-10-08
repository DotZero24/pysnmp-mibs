#
# PySNMP MIB module TRAPEZE-NETWORKS-QOS-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-QOS-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", trpzQosConfigMibObjects=trpzQosConfigMibObjects, trpzQosConfigCompliance=trpzQosConfigCompliance, trpzQosConfQosProfileConfigGroup=trpzQosConfQosProfileConfigGroup, trpzQosConfQosProfileConfigEntry=trpzQosConfQosProfileConfigEntry, trpzQosConfigCompliances=trpzQosConfigCompliances, trpzQosConfQosProfConfProfileName=trpzQosConfQosProfConfProfileName, trpzQosConfigConformance=trpzQosConfigConformance, PYSNMP_MODULE_ID=trpzQosConfigMib, trpzQosConfQosProfConfMaxBandwidthKbps=trpzQosConfQosProfConfMaxBandwidthKbps, trpzQosConfigGroups=trpzQosConfigGroups, trpzQosConfigMib=trpzQosConfigMib, trpzQosConfQosProfileConfigTable=trpzQosConfQosProfileConfigTable)
