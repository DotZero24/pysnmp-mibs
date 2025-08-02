_U='pdnActiveJack'
_T='pdnPortConfigXover'
_S='pdnPortConfigEthernetSpeed'
_R='pdnPortConfigEthernetAutoNegotiate'
_Q='pdnPortConfigEthernetResetState'
_P='pdnPortConfigEthernetManageType'
_O='pdnPortConfigEthernetDuplexMode'
_N='pdnPortConfigMauExtEntry'
_M='ResetStates'
_L='ManagementType'
_K='ifMauIndex'
_J='ifMauIfIndex'
_I='ifJackIndex'
_H='ifIndex'
_G='IF-MIB'
_F='SwitchState'
_E='Integer32'
_D='MAU-MIB'
_C='read-create'
_B='PDN-ETHER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ifJackIndex,ifMauEntry,ifMauIfIndex,ifMauIndex=mibBuilder.importSymbols(_D,_I,'ifMauEntry',_J,_K)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
ManagementType,ResetStates,SwitchState=mibBuilder.importSymbols('PDN-TC',_L,_M,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdn_ether=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,18))
if mibBuilder.loadTexts:pdn_ether.setRevisions(('1902-05-10 00:00','1902-01-09 00:00','2001-08-24 00:00','2000-05-02 00:00'))
_PdnPortConfigMIBObjects_ObjectIdentity=ObjectIdentity
pdnPortConfigMIBObjects=_PdnPortConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,18,1))
_PdnPortConfigEthernet_ObjectIdentity=ObjectIdentity
pdnPortConfigEthernet=_PdnPortConfigEthernet_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,18,1,1))
_PdnPortConfigEthernetTable_Object=MibTable
pdnPortConfigEthernetTable=_PdnPortConfigEthernetTable_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1))
if mibBuilder.loadTexts:pdnPortConfigEthernetTable.setStatus(_A)
_PdnPortConfigEthernetEntry_Object=MibTableRow
pdnPortConfigEthernetEntry=_PdnPortConfigEthernetEntry_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1,1))
pdnPortConfigEthernetEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pdnPortConfigEthernetEntry.setStatus(_A)
class _PdnPortConfigEthernetDuplexMode_Type(SwitchState):defaultValue=2
_PdnPortConfigEthernetDuplexMode_Type.__name__=_F
_PdnPortConfigEthernetDuplexMode_Object=MibTableColumn
pdnPortConfigEthernetDuplexMode=_PdnPortConfigEthernetDuplexMode_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1,1,1),_PdnPortConfigEthernetDuplexMode_Type())
pdnPortConfigEthernetDuplexMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigEthernetDuplexMode.setStatus(_A)
class _PdnPortConfigEthernetManageType_Type(ManagementType):defaultValue=2
_PdnPortConfigEthernetManageType_Type.__name__=_L
_PdnPortConfigEthernetManageType_Object=MibTableColumn
pdnPortConfigEthernetManageType=_PdnPortConfigEthernetManageType_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1,1,2),_PdnPortConfigEthernetManageType_Type())
pdnPortConfigEthernetManageType.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigEthernetManageType.setStatus(_A)
class _PdnPortConfigEthernetResetState_Type(ResetStates):defaultValue=1
_PdnPortConfigEthernetResetState_Type.__name__=_M
_PdnPortConfigEthernetResetState_Object=MibTableColumn
pdnPortConfigEthernetResetState=_PdnPortConfigEthernetResetState_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1,1,3),_PdnPortConfigEthernetResetState_Type())
pdnPortConfigEthernetResetState.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigEthernetResetState.setStatus(_A)
class _PdnPortConfigEthernetAutoNegotiate_Type(SwitchState):defaultValue=1
_PdnPortConfigEthernetAutoNegotiate_Type.__name__=_F
_PdnPortConfigEthernetAutoNegotiate_Object=MibTableColumn
pdnPortConfigEthernetAutoNegotiate=_PdnPortConfigEthernetAutoNegotiate_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1,1,4),_PdnPortConfigEthernetAutoNegotiate_Type())
pdnPortConfigEthernetAutoNegotiate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigEthernetAutoNegotiate.setStatus(_A)
class _PdnPortConfigEthernetSpeed_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tenBaseT',1),('hundredBaseT',2)))
_PdnPortConfigEthernetSpeed_Type.__name__=_E
_PdnPortConfigEthernetSpeed_Object=MibTableColumn
pdnPortConfigEthernetSpeed=_PdnPortConfigEthernetSpeed_Object((1,3,6,1,4,1,1795,2,24,2,18,1,1,1,1,5),_PdnPortConfigEthernetSpeed_Type())
pdnPortConfigEthernetSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigEthernetSpeed.setStatus(_A)
_PdnPortConfigGroups_ObjectIdentity=ObjectIdentity
pdnPortConfigGroups=_PdnPortConfigGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,18,1,2))
_PdnPortConfigMauExtMIBObject_ObjectIdentity=ObjectIdentity
pdnPortConfigMauExtMIBObject=_PdnPortConfigMauExtMIBObject_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,18,1,3))
_PdnPortConfigMauExtTable_Object=MibTable
pdnPortConfigMauExtTable=_PdnPortConfigMauExtTable_Object((1,3,6,1,4,1,1795,2,24,2,18,1,3,1))
if mibBuilder.loadTexts:pdnPortConfigMauExtTable.setStatus(_A)
_PdnPortConfigMauExtEntry_Object=MibTableRow
pdnPortConfigMauExtEntry=_PdnPortConfigMauExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,18,1,3,1,1))
if mibBuilder.loadTexts:pdnPortConfigMauExtEntry.setStatus(_A)
class _PdnPortConfigXover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mdi',1),('mdix',2)))
_PdnPortConfigXover_Type.__name__=_E
_PdnPortConfigXover_Object=MibTableColumn
pdnPortConfigXover=_PdnPortConfigXover_Object((1,3,6,1,4,1,1795,2,24,2,18,1,3,1,1,1),_PdnPortConfigXover_Type())
pdnPortConfigXover.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigXover.setStatus(_A)
_PdnPortConfigIfJackMIBObject_ObjectIdentity=ObjectIdentity
pdnPortConfigIfJackMIBObject=_PdnPortConfigIfJackMIBObject_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,18,1,4))
_PdnIfJackTable_Object=MibTable
pdnIfJackTable=_PdnIfJackTable_Object((1,3,6,1,4,1,1795,2,24,2,18,1,4,1))
if mibBuilder.loadTexts:pdnIfJackTable.setStatus(_A)
_PdnIfJackEntry_Object=MibTableRow
pdnIfJackEntry=_PdnIfJackEntry_Object((1,3,6,1,4,1,1795,2,24,2,18,1,4,1,1))
pdnIfJackEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:pdnIfJackEntry.setStatus(_A)
class _PdnActiveJack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fiber',1),('rj45',2),('auto',3)))
_PdnActiveJack_Type.__name__=_E
_PdnActiveJack_Object=MibTableColumn
pdnActiveJack=_PdnActiveJack_Object((1,3,6,1,4,1,1795,2,24,2,18,1,4,1,1,1),_PdnActiveJack_Type())
pdnActiveJack.setMaxAccess('read-write')
if mibBuilder.loadTexts:pdnActiveJack.setStatus(_A)
_PdnPortConfigMIBTraps_ObjectIdentity=ObjectIdentity
pdnPortConfigMIBTraps=_PdnPortConfigMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,18,2))
ifMauEntry.registerAugmentions((_B,_N))
pdnPortConfigMauExtEntry.setIndexNames(*ifMauEntry.getIndexNames())
pdnPortConfigEthernetGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,18,1,2,1))
pdnPortConfigEthernetGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:pdnPortConfigEthernetGroup.setStatus(_A)
pdnPortConfigExtMauGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,18,1,2,2))
pdnPortConfigExtMauGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:pdnPortConfigExtMauGroup.setStatus(_A)
pdnPortConfigExtIfJackGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,18,1,2,3))
pdnPortConfigExtIfJackGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:pdnPortConfigExtIfJackGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdn-ether':pdn_ether,'pdnPortConfigMIBObjects':pdnPortConfigMIBObjects,'pdnPortConfigEthernet':pdnPortConfigEthernet,'pdnPortConfigEthernetTable':pdnPortConfigEthernetTable,'pdnPortConfigEthernetEntry':pdnPortConfigEthernetEntry,_O:pdnPortConfigEthernetDuplexMode,_P:pdnPortConfigEthernetManageType,_Q:pdnPortConfigEthernetResetState,_R:pdnPortConfigEthernetAutoNegotiate,_S:pdnPortConfigEthernetSpeed,'pdnPortConfigGroups':pdnPortConfigGroups,'pdnPortConfigEthernetGroup':pdnPortConfigEthernetGroup,'pdnPortConfigExtMauGroup':pdnPortConfigExtMauGroup,'pdnPortConfigExtIfJackGroup':pdnPortConfigExtIfJackGroup,'pdnPortConfigMauExtMIBObject':pdnPortConfigMauExtMIBObject,'pdnPortConfigMauExtTable':pdnPortConfigMauExtTable,_N:pdnPortConfigMauExtEntry,_T:pdnPortConfigXover,'pdnPortConfigIfJackMIBObject':pdnPortConfigIfJackMIBObject,'pdnIfJackTable':pdnIfJackTable,'pdnIfJackEntry':pdnIfJackEntry,_U:pdnActiveJack,'pdnPortConfigMIBTraps':pdnPortConfigMIBTraps})