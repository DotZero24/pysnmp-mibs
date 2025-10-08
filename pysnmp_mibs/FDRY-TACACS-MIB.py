#
# PySNMP MIB module FDRY-TACACS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/FDRY-TACACS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ServerUsage, = mibBuilder.importSymbols("FDRY-RADIUS-MIB", "ServerUsage")
fdryTacacs, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryTacacs")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fdryTacacsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1))
fdryTacacsMIB.setRevisions(('2008-02-25 00:00', '2017-08-07 00:00',))
if mibBuilder.loadTexts: fdryTacacsMIB.setLastUpdated('201708070000Z')
if mibBuilder.loadTexts: fdryTacacsMIB.setOrganization('Ruckus Wireless, Inc..')
class InetAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

fdryTacacsServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1))
fdryTacacsServerTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1), )
if mibBuilder.loadTexts: fdryTacacsServerTable.setStatus('current')
fdryTacacsServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-TACACS-MIB", "fdryTacacsServerIndex"))
if mibBuilder.loadTexts: fdryTacacsServerEntry.setStatus('current')
fdryTacacsServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryTacacsServerIndex.setStatus('current')
fdryTacacsServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTacacsServerAddrType.setStatus('current')
fdryTacacsServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTacacsServerAddr.setStatus('current')
fdryTacacsServerAuthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 4), Unsigned32().clone(49)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTacacsServerAuthPort.setStatus('current')
fdryTacacsServerRowKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTacacsServerRowKey.setStatus('current')
fdryTacacsServerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 6), ServerUsage().clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTacacsServerUsage.setStatus('current')
fdryTacacsServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTacacsServerRowStatus.setStatus('current')
mibBuilder.exportSymbols("FDRY-TACACS-MIB", fdryTacacsServerAddrType=fdryTacacsServerAddrType, fdryTacacsServerIndex=fdryTacacsServerIndex, InetAddress=InetAddress, fdryTacacsServerTable=fdryTacacsServerTable, fdryTacacsServerRowStatus=fdryTacacsServerRowStatus, fdryTacacsServerAddr=fdryTacacsServerAddr, fdryTacacsServerAuthPort=fdryTacacsServerAuthPort, fdryTacacsServer=fdryTacacsServer, fdryTacacsServerRowKey=fdryTacacsServerRowKey, fdryTacacsMIB=fdryTacacsMIB, fdryTacacsServerEntry=fdryTacacsServerEntry, PYSNMP_MODULE_ID=fdryTacacsMIB, fdryTacacsServerUsage=fdryTacacsServerUsage)
