#
# PySNMP MIB module FDRY-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/FDRY-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fdryTrap, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryTrap")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fdryTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1))
fdryTrapMIB.setRevisions(('2008-02-25 00:00', '2023-05-25 00:00',))
if mibBuilder.loadTexts: fdryTrapMIB.setLastUpdated('202305250000Z')
if mibBuilder.loadTexts: fdryTrapMIB.setOrganization('Ruckus Wireless, Inc..')
class InetAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SecurityModel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("v1", 1), ("v2c", 2), ("usm", 3))

class SecurityLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noAuth", 1), ("auth", 2), ("authPriv", 3))

fdryTrapReceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1))
fdryTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1), )
if mibBuilder.loadTexts: fdryTrapReceiverTable.setStatus('current')
fdryTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-TRAP-MIB", "fdryTrapReceiverIndex"))
if mibBuilder.loadTexts: fdryTrapReceiverEntry.setStatus('current')
fdryTrapReceiverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryTrapReceiverIndex.setStatus('current')
fdryTrapReceiverAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverAddrType.setStatus('current')
fdryTrapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverAddr.setStatus('current')
fdryTrapReceiverCommunityOrSecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverCommunityOrSecurityName.setStatus('current')
fdryTrapReceiverUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverUDPPort.setStatus('current')
fdryTrapReceiverSecurityModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 6), SecurityModel().clone('v1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverSecurityModel.setStatus('current')
fdryTrapReceiverSecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 7), SecurityLevel().clone('noAuth')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverSecurityLevel.setStatus('current')
fdryTrapReceiverRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverRowStatus.setStatus('current')
mibBuilder.exportSymbols("FDRY-TRAP-MIB", fdryTrapReceiverAddr=fdryTrapReceiverAddr, fdryTrapReceiverEntry=fdryTrapReceiverEntry, PYSNMP_MODULE_ID=fdryTrapMIB, SecurityModel=SecurityModel, fdryTrapReceiverSecurityLevel=fdryTrapReceiverSecurityLevel, SecurityLevel=SecurityLevel, fdryTrapMIB=fdryTrapMIB, fdryTrapReceiverSecurityModel=fdryTrapReceiverSecurityModel, fdryTrapReceiverCommunityOrSecurityName=fdryTrapReceiverCommunityOrSecurityName, InetAddress=InetAddress, fdryTrapReceiverUDPPort=fdryTrapReceiverUDPPort, fdryTrapReceiverIndex=fdryTrapReceiverIndex, fdryTrapReceiverAddrType=fdryTrapReceiverAddrType, fdryTrapReceiver=fdryTrapReceiver, fdryTrapReceiverTable=fdryTrapReceiverTable, fdryTrapReceiverRowStatus=fdryTrapReceiverRowStatus)
