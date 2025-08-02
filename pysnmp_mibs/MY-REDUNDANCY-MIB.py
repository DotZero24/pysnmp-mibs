_U='myRedundancyMIBGroup'
_T='myPluggableModuleAction'
_S='myPluggableModuleOnlinePortsNum'
_R='myPluggableModuleConfigPortsNum'
_Q='myPluggableModuleOnlineInfoDescr'
_P='myPluggableModuleConfigInfoDescr'
_O='myPluggableModuleOnlineSwVer'
_N='myPluggableModuleConfigSwVer'
_M='myPluggableModuleConfigType'
_L='myPluggableModuleStatus'
_K='myMainCPU'
_J='myRedundancyForceSwitchover'
_I='none'
_H='myPluggableModuleInfoSlotIndex'
_G='myPluggableModuleInfoDeviceIndex'
_F='read-write'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='MY-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
myRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,34))
if mibBuilder.loadTexts:myRedundancyMIB.setRevisions(('2003-09-20 00:00',))
_MyRedundancyMIBObjects_ObjectIdentity=ObjectIdentity
myRedundancyMIBObjects=_MyRedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,34,1))
_MyRedundancyForceSwitchover_Type=Integer32
_MyRedundancyForceSwitchover_Object=MibScalar
myRedundancyForceSwitchover=_MyRedundancyForceSwitchover_Object((1,3,6,1,4,1,4881,1,1,10,2,34,1,1),_MyRedundancyForceSwitchover_Type())
myRedundancyForceSwitchover.setMaxAccess(_F)
if mibBuilder.loadTexts:myRedundancyForceSwitchover.setStatus(_A)
class _MyMainCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('increasing',0),('decreasing',1)))
_MyMainCPU_Type.__name__=_D
_MyMainCPU_Object=MibScalar
myMainCPU=_MyMainCPU_Object((1,3,6,1,4,1,4881,1,1,10,2,34,1,2),_MyMainCPU_Type())
myMainCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:myMainCPU.setStatus(_A)
_MyPluggableMIBObjects_ObjectIdentity=ObjectIdentity
myPluggableMIBObjects=_MyPluggableMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,34,2))
_MyPluggableModuleInfoTable_Object=MibTable
myPluggableModuleInfoTable=_MyPluggableModuleInfoTable_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1))
if mibBuilder.loadTexts:myPluggableModuleInfoTable.setStatus(_A)
_MyPluggableModuleInfoEntry_Object=MibTableRow
myPluggableModuleInfoEntry=_MyPluggableModuleInfoEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1))
myPluggableModuleInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:myPluggableModuleInfoEntry.setStatus(_A)
_MyPluggableModuleInfoDeviceIndex_Type=Integer32
_MyPluggableModuleInfoDeviceIndex_Object=MibTableColumn
myPluggableModuleInfoDeviceIndex=_MyPluggableModuleInfoDeviceIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,1),_MyPluggableModuleInfoDeviceIndex_Type())
myPluggableModuleInfoDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleInfoDeviceIndex.setStatus(_A)
_MyPluggableModuleInfoSlotIndex_Type=Integer32
_MyPluggableModuleInfoSlotIndex_Object=MibTableColumn
myPluggableModuleInfoSlotIndex=_MyPluggableModuleInfoSlotIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,2),_MyPluggableModuleInfoSlotIndex_Type())
myPluggableModuleInfoSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleInfoSlotIndex.setStatus(_A)
class _MyPluggableModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,0),('ok',1),('installed',2),('conflict',3),('removed',4),('uninstalled',5),('verIncompatible',6),('cannot-myup',7),('resetting',8),('master',9),('backup',10)))
_MyPluggableModuleStatus_Type.__name__=_D
_MyPluggableModuleStatus_Object=MibTableColumn
myPluggableModuleStatus=_MyPluggableModuleStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,3),_MyPluggableModuleStatus_Type())
myPluggableModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleStatus.setStatus(_A)
class _MyPluggableModuleConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,0),('m6800-24T-4SFP-4GT',1),('m6800-32T-4SFP-GT',2),('m6800-32FMT',3),('m6800-12GB',4),('m6800-24SFP',5),('m6800-12SFP-GT',6),('m6800-1XENPAK',7),('m6800-2XENPAK',8),('m6800-MSC',9),('m6800-CM',10),('m6800-24GT-8SFP',11)))
_MyPluggableModuleConfigType_Type.__name__=_D
_MyPluggableModuleConfigType_Object=MibTableColumn
myPluggableModuleConfigType=_MyPluggableModuleConfigType_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,4),_MyPluggableModuleConfigType_Type())
myPluggableModuleConfigType.setMaxAccess(_F)
if mibBuilder.loadTexts:myPluggableModuleConfigType.setStatus(_A)
class _MyPluggableModuleConfigSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyPluggableModuleConfigSwVer_Type.__name__=_E
_MyPluggableModuleConfigSwVer_Object=MibTableColumn
myPluggableModuleConfigSwVer=_MyPluggableModuleConfigSwVer_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,5),_MyPluggableModuleConfigSwVer_Type())
myPluggableModuleConfigSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleConfigSwVer.setStatus(_A)
class _MyPluggableModuleOnlineSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyPluggableModuleOnlineSwVer_Type.__name__=_E
_MyPluggableModuleOnlineSwVer_Object=MibTableColumn
myPluggableModuleOnlineSwVer=_MyPluggableModuleOnlineSwVer_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,6),_MyPluggableModuleOnlineSwVer_Type())
myPluggableModuleOnlineSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleOnlineSwVer.setStatus(_A)
class _MyPluggableModuleConfigInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyPluggableModuleConfigInfoDescr_Type.__name__=_E
_MyPluggableModuleConfigInfoDescr_Object=MibTableColumn
myPluggableModuleConfigInfoDescr=_MyPluggableModuleConfigInfoDescr_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,7),_MyPluggableModuleConfigInfoDescr_Type())
myPluggableModuleConfigInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleConfigInfoDescr.setStatus(_A)
class _MyPluggableModuleOnlineInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyPluggableModuleOnlineInfoDescr_Type.__name__=_E
_MyPluggableModuleOnlineInfoDescr_Object=MibTableColumn
myPluggableModuleOnlineInfoDescr=_MyPluggableModuleOnlineInfoDescr_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,8),_MyPluggableModuleOnlineInfoDescr_Type())
myPluggableModuleOnlineInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleOnlineInfoDescr.setStatus(_A)
_MyPluggableModuleConfigPortsNum_Type=Integer32
_MyPluggableModuleConfigPortsNum_Object=MibTableColumn
myPluggableModuleConfigPortsNum=_MyPluggableModuleConfigPortsNum_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,9),_MyPluggableModuleConfigPortsNum_Type())
myPluggableModuleConfigPortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleConfigPortsNum.setStatus(_A)
_MyPluggableModuleOnlinePortsNum_Type=Integer32
_MyPluggableModuleOnlinePortsNum_Object=MibTableColumn
myPluggableModuleOnlinePortsNum=_MyPluggableModuleOnlinePortsNum_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,10),_MyPluggableModuleOnlinePortsNum_Type())
myPluggableModuleOnlinePortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:myPluggableModuleOnlinePortsNum.setStatus(_A)
class _MyPluggableModuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('reset',1),('clearAllConf',2),('uninstall',3)))
_MyPluggableModuleAction_Type.__name__=_D
_MyPluggableModuleAction_Object=MibTableColumn
myPluggableModuleAction=_MyPluggableModuleAction_Object((1,3,6,1,4,1,4881,1,1,10,2,34,2,1,1,11),_MyPluggableModuleAction_Type())
myPluggableModuleAction.setMaxAccess(_F)
if mibBuilder.loadTexts:myPluggableModuleAction.setStatus(_A)
_MyRedundancyMIBConformance_ObjectIdentity=ObjectIdentity
myRedundancyMIBConformance=_MyRedundancyMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,34,3))
_MyRedundancyMIBCompliances_ObjectIdentity=ObjectIdentity
myRedundancyMIBCompliances=_MyRedundancyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,34,3,1))
_MyRedundancyMIBGroups_ObjectIdentity=ObjectIdentity
myRedundancyMIBGroups=_MyRedundancyMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,34,3,2))
myRedundancyMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,34,3,2,1))
myRedundancyMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_G),(_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:myRedundancyMIBGroup.setStatus(_A)
myRedundancyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,34,3,1,1))
myRedundancyMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:myRedundancyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myRedundancyMIB':myRedundancyMIB,'myRedundancyMIBObjects':myRedundancyMIBObjects,_J:myRedundancyForceSwitchover,_K:myMainCPU,'myPluggableMIBObjects':myPluggableMIBObjects,'myPluggableModuleInfoTable':myPluggableModuleInfoTable,'myPluggableModuleInfoEntry':myPluggableModuleInfoEntry,_G:myPluggableModuleInfoDeviceIndex,_H:myPluggableModuleInfoSlotIndex,_L:myPluggableModuleStatus,_M:myPluggableModuleConfigType,_N:myPluggableModuleConfigSwVer,_O:myPluggableModuleOnlineSwVer,_P:myPluggableModuleConfigInfoDescr,_Q:myPluggableModuleOnlineInfoDescr,_R:myPluggableModuleConfigPortsNum,_S:myPluggableModuleOnlinePortsNum,_T:myPluggableModuleAction,'myRedundancyMIBConformance':myRedundancyMIBConformance,'myRedundancyMIBCompliances':myRedundancyMIBCompliances,'myRedundancyMIBCompliance':myRedundancyMIBCompliance,'myRedundancyMIBGroups':myRedundancyMIBGroups,_U:myRedundancyMIBGroup})