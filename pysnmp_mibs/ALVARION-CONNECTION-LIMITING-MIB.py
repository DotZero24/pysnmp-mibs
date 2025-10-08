#
# PySNMP MIB module ALVARION-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alvarion/ALVARION-CONNECTION-LIMITING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alvarionConnectionLimitingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18))
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setOrganization('Alvarion Ltd.')
alvarionConnectionLimitingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1))
connectionLimitingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1))
connectionLimitingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2))
connectionLimitingMaximumUserConnections = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setStatus('current')
connectionLimitingMaximumSystemConnections = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setStatus('current')
alvarionConnectionLimitingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2))
alvarionConnectionLimitingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2, 0))
alvarionConnectionLimitingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3))
alvarionConnectionLimitingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1))
alvarionConnectionLimitingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2))
alvarionConnectionLimitingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1, 1)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "alvarionConnectionLimitingConfigMIBGroup"), ("ALVARION-CONNECTION-LIMITING-MIB", "alvarionConnectionLimitingInfoMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingMIBCompliance = alvarionConnectionLimitingMIBCompliance.setStatus('current')
alvarionConnectionLimitingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 1)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingConfigMIBGroup = alvarionConnectionLimitingConfigMIBGroup.setStatus('current')
alvarionConnectionLimitingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 2)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingInfoMIBGroup = alvarionConnectionLimitingInfoMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-CONNECTION-LIMITING-MIB", alvarionConnectionLimitingMIBConformance=alvarionConnectionLimitingMIBConformance, alvarionConnectionLimitingMIBGroups=alvarionConnectionLimitingMIBGroups, alvarionConnectionLimitingMIBNotificationPrefix=alvarionConnectionLimitingMIBNotificationPrefix, alvarionConnectionLimitingMIBNotifications=alvarionConnectionLimitingMIBNotifications, alvarionConnectionLimitingConfigMIBGroup=alvarionConnectionLimitingConfigMIBGroup, alvarionConnectionLimitingMIBCompliances=alvarionConnectionLimitingMIBCompliances, alvarionConnectionLimitingMIBObjects=alvarionConnectionLimitingMIBObjects, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections, connectionLimitingInfo=connectionLimitingInfo, PYSNMP_MODULE_ID=alvarionConnectionLimitingMIB, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, alvarionConnectionLimitingMIB=alvarionConnectionLimitingMIB, connectionLimitingConfig=connectionLimitingConfig, alvarionConnectionLimitingMIBCompliance=alvarionConnectionLimitingMIBCompliance, alvarionConnectionLimitingInfoMIBGroup=alvarionConnectionLimitingInfoMIBGroup)
