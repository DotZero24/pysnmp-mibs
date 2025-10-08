#
# PySNMP MIB module COLUBRIS-TCP-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/colubris/COLUBRIS-TCP-SERIAL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("COLUBRIS-TCP-SERIAL-MIB", colubrisTCPSerialMIB=colubrisTCPSerialMIB, PYSNMP_MODULE_ID=colubrisTCPSerialMIB, coTCPSerialRxBytes=coTCPSerialRxBytes, coTCPSerialConnectionStatus=coTCPSerialConnectionStatus, colubrisTCPSerialMIBCompliances=colubrisTCPSerialMIBCompliances, coTCPSerialTxBytes=coTCPSerialTxBytes, coTCPSerialRemoteTCPPort=coTCPSerialRemoteTCPPort, colubrisTCPSerialMIBGroups=colubrisTCPSerialMIBGroups, coTCPSerialRemoteIPAddress=coTCPSerialRemoteIPAddress, colubrisTCPSerialMIBNotifications=colubrisTCPSerialMIBNotifications, colubrisTCPSerialMIBNotificationPrefix=colubrisTCPSerialMIBNotificationPrefix, colubrisTCPSerialConfigMIBGroup=colubrisTCPSerialConfigMIBGroup, colubrisTCPSerialMIBObjects=colubrisTCPSerialMIBObjects, colubrisTCPSerialMIBCompliance=colubrisTCPSerialMIBCompliance, coTCPSerialStatusGroup=coTCPSerialStatusGroup, colubrisTCPSerialMIBConformance=colubrisTCPSerialMIBConformance, coTCPSerialConnectTime=coTCPSerialConnectTime)
