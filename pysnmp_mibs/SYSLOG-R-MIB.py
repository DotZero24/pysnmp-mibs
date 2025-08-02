_q='syslogStatusChanged'
_p='syslogControlRowStatus'
_o='syslogControlStorageType'
_n='syslogControlMaxMessageSize'
_m='syslogOperationsCounterDiscontinuityTime'
_l='syslogOperationsRunIndex'
_k='syslogOperationsLastErrorTime'
_j='syslogOperationsLastError'
_i='syslogOperationsStartTime'
_h='syslogOperationsLastMsgTransmittedTime'
_g='syslogOperationsLastMsgRecdTime'
_f='syslogOperationsMsgsDiscarded'
_e='syslogOperationsMsgsMalFormed'
_d='syslogOperationsMsgsDropped'
_c='syslogOperationsMsgsRelayed'
_b='syslogOperationsMsgsTransmitted'
_a='syslogOperationsMsgsReceived'
_Z='syslogDefaultEncapsulation'
_Y='syslogDefaultService'
_X='syslogOperationsEntry'
_W='syslogControlIndex'
_V='SyslogEncapsulation'
_U='SyslogService'
_T='StorageType'
_S='Unsigned32'
_R='SnmpAdminString'
_Q='syslogControlConfFileName'
_P='syslogControlService'
_O='syslogControlEncapsulation'
_N='syslogControlBindAddr'
_M='syslogControlBindAddrType'
_L='syslogControlRoles'
_K='syslogControlDescr'
_J='syslogOperationsStatus'
_I='Integer32'
_H='syslogNotificationGroup'
_G='syslogControlGroup'
_F='syslogOperationsGroup'
_E='syslogDefaultGroup'
_D='read-create'
_C='read-only'
_B='current'
_A='SYSLOG-R-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
radExperimental,=mibBuilder.importSymbols('RAD-SMI-MIB','radExperimental')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_T,'TextualConvention','TimeStamp')
syslogMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,14))
class SyslogRoles(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('sender',0),('receiver',1),('relay',2)))
class SyslogService(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SyslogEncapsulation(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('none',2),('tls',3),('beep',4)))
_SyslogNotifications_ObjectIdentity=ObjectIdentity
syslogNotifications=_SyslogNotifications_ObjectIdentity((1,3,6,1,4,1,164,20,14,0))
_SyslogObjects_ObjectIdentity=ObjectIdentity
syslogObjects=_SyslogObjects_ObjectIdentity((1,3,6,1,4,1,164,20,14,1))
_SyslogSystem_ObjectIdentity=ObjectIdentity
syslogSystem=_SyslogSystem_ObjectIdentity((1,3,6,1,4,1,164,20,14,1,1))
class _SyslogDefaultService_Type(SyslogService):defaultValue=OctetString('514')
_SyslogDefaultService_Type.__name__=_U
_SyslogDefaultService_Object=MibScalar
syslogDefaultService=_SyslogDefaultService_Object((1,3,6,1,4,1,164,20,14,1,1,1),_SyslogDefaultService_Type())
syslogDefaultService.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDefaultService.setStatus(_B)
class _SyslogDefaultEncapsulation_Type(SyslogEncapsulation):defaultValue=2
_SyslogDefaultEncapsulation_Type.__name__=_V
_SyslogDefaultEncapsulation_Object=MibScalar
syslogDefaultEncapsulation=_SyslogDefaultEncapsulation_Object((1,3,6,1,4,1,164,20,14,1,1,2),_SyslogDefaultEncapsulation_Type())
syslogDefaultEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDefaultEncapsulation.setStatus(_B)
_SyslogControlTable_Object=MibTable
syslogControlTable=_SyslogControlTable_Object((1,3,6,1,4,1,164,20,14,1,2))
if mibBuilder.loadTexts:syslogControlTable.setStatus(_B)
_SyslogControlEntry_Object=MibTableRow
syslogControlEntry=_SyslogControlEntry_Object((1,3,6,1,4,1,164,20,14,1,2,1))
syslogControlEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:syslogControlEntry.setStatus(_B)
class _SyslogControlIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SyslogControlIndex_Type.__name__=_S
_SyslogControlIndex_Object=MibTableColumn
syslogControlIndex=_SyslogControlIndex_Object((1,3,6,1,4,1,164,20,14,1,2,1,1),_SyslogControlIndex_Type())
syslogControlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:syslogControlIndex.setStatus(_B)
_SyslogControlDescr_Type=SnmpAdminString
_SyslogControlDescr_Object=MibTableColumn
syslogControlDescr=_SyslogControlDescr_Object((1,3,6,1,4,1,164,20,14,1,2,1,2),_SyslogControlDescr_Type())
syslogControlDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlDescr.setStatus(_B)
_SyslogControlRoles_Type=SyslogRoles
_SyslogControlRoles_Object=MibTableColumn
syslogControlRoles=_SyslogControlRoles_Object((1,3,6,1,4,1,164,20,14,1,2,1,3),_SyslogControlRoles_Type())
syslogControlRoles.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlRoles.setStatus(_B)
_SyslogControlBindAddrType_Type=InetAddressType
_SyslogControlBindAddrType_Object=MibTableColumn
syslogControlBindAddrType=_SyslogControlBindAddrType_Object((1,3,6,1,4,1,164,20,14,1,2,1,4),_SyslogControlBindAddrType_Type())
syslogControlBindAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlBindAddrType.setStatus(_B)
_SyslogControlBindAddr_Type=InetAddress
_SyslogControlBindAddr_Object=MibTableColumn
syslogControlBindAddr=_SyslogControlBindAddr_Object((1,3,6,1,4,1,164,20,14,1,2,1,5),_SyslogControlBindAddr_Type())
syslogControlBindAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlBindAddr.setStatus(_B)
_SyslogControlService_Type=SyslogService
_SyslogControlService_Object=MibTableColumn
syslogControlService=_SyslogControlService_Object((1,3,6,1,4,1,164,20,14,1,2,1,6),_SyslogControlService_Type())
syslogControlService.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlService.setStatus(_B)
_SyslogControlEncapsulation_Type=SyslogEncapsulation
_SyslogControlEncapsulation_Object=MibTableColumn
syslogControlEncapsulation=_SyslogControlEncapsulation_Object((1,3,6,1,4,1,164,20,14,1,2,1,7),_SyslogControlEncapsulation_Type())
syslogControlEncapsulation.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlEncapsulation.setStatus(_B)
_SyslogControlMaxMessageSize_Type=Unsigned32
_SyslogControlMaxMessageSize_Object=MibTableColumn
syslogControlMaxMessageSize=_SyslogControlMaxMessageSize_Object((1,3,6,1,4,1,164,20,14,1,2,1,8),_SyslogControlMaxMessageSize_Type())
syslogControlMaxMessageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlMaxMessageSize.setStatus(_B)
class _SyslogControlConfFileName_Type(SnmpAdminString):defaultValue=OctetString('/etc/syslog.conf')
_SyslogControlConfFileName_Type.__name__=_R
_SyslogControlConfFileName_Object=MibTableColumn
syslogControlConfFileName=_SyslogControlConfFileName_Object((1,3,6,1,4,1,164,20,14,1,2,1,9),_SyslogControlConfFileName_Type())
syslogControlConfFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlConfFileName.setStatus(_B)
class _SyslogControlStorageType_Type(StorageType):defaultValue=3
_SyslogControlStorageType_Type.__name__=_T
_SyslogControlStorageType_Object=MibTableColumn
syslogControlStorageType=_SyslogControlStorageType_Object((1,3,6,1,4,1,164,20,14,1,2,1,11),_SyslogControlStorageType_Type())
syslogControlStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlStorageType.setStatus(_B)
_SyslogControlRowStatus_Type=RowStatus
_SyslogControlRowStatus_Object=MibTableColumn
syslogControlRowStatus=_SyslogControlRowStatus_Object((1,3,6,1,4,1,164,20,14,1,2,1,12),_SyslogControlRowStatus_Type())
syslogControlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlRowStatus.setStatus(_B)
class _SyslogControlAccountingType_Type(Bits):namedValues=NamedValues(*(('shell',0),('system',1),('commands',2)))
_SyslogControlAccountingType_Type.__name__='Bits'
_SyslogControlAccountingType_Object=MibTableColumn
syslogControlAccountingType=_SyslogControlAccountingType_Object((1,3,6,1,4,1,164,20,14,1,2,1,13),_SyslogControlAccountingType_Type())
syslogControlAccountingType.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogControlAccountingType.setStatus(_B)
_SyslogOperationsTable_Object=MibTable
syslogOperationsTable=_SyslogOperationsTable_Object((1,3,6,1,4,1,164,20,14,1,3))
if mibBuilder.loadTexts:syslogOperationsTable.setStatus(_B)
_SyslogOperationsEntry_Object=MibTableRow
syslogOperationsEntry=_SyslogOperationsEntry_Object((1,3,6,1,4,1,164,20,14,1,3,1))
if mibBuilder.loadTexts:syslogOperationsEntry.setStatus(_B)
_SyslogOperationsMsgsReceived_Type=Counter32
_SyslogOperationsMsgsReceived_Object=MibTableColumn
syslogOperationsMsgsReceived=_SyslogOperationsMsgsReceived_Object((1,3,6,1,4,1,164,20,14,1,3,1,1),_SyslogOperationsMsgsReceived_Type())
syslogOperationsMsgsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsMsgsReceived.setStatus(_B)
_SyslogOperationsMsgsTransmitted_Type=Counter32
_SyslogOperationsMsgsTransmitted_Object=MibTableColumn
syslogOperationsMsgsTransmitted=_SyslogOperationsMsgsTransmitted_Object((1,3,6,1,4,1,164,20,14,1,3,1,2),_SyslogOperationsMsgsTransmitted_Type())
syslogOperationsMsgsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsMsgsTransmitted.setStatus(_B)
_SyslogOperationsMsgsRelayed_Type=Counter32
_SyslogOperationsMsgsRelayed_Object=MibTableColumn
syslogOperationsMsgsRelayed=_SyslogOperationsMsgsRelayed_Object((1,3,6,1,4,1,164,20,14,1,3,1,3),_SyslogOperationsMsgsRelayed_Type())
syslogOperationsMsgsRelayed.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsMsgsRelayed.setStatus(_B)
_SyslogOperationsMsgsDropped_Type=Counter32
_SyslogOperationsMsgsDropped_Object=MibTableColumn
syslogOperationsMsgsDropped=_SyslogOperationsMsgsDropped_Object((1,3,6,1,4,1,164,20,14,1,3,1,4),_SyslogOperationsMsgsDropped_Type())
syslogOperationsMsgsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsMsgsDropped.setStatus(_B)
_SyslogOperationsMsgsMalFormed_Type=Counter32
_SyslogOperationsMsgsMalFormed_Object=MibTableColumn
syslogOperationsMsgsMalFormed=_SyslogOperationsMsgsMalFormed_Object((1,3,6,1,4,1,164,20,14,1,3,1,5),_SyslogOperationsMsgsMalFormed_Type())
syslogOperationsMsgsMalFormed.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsMsgsMalFormed.setStatus(_B)
_SyslogOperationsMsgsDiscarded_Type=Counter32
_SyslogOperationsMsgsDiscarded_Object=MibTableColumn
syslogOperationsMsgsDiscarded=_SyslogOperationsMsgsDiscarded_Object((1,3,6,1,4,1,164,20,14,1,3,1,6),_SyslogOperationsMsgsDiscarded_Type())
syslogOperationsMsgsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsMsgsDiscarded.setStatus(_B)
_SyslogOperationsLastMsgRecdTime_Type=TimeStamp
_SyslogOperationsLastMsgRecdTime_Object=MibTableColumn
syslogOperationsLastMsgRecdTime=_SyslogOperationsLastMsgRecdTime_Object((1,3,6,1,4,1,164,20,14,1,3,1,7),_SyslogOperationsLastMsgRecdTime_Type())
syslogOperationsLastMsgRecdTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsLastMsgRecdTime.setStatus(_B)
_SyslogOperationsLastMsgTransmittedTime_Type=TimeStamp
_SyslogOperationsLastMsgTransmittedTime_Object=MibTableColumn
syslogOperationsLastMsgTransmittedTime=_SyslogOperationsLastMsgTransmittedTime_Object((1,3,6,1,4,1,164,20,14,1,3,1,8),_SyslogOperationsLastMsgTransmittedTime_Type())
syslogOperationsLastMsgTransmittedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsLastMsgTransmittedTime.setStatus(_B)
_SyslogOperationsStartTime_Type=TimeStamp
_SyslogOperationsStartTime_Object=MibTableColumn
syslogOperationsStartTime=_SyslogOperationsStartTime_Object((1,3,6,1,4,1,164,20,14,1,3,1,9),_SyslogOperationsStartTime_Type())
syslogOperationsStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsStartTime.setStatus(_B)
_SyslogOperationsLastError_Type=SnmpAdminString
_SyslogOperationsLastError_Object=MibTableColumn
syslogOperationsLastError=_SyslogOperationsLastError_Object((1,3,6,1,4,1,164,20,14,1,3,1,10),_SyslogOperationsLastError_Type())
syslogOperationsLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsLastError.setStatus(_B)
_SyslogOperationsLastErrorTime_Type=TimeStamp
_SyslogOperationsLastErrorTime_Object=MibTableColumn
syslogOperationsLastErrorTime=_SyslogOperationsLastErrorTime_Object((1,3,6,1,4,1,164,20,14,1,3,1,11),_SyslogOperationsLastErrorTime_Type())
syslogOperationsLastErrorTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsLastErrorTime.setStatus(_B)
class _SyslogOperationsRunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SyslogOperationsRunIndex_Type.__name__=_I
_SyslogOperationsRunIndex_Object=MibTableColumn
syslogOperationsRunIndex=_SyslogOperationsRunIndex_Object((1,3,6,1,4,1,164,20,14,1,3,1,12),_SyslogOperationsRunIndex_Type())
syslogOperationsRunIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsRunIndex.setStatus(_B)
_SyslogOperationsCounterDiscontinuityTime_Type=TimeStamp
_SyslogOperationsCounterDiscontinuityTime_Object=MibTableColumn
syslogOperationsCounterDiscontinuityTime=_SyslogOperationsCounterDiscontinuityTime_Object((1,3,6,1,4,1,164,20,14,1,3,1,13),_SyslogOperationsCounterDiscontinuityTime_Type())
syslogOperationsCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsCounterDiscontinuityTime.setStatus(_B)
class _SyslogOperationsStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('started',2),('suspended',3),('stopped',4)))
_SyslogOperationsStatus_Type.__name__=_I
_SyslogOperationsStatus_Object=MibTableColumn
syslogOperationsStatus=_SyslogOperationsStatus_Object((1,3,6,1,4,1,164,20,14,1,3,1,14),_SyslogOperationsStatus_Type())
syslogOperationsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogOperationsStatus.setStatus(_B)
_SyslogConformance_ObjectIdentity=ObjectIdentity
syslogConformance=_SyslogConformance_ObjectIdentity((1,3,6,1,4,1,164,20,14,3))
_SyslogGroups_ObjectIdentity=ObjectIdentity
syslogGroups=_SyslogGroups_ObjectIdentity((1,3,6,1,4,1,164,20,14,3,1))
_SyslogCompliances_ObjectIdentity=ObjectIdentity
syslogCompliances=_SyslogCompliances_ObjectIdentity((1,3,6,1,4,1,164,20,14,3,2))
syslogControlEntry.registerAugmentions((_A,_X))
syslogOperationsEntry.setIndexNames(*syslogControlEntry.getIndexNames())
syslogDefaultGroup=ObjectGroup((1,3,6,1,4,1,164,20,14,3,1,1))
syslogDefaultGroup.setObjects(*((_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:syslogDefaultGroup.setStatus(_B)
syslogOperationsGroup=ObjectGroup((1,3,6,1,4,1,164,20,14,3,1,2))
syslogOperationsGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_J)))
if mibBuilder.loadTexts:syslogOperationsGroup.setStatus(_B)
syslogControlGroup=ObjectGroup((1,3,6,1,4,1,164,20,14,3,1,3))
syslogControlGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_n),(_A,_Q),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:syslogControlGroup.setStatus(_B)
syslogStatusChanged=NotificationType((1,3,6,1,4,1,164,20,14,0,1))
syslogStatusChanged.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_O),(_A,_Q),(_A,_J)))
if mibBuilder.loadTexts:syslogStatusChanged.setStatus(_B)
syslogNotificationGroup=NotificationGroup((1,3,6,1,4,1,164,20,14,3,1,4))
syslogNotificationGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:syslogNotificationGroup.setStatus(_B)
syslogFullCompliance1=ModuleCompliance((1,3,6,1,4,1,164,20,14,3,2,1))
syslogFullCompliance1.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:syslogFullCompliance1.setStatus(_B)
syslogFullCompliance2=ModuleCompliance((1,3,6,1,4,1,164,20,14,3,2,2))
syslogFullCompliance2.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:syslogFullCompliance2.setStatus(_B)
syslogReadOnlyCompliance1=ModuleCompliance((1,3,6,1,4,1,164,20,14,3,2,3))
syslogReadOnlyCompliance1.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:syslogReadOnlyCompliance1.setStatus(_B)
syslogReadOnlyCompliance2=ModuleCompliance((1,3,6,1,4,1,164,20,14,3,2,4))
syslogReadOnlyCompliance2.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:syslogReadOnlyCompliance2.setStatus(_B)
syslogNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,14,3,2,5))
syslogNotificationCompliance.setObjects((_A,_H))
if mibBuilder.loadTexts:syslogNotificationCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SyslogRoles':SyslogRoles,_U:SyslogService,_V:SyslogEncapsulation,'syslogMIBR':syslogMIBR,'syslogNotifications':syslogNotifications,_q:syslogStatusChanged,'syslogObjects':syslogObjects,'syslogSystem':syslogSystem,_Y:syslogDefaultService,_Z:syslogDefaultEncapsulation,'syslogControlTable':syslogControlTable,'syslogControlEntry':syslogControlEntry,_W:syslogControlIndex,_K:syslogControlDescr,_L:syslogControlRoles,_M:syslogControlBindAddrType,_N:syslogControlBindAddr,_P:syslogControlService,_O:syslogControlEncapsulation,_n:syslogControlMaxMessageSize,_Q:syslogControlConfFileName,_o:syslogControlStorageType,_p:syslogControlRowStatus,'syslogControlAccountingType':syslogControlAccountingType,'syslogOperationsTable':syslogOperationsTable,_X:syslogOperationsEntry,_a:syslogOperationsMsgsReceived,_b:syslogOperationsMsgsTransmitted,_c:syslogOperationsMsgsRelayed,_d:syslogOperationsMsgsDropped,_e:syslogOperationsMsgsMalFormed,_f:syslogOperationsMsgsDiscarded,_g:syslogOperationsLastMsgRecdTime,_h:syslogOperationsLastMsgTransmittedTime,_i:syslogOperationsStartTime,_j:syslogOperationsLastError,_k:syslogOperationsLastErrorTime,_l:syslogOperationsRunIndex,_m:syslogOperationsCounterDiscontinuityTime,_J:syslogOperationsStatus,'syslogConformance':syslogConformance,'syslogGroups':syslogGroups,_E:syslogDefaultGroup,_F:syslogOperationsGroup,_G:syslogControlGroup,_H:syslogNotificationGroup,'syslogCompliances':syslogCompliances,'syslogFullCompliance1':syslogFullCompliance1,'syslogFullCompliance2':syslogFullCompliance2,'syslogReadOnlyCompliance1':syslogReadOnlyCompliance1,'syslogReadOnlyCompliance2':syslogReadOnlyCompliance2,'syslogNotificationCompliance':syslogNotificationCompliance})