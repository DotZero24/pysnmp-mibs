_H='rcCpuProPortIndex'
_G='EnableVar'
_F='rcCpuProPacketIndex'
_E='read-only'
_D='read-write'
_C='SWITCH-CPUPRO-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_G)
rcCpuPro=ModuleIdentity((1,3,6,1,4,1,8886,6,1,60))
if mibBuilder.loadTexts:rcCpuPro.setRevisions(('2010-04-01 00:00',))
_RcCpuProGroup_ObjectIdentity=ObjectIdentity
rcCpuProGroup=_RcCpuProGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,60,1))
_RcCpuProPortTable_Object=MibTable
rcCpuProPortTable=_RcCpuProPortTable_Object((1,3,6,1,4,1,8886,6,1,60,1,1))
if mibBuilder.loadTexts:rcCpuProPortTable.setStatus(_A)
_RcCpuProPortEntry_Object=MibTableRow
rcCpuProPortEntry=_RcCpuProPortEntry_Object((1,3,6,1,4,1,8886,6,1,60,1,1,1))
rcCpuProPortEntry.setIndexNames((0,_C,_H),(0,_C,_F))
if mibBuilder.loadTexts:rcCpuProPortEntry.setStatus(_A)
_RcCpuProPortIndex_Type=Integer32
_RcCpuProPortIndex_Object=MibTableColumn
rcCpuProPortIndex=_RcCpuProPortIndex_Object((1,3,6,1,4,1,8886,6,1,60,1,1,1,1),_RcCpuProPortIndex_Type())
rcCpuProPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcCpuProPortIndex.setStatus(_A)
class _RcCpuProPortPacketEnable_Type(EnableVar):defaultValue=2
_RcCpuProPortPacketEnable_Type.__name__=_G
_RcCpuProPortPacketEnable_Object=MibTableColumn
rcCpuProPortPacketEnable=_RcCpuProPortPacketEnable_Object((1,3,6,1,4,1,8886,6,1,60,1,1,1,2),_RcCpuProPortPacketEnable_Type())
rcCpuProPortPacketEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcCpuProPortPacketEnable.setStatus(_A)
class _RcCpuProPortPacketAttackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('attacking',1),('not-attacking',2)))
_RcCpuProPortPacketAttackStatus_Type.__name__=_B
_RcCpuProPortPacketAttackStatus_Object=MibTableColumn
rcCpuProPortPacketAttackStatus=_RcCpuProPortPacketAttackStatus_Object((1,3,6,1,4,1,8886,6,1,60,1,1,1,3),_RcCpuProPortPacketAttackStatus_Type())
rcCpuProPortPacketAttackStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCpuProPortPacketAttackStatus.setStatus(_A)
_RcCpuProPortPacketAttackedCount_Type=Counter32
_RcCpuProPortPacketAttackedCount_Object=MibTableColumn
rcCpuProPortPacketAttackedCount=_RcCpuProPortPacketAttackedCount_Object((1,3,6,1,4,1,8886,6,1,60,1,1,1,4),_RcCpuProPortPacketAttackedCount_Type())
rcCpuProPortPacketAttackedCount.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCpuProPortPacketAttackedCount.setStatus(_A)
_RcCpuProPacketTable_Object=MibTable
rcCpuProPacketTable=_RcCpuProPacketTable_Object((1,3,6,1,4,1,8886,6,1,60,1,2))
if mibBuilder.loadTexts:rcCpuProPacketTable.setStatus(_A)
_RcCpuProPacketEntry_Object=MibTableRow
rcCpuProPacketEntry=_RcCpuProPacketEntry_Object((1,3,6,1,4,1,8886,6,1,60,1,2,1))
rcCpuProPacketEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:rcCpuProPacketEntry.setStatus(_A)
class _RcCpuProPacketIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bpdu',1),('arp',2),('icmp',3)))
_RcCpuProPacketIndex_Type.__name__=_B
_RcCpuProPacketIndex_Object=MibTableColumn
rcCpuProPacketIndex=_RcCpuProPacketIndex_Object((1,3,6,1,4,1,8886,6,1,60,1,2,1,1),_RcCpuProPacketIndex_Type())
rcCpuProPacketIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCpuProPacketIndex.setStatus(_A)
class _RcCpuProPacketInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcCpuProPacketInterval_Type.__name__=_B
_RcCpuProPacketInterval_Object=MibTableColumn
rcCpuProPacketInterval=_RcCpuProPacketInterval_Object((1,3,6,1,4,1,8886,6,1,60,1,2,1,2),_RcCpuProPacketInterval_Type())
rcCpuProPacketInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rcCpuProPacketInterval.setStatus(_A)
class _RcCpuProPacketHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65535))
_RcCpuProPacketHigh_Type.__name__=_B
_RcCpuProPacketHigh_Object=MibTableColumn
rcCpuProPacketHigh=_RcCpuProPacketHigh_Object((1,3,6,1,4,1,8886,6,1,60,1,2,1,3),_RcCpuProPacketHigh_Type())
rcCpuProPacketHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:rcCpuProPacketHigh.setStatus(_A)
class _RcCpuProPacketLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcCpuProPacketLow_Type.__name__=_B
_RcCpuProPacketLow_Object=MibTableColumn
rcCpuProPacketLow=_RcCpuProPacketLow_Object((1,3,6,1,4,1,8886,6,1,60,1,2,1,4),_RcCpuProPacketLow_Type())
rcCpuProPacketLow.setMaxAccess(_D)
if mibBuilder.loadTexts:rcCpuProPacketLow.setStatus(_A)
class _RcCpuProPacketAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('shutdown',1),('filter',2),('deny',3)))
_RcCpuProPacketAction_Type.__name__=_B
_RcCpuProPacketAction_Object=MibTableColumn
rcCpuProPacketAction=_RcCpuProPacketAction_Object((1,3,6,1,4,1,8886,6,1,60,1,2,1,5),_RcCpuProPacketAction_Type())
rcCpuProPacketAction.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCpuProPacketAction.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcCpuPro':rcCpuPro,'rcCpuProGroup':rcCpuProGroup,'rcCpuProPortTable':rcCpuProPortTable,'rcCpuProPortEntry':rcCpuProPortEntry,_H:rcCpuProPortIndex,'rcCpuProPortPacketEnable':rcCpuProPortPacketEnable,'rcCpuProPortPacketAttackStatus':rcCpuProPortPacketAttackStatus,'rcCpuProPortPacketAttackedCount':rcCpuProPortPacketAttackedCount,'rcCpuProPacketTable':rcCpuProPacketTable,'rcCpuProPacketEntry':rcCpuProPacketEntry,_F:rcCpuProPacketIndex,'rcCpuProPacketInterval':rcCpuProPacketInterval,'rcCpuProPacketHigh':rcCpuProPacketHigh,'rcCpuProPacketLow':rcCpuProPacketLow,'rcCpuProPacketAction':rcCpuProPacketAction})