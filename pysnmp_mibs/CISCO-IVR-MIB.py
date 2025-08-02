_BF='civrNotificationGroupRev2'
_BE='civrZoneConfigurationGroupRev2'
_BD='civrTopologyGroupRev2'
_BC='civrGenericGroup'
_BB='deprecated'
_BA='civrAfidConfigNotify'
_B9='civrDomainConflictNotify'
_B8='civrZoneDeactivationDoneNotify'
_B7='civrZoneActivationDoneNotify'
_B6='civrZoneTableNextIndex'
_B5='civrZoneSetTableNextIndex'
_B4='civrZoneEnforcedZoneMemberLunID'
_B3='civrZoneMemberLunID'
_B2='civrZoneEnforcedZoneQosPriority'
_B1='civrZoneEnforcedZoneReadOnly'
_B0='civrZoneQosPriority'
_A_='civrZoneReadOnly'
_Az='civrTopologyClearAfidConfig'
_Ay='civrTopologyDefaultAfidChecksum'
_Ax='civrTopologyAfidConfigChecksum'
_Aw='civrTopologyIvrSrvGrpRowStatus'
_Av='civrTopologyIvrSrvGrpVsan4k'
_Au='civrTopologyIvrSrvGrpVsan2k'
_At='civrTopologyDefaultAfidStatus'
_As='civrTopologyDefaultAfidId'
_Ar='civrTopologyAfidConfRowStatus'
_Aq='civrTopologyAfidConfSwitchVsan4k'
_Ap='civrTopologyAfidConfSwitchVsan2k'
_Ao='civrVsanTopologyAutoDisc'
_An='civrFcidNatMode'
_Am='civrAddIvrVirtualDomainsVsans4k'
_Al='civrAddIvrVirtualDomainsVsans2k'
_Ak='civrEnabledDeviceCapability'
_Aj='civrEnabledDeviceSwitchWwn'
_Ai='civrZoneSetStatus'
_Ah='civrTopologyActive'
_Ag='civrTopologyClearConfigured'
_Af='civrTopologyCopyActiveToConfig'
_Ae='civrTopologyActivateTime'
_Ad='civrTopologyActivate'
_Ac='civrTopologyActiveChecksum'
_Ab='civrTopologyConfiguredChecksum'
_Aa='civrTopologyActiveSwitchVsan4k'
_AZ='civrTopologyActiveSwitchVsan2k'
_AY='civrTopologyConfigRowStatus'
_AX='civrTopologyConfigSwitchVsan4k'
_AW='civrTopologyConfigSwitchVsan2k'
_AV='civrZonesetActivateForce'
_AU='civrZoneClearFullZoneDb'
_AT='civrZoneCopyZoneSetEnforcdToFull'
_AS='civrZoneEnforcedZoneMemberAFId'
_AR='civrZoneEnforcedZoneMemberType'
_AQ='civrZoneEnforcedZoneMemberNumber'
_AP='civrZoneEnforcedZoneMemberList'
_AO='civrZoneEnforcedZoneName'
_AN='civrZoneEnforcedZoneNumber'
_AM='civrZoneEnforcedZoneSetActvtTime'
_AL='civrZoneEnforcedZoneSetZoneList'
_AK='civrZoneEnforcedZoneSetName'
_AJ='civrZoneMemberRowStatus'
_AI='civrActiveZonesetChecksum'
_AH='civrZonesetDbChecksum'
_AG='civrZoneMemberVsan'
_AF='civrZoneMemberAFId'
_AE='civrZoneMemberID'
_AD='civrZoneMemberType'
_AC='civrZoneMemberNumber'
_AB='civrZoneRowStatus'
_AA='civrZoneLastChange'
_A9='civrZoneMemberList'
_A8='civrZoneName'
_A7='civrZoneNumber'
_A6='civrZoneSetDeActivate'
_A5='civrZoneSetActivate'
_A4='civrZoneSetRowStatus'
_A3='civrZoneSetChecksum'
_A2='civrZoneSetLastChange'
_A1='civrZoneSetZoneList'
_A0='civrZoneSetNumber'
_z='civrEnabledDeviceDomainId'
_y='civrEnabledDeviceVsan'
_x='civrEnabledDeviceAutoFabricId'
_w='civrTopologyIvrSrvGrpName'
_v='civrTopologyDefaultAfidSwitchWwn'
_u='civrTopologyAfidConfSwitchWwn'
_t='civrTopologyActiveSwitchWwn'
_s='civrTopologyActiveAutoFabricId'
_r='civrTopologyConfigSwitchWwn'
_q='civrTopologyConfigAutoFabricId'
_p='deactivating'
_o='activating'
_n='civrZoneSetIndex'
_m='vsanIndex'
_l='CISCO-VSAN-MIB'
_k='civrVirtualDomainsGroup'
_j='civrTopologyMisConfigReason'
_i='civrAfidMisConfigRemoteSWwn'
_h='civrAfidMisConfigLocalSWwn'
_g='civrAfidMisConfigRemoteAfid'
_f='civrAfidMisConfigLocalAfid'
_e='civrAfidMisConfigVsan'
_d='civrZoneMemberFabricId'
_c='civDomainIdConflictVsan'
_b='civrZoneEnforcedZoneMemberVsan'
_a='civrZoneEnforcedZoneMemberID'
_Z='civrTopologyAfidConfId'
_Y='CIvrAutonomousFabricId'
_X='civrZoneMemberIndex'
_W='civrZoneMemberParentIndex'
_V='civrZoneIndex'
_U='clear'
_T='OctetString'
_S='civrNotificationGroup'
_R='civrStatsGroup'
_Q='civrTopologyGroup'
_P='civrZoneConfigurationGroup'
_O='civrZoneSetActDeactPartialSucss'
_N='civrZoneSetActvatDeactvatResult'
_M='civrZoneSetName'
_L='noOp'
_K='Unsigned32'
_J='SnmpAdminString'
_I='accessible-for-notify'
_H='FcList'
_G='read-write'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCO-IVR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
DomainId,FcAddressId,FcNameId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','DomainId','FcAddressId','FcNameId','VsanIndex')
vsanIndex,=mibBuilder.importSymbols(_l,_m)
FcList,ZoneQosPriorityLevel=mibBuilder.importSymbols('CISCO-ZS-MIB',_H,'ZoneQosPriorityLevel')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoIvrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,371))
if mibBuilder.loadTexts:ciscoIvrMIB.setRevisions(('2005-03-03 00:00','2004-10-27 00:00','2003-11-03 00:00','2003-10-20 00:00'))
class CIvrZoneMemberType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('pwwnVsan',1))
class CIvrAutonomousFabricId(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class CIvrChecksum(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiscoIvrMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoIvrMIBNotifications=_CiscoIvrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,371,0))
_CiscoIvrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIvrMIBObjects=_CiscoIvrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,371,1))
_CimIvrConfiguration_ObjectIdentity=ObjectIdentity
cimIvrConfiguration=_CimIvrConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1))
_CimIvrGeneric_ObjectIdentity=ObjectIdentity
cimIvrGeneric=_CimIvrGeneric_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1,1))
_CivrFcidNatMode_Type=TruthValue
_CivrFcidNatMode_Object=MibScalar
civrFcidNatMode=_CivrFcidNatMode_Object((1,3,6,1,4,1,9,9,371,1,1,1,1),_CivrFcidNatMode_Type())
civrFcidNatMode.setMaxAccess(_G)
if mibBuilder.loadTexts:civrFcidNatMode.setStatus(_B)
_CivrVsanTopologyAutoDisc_Type=TruthValue
_CivrVsanTopologyAutoDisc_Object=MibScalar
civrVsanTopologyAutoDisc=_CivrVsanTopologyAutoDisc_Object((1,3,6,1,4,1,9,9,371,1,1,1,2),_CivrVsanTopologyAutoDisc_Type())
civrVsanTopologyAutoDisc.setMaxAccess(_G)
if mibBuilder.loadTexts:civrVsanTopologyAutoDisc.setStatus(_B)
_CimIvrZoneset_ObjectIdentity=ObjectIdentity
cimIvrZoneset=_CimIvrZoneset_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1,2))
class _CivrZoneSetNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388608))
_CivrZoneSetNumber_Type.__name__=_E
_CivrZoneSetNumber_Object=MibScalar
civrZoneSetNumber=_CivrZoneSetNumber_Object((1,3,6,1,4,1,9,9,371,1,1,2,1),_CivrZoneSetNumber_Type())
civrZoneSetNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneSetNumber.setStatus(_B)
_CivrZoneSetTable_Object=MibTable
civrZoneSetTable=_CivrZoneSetTable_Object((1,3,6,1,4,1,9,9,371,1,1,2,2))
if mibBuilder.loadTexts:civrZoneSetTable.setStatus(_B)
_CivrZoneSetEntry_Object=MibTableRow
civrZoneSetEntry=_CivrZoneSetEntry_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1))
civrZoneSetEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:civrZoneSetEntry.setStatus(_B)
class _CivrZoneSetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CivrZoneSetIndex_Type.__name__=_K
_CivrZoneSetIndex_Object=MibTableColumn
civrZoneSetIndex=_CivrZoneSetIndex_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1,1),_CivrZoneSetIndex_Type())
civrZoneSetIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:civrZoneSetIndex.setStatus(_B)
class _CivrZoneSetName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CivrZoneSetName_Type.__name__=_J
_CivrZoneSetName_Object=MibTableColumn
civrZoneSetName=_CivrZoneSetName_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1,2),_CivrZoneSetName_Type())
civrZoneSetName.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneSetName.setStatus(_B)
class _CivrZoneSetZoneList_Type(FcList):defaultHexValue=''
_CivrZoneSetZoneList_Type.__name__=_H
_CivrZoneSetZoneList_Object=MibTableColumn
civrZoneSetZoneList=_CivrZoneSetZoneList_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1,3),_CivrZoneSetZoneList_Type())
civrZoneSetZoneList.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneSetZoneList.setStatus(_B)
_CivrZoneSetLastChange_Type=TimeStamp
_CivrZoneSetLastChange_Object=MibTableColumn
civrZoneSetLastChange=_CivrZoneSetLastChange_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1,4),_CivrZoneSetLastChange_Type())
civrZoneSetLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneSetLastChange.setStatus(_B)
_CivrZoneSetChecksum_Type=CIvrChecksum
_CivrZoneSetChecksum_Object=MibTableColumn
civrZoneSetChecksum=_CivrZoneSetChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1,5),_CivrZoneSetChecksum_Type())
civrZoneSetChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneSetChecksum.setStatus(_B)
_CivrZoneSetRowStatus_Type=RowStatus
_CivrZoneSetRowStatus_Object=MibTableColumn
civrZoneSetRowStatus=_CivrZoneSetRowStatus_Object((1,3,6,1,4,1,9,9,371,1,1,2,2,1,6),_CivrZoneSetRowStatus_Type())
civrZoneSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneSetRowStatus.setStatus(_B)
class _CivrZoneSetActivate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CivrZoneSetActivate_Type.__name__=_K
_CivrZoneSetActivate_Object=MibScalar
civrZoneSetActivate=_CivrZoneSetActivate_Object((1,3,6,1,4,1,9,9,371,1,1,2,3),_CivrZoneSetActivate_Type())
civrZoneSetActivate.setMaxAccess(_G)
if mibBuilder.loadTexts:civrZoneSetActivate.setStatus(_B)
class _CivrZoneSetActvatDeactvatResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('activateSuccess',1),('activateFailureNoMembers',2),('activateFailureZoneOneorLessMem',3),('activateFailureNoTopology',4),('activateFailureNoPerVsanSucc',5),('activateFailureNoZoneset',6),('activateFailureNoVsans',7),('activateFailureFabricUnstable',8),('deactivateSuccess',9),('deactivateFailureNoActiveZs',10),('deactivateFailureNoPerVsanSucc',11),('deactivateFailureFabricUnstable',12),(_o,13),(_p,14),('idle',15),('deactivateSuccessFcNatShutup13',16),('activateFailureFabric',17),('deactivateFailureFabric',18),('activatePartialSuccessFabric',19),('deactivatePartialSuccessFabric',20),('deviceCleanupInProgress',21),('activatingReadyToAdv',22),('activatingAdvertising',23)))
_CivrZoneSetActvatDeactvatResult_Type.__name__=_E
_CivrZoneSetActvatDeactvatResult_Object=MibScalar
civrZoneSetActvatDeactvatResult=_CivrZoneSetActvatDeactvatResult_Object((1,3,6,1,4,1,9,9,371,1,1,2,4),_CivrZoneSetActvatDeactvatResult_Type())
civrZoneSetActvatDeactvatResult.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneSetActvatDeactvatResult.setStatus(_B)
class _CivrZoneSetDeActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deactivate',1),('noop',2)))
_CivrZoneSetDeActivate_Type.__name__=_E
_CivrZoneSetDeActivate_Object=MibScalar
civrZoneSetDeActivate=_CivrZoneSetDeActivate_Object((1,3,6,1,4,1,9,9,371,1,1,2,5),_CivrZoneSetDeActivate_Type())
civrZoneSetDeActivate.setMaxAccess(_G)
if mibBuilder.loadTexts:civrZoneSetDeActivate.setStatus(_B)
_CivrZonesetDbChecksum_Type=CIvrChecksum
_CivrZonesetDbChecksum_Object=MibScalar
civrZonesetDbChecksum=_CivrZonesetDbChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,2,6),_CivrZonesetDbChecksum_Type())
civrZonesetDbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZonesetDbChecksum.setStatus(_B)
_CivrActiveZonesetChecksum_Type=CIvrChecksum
_CivrActiveZonesetChecksum_Object=MibScalar
civrActiveZonesetChecksum=_CivrActiveZonesetChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,2,7),_CivrActiveZonesetChecksum_Type())
civrActiveZonesetChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrActiveZonesetChecksum.setStatus(_B)
class _CivrZoneEnforcedZoneSetName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CivrZoneEnforcedZoneSetName_Type.__name__=_J
_CivrZoneEnforcedZoneSetName_Object=MibScalar
civrZoneEnforcedZoneSetName=_CivrZoneEnforcedZoneSetName_Object((1,3,6,1,4,1,9,9,371,1,1,2,8),_CivrZoneEnforcedZoneSetName_Type())
civrZoneEnforcedZoneSetName.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneSetName.setStatus(_B)
_CivrZoneEnforcedZoneSetZoneList_Type=FcList
_CivrZoneEnforcedZoneSetZoneList_Object=MibScalar
civrZoneEnforcedZoneSetZoneList=_CivrZoneEnforcedZoneSetZoneList_Object((1,3,6,1,4,1,9,9,371,1,1,2,9),_CivrZoneEnforcedZoneSetZoneList_Type())
civrZoneEnforcedZoneSetZoneList.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneSetZoneList.setStatus(_B)
_CivrZoneEnforcedZoneSetActvtTime_Type=TimeStamp
_CivrZoneEnforcedZoneSetActvtTime_Object=MibScalar
civrZoneEnforcedZoneSetActvtTime=_CivrZoneEnforcedZoneSetActvtTime_Object((1,3,6,1,4,1,9,9,371,1,1,2,10),_CivrZoneEnforcedZoneSetActvtTime_Type())
civrZoneEnforcedZoneSetActvtTime.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneSetActvtTime.setStatus(_B)
class _CivrZoneCopyZoneSetEnforcdToFull_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copy',1),(_L,2)))
_CivrZoneCopyZoneSetEnforcdToFull_Type.__name__=_E
_CivrZoneCopyZoneSetEnforcdToFull_Object=MibScalar
civrZoneCopyZoneSetEnforcdToFull=_CivrZoneCopyZoneSetEnforcdToFull_Object((1,3,6,1,4,1,9,9,371,1,1,2,11),_CivrZoneCopyZoneSetEnforcdToFull_Type())
civrZoneCopyZoneSetEnforcdToFull.setMaxAccess(_G)
if mibBuilder.loadTexts:civrZoneCopyZoneSetEnforcdToFull.setStatus(_B)
class _CivrZoneClearFullZoneDb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_L,2)))
_CivrZoneClearFullZoneDb_Type.__name__=_E
_CivrZoneClearFullZoneDb_Object=MibScalar
civrZoneClearFullZoneDb=_CivrZoneClearFullZoneDb_Object((1,3,6,1,4,1,9,9,371,1,1,2,12),_CivrZoneClearFullZoneDb_Type())
civrZoneClearFullZoneDb.setMaxAccess(_G)
if mibBuilder.loadTexts:civrZoneClearFullZoneDb.setStatus(_B)
_CivrZonesetActivateForce_Type=TruthValue
_CivrZonesetActivateForce_Object=MibScalar
civrZonesetActivateForce=_CivrZonesetActivateForce_Object((1,3,6,1,4,1,9,9,371,1,1,2,13),_CivrZonesetActivateForce_Type())
civrZonesetActivateForce.setMaxAccess(_G)
if mibBuilder.loadTexts:civrZonesetActivateForce.setStatus(_B)
_CivrZoneSetTableNextIndex_Type=Unsigned32
_CivrZoneSetTableNextIndex_Object=MibScalar
civrZoneSetTableNextIndex=_CivrZoneSetTableNextIndex_Object((1,3,6,1,4,1,9,9,371,1,1,2,14),_CivrZoneSetTableNextIndex_Type())
civrZoneSetTableNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneSetTableNextIndex.setStatus(_B)
_CimIvrZone_ObjectIdentity=ObjectIdentity
cimIvrZone=_CimIvrZone_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1,3))
class _CivrZoneNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CivrZoneNumber_Type.__name__=_E
_CivrZoneNumber_Object=MibScalar
civrZoneNumber=_CivrZoneNumber_Object((1,3,6,1,4,1,9,9,371,1,1,3,1),_CivrZoneNumber_Type())
civrZoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneNumber.setStatus(_B)
_CivrZoneTable_Object=MibTable
civrZoneTable=_CivrZoneTable_Object((1,3,6,1,4,1,9,9,371,1,1,3,2))
if mibBuilder.loadTexts:civrZoneTable.setStatus(_B)
_CivrZoneEntry_Object=MibTableRow
civrZoneEntry=_CivrZoneEntry_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1))
civrZoneEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:civrZoneEntry.setStatus(_B)
class _CivrZoneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CivrZoneIndex_Type.__name__=_K
_CivrZoneIndex_Object=MibTableColumn
civrZoneIndex=_CivrZoneIndex_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,1),_CivrZoneIndex_Type())
civrZoneIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:civrZoneIndex.setStatus(_B)
class _CivrZoneName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,58))
_CivrZoneName_Type.__name__=_J
_CivrZoneName_Object=MibTableColumn
civrZoneName=_CivrZoneName_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,2),_CivrZoneName_Type())
civrZoneName.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneName.setStatus(_B)
class _CivrZoneMemberList_Type(FcList):defaultHexValue=''
_CivrZoneMemberList_Type.__name__=_H
_CivrZoneMemberList_Object=MibTableColumn
civrZoneMemberList=_CivrZoneMemberList_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,3),_CivrZoneMemberList_Type())
civrZoneMemberList.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneMemberList.setStatus(_B)
_CivrZoneLastChange_Type=TimeStamp
_CivrZoneLastChange_Object=MibTableColumn
civrZoneLastChange=_CivrZoneLastChange_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,5),_CivrZoneLastChange_Type())
civrZoneLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneLastChange.setStatus(_B)
_CivrZoneRowStatus_Type=RowStatus
_CivrZoneRowStatus_Object=MibTableColumn
civrZoneRowStatus=_CivrZoneRowStatus_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,6),_CivrZoneRowStatus_Type())
civrZoneRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneRowStatus.setStatus(_B)
_CivrZoneReadOnly_Type=TruthValue
_CivrZoneReadOnly_Object=MibTableColumn
civrZoneReadOnly=_CivrZoneReadOnly_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,7),_CivrZoneReadOnly_Type())
civrZoneReadOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneReadOnly.setStatus(_B)
_CivrZoneQosPriority_Type=ZoneQosPriorityLevel
_CivrZoneQosPriority_Object=MibTableColumn
civrZoneQosPriority=_CivrZoneQosPriority_Object((1,3,6,1,4,1,9,9,371,1,1,3,2,1,8),_CivrZoneQosPriority_Type())
civrZoneQosPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneQosPriority.setStatus(_B)
class _CivrZoneEnforcedZoneNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388608))
_CivrZoneEnforcedZoneNumber_Type.__name__=_E
_CivrZoneEnforcedZoneNumber_Object=MibScalar
civrZoneEnforcedZoneNumber=_CivrZoneEnforcedZoneNumber_Object((1,3,6,1,4,1,9,9,371,1,1,3,3),_CivrZoneEnforcedZoneNumber_Type())
civrZoneEnforcedZoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneNumber.setStatus(_B)
_CivrZoneEnforcedZoneTable_Object=MibTable
civrZoneEnforcedZoneTable=_CivrZoneEnforcedZoneTable_Object((1,3,6,1,4,1,9,9,371,1,1,3,4))
if mibBuilder.loadTexts:civrZoneEnforcedZoneTable.setStatus(_B)
_CivrZoneEnforcedZoneEntry_Object=MibTableRow
civrZoneEnforcedZoneEntry=_CivrZoneEnforcedZoneEntry_Object((1,3,6,1,4,1,9,9,371,1,1,3,4,1))
civrZoneEnforcedZoneEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:civrZoneEnforcedZoneEntry.setStatus(_B)
class _CivrZoneEnforcedZoneName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,58))
_CivrZoneEnforcedZoneName_Type.__name__=_J
_CivrZoneEnforcedZoneName_Object=MibTableColumn
civrZoneEnforcedZoneName=_CivrZoneEnforcedZoneName_Object((1,3,6,1,4,1,9,9,371,1,1,3,4,1,1),_CivrZoneEnforcedZoneName_Type())
civrZoneEnforcedZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneName.setStatus(_B)
_CivrZoneEnforcedZoneMemberList_Type=FcList
_CivrZoneEnforcedZoneMemberList_Object=MibTableColumn
civrZoneEnforcedZoneMemberList=_CivrZoneEnforcedZoneMemberList_Object((1,3,6,1,4,1,9,9,371,1,1,3,4,1,2),_CivrZoneEnforcedZoneMemberList_Type())
civrZoneEnforcedZoneMemberList.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberList.setStatus(_B)
_CivrZoneEnforcedZoneReadOnly_Type=TruthValue
_CivrZoneEnforcedZoneReadOnly_Object=MibTableColumn
civrZoneEnforcedZoneReadOnly=_CivrZoneEnforcedZoneReadOnly_Object((1,3,6,1,4,1,9,9,371,1,1,3,4,1,3),_CivrZoneEnforcedZoneReadOnly_Type())
civrZoneEnforcedZoneReadOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneReadOnly.setStatus(_B)
_CivrZoneEnforcedZoneQosPriority_Type=ZoneQosPriorityLevel
_CivrZoneEnforcedZoneQosPriority_Object=MibTableColumn
civrZoneEnforcedZoneQosPriority=_CivrZoneEnforcedZoneQosPriority_Object((1,3,6,1,4,1,9,9,371,1,1,3,4,1,4),_CivrZoneEnforcedZoneQosPriority_Type())
civrZoneEnforcedZoneQosPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneQosPriority.setStatus(_B)
_CivrZoneTableNextIndex_Type=Unsigned32
_CivrZoneTableNextIndex_Object=MibScalar
civrZoneTableNextIndex=_CivrZoneTableNextIndex_Object((1,3,6,1,4,1,9,9,371,1,1,3,5),_CivrZoneTableNextIndex_Type())
civrZoneTableNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneTableNextIndex.setStatus(_B)
_CimIvrZoneMember_ObjectIdentity=ObjectIdentity
cimIvrZoneMember=_CimIvrZoneMember_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1,4))
class _CivrZoneMemberNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777216))
_CivrZoneMemberNumber_Type.__name__=_E
_CivrZoneMemberNumber_Object=MibScalar
civrZoneMemberNumber=_CivrZoneMemberNumber_Object((1,3,6,1,4,1,9,9,371,1,1,4,1),_CivrZoneMemberNumber_Type())
civrZoneMemberNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneMemberNumber.setStatus(_B)
_CivrZoneMemberTable_Object=MibTable
civrZoneMemberTable=_CivrZoneMemberTable_Object((1,3,6,1,4,1,9,9,371,1,1,4,2))
if mibBuilder.loadTexts:civrZoneMemberTable.setStatus(_B)
_CivrZoneMemberEntry_Object=MibTableRow
civrZoneMemberEntry=_CivrZoneMemberEntry_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1))
civrZoneMemberEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:civrZoneMemberEntry.setStatus(_B)
class _CivrZoneMemberParentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CivrZoneMemberParentIndex_Type.__name__=_K
_CivrZoneMemberParentIndex_Object=MibTableColumn
civrZoneMemberParentIndex=_CivrZoneMemberParentIndex_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,1),_CivrZoneMemberParentIndex_Type())
civrZoneMemberParentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:civrZoneMemberParentIndex.setStatus(_B)
class _CivrZoneMemberIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CivrZoneMemberIndex_Type.__name__=_K
_CivrZoneMemberIndex_Object=MibTableColumn
civrZoneMemberIndex=_CivrZoneMemberIndex_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,2),_CivrZoneMemberIndex_Type())
civrZoneMemberIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:civrZoneMemberIndex.setStatus(_B)
_CivrZoneMemberType_Type=CIvrZoneMemberType
_CivrZoneMemberType_Object=MibTableColumn
civrZoneMemberType=_CivrZoneMemberType_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,3),_CivrZoneMemberType_Type())
civrZoneMemberType.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneMemberType.setStatus(_B)
_CivrZoneMemberID_Type=OctetString
_CivrZoneMemberID_Object=MibTableColumn
civrZoneMemberID=_CivrZoneMemberID_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,4),_CivrZoneMemberID_Type())
civrZoneMemberID.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneMemberID.setStatus(_B)
class _CivrZoneMemberAFId_Type(CIvrAutonomousFabricId):defaultValue=1
_CivrZoneMemberAFId_Type.__name__=_Y
_CivrZoneMemberAFId_Object=MibTableColumn
civrZoneMemberAFId=_CivrZoneMemberAFId_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,5),_CivrZoneMemberAFId_Type())
civrZoneMemberAFId.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneMemberAFId.setStatus(_B)
_CivrZoneMemberVsan_Type=VsanIndex
_CivrZoneMemberVsan_Object=MibTableColumn
civrZoneMemberVsan=_CivrZoneMemberVsan_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,6),_CivrZoneMemberVsan_Type())
civrZoneMemberVsan.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneMemberVsan.setStatus(_B)
_CivrZoneMemberRowStatus_Type=RowStatus
_CivrZoneMemberRowStatus_Object=MibTableColumn
civrZoneMemberRowStatus=_CivrZoneMemberRowStatus_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,7),_CivrZoneMemberRowStatus_Type())
civrZoneMemberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneMemberRowStatus.setStatus(_B)
class _CivrZoneMemberLunID_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
_CivrZoneMemberLunID_Type.__name__=_T
_CivrZoneMemberLunID_Object=MibTableColumn
civrZoneMemberLunID=_CivrZoneMemberLunID_Object((1,3,6,1,4,1,9,9,371,1,1,4,2,1,8),_CivrZoneMemberLunID_Type())
civrZoneMemberLunID.setMaxAccess(_D)
if mibBuilder.loadTexts:civrZoneMemberLunID.setStatus(_B)
class _CivrZoneEnforcedZoneMemberNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777216))
_CivrZoneEnforcedZoneMemberNumber_Type.__name__=_E
_CivrZoneEnforcedZoneMemberNumber_Object=MibScalar
civrZoneEnforcedZoneMemberNumber=_CivrZoneEnforcedZoneMemberNumber_Object((1,3,6,1,4,1,9,9,371,1,1,4,3),_CivrZoneEnforcedZoneMemberNumber_Type())
civrZoneEnforcedZoneMemberNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberNumber.setStatus(_B)
_CivrZoneEnforcedZoneMemberTable_Object=MibTable
civrZoneEnforcedZoneMemberTable=_CivrZoneEnforcedZoneMemberTable_Object((1,3,6,1,4,1,9,9,371,1,1,4,4))
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberTable.setStatus(_B)
_CivrZoneEnforcedZoneMemberEntry_Object=MibTableRow
civrZoneEnforcedZoneMemberEntry=_CivrZoneEnforcedZoneMemberEntry_Object((1,3,6,1,4,1,9,9,371,1,1,4,4,1))
civrZoneEnforcedZoneMemberEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberEntry.setStatus(_B)
_CivrZoneEnforcedZoneMemberType_Type=CIvrZoneMemberType
_CivrZoneEnforcedZoneMemberType_Object=MibTableColumn
civrZoneEnforcedZoneMemberType=_CivrZoneEnforcedZoneMemberType_Object((1,3,6,1,4,1,9,9,371,1,1,4,4,1,2),_CivrZoneEnforcedZoneMemberType_Type())
civrZoneEnforcedZoneMemberType.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberType.setStatus(_B)
_CivrZoneEnforcedZoneMemberID_Type=OctetString
_CivrZoneEnforcedZoneMemberID_Object=MibTableColumn
civrZoneEnforcedZoneMemberID=_CivrZoneEnforcedZoneMemberID_Object((1,3,6,1,4,1,9,9,371,1,1,4,4,1,3),_CivrZoneEnforcedZoneMemberID_Type())
civrZoneEnforcedZoneMemberID.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberID.setStatus(_B)
_CivrZoneEnforcedZoneMemberAFId_Type=CIvrAutonomousFabricId
_CivrZoneEnforcedZoneMemberAFId_Object=MibTableColumn
civrZoneEnforcedZoneMemberAFId=_CivrZoneEnforcedZoneMemberAFId_Object((1,3,6,1,4,1,9,9,371,1,1,4,4,1,4),_CivrZoneEnforcedZoneMemberAFId_Type())
civrZoneEnforcedZoneMemberAFId.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberAFId.setStatus(_B)
_CivrZoneEnforcedZoneMemberVsan_Type=VsanIndex
_CivrZoneEnforcedZoneMemberVsan_Object=MibTableColumn
civrZoneEnforcedZoneMemberVsan=_CivrZoneEnforcedZoneMemberVsan_Object((1,3,6,1,4,1,9,9,371,1,1,4,4,1,5),_CivrZoneEnforcedZoneMemberVsan_Type())
civrZoneEnforcedZoneMemberVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberVsan.setStatus(_B)
class _CivrZoneEnforcedZoneMemberLunID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
_CivrZoneEnforcedZoneMemberLunID_Type.__name__=_T
_CivrZoneEnforcedZoneMemberLunID_Object=MibTableColumn
civrZoneEnforcedZoneMemberLunID=_CivrZoneEnforcedZoneMemberLunID_Object((1,3,6,1,4,1,9,9,371,1,1,4,4,1,6),_CivrZoneEnforcedZoneMemberLunID_Type())
civrZoneEnforcedZoneMemberLunID.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneEnforcedZoneMemberLunID.setStatus(_B)
_CimIvrTopology_ObjectIdentity=ObjectIdentity
cimIvrTopology=_CimIvrTopology_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1,5))
_CivrTopologyConfiguredChecksum_Type=CIvrChecksum
_CivrTopologyConfiguredChecksum_Object=MibScalar
civrTopologyConfiguredChecksum=_CivrTopologyConfiguredChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,5,1),_CivrTopologyConfiguredChecksum_Type())
civrTopologyConfiguredChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyConfiguredChecksum.setStatus(_B)
_CivrTopologyConfigTable_Object=MibTable
civrTopologyConfigTable=_CivrTopologyConfigTable_Object((1,3,6,1,4,1,9,9,371,1,1,5,2))
if mibBuilder.loadTexts:civrTopologyConfigTable.setStatus(_B)
_CivrTopologyConfigEntry_Object=MibTableRow
civrTopologyConfigEntry=_CivrTopologyConfigEntry_Object((1,3,6,1,4,1,9,9,371,1,1,5,2,1))
civrTopologyConfigEntry.setIndexNames((0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:civrTopologyConfigEntry.setStatus(_B)
_CivrTopologyConfigSwitchWwn_Type=FcNameId
_CivrTopologyConfigSwitchWwn_Object=MibTableColumn
civrTopologyConfigSwitchWwn=_CivrTopologyConfigSwitchWwn_Object((1,3,6,1,4,1,9,9,371,1,1,5,2,1,1),_CivrTopologyConfigSwitchWwn_Type())
civrTopologyConfigSwitchWwn.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyConfigSwitchWwn.setStatus(_B)
_CivrTopologyConfigAutoFabricId_Type=CIvrAutonomousFabricId
_CivrTopologyConfigAutoFabricId_Object=MibTableColumn
civrTopologyConfigAutoFabricId=_CivrTopologyConfigAutoFabricId_Object((1,3,6,1,4,1,9,9,371,1,1,5,2,1,2),_CivrTopologyConfigAutoFabricId_Type())
civrTopologyConfigAutoFabricId.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyConfigAutoFabricId.setStatus(_B)
class _CivrTopologyConfigSwitchVsan2k_Type(FcList):defaultHexValue=''
_CivrTopologyConfigSwitchVsan2k_Type.__name__=_H
_CivrTopologyConfigSwitchVsan2k_Object=MibTableColumn
civrTopologyConfigSwitchVsan2k=_CivrTopologyConfigSwitchVsan2k_Object((1,3,6,1,4,1,9,9,371,1,1,5,2,1,3),_CivrTopologyConfigSwitchVsan2k_Type())
civrTopologyConfigSwitchVsan2k.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyConfigSwitchVsan2k.setStatus(_B)
class _CivrTopologyConfigSwitchVsan4k_Type(FcList):defaultHexValue=''
_CivrTopologyConfigSwitchVsan4k_Type.__name__=_H
_CivrTopologyConfigSwitchVsan4k_Object=MibTableColumn
civrTopologyConfigSwitchVsan4k=_CivrTopologyConfigSwitchVsan4k_Object((1,3,6,1,4,1,9,9,371,1,1,5,2,1,4),_CivrTopologyConfigSwitchVsan4k_Type())
civrTopologyConfigSwitchVsan4k.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyConfigSwitchVsan4k.setStatus(_B)
_CivrTopologyConfigRowStatus_Type=RowStatus
_CivrTopologyConfigRowStatus_Object=MibTableColumn
civrTopologyConfigRowStatus=_CivrTopologyConfigRowStatus_Object((1,3,6,1,4,1,9,9,371,1,1,5,2,1,5),_CivrTopologyConfigRowStatus_Type())
civrTopologyConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyConfigRowStatus.setStatus(_B)
class _CivrTopologyActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activate',1),(_L,2)))
_CivrTopologyActivate_Type.__name__=_E
_CivrTopologyActivate_Object=MibScalar
civrTopologyActivate=_CivrTopologyActivate_Object((1,3,6,1,4,1,9,9,371,1,1,5,3),_CivrTopologyActivate_Type())
civrTopologyActivate.setMaxAccess(_G)
if mibBuilder.loadTexts:civrTopologyActivate.setStatus(_B)
_CivrTopologyActivateTime_Type=TimeStamp
_CivrTopologyActivateTime_Object=MibScalar
civrTopologyActivateTime=_CivrTopologyActivateTime_Object((1,3,6,1,4,1,9,9,371,1,1,5,4),_CivrTopologyActivateTime_Type())
civrTopologyActivateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyActivateTime.setStatus(_B)
class _CivrTopologyCopyActiveToConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copy',1),(_L,2)))
_CivrTopologyCopyActiveToConfig_Type.__name__=_E
_CivrTopologyCopyActiveToConfig_Object=MibScalar
civrTopologyCopyActiveToConfig=_CivrTopologyCopyActiveToConfig_Object((1,3,6,1,4,1,9,9,371,1,1,5,5),_CivrTopologyCopyActiveToConfig_Type())
civrTopologyCopyActiveToConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:civrTopologyCopyActiveToConfig.setStatus(_B)
class _CivrTopologyClearConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_L,2)))
_CivrTopologyClearConfigured_Type.__name__=_E
_CivrTopologyClearConfigured_Object=MibScalar
civrTopologyClearConfigured=_CivrTopologyClearConfigured_Object((1,3,6,1,4,1,9,9,371,1,1,5,6),_CivrTopologyClearConfigured_Type())
civrTopologyClearConfigured.setMaxAccess(_G)
if mibBuilder.loadTexts:civrTopologyClearConfigured.setStatus(_B)
_CivrTopologyActiveChecksum_Type=CIvrChecksum
_CivrTopologyActiveChecksum_Object=MibScalar
civrTopologyActiveChecksum=_CivrTopologyActiveChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,5,7),_CivrTopologyActiveChecksum_Type())
civrTopologyActiveChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyActiveChecksum.setStatus(_B)
_CivrTopologyActiveTable_Object=MibTable
civrTopologyActiveTable=_CivrTopologyActiveTable_Object((1,3,6,1,4,1,9,9,371,1,1,5,8))
if mibBuilder.loadTexts:civrTopologyActiveTable.setStatus(_B)
_CivrTopologyActiveEntry_Object=MibTableRow
civrTopologyActiveEntry=_CivrTopologyActiveEntry_Object((1,3,6,1,4,1,9,9,371,1,1,5,8,1))
civrTopologyActiveEntry.setIndexNames((0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:civrTopologyActiveEntry.setStatus(_B)
_CivrTopologyActiveSwitchWwn_Type=FcNameId
_CivrTopologyActiveSwitchWwn_Object=MibTableColumn
civrTopologyActiveSwitchWwn=_CivrTopologyActiveSwitchWwn_Object((1,3,6,1,4,1,9,9,371,1,1,5,8,1,1),_CivrTopologyActiveSwitchWwn_Type())
civrTopologyActiveSwitchWwn.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyActiveSwitchWwn.setStatus(_B)
_CivrTopologyActiveAutoFabricId_Type=CIvrAutonomousFabricId
_CivrTopologyActiveAutoFabricId_Object=MibTableColumn
civrTopologyActiveAutoFabricId=_CivrTopologyActiveAutoFabricId_Object((1,3,6,1,4,1,9,9,371,1,1,5,8,1,2),_CivrTopologyActiveAutoFabricId_Type())
civrTopologyActiveAutoFabricId.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyActiveAutoFabricId.setStatus(_B)
class _CivrTopologyActiveSwitchVsan2k_Type(FcList):defaultHexValue=''
_CivrTopologyActiveSwitchVsan2k_Type.__name__=_H
_CivrTopologyActiveSwitchVsan2k_Object=MibTableColumn
civrTopologyActiveSwitchVsan2k=_CivrTopologyActiveSwitchVsan2k_Object((1,3,6,1,4,1,9,9,371,1,1,5,8,1,3),_CivrTopologyActiveSwitchVsan2k_Type())
civrTopologyActiveSwitchVsan2k.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyActiveSwitchVsan2k.setStatus(_B)
class _CivrTopologyActiveSwitchVsan4k_Type(FcList):defaultHexValue=''
_CivrTopologyActiveSwitchVsan4k_Type.__name__=_H
_CivrTopologyActiveSwitchVsan4k_Object=MibTableColumn
civrTopologyActiveSwitchVsan4k=_CivrTopologyActiveSwitchVsan4k_Object((1,3,6,1,4,1,9,9,371,1,1,5,8,1,4),_CivrTopologyActiveSwitchVsan4k_Type())
civrTopologyActiveSwitchVsan4k.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyActiveSwitchVsan4k.setStatus(_B)
_CivrTopologyActive_Type=TruthValue
_CivrTopologyActive_Object=MibScalar
civrTopologyActive=_CivrTopologyActive_Object((1,3,6,1,4,1,9,9,371,1,1,5,9),_CivrTopologyActive_Type())
civrTopologyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyActive.setStatus(_B)
_CivrTopologyAfidConfigChecksum_Type=CIvrChecksum
_CivrTopologyAfidConfigChecksum_Object=MibScalar
civrTopologyAfidConfigChecksum=_CivrTopologyAfidConfigChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,5,10),_CivrTopologyAfidConfigChecksum_Type())
civrTopologyAfidConfigChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyAfidConfigChecksum.setStatus(_B)
_CivrTopologyAfidConfTable_Object=MibTable
civrTopologyAfidConfTable=_CivrTopologyAfidConfTable_Object((1,3,6,1,4,1,9,9,371,1,1,5,11))
if mibBuilder.loadTexts:civrTopologyAfidConfTable.setStatus(_B)
_CivrTopologyAfidConfEntry_Object=MibTableRow
civrTopologyAfidConfEntry=_CivrTopologyAfidConfEntry_Object((1,3,6,1,4,1,9,9,371,1,1,5,11,1))
civrTopologyAfidConfEntry.setIndexNames((0,_A,_u),(0,_A,_Z))
if mibBuilder.loadTexts:civrTopologyAfidConfEntry.setStatus(_B)
_CivrTopologyAfidConfSwitchWwn_Type=FcNameId
_CivrTopologyAfidConfSwitchWwn_Object=MibTableColumn
civrTopologyAfidConfSwitchWwn=_CivrTopologyAfidConfSwitchWwn_Object((1,3,6,1,4,1,9,9,371,1,1,5,11,1,1),_CivrTopologyAfidConfSwitchWwn_Type())
civrTopologyAfidConfSwitchWwn.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyAfidConfSwitchWwn.setStatus(_B)
_CivrTopologyAfidConfId_Type=CIvrAutonomousFabricId
_CivrTopologyAfidConfId_Object=MibTableColumn
civrTopologyAfidConfId=_CivrTopologyAfidConfId_Object((1,3,6,1,4,1,9,9,371,1,1,5,11,1,2),_CivrTopologyAfidConfId_Type())
civrTopologyAfidConfId.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyAfidConfId.setStatus(_B)
class _CivrTopologyAfidConfSwitchVsan2k_Type(FcList):defaultHexValue=''
_CivrTopologyAfidConfSwitchVsan2k_Type.__name__=_H
_CivrTopologyAfidConfSwitchVsan2k_Object=MibTableColumn
civrTopologyAfidConfSwitchVsan2k=_CivrTopologyAfidConfSwitchVsan2k_Object((1,3,6,1,4,1,9,9,371,1,1,5,11,1,3),_CivrTopologyAfidConfSwitchVsan2k_Type())
civrTopologyAfidConfSwitchVsan2k.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyAfidConfSwitchVsan2k.setStatus(_B)
class _CivrTopologyAfidConfSwitchVsan4k_Type(FcList):defaultHexValue=''
_CivrTopologyAfidConfSwitchVsan4k_Type.__name__=_H
_CivrTopologyAfidConfSwitchVsan4k_Object=MibTableColumn
civrTopologyAfidConfSwitchVsan4k=_CivrTopologyAfidConfSwitchVsan4k_Object((1,3,6,1,4,1,9,9,371,1,1,5,11,1,4),_CivrTopologyAfidConfSwitchVsan4k_Type())
civrTopologyAfidConfSwitchVsan4k.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyAfidConfSwitchVsan4k.setStatus(_B)
_CivrTopologyAfidConfRowStatus_Type=RowStatus
_CivrTopologyAfidConfRowStatus_Object=MibTableColumn
civrTopologyAfidConfRowStatus=_CivrTopologyAfidConfRowStatus_Object((1,3,6,1,4,1,9,9,371,1,1,5,11,1,5),_CivrTopologyAfidConfRowStatus_Type())
civrTopologyAfidConfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyAfidConfRowStatus.setStatus(_B)
_CivrTopologyDefaultAfidChecksum_Type=CIvrChecksum
_CivrTopologyDefaultAfidChecksum_Object=MibScalar
civrTopologyDefaultAfidChecksum=_CivrTopologyDefaultAfidChecksum_Object((1,3,6,1,4,1,9,9,371,1,1,5,12),_CivrTopologyDefaultAfidChecksum_Type())
civrTopologyDefaultAfidChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:civrTopologyDefaultAfidChecksum.setStatus(_B)
_CivrTopologyDefaultAfidTable_Object=MibTable
civrTopologyDefaultAfidTable=_CivrTopologyDefaultAfidTable_Object((1,3,6,1,4,1,9,9,371,1,1,5,13))
if mibBuilder.loadTexts:civrTopologyDefaultAfidTable.setStatus(_B)
_CivrTopologyDefaultAfidEntry_Object=MibTableRow
civrTopologyDefaultAfidEntry=_CivrTopologyDefaultAfidEntry_Object((1,3,6,1,4,1,9,9,371,1,1,5,13,1))
civrTopologyDefaultAfidEntry.setIndexNames((0,_A,_v))
if mibBuilder.loadTexts:civrTopologyDefaultAfidEntry.setStatus(_B)
_CivrTopologyDefaultAfidSwitchWwn_Type=FcNameId
_CivrTopologyDefaultAfidSwitchWwn_Object=MibTableColumn
civrTopologyDefaultAfidSwitchWwn=_CivrTopologyDefaultAfidSwitchWwn_Object((1,3,6,1,4,1,9,9,371,1,1,5,13,1,1),_CivrTopologyDefaultAfidSwitchWwn_Type())
civrTopologyDefaultAfidSwitchWwn.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyDefaultAfidSwitchWwn.setStatus(_B)
class _CivrTopologyDefaultAfidId_Type(CIvrAutonomousFabricId):defaultValue=1
_CivrTopologyDefaultAfidId_Type.__name__=_Y
_CivrTopologyDefaultAfidId_Object=MibTableColumn
civrTopologyDefaultAfidId=_CivrTopologyDefaultAfidId_Object((1,3,6,1,4,1,9,9,371,1,1,5,13,1,2),_CivrTopologyDefaultAfidId_Type())
civrTopologyDefaultAfidId.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyDefaultAfidId.setStatus(_B)
_CivrTopologyDefaultAfidStatus_Type=RowStatus
_CivrTopologyDefaultAfidStatus_Object=MibTableColumn
civrTopologyDefaultAfidStatus=_CivrTopologyDefaultAfidStatus_Object((1,3,6,1,4,1,9,9,371,1,1,5,13,1,3),_CivrTopologyDefaultAfidStatus_Type())
civrTopologyDefaultAfidStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyDefaultAfidStatus.setStatus(_B)
_CivrTopologyIvrSrvGrpTable_Object=MibTable
civrTopologyIvrSrvGrpTable=_CivrTopologyIvrSrvGrpTable_Object((1,3,6,1,4,1,9,9,371,1,1,5,14))
if mibBuilder.loadTexts:civrTopologyIvrSrvGrpTable.setStatus(_B)
_CivrTopologyIvrSrvGrpEntry_Object=MibTableRow
civrTopologyIvrSrvGrpEntry=_CivrTopologyIvrSrvGrpEntry_Object((1,3,6,1,4,1,9,9,371,1,1,5,14,1))
civrTopologyIvrSrvGrpEntry.setIndexNames((0,_A,_w),(0,_A,_Z))
if mibBuilder.loadTexts:civrTopologyIvrSrvGrpEntry.setStatus(_B)
class _CivrTopologyIvrSrvGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CivrTopologyIvrSrvGrpName_Type.__name__=_J
_CivrTopologyIvrSrvGrpName_Object=MibTableColumn
civrTopologyIvrSrvGrpName=_CivrTopologyIvrSrvGrpName_Object((1,3,6,1,4,1,9,9,371,1,1,5,14,1,1),_CivrTopologyIvrSrvGrpName_Type())
civrTopologyIvrSrvGrpName.setMaxAccess(_F)
if mibBuilder.loadTexts:civrTopologyIvrSrvGrpName.setStatus(_B)
_CivrTopologyIvrSrvGrpVsan2k_Type=FcList
_CivrTopologyIvrSrvGrpVsan2k_Object=MibTableColumn
civrTopologyIvrSrvGrpVsan2k=_CivrTopologyIvrSrvGrpVsan2k_Object((1,3,6,1,4,1,9,9,371,1,1,5,14,1,2),_CivrTopologyIvrSrvGrpVsan2k_Type())
civrTopologyIvrSrvGrpVsan2k.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyIvrSrvGrpVsan2k.setStatus(_B)
_CivrTopologyIvrSrvGrpVsan4k_Type=FcList
_CivrTopologyIvrSrvGrpVsan4k_Object=MibTableColumn
civrTopologyIvrSrvGrpVsan4k=_CivrTopologyIvrSrvGrpVsan4k_Object((1,3,6,1,4,1,9,9,371,1,1,5,14,1,3),_CivrTopologyIvrSrvGrpVsan4k_Type())
civrTopologyIvrSrvGrpVsan4k.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyIvrSrvGrpVsan4k.setStatus(_B)
_CivrTopologyIvrSrvGrpRowStatus_Type=RowStatus
_CivrTopologyIvrSrvGrpRowStatus_Object=MibTableColumn
civrTopologyIvrSrvGrpRowStatus=_CivrTopologyIvrSrvGrpRowStatus_Object((1,3,6,1,4,1,9,9,371,1,1,5,14,1,4),_CivrTopologyIvrSrvGrpRowStatus_Type())
civrTopologyIvrSrvGrpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:civrTopologyIvrSrvGrpRowStatus.setStatus(_B)
class _CivrTopologyClearAfidConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_L,2)))
_CivrTopologyClearAfidConfig_Type.__name__=_E
_CivrTopologyClearAfidConfig_Object=MibScalar
civrTopologyClearAfidConfig=_CivrTopologyClearAfidConfig_Object((1,3,6,1,4,1,9,9,371,1,1,5,15),_CivrTopologyClearAfidConfig_Type())
civrTopologyClearAfidConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:civrTopologyClearAfidConfig.setStatus(_B)
_CimIvrVirtualDomains_ObjectIdentity=ObjectIdentity
cimIvrVirtualDomains=_CimIvrVirtualDomains_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,1,6))
_CivrAddIvrVirtualDomainsVsans2k_Type=FcList
_CivrAddIvrVirtualDomainsVsans2k_Object=MibScalar
civrAddIvrVirtualDomainsVsans2k=_CivrAddIvrVirtualDomainsVsans2k_Object((1,3,6,1,4,1,9,9,371,1,1,6,1),_CivrAddIvrVirtualDomainsVsans2k_Type())
civrAddIvrVirtualDomainsVsans2k.setMaxAccess(_G)
if mibBuilder.loadTexts:civrAddIvrVirtualDomainsVsans2k.setStatus(_B)
_CivrAddIvrVirtualDomainsVsans4k_Type=FcList
_CivrAddIvrVirtualDomainsVsans4k_Object=MibScalar
civrAddIvrVirtualDomainsVsans4k=_CivrAddIvrVirtualDomainsVsans4k_Object((1,3,6,1,4,1,9,9,371,1,1,6,2),_CivrAddIvrVirtualDomainsVsans4k_Type())
civrAddIvrVirtualDomainsVsans4k.setMaxAccess(_G)
if mibBuilder.loadTexts:civrAddIvrVirtualDomainsVsans4k.setStatus(_B)
_CimIvrStats_ObjectIdentity=ObjectIdentity
cimIvrStats=_CimIvrStats_ObjectIdentity((1,3,6,1,4,1,9,9,371,1,2))
_CivrZoneSetStatusTable_Object=MibTable
civrZoneSetStatusTable=_CivrZoneSetStatusTable_Object((1,3,6,1,4,1,9,9,371,1,2,1))
if mibBuilder.loadTexts:civrZoneSetStatusTable.setStatus(_B)
_CivrZoneSetStatusEntry_Object=MibTableRow
civrZoneSetStatusEntry=_CivrZoneSetStatusEntry_Object((1,3,6,1,4,1,9,9,371,1,2,1,1))
civrZoneSetStatusEntry.setIndexNames((0,_l,_m))
if mibBuilder.loadTexts:civrZoneSetStatusEntry.setStatus(_B)
class _CivrZoneSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('idle',1),('active',2),('deactive',3),('defaultZoneDeny',4),('activationFailed',5),('deactivationFailed',6),('activationNotInitiated',7),('activationFailedFabricChgFailed',8),('deactivationNotInitiated',9),('deactivationFailedFabChgFailed',10),(_o,11),('activatingWaitForLowestSwwn',12),('activatingFabricChanging',13),(_p,14),('deactivatingWaitForLowestSwwn',15),('deactivatingFabricChanging',16),('defaultZonePermit',17),('defaultZonePermitNoForce',18),('defaultZonePermitActZsNoForce',19),('denyNoActiveZoneset',20),('activationFailedLowestWwnWait',21),('deactivationFailedLowestWwnWait',22)))
_CivrZoneSetStatus_Type.__name__=_E
_CivrZoneSetStatus_Object=MibTableColumn
civrZoneSetStatus=_CivrZoneSetStatus_Object((1,3,6,1,4,1,9,9,371,1,2,1,1,1),_CivrZoneSetStatus_Type())
civrZoneSetStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:civrZoneSetStatus.setStatus(_B)
_CivrEnabledDeviceTable_Object=MibTable
civrEnabledDeviceTable=_CivrEnabledDeviceTable_Object((1,3,6,1,4,1,9,9,371,1,2,2))
if mibBuilder.loadTexts:civrEnabledDeviceTable.setStatus(_B)
_CivrEnabledDeviceEntry_Object=MibTableRow
civrEnabledDeviceEntry=_CivrEnabledDeviceEntry_Object((1,3,6,1,4,1,9,9,371,1,2,2,1))
civrEnabledDeviceEntry.setIndexNames((0,_A,_x),(0,_A,_y),(0,_A,_z))
if mibBuilder.loadTexts:civrEnabledDeviceEntry.setStatus(_B)
_CivrEnabledDeviceVsan_Type=VsanIndex
_CivrEnabledDeviceVsan_Object=MibTableColumn
civrEnabledDeviceVsan=_CivrEnabledDeviceVsan_Object((1,3,6,1,4,1,9,9,371,1,2,2,1,1),_CivrEnabledDeviceVsan_Type())
civrEnabledDeviceVsan.setMaxAccess(_F)
if mibBuilder.loadTexts:civrEnabledDeviceVsan.setStatus(_B)
_CivrEnabledDeviceAutoFabricId_Type=CIvrAutonomousFabricId
_CivrEnabledDeviceAutoFabricId_Object=MibTableColumn
civrEnabledDeviceAutoFabricId=_CivrEnabledDeviceAutoFabricId_Object((1,3,6,1,4,1,9,9,371,1,2,2,1,2),_CivrEnabledDeviceAutoFabricId_Type())
civrEnabledDeviceAutoFabricId.setMaxAccess(_F)
if mibBuilder.loadTexts:civrEnabledDeviceAutoFabricId.setStatus(_B)
_CivrEnabledDeviceDomainId_Type=DomainId
_CivrEnabledDeviceDomainId_Object=MibTableColumn
civrEnabledDeviceDomainId=_CivrEnabledDeviceDomainId_Object((1,3,6,1,4,1,9,9,371,1,2,2,1,3),_CivrEnabledDeviceDomainId_Type())
civrEnabledDeviceDomainId.setMaxAccess(_F)
if mibBuilder.loadTexts:civrEnabledDeviceDomainId.setStatus(_B)
_CivrEnabledDeviceSwitchWwn_Type=FcNameId
_CivrEnabledDeviceSwitchWwn_Object=MibTableColumn
civrEnabledDeviceSwitchWwn=_CivrEnabledDeviceSwitchWwn_Object((1,3,6,1,4,1,9,9,371,1,2,2,1,4),_CivrEnabledDeviceSwitchWwn_Type())
civrEnabledDeviceSwitchWwn.setMaxAccess(_C)
if mibBuilder.loadTexts:civrEnabledDeviceSwitchWwn.setStatus(_B)
class _CivrEnabledDeviceCapability_Type(Bits):namedValues=NamedValues(('version1',0))
_CivrEnabledDeviceCapability_Type.__name__='Bits'
_CivrEnabledDeviceCapability_Object=MibTableColumn
civrEnabledDeviceCapability=_CivrEnabledDeviceCapability_Object((1,3,6,1,4,1,9,9,371,1,2,2,1,5),_CivrEnabledDeviceCapability_Type())
civrEnabledDeviceCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:civrEnabledDeviceCapability.setStatus(_B)
_CivrZoneMemberFabricId_Type=FcAddressId
_CivrZoneMemberFabricId_Object=MibScalar
civrZoneMemberFabricId=_CivrZoneMemberFabricId_Object((1,3,6,1,4,1,9,9,371,1,2,3),_CivrZoneMemberFabricId_Type())
civrZoneMemberFabricId.setMaxAccess(_I)
if mibBuilder.loadTexts:civrZoneMemberFabricId.setStatus(_B)
_CivDomainIdConflictVsan_Type=VsanIndex
_CivDomainIdConflictVsan_Object=MibScalar
civDomainIdConflictVsan=_CivDomainIdConflictVsan_Object((1,3,6,1,4,1,9,9,371,1,2,4),_CivDomainIdConflictVsan_Type())
civDomainIdConflictVsan.setMaxAccess(_I)
if mibBuilder.loadTexts:civDomainIdConflictVsan.setStatus(_B)
_CivrZoneSetActDeactPartialSucss_Type=TruthValue
_CivrZoneSetActDeactPartialSucss_Object=MibScalar
civrZoneSetActDeactPartialSucss=_CivrZoneSetActDeactPartialSucss_Object((1,3,6,1,4,1,9,9,371,1,2,5),_CivrZoneSetActDeactPartialSucss_Type())
civrZoneSetActDeactPartialSucss.setMaxAccess(_I)
if mibBuilder.loadTexts:civrZoneSetActDeactPartialSucss.setStatus(_B)
_CivrAfidMisConfigVsan_Type=VsanIndex
_CivrAfidMisConfigVsan_Object=MibScalar
civrAfidMisConfigVsan=_CivrAfidMisConfigVsan_Object((1,3,6,1,4,1,9,9,371,1,2,6),_CivrAfidMisConfigVsan_Type())
civrAfidMisConfigVsan.setMaxAccess(_I)
if mibBuilder.loadTexts:civrAfidMisConfigVsan.setStatus(_B)
_CivrAfidMisConfigLocalAfid_Type=CIvrAutonomousFabricId
_CivrAfidMisConfigLocalAfid_Object=MibScalar
civrAfidMisConfigLocalAfid=_CivrAfidMisConfigLocalAfid_Object((1,3,6,1,4,1,9,9,371,1,2,7),_CivrAfidMisConfigLocalAfid_Type())
civrAfidMisConfigLocalAfid.setMaxAccess(_I)
if mibBuilder.loadTexts:civrAfidMisConfigLocalAfid.setStatus(_B)
_CivrAfidMisConfigRemoteAfid_Type=CIvrAutonomousFabricId
_CivrAfidMisConfigRemoteAfid_Object=MibScalar
civrAfidMisConfigRemoteAfid=_CivrAfidMisConfigRemoteAfid_Object((1,3,6,1,4,1,9,9,371,1,2,8),_CivrAfidMisConfigRemoteAfid_Type())
civrAfidMisConfigRemoteAfid.setMaxAccess(_I)
if mibBuilder.loadTexts:civrAfidMisConfigRemoteAfid.setStatus(_B)
_CivrAfidMisConfigLocalSWwn_Type=FcNameId
_CivrAfidMisConfigLocalSWwn_Object=MibScalar
civrAfidMisConfigLocalSWwn=_CivrAfidMisConfigLocalSWwn_Object((1,3,6,1,4,1,9,9,371,1,2,9),_CivrAfidMisConfigLocalSWwn_Type())
civrAfidMisConfigLocalSWwn.setMaxAccess(_I)
if mibBuilder.loadTexts:civrAfidMisConfigLocalSWwn.setStatus(_B)
_CivrAfidMisConfigRemoteSWwn_Type=FcNameId
_CivrAfidMisConfigRemoteSWwn_Object=MibScalar
civrAfidMisConfigRemoteSWwn=_CivrAfidMisConfigRemoteSWwn_Object((1,3,6,1,4,1,9,9,371,1,2,10),_CivrAfidMisConfigRemoteSWwn_Type())
civrAfidMisConfigRemoteSWwn.setMaxAccess(_I)
if mibBuilder.loadTexts:civrAfidMisConfigRemoteSWwn.setStatus(_B)
class _CivrTopologyMisConfigReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unknown',1),('afidMismatch',2)))
_CivrTopologyMisConfigReason_Type.__name__=_E
_CivrTopologyMisConfigReason_Object=MibScalar
civrTopologyMisConfigReason=_CivrTopologyMisConfigReason_Object((1,3,6,1,4,1,9,9,371,1,2,11),_CivrTopologyMisConfigReason_Type())
civrTopologyMisConfigReason.setMaxAccess(_I)
if mibBuilder.loadTexts:civrTopologyMisConfigReason.setStatus(_B)
_CiscoIvrMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIvrMIBConformance=_CiscoIvrMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,371,2))
_CivrZoneServerMIBCompliances_ObjectIdentity=ObjectIdentity
civrZoneServerMIBCompliances=_CivrZoneServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,371,2,1))
_CivrZoneServerMIBGroups_ObjectIdentity=ObjectIdentity
civrZoneServerMIBGroups=_CivrZoneServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,371,2,2))
civrZoneConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,1))
civrZoneConfigurationGroup.setObjects(*((_A,_A0),(_A,_M),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_N),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_a),(_A,_AS),(_A,_b),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:civrZoneConfigurationGroup.setStatus(_B)
civrTopologyGroup=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,2))
civrTopologyGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:civrTopologyGroup.setStatus(_B)
civrStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,3))
civrStatsGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_c),(_A,_d),(_A,_O)))
if mibBuilder.loadTexts:civrStatsGroup.setStatus(_B)
civrVirtualDomainsGroup=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,5))
civrVirtualDomainsGroup.setObjects(*((_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:civrVirtualDomainsGroup.setStatus(_B)
civrGenericGroup=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,6))
civrGenericGroup.setObjects(*((_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:civrGenericGroup.setStatus(_B)
civrTopologyGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,7))
civrTopologyGroupRev2.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:civrTopologyGroupRev2.setStatus(_B)
civrZoneConfigurationGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,371,2,2,8))
civrZoneConfigurationGroupRev2.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6)))
if mibBuilder.loadTexts:civrZoneConfigurationGroupRev2.setStatus(_B)
civrZoneActivationDoneNotify=NotificationType((1,3,6,1,4,1,9,9,371,0,1))
civrZoneActivationDoneNotify.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:civrZoneActivationDoneNotify.setStatus(_B)
civrZoneDeactivationDoneNotify=NotificationType((1,3,6,1,4,1,9,9,371,0,2))
civrZoneDeactivationDoneNotify.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:civrZoneDeactivationDoneNotify.setStatus(_B)
civrDomainConflictNotify=NotificationType((1,3,6,1,4,1,9,9,371,0,3))
civrDomainConflictNotify.setObjects(*((_A,_a),(_A,_b),(_A,_d),(_A,_c)))
if mibBuilder.loadTexts:civrDomainConflictNotify.setStatus(_B)
civrAfidConfigNotify=NotificationType((1,3,6,1,4,1,9,9,371,0,4))
civrAfidConfigNotify.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_e),(_A,_j)))
if mibBuilder.loadTexts:civrAfidConfigNotify.setStatus(_B)
civrNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,371,2,2,4))
civrNotificationGroup.setObjects(*((_A,_B7),(_A,_B8),(_A,_B9)))
if mibBuilder.loadTexts:civrNotificationGroup.setStatus(_B)
civrNotificationGroupRev2=NotificationGroup((1,3,6,1,4,1,9,9,371,2,2,9))
civrNotificationGroupRev2.setObjects((_A,_BA))
if mibBuilder.loadTexts:civrNotificationGroupRev2.setStatus(_B)
civrZoneServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,371,2,1,1))
civrZoneServerMIBCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:civrZoneServerMIBCompliance.setStatus(_BB)
civrZoneServerMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,371,2,1,2))
civrZoneServerMIBComplianceRev1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_k)))
if mibBuilder.loadTexts:civrZoneServerMIBComplianceRev1.setStatus(_BB)
civrZoneServerMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,371,2,1,3))
civrZoneServerMIBComplianceRev2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_k),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF)))
if mibBuilder.loadTexts:civrZoneServerMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CIvrZoneMemberType':CIvrZoneMemberType,_Y:CIvrAutonomousFabricId,'CIvrChecksum':CIvrChecksum,'ciscoIvrMIB':ciscoIvrMIB,'ciscoIvrMIBNotifications':ciscoIvrMIBNotifications,_B7:civrZoneActivationDoneNotify,_B8:civrZoneDeactivationDoneNotify,_B9:civrDomainConflictNotify,_BA:civrAfidConfigNotify,'ciscoIvrMIBObjects':ciscoIvrMIBObjects,'cimIvrConfiguration':cimIvrConfiguration,'cimIvrGeneric':cimIvrGeneric,_An:civrFcidNatMode,_Ao:civrVsanTopologyAutoDisc,'cimIvrZoneset':cimIvrZoneset,_A0:civrZoneSetNumber,'civrZoneSetTable':civrZoneSetTable,'civrZoneSetEntry':civrZoneSetEntry,_n:civrZoneSetIndex,_M:civrZoneSetName,_A1:civrZoneSetZoneList,_A2:civrZoneSetLastChange,_A3:civrZoneSetChecksum,_A4:civrZoneSetRowStatus,_A5:civrZoneSetActivate,_N:civrZoneSetActvatDeactvatResult,_A6:civrZoneSetDeActivate,_AH:civrZonesetDbChecksum,_AI:civrActiveZonesetChecksum,_AK:civrZoneEnforcedZoneSetName,_AL:civrZoneEnforcedZoneSetZoneList,_AM:civrZoneEnforcedZoneSetActvtTime,_AT:civrZoneCopyZoneSetEnforcdToFull,_AU:civrZoneClearFullZoneDb,_AV:civrZonesetActivateForce,_B5:civrZoneSetTableNextIndex,'cimIvrZone':cimIvrZone,_A7:civrZoneNumber,'civrZoneTable':civrZoneTable,'civrZoneEntry':civrZoneEntry,_V:civrZoneIndex,_A8:civrZoneName,_A9:civrZoneMemberList,_AA:civrZoneLastChange,_AB:civrZoneRowStatus,_A_:civrZoneReadOnly,_B0:civrZoneQosPriority,_AN:civrZoneEnforcedZoneNumber,'civrZoneEnforcedZoneTable':civrZoneEnforcedZoneTable,'civrZoneEnforcedZoneEntry':civrZoneEnforcedZoneEntry,_AO:civrZoneEnforcedZoneName,_AP:civrZoneEnforcedZoneMemberList,_B1:civrZoneEnforcedZoneReadOnly,_B2:civrZoneEnforcedZoneQosPriority,_B6:civrZoneTableNextIndex,'cimIvrZoneMember':cimIvrZoneMember,_AC:civrZoneMemberNumber,'civrZoneMemberTable':civrZoneMemberTable,'civrZoneMemberEntry':civrZoneMemberEntry,_W:civrZoneMemberParentIndex,_X:civrZoneMemberIndex,_AD:civrZoneMemberType,_AE:civrZoneMemberID,_AF:civrZoneMemberAFId,_AG:civrZoneMemberVsan,_AJ:civrZoneMemberRowStatus,_B3:civrZoneMemberLunID,_AQ:civrZoneEnforcedZoneMemberNumber,'civrZoneEnforcedZoneMemberTable':civrZoneEnforcedZoneMemberTable,'civrZoneEnforcedZoneMemberEntry':civrZoneEnforcedZoneMemberEntry,_AR:civrZoneEnforcedZoneMemberType,_a:civrZoneEnforcedZoneMemberID,_AS:civrZoneEnforcedZoneMemberAFId,_b:civrZoneEnforcedZoneMemberVsan,_B4:civrZoneEnforcedZoneMemberLunID,'cimIvrTopology':cimIvrTopology,_Ab:civrTopologyConfiguredChecksum,'civrTopologyConfigTable':civrTopologyConfigTable,'civrTopologyConfigEntry':civrTopologyConfigEntry,_r:civrTopologyConfigSwitchWwn,_q:civrTopologyConfigAutoFabricId,_AW:civrTopologyConfigSwitchVsan2k,_AX:civrTopologyConfigSwitchVsan4k,_AY:civrTopologyConfigRowStatus,_Ad:civrTopologyActivate,_Ae:civrTopologyActivateTime,_Af:civrTopologyCopyActiveToConfig,_Ag:civrTopologyClearConfigured,_Ac:civrTopologyActiveChecksum,'civrTopologyActiveTable':civrTopologyActiveTable,'civrTopologyActiveEntry':civrTopologyActiveEntry,_t:civrTopologyActiveSwitchWwn,_s:civrTopologyActiveAutoFabricId,_AZ:civrTopologyActiveSwitchVsan2k,_Aa:civrTopologyActiveSwitchVsan4k,_Ah:civrTopologyActive,_Ax:civrTopologyAfidConfigChecksum,'civrTopologyAfidConfTable':civrTopologyAfidConfTable,'civrTopologyAfidConfEntry':civrTopologyAfidConfEntry,_u:civrTopologyAfidConfSwitchWwn,_Z:civrTopologyAfidConfId,_Ap:civrTopologyAfidConfSwitchVsan2k,_Aq:civrTopologyAfidConfSwitchVsan4k,_Ar:civrTopologyAfidConfRowStatus,_Ay:civrTopologyDefaultAfidChecksum,'civrTopologyDefaultAfidTable':civrTopologyDefaultAfidTable,'civrTopologyDefaultAfidEntry':civrTopologyDefaultAfidEntry,_v:civrTopologyDefaultAfidSwitchWwn,_As:civrTopologyDefaultAfidId,_At:civrTopologyDefaultAfidStatus,'civrTopologyIvrSrvGrpTable':civrTopologyIvrSrvGrpTable,'civrTopologyIvrSrvGrpEntry':civrTopologyIvrSrvGrpEntry,_w:civrTopologyIvrSrvGrpName,_Au:civrTopologyIvrSrvGrpVsan2k,_Av:civrTopologyIvrSrvGrpVsan4k,_Aw:civrTopologyIvrSrvGrpRowStatus,_Az:civrTopologyClearAfidConfig,'cimIvrVirtualDomains':cimIvrVirtualDomains,_Al:civrAddIvrVirtualDomainsVsans2k,_Am:civrAddIvrVirtualDomainsVsans4k,'cimIvrStats':cimIvrStats,'civrZoneSetStatusTable':civrZoneSetStatusTable,'civrZoneSetStatusEntry':civrZoneSetStatusEntry,_Ai:civrZoneSetStatus,'civrEnabledDeviceTable':civrEnabledDeviceTable,'civrEnabledDeviceEntry':civrEnabledDeviceEntry,_y:civrEnabledDeviceVsan,_x:civrEnabledDeviceAutoFabricId,_z:civrEnabledDeviceDomainId,_Aj:civrEnabledDeviceSwitchWwn,_Ak:civrEnabledDeviceCapability,_d:civrZoneMemberFabricId,_c:civDomainIdConflictVsan,_O:civrZoneSetActDeactPartialSucss,_e:civrAfidMisConfigVsan,_f:civrAfidMisConfigLocalAfid,_g:civrAfidMisConfigRemoteAfid,_h:civrAfidMisConfigLocalSWwn,_i:civrAfidMisConfigRemoteSWwn,_j:civrTopologyMisConfigReason,'ciscoIvrMIBConformance':ciscoIvrMIBConformance,'civrZoneServerMIBCompliances':civrZoneServerMIBCompliances,'civrZoneServerMIBCompliance':civrZoneServerMIBCompliance,'civrZoneServerMIBComplianceRev1':civrZoneServerMIBComplianceRev1,'civrZoneServerMIBComplianceRev2':civrZoneServerMIBComplianceRev2,'civrZoneServerMIBGroups':civrZoneServerMIBGroups,_P:civrZoneConfigurationGroup,_Q:civrTopologyGroup,_R:civrStatsGroup,_S:civrNotificationGroup,_k:civrVirtualDomainsGroup,_BC:civrGenericGroup,_BD:civrTopologyGroupRev2,_BE:civrZoneConfigurationGroupRev2,_BF:civrNotificationGroupRev2})