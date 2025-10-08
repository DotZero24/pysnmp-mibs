#
# PySNMP MIB module XEDIA-TRAFFIC-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/XEDIA-TRAFFIC-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaTrafficMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 2))
if mibBuilder.loadTexts: xediaTrafficMgmtMIB.setLastUpdated('9705022155Z')
if mibBuilder.loadTexts: xediaTrafficMgmtMIB.setOrganization('Xedia Corp.')
xtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 2, 1))
xtmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 2, 2))
xtmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 2, 3))
class XtmIpAddress(TextualConvention, IpAddress):
    status = 'current'
    displayHint = '1d.'

class XtmProtocol(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 17))
    namedValues = NamedValues(("any", 0), ("icmp", 1), ("tcp", 6), ("udp", 17))

class XtmPort(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 20, 21, 23, 25, 53, 67, 68, 69, 70, 79, 80, 119, 123, 161, 162, 179))
    namedValues = NamedValues(("any", 0), ("ftpData", 20), ("ftp", 21), ("telnet", 23), ("smtp", 25), ("domain", 53), ("bootps", 67), ("bootpc", 68), ("tftp", 69), ("gopher", 70), ("finger", 79), ("wwwHttp", 80), ("nntp", 119), ("ntp", 123), ("snmp", 161), ("snmpTrap", 162), ("bgp", 179))

class XtmBitRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class XtmTosOctet(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class XtmRange(DisplayString):
    status = 'current'

xtmClassTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2), )
if mibBuilder.loadTexts: xtmClassTable.setStatus('current')
xtmClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "XEDIA-TRAFFIC-MGMT-MIB", "xtmClassName"))
if mibBuilder.loadTexts: xtmClassEntry.setStatus('current')
xtmClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: xtmClassName.setStatus('current')
xtmClassParent = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)).clone('interface')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassParent.setStatus('current')
xtmClassRate = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 13), XtmBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassRate.setStatus('current')
xtmClassBounded = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassBounded.setStatus('current')
xtmClassPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassPriority.setStatus('current')
xtmClassOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("downConflict", 3), ("autoClassActive", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassOperStatus.setStatus('current')
xtmClassOperMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassOperMsg.setStatus('current')
xtmClassBwUse = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("atLimit", 1), ("underLimit", 2), ("overLimit", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassBwUse.setStatus('current')
xtmClassUnsatisfied = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 25), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassUnsatisfied.setStatus('current')
xtmClassQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 26), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassQueueSize.setStatus('current')
xtmClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassRowStatus.setStatus('current')
xtmClassMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 28), XtmBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassMaxRate.setStatus('current')
xtmClassPeerClassificationOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 44), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassPeerClassificationOrder.setStatus('current')
xtmClassSrcIpAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 45), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassSrcIpAddresses.setStatus('current')
xtmClassDestIpAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 46), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassDestIpAddresses.setStatus('current')
xtmClassProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 47), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassProtocols.setStatus('current')
xtmClassSrcPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 48), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassSrcPorts.setStatus('current')
xtmClassDestPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 49), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassDestPorts.setStatus('current')
xtmClassApplications = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 50), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassApplications.setStatus('current')
xtmClassClassificationTos = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 51), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassClassificationTos.setStatus('current')
xtmClassSrcDomainNames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 52), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassSrcDomainNames.setStatus('current')
xtmClassDestDomainNames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 53), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassDestDomainNames.setStatus('current')
xtmClassOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("and", 1), ("or", 2))).clone('and')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassOperator.setStatus('current')
mibBuilder.exportSymbols("XEDIA-TRAFFIC-MGMT-MIB", XtmTosOctet=XtmTosOctet, XtmBitRate=XtmBitRate, xtmClassQueueSize=xtmClassQueueSize, xtmNotifications=xtmNotifications, xtmClassDestDomainNames=xtmClassDestDomainNames, xtmClassEntry=xtmClassEntry, XtmPort=XtmPort, xtmClassMaxRate=xtmClassMaxRate, xtmClassSrcDomainNames=xtmClassSrcDomainNames, xtmClassOperMsg=xtmClassOperMsg, xtmClassRowStatus=xtmClassRowStatus, xtmClassSrcIpAddresses=xtmClassSrcIpAddresses, xtmClassRate=xtmClassRate, xtmClassBounded=xtmClassBounded, xtmClassTable=xtmClassTable, xtmClassPriority=xtmClassPriority, xtmClassDestPorts=xtmClassDestPorts, xtmClassOperStatus=xtmClassOperStatus, xtmConformance=xtmConformance, XtmProtocol=XtmProtocol, xtmClassClassificationTos=xtmClassClassificationTos, xtmClassUnsatisfied=xtmClassUnsatisfied, xtmClassSrcPorts=xtmClassSrcPorts, xtmClassDestIpAddresses=xtmClassDestIpAddresses, xtmClassProtocols=xtmClassProtocols, xtmClassOperator=xtmClassOperator, xtmObjects=xtmObjects, xtmClassName=xtmClassName, PYSNMP_MODULE_ID=xediaTrafficMgmtMIB, xtmClassPeerClassificationOrder=xtmClassPeerClassificationOrder, xtmClassApplications=xtmClassApplications, xtmClassParent=xtmClassParent, XtmIpAddress=XtmIpAddress, xediaTrafficMgmtMIB=xediaTrafficMgmtMIB, xtmClassBwUse=xtmClassBwUse, XtmRange=XtmRange)
