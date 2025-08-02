_A0='healthTrapsGroup'
_z='healthThreshGroup'
_y='healthControlGroup'
_x='healthPortGroup'
_w='healthModuleGroup'
_v='healthMonCmmTrap'
_u='healthMonPortTrap'
_t='healthMonModuleTrap'
_s='healthThreshFlashLimit'
_r='healthThreshCpuLimit'
_q='healthThreshMemoryLimit'
_p='healthThreshRxTxLimit'
_o='healthThreshRxLimit'
_n='healthSamplingInterval'
_m='healthPortRxTx1DayAvg'
_l='healthPortRxTx1HrAvg'
_k='healthPortRxTx1MinAvg'
_j='healthPortRx1DayAvg'
_i='healthPortRx1HrAvg'
_h='healthPortRx1MinAvg'
_g='healthModuleRxTxLatest'
_f='healthModuleRxLatest'
_e='healthModuleMemoryLatest'
_d='healthModuleCpu1DayAvg'
_c='healthModuleCpu1HrAvg'
_b='healthModuleCpu1MinAvg'
_a='healthModuleMemory1DayAvg'
_Z='healthModuleMemory1HrAvg'
_Y='healthModuleMemory1MinAvg'
_X='healthModuleRxTx1DayAvg'
_W='healthModuleRxTx1HrAvg'
_V='healthModuleRxTx1MinAvg'
_U='healthModuleRx1DayAvg'
_T='healthModuleRx1HrAvg'
_S='healthModuleRx1MinAvg'
_R='not-accessible'
_Q='healthMonFlashStatus'
_P='healthModuleCpuLatest'
_O='healthPortIfIndex'
_N='healthMonCpuStatus'
_M='healthMonMemoryStatus'
_L='healthMonRxTxStatus'
_K='healthMonRxStatus'
_J='healthModuleChassisId'
_I='healthModuleSlot'
_H='crossedAboveThreshold'
_G='noChange'
_F='crossedBelowThreshold'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='current'
_A='ALCATEL-ENT1-HEALTH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Health,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Health')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1HealthMonitorMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIB.setRevisions(('2010-05-13 00:00','2007-04-03 00:00'))
_AlcatelIND1HealthMonitorMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1HealthMonitorMIBNotifications=_AlcatelIND1HealthMonitorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,0))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIBNotifications.setStatus(_B)
_AlcatelIND1HealthMonitorMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1HealthMonitorMIBObjects=_AlcatelIND1HealthMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,1))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIBObjects.setStatus(_B)
_HealthModuleInfo_ObjectIdentity=ObjectIdentity
healthModuleInfo=_HealthModuleInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1))
_HealthModuleTable_Object=MibTable
healthModuleTable=_HealthModuleTable_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1))
if mibBuilder.loadTexts:healthModuleTable.setStatus(_B)
_HealthModuleEntry_Object=MibTableRow
healthModuleEntry=_HealthModuleEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1))
healthModuleEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:healthModuleEntry.setStatus(_B)
class _HealthModuleSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7016))
_HealthModuleSlot_Type.__name__=_C
_HealthModuleSlot_Object=MibTableColumn
healthModuleSlot=_HealthModuleSlot_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,1),_HealthModuleSlot_Type())
healthModuleSlot.setMaxAccess(_R)
if mibBuilder.loadTexts:healthModuleSlot.setStatus(_B)
class _HealthModuleRx1MinAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRx1MinAvg_Type.__name__=_C
_HealthModuleRx1MinAvg_Object=MibTableColumn
healthModuleRx1MinAvg=_HealthModuleRx1MinAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,2),_HealthModuleRx1MinAvg_Type())
healthModuleRx1MinAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRx1MinAvg.setStatus(_B)
class _HealthModuleRx1HrAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRx1HrAvg_Type.__name__=_C
_HealthModuleRx1HrAvg_Object=MibTableColumn
healthModuleRx1HrAvg=_HealthModuleRx1HrAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,3),_HealthModuleRx1HrAvg_Type())
healthModuleRx1HrAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRx1HrAvg.setStatus(_B)
class _HealthModuleRx1DayAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRx1DayAvg_Type.__name__=_C
_HealthModuleRx1DayAvg_Object=MibTableColumn
healthModuleRx1DayAvg=_HealthModuleRx1DayAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,4),_HealthModuleRx1DayAvg_Type())
healthModuleRx1DayAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRx1DayAvg.setStatus(_B)
class _HealthModuleRxTx1MinAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRxTx1MinAvg_Type.__name__=_C
_HealthModuleRxTx1MinAvg_Object=MibTableColumn
healthModuleRxTx1MinAvg=_HealthModuleRxTx1MinAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,5),_HealthModuleRxTx1MinAvg_Type())
healthModuleRxTx1MinAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRxTx1MinAvg.setStatus(_B)
class _HealthModuleRxTx1HrAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRxTx1HrAvg_Type.__name__=_C
_HealthModuleRxTx1HrAvg_Object=MibTableColumn
healthModuleRxTx1HrAvg=_HealthModuleRxTx1HrAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,6),_HealthModuleRxTx1HrAvg_Type())
healthModuleRxTx1HrAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRxTx1HrAvg.setStatus(_B)
class _HealthModuleRxTx1DayAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRxTx1DayAvg_Type.__name__=_C
_HealthModuleRxTx1DayAvg_Object=MibTableColumn
healthModuleRxTx1DayAvg=_HealthModuleRxTx1DayAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,7),_HealthModuleRxTx1DayAvg_Type())
healthModuleRxTx1DayAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRxTx1DayAvg.setStatus(_B)
class _HealthModuleMemory1MinAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleMemory1MinAvg_Type.__name__=_C
_HealthModuleMemory1MinAvg_Object=MibTableColumn
healthModuleMemory1MinAvg=_HealthModuleMemory1MinAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,8),_HealthModuleMemory1MinAvg_Type())
healthModuleMemory1MinAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleMemory1MinAvg.setStatus(_B)
class _HealthModuleMemory1HrAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleMemory1HrAvg_Type.__name__=_C
_HealthModuleMemory1HrAvg_Object=MibTableColumn
healthModuleMemory1HrAvg=_HealthModuleMemory1HrAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,9),_HealthModuleMemory1HrAvg_Type())
healthModuleMemory1HrAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleMemory1HrAvg.setStatus(_B)
class _HealthModuleMemory1DayAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleMemory1DayAvg_Type.__name__=_C
_HealthModuleMemory1DayAvg_Object=MibTableColumn
healthModuleMemory1DayAvg=_HealthModuleMemory1DayAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,10),_HealthModuleMemory1DayAvg_Type())
healthModuleMemory1DayAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleMemory1DayAvg.setStatus(_B)
class _HealthModuleCpu1MinAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleCpu1MinAvg_Type.__name__=_C
_HealthModuleCpu1MinAvg_Object=MibTableColumn
healthModuleCpu1MinAvg=_HealthModuleCpu1MinAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,11),_HealthModuleCpu1MinAvg_Type())
healthModuleCpu1MinAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleCpu1MinAvg.setStatus(_B)
class _HealthModuleCpu1HrAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleCpu1HrAvg_Type.__name__=_C
_HealthModuleCpu1HrAvg_Object=MibTableColumn
healthModuleCpu1HrAvg=_HealthModuleCpu1HrAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,12),_HealthModuleCpu1HrAvg_Type())
healthModuleCpu1HrAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleCpu1HrAvg.setStatus(_B)
class _HealthModuleCpu1DayAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleCpu1DayAvg_Type.__name__=_C
_HealthModuleCpu1DayAvg_Object=MibTableColumn
healthModuleCpu1DayAvg=_HealthModuleCpu1DayAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,13),_HealthModuleCpu1DayAvg_Type())
healthModuleCpu1DayAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleCpu1DayAvg.setStatus(_B)
class _HealthModuleChassisId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_HealthModuleChassisId_Type.__name__=_C
_HealthModuleChassisId_Object=MibTableColumn
healthModuleChassisId=_HealthModuleChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,14),_HealthModuleChassisId_Type())
healthModuleChassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleChassisId.setStatus(_B)
class _HealthModuleCpuLatest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleCpuLatest_Type.__name__=_C
_HealthModuleCpuLatest_Object=MibTableColumn
healthModuleCpuLatest=_HealthModuleCpuLatest_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,15),_HealthModuleCpuLatest_Type())
healthModuleCpuLatest.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleCpuLatest.setStatus(_B)
class _HealthModuleMemoryLatest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleMemoryLatest_Type.__name__=_C
_HealthModuleMemoryLatest_Object=MibTableColumn
healthModuleMemoryLatest=_HealthModuleMemoryLatest_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,16),_HealthModuleMemoryLatest_Type())
healthModuleMemoryLatest.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleMemoryLatest.setStatus(_B)
class _HealthModuleRxLatest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRxLatest_Type.__name__=_C
_HealthModuleRxLatest_Object=MibTableColumn
healthModuleRxLatest=_HealthModuleRxLatest_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,17),_HealthModuleRxLatest_Type())
healthModuleRxLatest.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRxLatest.setStatus(_B)
class _HealthModuleRxTxLatest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthModuleRxTxLatest_Type.__name__=_C
_HealthModuleRxTxLatest_Object=MibTableColumn
healthModuleRxTxLatest=_HealthModuleRxTxLatest_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,1,1,1,18),_HealthModuleRxTxLatest_Type())
healthModuleRxTxLatest.setMaxAccess(_D)
if mibBuilder.loadTexts:healthModuleRxTxLatest.setStatus(_B)
_HealthPortInfo_ObjectIdentity=ObjectIdentity
healthPortInfo=_HealthPortInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2))
_HealthPortTable_Object=MibTable
healthPortTable=_HealthPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1))
if mibBuilder.loadTexts:healthPortTable.setStatus(_B)
_HealthPortEntry_Object=MibTableRow
healthPortEntry=_HealthPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1))
healthPortEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:healthPortEntry.setStatus(_B)
class _HealthPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HealthPortIfIndex_Type.__name__=_C
_HealthPortIfIndex_Object=MibTableColumn
healthPortIfIndex=_HealthPortIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,1),_HealthPortIfIndex_Type())
healthPortIfIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:healthPortIfIndex.setStatus(_B)
class _HealthPortRx1MinAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthPortRx1MinAvg_Type.__name__=_C
_HealthPortRx1MinAvg_Object=MibTableColumn
healthPortRx1MinAvg=_HealthPortRx1MinAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,2),_HealthPortRx1MinAvg_Type())
healthPortRx1MinAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthPortRx1MinAvg.setStatus(_B)
class _HealthPortRx1HrAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthPortRx1HrAvg_Type.__name__=_C
_HealthPortRx1HrAvg_Object=MibTableColumn
healthPortRx1HrAvg=_HealthPortRx1HrAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,3),_HealthPortRx1HrAvg_Type())
healthPortRx1HrAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthPortRx1HrAvg.setStatus(_B)
class _HealthPortRx1DayAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthPortRx1DayAvg_Type.__name__=_C
_HealthPortRx1DayAvg_Object=MibTableColumn
healthPortRx1DayAvg=_HealthPortRx1DayAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,4),_HealthPortRx1DayAvg_Type())
healthPortRx1DayAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthPortRx1DayAvg.setStatus(_B)
class _HealthPortRxTx1MinAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthPortRxTx1MinAvg_Type.__name__=_C
_HealthPortRxTx1MinAvg_Object=MibTableColumn
healthPortRxTx1MinAvg=_HealthPortRxTx1MinAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,5),_HealthPortRxTx1MinAvg_Type())
healthPortRxTx1MinAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthPortRxTx1MinAvg.setStatus(_B)
class _HealthPortRxTx1HrAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthPortRxTx1HrAvg_Type.__name__=_C
_HealthPortRxTx1HrAvg_Object=MibTableColumn
healthPortRxTx1HrAvg=_HealthPortRxTx1HrAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,6),_HealthPortRxTx1HrAvg_Type())
healthPortRxTx1HrAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthPortRxTx1HrAvg.setStatus(_B)
class _HealthPortRxTx1DayAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthPortRxTx1DayAvg_Type.__name__=_C
_HealthPortRxTx1DayAvg_Object=MibTableColumn
healthPortRxTx1DayAvg=_HealthPortRxTx1DayAvg_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,2,1,1,7),_HealthPortRxTx1DayAvg_Type())
healthPortRxTx1DayAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:healthPortRxTx1DayAvg.setStatus(_B)
_HealthControlInfo_ObjectIdentity=ObjectIdentity
healthControlInfo=_HealthControlInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,3))
class _HealthSamplingInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_HealthSamplingInterval_Type.__name__=_C
_HealthSamplingInterval_Object=MibScalar
healthSamplingInterval=_HealthSamplingInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,3,1),_HealthSamplingInterval_Type())
healthSamplingInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:healthSamplingInterval.setStatus(_B)
_HealthThreshInfo_ObjectIdentity=ObjectIdentity
healthThreshInfo=_HealthThreshInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,4))
class _HealthThreshRxLimit_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthThreshRxLimit_Type.__name__=_C
_HealthThreshRxLimit_Object=MibScalar
healthThreshRxLimit=_HealthThreshRxLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,4,1),_HealthThreshRxLimit_Type())
healthThreshRxLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:healthThreshRxLimit.setStatus(_B)
class _HealthThreshRxTxLimit_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthThreshRxTxLimit_Type.__name__=_C
_HealthThreshRxTxLimit_Object=MibScalar
healthThreshRxTxLimit=_HealthThreshRxTxLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,4,2),_HealthThreshRxTxLimit_Type())
healthThreshRxTxLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:healthThreshRxTxLimit.setStatus(_B)
class _HealthThreshMemoryLimit_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthThreshMemoryLimit_Type.__name__=_C
_HealthThreshMemoryLimit_Object=MibScalar
healthThreshMemoryLimit=_HealthThreshMemoryLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,4,3),_HealthThreshMemoryLimit_Type())
healthThreshMemoryLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:healthThreshMemoryLimit.setStatus(_B)
class _HealthThreshCpuLimit_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthThreshCpuLimit_Type.__name__=_C
_HealthThreshCpuLimit_Object=MibScalar
healthThreshCpuLimit=_HealthThreshCpuLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,4,4),_HealthThreshCpuLimit_Type())
healthThreshCpuLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:healthThreshCpuLimit.setStatus(_B)
class _HealthThreshFlashLimit_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HealthThreshFlashLimit_Type.__name__=_C
_HealthThreshFlashLimit_Object=MibScalar
healthThreshFlashLimit=_HealthThreshFlashLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,4,5),_HealthThreshFlashLimit_Type())
healthThreshFlashLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:healthThreshFlashLimit.setStatus(_B)
_HealthTrapInfo_ObjectIdentity=ObjectIdentity
healthTrapInfo=_HealthTrapInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,5))
class _HealthMonRxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_HealthMonRxStatus_Type.__name__=_C
_HealthMonRxStatus_Object=MibScalar
healthMonRxStatus=_HealthMonRxStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,5,1),_HealthMonRxStatus_Type())
healthMonRxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:healthMonRxStatus.setStatus(_B)
class _HealthMonRxTxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_HealthMonRxTxStatus_Type.__name__=_C
_HealthMonRxTxStatus_Object=MibScalar
healthMonRxTxStatus=_HealthMonRxTxStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,5,2),_HealthMonRxTxStatus_Type())
healthMonRxTxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:healthMonRxTxStatus.setStatus(_B)
class _HealthMonMemoryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_HealthMonMemoryStatus_Type.__name__=_C
_HealthMonMemoryStatus_Object=MibScalar
healthMonMemoryStatus=_HealthMonMemoryStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,5,3),_HealthMonMemoryStatus_Type())
healthMonMemoryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:healthMonMemoryStatus.setStatus(_B)
class _HealthMonCpuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_HealthMonCpuStatus_Type.__name__=_C
_HealthMonCpuStatus_Object=MibScalar
healthMonCpuStatus=_HealthMonCpuStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,5,4),_HealthMonCpuStatus_Type())
healthMonCpuStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:healthMonCpuStatus.setStatus(_B)
class _HealthMonFlashStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_HealthMonFlashStatus_Type.__name__=_C
_HealthMonFlashStatus_Object=MibScalar
healthMonFlashStatus=_HealthMonFlashStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,16,1,1,5,5),_HealthMonFlashStatus_Type())
healthMonFlashStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:healthMonFlashStatus.setStatus(_B)
_AlcatelIND1HealthMonitorMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1HealthMonitorMIBConformance=_AlcatelIND1HealthMonitorMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,2))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIBConformance.setStatus(_B)
_AlcatelIND1HealthMonitorMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1HealthMonitorMIBGroups=_AlcatelIND1HealthMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIBGroups.setStatus(_B)
_AlcatelIND1HealthMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1HealthMonitorMIBCompliances=_AlcatelIND1HealthMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,2))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIBCompliances.setStatus(_B)
healthModuleGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1,1))
healthModuleGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_J),(_A,_P),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:healthModuleGroup.setStatus(_B)
healthPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1,2))
healthPortGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:healthPortGroup.setStatus(_B)
healthControlGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1,3))
healthControlGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:healthControlGroup.setStatus(_B)
healthThreshGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1,4))
healthThreshGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:healthThreshGroup.setStatus(_B)
healthTrapObjectsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1,5))
healthTrapObjectsGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q)))
if mibBuilder.loadTexts:healthTrapObjectsGroup.setStatus(_B)
healthMonModuleTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,16,1,0,1))
healthMonModuleTrap.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:healthMonModuleTrap.setStatus(_B)
healthMonPortTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,16,1,0,2))
healthMonPortTrap.setObjects(*((_A,_O),(_A,_K),(_A,_L),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:healthMonPortTrap.setStatus(_B)
healthMonCmmTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,16,1,0,3))
healthMonCmmTrap.setObjects(*((_A,_M),(_A,_N),(_A,_Q)))
if mibBuilder.loadTexts:healthMonCmmTrap.setStatus(_B)
healthTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,1,6))
healthTrapsGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:healthTrapsGroup.setStatus(_B)
alcatelIND1HealthMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,16,1,2,2,1))
alcatelIND1HealthMonitorMIBCompliance.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:alcatelIND1HealthMonitorMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1HealthMonitorMIB':alcatelIND1HealthMonitorMIB,'alcatelIND1HealthMonitorMIBNotifications':alcatelIND1HealthMonitorMIBNotifications,_t:healthMonModuleTrap,_u:healthMonPortTrap,_v:healthMonCmmTrap,'alcatelIND1HealthMonitorMIBObjects':alcatelIND1HealthMonitorMIBObjects,'healthModuleInfo':healthModuleInfo,'healthModuleTable':healthModuleTable,'healthModuleEntry':healthModuleEntry,_I:healthModuleSlot,_S:healthModuleRx1MinAvg,_T:healthModuleRx1HrAvg,_U:healthModuleRx1DayAvg,_V:healthModuleRxTx1MinAvg,_W:healthModuleRxTx1HrAvg,_X:healthModuleRxTx1DayAvg,_Y:healthModuleMemory1MinAvg,_Z:healthModuleMemory1HrAvg,_a:healthModuleMemory1DayAvg,_b:healthModuleCpu1MinAvg,_c:healthModuleCpu1HrAvg,_d:healthModuleCpu1DayAvg,_J:healthModuleChassisId,_P:healthModuleCpuLatest,_e:healthModuleMemoryLatest,_f:healthModuleRxLatest,_g:healthModuleRxTxLatest,'healthPortInfo':healthPortInfo,'healthPortTable':healthPortTable,'healthPortEntry':healthPortEntry,_O:healthPortIfIndex,_h:healthPortRx1MinAvg,_i:healthPortRx1HrAvg,_j:healthPortRx1DayAvg,_k:healthPortRxTx1MinAvg,_l:healthPortRxTx1HrAvg,_m:healthPortRxTx1DayAvg,'healthControlInfo':healthControlInfo,_n:healthSamplingInterval,'healthThreshInfo':healthThreshInfo,_o:healthThreshRxLimit,_p:healthThreshRxTxLimit,_q:healthThreshMemoryLimit,_r:healthThreshCpuLimit,_s:healthThreshFlashLimit,'healthTrapInfo':healthTrapInfo,_K:healthMonRxStatus,_L:healthMonRxTxStatus,_M:healthMonMemoryStatus,_N:healthMonCpuStatus,_Q:healthMonFlashStatus,'alcatelIND1HealthMonitorMIBConformance':alcatelIND1HealthMonitorMIBConformance,'alcatelIND1HealthMonitorMIBGroups':alcatelIND1HealthMonitorMIBGroups,_w:healthModuleGroup,_x:healthPortGroup,_y:healthControlGroup,_z:healthThreshGroup,'healthTrapObjectsGroup':healthTrapObjectsGroup,_A0:healthTrapsGroup,'alcatelIND1HealthMonitorMIBCompliances':alcatelIND1HealthMonitorMIBCompliances,'alcatelIND1HealthMonitorMIBCompliance':alcatelIND1HealthMonitorMIBCompliance})