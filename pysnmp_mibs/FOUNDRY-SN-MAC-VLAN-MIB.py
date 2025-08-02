_P='snMacBasedVlanMac'
_O='snMacBasedVlanId'
_N='create'
_M='delete'
_L='snMacVlanPortMemberPortId'
_K='snMacVlanPortMemberVLanId'
_J='enabled'
_I='disabled'
_H='snMacVlanIfIndex'
_G='clear'
_F='not-accessible'
_E='valid'
_D='FOUNDRY-SN-MAC-VLAN-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
snMacVlan=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,30))
if mibBuilder.loadTexts:snMacVlan.setRevisions(('2007-06-25 00:00',))
_SnMacVlanGlobalObjects_ObjectIdentity=ObjectIdentity
snMacVlanGlobalObjects=_SnMacVlanGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,30,1))
class _SnMacVlanGlobalClearOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_SnMacVlanGlobalClearOper_Type.__name__=_B
_SnMacVlanGlobalClearOper_Object=MibScalar
snMacVlanGlobalClearOper=_SnMacVlanGlobalClearOper_Object((1,3,6,1,4,1,1991,1,1,3,30,1,1),_SnMacVlanGlobalClearOper_Type())
snMacVlanGlobalClearOper.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanGlobalClearOper.setStatus(_A)
class _SnMacVlanGlobalDynConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SnMacVlanGlobalDynConfigState_Type.__name__=_B
_SnMacVlanGlobalDynConfigState_Object=MibScalar
snMacVlanGlobalDynConfigState=_SnMacVlanGlobalDynConfigState_Object((1,3,6,1,4,1,1991,1,1,3,30,1,2),_SnMacVlanGlobalDynConfigState_Type())
snMacVlanGlobalDynConfigState.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanGlobalDynConfigState.setStatus(_A)
_SnMacVlanTableObjects_ObjectIdentity=ObjectIdentity
snMacVlanTableObjects=_SnMacVlanTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,30,2))
_SnMacVlanPortMemberTable_Object=MibTable
snMacVlanPortMemberTable=_SnMacVlanPortMemberTable_Object((1,3,6,1,4,1,1991,1,1,3,30,2,1))
if mibBuilder.loadTexts:snMacVlanPortMemberTable.setStatus(_A)
_SnMacVlanPortMemberEntry_Object=MibTableRow
snMacVlanPortMemberEntry=_SnMacVlanPortMemberEntry_Object((1,3,6,1,4,1,1991,1,1,3,30,2,1,1))
snMacVlanPortMemberEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:snMacVlanPortMemberEntry.setStatus(_A)
class _SnMacVlanPortMemberVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnMacVlanPortMemberVLanId_Type.__name__=_B
_SnMacVlanPortMemberVLanId_Object=MibTableColumn
snMacVlanPortMemberVLanId=_SnMacVlanPortMemberVLanId_Object((1,3,6,1,4,1,1991,1,1,3,30,2,1,1,1),_SnMacVlanPortMemberVLanId_Type())
snMacVlanPortMemberVLanId.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacVlanPortMemberVLanId.setStatus(_A)
_SnMacVlanPortMemberPortId_Type=InterfaceIndex
_SnMacVlanPortMemberPortId_Object=MibTableColumn
snMacVlanPortMemberPortId=_SnMacVlanPortMemberPortId_Object((1,3,6,1,4,1,1991,1,1,3,30,2,1,1,2),_SnMacVlanPortMemberPortId_Type())
snMacVlanPortMemberPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacVlanPortMemberPortId.setStatus(_A)
class _SnMacVlanPortMemberRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_E,2),(_M,3),(_N,4)))
_SnMacVlanPortMemberRowStatus_Type.__name__=_B
_SnMacVlanPortMemberRowStatus_Object=MibTableColumn
snMacVlanPortMemberRowStatus=_SnMacVlanPortMemberRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,30,2,1,1,3),_SnMacVlanPortMemberRowStatus_Type())
snMacVlanPortMemberRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanPortMemberRowStatus.setStatus(_A)
_SnMacVlanIfTable_Object=MibTable
snMacVlanIfTable=_SnMacVlanIfTable_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2))
if mibBuilder.loadTexts:snMacVlanIfTable.setStatus(_A)
_SnMacVlanIfEntry_Object=MibTableRow
snMacVlanIfEntry=_SnMacVlanIfEntry_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2,1))
snMacVlanIfEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:snMacVlanIfEntry.setStatus(_A)
_SnMacVlanIfIndex_Type=InterfaceIndex
_SnMacVlanIfIndex_Object=MibTableColumn
snMacVlanIfIndex=_SnMacVlanIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2,1,1),_SnMacVlanIfIndex_Type())
snMacVlanIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacVlanIfIndex.setStatus(_A)
class _SnMacVlanIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SnMacVlanIfEnable_Type.__name__=_B
_SnMacVlanIfEnable_Object=MibTableColumn
snMacVlanIfEnable=_SnMacVlanIfEnable_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2,1,2),_SnMacVlanIfEnable_Type())
snMacVlanIfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanIfEnable.setStatus(_A)
class _SnMacVlanIfMaxEntry_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,32))
_SnMacVlanIfMaxEntry_Type.__name__=_B
_SnMacVlanIfMaxEntry_Object=MibTableColumn
snMacVlanIfMaxEntry=_SnMacVlanIfMaxEntry_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2,1,3),_SnMacVlanIfMaxEntry_Type())
snMacVlanIfMaxEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanIfMaxEntry.setStatus(_A)
class _SnMacVlanIfClearOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_SnMacVlanIfClearOper_Type.__name__=_B
_SnMacVlanIfClearOper_Object=MibTableColumn
snMacVlanIfClearOper=_SnMacVlanIfClearOper_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2,1,4),_SnMacVlanIfClearOper_Type())
snMacVlanIfClearOper.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanIfClearOper.setStatus(_A)
class _SnMacVlanIfClearConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_SnMacVlanIfClearConfig_Type.__name__=_B
_SnMacVlanIfClearConfig_Object=MibTableColumn
snMacVlanIfClearConfig=_SnMacVlanIfClearConfig_Object((1,3,6,1,4,1,1991,1,1,3,30,2,2,1,5),_SnMacVlanIfClearConfig_Type())
snMacVlanIfClearConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacVlanIfClearConfig.setStatus(_A)
_SnMacBasedVlanTable_Object=MibTable
snMacBasedVlanTable=_SnMacBasedVlanTable_Object((1,3,6,1,4,1,1991,1,1,3,30,2,3))
if mibBuilder.loadTexts:snMacBasedVlanTable.setStatus(_A)
_SnMacBasedVlanEntry_Object=MibTableRow
snMacBasedVlanEntry=_SnMacBasedVlanEntry_Object((1,3,6,1,4,1,1991,1,1,3,30,2,3,1))
snMacBasedVlanEntry.setIndexNames((0,_D,_H),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:snMacBasedVlanEntry.setStatus(_A)
class _SnMacBasedVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnMacBasedVlanId_Type.__name__=_B
_SnMacBasedVlanId_Object=MibTableColumn
snMacBasedVlanId=_SnMacBasedVlanId_Object((1,3,6,1,4,1,1991,1,1,3,30,2,3,1,1),_SnMacBasedVlanId_Type())
snMacBasedVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacBasedVlanId.setStatus(_A)
_SnMacBasedVlanMac_Type=MacAddress
_SnMacBasedVlanMac_Object=MibTableColumn
snMacBasedVlanMac=_SnMacBasedVlanMac_Object((1,3,6,1,4,1,1991,1,1,3,30,2,3,1,2),_SnMacBasedVlanMac_Type())
snMacBasedVlanMac.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacBasedVlanMac.setStatus(_A)
class _SnMacBasedVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnMacBasedVlanPriority_Type.__name__=_B
_SnMacBasedVlanPriority_Object=MibTableColumn
snMacBasedVlanPriority=_SnMacBasedVlanPriority_Object((1,3,6,1,4,1,1991,1,1,3,30,2,3,1,3),_SnMacBasedVlanPriority_Type())
snMacBasedVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacBasedVlanPriority.setStatus(_A)
class _SnMacBasedVlanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_E,2),(_M,3),(_N,4)))
_SnMacBasedVlanRowStatus_Type.__name__=_B
_SnMacBasedVlanRowStatus_Object=MibTableColumn
snMacBasedVlanRowStatus=_SnMacBasedVlanRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,30,2,3,1,4),_SnMacBasedVlanRowStatus_Type())
snMacBasedVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snMacBasedVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snMacVlan':snMacVlan,'snMacVlanGlobalObjects':snMacVlanGlobalObjects,'snMacVlanGlobalClearOper':snMacVlanGlobalClearOper,'snMacVlanGlobalDynConfigState':snMacVlanGlobalDynConfigState,'snMacVlanTableObjects':snMacVlanTableObjects,'snMacVlanPortMemberTable':snMacVlanPortMemberTable,'snMacVlanPortMemberEntry':snMacVlanPortMemberEntry,_K:snMacVlanPortMemberVLanId,_L:snMacVlanPortMemberPortId,'snMacVlanPortMemberRowStatus':snMacVlanPortMemberRowStatus,'snMacVlanIfTable':snMacVlanIfTable,'snMacVlanIfEntry':snMacVlanIfEntry,_H:snMacVlanIfIndex,'snMacVlanIfEnable':snMacVlanIfEnable,'snMacVlanIfMaxEntry':snMacVlanIfMaxEntry,'snMacVlanIfClearOper':snMacVlanIfClearOper,'snMacVlanIfClearConfig':snMacVlanIfClearConfig,'snMacBasedVlanTable':snMacBasedVlanTable,'snMacBasedVlanEntry':snMacBasedVlanEntry,_O:snMacBasedVlanId,_P:snMacBasedVlanMac,'snMacBasedVlanPriority':snMacBasedVlanPriority,'snMacBasedVlanRowStatus':snMacBasedVlanRowStatus})