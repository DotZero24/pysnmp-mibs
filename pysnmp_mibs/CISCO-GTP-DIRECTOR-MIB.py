_V='ciscoGtpDirectorNotifGroup'
_U='ciscoGtpDirectorNotifMgmtGroup'
_T='ciscoGtpDirectorStatisticsGroup'
_S='ciscoGtpDirectorStatusGroup'
_R='ciscoGtpDirectorConfigurationsGroup'
_Q='ciscoGtpDirectorNotification'
_P='cgdNotifEnable'
_O='cgdPdpRequestDropped'
_N='cgdTotalUnsupportedMessages'
_M='cgdCreateRequestRejected'
_L='cgdTotalCreatePdpRequestFwded'
_K='cgdCreatePdpRequestFwded'
_J='cgdPendingPdps'
_I='cgdCreatePdpRequestInfoSaveTimer'
_H='read-write'
_G='TruthValue'
_F='Unsigned32'
_E='Integer32'
_D='cgdNotifType'
_C='read-only'
_B='current'
_A='CISCO-GTP-DIRECTOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
ciscoGtpDirectorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,245))
if mibBuilder.loadTexts:ciscoGtpDirectorMIB.setRevisions(('2001-09-13 14:00',))
_CiscoGtpDirectorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGtpDirectorMIBObjects=_CiscoGtpDirectorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,245,1))
_CgdConfigurations_ObjectIdentity=ObjectIdentity
cgdConfigurations=_CgdConfigurations_ObjectIdentity((1,3,6,1,4,1,9,9,245,1,1))
class _CgdCreatePdpRequestInfoSaveTimer_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CgdCreatePdpRequestInfoSaveTimer_Type.__name__=_F
_CgdCreatePdpRequestInfoSaveTimer_Object=MibScalar
cgdCreatePdpRequestInfoSaveTimer=_CgdCreatePdpRequestInfoSaveTimer_Object((1,3,6,1,4,1,9,9,245,1,1,1),_CgdCreatePdpRequestInfoSaveTimer_Type())
cgdCreatePdpRequestInfoSaveTimer.setMaxAccess(_H)
if mibBuilder.loadTexts:cgdCreatePdpRequestInfoSaveTimer.setStatus(_B)
if mibBuilder.loadTexts:cgdCreatePdpRequestInfoSaveTimer.setUnits('seconds')
_CgdStatus_ObjectIdentity=ObjectIdentity
cgdStatus=_CgdStatus_ObjectIdentity((1,3,6,1,4,1,9,9,245,1,2))
_CgdPendingPdps_Type=Gauge32
_CgdPendingPdps_Object=MibScalar
cgdPendingPdps=_CgdPendingPdps_Object((1,3,6,1,4,1,9,9,245,1,2,1),_CgdPendingPdps_Type())
cgdPendingPdps.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdPendingPdps.setStatus(_B)
_CgdStatistics_ObjectIdentity=ObjectIdentity
cgdStatistics=_CgdStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,245,1,3))
_CgdCreatePdpRequestFwded_Type=Counter32
_CgdCreatePdpRequestFwded_Object=MibScalar
cgdCreatePdpRequestFwded=_CgdCreatePdpRequestFwded_Object((1,3,6,1,4,1,9,9,245,1,3,1),_CgdCreatePdpRequestFwded_Type())
cgdCreatePdpRequestFwded.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdCreatePdpRequestFwded.setStatus(_B)
_CgdTotalCreatePdpRequestFwded_Type=Counter32
_CgdTotalCreatePdpRequestFwded_Object=MibScalar
cgdTotalCreatePdpRequestFwded=_CgdTotalCreatePdpRequestFwded_Object((1,3,6,1,4,1,9,9,245,1,3,2),_CgdTotalCreatePdpRequestFwded_Type())
cgdTotalCreatePdpRequestFwded.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalCreatePdpRequestFwded.setStatus(_B)
_CgdCreateRequestRejected_Type=Counter32
_CgdCreateRequestRejected_Object=MibScalar
cgdCreateRequestRejected=_CgdCreateRequestRejected_Object((1,3,6,1,4,1,9,9,245,1,3,3),_CgdCreateRequestRejected_Type())
cgdCreateRequestRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdCreateRequestRejected.setStatus(_B)
_CgdTotalUnsupportedMessages_Type=Counter32
_CgdTotalUnsupportedMessages_Object=MibScalar
cgdTotalUnsupportedMessages=_CgdTotalUnsupportedMessages_Object((1,3,6,1,4,1,9,9,245,1,3,4),_CgdTotalUnsupportedMessages_Type())
cgdTotalUnsupportedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalUnsupportedMessages.setStatus(_B)
_CgdPdpRequestDropped_Type=Counter32
_CgdPdpRequestDropped_Object=MibScalar
cgdPdpRequestDropped=_CgdPdpRequestDropped_Object((1,3,6,1,4,1,9,9,245,1,3,5),_CgdPdpRequestDropped_Type())
cgdPdpRequestDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdPdpRequestDropped.setStatus(_B)
_CgdNotifMgmt_ObjectIdentity=ObjectIdentity
cgdNotifMgmt=_CgdNotifMgmt_ObjectIdentity((1,3,6,1,4,1,9,9,245,1,4))
class _CgdNotifEnable_Type(TruthValue):defaultValue=2
_CgdNotifEnable_Type.__name__=_G
_CgdNotifEnable_Object=MibScalar
cgdNotifEnable=_CgdNotifEnable_Object((1,3,6,1,4,1,9,9,245,1,4,1),_CgdNotifEnable_Type())
cgdNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cgdNotifEnable.setStatus(_B)
class _CgdNotifType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gdmServiceUp',1),('gdmServiceDown',2)))
_CgdNotifType_Type.__name__=_E
_CgdNotifType_Object=MibScalar
cgdNotifType=_CgdNotifType_Object((1,3,6,1,4,1,9,9,245,1,4,2),_CgdNotifType_Type())
cgdNotifType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cgdNotifType.setStatus(_B)
_CiscoGtpDirectorNotifPrefix_ObjectIdentity=ObjectIdentity
ciscoGtpDirectorNotifPrefix=_CiscoGtpDirectorNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,245,2))
_CiscoGtpDirectorNotifications_ObjectIdentity=ObjectIdentity
ciscoGtpDirectorNotifications=_CiscoGtpDirectorNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,245,2,0))
_CiscoGtpDirectorMIBConformance_ObjectIdentity=ObjectIdentity
ciscoGtpDirectorMIBConformance=_CiscoGtpDirectorMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,245,3))
_CiscoGtpDirectorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGtpDirectorMIBCompliances=_CiscoGtpDirectorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,245,3,1))
_CiscoGtpDirectorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGtpDirectorMIBGroups=_CiscoGtpDirectorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,245,3,2))
ciscoGtpDirectorConfigurationsGroup=ObjectGroup((1,3,6,1,4,1,9,9,245,3,2,1))
ciscoGtpDirectorConfigurationsGroup.setObjects((_A,_I))
if mibBuilder.loadTexts:ciscoGtpDirectorConfigurationsGroup.setStatus(_B)
ciscoGtpDirectorStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,245,3,2,2))
ciscoGtpDirectorStatusGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoGtpDirectorStatusGroup.setStatus(_B)
ciscoGtpDirectorStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,245,3,2,3))
ciscoGtpDirectorStatisticsGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoGtpDirectorStatisticsGroup.setStatus(_B)
ciscoGtpDirectorNotifMgmtGroup=ObjectGroup((1,3,6,1,4,1,9,9,245,3,2,4))
ciscoGtpDirectorNotifMgmtGroup.setObjects(*((_A,_P),(_A,_D)))
if mibBuilder.loadTexts:ciscoGtpDirectorNotifMgmtGroup.setStatus(_B)
ciscoGtpDirectorNotification=NotificationType((1,3,6,1,4,1,9,9,245,2,0,1))
ciscoGtpDirectorNotification.setObjects((_A,_D))
if mibBuilder.loadTexts:ciscoGtpDirectorNotification.setStatus(_B)
ciscoGtpDirectorNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,245,3,2,5))
ciscoGtpDirectorNotifGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:ciscoGtpDirectorNotifGroup.setStatus(_B)
ciscoGtpDirectorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,245,3,1,1))
ciscoGtpDirectorMIBCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoGtpDirectorMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoGtpDirectorMIB':ciscoGtpDirectorMIB,'ciscoGtpDirectorMIBObjects':ciscoGtpDirectorMIBObjects,'cgdConfigurations':cgdConfigurations,_I:cgdCreatePdpRequestInfoSaveTimer,'cgdStatus':cgdStatus,_J:cgdPendingPdps,'cgdStatistics':cgdStatistics,_K:cgdCreatePdpRequestFwded,_L:cgdTotalCreatePdpRequestFwded,_M:cgdCreateRequestRejected,_N:cgdTotalUnsupportedMessages,_O:cgdPdpRequestDropped,'cgdNotifMgmt':cgdNotifMgmt,_P:cgdNotifEnable,_D:cgdNotifType,'ciscoGtpDirectorNotifPrefix':ciscoGtpDirectorNotifPrefix,'ciscoGtpDirectorNotifications':ciscoGtpDirectorNotifications,_Q:ciscoGtpDirectorNotification,'ciscoGtpDirectorMIBConformance':ciscoGtpDirectorMIBConformance,'ciscoGtpDirectorMIBCompliances':ciscoGtpDirectorMIBCompliances,'ciscoGtpDirectorMIBCompliance':ciscoGtpDirectorMIBCompliance,'ciscoGtpDirectorMIBGroups':ciscoGtpDirectorMIBGroups,_R:ciscoGtpDirectorConfigurationsGroup,_S:ciscoGtpDirectorStatusGroup,_T:ciscoGtpDirectorStatisticsGroup,_U:ciscoGtpDirectorNotifMgmtGroup,_V:ciscoGtpDirectorNotifGroup})