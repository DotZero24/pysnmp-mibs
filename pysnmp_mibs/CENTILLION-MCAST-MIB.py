_N='igmpRouterPortPort'
_M='igmpRouterPortCard'
_L='igmpRouterPortStatic'
_K='igmpRouterPortVlanId'
_J='igmpGroupAddress'
_I='igmpGroupStatic'
_H='igmpGroupVlanId'
_G='igmpTimerConfigVlanId'
_F='igmpGeneralConfigVlanId'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='CENTILLION-MCAST-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Boolean,CardId,EnableIndicator,PortId,StatusIndicator,sysConfig=mibBuilder.importSymbols('CENTILLION-ROOT-MIB','Boolean','CardId','EnableIndicator','PortId','StatusIndicator','sysConfig')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,930,2,1,2,31))
_VlanMcastProtocolGroup_ObjectIdentity=ObjectIdentity
vlanMcastProtocolGroup=_VlanMcastProtocolGroup_ObjectIdentity((1,3,6,1,4,1,930,2,1,2,31,1))
_VlanIGMPProtocolGroup_ObjectIdentity=ObjectIdentity
vlanIGMPProtocolGroup=_VlanIGMPProtocolGroup_ObjectIdentity((1,3,6,1,4,1,930,2,1,2,31,1,1))
_VlanIGMPConfig_ObjectIdentity=ObjectIdentity
vlanIGMPConfig=_VlanIGMPConfig_ObjectIdentity((1,3,6,1,4,1,930,2,1,2,31,1,1,1))
_IgmpGeneralConfigTable_Object=MibTable
igmpGeneralConfigTable=_IgmpGeneralConfigTable_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1))
if mibBuilder.loadTexts:igmpGeneralConfigTable.setStatus(_A)
_IgmpGeneralConfigEntry_Object=MibTableRow
igmpGeneralConfigEntry=_IgmpGeneralConfigEntry_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1,1))
igmpGeneralConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:igmpGeneralConfigEntry.setStatus(_A)
_IgmpGeneralConfigVlanId_Type=VlanId
_IgmpGeneralConfigVlanId_Object=MibTableColumn
igmpGeneralConfigVlanId=_IgmpGeneralConfigVlanId_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1,1,1),_IgmpGeneralConfigVlanId_Type())
igmpGeneralConfigVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpGeneralConfigVlanId.setStatus(_A)
_IgmpGeneralConfigPseudoQuery_Type=EnableIndicator
_IgmpGeneralConfigPseudoQuery_Object=MibTableColumn
igmpGeneralConfigPseudoQuery=_IgmpGeneralConfigPseudoQuery_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1,1,2),_IgmpGeneralConfigPseudoQuery_Type())
igmpGeneralConfigPseudoQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGeneralConfigPseudoQuery.setStatus(_A)
_IgmpGeneralConfigIrapQuery_Type=EnableIndicator
_IgmpGeneralConfigIrapQuery_Object=MibTableColumn
igmpGeneralConfigIrapQuery=_IgmpGeneralConfigIrapQuery_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1,1,3),_IgmpGeneralConfigIrapQuery_Type())
igmpGeneralConfigIrapQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGeneralConfigIrapQuery.setStatus(_A)
_IgmpGeneralConfigIgmpSupport_Type=EnableIndicator
_IgmpGeneralConfigIgmpSupport_Object=MibTableColumn
igmpGeneralConfigIgmpSupport=_IgmpGeneralConfigIgmpSupport_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1,1,4),_IgmpGeneralConfigIgmpSupport_Type())
igmpGeneralConfigIgmpSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGeneralConfigIgmpSupport.setStatus(_A)
_IgmpGeneralConfigMaxGroup_Type=Integer32
_IgmpGeneralConfigMaxGroup_Object=MibTableColumn
igmpGeneralConfigMaxGroup=_IgmpGeneralConfigMaxGroup_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,1,1,5),_IgmpGeneralConfigMaxGroup_Type())
igmpGeneralConfigMaxGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGeneralConfigMaxGroup.setStatus(_A)
_IgmpTimerConfigTable_Object=MibTable
igmpTimerConfigTable=_IgmpTimerConfigTable_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,2))
if mibBuilder.loadTexts:igmpTimerConfigTable.setStatus(_A)
_IgmpTimerConfigEntry_Object=MibTableRow
igmpTimerConfigEntry=_IgmpTimerConfigEntry_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,2,1))
igmpTimerConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:igmpTimerConfigEntry.setStatus(_A)
_IgmpTimerConfigVlanId_Type=VlanId
_IgmpTimerConfigVlanId_Object=MibTableColumn
igmpTimerConfigVlanId=_IgmpTimerConfigVlanId_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,2,1,1),_IgmpTimerConfigVlanId_Type())
igmpTimerConfigVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpTimerConfigVlanId.setStatus(_A)
class _IgmpTimerConfigTimerRobustness_Type(Integer32):defaultValue=2
_IgmpTimerConfigTimerRobustness_Type.__name__=_E
_IgmpTimerConfigTimerRobustness_Object=MibTableColumn
igmpTimerConfigTimerRobustness=_IgmpTimerConfigTimerRobustness_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,2,1,2),_IgmpTimerConfigTimerRobustness_Type())
igmpTimerConfigTimerRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpTimerConfigTimerRobustness.setStatus(_A)
class _IgmpTimerConfigQueryInterval_Type(Integer32):defaultValue=125
_IgmpTimerConfigQueryInterval_Type.__name__=_E
_IgmpTimerConfigQueryInterval_Object=MibTableColumn
igmpTimerConfigQueryInterval=_IgmpTimerConfigQueryInterval_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,2,1,3),_IgmpTimerConfigQueryInterval_Type())
igmpTimerConfigQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpTimerConfigQueryInterval.setStatus(_A)
class _IgmpTimerConfigQueryResponse_Type(Integer32):defaultValue=100
_IgmpTimerConfigQueryResponse_Type.__name__=_E
_IgmpTimerConfigQueryResponse_Object=MibTableColumn
igmpTimerConfigQueryResponse=_IgmpTimerConfigQueryResponse_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,2,1,4),_IgmpTimerConfigQueryResponse_Type())
igmpTimerConfigQueryResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpTimerConfigQueryResponse.setStatus(_A)
_IgmpGroupTable_Object=MibTable
igmpGroupTable=_IgmpGroupTable_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3))
if mibBuilder.loadTexts:igmpGroupTable.setStatus(_A)
_IgmpGroupEntry_Object=MibTableRow
igmpGroupEntry=_IgmpGroupEntry_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3,1))
igmpGroupEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:igmpGroupEntry.setStatus(_A)
_IgmpGroupVlanId_Type=VlanId
_IgmpGroupVlanId_Object=MibTableColumn
igmpGroupVlanId=_IgmpGroupVlanId_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3,1,1),_IgmpGroupVlanId_Type())
igmpGroupVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpGroupVlanId.setStatus(_A)
_IgmpGroupStatic_Type=Boolean
_IgmpGroupStatic_Object=MibTableColumn
igmpGroupStatic=_IgmpGroupStatic_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3,1,2),_IgmpGroupStatic_Type())
igmpGroupStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpGroupStatic.setStatus(_A)
_IgmpGroupAddress_Type=IpAddress
_IgmpGroupAddress_Object=MibTableColumn
igmpGroupAddress=_IgmpGroupAddress_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3,1,3),_IgmpGroupAddress_Type())
igmpGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpGroupAddress.setStatus(_A)
class _IgmpGroupIncluded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('included',1),('excluded',2)))
_IgmpGroupIncluded_Type.__name__=_E
_IgmpGroupIncluded_Object=MibTableColumn
igmpGroupIncluded=_IgmpGroupIncluded_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3,1,4),_IgmpGroupIncluded_Type())
igmpGroupIncluded.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupIncluded.setStatus(_A)
_IgmpGroupStatus_Type=StatusIndicator
_IgmpGroupStatus_Object=MibTableColumn
igmpGroupStatus=_IgmpGroupStatus_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,3,1,5),_IgmpGroupStatus_Type())
igmpGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupStatus.setStatus(_A)
_IgmpRouterPortTable_Object=MibTable
igmpRouterPortTable=_IgmpRouterPortTable_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4))
if mibBuilder.loadTexts:igmpRouterPortTable.setStatus(_A)
_IgmpRouterPortEntry_Object=MibTableRow
igmpRouterPortEntry=_IgmpRouterPortEntry_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4,1))
igmpRouterPortEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:igmpRouterPortEntry.setStatus(_A)
_IgmpRouterPortVlanId_Type=VlanId
_IgmpRouterPortVlanId_Object=MibTableColumn
igmpRouterPortVlanId=_IgmpRouterPortVlanId_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4,1,1),_IgmpRouterPortVlanId_Type())
igmpRouterPortVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpRouterPortVlanId.setStatus(_A)
_IgmpRouterPortStatic_Type=Boolean
_IgmpRouterPortStatic_Object=MibTableColumn
igmpRouterPortStatic=_IgmpRouterPortStatic_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4,1,2),_IgmpRouterPortStatic_Type())
igmpRouterPortStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpRouterPortStatic.setStatus(_A)
_IgmpRouterPortCard_Type=CardId
_IgmpRouterPortCard_Object=MibTableColumn
igmpRouterPortCard=_IgmpRouterPortCard_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4,1,3),_IgmpRouterPortCard_Type())
igmpRouterPortCard.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpRouterPortCard.setStatus(_A)
_IgmpRouterPortPort_Type=PortId
_IgmpRouterPortPort_Object=MibTableColumn
igmpRouterPortPort=_IgmpRouterPortPort_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4,1,4),_IgmpRouterPortPort_Type())
igmpRouterPortPort.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpRouterPortPort.setStatus(_A)
_IgmpRouterPortStatus_Type=StatusIndicator
_IgmpRouterPortStatus_Object=MibTableColumn
igmpRouterPortStatus=_IgmpRouterPortStatus_Object((1,3,6,1,4,1,930,2,1,2,31,1,1,1,4,1,5),_IgmpRouterPortStatus_Type())
igmpRouterPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpRouterPortStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanId':VlanId,'vlan':vlan,'vlanMcastProtocolGroup':vlanMcastProtocolGroup,'vlanIGMPProtocolGroup':vlanIGMPProtocolGroup,'vlanIGMPConfig':vlanIGMPConfig,'igmpGeneralConfigTable':igmpGeneralConfigTable,'igmpGeneralConfigEntry':igmpGeneralConfigEntry,_F:igmpGeneralConfigVlanId,'igmpGeneralConfigPseudoQuery':igmpGeneralConfigPseudoQuery,'igmpGeneralConfigIrapQuery':igmpGeneralConfigIrapQuery,'igmpGeneralConfigIgmpSupport':igmpGeneralConfigIgmpSupport,'igmpGeneralConfigMaxGroup':igmpGeneralConfigMaxGroup,'igmpTimerConfigTable':igmpTimerConfigTable,'igmpTimerConfigEntry':igmpTimerConfigEntry,_G:igmpTimerConfigVlanId,'igmpTimerConfigTimerRobustness':igmpTimerConfigTimerRobustness,'igmpTimerConfigQueryInterval':igmpTimerConfigQueryInterval,'igmpTimerConfigQueryResponse':igmpTimerConfigQueryResponse,'igmpGroupTable':igmpGroupTable,'igmpGroupEntry':igmpGroupEntry,_H:igmpGroupVlanId,_I:igmpGroupStatic,_J:igmpGroupAddress,'igmpGroupIncluded':igmpGroupIncluded,'igmpGroupStatus':igmpGroupStatus,'igmpRouterPortTable':igmpRouterPortTable,'igmpRouterPortEntry':igmpRouterPortEntry,_K:igmpRouterPortVlanId,_L:igmpRouterPortStatic,_M:igmpRouterPortCard,_N:igmpRouterPortPort,'igmpRouterPortStatus':igmpRouterPortStatus})