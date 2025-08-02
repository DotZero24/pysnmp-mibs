_q='ciscoOscpBundleGroup'
_p='ciscoOscpNotificationsGroup'
_o='ciscoOscpBasicGroup'
_n='coscpNotifyTransDown'
_m='coscpBundleRowStatus'
_l='coscpBundlePortCount'
_k='coscpBundleIfIndex'
_j='coscpBundleActivePortId'
_i='coscpLinkSelPriority'
_h='coscpLinkConfigBundleId'
_g='coscpLinkDerivedBundleId'
_f='coscpPriorityChangeMode'
_e='coscpLinkOutHellos'
_d='coscpLinkInDiscardedHellos'
_c='coscpLinkInHellos'
_b='coscpLinkIfIndex'
_a='coscpLinkRemotePortId'
_Z='coscpLinkRemoteSwitchId'
_Y='coscpLinkHelloState'
_X='coscpLinkVersion'
_W='coscpLinkType'
_V='coscpNotifiesEnabled'
_U='coscpHelloInactivityFactor'
_T='coscpHelloInterval'
_S='coscpHelloHoldDown'
_R='coscpSwitchId'
_Q='coscpLowestVersion'
_P='coscpHighestVersion'
_O='coscpBundleId'
_N='coscpBundleRemoteSwitchId'
_M='CoscpBundleId'
_L='coscpLinkPortId'
_K='milliseconds'
_J='unknown'
_I='TruthValue'
_H='coscpLinkTransDown'
_G='not-accessible'
_F='Integer32'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='CISCO-OSCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
ciscoOscpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,202))
if mibBuilder.loadTexts:ciscoOscpMIB.setRevisions(('2001-05-18 00:00',))
class CoscpSwitchId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class CoscpPortId(TextualConvention,Unsigned32):status=_A
class CoscpBundleId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class CoscpVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('version1',2)))
_CiscoOscpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOscpMIBObjects=_CiscoOscpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,202,1))
_CiscoOscpBaseGroup_ObjectIdentity=ObjectIdentity
ciscoOscpBaseGroup=_CiscoOscpBaseGroup_ObjectIdentity((1,3,6,1,4,1,9,9,202,1,1))
_CoscpHighestVersion_Type=CoscpVersion
_CoscpHighestVersion_Object=MibScalar
coscpHighestVersion=_CoscpHighestVersion_Object((1,3,6,1,4,1,9,9,202,1,1,1),_CoscpHighestVersion_Type())
coscpHighestVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpHighestVersion.setStatus(_A)
_CoscpLowestVersion_Type=CoscpVersion
_CoscpLowestVersion_Object=MibScalar
coscpLowestVersion=_CoscpLowestVersion_Object((1,3,6,1,4,1,9,9,202,1,1,2),_CoscpLowestVersion_Type())
coscpLowestVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLowestVersion.setStatus(_A)
_CoscpSwitchId_Type=CoscpSwitchId
_CoscpSwitchId_Object=MibScalar
coscpSwitchId=_CoscpSwitchId_Object((1,3,6,1,4,1,9,9,202,1,1,3),_CoscpSwitchId_Type())
coscpSwitchId.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpSwitchId.setStatus(_A)
class _CoscpPriorityChangeMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('immediate',1),('delayed',2)))
_CoscpPriorityChangeMode_Type.__name__=_F
_CoscpPriorityChangeMode_Object=MibScalar
coscpPriorityChangeMode=_CoscpPriorityChangeMode_Object((1,3,6,1,4,1,9,9,202,1,1,4),_CoscpPriorityChangeMode_Type())
coscpPriorityChangeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpPriorityChangeMode.setStatus(_A)
class _CoscpHelloHoldDown_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_CoscpHelloHoldDown_Type.__name__=_E
_CoscpHelloHoldDown_Object=MibScalar
coscpHelloHoldDown=_CoscpHelloHoldDown_Object((1,3,6,1,4,1,9,9,202,1,1,5),_CoscpHelloHoldDown_Type())
coscpHelloHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpHelloHoldDown.setStatus(_A)
if mibBuilder.loadTexts:coscpHelloHoldDown.setUnits(_K)
class _CoscpHelloInterval_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,30000))
_CoscpHelloInterval_Type.__name__=_E
_CoscpHelloInterval_Object=MibScalar
coscpHelloInterval=_CoscpHelloInterval_Object((1,3,6,1,4,1,9,9,202,1,1,6),_CoscpHelloInterval_Type())
coscpHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:coscpHelloInterval.setUnits(_K)
class _CoscpHelloInactivityFactor_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,50))
_CoscpHelloInactivityFactor_Type.__name__=_E
_CoscpHelloInactivityFactor_Object=MibScalar
coscpHelloInactivityFactor=_CoscpHelloInactivityFactor_Object((1,3,6,1,4,1,9,9,202,1,1,7),_CoscpHelloInactivityFactor_Type())
coscpHelloInactivityFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpHelloInactivityFactor.setStatus(_A)
class _CoscpNotifiesEnabled_Type(TruthValue):defaultValue=2
_CoscpNotifiesEnabled_Type.__name__=_I
_CoscpNotifiesEnabled_Object=MibScalar
coscpNotifiesEnabled=_CoscpNotifiesEnabled_Object((1,3,6,1,4,1,9,9,202,1,1,8),_CoscpNotifiesEnabled_Type())
coscpNotifiesEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpNotifiesEnabled.setStatus(_A)
_CoscpLinkTable_Object=MibTable
coscpLinkTable=_CoscpLinkTable_Object((1,3,6,1,4,1,9,9,202,1,2))
if mibBuilder.loadTexts:coscpLinkTable.setStatus(_A)
_CoscpLinkEntry_Object=MibTableRow
coscpLinkEntry=_CoscpLinkEntry_Object((1,3,6,1,4,1,9,9,202,1,2,1))
coscpLinkEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:coscpLinkEntry.setStatus(_A)
_CoscpLinkPortId_Type=CoscpPortId
_CoscpLinkPortId_Object=MibTableColumn
coscpLinkPortId=_CoscpLinkPortId_Object((1,3,6,1,4,1,9,9,202,1,2,1,1),_CoscpLinkPortId_Type())
coscpLinkPortId.setMaxAccess(_G)
if mibBuilder.loadTexts:coscpLinkPortId.setStatus(_A)
class _CoscpLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('dedicatedWavelength',2),('inBand',3)))
_CoscpLinkType_Type.__name__=_F
_CoscpLinkType_Object=MibTableColumn
coscpLinkType=_CoscpLinkType_Object((1,3,6,1,4,1,9,9,202,1,2,1,2),_CoscpLinkType_Type())
coscpLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkType.setStatus(_A)
_CoscpLinkVersion_Type=CoscpVersion
_CoscpLinkVersion_Object=MibTableColumn
coscpLinkVersion=_CoscpLinkVersion_Object((1,3,6,1,4,1,9,9,202,1,2,1,3),_CoscpLinkVersion_Type())
coscpLinkVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkVersion.setStatus(_A)
class _CoscpLinkHelloState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),('attempt',2),('oneWay',3),('twoWay',4)))
_CoscpLinkHelloState_Type.__name__=_F
_CoscpLinkHelloState_Object=MibTableColumn
coscpLinkHelloState=_CoscpLinkHelloState_Object((1,3,6,1,4,1,9,9,202,1,2,1,4),_CoscpLinkHelloState_Type())
coscpLinkHelloState.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkHelloState.setStatus(_A)
_CoscpLinkRemoteSwitchId_Type=CoscpSwitchId
_CoscpLinkRemoteSwitchId_Object=MibTableColumn
coscpLinkRemoteSwitchId=_CoscpLinkRemoteSwitchId_Object((1,3,6,1,4,1,9,9,202,1,2,1,5),_CoscpLinkRemoteSwitchId_Type())
coscpLinkRemoteSwitchId.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkRemoteSwitchId.setStatus(_A)
_CoscpLinkRemotePortId_Type=CoscpPortId
_CoscpLinkRemotePortId_Object=MibTableColumn
coscpLinkRemotePortId=_CoscpLinkRemotePortId_Object((1,3,6,1,4,1,9,9,202,1,2,1,6),_CoscpLinkRemotePortId_Type())
coscpLinkRemotePortId.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkRemotePortId.setStatus(_A)
_CoscpLinkDerivedBundleId_Type=CoscpBundleId
_CoscpLinkDerivedBundleId_Object=MibTableColumn
coscpLinkDerivedBundleId=_CoscpLinkDerivedBundleId_Object((1,3,6,1,4,1,9,9,202,1,2,1,7),_CoscpLinkDerivedBundleId_Type())
coscpLinkDerivedBundleId.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkDerivedBundleId.setStatus(_A)
class _CoscpLinkConfigBundleId_Type(CoscpBundleId):defaultValue=0
_CoscpLinkConfigBundleId_Type.__name__=_M
_CoscpLinkConfigBundleId_Object=MibTableColumn
coscpLinkConfigBundleId=_CoscpLinkConfigBundleId_Object((1,3,6,1,4,1,9,9,202,1,2,1,8),_CoscpLinkConfigBundleId_Type())
coscpLinkConfigBundleId.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpLinkConfigBundleId.setStatus(_A)
_CoscpLinkIfIndex_Type=InterfaceIndex
_CoscpLinkIfIndex_Object=MibTableColumn
coscpLinkIfIndex=_CoscpLinkIfIndex_Object((1,3,6,1,4,1,9,9,202,1,2,1,9),_CoscpLinkIfIndex_Type())
coscpLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkIfIndex.setStatus(_A)
class _CoscpLinkSelPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CoscpLinkSelPriority_Type.__name__=_E
_CoscpLinkSelPriority_Object=MibTableColumn
coscpLinkSelPriority=_CoscpLinkSelPriority_Object((1,3,6,1,4,1,9,9,202,1,2,1,10),_CoscpLinkSelPriority_Type())
coscpLinkSelPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:coscpLinkSelPriority.setStatus(_A)
_CoscpLinkInHellos_Type=Counter32
_CoscpLinkInHellos_Object=MibTableColumn
coscpLinkInHellos=_CoscpLinkInHellos_Object((1,3,6,1,4,1,9,9,202,1,2,1,11),_CoscpLinkInHellos_Type())
coscpLinkInHellos.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkInHellos.setStatus(_A)
_CoscpLinkInDiscardedHellos_Type=Counter32
_CoscpLinkInDiscardedHellos_Object=MibTableColumn
coscpLinkInDiscardedHellos=_CoscpLinkInDiscardedHellos_Object((1,3,6,1,4,1,9,9,202,1,2,1,12),_CoscpLinkInDiscardedHellos_Type())
coscpLinkInDiscardedHellos.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkInDiscardedHellos.setStatus(_A)
_CoscpLinkOutHellos_Type=Counter32
_CoscpLinkOutHellos_Object=MibTableColumn
coscpLinkOutHellos=_CoscpLinkOutHellos_Object((1,3,6,1,4,1,9,9,202,1,2,1,13),_CoscpLinkOutHellos_Type())
coscpLinkOutHellos.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkOutHellos.setStatus(_A)
_CoscpLinkTransDown_Type=Counter32
_CoscpLinkTransDown_Object=MibTableColumn
coscpLinkTransDown=_CoscpLinkTransDown_Object((1,3,6,1,4,1,9,9,202,1,2,1,14),_CoscpLinkTransDown_Type())
coscpLinkTransDown.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpLinkTransDown.setStatus(_A)
_CoscpBundleTable_Object=MibTable
coscpBundleTable=_CoscpBundleTable_Object((1,3,6,1,4,1,9,9,202,1,3))
if mibBuilder.loadTexts:coscpBundleTable.setStatus(_A)
_CoscpBundleEntry_Object=MibTableRow
coscpBundleEntry=_CoscpBundleEntry_Object((1,3,6,1,4,1,9,9,202,1,3,1))
coscpBundleEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:coscpBundleEntry.setStatus(_A)
_CoscpBundleRemoteSwitchId_Type=CoscpSwitchId
_CoscpBundleRemoteSwitchId_Object=MibTableColumn
coscpBundleRemoteSwitchId=_CoscpBundleRemoteSwitchId_Object((1,3,6,1,4,1,9,9,202,1,3,1,1),_CoscpBundleRemoteSwitchId_Type())
coscpBundleRemoteSwitchId.setMaxAccess(_G)
if mibBuilder.loadTexts:coscpBundleRemoteSwitchId.setStatus(_A)
_CoscpBundleId_Type=CoscpBundleId
_CoscpBundleId_Object=MibTableColumn
coscpBundleId=_CoscpBundleId_Object((1,3,6,1,4,1,9,9,202,1,3,1,2),_CoscpBundleId_Type())
coscpBundleId.setMaxAccess(_G)
if mibBuilder.loadTexts:coscpBundleId.setStatus(_A)
_CoscpBundleActivePortId_Type=CoscpPortId
_CoscpBundleActivePortId_Object=MibTableColumn
coscpBundleActivePortId=_CoscpBundleActivePortId_Object((1,3,6,1,4,1,9,9,202,1,3,1,3),_CoscpBundleActivePortId_Type())
coscpBundleActivePortId.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpBundleActivePortId.setStatus(_A)
_CoscpBundleIfIndex_Type=InterfaceIndex
_CoscpBundleIfIndex_Object=MibTableColumn
coscpBundleIfIndex=_CoscpBundleIfIndex_Object((1,3,6,1,4,1,9,9,202,1,3,1,4),_CoscpBundleIfIndex_Type())
coscpBundleIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpBundleIfIndex.setStatus(_A)
_CoscpBundlePortCount_Type=Gauge32
_CoscpBundlePortCount_Object=MibTableColumn
coscpBundlePortCount=_CoscpBundlePortCount_Object((1,3,6,1,4,1,9,9,202,1,3,1,5),_CoscpBundlePortCount_Type())
coscpBundlePortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coscpBundlePortCount.setStatus(_A)
_CoscpBundleRowStatus_Type=RowStatus
_CoscpBundleRowStatus_Object=MibTableColumn
coscpBundleRowStatus=_CoscpBundleRowStatus_Object((1,3,6,1,4,1,9,9,202,1,3,1,6),_CoscpBundleRowStatus_Type())
coscpBundleRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:coscpBundleRowStatus.setStatus(_A)
_CiscoOscpMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoOscpMIBNotifications=_CiscoOscpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,202,2))
_CiscoOscpNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoOscpNotificationsPrefix=_CiscoOscpNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,202,2,0))
_CiscoOscpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoOscpMIBConformance=_CiscoOscpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,202,3))
_CiscoOscpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOscpMIBCompliances=_CiscoOscpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,202,3,1))
_CiscoOscpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOscpMIBGroups=_CiscoOscpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,202,3,2))
ciscoOscpBasicGroup=ObjectGroup((1,3,6,1,4,1,9,9,202,3,2,1))
ciscoOscpBasicGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_H)))
if mibBuilder.loadTexts:ciscoOscpBasicGroup.setStatus(_A)
ciscoOscpBundleGroup=ObjectGroup((1,3,6,1,4,1,9,9,202,3,2,2))
ciscoOscpBundleGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ciscoOscpBundleGroup.setStatus(_A)
coscpNotifyTransDown=NotificationType((1,3,6,1,4,1,9,9,202,2,0,1))
coscpNotifyTransDown.setObjects((_B,_H))
if mibBuilder.loadTexts:coscpNotifyTransDown.setStatus(_A)
ciscoOscpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,202,3,2,3))
ciscoOscpNotificationsGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:ciscoOscpNotificationsGroup.setStatus(_A)
ciscoOscpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,202,3,1,1))
ciscoOscpMIBCompliance.setObjects(*((_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoOscpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CoscpSwitchId':CoscpSwitchId,'CoscpPortId':CoscpPortId,_M:CoscpBundleId,'CoscpVersion':CoscpVersion,'ciscoOscpMIB':ciscoOscpMIB,'ciscoOscpMIBObjects':ciscoOscpMIBObjects,'ciscoOscpBaseGroup':ciscoOscpBaseGroup,_P:coscpHighestVersion,_Q:coscpLowestVersion,_R:coscpSwitchId,_f:coscpPriorityChangeMode,_S:coscpHelloHoldDown,_T:coscpHelloInterval,_U:coscpHelloInactivityFactor,_V:coscpNotifiesEnabled,'coscpLinkTable':coscpLinkTable,'coscpLinkEntry':coscpLinkEntry,_L:coscpLinkPortId,_W:coscpLinkType,_X:coscpLinkVersion,_Y:coscpLinkHelloState,_Z:coscpLinkRemoteSwitchId,_a:coscpLinkRemotePortId,_g:coscpLinkDerivedBundleId,_h:coscpLinkConfigBundleId,_b:coscpLinkIfIndex,_i:coscpLinkSelPriority,_c:coscpLinkInHellos,_d:coscpLinkInDiscardedHellos,_e:coscpLinkOutHellos,_H:coscpLinkTransDown,'coscpBundleTable':coscpBundleTable,'coscpBundleEntry':coscpBundleEntry,_N:coscpBundleRemoteSwitchId,_O:coscpBundleId,_j:coscpBundleActivePortId,_k:coscpBundleIfIndex,_l:coscpBundlePortCount,_m:coscpBundleRowStatus,'ciscoOscpMIBNotifications':ciscoOscpMIBNotifications,'ciscoOscpNotificationsPrefix':ciscoOscpNotificationsPrefix,_n:coscpNotifyTransDown,'ciscoOscpMIBConformance':ciscoOscpMIBConformance,'ciscoOscpMIBCompliances':ciscoOscpMIBCompliances,'ciscoOscpMIBCompliance':ciscoOscpMIBCompliance,'ciscoOscpMIBGroups':ciscoOscpMIBGroups,_o:ciscoOscpBasicGroup,_q:ciscoOscpBundleGroup,_p:ciscoOscpNotificationsGroup})