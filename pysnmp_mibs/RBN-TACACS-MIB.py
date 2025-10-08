#
# PySNMP MIB module RBN-TACACS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-TACACS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnTacacsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 33))
rbnTacacsMib.setRevisions(('2004-03-01 18:00',))
if mibBuilder.loadTexts: rbnTacacsMib.setLastUpdated('200403011800Z')
if mibBuilder.loadTexts: rbnTacacsMib.setOrganization('RedBack Networks, Inc.')
rbnTacacsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 0))
rbnTacacsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1))
rbnTacacsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2))
rbnTacacsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 1))
rbnTacacsAcctObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 2))
rbnTacacsNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3))
class RbnTacacsState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("up", 2), ("down", 3))

class RbnTacacsReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("responding", 1), ("packetTimeout", 2), ("serverTimeout", 3), ("serverError", 4))

rbnTacacsContext = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsContext.setStatus('current')
rbnTacacsServerIndex = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerIndex.setStatus('current')
rbnTacacsServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerAddressType.setStatus('current')
rbnTacacsServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerAddress.setStatus('current')
rbnTacacsServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerPort.setStatus('current')
rbnTacacsServerState = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 6), RbnTacacsState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerState.setStatus('current')
rbnTacacsServerReason = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 7), RbnTacacsReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerReason.setStatus('current')
rbnTacacsUserName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsUserName.setStatus('current')
rbnTacacsServerMsg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerMsg.setStatus('current')
rbnTacacsStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 33, 0, 1)).setObjects(("RBN-TACACS-MIB", "rbnTacacsContext"), ("RBN-TACACS-MIB", "rbnTacacsServerIndex"), ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"), ("RBN-TACACS-MIB", "rbnTacacsServerAddress"), ("RBN-TACACS-MIB", "rbnTacacsServerPort"), ("RBN-TACACS-MIB", "rbnTacacsServerState"), ("RBN-TACACS-MIB", "rbnTacacsServerReason"), ("RBN-TACACS-MIB", "rbnTacacsUserName"), ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
if mibBuilder.loadTexts: rbnTacacsStateChange.setStatus('current')
rbnTacacsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1))
rbnTacacsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2))
rbnTacacsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1, 1)).setObjects(("RBN-TACACS-MIB", "rbnTacacsNotifyObjectsGroup"), ("RBN-TACACS-MIB", "rbnTacacsNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsCompliance = rbnTacacsCompliance.setStatus('current')
rbnTacacsNotifyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 2)).setObjects(("RBN-TACACS-MIB", "rbnTacacsContext"), ("RBN-TACACS-MIB", "rbnTacacsServerIndex"), ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"), ("RBN-TACACS-MIB", "rbnTacacsServerAddress"), ("RBN-TACACS-MIB", "rbnTacacsServerPort"), ("RBN-TACACS-MIB", "rbnTacacsServerState"), ("RBN-TACACS-MIB", "rbnTacacsServerReason"), ("RBN-TACACS-MIB", "rbnTacacsUserName"), ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsNotifyObjectsGroup = rbnTacacsNotifyObjectsGroup.setStatus('current')
rbnTacacsNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 3)).setObjects(("RBN-TACACS-MIB", "rbnTacacsStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsNotifyGroup = rbnTacacsNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-TACACS-MIB", rbnTacacsNotifyGroup=rbnTacacsNotifyGroup, rbnTacacsNotifyObjectsGroup=rbnTacacsNotifyObjectsGroup, rbnTacacsMIBNotifications=rbnTacacsMIBNotifications, rbnTacacsUserName=rbnTacacsUserName, rbnTacacsStateChange=rbnTacacsStateChange, rbnTacacsServerReason=rbnTacacsServerReason, rbnTacacsServerIndex=rbnTacacsServerIndex, rbnTacacsGroups=rbnTacacsGroups, RbnTacacsState=RbnTacacsState, rbnTacacsServerMsg=rbnTacacsServerMsg, rbnTacacsNotifyObjects=rbnTacacsNotifyObjects, rbnTacacsServerAddress=rbnTacacsServerAddress, rbnTacacsServerAddressType=rbnTacacsServerAddressType, rbnTacacsMIBConformance=rbnTacacsMIBConformance, rbnTacacsServerPort=rbnTacacsServerPort, rbnTacacsObjects=rbnTacacsObjects, rbnTacacsCompliances=rbnTacacsCompliances, rbnTacacsAcctObjects=rbnTacacsAcctObjects, RbnTacacsReason=RbnTacacsReason, PYSNMP_MODULE_ID=rbnTacacsMib, rbnTacacsMIBObjects=rbnTacacsMIBObjects, rbnTacacsMib=rbnTacacsMib, rbnTacacsServerState=rbnTacacsServerState, rbnTacacsContext=rbnTacacsContext, rbnTacacsCompliance=rbnTacacsCompliance)
