_h='rcfJobNotifyGroup'
_g='rcfJobGroup'
_f='rcfJobCompleted'
_e='rcfJobRowStatus'
_d='rcfJobOwner'
_c='rcfJobNotifyOnCompletion'
_b='rcfJobStopTime'
_a='rcfJobStartTime'
_Z='rcfJobCreateTime'
_Y='rcfJobState'
_X='rcfJobSaveDefaults'
_W='rcfJobStopAtLine'
_V='rcfJobPassiveMode'
_U='rcfJobPassword'
_T='rcfJobUsername'
_S='rcfJobIpAddress'
_R='rcfJobIpAddressType'
_Q='rcfJobFilename'
_P='rcfJobProtocol'
_O='rcfJobOp'
_N='rcfJobNextIndex'
_M='rcfJobSpinLock'
_L='rcfJobIndex'
_K='OwnerString'
_J='rcfJobErrorMsgs'
_I='rcfJobResult'
_H='Unsigned32'
_G='TruthValue'
_F='SnmpAdminString'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='RBN-CONFIG-FILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
OwnerString,=mibBuilder.importSymbols('RMON-MIB',_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp',_G)
rbnConfigFileMib=ModuleIdentity((1,3,6,1,4,1,2352,2,13))
if mibBuilder.loadTexts:rbnConfigFileMib.setRevisions(('2002-05-29 00:00','2001-10-10 00:00'))
_RbnConfigFileMIBNotifications_ObjectIdentity=ObjectIdentity
rbnConfigFileMIBNotifications=_RbnConfigFileMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,13,0))
_RbnConfigFileMIBObjects_ObjectIdentity=ObjectIdentity
rbnConfigFileMIBObjects=_RbnConfigFileMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,13,1))
_RcfJobs_ObjectIdentity=ObjectIdentity
rcfJobs=_RcfJobs_ObjectIdentity((1,3,6,1,4,1,2352,2,13,1,1))
_RcfJobSpinLock_Type=TestAndIncr
_RcfJobSpinLock_Object=MibScalar
rcfJobSpinLock=_RcfJobSpinLock_Object((1,3,6,1,4,1,2352,2,13,1,1,1),_RcfJobSpinLock_Type())
rcfJobSpinLock.setMaxAccess('read-write')
if mibBuilder.loadTexts:rcfJobSpinLock.setStatus(_A)
_RcfJobNextIndex_Type=Unsigned32
_RcfJobNextIndex_Object=MibScalar
rcfJobNextIndex=_RcfJobNextIndex_Object((1,3,6,1,4,1,2352,2,13,1,1,2),_RcfJobNextIndex_Type())
rcfJobNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobNextIndex.setStatus(_A)
_RcfJobTable_Object=MibTable
rcfJobTable=_RcfJobTable_Object((1,3,6,1,4,1,2352,2,13,1,1,3))
if mibBuilder.loadTexts:rcfJobTable.setStatus(_A)
_RcfJobEntry_Object=MibTableRow
rcfJobEntry=_RcfJobEntry_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1))
rcfJobEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:rcfJobEntry.setStatus(_A)
class _RcfJobIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RcfJobIndex_Type.__name__=_H
_RcfJobIndex_Object=MibTableColumn
rcfJobIndex=_RcfJobIndex_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,1),_RcfJobIndex_Type())
rcfJobIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcfJobIndex.setStatus(_A)
class _RcfJobOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('load',0),('save',1)))
_RcfJobOp_Type.__name__=_E
_RcfJobOp_Object=MibTableColumn
rcfJobOp=_RcfJobOp_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,2),_RcfJobOp_Type())
rcfJobOp.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobOp.setStatus(_A)
class _RcfJobProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('local',0),('tftp',1),('ftp',2)))
_RcfJobProtocol_Type.__name__=_E
_RcfJobProtocol_Object=MibTableColumn
rcfJobProtocol=_RcfJobProtocol_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,3),_RcfJobProtocol_Type())
rcfJobProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobProtocol.setStatus(_A)
class _RcfJobFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RcfJobFilename_Type.__name__=_F
_RcfJobFilename_Object=MibTableColumn
rcfJobFilename=_RcfJobFilename_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,4),_RcfJobFilename_Type())
rcfJobFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobFilename.setStatus(_A)
_RcfJobIpAddressType_Type=InetAddressType
_RcfJobIpAddressType_Object=MibTableColumn
rcfJobIpAddressType=_RcfJobIpAddressType_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,5),_RcfJobIpAddressType_Type())
rcfJobIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobIpAddressType.setStatus(_A)
_RcfJobIpAddress_Type=InetAddress
_RcfJobIpAddress_Object=MibTableColumn
rcfJobIpAddress=_RcfJobIpAddress_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,6),_RcfJobIpAddress_Type())
rcfJobIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobIpAddress.setStatus(_A)
class _RcfJobUsername_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RcfJobUsername_Type.__name__=_F
_RcfJobUsername_Object=MibTableColumn
rcfJobUsername=_RcfJobUsername_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,7),_RcfJobUsername_Type())
rcfJobUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobUsername.setStatus(_A)
class _RcfJobPassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RcfJobPassword_Type.__name__=_F
_RcfJobPassword_Object=MibTableColumn
rcfJobPassword=_RcfJobPassword_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,8),_RcfJobPassword_Type())
rcfJobPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobPassword.setStatus(_A)
class _RcfJobPassiveMode_Type(TruthValue):defaultValue=2
_RcfJobPassiveMode_Type.__name__=_G
_RcfJobPassiveMode_Object=MibTableColumn
rcfJobPassiveMode=_RcfJobPassiveMode_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,9),_RcfJobPassiveMode_Type())
rcfJobPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobPassiveMode.setStatus(_A)
class _RcfJobStopAtLine_Type(Unsigned32):defaultValue=0
_RcfJobStopAtLine_Type.__name__=_H
_RcfJobStopAtLine_Object=MibTableColumn
rcfJobStopAtLine=_RcfJobStopAtLine_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,10),_RcfJobStopAtLine_Type())
rcfJobStopAtLine.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobStopAtLine.setStatus(_A)
class _RcfJobSaveDefaults_Type(TruthValue):defaultValue=2
_RcfJobSaveDefaults_Type.__name__=_G
_RcfJobSaveDefaults_Object=MibTableColumn
rcfJobSaveDefaults=_RcfJobSaveDefaults_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,11),_RcfJobSaveDefaults_Type())
rcfJobSaveDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobSaveDefaults.setStatus(_A)
class _RcfJobState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('pending',0),('inProgress',1),('completed',2)))
_RcfJobState_Type.__name__=_E
_RcfJobState_Object=MibTableColumn
rcfJobState=_RcfJobState_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,12),_RcfJobState_Type())
rcfJobState.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobState.setStatus(_A)
class _RcfJobResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('success',0),('other',1),('noMemory',2),('parse',3),('io',4),('access',5)))
_RcfJobResult_Type.__name__=_E
_RcfJobResult_Object=MibTableColumn
rcfJobResult=_RcfJobResult_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,13),_RcfJobResult_Type())
rcfJobResult.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobResult.setStatus(_A)
_RcfJobErrorMsgs_Type=SnmpAdminString
_RcfJobErrorMsgs_Object=MibTableColumn
rcfJobErrorMsgs=_RcfJobErrorMsgs_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,14),_RcfJobErrorMsgs_Type())
rcfJobErrorMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobErrorMsgs.setStatus(_A)
_RcfJobCreateTime_Type=TimeStamp
_RcfJobCreateTime_Object=MibTableColumn
rcfJobCreateTime=_RcfJobCreateTime_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,15),_RcfJobCreateTime_Type())
rcfJobCreateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobCreateTime.setStatus(_A)
_RcfJobStartTime_Type=TimeStamp
_RcfJobStartTime_Object=MibTableColumn
rcfJobStartTime=_RcfJobStartTime_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,16),_RcfJobStartTime_Type())
rcfJobStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobStartTime.setStatus(_A)
_RcfJobStopTime_Type=TimeStamp
_RcfJobStopTime_Object=MibTableColumn
rcfJobStopTime=_RcfJobStopTime_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,17),_RcfJobStopTime_Type())
rcfJobStopTime.setMaxAccess(_D)
if mibBuilder.loadTexts:rcfJobStopTime.setStatus(_A)
class _RcfJobNotifyOnCompletion_Type(TruthValue):defaultValue=2
_RcfJobNotifyOnCompletion_Type.__name__=_G
_RcfJobNotifyOnCompletion_Object=MibTableColumn
rcfJobNotifyOnCompletion=_RcfJobNotifyOnCompletion_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,18),_RcfJobNotifyOnCompletion_Type())
rcfJobNotifyOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobNotifyOnCompletion.setStatus(_A)
class _RcfJobOwner_Type(OwnerString):defaultValue=OctetString('')
_RcfJobOwner_Type.__name__=_K
_RcfJobOwner_Object=MibTableColumn
rcfJobOwner=_RcfJobOwner_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,19),_RcfJobOwner_Type())
rcfJobOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobOwner.setStatus(_A)
_RcfJobRowStatus_Type=RowStatus
_RcfJobRowStatus_Object=MibTableColumn
rcfJobRowStatus=_RcfJobRowStatus_Object((1,3,6,1,4,1,2352,2,13,1,1,3,1,20),_RcfJobRowStatus_Type())
rcfJobRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcfJobRowStatus.setStatus(_A)
_RbnConfigFileMIBConformance_ObjectIdentity=ObjectIdentity
rbnConfigFileMIBConformance=_RbnConfigFileMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,13,2))
_RbnConfigFileCompliances_ObjectIdentity=ObjectIdentity
rbnConfigFileCompliances=_RbnConfigFileCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,13,2,1))
_RbnConfigFileGroups_ObjectIdentity=ObjectIdentity
rbnConfigFileGroups=_RbnConfigFileGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,13,2,2))
rcfJobGroup=ObjectGroup((1,3,6,1,4,1,2352,2,13,2,2,1))
rcfJobGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_I),(_B,_Z),(_B,_a),(_B,_b),(_B,_J),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:rcfJobGroup.setStatus(_A)
rcfJobCompleted=NotificationType((1,3,6,1,4,1,2352,2,13,0,1))
rcfJobCompleted.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:rcfJobCompleted.setStatus(_A)
rcfJobNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,13,2,2,2))
rcfJobNotifyGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:rcfJobNotifyGroup.setStatus(_A)
rbnConfigFileCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,13,2,1,1))
rbnConfigFileCompliance.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:rbnConfigFileCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnConfigFileMib':rbnConfigFileMib,'rbnConfigFileMIBNotifications':rbnConfigFileMIBNotifications,_f:rcfJobCompleted,'rbnConfigFileMIBObjects':rbnConfigFileMIBObjects,'rcfJobs':rcfJobs,_M:rcfJobSpinLock,_N:rcfJobNextIndex,'rcfJobTable':rcfJobTable,'rcfJobEntry':rcfJobEntry,_L:rcfJobIndex,_O:rcfJobOp,_P:rcfJobProtocol,_Q:rcfJobFilename,_R:rcfJobIpAddressType,_S:rcfJobIpAddress,_T:rcfJobUsername,_U:rcfJobPassword,_V:rcfJobPassiveMode,_W:rcfJobStopAtLine,_X:rcfJobSaveDefaults,_Y:rcfJobState,_I:rcfJobResult,_J:rcfJobErrorMsgs,_Z:rcfJobCreateTime,_a:rcfJobStartTime,_b:rcfJobStopTime,_c:rcfJobNotifyOnCompletion,_d:rcfJobOwner,_e:rcfJobRowStatus,'rbnConfigFileMIBConformance':rbnConfigFileMIBConformance,'rbnConfigFileCompliances':rbnConfigFileCompliances,'rbnConfigFileCompliance':rbnConfigFileCompliance,'rbnConfigFileGroups':rbnConfigFileGroups,_g:rcfJobGroup,_h:rcfJobNotifyGroup})