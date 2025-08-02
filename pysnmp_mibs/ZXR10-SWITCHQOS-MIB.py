_P='zxr10AclQosTrafficStatisticsRuleId'
_O='zxr10AclQosTrafficStatisticsAclNo'
_N='zxr10AclQosRedirectRuleId'
_M='zxr10AclQosRedirectAclNo'
_L='zxr10AclQosTrafficMirrorRuleId'
_K='zxr10AclQosTrafficMirrorAclNo'
_J='zxr10AclQosTrafficLimitRuleId'
_I='zxr10AclQosTrafficLimitAclNo'
_H='zxr10AclQosPriorityMarkRuleId'
_G='zxr10AclQosPriorityMarkAclNo'
_F='interface'
_E='DisplayString'
_D='ZXR10-SWITCHQOS-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
class DisplayString(OctetString):0
class TrafficDropPriority(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('low',0),('medium',1),('high',2)))
class TrafficColorMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('blind',0),('aware',1)))
class TrafficForward(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('forwardRed',1))
class TrafficDrop(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('dropYellow',1))
class TrafficMirrorAction(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cpu',1),(_F,2)))
class RedirectFlag(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cpu',1),(_F,2),('next-hop',3),('next-hop-ipv6',4)))
class Packettype(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('red',1),('yellow',2),('green',3)))
class Statisticstype(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('packet',0),('byte',1)))
class GreenOnlyType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('green-only',1))
class InetAddressIPv6(TextualConvention,OctetString):status=_A;displayHint='2x:2x:2x:2x:2x:2x:2x:2x%4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10switch_ObjectIdentity=ObjectIdentity
zxr10switch=_Zxr10switch_ObjectIdentity((1,3,6,1,4,1,3902,3,102))
_Zxr10swqos_ObjectIdentity=ObjectIdentity
zxr10swqos=_Zxr10swqos_ObjectIdentity((1,3,6,1,4,1,3902,3,102,3))
_Zxr10AclQosPriorityMarkTable_Object=MibTable
zxr10AclQosPriorityMarkTable=_Zxr10AclQosPriorityMarkTable_Object((1,3,6,1,4,1,3902,3,102,3,1))
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkTable.setStatus(_A)
_Zxr10AclQosPriorityMarkEntry_Object=MibTableRow
zxr10AclQosPriorityMarkEntry=_Zxr10AclQosPriorityMarkEntry_Object((1,3,6,1,4,1,3902,3,102,3,1,1))
zxr10AclQosPriorityMarkEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkEntry.setStatus(_A)
_Zxr10AclQosPriorityMarkAclNo_Type=Integer32
_Zxr10AclQosPriorityMarkAclNo_Object=MibTableColumn
zxr10AclQosPriorityMarkAclNo=_Zxr10AclQosPriorityMarkAclNo_Object((1,3,6,1,4,1,3902,3,102,3,1,1,1),_Zxr10AclQosPriorityMarkAclNo_Type())
zxr10AclQosPriorityMarkAclNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkAclNo.setStatus(_A)
_Zxr10AclQosPriorityMarkRuleId_Type=Integer32
_Zxr10AclQosPriorityMarkRuleId_Object=MibTableColumn
zxr10AclQosPriorityMarkRuleId=_Zxr10AclQosPriorityMarkRuleId_Object((1,3,6,1,4,1,3902,3,102,3,1,1,2),_Zxr10AclQosPriorityMarkRuleId_Type())
zxr10AclQosPriorityMarkRuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkRuleId.setStatus(_A)
_Zxr10AclQosPriorityMarkAclName_Type=DisplayString
_Zxr10AclQosPriorityMarkAclName_Object=MibTableColumn
zxr10AclQosPriorityMarkAclName=_Zxr10AclQosPriorityMarkAclName_Object((1,3,6,1,4,1,3902,3,102,3,1,1,3),_Zxr10AclQosPriorityMarkAclName_Type())
zxr10AclQosPriorityMarkAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkAclName.setStatus(_A)
_Zxr10AclQosPriorityMarkDscpValue_Type=Integer32
_Zxr10AclQosPriorityMarkDscpValue_Object=MibTableColumn
zxr10AclQosPriorityMarkDscpValue=_Zxr10AclQosPriorityMarkDscpValue_Object((1,3,6,1,4,1,3902,3,102,3,1,1,4),_Zxr10AclQosPriorityMarkDscpValue_Type())
zxr10AclQosPriorityMarkDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkDscpValue.setStatus(_A)
_Zxr10AclQosPriorityMarkCosValue_Type=Integer32
_Zxr10AclQosPriorityMarkCosValue_Object=MibTableColumn
zxr10AclQosPriorityMarkCosValue=_Zxr10AclQosPriorityMarkCosValue_Object((1,3,6,1,4,1,3902,3,102,3,1,1,5),_Zxr10AclQosPriorityMarkCosValue_Type())
zxr10AclQosPriorityMarkCosValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkCosValue.setStatus(_A)
_Zxr10AclQosPriorityMarkLocalPrecedence_Type=Integer32
_Zxr10AclQosPriorityMarkLocalPrecedence_Object=MibTableColumn
zxr10AclQosPriorityMarkLocalPrecedence=_Zxr10AclQosPriorityMarkLocalPrecedence_Object((1,3,6,1,4,1,3902,3,102,3,1,1,6),_Zxr10AclQosPriorityMarkLocalPrecedence_Type())
zxr10AclQosPriorityMarkLocalPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkLocalPrecedence.setStatus(_A)
_Zxr10AclQosPriorityMarkDropPrecedence_Type=TrafficDropPriority
_Zxr10AclQosPriorityMarkDropPrecedence_Object=MibTableColumn
zxr10AclQosPriorityMarkDropPrecedence=_Zxr10AclQosPriorityMarkDropPrecedence_Object((1,3,6,1,4,1,3902,3,102,3,1,1,7),_Zxr10AclQosPriorityMarkDropPrecedence_Type())
zxr10AclQosPriorityMarkDropPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkDropPrecedence.setStatus(_A)
_Zxr10AclQosPriorityMarkOuterVlanId_Type=Integer32
_Zxr10AclQosPriorityMarkOuterVlanId_Object=MibTableColumn
zxr10AclQosPriorityMarkOuterVlanId=_Zxr10AclQosPriorityMarkOuterVlanId_Object((1,3,6,1,4,1,3902,3,102,3,1,1,8),_Zxr10AclQosPriorityMarkOuterVlanId_Type())
zxr10AclQosPriorityMarkOuterVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkOuterVlanId.setStatus(_A)
_Zxr10AclQosPriorityMarkPrecedenceValue_Type=Integer32
_Zxr10AclQosPriorityMarkPrecedenceValue_Object=MibTableColumn
zxr10AclQosPriorityMarkPrecedenceValue=_Zxr10AclQosPriorityMarkPrecedenceValue_Object((1,3,6,1,4,1,3902,3,102,3,1,1,9),_Zxr10AclQosPriorityMarkPrecedenceValue_Type())
zxr10AclQosPriorityMarkPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkPrecedenceValue.setStatus(_A)
_Zxr10AclQosPriorityMarkRowStatus_Type=RowStatus
_Zxr10AclQosPriorityMarkRowStatus_Object=MibTableColumn
zxr10AclQosPriorityMarkRowStatus=_Zxr10AclQosPriorityMarkRowStatus_Object((1,3,6,1,4,1,3902,3,102,3,1,1,10),_Zxr10AclQosPriorityMarkRowStatus_Type())
zxr10AclQosPriorityMarkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosPriorityMarkRowStatus.setStatus(_A)
_Zxr10AclQosTrafficLimitTable_Object=MibTable
zxr10AclQosTrafficLimitTable=_Zxr10AclQosTrafficLimitTable_Object((1,3,6,1,4,1,3902,3,102,3,2))
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitTable.setStatus(_A)
_Zxr10AclQosTrafficLimitEntry_Object=MibTableRow
zxr10AclQosTrafficLimitEntry=_Zxr10AclQosTrafficLimitEntry_Object((1,3,6,1,4,1,3902,3,102,3,2,1))
zxr10AclQosTrafficLimitEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitEntry.setStatus(_A)
_Zxr10AclQosTrafficLimitAclNo_Type=Integer32
_Zxr10AclQosTrafficLimitAclNo_Object=MibTableColumn
zxr10AclQosTrafficLimitAclNo=_Zxr10AclQosTrafficLimitAclNo_Object((1,3,6,1,4,1,3902,3,102,3,2,1,1),_Zxr10AclQosTrafficLimitAclNo_Type())
zxr10AclQosTrafficLimitAclNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitAclNo.setStatus(_A)
_Zxr10AclQosTrafficLimitRuleId_Type=Integer32
_Zxr10AclQosTrafficLimitRuleId_Object=MibTableColumn
zxr10AclQosTrafficLimitRuleId=_Zxr10AclQosTrafficLimitRuleId_Object((1,3,6,1,4,1,3902,3,102,3,2,1,2),_Zxr10AclQosTrafficLimitRuleId_Type())
zxr10AclQosTrafficLimitRuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitRuleId.setStatus(_A)
_Zxr10AclQosTrafficLimitAclName_Type=DisplayString
_Zxr10AclQosTrafficLimitAclName_Object=MibTableColumn
zxr10AclQosTrafficLimitAclName=_Zxr10AclQosTrafficLimitAclName_Object((1,3,6,1,4,1,3902,3,102,3,2,1,3),_Zxr10AclQosTrafficLimitAclName_Type())
zxr10AclQosTrafficLimitAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitAclName.setStatus(_A)
_Zxr10AclQosTrafficLimitCir_Type=Integer32
_Zxr10AclQosTrafficLimitCir_Object=MibTableColumn
zxr10AclQosTrafficLimitCir=_Zxr10AclQosTrafficLimitCir_Object((1,3,6,1,4,1,3902,3,102,3,2,1,4),_Zxr10AclQosTrafficLimitCir_Type())
zxr10AclQosTrafficLimitCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitCir.setStatus(_A)
_Zxr10AclQosTrafficLimitCbs_Type=Integer32
_Zxr10AclQosTrafficLimitCbs_Object=MibTableColumn
zxr10AclQosTrafficLimitCbs=_Zxr10AclQosTrafficLimitCbs_Object((1,3,6,1,4,1,3902,3,102,3,2,1,5),_Zxr10AclQosTrafficLimitCbs_Type())
zxr10AclQosTrafficLimitCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitCbs.setStatus(_A)
_Zxr10AclQosTrafficLimitEbs_Type=Integer32
_Zxr10AclQosTrafficLimitEbs_Object=MibTableColumn
zxr10AclQosTrafficLimitEbs=_Zxr10AclQosTrafficLimitEbs_Object((1,3,6,1,4,1,3902,3,102,3,2,1,6),_Zxr10AclQosTrafficLimitEbs_Type())
zxr10AclQosTrafficLimitEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitEbs.setStatus(_A)
_Zxr10AclQosTrafficLimitPir_Type=Integer32
_Zxr10AclQosTrafficLimitPir_Object=MibTableColumn
zxr10AclQosTrafficLimitPir=_Zxr10AclQosTrafficLimitPir_Object((1,3,6,1,4,1,3902,3,102,3,2,1,7),_Zxr10AclQosTrafficLimitPir_Type())
zxr10AclQosTrafficLimitPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitPir.setStatus(_A)
_Zxr10AclQosTrafficLimitPbs_Type=Integer32
_Zxr10AclQosTrafficLimitPbs_Object=MibTableColumn
zxr10AclQosTrafficLimitPbs=_Zxr10AclQosTrafficLimitPbs_Object((1,3,6,1,4,1,3902,3,102,3,2,1,8),_Zxr10AclQosTrafficLimitPbs_Type())
zxr10AclQosTrafficLimitPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitPbs.setStatus(_A)
_Zxr10AclQosTrafficLimitMode_Type=TrafficColorMode
_Zxr10AclQosTrafficLimitMode_Object=MibTableColumn
zxr10AclQosTrafficLimitMode=_Zxr10AclQosTrafficLimitMode_Object((1,3,6,1,4,1,3902,3,102,3,2,1,9),_Zxr10AclQosTrafficLimitMode_Type())
zxr10AclQosTrafficLimitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitMode.setStatus(_A)
_Zxr10AclQosTrafficLimitRedDscpValue_Type=Integer32
_Zxr10AclQosTrafficLimitRedDscpValue_Object=MibTableColumn
zxr10AclQosTrafficLimitRedDscpValue=_Zxr10AclQosTrafficLimitRedDscpValue_Object((1,3,6,1,4,1,3902,3,102,3,2,1,10),_Zxr10AclQosTrafficLimitRedDscpValue_Type())
zxr10AclQosTrafficLimitRedDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitRedDscpValue.setStatus(_A)
_Zxr10AclQosTrafficLimitYelDscpValue_Type=Integer32
_Zxr10AclQosTrafficLimitYelDscpValue_Object=MibTableColumn
zxr10AclQosTrafficLimitYelDscpValue=_Zxr10AclQosTrafficLimitYelDscpValue_Object((1,3,6,1,4,1,3902,3,102,3,2,1,11),_Zxr10AclQosTrafficLimitYelDscpValue_Type())
zxr10AclQosTrafficLimitYelDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitYelDscpValue.setStatus(_A)
_Zxr10AclQosTrafficLimitRedDp_Type=TrafficDropPriority
_Zxr10AclQosTrafficLimitRedDp_Object=MibTableColumn
zxr10AclQosTrafficLimitRedDp=_Zxr10AclQosTrafficLimitRedDp_Object((1,3,6,1,4,1,3902,3,102,3,2,1,12),_Zxr10AclQosTrafficLimitRedDp_Type())
zxr10AclQosTrafficLimitRedDp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitRedDp.setStatus(_A)
_Zxr10AclQosTrafficLimitYelDp_Type=TrafficDropPriority
_Zxr10AclQosTrafficLimitYelDp_Object=MibTableColumn
zxr10AclQosTrafficLimitYelDp=_Zxr10AclQosTrafficLimitYelDp_Object((1,3,6,1,4,1,3902,3,102,3,2,1,13),_Zxr10AclQosTrafficLimitYelDp_Type())
zxr10AclQosTrafficLimitYelDp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitYelDp.setStatus(_A)
_Zxr10AclQosTrafficLimitForwadRed_Type=TrafficForward
_Zxr10AclQosTrafficLimitForwadRed_Object=MibTableColumn
zxr10AclQosTrafficLimitForwadRed=_Zxr10AclQosTrafficLimitForwadRed_Object((1,3,6,1,4,1,3902,3,102,3,2,1,14),_Zxr10AclQosTrafficLimitForwadRed_Type())
zxr10AclQosTrafficLimitForwadRed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitForwadRed.setStatus(_A)
_Zxr10AclQosTrafficLimitDropYellow_Type=TrafficDrop
_Zxr10AclQosTrafficLimitDropYellow_Object=MibTableColumn
zxr10AclQosTrafficLimitDropYellow=_Zxr10AclQosTrafficLimitDropYellow_Object((1,3,6,1,4,1,3902,3,102,3,2,1,15),_Zxr10AclQosTrafficLimitDropYellow_Type())
zxr10AclQosTrafficLimitDropYellow.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitDropYellow.setStatus(_A)
_Zxr10AclQosTrafficLimitRowStatus_Type=RowStatus
_Zxr10AclQosTrafficLimitRowStatus_Object=MibTableColumn
zxr10AclQosTrafficLimitRowStatus=_Zxr10AclQosTrafficLimitRowStatus_Object((1,3,6,1,4,1,3902,3,102,3,2,1,16),_Zxr10AclQosTrafficLimitRowStatus_Type())
zxr10AclQosTrafficLimitRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficLimitRowStatus.setStatus(_A)
_Zxr10AclQosTrafficMirrorTable_Object=MibTable
zxr10AclQosTrafficMirrorTable=_Zxr10AclQosTrafficMirrorTable_Object((1,3,6,1,4,1,3902,3,102,3,3))
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorTable.setStatus(_A)
_Zxr10AclQosTrafficMirrorEntry_Object=MibTableRow
zxr10AclQosTrafficMirrorEntry=_Zxr10AclQosTrafficMirrorEntry_Object((1,3,6,1,4,1,3902,3,102,3,3,1))
zxr10AclQosTrafficMirrorEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorEntry.setStatus(_A)
_Zxr10AclQosTrafficMirrorAclNo_Type=Integer32
_Zxr10AclQosTrafficMirrorAclNo_Object=MibTableColumn
zxr10AclQosTrafficMirrorAclNo=_Zxr10AclQosTrafficMirrorAclNo_Object((1,3,6,1,4,1,3902,3,102,3,3,1,1),_Zxr10AclQosTrafficMirrorAclNo_Type())
zxr10AclQosTrafficMirrorAclNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorAclNo.setStatus(_A)
_Zxr10AclQosTrafficMirrorRuleId_Type=Integer32
_Zxr10AclQosTrafficMirrorRuleId_Object=MibTableColumn
zxr10AclQosTrafficMirrorRuleId=_Zxr10AclQosTrafficMirrorRuleId_Object((1,3,6,1,4,1,3902,3,102,3,3,1,2),_Zxr10AclQosTrafficMirrorRuleId_Type())
zxr10AclQosTrafficMirrorRuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorRuleId.setStatus(_A)
_Zxr10AclQosTrafficMirrorAclName_Type=DisplayString
_Zxr10AclQosTrafficMirrorAclName_Object=MibTableColumn
zxr10AclQosTrafficMirrorAclName=_Zxr10AclQosTrafficMirrorAclName_Object((1,3,6,1,4,1,3902,3,102,3,3,1,3),_Zxr10AclQosTrafficMirrorAclName_Type())
zxr10AclQosTrafficMirrorAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorAclName.setStatus(_A)
_Zxr10AclQosTrafficMirrorAction_Type=TrafficMirrorAction
_Zxr10AclQosTrafficMirrorAction_Object=MibTableColumn
zxr10AclQosTrafficMirrorAction=_Zxr10AclQosTrafficMirrorAction_Object((1,3,6,1,4,1,3902,3,102,3,3,1,4),_Zxr10AclQosTrafficMirrorAction_Type())
zxr10AclQosTrafficMirrorAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorAction.setStatus(_A)
_Zxr10AclQosTrafficMirrorIfName_Type=DisplayString
_Zxr10AclQosTrafficMirrorIfName_Object=MibTableColumn
zxr10AclQosTrafficMirrorIfName=_Zxr10AclQosTrafficMirrorIfName_Object((1,3,6,1,4,1,3902,3,102,3,3,1,5),_Zxr10AclQosTrafficMirrorIfName_Type())
zxr10AclQosTrafficMirrorIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorIfName.setStatus(_A)
_Zxr10AclQosTrafficMirrorRowStatus_Type=RowStatus
_Zxr10AclQosTrafficMirrorRowStatus_Object=MibTableColumn
zxr10AclQosTrafficMirrorRowStatus=_Zxr10AclQosTrafficMirrorRowStatus_Object((1,3,6,1,4,1,3902,3,102,3,3,1,6),_Zxr10AclQosTrafficMirrorRowStatus_Type())
zxr10AclQosTrafficMirrorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficMirrorRowStatus.setStatus(_A)
_Zxr10AclQosRedirectTable_Object=MibTable
zxr10AclQosRedirectTable=_Zxr10AclQosRedirectTable_Object((1,3,6,1,4,1,3902,3,102,3,4))
if mibBuilder.loadTexts:zxr10AclQosRedirectTable.setStatus(_A)
_Zxr10AclQosRedirectEntry_Object=MibTableRow
zxr10AclQosRedirectEntry=_Zxr10AclQosRedirectEntry_Object((1,3,6,1,4,1,3902,3,102,3,4,1))
zxr10AclQosRedirectEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:zxr10AclQosRedirectEntry.setStatus(_A)
_Zxr10AclQosRedirectAclNo_Type=Integer32
_Zxr10AclQosRedirectAclNo_Object=MibTableColumn
zxr10AclQosRedirectAclNo=_Zxr10AclQosRedirectAclNo_Object((1,3,6,1,4,1,3902,3,102,3,4,1,1),_Zxr10AclQosRedirectAclNo_Type())
zxr10AclQosRedirectAclNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosRedirectAclNo.setStatus(_A)
_Zxr10AclQosRedirectRuleId_Type=Integer32
_Zxr10AclQosRedirectRuleId_Object=MibTableColumn
zxr10AclQosRedirectRuleId=_Zxr10AclQosRedirectRuleId_Object((1,3,6,1,4,1,3902,3,102,3,4,1,2),_Zxr10AclQosRedirectRuleId_Type())
zxr10AclQosRedirectRuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosRedirectRuleId.setStatus(_A)
_Zxr10AclQosRedirectAclName_Type=DisplayString
_Zxr10AclQosRedirectAclName_Object=MibTableColumn
zxr10AclQosRedirectAclName=_Zxr10AclQosRedirectAclName_Object((1,3,6,1,4,1,3902,3,102,3,4,1,3),_Zxr10AclQosRedirectAclName_Type())
zxr10AclQosRedirectAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosRedirectAclName.setStatus(_A)
_Zxr10AclQosRedirectFlag_Type=RedirectFlag
_Zxr10AclQosRedirectFlag_Object=MibTableColumn
zxr10AclQosRedirectFlag=_Zxr10AclQosRedirectFlag_Object((1,3,6,1,4,1,3902,3,102,3,4,1,4),_Zxr10AclQosRedirectFlag_Type())
zxr10AclQosRedirectFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectFlag.setStatus(_A)
_Zxr10AclQosRedirectGPort_Type=DisplayString
_Zxr10AclQosRedirectGPort_Object=MibTableColumn
zxr10AclQosRedirectGPort=_Zxr10AclQosRedirectGPort_Object((1,3,6,1,4,1,3902,3,102,3,4,1,5),_Zxr10AclQosRedirectGPort_Type())
zxr10AclQosRedirectGPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectGPort.setStatus(_A)
_Zxr10AclQosRedirectIpAddr1_Type=IpAddress
_Zxr10AclQosRedirectIpAddr1_Object=MibTableColumn
zxr10AclQosRedirectIpAddr1=_Zxr10AclQosRedirectIpAddr1_Object((1,3,6,1,4,1,3902,3,102,3,4,1,6),_Zxr10AclQosRedirectIpAddr1_Type())
zxr10AclQosRedirectIpAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr1.setStatus(_A)
_Zxr10AclQosRedirectIpPri1_Type=Integer32
_Zxr10AclQosRedirectIpPri1_Object=MibTableColumn
zxr10AclQosRedirectIpPri1=_Zxr10AclQosRedirectIpPri1_Object((1,3,6,1,4,1,3902,3,102,3,4,1,7),_Zxr10AclQosRedirectIpPri1_Type())
zxr10AclQosRedirectIpPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri1.setStatus(_A)
_Zxr10AclQosRedirectIpAddr2_Type=IpAddress
_Zxr10AclQosRedirectIpAddr2_Object=MibTableColumn
zxr10AclQosRedirectIpAddr2=_Zxr10AclQosRedirectIpAddr2_Object((1,3,6,1,4,1,3902,3,102,3,4,1,8),_Zxr10AclQosRedirectIpAddr2_Type())
zxr10AclQosRedirectIpAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr2.setStatus(_A)
_Zxr10AclQosRedirectIpPri2_Type=Integer32
_Zxr10AclQosRedirectIpPri2_Object=MibTableColumn
zxr10AclQosRedirectIpPri2=_Zxr10AclQosRedirectIpPri2_Object((1,3,6,1,4,1,3902,3,102,3,4,1,9),_Zxr10AclQosRedirectIpPri2_Type())
zxr10AclQosRedirectIpPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri2.setStatus(_A)
_Zxr10AclQosRedirectIpAddr3_Type=IpAddress
_Zxr10AclQosRedirectIpAddr3_Object=MibTableColumn
zxr10AclQosRedirectIpAddr3=_Zxr10AclQosRedirectIpAddr3_Object((1,3,6,1,4,1,3902,3,102,3,4,1,10),_Zxr10AclQosRedirectIpAddr3_Type())
zxr10AclQosRedirectIpAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr3.setStatus(_A)
_Zxr10AclQosRedirectIpPri3_Type=Integer32
_Zxr10AclQosRedirectIpPri3_Object=MibTableColumn
zxr10AclQosRedirectIpPri3=_Zxr10AclQosRedirectIpPri3_Object((1,3,6,1,4,1,3902,3,102,3,4,1,11),_Zxr10AclQosRedirectIpPri3_Type())
zxr10AclQosRedirectIpPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri3.setStatus(_A)
_Zxr10AclQosRedirectIpAddr4_Type=IpAddress
_Zxr10AclQosRedirectIpAddr4_Object=MibTableColumn
zxr10AclQosRedirectIpAddr4=_Zxr10AclQosRedirectIpAddr4_Object((1,3,6,1,4,1,3902,3,102,3,4,1,12),_Zxr10AclQosRedirectIpAddr4_Type())
zxr10AclQosRedirectIpAddr4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr4.setStatus(_A)
_Zxr10AclQosRedirectIpPri4_Type=Integer32
_Zxr10AclQosRedirectIpPri4_Object=MibTableColumn
zxr10AclQosRedirectIpPri4=_Zxr10AclQosRedirectIpPri4_Object((1,3,6,1,4,1,3902,3,102,3,4,1,13),_Zxr10AclQosRedirectIpPri4_Type())
zxr10AclQosRedirectIpPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri4.setStatus(_A)
_Zxr10AclQosRedirectIpAddr5_Type=IpAddress
_Zxr10AclQosRedirectIpAddr5_Object=MibTableColumn
zxr10AclQosRedirectIpAddr5=_Zxr10AclQosRedirectIpAddr5_Object((1,3,6,1,4,1,3902,3,102,3,4,1,14),_Zxr10AclQosRedirectIpAddr5_Type())
zxr10AclQosRedirectIpAddr5.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr5.setStatus(_A)
_Zxr10AclQosRedirectIpPri5_Type=Integer32
_Zxr10AclQosRedirectIpPri5_Object=MibTableColumn
zxr10AclQosRedirectIpPri5=_Zxr10AclQosRedirectIpPri5_Object((1,3,6,1,4,1,3902,3,102,3,4,1,15),_Zxr10AclQosRedirectIpPri5_Type())
zxr10AclQosRedirectIpPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri5.setStatus(_A)
_Zxr10AclQosRedirectIpAddr6_Type=IpAddress
_Zxr10AclQosRedirectIpAddr6_Object=MibTableColumn
zxr10AclQosRedirectIpAddr6=_Zxr10AclQosRedirectIpAddr6_Object((1,3,6,1,4,1,3902,3,102,3,4,1,16),_Zxr10AclQosRedirectIpAddr6_Type())
zxr10AclQosRedirectIpAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr6.setStatus(_A)
_Zxr10AclQosRedirectIpPri6_Type=Integer32
_Zxr10AclQosRedirectIpPri6_Object=MibTableColumn
zxr10AclQosRedirectIpPri6=_Zxr10AclQosRedirectIpPri6_Object((1,3,6,1,4,1,3902,3,102,3,4,1,17),_Zxr10AclQosRedirectIpPri6_Type())
zxr10AclQosRedirectIpPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri6.setStatus(_A)
_Zxr10AclQosRedirectIpAddr7_Type=IpAddress
_Zxr10AclQosRedirectIpAddr7_Object=MibTableColumn
zxr10AclQosRedirectIpAddr7=_Zxr10AclQosRedirectIpAddr7_Object((1,3,6,1,4,1,3902,3,102,3,4,1,18),_Zxr10AclQosRedirectIpAddr7_Type())
zxr10AclQosRedirectIpAddr7.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr7.setStatus(_A)
_Zxr10AclQosRedirectIpPri7_Type=Integer32
_Zxr10AclQosRedirectIpPri7_Object=MibTableColumn
zxr10AclQosRedirectIpPri7=_Zxr10AclQosRedirectIpPri7_Object((1,3,6,1,4,1,3902,3,102,3,4,1,19),_Zxr10AclQosRedirectIpPri7_Type())
zxr10AclQosRedirectIpPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri7.setStatus(_A)
_Zxr10AclQosRedirectIpAddr8_Type=IpAddress
_Zxr10AclQosRedirectIpAddr8_Object=MibTableColumn
zxr10AclQosRedirectIpAddr8=_Zxr10AclQosRedirectIpAddr8_Object((1,3,6,1,4,1,3902,3,102,3,4,1,20),_Zxr10AclQosRedirectIpAddr8_Type())
zxr10AclQosRedirectIpAddr8.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpAddr8.setStatus(_A)
_Zxr10AclQosRedirectIpPri8_Type=Integer32
_Zxr10AclQosRedirectIpPri8_Object=MibTableColumn
zxr10AclQosRedirectIpPri8=_Zxr10AclQosRedirectIpPri8_Object((1,3,6,1,4,1,3902,3,102,3,4,1,21),_Zxr10AclQosRedirectIpPri8_Type())
zxr10AclQosRedirectIpPri8.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIpPri8.setStatus(_A)
_Zxr10AclQosRedirectIPv6Addr_Type=InetAddressIPv6
_Zxr10AclQosRedirectIPv6Addr_Object=MibTableColumn
zxr10AclQosRedirectIPv6Addr=_Zxr10AclQosRedirectIPv6Addr_Object((1,3,6,1,4,1,3902,3,102,3,4,1,22),_Zxr10AclQosRedirectIPv6Addr_Type())
zxr10AclQosRedirectIPv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectIPv6Addr.setStatus(_A)
_Zxr10AclQosRedirectGreenOnly_Type=GreenOnlyType
_Zxr10AclQosRedirectGreenOnly_Object=MibTableColumn
zxr10AclQosRedirectGreenOnly=_Zxr10AclQosRedirectGreenOnly_Object((1,3,6,1,4,1,3902,3,102,3,4,1,23),_Zxr10AclQosRedirectGreenOnly_Type())
zxr10AclQosRedirectGreenOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectGreenOnly.setStatus(_A)
_Zxr10AclQosRedirectRowStatus_Type=RowStatus
_Zxr10AclQosRedirectRowStatus_Object=MibTableColumn
zxr10AclQosRedirectRowStatus=_Zxr10AclQosRedirectRowStatus_Object((1,3,6,1,4,1,3902,3,102,3,4,1,24),_Zxr10AclQosRedirectRowStatus_Type())
zxr10AclQosRedirectRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosRedirectRowStatus.setStatus(_A)
_Zxr10AclQosTrafficStatisticsTable_Object=MibTable
zxr10AclQosTrafficStatisticsTable=_Zxr10AclQosTrafficStatisticsTable_Object((1,3,6,1,4,1,3902,3,102,3,5))
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsTable.setStatus(_A)
_Zxr10AclQosTrafficStatisticsEntry_Object=MibTableRow
zxr10AclQosTrafficStatisticsEntry=_Zxr10AclQosTrafficStatisticsEntry_Object((1,3,6,1,4,1,3902,3,102,3,5,1))
zxr10AclQosTrafficStatisticsEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsEntry.setStatus(_A)
_Zxr10AclQosTrafficStatisticsAclNo_Type=Integer32
_Zxr10AclQosTrafficStatisticsAclNo_Object=MibTableColumn
zxr10AclQosTrafficStatisticsAclNo=_Zxr10AclQosTrafficStatisticsAclNo_Object((1,3,6,1,4,1,3902,3,102,3,5,1,1),_Zxr10AclQosTrafficStatisticsAclNo_Type())
zxr10AclQosTrafficStatisticsAclNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsAclNo.setStatus(_A)
_Zxr10AclQosTrafficStatisticsRuleId_Type=Integer32
_Zxr10AclQosTrafficStatisticsRuleId_Object=MibTableColumn
zxr10AclQosTrafficStatisticsRuleId=_Zxr10AclQosTrafficStatisticsRuleId_Object((1,3,6,1,4,1,3902,3,102,3,5,1,2),_Zxr10AclQosTrafficStatisticsRuleId_Type())
zxr10AclQosTrafficStatisticsRuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsRuleId.setStatus(_A)
_Zxr10AclQosTrafficStatisticsAclName_Type=DisplayString
_Zxr10AclQosTrafficStatisticsAclName_Object=MibTableColumn
zxr10AclQosTrafficStatisticsAclName=_Zxr10AclQosTrafficStatisticsAclName_Object((1,3,6,1,4,1,3902,3,102,3,5,1,3),_Zxr10AclQosTrafficStatisticsAclName_Type())
zxr10AclQosTrafficStatisticsAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsAclName.setStatus(_A)
_Zxr10AclQosTrafficStatisticsPkttype_Type=Packettype
_Zxr10AclQosTrafficStatisticsPkttype_Object=MibTableColumn
zxr10AclQosTrafficStatisticsPkttype=_Zxr10AclQosTrafficStatisticsPkttype_Object((1,3,6,1,4,1,3902,3,102,3,5,1,4),_Zxr10AclQosTrafficStatisticsPkttype_Type())
zxr10AclQosTrafficStatisticsPkttype.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsPkttype.setStatus(_A)
_Zxr10AclQosTrafficStatisticsStatype_Type=Statisticstype
_Zxr10AclQosTrafficStatisticsStatype_Object=MibTableColumn
zxr10AclQosTrafficStatisticsStatype=_Zxr10AclQosTrafficStatisticsStatype_Object((1,3,6,1,4,1,3902,3,102,3,5,1,5),_Zxr10AclQosTrafficStatisticsStatype_Type())
zxr10AclQosTrafficStatisticsStatype.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsStatype.setStatus(_A)
_Zxr10AclQosTrafficStatisticsRowStatus_Type=RowStatus
_Zxr10AclQosTrafficStatisticsRowStatus_Object=MibTableColumn
zxr10AclQosTrafficStatisticsRowStatus=_Zxr10AclQosTrafficStatisticsRowStatus_Object((1,3,6,1,4,1,3902,3,102,3,5,1,6),_Zxr10AclQosTrafficStatisticsRowStatus_Type())
zxr10AclQosTrafficStatisticsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10AclQosTrafficStatisticsRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_E:DisplayString,'TrafficDropPriority':TrafficDropPriority,'TrafficColorMode':TrafficColorMode,'TrafficForward':TrafficForward,'TrafficDrop':TrafficDrop,'TrafficMirrorAction':TrafficMirrorAction,'RedirectFlag':RedirectFlag,'Packettype':Packettype,'Statisticstype':Statisticstype,'GreenOnlyType':GreenOnlyType,'InetAddressIPv6':InetAddressIPv6,'zte':zte,'zxr10':zxr10,'zxr10switch':zxr10switch,'zxr10swqos':zxr10swqos,'zxr10AclQosPriorityMarkTable':zxr10AclQosPriorityMarkTable,'zxr10AclQosPriorityMarkEntry':zxr10AclQosPriorityMarkEntry,_G:zxr10AclQosPriorityMarkAclNo,_H:zxr10AclQosPriorityMarkRuleId,'zxr10AclQosPriorityMarkAclName':zxr10AclQosPriorityMarkAclName,'zxr10AclQosPriorityMarkDscpValue':zxr10AclQosPriorityMarkDscpValue,'zxr10AclQosPriorityMarkCosValue':zxr10AclQosPriorityMarkCosValue,'zxr10AclQosPriorityMarkLocalPrecedence':zxr10AclQosPriorityMarkLocalPrecedence,'zxr10AclQosPriorityMarkDropPrecedence':zxr10AclQosPriorityMarkDropPrecedence,'zxr10AclQosPriorityMarkOuterVlanId':zxr10AclQosPriorityMarkOuterVlanId,'zxr10AclQosPriorityMarkPrecedenceValue':zxr10AclQosPriorityMarkPrecedenceValue,'zxr10AclQosPriorityMarkRowStatus':zxr10AclQosPriorityMarkRowStatus,'zxr10AclQosTrafficLimitTable':zxr10AclQosTrafficLimitTable,'zxr10AclQosTrafficLimitEntry':zxr10AclQosTrafficLimitEntry,_I:zxr10AclQosTrafficLimitAclNo,_J:zxr10AclQosTrafficLimitRuleId,'zxr10AclQosTrafficLimitAclName':zxr10AclQosTrafficLimitAclName,'zxr10AclQosTrafficLimitCir':zxr10AclQosTrafficLimitCir,'zxr10AclQosTrafficLimitCbs':zxr10AclQosTrafficLimitCbs,'zxr10AclQosTrafficLimitEbs':zxr10AclQosTrafficLimitEbs,'zxr10AclQosTrafficLimitPir':zxr10AclQosTrafficLimitPir,'zxr10AclQosTrafficLimitPbs':zxr10AclQosTrafficLimitPbs,'zxr10AclQosTrafficLimitMode':zxr10AclQosTrafficLimitMode,'zxr10AclQosTrafficLimitRedDscpValue':zxr10AclQosTrafficLimitRedDscpValue,'zxr10AclQosTrafficLimitYelDscpValue':zxr10AclQosTrafficLimitYelDscpValue,'zxr10AclQosTrafficLimitRedDp':zxr10AclQosTrafficLimitRedDp,'zxr10AclQosTrafficLimitYelDp':zxr10AclQosTrafficLimitYelDp,'zxr10AclQosTrafficLimitForwadRed':zxr10AclQosTrafficLimitForwadRed,'zxr10AclQosTrafficLimitDropYellow':zxr10AclQosTrafficLimitDropYellow,'zxr10AclQosTrafficLimitRowStatus':zxr10AclQosTrafficLimitRowStatus,'zxr10AclQosTrafficMirrorTable':zxr10AclQosTrafficMirrorTable,'zxr10AclQosTrafficMirrorEntry':zxr10AclQosTrafficMirrorEntry,_K:zxr10AclQosTrafficMirrorAclNo,_L:zxr10AclQosTrafficMirrorRuleId,'zxr10AclQosTrafficMirrorAclName':zxr10AclQosTrafficMirrorAclName,'zxr10AclQosTrafficMirrorAction':zxr10AclQosTrafficMirrorAction,'zxr10AclQosTrafficMirrorIfName':zxr10AclQosTrafficMirrorIfName,'zxr10AclQosTrafficMirrorRowStatus':zxr10AclQosTrafficMirrorRowStatus,'zxr10AclQosRedirectTable':zxr10AclQosRedirectTable,'zxr10AclQosRedirectEntry':zxr10AclQosRedirectEntry,_M:zxr10AclQosRedirectAclNo,_N:zxr10AclQosRedirectRuleId,'zxr10AclQosRedirectAclName':zxr10AclQosRedirectAclName,'zxr10AclQosRedirectFlag':zxr10AclQosRedirectFlag,'zxr10AclQosRedirectGPort':zxr10AclQosRedirectGPort,'zxr10AclQosRedirectIpAddr1':zxr10AclQosRedirectIpAddr1,'zxr10AclQosRedirectIpPri1':zxr10AclQosRedirectIpPri1,'zxr10AclQosRedirectIpAddr2':zxr10AclQosRedirectIpAddr2,'zxr10AclQosRedirectIpPri2':zxr10AclQosRedirectIpPri2,'zxr10AclQosRedirectIpAddr3':zxr10AclQosRedirectIpAddr3,'zxr10AclQosRedirectIpPri3':zxr10AclQosRedirectIpPri3,'zxr10AclQosRedirectIpAddr4':zxr10AclQosRedirectIpAddr4,'zxr10AclQosRedirectIpPri4':zxr10AclQosRedirectIpPri4,'zxr10AclQosRedirectIpAddr5':zxr10AclQosRedirectIpAddr5,'zxr10AclQosRedirectIpPri5':zxr10AclQosRedirectIpPri5,'zxr10AclQosRedirectIpAddr6':zxr10AclQosRedirectIpAddr6,'zxr10AclQosRedirectIpPri6':zxr10AclQosRedirectIpPri6,'zxr10AclQosRedirectIpAddr7':zxr10AclQosRedirectIpAddr7,'zxr10AclQosRedirectIpPri7':zxr10AclQosRedirectIpPri7,'zxr10AclQosRedirectIpAddr8':zxr10AclQosRedirectIpAddr8,'zxr10AclQosRedirectIpPri8':zxr10AclQosRedirectIpPri8,'zxr10AclQosRedirectIPv6Addr':zxr10AclQosRedirectIPv6Addr,'zxr10AclQosRedirectGreenOnly':zxr10AclQosRedirectGreenOnly,'zxr10AclQosRedirectRowStatus':zxr10AclQosRedirectRowStatus,'zxr10AclQosTrafficStatisticsTable':zxr10AclQosTrafficStatisticsTable,'zxr10AclQosTrafficStatisticsEntry':zxr10AclQosTrafficStatisticsEntry,_O:zxr10AclQosTrafficStatisticsAclNo,_P:zxr10AclQosTrafficStatisticsRuleId,'zxr10AclQosTrafficStatisticsAclName':zxr10AclQosTrafficStatisticsAclName,'zxr10AclQosTrafficStatisticsPkttype':zxr10AclQosTrafficStatisticsPkttype,'zxr10AclQosTrafficStatisticsStatype':zxr10AclQosTrafficStatisticsStatype,'zxr10AclQosTrafficStatisticsRowStatus':zxr10AclQosTrafficStatisticsRowStatus})