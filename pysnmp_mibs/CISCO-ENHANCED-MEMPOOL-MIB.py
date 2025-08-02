_AQ='cempMemPoolOvrflwGroup'
_AP='cempMemPoolHCGroup'
_AO='cempMemPoolExtGroup'
_AN='cempMemBufferNotify'
_AM='cempMemPoolSharedOvrflw'
_AL='cempMemPoolUsedLowWaterMarkOvrflw'
_AK='cempMemPoolLowestFreeOvrflw'
_AJ='cempMemPoolLargestFreeOvrflw'
_AI='cempMemPoolFreeOvrflw'
_AH='cempMemPoolUsedOvrflw'
_AG='cempMemPoolHCShared'
_AF='cempMemPoolHCUsedLowWaterMark'
_AE='cempMemPoolHCLowestFree'
_AD='cempMemPoolHCLargestFree'
_AC='cempMemPoolHCFree'
_AB='cempMemPoolHCUsed'
_AA='cempMemPoolShared'
_A9='cempMemPoolFreeMiss'
_A8='cempMemPoolFreeHit'
_A7='cempMemPoolAllocMiss'
_A6='cempMemPoolAllocHit'
_A5='cempMemPoolUsedLowWaterMark'
_A4='cempMemBufferNotifyEnabled'
_A3='cempMemBufferCacheThresholdCount'
_A2='cempMemBufferCacheThreshold'
_A1='cempMemBufferCacheMiss'
_A0='cempMemBufferCacheHit'
_z='cempMemBufferCacheUsed'
_y='cempMemBufferCacheTotal'
_x='cempMemBufferCacheSize'
_w='cempMemBufferNoStorage'
_v='cempMemBufferFailures'
_u='cempMemBufferGrow'
_t='cempMemBufferTrim'
_s='cempMemBufferPermChange'
_r='cempMemBufferFreeMiss'
_q='cempMemBufferFreeHit'
_p='cempMemBufferMiss'
_o='cempMemBufferHit'
_n='cempMemBufferFree'
_m='cempMemBufferTotal'
_l='cempMemBufferTransient'
_k='cempMemBufferPermanent'
_j='cempMemBufferMax'
_i='cempMemBufferMin'
_h='cempMemBufferSize'
_g='cempMemBufferDynamic'
_f='cempMemBufferMemPoolIndex'
_e='not-accessible'
_d='cempMemPoolIndex'
_c='TruthValue'
_b='cempMemPoolGroupRev1'
_a='cempMemPoolGroup'
_Z='cempMemBufferPeakTime'
_Y='cempMemBufferPeak'
_X='cempMemBufferName'
_W='cempMemPoolLowestFree'
_V='cempMemPoolLargestFree'
_U='cempMemPoolAlternate'
_T='cempMemPoolPlatformMemory'
_S='cempMemPoolFree'
_R='cempMemPoolUsed'
_Q='cempMemPoolValid'
_P='cempMemPoolName'
_O='cempMemPoolType'
_N='cempMemBufferPoolIndex'
_M='cempMemBufferNotifyGroup'
_L='cempMemBufferNotifyEnableGroup'
_K='cempMemBufferExtGroup'
_J='cempMemPoolExtGroupRev1'
_I='cempMemBufferGroup'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='deprecated'
_E='read-write'
_D='bytes'
_C='read-only'
_B='current'
_A='CISCO-ENHANCED-MEMPOOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TimeStamp',_c)
ciscoEnhancedMemPoolMIB=ModuleIdentity((1,3,6,1,4,1,9,9,221))
if mibBuilder.loadTexts:ciscoEnhancedMemPoolMIB.setRevisions(('2008-12-05 00:00','2008-05-07 00:00','2003-02-24 00:00','2001-06-05 00:00'))
class CempMemPoolIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CempMemPoolIndexOrNone(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class CempMemPoolTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('other',1),('processorMemory',2),('ioMemory',3),('pciMemory',4),('fastMemory',5),('multibusMemory',6),('interruptStackMemory',7),('processStackMemory',8),('localExceptionMemory',9),('virtualMemory',10),('reservedMemory',11),('imageMemory',12),('asicMemory',13),('posixMemory',14)))
class CempMemBufferPoolIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CempMIBNotifications_ObjectIdentity=ObjectIdentity
cempMIBNotifications=_CempMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,221,0))
_CempMIBObjects_ObjectIdentity=ObjectIdentity
cempMIBObjects=_CempMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,221,1))
_CempMemPool_ObjectIdentity=ObjectIdentity
cempMemPool=_CempMemPool_ObjectIdentity((1,3,6,1,4,1,9,9,221,1,1))
_CempMemPoolTable_Object=MibTable
cempMemPoolTable=_CempMemPoolTable_Object((1,3,6,1,4,1,9,9,221,1,1,1))
if mibBuilder.loadTexts:cempMemPoolTable.setStatus(_B)
_CempMemPoolEntry_Object=MibTableRow
cempMemPoolEntry=_CempMemPoolEntry_Object((1,3,6,1,4,1,9,9,221,1,1,1,1))
cempMemPoolEntry.setIndexNames((0,_G,_H),(0,_A,_d))
if mibBuilder.loadTexts:cempMemPoolEntry.setStatus(_B)
_CempMemPoolIndex_Type=CempMemPoolIndex
_CempMemPoolIndex_Object=MibTableColumn
cempMemPoolIndex=_CempMemPoolIndex_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,1),_CempMemPoolIndex_Type())
cempMemPoolIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:cempMemPoolIndex.setStatus(_B)
_CempMemPoolType_Type=CempMemPoolTypes
_CempMemPoolType_Object=MibTableColumn
cempMemPoolType=_CempMemPoolType_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,2),_CempMemPoolType_Type())
cempMemPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolType.setStatus(_B)
_CempMemPoolName_Type=SnmpAdminString
_CempMemPoolName_Object=MibTableColumn
cempMemPoolName=_CempMemPoolName_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,3),_CempMemPoolName_Type())
cempMemPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolName.setStatus(_B)
_CempMemPoolPlatformMemory_Type=AutonomousType
_CempMemPoolPlatformMemory_Object=MibTableColumn
cempMemPoolPlatformMemory=_CempMemPoolPlatformMemory_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,4),_CempMemPoolPlatformMemory_Type())
cempMemPoolPlatformMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolPlatformMemory.setStatus(_B)
_CempMemPoolAlternate_Type=CempMemPoolIndexOrNone
_CempMemPoolAlternate_Object=MibTableColumn
cempMemPoolAlternate=_CempMemPoolAlternate_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,5),_CempMemPoolAlternate_Type())
cempMemPoolAlternate.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolAlternate.setStatus(_B)
_CempMemPoolValid_Type=TruthValue
_CempMemPoolValid_Object=MibTableColumn
cempMemPoolValid=_CempMemPoolValid_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,6),_CempMemPoolValid_Type())
cempMemPoolValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolValid.setStatus(_B)
_CempMemPoolUsed_Type=Gauge32
_CempMemPoolUsed_Object=MibTableColumn
cempMemPoolUsed=_CempMemPoolUsed_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,7),_CempMemPoolUsed_Type())
cempMemPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolUsed.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolUsed.setUnits(_D)
_CempMemPoolFree_Type=Gauge32
_CempMemPoolFree_Object=MibTableColumn
cempMemPoolFree=_CempMemPoolFree_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,8),_CempMemPoolFree_Type())
cempMemPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolFree.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolFree.setUnits(_D)
_CempMemPoolLargestFree_Type=Gauge32
_CempMemPoolLargestFree_Object=MibTableColumn
cempMemPoolLargestFree=_CempMemPoolLargestFree_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,9),_CempMemPoolLargestFree_Type())
cempMemPoolLargestFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolLargestFree.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolLargestFree.setUnits(_D)
_CempMemPoolLowestFree_Type=Gauge32
_CempMemPoolLowestFree_Object=MibTableColumn
cempMemPoolLowestFree=_CempMemPoolLowestFree_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,10),_CempMemPoolLowestFree_Type())
cempMemPoolLowestFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolLowestFree.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolLowestFree.setUnits(_D)
_CempMemPoolUsedLowWaterMark_Type=Gauge32
_CempMemPoolUsedLowWaterMark_Object=MibTableColumn
cempMemPoolUsedLowWaterMark=_CempMemPoolUsedLowWaterMark_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,11),_CempMemPoolUsedLowWaterMark_Type())
cempMemPoolUsedLowWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolUsedLowWaterMark.setStatus(_B)
_CempMemPoolAllocHit_Type=Counter32
_CempMemPoolAllocHit_Object=MibTableColumn
cempMemPoolAllocHit=_CempMemPoolAllocHit_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,12),_CempMemPoolAllocHit_Type())
cempMemPoolAllocHit.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolAllocHit.setStatus(_B)
_CempMemPoolAllocMiss_Type=Counter32
_CempMemPoolAllocMiss_Object=MibTableColumn
cempMemPoolAllocMiss=_CempMemPoolAllocMiss_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,13),_CempMemPoolAllocMiss_Type())
cempMemPoolAllocMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolAllocMiss.setStatus(_B)
_CempMemPoolFreeHit_Type=Counter32
_CempMemPoolFreeHit_Object=MibTableColumn
cempMemPoolFreeHit=_CempMemPoolFreeHit_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,14),_CempMemPoolFreeHit_Type())
cempMemPoolFreeHit.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolFreeHit.setStatus(_B)
_CempMemPoolFreeMiss_Type=Counter32
_CempMemPoolFreeMiss_Object=MibTableColumn
cempMemPoolFreeMiss=_CempMemPoolFreeMiss_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,15),_CempMemPoolFreeMiss_Type())
cempMemPoolFreeMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolFreeMiss.setStatus(_B)
_CempMemPoolShared_Type=Gauge32
_CempMemPoolShared_Object=MibTableColumn
cempMemPoolShared=_CempMemPoolShared_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,16),_CempMemPoolShared_Type())
cempMemPoolShared.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolShared.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolShared.setUnits(_D)
_CempMemPoolUsedOvrflw_Type=Gauge32
_CempMemPoolUsedOvrflw_Object=MibTableColumn
cempMemPoolUsedOvrflw=_CempMemPoolUsedOvrflw_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,17),_CempMemPoolUsedOvrflw_Type())
cempMemPoolUsedOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolUsedOvrflw.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolUsedOvrflw.setUnits(_D)
_CempMemPoolHCUsed_Type=CounterBasedGauge64
_CempMemPoolHCUsed_Object=MibTableColumn
cempMemPoolHCUsed=_CempMemPoolHCUsed_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,18),_CempMemPoolHCUsed_Type())
cempMemPoolHCUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolHCUsed.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolHCUsed.setUnits(_D)
_CempMemPoolFreeOvrflw_Type=Gauge32
_CempMemPoolFreeOvrflw_Object=MibTableColumn
cempMemPoolFreeOvrflw=_CempMemPoolFreeOvrflw_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,19),_CempMemPoolFreeOvrflw_Type())
cempMemPoolFreeOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolFreeOvrflw.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolFreeOvrflw.setUnits(_D)
_CempMemPoolHCFree_Type=CounterBasedGauge64
_CempMemPoolHCFree_Object=MibTableColumn
cempMemPoolHCFree=_CempMemPoolHCFree_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,20),_CempMemPoolHCFree_Type())
cempMemPoolHCFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolHCFree.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolHCFree.setUnits(_D)
_CempMemPoolLargestFreeOvrflw_Type=Gauge32
_CempMemPoolLargestFreeOvrflw_Object=MibTableColumn
cempMemPoolLargestFreeOvrflw=_CempMemPoolLargestFreeOvrflw_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,21),_CempMemPoolLargestFreeOvrflw_Type())
cempMemPoolLargestFreeOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolLargestFreeOvrflw.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolLargestFreeOvrflw.setUnits(_D)
_CempMemPoolHCLargestFree_Type=CounterBasedGauge64
_CempMemPoolHCLargestFree_Object=MibTableColumn
cempMemPoolHCLargestFree=_CempMemPoolHCLargestFree_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,22),_CempMemPoolHCLargestFree_Type())
cempMemPoolHCLargestFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolHCLargestFree.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolHCLargestFree.setUnits(_D)
_CempMemPoolLowestFreeOvrflw_Type=Gauge32
_CempMemPoolLowestFreeOvrflw_Object=MibTableColumn
cempMemPoolLowestFreeOvrflw=_CempMemPoolLowestFreeOvrflw_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,23),_CempMemPoolLowestFreeOvrflw_Type())
cempMemPoolLowestFreeOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolLowestFreeOvrflw.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolLowestFreeOvrflw.setUnits(_D)
_CempMemPoolHCLowestFree_Type=CounterBasedGauge64
_CempMemPoolHCLowestFree_Object=MibTableColumn
cempMemPoolHCLowestFree=_CempMemPoolHCLowestFree_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,24),_CempMemPoolHCLowestFree_Type())
cempMemPoolHCLowestFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolHCLowestFree.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolHCLowestFree.setUnits(_D)
_CempMemPoolUsedLowWaterMarkOvrflw_Type=Gauge32
_CempMemPoolUsedLowWaterMarkOvrflw_Object=MibTableColumn
cempMemPoolUsedLowWaterMarkOvrflw=_CempMemPoolUsedLowWaterMarkOvrflw_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,25),_CempMemPoolUsedLowWaterMarkOvrflw_Type())
cempMemPoolUsedLowWaterMarkOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolUsedLowWaterMarkOvrflw.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolUsedLowWaterMarkOvrflw.setUnits(_D)
_CempMemPoolHCUsedLowWaterMark_Type=CounterBasedGauge64
_CempMemPoolHCUsedLowWaterMark_Object=MibTableColumn
cempMemPoolHCUsedLowWaterMark=_CempMemPoolHCUsedLowWaterMark_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,26),_CempMemPoolHCUsedLowWaterMark_Type())
cempMemPoolHCUsedLowWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolHCUsedLowWaterMark.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolHCUsedLowWaterMark.setUnits(_D)
_CempMemPoolSharedOvrflw_Type=Gauge32
_CempMemPoolSharedOvrflw_Object=MibTableColumn
cempMemPoolSharedOvrflw=_CempMemPoolSharedOvrflw_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,27),_CempMemPoolSharedOvrflw_Type())
cempMemPoolSharedOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolSharedOvrflw.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolSharedOvrflw.setUnits(_D)
_CempMemPoolHCShared_Type=CounterBasedGauge64
_CempMemPoolHCShared_Object=MibTableColumn
cempMemPoolHCShared=_CempMemPoolHCShared_Object((1,3,6,1,4,1,9,9,221,1,1,1,1,28),_CempMemPoolHCShared_Type())
cempMemPoolHCShared.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemPoolHCShared.setStatus(_B)
if mibBuilder.loadTexts:cempMemPoolHCShared.setUnits(_D)
_CempMemBufferPoolTable_Object=MibTable
cempMemBufferPoolTable=_CempMemBufferPoolTable_Object((1,3,6,1,4,1,9,9,221,1,1,2))
if mibBuilder.loadTexts:cempMemBufferPoolTable.setStatus(_B)
_CempMemBufferPoolEntry_Object=MibTableRow
cempMemBufferPoolEntry=_CempMemBufferPoolEntry_Object((1,3,6,1,4,1,9,9,221,1,1,2,1))
cempMemBufferPoolEntry.setIndexNames((0,_G,_H),(0,_A,_N))
if mibBuilder.loadTexts:cempMemBufferPoolEntry.setStatus(_B)
_CempMemBufferPoolIndex_Type=CempMemBufferPoolIndex
_CempMemBufferPoolIndex_Object=MibTableColumn
cempMemBufferPoolIndex=_CempMemBufferPoolIndex_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,1),_CempMemBufferPoolIndex_Type())
cempMemBufferPoolIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:cempMemBufferPoolIndex.setStatus(_B)
_CempMemBufferMemPoolIndex_Type=CempMemPoolIndex
_CempMemBufferMemPoolIndex_Object=MibTableColumn
cempMemBufferMemPoolIndex=_CempMemBufferMemPoolIndex_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,2),_CempMemBufferMemPoolIndex_Type())
cempMemBufferMemPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferMemPoolIndex.setStatus(_B)
_CempMemBufferName_Type=SnmpAdminString
_CempMemBufferName_Object=MibTableColumn
cempMemBufferName=_CempMemBufferName_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,3),_CempMemBufferName_Type())
cempMemBufferName.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferName.setStatus(_B)
_CempMemBufferDynamic_Type=TruthValue
_CempMemBufferDynamic_Object=MibTableColumn
cempMemBufferDynamic=_CempMemBufferDynamic_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,4),_CempMemBufferDynamic_Type())
cempMemBufferDynamic.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferDynamic.setStatus(_B)
_CempMemBufferSize_Type=Unsigned32
_CempMemBufferSize_Object=MibTableColumn
cempMemBufferSize=_CempMemBufferSize_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,5),_CempMemBufferSize_Type())
cempMemBufferSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cempMemBufferSize.setStatus(_B)
if mibBuilder.loadTexts:cempMemBufferSize.setUnits(_D)
_CempMemBufferMin_Type=Unsigned32
_CempMemBufferMin_Object=MibTableColumn
cempMemBufferMin=_CempMemBufferMin_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,6),_CempMemBufferMin_Type())
cempMemBufferMin.setMaxAccess(_E)
if mibBuilder.loadTexts:cempMemBufferMin.setStatus(_B)
_CempMemBufferMax_Type=Unsigned32
_CempMemBufferMax_Object=MibTableColumn
cempMemBufferMax=_CempMemBufferMax_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,7),_CempMemBufferMax_Type())
cempMemBufferMax.setMaxAccess(_E)
if mibBuilder.loadTexts:cempMemBufferMax.setStatus(_B)
_CempMemBufferPermanent_Type=Unsigned32
_CempMemBufferPermanent_Object=MibTableColumn
cempMemBufferPermanent=_CempMemBufferPermanent_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,8),_CempMemBufferPermanent_Type())
cempMemBufferPermanent.setMaxAccess(_E)
if mibBuilder.loadTexts:cempMemBufferPermanent.setStatus(_B)
_CempMemBufferTransient_Type=Unsigned32
_CempMemBufferTransient_Object=MibTableColumn
cempMemBufferTransient=_CempMemBufferTransient_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,9),_CempMemBufferTransient_Type())
cempMemBufferTransient.setMaxAccess(_E)
if mibBuilder.loadTexts:cempMemBufferTransient.setStatus(_B)
_CempMemBufferTotal_Type=Gauge32
_CempMemBufferTotal_Object=MibTableColumn
cempMemBufferTotal=_CempMemBufferTotal_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,10),_CempMemBufferTotal_Type())
cempMemBufferTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferTotal.setStatus(_B)
_CempMemBufferFree_Type=Gauge32
_CempMemBufferFree_Object=MibTableColumn
cempMemBufferFree=_CempMemBufferFree_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,11),_CempMemBufferFree_Type())
cempMemBufferFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferFree.setStatus(_B)
_CempMemBufferHit_Type=Counter32
_CempMemBufferHit_Object=MibTableColumn
cempMemBufferHit=_CempMemBufferHit_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,12),_CempMemBufferHit_Type())
cempMemBufferHit.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferHit.setStatus(_B)
_CempMemBufferMiss_Type=Counter32
_CempMemBufferMiss_Object=MibTableColumn
cempMemBufferMiss=_CempMemBufferMiss_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,13),_CempMemBufferMiss_Type())
cempMemBufferMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferMiss.setStatus(_B)
_CempMemBufferFreeHit_Type=Counter32
_CempMemBufferFreeHit_Object=MibTableColumn
cempMemBufferFreeHit=_CempMemBufferFreeHit_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,14),_CempMemBufferFreeHit_Type())
cempMemBufferFreeHit.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferFreeHit.setStatus(_B)
_CempMemBufferFreeMiss_Type=Counter32
_CempMemBufferFreeMiss_Object=MibTableColumn
cempMemBufferFreeMiss=_CempMemBufferFreeMiss_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,15),_CempMemBufferFreeMiss_Type())
cempMemBufferFreeMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferFreeMiss.setStatus(_B)
_CempMemBufferPermChange_Type=Integer32
_CempMemBufferPermChange_Object=MibTableColumn
cempMemBufferPermChange=_CempMemBufferPermChange_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,16),_CempMemBufferPermChange_Type())
cempMemBufferPermChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferPermChange.setStatus(_B)
_CempMemBufferPeak_Type=Counter32
_CempMemBufferPeak_Object=MibTableColumn
cempMemBufferPeak=_CempMemBufferPeak_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,17),_CempMemBufferPeak_Type())
cempMemBufferPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferPeak.setStatus(_B)
_CempMemBufferPeakTime_Type=TimeStamp
_CempMemBufferPeakTime_Object=MibTableColumn
cempMemBufferPeakTime=_CempMemBufferPeakTime_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,18),_CempMemBufferPeakTime_Type())
cempMemBufferPeakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferPeakTime.setStatus(_B)
_CempMemBufferTrim_Type=Counter32
_CempMemBufferTrim_Object=MibTableColumn
cempMemBufferTrim=_CempMemBufferTrim_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,19),_CempMemBufferTrim_Type())
cempMemBufferTrim.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferTrim.setStatus(_B)
_CempMemBufferGrow_Type=Counter32
_CempMemBufferGrow_Object=MibTableColumn
cempMemBufferGrow=_CempMemBufferGrow_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,20),_CempMemBufferGrow_Type())
cempMemBufferGrow.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferGrow.setStatus(_B)
_CempMemBufferFailures_Type=Counter32
_CempMemBufferFailures_Object=MibTableColumn
cempMemBufferFailures=_CempMemBufferFailures_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,21),_CempMemBufferFailures_Type())
cempMemBufferFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferFailures.setStatus(_B)
_CempMemBufferNoStorage_Type=Counter32
_CempMemBufferNoStorage_Object=MibTableColumn
cempMemBufferNoStorage=_CempMemBufferNoStorage_Object((1,3,6,1,4,1,9,9,221,1,1,2,1,22),_CempMemBufferNoStorage_Type())
cempMemBufferNoStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferNoStorage.setStatus(_B)
_CempMemBufferCachePoolTable_Object=MibTable
cempMemBufferCachePoolTable=_CempMemBufferCachePoolTable_Object((1,3,6,1,4,1,9,9,221,1,1,3))
if mibBuilder.loadTexts:cempMemBufferCachePoolTable.setStatus(_B)
_CempMemBufferCachePoolEntry_Object=MibTableRow
cempMemBufferCachePoolEntry=_CempMemBufferCachePoolEntry_Object((1,3,6,1,4,1,9,9,221,1,1,3,1))
cempMemBufferCachePoolEntry.setIndexNames((0,_G,_H),(0,_A,_N))
if mibBuilder.loadTexts:cempMemBufferCachePoolEntry.setStatus(_B)
_CempMemBufferCacheSize_Type=Unsigned32
_CempMemBufferCacheSize_Object=MibTableColumn
cempMemBufferCacheSize=_CempMemBufferCacheSize_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,1),_CempMemBufferCacheSize_Type())
cempMemBufferCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheSize.setStatus(_B)
_CempMemBufferCacheTotal_Type=Gauge32
_CempMemBufferCacheTotal_Object=MibTableColumn
cempMemBufferCacheTotal=_CempMemBufferCacheTotal_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,2),_CempMemBufferCacheTotal_Type())
cempMemBufferCacheTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheTotal.setStatus(_B)
_CempMemBufferCacheUsed_Type=Gauge32
_CempMemBufferCacheUsed_Object=MibTableColumn
cempMemBufferCacheUsed=_CempMemBufferCacheUsed_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,3),_CempMemBufferCacheUsed_Type())
cempMemBufferCacheUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheUsed.setStatus(_B)
_CempMemBufferCacheHit_Type=Counter32
_CempMemBufferCacheHit_Object=MibTableColumn
cempMemBufferCacheHit=_CempMemBufferCacheHit_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,4),_CempMemBufferCacheHit_Type())
cempMemBufferCacheHit.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheHit.setStatus(_B)
_CempMemBufferCacheMiss_Type=Counter32
_CempMemBufferCacheMiss_Object=MibTableColumn
cempMemBufferCacheMiss=_CempMemBufferCacheMiss_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,5),_CempMemBufferCacheMiss_Type())
cempMemBufferCacheMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheMiss.setStatus(_B)
_CempMemBufferCacheThreshold_Type=Gauge32
_CempMemBufferCacheThreshold_Object=MibTableColumn
cempMemBufferCacheThreshold=_CempMemBufferCacheThreshold_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,6),_CempMemBufferCacheThreshold_Type())
cempMemBufferCacheThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheThreshold.setStatus(_B)
_CempMemBufferCacheThresholdCount_Type=Counter32
_CempMemBufferCacheThresholdCount_Object=MibTableColumn
cempMemBufferCacheThresholdCount=_CempMemBufferCacheThresholdCount_Object((1,3,6,1,4,1,9,9,221,1,1,3,1,7),_CempMemBufferCacheThresholdCount_Type())
cempMemBufferCacheThresholdCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cempMemBufferCacheThresholdCount.setStatus(_B)
_CempNotificationConfig_ObjectIdentity=ObjectIdentity
cempNotificationConfig=_CempNotificationConfig_ObjectIdentity((1,3,6,1,4,1,9,9,221,1,2))
class _CempMemBufferNotifyEnabled_Type(TruthValue):defaultValue=2
_CempMemBufferNotifyEnabled_Type.__name__=_c
_CempMemBufferNotifyEnabled_Object=MibScalar
cempMemBufferNotifyEnabled=_CempMemBufferNotifyEnabled_Object((1,3,6,1,4,1,9,9,221,1,2,1),_CempMemBufferNotifyEnabled_Type())
cempMemBufferNotifyEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cempMemBufferNotifyEnabled.setStatus(_B)
_CempMIBConformance_ObjectIdentity=ObjectIdentity
cempMIBConformance=_CempMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,221,3))
_CempMIBCompliances_ObjectIdentity=ObjectIdentity
cempMIBCompliances=_CempMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,221,3,1))
_CempMIBGroups_ObjectIdentity=ObjectIdentity
cempMIBGroups=_CempMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,221,3,2))
cempMemPoolGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,1))
cempMemPoolGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cempMemPoolGroup.setStatus(_F)
cempMemPoolExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,2))
cempMemPoolExtGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cempMemPoolExtGroup.setStatus(_F)
cempMemBufferGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,3))
cempMemBufferGroup.setObjects(*((_A,_f),(_A,_X),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_Y),(_A,_Z),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cempMemBufferGroup.setStatus(_B)
cempMemBufferExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,4))
cempMemBufferExtGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:cempMemBufferExtGroup.setStatus(_B)
cempMemBufferNotifyEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,5))
cempMemBufferNotifyEnableGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:cempMemBufferNotifyEnableGroup.setStatus(_B)
cempMemPoolExtGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,7))
cempMemPoolExtGroupRev1.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cempMemPoolExtGroupRev1.setStatus(_B)
cempMemPoolGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,8))
cempMemPoolGroupRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_AA)))
if mibBuilder.loadTexts:cempMemPoolGroupRev1.setStatus(_B)
cempMemPoolHCGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,9))
cempMemPoolHCGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:cempMemPoolHCGroup.setStatus(_B)
cempMemPoolOvrflwGroup=ObjectGroup((1,3,6,1,4,1,9,9,221,3,2,10))
cempMemPoolOvrflwGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:cempMemPoolOvrflwGroup.setStatus(_B)
cempMemBufferNotify=NotificationType((1,3,6,1,4,1,9,9,221,0,1))
cempMemBufferNotify.setObjects(*((_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cempMemBufferNotify.setStatus(_B)
cempMemBufferNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,221,3,2,6))
cempMemBufferNotifyGroup.setObjects((_A,_AN))
if mibBuilder.loadTexts:cempMemBufferNotifyGroup.setStatus(_B)
cempMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,221,3,1,1))
cempMIBCompliance.setObjects(*((_A,_a),(_A,_AO)))
if mibBuilder.loadTexts:cempMIBCompliance.setStatus(_F)
cempMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,221,3,1,2))
cempMIBComplianceRev1.setObjects(*((_A,_a),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cempMIBComplianceRev1.setStatus(_F)
cempMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,221,3,1,3))
cempMIBComplianceRev2.setObjects(*((_A,_b),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cempMIBComplianceRev2.setStatus(_F)
cempMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,221,3,1,4))
cempMIBComplianceRev3.setObjects(*((_A,_b),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:cempMIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CempMemPoolIndex':CempMemPoolIndex,'CempMemPoolIndexOrNone':CempMemPoolIndexOrNone,'CempMemPoolTypes':CempMemPoolTypes,'CempMemBufferPoolIndex':CempMemBufferPoolIndex,'ciscoEnhancedMemPoolMIB':ciscoEnhancedMemPoolMIB,'cempMIBNotifications':cempMIBNotifications,_AN:cempMemBufferNotify,'cempMIBObjects':cempMIBObjects,'cempMemPool':cempMemPool,'cempMemPoolTable':cempMemPoolTable,'cempMemPoolEntry':cempMemPoolEntry,_d:cempMemPoolIndex,_O:cempMemPoolType,_P:cempMemPoolName,_T:cempMemPoolPlatformMemory,_U:cempMemPoolAlternate,_Q:cempMemPoolValid,_R:cempMemPoolUsed,_S:cempMemPoolFree,_V:cempMemPoolLargestFree,_W:cempMemPoolLowestFree,_A5:cempMemPoolUsedLowWaterMark,_A6:cempMemPoolAllocHit,_A7:cempMemPoolAllocMiss,_A8:cempMemPoolFreeHit,_A9:cempMemPoolFreeMiss,_AA:cempMemPoolShared,_AH:cempMemPoolUsedOvrflw,_AB:cempMemPoolHCUsed,_AI:cempMemPoolFreeOvrflw,_AC:cempMemPoolHCFree,_AJ:cempMemPoolLargestFreeOvrflw,_AD:cempMemPoolHCLargestFree,_AK:cempMemPoolLowestFreeOvrflw,_AE:cempMemPoolHCLowestFree,_AL:cempMemPoolUsedLowWaterMarkOvrflw,_AF:cempMemPoolHCUsedLowWaterMark,_AM:cempMemPoolSharedOvrflw,_AG:cempMemPoolHCShared,'cempMemBufferPoolTable':cempMemBufferPoolTable,'cempMemBufferPoolEntry':cempMemBufferPoolEntry,_N:cempMemBufferPoolIndex,_f:cempMemBufferMemPoolIndex,_X:cempMemBufferName,_g:cempMemBufferDynamic,_h:cempMemBufferSize,_i:cempMemBufferMin,_j:cempMemBufferMax,_k:cempMemBufferPermanent,_l:cempMemBufferTransient,_m:cempMemBufferTotal,_n:cempMemBufferFree,_o:cempMemBufferHit,_p:cempMemBufferMiss,_q:cempMemBufferFreeHit,_r:cempMemBufferFreeMiss,_s:cempMemBufferPermChange,_Y:cempMemBufferPeak,_Z:cempMemBufferPeakTime,_t:cempMemBufferTrim,_u:cempMemBufferGrow,_v:cempMemBufferFailures,_w:cempMemBufferNoStorage,'cempMemBufferCachePoolTable':cempMemBufferCachePoolTable,'cempMemBufferCachePoolEntry':cempMemBufferCachePoolEntry,_x:cempMemBufferCacheSize,_y:cempMemBufferCacheTotal,_z:cempMemBufferCacheUsed,_A0:cempMemBufferCacheHit,_A1:cempMemBufferCacheMiss,_A2:cempMemBufferCacheThreshold,_A3:cempMemBufferCacheThresholdCount,'cempNotificationConfig':cempNotificationConfig,_A4:cempMemBufferNotifyEnabled,'cempMIBConformance':cempMIBConformance,'cempMIBCompliances':cempMIBCompliances,'cempMIBCompliance':cempMIBCompliance,'cempMIBComplianceRev1':cempMIBComplianceRev1,'cempMIBComplianceRev2':cempMIBComplianceRev2,'cempMIBComplianceRev3':cempMIBComplianceRev3,'cempMIBGroups':cempMIBGroups,_a:cempMemPoolGroup,_AO:cempMemPoolExtGroup,_I:cempMemBufferGroup,_K:cempMemBufferExtGroup,_L:cempMemBufferNotifyEnableGroup,_M:cempMemBufferNotifyGroup,_J:cempMemPoolExtGroupRev1,_b:cempMemPoolGroupRev1,_AP:cempMemPoolHCGroup,_AQ:cempMemPoolOvrflwGroup})