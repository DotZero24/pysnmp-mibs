_j='ciscoVisionDmpGroup'
_i='ciscoVdHdmiUpDwnNotifs'
_h='ciscoVdNtpNotifs'
_g='ciscoVdBackupTaskNotifs'
_f='ciscoVdServiceStatusNotifs'
_e='ssCpuRawIdle'
_d='ssCpuRawUser'
_c='ciscoVisionDmpPktErrCnt'
_b='ciscoVisionDmpPktCnt'
_a='ciscoVisionDmpBytesOut'
_Z='ciscoVisionDmpBytesIn'
_Y='ciscoVisionDmpInterfaceDesc'
_X='ciscoVisionDmpPTPDeviation'
_W='ciscoVisionDmpPTPMaster'
_V='ciscoVisionDmpPTPstatus'
_U='ciscoVisionDmpNtpStatus'
_T='ciscoVisionDmpTvOnOff'
_S='ciscoVdDmpStatus'
_R='ciscoVdDmpIP'
_Q='not-accessible'
_P='ciscoVdDsdServiceName'
_O='ciscoVisiondsdMIBNotifsGroup'
_N='ciscoVisiondsdDmpGroup'
_M='ciscoVisiondsdSvcGroup'
_L='ciscoVdDmpidentifier'
_K='ciscoVdHdmiUpDownStatus'
_J='ciscoVdDsdServiceDesc'
_I='ciscoVdBkpStatus'
_H='ciscoVdNtpSyncStatus'
_G='ciscoVdDsdServiceStatus'
_F='accessible-for-notify'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-VISION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoVisionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1051))
if mibBuilder.loadTexts:ciscoVisionMIB.setRevisions(('2021-02-08 00:00',))
_CiscoVisionMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVisionMIBNotifs=_CiscoVisionMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,1051,0))
_CiscoVisionMIBConform_ObjectIdentity=ObjectIdentity
ciscoVisionMIBConform=_CiscoVisionMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,1051,1))
_CiscoVisionMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVisionMIBCompliances=_CiscoVisionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,1051,1,1))
_CiscoVisionMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVisionMIBGroups=_CiscoVisionMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1051,1,2))
_CiscoVisionDsd_ObjectIdentity=ObjectIdentity
ciscoVisionDsd=_CiscoVisionDsd_ObjectIdentity((1,3,6,1,4,1,9,9,1051,2))
_CiscoVdService_ObjectIdentity=ObjectIdentity
ciscoVdService=_CiscoVdService_ObjectIdentity((1,3,6,1,4,1,9,9,1051,2,1))
_CiscoVdServiceTable_Object=MibTable
ciscoVdServiceTable=_CiscoVdServiceTable_Object((1,3,6,1,4,1,9,9,1051,2,1,1))
if mibBuilder.loadTexts:ciscoVdServiceTable.setStatus(_B)
_CiscoVdServiceEntry_Object=MibTableRow
ciscoVdServiceEntry=_CiscoVdServiceEntry_Object((1,3,6,1,4,1,9,9,1051,2,1,1,1))
ciscoVdServiceEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:ciscoVdServiceEntry.setStatus(_B)
class _CiscoVdDsdServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CiscoVdDsdServiceName_Type.__name__=_E
_CiscoVdDsdServiceName_Object=MibTableColumn
ciscoVdDsdServiceName=_CiscoVdDsdServiceName_Object((1,3,6,1,4,1,9,9,1051,2,1,1,1,1),_CiscoVdDsdServiceName_Type())
ciscoVdDsdServiceName.setMaxAccess(_Q)
if mibBuilder.loadTexts:ciscoVdDsdServiceName.setStatus(_B)
class _CiscoVdDsdServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVdDsdServiceStatus_Type.__name__=_D
_CiscoVdDsdServiceStatus_Object=MibTableColumn
ciscoVdDsdServiceStatus=_CiscoVdDsdServiceStatus_Object((1,3,6,1,4,1,9,9,1051,2,1,1,1,2),_CiscoVdDsdServiceStatus_Type())
ciscoVdDsdServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdDsdServiceStatus.setStatus(_B)
_CiscoVdDsdServiceDesc_Type=DisplayString
_CiscoVdDsdServiceDesc_Object=MibTableColumn
ciscoVdDsdServiceDesc=_CiscoVdDsdServiceDesc_Object((1,3,6,1,4,1,9,9,1051,2,1,1,1,3),_CiscoVdDsdServiceDesc_Type())
ciscoVdDsdServiceDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdDsdServiceDesc.setStatus(_B)
_CiscoVdDmpsStatuses_ObjectIdentity=ObjectIdentity
ciscoVdDmpsStatuses=_CiscoVdDmpsStatuses_ObjectIdentity((1,3,6,1,4,1,9,9,1051,2,2))
_CiscoVdDmpStatusTable_Object=MibTable
ciscoVdDmpStatusTable=_CiscoVdDmpStatusTable_Object((1,3,6,1,4,1,9,9,1051,2,2,1))
if mibBuilder.loadTexts:ciscoVdDmpStatusTable.setStatus(_B)
_CiscoVdDmpStatusEntry_Object=MibTableRow
ciscoVdDmpStatusEntry=_CiscoVdDmpStatusEntry_Object((1,3,6,1,4,1,9,9,1051,2,2,1,1))
ciscoVdDmpStatusEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:ciscoVdDmpStatusEntry.setStatus(_B)
_CiscoVdDmpIP_Type=IpAddress
_CiscoVdDmpIP_Object=MibTableColumn
ciscoVdDmpIP=_CiscoVdDmpIP_Object((1,3,6,1,4,1,9,9,1051,2,2,1,1,1),_CiscoVdDmpIP_Type())
ciscoVdDmpIP.setMaxAccess(_Q)
if mibBuilder.loadTexts:ciscoVdDmpIP.setStatus(_B)
class _CiscoVdHdmiUpDownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVdHdmiUpDownStatus_Type.__name__=_D
_CiscoVdHdmiUpDownStatus_Object=MibTableColumn
ciscoVdHdmiUpDownStatus=_CiscoVdHdmiUpDownStatus_Object((1,3,6,1,4,1,9,9,1051,2,2,1,1,2),_CiscoVdHdmiUpDownStatus_Type())
ciscoVdHdmiUpDownStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdHdmiUpDownStatus.setStatus(_B)
class _CiscoVdDmpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVdDmpStatus_Type.__name__=_D
_CiscoVdDmpStatus_Object=MibTableColumn
ciscoVdDmpStatus=_CiscoVdDmpStatus_Object((1,3,6,1,4,1,9,9,1051,2,2,1,1,3),_CiscoVdDmpStatus_Type())
ciscoVdDmpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdDmpStatus.setStatus(_B)
class _CiscoVdDmpidentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoVdDmpidentifier_Type.__name__=_E
_CiscoVdDmpidentifier_Object=MibTableColumn
ciscoVdDmpidentifier=_CiscoVdDmpidentifier_Object((1,3,6,1,4,1,9,9,1051,2,2,1,1,4),_CiscoVdDmpidentifier_Type())
ciscoVdDmpidentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdDmpidentifier.setStatus(_B)
class _CiscoVdNtpSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVdNtpSyncStatus_Type.__name__=_D
_CiscoVdNtpSyncStatus_Object=MibScalar
ciscoVdNtpSyncStatus=_CiscoVdNtpSyncStatus_Object((1,3,6,1,4,1,9,9,1051,2,3),_CiscoVdNtpSyncStatus_Type())
ciscoVdNtpSyncStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciscoVdNtpSyncStatus.setStatus(_B)
class _CiscoVdBkpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVdBkpStatus_Type.__name__=_D
_CiscoVdBkpStatus_Object=MibScalar
ciscoVdBkpStatus=_CiscoVdBkpStatus_Object((1,3,6,1,4,1,9,9,1051,2,4),_CiscoVdBkpStatus_Type())
ciscoVdBkpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoVdBkpStatus.setStatus(_B)
_CiscoVisionDmp_ObjectIdentity=ObjectIdentity
ciscoVisionDmp=_CiscoVisionDmp_ObjectIdentity((1,3,6,1,4,1,9,9,1051,3))
class _CiscoVisionDmpTvOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVisionDmpTvOnOff_Type.__name__=_D
_CiscoVisionDmpTvOnOff_Object=MibScalar
ciscoVisionDmpTvOnOff=_CiscoVisionDmpTvOnOff_Object((1,3,6,1,4,1,9,9,1051,3,1),_CiscoVisionDmpTvOnOff_Type())
ciscoVisionDmpTvOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpTvOnOff.setStatus(_B)
class _CiscoVisionDmpNtpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVisionDmpNtpStatus_Type.__name__=_D
_CiscoVisionDmpNtpStatus_Object=MibScalar
ciscoVisionDmpNtpStatus=_CiscoVisionDmpNtpStatus_Object((1,3,6,1,4,1,9,9,1051,3,2),_CiscoVisionDmpNtpStatus_Type())
ciscoVisionDmpNtpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpNtpStatus.setStatus(_B)
_CiscoVisionDmpPTP_ObjectIdentity=ObjectIdentity
ciscoVisionDmpPTP=_CiscoVisionDmpPTP_ObjectIdentity((1,3,6,1,4,1,9,9,1051,3,3))
class _CiscoVisionDmpPTPstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVisionDmpPTPstatus_Type.__name__=_D
_CiscoVisionDmpPTPstatus_Object=MibScalar
ciscoVisionDmpPTPstatus=_CiscoVisionDmpPTPstatus_Object((1,3,6,1,4,1,9,9,1051,3,3,1),_CiscoVisionDmpPTPstatus_Type())
ciscoVisionDmpPTPstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpPTPstatus.setStatus(_B)
class _CiscoVisionDmpPTPMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_CiscoVisionDmpPTPMaster_Type.__name__=_D
_CiscoVisionDmpPTPMaster_Object=MibScalar
ciscoVisionDmpPTPMaster=_CiscoVisionDmpPTPMaster_Object((1,3,6,1,4,1,9,9,1051,3,3,2),_CiscoVisionDmpPTPMaster_Type())
ciscoVisionDmpPTPMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpPTPMaster.setStatus(_B)
class _CiscoVisionDmpPTPDeviation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoVisionDmpPTPDeviation_Type.__name__=_E
_CiscoVisionDmpPTPDeviation_Object=MibScalar
ciscoVisionDmpPTPDeviation=_CiscoVisionDmpPTPDeviation_Object((1,3,6,1,4,1,9,9,1051,3,3,3),_CiscoVisionDmpPTPDeviation_Type())
ciscoVisionDmpPTPDeviation.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpPTPDeviation.setStatus(_B)
_CiscoVisionNetwork_ObjectIdentity=ObjectIdentity
ciscoVisionNetwork=_CiscoVisionNetwork_ObjectIdentity((1,3,6,1,4,1,9,9,1051,3,4))
class _CiscoVisionDmpInterfaceDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoVisionDmpInterfaceDesc_Type.__name__=_E
_CiscoVisionDmpInterfaceDesc_Object=MibScalar
ciscoVisionDmpInterfaceDesc=_CiscoVisionDmpInterfaceDesc_Object((1,3,6,1,4,1,9,9,1051,3,4,1),_CiscoVisionDmpInterfaceDesc_Type())
ciscoVisionDmpInterfaceDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpInterfaceDesc.setStatus(_B)
_CiscoVisionDmpBytesIn_Type=Integer32
_CiscoVisionDmpBytesIn_Object=MibScalar
ciscoVisionDmpBytesIn=_CiscoVisionDmpBytesIn_Object((1,3,6,1,4,1,9,9,1051,3,4,2),_CiscoVisionDmpBytesIn_Type())
ciscoVisionDmpBytesIn.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoVisionDmpBytesIn.setStatus(_B)
_CiscoVisionDmpBytesOut_Type=Integer32
_CiscoVisionDmpBytesOut_Object=MibScalar
ciscoVisionDmpBytesOut=_CiscoVisionDmpBytesOut_Object((1,3,6,1,4,1,9,9,1051,3,4,3),_CiscoVisionDmpBytesOut_Type())
ciscoVisionDmpBytesOut.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoVisionDmpBytesOut.setStatus(_B)
_CiscoVisionDmpPktCnt_Type=Integer32
_CiscoVisionDmpPktCnt_Object=MibScalar
ciscoVisionDmpPktCnt=_CiscoVisionDmpPktCnt_Object((1,3,6,1,4,1,9,9,1051,3,4,4),_CiscoVisionDmpPktCnt_Type())
ciscoVisionDmpPktCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpPktCnt.setStatus(_B)
_CiscoVisionDmpPktErrCnt_Type=Integer32
_CiscoVisionDmpPktErrCnt_Object=MibScalar
ciscoVisionDmpPktErrCnt=_CiscoVisionDmpPktErrCnt_Object((1,3,6,1,4,1,9,9,1051,3,4,5),_CiscoVisionDmpPktErrCnt_Type())
ciscoVisionDmpPktErrCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVisionDmpPktErrCnt.setStatus(_B)
_CiscoVisionDmpCpu_ObjectIdentity=ObjectIdentity
ciscoVisionDmpCpu=_CiscoVisionDmpCpu_ObjectIdentity((1,3,6,1,4,1,9,9,1051,3,5))
_SsCpuRawUser_Type=Integer32
_SsCpuRawUser_Object=MibScalar
ssCpuRawUser=_SsCpuRawUser_Object((1,3,6,1,4,1,9,9,1051,3,5,1),_SsCpuRawUser_Type())
ssCpuRawUser.setMaxAccess(_C)
if mibBuilder.loadTexts:ssCpuRawUser.setStatus(_B)
_SsCpuRawIdle_Type=Integer32
_SsCpuRawIdle_Object=MibScalar
ssCpuRawIdle=_SsCpuRawIdle_Object((1,3,6,1,4,1,9,9,1051,3,5,2),_SsCpuRawIdle_Type())
ssCpuRawIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:ssCpuRawIdle.setStatus(_B)
ciscoVisiondsdSvcGroup=ObjectGroup((1,3,6,1,4,1,9,9,1051,1,2,1))
ciscoVisiondsdSvcGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoVisiondsdSvcGroup.setStatus(_B)
ciscoVisiondsdDmpGroup=ObjectGroup((1,3,6,1,4,1,9,9,1051,1,2,3))
ciscoVisiondsdDmpGroup.setObjects(*((_A,_K),(_A,_S),(_A,_L)))
if mibBuilder.loadTexts:ciscoVisiondsdDmpGroup.setStatus(_B)
ciscoVisionDmpGroup=ObjectGroup((1,3,6,1,4,1,9,9,1051,1,2,4))
ciscoVisionDmpGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoVisionDmpGroup.setStatus(_B)
ciscoVdServiceStatusNotifs=NotificationType((1,3,6,1,4,1,9,9,1051,0,1))
ciscoVdServiceStatusNotifs.setObjects(*((_A,_G),(_A,_J)))
if mibBuilder.loadTexts:ciscoVdServiceStatusNotifs.setStatus(_B)
ciscoVdBackupTaskNotifs=NotificationType((1,3,6,1,4,1,9,9,1051,0,2))
ciscoVdBackupTaskNotifs.setObjects((_A,_I))
if mibBuilder.loadTexts:ciscoVdBackupTaskNotifs.setStatus(_B)
ciscoVdNtpNotifs=NotificationType((1,3,6,1,4,1,9,9,1051,0,3))
ciscoVdNtpNotifs.setObjects((_A,_H))
if mibBuilder.loadTexts:ciscoVdNtpNotifs.setStatus(_B)
ciscoVdHdmiUpDwnNotifs=NotificationType((1,3,6,1,4,1,9,9,1051,0,4))
ciscoVdHdmiUpDwnNotifs.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoVdHdmiUpDwnNotifs.setStatus(_B)
ciscoVisiondsdMIBNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,1051,1,2,2))
ciscoVisiondsdMIBNotifsGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoVisiondsdMIBNotifsGroup.setStatus(_B)
ciscoVisionDsdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,1051,1,1,1))
ciscoVisionDsdMIBCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoVisionDsdMIBCompliance.setStatus(_B)
ciscoVisionDmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,1051,1,1,2))
ciscoVisionDmpMIBCompliance.setObjects(*((_A,_j),(_A,_M),(_A,_O),(_A,_N)))
if mibBuilder.loadTexts:ciscoVisionDmpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoVisionMIB':ciscoVisionMIB,'ciscoVisionMIBNotifs':ciscoVisionMIBNotifs,_f:ciscoVdServiceStatusNotifs,_g:ciscoVdBackupTaskNotifs,_h:ciscoVdNtpNotifs,_i:ciscoVdHdmiUpDwnNotifs,'ciscoVisionMIBConform':ciscoVisionMIBConform,'ciscoVisionMIBCompliances':ciscoVisionMIBCompliances,'ciscoVisionDsdMIBCompliance':ciscoVisionDsdMIBCompliance,'ciscoVisionDmpMIBCompliance':ciscoVisionDmpMIBCompliance,'ciscoVisionMIBGroups':ciscoVisionMIBGroups,_M:ciscoVisiondsdSvcGroup,_O:ciscoVisiondsdMIBNotifsGroup,_N:ciscoVisiondsdDmpGroup,_j:ciscoVisionDmpGroup,'ciscoVisionDsd':ciscoVisionDsd,'ciscoVdService':ciscoVdService,'ciscoVdServiceTable':ciscoVdServiceTable,'ciscoVdServiceEntry':ciscoVdServiceEntry,_P:ciscoVdDsdServiceName,_G:ciscoVdDsdServiceStatus,_J:ciscoVdDsdServiceDesc,'ciscoVdDmpsStatuses':ciscoVdDmpsStatuses,'ciscoVdDmpStatusTable':ciscoVdDmpStatusTable,'ciscoVdDmpStatusEntry':ciscoVdDmpStatusEntry,_R:ciscoVdDmpIP,_K:ciscoVdHdmiUpDownStatus,_S:ciscoVdDmpStatus,_L:ciscoVdDmpidentifier,_H:ciscoVdNtpSyncStatus,_I:ciscoVdBkpStatus,'ciscoVisionDmp':ciscoVisionDmp,_T:ciscoVisionDmpTvOnOff,_U:ciscoVisionDmpNtpStatus,'ciscoVisionDmpPTP':ciscoVisionDmpPTP,_V:ciscoVisionDmpPTPstatus,_W:ciscoVisionDmpPTPMaster,_X:ciscoVisionDmpPTPDeviation,'ciscoVisionNetwork':ciscoVisionNetwork,_Y:ciscoVisionDmpInterfaceDesc,_Z:ciscoVisionDmpBytesIn,_a:ciscoVisionDmpBytesOut,_b:ciscoVisionDmpPktCnt,_c:ciscoVisionDmpPktErrCnt,'ciscoVisionDmpCpu':ciscoVisionDmpCpu,_d:ssCpuRawUser,_e:ssCpuRawIdle})