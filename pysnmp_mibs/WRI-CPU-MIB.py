_K='disable'
_J='enable'
_I='cpuIndex'
_H='cpuLthreshold'
_G='cpuHthreshold'
_F='cpuUsage'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='WRI-CPU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wri,wriProducts=mibBuilder.importSymbols('WRI-SMI','wri','wriProducts')
msppCpu=ModuleIdentity((1,3,6,1,4,1,3807,1,8012,1,4))
if mibBuilder.loadTexts:msppCpu.setRevisions(('2010-01-11 00:00','2009-01-11 00:00'))
_Mspp_ObjectIdentity=ObjectIdentity
mspp=_Mspp_ObjectIdentity((1,3,6,1,4,1,3807,1,8012))
_MsppChassis_ObjectIdentity=ObjectIdentity
msppChassis=_MsppChassis_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1))
_CpuTable_Object=MibTable
cpuTable=_CpuTable_Object((1,3,6,1,4,1,3807,1,8012,1,4,1))
if mibBuilder.loadTexts:cpuTable.setStatus(_A)
_CpuEntry_Object=MibTableRow
cpuEntry=_CpuEntry_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1))
cpuEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cpuEntry.setStatus(_A)
_CpuIndex_Type=Unsigned32
_CpuIndex_Object=MibTableColumn
cpuIndex=_CpuIndex_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,1),_CpuIndex_Type())
cpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuIndex.setStatus(_A)
_CpuUsage_Type=Counter32
_CpuUsage_Object=MibTableColumn
cpuUsage=_CpuUsage_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,2),_CpuUsage_Type())
cpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuUsage.setStatus(_A)
_CpuMaxUsage_Type=Counter32
_CpuMaxUsage_Object=MibTableColumn
cpuMaxUsage=_CpuMaxUsage_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,3),_CpuMaxUsage_Type())
cpuMaxUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuMaxUsage.setStatus(_A)
_CpuHthreshold_Type=Counter32
_CpuHthreshold_Object=MibTableColumn
cpuHthreshold=_CpuHthreshold_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,4),_CpuHthreshold_Type())
cpuHthreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuHthreshold.setStatus(_A)
_CpuLthreshold_Type=Counter32
_CpuLthreshold_Object=MibTableColumn
cpuLthreshold=_CpuLthreshold_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,5),_CpuLthreshold_Type())
cpuLthreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLthreshold.setStatus(_A)
class _CpuOneTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CpuOneTrap_Type.__name__=_E
_CpuOneTrap_Object=MibTableColumn
cpuOneTrap=_CpuOneTrap_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,6),_CpuOneTrap_Type())
cpuOneTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuOneTrap.setStatus(_A)
class _CpuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('highoverflow',1)))
_CpuStatus_Type.__name__=_E
_CpuStatus_Object=MibTableColumn
cpuStatus=_CpuStatus_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,7),_CpuStatus_Type())
cpuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuStatus.setStatus(_A)
_CpuDescr_Type=OctetString
_CpuDescr_Object=MibTableColumn
cpuDescr=_CpuDescr_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,8),_CpuDescr_Type())
cpuDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuDescr.setStatus(_A)
_CpuAllSetting_Type=OctetString
_CpuAllSetting_Object=MibTableColumn
cpuAllSetting=_CpuAllSetting_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,9),_CpuAllSetting_Type())
cpuAllSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuAllSetting.setStatus(_A)
_CpuLastOneMinuteUsage_Type=Counter32
_CpuLastOneMinuteUsage_Object=MibTableColumn
cpuLastOneMinuteUsage=_CpuLastOneMinuteUsage_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,10),_CpuLastOneMinuteUsage_Type())
cpuLastOneMinuteUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuLastOneMinuteUsage.setStatus(_A)
_CpuLastFiveMinuteUsage_Type=Counter32
_CpuLastFiveMinuteUsage_Object=MibTableColumn
cpuLastFiveMinuteUsage=_CpuLastFiveMinuteUsage_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,11),_CpuLastFiveMinuteUsage_Type())
cpuLastFiveMinuteUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuLastFiveMinuteUsage.setStatus(_A)
_CpuIndexDescr_Type=OctetString
_CpuIndexDescr_Object=MibTableColumn
cpuIndexDescr=_CpuIndexDescr_Object((1,3,6,1,4,1,3807,1,8012,1,4,1,1,12),_CpuIndexDescr_Type())
cpuIndexDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuIndexDescr.setStatus(_A)
_CpuTrap_ObjectIdentity=ObjectIdentity
cpuTrap=_CpuTrap_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,4,2))
_CpuGeneral_ObjectIdentity=ObjectIdentity
cpuGeneral=_CpuGeneral_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,4,3))
_CpuNum_Type=Integer32
_CpuNum_Object=MibScalar
cpuNum=_CpuNum_Object((1,3,6,1,4,1,3807,1,8012,1,4,3,1),_CpuNum_Type())
cpuNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuNum.setStatus(_A)
_CpuTrapEnable_Type=Integer32
_CpuTrapEnable_Object=MibScalar
cpuTrapEnable=_CpuTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,1,4,3,2),_CpuTrapEnable_Type())
cpuTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuTrapEnable.setStatus(_A)
class _CpuMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CpuMonitor_Type.__name__=_E
_CpuMonitor_Object=MibScalar
cpuMonitor=_CpuMonitor_Object((1,3,6,1,4,1,3807,1,8012,1,4,3,3),_CpuMonitor_Type())
cpuMonitor.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuMonitor.setStatus(_A)
cpuOverThreshold=NotificationType((1,3,6,1,4,1,3807,1,8012,1,4,2,1))
cpuOverThreshold.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cpuOverThreshold.setStatus(_A)
cpuUnderThreshold=NotificationType((1,3,6,1,4,1,3807,1,8012,1,4,2,2))
cpuUnderThreshold.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cpuUnderThreshold.setStatus(_A)
cpuRecoverThreshold=NotificationType((1,3,6,1,4,1,3807,1,8012,1,4,2,3))
cpuRecoverThreshold.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cpuRecoverThreshold.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mspp':mspp,'msppChassis':msppChassis,'msppCpu':msppCpu,'cpuTable':cpuTable,'cpuEntry':cpuEntry,_I:cpuIndex,_F:cpuUsage,'cpuMaxUsage':cpuMaxUsage,_G:cpuHthreshold,_H:cpuLthreshold,'cpuOneTrap':cpuOneTrap,'cpuStatus':cpuStatus,'cpuDescr':cpuDescr,'cpuAllSetting':cpuAllSetting,'cpuLastOneMinuteUsage':cpuLastOneMinuteUsage,'cpuLastFiveMinuteUsage':cpuLastFiveMinuteUsage,'cpuIndexDescr':cpuIndexDescr,'cpuTrap':cpuTrap,'cpuOverThreshold':cpuOverThreshold,'cpuUnderThreshold':cpuUnderThreshold,'cpuRecoverThreshold':cpuRecoverThreshold,'cpuGeneral':cpuGeneral,'cpuNum':cpuNum,'cpuTrapEnable':cpuTrapEnable,'cpuMonitor':cpuMonitor})