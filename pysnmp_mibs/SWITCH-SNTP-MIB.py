#
# PySNMP MIB module SWITCH-SNTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/SWITCH-SNTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
EnableVar, = mibBuilder.importSymbols("SWITCH-TC", "EnableVar")
rcSntp = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8))
rcSntp.setRevisions(('1904-12-20 00:00',))
if mibBuilder.loadTexts: rcSntp.setLastUpdated('0412200000Z')
if mibBuilder.loadTexts: rcSntp.setOrganization('Raisecom Science & Technology Co., ltd')
rcSntpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1))
rcSntpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2))
rcSntpServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1, 1), EnableVar().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcSntpServerEnable.setStatus('current')
rcSntpServerBroadcastAddress = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcSntpServerBroadcastAddress.setStatus('current')
rcSntpServerSendInterval = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcSntpServerSendInterval.setStatus('current')
rcSntpClientAddress = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcSntpClientAddress.setStatus('current')
rcSntpClientGet = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("get", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcSntpClientGet.setStatus('current')
rcSntpClientListenEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2, 3), EnableVar().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcSntpClientListenEnable.setStatus('current')
mibBuilder.exportSymbols("SWITCH-SNTP-MIB", rcSntpServerEnable=rcSntpServerEnable, rcSntpServerSendInterval=rcSntpServerSendInterval, rcSntpClientGet=rcSntpClientGet, rcSntpServerBroadcastAddress=rcSntpServerBroadcastAddress, PYSNMP_MODULE_ID=rcSntp, rcSntpClient=rcSntpClient, rcSntpClientAddress=rcSntpClientAddress, rcSntp=rcSntp, rcSntpServer=rcSntpServer, rcSntpClientListenEnable=rcSntpClientListenEnable)
