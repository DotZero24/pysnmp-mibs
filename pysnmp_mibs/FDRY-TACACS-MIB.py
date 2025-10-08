#
# PySNMP MIB module FDRY-TACACS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/FDRY-TACACS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ServerUsage, = mibBuilder.importSymbols("FDRY-RADIUS-MIB", "ServerUsage")
fdryTacacs, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryTacacs")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("FDRY-TACACS-MIB", fdryTacacsServerRowKey=fdryTacacsServerRowKey, fdryTacacsServer=fdryTacacsServer, fdryTacacsServerAuthPort=fdryTacacsServerAuthPort, fdryTacacsServerTable=fdryTacacsServerTable, fdryTacacsServerRowStatus=fdryTacacsServerRowStatus, InetAddress=InetAddress, fdryTacacsMIB=fdryTacacsMIB, PYSNMP_MODULE_ID=fdryTacacsMIB, fdryTacacsServerUsage=fdryTacacsServerUsage, fdryTacacsServerAddrType=fdryTacacsServerAddrType, fdryTacacsServerIndex=fdryTacacsServerIndex, fdryTacacsServerEntry=fdryTacacsServerEntry, fdryTacacsServerAddr=fdryTacacsServerAddr)
