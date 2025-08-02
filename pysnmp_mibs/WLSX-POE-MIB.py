_d='wlsxPoEMIBNotificationsGroup'
_c='wlsxPoEMIBMainPseGroup'
_b='wlsxPoEMIBPortGroup'
_a='wlsxTrapInterfacePoEState'
_Z='wlsxPseSlotPoEManagementMode'
_Y='wlsxPseSlotGuardBand'
_X='wlsxPseSlotPowerConsumption'
_W='wlsxPseSlotPowerAvailable'
_V='wlsxPsePortCurrent'
_U='wlsxPsePortVoltage'
_T='wlsxPsePortPowerConsumed'
_S='wlsxPsePortPowerAllocated'
_R='wlsxPsePortDefaultPowerMax'
_Q='wlsxPsePortPriority'
_P='wlsxPsePortPdClass'
_O='wlsxPsePortIsIeeePd'
_N='wlsxPsePortIsPdDetected'
_M='wlsxPsePortDiscoveryMode'
_L='wlsxPsePortAdminStatus'
_K='wlsxPseSlotIndex'
_J='unknown'
_I='not-accessible'
_H='wlsxPsePortStatus'
_G='wlsxPsePortState'
_F='milliwatts'
_E='wlsxPsePortIndex'
_D='Integer32'
_C='read-only'
_B='WLSX-POE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
wlsxPoEMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,18))
if mibBuilder.loadTexts:wlsxPoEMIB.setRevisions(('2011-05-16 00:00',))
_WlsxPoEMIBNotifications_ObjectIdentity=ObjectIdentity
wlsxPoEMIBNotifications=_WlsxPoEMIBNotifications_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,18,0))
_WlsxPoEMIBObjects_ObjectIdentity=ObjectIdentity
wlsxPoEMIBObjects=_WlsxPoEMIBObjects_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,18,1))
_WlsxPsePortTable_Object=MibTable
wlsxPsePortTable=_WlsxPsePortTable_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1))
if mibBuilder.loadTexts:wlsxPsePortTable.setStatus(_A)
_WlsxPsePortEntry_Object=MibTableRow
wlsxPsePortEntry=_WlsxPsePortEntry_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1))
wlsxPsePortEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:wlsxPsePortEntry.setStatus(_A)
_WlsxPsePortIndex_Type=Integer32
_WlsxPsePortIndex_Object=MibTableColumn
wlsxPsePortIndex=_WlsxPsePortIndex_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,1),_WlsxPsePortIndex_Type())
wlsxPsePortIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wlsxPsePortIndex.setStatus(_A)
class _WlsxPsePortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WlsxPsePortAdminStatus_Type.__name__=_D
_WlsxPsePortAdminStatus_Object=MibTableColumn
wlsxPsePortAdminStatus=_WlsxPsePortAdminStatus_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,2),_WlsxPsePortAdminStatus_Type())
wlsxPsePortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortAdminStatus.setStatus(_A)
class _WlsxPsePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WlsxPsePortState_Type.__name__=_D
_WlsxPsePortState_Object=MibTableColumn
wlsxPsePortState=_WlsxPsePortState_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,3),_WlsxPsePortState_Type())
wlsxPsePortState.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortState.setStatus(_A)
class _WlsxPsePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),('offAdmin',2),('offPowerManagement',3),('offIllegalClass',4),('offDetectionProgress',5),('offHardwareError',6),('offNonStandardPd',7)))
_WlsxPsePortStatus_Type.__name__=_D
_WlsxPsePortStatus_Object=MibTableColumn
wlsxPsePortStatus=_WlsxPsePortStatus_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,4),_WlsxPsePortStatus_Type())
wlsxPsePortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortStatus.setStatus(_A)
class _WlsxPsePortDiscoveryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('off',1),('ieee',2),('cisco',3)))
_WlsxPsePortDiscoveryMode_Type.__name__=_D
_WlsxPsePortDiscoveryMode_Object=MibTableColumn
wlsxPsePortDiscoveryMode=_WlsxPsePortDiscoveryMode_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,5),_WlsxPsePortDiscoveryMode_Type())
wlsxPsePortDiscoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortDiscoveryMode.setStatus(_A)
_WlsxPsePortIsPdDetected_Type=TruthValue
_WlsxPsePortIsPdDetected_Object=MibTableColumn
wlsxPsePortIsPdDetected=_WlsxPsePortIsPdDetected_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,6),_WlsxPsePortIsPdDetected_Type())
wlsxPsePortIsPdDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortIsPdDetected.setStatus(_A)
_WlsxPsePortIsIeeePd_Type=TruthValue
_WlsxPsePortIsIeeePd_Object=MibTableColumn
wlsxPsePortIsIeeePd=_WlsxPsePortIsIeeePd_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,7),_WlsxPsePortIsIeeePd_Type())
wlsxPsePortIsIeeePd.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortIsIeeePd.setStatus(_A)
class _WlsxPsePortPdClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unknownClass',0),('class0',1),('class1',2),('class2',3),('class3',4),('class4',5)))
_WlsxPsePortPdClass_Type.__name__=_D
_WlsxPsePortPdClass_Object=MibTableColumn
wlsxPsePortPdClass=_WlsxPsePortPdClass_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,8),_WlsxPsePortPdClass_Type())
wlsxPsePortPdClass.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortPdClass.setStatus(_A)
class _WlsxPsePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('high',2),('critical',3)))
_WlsxPsePortPriority_Type.__name__=_D
_WlsxPsePortPriority_Object=MibTableColumn
wlsxPsePortPriority=_WlsxPsePortPriority_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,9),_WlsxPsePortPriority_Type())
wlsxPsePortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortPriority.setStatus(_A)
_WlsxPsePortDefaultPowerMax_Type=Integer32
_WlsxPsePortDefaultPowerMax_Object=MibTableColumn
wlsxPsePortDefaultPowerMax=_WlsxPsePortDefaultPowerMax_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,10),_WlsxPsePortDefaultPowerMax_Type())
wlsxPsePortDefaultPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortDefaultPowerMax.setStatus(_A)
if mibBuilder.loadTexts:wlsxPsePortDefaultPowerMax.setUnits(_F)
_WlsxPsePortPowerAllocated_Type=Integer32
_WlsxPsePortPowerAllocated_Object=MibTableColumn
wlsxPsePortPowerAllocated=_WlsxPsePortPowerAllocated_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,11),_WlsxPsePortPowerAllocated_Type())
wlsxPsePortPowerAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortPowerAllocated.setStatus(_A)
if mibBuilder.loadTexts:wlsxPsePortPowerAllocated.setUnits(_F)
_WlsxPsePortPowerConsumed_Type=Integer32
_WlsxPsePortPowerConsumed_Object=MibTableColumn
wlsxPsePortPowerConsumed=_WlsxPsePortPowerConsumed_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,12),_WlsxPsePortPowerConsumed_Type())
wlsxPsePortPowerConsumed.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortPowerConsumed.setStatus(_A)
if mibBuilder.loadTexts:wlsxPsePortPowerConsumed.setUnits(_F)
_WlsxPsePortVoltage_Type=Integer32
_WlsxPsePortVoltage_Object=MibTableColumn
wlsxPsePortVoltage=_WlsxPsePortVoltage_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,13),_WlsxPsePortVoltage_Type())
wlsxPsePortVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortVoltage.setStatus(_A)
if mibBuilder.loadTexts:wlsxPsePortVoltage.setUnits('milliVolts')
_WlsxPsePortCurrent_Type=Integer32
_WlsxPsePortCurrent_Object=MibTableColumn
wlsxPsePortCurrent=_WlsxPsePortCurrent_Object((1,3,6,1,4,1,14823,2,2,1,18,1,1,1,14),_WlsxPsePortCurrent_Type())
wlsxPsePortCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPsePortCurrent.setStatus(_A)
if mibBuilder.loadTexts:wlsxPsePortCurrent.setUnits('milliAmps')
_WlsxPseSlotTable_Object=MibTable
wlsxPseSlotTable=_WlsxPseSlotTable_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2))
if mibBuilder.loadTexts:wlsxPseSlotTable.setStatus(_A)
_WlsxPseSlotEntry_Object=MibTableRow
wlsxPseSlotEntry=_WlsxPseSlotEntry_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2,1))
wlsxPseSlotEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:wlsxPseSlotEntry.setStatus(_A)
_WlsxPseSlotIndex_Type=Integer32
_WlsxPseSlotIndex_Object=MibTableColumn
wlsxPseSlotIndex=_WlsxPseSlotIndex_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2,1,1),_WlsxPseSlotIndex_Type())
wlsxPseSlotIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wlsxPseSlotIndex.setStatus(_A)
_WlsxPseSlotPowerAvailable_Type=Integer32
_WlsxPseSlotPowerAvailable_Object=MibTableColumn
wlsxPseSlotPowerAvailable=_WlsxPseSlotPowerAvailable_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2,1,2),_WlsxPseSlotPowerAvailable_Type())
wlsxPseSlotPowerAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPseSlotPowerAvailable.setStatus(_A)
if mibBuilder.loadTexts:wlsxPseSlotPowerAvailable.setUnits('watts')
_WlsxPseSlotPowerConsumption_Type=Integer32
_WlsxPseSlotPowerConsumption_Object=MibTableColumn
wlsxPseSlotPowerConsumption=_WlsxPseSlotPowerConsumption_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2,1,3),_WlsxPseSlotPowerConsumption_Type())
wlsxPseSlotPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPseSlotPowerConsumption.setStatus(_A)
if mibBuilder.loadTexts:wlsxPseSlotPowerConsumption.setUnits('watts')
_WlsxPseSlotGuardBand_Type=Integer32
_WlsxPseSlotGuardBand_Object=MibTableColumn
wlsxPseSlotGuardBand=_WlsxPseSlotGuardBand_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2,1,4),_WlsxPseSlotGuardBand_Type())
wlsxPseSlotGuardBand.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPseSlotGuardBand.setStatus(_A)
class _WlsxPseSlotPoEManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('static',2),('class',3)))
_WlsxPseSlotPoEManagementMode_Type.__name__=_D
_WlsxPseSlotPoEManagementMode_Object=MibTableColumn
wlsxPseSlotPoEManagementMode=_WlsxPseSlotPoEManagementMode_Object((1,3,6,1,4,1,14823,2,2,1,18,1,2,1,5),_WlsxPseSlotPoEManagementMode_Type())
wlsxPseSlotPoEManagementMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wlsxPseSlotPoEManagementMode.setStatus(_A)
_WlsxPoEMIBConformance_ObjectIdentity=ObjectIdentity
wlsxPoEMIBConformance=_WlsxPoEMIBConformance_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,18,2))
_WlsxPoEMIBCompliances_ObjectIdentity=ObjectIdentity
wlsxPoEMIBCompliances=_WlsxPoEMIBCompliances_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,18,2,1))
_WlsxPoEMIBGroups_ObjectIdentity=ObjectIdentity
wlsxPoEMIBGroups=_WlsxPoEMIBGroups_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,18,2,2))
wlsxPoEMIBPortGroup=ObjectGroup((1,3,6,1,4,1,14823,2,2,1,18,2,2,1))
wlsxPoEMIBPortGroup.setObjects(*((_B,_L),(_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:wlsxPoEMIBPortGroup.setStatus(_A)
wlsxPoEMIBMainPseGroup=ObjectGroup((1,3,6,1,4,1,14823,2,2,1,18,2,2,2))
wlsxPoEMIBMainPseGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:wlsxPoEMIBMainPseGroup.setStatus(_A)
wlsxTrapInterfacePoEState=NotificationType((1,3,6,1,4,1,14823,2,2,1,18,0,1))
wlsxTrapInterfacePoEState.setObjects(*((_B,_E),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:wlsxTrapInterfacePoEState.setStatus(_A)
wlsxPoEMIBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,14823,2,2,1,18,2,2,3))
wlsxPoEMIBNotificationsGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:wlsxPoEMIBNotificationsGroup.setStatus(_A)
wlsxPoEMIBCompliance=ModuleCompliance((1,3,6,1,4,1,14823,2,2,1,18,2,1,1))
wlsxPoEMIBCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:wlsxPoEMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'wlsxPoEMIB':wlsxPoEMIB,'wlsxPoEMIBNotifications':wlsxPoEMIBNotifications,_a:wlsxTrapInterfacePoEState,'wlsxPoEMIBObjects':wlsxPoEMIBObjects,'wlsxPsePortTable':wlsxPsePortTable,'wlsxPsePortEntry':wlsxPsePortEntry,_E:wlsxPsePortIndex,_L:wlsxPsePortAdminStatus,_G:wlsxPsePortState,_H:wlsxPsePortStatus,_M:wlsxPsePortDiscoveryMode,_N:wlsxPsePortIsPdDetected,_O:wlsxPsePortIsIeeePd,_P:wlsxPsePortPdClass,_Q:wlsxPsePortPriority,_R:wlsxPsePortDefaultPowerMax,_S:wlsxPsePortPowerAllocated,_T:wlsxPsePortPowerConsumed,_U:wlsxPsePortVoltage,_V:wlsxPsePortCurrent,'wlsxPseSlotTable':wlsxPseSlotTable,'wlsxPseSlotEntry':wlsxPseSlotEntry,_K:wlsxPseSlotIndex,_W:wlsxPseSlotPowerAvailable,_X:wlsxPseSlotPowerConsumption,_Y:wlsxPseSlotGuardBand,_Z:wlsxPseSlotPoEManagementMode,'wlsxPoEMIBConformance':wlsxPoEMIBConformance,'wlsxPoEMIBCompliances':wlsxPoEMIBCompliances,'wlsxPoEMIBCompliance':wlsxPoEMIBCompliance,'wlsxPoEMIBGroups':wlsxPoEMIBGroups,_b:wlsxPoEMIBPortGroup,_c:wlsxPoEMIBMainPseGroup,_d:wlsxPoEMIBNotificationsGroup})