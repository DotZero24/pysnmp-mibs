#
# PySNMP MIB module FDRY-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/FDRY-RADIUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fdryRadius, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryRadius")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fdryRadiusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1))
fdryRadiusMIB.setRevisions(('2008-02-25 00:00', '2017-08-07 00:00',))
if mibBuilder.loadTexts: fdryRadiusMIB.setLastUpdated('201708070000Z')
if mibBuilder.loadTexts: fdryRadiusMIB.setOrganization('Ruckus Wireless, Inc..')
class ServerUsage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("default", 1), ("authenticationOnly", 2), ("authorizationOnly", 3), ("accountingOnly", 4))

class InetAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

fdryRadiusServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1))
fdryRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1), )
if mibBuilder.loadTexts: fdryRadiusServerTable.setStatus('current')
fdryRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-RADIUS-MIB", "fdryRadiusServerIndex"))
if mibBuilder.loadTexts: fdryRadiusServerEntry.setStatus('current')
fdryRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryRadiusServerIndex.setStatus('current')
fdryRadiusServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAddrType.setStatus('current')
fdryRadiusServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAddr.setStatus('current')
fdryRadiusServerAuthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 4), Unsigned32().clone(1645)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAuthPort.setStatus('current')
fdryRadiusServerAcctPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 5), Unsigned32().clone(1646)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAcctPort.setStatus('current')
fdryRadiusServerRowKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerRowKey.setStatus('current')
fdryRadiusServerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 7), ServerUsage().clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerUsage.setStatus('current')
fdryRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerRowStatus.setStatus('current')
fdryRadiusServerAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAuthType.setStatus('current')
fdryRadiusServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerPriority.setStatus('current')
mibBuilder.exportSymbols("FDRY-RADIUS-MIB", fdryRadiusServerPriority=fdryRadiusServerPriority, fdryRadiusServerTable=fdryRadiusServerTable, ServerUsage=ServerUsage, fdryRadiusServerRowStatus=fdryRadiusServerRowStatus, fdryRadiusServerAuthType=fdryRadiusServerAuthType, fdryRadiusServer=fdryRadiusServer, fdryRadiusServerAddr=fdryRadiusServerAddr, fdryRadiusServerAcctPort=fdryRadiusServerAcctPort, fdryRadiusServerEntry=fdryRadiusServerEntry, InetAddress=InetAddress, fdryRadiusServerRowKey=fdryRadiusServerRowKey, fdryRadiusServerAddrType=fdryRadiusServerAddrType, fdryRadiusServerIndex=fdryRadiusServerIndex, fdryRadiusServerUsage=fdryRadiusServerUsage, PYSNMP_MODULE_ID=fdryRadiusMIB, fdryRadiusServerAuthPort=fdryRadiusServerAuthPort, fdryRadiusMIB=fdryRadiusMIB)
