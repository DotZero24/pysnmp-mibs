_f='ciscoErrDisableFeatureFlapGroup'
_e='ciscoErrDisableNotifGroup'
_d='cErrDisableInterfaceEventRev1'
_c='cErrDisableInterfaceEvent'
_b='cErrDisableFeatureFlapTimePeriod'
_a='cErrDisableFeatureMaxFlapCount'
_Z='cErrDisableFeatureDetectShutdownVlan'
_Y='cErrDisableNotifRate'
_X='cErrDisableNotifEnable'
_W='cErrDisableIfStatusTimeToRecover'
_V='cErrDisableFeatureRecoveryInterval'
_U='cErrDisableFeatureRecoveryEnable'
_T='cErrDisableFeatureDetectEnable'
_S='cErrDisableFeatureConfigurable'
_R='cErrDisableRecoveryInterval'
_Q='cErrDisableIfStatusVlanIndex'
_P='not-accessible'
_O='cErrDisableFeatureIndex'
_N='ifIndex'
_M='IF-MIB'
_L='ciscoErrDisableShutdownVlanGroup'
_K='ciscoErrDisableNotifGroupRev1'
_J='read-only'
_I='ciscoErrDisableNotifCfgGroup'
_H='ciscoErrDisableIfStatusGroup'
_G='ciscoErrDisableFeatureCfgGroup'
_F='ciscoErrDisableGlobalCfgGroup'
_E='deprecated'
_D='cErrDisableIfStatusCause'
_C='read-write'
_B='current'
_A='CISCO-ERR-DISABLE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIndexOrZero,=mibBuilder.importSymbols('CISCO-PRIVATE-VLAN-MIB','VlanIndexOrZero')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
TimeIntervalSec,=mibBuilder.importSymbols('CISCO-TC','TimeIntervalSec')
ifIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoErrDisableMIB=ModuleIdentity((1,3,6,1,4,1,9,9,548))
if mibBuilder.loadTexts:ciscoErrDisableMIB.setRevisions(('2019-11-28 00:00','2016-06-02 00:00','2013-04-23 00:00','2010-10-19 00:00','2009-03-23 00:00','2008-04-07 00:00','2006-05-31 00:00'))
class CErrDisableFeatureID(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62)));namedValues=NamedValues(*(('udld',1),('bpduGuard',2),('channelMisconfig',3),('pagpFlap',4),('dtpFlap',5),('linkFlap',6),('l2ptGuard',7),('dot1xSecurityViolation',8),('portSecurityViolation',9),('gbicInvalid',10),('dhcpRateLimit',11),('unicastFlood',12),('vmps',13),('stormControl',14),('inlinePower',15),('arpInspection',16),('portLoopback',17),('packetBuffer',18),('macLimit',19),('linkMonitorFailure',20),('oamRemoteFailure',21),('dot1adIncompEtype',22),('dot1adIncompTunnel',23),('sfpConfigMismatch',24),('communityLimit',25),('invalidPolicy',26),('lsGroup',27),('ekey',28),('portModeFailure',29),('pppoeIaRateLimit',30),('oamRemoteCriticalEvent',31),('oamRemoteDyingGasp',32),('oamRemoteLinkFault',33),('mvrp',34),('tranceiverIncomp',35),('other',36),('portReinitLimitReached',37),('adminRxBBCreditPerfBufIncomp',38),('ficonNotEnabled',39),('adminModeIncomp',40),('adminSpeedIncomp',41),('adminRxBBCreditIncomp',42),('adminRxBufSizeIncomp',43),('eppFailure',44),('osmEPortUp',45),('osmNonEPortUp',46),('udldUniDir',47),('udldTxRxLoop',48),('udldNeighbourMismatch',49),('udldEmptyEcho',50),('udldAggrasiveModeLinkFailed',51),('excessivePortInterrupts',52),('channelErrDisabled',53),('hwProgFailed',54),('internalHandshakeFailed',55),('stpInconsistencyOnVpcPeerLink',56),('stpPortStateFailure',57),('ipConflict',58),('multipleMSapIdsRcvd',59),('oneHundredPdusWithoutAck',60),('ipQosCompatCheckFailure',61),('loopDetect',62)))
_CiscoErrDisableMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoErrDisableMIBNotifs=_CiscoErrDisableMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,548,0))
_CErrDisableNotificationsPrefix_ObjectIdentity=ObjectIdentity
cErrDisableNotificationsPrefix=_CErrDisableNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,548,0,1))
_CiscoErrDisableMIBObjects_ObjectIdentity=ObjectIdentity
ciscoErrDisableMIBObjects=_CiscoErrDisableMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,548,1))
_CErrDisableGlobalObjects_ObjectIdentity=ObjectIdentity
cErrDisableGlobalObjects=_CErrDisableGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,548,1,1))
_CErrDisableRecoveryInterval_Type=TimeIntervalSec
_CErrDisableRecoveryInterval_Object=MibScalar
cErrDisableRecoveryInterval=_CErrDisableRecoveryInterval_Object((1,3,6,1,4,1,9,9,548,1,1,1),_CErrDisableRecoveryInterval_Type())
cErrDisableRecoveryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableRecoveryInterval.setStatus(_B)
_CErrDisableNotifEnable_Type=TruthValue
_CErrDisableNotifEnable_Object=MibScalar
cErrDisableNotifEnable=_CErrDisableNotifEnable_Object((1,3,6,1,4,1,9,9,548,1,1,2),_CErrDisableNotifEnable_Type())
cErrDisableNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableNotifEnable.setStatus(_B)
_CErrDisableNotifRate_Type=Unsigned32
_CErrDisableNotifRate_Object=MibScalar
cErrDisableNotifRate=_CErrDisableNotifRate_Object((1,3,6,1,4,1,9,9,548,1,1,3),_CErrDisableNotifRate_Type())
cErrDisableNotifRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableNotifRate.setStatus(_B)
if mibBuilder.loadTexts:cErrDisableNotifRate.setUnits('Notification/Minute')
_CErrDisableFeatureObjects_ObjectIdentity=ObjectIdentity
cErrDisableFeatureObjects=_CErrDisableFeatureObjects_ObjectIdentity((1,3,6,1,4,1,9,9,548,1,2))
_CErrDisableFeatureTable_Object=MibTable
cErrDisableFeatureTable=_CErrDisableFeatureTable_Object((1,3,6,1,4,1,9,9,548,1,2,1))
if mibBuilder.loadTexts:cErrDisableFeatureTable.setStatus(_B)
_CErrDisableFeatureEntry_Object=MibTableRow
cErrDisableFeatureEntry=_CErrDisableFeatureEntry_Object((1,3,6,1,4,1,9,9,548,1,2,1,1))
cErrDisableFeatureEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:cErrDisableFeatureEntry.setStatus(_B)
_CErrDisableFeatureIndex_Type=CErrDisableFeatureID
_CErrDisableFeatureIndex_Object=MibTableColumn
cErrDisableFeatureIndex=_CErrDisableFeatureIndex_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,1),_CErrDisableFeatureIndex_Type())
cErrDisableFeatureIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cErrDisableFeatureIndex.setStatus(_B)
class _CErrDisableFeatureConfigurable_Type(Bits):namedValues=NamedValues(*(('detectionEnable',0),('recoveryEnable',1),('recoveryInterval',2),('detectShutdownVlan',3),('flapControl',4)))
_CErrDisableFeatureConfigurable_Type.__name__='Bits'
_CErrDisableFeatureConfigurable_Object=MibTableColumn
cErrDisableFeatureConfigurable=_CErrDisableFeatureConfigurable_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,2),_CErrDisableFeatureConfigurable_Type())
cErrDisableFeatureConfigurable.setMaxAccess(_J)
if mibBuilder.loadTexts:cErrDisableFeatureConfigurable.setStatus(_B)
_CErrDisableFeatureDetectEnable_Type=TruthValue
_CErrDisableFeatureDetectEnable_Object=MibTableColumn
cErrDisableFeatureDetectEnable=_CErrDisableFeatureDetectEnable_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,3),_CErrDisableFeatureDetectEnable_Type())
cErrDisableFeatureDetectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableFeatureDetectEnable.setStatus(_B)
_CErrDisableFeatureRecoveryEnable_Type=TruthValue
_CErrDisableFeatureRecoveryEnable_Object=MibTableColumn
cErrDisableFeatureRecoveryEnable=_CErrDisableFeatureRecoveryEnable_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,4),_CErrDisableFeatureRecoveryEnable_Type())
cErrDisableFeatureRecoveryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableFeatureRecoveryEnable.setStatus(_B)
_CErrDisableFeatureRecoveryInterval_Type=TimeIntervalSec
_CErrDisableFeatureRecoveryInterval_Object=MibTableColumn
cErrDisableFeatureRecoveryInterval=_CErrDisableFeatureRecoveryInterval_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,5),_CErrDisableFeatureRecoveryInterval_Type())
cErrDisableFeatureRecoveryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableFeatureRecoveryInterval.setStatus(_B)
_CErrDisableFeatureDetectShutdownVlan_Type=TruthValue
_CErrDisableFeatureDetectShutdownVlan_Object=MibTableColumn
cErrDisableFeatureDetectShutdownVlan=_CErrDisableFeatureDetectShutdownVlan_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,6),_CErrDisableFeatureDetectShutdownVlan_Type())
cErrDisableFeatureDetectShutdownVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableFeatureDetectShutdownVlan.setStatus(_B)
_CErrDisableFeatureMaxFlapCount_Type=Unsigned32
_CErrDisableFeatureMaxFlapCount_Object=MibTableColumn
cErrDisableFeatureMaxFlapCount=_CErrDisableFeatureMaxFlapCount_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,7),_CErrDisableFeatureMaxFlapCount_Type())
cErrDisableFeatureMaxFlapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableFeatureMaxFlapCount.setStatus(_B)
_CErrDisableFeatureFlapTimePeriod_Type=Unsigned32
_CErrDisableFeatureFlapTimePeriod_Object=MibTableColumn
cErrDisableFeatureFlapTimePeriod=_CErrDisableFeatureFlapTimePeriod_Object((1,3,6,1,4,1,9,9,548,1,2,1,1,8),_CErrDisableFeatureFlapTimePeriod_Type())
cErrDisableFeatureFlapTimePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cErrDisableFeatureFlapTimePeriod.setStatus(_B)
_CErrDisableIfObjects_ObjectIdentity=ObjectIdentity
cErrDisableIfObjects=_CErrDisableIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,548,1,3))
_CErrDisableIfStatusTable_Object=MibTable
cErrDisableIfStatusTable=_CErrDisableIfStatusTable_Object((1,3,6,1,4,1,9,9,548,1,3,1))
if mibBuilder.loadTexts:cErrDisableIfStatusTable.setStatus(_B)
_CErrDisableIfStatusEntry_Object=MibTableRow
cErrDisableIfStatusEntry=_CErrDisableIfStatusEntry_Object((1,3,6,1,4,1,9,9,548,1,3,1,1))
cErrDisableIfStatusEntry.setIndexNames((0,_M,_N),(0,_A,_Q))
if mibBuilder.loadTexts:cErrDisableIfStatusEntry.setStatus(_B)
_CErrDisableIfStatusVlanIndex_Type=VlanIndexOrZero
_CErrDisableIfStatusVlanIndex_Object=MibTableColumn
cErrDisableIfStatusVlanIndex=_CErrDisableIfStatusVlanIndex_Object((1,3,6,1,4,1,9,9,548,1,3,1,1,1),_CErrDisableIfStatusVlanIndex_Type())
cErrDisableIfStatusVlanIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cErrDisableIfStatusVlanIndex.setStatus(_B)
_CErrDisableIfStatusCause_Type=CErrDisableFeatureID
_CErrDisableIfStatusCause_Object=MibTableColumn
cErrDisableIfStatusCause=_CErrDisableIfStatusCause_Object((1,3,6,1,4,1,9,9,548,1,3,1,1,2),_CErrDisableIfStatusCause_Type())
cErrDisableIfStatusCause.setMaxAccess(_J)
if mibBuilder.loadTexts:cErrDisableIfStatusCause.setStatus(_B)
_CErrDisableIfStatusTimeToRecover_Type=TimeIntervalSec
_CErrDisableIfStatusTimeToRecover_Object=MibTableColumn
cErrDisableIfStatusTimeToRecover=_CErrDisableIfStatusTimeToRecover_Object((1,3,6,1,4,1,9,9,548,1,3,1,1,3),_CErrDisableIfStatusTimeToRecover_Type())
cErrDisableIfStatusTimeToRecover.setMaxAccess(_J)
if mibBuilder.loadTexts:cErrDisableIfStatusTimeToRecover.setStatus(_B)
_CiscoErrDisableMIBConform_ObjectIdentity=ObjectIdentity
ciscoErrDisableMIBConform=_CiscoErrDisableMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,548,2))
_CiscoErrDisableMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoErrDisableMIBCompliances=_CiscoErrDisableMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,548,2,1))
_CiscoErrDisableMIBGroups_ObjectIdentity=ObjectIdentity
ciscoErrDisableMIBGroups=_CiscoErrDisableMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,548,2,2))
ciscoErrDisableGlobalCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,548,2,2,1))
ciscoErrDisableGlobalCfgGroup.setObjects((_A,_R))
if mibBuilder.loadTexts:ciscoErrDisableGlobalCfgGroup.setStatus(_B)
ciscoErrDisableFeatureCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,548,2,2,2))
ciscoErrDisableFeatureCfgGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoErrDisableFeatureCfgGroup.setStatus(_B)
ciscoErrDisableIfStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,548,2,2,3))
ciscoErrDisableIfStatusGroup.setObjects(*((_A,_D),(_A,_W)))
if mibBuilder.loadTexts:ciscoErrDisableIfStatusGroup.setStatus(_B)
ciscoErrDisableNotifCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,548,2,2,4))
ciscoErrDisableNotifCfgGroup.setObjects(*((_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoErrDisableNotifCfgGroup.setStatus(_B)
ciscoErrDisableShutdownVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,548,2,2,7))
ciscoErrDisableShutdownVlanGroup.setObjects((_A,_Z))
if mibBuilder.loadTexts:ciscoErrDisableShutdownVlanGroup.setStatus(_B)
ciscoErrDisableFeatureFlapGroup=ObjectGroup((1,3,6,1,4,1,9,9,548,2,2,8))
ciscoErrDisableFeatureFlapGroup.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ciscoErrDisableFeatureFlapGroup.setStatus(_B)
cErrDisableInterfaceEvent=NotificationType((1,3,6,1,4,1,9,9,548,0,1,1))
cErrDisableInterfaceEvent.setObjects((_A,_D))
if mibBuilder.loadTexts:cErrDisableInterfaceEvent.setStatus(_E)
cErrDisableInterfaceEventRev1=NotificationType((1,3,6,1,4,1,9,9,548,0,2))
cErrDisableInterfaceEventRev1.setObjects((_A,_D))
if mibBuilder.loadTexts:cErrDisableInterfaceEventRev1.setStatus(_B)
ciscoErrDisableNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,548,2,2,5))
ciscoErrDisableNotifGroup.setObjects((_A,_c))
if mibBuilder.loadTexts:ciscoErrDisableNotifGroup.setStatus(_E)
ciscoErrDisableNotifGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,548,2,2,6))
ciscoErrDisableNotifGroupRev1.setObjects((_A,_d))
if mibBuilder.loadTexts:ciscoErrDisableNotifGroupRev1.setStatus(_B)
ciscoErrDisableMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,548,2,1,1))
ciscoErrDisableMIBCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_e)))
if mibBuilder.loadTexts:ciscoErrDisableMIBCompliance.setStatus(_E)
ciscoErrDisableMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,548,2,1,2))
ciscoErrDisableMIBComplianceRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoErrDisableMIBComplianceRev1.setStatus(_E)
ciscoErrDisableMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,548,2,1,3))
ciscoErrDisableMIBComplianceRev2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_L),(_A,_f)))
if mibBuilder.loadTexts:ciscoErrDisableMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CErrDisableFeatureID':CErrDisableFeatureID,'ciscoErrDisableMIB':ciscoErrDisableMIB,'ciscoErrDisableMIBNotifs':ciscoErrDisableMIBNotifs,'cErrDisableNotificationsPrefix':cErrDisableNotificationsPrefix,_c:cErrDisableInterfaceEvent,_d:cErrDisableInterfaceEventRev1,'ciscoErrDisableMIBObjects':ciscoErrDisableMIBObjects,'cErrDisableGlobalObjects':cErrDisableGlobalObjects,_R:cErrDisableRecoveryInterval,_X:cErrDisableNotifEnable,_Y:cErrDisableNotifRate,'cErrDisableFeatureObjects':cErrDisableFeatureObjects,'cErrDisableFeatureTable':cErrDisableFeatureTable,'cErrDisableFeatureEntry':cErrDisableFeatureEntry,_O:cErrDisableFeatureIndex,_S:cErrDisableFeatureConfigurable,_T:cErrDisableFeatureDetectEnable,_U:cErrDisableFeatureRecoveryEnable,_V:cErrDisableFeatureRecoveryInterval,_Z:cErrDisableFeatureDetectShutdownVlan,_a:cErrDisableFeatureMaxFlapCount,_b:cErrDisableFeatureFlapTimePeriod,'cErrDisableIfObjects':cErrDisableIfObjects,'cErrDisableIfStatusTable':cErrDisableIfStatusTable,'cErrDisableIfStatusEntry':cErrDisableIfStatusEntry,_Q:cErrDisableIfStatusVlanIndex,_D:cErrDisableIfStatusCause,_W:cErrDisableIfStatusTimeToRecover,'ciscoErrDisableMIBConform':ciscoErrDisableMIBConform,'ciscoErrDisableMIBCompliances':ciscoErrDisableMIBCompliances,'ciscoErrDisableMIBCompliance':ciscoErrDisableMIBCompliance,'ciscoErrDisableMIBComplianceRev1':ciscoErrDisableMIBComplianceRev1,'ciscoErrDisableMIBComplianceRev2':ciscoErrDisableMIBComplianceRev2,'ciscoErrDisableMIBGroups':ciscoErrDisableMIBGroups,_F:ciscoErrDisableGlobalCfgGroup,_G:ciscoErrDisableFeatureCfgGroup,_H:ciscoErrDisableIfStatusGroup,_I:ciscoErrDisableNotifCfgGroup,_e:ciscoErrDisableNotifGroup,_K:ciscoErrDisableNotifGroupRev1,_L:ciscoErrDisableShutdownVlanGroup,_f:ciscoErrDisableFeatureFlapGroup})