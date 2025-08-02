_N='fsDiffServSchedulerId'
_M='fsDiffServMeterId'
_L='fsDiffServOutProfileActionId'
_K='fsDiffServInProfileActionId'
_J='fsDiffServClfrId'
_I='fsDiffServMultiFieldClfrId'
_H='Unsigned32'
_G='OctetString'
_F='read-create'
_E='not-accessible'
_D='SUPERMICRO-DIFFSERV-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressPrefixLength,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsDiffServMib=ModuleIdentity((1,3,6,1,4,1,10876,101,1,83))
if mibBuilder.loadTexts:fsDiffServMib.setRevisions(('2012-09-05 00:00',))
class IfDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outbound',1),('inbound',2)))
class PortList(TextualConvention,OctetString):status=_A
class DscpOrAny(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsDiffServMIBObjects_ObjectIdentity=ObjectIdentity
fsDiffServMIBObjects=_FsDiffServMIBObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1))
_FsDiffServSystem_ObjectIdentity=ObjectIdentity
fsDiffServSystem=_FsDiffServSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,1))
class _FsDsSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsDsSystemControl_Type.__name__=_C
_FsDsSystemControl_Object=MibScalar
fsDsSystemControl=_FsDsSystemControl_Object((1,3,6,1,4,1,10876,101,1,83,1,1,1),_FsDsSystemControl_Type())
fsDsSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDsSystemControl.setStatus(_A)
class _FsDsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsDsStatus_Type.__name__=_C
_FsDsStatus_Object=MibScalar
fsDsStatus=_FsDsStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,1,2),_FsDsStatus_Type())
fsDsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDsStatus.setStatus(_A)
_FsDiffServMFClassifier_ObjectIdentity=ObjectIdentity
fsDiffServMFClassifier=_FsDiffServMFClassifier_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,2))
_FsDiffServMultiFieldClfrTable_Object=MibTable
fsDiffServMultiFieldClfrTable=_FsDiffServMultiFieldClfrTable_Object((1,3,6,1,4,1,10876,101,1,83,1,2,1))
if mibBuilder.loadTexts:fsDiffServMultiFieldClfrTable.setStatus(_A)
_FsDiffServMultiFieldClfrEntry_Object=MibTableRow
fsDiffServMultiFieldClfrEntry=_FsDiffServMultiFieldClfrEntry_Object((1,3,6,1,4,1,10876,101,1,83,1,2,1,1))
fsDiffServMultiFieldClfrEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:fsDiffServMultiFieldClfrEntry.setStatus(_A)
class _FsDiffServMultiFieldClfrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDiffServMultiFieldClfrId_Type.__name__=_C
_FsDiffServMultiFieldClfrId_Object=MibTableColumn
fsDiffServMultiFieldClfrId=_FsDiffServMultiFieldClfrId_Object((1,3,6,1,4,1,10876,101,1,83,1,2,1,1,1),_FsDiffServMultiFieldClfrId_Type())
fsDiffServMultiFieldClfrId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDiffServMultiFieldClfrId.setStatus(_A)
_FsDiffServMultiFieldClfrFilterId_Type=Unsigned32
_FsDiffServMultiFieldClfrFilterId_Object=MibTableColumn
fsDiffServMultiFieldClfrFilterId=_FsDiffServMultiFieldClfrFilterId_Object((1,3,6,1,4,1,10876,101,1,83,1,2,1,1,2),_FsDiffServMultiFieldClfrFilterId_Type())
fsDiffServMultiFieldClfrFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServMultiFieldClfrFilterId.setStatus(_A)
class _FsDiffServMultiFieldClfrFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('macfilter',1),('ipfilter',2)))
_FsDiffServMultiFieldClfrFilterType_Type.__name__=_C
_FsDiffServMultiFieldClfrFilterType_Object=MibTableColumn
fsDiffServMultiFieldClfrFilterType=_FsDiffServMultiFieldClfrFilterType_Object((1,3,6,1,4,1,10876,101,1,83,1,2,1,1,3),_FsDiffServMultiFieldClfrFilterType_Type())
fsDiffServMultiFieldClfrFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServMultiFieldClfrFilterType.setStatus(_A)
_FsDiffServMultiFieldClfrStatus_Type=RowStatus
_FsDiffServMultiFieldClfrStatus_Object=MibTableColumn
fsDiffServMultiFieldClfrStatus=_FsDiffServMultiFieldClfrStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,2,1,1,4),_FsDiffServMultiFieldClfrStatus_Type())
fsDiffServMultiFieldClfrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDiffServMultiFieldClfrStatus.setStatus(_A)
_FsDiffServClassifier_ObjectIdentity=ObjectIdentity
fsDiffServClassifier=_FsDiffServClassifier_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,3))
_FsDiffServClfrTable_Object=MibTable
fsDiffServClfrTable=_FsDiffServClfrTable_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1))
if mibBuilder.loadTexts:fsDiffServClfrTable.setStatus(_A)
_FsDiffServClfrEntry_Object=MibTableRow
fsDiffServClfrEntry=_FsDiffServClfrEntry_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1,1))
fsDiffServClfrEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:fsDiffServClfrEntry.setStatus(_A)
class _FsDiffServClfrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDiffServClfrId_Type.__name__=_C
_FsDiffServClfrId_Object=MibTableColumn
fsDiffServClfrId=_FsDiffServClfrId_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1,1,1),_FsDiffServClfrId_Type())
fsDiffServClfrId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDiffServClfrId.setStatus(_A)
class _FsDiffServClfrMFClfrId_Type(Integer32):defaultValue=0
_FsDiffServClfrMFClfrId_Type.__name__=_C
_FsDiffServClfrMFClfrId_Object=MibTableColumn
fsDiffServClfrMFClfrId=_FsDiffServClfrMFClfrId_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1,1,2),_FsDiffServClfrMFClfrId_Type())
fsDiffServClfrMFClfrId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServClfrMFClfrId.setStatus(_A)
class _FsDiffServClfrInProActionId_Type(Integer32):defaultValue=0
_FsDiffServClfrInProActionId_Type.__name__=_C
_FsDiffServClfrInProActionId_Object=MibTableColumn
fsDiffServClfrInProActionId=_FsDiffServClfrInProActionId_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1,1,3),_FsDiffServClfrInProActionId_Type())
fsDiffServClfrInProActionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServClfrInProActionId.setStatus(_A)
class _FsDiffServClfrOutProActionId_Type(Integer32):defaultValue=0
_FsDiffServClfrOutProActionId_Type.__name__=_C
_FsDiffServClfrOutProActionId_Object=MibTableColumn
fsDiffServClfrOutProActionId=_FsDiffServClfrOutProActionId_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1,1,4),_FsDiffServClfrOutProActionId_Type())
fsDiffServClfrOutProActionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServClfrOutProActionId.setStatus(_A)
_FsDiffServClfrStatus_Type=RowStatus
_FsDiffServClfrStatus_Object=MibTableColumn
fsDiffServClfrStatus=_FsDiffServClfrStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,3,1,1,5),_FsDiffServClfrStatus_Type())
fsDiffServClfrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDiffServClfrStatus.setStatus(_A)
_FsDiffServInProfileAction_ObjectIdentity=ObjectIdentity
fsDiffServInProfileAction=_FsDiffServInProfileAction_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,4))
_FsDiffServInProfileActionTable_Object=MibTable
fsDiffServInProfileActionTable=_FsDiffServInProfileActionTable_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1))
if mibBuilder.loadTexts:fsDiffServInProfileActionTable.setStatus(_A)
_FsDiffServInProfileActionEntry_Object=MibTableRow
fsDiffServInProfileActionEntry=_FsDiffServInProfileActionEntry_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1))
fsDiffServInProfileActionEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fsDiffServInProfileActionEntry.setStatus(_A)
class _FsDiffServInProfileActionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDiffServInProfileActionId_Type.__name__=_C
_FsDiffServInProfileActionId_Object=MibTableColumn
fsDiffServInProfileActionId=_FsDiffServInProfileActionId_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,1),_FsDiffServInProfileActionId_Type())
fsDiffServInProfileActionId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDiffServInProfileActionId.setStatus(_A)
_FsDiffServInProfileActionFlag_Type=Unsigned32
_FsDiffServInProfileActionFlag_Object=MibTableColumn
fsDiffServInProfileActionFlag=_FsDiffServInProfileActionFlag_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,2),_FsDiffServInProfileActionFlag_Type())
fsDiffServInProfileActionFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServInProfileActionFlag.setStatus(_A)
_FsDiffServInProfileActionNewPrio_Type=Unsigned32
_FsDiffServInProfileActionNewPrio_Object=MibTableColumn
fsDiffServInProfileActionNewPrio=_FsDiffServInProfileActionNewPrio_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,3),_FsDiffServInProfileActionNewPrio_Type())
fsDiffServInProfileActionNewPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServInProfileActionNewPrio.setStatus(_A)
_FsDiffServInProfileActionIpTOS_Type=Unsigned32
_FsDiffServInProfileActionIpTOS_Object=MibTableColumn
fsDiffServInProfileActionIpTOS=_FsDiffServInProfileActionIpTOS_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,4),_FsDiffServInProfileActionIpTOS_Type())
fsDiffServInProfileActionIpTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServInProfileActionIpTOS.setStatus(_A)
_FsDiffServInProfileActionPort_Type=Unsigned32
_FsDiffServInProfileActionPort_Object=MibTableColumn
fsDiffServInProfileActionPort=_FsDiffServInProfileActionPort_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,5),_FsDiffServInProfileActionPort_Type())
fsDiffServInProfileActionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServInProfileActionPort.setStatus(_A)
_FsDiffServInProfileActionDscp_Type=DscpOrAny
_FsDiffServInProfileActionDscp_Object=MibTableColumn
fsDiffServInProfileActionDscp=_FsDiffServInProfileActionDscp_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,6),_FsDiffServInProfileActionDscp_Type())
fsDiffServInProfileActionDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServInProfileActionDscp.setStatus(_A)
_FsDiffServInProfileActionStatus_Type=RowStatus
_FsDiffServInProfileActionStatus_Object=MibTableColumn
fsDiffServInProfileActionStatus=_FsDiffServInProfileActionStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,4,1,1,7),_FsDiffServInProfileActionStatus_Type())
fsDiffServInProfileActionStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDiffServInProfileActionStatus.setStatus(_A)
_FsDiffServOutProfileAction_ObjectIdentity=ObjectIdentity
fsDiffServOutProfileAction=_FsDiffServOutProfileAction_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,5))
_FsDiffServOutProfileActionTable_Object=MibTable
fsDiffServOutProfileActionTable=_FsDiffServOutProfileActionTable_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1))
if mibBuilder.loadTexts:fsDiffServOutProfileActionTable.setStatus(_A)
_FsDiffServOutProfileActionEntry_Object=MibTableRow
fsDiffServOutProfileActionEntry=_FsDiffServOutProfileActionEntry_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1,1))
fsDiffServOutProfileActionEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:fsDiffServOutProfileActionEntry.setStatus(_A)
class _FsDiffServOutProfileActionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDiffServOutProfileActionId_Type.__name__=_C
_FsDiffServOutProfileActionId_Object=MibTableColumn
fsDiffServOutProfileActionId=_FsDiffServOutProfileActionId_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1,1,1),_FsDiffServOutProfileActionId_Type())
fsDiffServOutProfileActionId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDiffServOutProfileActionId.setStatus(_A)
_FsDiffServOutProfileActionFlag_Type=Unsigned32
_FsDiffServOutProfileActionFlag_Object=MibTableColumn
fsDiffServOutProfileActionFlag=_FsDiffServOutProfileActionFlag_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1,1,2),_FsDiffServOutProfileActionFlag_Type())
fsDiffServOutProfileActionFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServOutProfileActionFlag.setStatus(_A)
_FsDiffServOutProfileActionDscp_Type=DscpOrAny
_FsDiffServOutProfileActionDscp_Object=MibTableColumn
fsDiffServOutProfileActionDscp=_FsDiffServOutProfileActionDscp_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1,1,3),_FsDiffServOutProfileActionDscp_Type())
fsDiffServOutProfileActionDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServOutProfileActionDscp.setStatus(_A)
_FsDiffServOutProfileActionMID_Type=Integer32
_FsDiffServOutProfileActionMID_Object=MibTableColumn
fsDiffServOutProfileActionMID=_FsDiffServOutProfileActionMID_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1,1,4),_FsDiffServOutProfileActionMID_Type())
fsDiffServOutProfileActionMID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServOutProfileActionMID.setStatus(_A)
_FsDiffServOutProfileActionStatus_Type=RowStatus
_FsDiffServOutProfileActionStatus_Object=MibTableColumn
fsDiffServOutProfileActionStatus=_FsDiffServOutProfileActionStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,5,1,1,5),_FsDiffServOutProfileActionStatus_Type())
fsDiffServOutProfileActionStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDiffServOutProfileActionStatus.setStatus(_A)
_FsDiffServMeter_ObjectIdentity=ObjectIdentity
fsDiffServMeter=_FsDiffServMeter_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,6))
_FsDiffServMeterTable_Object=MibTable
fsDiffServMeterTable=_FsDiffServMeterTable_Object((1,3,6,1,4,1,10876,101,1,83,1,6,1))
if mibBuilder.loadTexts:fsDiffServMeterTable.setStatus(_A)
_FsDiffServMeterEntry_Object=MibTableRow
fsDiffServMeterEntry=_FsDiffServMeterEntry_Object((1,3,6,1,4,1,10876,101,1,83,1,6,1,1))
fsDiffServMeterEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:fsDiffServMeterEntry.setStatus(_A)
class _FsDiffServMeterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDiffServMeterId_Type.__name__=_C
_FsDiffServMeterId_Object=MibTableColumn
fsDiffServMeterId=_FsDiffServMeterId_Object((1,3,6,1,4,1,10876,101,1,83,1,6,1,1,1),_FsDiffServMeterId_Type())
fsDiffServMeterId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDiffServMeterId.setStatus(_A)
_FsDiffServMetertokenSize_Type=Unsigned32
_FsDiffServMetertokenSize_Object=MibTableColumn
fsDiffServMetertokenSize=_FsDiffServMetertokenSize_Object((1,3,6,1,4,1,10876,101,1,83,1,6,1,1,2),_FsDiffServMetertokenSize_Type())
fsDiffServMetertokenSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServMetertokenSize.setStatus(_A)
_FsDiffServMeterRefreshCount_Type=Unsigned32
_FsDiffServMeterRefreshCount_Object=MibTableColumn
fsDiffServMeterRefreshCount=_FsDiffServMeterRefreshCount_Object((1,3,6,1,4,1,10876,101,1,83,1,6,1,1,3),_FsDiffServMeterRefreshCount_Type())
fsDiffServMeterRefreshCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServMeterRefreshCount.setStatus(_A)
_FsDiffServMeterStatus_Type=RowStatus
_FsDiffServMeterStatus_Object=MibTableColumn
fsDiffServMeterStatus=_FsDiffServMeterStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,6,1,1,4),_FsDiffServMeterStatus_Type())
fsDiffServMeterStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDiffServMeterStatus.setStatus(_A)
_FsDiffServScheduler_ObjectIdentity=ObjectIdentity
fsDiffServScheduler=_FsDiffServScheduler_ObjectIdentity((1,3,6,1,4,1,10876,101,1,83,1,7))
_FsDiffServSchedulerTable_Object=MibTable
fsDiffServSchedulerTable=_FsDiffServSchedulerTable_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1))
if mibBuilder.loadTexts:fsDiffServSchedulerTable.setStatus(_A)
_FsDiffServSchedulerEntry_Object=MibTableRow
fsDiffServSchedulerEntry=_FsDiffServSchedulerEntry_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1,1))
fsDiffServSchedulerEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:fsDiffServSchedulerEntry.setStatus(_A)
class _FsDiffServSchedulerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDiffServSchedulerId_Type.__name__=_C
_FsDiffServSchedulerId_Object=MibTableColumn
fsDiffServSchedulerId=_FsDiffServSchedulerId_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1,1,1),_FsDiffServSchedulerId_Type())
fsDiffServSchedulerId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDiffServSchedulerId.setStatus(_A)
_FsDiffServSchedulerDPId_Type=Integer32
_FsDiffServSchedulerDPId_Object=MibTableColumn
fsDiffServSchedulerDPId=_FsDiffServSchedulerDPId_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1,1,2),_FsDiffServSchedulerDPId_Type())
fsDiffServSchedulerDPId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServSchedulerDPId.setStatus(_A)
class _FsDiffServSchedulerQueueCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FsDiffServSchedulerQueueCount_Type.__name__=_H
_FsDiffServSchedulerQueueCount_Object=MibTableColumn
fsDiffServSchedulerQueueCount=_FsDiffServSchedulerQueueCount_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1,1,3),_FsDiffServSchedulerQueueCount_Type())
fsDiffServSchedulerQueueCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServSchedulerQueueCount.setStatus(_A)
class _FsDiffServSchedulerWeight_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_FsDiffServSchedulerWeight_Type.__name__=_G
_FsDiffServSchedulerWeight_Object=MibTableColumn
fsDiffServSchedulerWeight=_FsDiffServSchedulerWeight_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1,1,4),_FsDiffServSchedulerWeight_Type())
fsDiffServSchedulerWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServSchedulerWeight.setStatus(_A)
_FsDiffServSchedulerStatus_Type=RowStatus
_FsDiffServSchedulerStatus_Object=MibTableColumn
fsDiffServSchedulerStatus=_FsDiffServSchedulerStatus_Object((1,3,6,1,4,1,10876,101,1,83,1,7,1,1,5),_FsDiffServSchedulerStatus_Type())
fsDiffServSchedulerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDiffServSchedulerStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'IfDirection':IfDirection,'PortList':PortList,'DscpOrAny':DscpOrAny,'fsDiffServMib':fsDiffServMib,'fsDiffServMIBObjects':fsDiffServMIBObjects,'fsDiffServSystem':fsDiffServSystem,'fsDsSystemControl':fsDsSystemControl,'fsDsStatus':fsDsStatus,'fsDiffServMFClassifier':fsDiffServMFClassifier,'fsDiffServMultiFieldClfrTable':fsDiffServMultiFieldClfrTable,'fsDiffServMultiFieldClfrEntry':fsDiffServMultiFieldClfrEntry,_I:fsDiffServMultiFieldClfrId,'fsDiffServMultiFieldClfrFilterId':fsDiffServMultiFieldClfrFilterId,'fsDiffServMultiFieldClfrFilterType':fsDiffServMultiFieldClfrFilterType,'fsDiffServMultiFieldClfrStatus':fsDiffServMultiFieldClfrStatus,'fsDiffServClassifier':fsDiffServClassifier,'fsDiffServClfrTable':fsDiffServClfrTable,'fsDiffServClfrEntry':fsDiffServClfrEntry,_J:fsDiffServClfrId,'fsDiffServClfrMFClfrId':fsDiffServClfrMFClfrId,'fsDiffServClfrInProActionId':fsDiffServClfrInProActionId,'fsDiffServClfrOutProActionId':fsDiffServClfrOutProActionId,'fsDiffServClfrStatus':fsDiffServClfrStatus,'fsDiffServInProfileAction':fsDiffServInProfileAction,'fsDiffServInProfileActionTable':fsDiffServInProfileActionTable,'fsDiffServInProfileActionEntry':fsDiffServInProfileActionEntry,_K:fsDiffServInProfileActionId,'fsDiffServInProfileActionFlag':fsDiffServInProfileActionFlag,'fsDiffServInProfileActionNewPrio':fsDiffServInProfileActionNewPrio,'fsDiffServInProfileActionIpTOS':fsDiffServInProfileActionIpTOS,'fsDiffServInProfileActionPort':fsDiffServInProfileActionPort,'fsDiffServInProfileActionDscp':fsDiffServInProfileActionDscp,'fsDiffServInProfileActionStatus':fsDiffServInProfileActionStatus,'fsDiffServOutProfileAction':fsDiffServOutProfileAction,'fsDiffServOutProfileActionTable':fsDiffServOutProfileActionTable,'fsDiffServOutProfileActionEntry':fsDiffServOutProfileActionEntry,_L:fsDiffServOutProfileActionId,'fsDiffServOutProfileActionFlag':fsDiffServOutProfileActionFlag,'fsDiffServOutProfileActionDscp':fsDiffServOutProfileActionDscp,'fsDiffServOutProfileActionMID':fsDiffServOutProfileActionMID,'fsDiffServOutProfileActionStatus':fsDiffServOutProfileActionStatus,'fsDiffServMeter':fsDiffServMeter,'fsDiffServMeterTable':fsDiffServMeterTable,'fsDiffServMeterEntry':fsDiffServMeterEntry,_M:fsDiffServMeterId,'fsDiffServMetertokenSize':fsDiffServMetertokenSize,'fsDiffServMeterRefreshCount':fsDiffServMeterRefreshCount,'fsDiffServMeterStatus':fsDiffServMeterStatus,'fsDiffServScheduler':fsDiffServScheduler,'fsDiffServSchedulerTable':fsDiffServSchedulerTable,'fsDiffServSchedulerEntry':fsDiffServSchedulerEntry,_N:fsDiffServSchedulerId,'fsDiffServSchedulerDPId':fsDiffServSchedulerDPId,'fsDiffServSchedulerQueueCount':fsDiffServSchedulerQueueCount,'fsDiffServSchedulerWeight':fsDiffServSchedulerWeight,'fsDiffServSchedulerStatus':fsDiffServSchedulerStatus})