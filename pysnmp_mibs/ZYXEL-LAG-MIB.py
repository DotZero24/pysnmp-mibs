_G='zyAggregationGroupIndex'
_F='ZYXEL-LAG-MIB'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelLinkAggregation=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,42))
_ZyxelAggregationSetup_ObjectIdentity=ObjectIdentity
zyxelAggregationSetup=_ZyxelAggregationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,42,1))
_ZyAggregationState_Type=EnabledStatus
_ZyAggregationState_Object=MibScalar
zyAggregationState=_ZyAggregationState_Object((1,3,6,1,4,1,890,1,15,3,42,1,1),_ZyAggregationState_Type())
zyAggregationState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationState.setStatus(_A)
_ZyAggregationSysPriority_Type=Integer32
_ZyAggregationSysPriority_Object=MibScalar
zyAggregationSysPriority=_ZyAggregationSysPriority_Object((1,3,6,1,4,1,890,1,15,3,42,1,2),_ZyAggregationSysPriority_Type())
zyAggregationSysPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationSysPriority.setStatus(_A)
_ZyxelAggregationGroupTable_Object=MibTable
zyxelAggregationGroupTable=_ZyxelAggregationGroupTable_Object((1,3,6,1,4,1,890,1,15,3,42,1,3))
if mibBuilder.loadTexts:zyxelAggregationGroupTable.setStatus(_A)
_ZyxelAggregationGroupEntry_Object=MibTableRow
zyxelAggregationGroupEntry=_ZyxelAggregationGroupEntry_Object((1,3,6,1,4,1,890,1,15,3,42,1,3,1))
zyxelAggregationGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelAggregationGroupEntry.setStatus(_A)
_ZyAggregationGroupIndex_Type=Integer32
_ZyAggregationGroupIndex_Object=MibTableColumn
zyAggregationGroupIndex=_ZyAggregationGroupIndex_Object((1,3,6,1,4,1,890,1,15,3,42,1,3,1,1),_ZyAggregationGroupIndex_Type())
zyAggregationGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyAggregationGroupIndex.setStatus(_A)
_ZyAggregationGroupState_Type=EnabledStatus
_ZyAggregationGroupState_Object=MibTableColumn
zyAggregationGroupState=_ZyAggregationGroupState_Object((1,3,6,1,4,1,890,1,15,3,42,1,3,1,2),_ZyAggregationGroupState_Type())
zyAggregationGroupState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationGroupState.setStatus(_A)
_ZyAggregationGroupDynamicState_Type=EnabledStatus
_ZyAggregationGroupDynamicState_Object=MibTableColumn
zyAggregationGroupDynamicState=_ZyAggregationGroupDynamicState_Object((1,3,6,1,4,1,890,1,15,3,42,1,3,1,3),_ZyAggregationGroupDynamicState_Type())
zyAggregationGroupDynamicState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationGroupDynamicState.setStatus(_A)
class _ZyAggregationGroupCriteria_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('srcMac',1),('dstMac',2),('srcDstMac',3),('srcIp',4),('dstIp',5),('srcDstIp',6)))
_ZyAggregationGroupCriteria_Type.__name__=_C
_ZyAggregationGroupCriteria_Object=MibTableColumn
zyAggregationGroupCriteria=_ZyAggregationGroupCriteria_Object((1,3,6,1,4,1,890,1,15,3,42,1,3,1,4),_ZyAggregationGroupCriteria_Type())
zyAggregationGroupCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationGroupCriteria.setStatus(_A)
_ZyxelAggregationPortTable_Object=MibTable
zyxelAggregationPortTable=_ZyxelAggregationPortTable_Object((1,3,6,1,4,1,890,1,15,3,42,1,4))
if mibBuilder.loadTexts:zyxelAggregationPortTable.setStatus(_A)
_ZyxelAggregationPortEntry_Object=MibTableRow
zyxelAggregationPortEntry=_ZyxelAggregationPortEntry_Object((1,3,6,1,4,1,890,1,15,3,42,1,4,1))
zyxelAggregationPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelAggregationPortEntry.setStatus(_A)
class _ZyAggregationPortGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48)));namedValues=NamedValues(*(('none',0),('t1',1),('t2',2),('t3',3),('t4',4),('t5',5),('t6',6),('t7',7),('t8',8),('t9',9),('t10',10),('t11',11),('t12',12),('t13',13),('t14',14),('t15',15),('t16',16),('t17',17),('t18',18),('t19',19),('t20',20),('t21',21),('t22',22),('t23',23),('t24',24),('t25',25),('t26',26),('t27',27),('t28',28),('t29',29),('t30',30),('t31',31),('t32',32),('t33',33),('t34',34),('t35',35),('t36',36),('t37',37),('t38',38),('t39',39),('t40',40),('t41',41),('t42',42),('t43',43),('t44',44),('t45',45),('t46',46),('t47',47),('t48',48)))
_ZyAggregationPortGroup_Type.__name__=_C
_ZyAggregationPortGroup_Object=MibTableColumn
zyAggregationPortGroup=_ZyAggregationPortGroup_Object((1,3,6,1,4,1,890,1,15,3,42,1,4,1,1),_ZyAggregationPortGroup_Type())
zyAggregationPortGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationPortGroup.setStatus(_A)
_ZyAggregationPortDynamicStateTimeout_Type=Integer32
_ZyAggregationPortDynamicStateTimeout_Object=MibTableColumn
zyAggregationPortDynamicStateTimeout=_ZyAggregationPortDynamicStateTimeout_Object((1,3,6,1,4,1,890,1,15,3,42,1,4,1,2),_ZyAggregationPortDynamicStateTimeout_Type())
zyAggregationPortDynamicStateTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAggregationPortDynamicStateTimeout.setStatus(_A)
_ZyxelAggregationStatus_ObjectIdentity=ObjectIdentity
zyxelAggregationStatus=_ZyxelAggregationStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,42,2))
mibBuilder.exportSymbols(_F,**{'zyxelLinkAggregation':zyxelLinkAggregation,'zyxelAggregationSetup':zyxelAggregationSetup,'zyAggregationState':zyAggregationState,'zyAggregationSysPriority':zyAggregationSysPriority,'zyxelAggregationGroupTable':zyxelAggregationGroupTable,'zyxelAggregationGroupEntry':zyxelAggregationGroupEntry,_G:zyAggregationGroupIndex,'zyAggregationGroupState':zyAggregationGroupState,'zyAggregationGroupDynamicState':zyAggregationGroupDynamicState,'zyAggregationGroupCriteria':zyAggregationGroupCriteria,'zyxelAggregationPortTable':zyxelAggregationPortTable,'zyxelAggregationPortEntry':zyxelAggregationPortEntry,'zyAggregationPortGroup':zyAggregationPortGroup,'zyAggregationPortDynamicStateTimeout':zyAggregationPortDynamicStateTimeout,'zyxelAggregationStatus':zyxelAggregationStatus})