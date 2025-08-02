_V='slePortSrcGuardAddressControlTImeStamp'
_U='slePortSrcGuardEnable'
_T='slePortSrcGuardConfigControlReqResult'
_S='slePortSrcGuardConfigControlRequest'
_R='sleFeatureEnable'
_Q='sleGlobalControlReqResult'
_P='sleGlobalControlTimeStamp'
_O='sleGlobalControlRequest'
_N='enable'
_M='disable'
_L='active'
_K='inactive'
_J='slePortSrcGuardAddressMask'
_I='slePortSrcGuardAddressControlReqResult'
_H='slePortSrcGuardAddressControlRequest'
_G='slePortSrcGuardIndex'
_F='slePortSrcGuardAddressIp'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='SLE-DHCP-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
sleDhcpSnooping=ModuleIdentity((1,3,6,1,4,1,6296,101,12))
if mibBuilder.loadTexts:sleDhcpSnooping.setRevisions(('2005-07-29 14:25',))
_SleGlobal_ObjectIdentity=ObjectIdentity
sleGlobal=_SleGlobal_ObjectIdentity((1,3,6,1,4,1,6296,101,12,1))
_SleGlobalInfo_ObjectIdentity=ObjectIdentity
sleGlobalInfo=_SleGlobalInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,12,1,1))
class _SleFeatureEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_SleFeatureEnable_Type.__name__=_E
_SleFeatureEnable_Object=MibScalar
sleFeatureEnable=_SleFeatureEnable_Object((1,3,6,1,4,1,6296,101,12,1,1,1),_SleFeatureEnable_Type())
sleFeatureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sleFeatureEnable.setStatus(_A)
_SleGlobalControl_ObjectIdentity=ObjectIdentity
sleGlobalControl=_SleGlobalControl_ObjectIdentity((1,3,6,1,4,1,6296,101,12,1,2))
class _SleGlobalControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setSnoopingEnable',1))
_SleGlobalControlRequest_Type.__name__=_E
_SleGlobalControlRequest_Object=MibScalar
sleGlobalControlRequest=_SleGlobalControlRequest_Object((1,3,6,1,4,1,6296,101,12,1,2,1),_SleGlobalControlRequest_Type())
sleGlobalControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleGlobalControlRequest.setStatus(_A)
_SleGlobalControlStatus_Type=SleControlStatusType
_SleGlobalControlStatus_Object=MibScalar
sleGlobalControlStatus=_SleGlobalControlStatus_Object((1,3,6,1,4,1,6296,101,12,1,2,2),_SleGlobalControlStatus_Type())
sleGlobalControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleGlobalControlStatus.setStatus(_A)
_SleGlobalControlTimer_Type=Gauge32
_SleGlobalControlTimer_Object=MibScalar
sleGlobalControlTimer=_SleGlobalControlTimer_Object((1,3,6,1,4,1,6296,101,12,1,2,3),_SleGlobalControlTimer_Type())
sleGlobalControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleGlobalControlTimer.setStatus(_A)
_SleGlobalControlTimeStamp_Type=TimeTicks
_SleGlobalControlTimeStamp_Object=MibScalar
sleGlobalControlTimeStamp=_SleGlobalControlTimeStamp_Object((1,3,6,1,4,1,6296,101,12,1,2,4),_SleGlobalControlTimeStamp_Type())
sleGlobalControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleGlobalControlTimeStamp.setStatus(_A)
_SleGlobalControlReqResult_Type=SleControlRequestResultType
_SleGlobalControlReqResult_Object=MibScalar
sleGlobalControlReqResult=_SleGlobalControlReqResult_Object((1,3,6,1,4,1,6296,101,12,1,2,5),_SleGlobalControlReqResult_Type())
sleGlobalControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleGlobalControlReqResult.setStatus(_A)
class _SleGlobalControlFeatureEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_SleGlobalControlFeatureEnable_Type.__name__=_E
_SleGlobalControlFeatureEnable_Object=MibScalar
sleGlobalControlFeatureEnable=_SleGlobalControlFeatureEnable_Object((1,3,6,1,4,1,6296,101,12,1,2,6),_SleGlobalControlFeatureEnable_Type())
sleGlobalControlFeatureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sleGlobalControlFeatureEnable.setStatus(_A)
_SleGlobalNotification_ObjectIdentity=ObjectIdentity
sleGlobalNotification=_SleGlobalNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,12,1,3))
_SlePortSrcGuard_ObjectIdentity=ObjectIdentity
slePortSrcGuard=_SlePortSrcGuard_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2))
_SlePortSrcGuardConfig_ObjectIdentity=ObjectIdentity
slePortSrcGuardConfig=_SlePortSrcGuardConfig_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2,1))
_SlePortSrcGuardConfigTable_Object=MibTable
slePortSrcGuardConfigTable=_SlePortSrcGuardConfigTable_Object((1,3,6,1,4,1,6296,101,12,2,1,1))
if mibBuilder.loadTexts:slePortSrcGuardConfigTable.setStatus(_A)
_SlePortSrcGuardConfigEntry_Object=MibTableRow
slePortSrcGuardConfigEntry=_SlePortSrcGuardConfigEntry_Object((1,3,6,1,4,1,6296,101,12,2,1,1,1))
slePortSrcGuardConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:slePortSrcGuardConfigEntry.setStatus(_A)
_SlePortSrcGuardIndex_Type=Integer32
_SlePortSrcGuardIndex_Object=MibTableColumn
slePortSrcGuardIndex=_SlePortSrcGuardIndex_Object((1,3,6,1,4,1,6296,101,12,2,1,1,1,1),_SlePortSrcGuardIndex_Type())
slePortSrcGuardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardIndex.setStatus(_A)
class _SlePortSrcGuardEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SlePortSrcGuardEnable_Type.__name__=_E
_SlePortSrcGuardEnable_Object=MibTableColumn
slePortSrcGuardEnable=_SlePortSrcGuardEnable_Object((1,3,6,1,4,1,6296,101,12,2,1,1,1,2),_SlePortSrcGuardEnable_Type())
slePortSrcGuardEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardEnable.setStatus(_A)
_SlePortSrcGuardConfigControl_ObjectIdentity=ObjectIdentity
slePortSrcGuardConfigControl=_SlePortSrcGuardConfigControl_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2,1,2))
class _SlePortSrcGuardConfigControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setPortSrcGuardConfig',1))
_SlePortSrcGuardConfigControlRequest_Type.__name__=_E
_SlePortSrcGuardConfigControlRequest_Object=MibScalar
slePortSrcGuardConfigControlRequest=_SlePortSrcGuardConfigControlRequest_Object((1,3,6,1,4,1,6296,101,12,2,1,2,1),_SlePortSrcGuardConfigControlRequest_Type())
slePortSrcGuardConfigControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlRequest.setStatus(_A)
_SlePortSrcGuardConfigControlStatus_Type=SleControlStatusType
_SlePortSrcGuardConfigControlStatus_Object=MibScalar
slePortSrcGuardConfigControlStatus=_SlePortSrcGuardConfigControlStatus_Object((1,3,6,1,4,1,6296,101,12,2,1,2,2),_SlePortSrcGuardConfigControlStatus_Type())
slePortSrcGuardConfigControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlStatus.setStatus(_A)
_SlePortSrcGuardConfigControlTimer_Type=Gauge32
_SlePortSrcGuardConfigControlTimer_Object=MibScalar
slePortSrcGuardConfigControlTimer=_SlePortSrcGuardConfigControlTimer_Object((1,3,6,1,4,1,6296,101,12,2,1,2,3),_SlePortSrcGuardConfigControlTimer_Type())
slePortSrcGuardConfigControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlTimer.setStatus(_A)
_SlePortSrcGuardConfigControlTimeStamp_Type=TimeTicks
_SlePortSrcGuardConfigControlTimeStamp_Object=MibScalar
slePortSrcGuardConfigControlTimeStamp=_SlePortSrcGuardConfigControlTimeStamp_Object((1,3,6,1,4,1,6296,101,12,2,1,2,4),_SlePortSrcGuardConfigControlTimeStamp_Type())
slePortSrcGuardConfigControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlTimeStamp.setStatus(_A)
_SlePortSrcGuardConfigControlReqResult_Type=SleControlRequestResultType
_SlePortSrcGuardConfigControlReqResult_Object=MibScalar
slePortSrcGuardConfigControlReqResult=_SlePortSrcGuardConfigControlReqResult_Object((1,3,6,1,4,1,6296,101,12,2,1,2,5),_SlePortSrcGuardConfigControlReqResult_Type())
slePortSrcGuardConfigControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlReqResult.setStatus(_A)
_SlePortSrcGuardConfigControlIndex_Type=Integer32
_SlePortSrcGuardConfigControlIndex_Object=MibScalar
slePortSrcGuardConfigControlIndex=_SlePortSrcGuardConfigControlIndex_Object((1,3,6,1,4,1,6296,101,12,2,1,2,6),_SlePortSrcGuardConfigControlIndex_Type())
slePortSrcGuardConfigControlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlIndex.setStatus(_A)
class _SlePortSrcGuardConfigControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SlePortSrcGuardConfigControlEnable_Type.__name__=_E
_SlePortSrcGuardConfigControlEnable_Object=MibScalar
slePortSrcGuardConfigControlEnable=_SlePortSrcGuardConfigControlEnable_Object((1,3,6,1,4,1,6296,101,12,2,1,2,7),_SlePortSrcGuardConfigControlEnable_Type())
slePortSrcGuardConfigControlEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardConfigControlEnable.setStatus(_A)
_SlePortSrcGuardConfigNotification_ObjectIdentity=ObjectIdentity
slePortSrcGuardConfigNotification=_SlePortSrcGuardConfigNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2,1,3))
_SlePortSrcGuardAddress_ObjectIdentity=ObjectIdentity
slePortSrcGuardAddress=_SlePortSrcGuardAddress_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2,2))
_SlePortSrcGuardAddressTable_Object=MibTable
slePortSrcGuardAddressTable=_SlePortSrcGuardAddressTable_Object((1,3,6,1,4,1,6296,101,12,2,2,1))
if mibBuilder.loadTexts:slePortSrcGuardAddressTable.setStatus(_A)
_SlePortSrcGuardAddressEntry_Object=MibTableRow
slePortSrcGuardAddressEntry=_SlePortSrcGuardAddressEntry_Object((1,3,6,1,4,1,6296,101,12,2,2,1,1))
slePortSrcGuardAddressEntry.setIndexNames((0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:slePortSrcGuardAddressEntry.setStatus(_A)
_SlePortSrcGuardAddressIp_Type=IpAddress
_SlePortSrcGuardAddressIp_Object=MibTableColumn
slePortSrcGuardAddressIp=_SlePortSrcGuardAddressIp_Object((1,3,6,1,4,1,6296,101,12,2,2,1,1,1),_SlePortSrcGuardAddressIp_Type())
slePortSrcGuardAddressIp.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressIp.setStatus(_A)
_SlePortSrcGuardAddressMask_Type=IpAddress
_SlePortSrcGuardAddressMask_Object=MibTableColumn
slePortSrcGuardAddressMask=_SlePortSrcGuardAddressMask_Object((1,3,6,1,4,1,6296,101,12,2,2,1,1,2),_SlePortSrcGuardAddressMask_Type())
slePortSrcGuardAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressMask.setStatus(_A)
_SlePortSrcGuardAddressMac_Type=MacAddress
_SlePortSrcGuardAddressMac_Object=MibTableColumn
slePortSrcGuardAddressMac=_SlePortSrcGuardAddressMac_Object((1,3,6,1,4,1,6296,101,12,2,2,1,1,3),_SlePortSrcGuardAddressMac_Type())
slePortSrcGuardAddressMac.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressMac.setStatus(_A)
_SlePortSrcGuardAddressLease_Type=Integer32
_SlePortSrcGuardAddressLease_Object=MibTableColumn
slePortSrcGuardAddressLease=_SlePortSrcGuardAddressLease_Object((1,3,6,1,4,1,6296,101,12,2,2,1,1,4),_SlePortSrcGuardAddressLease_Type())
slePortSrcGuardAddressLease.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressLease.setStatus(_A)
_SlePortSrcGuardAddressControl_ObjectIdentity=ObjectIdentity
slePortSrcGuardAddressControl=_SlePortSrcGuardAddressControl_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2,2,2))
class _SlePortSrcGuardAddressControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('createPortSrcGuardAddress',1),('destroyPortSrcGuardAddress',2)))
_SlePortSrcGuardAddressControlRequest_Type.__name__=_E
_SlePortSrcGuardAddressControlRequest_Object=MibScalar
slePortSrcGuardAddressControlRequest=_SlePortSrcGuardAddressControlRequest_Object((1,3,6,1,4,1,6296,101,12,2,2,2,1),_SlePortSrcGuardAddressControlRequest_Type())
slePortSrcGuardAddressControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlRequest.setStatus(_A)
_SlePortSrcGuardAddressControlStatus_Type=SleControlStatusType
_SlePortSrcGuardAddressControlStatus_Object=MibScalar
slePortSrcGuardAddressControlStatus=_SlePortSrcGuardAddressControlStatus_Object((1,3,6,1,4,1,6296,101,12,2,2,2,2),_SlePortSrcGuardAddressControlStatus_Type())
slePortSrcGuardAddressControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlStatus.setStatus(_A)
_SlePortSrcGuardAddressControlTimer_Type=Gauge32
_SlePortSrcGuardAddressControlTimer_Object=MibScalar
slePortSrcGuardAddressControlTimer=_SlePortSrcGuardAddressControlTimer_Object((1,3,6,1,4,1,6296,101,12,2,2,2,3),_SlePortSrcGuardAddressControlTimer_Type())
slePortSrcGuardAddressControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlTimer.setStatus(_A)
_SlePortSrcGuardAddressControlTimeStamp_Type=TimeTicks
_SlePortSrcGuardAddressControlTimeStamp_Object=MibScalar
slePortSrcGuardAddressControlTimeStamp=_SlePortSrcGuardAddressControlTimeStamp_Object((1,3,6,1,4,1,6296,101,12,2,2,2,4),_SlePortSrcGuardAddressControlTimeStamp_Type())
slePortSrcGuardAddressControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlTimeStamp.setStatus(_A)
_SlePortSrcGuardAddressControlReqResult_Type=SleControlRequestResultType
_SlePortSrcGuardAddressControlReqResult_Object=MibScalar
slePortSrcGuardAddressControlReqResult=_SlePortSrcGuardAddressControlReqResult_Object((1,3,6,1,4,1,6296,101,12,2,2,2,5),_SlePortSrcGuardAddressControlReqResult_Type())
slePortSrcGuardAddressControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlReqResult.setStatus(_A)
_SlePortSrcGuardAddressControlIndex_Type=InterfaceIndex
_SlePortSrcGuardAddressControlIndex_Object=MibScalar
slePortSrcGuardAddressControlIndex=_SlePortSrcGuardAddressControlIndex_Object((1,3,6,1,4,1,6296,101,12,2,2,2,6),_SlePortSrcGuardAddressControlIndex_Type())
slePortSrcGuardAddressControlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlIndex.setStatus(_A)
_SlePortSrcGuardAddressControlIp_Type=IpAddress
_SlePortSrcGuardAddressControlIp_Object=MibScalar
slePortSrcGuardAddressControlIp=_SlePortSrcGuardAddressControlIp_Object((1,3,6,1,4,1,6296,101,12,2,2,2,7),_SlePortSrcGuardAddressControlIp_Type())
slePortSrcGuardAddressControlIp.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlIp.setStatus(_A)
_SlePortSrcGuardAddressControlMask_Type=IpAddress
_SlePortSrcGuardAddressControlMask_Object=MibScalar
slePortSrcGuardAddressControlMask=_SlePortSrcGuardAddressControlMask_Object((1,3,6,1,4,1,6296,101,12,2,2,2,8),_SlePortSrcGuardAddressControlMask_Type())
slePortSrcGuardAddressControlMask.setMaxAccess(_D)
if mibBuilder.loadTexts:slePortSrcGuardAddressControlMask.setStatus(_A)
_SlePortSrcGuardAddressNotification_ObjectIdentity=ObjectIdentity
slePortSrcGuardAddressNotification=_SlePortSrcGuardAddressNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,12,2,2,3))
sleGlobalFeatureEnableChanged=NotificationType((1,3,6,1,4,1,6296,101,12,1,3,1))
sleGlobalFeatureEnableChanged.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:sleGlobalFeatureEnableChanged.setStatus(_A)
slePortSrcGuardConfigEnableChanged=NotificationType((1,3,6,1,4,1,6296,101,12,2,1,3,1))
slePortSrcGuardConfigEnableChanged.setObjects(*((_B,_S),(_B,'slePortSrcGuardConfigControlTImeStamp'),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:slePortSrcGuardConfigEnableChanged.setStatus(_A)
slePortSrcGuardAddressCreated=NotificationType((1,3,6,1,4,1,6296,101,12,2,2,3,1))
slePortSrcGuardAddressCreated.setObjects(*((_B,_H),(_B,_V),(_B,_I),(_B,_F),(_B,_J)))
if mibBuilder.loadTexts:slePortSrcGuardAddressCreated.setStatus(_A)
slePortSrcGuardAddressDestroyed=NotificationType((1,3,6,1,4,1,6296,101,12,2,2,3,2))
slePortSrcGuardAddressDestroyed.setObjects(*((_B,_H),(_B,_V),(_B,_I),(_B,_F),(_B,_J)))
if mibBuilder.loadTexts:slePortSrcGuardAddressDestroyed.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sleDhcpSnooping':sleDhcpSnooping,'sleGlobal':sleGlobal,'sleGlobalInfo':sleGlobalInfo,_R:sleFeatureEnable,'sleGlobalControl':sleGlobalControl,_O:sleGlobalControlRequest,'sleGlobalControlStatus':sleGlobalControlStatus,'sleGlobalControlTimer':sleGlobalControlTimer,_P:sleGlobalControlTimeStamp,_Q:sleGlobalControlReqResult,'sleGlobalControlFeatureEnable':sleGlobalControlFeatureEnable,'sleGlobalNotification':sleGlobalNotification,'sleGlobalFeatureEnableChanged':sleGlobalFeatureEnableChanged,'slePortSrcGuard':slePortSrcGuard,'slePortSrcGuardConfig':slePortSrcGuardConfig,'slePortSrcGuardConfigTable':slePortSrcGuardConfigTable,'slePortSrcGuardConfigEntry':slePortSrcGuardConfigEntry,_G:slePortSrcGuardIndex,_U:slePortSrcGuardEnable,'slePortSrcGuardConfigControl':slePortSrcGuardConfigControl,_S:slePortSrcGuardConfigControlRequest,'slePortSrcGuardConfigControlStatus':slePortSrcGuardConfigControlStatus,'slePortSrcGuardConfigControlTimer':slePortSrcGuardConfigControlTimer,'slePortSrcGuardConfigControlTimeStamp':slePortSrcGuardConfigControlTimeStamp,_T:slePortSrcGuardConfigControlReqResult,'slePortSrcGuardConfigControlIndex':slePortSrcGuardConfigControlIndex,'slePortSrcGuardConfigControlEnable':slePortSrcGuardConfigControlEnable,'slePortSrcGuardConfigNotification':slePortSrcGuardConfigNotification,'slePortSrcGuardConfigEnableChanged':slePortSrcGuardConfigEnableChanged,'slePortSrcGuardAddress':slePortSrcGuardAddress,'slePortSrcGuardAddressTable':slePortSrcGuardAddressTable,'slePortSrcGuardAddressEntry':slePortSrcGuardAddressEntry,_F:slePortSrcGuardAddressIp,_J:slePortSrcGuardAddressMask,'slePortSrcGuardAddressMac':slePortSrcGuardAddressMac,'slePortSrcGuardAddressLease':slePortSrcGuardAddressLease,'slePortSrcGuardAddressControl':slePortSrcGuardAddressControl,_H:slePortSrcGuardAddressControlRequest,'slePortSrcGuardAddressControlStatus':slePortSrcGuardAddressControlStatus,'slePortSrcGuardAddressControlTimer':slePortSrcGuardAddressControlTimer,'slePortSrcGuardAddressControlTimeStamp':slePortSrcGuardAddressControlTimeStamp,_I:slePortSrcGuardAddressControlReqResult,'slePortSrcGuardAddressControlIndex':slePortSrcGuardAddressControlIndex,'slePortSrcGuardAddressControlIp':slePortSrcGuardAddressControlIp,'slePortSrcGuardAddressControlMask':slePortSrcGuardAddressControlMask,'slePortSrcGuardAddressNotification':slePortSrcGuardAddressNotification,'slePortSrcGuardAddressCreated':slePortSrcGuardAddressCreated,'slePortSrcGuardAddressDestroyed':slePortSrcGuardAddressDestroyed})