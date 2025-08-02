_Ao='tmnxCallTraceJob20v0Group'
_An='tmnxCallTraceScalarCfg20v0Group'
_Am='tmnxCallTraceJobGroup'
_Al='tmnxCallTraceLocSizeLimitReached'
_Ak='tmnxCallTraceMaxFilesNumReached'
_Aj='tmnxCallTraceJobTraceName'
_Ai='tmnxCallTraceJobRemoteId'
_Ah='tmnxCallTraceJobCircuitId'
_Ag='tmnxCallTraceJobIpoeIeeeAddr'
_Af='tmnxCallTraceJobSapEncapVal'
_Ae='tmnxCallTraceJobSapPortId'
_Ad='tmnxCallTraceJobUserName'
_Ac='tmnxCallTraceBuffering'
_Ab='tmnxCallTraceJobDstType'
_Aa='tmnxCallTraceAvailFilesNumber'
_AZ='tmnxCallTraceUsedFilesNumber'
_AY='tmnxCallTraceFileLastDataModif'
_AX='tmnxCallTraceFileSize'
_AW='tmnxCallTraceFileDir'
_AV='tmnxCallTracePrimaryCFlash'
_AU='tmnxCallTraceLocationAvailSpace'
_AT='tmnxCallTraceLocationUsedSpace'
_AS='tmnxCallTraceLocationDisable'
_AR='tmnxCallTraceLocationLstChgd'
_AQ='tmnxCallTraceLocationTblLstChgd'
_AP='tmnxCallTraceProfileEvents'
_AO='tmnxCallTraceProfileDbgOutput'
_AN='tmnxCallTraceProfileApplications'
_AM='tmnxCallTraceProfileVRtrId'
_AL='tmnxCallTraceProfileDstPort'
_AK='tmnxCallTraceProfileDstAddr'
_AJ='tmnxCallTraceProfileDstAddrType'
_AI='tmnxCallTraceProfileTimeLimit'
_AH='tmnxCallTraceProfileSizeLimit'
_AG='tmnxCallTraceProfileDescription'
_AF='tmnxCallTraceProfileRowStatus'
_AE='tmnxCallTraceProfileLstChgd'
_AD='tmnxCallTraceProfileTblLstChgd'
_AC='tmnxCallTraceLocationStatsEntry'
_AB='tmnxCallTraceTraceId'
_AA='tmnxCallTraceFileName'
_A9='tmnxCallTraceFileCFlashId'
_A8='tmnxCallTraceFileCpmSlotNum'
_A7='tmnxCallTraceFileJobStatus'
_A6='tmnxCallTraceJobId'
_A5='tmnxCallTraceLocationCFlashId'
_A4='TmnxCallTraceTimeLimit'
_A3='TmnxCallTraceSizeLimit'
_A2='tmnxCallTraceProfileName'
_A1='TmnxCallTraceCFlashId'
_A0='2015-02-01 00:00'
_z='TmnxVRtrID'
_y='TItemDescription'
_x='InetAddressType'
_w='tmnxCallTraceJob15v0Group'
_v='tmnxCallTraceTraceMaxJobs'
_u='tmnxCallTraceTraceName'
_t='tmnxCallTraceTraceRemoteId'
_s='tmnxCallTraceTraceCircuitId'
_r='tmnxCallTraceTraceIeeeAddr'
_q='tmnxCallTraceTraceSapId'
_p='tmnxCallTraceTraceType'
_o='tmnxCallTraceJobCaptMsgsSize'
_n='tmnxCallTraceJobCaptMsgsCnt'
_m='tmnxCallTraceJobStartTime'
_l='tmnxCallTraceJobVRtrId'
_k='tmnxCallTraceJobDstPort'
_j='tmnxCallTraceJobDstResAddr'
_i='tmnxCallTraceJobDstResAddrType'
_h='tmnxCallTraceJobDstAddr'
_g='tmnxCallTraceJobDstAddrType'
_f='tmnxCallTraceJobCaptureFormat'
_e='tmnxCallTraceJobTimeLimit'
_d='tmnxCallTraceJobSizeLimit'
_c='tmnxCallTraceJobProfileName'
_b='tmnxCallTraceJobStatus'
_a='tmnxCallTraceJobWlanGwUeIeeeAddr'
_Z='tmnxCallTraceJobType'
_Y='tmnxCallTraceMaxFilesNumber'
_X='tmnxCallTraceLocationSizeLimit'
_W='InetPortNumber'
_V='tmnxCallTraceIpoeTraceGroup'
_U='tmnxCallTraceIpoeJobGroup'
_T='tmnxCallTraceScalarStatsGroup'
_S='tmnxCallTraceFileGroup'
_R='tmnxCallTraceNotifyGroup'
_Q='tmnxCallTraceScalarCfgGroup'
_P='tmnxCallTraceLocStoreGroup'
_O='tmnxCallTraceProfileGroup'
_N='obsolete'
_M='TruthValue'
_L='Integer32'
_K='InetAddress'
_J='OctetString'
_I='megabytes'
_H='read-write'
_G='DisplayString'
_F='not-accessible'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='TIMETRA-CALLTRACE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,_x,_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_M)
TmnxSlotNum,=mibBuilder.importSymbols('TIMETRA-CHASSIS-MIB','TmnxSlotNum')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TNamedItem,TNamedItemOrEmpty,TmnxEncapVal,TmnxPortID,TmnxVRtrID=mibBuilder.importSymbols('TIMETRA-TC-MIB',_y,'TNamedItem','TNamedItemOrEmpty','TmnxEncapVal','TmnxPortID',_z)
timetraCallTraceMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,102))
if mibBuilder.loadTexts:timetraCallTraceMIBModule.setRevisions(('2016-01-01 00:00',_A0,_A0))
class TmnxCallTraceSizeLimit(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
class TmnxCallTraceTimeLimit(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
class TmnxCallTraceJobStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('running',0),('finished',1)))
class TmnxCallTraceCFlashId(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cf1',1),('cf2',2)))
class TmnxCallTraceApplications(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('connectivityManagement',0),('reserved1',1),('reserved2',2),('reserved3',3),('radiusAuth',4),('radiusAcct',5),('python',6),('ludb',7),('msap',8),('reserved9',9),('reserved10',10),('pppEvent',11)))
class TmnxCallTraceHostType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ue',1),('ipoe',2),('pppoe',3)))
_TmnxCallTraceConformance_ObjectIdentity=ObjectIdentity
tmnxCallTraceConformance=_TmnxCallTraceConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,102))
_TmnxCallTraceCompliances_ObjectIdentity=ObjectIdentity
tmnxCallTraceCompliances=_TmnxCallTraceCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,102,1))
_TmnxCallTraceGroups_ObjectIdentity=ObjectIdentity
tmnxCallTraceGroups=_TmnxCallTraceGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,102,2))
_TmnxCallTraceInitialGroups_ObjectIdentity=ObjectIdentity
tmnxCallTraceInitialGroups=_TmnxCallTraceInitialGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,102,2,1))
_TmnxCallTraceIpoeGroups_ObjectIdentity=ObjectIdentity
tmnxCallTraceIpoeGroups=_TmnxCallTraceIpoeGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,102,2,2))
_TmnxCallTraceObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceObjs=_TmnxCallTraceObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102))
_TmnxCallTraceScalarObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceScalarObjs=_TmnxCallTraceScalarObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,1))
_TmnxCallTraceLastChangedObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceLastChangedObjs=_TmnxCallTraceLastChangedObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,1,1))
_TmnxCallTraceProfileTblLstChgd_Type=TimeStamp
_TmnxCallTraceProfileTblLstChgd_Object=MibScalar
tmnxCallTraceProfileTblLstChgd=_TmnxCallTraceProfileTblLstChgd_Object((1,3,6,1,4,1,6527,3,1,2,102,1,1,1),_TmnxCallTraceProfileTblLstChgd_Type())
tmnxCallTraceProfileTblLstChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceProfileTblLstChgd.setStatus(_B)
_TmnxCallTraceLocationTblLstChgd_Type=TimeStamp
_TmnxCallTraceLocationTblLstChgd_Object=MibScalar
tmnxCallTraceLocationTblLstChgd=_TmnxCallTraceLocationTblLstChgd_Object((1,3,6,1,4,1,6527,3,1,2,102,1,1,2),_TmnxCallTraceLocationTblLstChgd_Type())
tmnxCallTraceLocationTblLstChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceLocationTblLstChgd.setStatus(_B)
_TmnxCallTraceScalarConfigObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceScalarConfigObjs=_TmnxCallTraceScalarConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,1,2))
class _TmnxCallTraceMaxFilesNumber_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_TmnxCallTraceMaxFilesNumber_Type.__name__=_E
_TmnxCallTraceMaxFilesNumber_Object=MibScalar
tmnxCallTraceMaxFilesNumber=_TmnxCallTraceMaxFilesNumber_Object((1,3,6,1,4,1,6527,3,1,2,102,1,2,1),_TmnxCallTraceMaxFilesNumber_Type())
tmnxCallTraceMaxFilesNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxCallTraceMaxFilesNumber.setStatus(_B)
class _TmnxCallTracePrimaryCFlash_Type(TmnxCallTraceCFlashId):defaultValue=1
_TmnxCallTracePrimaryCFlash_Type.__name__=_A1
_TmnxCallTracePrimaryCFlash_Object=MibScalar
tmnxCallTracePrimaryCFlash=_TmnxCallTracePrimaryCFlash_Object((1,3,6,1,4,1,6527,3,1,2,102,1,2,2),_TmnxCallTracePrimaryCFlash_Type())
tmnxCallTracePrimaryCFlash.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxCallTracePrimaryCFlash.setStatus(_B)
class _TmnxCallTraceBuffering_Type(TruthValue):defaultValue=2
_TmnxCallTraceBuffering_Type.__name__=_M
_TmnxCallTraceBuffering_Object=MibScalar
tmnxCallTraceBuffering=_TmnxCallTraceBuffering_Object((1,3,6,1,4,1,6527,3,1,2,102,1,2,3),_TmnxCallTraceBuffering_Type())
tmnxCallTraceBuffering.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxCallTraceBuffering.setStatus(_B)
_TmnxCallTraceScalarStatsObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceScalarStatsObjs=_TmnxCallTraceScalarStatsObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,1,3))
class _TmnxCallTraceUsedFilesNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_TmnxCallTraceUsedFilesNumber_Type.__name__=_E
_TmnxCallTraceUsedFilesNumber_Object=MibScalar
tmnxCallTraceUsedFilesNumber=_TmnxCallTraceUsedFilesNumber_Object((1,3,6,1,4,1,6527,3,1,2,102,1,3,1),_TmnxCallTraceUsedFilesNumber_Type())
tmnxCallTraceUsedFilesNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceUsedFilesNumber.setStatus(_B)
class _TmnxCallTraceAvailFilesNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_TmnxCallTraceAvailFilesNumber_Type.__name__=_E
_TmnxCallTraceAvailFilesNumber_Object=MibScalar
tmnxCallTraceAvailFilesNumber=_TmnxCallTraceAvailFilesNumber_Object((1,3,6,1,4,1,6527,3,1,2,102,1,3,2),_TmnxCallTraceAvailFilesNumber_Type())
tmnxCallTraceAvailFilesNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceAvailFilesNumber.setStatus(_B)
_TmnxCallTraceConfigObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceConfigObjs=_TmnxCallTraceConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,2))
_TmnxCallTraceProfileTable_Object=MibTable
tmnxCallTraceProfileTable=_TmnxCallTraceProfileTable_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1))
if mibBuilder.loadTexts:tmnxCallTraceProfileTable.setStatus(_B)
_TmnxCallTraceProfileEntry_Object=MibTableRow
tmnxCallTraceProfileEntry=_TmnxCallTraceProfileEntry_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1))
tmnxCallTraceProfileEntry.setIndexNames((1,_A,_A2))
if mibBuilder.loadTexts:tmnxCallTraceProfileEntry.setStatus(_B)
_TmnxCallTraceProfileName_Type=TNamedItem
_TmnxCallTraceProfileName_Object=MibTableColumn
tmnxCallTraceProfileName=_TmnxCallTraceProfileName_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,1),_TmnxCallTraceProfileName_Type())
tmnxCallTraceProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceProfileName.setStatus(_B)
_TmnxCallTraceProfileLstChgd_Type=TimeStamp
_TmnxCallTraceProfileLstChgd_Object=MibTableColumn
tmnxCallTraceProfileLstChgd=_TmnxCallTraceProfileLstChgd_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,2),_TmnxCallTraceProfileLstChgd_Type())
tmnxCallTraceProfileLstChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceProfileLstChgd.setStatus(_B)
_TmnxCallTraceProfileRowStatus_Type=RowStatus
_TmnxCallTraceProfileRowStatus_Object=MibTableColumn
tmnxCallTraceProfileRowStatus=_TmnxCallTraceProfileRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,3),_TmnxCallTraceProfileRowStatus_Type())
tmnxCallTraceProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileRowStatus.setStatus(_B)
class _TmnxCallTraceProfileDescription_Type(TItemDescription):defaultHexValue=''
_TmnxCallTraceProfileDescription_Type.__name__=_y
_TmnxCallTraceProfileDescription_Object=MibTableColumn
tmnxCallTraceProfileDescription=_TmnxCallTraceProfileDescription_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,4),_TmnxCallTraceProfileDescription_Type())
tmnxCallTraceProfileDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileDescription.setStatus(_B)
class _TmnxCallTraceProfileSizeLimit_Type(TmnxCallTraceSizeLimit):defaultValue=10
_TmnxCallTraceProfileSizeLimit_Type.__name__=_A3
_TmnxCallTraceProfileSizeLimit_Object=MibTableColumn
tmnxCallTraceProfileSizeLimit=_TmnxCallTraceProfileSizeLimit_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,5),_TmnxCallTraceProfileSizeLimit_Type())
tmnxCallTraceProfileSizeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileSizeLimit.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceProfileSizeLimit.setUnits(_I)
class _TmnxCallTraceProfileTimeLimit_Type(TmnxCallTraceTimeLimit):defaultValue=86400
_TmnxCallTraceProfileTimeLimit_Type.__name__=_A4
_TmnxCallTraceProfileTimeLimit_Object=MibTableColumn
tmnxCallTraceProfileTimeLimit=_TmnxCallTraceProfileTimeLimit_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,6),_TmnxCallTraceProfileTimeLimit_Type())
tmnxCallTraceProfileTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileTimeLimit.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceProfileTimeLimit.setUnits('sec')
class _TmnxCallTraceProfileDstAddrType_Type(InetAddressType):defaultValue=0
_TmnxCallTraceProfileDstAddrType_Type.__name__=_x
_TmnxCallTraceProfileDstAddrType_Object=MibTableColumn
tmnxCallTraceProfileDstAddrType=_TmnxCallTraceProfileDstAddrType_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,7),_TmnxCallTraceProfileDstAddrType_Type())
tmnxCallTraceProfileDstAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileDstAddrType.setStatus(_B)
class _TmnxCallTraceProfileDstAddr_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCallTraceProfileDstAddr_Type.__name__=_K
_TmnxCallTraceProfileDstAddr_Object=MibTableColumn
tmnxCallTraceProfileDstAddr=_TmnxCallTraceProfileDstAddr_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,8),_TmnxCallTraceProfileDstAddr_Type())
tmnxCallTraceProfileDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileDstAddr.setStatus(_B)
class _TmnxCallTraceProfileDstPort_Type(InetPortNumber):defaultValue=29770;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxCallTraceProfileDstPort_Type.__name__=_W
_TmnxCallTraceProfileDstPort_Object=MibTableColumn
tmnxCallTraceProfileDstPort=_TmnxCallTraceProfileDstPort_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,9),_TmnxCallTraceProfileDstPort_Type())
tmnxCallTraceProfileDstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileDstPort.setStatus(_B)
class _TmnxCallTraceProfileVRtrId_Type(TmnxVRtrID):defaultValue=1
_TmnxCallTraceProfileVRtrId_Type.__name__=_z
_TmnxCallTraceProfileVRtrId_Object=MibTableColumn
tmnxCallTraceProfileVRtrId=_TmnxCallTraceProfileVRtrId_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,10),_TmnxCallTraceProfileVRtrId_Type())
tmnxCallTraceProfileVRtrId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileVRtrId.setStatus(_B)
_TmnxCallTraceProfileApplications_Type=TmnxCallTraceApplications
_TmnxCallTraceProfileApplications_Object=MibTableColumn
tmnxCallTraceProfileApplications=_TmnxCallTraceProfileApplications_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,11),_TmnxCallTraceProfileApplications_Type())
tmnxCallTraceProfileApplications.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileApplications.setStatus(_B)
class _TmnxCallTraceProfileDbgOutput_Type(TruthValue):defaultValue=2
_TmnxCallTraceProfileDbgOutput_Type.__name__=_M
_TmnxCallTraceProfileDbgOutput_Object=MibTableColumn
tmnxCallTraceProfileDbgOutput=_TmnxCallTraceProfileDbgOutput_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,12),_TmnxCallTraceProfileDbgOutput_Type())
tmnxCallTraceProfileDbgOutput.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileDbgOutput.setStatus(_B)
class _TmnxCallTraceProfileEvents_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('publicOnly',2),('all',3)))
_TmnxCallTraceProfileEvents_Type.__name__=_L
_TmnxCallTraceProfileEvents_Object=MibTableColumn
tmnxCallTraceProfileEvents=_TmnxCallTraceProfileEvents_Object((1,3,6,1,4,1,6527,3,1,2,102,2,1,1,13),_TmnxCallTraceProfileEvents_Type())
tmnxCallTraceProfileEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxCallTraceProfileEvents.setStatus(_B)
_TmnxCallTraceLocationTable_Object=MibTable
tmnxCallTraceLocationTable=_TmnxCallTraceLocationTable_Object((1,3,6,1,4,1,6527,3,1,2,102,2,2))
if mibBuilder.loadTexts:tmnxCallTraceLocationTable.setStatus(_B)
_TmnxCallTraceLocationEntry_Object=MibTableRow
tmnxCallTraceLocationEntry=_TmnxCallTraceLocationEntry_Object((1,3,6,1,4,1,6527,3,1,2,102,2,2,1))
tmnxCallTraceLocationEntry.setIndexNames((0,_A,_A5))
if mibBuilder.loadTexts:tmnxCallTraceLocationEntry.setStatus(_B)
class _TmnxCallTraceLocationCFlashId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_TmnxCallTraceLocationCFlashId_Type.__name__=_E
_TmnxCallTraceLocationCFlashId_Object=MibTableColumn
tmnxCallTraceLocationCFlashId=_TmnxCallTraceLocationCFlashId_Object((1,3,6,1,4,1,6527,3,1,2,102,2,2,1,1),_TmnxCallTraceLocationCFlashId_Type())
tmnxCallTraceLocationCFlashId.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceLocationCFlashId.setStatus(_B)
_TmnxCallTraceLocationLstChgd_Type=TimeStamp
_TmnxCallTraceLocationLstChgd_Object=MibTableColumn
tmnxCallTraceLocationLstChgd=_TmnxCallTraceLocationLstChgd_Object((1,3,6,1,4,1,6527,3,1,2,102,2,2,1,2),_TmnxCallTraceLocationLstChgd_Type())
tmnxCallTraceLocationLstChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceLocationLstChgd.setStatus(_B)
class _TmnxCallTraceLocationSizeLimit_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_TmnxCallTraceLocationSizeLimit_Type.__name__=_E
_TmnxCallTraceLocationSizeLimit_Object=MibTableColumn
tmnxCallTraceLocationSizeLimit=_TmnxCallTraceLocationSizeLimit_Object((1,3,6,1,4,1,6527,3,1,2,102,2,2,1,3),_TmnxCallTraceLocationSizeLimit_Type())
tmnxCallTraceLocationSizeLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxCallTraceLocationSizeLimit.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceLocationSizeLimit.setUnits(_I)
class _TmnxCallTraceLocationDisable_Type(TruthValue):defaultValue=2
_TmnxCallTraceLocationDisable_Type.__name__=_M
_TmnxCallTraceLocationDisable_Object=MibTableColumn
tmnxCallTraceLocationDisable=_TmnxCallTraceLocationDisable_Object((1,3,6,1,4,1,6527,3,1,2,102,2,2,1,4),_TmnxCallTraceLocationDisable_Type())
tmnxCallTraceLocationDisable.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxCallTraceLocationDisable.setStatus(_B)
_TmnxCallTraceLocationStatsTable_Object=MibTable
tmnxCallTraceLocationStatsTable=_TmnxCallTraceLocationStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,102,2,3))
if mibBuilder.loadTexts:tmnxCallTraceLocationStatsTable.setStatus(_B)
_TmnxCallTraceLocationStatsEntry_Object=MibTableRow
tmnxCallTraceLocationStatsEntry=_TmnxCallTraceLocationStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,102,2,3,1))
if mibBuilder.loadTexts:tmnxCallTraceLocationStatsEntry.setStatus(_B)
_TmnxCallTraceLocationUsedSpace_Type=Unsigned32
_TmnxCallTraceLocationUsedSpace_Object=MibTableColumn
tmnxCallTraceLocationUsedSpace=_TmnxCallTraceLocationUsedSpace_Object((1,3,6,1,4,1,6527,3,1,2,102,2,3,1,1),_TmnxCallTraceLocationUsedSpace_Type())
tmnxCallTraceLocationUsedSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceLocationUsedSpace.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceLocationUsedSpace.setUnits(_I)
_TmnxCallTraceLocationAvailSpace_Type=Unsigned32
_TmnxCallTraceLocationAvailSpace_Object=MibTableColumn
tmnxCallTraceLocationAvailSpace=_TmnxCallTraceLocationAvailSpace_Object((1,3,6,1,4,1,6527,3,1,2,102,2,3,1,2),_TmnxCallTraceLocationAvailSpace_Type())
tmnxCallTraceLocationAvailSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceLocationAvailSpace.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceLocationAvailSpace.setUnits(_I)
_TmnxCallTraceStatsObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceStatsObjs=_TmnxCallTraceStatsObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,3))
_TmnxCallTraceJobTable_Object=MibTable
tmnxCallTraceJobTable=_TmnxCallTraceJobTable_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1))
if mibBuilder.loadTexts:tmnxCallTraceJobTable.setStatus(_B)
_TmnxCallTraceJobEntry_Object=MibTableRow
tmnxCallTraceJobEntry=_TmnxCallTraceJobEntry_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1))
tmnxCallTraceJobEntry.setIndexNames((0,_A,_A6))
if mibBuilder.loadTexts:tmnxCallTraceJobEntry.setStatus(_B)
class _TmnxCallTraceJobId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_TmnxCallTraceJobId_Type.__name__=_E
_TmnxCallTraceJobId_Object=MibTableColumn
tmnxCallTraceJobId=_TmnxCallTraceJobId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,1),_TmnxCallTraceJobId_Type())
tmnxCallTraceJobId.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceJobId.setStatus(_B)
_TmnxCallTraceJobType_Type=TmnxCallTraceHostType
_TmnxCallTraceJobType_Object=MibTableColumn
tmnxCallTraceJobType=_TmnxCallTraceJobType_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,2),_TmnxCallTraceJobType_Type())
tmnxCallTraceJobType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobType.setStatus(_B)
_TmnxCallTraceJobWlanGwUeIeeeAddr_Type=MacAddress
_TmnxCallTraceJobWlanGwUeIeeeAddr_Object=MibTableColumn
tmnxCallTraceJobWlanGwUeIeeeAddr=_TmnxCallTraceJobWlanGwUeIeeeAddr_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,3),_TmnxCallTraceJobWlanGwUeIeeeAddr_Type())
tmnxCallTraceJobWlanGwUeIeeeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobWlanGwUeIeeeAddr.setStatus(_B)
_TmnxCallTraceJobStatus_Type=TmnxCallTraceJobStatus
_TmnxCallTraceJobStatus_Object=MibTableColumn
tmnxCallTraceJobStatus=_TmnxCallTraceJobStatus_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,4),_TmnxCallTraceJobStatus_Type())
tmnxCallTraceJobStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobStatus.setStatus(_B)
_TmnxCallTraceJobProfileName_Type=TNamedItem
_TmnxCallTraceJobProfileName_Object=MibTableColumn
tmnxCallTraceJobProfileName=_TmnxCallTraceJobProfileName_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,5),_TmnxCallTraceJobProfileName_Type())
tmnxCallTraceJobProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobProfileName.setStatus(_B)
_TmnxCallTraceJobSizeLimit_Type=TmnxCallTraceSizeLimit
_TmnxCallTraceJobSizeLimit_Object=MibTableColumn
tmnxCallTraceJobSizeLimit=_TmnxCallTraceJobSizeLimit_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,6),_TmnxCallTraceJobSizeLimit_Type())
tmnxCallTraceJobSizeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobSizeLimit.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceJobSizeLimit.setUnits(_I)
_TmnxCallTraceJobTimeLimit_Type=TmnxCallTraceTimeLimit
_TmnxCallTraceJobTimeLimit_Object=MibTableColumn
tmnxCallTraceJobTimeLimit=_TmnxCallTraceJobTimeLimit_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,7),_TmnxCallTraceJobTimeLimit_Type())
tmnxCallTraceJobTimeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobTimeLimit.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceJobTimeLimit.setUnits('sec')
class _TmnxCallTraceJobCaptureFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('pcap',1))
_TmnxCallTraceJobCaptureFormat_Type.__name__=_L
_TmnxCallTraceJobCaptureFormat_Object=MibTableColumn
tmnxCallTraceJobCaptureFormat=_TmnxCallTraceJobCaptureFormat_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,8),_TmnxCallTraceJobCaptureFormat_Type())
tmnxCallTraceJobCaptureFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobCaptureFormat.setStatus(_N)
_TmnxCallTraceJobDstAddrType_Type=InetAddressType
_TmnxCallTraceJobDstAddrType_Object=MibTableColumn
tmnxCallTraceJobDstAddrType=_TmnxCallTraceJobDstAddrType_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,9),_TmnxCallTraceJobDstAddrType_Type())
tmnxCallTraceJobDstAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobDstAddrType.setStatus(_B)
class _TmnxCallTraceJobDstAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCallTraceJobDstAddr_Type.__name__=_K
_TmnxCallTraceJobDstAddr_Object=MibTableColumn
tmnxCallTraceJobDstAddr=_TmnxCallTraceJobDstAddr_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,10),_TmnxCallTraceJobDstAddr_Type())
tmnxCallTraceJobDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobDstAddr.setStatus(_B)
_TmnxCallTraceJobDstResAddrType_Type=InetAddressType
_TmnxCallTraceJobDstResAddrType_Object=MibTableColumn
tmnxCallTraceJobDstResAddrType=_TmnxCallTraceJobDstResAddrType_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,11),_TmnxCallTraceJobDstResAddrType_Type())
tmnxCallTraceJobDstResAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobDstResAddrType.setStatus(_B)
class _TmnxCallTraceJobDstResAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxCallTraceJobDstResAddr_Type.__name__=_K
_TmnxCallTraceJobDstResAddr_Object=MibTableColumn
tmnxCallTraceJobDstResAddr=_TmnxCallTraceJobDstResAddr_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,12),_TmnxCallTraceJobDstResAddr_Type())
tmnxCallTraceJobDstResAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobDstResAddr.setStatus(_B)
class _TmnxCallTraceJobDstPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxCallTraceJobDstPort_Type.__name__=_W
_TmnxCallTraceJobDstPort_Object=MibTableColumn
tmnxCallTraceJobDstPort=_TmnxCallTraceJobDstPort_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,13),_TmnxCallTraceJobDstPort_Type())
tmnxCallTraceJobDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobDstPort.setStatus(_B)
_TmnxCallTraceJobVRtrId_Type=TmnxVRtrID
_TmnxCallTraceJobVRtrId_Object=MibTableColumn
tmnxCallTraceJobVRtrId=_TmnxCallTraceJobVRtrId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,14),_TmnxCallTraceJobVRtrId_Type())
tmnxCallTraceJobVRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobVRtrId.setStatus(_B)
_TmnxCallTraceJobStartTime_Type=DateAndTime
_TmnxCallTraceJobStartTime_Object=MibTableColumn
tmnxCallTraceJobStartTime=_TmnxCallTraceJobStartTime_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,15),_TmnxCallTraceJobStartTime_Type())
tmnxCallTraceJobStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobStartTime.setStatus(_B)
_TmnxCallTraceJobCaptMsgsCnt_Type=Unsigned32
_TmnxCallTraceJobCaptMsgsCnt_Object=MibTableColumn
tmnxCallTraceJobCaptMsgsCnt=_TmnxCallTraceJobCaptMsgsCnt_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,16),_TmnxCallTraceJobCaptMsgsCnt_Type())
tmnxCallTraceJobCaptMsgsCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobCaptMsgsCnt.setStatus(_B)
_TmnxCallTraceJobCaptMsgsSize_Type=Unsigned32
_TmnxCallTraceJobCaptMsgsSize_Object=MibTableColumn
tmnxCallTraceJobCaptMsgsSize=_TmnxCallTraceJobCaptMsgsSize_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,17),_TmnxCallTraceJobCaptMsgsSize_Type())
tmnxCallTraceJobCaptMsgsSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobCaptMsgsSize.setStatus(_B)
_TmnxCallTraceJobSapPortId_Type=TmnxPortID
_TmnxCallTraceJobSapPortId_Object=MibTableColumn
tmnxCallTraceJobSapPortId=_TmnxCallTraceJobSapPortId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,18),_TmnxCallTraceJobSapPortId_Type())
tmnxCallTraceJobSapPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobSapPortId.setStatus(_B)
_TmnxCallTraceJobSapEncapVal_Type=TmnxEncapVal
_TmnxCallTraceJobSapEncapVal_Object=MibTableColumn
tmnxCallTraceJobSapEncapVal=_TmnxCallTraceJobSapEncapVal_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,19),_TmnxCallTraceJobSapEncapVal_Type())
tmnxCallTraceJobSapEncapVal.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobSapEncapVal.setStatus(_B)
_TmnxCallTraceJobIpoeIeeeAddr_Type=MacAddress
_TmnxCallTraceJobIpoeIeeeAddr_Object=MibTableColumn
tmnxCallTraceJobIpoeIeeeAddr=_TmnxCallTraceJobIpoeIeeeAddr_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,20),_TmnxCallTraceJobIpoeIeeeAddr_Type())
tmnxCallTraceJobIpoeIeeeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobIpoeIeeeAddr.setStatus(_B)
class _TmnxCallTraceJobCircuitId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCallTraceJobCircuitId_Type.__name__=_J
_TmnxCallTraceJobCircuitId_Object=MibTableColumn
tmnxCallTraceJobCircuitId=_TmnxCallTraceJobCircuitId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,21),_TmnxCallTraceJobCircuitId_Type())
tmnxCallTraceJobCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobCircuitId.setStatus(_B)
class _TmnxCallTraceJobRemoteId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCallTraceJobRemoteId_Type.__name__=_J
_TmnxCallTraceJobRemoteId_Object=MibTableColumn
tmnxCallTraceJobRemoteId=_TmnxCallTraceJobRemoteId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,22),_TmnxCallTraceJobRemoteId_Type())
tmnxCallTraceJobRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobRemoteId.setStatus(_B)
_TmnxCallTraceJobTraceName_Type=TNamedItemOrEmpty
_TmnxCallTraceJobTraceName_Object=MibTableColumn
tmnxCallTraceJobTraceName=_TmnxCallTraceJobTraceName_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,23),_TmnxCallTraceJobTraceName_Type())
tmnxCallTraceJobTraceName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobTraceName.setStatus(_B)
class _TmnxCallTraceJobDstType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cflash',1),('live-output',2),('debug-output',3)))
_TmnxCallTraceJobDstType_Type.__name__=_L
_TmnxCallTraceJobDstType_Object=MibTableColumn
tmnxCallTraceJobDstType=_TmnxCallTraceJobDstType_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,24),_TmnxCallTraceJobDstType_Type())
tmnxCallTraceJobDstType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobDstType.setStatus(_B)
class _TmnxCallTraceJobUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_TmnxCallTraceJobUserName_Type.__name__=_J
_TmnxCallTraceJobUserName_Object=MibTableColumn
tmnxCallTraceJobUserName=_TmnxCallTraceJobUserName_Object((1,3,6,1,4,1,6527,3,1,2,102,3,1,1,25),_TmnxCallTraceJobUserName_Type())
tmnxCallTraceJobUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceJobUserName.setStatus(_B)
_TmnxCallTraceFileTable_Object=MibTable
tmnxCallTraceFileTable=_TmnxCallTraceFileTable_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2))
if mibBuilder.loadTexts:tmnxCallTraceFileTable.setStatus(_B)
_TmnxCallTraceFileEntry_Object=MibTableRow
tmnxCallTraceFileEntry=_TmnxCallTraceFileEntry_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1))
tmnxCallTraceFileEntry.setIndexNames((0,_A,_A7),(0,_A,_A8),(0,_A,_A9),(0,_A,_AA))
if mibBuilder.loadTexts:tmnxCallTraceFileEntry.setStatus(_B)
_TmnxCallTraceFileJobStatus_Type=TmnxCallTraceJobStatus
_TmnxCallTraceFileJobStatus_Object=MibTableColumn
tmnxCallTraceFileJobStatus=_TmnxCallTraceFileJobStatus_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,1),_TmnxCallTraceFileJobStatus_Type())
tmnxCallTraceFileJobStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceFileJobStatus.setStatus(_B)
_TmnxCallTraceFileCpmSlotNum_Type=TmnxSlotNum
_TmnxCallTraceFileCpmSlotNum_Object=MibTableColumn
tmnxCallTraceFileCpmSlotNum=_TmnxCallTraceFileCpmSlotNum_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,2),_TmnxCallTraceFileCpmSlotNum_Type())
tmnxCallTraceFileCpmSlotNum.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceFileCpmSlotNum.setStatus(_B)
_TmnxCallTraceFileCFlashId_Type=TmnxCallTraceCFlashId
_TmnxCallTraceFileCFlashId_Object=MibTableColumn
tmnxCallTraceFileCFlashId=_TmnxCallTraceFileCFlashId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,3),_TmnxCallTraceFileCFlashId_Type())
tmnxCallTraceFileCFlashId.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceFileCFlashId.setStatus(_B)
class _TmnxCallTraceFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(38,83))
_TmnxCallTraceFileName_Type.__name__=_G
_TmnxCallTraceFileName_Object=MibTableColumn
tmnxCallTraceFileName=_TmnxCallTraceFileName_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,4),_TmnxCallTraceFileName_Type())
tmnxCallTraceFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceFileName.setStatus(_B)
class _TmnxCallTraceFileDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(18,19))
_TmnxCallTraceFileDir_Type.__name__=_G
_TmnxCallTraceFileDir_Object=MibTableColumn
tmnxCallTraceFileDir=_TmnxCallTraceFileDir_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,5),_TmnxCallTraceFileDir_Type())
tmnxCallTraceFileDir.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceFileDir.setStatus(_B)
_TmnxCallTraceFileSize_Type=Unsigned32
_TmnxCallTraceFileSize_Object=MibTableColumn
tmnxCallTraceFileSize=_TmnxCallTraceFileSize_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,6),_TmnxCallTraceFileSize_Type())
tmnxCallTraceFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceFileSize.setStatus(_B)
if mibBuilder.loadTexts:tmnxCallTraceFileSize.setUnits('bytes')
_TmnxCallTraceFileLastDataModif_Type=DateAndTime
_TmnxCallTraceFileLastDataModif_Object=MibTableColumn
tmnxCallTraceFileLastDataModif=_TmnxCallTraceFileLastDataModif_Object((1,3,6,1,4,1,6527,3,1,2,102,3,2,1,7),_TmnxCallTraceFileLastDataModif_Type())
tmnxCallTraceFileLastDataModif.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceFileLastDataModif.setStatus(_B)
_TmnxCallTraceTraceTable_Object=MibTable
tmnxCallTraceTraceTable=_TmnxCallTraceTraceTable_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3))
if mibBuilder.loadTexts:tmnxCallTraceTraceTable.setStatus(_B)
_TmnxCallTraceTraceEntry_Object=MibTableRow
tmnxCallTraceTraceEntry=_TmnxCallTraceTraceEntry_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1))
tmnxCallTraceTraceEntry.setIndexNames((0,_A,_AB))
if mibBuilder.loadTexts:tmnxCallTraceTraceEntry.setStatus(_B)
class _TmnxCallTraceTraceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_TmnxCallTraceTraceId_Type.__name__=_E
_TmnxCallTraceTraceId_Object=MibTableColumn
tmnxCallTraceTraceId=_TmnxCallTraceTraceId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,1),_TmnxCallTraceTraceId_Type())
tmnxCallTraceTraceId.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCallTraceTraceId.setStatus(_B)
_TmnxCallTraceTraceType_Type=TmnxCallTraceHostType
_TmnxCallTraceTraceType_Object=MibTableColumn
tmnxCallTraceTraceType=_TmnxCallTraceTraceType_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,2),_TmnxCallTraceTraceType_Type())
tmnxCallTraceTraceType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceType.setStatus(_B)
class _TmnxCallTraceTraceSapId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,44))
_TmnxCallTraceTraceSapId_Type.__name__=_G
_TmnxCallTraceTraceSapId_Object=MibTableColumn
tmnxCallTraceTraceSapId=_TmnxCallTraceTraceSapId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,3),_TmnxCallTraceTraceSapId_Type())
tmnxCallTraceTraceSapId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceSapId.setStatus(_B)
class _TmnxCallTraceTraceIeeeAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_TmnxCallTraceTraceIeeeAddr_Type.__name__=_G
_TmnxCallTraceTraceIeeeAddr_Object=MibTableColumn
tmnxCallTraceTraceIeeeAddr=_TmnxCallTraceTraceIeeeAddr_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,4),_TmnxCallTraceTraceIeeeAddr_Type())
tmnxCallTraceTraceIeeeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceIeeeAddr.setStatus(_B)
class _TmnxCallTraceTraceCircuitId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCallTraceTraceCircuitId_Type.__name__=_G
_TmnxCallTraceTraceCircuitId_Object=MibTableColumn
tmnxCallTraceTraceCircuitId=_TmnxCallTraceTraceCircuitId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,5),_TmnxCallTraceTraceCircuitId_Type())
tmnxCallTraceTraceCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceCircuitId.setStatus(_B)
class _TmnxCallTraceTraceRemoteId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCallTraceTraceRemoteId_Type.__name__=_G
_TmnxCallTraceTraceRemoteId_Object=MibTableColumn
tmnxCallTraceTraceRemoteId=_TmnxCallTraceTraceRemoteId_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,6),_TmnxCallTraceTraceRemoteId_Type())
tmnxCallTraceTraceRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceRemoteId.setStatus(_B)
_TmnxCallTraceTraceName_Type=TNamedItem
_TmnxCallTraceTraceName_Object=MibTableColumn
tmnxCallTraceTraceName=_TmnxCallTraceTraceName_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,7),_TmnxCallTraceTraceName_Type())
tmnxCallTraceTraceName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceName.setStatus(_B)
class _TmnxCallTraceTraceMaxJobs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_TmnxCallTraceTraceMaxJobs_Type.__name__=_E
_TmnxCallTraceTraceMaxJobs_Object=MibTableColumn
tmnxCallTraceTraceMaxJobs=_TmnxCallTraceTraceMaxJobs_Object((1,3,6,1,4,1,6527,3,1,2,102,3,3,1,8),_TmnxCallTraceTraceMaxJobs_Type())
tmnxCallTraceTraceMaxJobs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCallTraceTraceMaxJobs.setStatus(_B)
_TmnxCallTraceNotificationObjs_ObjectIdentity=ObjectIdentity
tmnxCallTraceNotificationObjs=_TmnxCallTraceNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,102,20))
_TmnxCallTraceNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxCallTraceNotifyPrefix=_TmnxCallTraceNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,102))
_TmnxCallTraceNotifications_ObjectIdentity=ObjectIdentity
tmnxCallTraceNotifications=_TmnxCallTraceNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,102,0))
tmnxCallTraceLocationEntry.registerAugmentions((_A,_AC))
tmnxCallTraceLocationStatsEntry.setIndexNames(*tmnxCallTraceLocationEntry.getIndexNames())
tmnxCallTraceProfileGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,1))
tmnxCallTraceProfileGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:tmnxCallTraceProfileGroup.setStatus(_B)
tmnxCallTraceLocStoreGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,2))
tmnxCallTraceLocStoreGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_X),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:tmnxCallTraceLocStoreGroup.setStatus(_B)
tmnxCallTraceScalarCfgGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,3))
tmnxCallTraceScalarCfgGroup.setObjects(*((_A,_Y),(_A,_AV)))
if mibBuilder.loadTexts:tmnxCallTraceScalarCfgGroup.setStatus(_B)
tmnxCallTraceJobGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,4))
tmnxCallTraceJobGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:tmnxCallTraceJobGroup.setStatus(_N)
tmnxCallTraceFileGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,6))
tmnxCallTraceFileGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:tmnxCallTraceFileGroup.setStatus(_B)
tmnxCallTraceScalarStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,7))
tmnxCallTraceScalarStatsGroup.setObjects(*((_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:tmnxCallTraceScalarStatsGroup.setStatus(_B)
tmnxCallTraceJob15v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,8))
tmnxCallTraceJob15v0Group.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_Ab)))
if mibBuilder.loadTexts:tmnxCallTraceJob15v0Group.setStatus(_B)
tmnxCallTraceJobObsoletedGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,9))
tmnxCallTraceJobObsoletedGroup.setObjects((_A,_f))
if mibBuilder.loadTexts:tmnxCallTraceJobObsoletedGroup.setStatus(_B)
tmnxCallTraceScalarCfg20v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,10))
tmnxCallTraceScalarCfg20v0Group.setObjects((_A,_Ac))
if mibBuilder.loadTexts:tmnxCallTraceScalarCfg20v0Group.setStatus(_B)
tmnxCallTraceJob20v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,11))
tmnxCallTraceJob20v0Group.setObjects((_A,_Ad))
if mibBuilder.loadTexts:tmnxCallTraceJob20v0Group.setStatus(_B)
tmnxCallTraceIpoeJobGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,2,1))
tmnxCallTraceIpoeJobGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:tmnxCallTraceIpoeJobGroup.setStatus(_B)
tmnxCallTraceIpoeTraceGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,102,2,2,2))
tmnxCallTraceIpoeTraceGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:tmnxCallTraceIpoeTraceGroup.setStatus(_B)
tmnxCallTraceMaxFilesNumReached=NotificationType((1,3,6,1,4,1,6527,3,1,3,102,0,1))
tmnxCallTraceMaxFilesNumReached.setObjects((_A,_Y))
if mibBuilder.loadTexts:tmnxCallTraceMaxFilesNumReached.setStatus(_B)
tmnxCallTraceLocSizeLimitReached=NotificationType((1,3,6,1,4,1,6527,3,1,3,102,0,2))
tmnxCallTraceLocSizeLimitReached.setObjects((_A,_X))
if mibBuilder.loadTexts:tmnxCallTraceLocSizeLimitReached.setStatus(_B)
tmnxCallTraceNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,102,2,1,5))
tmnxCallTraceNotifyGroup.setObjects(*((_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:tmnxCallTraceNotifyGroup.setStatus(_B)
tmnxCallTraceCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,102,1,1))
tmnxCallTraceCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_Am),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:tmnxCallTraceCompliance.setStatus(_N)
tmnxCallTrace15v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,102,1,2))
tmnxCallTrace15v0Compliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_w),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:tmnxCallTrace15v0Compliance.setStatus(_N)
tmnxCallTrace20v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,102,1,3))
tmnxCallTrace20v0Compliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_w),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:tmnxCallTrace20v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_A3:TmnxCallTraceSizeLimit,_A4:TmnxCallTraceTimeLimit,'TmnxCallTraceJobStatus':TmnxCallTraceJobStatus,_A1:TmnxCallTraceCFlashId,'TmnxCallTraceApplications':TmnxCallTraceApplications,'TmnxCallTraceHostType':TmnxCallTraceHostType,'timetraCallTraceMIBModule':timetraCallTraceMIBModule,'tmnxCallTraceConformance':tmnxCallTraceConformance,'tmnxCallTraceCompliances':tmnxCallTraceCompliances,'tmnxCallTraceCompliance':tmnxCallTraceCompliance,'tmnxCallTrace15v0Compliance':tmnxCallTrace15v0Compliance,'tmnxCallTrace20v0Compliance':tmnxCallTrace20v0Compliance,'tmnxCallTraceGroups':tmnxCallTraceGroups,'tmnxCallTraceInitialGroups':tmnxCallTraceInitialGroups,_O:tmnxCallTraceProfileGroup,_P:tmnxCallTraceLocStoreGroup,_Q:tmnxCallTraceScalarCfgGroup,_Am:tmnxCallTraceJobGroup,_R:tmnxCallTraceNotifyGroup,_S:tmnxCallTraceFileGroup,_T:tmnxCallTraceScalarStatsGroup,_w:tmnxCallTraceJob15v0Group,'tmnxCallTraceJobObsoletedGroup':tmnxCallTraceJobObsoletedGroup,_An:tmnxCallTraceScalarCfg20v0Group,_Ao:tmnxCallTraceJob20v0Group,'tmnxCallTraceIpoeGroups':tmnxCallTraceIpoeGroups,_U:tmnxCallTraceIpoeJobGroup,_V:tmnxCallTraceIpoeTraceGroup,'tmnxCallTraceObjs':tmnxCallTraceObjs,'tmnxCallTraceScalarObjs':tmnxCallTraceScalarObjs,'tmnxCallTraceLastChangedObjs':tmnxCallTraceLastChangedObjs,_AD:tmnxCallTraceProfileTblLstChgd,_AQ:tmnxCallTraceLocationTblLstChgd,'tmnxCallTraceScalarConfigObjs':tmnxCallTraceScalarConfigObjs,_Y:tmnxCallTraceMaxFilesNumber,_AV:tmnxCallTracePrimaryCFlash,_Ac:tmnxCallTraceBuffering,'tmnxCallTraceScalarStatsObjs':tmnxCallTraceScalarStatsObjs,_AZ:tmnxCallTraceUsedFilesNumber,_Aa:tmnxCallTraceAvailFilesNumber,'tmnxCallTraceConfigObjs':tmnxCallTraceConfigObjs,'tmnxCallTraceProfileTable':tmnxCallTraceProfileTable,'tmnxCallTraceProfileEntry':tmnxCallTraceProfileEntry,_A2:tmnxCallTraceProfileName,_AE:tmnxCallTraceProfileLstChgd,_AF:tmnxCallTraceProfileRowStatus,_AG:tmnxCallTraceProfileDescription,_AH:tmnxCallTraceProfileSizeLimit,_AI:tmnxCallTraceProfileTimeLimit,_AJ:tmnxCallTraceProfileDstAddrType,_AK:tmnxCallTraceProfileDstAddr,_AL:tmnxCallTraceProfileDstPort,_AM:tmnxCallTraceProfileVRtrId,_AN:tmnxCallTraceProfileApplications,_AO:tmnxCallTraceProfileDbgOutput,_AP:tmnxCallTraceProfileEvents,'tmnxCallTraceLocationTable':tmnxCallTraceLocationTable,'tmnxCallTraceLocationEntry':tmnxCallTraceLocationEntry,_A5:tmnxCallTraceLocationCFlashId,_AR:tmnxCallTraceLocationLstChgd,_X:tmnxCallTraceLocationSizeLimit,_AS:tmnxCallTraceLocationDisable,'tmnxCallTraceLocationStatsTable':tmnxCallTraceLocationStatsTable,_AC:tmnxCallTraceLocationStatsEntry,_AT:tmnxCallTraceLocationUsedSpace,_AU:tmnxCallTraceLocationAvailSpace,'tmnxCallTraceStatsObjs':tmnxCallTraceStatsObjs,'tmnxCallTraceJobTable':tmnxCallTraceJobTable,'tmnxCallTraceJobEntry':tmnxCallTraceJobEntry,_A6:tmnxCallTraceJobId,_Z:tmnxCallTraceJobType,_a:tmnxCallTraceJobWlanGwUeIeeeAddr,_b:tmnxCallTraceJobStatus,_c:tmnxCallTraceJobProfileName,_d:tmnxCallTraceJobSizeLimit,_e:tmnxCallTraceJobTimeLimit,_f:tmnxCallTraceJobCaptureFormat,_g:tmnxCallTraceJobDstAddrType,_h:tmnxCallTraceJobDstAddr,_i:tmnxCallTraceJobDstResAddrType,_j:tmnxCallTraceJobDstResAddr,_k:tmnxCallTraceJobDstPort,_l:tmnxCallTraceJobVRtrId,_m:tmnxCallTraceJobStartTime,_n:tmnxCallTraceJobCaptMsgsCnt,_o:tmnxCallTraceJobCaptMsgsSize,_Ae:tmnxCallTraceJobSapPortId,_Af:tmnxCallTraceJobSapEncapVal,_Ag:tmnxCallTraceJobIpoeIeeeAddr,_Ah:tmnxCallTraceJobCircuitId,_Ai:tmnxCallTraceJobRemoteId,_Aj:tmnxCallTraceJobTraceName,_Ab:tmnxCallTraceJobDstType,_Ad:tmnxCallTraceJobUserName,'tmnxCallTraceFileTable':tmnxCallTraceFileTable,'tmnxCallTraceFileEntry':tmnxCallTraceFileEntry,_A7:tmnxCallTraceFileJobStatus,_A8:tmnxCallTraceFileCpmSlotNum,_A9:tmnxCallTraceFileCFlashId,_AA:tmnxCallTraceFileName,_AW:tmnxCallTraceFileDir,_AX:tmnxCallTraceFileSize,_AY:tmnxCallTraceFileLastDataModif,'tmnxCallTraceTraceTable':tmnxCallTraceTraceTable,'tmnxCallTraceTraceEntry':tmnxCallTraceTraceEntry,_AB:tmnxCallTraceTraceId,_p:tmnxCallTraceTraceType,_q:tmnxCallTraceTraceSapId,_r:tmnxCallTraceTraceIeeeAddr,_s:tmnxCallTraceTraceCircuitId,_t:tmnxCallTraceTraceRemoteId,_u:tmnxCallTraceTraceName,_v:tmnxCallTraceTraceMaxJobs,'tmnxCallTraceNotificationObjs':tmnxCallTraceNotificationObjs,'tmnxCallTraceNotifyPrefix':tmnxCallTraceNotifyPrefix,'tmnxCallTraceNotifications':tmnxCallTraceNotifications,_Ak:tmnxCallTraceMaxFilesNumReached,_Al:tmnxCallTraceLocSizeLimitReached})