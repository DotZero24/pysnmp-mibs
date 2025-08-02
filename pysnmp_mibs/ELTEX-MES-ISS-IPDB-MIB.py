_O='eltMesIssIpDbv6BindingEntry'
_N='eltMesIssIpDbBindingEntry'
_M='disable'
_L='enable'
_K='eltMesIssIpDbSrcGuardVlanId'
_J='read-only'
_I='eltMesIssIpDbIntfStatIndex'
_H='eltMesIssIpDbIntfConfIndex'
_G='Unsigned32'
_F='not-accessible'
_E='TruthValue'
_D='ELTEX-MES-ISS-IPDB-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsIpDbBindingEntry,fsIpDbv6BindingEntry=mibBuilder.importSymbols('ARICENT-IPDB-MIB','fsIpDbBindingEntry','fsIpDbv6BindingEntry')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
eltMesIssIpDbMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,9))
if mibBuilder.loadTexts:eltMesIssIpDbMIB.setRevisions(('2022-06-10 00:00','2022-03-17 00:00','2022-03-04 00:00','2020-05-21 00:00','2019-02-06 00:00'))
_EltMesIssIpDbObjects_ObjectIdentity=ObjectIdentity
eltMesIssIpDbObjects=_EltMesIssIpDbObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,9,1))
_EltMesIssIpDbInterfaces_ObjectIdentity=ObjectIdentity
eltMesIssIpDbInterfaces=_EltMesIssIpDbInterfaces_ObjectIdentity((1,3,6,1,4,1,35265,1,139,9,1,1))
_EltMesIssIpDbIntfConfTable_Object=MibTable
eltMesIssIpDbIntfConfTable=_EltMesIssIpDbIntfConfTable_Object((1,3,6,1,4,1,35265,1,139,9,1,1,1))
if mibBuilder.loadTexts:eltMesIssIpDbIntfConfTable.setStatus(_A)
_EltMesIssIpDbIntfConfEntry_Object=MibTableRow
eltMesIssIpDbIntfConfEntry=_EltMesIssIpDbIntfConfEntry_Object((1,3,6,1,4,1,35265,1,139,9,1,1,1,1))
eltMesIssIpDbIntfConfEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:eltMesIssIpDbIntfConfEntry.setStatus(_A)
_EltMesIssIpDbIntfConfIndex_Type=InterfaceIndex
_EltMesIssIpDbIntfConfIndex_Object=MibTableColumn
eltMesIssIpDbIntfConfIndex=_EltMesIssIpDbIntfConfIndex_Object((1,3,6,1,4,1,35265,1,139,9,1,1,1,1,1),_EltMesIssIpDbIntfConfIndex_Type())
eltMesIssIpDbIntfConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssIpDbIntfConfIndex.setStatus(_A)
class _EltMesIssIpDbIntfConfBindingLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_EltMesIssIpDbIntfConfBindingLimit_Type.__name__=_G
_EltMesIssIpDbIntfConfBindingLimit_Object=MibTableColumn
eltMesIssIpDbIntfConfBindingLimit=_EltMesIssIpDbIntfConfBindingLimit_Object((1,3,6,1,4,1,35265,1,139,9,1,1,1,1,2),_EltMesIssIpDbIntfConfBindingLimit_Type())
eltMesIssIpDbIntfConfBindingLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbIntfConfBindingLimit.setStatus(_A)
class _EltMesIssIpDbIntfConfBindingLimitControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EltMesIssIpDbIntfConfBindingLimitControl_Type.__name__=_C
_EltMesIssIpDbIntfConfBindingLimitControl_Object=MibTableColumn
eltMesIssIpDbIntfConfBindingLimitControl=_EltMesIssIpDbIntfConfBindingLimitControl_Object((1,3,6,1,4,1,35265,1,139,9,1,1,1,1,3),_EltMesIssIpDbIntfConfBindingLimitControl_Type())
eltMesIssIpDbIntfConfBindingLimitControl.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbIntfConfBindingLimitControl.setStatus(_A)
_EltMesIssIpDbIntfStatTable_Object=MibTable
eltMesIssIpDbIntfStatTable=_EltMesIssIpDbIntfStatTable_Object((1,3,6,1,4,1,35265,1,139,9,1,1,2))
if mibBuilder.loadTexts:eltMesIssIpDbIntfStatTable.setStatus(_A)
_EltMesIssIpDbIntfStatEntry_Object=MibTableRow
eltMesIssIpDbIntfStatEntry=_EltMesIssIpDbIntfStatEntry_Object((1,3,6,1,4,1,35265,1,139,9,1,1,2,1))
eltMesIssIpDbIntfStatEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:eltMesIssIpDbIntfStatEntry.setStatus(_A)
_EltMesIssIpDbIntfStatIndex_Type=InterfaceIndex
_EltMesIssIpDbIntfStatIndex_Object=MibTableColumn
eltMesIssIpDbIntfStatIndex=_EltMesIssIpDbIntfStatIndex_Object((1,3,6,1,4,1,35265,1,139,9,1,1,2,1,1),_EltMesIssIpDbIntfStatIndex_Type())
eltMesIssIpDbIntfStatIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssIpDbIntfStatIndex.setStatus(_A)
_EltMesIssIpDbIntfStatNoOfStaticBindings_Type=Counter32
_EltMesIssIpDbIntfStatNoOfStaticBindings_Object=MibTableColumn
eltMesIssIpDbIntfStatNoOfStaticBindings=_EltMesIssIpDbIntfStatNoOfStaticBindings_Object((1,3,6,1,4,1,35265,1,139,9,1,1,2,1,2),_EltMesIssIpDbIntfStatNoOfStaticBindings_Type())
eltMesIssIpDbIntfStatNoOfStaticBindings.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssIpDbIntfStatNoOfStaticBindings.setStatus(_A)
_EltMesIssIpDbIntfStatNoOfDHCPBindings_Type=Counter32
_EltMesIssIpDbIntfStatNoOfDHCPBindings_Object=MibTableColumn
eltMesIssIpDbIntfStatNoOfDHCPBindings=_EltMesIssIpDbIntfStatNoOfDHCPBindings_Object((1,3,6,1,4,1,35265,1,139,9,1,1,2,1,3),_EltMesIssIpDbIntfStatNoOfDHCPBindings_Type())
eltMesIssIpDbIntfStatNoOfDHCPBindings.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssIpDbIntfStatNoOfDHCPBindings.setStatus(_A)
_EltMesIssIpDbSrcGuardVlanTable_Object=MibTable
eltMesIssIpDbSrcGuardVlanTable=_EltMesIssIpDbSrcGuardVlanTable_Object((1,3,6,1,4,1,35265,1,139,9,1,1,3))
if mibBuilder.loadTexts:eltMesIssIpDbSrcGuardVlanTable.setStatus(_A)
_EltMesIssIpDbSrcGuardVlanEntry_Object=MibTableRow
eltMesIssIpDbSrcGuardVlanEntry=_EltMesIssIpDbSrcGuardVlanEntry_Object((1,3,6,1,4,1,35265,1,139,9,1,1,3,1))
eltMesIssIpDbSrcGuardVlanEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:eltMesIssIpDbSrcGuardVlanEntry.setStatus(_A)
class _EltMesIssIpDbSrcGuardVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_EltMesIssIpDbSrcGuardVlanId_Type.__name__=_C
_EltMesIssIpDbSrcGuardVlanId_Object=MibTableColumn
eltMesIssIpDbSrcGuardVlanId=_EltMesIssIpDbSrcGuardVlanId_Object((1,3,6,1,4,1,35265,1,139,9,1,1,3,1,1),_EltMesIssIpDbSrcGuardVlanId_Type())
eltMesIssIpDbSrcGuardVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssIpDbSrcGuardVlanId.setStatus(_A)
class _EltMesIssIpDbSrcGuardVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_EltMesIssIpDbSrcGuardVlanStatus_Type.__name__=_C
_EltMesIssIpDbSrcGuardVlanStatus_Object=MibTableColumn
eltMesIssIpDbSrcGuardVlanStatus=_EltMesIssIpDbSrcGuardVlanStatus_Object((1,3,6,1,4,1,35265,1,139,9,1,1,3,1,2),_EltMesIssIpDbSrcGuardVlanStatus_Type())
eltMesIssIpDbSrcGuardVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbSrcGuardVlanStatus.setStatus(_A)
class _EltMesIssIpDbv6SrcGuardVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_EltMesIssIpDbv6SrcGuardVlanStatus_Type.__name__=_C
_EltMesIssIpDbv6SrcGuardVlanStatus_Object=MibTableColumn
eltMesIssIpDbv6SrcGuardVlanStatus=_EltMesIssIpDbv6SrcGuardVlanStatus_Object((1,3,6,1,4,1,35265,1,139,9,1,1,3,1,3),_EltMesIssIpDbv6SrcGuardVlanStatus_Type())
eltMesIssIpDbv6SrcGuardVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbv6SrcGuardVlanStatus.setStatus(_A)
_EltMesIssIpDbBinding_ObjectIdentity=ObjectIdentity
eltMesIssIpDbBinding=_EltMesIssIpDbBinding_ObjectIdentity((1,3,6,1,4,1,35265,1,139,9,1,2))
_EltMesIssIpDbBindingTable_Object=MibTable
eltMesIssIpDbBindingTable=_EltMesIssIpDbBindingTable_Object((1,3,6,1,4,1,35265,1,139,9,1,2,1))
if mibBuilder.loadTexts:eltMesIssIpDbBindingTable.setStatus(_A)
_EltMesIssIpDbBindingEntry_Object=MibTableRow
eltMesIssIpDbBindingEntry=_EltMesIssIpDbBindingEntry_Object((1,3,6,1,4,1,35265,1,139,9,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssIpDbBindingEntry.setStatus(_A)
class _EltMesIssIpDbBindingEntryClearFlag_Type(TruthValue):defaultValue=2
_EltMesIssIpDbBindingEntryClearFlag_Type.__name__=_E
_EltMesIssIpDbBindingEntryClearFlag_Object=MibTableColumn
eltMesIssIpDbBindingEntryClearFlag=_EltMesIssIpDbBindingEntryClearFlag_Object((1,3,6,1,4,1,35265,1,139,9,1,2,1,1,1),_EltMesIssIpDbBindingEntryClearFlag_Type())
eltMesIssIpDbBindingEntryClearFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbBindingEntryClearFlag.setStatus(_A)
class _EltMesIssIpDbBindingDynamicEntriesPortDownAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('retain',1),('clear',2)))
_EltMesIssIpDbBindingDynamicEntriesPortDownAction_Type.__name__=_C
_EltMesIssIpDbBindingDynamicEntriesPortDownAction_Object=MibScalar
eltMesIssIpDbBindingDynamicEntriesPortDownAction=_EltMesIssIpDbBindingDynamicEntriesPortDownAction_Object((1,3,6,1,4,1,35265,1,139,9,1,2,2),_EltMesIssIpDbBindingDynamicEntriesPortDownAction_Type())
eltMesIssIpDbBindingDynamicEntriesPortDownAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbBindingDynamicEntriesPortDownAction.setStatus(_A)
_EltMesIssIpDbv6Binding_ObjectIdentity=ObjectIdentity
eltMesIssIpDbv6Binding=_EltMesIssIpDbv6Binding_ObjectIdentity((1,3,6,1,4,1,35265,1,139,9,1,3))
_EltMesIssIpDbv6BindingTable_Object=MibTable
eltMesIssIpDbv6BindingTable=_EltMesIssIpDbv6BindingTable_Object((1,3,6,1,4,1,35265,1,139,9,1,3,1))
if mibBuilder.loadTexts:eltMesIssIpDbv6BindingTable.setStatus(_A)
_EltMesIssIpDbv6BindingEntry_Object=MibTableRow
eltMesIssIpDbv6BindingEntry=_EltMesIssIpDbv6BindingEntry_Object((1,3,6,1,4,1,35265,1,139,9,1,3,1,1))
if mibBuilder.loadTexts:eltMesIssIpDbv6BindingEntry.setStatus(_A)
class _EltMesIssIpDbv6BindingEntryClearFlag_Type(TruthValue):defaultValue=2
_EltMesIssIpDbv6BindingEntryClearFlag_Type.__name__=_E
_EltMesIssIpDbv6BindingEntryClearFlag_Object=MibTableColumn
eltMesIssIpDbv6BindingEntryClearFlag=_EltMesIssIpDbv6BindingEntryClearFlag_Object((1,3,6,1,4,1,35265,1,139,9,1,3,1,1,1),_EltMesIssIpDbv6BindingEntryClearFlag_Type())
eltMesIssIpDbv6BindingEntryClearFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpDbv6BindingEntryClearFlag.setStatus(_A)
_EltMesIssIpDbNotifications_ObjectIdentity=ObjectIdentity
eltMesIssIpDbNotifications=_EltMesIssIpDbNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,9,2))
fsIpDbBindingEntry.registerAugmentions((_D,_N))
eltMesIssIpDbBindingEntry.setIndexNames(*fsIpDbBindingEntry.getIndexNames())
fsIpDbv6BindingEntry.registerAugmentions((_D,_O))
eltMesIssIpDbv6BindingEntry.setIndexNames(*fsIpDbv6BindingEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'eltMesIssIpDbMIB':eltMesIssIpDbMIB,'eltMesIssIpDbObjects':eltMesIssIpDbObjects,'eltMesIssIpDbInterfaces':eltMesIssIpDbInterfaces,'eltMesIssIpDbIntfConfTable':eltMesIssIpDbIntfConfTable,'eltMesIssIpDbIntfConfEntry':eltMesIssIpDbIntfConfEntry,_H:eltMesIssIpDbIntfConfIndex,'eltMesIssIpDbIntfConfBindingLimit':eltMesIssIpDbIntfConfBindingLimit,'eltMesIssIpDbIntfConfBindingLimitControl':eltMesIssIpDbIntfConfBindingLimitControl,'eltMesIssIpDbIntfStatTable':eltMesIssIpDbIntfStatTable,'eltMesIssIpDbIntfStatEntry':eltMesIssIpDbIntfStatEntry,_I:eltMesIssIpDbIntfStatIndex,'eltMesIssIpDbIntfStatNoOfStaticBindings':eltMesIssIpDbIntfStatNoOfStaticBindings,'eltMesIssIpDbIntfStatNoOfDHCPBindings':eltMesIssIpDbIntfStatNoOfDHCPBindings,'eltMesIssIpDbSrcGuardVlanTable':eltMesIssIpDbSrcGuardVlanTable,'eltMesIssIpDbSrcGuardVlanEntry':eltMesIssIpDbSrcGuardVlanEntry,_K:eltMesIssIpDbSrcGuardVlanId,'eltMesIssIpDbSrcGuardVlanStatus':eltMesIssIpDbSrcGuardVlanStatus,'eltMesIssIpDbv6SrcGuardVlanStatus':eltMesIssIpDbv6SrcGuardVlanStatus,'eltMesIssIpDbBinding':eltMesIssIpDbBinding,'eltMesIssIpDbBindingTable':eltMesIssIpDbBindingTable,_N:eltMesIssIpDbBindingEntry,'eltMesIssIpDbBindingEntryClearFlag':eltMesIssIpDbBindingEntryClearFlag,'eltMesIssIpDbBindingDynamicEntriesPortDownAction':eltMesIssIpDbBindingDynamicEntriesPortDownAction,'eltMesIssIpDbv6Binding':eltMesIssIpDbv6Binding,'eltMesIssIpDbv6BindingTable':eltMesIssIpDbv6BindingTable,_O:eltMesIssIpDbv6BindingEntry,'eltMesIssIpDbv6BindingEntryClearFlag':eltMesIssIpDbv6BindingEntryClearFlag,'eltMesIssIpDbNotifications':eltMesIssIpDbNotifications})