#
# PySNMP MIB module ALVARION-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alvarion/ALVARION-CONNECTION-LIMITING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALVARION-CONNECTION-LIMITING-MIB", alvarionConnectionLimitingMIBNotifications=alvarionConnectionLimitingMIBNotifications, alvarionConnectionLimitingInfoMIBGroup=alvarionConnectionLimitingInfoMIBGroup, alvarionConnectionLimitingConfigMIBGroup=alvarionConnectionLimitingConfigMIBGroup, alvarionConnectionLimitingMIBGroups=alvarionConnectionLimitingMIBGroups, connectionLimitingInfo=connectionLimitingInfo, alvarionConnectionLimitingMIBCompliance=alvarionConnectionLimitingMIBCompliance, alvarionConnectionLimitingMIB=alvarionConnectionLimitingMIB, alvarionConnectionLimitingMIBConformance=alvarionConnectionLimitingMIBConformance, PYSNMP_MODULE_ID=alvarionConnectionLimitingMIB, alvarionConnectionLimitingMIBCompliances=alvarionConnectionLimitingMIBCompliances, alvarionConnectionLimitingMIBNotificationPrefix=alvarionConnectionLimitingMIBNotificationPrefix, alvarionConnectionLimitingMIBObjects=alvarionConnectionLimitingMIBObjects, connectionLimitingConfig=connectionLimitingConfig, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections)
