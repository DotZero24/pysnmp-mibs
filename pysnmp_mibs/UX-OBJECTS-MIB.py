_s='uxDSX0ConfigEntry'
_r='uxUserStatsIntervalNumber'
_q='uxCardIndex'
_p='uxFanIndex'
_o='notapplicable'
_n='uxPSUIndex'
_m='fXS-4PortsNRLowerBoard'
_l='dS1-2SpansBoard'
_k='dS1-1SpanBoard'
_j='bRI-4PortsBoard'
_i='fXO-4PortsUpperBoard'
_h='fXO-4PortsLowerBoard'
_g='fXS-4PortsUpperBoard'
_f='fXS-4PortsLowerBoard'
_e='fXS-24PortsLineCard'
_d='fXS-16PortsLineCard'
_c='fXS-8PortsLineCard'
_b='dS1-8Spans'
_a='dS1-4Spans'
_Z='dS1-2Spans'
_Y='uxModuleIndex'
_X='uxDSPIndex'
_W='uxDSPPeakUsageIntervalIndex'
_V='uxSystemUsageIntervalNumber'
_U='uxAlarmActiveIndex'
_T='autoCancel'
_S='nonAutoCancel'
_R='security'
_Q='environmental'
_P='general'
_O='processing'
_N='equipment'
_M='communication'
_L='uxAlarmIndex'
_K='deprecated'
_J='unknown'
_I='down'
_H='critical'
_G='major'
_F='minor'
_E='warning'
_D='UX-OBJECTS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx0ConfigEntry,=mibBuilder.importSymbols('DS0-MIB','dsx0ConfigEntry')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ux=ModuleIdentity((1,3,6,1,4,1,177,15))
if mibBuilder.loadTexts:ux.setRevisions(('2009-11-04 17:05',))
_Net_ObjectIdentity=ObjectIdentity
net=_Net_ObjectIdentity((1,3,6,1,4,1,177))
_UxObjects_ObjectIdentity=ObjectIdentity
uxObjects=_UxObjects_ObjectIdentity((1,3,6,1,4,1,177,15,1))
_UxChassis_ObjectIdentity=ObjectIdentity
uxChassis=_UxChassis_ObjectIdentity((1,3,6,1,4,1,177,15,1,1))
_ChasiDescUX2000_Type=DisplayString
_ChasiDescUX2000_Object=MibScalar
chasiDescUX2000=_ChasiDescUX2000_Object((1,3,6,1,4,1,177,15,1,1,1),_ChasiDescUX2000_Type())
chasiDescUX2000.setMaxAccess(_B)
if mibBuilder.loadTexts:chasiDescUX2000.setStatus(_K)
_ChasiDescUX1000_Type=DisplayString
_ChasiDescUX1000_Object=MibScalar
chasiDescUX1000=_ChasiDescUX1000_Object((1,3,6,1,4,1,177,15,1,1,2),_ChasiDescUX1000_Type())
chasiDescUX1000.setMaxAccess(_B)
if mibBuilder.loadTexts:chasiDescUX1000.setStatus(_K)
_ChasiType_Type=DisplayString
_ChasiType_Object=MibScalar
chasiType=_ChasiType_Object((1,3,6,1,4,1,177,15,1,1,3),_ChasiType_Type())
chasiType.setMaxAccess(_B)
if mibBuilder.loadTexts:chasiType.setStatus(_A)
_UxAlarmCfgTable_Object=MibTable
uxAlarmCfgTable=_UxAlarmCfgTable_Object((1,3,6,1,4,1,177,15,1,2))
if mibBuilder.loadTexts:uxAlarmCfgTable.setStatus(_A)
_UxAlarmCfgEntry_Object=MibTableRow
uxAlarmCfgEntry=_UxAlarmCfgEntry_Object((1,3,6,1,4,1,177,15,1,2,1))
uxAlarmCfgEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:uxAlarmCfgEntry.setStatus(_A)
class _UxAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147418112))
_UxAlarmIndex_Type.__name__=_C
_UxAlarmIndex_Object=MibTableColumn
uxAlarmIndex=_UxAlarmIndex_Object((1,3,6,1,4,1,177,15,1,2,1,1),_UxAlarmIndex_Type())
uxAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmIndex.setStatus(_A)
class _UxAlarmID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_UxAlarmID_Type.__name__=_C
_UxAlarmID_Object=MibTableColumn
uxAlarmID=_UxAlarmID_Object((1,3,6,1,4,1,177,15,1,2,1,2),_UxAlarmID_Type())
uxAlarmID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmID.setStatus(_A)
class _UxAlarmSubID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxAlarmSubID_Type.__name__=_C
_UxAlarmSubID_Object=MibTableColumn
uxAlarmSubID=_UxAlarmSubID_Object((1,3,6,1,4,1,177,15,1,2,1,3),_UxAlarmSubID_Type())
uxAlarmSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmSubID.setStatus(_A)
_UxAlarmCondition_Type=DisplayString
_UxAlarmCondition_Object=MibTableColumn
uxAlarmCondition=_UxAlarmCondition_Object((1,3,6,1,4,1,177,15,1,2,1,4),_UxAlarmCondition_Type())
uxAlarmCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmCondition.setStatus(_A)
class _UxAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),(_E,1),(_F,2),(_G,3),(_H,4)))
_UxAlarmSeverity_Type.__name__=_C
_UxAlarmSeverity_Object=MibTableColumn
uxAlarmSeverity=_UxAlarmSeverity_Object((1,3,6,1,4,1,177,15,1,2,1,5),_UxAlarmSeverity_Type())
uxAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmSeverity.setStatus(_A)
class _UxAlarmCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),('qos',6),(_R,7)))
_UxAlarmCategory_Type.__name__=_C
_UxAlarmCategory_Object=MibTableColumn
uxAlarmCategory=_UxAlarmCategory_Object((1,3,6,1,4,1,177,15,1,2,1,6),_UxAlarmCategory_Type())
uxAlarmCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmCategory.setStatus(_A)
class _UxAlarmCancelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_UxAlarmCancelType_Type.__name__=_C
_UxAlarmCancelType_Object=MibTableColumn
uxAlarmCancelType=_UxAlarmCancelType_Object((1,3,6,1,4,1,177,15,1,2,1,7),_UxAlarmCancelType_Type())
uxAlarmCancelType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmCancelType.setStatus(_A)
class _UxAlarmEvtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarm',1),('event',2)))
_UxAlarmEvtType_Type.__name__=_C
_UxAlarmEvtType_Object=MibTableColumn
uxAlarmEvtType=_UxAlarmEvtType_Object((1,3,6,1,4,1,177,15,1,2,1,8),_UxAlarmEvtType_Type())
uxAlarmEvtType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmEvtType.setStatus(_A)
_UxAlarmDecodeKey_Type=DisplayString
_UxAlarmDecodeKey_Object=MibTableColumn
uxAlarmDecodeKey=_UxAlarmDecodeKey_Object((1,3,6,1,4,1,177,15,1,2,1,9),_UxAlarmDecodeKey_Type())
uxAlarmDecodeKey.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmDecodeKey.setStatus(_A)
class _UxAlarmClrID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_UxAlarmClrID_Type.__name__=_C
_UxAlarmClrID_Object=MibTableColumn
uxAlarmClrID=_UxAlarmClrID_Object((1,3,6,1,4,1,177,15,1,2,1,10),_UxAlarmClrID_Type())
uxAlarmClrID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmClrID.setStatus(_A)
class _UxAlarmClrSubID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxAlarmClrSubID_Type.__name__=_C
_UxAlarmClrSubID_Object=MibTableColumn
uxAlarmClrSubID=_UxAlarmClrSubID_Object((1,3,6,1,4,1,177,15,1,2,1,11),_UxAlarmClrSubID_Type())
uxAlarmClrSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmClrSubID.setStatus(_A)
_UxAlarmDescription_Type=DisplayString
_UxAlarmDescription_Object=MibTableColumn
uxAlarmDescription=_UxAlarmDescription_Object((1,3,6,1,4,1,177,15,1,2,1,12),_UxAlarmDescription_Type())
uxAlarmDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmDescription.setStatus(_A)
_UxActAlarmTable_Object=MibTable
uxActAlarmTable=_UxActAlarmTable_Object((1,3,6,1,4,1,177,15,1,3))
if mibBuilder.loadTexts:uxActAlarmTable.setStatus(_A)
_UxActAlarmEntry_Object=MibTableRow
uxActAlarmEntry=_UxActAlarmEntry_Object((1,3,6,1,4,1,177,15,1,3,1))
uxActAlarmEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:uxActAlarmEntry.setStatus(_A)
class _UxAlarmActiveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147418112))
_UxAlarmActiveIndex_Type.__name__=_C
_UxAlarmActiveIndex_Object=MibTableColumn
uxAlarmActiveIndex=_UxAlarmActiveIndex_Object((1,3,6,1,4,1,177,15,1,3,1,1),_UxAlarmActiveIndex_Type())
uxAlarmActiveIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveIndex.setStatus(_A)
class _UxAlarmConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147418112))
_UxAlarmConfigIndex_Type.__name__=_C
_UxAlarmConfigIndex_Object=MibTableColumn
uxAlarmConfigIndex=_UxAlarmConfigIndex_Object((1,3,6,1,4,1,177,15,1,3,1,2),_UxAlarmConfigIndex_Type())
uxAlarmConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmConfigIndex.setStatus(_A)
class _UxAlarmActiveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_UxAlarmActiveID_Type.__name__=_C
_UxAlarmActiveID_Object=MibTableColumn
uxAlarmActiveID=_UxAlarmActiveID_Object((1,3,6,1,4,1,177,15,1,3,1,3),_UxAlarmActiveID_Type())
uxAlarmActiveID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveID.setStatus(_A)
class _UxAlarmActiveSubID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxAlarmActiveSubID_Type.__name__=_C
_UxAlarmActiveSubID_Object=MibTableColumn
uxAlarmActiveSubID=_UxAlarmActiveSubID_Object((1,3,6,1,4,1,177,15,1,3,1,4),_UxAlarmActiveSubID_Type())
uxAlarmActiveSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveSubID.setStatus(_A)
_UxAlarmActiveCondition_Type=DisplayString
_UxAlarmActiveCondition_Object=MibTableColumn
uxAlarmActiveCondition=_UxAlarmActiveCondition_Object((1,3,6,1,4,1,177,15,1,3,1,5),_UxAlarmActiveCondition_Type())
uxAlarmActiveCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveCondition.setStatus(_A)
class _UxAlarmActiveSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),(_E,1),(_F,2),(_G,3),(_H,4)))
_UxAlarmActiveSeverity_Type.__name__=_C
_UxAlarmActiveSeverity_Object=MibTableColumn
uxAlarmActiveSeverity=_UxAlarmActiveSeverity_Object((1,3,6,1,4,1,177,15,1,3,1,6),_UxAlarmActiveSeverity_Type())
uxAlarmActiveSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveSeverity.setStatus(_A)
class _UxAlarmActiveCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),('qos',6),(_R,7)))
_UxAlarmActiveCategory_Type.__name__=_C
_UxAlarmActiveCategory_Object=MibTableColumn
uxAlarmActiveCategory=_UxAlarmActiveCategory_Object((1,3,6,1,4,1,177,15,1,3,1,7),_UxAlarmActiveCategory_Type())
uxAlarmActiveCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveCategory.setStatus(_A)
class _UxAlarmActiveCancelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_UxAlarmActiveCancelType_Type.__name__=_C
_UxAlarmActiveCancelType_Object=MibTableColumn
uxAlarmActiveCancelType=_UxAlarmActiveCancelType_Object((1,3,6,1,4,1,177,15,1,3,1,8),_UxAlarmActiveCancelType_Type())
uxAlarmActiveCancelType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveCancelType.setStatus(_A)
_UxAlarmActiveFirstOccur_Type=Counter64
_UxAlarmActiveFirstOccur_Object=MibTableColumn
uxAlarmActiveFirstOccur=_UxAlarmActiveFirstOccur_Object((1,3,6,1,4,1,177,15,1,3,1,9),_UxAlarmActiveFirstOccur_Type())
uxAlarmActiveFirstOccur.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveFirstOccur.setStatus(_A)
_UxAlarmActiveLastOccur_Type=Counter64
_UxAlarmActiveLastOccur_Object=MibTableColumn
uxAlarmActiveLastOccur=_UxAlarmActiveLastOccur_Object((1,3,6,1,4,1,177,15,1,3,1,10),_UxAlarmActiveLastOccur_Type())
uxAlarmActiveLastOccur.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveLastOccur.setStatus(_A)
class _UxAlarmActiveCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_UxAlarmActiveCount_Type.__name__=_C
_UxAlarmActiveCount_Object=MibTableColumn
uxAlarmActiveCount=_UxAlarmActiveCount_Object((1,3,6,1,4,1,177,15,1,3,1,11),_UxAlarmActiveCount_Type())
uxAlarmActiveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveCount.setStatus(_A)
_UxAlarmActiveDecodeKey_Type=DisplayString
_UxAlarmActiveDecodeKey_Object=MibTableColumn
uxAlarmActiveDecodeKey=_UxAlarmActiveDecodeKey_Object((1,3,6,1,4,1,177,15,1,3,1,12),_UxAlarmActiveDecodeKey_Type())
uxAlarmActiveDecodeKey.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveDecodeKey.setStatus(_A)
_UxAlarmActiveSourceInstance_Type=DisplayString
_UxAlarmActiveSourceInstance_Object=MibTableColumn
uxAlarmActiveSourceInstance=_UxAlarmActiveSourceInstance_Object((1,3,6,1,4,1,177,15,1,3,1,13),_UxAlarmActiveSourceInstance_Type())
uxAlarmActiveSourceInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveSourceInstance.setStatus(_A)
class _UxAlarmActiveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acklnowledged',1),('unacknowledged',2),('cancel',3)))
_UxAlarmActiveState_Type.__name__=_C
_UxAlarmActiveState_Object=MibTableColumn
uxAlarmActiveState=_UxAlarmActiveState_Object((1,3,6,1,4,1,177,15,1,3,1,14),_UxAlarmActiveState_Type())
uxAlarmActiveState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveState.setStatus(_A)
class _UxAlarmActiveClrEvtID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_UxAlarmActiveClrEvtID_Type.__name__=_C
_UxAlarmActiveClrEvtID_Object=MibTableColumn
uxAlarmActiveClrEvtID=_UxAlarmActiveClrEvtID_Object((1,3,6,1,4,1,177,15,1,3,1,15),_UxAlarmActiveClrEvtID_Type())
uxAlarmActiveClrEvtID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveClrEvtID.setStatus(_A)
class _UxAlarmActiveClrEvtSubID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxAlarmActiveClrEvtSubID_Type.__name__=_C
_UxAlarmActiveClrEvtSubID_Object=MibTableColumn
uxAlarmActiveClrEvtSubID=_UxAlarmActiveClrEvtSubID_Object((1,3,6,1,4,1,177,15,1,3,1,16),_UxAlarmActiveClrEvtSubID_Type())
uxAlarmActiveClrEvtSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveClrEvtSubID.setStatus(_A)
_UxAlarmActiveDescription_Type=DisplayString
_UxAlarmActiveDescription_Object=MibTableColumn
uxAlarmActiveDescription=_UxAlarmActiveDescription_Object((1,3,6,1,4,1,177,15,1,3,1,17),_UxAlarmActiveDescription_Type())
uxAlarmActiveDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveDescription.setStatus(_A)
class _UxAlarmActiveHighestSeverityAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_UxAlarmActiveHighestSeverityAlarm_Type.__name__=_C
_UxAlarmActiveHighestSeverityAlarm_Object=MibTableColumn
uxAlarmActiveHighestSeverityAlarm=_UxAlarmActiveHighestSeverityAlarm_Object((1,3,6,1,4,1,177,15,1,3,1,18),_UxAlarmActiveHighestSeverityAlarm_Type())
uxAlarmActiveHighestSeverityAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveHighestSeverityAlarm.setStatus(_A)
_UxAlarmActiveHardWareID_Type=DisplayString
_UxAlarmActiveHardWareID_Object=MibTableColumn
uxAlarmActiveHardWareID=_UxAlarmActiveHardWareID_Object((1,3,6,1,4,1,177,15,1,3,1,19),_UxAlarmActiveHardWareID_Type())
uxAlarmActiveHardWareID.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAlarmActiveHardWareID.setStatus(_A)
_IpTelephony_ObjectIdentity=ObjectIdentity
ipTelephony=_IpTelephony_ObjectIdentity((1,3,6,1,4,1,177,15,1,5))
_UxSystemUsageStatsIntervalTable_Object=MibTable
uxSystemUsageStatsIntervalTable=_UxSystemUsageStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,9))
if mibBuilder.loadTexts:uxSystemUsageStatsIntervalTable.setStatus(_A)
_UxSystemUsageIntervalEntry_Object=MibTableRow
uxSystemUsageIntervalEntry=_UxSystemUsageIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,9,1))
uxSystemUsageIntervalEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:uxSystemUsageIntervalEntry.setStatus(_A)
class _UxSystemUsageIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_UxSystemUsageIntervalNumber_Type.__name__=_C
_UxSystemUsageIntervalNumber_Object=MibTableColumn
uxSystemUsageIntervalNumber=_UxSystemUsageIntervalNumber_Object((1,3,6,1,4,1,177,15,1,5,9,1,1),_UxSystemUsageIntervalNumber_Type())
uxSystemUsageIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemUsageIntervalNumber.setStatus(_A)
_UxSystemUsageIntervalCPUUsage_Type=PerfTotalCount
_UxSystemUsageIntervalCPUUsage_Object=MibTableColumn
uxSystemUsageIntervalCPUUsage=_UxSystemUsageIntervalCPUUsage_Object((1,3,6,1,4,1,177,15,1,5,9,1,2),_UxSystemUsageIntervalCPUUsage_Type())
uxSystemUsageIntervalCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemUsageIntervalCPUUsage.setStatus(_A)
_UxSystemUsageIntervalMemoryUsage_Type=PerfTotalCount
_UxSystemUsageIntervalMemoryUsage_Object=MibTableColumn
uxSystemUsageIntervalMemoryUsage=_UxSystemUsageIntervalMemoryUsage_Object((1,3,6,1,4,1,177,15,1,5,9,1,3),_UxSystemUsageIntervalMemoryUsage_Type())
uxSystemUsageIntervalMemoryUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemUsageIntervalMemoryUsage.setStatus(_A)
_UxDSPPeakUsageStatsIntervalTable_Object=MibTable
uxDSPPeakUsageStatsIntervalTable=_UxDSPPeakUsageStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,14))
if mibBuilder.loadTexts:uxDSPPeakUsageStatsIntervalTable.setStatus(_A)
_UxDSPPeakUsageIntervalEntry_Object=MibTableRow
uxDSPPeakUsageIntervalEntry=_UxDSPPeakUsageIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,14,1))
uxDSPPeakUsageIntervalEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:uxDSPPeakUsageIntervalEntry.setStatus(_A)
class _UxDSPPeakUsageIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxDSPPeakUsageIntervalIndex_Type.__name__=_C
_UxDSPPeakUsageIntervalIndex_Object=MibTableColumn
uxDSPPeakUsageIntervalIndex=_UxDSPPeakUsageIntervalIndex_Object((1,3,6,1,4,1,177,15,1,5,14,1,1),_UxDSPPeakUsageIntervalIndex_Type())
uxDSPPeakUsageIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPPeakUsageIntervalIndex.setStatus(_A)
_UxDSPPeakIntervalUsage_Type=PerfCurrentCount
_UxDSPPeakIntervalUsage_Object=MibTableColumn
uxDSPPeakIntervalUsage=_UxDSPPeakIntervalUsage_Object((1,3,6,1,4,1,177,15,1,5,14,1,2),_UxDSPPeakIntervalUsage_Type())
uxDSPPeakIntervalUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPPeakIntervalUsage.setStatus(_A)
_UxDSPResourceTable_Object=MibTable
uxDSPResourceTable=_UxDSPResourceTable_Object((1,3,6,1,4,1,177,15,1,6))
if mibBuilder.loadTexts:uxDSPResourceTable.setStatus(_A)
_UxDSPResourceEntry_Object=MibTableRow
uxDSPResourceEntry=_UxDSPResourceEntry_Object((1,3,6,1,4,1,177,15,1,6,1))
uxDSPResourceEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:uxDSPResourceEntry.setStatus(_A)
class _UxDSPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxDSPIndex_Type.__name__=_C
_UxDSPIndex_Object=MibTableColumn
uxDSPIndex=_UxDSPIndex_Object((1,3,6,1,4,1,177,15,1,6,1,1),_UxDSPIndex_Type())
uxDSPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPIndex.setStatus(_A)
_UxDSPModType_Type=DisplayString
_UxDSPModType_Object=MibTableColumn
uxDSPModType=_UxDSPModType_Object((1,3,6,1,4,1,177,15,1,6,1,2),_UxDSPModType_Type())
uxDSPModType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPModType.setStatus(_A)
class _UxDSPIsPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_UxDSPIsPresent_Type.__name__=_C
_UxDSPIsPresent_Object=MibTableColumn
uxDSPIsPresent=_UxDSPIsPresent_Object((1,3,6,1,4,1,177,15,1,6,1,3),_UxDSPIsPresent_Type())
uxDSPIsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPIsPresent.setStatus(_A)
_UxDSPCPUUsage_Type=Integer32
_UxDSPCPUUsage_Object=MibTableColumn
uxDSPCPUUsage=_UxDSPCPUUsage_Object((1,3,6,1,4,1,177,15,1,6,1,4),_UxDSPCPUUsage_Type())
uxDSPCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPCPUUsage.setStatus(_A)
_UxDSPChannelsInUse_Type=Integer32
_UxDSPChannelsInUse_Object=MibTableColumn
uxDSPChannelsInUse=_UxDSPChannelsInUse_Object((1,3,6,1,4,1,177,15,1,6,1,5),_UxDSPChannelsInUse_Type())
uxDSPChannelsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPChannelsInUse.setStatus(_A)
class _UxDSPServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('up',1)))
_UxDSPServiceStatus_Type.__name__=_C
_UxDSPServiceStatus_Object=MibTableColumn
uxDSPServiceStatus=_UxDSPServiceStatus_Object((1,3,6,1,4,1,177,15,1,6,1,6),_UxDSPServiceStatus_Type())
uxDSPServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPServiceStatus.setStatus(_A)
_UxCodecsSupported_Type=DisplayString
_UxCodecsSupported_Object=MibTableColumn
uxCodecsSupported=_UxCodecsSupported_Object((1,3,6,1,4,1,177,15,1,6,1,7),_UxCodecsSupported_Type())
uxCodecsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCodecsSupported.setStatus(_A)
_UxDSX0ConfigTable_Object=MibTable
uxDSX0ConfigTable=_UxDSX0ConfigTable_Object((1,3,6,1,4,1,177,15,1,7))
if mibBuilder.loadTexts:uxDSX0ConfigTable.setStatus(_A)
_UxDSX0ConfigEntry_Object=MibTableRow
uxDSX0ConfigEntry=_UxDSX0ConfigEntry_Object((1,3,6,1,4,1,177,15,1,7,1))
if mibBuilder.loadTexts:uxDSX0ConfigEntry.setStatus(_A)
class _UxDSX0Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('e1',0),('t1',1)))
_UxDSX0Type_Type.__name__=_C
_UxDSX0Type_Object=MibTableColumn
uxDSX0Type=_UxDSX0Type_Object((1,3,6,1,4,1,177,15,1,7,1,1),_UxDSX0Type_Type())
uxDSX0Type.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSX0Type.setStatus(_A)
_UxDSX0Speed_Type=Integer32
_UxDSX0Speed_Object=MibTableColumn
uxDSX0Speed=_UxDSX0Speed_Object((1,3,6,1,4,1,177,15,1,7,1,2),_UxDSX0Speed_Type())
uxDSX0Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSX0Speed.setStatus(_A)
_UxDSX0Lastchange_Type=Integer32
_UxDSX0Lastchange_Object=MibTableColumn
uxDSX0Lastchange=_UxDSX0Lastchange_Object((1,3,6,1,4,1,177,15,1,7,1,3),_UxDSX0Lastchange_Type())
uxDSX0Lastchange.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSX0Lastchange.setStatus(_A)
class _UxDSX0AdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('up',1)))
_UxDSX0AdminState_Type.__name__=_C
_UxDSX0AdminState_Object=MibTableColumn
uxDSX0AdminState=_UxDSX0AdminState_Object((1,3,6,1,4,1,177,15,1,7,1,4),_UxDSX0AdminState_Type())
uxDSX0AdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSX0AdminState.setStatus(_A)
_UxModuleTable_Object=MibTable
uxModuleTable=_UxModuleTable_Object((1,3,6,1,4,1,177,15,1,8))
if mibBuilder.loadTexts:uxModuleTable.setStatus(_A)
_UxModuleEntry_Object=MibTableRow
uxModuleEntry=_UxModuleEntry_Object((1,3,6,1,4,1,177,15,1,8,1))
uxModuleEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:uxModuleEntry.setStatus(_A)
class _UxModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxModuleIndex_Type.__name__=_C
_UxModuleIndex_Object=MibTableColumn
uxModuleIndex=_UxModuleIndex_Object((1,3,6,1,4,1,177,15,1,8,1,1),_UxModuleIndex_Type())
uxModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModuleIndex.setStatus(_A)
class _UxModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_J,0),(_Z,1),(_a,2),(_b,3),('eX',4),('mSPDC910DSP',5),('mSPDC300DSP',6),('reservedModule1',7),('reservedModule2',8),('reservedModule3',9),('reservedModule4',10),('aSM',11),('mainBoard',12),('chassis',13),('powerSupply',14),('reservedModule5',15),('node',16),(_c,17),(_d,18),(_e,19),(_f,20),(_g,21),(_h,22),(_i,23),(_j,24),(_k,25),(_l,26),(_m,27)))
_UxModuleType_Type.__name__=_C
_UxModuleType_Object=MibTableColumn
uxModuleType=_UxModuleType_Object((1,3,6,1,4,1,177,15,1,8,1,2),_UxModuleType_Type())
uxModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModuleType.setStatus(_A)
_UxModulePartNumber_Type=DisplayString
_UxModulePartNumber_Object=MibTableColumn
uxModulePartNumber=_UxModulePartNumber_Object((1,3,6,1,4,1,177,15,1,8,1,3),_UxModulePartNumber_Type())
uxModulePartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModulePartNumber.setStatus(_A)
_UxModuleVersionNumber_Type=DisplayString
_UxModuleVersionNumber_Object=MibTableColumn
uxModuleVersionNumber=_UxModuleVersionNumber_Object((1,3,6,1,4,1,177,15,1,8,1,4),_UxModuleVersionNumber_Type())
uxModuleVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModuleVersionNumber.setStatus(_A)
_UxModuleSerialNumber_Type=DisplayString
_UxModuleSerialNumber_Object=MibTableColumn
uxModuleSerialNumber=_UxModuleSerialNumber_Object((1,3,6,1,4,1,177,15,1,8,1,5),_UxModuleSerialNumber_Type())
uxModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModuleSerialNumber.setStatus(_A)
_UxModuleMfgWeek_Type=Integer32
_UxModuleMfgWeek_Object=MibTableColumn
uxModuleMfgWeek=_UxModuleMfgWeek_Object((1,3,6,1,4,1,177,15,1,8,1,6),_UxModuleMfgWeek_Type())
uxModuleMfgWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModuleMfgWeek.setStatus(_A)
_UxModuleMfgYear_Type=Integer32
_UxModuleMfgYear_Object=MibTableColumn
uxModuleMfgYear=_UxModuleMfgYear_Object((1,3,6,1,4,1,177,15,1,8,1,7),_UxModuleMfgYear_Type())
uxModuleMfgYear.setMaxAccess(_B)
if mibBuilder.loadTexts:uxModuleMfgYear.setStatus(_A)
_UxPSUTable_Object=MibTable
uxPSUTable=_UxPSUTable_Object((1,3,6,1,4,1,177,15,1,9))
if mibBuilder.loadTexts:uxPSUTable.setStatus(_A)
_UxPSUEntry_Object=MibTableRow
uxPSUEntry=_UxPSUEntry_Object((1,3,6,1,4,1,177,15,1,9,1))
uxPSUEntry.setIndexNames((0,_D,_n))
if mibBuilder.loadTexts:uxPSUEntry.setStatus(_A)
class _UxPSUIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_UxPSUIndex_Type.__name__=_C
_UxPSUIndex_Object=MibTableColumn
uxPSUIndex=_UxPSUIndex_Object((1,3,6,1,4,1,177,15,1,9,1,1),_UxPSUIndex_Type())
uxPSUIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUIndex.setStatus(_A)
class _UxPSUIsPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('present',1),('notpresent',2)))
_UxPSUIsPresent_Type.__name__=_C
_UxPSUIsPresent_Object=MibTableColumn
uxPSUIsPresent=_UxPSUIsPresent_Object((1,3,6,1,4,1,177,15,1,9,1,2),_UxPSUIsPresent_Type())
uxPSUIsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUIsPresent.setStatus(_A)
class _UxPSUIsInputGood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_UxPSUIsInputGood_Type.__name__=_C
_UxPSUIsInputGood_Object=MibTableColumn
uxPSUIsInputGood=_UxPSUIsInputGood_Object((1,3,6,1,4,1,177,15,1,9,1,3),_UxPSUIsInputGood_Type())
uxPSUIsInputGood.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUIsInputGood.setStatus(_A)
class _UxPSUInputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_o,0),('ac',1),('dc',2)))
_UxPSUInputType_Type.__name__=_C
_UxPSUInputType_Object=MibTableColumn
uxPSUInputType=_UxPSUInputType_Object((1,3,6,1,4,1,177,15,1,9,1,4),_UxPSUInputType_Type())
uxPSUInputType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUInputType.setStatus(_A)
class _UxPSUPowerIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_UxPSUPowerIn_Type.__name__=_C
_UxPSUPowerIn_Object=MibTableColumn
uxPSUPowerIn=_UxPSUPowerIn_Object((1,3,6,1,4,1,177,15,1,9,1,5),_UxPSUPowerIn_Type())
uxPSUPowerIn.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUPowerIn.setStatus(_A)
class _UxPSUPowerOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_UxPSUPowerOut_Type.__name__=_C
_UxPSUPowerOut_Object=MibTableColumn
uxPSUPowerOut=_UxPSUPowerOut_Object((1,3,6,1,4,1,177,15,1,9,1,6),_UxPSUPowerOut_Type())
uxPSUPowerOut.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUPowerOut.setStatus(_A)
class _UxPSUVoltageIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_UxPSUVoltageIn_Type.__name__=_C
_UxPSUVoltageIn_Object=MibTableColumn
uxPSUVoltageIn=_UxPSUVoltageIn_Object((1,3,6,1,4,1,177,15,1,9,1,7),_UxPSUVoltageIn_Type())
uxPSUVoltageIn.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUVoltageIn.setStatus(_A)
class _UxPSUVoltageOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_UxPSUVoltageOut_Type.__name__=_C
_UxPSUVoltageOut_Object=MibTableColumn
uxPSUVoltageOut=_UxPSUVoltageOut_Object((1,3,6,1,4,1,177,15,1,9,1,8),_UxPSUVoltageOut_Type())
uxPSUVoltageOut.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUVoltageOut.setStatus(_A)
class _UxPSUCurrentIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_UxPSUCurrentIn_Type.__name__=_C
_UxPSUCurrentIn_Object=MibTableColumn
uxPSUCurrentIn=_UxPSUCurrentIn_Object((1,3,6,1,4,1,177,15,1,9,1,9),_UxPSUCurrentIn_Type())
uxPSUCurrentIn.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUCurrentIn.setStatus(_A)
class _UxPSUCurrentOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_UxPSUCurrentOut_Type.__name__=_C
_UxPSUCurrentOut_Object=MibTableColumn
uxPSUCurrentOut=_UxPSUCurrentOut_Object((1,3,6,1,4,1,177,15,1,9,1,10),_UxPSUCurrentOut_Type())
uxPSUCurrentOut.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUCurrentOut.setStatus(_A)
class _UxPSUTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_UxPSUTemperature_Type.__name__=_C
_UxPSUTemperature_Object=MibTableColumn
uxPSUTemperature=_UxPSUTemperature_Object((1,3,6,1,4,1,177,15,1,9,1,11),_UxPSUTemperature_Type())
uxPSUTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUTemperature.setStatus(_A)
class _UxPSUFanSpeed1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UxPSUFanSpeed1_Type.__name__=_C
_UxPSUFanSpeed1_Object=MibTableColumn
uxPSUFanSpeed1=_UxPSUFanSpeed1_Object((1,3,6,1,4,1,177,15,1,9,1,12),_UxPSUFanSpeed1_Type())
uxPSUFanSpeed1.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUFanSpeed1.setStatus(_A)
class _UxPSUFanSpeed2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UxPSUFanSpeed2_Type.__name__=_C
_UxPSUFanSpeed2_Object=MibTableColumn
uxPSUFanSpeed2=_UxPSUFanSpeed2_Object((1,3,6,1,4,1,177,15,1,9,1,13),_UxPSUFanSpeed2_Type())
uxPSUFanSpeed2.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPSUFanSpeed2.setStatus(_A)
_UxFanTable_Object=MibTable
uxFanTable=_UxFanTable_Object((1,3,6,1,4,1,177,15,1,10))
if mibBuilder.loadTexts:uxFanTable.setStatus(_A)
_UxFanEntry_Object=MibTableRow
uxFanEntry=_UxFanEntry_Object((1,3,6,1,4,1,177,15,1,10,1))
uxFanEntry.setIndexNames((0,_D,_p))
if mibBuilder.loadTexts:uxFanEntry.setStatus(_A)
class _UxFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_UxFanIndex_Type.__name__=_C
_UxFanIndex_Object=MibTableColumn
uxFanIndex=_UxFanIndex_Object((1,3,6,1,4,1,177,15,1,10,1,1),_UxFanIndex_Type())
uxFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxFanIndex.setStatus(_A)
class _UxFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UxFanSpeed_Type.__name__=_C
_UxFanSpeed_Object=MibTableColumn
uxFanSpeed=_UxFanSpeed_Object((1,3,6,1,4,1,177,15,1,10,1,2),_UxFanSpeed_Type())
uxFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:uxFanSpeed.setStatus(_A)
_UxCardTable_Object=MibTable
uxCardTable=_UxCardTable_Object((1,3,6,1,4,1,177,15,1,11))
if mibBuilder.loadTexts:uxCardTable.setStatus(_A)
_UxCardEntry_Object=MibTableRow
uxCardEntry=_UxCardEntry_Object((1,3,6,1,4,1,177,15,1,11,1))
uxCardEntry.setIndexNames((0,_D,_q))
if mibBuilder.loadTexts:uxCardEntry.setStatus(_A)
class _UxCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCardIndex_Type.__name__=_C
_UxCardIndex_Object=MibTableColumn
uxCardIndex=_UxCardIndex_Object((1,3,6,1,4,1,177,15,1,11,1,1),_UxCardIndex_Type())
uxCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCardIndex.setStatus(_A)
class _UxCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_J,0),(_Z,1),(_a,2),(_b,3),('eX',4),(_c,17),(_d,18),(_e,19),(_f,20),(_g,21),(_h,22),(_i,23),(_j,24),(_k,25),(_l,26),(_m,27)))
_UxCardType_Type.__name__=_C
_UxCardType_Object=MibTableColumn
uxCardType=_UxCardType_Object((1,3,6,1,4,1,177,15,1,11,1,2),_UxCardType_Type())
uxCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCardType.setStatus(_A)
class _UxCardServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('up',1),(_o,2)))
_UxCardServiceStatus_Type.__name__=_C
_UxCardServiceStatus_Object=MibTableColumn
uxCardServiceStatus=_UxCardServiceStatus_Object((1,3,6,1,4,1,177,15,1,11,1,3),_UxCardServiceStatus_Type())
uxCardServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCardServiceStatus.setStatus(_A)
_UxSystem_ObjectIdentity=ObjectIdentity
uxSystem=_UxSystem_ObjectIdentity((1,3,6,1,4,1,177,15,1,12))
class _UxSystemHighestSeverityAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),('normal',1),(_E,2),(_F,3),(_G,4),(_H,5)))
_UxSystemHighestSeverityAlarm_Type.__name__=_C
_UxSystemHighestSeverityAlarm_Object=MibScalar
uxSystemHighestSeverityAlarm=_UxSystemHighestSeverityAlarm_Object((1,3,6,1,4,1,177,15,1,12,1),_UxSystemHighestSeverityAlarm_Type())
uxSystemHighestSeverityAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemHighestSeverityAlarm.setStatus(_A)
class _UxSystemCoreSwitchTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSystemCoreSwitchTemp_Type.__name__=_C
_UxSystemCoreSwitchTemp_Object=MibScalar
uxSystemCoreSwitchTemp=_UxSystemCoreSwitchTemp_Object((1,3,6,1,4,1,177,15,1,12,2),_UxSystemCoreSwitchTemp_Type())
uxSystemCoreSwitchTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemCoreSwitchTemp.setStatus(_A)
_UxSystemCurrentCPUUsage_Type=PerfCurrentCount
_UxSystemCurrentCPUUsage_Object=MibScalar
uxSystemCurrentCPUUsage=_UxSystemCurrentCPUUsage_Object((1,3,6,1,4,1,177,15,1,12,3),_UxSystemCurrentCPUUsage_Type())
uxSystemCurrentCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemCurrentCPUUsage.setStatus(_A)
_UxSystemCurrentMemoryUsage_Type=PerfCurrentCount
_UxSystemCurrentMemoryUsage_Object=MibScalar
uxSystemCurrentMemoryUsage=_UxSystemCurrentMemoryUsage_Object((1,3,6,1,4,1,177,15,1,12,4),_UxSystemCurrentMemoryUsage_Type())
uxSystemCurrentMemoryUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSystemCurrentMemoryUsage.setStatus(_A)
_UxLicenseCurrentPeakSIPCall_Type=PerfCurrentCount
_UxLicenseCurrentPeakSIPCall_Object=MibScalar
uxLicenseCurrentPeakSIPCall=_UxLicenseCurrentPeakSIPCall_Object((1,3,6,1,4,1,177,15,1,12,5),_UxLicenseCurrentPeakSIPCall_Type())
uxLicenseCurrentPeakSIPCall.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseCurrentPeakSIPCall.setStatus(_A)
_UxLicenseCurrentPeakSIPRegistration_Type=PerfCurrentCount
_UxLicenseCurrentPeakSIPRegistration_Object=MibScalar
uxLicenseCurrentPeakSIPRegistration=_UxLicenseCurrentPeakSIPRegistration_Object((1,3,6,1,4,1,177,15,1,12,6),_UxLicenseCurrentPeakSIPRegistration_Type())
uxLicenseCurrentPeakSIPRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseCurrentPeakSIPRegistration.setStatus(_A)
_UxDSPPeakCurrentUsage_Type=PerfTotalCount
_UxDSPPeakCurrentUsage_Object=MibScalar
uxDSPPeakCurrentUsage=_UxDSPPeakCurrentUsage_Object((1,3,6,1,4,1,177,15,1,12,7),_UxDSPPeakCurrentUsage_Type())
uxDSPPeakCurrentUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDSPPeakCurrentUsage.setStatus(_A)
_UxLicenseCurrentPeakTDMChannel_Type=PerfCurrentCount
_UxLicenseCurrentPeakTDMChannel_Object=MibScalar
uxLicenseCurrentPeakTDMChannel=_UxLicenseCurrentPeakTDMChannel_Object((1,3,6,1,4,1,177,15,1,12,8),_UxLicenseCurrentPeakTDMChannel_Type())
uxLicenseCurrentPeakTDMChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseCurrentPeakTDMChannel.setStatus(_A)
_UxLicenseCurrentPeakDSP_Type=PerfCurrentCount
_UxLicenseCurrentPeakDSP_Object=MibScalar
uxLicenseCurrentPeakDSP=_UxLicenseCurrentPeakDSP_Object((1,3,6,1,4,1,177,15,1,12,9),_UxLicenseCurrentPeakDSP_Type())
uxLicenseCurrentPeakDSP.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseCurrentPeakDSP.setStatus(_A)
_UxUserStatsPeakSessionsCurrentInerval_Type=Integer32
_UxUserStatsPeakSessionsCurrentInerval_Object=MibScalar
uxUserStatsPeakSessionsCurrentInerval=_UxUserStatsPeakSessionsCurrentInerval_Object((1,3,6,1,4,1,177,15,1,12,10),_UxUserStatsPeakSessionsCurrentInerval_Type())
uxUserStatsPeakSessionsCurrentInerval.setMaxAccess(_B)
if mibBuilder.loadTexts:uxUserStatsPeakSessionsCurrentInerval.setStatus(_A)
_UxUserStatsIntervalTable_Object=MibTable
uxUserStatsIntervalTable=_UxUserStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,12,11))
if mibBuilder.loadTexts:uxUserStatsIntervalTable.setStatus(_A)
_UxUserStatsIntervalEntry_Object=MibTableRow
uxUserStatsIntervalEntry=_UxUserStatsIntervalEntry_Object((1,3,6,1,4,1,177,15,1,12,11,1))
uxUserStatsIntervalEntry.setIndexNames((0,_D,_r))
if mibBuilder.loadTexts:uxUserStatsIntervalEntry.setStatus(_A)
class _UxUserStatsIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxUserStatsIntervalNumber_Type.__name__=_C
_UxUserStatsIntervalNumber_Object=MibTableColumn
uxUserStatsIntervalNumber=_UxUserStatsIntervalNumber_Object((1,3,6,1,4,1,177,15,1,12,11,1,1),_UxUserStatsIntervalNumber_Type())
uxUserStatsIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxUserStatsIntervalNumber.setStatus(_A)
_UxUserStatsPeakSessions_Type=Integer32
_UxUserStatsPeakSessions_Object=MibTableColumn
uxUserStatsPeakSessions=_UxUserStatsPeakSessions_Object((1,3,6,1,4,1,177,15,1,12,11,1,2),_UxUserStatsPeakSessions_Type())
uxUserStatsPeakSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:uxUserStatsPeakSessions.setStatus(_A)
_UxTraps_ObjectIdentity=ObjectIdentity
uxTraps=_UxTraps_ObjectIdentity((1,3,6,1,4,1,177,15,2))
dsx0ConfigEntry.registerAugmentions((_D,_s))
uxDSX0ConfigEntry.setIndexNames(*dsx0ConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'net':net,'ux':ux,'uxObjects':uxObjects,'uxChassis':uxChassis,'chasiDescUX2000':chasiDescUX2000,'chasiDescUX1000':chasiDescUX1000,'chasiType':chasiType,'uxAlarmCfgTable':uxAlarmCfgTable,'uxAlarmCfgEntry':uxAlarmCfgEntry,_L:uxAlarmIndex,'uxAlarmID':uxAlarmID,'uxAlarmSubID':uxAlarmSubID,'uxAlarmCondition':uxAlarmCondition,'uxAlarmSeverity':uxAlarmSeverity,'uxAlarmCategory':uxAlarmCategory,'uxAlarmCancelType':uxAlarmCancelType,'uxAlarmEvtType':uxAlarmEvtType,'uxAlarmDecodeKey':uxAlarmDecodeKey,'uxAlarmClrID':uxAlarmClrID,'uxAlarmClrSubID':uxAlarmClrSubID,'uxAlarmDescription':uxAlarmDescription,'uxActAlarmTable':uxActAlarmTable,'uxActAlarmEntry':uxActAlarmEntry,_U:uxAlarmActiveIndex,'uxAlarmConfigIndex':uxAlarmConfigIndex,'uxAlarmActiveID':uxAlarmActiveID,'uxAlarmActiveSubID':uxAlarmActiveSubID,'uxAlarmActiveCondition':uxAlarmActiveCondition,'uxAlarmActiveSeverity':uxAlarmActiveSeverity,'uxAlarmActiveCategory':uxAlarmActiveCategory,'uxAlarmActiveCancelType':uxAlarmActiveCancelType,'uxAlarmActiveFirstOccur':uxAlarmActiveFirstOccur,'uxAlarmActiveLastOccur':uxAlarmActiveLastOccur,'uxAlarmActiveCount':uxAlarmActiveCount,'uxAlarmActiveDecodeKey':uxAlarmActiveDecodeKey,'uxAlarmActiveSourceInstance':uxAlarmActiveSourceInstance,'uxAlarmActiveState':uxAlarmActiveState,'uxAlarmActiveClrEvtID':uxAlarmActiveClrEvtID,'uxAlarmActiveClrEvtSubID':uxAlarmActiveClrEvtSubID,'uxAlarmActiveDescription':uxAlarmActiveDescription,'uxAlarmActiveHighestSeverityAlarm':uxAlarmActiveHighestSeverityAlarm,'uxAlarmActiveHardWareID':uxAlarmActiveHardWareID,'ipTelephony':ipTelephony,'uxSystemUsageStatsIntervalTable':uxSystemUsageStatsIntervalTable,'uxSystemUsageIntervalEntry':uxSystemUsageIntervalEntry,_V:uxSystemUsageIntervalNumber,'uxSystemUsageIntervalCPUUsage':uxSystemUsageIntervalCPUUsage,'uxSystemUsageIntervalMemoryUsage':uxSystemUsageIntervalMemoryUsage,'uxDSPPeakUsageStatsIntervalTable':uxDSPPeakUsageStatsIntervalTable,'uxDSPPeakUsageIntervalEntry':uxDSPPeakUsageIntervalEntry,_W:uxDSPPeakUsageIntervalIndex,'uxDSPPeakIntervalUsage':uxDSPPeakIntervalUsage,'uxDSPResourceTable':uxDSPResourceTable,'uxDSPResourceEntry':uxDSPResourceEntry,_X:uxDSPIndex,'uxDSPModType':uxDSPModType,'uxDSPIsPresent':uxDSPIsPresent,'uxDSPCPUUsage':uxDSPCPUUsage,'uxDSPChannelsInUse':uxDSPChannelsInUse,'uxDSPServiceStatus':uxDSPServiceStatus,'uxCodecsSupported':uxCodecsSupported,'uxDSX0ConfigTable':uxDSX0ConfigTable,_s:uxDSX0ConfigEntry,'uxDSX0Type':uxDSX0Type,'uxDSX0Speed':uxDSX0Speed,'uxDSX0Lastchange':uxDSX0Lastchange,'uxDSX0AdminState':uxDSX0AdminState,'uxModuleTable':uxModuleTable,'uxModuleEntry':uxModuleEntry,_Y:uxModuleIndex,'uxModuleType':uxModuleType,'uxModulePartNumber':uxModulePartNumber,'uxModuleVersionNumber':uxModuleVersionNumber,'uxModuleSerialNumber':uxModuleSerialNumber,'uxModuleMfgWeek':uxModuleMfgWeek,'uxModuleMfgYear':uxModuleMfgYear,'uxPSUTable':uxPSUTable,'uxPSUEntry':uxPSUEntry,_n:uxPSUIndex,'uxPSUIsPresent':uxPSUIsPresent,'uxPSUIsInputGood':uxPSUIsInputGood,'uxPSUInputType':uxPSUInputType,'uxPSUPowerIn':uxPSUPowerIn,'uxPSUPowerOut':uxPSUPowerOut,'uxPSUVoltageIn':uxPSUVoltageIn,'uxPSUVoltageOut':uxPSUVoltageOut,'uxPSUCurrentIn':uxPSUCurrentIn,'uxPSUCurrentOut':uxPSUCurrentOut,'uxPSUTemperature':uxPSUTemperature,'uxPSUFanSpeed1':uxPSUFanSpeed1,'uxPSUFanSpeed2':uxPSUFanSpeed2,'uxFanTable':uxFanTable,'uxFanEntry':uxFanEntry,_p:uxFanIndex,'uxFanSpeed':uxFanSpeed,'uxCardTable':uxCardTable,'uxCardEntry':uxCardEntry,_q:uxCardIndex,'uxCardType':uxCardType,'uxCardServiceStatus':uxCardServiceStatus,'uxSystem':uxSystem,'uxSystemHighestSeverityAlarm':uxSystemHighestSeverityAlarm,'uxSystemCoreSwitchTemp':uxSystemCoreSwitchTemp,'uxSystemCurrentCPUUsage':uxSystemCurrentCPUUsage,'uxSystemCurrentMemoryUsage':uxSystemCurrentMemoryUsage,'uxLicenseCurrentPeakSIPCall':uxLicenseCurrentPeakSIPCall,'uxLicenseCurrentPeakSIPRegistration':uxLicenseCurrentPeakSIPRegistration,'uxDSPPeakCurrentUsage':uxDSPPeakCurrentUsage,'uxLicenseCurrentPeakTDMChannel':uxLicenseCurrentPeakTDMChannel,'uxLicenseCurrentPeakDSP':uxLicenseCurrentPeakDSP,'uxUserStatsPeakSessionsCurrentInerval':uxUserStatsPeakSessionsCurrentInerval,'uxUserStatsIntervalTable':uxUserStatsIntervalTable,'uxUserStatsIntervalEntry':uxUserStatsIntervalEntry,_r:uxUserStatsIntervalNumber,'uxUserStatsPeakSessions':uxUserStatsPeakSessions,'uxTraps':uxTraps})