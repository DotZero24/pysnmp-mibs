_O='fdryMacBasedVlanMac'
_N='fdryMacBasedVlanId'
_M='fdryMacVlanPortMemberPortId'
_L='fdryMacVlanPortMemberVLanId'
_K='enabled'
_J='disabled'
_I='fdryMacVlanIfIndex'
_H='read-create'
_G='clear'
_F='valid'
_E='not-accessible'
_D='read-write'
_C='FOUNDRY-MAC-VLAN-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fdryMacVlanMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,32))
if mibBuilder.loadTexts:fdryMacVlanMIB.setRevisions(('2010-06-02 00:00','2008-12-17 00:00'))
_FdryMacVlanGlobalObjects_ObjectIdentity=ObjectIdentity
fdryMacVlanGlobalObjects=_FdryMacVlanGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,32,1))
class _FdryMacVlanGlobalClearOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_FdryMacVlanGlobalClearOper_Type.__name__=_B
_FdryMacVlanGlobalClearOper_Object=MibScalar
fdryMacVlanGlobalClearOper=_FdryMacVlanGlobalClearOper_Object((1,3,6,1,4,1,1991,1,1,3,32,1,1),_FdryMacVlanGlobalClearOper_Type())
fdryMacVlanGlobalClearOper.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryMacVlanGlobalClearOper.setStatus(_A)
class _FdryMacVlanGlobalDynConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_FdryMacVlanGlobalDynConfigState_Type.__name__=_B
_FdryMacVlanGlobalDynConfigState_Object=MibScalar
fdryMacVlanGlobalDynConfigState=_FdryMacVlanGlobalDynConfigState_Object((1,3,6,1,4,1,1991,1,1,3,32,1,2),_FdryMacVlanGlobalDynConfigState_Type())
fdryMacVlanGlobalDynConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryMacVlanGlobalDynConfigState.setStatus(_A)
_FdryMacVlanTableObjects_ObjectIdentity=ObjectIdentity
fdryMacVlanTableObjects=_FdryMacVlanTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,32,2))
_FdryMacVlanPortMemberTable_Object=MibTable
fdryMacVlanPortMemberTable=_FdryMacVlanPortMemberTable_Object((1,3,6,1,4,1,1991,1,1,3,32,2,1))
if mibBuilder.loadTexts:fdryMacVlanPortMemberTable.setStatus(_A)
_FdryMacVlanPortMemberEntry_Object=MibTableRow
fdryMacVlanPortMemberEntry=_FdryMacVlanPortMemberEntry_Object((1,3,6,1,4,1,1991,1,1,3,32,2,1,1))
fdryMacVlanPortMemberEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fdryMacVlanPortMemberEntry.setStatus(_A)
class _FdryMacVlanPortMemberVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_FdryMacVlanPortMemberVLanId_Type.__name__=_B
_FdryMacVlanPortMemberVLanId_Object=MibTableColumn
fdryMacVlanPortMemberVLanId=_FdryMacVlanPortMemberVLanId_Object((1,3,6,1,4,1,1991,1,1,3,32,2,1,1,1),_FdryMacVlanPortMemberVLanId_Type())
fdryMacVlanPortMemberVLanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryMacVlanPortMemberVLanId.setStatus(_A)
_FdryMacVlanPortMemberPortId_Type=InterfaceIndex
_FdryMacVlanPortMemberPortId_Object=MibTableColumn
fdryMacVlanPortMemberPortId=_FdryMacVlanPortMemberPortId_Object((1,3,6,1,4,1,1991,1,1,3,32,2,1,1,2),_FdryMacVlanPortMemberPortId_Type())
fdryMacVlanPortMemberPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryMacVlanPortMemberPortId.setStatus(_A)
_FdryMacVlanPortMemberRowStatus_Type=RowStatus
_FdryMacVlanPortMemberRowStatus_Object=MibTableColumn
fdryMacVlanPortMemberRowStatus=_FdryMacVlanPortMemberRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,32,2,1,1,3),_FdryMacVlanPortMemberRowStatus_Type())
fdryMacVlanPortMemberRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fdryMacVlanPortMemberRowStatus.setStatus(_A)
_FdryMacVlanIfTable_Object=MibTable
fdryMacVlanIfTable=_FdryMacVlanIfTable_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2))
if mibBuilder.loadTexts:fdryMacVlanIfTable.setStatus(_A)
_FdryMacVlanIfEntry_Object=MibTableRow
fdryMacVlanIfEntry=_FdryMacVlanIfEntry_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2,1))
fdryMacVlanIfEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:fdryMacVlanIfEntry.setStatus(_A)
_FdryMacVlanIfIndex_Type=InterfaceIndex
_FdryMacVlanIfIndex_Object=MibTableColumn
fdryMacVlanIfIndex=_FdryMacVlanIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2,1,1),_FdryMacVlanIfIndex_Type())
fdryMacVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryMacVlanIfIndex.setStatus(_A)
class _FdryMacVlanIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_FdryMacVlanIfEnable_Type.__name__=_B
_FdryMacVlanIfEnable_Object=MibTableColumn
fdryMacVlanIfEnable=_FdryMacVlanIfEnable_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2,1,2),_FdryMacVlanIfEnable_Type())
fdryMacVlanIfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryMacVlanIfEnable.setStatus(_A)
class _FdryMacVlanIfMaxEntry_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,32))
_FdryMacVlanIfMaxEntry_Type.__name__=_B
_FdryMacVlanIfMaxEntry_Object=MibTableColumn
fdryMacVlanIfMaxEntry=_FdryMacVlanIfMaxEntry_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2,1,3),_FdryMacVlanIfMaxEntry_Type())
fdryMacVlanIfMaxEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryMacVlanIfMaxEntry.setStatus(_A)
class _FdryMacVlanIfClearOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_FdryMacVlanIfClearOper_Type.__name__=_B
_FdryMacVlanIfClearOper_Object=MibTableColumn
fdryMacVlanIfClearOper=_FdryMacVlanIfClearOper_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2,1,4),_FdryMacVlanIfClearOper_Type())
fdryMacVlanIfClearOper.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryMacVlanIfClearOper.setStatus(_A)
class _FdryMacVlanIfClearConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_FdryMacVlanIfClearConfig_Type.__name__=_B
_FdryMacVlanIfClearConfig_Object=MibTableColumn
fdryMacVlanIfClearConfig=_FdryMacVlanIfClearConfig_Object((1,3,6,1,4,1,1991,1,1,3,32,2,2,1,5),_FdryMacVlanIfClearConfig_Type())
fdryMacVlanIfClearConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryMacVlanIfClearConfig.setStatus(_A)
_FdryMacBasedVlanTable_Object=MibTable
fdryMacBasedVlanTable=_FdryMacBasedVlanTable_Object((1,3,6,1,4,1,1991,1,1,3,32,2,3))
if mibBuilder.loadTexts:fdryMacBasedVlanTable.setStatus(_A)
_FdryMacBasedVlanEntry_Object=MibTableRow
fdryMacBasedVlanEntry=_FdryMacBasedVlanEntry_Object((1,3,6,1,4,1,1991,1,1,3,32,2,3,1))
fdryMacBasedVlanEntry.setIndexNames((0,_C,_I),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:fdryMacBasedVlanEntry.setStatus(_A)
class _FdryMacBasedVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_FdryMacBasedVlanId_Type.__name__=_B
_FdryMacBasedVlanId_Object=MibTableColumn
fdryMacBasedVlanId=_FdryMacBasedVlanId_Object((1,3,6,1,4,1,1991,1,1,3,32,2,3,1,1),_FdryMacBasedVlanId_Type())
fdryMacBasedVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryMacBasedVlanId.setStatus(_A)
_FdryMacBasedVlanMac_Type=MacAddress
_FdryMacBasedVlanMac_Object=MibTableColumn
fdryMacBasedVlanMac=_FdryMacBasedVlanMac_Object((1,3,6,1,4,1,1991,1,1,3,32,2,3,1,2),_FdryMacBasedVlanMac_Type())
fdryMacBasedVlanMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryMacBasedVlanMac.setStatus(_A)
class _FdryMacBasedVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FdryMacBasedVlanPriority_Type.__name__=_B
_FdryMacBasedVlanPriority_Object=MibTableColumn
fdryMacBasedVlanPriority=_FdryMacBasedVlanPriority_Object((1,3,6,1,4,1,1991,1,1,3,32,2,3,1,3),_FdryMacBasedVlanPriority_Type())
fdryMacBasedVlanPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:fdryMacBasedVlanPriority.setStatus(_A)
_FdryMacBasedVlanRowStatus_Type=RowStatus
_FdryMacBasedVlanRowStatus_Object=MibTableColumn
fdryMacBasedVlanRowStatus=_FdryMacBasedVlanRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,32,2,3,1,4),_FdryMacBasedVlanRowStatus_Type())
fdryMacBasedVlanRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fdryMacBasedVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fdryMacVlanMIB':fdryMacVlanMIB,'fdryMacVlanGlobalObjects':fdryMacVlanGlobalObjects,'fdryMacVlanGlobalClearOper':fdryMacVlanGlobalClearOper,'fdryMacVlanGlobalDynConfigState':fdryMacVlanGlobalDynConfigState,'fdryMacVlanTableObjects':fdryMacVlanTableObjects,'fdryMacVlanPortMemberTable':fdryMacVlanPortMemberTable,'fdryMacVlanPortMemberEntry':fdryMacVlanPortMemberEntry,_L:fdryMacVlanPortMemberVLanId,_M:fdryMacVlanPortMemberPortId,'fdryMacVlanPortMemberRowStatus':fdryMacVlanPortMemberRowStatus,'fdryMacVlanIfTable':fdryMacVlanIfTable,'fdryMacVlanIfEntry':fdryMacVlanIfEntry,_I:fdryMacVlanIfIndex,'fdryMacVlanIfEnable':fdryMacVlanIfEnable,'fdryMacVlanIfMaxEntry':fdryMacVlanIfMaxEntry,'fdryMacVlanIfClearOper':fdryMacVlanIfClearOper,'fdryMacVlanIfClearConfig':fdryMacVlanIfClearConfig,'fdryMacBasedVlanTable':fdryMacBasedVlanTable,'fdryMacBasedVlanEntry':fdryMacBasedVlanEntry,_N:fdryMacBasedVlanId,_O:fdryMacBasedVlanMac,'fdryMacBasedVlanPriority':fdryMacBasedVlanPriority,'fdryMacBasedVlanRowStatus':fdryMacBasedVlanRowStatus})