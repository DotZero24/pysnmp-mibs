#
# PySNMP MIB module ALVARION-BANDWIDTH-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alvarion/ALVARION-BANDWIDTH-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionPriorityQueue, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionPriorityQueue")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
alvarionBandwidthControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14))
if mibBuilder.loadTexts: alvarionBandwidthControlMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionBandwidthControlMIB.setOrganization('Alvarion Ltd.')
alvarionBandwidthControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1))
coBandwidthControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1))
coBandwidthControlEnable = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlEnable.setStatus('current')
coBandwidthControlMaxTransmitRate = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxTransmitRate.setStatus('current')
coBandwidthControlMaxReceiveRate = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxReceiveRate.setStatus('current')
coBandwidthControlLevelTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4), )
if mibBuilder.loadTexts: coBandwidthControlLevelTable.setStatus('current')
coBandwidthControlLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1), ).setIndexNames((0, "ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelIndex"))
if mibBuilder.loadTexts: coBandwidthControlLevelEntry.setStatus('current')
coBandwidthControlLevelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 1), AlvarionPriorityQueue())
if mibBuilder.loadTexts: coBandwidthControlLevelIndex.setStatus('current')
coBandwidthControlLevelMinTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinTransmitRate.setStatus('current')
coBandwidthControlLevelMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxTransmitRate.setStatus('current')
coBandwidthControlLevelMinReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinReceiveRate.setStatus('current')
coBandwidthControlLevelMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxReceiveRate.setStatus('current')
alvarionBandwidthControlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2))
alvarionBandwidthControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 1))
alvarionBandwidthControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 2))
alvarionBandwidthControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 1, 1)).setObjects(("ALVARION-BANDWIDTH-CONTROL-MIB", "alvarionBandwidthControlMIBGroup"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "alvarionBandwidthControlLevelMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionBandwidthControlMIBCompliance = alvarionBandwidthControlMIBCompliance.setStatus('current')
alvarionBandwidthControlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 2, 1)).setObjects(("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlEnable"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxTransmitRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionBandwidthControlMIBGroup = alvarionBandwidthControlMIBGroup.setStatus('current')
alvarionBandwidthControlLevelMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 2, 2)).setObjects(("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinTransmitRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxTransmitRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinReceiveRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionBandwidthControlLevelMIBGroup = alvarionBandwidthControlLevelMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-BANDWIDTH-CONTROL-MIB", alvarionBandwidthControlMIBGroups=alvarionBandwidthControlMIBGroups, alvarionBandwidthControlLevelMIBGroup=alvarionBandwidthControlLevelMIBGroup, coBandwidthControlLevelMinTransmitRate=coBandwidthControlLevelMinTransmitRate, alvarionBandwidthControlMIBObjects=alvarionBandwidthControlMIBObjects, coBandwidthControlConfig=coBandwidthControlConfig, coBandwidthControlLevelMaxReceiveRate=coBandwidthControlLevelMaxReceiveRate, PYSNMP_MODULE_ID=alvarionBandwidthControlMIB, coBandwidthControlEnable=coBandwidthControlEnable, coBandwidthControlMaxTransmitRate=coBandwidthControlMaxTransmitRate, coBandwidthControlLevelMaxTransmitRate=coBandwidthControlLevelMaxTransmitRate, coBandwidthControlMaxReceiveRate=coBandwidthControlMaxReceiveRate, coBandwidthControlLevelIndex=coBandwidthControlLevelIndex, coBandwidthControlLevelTable=coBandwidthControlLevelTable, alvarionBandwidthControlMIBCompliance=alvarionBandwidthControlMIBCompliance, coBandwidthControlLevelMinReceiveRate=coBandwidthControlLevelMinReceiveRate, alvarionBandwidthControlMIBCompliances=alvarionBandwidthControlMIBCompliances, coBandwidthControlLevelEntry=coBandwidthControlLevelEntry, alvarionBandwidthControlMIB=alvarionBandwidthControlMIB, alvarionBandwidthControlMIBConformance=alvarionBandwidthControlMIBConformance, alvarionBandwidthControlMIBGroup=alvarionBandwidthControlMIBGroup)
