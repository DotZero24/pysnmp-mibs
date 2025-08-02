_f='tmnxDiscoveryNotificationGroup'
_e='tmnxDiscoveryGrpNotifyObjs'
_d='tmnxDiscoveryGroup'
_c='tmnxDiscoveryEndNotify'
_b='tmnxDiscoveryCellularReq'
_a='tmnxSbiDiscoverReqDest2'
_Z='tmnxSbiDiscoverReqDest1'
_Y='tmnxSbiDiscoverConfig'
_X='tmnxDiscoveryEndTime'
_W='tmnxDiscoveryStartTime'
_V='tmnxDiscoveryStatus'
_U='read-only'
_T='complete'
_S='tmnxPortNotifyPortId'
_R='TIMETRA-PORT-MIB'
_Q='tmnxChassisIndex'
_P='TruthValue'
_O='Integer32'
_N='tmnxAdpNotifySwVersion'
_M='tmnxAdpNotifyEndReason'
_L='tmnxAdpNotifyCellPdnIpAddr'
_K='tmnxAdpNotifyCellPdnIpAddrType'
_J='tmnxAdpNotifyCellSimCardImsi'
_I='tmnxAdpNotifyCellSimCardId'
_H='tmnxChassisNotifyChassisId'
_G='DisplayString'
_F='tmnxAdpNotifyChassisSerialNum'
_E='read-write'
_D='TIMETRA-CHASSIS-MIB'
_C='accessible-for-notify'
_B='current'
_A='TIMETRA-DISCOVERY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
TmnxCellularImsi,TmnxCellularSimCardNumber=mibBuilder.importSymbols('TIMETRA-CELLULAR-MIB','TmnxCellularImsi','TmnxCellularSimCardNumber')
tmnxChassisIndex,tmnxChassisNotifyChassisId=mibBuilder.importSymbols(_D,_Q,_H)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tmnxPortNotifyPortId,=mibBuilder.importSymbols(_R,_S)
tmnxDiscoveryMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,112))
if mibBuilder.loadTexts:tmnxDiscoveryMIBModule.setRevisions(('2017-03-09 00:00',))
class TmnxDiscoveryStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noDiscovery',0),('connecting',1),('requestingConfig',2),('terminated',3),(_T,4)))
_TmnxDiscoveryMIBConformance_ObjectIdentity=ObjectIdentity
tmnxDiscoveryMIBConformance=_TmnxDiscoveryMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,112))
_TmnxDiscoveryConformance_ObjectIdentity=ObjectIdentity
tmnxDiscoveryConformance=_TmnxDiscoveryConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,112,1))
_TmnxDiscoveryCompliances_ObjectIdentity=ObjectIdentity
tmnxDiscoveryCompliances=_TmnxDiscoveryCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,112,1,1))
_TmnxDiscoveryGroups_ObjectIdentity=ObjectIdentity
tmnxDiscoveryGroups=_TmnxDiscoveryGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,112,1,2))
_TmnxDiscoveryObjs_ObjectIdentity=ObjectIdentity
tmnxDiscoveryObjs=_TmnxDiscoveryObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,112))
_TmnxDiscoveryNotifyObjs_ObjectIdentity=ObjectIdentity
tmnxDiscoveryNotifyObjs=_TmnxDiscoveryNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,112,1))
_TmnxAdpNotifyChassisSerialNum_Type=SnmpAdminString
_TmnxAdpNotifyChassisSerialNum_Object=MibScalar
tmnxAdpNotifyChassisSerialNum=_TmnxAdpNotifyChassisSerialNum_Object((1,3,6,1,4,1,6527,3,1,2,112,1,1),_TmnxAdpNotifyChassisSerialNum_Type())
tmnxAdpNotifyChassisSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifyChassisSerialNum.setStatus(_B)
_TmnxAdpNotifyCellSimCardId_Type=TmnxCellularSimCardNumber
_TmnxAdpNotifyCellSimCardId_Object=MibScalar
tmnxAdpNotifyCellSimCardId=_TmnxAdpNotifyCellSimCardId_Object((1,3,6,1,4,1,6527,3,1,2,112,1,2),_TmnxAdpNotifyCellSimCardId_Type())
tmnxAdpNotifyCellSimCardId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifyCellSimCardId.setStatus(_B)
_TmnxAdpNotifyCellSimCardImsi_Type=TmnxCellularImsi
_TmnxAdpNotifyCellSimCardImsi_Object=MibScalar
tmnxAdpNotifyCellSimCardImsi=_TmnxAdpNotifyCellSimCardImsi_Object((1,3,6,1,4,1,6527,3,1,2,112,1,3),_TmnxAdpNotifyCellSimCardImsi_Type())
tmnxAdpNotifyCellSimCardImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifyCellSimCardImsi.setStatus(_B)
_TmnxAdpNotifyCellPdnIpAddrType_Type=InetAddressType
_TmnxAdpNotifyCellPdnIpAddrType_Object=MibScalar
tmnxAdpNotifyCellPdnIpAddrType=_TmnxAdpNotifyCellPdnIpAddrType_Object((1,3,6,1,4,1,6527,3,1,2,112,1,4),_TmnxAdpNotifyCellPdnIpAddrType_Type())
tmnxAdpNotifyCellPdnIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifyCellPdnIpAddrType.setStatus(_B)
_TmnxAdpNotifyCellPdnIpAddr_Type=InetAddress
_TmnxAdpNotifyCellPdnIpAddr_Object=MibScalar
tmnxAdpNotifyCellPdnIpAddr=_TmnxAdpNotifyCellPdnIpAddr_Object((1,3,6,1,4,1,6527,3,1,2,112,1,5),_TmnxAdpNotifyCellPdnIpAddr_Type())
tmnxAdpNotifyCellPdnIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifyCellPdnIpAddr.setStatus(_B)
class _TmnxAdpNotifyEndReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operatorTerminated',1),(_T,2)))
_TmnxAdpNotifyEndReason_Type.__name__=_O
_TmnxAdpNotifyEndReason_Object=MibScalar
tmnxAdpNotifyEndReason=_TmnxAdpNotifyEndReason_Object((1,3,6,1,4,1,6527,3,1,2,112,1,6),_TmnxAdpNotifyEndReason_Type())
tmnxAdpNotifyEndReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifyEndReason.setStatus(_B)
_TmnxAdpNotifySwVersion_Type=DisplayString
_TmnxAdpNotifySwVersion_Object=MibScalar
tmnxAdpNotifySwVersion=_TmnxAdpNotifySwVersion_Object((1,3,6,1,4,1,6527,3,1,2,112,1,7),_TmnxAdpNotifySwVersion_Type())
tmnxAdpNotifySwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxAdpNotifySwVersion.setStatus(_B)
_TmnxDiscoveryTable_Object=MibTable
tmnxDiscoveryTable=_TmnxDiscoveryTable_Object((1,3,6,1,4,1,6527,3,1,2,112,2))
if mibBuilder.loadTexts:tmnxDiscoveryTable.setStatus(_B)
_TmnxDiscoveryEntry_Object=MibTableRow
tmnxDiscoveryEntry=_TmnxDiscoveryEntry_Object((1,3,6,1,4,1,6527,3,1,2,112,2,1))
tmnxDiscoveryEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:tmnxDiscoveryEntry.setStatus(_B)
_TmnxDiscoveryStatus_Type=TmnxDiscoveryStatus
_TmnxDiscoveryStatus_Object=MibTableColumn
tmnxDiscoveryStatus=_TmnxDiscoveryStatus_Object((1,3,6,1,4,1,6527,3,1,2,112,2,1,1),_TmnxDiscoveryStatus_Type())
tmnxDiscoveryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxDiscoveryStatus.setStatus(_B)
_TmnxDiscoveryStartTime_Type=TimeStamp
_TmnxDiscoveryStartTime_Object=MibTableColumn
tmnxDiscoveryStartTime=_TmnxDiscoveryStartTime_Object((1,3,6,1,4,1,6527,3,1,2,112,2,1,2),_TmnxDiscoveryStartTime_Type())
tmnxDiscoveryStartTime.setMaxAccess(_U)
if mibBuilder.loadTexts:tmnxDiscoveryStartTime.setStatus(_B)
_TmnxDiscoveryEndTime_Type=TimeStamp
_TmnxDiscoveryEndTime_Object=MibTableColumn
tmnxDiscoveryEndTime=_TmnxDiscoveryEndTime_Object((1,3,6,1,4,1,6527,3,1,2,112,2,1,3),_TmnxDiscoveryEndTime_Type())
tmnxDiscoveryEndTime.setMaxAccess(_U)
if mibBuilder.loadTexts:tmnxDiscoveryEndTime.setStatus(_B)
_TmnxDiscoveryBofInfo_ObjectIdentity=ObjectIdentity
tmnxDiscoveryBofInfo=_TmnxDiscoveryBofInfo_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,112,3))
class _TmnxSbiDiscoverConfig_Type(TruthValue):defaultValue=2
_TmnxSbiDiscoverConfig_Type.__name__=_P
_TmnxSbiDiscoverConfig_Object=MibScalar
tmnxSbiDiscoverConfig=_TmnxSbiDiscoverConfig_Object((1,3,6,1,4,1,6527,3,1,2,112,3,1),_TmnxSbiDiscoverConfig_Type())
tmnxSbiDiscoverConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSbiDiscoverConfig.setStatus(_B)
class _TmnxSbiDiscoverReqDest1_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_TmnxSbiDiscoverReqDest1_Type.__name__=_G
_TmnxSbiDiscoverReqDest1_Object=MibScalar
tmnxSbiDiscoverReqDest1=_TmnxSbiDiscoverReqDest1_Object((1,3,6,1,4,1,6527,3,1,2,112,3,2),_TmnxSbiDiscoverReqDest1_Type())
tmnxSbiDiscoverReqDest1.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSbiDiscoverReqDest1.setStatus(_B)
class _TmnxSbiDiscoverReqDest2_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_TmnxSbiDiscoverReqDest2_Type.__name__=_G
_TmnxSbiDiscoverReqDest2_Object=MibScalar
tmnxSbiDiscoverReqDest2=_TmnxSbiDiscoverReqDest2_Object((1,3,6,1,4,1,6527,3,1,2,112,3,3),_TmnxSbiDiscoverReqDest2_Type())
tmnxSbiDiscoverReqDest2.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSbiDiscoverReqDest2.setStatus(_B)
_TmnxDiscoveryNotificationsPrefix_ObjectIdentity=ObjectIdentity
tmnxDiscoveryNotificationsPrefix=_TmnxDiscoveryNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,112))
_TmnxDiscoveryNotifications_ObjectIdentity=ObjectIdentity
tmnxDiscoveryNotifications=_TmnxDiscoveryNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,112,0))
tmnxDiscoveryGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,112,1,2,1))
tmnxDiscoveryGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:tmnxDiscoveryGroup.setStatus(_B)
tmnxDiscoveryGrpNotifyObjs=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,112,1,2,2))
tmnxDiscoveryGrpNotifyObjs.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:tmnxDiscoveryGrpNotifyObjs.setStatus(_B)
tmnxDiscoveryCellularReq=NotificationType((1,3,6,1,4,1,6527,3,1,3,112,0,1))
tmnxDiscoveryCellularReq.setObjects(*((_D,_H),(_R,_S),(_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_N)))
if mibBuilder.loadTexts:tmnxDiscoveryCellularReq.setStatus(_B)
tmnxDiscoveryEndNotify=NotificationType((1,3,6,1,4,1,6527,3,1,3,112,0,2))
tmnxDiscoveryEndNotify.setObjects(*((_D,_H),(_A,_F),(_A,_M)))
if mibBuilder.loadTexts:tmnxDiscoveryEndNotify.setStatus(_B)
tmnxDiscoveryNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,112,1,2,3))
tmnxDiscoveryNotificationGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:tmnxDiscoveryNotificationGroup.setStatus(_B)
aluDiscoveryCompV1v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,112,1,1,1))
aluDiscoveryCompV1v0.setObjects(*((_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:aluDiscoveryCompV1v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TmnxDiscoveryStatus':TmnxDiscoveryStatus,'tmnxDiscoveryMIBModule':tmnxDiscoveryMIBModule,'tmnxDiscoveryMIBConformance':tmnxDiscoveryMIBConformance,'tmnxDiscoveryConformance':tmnxDiscoveryConformance,'tmnxDiscoveryCompliances':tmnxDiscoveryCompliances,'aluDiscoveryCompV1v0':aluDiscoveryCompV1v0,'tmnxDiscoveryGroups':tmnxDiscoveryGroups,_d:tmnxDiscoveryGroup,_e:tmnxDiscoveryGrpNotifyObjs,_f:tmnxDiscoveryNotificationGroup,'tmnxDiscoveryObjs':tmnxDiscoveryObjs,'tmnxDiscoveryNotifyObjs':tmnxDiscoveryNotifyObjs,_F:tmnxAdpNotifyChassisSerialNum,_I:tmnxAdpNotifyCellSimCardId,_J:tmnxAdpNotifyCellSimCardImsi,_K:tmnxAdpNotifyCellPdnIpAddrType,_L:tmnxAdpNotifyCellPdnIpAddr,_M:tmnxAdpNotifyEndReason,_N:tmnxAdpNotifySwVersion,'tmnxDiscoveryTable':tmnxDiscoveryTable,'tmnxDiscoveryEntry':tmnxDiscoveryEntry,_V:tmnxDiscoveryStatus,_W:tmnxDiscoveryStartTime,_X:tmnxDiscoveryEndTime,'tmnxDiscoveryBofInfo':tmnxDiscoveryBofInfo,_Y:tmnxSbiDiscoverConfig,_Z:tmnxSbiDiscoverReqDest1,_a:tmnxSbiDiscoverReqDest2,'tmnxDiscoveryNotificationsPrefix':tmnxDiscoveryNotificationsPrefix,'tmnxDiscoveryNotifications':tmnxDiscoveryNotifications,_b:tmnxDiscoveryCellularReq,_c:tmnxDiscoveryEndNotify})