_M='bits per second'
_L='xtmClassName'
_K='XEDIA-TRAFFIC-MGMT-MIB'
_J='TruthValue'
_I='Gauge32'
_H='ifIndex'
_G='IF-MIB'
_F='XtmBitRate'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_I,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention',_J)
xediaMibs,=mibBuilder.importSymbols('XEDIA-REG','xediaMibs')
xediaTrafficMgmtMIB=ModuleIdentity((1,3,6,1,4,1,838,3,2))
class XtmIpAddress(TextualConvention,IpAddress):status=_A;displayHint='1d.'
class XtmProtocol(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,6,17)));namedValues=NamedValues(*(('any',0),('icmp',1),('tcp',6),('udp',17)))
class XtmPort(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,20,21,23,25,53,67,68,69,70,79,80,119,123,161,162,179)));namedValues=NamedValues(*(('any',0),('ftpData',20),('ftp',21),('telnet',23),('smtp',25),('domain',53),('bootps',67),('bootpc',68),('tftp',69),('gopher',70),('finger',79),('wwwHttp',80),('nntp',119),('ntp',123),('snmp',161),('snmpTrap',162),('bgp',179)))
class XtmBitRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class XtmTosOctet(TextualConvention,OctetString):status=_A;displayHint='1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class XtmRange(DisplayString):status=_A
_XtmObjects_ObjectIdentity=ObjectIdentity
xtmObjects=_XtmObjects_ObjectIdentity((1,3,6,1,4,1,838,3,2,1))
_XtmClassTable_Object=MibTable
xtmClassTable=_XtmClassTable_Object((1,3,6,1,4,1,838,3,2,1,2))
if mibBuilder.loadTexts:xtmClassTable.setStatus(_A)
_XtmClassEntry_Object=MibTableRow
xtmClassEntry=_XtmClassEntry_Object((1,3,6,1,4,1,838,3,2,1,2,1))
xtmClassEntry.setIndexNames((0,_G,_H),(0,_K,_L))
if mibBuilder.loadTexts:xtmClassEntry.setStatus(_A)
class _XtmClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_XtmClassName_Type.__name__=_E
_XtmClassName_Object=MibTableColumn
xtmClassName=_XtmClassName_Object((1,3,6,1,4,1,838,3,2,1,2,1,1),_XtmClassName_Type())
xtmClassName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:xtmClassName.setStatus(_A)
class _XtmClassParent_Type(DisplayString):defaultValue=OctetString('interface');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_XtmClassParent_Type.__name__=_E
_XtmClassParent_Object=MibTableColumn
xtmClassParent=_XtmClassParent_Object((1,3,6,1,4,1,838,3,2,1,2,1,2),_XtmClassParent_Type())
xtmClassParent.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassParent.setStatus(_A)
class _XtmClassRate_Type(XtmBitRate):defaultValue=0
_XtmClassRate_Type.__name__=_F
_XtmClassRate_Object=MibTableColumn
xtmClassRate=_XtmClassRate_Object((1,3,6,1,4,1,838,3,2,1,2,1,13),_XtmClassRate_Type())
xtmClassRate.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassRate.setStatus(_A)
if mibBuilder.loadTexts:xtmClassRate.setUnits(_M)
class _XtmClassBounded_Type(TruthValue):defaultValue=2
_XtmClassBounded_Type.__name__=_J
_XtmClassBounded_Object=MibTableColumn
xtmClassBounded=_XtmClassBounded_Object((1,3,6,1,4,1,838,3,2,1,2,1,14),_XtmClassBounded_Type())
xtmClassBounded.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassBounded.setStatus(_A)
class _XtmClassPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_XtmClassPriority_Type.__name__=_C
_XtmClassPriority_Object=MibTableColumn
xtmClassPriority=_XtmClassPriority_Object((1,3,6,1,4,1,838,3,2,1,2,1,15),_XtmClassPriority_Type())
xtmClassPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassPriority.setStatus(_A)
class _XtmClassOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('downConflict',3),('autoClassActive',4)))
_XtmClassOperStatus_Type.__name__=_C
_XtmClassOperStatus_Object=MibTableColumn
xtmClassOperStatus=_XtmClassOperStatus_Object((1,3,6,1,4,1,838,3,2,1,2,1,22),_XtmClassOperStatus_Type())
xtmClassOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xtmClassOperStatus.setStatus(_A)
_XtmClassOperMsg_Type=DisplayString
_XtmClassOperMsg_Object=MibTableColumn
xtmClassOperMsg=_XtmClassOperMsg_Object((1,3,6,1,4,1,838,3,2,1,2,1,23),_XtmClassOperMsg_Type())
xtmClassOperMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:xtmClassOperMsg.setStatus(_A)
class _XtmClassBwUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('atLimit',1),('underLimit',2),('overLimit',3)))
_XtmClassBwUse_Type.__name__=_C
_XtmClassBwUse_Object=MibTableColumn
xtmClassBwUse=_XtmClassBwUse_Object((1,3,6,1,4,1,838,3,2,1,2,1,24),_XtmClassBwUse_Type())
xtmClassBwUse.setMaxAccess(_D)
if mibBuilder.loadTexts:xtmClassBwUse.setStatus(_A)
_XtmClassUnsatisfied_Type=TruthValue
_XtmClassUnsatisfied_Object=MibTableColumn
xtmClassUnsatisfied=_XtmClassUnsatisfied_Object((1,3,6,1,4,1,838,3,2,1,2,1,25),_XtmClassUnsatisfied_Type())
xtmClassUnsatisfied.setMaxAccess(_D)
if mibBuilder.loadTexts:xtmClassUnsatisfied.setStatus(_A)
class _XtmClassQueueSize_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_XtmClassQueueSize_Type.__name__=_I
_XtmClassQueueSize_Object=MibTableColumn
xtmClassQueueSize=_XtmClassQueueSize_Object((1,3,6,1,4,1,838,3,2,1,2,1,26),_XtmClassQueueSize_Type())
xtmClassQueueSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xtmClassQueueSize.setStatus(_A)
_XtmClassRowStatus_Type=RowStatus
_XtmClassRowStatus_Object=MibTableColumn
xtmClassRowStatus=_XtmClassRowStatus_Object((1,3,6,1,4,1,838,3,2,1,2,1,27),_XtmClassRowStatus_Type())
xtmClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassRowStatus.setStatus(_A)
class _XtmClassMaxRate_Type(XtmBitRate):defaultValue=0
_XtmClassMaxRate_Type.__name__=_F
_XtmClassMaxRate_Object=MibTableColumn
xtmClassMaxRate=_XtmClassMaxRate_Object((1,3,6,1,4,1,838,3,2,1,2,1,28),_XtmClassMaxRate_Type())
xtmClassMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassMaxRate.setStatus(_A)
if mibBuilder.loadTexts:xtmClassMaxRate.setUnits(_M)
class _XtmClassPeerClassificationOrder_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_XtmClassPeerClassificationOrder_Type.__name__=_C
_XtmClassPeerClassificationOrder_Object=MibTableColumn
xtmClassPeerClassificationOrder=_XtmClassPeerClassificationOrder_Object((1,3,6,1,4,1,838,3,2,1,2,1,44),_XtmClassPeerClassificationOrder_Type())
xtmClassPeerClassificationOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassPeerClassificationOrder.setStatus(_A)
_XtmClassSrcIpAddresses_Type=XtmRange
_XtmClassSrcIpAddresses_Object=MibTableColumn
xtmClassSrcIpAddresses=_XtmClassSrcIpAddresses_Object((1,3,6,1,4,1,838,3,2,1,2,1,45),_XtmClassSrcIpAddresses_Type())
xtmClassSrcIpAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassSrcIpAddresses.setStatus(_A)
_XtmClassDestIpAddresses_Type=XtmRange
_XtmClassDestIpAddresses_Object=MibTableColumn
xtmClassDestIpAddresses=_XtmClassDestIpAddresses_Object((1,3,6,1,4,1,838,3,2,1,2,1,46),_XtmClassDestIpAddresses_Type())
xtmClassDestIpAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassDestIpAddresses.setStatus(_A)
_XtmClassProtocols_Type=XtmRange
_XtmClassProtocols_Object=MibTableColumn
xtmClassProtocols=_XtmClassProtocols_Object((1,3,6,1,4,1,838,3,2,1,2,1,47),_XtmClassProtocols_Type())
xtmClassProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassProtocols.setStatus(_A)
_XtmClassSrcPorts_Type=XtmRange
_XtmClassSrcPorts_Object=MibTableColumn
xtmClassSrcPorts=_XtmClassSrcPorts_Object((1,3,6,1,4,1,838,3,2,1,2,1,48),_XtmClassSrcPorts_Type())
xtmClassSrcPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassSrcPorts.setStatus(_A)
_XtmClassDestPorts_Type=XtmRange
_XtmClassDestPorts_Object=MibTableColumn
xtmClassDestPorts=_XtmClassDestPorts_Object((1,3,6,1,4,1,838,3,2,1,2,1,49),_XtmClassDestPorts_Type())
xtmClassDestPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassDestPorts.setStatus(_A)
_XtmClassApplications_Type=XtmRange
_XtmClassApplications_Object=MibTableColumn
xtmClassApplications=_XtmClassApplications_Object((1,3,6,1,4,1,838,3,2,1,2,1,50),_XtmClassApplications_Type())
xtmClassApplications.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassApplications.setStatus(_A)
_XtmClassClassificationTos_Type=XtmRange
_XtmClassClassificationTos_Object=MibTableColumn
xtmClassClassificationTos=_XtmClassClassificationTos_Object((1,3,6,1,4,1,838,3,2,1,2,1,51),_XtmClassClassificationTos_Type())
xtmClassClassificationTos.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassClassificationTos.setStatus(_A)
_XtmClassSrcDomainNames_Type=XtmRange
_XtmClassSrcDomainNames_Object=MibTableColumn
xtmClassSrcDomainNames=_XtmClassSrcDomainNames_Object((1,3,6,1,4,1,838,3,2,1,2,1,52),_XtmClassSrcDomainNames_Type())
xtmClassSrcDomainNames.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassSrcDomainNames.setStatus(_A)
_XtmClassDestDomainNames_Type=XtmRange
_XtmClassDestDomainNames_Object=MibTableColumn
xtmClassDestDomainNames=_XtmClassDestDomainNames_Object((1,3,6,1,4,1,838,3,2,1,2,1,53),_XtmClassDestDomainNames_Type())
xtmClassDestDomainNames.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassDestDomainNames.setStatus(_A)
class _XtmClassOperator_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('and',1),('or',2)))
_XtmClassOperator_Type.__name__=_C
_XtmClassOperator_Object=MibTableColumn
xtmClassOperator=_XtmClassOperator_Object((1,3,6,1,4,1,838,3,2,1,2,1,54),_XtmClassOperator_Type())
xtmClassOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:xtmClassOperator.setStatus(_A)
_XtmNotifications_ObjectIdentity=ObjectIdentity
xtmNotifications=_XtmNotifications_ObjectIdentity((1,3,6,1,4,1,838,3,2,2))
_XtmConformance_ObjectIdentity=ObjectIdentity
xtmConformance=_XtmConformance_ObjectIdentity((1,3,6,1,4,1,838,3,2,3))
mibBuilder.exportSymbols(_K,**{'XtmIpAddress':XtmIpAddress,'XtmProtocol':XtmProtocol,'XtmPort':XtmPort,_F:XtmBitRate,'XtmTosOctet':XtmTosOctet,'XtmRange':XtmRange,'xediaTrafficMgmtMIB':xediaTrafficMgmtMIB,'xtmObjects':xtmObjects,'xtmClassTable':xtmClassTable,'xtmClassEntry':xtmClassEntry,_L:xtmClassName,'xtmClassParent':xtmClassParent,'xtmClassRate':xtmClassRate,'xtmClassBounded':xtmClassBounded,'xtmClassPriority':xtmClassPriority,'xtmClassOperStatus':xtmClassOperStatus,'xtmClassOperMsg':xtmClassOperMsg,'xtmClassBwUse':xtmClassBwUse,'xtmClassUnsatisfied':xtmClassUnsatisfied,'xtmClassQueueSize':xtmClassQueueSize,'xtmClassRowStatus':xtmClassRowStatus,'xtmClassMaxRate':xtmClassMaxRate,'xtmClassPeerClassificationOrder':xtmClassPeerClassificationOrder,'xtmClassSrcIpAddresses':xtmClassSrcIpAddresses,'xtmClassDestIpAddresses':xtmClassDestIpAddresses,'xtmClassProtocols':xtmClassProtocols,'xtmClassSrcPorts':xtmClassSrcPorts,'xtmClassDestPorts':xtmClassDestPorts,'xtmClassApplications':xtmClassApplications,'xtmClassClassificationTos':xtmClassClassificationTos,'xtmClassSrcDomainNames':xtmClassSrcDomainNames,'xtmClassDestDomainNames':xtmClassDestDomainNames,'xtmClassOperator':xtmClassOperator,'xtmNotifications':xtmNotifications,'xtmConformance':xtmConformance})