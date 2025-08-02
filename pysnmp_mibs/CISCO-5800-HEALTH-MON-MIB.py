_m='cisco5800HealthMonMIBGroup'
_l='ciscoHealthMonEnableNotification'
_k='ciscoHealthMonNumUnavailableModems'
_j='ciscoHealthMonNumModemsInUse'
_i='ciscoHealthMonNumTotalModems'
_h='ciscoHealthMonNumTotalDS0'
_g='ciscoHealthMonNumActiveDS0'
_f='ciscoHealthMonNumT1E1LinesDown'
_e='ciscoHealthMonNumT1E1LinesUp'
_d='ciscoHealthMonNumShelves'
_c='ciscoHealthMonShelfLastUpdate'
_b='ciscoHealthMonUtilEgressOutOctet'
_a='ciscoHealthMonUtilEgressInOctet'
_Z='ciscoHealthMonCPUavgBusy5'
_Y='ciscoHealthMonIOMemFree'
_X='ciscoHealthMonIOMemUsed'
_W='ciscoHealthMonUnavailableModems'
_V='ciscoHealthMonModemsInUse'
_U='ciscoHealthMonTotalModems'
_T='ciscoHealthMonTotalDS0'
_S='ciscoHealthMonActiveDS0'
_R='ciscoHealthMonT1E1LinesDown'
_Q='ciscoHealthMonT1E1LinesUp'
_P='ciscoHealthMonThresholdExceedCount'
_O='ciscoHealthMonCountIndex'
_N='not-accessible'
_M='ciscoHealthMonStatusIndex'
_L='TruthValue'
_K='ciscoHealthMonThreshold'
_J='ciscoHealthMonValue'
_I='ciscoHealthMonDescr'
_H='ciscoHealthMonAddress'
_G='ciscoHealthMonShelfId'
_F='DisplayString'
_E='ciscoHealthMonStatusType'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-5800-HEALTH-MON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_L)
cisco5800HealthMonMIB=ModuleIdentity((1,3,6,1,4,1,9,10,28))
_Cisco5800HealthMonObjects_ObjectIdentity=ObjectIdentity
cisco5800HealthMonObjects=_Cisco5800HealthMonObjects_ObjectIdentity((1,3,6,1,4,1,9,10,28,1))
_CiscoHealthMonStatusTable_Object=MibTable
ciscoHealthMonStatusTable=_CiscoHealthMonStatusTable_Object((1,3,6,1,4,1,9,10,28,1,1))
if mibBuilder.loadTexts:ciscoHealthMonStatusTable.setStatus(_B)
_CiscoHealthMonStatusEntry_Object=MibTableRow
ciscoHealthMonStatusEntry=_CiscoHealthMonStatusEntry_Object((1,3,6,1,4,1,9,10,28,1,1,1))
ciscoHealthMonStatusEntry.setIndexNames((0,_A,_M),(0,_A,_E))
if mibBuilder.loadTexts:ciscoHealthMonStatusEntry.setStatus(_B)
class _CiscoHealthMonStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoHealthMonStatusIndex_Type.__name__=_D
_CiscoHealthMonStatusIndex_Object=MibTableColumn
ciscoHealthMonStatusIndex=_CiscoHealthMonStatusIndex_Object((1,3,6,1,4,1,9,10,28,1,1,1,1),_CiscoHealthMonStatusIndex_Type())
ciscoHealthMonStatusIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoHealthMonStatusIndex.setStatus(_B)
class _CiscoHealthMonStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CiscoHealthMonStatusType_Type.__name__=_D
_CiscoHealthMonStatusType_Object=MibTableColumn
ciscoHealthMonStatusType=_CiscoHealthMonStatusType_Object((1,3,6,1,4,1,9,10,28,1,1,1,2),_CiscoHealthMonStatusType_Type())
ciscoHealthMonStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonStatusType.setStatus(_B)
_CiscoHealthMonShelfId_Type=Integer32
_CiscoHealthMonShelfId_Object=MibTableColumn
ciscoHealthMonShelfId=_CiscoHealthMonShelfId_Object((1,3,6,1,4,1,9,10,28,1,1,1,3),_CiscoHealthMonShelfId_Type())
ciscoHealthMonShelfId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonShelfId.setStatus(_B)
_CiscoHealthMonAddress_Type=IpAddress
_CiscoHealthMonAddress_Object=MibTableColumn
ciscoHealthMonAddress=_CiscoHealthMonAddress_Object((1,3,6,1,4,1,9,10,28,1,1,1,4),_CiscoHealthMonAddress_Type())
ciscoHealthMonAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonAddress.setStatus(_B)
class _CiscoHealthMonDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoHealthMonDescr_Type.__name__=_F
_CiscoHealthMonDescr_Object=MibTableColumn
ciscoHealthMonDescr=_CiscoHealthMonDescr_Object((1,3,6,1,4,1,9,10,28,1,1,1,5),_CiscoHealthMonDescr_Type())
ciscoHealthMonDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonDescr.setStatus(_B)
_CiscoHealthMonValue_Type=Gauge32
_CiscoHealthMonValue_Object=MibTableColumn
ciscoHealthMonValue=_CiscoHealthMonValue_Object((1,3,6,1,4,1,9,10,28,1,1,1,6),_CiscoHealthMonValue_Type())
ciscoHealthMonValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonValue.setStatus(_B)
class _CiscoHealthMonThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoHealthMonThreshold_Type.__name__=_D
_CiscoHealthMonThreshold_Object=MibTableColumn
ciscoHealthMonThreshold=_CiscoHealthMonThreshold_Object((1,3,6,1,4,1,9,10,28,1,1,1,7),_CiscoHealthMonThreshold_Type())
ciscoHealthMonThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonThreshold.setStatus(_B)
_CiscoHealthMonThresholdExceedCount_Type=Integer32
_CiscoHealthMonThresholdExceedCount_Object=MibTableColumn
ciscoHealthMonThresholdExceedCount=_CiscoHealthMonThresholdExceedCount_Object((1,3,6,1,4,1,9,10,28,1,1,1,8),_CiscoHealthMonThresholdExceedCount_Type())
ciscoHealthMonThresholdExceedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonThresholdExceedCount.setStatus(_B)
_CiscoHealthMonCountTable_Object=MibTable
ciscoHealthMonCountTable=_CiscoHealthMonCountTable_Object((1,3,6,1,4,1,9,10,28,1,2))
if mibBuilder.loadTexts:ciscoHealthMonCountTable.setStatus(_B)
_CiscoHealthMonCountEntry_Object=MibTableRow
ciscoHealthMonCountEntry=_CiscoHealthMonCountEntry_Object((1,3,6,1,4,1,9,10,28,1,2,1))
ciscoHealthMonCountEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:ciscoHealthMonCountEntry.setStatus(_B)
class _CiscoHealthMonCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CiscoHealthMonCountIndex_Type.__name__=_D
_CiscoHealthMonCountIndex_Object=MibTableColumn
ciscoHealthMonCountIndex=_CiscoHealthMonCountIndex_Object((1,3,6,1,4,1,9,10,28,1,2,1,1),_CiscoHealthMonCountIndex_Type())
ciscoHealthMonCountIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoHealthMonCountIndex.setStatus(_B)
_CiscoHealthMonT1E1LinesUp_Type=Gauge32
_CiscoHealthMonT1E1LinesUp_Object=MibTableColumn
ciscoHealthMonT1E1LinesUp=_CiscoHealthMonT1E1LinesUp_Object((1,3,6,1,4,1,9,10,28,1,2,1,2),_CiscoHealthMonT1E1LinesUp_Type())
ciscoHealthMonT1E1LinesUp.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonT1E1LinesUp.setStatus(_B)
_CiscoHealthMonT1E1LinesDown_Type=Gauge32
_CiscoHealthMonT1E1LinesDown_Object=MibTableColumn
ciscoHealthMonT1E1LinesDown=_CiscoHealthMonT1E1LinesDown_Object((1,3,6,1,4,1,9,10,28,1,2,1,3),_CiscoHealthMonT1E1LinesDown_Type())
ciscoHealthMonT1E1LinesDown.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonT1E1LinesDown.setStatus(_B)
_CiscoHealthMonActiveDS0_Type=Gauge32
_CiscoHealthMonActiveDS0_Object=MibTableColumn
ciscoHealthMonActiveDS0=_CiscoHealthMonActiveDS0_Object((1,3,6,1,4,1,9,10,28,1,2,1,4),_CiscoHealthMonActiveDS0_Type())
ciscoHealthMonActiveDS0.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonActiveDS0.setStatus(_B)
_CiscoHealthMonTotalDS0_Type=Gauge32
_CiscoHealthMonTotalDS0_Object=MibTableColumn
ciscoHealthMonTotalDS0=_CiscoHealthMonTotalDS0_Object((1,3,6,1,4,1,9,10,28,1,2,1,5),_CiscoHealthMonTotalDS0_Type())
ciscoHealthMonTotalDS0.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonTotalDS0.setStatus(_B)
_CiscoHealthMonTotalModems_Type=Gauge32
_CiscoHealthMonTotalModems_Object=MibTableColumn
ciscoHealthMonTotalModems=_CiscoHealthMonTotalModems_Object((1,3,6,1,4,1,9,10,28,1,2,1,6),_CiscoHealthMonTotalModems_Type())
ciscoHealthMonTotalModems.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonTotalModems.setStatus(_B)
_CiscoHealthMonModemsInUse_Type=Gauge32
_CiscoHealthMonModemsInUse_Object=MibTableColumn
ciscoHealthMonModemsInUse=_CiscoHealthMonModemsInUse_Object((1,3,6,1,4,1,9,10,28,1,2,1,7),_CiscoHealthMonModemsInUse_Type())
ciscoHealthMonModemsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonModemsInUse.setStatus(_B)
_CiscoHealthMonUnavailableModems_Type=Gauge32
_CiscoHealthMonUnavailableModems_Object=MibTableColumn
ciscoHealthMonUnavailableModems=_CiscoHealthMonUnavailableModems_Object((1,3,6,1,4,1,9,10,28,1,2,1,8),_CiscoHealthMonUnavailableModems_Type())
ciscoHealthMonUnavailableModems.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonUnavailableModems.setStatus(_B)
_CiscoHealthMonIOMemUsed_Type=Gauge32
_CiscoHealthMonIOMemUsed_Object=MibTableColumn
ciscoHealthMonIOMemUsed=_CiscoHealthMonIOMemUsed_Object((1,3,6,1,4,1,9,10,28,1,2,1,9),_CiscoHealthMonIOMemUsed_Type())
ciscoHealthMonIOMemUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonIOMemUsed.setStatus(_B)
if mibBuilder.loadTexts:ciscoHealthMonIOMemUsed.setUnits('bytes')
_CiscoHealthMonIOMemFree_Type=Gauge32
_CiscoHealthMonIOMemFree_Object=MibTableColumn
ciscoHealthMonIOMemFree=_CiscoHealthMonIOMemFree_Object((1,3,6,1,4,1,9,10,28,1,2,1,10),_CiscoHealthMonIOMemFree_Type())
ciscoHealthMonIOMemFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonIOMemFree.setStatus(_B)
if mibBuilder.loadTexts:ciscoHealthMonIOMemFree.setUnits('bytes')
class _CiscoHealthMonCPUavgBusy5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoHealthMonCPUavgBusy5_Type.__name__=_D
_CiscoHealthMonCPUavgBusy5_Object=MibTableColumn
ciscoHealthMonCPUavgBusy5=_CiscoHealthMonCPUavgBusy5_Object((1,3,6,1,4,1,9,10,28,1,2,1,11),_CiscoHealthMonCPUavgBusy5_Type())
ciscoHealthMonCPUavgBusy5.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonCPUavgBusy5.setStatus(_B)
_CiscoHealthMonUtilEgressInOctet_Type=Counter32
_CiscoHealthMonUtilEgressInOctet_Object=MibTableColumn
ciscoHealthMonUtilEgressInOctet=_CiscoHealthMonUtilEgressInOctet_Object((1,3,6,1,4,1,9,10,28,1,2,1,12),_CiscoHealthMonUtilEgressInOctet_Type())
ciscoHealthMonUtilEgressInOctet.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonUtilEgressInOctet.setStatus(_B)
_CiscoHealthMonUtilEgressOutOctet_Type=Counter32
_CiscoHealthMonUtilEgressOutOctet_Object=MibTableColumn
ciscoHealthMonUtilEgressOutOctet=_CiscoHealthMonUtilEgressOutOctet_Object((1,3,6,1,4,1,9,10,28,1,2,1,13),_CiscoHealthMonUtilEgressOutOctet_Type())
ciscoHealthMonUtilEgressOutOctet.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonUtilEgressOutOctet.setStatus(_B)
class _CiscoHealthMonShelfLastUpdate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoHealthMonShelfLastUpdate_Type.__name__=_F
_CiscoHealthMonShelfLastUpdate_Object=MibTableColumn
ciscoHealthMonShelfLastUpdate=_CiscoHealthMonShelfLastUpdate_Object((1,3,6,1,4,1,9,10,28,1,2,1,14),_CiscoHealthMonShelfLastUpdate_Type())
ciscoHealthMonShelfLastUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonShelfLastUpdate.setStatus(_B)
_CiscoHealthMonNumShelves_Type=Integer32
_CiscoHealthMonNumShelves_Object=MibScalar
ciscoHealthMonNumShelves=_CiscoHealthMonNumShelves_Object((1,3,6,1,4,1,9,10,28,1,3),_CiscoHealthMonNumShelves_Type())
ciscoHealthMonNumShelves.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumShelves.setStatus(_B)
_CiscoHealthMonNumT1E1LinesUp_Type=Gauge32
_CiscoHealthMonNumT1E1LinesUp_Object=MibScalar
ciscoHealthMonNumT1E1LinesUp=_CiscoHealthMonNumT1E1LinesUp_Object((1,3,6,1,4,1,9,10,28,1,4),_CiscoHealthMonNumT1E1LinesUp_Type())
ciscoHealthMonNumT1E1LinesUp.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumT1E1LinesUp.setStatus(_B)
_CiscoHealthMonNumT1E1LinesDown_Type=Gauge32
_CiscoHealthMonNumT1E1LinesDown_Object=MibScalar
ciscoHealthMonNumT1E1LinesDown=_CiscoHealthMonNumT1E1LinesDown_Object((1,3,6,1,4,1,9,10,28,1,5),_CiscoHealthMonNumT1E1LinesDown_Type())
ciscoHealthMonNumT1E1LinesDown.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumT1E1LinesDown.setStatus(_B)
_CiscoHealthMonNumActiveDS0_Type=Gauge32
_CiscoHealthMonNumActiveDS0_Object=MibScalar
ciscoHealthMonNumActiveDS0=_CiscoHealthMonNumActiveDS0_Object((1,3,6,1,4,1,9,10,28,1,6),_CiscoHealthMonNumActiveDS0_Type())
ciscoHealthMonNumActiveDS0.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumActiveDS0.setStatus(_B)
_CiscoHealthMonNumTotalDS0_Type=Gauge32
_CiscoHealthMonNumTotalDS0_Object=MibScalar
ciscoHealthMonNumTotalDS0=_CiscoHealthMonNumTotalDS0_Object((1,3,6,1,4,1,9,10,28,1,7),_CiscoHealthMonNumTotalDS0_Type())
ciscoHealthMonNumTotalDS0.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumTotalDS0.setStatus(_B)
_CiscoHealthMonNumTotalModems_Type=Gauge32
_CiscoHealthMonNumTotalModems_Object=MibScalar
ciscoHealthMonNumTotalModems=_CiscoHealthMonNumTotalModems_Object((1,3,6,1,4,1,9,10,28,1,8),_CiscoHealthMonNumTotalModems_Type())
ciscoHealthMonNumTotalModems.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumTotalModems.setStatus(_B)
_CiscoHealthMonNumModemsInUse_Type=Gauge32
_CiscoHealthMonNumModemsInUse_Object=MibScalar
ciscoHealthMonNumModemsInUse=_CiscoHealthMonNumModemsInUse_Object((1,3,6,1,4,1,9,10,28,1,9),_CiscoHealthMonNumModemsInUse_Type())
ciscoHealthMonNumModemsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumModemsInUse.setStatus(_B)
_CiscoHealthMonNumUnavailableModems_Type=Gauge32
_CiscoHealthMonNumUnavailableModems_Object=MibScalar
ciscoHealthMonNumUnavailableModems=_CiscoHealthMonNumUnavailableModems_Object((1,3,6,1,4,1,9,10,28,1,10),_CiscoHealthMonNumUnavailableModems_Type())
ciscoHealthMonNumUnavailableModems.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonNumUnavailableModems.setStatus(_B)
_CiscoHealthMonMIBNotificationEnables_ObjectIdentity=ObjectIdentity
ciscoHealthMonMIBNotificationEnables=_CiscoHealthMonMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9,10,28,2))
class _CiscoHealthMonEnableNotification_Type(TruthValue):defaultValue=2
_CiscoHealthMonEnableNotification_Type.__name__=_L
_CiscoHealthMonEnableNotification_Object=MibScalar
ciscoHealthMonEnableNotification=_CiscoHealthMonEnableNotification_Object((1,3,6,1,4,1,9,10,28,2,1),_CiscoHealthMonEnableNotification_Type())
ciscoHealthMonEnableNotification.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciscoHealthMonEnableNotification.setStatus(_B)
_CiscoHealthMonMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoHealthMonMIBNotificationPrefix=_CiscoHealthMonMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,28,3))
_CiscoHealthMonMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoHealthMonMIBNotifications=_CiscoHealthMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,28,3,0))
_Cisco5800HealthMonMIBConformance_ObjectIdentity=ObjectIdentity
cisco5800HealthMonMIBConformance=_Cisco5800HealthMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,28,4))
_Cisco5800HealthMonMIBCompliances_ObjectIdentity=ObjectIdentity
cisco5800HealthMonMIBCompliances=_Cisco5800HealthMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,28,4,1))
_Cisco5800HealthMonMIBGroups_ObjectIdentity=ObjectIdentity
cisco5800HealthMonMIBGroups=_Cisco5800HealthMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,28,4,2))
cisco5800HealthMonMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,28,4,2,1))
cisco5800HealthMonMIBGroup.setObjects(*((_A,_E),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cisco5800HealthMonMIBGroup.setStatus(_B)
ciscoHealthMonNotification=NotificationType((1,3,6,1,4,1,9,10,28,3,0,1))
ciscoHealthMonNotification.setObjects(*((_A,_E),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoHealthMonNotification.setStatus(_B)
cisco5800HealthMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,28,4,1,1))
cisco5800HealthMonMIBCompliance.setObjects((_A,_m))
if mibBuilder.loadTexts:cisco5800HealthMonMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cisco5800HealthMonMIB':cisco5800HealthMonMIB,'cisco5800HealthMonObjects':cisco5800HealthMonObjects,'ciscoHealthMonStatusTable':ciscoHealthMonStatusTable,'ciscoHealthMonStatusEntry':ciscoHealthMonStatusEntry,_M:ciscoHealthMonStatusIndex,_E:ciscoHealthMonStatusType,_G:ciscoHealthMonShelfId,_H:ciscoHealthMonAddress,_I:ciscoHealthMonDescr,_J:ciscoHealthMonValue,_K:ciscoHealthMonThreshold,_P:ciscoHealthMonThresholdExceedCount,'ciscoHealthMonCountTable':ciscoHealthMonCountTable,'ciscoHealthMonCountEntry':ciscoHealthMonCountEntry,_O:ciscoHealthMonCountIndex,_Q:ciscoHealthMonT1E1LinesUp,_R:ciscoHealthMonT1E1LinesDown,_S:ciscoHealthMonActiveDS0,_T:ciscoHealthMonTotalDS0,_U:ciscoHealthMonTotalModems,_V:ciscoHealthMonModemsInUse,_W:ciscoHealthMonUnavailableModems,_X:ciscoHealthMonIOMemUsed,_Y:ciscoHealthMonIOMemFree,_Z:ciscoHealthMonCPUavgBusy5,_a:ciscoHealthMonUtilEgressInOctet,_b:ciscoHealthMonUtilEgressOutOctet,_c:ciscoHealthMonShelfLastUpdate,_d:ciscoHealthMonNumShelves,_e:ciscoHealthMonNumT1E1LinesUp,_f:ciscoHealthMonNumT1E1LinesDown,_g:ciscoHealthMonNumActiveDS0,_h:ciscoHealthMonNumTotalDS0,_i:ciscoHealthMonNumTotalModems,_j:ciscoHealthMonNumModemsInUse,_k:ciscoHealthMonNumUnavailableModems,'ciscoHealthMonMIBNotificationEnables':ciscoHealthMonMIBNotificationEnables,_l:ciscoHealthMonEnableNotification,'ciscoHealthMonMIBNotificationPrefix':ciscoHealthMonMIBNotificationPrefix,'ciscoHealthMonMIBNotifications':ciscoHealthMonMIBNotifications,'ciscoHealthMonNotification':ciscoHealthMonNotification,'cisco5800HealthMonMIBConformance':cisco5800HealthMonMIBConformance,'cisco5800HealthMonMIBCompliances':cisco5800HealthMonMIBCompliances,'cisco5800HealthMonMIBCompliance':cisco5800HealthMonMIBCompliance,'cisco5800HealthMonMIBGroups':cisco5800HealthMonMIBGroups,_m:cisco5800HealthMonMIBGroup})