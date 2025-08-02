_P='proElsSubSysEventMsg'
_O='proElsTrapEvent'
_N='proElsTrapSubSystem'
_M='proElsTrapSeqs'
_L='proElsSubSysEventIndex'
_K='NotificationType'
_J='ifIndex'
_I='IF-MIB'
_H='proElsSubSysIndex'
_G='deprecated'
_F='DisplayString'
_E='PROTEON-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class ProElsMsgLogLevel(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('other',1),('proMsgLevelUIError',2),('proMsgLevelCIError',3),('proMsgLevelUEError',4),('proMsgLevelCEError',5),('proMsgLevelError',6),('proMsgLevelUInfo',7),('proMsgLevelCInfo',8),('proMsgLevelInfo',9),('proMsgLevelPTrace',10),('proMsgLevelUTrace',11),('proMsgLevelCTrace',12),('proMsgLevelTrace',13),('proMsgLevelAlways',14),('proMsgLevelStandard',15),('proMsgLevelAll',16)))
class ProElsLogStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proElsLogDisabled',1),('proElsLogEnabled',2)))
_Proteon_ObjectIdentity=ObjectIdentity
proteon=_Proteon_ObjectIdentity((1,3,6,1,4,1,1))
_ProAdmin_ObjectIdentity=ObjectIdentity
proAdmin=_ProAdmin_ObjectIdentity((1,3,6,1,4,1,1,1))
_ProSysObjId_ObjectIdentity=ObjectIdentity
proSysObjId=_ProSysObjId_ObjectIdentity((1,3,6,1,4,1,1,1,1))
_ProElsTrapSeqs_Type=Counter32
_ProElsTrapSeqs_Object=MibScalar
proElsTrapSeqs=_ProElsTrapSeqs_Object((1,3,6,1,4,1,1,1,1,1),_ProElsTrapSeqs_Type())
proElsTrapSeqs.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsTrapSeqs.setStatus(_G)
_ProElsTrapSubSystem_Type=Integer32
_ProElsTrapSubSystem_Object=MibScalar
proElsTrapSubSystem=_ProElsTrapSubSystem_Object((1,3,6,1,4,1,1,1,1,2),_ProElsTrapSubSystem_Type())
proElsTrapSubSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsTrapSubSystem.setStatus(_G)
_ProElsTrapEvent_Type=Integer32
_ProElsTrapEvent_Object=MibScalar
proElsTrapEvent=_ProElsTrapEvent_Object((1,3,6,1,4,1,1,1,1,3),_ProElsTrapEvent_Type())
proElsTrapEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsTrapEvent.setStatus(_G)
_ProElsTrapVar1_ObjectIdentity=ObjectIdentity
proElsTrapVar1=_ProElsTrapVar1_ObjectIdentity((1,3,6,1,4,1,1,1,1,5))
_ProElsTrapVar2_ObjectIdentity=ObjectIdentity
proElsTrapVar2=_ProElsTrapVar2_ObjectIdentity((1,3,6,1,4,1,1,1,1,6))
_ProElsTrapVar3_ObjectIdentity=ObjectIdentity
proElsTrapVar3=_ProElsTrapVar3_ObjectIdentity((1,3,6,1,4,1,1,1,1,7))
_ProElsTrapVar4_ObjectIdentity=ObjectIdentity
proElsTrapVar4=_ProElsTrapVar4_ObjectIdentity((1,3,6,1,4,1,1,1,1,8))
_ProElsTrapVar5_ObjectIdentity=ObjectIdentity
proElsTrapVar5=_ProElsTrapVar5_ObjectIdentity((1,3,6,1,4,1,1,1,1,9))
_ProElsTrapVar6_ObjectIdentity=ObjectIdentity
proElsTrapVar6=_ProElsTrapVar6_ObjectIdentity((1,3,6,1,4,1,1,1,1,10))
_ProElsTrapVar7_ObjectIdentity=ObjectIdentity
proElsTrapVar7=_ProElsTrapVar7_ObjectIdentity((1,3,6,1,4,1,1,1,1,11))
_ProElsTrapVar8_ObjectIdentity=ObjectIdentity
proElsTrapVar8=_ProElsTrapVar8_ObjectIdentity((1,3,6,1,4,1,1,1,1,12))
_ProElsTrapVar9_ObjectIdentity=ObjectIdentity
proElsTrapVar9=_ProElsTrapVar9_ObjectIdentity((1,3,6,1,4,1,1,1,1,13))
_ProSysObjIdP4100_ObjectIdentity=ObjectIdentity
proSysObjIdP4100=_ProSysObjIdP4100_ObjectIdentity((1,3,6,1,4,1,1,1,1,41))
_ProSysObjIdP4200_ObjectIdentity=ObjectIdentity
proSysObjIdP4200=_ProSysObjIdP4200_ObjectIdentity((1,3,6,1,4,1,1,1,1,42))
_ProSysObjIdDNX300_ObjectIdentity=ObjectIdentity
proSysObjIdDNX300=_ProSysObjIdDNX300_ObjectIdentity((1,3,6,1,4,1,1,1,1,43))
_ProSysObjIdCNX400_ObjectIdentity=ObjectIdentity
proSysObjIdCNX400=_ProSysObjIdCNX400_ObjectIdentity((1,3,6,1,4,1,1,1,1,44))
_ProSysObjIdCNX600_ObjectIdentity=ObjectIdentity
proSysObjIdCNX600=_ProSysObjIdCNX600_ObjectIdentity((1,3,6,1,4,1,1,1,1,46))
_ProSysObjIdRBX200_ObjectIdentity=ObjectIdentity
proSysObjIdRBX200=_ProSysObjIdRBX200_ObjectIdentity((1,3,6,1,4,1,1,1,1,47))
_ProSysObjIdCNX500_ObjectIdentity=ObjectIdentity
proSysObjIdCNX500=_ProSysObjIdCNX500_ObjectIdentity((1,3,6,1,4,1,1,1,1,49))
_ProSysObjIdRBX250_ObjectIdentity=ObjectIdentity
proSysObjIdRBX250=_ProSysObjIdRBX250_ObjectIdentity((1,3,6,1,4,1,1,1,1,50))
_ProSysObjIdBOSS3Slot_ObjectIdentity=ObjectIdentity
proSysObjIdBOSS3Slot=_ProSysObjIdBOSS3Slot_ObjectIdentity((1,3,6,1,4,1,1,1,1,53))
_ProSysObjIdBOSSs90_ObjectIdentity=ObjectIdentity
proSysObjIdBOSSs90=_ProSysObjIdBOSSs90_ObjectIdentity((1,3,6,1,4,1,1,1,1,54))
_ProStatus_ObjectIdentity=ObjectIdentity
proStatus=_ProStatus_ObjectIdentity((1,3,6,1,4,1,1,1,2))
_ProStatusReloadTime_Type=TimeTicks
_ProStatusReloadTime_Object=MibScalar
proStatusReloadTime=_ProStatusReloadTime_Object((1,3,6,1,4,1,1,1,2,1),_ProStatusReloadTime_Type())
proStatusReloadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:proStatusReloadTime.setStatus(_A)
_ProStatusStarts_Type=Counter32
_ProStatusStarts_Object=MibScalar
proStatusStarts=_ProStatusStarts_Object((1,3,6,1,4,1,1,1,2,2),_ProStatusStarts_Type())
proStatusStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:proStatusStarts.setStatus(_A)
_ProStatusCrashes_Type=Counter32
_ProStatusCrashes_Object=MibScalar
proStatusCrashes=_ProStatusCrashes_Object((1,3,6,1,4,1,1,1,2,3),_ProStatusCrashes_Type())
proStatusCrashes.setMaxAccess(_B)
if mibBuilder.loadTexts:proStatusCrashes.setStatus(_A)
_ProStatusCrashMsg_Type=DisplayString
_ProStatusCrashMsg_Object=MibScalar
proStatusCrashMsg=_ProStatusCrashMsg_Object((1,3,6,1,4,1,1,1,2,4),_ProStatusCrashMsg_Type())
proStatusCrashMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:proStatusCrashMsg.setStatus(_A)
_ProPriv_ObjectIdentity=ObjectIdentity
proPriv=_ProPriv_ObjectIdentity((1,3,6,1,4,1,1,1,5))
_ProActionReset_Type=Integer32
_ProActionReset_Object=MibScalar
proActionReset=_ProActionReset_Object((1,3,6,1,4,1,1,1,5,2),_ProActionReset_Type())
proActionReset.setMaxAccess(_C)
if mibBuilder.loadTexts:proActionReset.setStatus(_A)
_ProActionReload_Type=Integer32
_ProActionReload_Object=MibScalar
proActionReload=_ProActionReload_Object((1,3,6,1,4,1,1,1,5,4),_ProActionReload_Type())
proActionReload.setMaxAccess(_C)
if mibBuilder.loadTexts:proActionReload.setStatus(_A)
_ProSystem_ObjectIdentity=ObjectIdentity
proSystem=_ProSystem_ObjectIdentity((1,3,6,1,4,1,1,6))
_ProResource_ObjectIdentity=ObjectIdentity
proResource=_ProResource_ObjectIdentity((1,3,6,1,4,1,1,6,1))
_ProResMemory_ObjectIdentity=ObjectIdentity
proResMemory=_ProResMemory_ObjectIdentity((1,3,6,1,4,1,1,6,1,1))
_ProResMemHeap_ObjectIdentity=ObjectIdentity
proResMemHeap=_ProResMemHeap_ObjectIdentity((1,3,6,1,4,1,1,6,1,1,1))
_ProResMemHeapTotal_Type=Integer32
_ProResMemHeapTotal_Object=MibScalar
proResMemHeapTotal=_ProResMemHeapTotal_Object((1,3,6,1,4,1,1,6,1,1,1,1),_ProResMemHeapTotal_Type())
proResMemHeapTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemHeapTotal.setStatus(_A)
_ProResMemHeapReserve_Type=Integer32
_ProResMemHeapReserve_Object=MibScalar
proResMemHeapReserve=_ProResMemHeapReserve_Object((1,3,6,1,4,1,1,6,1,1,1,2),_ProResMemHeapReserve_Type())
proResMemHeapReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemHeapReserve.setStatus(_A)
_ProResMemHeapNeverAlloc_Type=Integer32
_ProResMemHeapNeverAlloc_Object=MibScalar
proResMemHeapNeverAlloc=_ProResMemHeapNeverAlloc_Object((1,3,6,1,4,1,1,6,1,1,1,3),_ProResMemHeapNeverAlloc_Type())
proResMemHeapNeverAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemHeapNeverAlloc.setStatus(_A)
_ProResMemHeapPermAlloc_Type=Integer32
_ProResMemHeapPermAlloc_Object=MibScalar
proResMemHeapPermAlloc=_ProResMemHeapPermAlloc_Object((1,3,6,1,4,1,1,6,1,1,1,4),_ProResMemHeapPermAlloc_Type())
proResMemHeapPermAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemHeapPermAlloc.setStatus(_A)
_ProResMemHeapTempAlloc_Type=Integer32
_ProResMemHeapTempAlloc_Object=MibScalar
proResMemHeapTempAlloc=_ProResMemHeapTempAlloc_Object((1,3,6,1,4,1,1,6,1,1,1,5),_ProResMemHeapTempAlloc_Type())
proResMemHeapTempAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemHeapTempAlloc.setStatus(_A)
_ProResMemHeapPrevAlloc_Type=Integer32
_ProResMemHeapPrevAlloc_Object=MibScalar
proResMemHeapPrevAlloc=_ProResMemHeapPrevAlloc_Object((1,3,6,1,4,1,1,6,1,1,1,6),_ProResMemHeapPrevAlloc_Type())
proResMemHeapPrevAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemHeapPrevAlloc.setStatus(_A)
_ProResMemBuf_ObjectIdentity=ObjectIdentity
proResMemBuf=_ProResMemBuf_ObjectIdentity((1,3,6,1,4,1,1,6,1,1,2))
_ProResMemBufTotal_Type=Integer32
_ProResMemBufTotal_Object=MibScalar
proResMemBufTotal=_ProResMemBufTotal_Object((1,3,6,1,4,1,1,6,1,1,2,1),_ProResMemBufTotal_Type())
proResMemBufTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemBufTotal.setStatus(_A)
_ProResMemBufReserve_Type=Integer32
_ProResMemBufReserve_Object=MibScalar
proResMemBufReserve=_ProResMemBufReserve_Object((1,3,6,1,4,1,1,6,1,1,2,2),_ProResMemBufReserve_Type())
proResMemBufReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemBufReserve.setStatus(_A)
_ProResMemBufNeverAlloc_Type=Integer32
_ProResMemBufNeverAlloc_Object=MibScalar
proResMemBufNeverAlloc=_ProResMemBufNeverAlloc_Object((1,3,6,1,4,1,1,6,1,1,2,3),_ProResMemBufNeverAlloc_Type())
proResMemBufNeverAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemBufNeverAlloc.setStatus(_A)
_ProResMemBufPermAlloc_Type=Integer32
_ProResMemBufPermAlloc_Object=MibScalar
proResMemBufPermAlloc=_ProResMemBufPermAlloc_Object((1,3,6,1,4,1,1,6,1,1,2,4),_ProResMemBufPermAlloc_Type())
proResMemBufPermAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResMemBufPermAlloc.setStatus(_A)
_ProResBuffers_ObjectIdentity=ObjectIdentity
proResBuffers=_ProResBuffers_ObjectIdentity((1,3,6,1,4,1,1,6,1,2))
_ProResBufGlobal_ObjectIdentity=ObjectIdentity
proResBufGlobal=_ProResBufGlobal_ObjectIdentity((1,3,6,1,4,1,1,6,1,2,1))
_ProResBufGlobalTotal_Type=Integer32
_ProResBufGlobalTotal_Object=MibScalar
proResBufGlobalTotal=_ProResBufGlobalTotal_Object((1,3,6,1,4,1,1,6,1,2,1,1),_ProResBufGlobalTotal_Type())
proResBufGlobalTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:proResBufGlobalTotal.setStatus(_A)
_ProResBufGlobalFree_Type=Integer32
_ProResBufGlobalFree_Object=MibScalar
proResBufGlobalFree=_ProResBufGlobalFree_Object((1,3,6,1,4,1,1,6,1,2,1,2),_ProResBufGlobalFree_Type())
proResBufGlobalFree.setMaxAccess(_B)
if mibBuilder.loadTexts:proResBufGlobalFree.setStatus(_A)
_ProResBufGlobalFair_Type=Integer32
_ProResBufGlobalFair_Object=MibScalar
proResBufGlobalFair=_ProResBufGlobalFair_Object((1,3,6,1,4,1,1,6,1,2,1,3),_ProResBufGlobalFair_Type())
proResBufGlobalFair.setMaxAccess(_B)
if mibBuilder.loadTexts:proResBufGlobalFair.setStatus(_A)
_ProResBufGlobalLow_Type=Integer32
_ProResBufGlobalLow_Object=MibScalar
proResBufGlobalLow=_ProResBufGlobalLow_Object((1,3,6,1,4,1,1,6,1,2,1,4),_ProResBufGlobalLow_Type())
proResBufGlobalLow.setMaxAccess(_B)
if mibBuilder.loadTexts:proResBufGlobalLow.setStatus(_A)
_ProResBufTable_Object=MibTable
proResBufTable=_ProResBufTable_Object((1,3,6,1,4,1,1,6,1,2,2))
if mibBuilder.loadTexts:proResBufTable.setStatus(_A)
_ProResBufTableEntry_Object=MibTableRow
proResBufTableEntry=_ProResBufTableEntry_Object((1,3,6,1,4,1,1,6,1,2,2,1))
proResBufTableEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:proResBufTableEntry.setStatus(_A)
_ProResInputBufsReq_Type=Integer32
_ProResInputBufsReq_Object=MibTableColumn
proResInputBufsReq=_ProResInputBufsReq_Object((1,3,6,1,4,1,1,6,1,2,2,1,1),_ProResInputBufsReq_Type())
proResInputBufsReq.setMaxAccess(_B)
if mibBuilder.loadTexts:proResInputBufsReq.setStatus(_A)
_ProResInputBufsAlloc_Type=Integer32
_ProResInputBufsAlloc_Object=MibTableColumn
proResInputBufsAlloc=_ProResInputBufsAlloc_Object((1,3,6,1,4,1,1,6,1,2,2,1,2),_ProResInputBufsAlloc_Type())
proResInputBufsAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:proResInputBufsAlloc.setStatus(_A)
_ProResInputBufsLow_Type=Integer32
_ProResInputBufsLow_Object=MibTableColumn
proResInputBufsLow=_ProResInputBufsLow_Object((1,3,6,1,4,1,1,6,1,2,2,1,3),_ProResInputBufsLow_Type())
proResInputBufsLow.setMaxAccess(_B)
if mibBuilder.loadTexts:proResInputBufsLow.setStatus(_A)
_ProResInputBufsCurrent_Type=Integer32
_ProResInputBufsCurrent_Object=MibTableColumn
proResInputBufsCurrent=_ProResInputBufsCurrent_Object((1,3,6,1,4,1,1,6,1,2,2,1,4),_ProResInputBufsCurrent_Type())
proResInputBufsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:proResInputBufsCurrent.setStatus(_A)
_ProResInputBufsSize_Type=Integer32
_ProResInputBufsSize_Object=MibTableColumn
proResInputBufsSize=_ProResInputBufsSize_Object((1,3,6,1,4,1,1,6,1,2,2,1,5),_ProResInputBufsSize_Type())
proResInputBufsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:proResInputBufsSize.setStatus(_A)
_ProResInputBufsTotalBytes_Type=Integer32
_ProResInputBufsTotalBytes_Object=MibTableColumn
proResInputBufsTotalBytes=_ProResInputBufsTotalBytes_Object((1,3,6,1,4,1,1,6,1,2,2,1,6),_ProResInputBufsTotalBytes_Type())
proResInputBufsTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:proResInputBufsTotalBytes.setStatus(_A)
_ProEls_ObjectIdentity=ObjectIdentity
proEls=_ProEls_ObjectIdentity((1,3,6,1,4,1,1,6,2))
_ProElsGeneric_ObjectIdentity=ObjectIdentity
proElsGeneric=_ProElsGeneric_ObjectIdentity((1,3,6,1,4,1,1,6,2,1))
class _ProElsPin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ProElsPin_Type.__name__=_D
_ProElsPin_Object=MibScalar
proElsPin=_ProElsPin_Object((1,3,6,1,4,1,1,6,2,1,1),_ProElsPin_Type())
proElsPin.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsPin.setStatus(_A)
_ProElsDropped_Type=Counter32
_ProElsDropped_Object=MibScalar
proElsDropped=_ProElsDropped_Object((1,3,6,1,4,1,1,6,2,1,2),_ProElsDropped_Type())
proElsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsDropped.setStatus(_A)
class _ProElsTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('proTSOff',1),('proTSSysUpTime',2),('proTSTimeOfDay',3)))
_ProElsTimestamp_Type.__name__=_D
_ProElsTimestamp_Object=MibScalar
proElsTimestamp=_ProElsTimestamp_Object((1,3,6,1,4,1,1,6,2,1,3),_ProElsTimestamp_Type())
proElsTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsTimestamp.setStatus(_A)
class _ProElsAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('proElsActionClear',2),('proElsActionDefault',3)))
_ProElsAction_Type.__name__=_D
_ProElsAction_Object=MibScalar
proElsAction=_ProElsAction_Object((1,3,6,1,4,1,1,6,2,1,4),_ProElsAction_Type())
proElsAction.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsAction.setStatus(_A)
class _ProElsTrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proElsTrapVersionV1',1),('proElsTrapVersionV2',2)))
_ProElsTrapVersion_Type.__name__=_D
_ProElsTrapVersion_Object=MibScalar
proElsTrapVersion=_ProElsTrapVersion_Object((1,3,6,1,4,1,1,6,2,1,5),_ProElsTrapVersion_Type())
proElsTrapVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsTrapVersion.setStatus(_A)
_ProElsSubSysTable_Object=MibTable
proElsSubSysTable=_ProElsSubSysTable_Object((1,3,6,1,4,1,1,6,2,2))
if mibBuilder.loadTexts:proElsSubSysTable.setStatus(_A)
_ProElsSubSysTableEntry_Object=MibTableRow
proElsSubSysTableEntry=_ProElsSubSysTableEntry_Object((1,3,6,1,4,1,1,6,2,2,1))
proElsSubSysTableEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:proElsSubSysTableEntry.setStatus(_A)
class _ProElsSubSysIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,10,11,12,13,14,15,17,18,19,21,22,25,30,35,40,41,42,43,53,54,56,60,72,73,74,75,81,83,84,85,88,90,92,95,96,97,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,119,120,121,123,124,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154)));namedValues=NamedValues(*(('proElsSubSysIndexGw',1),('proElsSubSysIndexFlt',2),('proElsSubSysIndexBrs',3),('proElsSubSysIndexArp',5),('proElsSubSysIndexIp',10),('proElsSubSysIndexIcmp',11),('proElsSubSysIndexTcp',12),('proElsSubSysIndexUdp',13),('proElsSubSysIndexBtp',14),('proElsSubSysIndexRip',15),('proElsSubSysIndexSpf',17),('proElsSubSysIndexMspf',18),('proElsSubSysIndexTftp',19),('proElsSubSysIndexSnmp',21),('proElsSubSysIndexDvm',22),('proElsSubSysIndexDn',25),('proElsSubSysIndexXn',30),('proElsSubSysIndexIpx',35),('proElsSubSysIndexIso',40),('proElsSubSysIndexEsis',41),('proElsSubSysIndexIsis',42),('proElsSubSysIndexDnav',43),('proElsSubSysIndexAp2',53),('proElsSubSysIndexZip2',54),('proElsSubSysIndexR2mp',56),('proElsSubSysIndexVin',60),('proElsSubSysIndexSrt',72),('proElsSubSysIndexStp',73),('proElsSubSysIndexBr',74),('proElsSubSysIndexSrly',75),('proElsSubSysIndexEth',81),('proElsSubSysIndexSl',83),('proElsSubSysIndexTkr',84),('proElsSubSysIndexX25',85),('proElsSubSysIndexFddi',88),('proElsSubSysIndexSdlc',90),('proElsSubSysIndexFr',92),('proElsSubSysIndexPpp',95),('proElsSubSysIndexX251',96),('proElsSubSysIndexX252',97),('proElsSubSysIndexX253',98),('proElsSubSysIndexIsdn',99),('proElsSubSysIndexIppn',100),('proElsSubSysIndexWrs',101),('proElsSubSysIndexLnm',102),('proElsSubSysIndexLlc',103),('proElsSubSysIndexBgp',104),('proElsSubSysIndexMcf',105),('proElsSubSysIndexDls',107),('proElsSubSysIndexV25b',108),('proElsSubSysIndexEzstrt',109),('proElsSubSysIndexAi',110),('proElsSubSysIndexBan',111),('proElsSubSysIndexEnv',112),('proElsSubSysIndexCmp',113),('proElsSubSysIndexNbs',114),('proElsSubSysIndexAtm',115),('proElsSubSysIndexLec',116),('proElsSubSysIndexAppn',117),('proElsSubSysIndexIlmi',119),('proElsSubSysIndexSaal',120),('proElsSubSysIndexSvc',121),('proElsSubSysIndexLes',123),('proElsSubSysIndexLecs',124),('proElsSubSysIndexEvlog',126),('proElsSubSysIndexNot',127),('proElsSubSysIndexMars',128),('proElsSubSysIndexMcs',129),('proElsSubSysIndexIlec',130),('proElsSubSysIndexNhrp',131),('proElsSubSysIndexXtp',132),('proElsSubSysIndexEsc',133),('proElsSubSysIndexBbcm',134),('proElsSubSysIndexLcs',135),('proElsSubSysIndexLsa',136),('proElsSubSysIndexMpc',137),('proElsSubSysIndexRsvp',138),('proElsSubSysIndexVcrm',139),('proElsSubSysIndexScsp',140),('proElsSubSysIndexAllc',141),('proElsSubSysIndexNdr',142),('proElsSubSysIndexV34',143),('proElsSubSysIndexDout',144),('proElsSubSysIndexMlp',145),('proElsSubSysIndexDhcp',146),('proElsSubSysIndexSec',147),('proElsSubSysIndexEncr',148),('proElsSubSysIndexPm',149),('proElsSubSysIndexVlan',150),('proElsSubSysIndexDgw',151),('proElsSubSysIndexQllc',152),('proElsSubSysIndexAris',153),('proElsSubSysIndexGsmp',154)))
_ProElsSubSysIndex_Type.__name__=_D
_ProElsSubSysIndex_Object=MibTableColumn
proElsSubSysIndex=_ProElsSubSysIndex_Object((1,3,6,1,4,1,1,6,2,2,1,1),_ProElsSubSysIndex_Type())
proElsSubSysIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysIndex.setStatus(_A)
class _ProElsSubSysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ProElsSubSysDescr_Type.__name__=_F
_ProElsSubSysDescr_Object=MibTableColumn
proElsSubSysDescr=_ProElsSubSysDescr_Object((1,3,6,1,4,1,1,6,2,2,1,2),_ProElsSubSysDescr_Type())
proElsSubSysDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysDescr.setStatus(_A)
_ProElsSubSysNumEvents_Type=Integer32
_ProElsSubSysNumEvents_Object=MibTableColumn
proElsSubSysNumEvents=_ProElsSubSysNumEvents_Object((1,3,6,1,4,1,1,6,2,2,1,3),_ProElsSubSysNumEvents_Type())
proElsSubSysNumEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysNumEvents.setStatus(_A)
_ProElsSubSysDisplayEnable_Type=ProElsMsgLogLevel
_ProElsSubSysDisplayEnable_Object=MibTableColumn
proElsSubSysDisplayEnable=_ProElsSubSysDisplayEnable_Object((1,3,6,1,4,1,1,6,2,2,1,4),_ProElsSubSysDisplayEnable_Type())
proElsSubSysDisplayEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsSubSysDisplayEnable.setStatus(_A)
_ProElsSubSysDisplayDisable_Type=ProElsMsgLogLevel
_ProElsSubSysDisplayDisable_Object=MibTableColumn
proElsSubSysDisplayDisable=_ProElsSubSysDisplayDisable_Object((1,3,6,1,4,1,1,6,2,2,1,5),_ProElsSubSysDisplayDisable_Type())
proElsSubSysDisplayDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsSubSysDisplayDisable.setStatus(_A)
_ProElsSubSysTrapEnable_Type=ProElsMsgLogLevel
_ProElsSubSysTrapEnable_Object=MibTableColumn
proElsSubSysTrapEnable=_ProElsSubSysTrapEnable_Object((1,3,6,1,4,1,1,6,2,2,1,6),_ProElsSubSysTrapEnable_Type())
proElsSubSysTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsSubSysTrapEnable.setStatus(_A)
_ProElsSubSysTrapDisable_Type=ProElsMsgLogLevel
_ProElsSubSysTrapDisable_Object=MibTableColumn
proElsSubSysTrapDisable=_ProElsSubSysTrapDisable_Object((1,3,6,1,4,1,1,6,2,2,1,7),_ProElsSubSysTrapDisable_Type())
proElsSubSysTrapDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsSubSysTrapDisable.setStatus(_A)
_ProElsSubSysCurrDisplayLevel_Type=Integer32
_ProElsSubSysCurrDisplayLevel_Object=MibTableColumn
proElsSubSysCurrDisplayLevel=_ProElsSubSysCurrDisplayLevel_Object((1,3,6,1,4,1,1,6,2,2,1,8),_ProElsSubSysCurrDisplayLevel_Type())
proElsSubSysCurrDisplayLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysCurrDisplayLevel.setStatus(_A)
_ProElsSubSysCurrTrapLevel_Type=Integer32
_ProElsSubSysCurrTrapLevel_Object=MibTableColumn
proElsSubSysCurrTrapLevel=_ProElsSubSysCurrTrapLevel_Object((1,3,6,1,4,1,1,6,2,2,1,9),_ProElsSubSysCurrTrapLevel_Type())
proElsSubSysCurrTrapLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysCurrTrapLevel.setStatus(_A)
_ProElsSubSysEventTable_Object=MibTable
proElsSubSysEventTable=_ProElsSubSysEventTable_Object((1,3,6,1,4,1,1,6,2,3))
if mibBuilder.loadTexts:proElsSubSysEventTable.setStatus(_A)
_ProElsSubSysEventTableEntry_Object=MibTableRow
proElsSubSysEventTableEntry=_ProElsSubSysEventTableEntry_Object((1,3,6,1,4,1,1,6,2,3,1))
proElsSubSysEventTableEntry.setIndexNames((0,_E,_H),(0,_E,_L))
if mibBuilder.loadTexts:proElsSubSysEventTableEntry.setStatus(_A)
_ProElsSubSysEventIndex_Type=Integer32
_ProElsSubSysEventIndex_Object=MibTableColumn
proElsSubSysEventIndex=_ProElsSubSysEventIndex_Object((1,3,6,1,4,1,1,6,2,3,1,1),_ProElsSubSysEventIndex_Type())
proElsSubSysEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysEventIndex.setStatus(_A)
_ProElsSubSysEventMsg_Type=DisplayString
_ProElsSubSysEventMsg_Object=MibTableColumn
proElsSubSysEventMsg=_ProElsSubSysEventMsg_Object((1,3,6,1,4,1,1,6,2,3,1,2),_ProElsSubSysEventMsg_Type())
proElsSubSysEventMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysEventMsg.setStatus(_A)
_ProElsSubSysEventCount_Type=Integer32
_ProElsSubSysEventCount_Object=MibTableColumn
proElsSubSysEventCount=_ProElsSubSysEventCount_Object((1,3,6,1,4,1,1,6,2,3,1,3),_ProElsSubSysEventCount_Type())
proElsSubSysEventCount.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysEventCount.setStatus(_A)
_ProElsSubSysEventLogLevel_Type=ProElsMsgLogLevel
_ProElsSubSysEventLogLevel_Object=MibTableColumn
proElsSubSysEventLogLevel=_ProElsSubSysEventLogLevel_Object((1,3,6,1,4,1,1,6,2,3,1,4),_ProElsSubSysEventLogLevel_Type())
proElsSubSysEventLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:proElsSubSysEventLogLevel.setStatus(_A)
_ProElsSubSysEventLogToConsole_Type=ProElsLogStatus
_ProElsSubSysEventLogToConsole_Object=MibTableColumn
proElsSubSysEventLogToConsole=_ProElsSubSysEventLogToConsole_Object((1,3,6,1,4,1,1,6,2,3,1,5),_ProElsSubSysEventLogToConsole_Type())
proElsSubSysEventLogToConsole.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsSubSysEventLogToConsole.setStatus(_A)
_ProElsSubSysEventLogToTrap_Type=ProElsLogStatus
_ProElsSubSysEventLogToTrap_Object=MibTableColumn
proElsSubSysEventLogToTrap=_ProElsSubSysEventLogToTrap_Object((1,3,6,1,4,1,1,6,2,3,1,6),_ProElsSubSysEventLogToTrap_Type())
proElsSubSysEventLogToTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:proElsSubSysEventLogToTrap.setStatus(_A)
_ProTemp_ObjectIdentity=ObjectIdentity
proTemp=_ProTemp_ObjectIdentity((1,3,6,1,4,1,1,6,3))
class _ProTempScale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('celsius',1),('fahrenheit',2)))
_ProTempScale_Type.__name__=_D
_ProTempScale_Object=MibScalar
proTempScale=_ProTempScale_Object((1,3,6,1,4,1,1,6,3,1),_ProTempScale_Type())
proTempScale.setMaxAccess(_B)
if mibBuilder.loadTexts:proTempScale.setStatus(_A)
_ProMaxHwTemp_Type=Integer32
_ProMaxHwTemp_Object=MibScalar
proMaxHwTemp=_ProMaxHwTemp_Object((1,3,6,1,4,1,1,6,3,2),_ProMaxHwTemp_Type())
proMaxHwTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:proMaxHwTemp.setStatus(_A)
_ProMinHwTemp_Type=Integer32
_ProMinHwTemp_Object=MibScalar
proMinHwTemp=_ProMinHwTemp_Object((1,3,6,1,4,1,1,6,3,3),_ProMinHwTemp_Type())
proMinHwTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:proMinHwTemp.setStatus(_A)
class _ProTempPollPeriod_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_ProTempPollPeriod_Type.__name__=_D
_ProTempPollPeriod_Object=MibScalar
proTempPollPeriod=_ProTempPollPeriod_Object((1,3,6,1,4,1,1,6,3,4),_ProTempPollPeriod_Type())
proTempPollPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:proTempPollPeriod.setStatus(_A)
_ProCurrentTemp_Type=Integer32
_ProCurrentTemp_Object=MibScalar
proCurrentTemp=_ProCurrentTemp_Object((1,3,6,1,4,1,1,6,3,5),_ProCurrentTemp_Type())
proCurrentTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:proCurrentTemp.setStatus(_A)
_ProLowTempThreshold_Type=Integer32
_ProLowTempThreshold_Object=MibScalar
proLowTempThreshold=_ProLowTempThreshold_Object((1,3,6,1,4,1,1,6,3,6),_ProLowTempThreshold_Type())
proLowTempThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:proLowTempThreshold.setStatus(_A)
_ProHighTempThreshold_Type=Integer32
_ProHighTempThreshold_Object=MibScalar
proHighTempThreshold=_ProHighTempThreshold_Object((1,3,6,1,4,1,1,6,3,7),_ProHighTempThreshold_Type())
proHighTempThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:proHighTempThreshold.setStatus(_A)
class _ProTempHysteresis_Type(Integer32):defaultValue=5
_ProTempHysteresis_Type.__name__=_D
_ProTempHysteresis_Object=MibScalar
proTempHysteresis=_ProTempHysteresis_Object((1,3,6,1,4,1,1,6,3,8),_ProTempHysteresis_Type())
proTempHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:proTempHysteresis.setStatus(_A)
class _ProHighTempCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ProHighTempCondition_Type.__name__=_D
_ProHighTempCondition_Object=MibScalar
proHighTempCondition=_ProHighTempCondition_Object((1,3,6,1,4,1,1,6,3,9),_ProHighTempCondition_Type())
proHighTempCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:proHighTempCondition.setStatus(_A)
class _ProLowTempCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ProLowTempCondition_Type.__name__=_D
_ProLowTempCondition_Object=MibScalar
proLowTempCondition=_ProLowTempCondition_Object((1,3,6,1,4,1,1,6,3,10),_ProLowTempCondition_Type())
proLowTempCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:proLowTempCondition.setStatus(_A)
_ProHighestTemp_Type=Integer32
_ProHighestTemp_Object=MibScalar
proHighestTemp=_ProHighestTemp_Object((1,3,6,1,4,1,1,6,3,11),_ProHighestTemp_Type())
proHighestTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:proHighestTemp.setStatus(_A)
_ProHighTempTime_Type=TimeTicks
_ProHighTempTime_Object=MibScalar
proHighTempTime=_ProHighTempTime_Object((1,3,6,1,4,1,1,6,3,12),_ProHighTempTime_Type())
proHighTempTime.setMaxAccess(_B)
if mibBuilder.loadTexts:proHighTempTime.setStatus(_A)
_ProLowestTemp_Type=Integer32
_ProLowestTemp_Object=MibScalar
proLowestTemp=_ProLowestTemp_Object((1,3,6,1,4,1,1,6,3,13),_ProLowestTemp_Type())
proLowestTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:proLowestTemp.setStatus(_A)
_ProLowTempTime_Type=TimeTicks
_ProLowTempTime_Object=MibScalar
proLowTempTime=_ProLowTempTime_Object((1,3,6,1,4,1,1,6,3,14),_ProLowTempTime_Type())
proLowTempTime.setMaxAccess(_B)
if mibBuilder.loadTexts:proLowTempTime.setStatus(_A)
_ProConfig_ObjectIdentity=ObjectIdentity
proConfig=_ProConfig_ObjectIdentity((1,3,6,1,4,1,1,6,4))
_ProCfgLoad_ObjectIdentity=ObjectIdentity
proCfgLoad=_ProCfgLoad_ObjectIdentity((1,3,6,1,4,1,1,6,4,1))
class _ProCfgProtocols_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProCfgProtocols_Type.__name__=_F
_ProCfgProtocols_Object=MibScalar
proCfgProtocols=_ProCfgProtocols_Object((1,3,6,1,4,1,1,6,4,1,1),_ProCfgProtocols_Type())
proCfgProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:proCfgProtocols.setStatus(_A)
class _ProCfgDatalinks_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProCfgDatalinks_Type.__name__=_F
_ProCfgDatalinks_Object=MibScalar
proCfgDatalinks=_ProCfgDatalinks_Object((1,3,6,1,4,1,1,6,4,1,2),_ProCfgDatalinks_Type())
proCfgDatalinks.setMaxAccess(_B)
if mibBuilder.loadTexts:proCfgDatalinks.setStatus(_A)
class _ProCfgFeatures_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProCfgFeatures_Type.__name__=_F
_ProCfgFeatures_Object=MibScalar
proCfgFeatures=_ProCfgFeatures_Object((1,3,6,1,4,1,1,6,4,1,3),_ProCfgFeatures_Type())
proCfgFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:proCfgFeatures.setStatus(_A)
proElsTrapV1=NotificationType((1,3,6,1,4,1,1,0,1))
proElsTrapV1.setObjects(*((_E,_M),(_E,_N),(_E,_O)))
if mibBuilder.loadTexts:proElsTrapV1.setStatus('')
proElsTrapV2=NotificationType((1,3,6,1,4,1,1,0,2))
proElsTrapV2.setObjects((_E,_P))
if mibBuilder.loadTexts:proElsTrapV2.setStatus('')
mibBuilder.exportSymbols(_E,**{'ProElsMsgLogLevel':ProElsMsgLogLevel,'ProElsLogStatus':ProElsLogStatus,'proteon':proteon,'proElsTrapV1':proElsTrapV1,'proElsTrapV2':proElsTrapV2,'proAdmin':proAdmin,'proSysObjId':proSysObjId,_M:proElsTrapSeqs,_N:proElsTrapSubSystem,_O:proElsTrapEvent,'proElsTrapVar1':proElsTrapVar1,'proElsTrapVar2':proElsTrapVar2,'proElsTrapVar3':proElsTrapVar3,'proElsTrapVar4':proElsTrapVar4,'proElsTrapVar5':proElsTrapVar5,'proElsTrapVar6':proElsTrapVar6,'proElsTrapVar7':proElsTrapVar7,'proElsTrapVar8':proElsTrapVar8,'proElsTrapVar9':proElsTrapVar9,'proSysObjIdP4100':proSysObjIdP4100,'proSysObjIdP4200':proSysObjIdP4200,'proSysObjIdDNX300':proSysObjIdDNX300,'proSysObjIdCNX400':proSysObjIdCNX400,'proSysObjIdCNX600':proSysObjIdCNX600,'proSysObjIdRBX200':proSysObjIdRBX200,'proSysObjIdCNX500':proSysObjIdCNX500,'proSysObjIdRBX250':proSysObjIdRBX250,'proSysObjIdBOSS3Slot':proSysObjIdBOSS3Slot,'proSysObjIdBOSSs90':proSysObjIdBOSSs90,'proStatus':proStatus,'proStatusReloadTime':proStatusReloadTime,'proStatusStarts':proStatusStarts,'proStatusCrashes':proStatusCrashes,'proStatusCrashMsg':proStatusCrashMsg,'proPriv':proPriv,'proActionReset':proActionReset,'proActionReload':proActionReload,'proSystem':proSystem,'proResource':proResource,'proResMemory':proResMemory,'proResMemHeap':proResMemHeap,'proResMemHeapTotal':proResMemHeapTotal,'proResMemHeapReserve':proResMemHeapReserve,'proResMemHeapNeverAlloc':proResMemHeapNeverAlloc,'proResMemHeapPermAlloc':proResMemHeapPermAlloc,'proResMemHeapTempAlloc':proResMemHeapTempAlloc,'proResMemHeapPrevAlloc':proResMemHeapPrevAlloc,'proResMemBuf':proResMemBuf,'proResMemBufTotal':proResMemBufTotal,'proResMemBufReserve':proResMemBufReserve,'proResMemBufNeverAlloc':proResMemBufNeverAlloc,'proResMemBufPermAlloc':proResMemBufPermAlloc,'proResBuffers':proResBuffers,'proResBufGlobal':proResBufGlobal,'proResBufGlobalTotal':proResBufGlobalTotal,'proResBufGlobalFree':proResBufGlobalFree,'proResBufGlobalFair':proResBufGlobalFair,'proResBufGlobalLow':proResBufGlobalLow,'proResBufTable':proResBufTable,'proResBufTableEntry':proResBufTableEntry,'proResInputBufsReq':proResInputBufsReq,'proResInputBufsAlloc':proResInputBufsAlloc,'proResInputBufsLow':proResInputBufsLow,'proResInputBufsCurrent':proResInputBufsCurrent,'proResInputBufsSize':proResInputBufsSize,'proResInputBufsTotalBytes':proResInputBufsTotalBytes,'proEls':proEls,'proElsGeneric':proElsGeneric,'proElsPin':proElsPin,'proElsDropped':proElsDropped,'proElsTimestamp':proElsTimestamp,'proElsAction':proElsAction,'proElsTrapVersion':proElsTrapVersion,'proElsSubSysTable':proElsSubSysTable,'proElsSubSysTableEntry':proElsSubSysTableEntry,_H:proElsSubSysIndex,'proElsSubSysDescr':proElsSubSysDescr,'proElsSubSysNumEvents':proElsSubSysNumEvents,'proElsSubSysDisplayEnable':proElsSubSysDisplayEnable,'proElsSubSysDisplayDisable':proElsSubSysDisplayDisable,'proElsSubSysTrapEnable':proElsSubSysTrapEnable,'proElsSubSysTrapDisable':proElsSubSysTrapDisable,'proElsSubSysCurrDisplayLevel':proElsSubSysCurrDisplayLevel,'proElsSubSysCurrTrapLevel':proElsSubSysCurrTrapLevel,'proElsSubSysEventTable':proElsSubSysEventTable,'proElsSubSysEventTableEntry':proElsSubSysEventTableEntry,_L:proElsSubSysEventIndex,_P:proElsSubSysEventMsg,'proElsSubSysEventCount':proElsSubSysEventCount,'proElsSubSysEventLogLevel':proElsSubSysEventLogLevel,'proElsSubSysEventLogToConsole':proElsSubSysEventLogToConsole,'proElsSubSysEventLogToTrap':proElsSubSysEventLogToTrap,'proTemp':proTemp,'proTempScale':proTempScale,'proMaxHwTemp':proMaxHwTemp,'proMinHwTemp':proMinHwTemp,'proTempPollPeriod':proTempPollPeriod,'proCurrentTemp':proCurrentTemp,'proLowTempThreshold':proLowTempThreshold,'proHighTempThreshold':proHighTempThreshold,'proTempHysteresis':proTempHysteresis,'proHighTempCondition':proHighTempCondition,'proLowTempCondition':proLowTempCondition,'proHighestTemp':proHighestTemp,'proHighTempTime':proHighTempTime,'proLowestTemp':proLowestTemp,'proLowTempTime':proLowTempTime,'proConfig':proConfig,'proCfgLoad':proCfgLoad,'proCfgProtocols':proCfgProtocols,'proCfgDatalinks':proCfgDatalinks,'proCfgFeatures':proCfgFeatures})