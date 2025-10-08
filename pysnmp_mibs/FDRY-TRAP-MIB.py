#
# PySNMP MIB module FDRY-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/FDRY-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fdryTrap, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryTrap")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("FDRY-TRAP-MIB", fdryTrapReceiverAddr=fdryTrapReceiverAddr, fdryTrapReceiverTable=fdryTrapReceiverTable, fdryTrapReceiverRowStatus=fdryTrapReceiverRowStatus, PYSNMP_MODULE_ID=fdryTrapMIB, fdryTrapReceiverUDPPort=fdryTrapReceiverUDPPort, fdryTrapReceiverEntry=fdryTrapReceiverEntry, fdryTrapReceiverIndex=fdryTrapReceiverIndex, fdryTrapReceiverSecurityLevel=fdryTrapReceiverSecurityLevel, fdryTrapReceiverAddrType=fdryTrapReceiverAddrType, fdryTrapReceiver=fdryTrapReceiver, fdryTrapReceiverSecurityModel=fdryTrapReceiverSecurityModel, fdryTrapMIB=fdryTrapMIB, SecurityLevel=SecurityLevel, InetAddress=InetAddress, fdryTrapReceiverCommunityOrSecurityName=fdryTrapReceiverCommunityOrSecurityName, SecurityModel=SecurityModel)
