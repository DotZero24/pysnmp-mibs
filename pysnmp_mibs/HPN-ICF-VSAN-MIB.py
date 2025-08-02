_O='hpnicfVsanDmDomainIdAssigned'
_N='hpnicfVsanDmDatabaseDomainId'
_M='HpnicfFcNameIdOrZero'
_L='HpnicfFcDomainPriority'
_K='HpnicfFcDomainIdOrZero'
_J='ifIndex'
_I='IF-MIB'
_H='hpnicfVsanDmLocalSwitchWWN'
_G='Integer32'
_F='TruthValue'
_E='hpnicfVsanIndex'
_D='read-write'
_C='read-only'
_B='HPN-ICF-VSAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcDmState,HpnicfFcDomainId,HpnicfFcDomainIdList,HpnicfFcDomainIdOrZero,HpnicfFcDomainPriority,HpnicfFcNameId,HpnicfFcNameIdOrZero,HpnicfFcVsanIndex=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcDmState','HpnicfFcDomainId','HpnicfFcDomainIdList',_K,_L,'HpnicfFcNameId',_M,'HpnicfFcVsanIndex')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
hpnicfSan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127))
if mibBuilder.loadTexts:hpnicfSan.setRevisions(('2014-03-04 15:50','2013-02-28 09:40'))
_HpnicfVsan_ObjectIdentity=ObjectIdentity
hpnicfVsan=_HpnicfVsan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1))
_HpnicfVsanMibObjects_ObjectIdentity=ObjectIdentity
hpnicfVsanMibObjects=_HpnicfVsanMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1))
_HpnicfVsanDmConfiguration_ObjectIdentity=ObjectIdentity
hpnicfVsanDmConfiguration=_HpnicfVsanDmConfiguration_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1))
_HpnicfVsanTable_Object=MibTable
hpnicfVsanTable=_HpnicfVsanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,1))
if mibBuilder.loadTexts:hpnicfVsanTable.setStatus(_A)
_HpnicfVsanEntry_Object=MibTableRow
hpnicfVsanEntry=_HpnicfVsanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,1,1))
hpnicfVsanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfVsanEntry.setStatus(_A)
_HpnicfVsanIndex_Type=HpnicfFcVsanIndex
_HpnicfVsanIndex_Object=MibTableColumn
hpnicfVsanIndex=_HpnicfVsanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,1,1,1),_HpnicfVsanIndex_Type())
hpnicfVsanIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfVsanIndex.setStatus(_A)
class _HpnicfVsanCoreSwitchName_Type(HpnicfFcNameIdOrZero):subtypeSpec=HpnicfFcNameIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(16,16))
_HpnicfVsanCoreSwitchName_Type.__name__=_M
_HpnicfVsanCoreSwitchName_Object=MibTableColumn
hpnicfVsanCoreSwitchName=_HpnicfVsanCoreSwitchName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,1,1,2),_HpnicfVsanCoreSwitchName_Type())
hpnicfVsanCoreSwitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanCoreSwitchName.setStatus(_A)
_HpnicfVsanRowStatus_Type=RowStatus
_HpnicfVsanRowStatus_Object=MibTableColumn
hpnicfVsanRowStatus=_HpnicfVsanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,1,1,3),_HpnicfVsanRowStatus_Type())
hpnicfVsanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfVsanRowStatus.setStatus(_A)
_HpnicfVsanDmTable_Object=MibTable
hpnicfVsanDmTable=_HpnicfVsanDmTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2))
if mibBuilder.loadTexts:hpnicfVsanDmTable.setStatus(_A)
_HpnicfVsanDmEntry_Object=MibTableRow
hpnicfVsanDmEntry=_HpnicfVsanDmEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1))
hpnicfVsanDmEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfVsanDmEntry.setStatus(_A)
class _HpnicfVsanDmDomainConfigureEnable_Type(TruthValue):defaultValue=1
_HpnicfVsanDmDomainConfigureEnable_Type.__name__=_F
_HpnicfVsanDmDomainConfigureEnable_Object=MibTableColumn
hpnicfVsanDmDomainConfigureEnable=_HpnicfVsanDmDomainConfigureEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,1),_HpnicfVsanDmDomainConfigureEnable_Type())
hpnicfVsanDmDomainConfigureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmDomainConfigureEnable.setStatus(_A)
_HpnicfVsanDmFabricNameConfigured_Type=HpnicfFcNameIdOrZero
_HpnicfVsanDmFabricNameConfigured_Object=MibTableColumn
hpnicfVsanDmFabricNameConfigured=_HpnicfVsanDmFabricNameConfigured_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,2),_HpnicfVsanDmFabricNameConfigured_Type())
hpnicfVsanDmFabricNameConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmFabricNameConfigured.setStatus(_A)
class _HpnicfVsanDmPriorityConfigured_Type(HpnicfFcDomainPriority):defaultValue=128
_HpnicfVsanDmPriorityConfigured_Type.__name__=_L
_HpnicfVsanDmPriorityConfigured_Object=MibTableColumn
hpnicfVsanDmPriorityConfigured=_HpnicfVsanDmPriorityConfigured_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,3),_HpnicfVsanDmPriorityConfigured_Type())
hpnicfVsanDmPriorityConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmPriorityConfigured.setStatus(_A)
_HpnicfVsanDmAllowedDomainIdList_Type=HpnicfFcDomainIdList
_HpnicfVsanDmAllowedDomainIdList_Object=MibTableColumn
hpnicfVsanDmAllowedDomainIdList=_HpnicfVsanDmAllowedDomainIdList_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,4),_HpnicfVsanDmAllowedDomainIdList_Type())
hpnicfVsanDmAllowedDomainIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmAllowedDomainIdList.setStatus(_A)
class _HpnicfVsanDmDomainIdConfigured_Type(HpnicfFcDomainIdOrZero):defaultValue=0
_HpnicfVsanDmDomainIdConfigured_Type.__name__=_K
_HpnicfVsanDmDomainIdConfigured_Object=MibTableColumn
hpnicfVsanDmDomainIdConfigured=_HpnicfVsanDmDomainIdConfigured_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,5),_HpnicfVsanDmDomainIdConfigured_Type())
hpnicfVsanDmDomainIdConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmDomainIdConfigured.setStatus(_A)
class _HpnicfVsanDmDomainIdTypeConfigured_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('preferred',2)))
_HpnicfVsanDmDomainIdTypeConfigured_Type.__name__=_G
_HpnicfVsanDmDomainIdTypeConfigured_Object=MibTableColumn
hpnicfVsanDmDomainIdTypeConfigured=_HpnicfVsanDmDomainIdTypeConfigured_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,6),_HpnicfVsanDmDomainIdTypeConfigured_Type())
hpnicfVsanDmDomainIdTypeConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmDomainIdTypeConfigured.setStatus(_A)
class _HpnicfVsanDmAutoReconfigureEnable_Type(TruthValue):defaultValue=2
_HpnicfVsanDmAutoReconfigureEnable_Type.__name__=_F
_HpnicfVsanDmAutoReconfigureEnable_Object=MibTableColumn
hpnicfVsanDmAutoReconfigureEnable=_HpnicfVsanDmAutoReconfigureEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,7),_HpnicfVsanDmAutoReconfigureEnable_Type())
hpnicfVsanDmAutoReconfigureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmAutoReconfigureEnable.setStatus(_A)
class _HpnicfVsanDmDomainRestart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOperation',1),('nonDisruptive',2),('disruptive',3)))
_HpnicfVsanDmDomainRestart_Type.__name__=_G
_HpnicfVsanDmDomainRestart_Object=MibTableColumn
hpnicfVsanDmDomainRestart=_HpnicfVsanDmDomainRestart_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,8),_HpnicfVsanDmDomainRestart_Type())
hpnicfVsanDmDomainRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmDomainRestart.setStatus(_A)
_HpnicfVsanDmState_Type=HpnicfFcDmState
_HpnicfVsanDmState_Object=MibTableColumn
hpnicfVsanDmState=_HpnicfVsanDmState_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,9),_HpnicfVsanDmState_Type())
hpnicfVsanDmState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmState.setStatus(_A)
_HpnicfVsanDmDomainIdAssigned_Type=HpnicfFcDomainIdOrZero
_HpnicfVsanDmDomainIdAssigned_Object=MibTableColumn
hpnicfVsanDmDomainIdAssigned=_HpnicfVsanDmDomainIdAssigned_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,10),_HpnicfVsanDmDomainIdAssigned_Type())
hpnicfVsanDmDomainIdAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmDomainIdAssigned.setStatus(_A)
_HpnicfVsanDmPrincipalSwitchWWN_Type=HpnicfFcNameId
_HpnicfVsanDmPrincipalSwitchWWN_Object=MibTableColumn
hpnicfVsanDmPrincipalSwitchWWN=_HpnicfVsanDmPrincipalSwitchWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,11),_HpnicfVsanDmPrincipalSwitchWWN_Type())
hpnicfVsanDmPrincipalSwitchWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmPrincipalSwitchWWN.setStatus(_A)
_HpnicfVsanDmLocalSwitchWWN_Type=HpnicfFcNameId
_HpnicfVsanDmLocalSwitchWWN_Object=MibTableColumn
hpnicfVsanDmLocalSwitchWWN=_HpnicfVsanDmLocalSwitchWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,12),_HpnicfVsanDmLocalSwitchWWN_Type())
hpnicfVsanDmLocalSwitchWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmLocalSwitchWWN.setStatus(_A)
_HpnicfVsanDmPrincipalSwRunPriority_Type=HpnicfFcDomainPriority
_HpnicfVsanDmPrincipalSwRunPriority_Object=MibTableColumn
hpnicfVsanDmPrincipalSwRunPriority=_HpnicfVsanDmPrincipalSwRunPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,13),_HpnicfVsanDmPrincipalSwRunPriority_Type())
hpnicfVsanDmPrincipalSwRunPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmPrincipalSwRunPriority.setStatus(_A)
_HpnicfVsanDmLocalSwRunPriority_Type=HpnicfFcDomainPriority
_HpnicfVsanDmLocalSwRunPriority_Object=MibTableColumn
hpnicfVsanDmLocalSwRunPriority=_HpnicfVsanDmLocalSwRunPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,14),_HpnicfVsanDmLocalSwRunPriority_Type())
hpnicfVsanDmLocalSwRunPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmLocalSwRunPriority.setStatus(_A)
_HpnicfVsanDmPrincipalSwSlctCnt_Type=Counter32
_HpnicfVsanDmPrincipalSwSlctCnt_Object=MibTableColumn
hpnicfVsanDmPrincipalSwSlctCnt=_HpnicfVsanDmPrincipalSwSlctCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,15),_HpnicfVsanDmPrincipalSwSlctCnt_Type())
hpnicfVsanDmPrincipalSwSlctCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmPrincipalSwSlctCnt.setStatus(_A)
_HpnicfVsanDmLocalPrincipalSwSlctCnt_Type=Counter32
_HpnicfVsanDmLocalPrincipalSwSlctCnt_Object=MibTableColumn
hpnicfVsanDmLocalPrincipalSwSlctCnt=_HpnicfVsanDmLocalPrincipalSwSlctCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,16),_HpnicfVsanDmLocalPrincipalSwSlctCnt_Type())
hpnicfVsanDmLocalPrincipalSwSlctCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmLocalPrincipalSwSlctCnt.setStatus(_A)
_HpnicfVsanDmBFCnt_Type=Counter32
_HpnicfVsanDmBFCnt_Object=MibTableColumn
hpnicfVsanDmBFCnt=_HpnicfVsanDmBFCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,17),_HpnicfVsanDmBFCnt_Type())
hpnicfVsanDmBFCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmBFCnt.setStatus(_A)
_HpnicfVsanDmRCFCnt_Type=Counter32
_HpnicfVsanDmRCFCnt_Object=MibTableColumn
hpnicfVsanDmRCFCnt=_HpnicfVsanDmRCFCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,2,1,18),_HpnicfVsanDmRCFCnt_Type())
hpnicfVsanDmRCFCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmRCFCnt.setStatus(_A)
_HpnicfVsanDmIfConfigTable_Object=MibTable
hpnicfVsanDmIfConfigTable=_HpnicfVsanDmIfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,3))
if mibBuilder.loadTexts:hpnicfVsanDmIfConfigTable.setStatus(_A)
_HpnicfVsanDmIfConfigEntry_Object=MibTableRow
hpnicfVsanDmIfConfigEntry=_HpnicfVsanDmIfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,3,1))
hpnicfVsanDmIfConfigEntry.setIndexNames((0,_I,_J),(0,_B,_E))
if mibBuilder.loadTexts:hpnicfVsanDmIfConfigEntry.setStatus(_A)
class _HpnicfVsanDmIfConfigRcfReject_Type(TruthValue):defaultValue=2
_HpnicfVsanDmIfConfigRcfReject_Type.__name__=_F
_HpnicfVsanDmIfConfigRcfReject_Object=MibTableColumn
hpnicfVsanDmIfConfigRcfReject=_HpnicfVsanDmIfConfigRcfReject_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,1,3,1,1),_HpnicfVsanDmIfConfigRcfReject_Type())
hpnicfVsanDmIfConfigRcfReject.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmIfConfigRcfReject.setStatus(_A)
_HpnicfVsanDmInformation_ObjectIdentity=ObjectIdentity
hpnicfVsanDmInformation=_HpnicfVsanDmInformation_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2))
_HpnicfVsanDmDatabaseTable_Object=MibTable
hpnicfVsanDmDatabaseTable=_HpnicfVsanDmDatabaseTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,1))
if mibBuilder.loadTexts:hpnicfVsanDmDatabaseTable.setStatus(_A)
_HpnicfVsanDmDatabaseEntry_Object=MibTableRow
hpnicfVsanDmDatabaseEntry=_HpnicfVsanDmDatabaseEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,1,1))
hpnicfVsanDmDatabaseEntry.setIndexNames((0,_B,_E),(0,_B,_N))
if mibBuilder.loadTexts:hpnicfVsanDmDatabaseEntry.setStatus(_A)
_HpnicfVsanDmDatabaseDomainId_Type=HpnicfFcDomainId
_HpnicfVsanDmDatabaseDomainId_Object=MibTableColumn
hpnicfVsanDmDatabaseDomainId=_HpnicfVsanDmDatabaseDomainId_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,1,1,1),_HpnicfVsanDmDatabaseDomainId_Type())
hpnicfVsanDmDatabaseDomainId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfVsanDmDatabaseDomainId.setStatus(_A)
_HpnicfVsanDmDatabaseSwitchWWN_Type=HpnicfFcNameId
_HpnicfVsanDmDatabaseSwitchWWN_Object=MibTableColumn
hpnicfVsanDmDatabaseSwitchWWN=_HpnicfVsanDmDatabaseSwitchWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,1,1,2),_HpnicfVsanDmDatabaseSwitchWWN_Type())
hpnicfVsanDmDatabaseSwitchWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmDatabaseSwitchWWN.setStatus(_A)
_HpnicfVsanDmIfInfoTable_Object=MibTable
hpnicfVsanDmIfInfoTable=_HpnicfVsanDmIfInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,2))
if mibBuilder.loadTexts:hpnicfVsanDmIfInfoTable.setStatus(_A)
_HpnicfVsanDmIfInfoEntry_Object=MibTableRow
hpnicfVsanDmIfInfoEntry=_HpnicfVsanDmIfInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,2,1))
hpnicfVsanDmIfInfoEntry.setIndexNames((0,_I,_J),(0,_B,_E))
if mibBuilder.loadTexts:hpnicfVsanDmIfInfoEntry.setStatus(_A)
class _HpnicfVsanDmIfInfoRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonPrincipal',1),('principalUpstream',2),('principalDownstream',3),('isolated',4),('unknown',5)))
_HpnicfVsanDmIfInfoRole_Type.__name__=_G
_HpnicfVsanDmIfInfoRole_Object=MibTableColumn
hpnicfVsanDmIfInfoRole=_HpnicfVsanDmIfInfoRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,2,2,1,1),_HpnicfVsanDmIfInfoRole_Type())
hpnicfVsanDmIfInfoRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsanDmIfInfoRole.setStatus(_A)
_HpnicfVsanDmNotifications_ObjectIdentity=ObjectIdentity
hpnicfVsanDmNotifications=_HpnicfVsanDmNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3))
_HpnicfVsanDmNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfVsanDmNotificationPrefix=_HpnicfVsanDmNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,0))
_HpnicfVsanDmNotificationSwitch_ObjectIdentity=ObjectIdentity
hpnicfVsanDmNotificationSwitch=_HpnicfVsanDmNotificationSwitch_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,1))
class _HpnicfVsanDmFabricChangeNotifyEnable_Type(TruthValue):defaultValue=2
_HpnicfVsanDmFabricChangeNotifyEnable_Type.__name__=_F
_HpnicfVsanDmFabricChangeNotifyEnable_Object=MibScalar
hpnicfVsanDmFabricChangeNotifyEnable=_HpnicfVsanDmFabricChangeNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,1,1),_HpnicfVsanDmFabricChangeNotifyEnable_Type())
hpnicfVsanDmFabricChangeNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmFabricChangeNotifyEnable.setStatus(_A)
class _HpnicfVsanDmDomainIdChangeNotifyEnable_Type(TruthValue):defaultValue=2
_HpnicfVsanDmDomainIdChangeNotifyEnable_Type.__name__=_F
_HpnicfVsanDmDomainIdChangeNotifyEnable_Object=MibScalar
hpnicfVsanDmDomainIdChangeNotifyEnable=_HpnicfVsanDmDomainIdChangeNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,1,2),_HpnicfVsanDmDomainIdChangeNotifyEnable_Type())
hpnicfVsanDmDomainIdChangeNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVsanDmDomainIdChangeNotifyEnable.setStatus(_A)
hpnicfVsanDmDomainIdNotAssignedNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,0,1))
hpnicfVsanDmDomainIdNotAssignedNotify.setObjects(*((_B,_E),(_B,_H)))
if mibBuilder.loadTexts:hpnicfVsanDmDomainIdNotAssignedNotify.setStatus(_A)
hpnicfVsanDmNewPrincipalSwitchNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,0,2))
hpnicfVsanDmNewPrincipalSwitchNotify.setObjects(*((_B,_E),(_B,_H)))
if mibBuilder.loadTexts:hpnicfVsanDmNewPrincipalSwitchNotify.setStatus(_A)
hpnicfVsanDmFabricChangeNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,0,3))
hpnicfVsanDmFabricChangeNotify.setObjects((_B,_E))
if mibBuilder.loadTexts:hpnicfVsanDmFabricChangeNotify.setStatus(_A)
hpnicfVsanDmDomainIdChangeNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,1,1,3,0,4))
hpnicfVsanDmDomainIdChangeNotify.setObjects(*((_B,_E),(_B,_O),(_B,_H)))
if mibBuilder.loadTexts:hpnicfVsanDmDomainIdChangeNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfSan':hpnicfSan,'hpnicfVsan':hpnicfVsan,'hpnicfVsanMibObjects':hpnicfVsanMibObjects,'hpnicfVsanDmConfiguration':hpnicfVsanDmConfiguration,'hpnicfVsanTable':hpnicfVsanTable,'hpnicfVsanEntry':hpnicfVsanEntry,_E:hpnicfVsanIndex,'hpnicfVsanCoreSwitchName':hpnicfVsanCoreSwitchName,'hpnicfVsanRowStatus':hpnicfVsanRowStatus,'hpnicfVsanDmTable':hpnicfVsanDmTable,'hpnicfVsanDmEntry':hpnicfVsanDmEntry,'hpnicfVsanDmDomainConfigureEnable':hpnicfVsanDmDomainConfigureEnable,'hpnicfVsanDmFabricNameConfigured':hpnicfVsanDmFabricNameConfigured,'hpnicfVsanDmPriorityConfigured':hpnicfVsanDmPriorityConfigured,'hpnicfVsanDmAllowedDomainIdList':hpnicfVsanDmAllowedDomainIdList,'hpnicfVsanDmDomainIdConfigured':hpnicfVsanDmDomainIdConfigured,'hpnicfVsanDmDomainIdTypeConfigured':hpnicfVsanDmDomainIdTypeConfigured,'hpnicfVsanDmAutoReconfigureEnable':hpnicfVsanDmAutoReconfigureEnable,'hpnicfVsanDmDomainRestart':hpnicfVsanDmDomainRestart,'hpnicfVsanDmState':hpnicfVsanDmState,_O:hpnicfVsanDmDomainIdAssigned,'hpnicfVsanDmPrincipalSwitchWWN':hpnicfVsanDmPrincipalSwitchWWN,_H:hpnicfVsanDmLocalSwitchWWN,'hpnicfVsanDmPrincipalSwRunPriority':hpnicfVsanDmPrincipalSwRunPriority,'hpnicfVsanDmLocalSwRunPriority':hpnicfVsanDmLocalSwRunPriority,'hpnicfVsanDmPrincipalSwSlctCnt':hpnicfVsanDmPrincipalSwSlctCnt,'hpnicfVsanDmLocalPrincipalSwSlctCnt':hpnicfVsanDmLocalPrincipalSwSlctCnt,'hpnicfVsanDmBFCnt':hpnicfVsanDmBFCnt,'hpnicfVsanDmRCFCnt':hpnicfVsanDmRCFCnt,'hpnicfVsanDmIfConfigTable':hpnicfVsanDmIfConfigTable,'hpnicfVsanDmIfConfigEntry':hpnicfVsanDmIfConfigEntry,'hpnicfVsanDmIfConfigRcfReject':hpnicfVsanDmIfConfigRcfReject,'hpnicfVsanDmInformation':hpnicfVsanDmInformation,'hpnicfVsanDmDatabaseTable':hpnicfVsanDmDatabaseTable,'hpnicfVsanDmDatabaseEntry':hpnicfVsanDmDatabaseEntry,_N:hpnicfVsanDmDatabaseDomainId,'hpnicfVsanDmDatabaseSwitchWWN':hpnicfVsanDmDatabaseSwitchWWN,'hpnicfVsanDmIfInfoTable':hpnicfVsanDmIfInfoTable,'hpnicfVsanDmIfInfoEntry':hpnicfVsanDmIfInfoEntry,'hpnicfVsanDmIfInfoRole':hpnicfVsanDmIfInfoRole,'hpnicfVsanDmNotifications':hpnicfVsanDmNotifications,'hpnicfVsanDmNotificationPrefix':hpnicfVsanDmNotificationPrefix,'hpnicfVsanDmDomainIdNotAssignedNotify':hpnicfVsanDmDomainIdNotAssignedNotify,'hpnicfVsanDmNewPrincipalSwitchNotify':hpnicfVsanDmNewPrincipalSwitchNotify,'hpnicfVsanDmFabricChangeNotify':hpnicfVsanDmFabricChangeNotify,'hpnicfVsanDmDomainIdChangeNotify':hpnicfVsanDmDomainIdChangeNotify,'hpnicfVsanDmNotificationSwitch':hpnicfVsanDmNotificationSwitch,'hpnicfVsanDmFabricChangeNotifyEnable':hpnicfVsanDmFabricChangeNotifyEnable,'hpnicfVsanDmDomainIdChangeNotifyEnable':hpnicfVsanDmDomainIdChangeNotifyEnable})