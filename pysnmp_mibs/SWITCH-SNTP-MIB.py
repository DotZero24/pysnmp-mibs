#
# PySNMP MIB module SWITCH-SNTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/SWITCH-SNTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SWITCH-SNTP-MIB", rcSntpServerBroadcastAddress=rcSntpServerBroadcastAddress, PYSNMP_MODULE_ID=rcSntp, rcSntpClient=rcSntpClient, rcSntp=rcSntp, rcSntpServerSendInterval=rcSntpServerSendInterval, rcSntpClientAddress=rcSntpClientAddress, rcSntpServer=rcSntpServer, rcSntpServerEnable=rcSntpServerEnable, rcSntpClientListenEnable=rcSntpClientListenEnable, rcSntpClientGet=rcSntpClientGet)
