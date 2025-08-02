_Q='adGenProcessesMemStatHeapFree'
_P='adGenProcessesProvHeapFreeThreshold'
_O='enable'
_N='disable'
_M='Unsigned32'
_L='ADTRAN-GENPROCESSES-MIB'
_K='read-write'
_J='Integer32'
_I='sysName'
_H='SNMPv2-MIB'
_G='adTrapInformSeqNum'
_F='ADTRAN-GENTRAPINFORM-MIB'
_E='bytes'
_D='read-only'
_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adTrapInformSeqNum,=mibBuilder.importSymbols(_F,_G)
adGenProcesses,adGenProcessesID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenProcesses','adGenProcessesID')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
adGenProcessesMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,22,1))
if mibBuilder.loadTexts:adGenProcessesMIB.setRevisions(('2017-06-23 00:00','2011-09-23 00:00','2010-02-23 00:00','2010-02-22 00:00'))
_AdGenProcessesNotifications_ObjectIdentity=ObjectIdentity
adGenProcessesNotifications=_AdGenProcessesNotifications_ObjectIdentity((1,3,6,1,4,1,664,5,70,22,0))
_AdGenProcessesProvisioning_ObjectIdentity=ObjectIdentity
adGenProcessesProvisioning=_AdGenProcessesProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,22,1))
_AdGenProcessesProvTable_Object=MibTable
adGenProcessesProvTable=_AdGenProcessesProvTable_Object((1,3,6,1,4,1,664,5,70,22,1,1))
if mibBuilder.loadTexts:adGenProcessesProvTable.setStatus(_A)
_AdGenProcessesProvEntry_Object=MibTableRow
adGenProcessesProvEntry=_AdGenProcessesProvEntry_Object((1,3,6,1,4,1,664,5,70,22,1,1,1))
adGenProcessesProvEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenProcessesProvEntry.setStatus(_A)
class _AdGenProcessesProvHeapFreeThreshold_Type(Unsigned32):defaultValue=0
_AdGenProcessesProvHeapFreeThreshold_Type.__name__=_M
_AdGenProcessesProvHeapFreeThreshold_Object=MibTableColumn
adGenProcessesProvHeapFreeThreshold=_AdGenProcessesProvHeapFreeThreshold_Object((1,3,6,1,4,1,664,5,70,22,1,1,1,1),_AdGenProcessesProvHeapFreeThreshold_Type())
adGenProcessesProvHeapFreeThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:adGenProcessesProvHeapFreeThreshold.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesProvHeapFreeThreshold.setUnits(_E)
class _AdGenProcessesStarvationAlarmEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_AdGenProcessesStarvationAlarmEnable_Type.__name__=_J
_AdGenProcessesStarvationAlarmEnable_Object=MibTableColumn
adGenProcessesStarvationAlarmEnable=_AdGenProcessesStarvationAlarmEnable_Object((1,3,6,1,4,1,664,5,70,22,1,1,1,2),_AdGenProcessesStarvationAlarmEnable_Type())
adGenProcessesStarvationAlarmEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:adGenProcessesStarvationAlarmEnable.setStatus(_A)
class _AdGenProcessesDeadlockAlarmEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_AdGenProcessesDeadlockAlarmEnable_Type.__name__=_J
_AdGenProcessesDeadlockAlarmEnable_Object=MibTableColumn
adGenProcessesDeadlockAlarmEnable=_AdGenProcessesDeadlockAlarmEnable_Object((1,3,6,1,4,1,664,5,70,22,1,1,1,3),_AdGenProcessesDeadlockAlarmEnable_Type())
adGenProcessesDeadlockAlarmEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:adGenProcessesDeadlockAlarmEnable.setStatus(_A)
_AdGenProcessesStatus_ObjectIdentity=ObjectIdentity
adGenProcessesStatus=_AdGenProcessesStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,22,2))
_AdGenProcessesMemStatTable_Object=MibTable
adGenProcessesMemStatTable=_AdGenProcessesMemStatTable_Object((1,3,6,1,4,1,664,5,70,22,2,1))
if mibBuilder.loadTexts:adGenProcessesMemStatTable.setStatus(_A)
_AdGenProcessesMemStatEntry_Object=MibTableRow
adGenProcessesMemStatEntry=_AdGenProcessesMemStatEntry_Object((1,3,6,1,4,1,664,5,70,22,2,1,1))
adGenProcessesMemStatEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenProcessesMemStatEntry.setStatus(_A)
_AdGenProcessesMemStatHeapSize_Type=Unsigned32
_AdGenProcessesMemStatHeapSize_Object=MibTableColumn
adGenProcessesMemStatHeapSize=_AdGenProcessesMemStatHeapSize_Object((1,3,6,1,4,1,664,5,70,22,2,1,1,1),_AdGenProcessesMemStatHeapSize_Type())
adGenProcessesMemStatHeapSize.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesMemStatHeapSize.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesMemStatHeapSize.setUnits(_E)
_AdGenProcessesMemStatHeapUsed_Type=Unsigned32
_AdGenProcessesMemStatHeapUsed_Object=MibTableColumn
adGenProcessesMemStatHeapUsed=_AdGenProcessesMemStatHeapUsed_Object((1,3,6,1,4,1,664,5,70,22,2,1,1,2),_AdGenProcessesMemStatHeapUsed_Type())
adGenProcessesMemStatHeapUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesMemStatHeapUsed.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesMemStatHeapUsed.setUnits(_E)
_AdGenProcessesMemStatHeapFree_Type=Unsigned32
_AdGenProcessesMemStatHeapFree_Object=MibTableColumn
adGenProcessesMemStatHeapFree=_AdGenProcessesMemStatHeapFree_Object((1,3,6,1,4,1,664,5,70,22,2,1,1,3),_AdGenProcessesMemStatHeapFree_Type())
adGenProcessesMemStatHeapFree.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesMemStatHeapFree.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesMemStatHeapFree.setUnits(_E)
_AdGenProcessesMemStatBlockMgrSize_Type=Unsigned32
_AdGenProcessesMemStatBlockMgrSize_Object=MibTableColumn
adGenProcessesMemStatBlockMgrSize=_AdGenProcessesMemStatBlockMgrSize_Object((1,3,6,1,4,1,664,5,70,22,2,1,1,4),_AdGenProcessesMemStatBlockMgrSize_Type())
adGenProcessesMemStatBlockMgrSize.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesMemStatBlockMgrSize.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesMemStatBlockMgrSize.setUnits(_E)
_AdGenProcessesMemStatBlockMgrUsed_Type=Unsigned32
_AdGenProcessesMemStatBlockMgrUsed_Object=MibTableColumn
adGenProcessesMemStatBlockMgrUsed=_AdGenProcessesMemStatBlockMgrUsed_Object((1,3,6,1,4,1,664,5,70,22,2,1,1,5),_AdGenProcessesMemStatBlockMgrUsed_Type())
adGenProcessesMemStatBlockMgrUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesMemStatBlockMgrUsed.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesMemStatBlockMgrUsed.setUnits(_E)
_AdGenProcessesMemStatBlockMgrFree_Type=Unsigned32
_AdGenProcessesMemStatBlockMgrFree_Object=MibTableColumn
adGenProcessesMemStatBlockMgrFree=_AdGenProcessesMemStatBlockMgrFree_Object((1,3,6,1,4,1,664,5,70,22,2,1,1,6),_AdGenProcessesMemStatBlockMgrFree_Type())
adGenProcessesMemStatBlockMgrFree.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesMemStatBlockMgrFree.setStatus(_A)
if mibBuilder.loadTexts:adGenProcessesMemStatBlockMgrFree.setUnits(_E)
_AdGenProcessesCpuStatTable_Object=MibTable
adGenProcessesCpuStatTable=_AdGenProcessesCpuStatTable_Object((1,3,6,1,4,1,664,5,70,22,2,2))
if mibBuilder.loadTexts:adGenProcessesCpuStatTable.setStatus(_A)
_AdGenProcessesCpuStatEntry_Object=MibTableRow
adGenProcessesCpuStatEntry=_AdGenProcessesCpuStatEntry_Object((1,3,6,1,4,1,664,5,70,22,2,2,1))
adGenProcessesCpuStatEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenProcessesCpuStatEntry.setStatus(_A)
class _AdGenProcessesCpuStatCurUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AdGenProcessesCpuStatCurUtilization_Type.__name__=_J
_AdGenProcessesCpuStatCurUtilization_Object=MibTableColumn
adGenProcessesCpuStatCurUtilization=_AdGenProcessesCpuStatCurUtilization_Object((1,3,6,1,4,1,664,5,70,22,2,2,1,1),_AdGenProcessesCpuStatCurUtilization_Type())
adGenProcessesCpuStatCurUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesCpuStatCurUtilization.setStatus(_A)
class _AdGenProcessesCpuStatMaxUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AdGenProcessesCpuStatMaxUtilization_Type.__name__=_J
_AdGenProcessesCpuStatMaxUtilization_Object=MibTableColumn
adGenProcessesCpuStatMaxUtilization=_AdGenProcessesCpuStatMaxUtilization_Object((1,3,6,1,4,1,664,5,70,22,2,2,1,2),_AdGenProcessesCpuStatMaxUtilization_Type())
adGenProcessesCpuStatMaxUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenProcessesCpuStatMaxUtilization.setStatus(_A)
adGenProcessesHeapFreeThreshCrossed=NotificationType((1,3,6,1,4,1,664,5,70,22,0,1))
adGenProcessesHeapFreeThreshCrossed.setObjects(*((_F,_G),(_H,_I),(_B,_C),(_L,_P),(_L,_Q)))
if mibBuilder.loadTexts:adGenProcessesHeapFreeThreshCrossed.setStatus(_A)
adGenProcessesStarvationAlarmClr=NotificationType((1,3,6,1,4,1,664,5,70,22,0,2))
adGenProcessesStarvationAlarmClr.setObjects(*((_F,_G),(_H,_I),(_B,_C)))
if mibBuilder.loadTexts:adGenProcessesStarvationAlarmClr.setStatus(_A)
adGenProcessesStarvationAlarmAct=NotificationType((1,3,6,1,4,1,664,5,70,22,0,3))
adGenProcessesStarvationAlarmAct.setObjects(*((_F,_G),(_H,_I),(_B,_C)))
if mibBuilder.loadTexts:adGenProcessesStarvationAlarmAct.setStatus(_A)
adGenProcessesDeadlockAlarmClr=NotificationType((1,3,6,1,4,1,664,5,70,22,0,4))
adGenProcessesDeadlockAlarmClr.setObjects(*((_F,_G),(_H,_I),(_B,_C)))
if mibBuilder.loadTexts:adGenProcessesDeadlockAlarmClr.setStatus(_A)
adGenProcessesDeadlockAlarmAct=NotificationType((1,3,6,1,4,1,664,5,70,22,0,5))
adGenProcessesDeadlockAlarmAct.setObjects(*((_F,_G),(_H,_I),(_B,_C)))
if mibBuilder.loadTexts:adGenProcessesDeadlockAlarmAct.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'adGenProcessesNotifications':adGenProcessesNotifications,'adGenProcessesHeapFreeThreshCrossed':adGenProcessesHeapFreeThreshCrossed,'adGenProcessesStarvationAlarmClr':adGenProcessesStarvationAlarmClr,'adGenProcessesStarvationAlarmAct':adGenProcessesStarvationAlarmAct,'adGenProcessesDeadlockAlarmClr':adGenProcessesDeadlockAlarmClr,'adGenProcessesDeadlockAlarmAct':adGenProcessesDeadlockAlarmAct,'adGenProcessesProvisioning':adGenProcessesProvisioning,'adGenProcessesProvTable':adGenProcessesProvTable,'adGenProcessesProvEntry':adGenProcessesProvEntry,_P:adGenProcessesProvHeapFreeThreshold,'adGenProcessesStarvationAlarmEnable':adGenProcessesStarvationAlarmEnable,'adGenProcessesDeadlockAlarmEnable':adGenProcessesDeadlockAlarmEnable,'adGenProcessesStatus':adGenProcessesStatus,'adGenProcessesMemStatTable':adGenProcessesMemStatTable,'adGenProcessesMemStatEntry':adGenProcessesMemStatEntry,'adGenProcessesMemStatHeapSize':adGenProcessesMemStatHeapSize,'adGenProcessesMemStatHeapUsed':adGenProcessesMemStatHeapUsed,_Q:adGenProcessesMemStatHeapFree,'adGenProcessesMemStatBlockMgrSize':adGenProcessesMemStatBlockMgrSize,'adGenProcessesMemStatBlockMgrUsed':adGenProcessesMemStatBlockMgrUsed,'adGenProcessesMemStatBlockMgrFree':adGenProcessesMemStatBlockMgrFree,'adGenProcessesCpuStatTable':adGenProcessesCpuStatTable,'adGenProcessesCpuStatEntry':adGenProcessesCpuStatEntry,'adGenProcessesCpuStatCurUtilization':adGenProcessesCpuStatCurUtilization,'adGenProcessesCpuStatMaxUtilization':adGenProcessesCpuStatMaxUtilization,'adGenProcessesMIB':adGenProcessesMIB})