_F='dskIndex'
_E='BORDERWARE-MIB'
_D='Integer32'
_C='deprecated'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
borderware=ModuleIdentity((1,3,6,1,4,1,8673))
if mibBuilder.loadTexts:borderware.setRevisions(('2002-11-07 00:00',))
class Float(TextualConvention,Opaque):status=_B;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_BwProducts_ObjectIdentity=ObjectIdentity
bwProducts=_BwProducts_ObjectIdentity((1,3,6,1,4,1,8673,1))
_BwProductId_ObjectIdentity=ObjectIdentity
bwProductId=_BwProductId_ObjectIdentity((1,3,6,1,4,1,8673,1,2))
_BwFirewallServer7_ObjectIdentity=ObjectIdentity
bwFirewallServer7=_BwFirewallServer7_ObjectIdentity((1,3,6,1,4,1,8673,1,2,1))
_BwSysMemory_ObjectIdentity=ObjectIdentity
bwSysMemory=_BwSysMemory_ObjectIdentity((1,3,6,1,4,1,8673,4))
_MemIndex_Type=Integer32
_MemIndex_Object=MibScalar
memIndex=_MemIndex_Object((1,3,6,1,4,1,8673,4,1),_MemIndex_Type())
memIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:memIndex.setStatus(_B)
_MemErrorName_Type=DisplayString
_MemErrorName_Object=MibScalar
memErrorName=_MemErrorName_Object((1,3,6,1,4,1,8673,4,2),_MemErrorName_Type())
memErrorName.setMaxAccess(_A)
if mibBuilder.loadTexts:memErrorName.setStatus(_B)
_MemTotalSwap_Type=Integer32
_MemTotalSwap_Object=MibScalar
memTotalSwap=_MemTotalSwap_Object((1,3,6,1,4,1,8673,4,3),_MemTotalSwap_Type())
memTotalSwap.setMaxAccess(_A)
if mibBuilder.loadTexts:memTotalSwap.setStatus(_B)
_MemAvailSwap_Type=Integer32
_MemAvailSwap_Object=MibScalar
memAvailSwap=_MemAvailSwap_Object((1,3,6,1,4,1,8673,4,4),_MemAvailSwap_Type())
memAvailSwap.setMaxAccess(_A)
if mibBuilder.loadTexts:memAvailSwap.setStatus(_B)
_MemTotalReal_Type=Integer32
_MemTotalReal_Object=MibScalar
memTotalReal=_MemTotalReal_Object((1,3,6,1,4,1,8673,4,5),_MemTotalReal_Type())
memTotalReal.setMaxAccess(_A)
if mibBuilder.loadTexts:memTotalReal.setStatus(_B)
_MemAvailReal_Type=Integer32
_MemAvailReal_Object=MibScalar
memAvailReal=_MemAvailReal_Object((1,3,6,1,4,1,8673,4,6),_MemAvailReal_Type())
memAvailReal.setMaxAccess(_A)
if mibBuilder.loadTexts:memAvailReal.setStatus(_B)
_MemTotalSwapTXT_Type=Integer32
_MemTotalSwapTXT_Object=MibScalar
memTotalSwapTXT=_MemTotalSwapTXT_Object((1,3,6,1,4,1,8673,4,7),_MemTotalSwapTXT_Type())
memTotalSwapTXT.setMaxAccess(_A)
if mibBuilder.loadTexts:memTotalSwapTXT.setStatus(_B)
_MemAvailSwapTXT_Type=Integer32
_MemAvailSwapTXT_Object=MibScalar
memAvailSwapTXT=_MemAvailSwapTXT_Object((1,3,6,1,4,1,8673,4,8),_MemAvailSwapTXT_Type())
memAvailSwapTXT.setMaxAccess(_A)
if mibBuilder.loadTexts:memAvailSwapTXT.setStatus(_B)
_MemTotalRealTXT_Type=Integer32
_MemTotalRealTXT_Object=MibScalar
memTotalRealTXT=_MemTotalRealTXT_Object((1,3,6,1,4,1,8673,4,9),_MemTotalRealTXT_Type())
memTotalRealTXT.setMaxAccess(_A)
if mibBuilder.loadTexts:memTotalRealTXT.setStatus(_B)
_MemAvailRealTXT_Type=Integer32
_MemAvailRealTXT_Object=MibScalar
memAvailRealTXT=_MemAvailRealTXT_Object((1,3,6,1,4,1,8673,4,10),_MemAvailRealTXT_Type())
memAvailRealTXT.setMaxAccess(_A)
if mibBuilder.loadTexts:memAvailRealTXT.setStatus(_B)
_MemTotalFree_Type=Integer32
_MemTotalFree_Object=MibScalar
memTotalFree=_MemTotalFree_Object((1,3,6,1,4,1,8673,4,11),_MemTotalFree_Type())
memTotalFree.setMaxAccess(_A)
if mibBuilder.loadTexts:memTotalFree.setStatus(_B)
_MemMinimumSwap_Type=Integer32
_MemMinimumSwap_Object=MibScalar
memMinimumSwap=_MemMinimumSwap_Object((1,3,6,1,4,1,8673,4,12),_MemMinimumSwap_Type())
memMinimumSwap.setMaxAccess(_A)
if mibBuilder.loadTexts:memMinimumSwap.setStatus(_B)
_MemShared_Type=Integer32
_MemShared_Object=MibScalar
memShared=_MemShared_Object((1,3,6,1,4,1,8673,4,13),_MemShared_Type())
memShared.setMaxAccess(_A)
if mibBuilder.loadTexts:memShared.setStatus(_B)
_MemBuffer_Type=Integer32
_MemBuffer_Object=MibScalar
memBuffer=_MemBuffer_Object((1,3,6,1,4,1,8673,4,14),_MemBuffer_Type())
memBuffer.setMaxAccess(_A)
if mibBuilder.loadTexts:memBuffer.setStatus(_B)
_MemCached_Type=Integer32
_MemCached_Object=MibScalar
memCached=_MemCached_Object((1,3,6,1,4,1,8673,4,15),_MemCached_Type())
memCached.setMaxAccess(_A)
if mibBuilder.loadTexts:memCached.setStatus(_B)
_MemSwapError_Type=Integer32
_MemSwapError_Object=MibScalar
memSwapError=_MemSwapError_Object((1,3,6,1,4,1,8673,4,100),_MemSwapError_Type())
memSwapError.setMaxAccess(_A)
if mibBuilder.loadTexts:memSwapError.setStatus(_B)
_MemSwapErrorMsg_Type=DisplayString
_MemSwapErrorMsg_Object=MibScalar
memSwapErrorMsg=_MemSwapErrorMsg_Object((1,3,6,1,4,1,8673,4,101),_MemSwapErrorMsg_Type())
memSwapErrorMsg.setMaxAccess(_A)
if mibBuilder.loadTexts:memSwapErrorMsg.setStatus(_B)
_DskTable_Object=MibTable
dskTable=_DskTable_Object((1,3,6,1,4,1,8673,9))
if mibBuilder.loadTexts:dskTable.setStatus(_B)
_DskEntry_Object=MibTableRow
dskEntry=_DskEntry_Object((1,3,6,1,4,1,8673,9,1))
dskEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dskEntry.setStatus(_B)
class _DskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DskIndex_Type.__name__=_D
_DskIndex_Object=MibTableColumn
dskIndex=_DskIndex_Object((1,3,6,1,4,1,8673,9,1,1),_DskIndex_Type())
dskIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:dskIndex.setStatus(_B)
_DskPath_Type=DisplayString
_DskPath_Object=MibTableColumn
dskPath=_DskPath_Object((1,3,6,1,4,1,8673,9,1,2),_DskPath_Type())
dskPath.setMaxAccess(_A)
if mibBuilder.loadTexts:dskPath.setStatus(_B)
_DskDevice_Type=DisplayString
_DskDevice_Object=MibTableColumn
dskDevice=_DskDevice_Object((1,3,6,1,4,1,8673,9,1,3),_DskDevice_Type())
dskDevice.setMaxAccess(_A)
if mibBuilder.loadTexts:dskDevice.setStatus(_B)
_DskMinimum_Type=Integer32
_DskMinimum_Object=MibTableColumn
dskMinimum=_DskMinimum_Object((1,3,6,1,4,1,8673,9,1,4),_DskMinimum_Type())
dskMinimum.setMaxAccess(_A)
if mibBuilder.loadTexts:dskMinimum.setStatus(_B)
_DskMinPercent_Type=Integer32
_DskMinPercent_Object=MibTableColumn
dskMinPercent=_DskMinPercent_Object((1,3,6,1,4,1,8673,9,1,5),_DskMinPercent_Type())
dskMinPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:dskMinPercent.setStatus(_B)
_DskTotal_Type=Integer32
_DskTotal_Object=MibTableColumn
dskTotal=_DskTotal_Object((1,3,6,1,4,1,8673,9,1,6),_DskTotal_Type())
dskTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:dskTotal.setStatus(_B)
_DskAvail_Type=Integer32
_DskAvail_Object=MibTableColumn
dskAvail=_DskAvail_Object((1,3,6,1,4,1,8673,9,1,7),_DskAvail_Type())
dskAvail.setMaxAccess(_A)
if mibBuilder.loadTexts:dskAvail.setStatus(_B)
_DskUsed_Type=Integer32
_DskUsed_Object=MibTableColumn
dskUsed=_DskUsed_Object((1,3,6,1,4,1,8673,9,1,8),_DskUsed_Type())
dskUsed.setMaxAccess(_A)
if mibBuilder.loadTexts:dskUsed.setStatus(_B)
_DskPercent_Type=Integer32
_DskPercent_Object=MibTableColumn
dskPercent=_DskPercent_Object((1,3,6,1,4,1,8673,9,1,9),_DskPercent_Type())
dskPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:dskPercent.setStatus(_B)
_DskPercentNode_Type=Integer32
_DskPercentNode_Object=MibTableColumn
dskPercentNode=_DskPercentNode_Object((1,3,6,1,4,1,8673,9,1,10),_DskPercentNode_Type())
dskPercentNode.setMaxAccess(_A)
if mibBuilder.loadTexts:dskPercentNode.setStatus(_B)
_DskErrorFlag_Type=Integer32
_DskErrorFlag_Object=MibTableColumn
dskErrorFlag=_DskErrorFlag_Object((1,3,6,1,4,1,8673,9,1,100),_DskErrorFlag_Type())
dskErrorFlag.setMaxAccess(_A)
if mibBuilder.loadTexts:dskErrorFlag.setStatus(_B)
_DskErrorMsg_Type=DisplayString
_DskErrorMsg_Object=MibTableColumn
dskErrorMsg=_DskErrorMsg_Object((1,3,6,1,4,1,8673,9,1,101),_DskErrorMsg_Type())
dskErrorMsg.setMaxAccess(_A)
if mibBuilder.loadTexts:dskErrorMsg.setStatus(_B)
_SystemStats_ObjectIdentity=ObjectIdentity
systemStats=_SystemStats_ObjectIdentity((1,3,6,1,4,1,8673,11))
_SsIndex_Type=Integer32
_SsIndex_Object=MibScalar
ssIndex=_SsIndex_Object((1,3,6,1,4,1,8673,11,1),_SsIndex_Type())
ssIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ssIndex.setStatus(_B)
_SsErrorName_Type=DisplayString
_SsErrorName_Object=MibScalar
ssErrorName=_SsErrorName_Object((1,3,6,1,4,1,8673,11,2),_SsErrorName_Type())
ssErrorName.setMaxAccess(_A)
if mibBuilder.loadTexts:ssErrorName.setStatus(_B)
_SsSwapIn_Type=Integer32
_SsSwapIn_Object=MibScalar
ssSwapIn=_SsSwapIn_Object((1,3,6,1,4,1,8673,11,3),_SsSwapIn_Type())
ssSwapIn.setMaxAccess(_A)
if mibBuilder.loadTexts:ssSwapIn.setStatus(_B)
_SsSwapOut_Type=Integer32
_SsSwapOut_Object=MibScalar
ssSwapOut=_SsSwapOut_Object((1,3,6,1,4,1,8673,11,4),_SsSwapOut_Type())
ssSwapOut.setMaxAccess(_A)
if mibBuilder.loadTexts:ssSwapOut.setStatus(_B)
_SsIOSent_Type=Integer32
_SsIOSent_Object=MibScalar
ssIOSent=_SsIOSent_Object((1,3,6,1,4,1,8673,11,5),_SsIOSent_Type())
ssIOSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ssIOSent.setStatus(_C)
_SsIOReceive_Type=Integer32
_SsIOReceive_Object=MibScalar
ssIOReceive=_SsIOReceive_Object((1,3,6,1,4,1,8673,11,6),_SsIOReceive_Type())
ssIOReceive.setMaxAccess(_A)
if mibBuilder.loadTexts:ssIOReceive.setStatus(_C)
_SsSysInterrupts_Type=Integer32
_SsSysInterrupts_Object=MibScalar
ssSysInterrupts=_SsSysInterrupts_Object((1,3,6,1,4,1,8673,11,7),_SsSysInterrupts_Type())
ssSysInterrupts.setMaxAccess(_A)
if mibBuilder.loadTexts:ssSysInterrupts.setStatus(_C)
_SsSysContext_Type=Integer32
_SsSysContext_Object=MibScalar
ssSysContext=_SsSysContext_Object((1,3,6,1,4,1,8673,11,8),_SsSysContext_Type())
ssSysContext.setMaxAccess(_A)
if mibBuilder.loadTexts:ssSysContext.setStatus(_C)
_SsCpuUser_Type=Integer32
_SsCpuUser_Object=MibScalar
ssCpuUser=_SsCpuUser_Object((1,3,6,1,4,1,8673,11,9),_SsCpuUser_Type())
ssCpuUser.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuUser.setStatus(_C)
_SsCpuSystem_Type=Integer32
_SsCpuSystem_Object=MibScalar
ssCpuSystem=_SsCpuSystem_Object((1,3,6,1,4,1,8673,11,10),_SsCpuSystem_Type())
ssCpuSystem.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuSystem.setStatus(_C)
_SsCpuIdle_Type=Integer32
_SsCpuIdle_Object=MibScalar
ssCpuIdle=_SsCpuIdle_Object((1,3,6,1,4,1,8673,11,11),_SsCpuIdle_Type())
ssCpuIdle.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuIdle.setStatus(_C)
_SsCpuRawUser_Type=Counter32
_SsCpuRawUser_Object=MibScalar
ssCpuRawUser=_SsCpuRawUser_Object((1,3,6,1,4,1,8673,11,50),_SsCpuRawUser_Type())
ssCpuRawUser.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawUser.setStatus(_B)
_SsCpuRawNice_Type=Counter32
_SsCpuRawNice_Object=MibScalar
ssCpuRawNice=_SsCpuRawNice_Object((1,3,6,1,4,1,8673,11,51),_SsCpuRawNice_Type())
ssCpuRawNice.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawNice.setStatus(_B)
_SsCpuRawSystem_Type=Counter32
_SsCpuRawSystem_Object=MibScalar
ssCpuRawSystem=_SsCpuRawSystem_Object((1,3,6,1,4,1,8673,11,52),_SsCpuRawSystem_Type())
ssCpuRawSystem.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawSystem.setStatus(_B)
_SsCpuRawIdle_Type=Counter32
_SsCpuRawIdle_Object=MibScalar
ssCpuRawIdle=_SsCpuRawIdle_Object((1,3,6,1,4,1,8673,11,53),_SsCpuRawIdle_Type())
ssCpuRawIdle.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawIdle.setStatus(_B)
_SsCpuRawWait_Type=Counter32
_SsCpuRawWait_Object=MibScalar
ssCpuRawWait=_SsCpuRawWait_Object((1,3,6,1,4,1,8673,11,54),_SsCpuRawWait_Type())
ssCpuRawWait.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawWait.setStatus(_B)
_SsCpuRawKernel_Type=Counter32
_SsCpuRawKernel_Object=MibScalar
ssCpuRawKernel=_SsCpuRawKernel_Object((1,3,6,1,4,1,8673,11,55),_SsCpuRawKernel_Type())
ssCpuRawKernel.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawKernel.setStatus(_B)
_SsCpuRawInterrupt_Type=Counter32
_SsCpuRawInterrupt_Object=MibScalar
ssCpuRawInterrupt=_SsCpuRawInterrupt_Object((1,3,6,1,4,1,8673,11,56),_SsCpuRawInterrupt_Type())
ssCpuRawInterrupt.setMaxAccess(_A)
if mibBuilder.loadTexts:ssCpuRawInterrupt.setStatus(_B)
_SsIORawSent_Type=Counter32
_SsIORawSent_Object=MibScalar
ssIORawSent=_SsIORawSent_Object((1,3,6,1,4,1,8673,11,57),_SsIORawSent_Type())
ssIORawSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ssIORawSent.setStatus(_B)
_SsIORawReceived_Type=Counter32
_SsIORawReceived_Object=MibScalar
ssIORawReceived=_SsIORawReceived_Object((1,3,6,1,4,1,8673,11,58),_SsIORawReceived_Type())
ssIORawReceived.setMaxAccess(_A)
if mibBuilder.loadTexts:ssIORawReceived.setStatus(_B)
_SsRawInterrupts_Type=Counter32
_SsRawInterrupts_Object=MibScalar
ssRawInterrupts=_SsRawInterrupts_Object((1,3,6,1,4,1,8673,11,59),_SsRawInterrupts_Type())
ssRawInterrupts.setMaxAccess(_A)
if mibBuilder.loadTexts:ssRawInterrupts.setStatus(_B)
_SsRawContexts_Type=Counter32
_SsRawContexts_Object=MibScalar
ssRawContexts=_SsRawContexts_Object((1,3,6,1,4,1,8673,11,60),_SsRawContexts_Type())
ssRawContexts.setMaxAccess(_A)
if mibBuilder.loadTexts:ssRawContexts.setStatus(_B)
mibBuilder.exportSymbols(_E,**{'Float':Float,'borderware':borderware,'bwProducts':bwProducts,'bwProductId':bwProductId,'bwFirewallServer7':bwFirewallServer7,'bwSysMemory':bwSysMemory,'memIndex':memIndex,'memErrorName':memErrorName,'memTotalSwap':memTotalSwap,'memAvailSwap':memAvailSwap,'memTotalReal':memTotalReal,'memAvailReal':memAvailReal,'memTotalSwapTXT':memTotalSwapTXT,'memAvailSwapTXT':memAvailSwapTXT,'memTotalRealTXT':memTotalRealTXT,'memAvailRealTXT':memAvailRealTXT,'memTotalFree':memTotalFree,'memMinimumSwap':memMinimumSwap,'memShared':memShared,'memBuffer':memBuffer,'memCached':memCached,'memSwapError':memSwapError,'memSwapErrorMsg':memSwapErrorMsg,'dskTable':dskTable,'dskEntry':dskEntry,_F:dskIndex,'dskPath':dskPath,'dskDevice':dskDevice,'dskMinimum':dskMinimum,'dskMinPercent':dskMinPercent,'dskTotal':dskTotal,'dskAvail':dskAvail,'dskUsed':dskUsed,'dskPercent':dskPercent,'dskPercentNode':dskPercentNode,'dskErrorFlag':dskErrorFlag,'dskErrorMsg':dskErrorMsg,'systemStats':systemStats,'ssIndex':ssIndex,'ssErrorName':ssErrorName,'ssSwapIn':ssSwapIn,'ssSwapOut':ssSwapOut,'ssIOSent':ssIOSent,'ssIOReceive':ssIOReceive,'ssSysInterrupts':ssSysInterrupts,'ssSysContext':ssSysContext,'ssCpuUser':ssCpuUser,'ssCpuSystem':ssCpuSystem,'ssCpuIdle':ssCpuIdle,'ssCpuRawUser':ssCpuRawUser,'ssCpuRawNice':ssCpuRawNice,'ssCpuRawSystem':ssCpuRawSystem,'ssCpuRawIdle':ssCpuRawIdle,'ssCpuRawWait':ssCpuRawWait,'ssCpuRawKernel':ssCpuRawKernel,'ssCpuRawInterrupt':ssCpuRawInterrupt,'ssIORawSent':ssIORawSent,'ssIORawReceived':ssIORawReceived,'ssRawInterrupts':ssRawInterrupts,'ssRawContexts':ssRawContexts})