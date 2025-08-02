_AO='ciscoRFStatusClientGroup'
_AN='ciscoRFIssuStateObjGroup'
_AM='ciscoRFIssuStateNotifGroup'
_AL='ciscoRFConfigGroup'
_AK='ciscoRFIssuStateNotifRev1'
_AJ='ciscoRFIssuStateNotif'
_AI='ciscoRFProgressionNotif'
_AH='ciscoRFSwactNotif'
_AG='cRFStatusRFClientStatus'
_AF='cRFStatusRFClientRedTime'
_AE='cRFStatusRFClientSeq'
_AD='cRFStatusRFClientDescr'
_AC='cRFStatusRFModeCapsModeDescr'
_AB='cRFCfgRedundancyOperMode'
_AA='cRFHistoryTableMaxLength'
_A9='cRFHistoryStandByAvailTime'
_A8='cRFHistoryColdStarts'
_A7='cRFHistorySwactTime'
_A6='cRFHistorySwitchOverReason'
_A5='cRFHistoryCurrActiveUnitId'
_A4='cRFHistoryPrevActiveUnitId'
_A3='cRFStatusPeerStandByEntryTime'
_A2='cRFStatusFailoverTime'
_A1='cRFCfgMaintenanceMode'
_A0='cRFCfgSplitMode'
_z='cRFStatusRFClientID'
_y='cRFHistorySwitchOverIndex'
_x='cRFStatusRFModeCapsMode'
_w='commitVersion'
_v='runVersion'
_u='loadVersion'
_t='notKnown'
_s='TruthValue'
_r='sysUpTime'
_q='SNMPv2-MIB'
_p='ciscoRFIssuStateObjGroupRev1'
_o='ciscoRFIssuStateNotifGroupRev1'
_n='ciscoRFStatusGroup'
_m='cRFStatusIssuToVersion'
_l='cRFStatusIssuFromVersion'
_k='cRFStatusIssuStateRev1'
_j='cRFStatusIssuState'
_i='cRFCfgRedundancyModeDescr'
_h='cRFCfgRedundancyMode'
_g='cRFCfgNotifsEnabled'
_f='cRFCfgAdminAction'
_e='cRFCfgNotifTimerMax'
_d='cRFCfgNotifTimerMin'
_c='cRFCfgNotifTimer'
_b='cRFCfgKeepaliveTimerMax'
_a='cRFCfgKeepaliveTimerMin'
_Z='cRFCfgKeepaliveTimer'
_Y='cRFCfgKeepaliveThreshMax'
_X='cRFCfgKeepaliveThreshMin'
_W='cRFCfgKeepaliveThresh'
_V='cRFStatusManualSwactInhibit'
_U='cRFStatusDuplexMode'
_T='cRFStatusPrimaryMode'
_S='not-accessible'
_R='ciscoRFStatusRFModeCapsGroup'
_Q='ciscoRFConfigRFOperModeGroup'
_P='cRFStatusPeerUnitState'
_O='cRFStatusPeerUnitId'
_N='Unsigned32'
_M='ciscoRFHistoryGroup'
_L='ciscoRFStatusGroupRev1'
_K='cRFStatusLastSwactReasonCode'
_J='cRFStatusUnitState'
_I='ciscoRFConfigGroupRev1'
_H='cRFStatusUnitId'
_G='ciscoRFNotifGroup'
_F='milliseconds'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-RF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysUpTime,=mibBuilder.importSymbols(_q,_r)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeInterval','TimeStamp',_s)
ciscoRFMIB=ModuleIdentity((1,3,6,1,4,1,9,9,176))
if mibBuilder.loadTexts:ciscoRFMIB.setRevisions(('2023-07-13 00:00','2005-09-01 00:00','2004-04-01 00:00','2004-02-04 00:00','2003-10-02 00:00','2002-01-07 00:00','2001-07-20 00:00','2001-06-26 00:00','2001-04-03 09:45'))
class RFState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_t,1),('disabled',2),('initialization',3),('negotiation',4),('standbyCold',5),('standbyColdConfig',6),('standbyColdFileSys',7),('standbyColdBulk',8),('standbyHot',9),('activeFast',10),('activeDrain',11),('activePreconfig',12),('activePostconfig',13),('active',14),('activeExtraload',15),('activeHandback',16),('standbyWarm',17)))
class RFMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nonRedundant',1),('staticLoadShareNonRedundant',2),('dynamicLoadShareNonRedundant',3),('staticLoadShareRedundant',4),('dynamicLoadShareRedundant',5),('coldStandbyRedundant',6),('warmStandbyRedundant',7),('hotStandbyRedundant',8)))
class RFAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noAction',0),('reloadPeer',1),('reloadShelf',2),('switchActivity',3),('forceSwitchActivity',4)))
class RFSwactReasonType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unsupported',1),('none',2),(_t,3),('userInitiated',4),('userForced',5),('activeUnitFailed',6),('activeUnitRemoved',7),('activeGWdown',8),('activeRMIportdown',9)))
class RFUnitIdentifier(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class RFIssuState(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unset',0),('init',1),(_u,2),(_v,3),(_w,4)))
class RFIssuStateRev1(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4,6,7,9)));namedValues=NamedValues(*(('init',0),('systemReset',1),(_u,3),('loadVersionSwitchover',4),(_v,6),('runVersionSwitchover',7),(_w,9)))
class RFClientStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noStatus',1),('clientNotRedundant',2),('clientRedundancyInProgress',3),('clientRedundant',4)))
_CiscoRFMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRFMIBObjects=_CiscoRFMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,176,1))
_CRFStatus_ObjectIdentity=ObjectIdentity
cRFStatus=_CRFStatus_ObjectIdentity((1,3,6,1,4,1,9,9,176,1,1))
_CRFStatusUnitId_Type=RFUnitIdentifier
_CRFStatusUnitId_Object=MibScalar
cRFStatusUnitId=_CRFStatusUnitId_Object((1,3,6,1,4,1,9,9,176,1,1,1),_CRFStatusUnitId_Type())
cRFStatusUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusUnitId.setStatus(_B)
_CRFStatusUnitState_Type=RFState
_CRFStatusUnitState_Object=MibScalar
cRFStatusUnitState=_CRFStatusUnitState_Object((1,3,6,1,4,1,9,9,176,1,1,2),_CRFStatusUnitState_Type())
cRFStatusUnitState.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusUnitState.setStatus(_B)
_CRFStatusPeerUnitId_Type=RFUnitIdentifier
_CRFStatusPeerUnitId_Object=MibScalar
cRFStatusPeerUnitId=_CRFStatusPeerUnitId_Object((1,3,6,1,4,1,9,9,176,1,1,3),_CRFStatusPeerUnitId_Type())
cRFStatusPeerUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusPeerUnitId.setStatus(_B)
_CRFStatusPeerUnitState_Type=RFState
_CRFStatusPeerUnitState_Object=MibScalar
cRFStatusPeerUnitState=_CRFStatusPeerUnitState_Object((1,3,6,1,4,1,9,9,176,1,1,4),_CRFStatusPeerUnitState_Type())
cRFStatusPeerUnitState.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusPeerUnitState.setStatus(_B)
_CRFStatusPrimaryMode_Type=TruthValue
_CRFStatusPrimaryMode_Object=MibScalar
cRFStatusPrimaryMode=_CRFStatusPrimaryMode_Object((1,3,6,1,4,1,9,9,176,1,1,5),_CRFStatusPrimaryMode_Type())
cRFStatusPrimaryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusPrimaryMode.setStatus(_B)
_CRFStatusDuplexMode_Type=TruthValue
_CRFStatusDuplexMode_Object=MibScalar
cRFStatusDuplexMode=_CRFStatusDuplexMode_Object((1,3,6,1,4,1,9,9,176,1,1,6),_CRFStatusDuplexMode_Type())
cRFStatusDuplexMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusDuplexMode.setStatus(_B)
_CRFStatusManualSwactInhibit_Type=TruthValue
_CRFStatusManualSwactInhibit_Object=MibScalar
cRFStatusManualSwactInhibit=_CRFStatusManualSwactInhibit_Object((1,3,6,1,4,1,9,9,176,1,1,7),_CRFStatusManualSwactInhibit_Type())
cRFStatusManualSwactInhibit.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusManualSwactInhibit.setStatus(_B)
_CRFStatusLastSwactReasonCode_Type=RFSwactReasonType
_CRFStatusLastSwactReasonCode_Object=MibScalar
cRFStatusLastSwactReasonCode=_CRFStatusLastSwactReasonCode_Object((1,3,6,1,4,1,9,9,176,1,1,8),_CRFStatusLastSwactReasonCode_Type())
cRFStatusLastSwactReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusLastSwactReasonCode.setStatus(_B)
_CRFStatusFailoverTime_Type=TimeStamp
_CRFStatusFailoverTime_Object=MibScalar
cRFStatusFailoverTime=_CRFStatusFailoverTime_Object((1,3,6,1,4,1,9,9,176,1,1,9),_CRFStatusFailoverTime_Type())
cRFStatusFailoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusFailoverTime.setStatus(_B)
_CRFStatusPeerStandByEntryTime_Type=TimeStamp
_CRFStatusPeerStandByEntryTime_Object=MibScalar
cRFStatusPeerStandByEntryTime=_CRFStatusPeerStandByEntryTime_Object((1,3,6,1,4,1,9,9,176,1,1,10),_CRFStatusPeerStandByEntryTime_Type())
cRFStatusPeerStandByEntryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusPeerStandByEntryTime.setStatus(_B)
_CRFStatusRFModeCapsTable_Object=MibTable
cRFStatusRFModeCapsTable=_CRFStatusRFModeCapsTable_Object((1,3,6,1,4,1,9,9,176,1,1,11))
if mibBuilder.loadTexts:cRFStatusRFModeCapsTable.setStatus(_B)
_CRFStatusRFModeCapsEntry_Object=MibTableRow
cRFStatusRFModeCapsEntry=_CRFStatusRFModeCapsEntry_Object((1,3,6,1,4,1,9,9,176,1,1,11,1))
cRFStatusRFModeCapsEntry.setIndexNames((0,_A,_x))
if mibBuilder.loadTexts:cRFStatusRFModeCapsEntry.setStatus(_B)
_CRFStatusRFModeCapsMode_Type=RFMode
_CRFStatusRFModeCapsMode_Object=MibTableColumn
cRFStatusRFModeCapsMode=_CRFStatusRFModeCapsMode_Object((1,3,6,1,4,1,9,9,176,1,1,11,1,1),_CRFStatusRFModeCapsMode_Type())
cRFStatusRFModeCapsMode.setMaxAccess(_S)
if mibBuilder.loadTexts:cRFStatusRFModeCapsMode.setStatus(_B)
_CRFStatusRFModeCapsModeDescr_Type=SnmpAdminString
_CRFStatusRFModeCapsModeDescr_Object=MibTableColumn
cRFStatusRFModeCapsModeDescr=_CRFStatusRFModeCapsModeDescr_Object((1,3,6,1,4,1,9,9,176,1,1,11,1,2),_CRFStatusRFModeCapsModeDescr_Type())
cRFStatusRFModeCapsModeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusRFModeCapsModeDescr.setStatus(_B)
_CRFStatusIssuState_Type=RFIssuState
_CRFStatusIssuState_Object=MibScalar
cRFStatusIssuState=_CRFStatusIssuState_Object((1,3,6,1,4,1,9,9,176,1,1,12),_CRFStatusIssuState_Type())
cRFStatusIssuState.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusIssuState.setStatus(_D)
_CRFStatusIssuStateRev1_Type=RFIssuStateRev1
_CRFStatusIssuStateRev1_Object=MibScalar
cRFStatusIssuStateRev1=_CRFStatusIssuStateRev1_Object((1,3,6,1,4,1,9,9,176,1,1,13),_CRFStatusIssuStateRev1_Type())
cRFStatusIssuStateRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusIssuStateRev1.setStatus(_B)
_CRFStatusIssuFromVersion_Type=SnmpAdminString
_CRFStatusIssuFromVersion_Object=MibScalar
cRFStatusIssuFromVersion=_CRFStatusIssuFromVersion_Object((1,3,6,1,4,1,9,9,176,1,1,14),_CRFStatusIssuFromVersion_Type())
cRFStatusIssuFromVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusIssuFromVersion.setStatus(_B)
_CRFStatusIssuToVersion_Type=SnmpAdminString
_CRFStatusIssuToVersion_Object=MibScalar
cRFStatusIssuToVersion=_CRFStatusIssuToVersion_Object((1,3,6,1,4,1,9,9,176,1,1,15),_CRFStatusIssuToVersion_Type())
cRFStatusIssuToVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusIssuToVersion.setStatus(_B)
_CRFCfg_ObjectIdentity=ObjectIdentity
cRFCfg=_CRFCfg_ObjectIdentity((1,3,6,1,4,1,9,9,176,1,2))
_CRFCfgSplitMode_Type=TruthValue
_CRFCfgSplitMode_Object=MibScalar
cRFCfgSplitMode=_CRFCfgSplitMode_Object((1,3,6,1,4,1,9,9,176,1,2,1),_CRFCfgSplitMode_Type())
cRFCfgSplitMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgSplitMode.setStatus(_D)
_CRFCfgKeepaliveThresh_Type=Unsigned32
_CRFCfgKeepaliveThresh_Object=MibScalar
cRFCfgKeepaliveThresh=_CRFCfgKeepaliveThresh_Object((1,3,6,1,4,1,9,9,176,1,2,2),_CRFCfgKeepaliveThresh_Type())
cRFCfgKeepaliveThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgKeepaliveThresh.setStatus(_B)
_CRFCfgKeepaliveThreshMin_Type=Unsigned32
_CRFCfgKeepaliveThreshMin_Object=MibScalar
cRFCfgKeepaliveThreshMin=_CRFCfgKeepaliveThreshMin_Object((1,3,6,1,4,1,9,9,176,1,2,3),_CRFCfgKeepaliveThreshMin_Type())
cRFCfgKeepaliveThreshMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgKeepaliveThreshMin.setStatus(_B)
_CRFCfgKeepaliveThreshMax_Type=Unsigned32
_CRFCfgKeepaliveThreshMax_Object=MibScalar
cRFCfgKeepaliveThreshMax=_CRFCfgKeepaliveThreshMax_Object((1,3,6,1,4,1,9,9,176,1,2,4),_CRFCfgKeepaliveThreshMax_Type())
cRFCfgKeepaliveThreshMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgKeepaliveThreshMax.setStatus(_B)
_CRFCfgKeepaliveTimer_Type=Unsigned32
_CRFCfgKeepaliveTimer_Object=MibScalar
cRFCfgKeepaliveTimer=_CRFCfgKeepaliveTimer_Object((1,3,6,1,4,1,9,9,176,1,2,5),_CRFCfgKeepaliveTimer_Type())
cRFCfgKeepaliveTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgKeepaliveTimer.setStatus(_B)
if mibBuilder.loadTexts:cRFCfgKeepaliveTimer.setUnits(_F)
_CRFCfgKeepaliveTimerMin_Type=Unsigned32
_CRFCfgKeepaliveTimerMin_Object=MibScalar
cRFCfgKeepaliveTimerMin=_CRFCfgKeepaliveTimerMin_Object((1,3,6,1,4,1,9,9,176,1,2,6),_CRFCfgKeepaliveTimerMin_Type())
cRFCfgKeepaliveTimerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgKeepaliveTimerMin.setStatus(_B)
if mibBuilder.loadTexts:cRFCfgKeepaliveTimerMin.setUnits(_F)
_CRFCfgKeepaliveTimerMax_Type=Unsigned32
_CRFCfgKeepaliveTimerMax_Object=MibScalar
cRFCfgKeepaliveTimerMax=_CRFCfgKeepaliveTimerMax_Object((1,3,6,1,4,1,9,9,176,1,2,7),_CRFCfgKeepaliveTimerMax_Type())
cRFCfgKeepaliveTimerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgKeepaliveTimerMax.setStatus(_B)
if mibBuilder.loadTexts:cRFCfgKeepaliveTimerMax.setUnits(_F)
_CRFCfgNotifTimer_Type=Unsigned32
_CRFCfgNotifTimer_Object=MibScalar
cRFCfgNotifTimer=_CRFCfgNotifTimer_Object((1,3,6,1,4,1,9,9,176,1,2,8),_CRFCfgNotifTimer_Type())
cRFCfgNotifTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgNotifTimer.setStatus(_B)
if mibBuilder.loadTexts:cRFCfgNotifTimer.setUnits(_F)
_CRFCfgNotifTimerMin_Type=Unsigned32
_CRFCfgNotifTimerMin_Object=MibScalar
cRFCfgNotifTimerMin=_CRFCfgNotifTimerMin_Object((1,3,6,1,4,1,9,9,176,1,2,9),_CRFCfgNotifTimerMin_Type())
cRFCfgNotifTimerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgNotifTimerMin.setStatus(_B)
if mibBuilder.loadTexts:cRFCfgNotifTimerMin.setUnits(_F)
_CRFCfgNotifTimerMax_Type=Unsigned32
_CRFCfgNotifTimerMax_Object=MibScalar
cRFCfgNotifTimerMax=_CRFCfgNotifTimerMax_Object((1,3,6,1,4,1,9,9,176,1,2,10),_CRFCfgNotifTimerMax_Type())
cRFCfgNotifTimerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgNotifTimerMax.setStatus(_B)
if mibBuilder.loadTexts:cRFCfgNotifTimerMax.setUnits(_F)
_CRFCfgAdminAction_Type=RFAction
_CRFCfgAdminAction_Object=MibScalar
cRFCfgAdminAction=_CRFCfgAdminAction_Object((1,3,6,1,4,1,9,9,176,1,2,11),_CRFCfgAdminAction_Type())
cRFCfgAdminAction.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgAdminAction.setStatus(_B)
class _CRFCfgNotifsEnabled_Type(TruthValue):defaultValue=2
_CRFCfgNotifsEnabled_Type.__name__=_s
_CRFCfgNotifsEnabled_Object=MibScalar
cRFCfgNotifsEnabled=_CRFCfgNotifsEnabled_Object((1,3,6,1,4,1,9,9,176,1,2,12),_CRFCfgNotifsEnabled_Type())
cRFCfgNotifsEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgNotifsEnabled.setStatus(_B)
_CRFCfgMaintenanceMode_Type=TruthValue
_CRFCfgMaintenanceMode_Object=MibScalar
cRFCfgMaintenanceMode=_CRFCfgMaintenanceMode_Object((1,3,6,1,4,1,9,9,176,1,2,13),_CRFCfgMaintenanceMode_Type())
cRFCfgMaintenanceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgMaintenanceMode.setStatus(_B)
_CRFCfgRedundancyMode_Type=RFMode
_CRFCfgRedundancyMode_Object=MibScalar
cRFCfgRedundancyMode=_CRFCfgRedundancyMode_Object((1,3,6,1,4,1,9,9,176,1,2,14),_CRFCfgRedundancyMode_Type())
cRFCfgRedundancyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFCfgRedundancyMode.setStatus(_B)
_CRFCfgRedundancyModeDescr_Type=SnmpAdminString
_CRFCfgRedundancyModeDescr_Object=MibScalar
cRFCfgRedundancyModeDescr=_CRFCfgRedundancyModeDescr_Object((1,3,6,1,4,1,9,9,176,1,2,15),_CRFCfgRedundancyModeDescr_Type())
cRFCfgRedundancyModeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgRedundancyModeDescr.setStatus(_B)
_CRFCfgRedundancyOperMode_Type=RFMode
_CRFCfgRedundancyOperMode_Object=MibScalar
cRFCfgRedundancyOperMode=_CRFCfgRedundancyOperMode_Object((1,3,6,1,4,1,9,9,176,1,2,16),_CRFCfgRedundancyOperMode_Type())
cRFCfgRedundancyOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFCfgRedundancyOperMode.setStatus(_B)
_CRFHistory_ObjectIdentity=ObjectIdentity
cRFHistory=_CRFHistory_ObjectIdentity((1,3,6,1,4,1,9,9,176,1,3))
class _CRFHistoryTableMaxLength_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_CRFHistoryTableMaxLength_Type.__name__=_N
_CRFHistoryTableMaxLength_Object=MibScalar
cRFHistoryTableMaxLength=_CRFHistoryTableMaxLength_Object((1,3,6,1,4,1,9,9,176,1,3,1),_CRFHistoryTableMaxLength_Type())
cRFHistoryTableMaxLength.setMaxAccess(_E)
if mibBuilder.loadTexts:cRFHistoryTableMaxLength.setStatus(_B)
_CRFHistorySwitchOverTable_Object=MibTable
cRFHistorySwitchOverTable=_CRFHistorySwitchOverTable_Object((1,3,6,1,4,1,9,9,176,1,3,2))
if mibBuilder.loadTexts:cRFHistorySwitchOverTable.setStatus(_B)
_CRFHistorySwitchOverEntry_Object=MibTableRow
cRFHistorySwitchOverEntry=_CRFHistorySwitchOverEntry_Object((1,3,6,1,4,1,9,9,176,1,3,2,1))
cRFHistorySwitchOverEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:cRFHistorySwitchOverEntry.setStatus(_B)
class _CRFHistorySwitchOverIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CRFHistorySwitchOverIndex_Type.__name__=_N
_CRFHistorySwitchOverIndex_Object=MibTableColumn
cRFHistorySwitchOverIndex=_CRFHistorySwitchOverIndex_Object((1,3,6,1,4,1,9,9,176,1,3,2,1,1),_CRFHistorySwitchOverIndex_Type())
cRFHistorySwitchOverIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cRFHistorySwitchOverIndex.setStatus(_B)
_CRFHistoryPrevActiveUnitId_Type=RFUnitIdentifier
_CRFHistoryPrevActiveUnitId_Object=MibTableColumn
cRFHistoryPrevActiveUnitId=_CRFHistoryPrevActiveUnitId_Object((1,3,6,1,4,1,9,9,176,1,3,2,1,2),_CRFHistoryPrevActiveUnitId_Type())
cRFHistoryPrevActiveUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFHistoryPrevActiveUnitId.setStatus(_B)
_CRFHistoryCurrActiveUnitId_Type=RFUnitIdentifier
_CRFHistoryCurrActiveUnitId_Object=MibTableColumn
cRFHistoryCurrActiveUnitId=_CRFHistoryCurrActiveUnitId_Object((1,3,6,1,4,1,9,9,176,1,3,2,1,3),_CRFHistoryCurrActiveUnitId_Type())
cRFHistoryCurrActiveUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFHistoryCurrActiveUnitId.setStatus(_B)
_CRFHistorySwitchOverReason_Type=RFSwactReasonType
_CRFHistorySwitchOverReason_Object=MibTableColumn
cRFHistorySwitchOverReason=_CRFHistorySwitchOverReason_Object((1,3,6,1,4,1,9,9,176,1,3,2,1,4),_CRFHistorySwitchOverReason_Type())
cRFHistorySwitchOverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFHistorySwitchOverReason.setStatus(_B)
_CRFHistorySwactTime_Type=DateAndTime
_CRFHistorySwactTime_Object=MibTableColumn
cRFHistorySwactTime=_CRFHistorySwactTime_Object((1,3,6,1,4,1,9,9,176,1,3,2,1,5),_CRFHistorySwactTime_Type())
cRFHistorySwactTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFHistorySwactTime.setStatus(_B)
_CRFHistoryColdStarts_Type=Counter32
_CRFHistoryColdStarts_Object=MibScalar
cRFHistoryColdStarts=_CRFHistoryColdStarts_Object((1,3,6,1,4,1,9,9,176,1,3,3),_CRFHistoryColdStarts_Type())
cRFHistoryColdStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFHistoryColdStarts.setStatus(_B)
_CRFHistoryStandByAvailTime_Type=TimeInterval
_CRFHistoryStandByAvailTime_Object=MibScalar
cRFHistoryStandByAvailTime=_CRFHistoryStandByAvailTime_Object((1,3,6,1,4,1,9,9,176,1,3,4),_CRFHistoryStandByAvailTime_Type())
cRFHistoryStandByAvailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFHistoryStandByAvailTime.setStatus(_B)
_CRFClient_ObjectIdentity=ObjectIdentity
cRFClient=_CRFClient_ObjectIdentity((1,3,6,1,4,1,9,9,176,1,4))
_CRFStatusRFClientTable_Object=MibTable
cRFStatusRFClientTable=_CRFStatusRFClientTable_Object((1,3,6,1,4,1,9,9,176,1,4,1))
if mibBuilder.loadTexts:cRFStatusRFClientTable.setStatus(_B)
_CRFStatusRFClientEntry_Object=MibTableRow
cRFStatusRFClientEntry=_CRFStatusRFClientEntry_Object((1,3,6,1,4,1,9,9,176,1,4,1,1))
cRFStatusRFClientEntry.setIndexNames((0,_A,_z))
if mibBuilder.loadTexts:cRFStatusRFClientEntry.setStatus(_B)
class _CRFStatusRFClientID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CRFStatusRFClientID_Type.__name__=_N
_CRFStatusRFClientID_Object=MibTableColumn
cRFStatusRFClientID=_CRFStatusRFClientID_Object((1,3,6,1,4,1,9,9,176,1,4,1,1,1),_CRFStatusRFClientID_Type())
cRFStatusRFClientID.setMaxAccess(_S)
if mibBuilder.loadTexts:cRFStatusRFClientID.setStatus(_B)
_CRFStatusRFClientDescr_Type=SnmpAdminString
_CRFStatusRFClientDescr_Object=MibTableColumn
cRFStatusRFClientDescr=_CRFStatusRFClientDescr_Object((1,3,6,1,4,1,9,9,176,1,4,1,1,2),_CRFStatusRFClientDescr_Type())
cRFStatusRFClientDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusRFClientDescr.setStatus(_B)
_CRFStatusRFClientSeq_Type=Unsigned32
_CRFStatusRFClientSeq_Object=MibTableColumn
cRFStatusRFClientSeq=_CRFStatusRFClientSeq_Object((1,3,6,1,4,1,9,9,176,1,4,1,1,3),_CRFStatusRFClientSeq_Type())
cRFStatusRFClientSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusRFClientSeq.setStatus(_B)
_CRFStatusRFClientRedTime_Type=Unsigned32
_CRFStatusRFClientRedTime_Object=MibTableColumn
cRFStatusRFClientRedTime=_CRFStatusRFClientRedTime_Object((1,3,6,1,4,1,9,9,176,1,4,1,1,4),_CRFStatusRFClientRedTime_Type())
cRFStatusRFClientRedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusRFClientRedTime.setStatus(_B)
if mibBuilder.loadTexts:cRFStatusRFClientRedTime.setUnits(_F)
_CRFStatusRFClientStatus_Type=RFClientStatus
_CRFStatusRFClientStatus_Object=MibTableColumn
cRFStatusRFClientStatus=_CRFStatusRFClientStatus_Object((1,3,6,1,4,1,9,9,176,1,4,1,1,5),_CRFStatusRFClientStatus_Type())
cRFStatusRFClientStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cRFStatusRFClientStatus.setStatus(_B)
_CiscoRFMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoRFMIBNotificationsPrefix=_CiscoRFMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,176,2))
_CiscoRFMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoRFMIBNotifications=_CiscoRFMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,176,2,0))
_CiscoRFMIBConformance_ObjectIdentity=ObjectIdentity
ciscoRFMIBConformance=_CiscoRFMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,176,3))
_CiscoRFMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoRFMIBCompliances=_CiscoRFMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,176,3,1))
_CiscoRFMIBGroups_ObjectIdentity=ObjectIdentity
ciscoRFMIBGroups=_CiscoRFMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,176,3,2))
ciscoRFStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,1))
ciscoRFStatusGroup.setObjects(*((_A,_H),(_A,_J),(_A,_O),(_A,_P),(_A,_T),(_A,_U),(_A,_V),(_A,_K)))
if mibBuilder.loadTexts:ciscoRFStatusGroup.setStatus(_D)
ciscoRFConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,2))
ciscoRFConfigGroup.setObjects(*((_A,_A0),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoRFConfigGroup.setStatus(_D)
ciscoRFConfigGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,4))
ciscoRFConfigGroupRev1.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_A1),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoRFConfigGroupRev1.setStatus(_B)
ciscoRFStatusGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,5))
ciscoRFStatusGroupRev1.setObjects(*((_A,_H),(_A,_J),(_A,_O),(_A,_P),(_A,_T),(_A,_U),(_A,_V),(_A,_K),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoRFStatusGroupRev1.setStatus(_B)
ciscoRFHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,6))
ciscoRFHistoryGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoRFHistoryGroup.setStatus(_B)
ciscoRFConfigRFOperModeGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,7))
ciscoRFConfigRFOperModeGroup.setObjects((_A,_AB))
if mibBuilder.loadTexts:ciscoRFConfigRFOperModeGroup.setStatus(_B)
ciscoRFStatusRFModeCapsGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,8))
ciscoRFStatusRFModeCapsGroup.setObjects((_A,_AC))
if mibBuilder.loadTexts:ciscoRFStatusRFModeCapsGroup.setStatus(_B)
ciscoRFIssuStateObjGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,11))
ciscoRFIssuStateObjGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:ciscoRFIssuStateObjGroup.setStatus(_D)
ciscoRFIssuStateObjGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,12))
ciscoRFIssuStateObjGroupRev1.setObjects(*((_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ciscoRFIssuStateObjGroupRev1.setStatus(_B)
ciscoRFStatusClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,176,3,2,13))
ciscoRFStatusClientGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:ciscoRFStatusClientGroup.setStatus(_B)
ciscoRFSwactNotif=NotificationType((1,3,6,1,4,1,9,9,176,2,0,1))
ciscoRFSwactNotif.setObjects(*((_A,_H),(_q,_r),(_A,_K)))
if mibBuilder.loadTexts:ciscoRFSwactNotif.setStatus(_B)
ciscoRFProgressionNotif=NotificationType((1,3,6,1,4,1,9,9,176,2,0,2))
ciscoRFProgressionNotif.setObjects(*((_A,_H),(_A,_J),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoRFProgressionNotif.setStatus(_B)
ciscoRFIssuStateNotif=NotificationType((1,3,6,1,4,1,9,9,176,2,0,3))
ciscoRFIssuStateNotif.setObjects(*((_A,_H),(_A,_J),(_A,_j)))
if mibBuilder.loadTexts:ciscoRFIssuStateNotif.setStatus(_D)
ciscoRFIssuStateNotifRev1=NotificationType((1,3,6,1,4,1,9,9,176,2,0,4))
ciscoRFIssuStateNotifRev1.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_K)))
if mibBuilder.loadTexts:ciscoRFIssuStateNotifRev1.setStatus(_B)
ciscoRFNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,176,3,2,3))
ciscoRFNotifGroup.setObjects(*((_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ciscoRFNotifGroup.setStatus(_B)
ciscoRFIssuStateNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,176,3,2,9))
ciscoRFIssuStateNotifGroup.setObjects((_A,_AJ))
if mibBuilder.loadTexts:ciscoRFIssuStateNotifGroup.setStatus(_D)
ciscoRFIssuStateNotifGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,176,3,2,10))
ciscoRFIssuStateNotifGroupRev1.setObjects((_A,_AK))
if mibBuilder.loadTexts:ciscoRFIssuStateNotifGroupRev1.setStatus(_B)
ciscoRFMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,176,3,1,1))
ciscoRFMIBCompliance.setObjects(*((_A,_n),(_A,_AL),(_A,_G)))
if mibBuilder.loadTexts:ciscoRFMIBCompliance.setStatus(_D)
ciscoRFMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,176,3,1,2))
ciscoRFMIBComplianceRev1.setObjects(*((_A,_n),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:ciscoRFMIBComplianceRev1.setStatus(_D)
ciscoRFMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,176,3,1,3))
ciscoRFMIBComplianceRev2.setObjects(*((_A,_L),(_A,_I),(_A,_G),(_A,_M)))
if mibBuilder.loadTexts:ciscoRFMIBComplianceRev2.setStatus(_D)
ciscoRFMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,176,3,1,4))
ciscoRFMIBComplianceRev3.setObjects(*((_A,_L),(_A,_I),(_A,_G),(_A,_M),(_A,_Q),(_A,_R),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:ciscoRFMIBComplianceRev3.setStatus(_D)
ciscoRFMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,176,3,1,5))
ciscoRFMIBComplianceRev4.setObjects(*((_A,_L),(_A,_I),(_A,_G),(_A,_M),(_A,_Q),(_A,_R),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ciscoRFMIBComplianceRev4.setStatus(_D)
ciscoRFMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,176,3,1,6))
ciscoRFMIBComplianceRev5.setObjects(*((_A,_L),(_A,_I),(_A,_G),(_A,_M),(_A,_Q),(_A,_R),(_A,_o),(_A,_p),(_A,_AO)))
if mibBuilder.loadTexts:ciscoRFMIBComplianceRev5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RFState':RFState,'RFMode':RFMode,'RFAction':RFAction,'RFSwactReasonType':RFSwactReasonType,'RFUnitIdentifier':RFUnitIdentifier,'RFIssuState':RFIssuState,'RFIssuStateRev1':RFIssuStateRev1,'RFClientStatus':RFClientStatus,'ciscoRFMIB':ciscoRFMIB,'ciscoRFMIBObjects':ciscoRFMIBObjects,'cRFStatus':cRFStatus,_H:cRFStatusUnitId,_J:cRFStatusUnitState,_O:cRFStatusPeerUnitId,_P:cRFStatusPeerUnitState,_T:cRFStatusPrimaryMode,_U:cRFStatusDuplexMode,_V:cRFStatusManualSwactInhibit,_K:cRFStatusLastSwactReasonCode,_A2:cRFStatusFailoverTime,_A3:cRFStatusPeerStandByEntryTime,'cRFStatusRFModeCapsTable':cRFStatusRFModeCapsTable,'cRFStatusRFModeCapsEntry':cRFStatusRFModeCapsEntry,_x:cRFStatusRFModeCapsMode,_AC:cRFStatusRFModeCapsModeDescr,_j:cRFStatusIssuState,_k:cRFStatusIssuStateRev1,_l:cRFStatusIssuFromVersion,_m:cRFStatusIssuToVersion,'cRFCfg':cRFCfg,_A0:cRFCfgSplitMode,_W:cRFCfgKeepaliveThresh,_X:cRFCfgKeepaliveThreshMin,_Y:cRFCfgKeepaliveThreshMax,_Z:cRFCfgKeepaliveTimer,_a:cRFCfgKeepaliveTimerMin,_b:cRFCfgKeepaliveTimerMax,_c:cRFCfgNotifTimer,_d:cRFCfgNotifTimerMin,_e:cRFCfgNotifTimerMax,_f:cRFCfgAdminAction,_g:cRFCfgNotifsEnabled,_A1:cRFCfgMaintenanceMode,_h:cRFCfgRedundancyMode,_i:cRFCfgRedundancyModeDescr,_AB:cRFCfgRedundancyOperMode,'cRFHistory':cRFHistory,_AA:cRFHistoryTableMaxLength,'cRFHistorySwitchOverTable':cRFHistorySwitchOverTable,'cRFHistorySwitchOverEntry':cRFHistorySwitchOverEntry,_y:cRFHistorySwitchOverIndex,_A4:cRFHistoryPrevActiveUnitId,_A5:cRFHistoryCurrActiveUnitId,_A6:cRFHistorySwitchOverReason,_A7:cRFHistorySwactTime,_A8:cRFHistoryColdStarts,_A9:cRFHistoryStandByAvailTime,'cRFClient':cRFClient,'cRFStatusRFClientTable':cRFStatusRFClientTable,'cRFStatusRFClientEntry':cRFStatusRFClientEntry,_z:cRFStatusRFClientID,_AD:cRFStatusRFClientDescr,_AE:cRFStatusRFClientSeq,_AF:cRFStatusRFClientRedTime,_AG:cRFStatusRFClientStatus,'ciscoRFMIBNotificationsPrefix':ciscoRFMIBNotificationsPrefix,'ciscoRFMIBNotifications':ciscoRFMIBNotifications,_AH:ciscoRFSwactNotif,_AI:ciscoRFProgressionNotif,_AJ:ciscoRFIssuStateNotif,_AK:ciscoRFIssuStateNotifRev1,'ciscoRFMIBConformance':ciscoRFMIBConformance,'ciscoRFMIBCompliances':ciscoRFMIBCompliances,'ciscoRFMIBCompliance':ciscoRFMIBCompliance,'ciscoRFMIBComplianceRev1':ciscoRFMIBComplianceRev1,'ciscoRFMIBComplianceRev2':ciscoRFMIBComplianceRev2,'ciscoRFMIBComplianceRev3':ciscoRFMIBComplianceRev3,'ciscoRFMIBComplianceRev4':ciscoRFMIBComplianceRev4,'ciscoRFMIBComplianceRev5':ciscoRFMIBComplianceRev5,'ciscoRFMIBGroups':ciscoRFMIBGroups,_n:ciscoRFStatusGroup,_AL:ciscoRFConfigGroup,_G:ciscoRFNotifGroup,_I:ciscoRFConfigGroupRev1,_L:ciscoRFStatusGroupRev1,_M:ciscoRFHistoryGroup,_Q:ciscoRFConfigRFOperModeGroup,_R:ciscoRFStatusRFModeCapsGroup,_AM:ciscoRFIssuStateNotifGroup,_o:ciscoRFIssuStateNotifGroupRev1,_AN:ciscoRFIssuStateObjGroup,_p:ciscoRFIssuStateObjGroupRev1,_AO:ciscoRFStatusClientGroup})