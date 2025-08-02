_U='fsRedundancyMIBGroup'
_T='fsPluggableModuleAction'
_S='fsPluggableModuleOnlinePortsNum'
_R='fsPluggableModuleConfigPortsNum'
_Q='fsPluggableModuleOnlineInfoDescr'
_P='fsPluggableModuleConfigInfoDescr'
_O='fsPluggableModuleOnlineSwVer'
_N='fsPluggableModuleConfigSwVer'
_M='fsPluggableModuleConfigType'
_L='fsPluggableModuleStatus'
_K='fsMainCPU'
_J='fsRedundancyForceSwitchover'
_I='none'
_H='fsPluggableModuleInfoSlotIndex'
_G='fsPluggableModuleInfoDeviceIndex'
_F='read-write'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='FS-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
fsRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,34))
if mibBuilder.loadTexts:fsRedundancyMIB.setRevisions(('2003-09-20 00:00',))
_FsRedundancyMIBObjects_ObjectIdentity=ObjectIdentity
fsRedundancyMIBObjects=_FsRedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,34,1))
_FsRedundancyForceSwitchover_Type=Integer32
_FsRedundancyForceSwitchover_Object=MibScalar
fsRedundancyForceSwitchover=_FsRedundancyForceSwitchover_Object((1,3,6,1,4,1,52642,1,1,10,2,34,1,1),_FsRedundancyForceSwitchover_Type())
fsRedundancyForceSwitchover.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRedundancyForceSwitchover.setStatus(_A)
class _FsMainCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('increasing',0),('decreasing',1)))
_FsMainCPU_Type.__name__=_D
_FsMainCPU_Object=MibScalar
fsMainCPU=_FsMainCPU_Object((1,3,6,1,4,1,52642,1,1,10,2,34,1,2),_FsMainCPU_Type())
fsMainCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMainCPU.setStatus(_A)
_FsPluggableMIBObjects_ObjectIdentity=ObjectIdentity
fsPluggableMIBObjects=_FsPluggableMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,34,2))
_FsPluggableModuleInfoTable_Object=MibTable
fsPluggableModuleInfoTable=_FsPluggableModuleInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1))
if mibBuilder.loadTexts:fsPluggableModuleInfoTable.setStatus(_A)
_FsPluggableModuleInfoEntry_Object=MibTableRow
fsPluggableModuleInfoEntry=_FsPluggableModuleInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1))
fsPluggableModuleInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:fsPluggableModuleInfoEntry.setStatus(_A)
_FsPluggableModuleInfoDeviceIndex_Type=Integer32
_FsPluggableModuleInfoDeviceIndex_Object=MibTableColumn
fsPluggableModuleInfoDeviceIndex=_FsPluggableModuleInfoDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,1),_FsPluggableModuleInfoDeviceIndex_Type())
fsPluggableModuleInfoDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleInfoDeviceIndex.setStatus(_A)
_FsPluggableModuleInfoSlotIndex_Type=Integer32
_FsPluggableModuleInfoSlotIndex_Object=MibTableColumn
fsPluggableModuleInfoSlotIndex=_FsPluggableModuleInfoSlotIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,2),_FsPluggableModuleInfoSlotIndex_Type())
fsPluggableModuleInfoSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleInfoSlotIndex.setStatus(_A)
class _FsPluggableModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,0),('ok',1),('installed',2),('conflict',3),('removed',4),('uninstalled',5),('verIncompatible',6),('cannot-fsup',7),('resetting',8),('master',9),('backup',10)))
_FsPluggableModuleStatus_Type.__name__=_D
_FsPluggableModuleStatus_Object=MibTableColumn
fsPluggableModuleStatus=_FsPluggableModuleStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,3),_FsPluggableModuleStatus_Type())
fsPluggableModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleStatus.setStatus(_A)
class _FsPluggableModuleConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,0),('m6800-24T-4SFP-4GT',1),('m6800-32T-4SFP-GT',2),('m6800-32FMT',3),('m6800-12GB',4),('m6800-24SFP',5),('m6800-12SFP-GT',6),('m6800-1XENPAK',7),('m6800-2XENPAK',8),('m6800-MSC',9),('m6800-CM',10),('m6800-24GT-8SFP',11)))
_FsPluggableModuleConfigType_Type.__name__=_D
_FsPluggableModuleConfigType_Object=MibTableColumn
fsPluggableModuleConfigType=_FsPluggableModuleConfigType_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,4),_FsPluggableModuleConfigType_Type())
fsPluggableModuleConfigType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPluggableModuleConfigType.setStatus(_A)
class _FsPluggableModuleConfigSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsPluggableModuleConfigSwVer_Type.__name__=_E
_FsPluggableModuleConfigSwVer_Object=MibTableColumn
fsPluggableModuleConfigSwVer=_FsPluggableModuleConfigSwVer_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,5),_FsPluggableModuleConfigSwVer_Type())
fsPluggableModuleConfigSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleConfigSwVer.setStatus(_A)
class _FsPluggableModuleOnlineSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsPluggableModuleOnlineSwVer_Type.__name__=_E
_FsPluggableModuleOnlineSwVer_Object=MibTableColumn
fsPluggableModuleOnlineSwVer=_FsPluggableModuleOnlineSwVer_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,6),_FsPluggableModuleOnlineSwVer_Type())
fsPluggableModuleOnlineSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleOnlineSwVer.setStatus(_A)
class _FsPluggableModuleConfigInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsPluggableModuleConfigInfoDescr_Type.__name__=_E
_FsPluggableModuleConfigInfoDescr_Object=MibTableColumn
fsPluggableModuleConfigInfoDescr=_FsPluggableModuleConfigInfoDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,7),_FsPluggableModuleConfigInfoDescr_Type())
fsPluggableModuleConfigInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleConfigInfoDescr.setStatus(_A)
class _FsPluggableModuleOnlineInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsPluggableModuleOnlineInfoDescr_Type.__name__=_E
_FsPluggableModuleOnlineInfoDescr_Object=MibTableColumn
fsPluggableModuleOnlineInfoDescr=_FsPluggableModuleOnlineInfoDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,8),_FsPluggableModuleOnlineInfoDescr_Type())
fsPluggableModuleOnlineInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleOnlineInfoDescr.setStatus(_A)
_FsPluggableModuleConfigPortsNum_Type=Integer32
_FsPluggableModuleConfigPortsNum_Object=MibTableColumn
fsPluggableModuleConfigPortsNum=_FsPluggableModuleConfigPortsNum_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,9),_FsPluggableModuleConfigPortsNum_Type())
fsPluggableModuleConfigPortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleConfigPortsNum.setStatus(_A)
_FsPluggableModuleOnlinePortsNum_Type=Integer32
_FsPluggableModuleOnlinePortsNum_Object=MibTableColumn
fsPluggableModuleOnlinePortsNum=_FsPluggableModuleOnlinePortsNum_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,10),_FsPluggableModuleOnlinePortsNum_Type())
fsPluggableModuleOnlinePortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPluggableModuleOnlinePortsNum.setStatus(_A)
class _FsPluggableModuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('reset',1),('clearAllConf',2),('uninstall',3)))
_FsPluggableModuleAction_Type.__name__=_D
_FsPluggableModuleAction_Object=MibTableColumn
fsPluggableModuleAction=_FsPluggableModuleAction_Object((1,3,6,1,4,1,52642,1,1,10,2,34,2,1,1,11),_FsPluggableModuleAction_Type())
fsPluggableModuleAction.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPluggableModuleAction.setStatus(_A)
_FsRedundancyMIBConformance_ObjectIdentity=ObjectIdentity
fsRedundancyMIBConformance=_FsRedundancyMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,34,3))
_FsRedundancyMIBCompliances_ObjectIdentity=ObjectIdentity
fsRedundancyMIBCompliances=_FsRedundancyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,34,3,1))
_FsRedundancyMIBGroups_ObjectIdentity=ObjectIdentity
fsRedundancyMIBGroups=_FsRedundancyMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,34,3,2))
fsRedundancyMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,34,3,2,1))
fsRedundancyMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_G),(_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:fsRedundancyMIBGroup.setStatus(_A)
fsRedundancyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,34,3,1,1))
fsRedundancyMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:fsRedundancyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsRedundancyMIB':fsRedundancyMIB,'fsRedundancyMIBObjects':fsRedundancyMIBObjects,_J:fsRedundancyForceSwitchover,_K:fsMainCPU,'fsPluggableMIBObjects':fsPluggableMIBObjects,'fsPluggableModuleInfoTable':fsPluggableModuleInfoTable,'fsPluggableModuleInfoEntry':fsPluggableModuleInfoEntry,_G:fsPluggableModuleInfoDeviceIndex,_H:fsPluggableModuleInfoSlotIndex,_L:fsPluggableModuleStatus,_M:fsPluggableModuleConfigType,_N:fsPluggableModuleConfigSwVer,_O:fsPluggableModuleOnlineSwVer,_P:fsPluggableModuleConfigInfoDescr,_Q:fsPluggableModuleOnlineInfoDescr,_R:fsPluggableModuleConfigPortsNum,_S:fsPluggableModuleOnlinePortsNum,_T:fsPluggableModuleAction,'fsRedundancyMIBConformance':fsRedundancyMIBConformance,'fsRedundancyMIBCompliances':fsRedundancyMIBCompliances,'fsRedundancyMIBCompliance':fsRedundancyMIBCompliance,'fsRedundancyMIBGroups':fsRedundancyMIBGroups,_U:fsRedundancyMIBGroup})