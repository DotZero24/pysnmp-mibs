#
# PySNMP MIB module FDRY-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/FDRY-RADIUS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fdryRadius, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryRadius")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("FDRY-RADIUS-MIB", fdryRadiusServerTable=fdryRadiusServerTable, fdryRadiusServerAuthPort=fdryRadiusServerAuthPort, fdryRadiusMIB=fdryRadiusMIB, fdryRadiusServerEntry=fdryRadiusServerEntry, fdryRadiusServerRowStatus=fdryRadiusServerRowStatus, fdryRadiusServerIndex=fdryRadiusServerIndex, fdryRadiusServerAuthType=fdryRadiusServerAuthType, fdryRadiusServerAddr=fdryRadiusServerAddr, fdryRadiusServerRowKey=fdryRadiusServerRowKey, fdryRadiusServerUsage=fdryRadiusServerUsage, fdryRadiusServer=fdryRadiusServer, fdryRadiusServerAddrType=fdryRadiusServerAddrType, fdryRadiusServerPriority=fdryRadiusServerPriority, ServerUsage=ServerUsage, InetAddress=InetAddress, fdryRadiusServerAcctPort=fdryRadiusServerAcctPort, PYSNMP_MODULE_ID=fdryRadiusMIB)
