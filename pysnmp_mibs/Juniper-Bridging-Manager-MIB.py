_h='juniBridgingMgrConfGroup'
_g='juniBridgingMgrBridgeMode'
_f='juniBridgingMgrBridgeSubscriberPolicyName'
_e='juniBridgingMgrBridgeSubscriberPolicyMpls'
_d='juniBridgingMgrBridgeSubscriberPolicyRelearn'
_c='juniBridgingMgrBridgeSubscriberPolicyPPPoE'
_b='juniBridgingMgrBridgeSubscriberPolicyUnicast'
_a='juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol'
_Z='juniBridgingMgrBridgeSubscriberPolicyIp'
_Y='juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast'
_X='juniBridgingMgrBridgeSubscriberPolicyMulticast'
_W='juniBridgingMgrBridgeSubscriberPolicyBroadcast'
_V='juniBridgingMgrBridgeSubscriberPolicyArp'
_U='juniBridgingMgrBridgeSubscriberPolicyRowStatus'
_T='juniBridgingMgrSubscriberNextIndex'
_S='juniBridgingMgrBridgeGroupLearnCount'
_R='juniBridgingMgrBridgeGroupRouteProtocol'
_Q='juniBridgingMgrBridgeGroupSPolicyIndex'
_P='juniBridgingMgrBridgeGroupName'
_O='juniBridgingMgrBridgeGroupLearning'
_N='juniBridgingMgrBridgeRowStatus'
_M='juniBridgingMgrNextIndex'
_L='juniBridgingMgrBridgeSubscriberPolicyIndex'
_K='not-accessible'
_J='juniBridgingMgrBridgeGroupIndex'
_I='read-only'
_H='Unsigned32'
_G='DisplayString'
_F='deny'
_E='permit'
_D='Integer32'
_C='read-create'
_B='Juniper-Bridging-Manager-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
juniBridgingMgrMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,64))
if mibBuilder.loadTexts:juniBridgingMgrMIB.setRevisions(('2002-10-11 20:25',))
class JuniBridgingMgrBridgeRouteMask(TextualConvention,Integer32):status=_A
class JuniBridgingMgrNextIndex(TextualConvention,Unsigned32):status=_A
_JuniBridgingMgrBridgeGroup_ObjectIdentity=ObjectIdentity
juniBridgingMgrBridgeGroup=_JuniBridgingMgrBridgeGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,64,1))
_JuniBridgingMgrNextIndex_Type=JuniBridgingMgrNextIndex
_JuniBridgingMgrNextIndex_Object=MibScalar
juniBridgingMgrNextIndex=_JuniBridgingMgrNextIndex_Object((1,3,6,1,4,1,4874,2,2,64,1,1),_JuniBridgingMgrNextIndex_Type())
juniBridgingMgrNextIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniBridgingMgrNextIndex.setStatus(_A)
_JuniBridgingMgrBridgeGroupTable_Object=MibTable
juniBridgingMgrBridgeGroupTable=_JuniBridgingMgrBridgeGroupTable_Object((1,3,6,1,4,1,4874,2,2,64,1,3))
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupTable.setStatus(_A)
_JuniBridgingMgrBridgeGroupEntry_Object=MibTableRow
juniBridgingMgrBridgeGroupEntry=_JuniBridgingMgrBridgeGroupEntry_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1))
juniBridgingMgrBridgeGroupEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupEntry.setStatus(_A)
class _JuniBridgingMgrBridgeGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JuniBridgingMgrBridgeGroupIndex_Type.__name__=_H
_JuniBridgingMgrBridgeGroupIndex_Object=MibTableColumn
juniBridgingMgrBridgeGroupIndex=_JuniBridgingMgrBridgeGroupIndex_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,1),_JuniBridgingMgrBridgeGroupIndex_Type())
juniBridgingMgrBridgeGroupIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupIndex.setStatus(_A)
_JuniBridgingMgrBridgeRowStatus_Type=RowStatus
_JuniBridgingMgrBridgeRowStatus_Object=MibTableColumn
juniBridgingMgrBridgeRowStatus=_JuniBridgingMgrBridgeRowStatus_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,2),_JuniBridgingMgrBridgeRowStatus_Type())
juniBridgingMgrBridgeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeRowStatus.setStatus(_A)
class _JuniBridgingMgrBridgeGroupLearning_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_JuniBridgingMgrBridgeGroupLearning_Type.__name__=_D
_JuniBridgingMgrBridgeGroupLearning_Object=MibTableColumn
juniBridgingMgrBridgeGroupLearning=_JuniBridgingMgrBridgeGroupLearning_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,3),_JuniBridgingMgrBridgeGroupLearning_Type())
juniBridgingMgrBridgeGroupLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupLearning.setStatus(_A)
class _JuniBridgingMgrBridgeGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniBridgingMgrBridgeGroupName_Type.__name__=_G
_JuniBridgingMgrBridgeGroupName_Object=MibTableColumn
juniBridgingMgrBridgeGroupName=_JuniBridgingMgrBridgeGroupName_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,4),_JuniBridgingMgrBridgeGroupName_Type())
juniBridgingMgrBridgeGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupName.setStatus(_A)
_JuniBridgingMgrBridgeGroupSPolicyIndex_Type=Integer32
_JuniBridgingMgrBridgeGroupSPolicyIndex_Object=MibTableColumn
juniBridgingMgrBridgeGroupSPolicyIndex=_JuniBridgingMgrBridgeGroupSPolicyIndex_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,5),_JuniBridgingMgrBridgeGroupSPolicyIndex_Type())
juniBridgingMgrBridgeGroupSPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupSPolicyIndex.setStatus(_A)
_JuniBridgingMgrBridgeGroupRouteProtocol_Type=JuniBridgingMgrBridgeRouteMask
_JuniBridgingMgrBridgeGroupRouteProtocol_Object=MibTableColumn
juniBridgingMgrBridgeGroupRouteProtocol=_JuniBridgingMgrBridgeGroupRouteProtocol_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,6),_JuniBridgingMgrBridgeGroupRouteProtocol_Type())
juniBridgingMgrBridgeGroupRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupRouteProtocol.setStatus(_A)
class _JuniBridgingMgrBridgeGroupLearnCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64000))
_JuniBridgingMgrBridgeGroupLearnCount_Type.__name__=_D
_JuniBridgingMgrBridgeGroupLearnCount_Object=MibTableColumn
juniBridgingMgrBridgeGroupLearnCount=_JuniBridgingMgrBridgeGroupLearnCount_Object((1,3,6,1,4,1,4874,2,2,64,1,3,1,7),_JuniBridgingMgrBridgeGroupLearnCount_Type())
juniBridgingMgrBridgeGroupLearnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeGroupLearnCount.setStatus(_A)
_JuniBridgingMgrBridgeSubscriberPolicy_ObjectIdentity=ObjectIdentity
juniBridgingMgrBridgeSubscriberPolicy=_JuniBridgingMgrBridgeSubscriberPolicy_ObjectIdentity((1,3,6,1,4,1,4874,2,2,64,2))
class _JuniBridgingMgrSubscriberNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniBridgingMgrSubscriberNextIndex_Type.__name__=_D
_JuniBridgingMgrSubscriberNextIndex_Object=MibScalar
juniBridgingMgrSubscriberNextIndex=_JuniBridgingMgrSubscriberNextIndex_Object((1,3,6,1,4,1,4874,2,2,64,2,1),_JuniBridgingMgrSubscriberNextIndex_Type())
juniBridgingMgrSubscriberNextIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniBridgingMgrSubscriberNextIndex.setStatus(_A)
_JuniBridgingMgrBridgeSubscriberPolicyTable_Object=MibTable
juniBridgingMgrBridgeSubscriberPolicyTable=_JuniBridgingMgrBridgeSubscriberPolicyTable_Object((1,3,6,1,4,1,4874,2,2,64,2,2))
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyTable.setStatus(_A)
_JuniBridgingMgrBridgeSubscriberPolicyEntry_Object=MibTableRow
juniBridgingMgrBridgeSubscriberPolicyEntry=_JuniBridgingMgrBridgeSubscriberPolicyEntry_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1))
juniBridgingMgrBridgeSubscriberPolicyEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyEntry.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniBridgingMgrBridgeSubscriberPolicyIndex_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyIndex_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyIndex=_JuniBridgingMgrBridgeSubscriberPolicyIndex_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,1),_JuniBridgingMgrBridgeSubscriberPolicyIndex_Type())
juniBridgingMgrBridgeSubscriberPolicyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyIndex.setStatus(_A)
_JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Type=RowStatus
_JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyRowStatus=_JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,2),_JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Type())
juniBridgingMgrBridgeSubscriberPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyRowStatus.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyArp_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyArp_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyArp=_JuniBridgingMgrBridgeSubscriberPolicyArp_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,3),_JuniBridgingMgrBridgeSubscriberPolicyArp_Type())
juniBridgingMgrBridgeSubscriberPolicyArp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyArp.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyBroadcast=_JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,4),_JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Type())
juniBridgingMgrBridgeSubscriberPolicyBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyBroadcast.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyMulticast_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyMulticast_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyMulticast=_JuniBridgingMgrBridgeSubscriberPolicyMulticast_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,5),_JuniBridgingMgrBridgeSubscriberPolicyMulticast_Type())
juniBridgingMgrBridgeSubscriberPolicyMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyMulticast.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast=_JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,6),_JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Type())
juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyIp_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyIp_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyIp=_JuniBridgingMgrBridgeSubscriberPolicyIp_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,7),_JuniBridgingMgrBridgeSubscriberPolicyIp_Type())
juniBridgingMgrBridgeSubscriberPolicyIp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyIp.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol=_JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,8),_JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Type())
juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyUnicast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyUnicast_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyUnicast_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyUnicast=_JuniBridgingMgrBridgeSubscriberPolicyUnicast_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,9),_JuniBridgingMgrBridgeSubscriberPolicyUnicast_Type())
juniBridgingMgrBridgeSubscriberPolicyUnicast.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyUnicast.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyPPPoE=_JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,10),_JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Type())
juniBridgingMgrBridgeSubscriberPolicyPPPoE.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyPPPoE.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyRelearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyRelearn_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyRelearn_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyRelearn=_JuniBridgingMgrBridgeSubscriberPolicyRelearn_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,11),_JuniBridgingMgrBridgeSubscriberPolicyRelearn_Type())
juniBridgingMgrBridgeSubscriberPolicyRelearn.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyRelearn.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyMpls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_JuniBridgingMgrBridgeSubscriberPolicyMpls_Type.__name__=_D
_JuniBridgingMgrBridgeSubscriberPolicyMpls_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyMpls=_JuniBridgingMgrBridgeSubscriberPolicyMpls_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,12),_JuniBridgingMgrBridgeSubscriberPolicyMpls_Type())
juniBridgingMgrBridgeSubscriberPolicyMpls.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyMpls.setStatus(_A)
class _JuniBridgingMgrBridgeSubscriberPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniBridgingMgrBridgeSubscriberPolicyName_Type.__name__=_G
_JuniBridgingMgrBridgeSubscriberPolicyName_Object=MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyName=_JuniBridgingMgrBridgeSubscriberPolicyName_Object((1,3,6,1,4,1,4874,2,2,64,2,2,1,13),_JuniBridgingMgrBridgeSubscriberPolicyName_Type())
juniBridgingMgrBridgeSubscriberPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgingMgrBridgeSubscriberPolicyName.setStatus(_A)
_JuniBridgingMgrBridge_ObjectIdentity=ObjectIdentity
juniBridgingMgrBridge=_JuniBridgingMgrBridge_ObjectIdentity((1,3,6,1,4,1,4874,2,2,64,3))
class _JuniBridgingMgrBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('default',0),('crb',1),('irb',2),('other',3)))
_JuniBridgingMgrBridgeMode_Type.__name__=_D
_JuniBridgingMgrBridgeMode_Object=MibScalar
juniBridgingMgrBridgeMode=_JuniBridgingMgrBridgeMode_Object((1,3,6,1,4,1,4874,2,2,64,3,1),_JuniBridgingMgrBridgeMode_Type())
juniBridgingMgrBridgeMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:juniBridgingMgrBridgeMode.setStatus(_A)
_JuniBridgingMgrConformance_ObjectIdentity=ObjectIdentity
juniBridgingMgrConformance=_JuniBridgingMgrConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,64,4))
_JuniBridgingMgrCompliances_ObjectIdentity=ObjectIdentity
juniBridgingMgrCompliances=_JuniBridgingMgrCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,64,4,1))
_JuniBridgingMgrGroups_ObjectIdentity=ObjectIdentity
juniBridgingMgrGroups=_JuniBridgingMgrGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,64,4,2))
juniBridgingMgrConfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,64,4,2,1))
juniBridgingMgrConfGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:juniBridgingMgrConfGroup.setStatus(_A)
juniBridgingMgrCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,64,4,1,1))
juniBridgingMgrCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:juniBridgingMgrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniBridgingMgrBridgeRouteMask':JuniBridgingMgrBridgeRouteMask,'JuniBridgingMgrNextIndex':JuniBridgingMgrNextIndex,'juniBridgingMgrMIB':juniBridgingMgrMIB,'juniBridgingMgrBridgeGroup':juniBridgingMgrBridgeGroup,_M:juniBridgingMgrNextIndex,'juniBridgingMgrBridgeGroupTable':juniBridgingMgrBridgeGroupTable,'juniBridgingMgrBridgeGroupEntry':juniBridgingMgrBridgeGroupEntry,_J:juniBridgingMgrBridgeGroupIndex,_N:juniBridgingMgrBridgeRowStatus,_O:juniBridgingMgrBridgeGroupLearning,_P:juniBridgingMgrBridgeGroupName,_Q:juniBridgingMgrBridgeGroupSPolicyIndex,_R:juniBridgingMgrBridgeGroupRouteProtocol,_S:juniBridgingMgrBridgeGroupLearnCount,'juniBridgingMgrBridgeSubscriberPolicy':juniBridgingMgrBridgeSubscriberPolicy,_T:juniBridgingMgrSubscriberNextIndex,'juniBridgingMgrBridgeSubscriberPolicyTable':juniBridgingMgrBridgeSubscriberPolicyTable,'juniBridgingMgrBridgeSubscriberPolicyEntry':juniBridgingMgrBridgeSubscriberPolicyEntry,_L:juniBridgingMgrBridgeSubscriberPolicyIndex,_U:juniBridgingMgrBridgeSubscriberPolicyRowStatus,_V:juniBridgingMgrBridgeSubscriberPolicyArp,_W:juniBridgingMgrBridgeSubscriberPolicyBroadcast,_X:juniBridgingMgrBridgeSubscriberPolicyMulticast,_Y:juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast,_Z:juniBridgingMgrBridgeSubscriberPolicyIp,_a:juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol,_b:juniBridgingMgrBridgeSubscriberPolicyUnicast,_c:juniBridgingMgrBridgeSubscriberPolicyPPPoE,_d:juniBridgingMgrBridgeSubscriberPolicyRelearn,_e:juniBridgingMgrBridgeSubscriberPolicyMpls,_f:juniBridgingMgrBridgeSubscriberPolicyName,'juniBridgingMgrBridge':juniBridgingMgrBridge,_g:juniBridgingMgrBridgeMode,'juniBridgingMgrConformance':juniBridgingMgrConformance,'juniBridgingMgrCompliances':juniBridgingMgrCompliances,'juniBridgingMgrCompliance':juniBridgingMgrCompliance,'juniBridgingMgrGroups':juniBridgingMgrGroups,_h:juniBridgingMgrConfGroup})