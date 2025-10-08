#
# PySNMP MIB module COLUBRIS-TCP-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/colubris/COLUBRIS-TCP-SERIAL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisTCPSerialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 37))
if mibBuilder.loadTexts: colubrisTCPSerialMIB.setLastUpdated('200808210000Z')
if mibBuilder.loadTexts: colubrisTCPSerialMIB.setOrganization('Colubris Networks, Inc.')
colubrisTCPSerialMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1))
coTCPSerialStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1))
coTCPSerialConnectionStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("active", 3), ("idle", 4), ("connect", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialConnectionStatus.setStatus('current')
coTCPSerialRemoteIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialRemoteIPAddress.setStatus('current')
coTCPSerialRemoteTCPPort = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialRemoteTCPPort.setStatus('current')
coTCPSerialConnectTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialConnectTime.setStatus('current')
coTCPSerialTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 5), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialTxBytes.setStatus('current')
coTCPSerialRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 6), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialRxBytes.setStatus('current')
colubrisTCPSerialMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 2))
colubrisTCPSerialMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 2, 0))
colubrisTCPSerialMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3))
colubrisTCPSerialMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 1))
colubrisTCPSerialMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 2))
colubrisTCPSerialMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 1, 1)).setObjects(("COLUBRIS-TCP-SERIAL-MIB", "colubrisTCPSerialConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisTCPSerialMIBCompliance = colubrisTCPSerialMIBCompliance.setStatus('current')
colubrisTCPSerialConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 2, 1)).setObjects(("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialConnectionStatus"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRemoteIPAddress"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRemoteTCPPort"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialConnectTime"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialTxBytes"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRxBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisTCPSerialConfigMIBGroup = colubrisTCPSerialConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-TCP-SERIAL-MIB", coTCPSerialRemoteTCPPort=coTCPSerialRemoteTCPPort, colubrisTCPSerialMIBNotificationPrefix=colubrisTCPSerialMIBNotificationPrefix, colubrisTCPSerialMIBCompliance=colubrisTCPSerialMIBCompliance, colubrisTCPSerialMIBNotifications=colubrisTCPSerialMIBNotifications, colubrisTCPSerialConfigMIBGroup=colubrisTCPSerialConfigMIBGroup, coTCPSerialTxBytes=coTCPSerialTxBytes, colubrisTCPSerialMIBConformance=colubrisTCPSerialMIBConformance, coTCPSerialRxBytes=coTCPSerialRxBytes, coTCPSerialStatusGroup=coTCPSerialStatusGroup, colubrisTCPSerialMIBGroups=colubrisTCPSerialMIBGroups, colubrisTCPSerialMIB=colubrisTCPSerialMIB, colubrisTCPSerialMIBObjects=colubrisTCPSerialMIBObjects, coTCPSerialRemoteIPAddress=coTCPSerialRemoteIPAddress, coTCPSerialConnectionStatus=coTCPSerialConnectionStatus, colubrisTCPSerialMIBCompliances=colubrisTCPSerialMIBCompliances, PYSNMP_MODULE_ID=colubrisTCPSerialMIB, coTCPSerialConnectTime=coTCPSerialConnectTime)
