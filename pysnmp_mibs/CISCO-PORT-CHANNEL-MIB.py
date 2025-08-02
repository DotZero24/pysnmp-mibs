_k='portChannelFcipGroup'
_j='portChannelExtFcipEnhanced'
_i='portChannelExtOperChannelGrpMode'
_h='portChannelExtPersistent'
_g='portChannelExtAutoCreated'
_f='portChannelExtChannelGrpMode'
_e='portChannelGrpIfAutoCreation'
_d='portChannelProtocolEnable'
_c='portChannelMemberOperStatus'
_b='portChannelRowStatus'
_a='portChannelCreationTime'
_Z='portChannelMemberList'
_Y='portChannelLastActionTime'
_X='portChannelLastActionStatusCause'
_W='portChannelLastActionStatus'
_V='portChannelAddType'
_U='portChannelOperChannelMode'
_T='portChannelAdminChannelMode'
_S='portChannelIfIndex'
_R='portChannelExtEntry'
_Q='enable'
_P='PortChannelMode'
_O='portChannelIndex'
_N='Unsigned32'
_M='ifIndex'
_L='IF-MIB'
_K='portChannelProtocolGroup'
_J='PortMemberList'
_I='portChannelGroupRev1'
_H='deprecated'
_G='read-create'
_F='read-write'
_E='Integer32'
_D='portChannelGroup'
_C='read-only'
_B='CISCO-PORT-CHANNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PortMemberList,=mibBuilder.importSymbols('CISCO-ST-TC',_J)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_L,'InterfaceIndex',_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoPortChannelMIB=ModuleIdentity((1,3,6,1,4,1,9,9,285))
if mibBuilder.loadTexts:ciscoPortChannelMIB.setRevisions(('2017-02-28 00:00','2004-09-13 00:00','2004-06-08 00:00','2004-03-11 00:00','2003-05-28 00:00','2002-10-02 00:00'))
class PortChannelMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('on',2),('off',3),('desirable',4)))
class PortChannelGroupMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('active',2)))
_CiscoPortChannelObjects_ObjectIdentity=ObjectIdentity
ciscoPortChannelObjects=_CiscoPortChannelObjects_ObjectIdentity((1,3,6,1,4,1,9,9,285,1))
_PortChannelConfig_ObjectIdentity=ObjectIdentity
portChannelConfig=_PortChannelConfig_ObjectIdentity((1,3,6,1,4,1,9,9,285,1,1))
_PortChannelTable_Object=MibTable
portChannelTable=_PortChannelTable_Object((1,3,6,1,4,1,9,9,285,1,1,1))
if mibBuilder.loadTexts:portChannelTable.setStatus(_A)
_PortChannelEntry_Object=MibTableRow
portChannelEntry=_PortChannelEntry_Object((1,3,6,1,4,1,9,9,285,1,1,1,1))
portChannelEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:portChannelEntry.setStatus(_A)
class _PortChannelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_PortChannelIndex_Type.__name__=_N
_PortChannelIndex_Object=MibTableColumn
portChannelIndex=_PortChannelIndex_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,1),_PortChannelIndex_Type())
portChannelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:portChannelIndex.setStatus(_A)
_PortChannelIfIndex_Type=InterfaceIndex
_PortChannelIfIndex_Object=MibTableColumn
portChannelIfIndex=_PortChannelIfIndex_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,2),_PortChannelIfIndex_Type())
portChannelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelIfIndex.setStatus(_A)
class _PortChannelAdminChannelMode_Type(PortChannelMode):defaultValue=2
_PortChannelAdminChannelMode_Type.__name__=_P
_PortChannelAdminChannelMode_Object=MibTableColumn
portChannelAdminChannelMode=_PortChannelAdminChannelMode_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,3),_PortChannelAdminChannelMode_Type())
portChannelAdminChannelMode.setMaxAccess(_G)
if mibBuilder.loadTexts:portChannelAdminChannelMode.setStatus(_A)
_PortChannelOperChannelMode_Type=PortChannelMode
_PortChannelOperChannelMode_Object=MibTableColumn
portChannelOperChannelMode=_PortChannelOperChannelMode_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,4),_PortChannelOperChannelMode_Type())
portChannelOperChannelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelOperChannelMode.setStatus(_A)
class _PortChannelAddType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('force',2)))
_PortChannelAddType_Type.__name__=_E
_PortChannelAddType_Object=MibTableColumn
portChannelAddType=_PortChannelAddType_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,5),_PortChannelAddType_Type())
portChannelAddType.setMaxAccess(_G)
if mibBuilder.loadTexts:portChannelAddType.setStatus(_A)
class _PortChannelLastActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('successful',1),('failed',2)))
_PortChannelLastActionStatus_Type.__name__=_E
_PortChannelLastActionStatus_Object=MibTableColumn
portChannelLastActionStatus=_PortChannelLastActionStatus_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,6),_PortChannelLastActionStatus_Type())
portChannelLastActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelLastActionStatus.setStatus(_A)
_PortChannelLastActionStatusCause_Type=SnmpAdminString
_PortChannelLastActionStatusCause_Object=MibTableColumn
portChannelLastActionStatusCause=_PortChannelLastActionStatusCause_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,7),_PortChannelLastActionStatusCause_Type())
portChannelLastActionStatusCause.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelLastActionStatusCause.setStatus(_A)
_PortChannelLastActionTime_Type=TimeStamp
_PortChannelLastActionTime_Object=MibTableColumn
portChannelLastActionTime=_PortChannelLastActionTime_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,8),_PortChannelLastActionTime_Type())
portChannelLastActionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelLastActionTime.setStatus(_A)
class _PortChannelMemberList_Type(PortMemberList):defaultHexValue=''
_PortChannelMemberList_Type.__name__=_J
_PortChannelMemberList_Object=MibTableColumn
portChannelMemberList=_PortChannelMemberList_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,9),_PortChannelMemberList_Type())
portChannelMemberList.setMaxAccess(_G)
if mibBuilder.loadTexts:portChannelMemberList.setStatus(_A)
_PortChannelCreationTime_Type=TimeStamp
_PortChannelCreationTime_Object=MibTableColumn
portChannelCreationTime=_PortChannelCreationTime_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,10),_PortChannelCreationTime_Type())
portChannelCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelCreationTime.setStatus(_A)
_PortChannelRowStatus_Type=RowStatus
_PortChannelRowStatus_Object=MibTableColumn
portChannelRowStatus=_PortChannelRowStatus_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,11),_PortChannelRowStatus_Type())
portChannelRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:portChannelRowStatus.setStatus(_A)
class _PortChannelMemberOperStatus_Type(PortMemberList):defaultHexValue=''
_PortChannelMemberOperStatus_Type.__name__=_J
_PortChannelMemberOperStatus_Object=MibTableColumn
portChannelMemberOperStatus=_PortChannelMemberOperStatus_Object((1,3,6,1,4,1,9,9,285,1,1,1,1,12),_PortChannelMemberOperStatus_Type())
portChannelMemberOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelMemberOperStatus.setStatus(_A)
_PortChannelProtocolEnable_Type=TruthValue
_PortChannelProtocolEnable_Object=MibScalar
portChannelProtocolEnable=_PortChannelProtocolEnable_Object((1,3,6,1,4,1,9,9,285,1,1,2),_PortChannelProtocolEnable_Type())
portChannelProtocolEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:portChannelProtocolEnable.setStatus(_A)
_PortChannelGrpIfExtTable_Object=MibTable
portChannelGrpIfExtTable=_PortChannelGrpIfExtTable_Object((1,3,6,1,4,1,9,9,285,1,1,3))
if mibBuilder.loadTexts:portChannelGrpIfExtTable.setStatus(_A)
_PortChannelGrpIfExtEntry_Object=MibTableRow
portChannelGrpIfExtEntry=_PortChannelGrpIfExtEntry_Object((1,3,6,1,4,1,9,9,285,1,1,3,1))
portChannelGrpIfExtEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:portChannelGrpIfExtEntry.setStatus(_A)
_PortChannelGrpIfAutoCreation_Type=TruthValue
_PortChannelGrpIfAutoCreation_Object=MibTableColumn
portChannelGrpIfAutoCreation=_PortChannelGrpIfAutoCreation_Object((1,3,6,1,4,1,9,9,285,1,1,3,1,1),_PortChannelGrpIfAutoCreation_Type())
portChannelGrpIfAutoCreation.setMaxAccess(_F)
if mibBuilder.loadTexts:portChannelGrpIfAutoCreation.setStatus(_A)
_PortChannelExtTable_Object=MibTable
portChannelExtTable=_PortChannelExtTable_Object((1,3,6,1,4,1,9,9,285,1,1,4))
if mibBuilder.loadTexts:portChannelExtTable.setStatus(_A)
_PortChannelExtEntry_Object=MibTableRow
portChannelExtEntry=_PortChannelExtEntry_Object((1,3,6,1,4,1,9,9,285,1,1,4,1))
if mibBuilder.loadTexts:portChannelExtEntry.setStatus(_A)
_PortChannelExtChannelGrpMode_Type=PortChannelGroupMode
_PortChannelExtChannelGrpMode_Object=MibTableColumn
portChannelExtChannelGrpMode=_PortChannelExtChannelGrpMode_Object((1,3,6,1,4,1,9,9,285,1,1,4,1,1),_PortChannelExtChannelGrpMode_Type())
portChannelExtChannelGrpMode.setMaxAccess(_F)
if mibBuilder.loadTexts:portChannelExtChannelGrpMode.setStatus(_A)
_PortChannelExtAutoCreated_Type=TruthValue
_PortChannelExtAutoCreated_Object=MibTableColumn
portChannelExtAutoCreated=_PortChannelExtAutoCreated_Object((1,3,6,1,4,1,9,9,285,1,1,4,1,2),_PortChannelExtAutoCreated_Type())
portChannelExtAutoCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelExtAutoCreated.setStatus(_A)
class _PortChannelExtPersistent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),(_Q,2)))
_PortChannelExtPersistent_Type.__name__=_E
_PortChannelExtPersistent_Object=MibTableColumn
portChannelExtPersistent=_PortChannelExtPersistent_Object((1,3,6,1,4,1,9,9,285,1,1,4,1,3),_PortChannelExtPersistent_Type())
portChannelExtPersistent.setMaxAccess(_F)
if mibBuilder.loadTexts:portChannelExtPersistent.setStatus(_A)
_PortChannelExtOperChannelGrpMode_Type=PortChannelGroupMode
_PortChannelExtOperChannelGrpMode_Object=MibTableColumn
portChannelExtOperChannelGrpMode=_PortChannelExtOperChannelGrpMode_Object((1,3,6,1,4,1,9,9,285,1,1,4,1,4),_PortChannelExtOperChannelGrpMode_Type())
portChannelExtOperChannelGrpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portChannelExtOperChannelGrpMode.setStatus(_A)
class _PortChannelExtFcipEnhanced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),(_Q,2)))
_PortChannelExtFcipEnhanced_Type.__name__=_E
_PortChannelExtFcipEnhanced_Object=MibTableColumn
portChannelExtFcipEnhanced=_PortChannelExtFcipEnhanced_Object((1,3,6,1,4,1,9,9,285,1,1,4,1,5),_PortChannelExtFcipEnhanced_Type())
portChannelExtFcipEnhanced.setMaxAccess(_F)
if mibBuilder.loadTexts:portChannelExtFcipEnhanced.setStatus(_A)
_PortChannelStatistics_ObjectIdentity=ObjectIdentity
portChannelStatistics=_PortChannelStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,285,1,2))
_PortChannelNotification_ObjectIdentity=ObjectIdentity
portChannelNotification=_PortChannelNotification_ObjectIdentity((1,3,6,1,4,1,9,9,285,1,3))
_PortChannelNotifications_ObjectIdentity=ObjectIdentity
portChannelNotifications=_PortChannelNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,285,1,3,0))
_PortChannelMIBConformance_ObjectIdentity=ObjectIdentity
portChannelMIBConformance=_PortChannelMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,285,2))
_PortChannelMIBCompliances_ObjectIdentity=ObjectIdentity
portChannelMIBCompliances=_PortChannelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,285,2,1))
_PortChannelMIBGroups_ObjectIdentity=ObjectIdentity
portChannelMIBGroups=_PortChannelMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,285,2,2))
portChannelEntry.registerAugmentions((_B,_R))
portChannelExtEntry.setIndexNames(*portChannelEntry.getIndexNames())
portChannelGroup=ObjectGroup((1,3,6,1,4,1,9,9,285,2,2,1))
portChannelGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:portChannelGroup.setStatus(_A)
portChannelGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,285,2,2,2))
portChannelGroupRev1.setObjects((_B,_c))
if mibBuilder.loadTexts:portChannelGroupRev1.setStatus(_A)
portChannelProtocolGroup=ObjectGroup((1,3,6,1,4,1,9,9,285,2,2,3))
portChannelProtocolGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:portChannelProtocolGroup.setStatus(_A)
portChannelFcipGroup=ObjectGroup((1,3,6,1,4,1,9,9,285,2,2,4))
portChannelFcipGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:portChannelFcipGroup.setStatus(_A)
portChannelMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,285,2,1,1))
portChannelMIBCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:portChannelMIBCompliance.setStatus(_H)
portChannelMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,285,2,1,2))
portChannelMIBCompliance1.setObjects((_B,_D))
if mibBuilder.loadTexts:portChannelMIBCompliance1.setStatus(_H)
portChannelMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,285,2,1,3))
portChannelMIBCompliance2.setObjects(*((_B,_D),(_B,_I)))
if mibBuilder.loadTexts:portChannelMIBCompliance2.setStatus(_H)
portChannelMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,285,2,1,4))
portChannelMIBCompliance3.setObjects(*((_B,_D),(_B,_I),(_B,_K)))
if mibBuilder.loadTexts:portChannelMIBCompliance3.setStatus(_H)
portChannelMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,285,2,1,5))
portChannelMIBCompliance4.setObjects(*((_B,_D),(_B,_I),(_B,_K),(_B,_k)))
if mibBuilder.loadTexts:portChannelMIBCompliance4.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:PortChannelMode,'PortChannelGroupMode':PortChannelGroupMode,'ciscoPortChannelMIB':ciscoPortChannelMIB,'ciscoPortChannelObjects':ciscoPortChannelObjects,'portChannelConfig':portChannelConfig,'portChannelTable':portChannelTable,'portChannelEntry':portChannelEntry,_O:portChannelIndex,_S:portChannelIfIndex,_T:portChannelAdminChannelMode,_U:portChannelOperChannelMode,_V:portChannelAddType,_W:portChannelLastActionStatus,_X:portChannelLastActionStatusCause,_Y:portChannelLastActionTime,_Z:portChannelMemberList,_a:portChannelCreationTime,_b:portChannelRowStatus,_c:portChannelMemberOperStatus,_d:portChannelProtocolEnable,'portChannelGrpIfExtTable':portChannelGrpIfExtTable,'portChannelGrpIfExtEntry':portChannelGrpIfExtEntry,_e:portChannelGrpIfAutoCreation,'portChannelExtTable':portChannelExtTable,_R:portChannelExtEntry,_f:portChannelExtChannelGrpMode,_g:portChannelExtAutoCreated,_h:portChannelExtPersistent,_i:portChannelExtOperChannelGrpMode,_j:portChannelExtFcipEnhanced,'portChannelStatistics':portChannelStatistics,'portChannelNotification':portChannelNotification,'portChannelNotifications':portChannelNotifications,'portChannelMIBConformance':portChannelMIBConformance,'portChannelMIBCompliances':portChannelMIBCompliances,'portChannelMIBCompliance':portChannelMIBCompliance,'portChannelMIBCompliance1':portChannelMIBCompliance1,'portChannelMIBCompliance2':portChannelMIBCompliance2,'portChannelMIBCompliance3':portChannelMIBCompliance3,'portChannelMIBCompliance4':portChannelMIBCompliance4,'portChannelMIBGroups':portChannelMIBGroups,_D:portChannelGroup,_I:portChannelGroupRev1,_K:portChannelProtocolGroup,_k:portChannelFcipGroup})