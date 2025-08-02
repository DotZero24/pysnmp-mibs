_g='cFCCPortEntriesGroupRev1'
_f='cFCCPortEntriesGroup'
_e='ciscoFCCCongestionRateLimitEnd'
_d='ciscoFCCCongestionRateLimitStart'
_c='ciscoFCCCongestionStateChange'
_b='cFCCIsRateLimitingApplied'
_a='cFCCLastCongestionStartTime'
_Z='deprecated'
_Y='cFCCNotificationEnable'
_X='cFCCPacketPriority'
_W='cFCCEnable'
_V='TruthValue'
_U='cFCCNotificationGroup'
_T='cFCCNotificationObjectsGroup'
_S='cFCCConfigurationGroup'
_R='cFCCCongestionState'
_Q='cFCCLastCongestedTime'
_P='cFCCCurrentCongestionState'
_O='cFCCPathQuenchPktsSent'
_N='cFCCPathQuenchPktsRecd'
_M='cFCCEdgeQuenchPktsSent'
_L='cFCCEdgeQuenchPktsRecd'
_K='read-write'
_J='Integer32'
_I='cFCCCongestionNotifyVSANIndex'
_H='cFCCCongestionSourceID'
_G='cFCCCongestionDestinationID'
_F='accessible-for-notify'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='current'
_A='CISCO-FCC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddressId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcAddressId','VsanIndex')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_V)
ciscoFCCMIB=ModuleIdentity((1,3,6,1,4,1,9,9,365))
if mibBuilder.loadTexts:ciscoFCCMIB.setRevisions(('2004-07-08 00:00','2004-02-25 00:00','2003-08-06 00:00','2003-05-26 00:00'))
class CiscoFCCCongestionState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCongestion',1),('congested',2),('severelyCongested',3)))
_CiscoFCCMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFCCMIBNotifs=_CiscoFCCMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,365,0))
_CiscoFCCMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFCCMIBObjects=_CiscoFCCMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,365,1))
_CFCCConfig_ObjectIdentity=ObjectIdentity
cFCCConfig=_CFCCConfig_ObjectIdentity((1,3,6,1,4,1,9,9,365,1,1))
class _CFCCEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CFCCEnable_Type.__name__=_J
_CFCCEnable_Object=MibScalar
cFCCEnable=_CFCCEnable_Object((1,3,6,1,4,1,9,9,365,1,1,1),_CFCCEnable_Type())
cFCCEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:cFCCEnable.setStatus(_B)
class _CFCCPacketPriority_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CFCCPacketPriority_Type.__name__=_J
_CFCCPacketPriority_Object=MibScalar
cFCCPacketPriority=_CFCCPacketPriority_Object((1,3,6,1,4,1,9,9,365,1,1,2),_CFCCPacketPriority_Type())
cFCCPacketPriority.setMaxAccess(_K)
if mibBuilder.loadTexts:cFCCPacketPriority.setStatus(_B)
class _CFCCNotificationEnable_Type(TruthValue):defaultValue=2
_CFCCNotificationEnable_Type.__name__=_V
_CFCCNotificationEnable_Object=MibScalar
cFCCNotificationEnable=_CFCCNotificationEnable_Object((1,3,6,1,4,1,9,9,365,1,1,3),_CFCCNotificationEnable_Type())
cFCCNotificationEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:cFCCNotificationEnable.setStatus(_B)
_CFCCPortEntries_ObjectIdentity=ObjectIdentity
cFCCPortEntries=_CFCCPortEntries_ObjectIdentity((1,3,6,1,4,1,9,9,365,1,2))
_CFCCPortTable_Object=MibTable
cFCCPortTable=_CFCCPortTable_Object((1,3,6,1,4,1,9,9,365,1,2,1))
if mibBuilder.loadTexts:cFCCPortTable.setStatus(_B)
_CFCCPortEntry_Object=MibTableRow
cFCCPortEntry=_CFCCPortEntry_Object((1,3,6,1,4,1,9,9,365,1,2,1,1))
cFCCPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cFCCPortEntry.setStatus(_B)
_CFCCEdgeQuenchPktsRecd_Type=Counter32
_CFCCEdgeQuenchPktsRecd_Object=MibTableColumn
cFCCEdgeQuenchPktsRecd=_CFCCEdgeQuenchPktsRecd_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,1),_CFCCEdgeQuenchPktsRecd_Type())
cFCCEdgeQuenchPktsRecd.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCEdgeQuenchPktsRecd.setStatus(_B)
_CFCCEdgeQuenchPktsSent_Type=Counter32
_CFCCEdgeQuenchPktsSent_Object=MibTableColumn
cFCCEdgeQuenchPktsSent=_CFCCEdgeQuenchPktsSent_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,2),_CFCCEdgeQuenchPktsSent_Type())
cFCCEdgeQuenchPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCEdgeQuenchPktsSent.setStatus(_B)
_CFCCPathQuenchPktsRecd_Type=Counter32
_CFCCPathQuenchPktsRecd_Object=MibTableColumn
cFCCPathQuenchPktsRecd=_CFCCPathQuenchPktsRecd_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,3),_CFCCPathQuenchPktsRecd_Type())
cFCCPathQuenchPktsRecd.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCPathQuenchPktsRecd.setStatus(_B)
_CFCCPathQuenchPktsSent_Type=Counter32
_CFCCPathQuenchPktsSent_Object=MibTableColumn
cFCCPathQuenchPktsSent=_CFCCPathQuenchPktsSent_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,4),_CFCCPathQuenchPktsSent_Type())
cFCCPathQuenchPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCPathQuenchPktsSent.setStatus(_B)
_CFCCCurrentCongestionState_Type=CiscoFCCCongestionState
_CFCCCurrentCongestionState_Object=MibTableColumn
cFCCCurrentCongestionState=_CFCCCurrentCongestionState_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,5),_CFCCCurrentCongestionState_Type())
cFCCCurrentCongestionState.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCCurrentCongestionState.setStatus(_B)
_CFCCLastCongestedTime_Type=TimeStamp
_CFCCLastCongestedTime_Object=MibTableColumn
cFCCLastCongestedTime=_CFCCLastCongestedTime_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,6),_CFCCLastCongestedTime_Type())
cFCCLastCongestedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCLastCongestedTime.setStatus(_B)
_CFCCLastCongestionStartTime_Type=TimeStamp
_CFCCLastCongestionStartTime_Object=MibTableColumn
cFCCLastCongestionStartTime=_CFCCLastCongestionStartTime_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,7),_CFCCLastCongestionStartTime_Type())
cFCCLastCongestionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCLastCongestionStartTime.setStatus(_B)
_CFCCIsRateLimitingApplied_Type=TruthValue
_CFCCIsRateLimitingApplied_Object=MibTableColumn
cFCCIsRateLimitingApplied=_CFCCIsRateLimitingApplied_Object((1,3,6,1,4,1,9,9,365,1,2,1,1,8),_CFCCIsRateLimitingApplied_Type())
cFCCIsRateLimitingApplied.setMaxAccess(_C)
if mibBuilder.loadTexts:cFCCIsRateLimitingApplied.setStatus(_B)
_CFCCNotifObjects_ObjectIdentity=ObjectIdentity
cFCCNotifObjects=_CFCCNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,365,1,3))
_CFCCCongestionSourceID_Type=FcAddressId
_CFCCCongestionSourceID_Object=MibScalar
cFCCCongestionSourceID=_CFCCCongestionSourceID_Object((1,3,6,1,4,1,9,9,365,1,3,1),_CFCCCongestionSourceID_Type())
cFCCCongestionSourceID.setMaxAccess(_F)
if mibBuilder.loadTexts:cFCCCongestionSourceID.setStatus(_B)
_CFCCCongestionDestinationID_Type=FcAddressId
_CFCCCongestionDestinationID_Object=MibScalar
cFCCCongestionDestinationID=_CFCCCongestionDestinationID_Object((1,3,6,1,4,1,9,9,365,1,3,2),_CFCCCongestionDestinationID_Type())
cFCCCongestionDestinationID.setMaxAccess(_F)
if mibBuilder.loadTexts:cFCCCongestionDestinationID.setStatus(_B)
_CFCCCongestionNotifyVSANIndex_Type=VsanIndex
_CFCCCongestionNotifyVSANIndex_Object=MibScalar
cFCCCongestionNotifyVSANIndex=_CFCCCongestionNotifyVSANIndex_Object((1,3,6,1,4,1,9,9,365,1,3,3),_CFCCCongestionNotifyVSANIndex_Type())
cFCCCongestionNotifyVSANIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cFCCCongestionNotifyVSANIndex.setStatus(_B)
_CFCCCongestionState_Type=CiscoFCCCongestionState
_CFCCCongestionState_Object=MibScalar
cFCCCongestionState=_CFCCCongestionState_Object((1,3,6,1,4,1,9,9,365,1,3,4),_CFCCCongestionState_Type())
cFCCCongestionState.setMaxAccess(_F)
if mibBuilder.loadTexts:cFCCCongestionState.setStatus(_B)
_CiscoFCCMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFCCMIBConformance=_CiscoFCCMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,365,2))
_CiscoFCCMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFCCMIBCompliances=_CiscoFCCMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,365,2,1))
_CiscoFCCMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFCCMIBGroups=_CiscoFCCMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,365,2,2))
cFCCConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,365,2,2,1))
cFCCConfigurationGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cFCCConfigurationGroup.setStatus(_B)
cFCCPortEntriesGroup=ObjectGroup((1,3,6,1,4,1,9,9,365,2,2,2))
cFCCPortEntriesGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:cFCCPortEntriesGroup.setStatus(_Z)
cFCCNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,365,2,2,3))
cFCCNotificationObjectsGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_R)))
if mibBuilder.loadTexts:cFCCNotificationObjectsGroup.setStatus(_B)
cFCCPortEntriesGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,365,2,2,5))
cFCCPortEntriesGroupRev1.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cFCCPortEntriesGroupRev1.setStatus(_B)
ciscoFCCCongestionStateChange=NotificationType((1,3,6,1,4,1,9,9,365,0,1))
ciscoFCCCongestionStateChange.setObjects(*((_D,_E),(_A,_R)))
if mibBuilder.loadTexts:ciscoFCCCongestionStateChange.setStatus(_B)
ciscoFCCCongestionRateLimitStart=NotificationType((1,3,6,1,4,1,9,9,365,0,2))
ciscoFCCCongestionRateLimitStart.setObjects(*((_D,_E),(_A,_H),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:ciscoFCCCongestionRateLimitStart.setStatus(_B)
ciscoFCCCongestionRateLimitEnd=NotificationType((1,3,6,1,4,1,9,9,365,0,3))
ciscoFCCCongestionRateLimitEnd.setObjects(*((_D,_E),(_A,_H),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:ciscoFCCCongestionRateLimitEnd.setStatus(_B)
cFCCNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,365,2,2,4))
cFCCNotificationGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cFCCNotificationGroup.setStatus(_B)
ciscoFCCMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,365,2,1,1))
ciscoFCCMIBCompliance.setObjects(*((_A,_S),(_A,_f),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoFCCMIBCompliance.setStatus(_Z)
ciscoFCCMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,365,2,1,2))
ciscoFCCMIBComplianceRev1.setObjects(*((_A,_S),(_A,_g),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoFCCMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoFCCCongestionState':CiscoFCCCongestionState,'ciscoFCCMIB':ciscoFCCMIB,'ciscoFCCMIBNotifs':ciscoFCCMIBNotifs,_c:ciscoFCCCongestionStateChange,_d:ciscoFCCCongestionRateLimitStart,_e:ciscoFCCCongestionRateLimitEnd,'ciscoFCCMIBObjects':ciscoFCCMIBObjects,'cFCCConfig':cFCCConfig,_W:cFCCEnable,_X:cFCCPacketPriority,_Y:cFCCNotificationEnable,'cFCCPortEntries':cFCCPortEntries,'cFCCPortTable':cFCCPortTable,'cFCCPortEntry':cFCCPortEntry,_L:cFCCEdgeQuenchPktsRecd,_M:cFCCEdgeQuenchPktsSent,_N:cFCCPathQuenchPktsRecd,_O:cFCCPathQuenchPktsSent,_P:cFCCCurrentCongestionState,_Q:cFCCLastCongestedTime,_a:cFCCLastCongestionStartTime,_b:cFCCIsRateLimitingApplied,'cFCCNotifObjects':cFCCNotifObjects,_H:cFCCCongestionSourceID,_G:cFCCCongestionDestinationID,_I:cFCCCongestionNotifyVSANIndex,_R:cFCCCongestionState,'ciscoFCCMIBConformance':ciscoFCCMIBConformance,'ciscoFCCMIBCompliances':ciscoFCCMIBCompliances,'ciscoFCCMIBCompliance':ciscoFCCMIBCompliance,'ciscoFCCMIBComplianceRev1':ciscoFCCMIBComplianceRev1,'ciscoFCCMIBGroups':ciscoFCCMIBGroups,_S:cFCCConfigurationGroup,_f:cFCCPortEntriesGroup,_T:cFCCNotificationObjectsGroup,_U:cFCCNotificationGroup,_g:cFCCPortEntriesGroupRev1})