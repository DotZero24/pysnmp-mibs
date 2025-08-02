_d='rcL2cpPortVlanCfgVlanIndex'
_c='rcL2cpPortVlanCfgPortIndex'
_b='rcL2cpStatsProtocolIndex'
_a='rcL2cpStatsPortIndex'
_Z='rcL2cpPortIndex'
_Y='forward'
_X='daMac0180-C200-0020to2f'
_W='daMac0180-C200-000f'
_V='daMac0180-C200-000d'
_U='daMac0180-C200-000c'
_T='daMac0180-C200-000b'
_S='daMac0180-C200-000a'
_R='daMac0180-C200-0009'
_Q='daMac0180-C200-0008'
_P='daMac0180-C200-0006'
_O='daMac0180-C200-0005'
_N='daMac0180-C200-0004'
_M='slow-protocol'
_L='rcL2cpProfileActionProtocolIndex'
_K='rcL2cpProfileActionProfileIndex'
_J='read-only'
_I='read-create'
_H='rcL2cpProfileNumber'
_G='OctetString'
_F='EnableVar'
_E='not-accessible'
_D='read-write'
_C='RAISECOM-L2CP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_F)
rcL2cp=ModuleIdentity((1,3,6,1,4,1,8886,6,1,71))
if mibBuilder.loadTexts:rcL2cp.setRevisions(('2012-05-25 00:00',))
_RcL2cpGrobal_ObjectIdentity=ObjectIdentity
rcL2cpGrobal=_RcL2cpGrobal_ObjectIdentity((1,3,6,1,4,1,8886,6,1,71,1))
class _RcL2cpEnable_Type(EnableVar):defaultValue=2
_RcL2cpEnable_Type.__name__=_F
_RcL2cpEnable_Object=MibScalar
rcL2cpEnable=_RcL2cpEnable_Object((1,3,6,1,4,1,8886,6,1,71,1,1),_RcL2cpEnable_Type())
rcL2cpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpEnable.setStatus(_A)
_RcL2cpMacAddress_Type=MacAddress
_RcL2cpMacAddress_Object=MibScalar
rcL2cpMacAddress=_RcL2cpMacAddress_Object((1,3,6,1,4,1,8886,6,1,71,1,2),_RcL2cpMacAddress_Type())
rcL2cpMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpMacAddress.setStatus(_A)
_RcL2cpProfileTable_Object=MibTable
rcL2cpProfileTable=_RcL2cpProfileTable_Object((1,3,6,1,4,1,8886,6,1,71,2))
if mibBuilder.loadTexts:rcL2cpProfileTable.setStatus(_A)
_RcL2cpProfileEntry_Object=MibTableRow
rcL2cpProfileEntry=_RcL2cpProfileEntry_Object((1,3,6,1,4,1,8886,6,1,71,2,1))
rcL2cpProfileEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:rcL2cpProfileEntry.setStatus(_A)
class _RcL2cpProfileNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,19))
_RcL2cpProfileNumber_Type.__name__=_B
_RcL2cpProfileNumber_Object=MibTableColumn
rcL2cpProfileNumber=_RcL2cpProfileNumber_Object((1,3,6,1,4,1,8886,6,1,71,2,1,1),_RcL2cpProfileNumber_Type())
rcL2cpProfileNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpProfileNumber.setStatus(_A)
class _RcL2cpProfileDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcL2cpProfileDescription_Type.__name__=_G
_RcL2cpProfileDescription_Object=MibTableColumn
rcL2cpProfileDescription=_RcL2cpProfileDescription_Object((1,3,6,1,4,1,8886,6,1,71,2,1,2),_RcL2cpProfileDescription_Type())
rcL2cpProfileDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:rcL2cpProfileDescription.setStatus(_A)
_RcL2cpProfileRef_Type=Gauge32
_RcL2cpProfileRef_Object=MibTableColumn
rcL2cpProfileRef=_RcL2cpProfileRef_Object((1,3,6,1,4,1,8886,6,1,71,2,1,3),_RcL2cpProfileRef_Type())
rcL2cpProfileRef.setMaxAccess(_J)
if mibBuilder.loadTexts:rcL2cpProfileRef.setStatus(_A)
_RcL2cpProfileStatus_Type=RowStatus
_RcL2cpProfileStatus_Object=MibTableColumn
rcL2cpProfileStatus=_RcL2cpProfileStatus_Object((1,3,6,1,4,1,8886,6,1,71,2,1,4),_RcL2cpProfileStatus_Type())
rcL2cpProfileStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:rcL2cpProfileStatus.setStatus(_A)
_RcL2cpProfileActionTable_Object=MibTable
rcL2cpProfileActionTable=_RcL2cpProfileActionTable_Object((1,3,6,1,4,1,8886,6,1,71,3))
if mibBuilder.loadTexts:rcL2cpProfileActionTable.setStatus(_A)
_RcL2cpProfileActionEntry_Object=MibTableRow
rcL2cpProfileActionEntry=_RcL2cpProfileActionEntry_Object((1,3,6,1,4,1,8886,6,1,71,3,1))
rcL2cpProfileActionEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:rcL2cpProfileActionEntry.setStatus(_A)
class _RcL2cpProfileActionProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,19))
_RcL2cpProfileActionProfileIndex_Type.__name__=_B
_RcL2cpProfileActionProfileIndex_Object=MibTableColumn
rcL2cpProfileActionProfileIndex=_RcL2cpProfileActionProfileIndex_Object((1,3,6,1,4,1,8886,6,1,71,3,1,1),_RcL2cpProfileActionProfileIndex_Type())
rcL2cpProfileActionProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpProfileActionProfileIndex.setStatus(_A)
class _RcL2cpProfileActionProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('stp',1),(_M,2),('dot1x',3),('elmi',4),('lldp',5),('sisco',6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14),(_V,15),(_W,16),(_X,17),('lacp',18),('lamp',19),('link-oam',20),('esmc',21)))
_RcL2cpProfileActionProtocolIndex_Type.__name__=_B
_RcL2cpProfileActionProtocolIndex_Object=MibTableColumn
rcL2cpProfileActionProtocolIndex=_RcL2cpProfileActionProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,71,3,1,2),_RcL2cpProfileActionProtocolIndex_Type())
rcL2cpProfileActionProtocolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpProfileActionProtocolIndex.setStatus(_A)
class _RcL2cpProfileActionProtocolAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Y,0),('peer',1),('discard',2),('tunnel',3),('forward-statistics',4)))
_RcL2cpProfileActionProtocolAction_Type.__name__=_B
_RcL2cpProfileActionProtocolAction_Object=MibTableColumn
rcL2cpProfileActionProtocolAction=_RcL2cpProfileActionProtocolAction_Object((1,3,6,1,4,1,8886,6,1,71,3,1,3),_RcL2cpProfileActionProtocolAction_Type())
rcL2cpProfileActionProtocolAction.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpProfileActionProtocolAction.setStatus(_A)
class _RcL2cpProfileActionProtocolCos_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_RcL2cpProfileActionProtocolCos_Type.__name__=_B
_RcL2cpProfileActionProtocolCos_Object=MibTableColumn
rcL2cpProfileActionProtocolCos=_RcL2cpProfileActionProtocolCos_Object((1,3,6,1,4,1,8886,6,1,71,3,1,4),_RcL2cpProfileActionProtocolCos_Type())
rcL2cpProfileActionProtocolCos.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpProfileActionProtocolCos.setStatus(_A)
_RcL2cpPortCfgTable_Object=MibTable
rcL2cpPortCfgTable=_RcL2cpPortCfgTable_Object((1,3,6,1,4,1,8886,6,1,71,4))
if mibBuilder.loadTexts:rcL2cpPortCfgTable.setStatus(_A)
_RcL2cpPortCfgEntry_Object=MibTableRow
rcL2cpPortCfgEntry=_RcL2cpPortCfgEntry_Object((1,3,6,1,4,1,8886,6,1,71,4,1))
rcL2cpPortCfgEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:rcL2cpPortCfgEntry.setStatus(_A)
_RcL2cpPortIndex_Type=InterfaceIndex
_RcL2cpPortIndex_Object=MibTableColumn
rcL2cpPortIndex=_RcL2cpPortIndex_Object((1,3,6,1,4,1,8886,6,1,71,4,1,1),_RcL2cpPortIndex_Type())
rcL2cpPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpPortIndex.setStatus(_A)
class _RcL2cpPortProfileID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_RcL2cpPortProfileID_Type.__name__=_B
_RcL2cpPortProfileID_Object=MibTableColumn
rcL2cpPortProfileID=_RcL2cpPortProfileID_Object((1,3,6,1,4,1,8886,6,1,71,4,1,2),_RcL2cpPortProfileID_Type())
rcL2cpPortProfileID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpPortProfileID.setStatus(_A)
class _RcL2cpPortTerminal_Type(EnableVar):defaultValue=2
_RcL2cpPortTerminal_Type.__name__=_F
_RcL2cpPortTerminal_Object=MibTableColumn
rcL2cpPortTerminal=_RcL2cpPortTerminal_Object((1,3,6,1,4,1,8886,6,1,71,4,1,3),_RcL2cpPortTerminal_Type())
rcL2cpPortTerminal.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpPortTerminal.setStatus(_A)
class _RcL2cpPortClearStats_Type(EnableVar):defaultValue=2
_RcL2cpPortClearStats_Type.__name__=_F
_RcL2cpPortClearStats_Object=MibTableColumn
rcL2cpPortClearStats=_RcL2cpPortClearStats_Object((1,3,6,1,4,1,8886,6,1,71,4,1,4),_RcL2cpPortClearStats_Type())
rcL2cpPortClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpPortClearStats.setStatus(_A)
_RcL2cpStatsTable_Object=MibTable
rcL2cpStatsTable=_RcL2cpStatsTable_Object((1,3,6,1,4,1,8886,6,1,71,5))
if mibBuilder.loadTexts:rcL2cpStatsTable.setStatus(_A)
_RcL2cpStatsEntry_Object=MibTableRow
rcL2cpStatsEntry=_RcL2cpStatsEntry_Object((1,3,6,1,4,1,8886,6,1,71,5,1))
rcL2cpStatsEntry.setIndexNames((0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:rcL2cpStatsEntry.setStatus(_A)
_RcL2cpStatsPortIndex_Type=InterfaceIndex
_RcL2cpStatsPortIndex_Object=MibTableColumn
rcL2cpStatsPortIndex=_RcL2cpStatsPortIndex_Object((1,3,6,1,4,1,8886,6,1,71,5,1,1),_RcL2cpStatsPortIndex_Type())
rcL2cpStatsPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpStatsPortIndex.setStatus(_A)
class _RcL2cpStatsProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('stp',1),(_M,2),('dot1x',3),('elmi',4),('lldp',5),('sisco',6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14),(_V,15),(_W,16),(_X,17)))
_RcL2cpStatsProtocolIndex_Type.__name__=_B
_RcL2cpStatsProtocolIndex_Object=MibTableColumn
rcL2cpStatsProtocolIndex=_RcL2cpStatsProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,71,5,1,2),_RcL2cpStatsProtocolIndex_Type())
rcL2cpStatsProtocolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpStatsProtocolIndex.setStatus(_A)
_RcL2cpStatsProtocolStats_Type=Counter32
_RcL2cpStatsProtocolStats_Object=MibTableColumn
rcL2cpStatsProtocolStats=_RcL2cpStatsProtocolStats_Object((1,3,6,1,4,1,8886,6,1,71,5,1,3),_RcL2cpStatsProtocolStats_Type())
rcL2cpStatsProtocolStats.setMaxAccess(_J)
if mibBuilder.loadTexts:rcL2cpStatsProtocolStats.setStatus(_A)
_RcL2cpPortVlanCfgTable_Object=MibTable
rcL2cpPortVlanCfgTable=_RcL2cpPortVlanCfgTable_Object((1,3,6,1,4,1,8886,6,1,71,6))
if mibBuilder.loadTexts:rcL2cpPortVlanCfgTable.setStatus(_A)
_RcL2cpPortVlanCfgEntry_Object=MibTableRow
rcL2cpPortVlanCfgEntry=_RcL2cpPortVlanCfgEntry_Object((1,3,6,1,4,1,8886,6,1,71,6,1))
rcL2cpPortVlanCfgEntry.setIndexNames((0,_C,_c),(0,_C,_d))
if mibBuilder.loadTexts:rcL2cpPortVlanCfgEntry.setStatus(_A)
_RcL2cpPortVlanCfgPortIndex_Type=InterfaceIndex
_RcL2cpPortVlanCfgPortIndex_Object=MibTableColumn
rcL2cpPortVlanCfgPortIndex=_RcL2cpPortVlanCfgPortIndex_Object((1,3,6,1,4,1,8886,6,1,71,6,1,1),_RcL2cpPortVlanCfgPortIndex_Type())
rcL2cpPortVlanCfgPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpPortVlanCfgPortIndex.setStatus(_A)
class _RcL2cpPortVlanCfgVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcL2cpPortVlanCfgVlanIndex_Type.__name__=_B
_RcL2cpPortVlanCfgVlanIndex_Object=MibTableColumn
rcL2cpPortVlanCfgVlanIndex=_RcL2cpPortVlanCfgVlanIndex_Object((1,3,6,1,4,1,8886,6,1,71,6,1,2),_RcL2cpPortVlanCfgVlanIndex_Type())
rcL2cpPortVlanCfgVlanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL2cpPortVlanCfgVlanIndex.setStatus(_A)
class _RcL2cpPortVlanCfgL2cpProcess_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),('peer',1)))
_RcL2cpPortVlanCfgL2cpProcess_Type.__name__=_B
_RcL2cpPortVlanCfgL2cpProcess_Object=MibTableColumn
rcL2cpPortVlanCfgL2cpProcess=_RcL2cpPortVlanCfgL2cpProcess_Object((1,3,6,1,4,1,8886,6,1,71,6,1,3),_RcL2cpPortVlanCfgL2cpProcess_Type())
rcL2cpPortVlanCfgL2cpProcess.setMaxAccess(_D)
if mibBuilder.loadTexts:rcL2cpPortVlanCfgL2cpProcess.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcL2cp':rcL2cp,'rcL2cpGrobal':rcL2cpGrobal,'rcL2cpEnable':rcL2cpEnable,'rcL2cpMacAddress':rcL2cpMacAddress,'rcL2cpProfileTable':rcL2cpProfileTable,'rcL2cpProfileEntry':rcL2cpProfileEntry,_H:rcL2cpProfileNumber,'rcL2cpProfileDescription':rcL2cpProfileDescription,'rcL2cpProfileRef':rcL2cpProfileRef,'rcL2cpProfileStatus':rcL2cpProfileStatus,'rcL2cpProfileActionTable':rcL2cpProfileActionTable,'rcL2cpProfileActionEntry':rcL2cpProfileActionEntry,_K:rcL2cpProfileActionProfileIndex,_L:rcL2cpProfileActionProtocolIndex,'rcL2cpProfileActionProtocolAction':rcL2cpProfileActionProtocolAction,'rcL2cpProfileActionProtocolCos':rcL2cpProfileActionProtocolCos,'rcL2cpPortCfgTable':rcL2cpPortCfgTable,'rcL2cpPortCfgEntry':rcL2cpPortCfgEntry,_Z:rcL2cpPortIndex,'rcL2cpPortProfileID':rcL2cpPortProfileID,'rcL2cpPortTerminal':rcL2cpPortTerminal,'rcL2cpPortClearStats':rcL2cpPortClearStats,'rcL2cpStatsTable':rcL2cpStatsTable,'rcL2cpStatsEntry':rcL2cpStatsEntry,_a:rcL2cpStatsPortIndex,_b:rcL2cpStatsProtocolIndex,'rcL2cpStatsProtocolStats':rcL2cpStatsProtocolStats,'rcL2cpPortVlanCfgTable':rcL2cpPortVlanCfgTable,'rcL2cpPortVlanCfgEntry':rcL2cpPortVlanCfgEntry,_c:rcL2cpPortVlanCfgPortIndex,_d:rcL2cpPortVlanCfgVlanIndex,'rcL2cpPortVlanCfgL2cpProcess':rcL2cpPortVlanCfgL2cpProcess})