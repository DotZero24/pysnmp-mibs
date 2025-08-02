_p='tnUserInterfacePanelCpoGroup'
_o='tnUserInterfacePanelCpiGroup'
_n='tnUserInterfacePanelGroup'
_m='tnUserInterfacePanelCpoConnTo'
_l='tnUserInterfacePanelCpoContType'
_k='tnUserInterfacePanelCpoConState'
_j='tnUserInterfacePanelCpiCategory'
_i='tnUserInterfacePanelCpiPolarity'
_h='tnUserInterfacePanelCpiAlarmMsg'
_g='tnUserInterfacePanelNodeWarningLEDState'
_f='tnUserInterfacePanelNodeWarningLEDColor'
_e='tnUserInterfacePanelACO'
_d='tnUserInterfacePanelShelfLEDState'
_c='tnUserInterfacePanelShelfLEDColor'
_b='tnUserInterfacePanelNodeMinorLEDState'
_a='tnUserInterfacePanelNodeMinorLEDColor'
_Z='tnUserInterfacePanelNodeMajorLEDState'
_Y='tnUserInterfacePanelNodeMajorLEDColor'
_X='tnUserInterfacePanelNodeCriticalLEDState'
_W='tnUserInterfacePanelNodeCriticalLEDColor'
_V='tnUserInterfacePanelACOLEDState'
_U='tnUserInterfacePanelACOLEDColor'
_T='tnUserInterfacePanelMarketingPartNumber'
_S='tnUserInterfacePanelManufacturingPartNumber'
_R='tnUserInterfacePanelSerialNumber'
_Q='tnUserInterfacePanelHFD'
_P='tnUserInterfacePanelCLEI'
_O='tnUserInterfacePanelDescr'
_N='tnUserInterfacePanelName'
_M='tnUserInterfacePanelCpoIndex'
_L='not-accessible'
_K='tnUserInterfacePanelCpiIndex'
_J='Integer32'
_I='tnSlotIndex'
_H='TROPIC-SLOT-MIB'
_G='tnShelfIndex'
_F='TROPIC-SHELF-MIB'
_E='SnmpAdminString'
_D='read-create'
_C='read-only'
_B='TROPIC-ALARMPANEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnAlarmPanelMIB,tnMiscModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnAlarmPanelMIB','tnMiscModules')
tnShelfIndex,=mibBuilder.importSymbols(_F,_G)
tnSlotIndex,=mibBuilder.importSymbols(_H,_I)
TnCommand,TnTrapCategory,TropicCardCLEI,TropicCardHFD,TropicCardManufacturingPartNumber,TropicCardMarketingPartNumber,TropicCardSerialNumber,TropicLEDColorType,TropicLEDStateType=mibBuilder.importSymbols('TROPIC-TC','TnCommand','TnTrapCategory','TropicCardCLEI','TropicCardHFD','TropicCardManufacturingPartNumber','TropicCardMarketingPartNumber','TropicCardSerialNumber','TropicLEDColorType','TropicLEDStateType')
tnAlarmPanelMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,5,3))
if mibBuilder.loadTexts:tnAlarmPanelMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2014-01-13 12:00','2013-05-20 12:00','2013-03-14 12:00','2012-03-29 12:00','2010-04-16 12:00','2010-01-06 12:00','2009-09-01 12:00','2009-08-24 12:00','2009-05-21 12:00','2009-03-03 12:00','2009-02-27 12:00','2008-05-29 12:00'))
_TnAlarmPanelConf_ObjectIdentity=ObjectIdentity
tnAlarmPanelConf=_TnAlarmPanelConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,3,1))
_TnAlarmPanelGroups_ObjectIdentity=ObjectIdentity
tnAlarmPanelGroups=_TnAlarmPanelGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,3,1,1))
_TnAlarmPanelCompliances_ObjectIdentity=ObjectIdentity
tnAlarmPanelCompliances=_TnAlarmPanelCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,3,1,2))
_TnAlarmPanelObjs_ObjectIdentity=ObjectIdentity
tnAlarmPanelObjs=_TnAlarmPanelObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,3,2))
_TnAlarmPanelBasics_ObjectIdentity=ObjectIdentity
tnAlarmPanelBasics=_TnAlarmPanelBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,3,2,1))
_TnUserInterfacePanelTable_Object=MibTable
tnUserInterfacePanelTable=_TnUserInterfacePanelTable_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3))
if mibBuilder.loadTexts:tnUserInterfacePanelTable.setStatus(_A)
_TnUserInterfacePanelEntry_Object=MibTableRow
tnUserInterfacePanelEntry=_TnUserInterfacePanelEntry_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1))
tnUserInterfacePanelEntry.setIndexNames((0,_F,_G),(0,_H,_I))
if mibBuilder.loadTexts:tnUserInterfacePanelEntry.setStatus(_A)
class _TnUserInterfacePanelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TnUserInterfacePanelName_Type.__name__=_E
_TnUserInterfacePanelName_Object=MibTableColumn
tnUserInterfacePanelName=_TnUserInterfacePanelName_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,1),_TnUserInterfacePanelName_Type())
tnUserInterfacePanelName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelName.setStatus(_A)
class _TnUserInterfacePanelDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnUserInterfacePanelDescr_Type.__name__=_E
_TnUserInterfacePanelDescr_Object=MibTableColumn
tnUserInterfacePanelDescr=_TnUserInterfacePanelDescr_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,2),_TnUserInterfacePanelDescr_Type())
tnUserInterfacePanelDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelDescr.setStatus(_A)
_TnUserInterfacePanelCLEI_Type=TropicCardCLEI
_TnUserInterfacePanelCLEI_Object=MibTableColumn
tnUserInterfacePanelCLEI=_TnUserInterfacePanelCLEI_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,3),_TnUserInterfacePanelCLEI_Type())
tnUserInterfacePanelCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelCLEI.setStatus(_A)
_TnUserInterfacePanelHFD_Type=TropicCardHFD
_TnUserInterfacePanelHFD_Object=MibTableColumn
tnUserInterfacePanelHFD=_TnUserInterfacePanelHFD_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,4),_TnUserInterfacePanelHFD_Type())
tnUserInterfacePanelHFD.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelHFD.setStatus(_A)
_TnUserInterfacePanelSerialNumber_Type=TropicCardSerialNumber
_TnUserInterfacePanelSerialNumber_Object=MibTableColumn
tnUserInterfacePanelSerialNumber=_TnUserInterfacePanelSerialNumber_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,5),_TnUserInterfacePanelSerialNumber_Type())
tnUserInterfacePanelSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelSerialNumber.setStatus(_A)
_TnUserInterfacePanelManufacturingPartNumber_Type=TropicCardManufacturingPartNumber
_TnUserInterfacePanelManufacturingPartNumber_Object=MibTableColumn
tnUserInterfacePanelManufacturingPartNumber=_TnUserInterfacePanelManufacturingPartNumber_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,6),_TnUserInterfacePanelManufacturingPartNumber_Type())
tnUserInterfacePanelManufacturingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelManufacturingPartNumber.setStatus(_A)
_TnUserInterfacePanelMarketingPartNumber_Type=TropicCardMarketingPartNumber
_TnUserInterfacePanelMarketingPartNumber_Object=MibTableColumn
tnUserInterfacePanelMarketingPartNumber=_TnUserInterfacePanelMarketingPartNumber_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,7),_TnUserInterfacePanelMarketingPartNumber_Type())
tnUserInterfacePanelMarketingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelMarketingPartNumber.setStatus(_A)
_TnUserInterfacePanelACOLEDColor_Type=TropicLEDColorType
_TnUserInterfacePanelACOLEDColor_Object=MibTableColumn
tnUserInterfacePanelACOLEDColor=_TnUserInterfacePanelACOLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,8),_TnUserInterfacePanelACOLEDColor_Type())
tnUserInterfacePanelACOLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelACOLEDColor.setStatus(_A)
_TnUserInterfacePanelACOLEDState_Type=TropicLEDStateType
_TnUserInterfacePanelACOLEDState_Object=MibTableColumn
tnUserInterfacePanelACOLEDState=_TnUserInterfacePanelACOLEDState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,9),_TnUserInterfacePanelACOLEDState_Type())
tnUserInterfacePanelACOLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelACOLEDState.setStatus(_A)
_TnUserInterfacePanelNodeCriticalLEDColor_Type=TropicLEDColorType
_TnUserInterfacePanelNodeCriticalLEDColor_Object=MibTableColumn
tnUserInterfacePanelNodeCriticalLEDColor=_TnUserInterfacePanelNodeCriticalLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,10),_TnUserInterfacePanelNodeCriticalLEDColor_Type())
tnUserInterfacePanelNodeCriticalLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeCriticalLEDColor.setStatus(_A)
_TnUserInterfacePanelNodeCriticalLEDState_Type=TropicLEDStateType
_TnUserInterfacePanelNodeCriticalLEDState_Object=MibTableColumn
tnUserInterfacePanelNodeCriticalLEDState=_TnUserInterfacePanelNodeCriticalLEDState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,11),_TnUserInterfacePanelNodeCriticalLEDState_Type())
tnUserInterfacePanelNodeCriticalLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeCriticalLEDState.setStatus(_A)
_TnUserInterfacePanelNodeMajorLEDColor_Type=TropicLEDColorType
_TnUserInterfacePanelNodeMajorLEDColor_Object=MibTableColumn
tnUserInterfacePanelNodeMajorLEDColor=_TnUserInterfacePanelNodeMajorLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,12),_TnUserInterfacePanelNodeMajorLEDColor_Type())
tnUserInterfacePanelNodeMajorLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeMajorLEDColor.setStatus(_A)
_TnUserInterfacePanelNodeMajorLEDState_Type=TropicLEDStateType
_TnUserInterfacePanelNodeMajorLEDState_Object=MibTableColumn
tnUserInterfacePanelNodeMajorLEDState=_TnUserInterfacePanelNodeMajorLEDState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,13),_TnUserInterfacePanelNodeMajorLEDState_Type())
tnUserInterfacePanelNodeMajorLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeMajorLEDState.setStatus(_A)
_TnUserInterfacePanelNodeMinorLEDColor_Type=TropicLEDColorType
_TnUserInterfacePanelNodeMinorLEDColor_Object=MibTableColumn
tnUserInterfacePanelNodeMinorLEDColor=_TnUserInterfacePanelNodeMinorLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,14),_TnUserInterfacePanelNodeMinorLEDColor_Type())
tnUserInterfacePanelNodeMinorLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeMinorLEDColor.setStatus(_A)
_TnUserInterfacePanelNodeMinorLEDState_Type=TropicLEDStateType
_TnUserInterfacePanelNodeMinorLEDState_Object=MibTableColumn
tnUserInterfacePanelNodeMinorLEDState=_TnUserInterfacePanelNodeMinorLEDState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,15),_TnUserInterfacePanelNodeMinorLEDState_Type())
tnUserInterfacePanelNodeMinorLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeMinorLEDState.setStatus(_A)
_TnUserInterfacePanelShelfLEDColor_Type=TropicLEDColorType
_TnUserInterfacePanelShelfLEDColor_Object=MibTableColumn
tnUserInterfacePanelShelfLEDColor=_TnUserInterfacePanelShelfLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,16),_TnUserInterfacePanelShelfLEDColor_Type())
tnUserInterfacePanelShelfLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelShelfLEDColor.setStatus(_A)
_TnUserInterfacePanelShelfLEDState_Type=TropicLEDStateType
_TnUserInterfacePanelShelfLEDState_Object=MibTableColumn
tnUserInterfacePanelShelfLEDState=_TnUserInterfacePanelShelfLEDState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,17),_TnUserInterfacePanelShelfLEDState_Type())
tnUserInterfacePanelShelfLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelShelfLEDState.setStatus(_A)
_TnUserInterfacePanelACO_Type=TnCommand
_TnUserInterfacePanelACO_Object=MibTableColumn
tnUserInterfacePanelACO=_TnUserInterfacePanelACO_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,18),_TnUserInterfacePanelACO_Type())
tnUserInterfacePanelACO.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelACO.setStatus(_A)
_TnUserInterfacePanelNodeWarningLEDColor_Type=TropicLEDColorType
_TnUserInterfacePanelNodeWarningLEDColor_Object=MibTableColumn
tnUserInterfacePanelNodeWarningLEDColor=_TnUserInterfacePanelNodeWarningLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,19),_TnUserInterfacePanelNodeWarningLEDColor_Type())
tnUserInterfacePanelNodeWarningLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeWarningLEDColor.setStatus(_A)
_TnUserInterfacePanelNodeWarningLEDState_Type=TropicLEDStateType
_TnUserInterfacePanelNodeWarningLEDState_Object=MibTableColumn
tnUserInterfacePanelNodeWarningLEDState=_TnUserInterfacePanelNodeWarningLEDState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,3,1,20),_TnUserInterfacePanelNodeWarningLEDState_Type())
tnUserInterfacePanelNodeWarningLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnUserInterfacePanelNodeWarningLEDState.setStatus(_A)
_TnUserInterfacePanelCpiTable_Object=MibTable
tnUserInterfacePanelCpiTable=_TnUserInterfacePanelCpiTable_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,4))
if mibBuilder.loadTexts:tnUserInterfacePanelCpiTable.setStatus(_A)
_TnUserInterfacePanelCpiEntry_Object=MibTableRow
tnUserInterfacePanelCpiEntry=_TnUserInterfacePanelCpiEntry_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,4,1))
tnUserInterfacePanelCpiEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_B,_K))
if mibBuilder.loadTexts:tnUserInterfacePanelCpiEntry.setStatus(_A)
_TnUserInterfacePanelCpiIndex_Type=Unsigned32
_TnUserInterfacePanelCpiIndex_Object=MibTableColumn
tnUserInterfacePanelCpiIndex=_TnUserInterfacePanelCpiIndex_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,4,1,1),_TnUserInterfacePanelCpiIndex_Type())
tnUserInterfacePanelCpiIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:tnUserInterfacePanelCpiIndex.setStatus(_A)
class _TnUserInterfacePanelCpiAlarmMsg_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,56))
_TnUserInterfacePanelCpiAlarmMsg_Type.__name__=_E
_TnUserInterfacePanelCpiAlarmMsg_Object=MibTableColumn
tnUserInterfacePanelCpiAlarmMsg=_TnUserInterfacePanelCpiAlarmMsg_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,4,1,3),_TnUserInterfacePanelCpiAlarmMsg_Type())
tnUserInterfacePanelCpiAlarmMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelCpiAlarmMsg.setStatus(_A)
class _TnUserInterfacePanelCpiPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alow',1),('ahigh',2)))
_TnUserInterfacePanelCpiPolarity_Type.__name__=_J
_TnUserInterfacePanelCpiPolarity_Object=MibTableColumn
tnUserInterfacePanelCpiPolarity=_TnUserInterfacePanelCpiPolarity_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,4,1,4),_TnUserInterfacePanelCpiPolarity_Type())
tnUserInterfacePanelCpiPolarity.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelCpiPolarity.setStatus(_A)
_TnUserInterfacePanelCpiCategory_Type=TnTrapCategory
_TnUserInterfacePanelCpiCategory_Object=MibTableColumn
tnUserInterfacePanelCpiCategory=_TnUserInterfacePanelCpiCategory_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,4,1,5),_TnUserInterfacePanelCpiCategory_Type())
tnUserInterfacePanelCpiCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelCpiCategory.setStatus(_A)
_TnUserInterfacePanelCpoTable_Object=MibTable
tnUserInterfacePanelCpoTable=_TnUserInterfacePanelCpoTable_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,5))
if mibBuilder.loadTexts:tnUserInterfacePanelCpoTable.setStatus(_A)
_TnUserInterfacePanelCpoEntry_Object=MibTableRow
tnUserInterfacePanelCpoEntry=_TnUserInterfacePanelCpoEntry_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,5,1))
tnUserInterfacePanelCpoEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_B,_M))
if mibBuilder.loadTexts:tnUserInterfacePanelCpoEntry.setStatus(_A)
_TnUserInterfacePanelCpoIndex_Type=Unsigned32
_TnUserInterfacePanelCpoIndex_Object=MibTableColumn
tnUserInterfacePanelCpoIndex=_TnUserInterfacePanelCpoIndex_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,5,1,1),_TnUserInterfacePanelCpoIndex_Type())
tnUserInterfacePanelCpoIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:tnUserInterfacePanelCpoIndex.setStatus(_A)
class _TnUserInterfacePanelCpoConState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rls',1),('opr',2),('auto',3),('racklamp',4)))
_TnUserInterfacePanelCpoConState_Type.__name__=_J
_TnUserInterfacePanelCpoConState_Object=MibTableColumn
tnUserInterfacePanelCpoConState=_TnUserInterfacePanelCpoConState_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,5,1,2),_TnUserInterfacePanelCpoConState_Type())
tnUserInterfacePanelCpoConState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelCpoConState.setStatus(_A)
class _TnUserInterfacePanelCpoContType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,56))
_TnUserInterfacePanelCpoContType_Type.__name__=_E
_TnUserInterfacePanelCpoContType_Object=MibTableColumn
tnUserInterfacePanelCpoContType=_TnUserInterfacePanelCpoContType_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,5,1,3),_TnUserInterfacePanelCpoContType_Type())
tnUserInterfacePanelCpoContType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelCpoContType.setStatus(_A)
_TnUserInterfacePanelCpoConnTo_Type=InterfaceIndexOrZero
_TnUserInterfacePanelCpoConnTo_Object=MibTableColumn
tnUserInterfacePanelCpoConnTo=_TnUserInterfacePanelCpoConnTo_Object((1,3,6,1,4,1,7483,2,2,5,3,2,1,5,1,5),_TnUserInterfacePanelCpoConnTo_Type())
tnUserInterfacePanelCpoConnTo.setMaxAccess(_D)
if mibBuilder.loadTexts:tnUserInterfacePanelCpoConnTo.setStatus(_A)
tnUserInterfacePanelGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,5,3,1,1,3))
tnUserInterfacePanelGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:tnUserInterfacePanelGroup.setStatus(_A)
tnUserInterfacePanelCpiGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,5,3,1,1,4))
tnUserInterfacePanelCpiGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:tnUserInterfacePanelCpiGroup.setStatus(_A)
tnUserInterfacePanelCpoGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,5,3,1,1,5))
tnUserInterfacePanelCpoGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:tnUserInterfacePanelCpoGroup.setStatus(_A)
tnAlarmPanelCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,5,3,1,2,1))
tnAlarmPanelCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:tnAlarmPanelCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnAlarmPanelMibModule':tnAlarmPanelMibModule,'tnAlarmPanelConf':tnAlarmPanelConf,'tnAlarmPanelGroups':tnAlarmPanelGroups,_n:tnUserInterfacePanelGroup,_o:tnUserInterfacePanelCpiGroup,_p:tnUserInterfacePanelCpoGroup,'tnAlarmPanelCompliances':tnAlarmPanelCompliances,'tnAlarmPanelCompliance':tnAlarmPanelCompliance,'tnAlarmPanelObjs':tnAlarmPanelObjs,'tnAlarmPanelBasics':tnAlarmPanelBasics,'tnUserInterfacePanelTable':tnUserInterfacePanelTable,'tnUserInterfacePanelEntry':tnUserInterfacePanelEntry,_N:tnUserInterfacePanelName,_O:tnUserInterfacePanelDescr,_P:tnUserInterfacePanelCLEI,_Q:tnUserInterfacePanelHFD,_R:tnUserInterfacePanelSerialNumber,_S:tnUserInterfacePanelManufacturingPartNumber,_T:tnUserInterfacePanelMarketingPartNumber,_U:tnUserInterfacePanelACOLEDColor,_V:tnUserInterfacePanelACOLEDState,_W:tnUserInterfacePanelNodeCriticalLEDColor,_X:tnUserInterfacePanelNodeCriticalLEDState,_Y:tnUserInterfacePanelNodeMajorLEDColor,_Z:tnUserInterfacePanelNodeMajorLEDState,_a:tnUserInterfacePanelNodeMinorLEDColor,_b:tnUserInterfacePanelNodeMinorLEDState,_c:tnUserInterfacePanelShelfLEDColor,_d:tnUserInterfacePanelShelfLEDState,_e:tnUserInterfacePanelACO,_f:tnUserInterfacePanelNodeWarningLEDColor,_g:tnUserInterfacePanelNodeWarningLEDState,'tnUserInterfacePanelCpiTable':tnUserInterfacePanelCpiTable,'tnUserInterfacePanelCpiEntry':tnUserInterfacePanelCpiEntry,_K:tnUserInterfacePanelCpiIndex,_h:tnUserInterfacePanelCpiAlarmMsg,_i:tnUserInterfacePanelCpiPolarity,_j:tnUserInterfacePanelCpiCategory,'tnUserInterfacePanelCpoTable':tnUserInterfacePanelCpoTable,'tnUserInterfacePanelCpoEntry':tnUserInterfacePanelCpoEntry,_M:tnUserInterfacePanelCpoIndex,_k:tnUserInterfacePanelCpoConState,_l:tnUserInterfacePanelCpoContType,_m:tnUserInterfacePanelCpoConnTo})