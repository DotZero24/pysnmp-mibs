_U='qtechRedundancyMIBGroup'
_T='qtechPluggableModuleAction'
_S='qtechPluggableModuleOnlinePortsNum'
_R='qtechPluggableModuleConfigPortsNum'
_Q='qtechPluggableModuleOnlineInfoDescr'
_P='qtechPluggableModuleConfigInfoDescr'
_O='qtechPluggableModuleOnlineSwVer'
_N='qtechPluggableModuleConfigSwVer'
_M='qtechPluggableModuleConfigType'
_L='qtechPluggableModuleStatus'
_K='qtechMainCPU'
_J='qtechRedundancyForceSwitchover'
_I='none'
_H='qtechPluggableModuleInfoSlotIndex'
_G='qtechPluggableModuleInfoDeviceIndex'
_F='read-write'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='QTECH-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
qtechRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,34))
if mibBuilder.loadTexts:qtechRedundancyMIB.setRevisions(('2003-09-20 00:00',))
_QtechRedundancyMIBObjects_ObjectIdentity=ObjectIdentity
qtechRedundancyMIBObjects=_QtechRedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,34,1))
_QtechRedundancyForceSwitchover_Type=Integer32
_QtechRedundancyForceSwitchover_Object=MibScalar
qtechRedundancyForceSwitchover=_QtechRedundancyForceSwitchover_Object((1,3,6,1,4,1,27514,1,1,10,2,34,1,1),_QtechRedundancyForceSwitchover_Type())
qtechRedundancyForceSwitchover.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechRedundancyForceSwitchover.setStatus(_A)
class _QtechMainCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('increasing',0),('decreasing',1)))
_QtechMainCPU_Type.__name__=_D
_QtechMainCPU_Object=MibScalar
qtechMainCPU=_QtechMainCPU_Object((1,3,6,1,4,1,27514,1,1,10,2,34,1,2),_QtechMainCPU_Type())
qtechMainCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMainCPU.setStatus(_A)
_QtechPluggableMIBObjects_ObjectIdentity=ObjectIdentity
qtechPluggableMIBObjects=_QtechPluggableMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,34,2))
_QtechPluggableModuleInfoTable_Object=MibTable
qtechPluggableModuleInfoTable=_QtechPluggableModuleInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1))
if mibBuilder.loadTexts:qtechPluggableModuleInfoTable.setStatus(_A)
_QtechPluggableModuleInfoEntry_Object=MibTableRow
qtechPluggableModuleInfoEntry=_QtechPluggableModuleInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1))
qtechPluggableModuleInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:qtechPluggableModuleInfoEntry.setStatus(_A)
_QtechPluggableModuleInfoDeviceIndex_Type=Integer32
_QtechPluggableModuleInfoDeviceIndex_Object=MibTableColumn
qtechPluggableModuleInfoDeviceIndex=_QtechPluggableModuleInfoDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,1),_QtechPluggableModuleInfoDeviceIndex_Type())
qtechPluggableModuleInfoDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleInfoDeviceIndex.setStatus(_A)
_QtechPluggableModuleInfoSlotIndex_Type=Integer32
_QtechPluggableModuleInfoSlotIndex_Object=MibTableColumn
qtechPluggableModuleInfoSlotIndex=_QtechPluggableModuleInfoSlotIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,2),_QtechPluggableModuleInfoSlotIndex_Type())
qtechPluggableModuleInfoSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleInfoSlotIndex.setStatus(_A)
class _QtechPluggableModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,0),('ok',1),('installed',2),('conflict',3),('removed',4),('uninstalled',5),('verIncompatible',6),('cannot-qtechup',7),('resetting',8),('master',9),('backup',10)))
_QtechPluggableModuleStatus_Type.__name__=_D
_QtechPluggableModuleStatus_Object=MibTableColumn
qtechPluggableModuleStatus=_QtechPluggableModuleStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,3),_QtechPluggableModuleStatus_Type())
qtechPluggableModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleStatus.setStatus(_A)
class _QtechPluggableModuleConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,0),('m6800-24T-4SFP-4GT',1),('m6800-32T-4SFP-GT',2),('m6800-32FMT',3),('m6800-12GB',4),('m6800-24SFP',5),('m6800-12SFP-GT',6),('m6800-1XENPAK',7),('m6800-2XENPAK',8),('m6800-MSC',9),('m6800-CM',10),('m6800-24GT-8SFP',11)))
_QtechPluggableModuleConfigType_Type.__name__=_D
_QtechPluggableModuleConfigType_Object=MibTableColumn
qtechPluggableModuleConfigType=_QtechPluggableModuleConfigType_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,4),_QtechPluggableModuleConfigType_Type())
qtechPluggableModuleConfigType.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechPluggableModuleConfigType.setStatus(_A)
class _QtechPluggableModuleConfigSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechPluggableModuleConfigSwVer_Type.__name__=_E
_QtechPluggableModuleConfigSwVer_Object=MibTableColumn
qtechPluggableModuleConfigSwVer=_QtechPluggableModuleConfigSwVer_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,5),_QtechPluggableModuleConfigSwVer_Type())
qtechPluggableModuleConfigSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleConfigSwVer.setStatus(_A)
class _QtechPluggableModuleOnlineSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechPluggableModuleOnlineSwVer_Type.__name__=_E
_QtechPluggableModuleOnlineSwVer_Object=MibTableColumn
qtechPluggableModuleOnlineSwVer=_QtechPluggableModuleOnlineSwVer_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,6),_QtechPluggableModuleOnlineSwVer_Type())
qtechPluggableModuleOnlineSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleOnlineSwVer.setStatus(_A)
class _QtechPluggableModuleConfigInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechPluggableModuleConfigInfoDescr_Type.__name__=_E
_QtechPluggableModuleConfigInfoDescr_Object=MibTableColumn
qtechPluggableModuleConfigInfoDescr=_QtechPluggableModuleConfigInfoDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,7),_QtechPluggableModuleConfigInfoDescr_Type())
qtechPluggableModuleConfigInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleConfigInfoDescr.setStatus(_A)
class _QtechPluggableModuleOnlineInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechPluggableModuleOnlineInfoDescr_Type.__name__=_E
_QtechPluggableModuleOnlineInfoDescr_Object=MibTableColumn
qtechPluggableModuleOnlineInfoDescr=_QtechPluggableModuleOnlineInfoDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,8),_QtechPluggableModuleOnlineInfoDescr_Type())
qtechPluggableModuleOnlineInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleOnlineInfoDescr.setStatus(_A)
_QtechPluggableModuleConfigPortsNum_Type=Integer32
_QtechPluggableModuleConfigPortsNum_Object=MibTableColumn
qtechPluggableModuleConfigPortsNum=_QtechPluggableModuleConfigPortsNum_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,9),_QtechPluggableModuleConfigPortsNum_Type())
qtechPluggableModuleConfigPortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleConfigPortsNum.setStatus(_A)
_QtechPluggableModuleOnlinePortsNum_Type=Integer32
_QtechPluggableModuleOnlinePortsNum_Object=MibTableColumn
qtechPluggableModuleOnlinePortsNum=_QtechPluggableModuleOnlinePortsNum_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,10),_QtechPluggableModuleOnlinePortsNum_Type())
qtechPluggableModuleOnlinePortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPluggableModuleOnlinePortsNum.setStatus(_A)
class _QtechPluggableModuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('reset',1),('clearAllConf',2),('uninstall',3)))
_QtechPluggableModuleAction_Type.__name__=_D
_QtechPluggableModuleAction_Object=MibTableColumn
qtechPluggableModuleAction=_QtechPluggableModuleAction_Object((1,3,6,1,4,1,27514,1,1,10,2,34,2,1,1,11),_QtechPluggableModuleAction_Type())
qtechPluggableModuleAction.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechPluggableModuleAction.setStatus(_A)
_QtechRedundancyMIBConformance_ObjectIdentity=ObjectIdentity
qtechRedundancyMIBConformance=_QtechRedundancyMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,34,3))
_QtechRedundancyMIBCompliances_ObjectIdentity=ObjectIdentity
qtechRedundancyMIBCompliances=_QtechRedundancyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,34,3,1))
_QtechRedundancyMIBGroups_ObjectIdentity=ObjectIdentity
qtechRedundancyMIBGroups=_QtechRedundancyMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,34,3,2))
qtechRedundancyMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,34,3,2,1))
qtechRedundancyMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_G),(_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:qtechRedundancyMIBGroup.setStatus(_A)
qtechRedundancyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,34,3,1,1))
qtechRedundancyMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:qtechRedundancyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechRedundancyMIB':qtechRedundancyMIB,'qtechRedundancyMIBObjects':qtechRedundancyMIBObjects,_J:qtechRedundancyForceSwitchover,_K:qtechMainCPU,'qtechPluggableMIBObjects':qtechPluggableMIBObjects,'qtechPluggableModuleInfoTable':qtechPluggableModuleInfoTable,'qtechPluggableModuleInfoEntry':qtechPluggableModuleInfoEntry,_G:qtechPluggableModuleInfoDeviceIndex,_H:qtechPluggableModuleInfoSlotIndex,_L:qtechPluggableModuleStatus,_M:qtechPluggableModuleConfigType,_N:qtechPluggableModuleConfigSwVer,_O:qtechPluggableModuleOnlineSwVer,_P:qtechPluggableModuleConfigInfoDescr,_Q:qtechPluggableModuleOnlineInfoDescr,_R:qtechPluggableModuleConfigPortsNum,_S:qtechPluggableModuleOnlinePortsNum,_T:qtechPluggableModuleAction,'qtechRedundancyMIBConformance':qtechRedundancyMIBConformance,'qtechRedundancyMIBCompliances':qtechRedundancyMIBCompliances,'qtechRedundancyMIBCompliance':qtechRedundancyMIBCompliance,'qtechRedundancyMIBGroups':qtechRedundancyMIBGroups,_U:qtechRedundancyMIBGroup})