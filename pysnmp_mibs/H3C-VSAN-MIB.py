_T='h3cVsanDmDomainIdAssigned'
_S='h3cVsanDmDatabaseDomainId'
_R='not-accessible'
_Q='h3cVsanFcIdPersistencyWwn'
_P='static'
_O='SnmpAdminString'
_N='H3cFcNameIdOrZero'
_M='H3cFcDomainPriority'
_L='H3cFcDomainIdOrZero'
_K='ifIndex'
_J='IF-MIB'
_I='h3cVsanDmLocalSwitchWWN'
_H='read-create'
_G='Integer32'
_F='TruthValue'
_E='h3cVsanIndex'
_D='read-write'
_C='read-only'
_B='H3C-VSAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcAddressId,H3cFcDmState,H3cFcDomainId,H3cFcDomainIdList,H3cFcDomainIdOrZero,H3cFcDomainPriority,H3cFcNameId,H3cFcNameIdOrZero,H3cFcVsanIndex=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcAddressId','H3cFcDmState','H3cFcDomainId','H3cFcDomainIdList',_L,_M,'H3cFcNameId',_N,'H3cFcVsanIndex')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
h3cSan=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127))
if mibBuilder.loadTexts:h3cSan.setRevisions(('2014-07-25 18:40','2014-05-09 18:40','2014-03-04 15:50','2013-02-28 09:40'))
_H3cVsan_ObjectIdentity=ObjectIdentity
h3cVsan=_H3cVsan_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1))
_H3cVsanMibObjects_ObjectIdentity=ObjectIdentity
h3cVsanMibObjects=_H3cVsanMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1,1))
_H3cVsanDmConfiguration_ObjectIdentity=ObjectIdentity
h3cVsanDmConfiguration=_H3cVsanDmConfiguration_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1,1,1))
_H3cVsanTable_Object=MibTable
h3cVsanTable=_H3cVsanTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1))
if mibBuilder.loadTexts:h3cVsanTable.setStatus(_A)
_H3cVsanEntry_Object=MibTableRow
h3cVsanEntry=_H3cVsanEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1,1))
h3cVsanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cVsanEntry.setStatus(_A)
_H3cVsanIndex_Type=H3cFcVsanIndex
_H3cVsanIndex_Object=MibTableColumn
h3cVsanIndex=_H3cVsanIndex_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1,1,1),_H3cVsanIndex_Type())
h3cVsanIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cVsanIndex.setStatus(_A)
class _H3cVsanCoreSwitchName_Type(H3cFcNameIdOrZero):subtypeSpec=H3cFcNameIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(16,16))
_H3cVsanCoreSwitchName_Type.__name__=_N
_H3cVsanCoreSwitchName_Object=MibTableColumn
h3cVsanCoreSwitchName=_H3cVsanCoreSwitchName_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1,1,2),_H3cVsanCoreSwitchName_Type())
h3cVsanCoreSwitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanCoreSwitchName.setStatus(_A)
_H3cVsanRowStatus_Type=RowStatus
_H3cVsanRowStatus_Object=MibTableColumn
h3cVsanRowStatus=_H3cVsanRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1,1,3),_H3cVsanRowStatus_Type())
h3cVsanRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVsanRowStatus.setStatus(_A)
class _H3cVsanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cVsanName_Type.__name__=_O
_H3cVsanName_Object=MibTableColumn
h3cVsanName=_H3cVsanName_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1,1,4),_H3cVsanName_Type())
h3cVsanName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVsanName.setStatus(_A)
_H3cVsanWorkingMode_Type=Integer32
_H3cVsanWorkingMode_Object=MibTableColumn
h3cVsanWorkingMode=_H3cVsanWorkingMode_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,1,1,5),_H3cVsanWorkingMode_Type())
h3cVsanWorkingMode.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVsanWorkingMode.setStatus(_A)
_H3cVsanDmTable_Object=MibTable
h3cVsanDmTable=_H3cVsanDmTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2))
if mibBuilder.loadTexts:h3cVsanDmTable.setStatus(_A)
_H3cVsanDmEntry_Object=MibTableRow
h3cVsanDmEntry=_H3cVsanDmEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1))
h3cVsanDmEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cVsanDmEntry.setStatus(_A)
class _H3cVsanDmDomainConfigureEnable_Type(TruthValue):defaultValue=1
_H3cVsanDmDomainConfigureEnable_Type.__name__=_F
_H3cVsanDmDomainConfigureEnable_Object=MibTableColumn
h3cVsanDmDomainConfigureEnable=_H3cVsanDmDomainConfigureEnable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,1),_H3cVsanDmDomainConfigureEnable_Type())
h3cVsanDmDomainConfigureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmDomainConfigureEnable.setStatus(_A)
_H3cVsanDmFabricNameConfigured_Type=H3cFcNameIdOrZero
_H3cVsanDmFabricNameConfigured_Object=MibTableColumn
h3cVsanDmFabricNameConfigured=_H3cVsanDmFabricNameConfigured_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,2),_H3cVsanDmFabricNameConfigured_Type())
h3cVsanDmFabricNameConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmFabricNameConfigured.setStatus(_A)
class _H3cVsanDmPriorityConfigured_Type(H3cFcDomainPriority):defaultValue=128
_H3cVsanDmPriorityConfigured_Type.__name__=_M
_H3cVsanDmPriorityConfigured_Object=MibTableColumn
h3cVsanDmPriorityConfigured=_H3cVsanDmPriorityConfigured_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,3),_H3cVsanDmPriorityConfigured_Type())
h3cVsanDmPriorityConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmPriorityConfigured.setStatus(_A)
_H3cVsanDmAllowedDomainIdList_Type=H3cFcDomainIdList
_H3cVsanDmAllowedDomainIdList_Object=MibTableColumn
h3cVsanDmAllowedDomainIdList=_H3cVsanDmAllowedDomainIdList_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,4),_H3cVsanDmAllowedDomainIdList_Type())
h3cVsanDmAllowedDomainIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmAllowedDomainIdList.setStatus(_A)
class _H3cVsanDmDomainIdConfigured_Type(H3cFcDomainIdOrZero):defaultValue=0
_H3cVsanDmDomainIdConfigured_Type.__name__=_L
_H3cVsanDmDomainIdConfigured_Object=MibTableColumn
h3cVsanDmDomainIdConfigured=_H3cVsanDmDomainIdConfigured_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,5),_H3cVsanDmDomainIdConfigured_Type())
h3cVsanDmDomainIdConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmDomainIdConfigured.setStatus(_A)
class _H3cVsanDmDomainIdTypeConfigured_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('preferred',2)))
_H3cVsanDmDomainIdTypeConfigured_Type.__name__=_G
_H3cVsanDmDomainIdTypeConfigured_Object=MibTableColumn
h3cVsanDmDomainIdTypeConfigured=_H3cVsanDmDomainIdTypeConfigured_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,6),_H3cVsanDmDomainIdTypeConfigured_Type())
h3cVsanDmDomainIdTypeConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmDomainIdTypeConfigured.setStatus(_A)
class _H3cVsanDmAutoReconfigureEnable_Type(TruthValue):defaultValue=2
_H3cVsanDmAutoReconfigureEnable_Type.__name__=_F
_H3cVsanDmAutoReconfigureEnable_Object=MibTableColumn
h3cVsanDmAutoReconfigureEnable=_H3cVsanDmAutoReconfigureEnable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,7),_H3cVsanDmAutoReconfigureEnable_Type())
h3cVsanDmAutoReconfigureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmAutoReconfigureEnable.setStatus(_A)
class _H3cVsanDmDomainRestart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOperation',1),('nonDisruptive',2),('disruptive',3)))
_H3cVsanDmDomainRestart_Type.__name__=_G
_H3cVsanDmDomainRestart_Object=MibTableColumn
h3cVsanDmDomainRestart=_H3cVsanDmDomainRestart_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,8),_H3cVsanDmDomainRestart_Type())
h3cVsanDmDomainRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmDomainRestart.setStatus(_A)
_H3cVsanDmState_Type=H3cFcDmState
_H3cVsanDmState_Object=MibTableColumn
h3cVsanDmState=_H3cVsanDmState_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,9),_H3cVsanDmState_Type())
h3cVsanDmState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmState.setStatus(_A)
_H3cVsanDmDomainIdAssigned_Type=H3cFcDomainIdOrZero
_H3cVsanDmDomainIdAssigned_Object=MibTableColumn
h3cVsanDmDomainIdAssigned=_H3cVsanDmDomainIdAssigned_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,10),_H3cVsanDmDomainIdAssigned_Type())
h3cVsanDmDomainIdAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmDomainIdAssigned.setStatus(_A)
_H3cVsanDmPrincipalSwitchWWN_Type=H3cFcNameId
_H3cVsanDmPrincipalSwitchWWN_Object=MibTableColumn
h3cVsanDmPrincipalSwitchWWN=_H3cVsanDmPrincipalSwitchWWN_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,11),_H3cVsanDmPrincipalSwitchWWN_Type())
h3cVsanDmPrincipalSwitchWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmPrincipalSwitchWWN.setStatus(_A)
_H3cVsanDmLocalSwitchWWN_Type=H3cFcNameId
_H3cVsanDmLocalSwitchWWN_Object=MibTableColumn
h3cVsanDmLocalSwitchWWN=_H3cVsanDmLocalSwitchWWN_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,12),_H3cVsanDmLocalSwitchWWN_Type())
h3cVsanDmLocalSwitchWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmLocalSwitchWWN.setStatus(_A)
_H3cVsanDmPrincipalSwRunPriority_Type=H3cFcDomainPriority
_H3cVsanDmPrincipalSwRunPriority_Object=MibTableColumn
h3cVsanDmPrincipalSwRunPriority=_H3cVsanDmPrincipalSwRunPriority_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,13),_H3cVsanDmPrincipalSwRunPriority_Type())
h3cVsanDmPrincipalSwRunPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmPrincipalSwRunPriority.setStatus(_A)
_H3cVsanDmLocalSwRunPriority_Type=H3cFcDomainPriority
_H3cVsanDmLocalSwRunPriority_Object=MibTableColumn
h3cVsanDmLocalSwRunPriority=_H3cVsanDmLocalSwRunPriority_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,14),_H3cVsanDmLocalSwRunPriority_Type())
h3cVsanDmLocalSwRunPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmLocalSwRunPriority.setStatus(_A)
_H3cVsanDmPrincipalSwSlctCnt_Type=Counter32
_H3cVsanDmPrincipalSwSlctCnt_Object=MibTableColumn
h3cVsanDmPrincipalSwSlctCnt=_H3cVsanDmPrincipalSwSlctCnt_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,15),_H3cVsanDmPrincipalSwSlctCnt_Type())
h3cVsanDmPrincipalSwSlctCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmPrincipalSwSlctCnt.setStatus(_A)
_H3cVsanDmLocalPrincipalSwSlctCnt_Type=Counter32
_H3cVsanDmLocalPrincipalSwSlctCnt_Object=MibTableColumn
h3cVsanDmLocalPrincipalSwSlctCnt=_H3cVsanDmLocalPrincipalSwSlctCnt_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,16),_H3cVsanDmLocalPrincipalSwSlctCnt_Type())
h3cVsanDmLocalPrincipalSwSlctCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmLocalPrincipalSwSlctCnt.setStatus(_A)
_H3cVsanDmBFCnt_Type=Counter32
_H3cVsanDmBFCnt_Object=MibTableColumn
h3cVsanDmBFCnt=_H3cVsanDmBFCnt_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,17),_H3cVsanDmBFCnt_Type())
h3cVsanDmBFCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmBFCnt.setStatus(_A)
_H3cVsanDmRCFCnt_Type=Counter32
_H3cVsanDmRCFCnt_Object=MibTableColumn
h3cVsanDmRCFCnt=_H3cVsanDmRCFCnt_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,2,1,18),_H3cVsanDmRCFCnt_Type())
h3cVsanDmRCFCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmRCFCnt.setStatus(_A)
_H3cVsanDmIfConfigTable_Object=MibTable
h3cVsanDmIfConfigTable=_H3cVsanDmIfConfigTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,3))
if mibBuilder.loadTexts:h3cVsanDmIfConfigTable.setStatus(_A)
_H3cVsanDmIfConfigEntry_Object=MibTableRow
h3cVsanDmIfConfigEntry=_H3cVsanDmIfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,3,1))
h3cVsanDmIfConfigEntry.setIndexNames((0,_J,_K),(0,_B,_E))
if mibBuilder.loadTexts:h3cVsanDmIfConfigEntry.setStatus(_A)
class _H3cVsanDmIfConfigRcfReject_Type(TruthValue):defaultValue=2
_H3cVsanDmIfConfigRcfReject_Type.__name__=_F
_H3cVsanDmIfConfigRcfReject_Object=MibTableColumn
h3cVsanDmIfConfigRcfReject=_H3cVsanDmIfConfigRcfReject_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,3,1,1),_H3cVsanDmIfConfigRcfReject_Type())
h3cVsanDmIfConfigRcfReject.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmIfConfigRcfReject.setStatus(_A)
_H3cVsanFcIdTable_Object=MibTable
h3cVsanFcIdTable=_H3cVsanFcIdTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,4))
if mibBuilder.loadTexts:h3cVsanFcIdTable.setStatus(_A)
_H3cVsanFcIdEntry_Object=MibTableRow
h3cVsanFcIdEntry=_H3cVsanFcIdEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,4,1))
h3cVsanFcIdEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cVsanFcIdEntry.setStatus(_A)
_H3cVsanFreeFcIds_Type=Counter32
_H3cVsanFreeFcIds_Object=MibTableColumn
h3cVsanFreeFcIds=_H3cVsanFreeFcIds_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,4,1,1),_H3cVsanFreeFcIds_Type())
h3cVsanFreeFcIds.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanFreeFcIds.setStatus(_A)
_H3cVsanAssignedFcIds_Type=Counter32
_H3cVsanAssignedFcIds_Object=MibTableColumn
h3cVsanAssignedFcIds=_H3cVsanAssignedFcIds_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,4,1,2),_H3cVsanAssignedFcIds_Type())
h3cVsanAssignedFcIds.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanAssignedFcIds.setStatus(_A)
class _H3cVsanFcIdPersistency_Type(TruthValue):defaultValue=1
_H3cVsanFcIdPersistency_Type.__name__=_F
_H3cVsanFcIdPersistency_Object=MibTableColumn
h3cVsanFcIdPersistency=_H3cVsanFcIdPersistency_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,4,1,3),_H3cVsanFcIdPersistency_Type())
h3cVsanFcIdPersistency.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanFcIdPersistency.setStatus(_A)
class _H3cVsanFcIdPurge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('enable',2)))
_H3cVsanFcIdPurge_Type.__name__=_G
_H3cVsanFcIdPurge_Object=MibTableColumn
h3cVsanFcIdPurge=_H3cVsanFcIdPurge_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,4,1,4),_H3cVsanFcIdPurge_Type())
h3cVsanFcIdPurge.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanFcIdPurge.setStatus(_A)
_H3cVsanFcIdPersistencyTable_Object=MibTable
h3cVsanFcIdPersistencyTable=_H3cVsanFcIdPersistencyTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5))
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyTable.setStatus(_A)
_H3cVsanFcIdPersistencyEntry_Object=MibTableRow
h3cVsanFcIdPersistencyEntry=_H3cVsanFcIdPersistencyEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5,1))
h3cVsanFcIdPersistencyEntry.setIndexNames((0,_B,_E),(0,_B,_Q))
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyEntry.setStatus(_A)
_H3cVsanFcIdPersistencyWwn_Type=H3cFcNameId
_H3cVsanFcIdPersistencyWwn_Object=MibTableColumn
h3cVsanFcIdPersistencyWwn=_H3cVsanFcIdPersistencyWwn_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5,1,1),_H3cVsanFcIdPersistencyWwn_Type())
h3cVsanFcIdPersistencyWwn.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyWwn.setStatus(_A)
_H3cVsanFcIdPersistencyFcId_Type=H3cFcAddressId
_H3cVsanFcIdPersistencyFcId_Object=MibTableColumn
h3cVsanFcIdPersistencyFcId=_H3cVsanFcIdPersistencyFcId_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5,1,2),_H3cVsanFcIdPersistencyFcId_Type())
h3cVsanFcIdPersistencyFcId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyFcId.setStatus(_A)
_H3cVsanFcIdPersistencyUsed_Type=TruthValue
_H3cVsanFcIdPersistencyUsed_Object=MibTableColumn
h3cVsanFcIdPersistencyUsed=_H3cVsanFcIdPersistencyUsed_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5,1,3),_H3cVsanFcIdPersistencyUsed_Type())
h3cVsanFcIdPersistencyUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyUsed.setStatus(_A)
class _H3cVsanFcIdPersistencyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('dynamic',2)))
_H3cVsanFcIdPersistencyType_Type.__name__=_G
_H3cVsanFcIdPersistencyType_Object=MibTableColumn
h3cVsanFcIdPersistencyType=_H3cVsanFcIdPersistencyType_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5,1,4),_H3cVsanFcIdPersistencyType_Type())
h3cVsanFcIdPersistencyType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyType.setStatus(_A)
_H3cVsanFcIdPersistencyRowStatus_Type=RowStatus
_H3cVsanFcIdPersistencyRowStatus_Object=MibTableColumn
h3cVsanFcIdPersistencyRowStatus=_H3cVsanFcIdPersistencyRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,1,1,1,5,1,5),_H3cVsanFcIdPersistencyRowStatus_Type())
h3cVsanFcIdPersistencyRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVsanFcIdPersistencyRowStatus.setStatus(_A)
_H3cVsanDmInformation_ObjectIdentity=ObjectIdentity
h3cVsanDmInformation=_H3cVsanDmInformation_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1,1,2))
_H3cVsanDmDatabaseTable_Object=MibTable
h3cVsanDmDatabaseTable=_H3cVsanDmDatabaseTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,1))
if mibBuilder.loadTexts:h3cVsanDmDatabaseTable.setStatus(_A)
_H3cVsanDmDatabaseEntry_Object=MibTableRow
h3cVsanDmDatabaseEntry=_H3cVsanDmDatabaseEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,1,1))
h3cVsanDmDatabaseEntry.setIndexNames((0,_B,_E),(0,_B,_S))
if mibBuilder.loadTexts:h3cVsanDmDatabaseEntry.setStatus(_A)
_H3cVsanDmDatabaseDomainId_Type=H3cFcDomainId
_H3cVsanDmDatabaseDomainId_Object=MibTableColumn
h3cVsanDmDatabaseDomainId=_H3cVsanDmDatabaseDomainId_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,1,1,1),_H3cVsanDmDatabaseDomainId_Type())
h3cVsanDmDatabaseDomainId.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cVsanDmDatabaseDomainId.setStatus(_A)
_H3cVsanDmDatabaseSwitchWWN_Type=H3cFcNameId
_H3cVsanDmDatabaseSwitchWWN_Object=MibTableColumn
h3cVsanDmDatabaseSwitchWWN=_H3cVsanDmDatabaseSwitchWWN_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,1,1,2),_H3cVsanDmDatabaseSwitchWWN_Type())
h3cVsanDmDatabaseSwitchWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmDatabaseSwitchWWN.setStatus(_A)
_H3cVsanDmIfInfoTable_Object=MibTable
h3cVsanDmIfInfoTable=_H3cVsanDmIfInfoTable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,2))
if mibBuilder.loadTexts:h3cVsanDmIfInfoTable.setStatus(_A)
_H3cVsanDmIfInfoEntry_Object=MibTableRow
h3cVsanDmIfInfoEntry=_H3cVsanDmIfInfoEntry_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,2,1))
h3cVsanDmIfInfoEntry.setIndexNames((0,_J,_K),(0,_B,_E))
if mibBuilder.loadTexts:h3cVsanDmIfInfoEntry.setStatus(_A)
class _H3cVsanDmIfInfoRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonPrincipal',1),('principalUpstream',2),('principalDownstream',3),('isolated',4),('unknown',5)))
_H3cVsanDmIfInfoRole_Type.__name__=_G
_H3cVsanDmIfInfoRole_Object=MibTableColumn
h3cVsanDmIfInfoRole=_H3cVsanDmIfInfoRole_Object((1,3,6,1,4,1,2011,10,2,127,1,1,2,2,1,1),_H3cVsanDmIfInfoRole_Type())
h3cVsanDmIfInfoRole.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVsanDmIfInfoRole.setStatus(_A)
_H3cVsanDmNotifications_ObjectIdentity=ObjectIdentity
h3cVsanDmNotifications=_H3cVsanDmNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1,1,3))
_H3cVsanDmNotificationPrefix_ObjectIdentity=ObjectIdentity
h3cVsanDmNotificationPrefix=_H3cVsanDmNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1,1,3,0))
_H3cVsanDmNotificationSwitch_ObjectIdentity=ObjectIdentity
h3cVsanDmNotificationSwitch=_H3cVsanDmNotificationSwitch_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,1,1,3,1))
class _H3cVsanDmFabricChangeNotifyEnable_Type(TruthValue):defaultValue=2
_H3cVsanDmFabricChangeNotifyEnable_Type.__name__=_F
_H3cVsanDmFabricChangeNotifyEnable_Object=MibScalar
h3cVsanDmFabricChangeNotifyEnable=_H3cVsanDmFabricChangeNotifyEnable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,3,1,1),_H3cVsanDmFabricChangeNotifyEnable_Type())
h3cVsanDmFabricChangeNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmFabricChangeNotifyEnable.setStatus(_A)
class _H3cVsanDmDomainIdChangeNotifyEnable_Type(TruthValue):defaultValue=2
_H3cVsanDmDomainIdChangeNotifyEnable_Type.__name__=_F
_H3cVsanDmDomainIdChangeNotifyEnable_Object=MibScalar
h3cVsanDmDomainIdChangeNotifyEnable=_H3cVsanDmDomainIdChangeNotifyEnable_Object((1,3,6,1,4,1,2011,10,2,127,1,1,3,1,2),_H3cVsanDmDomainIdChangeNotifyEnable_Type())
h3cVsanDmDomainIdChangeNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVsanDmDomainIdChangeNotifyEnable.setStatus(_A)
h3cVsanDmDomainIdNotAssignedNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,1,1,3,0,1))
h3cVsanDmDomainIdNotAssignedNotify.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:h3cVsanDmDomainIdNotAssignedNotify.setStatus(_A)
h3cVsanDmNewPrincipalSwitchNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,1,1,3,0,2))
h3cVsanDmNewPrincipalSwitchNotify.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:h3cVsanDmNewPrincipalSwitchNotify.setStatus(_A)
h3cVsanDmFabricChangeNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,1,1,3,0,3))
h3cVsanDmFabricChangeNotify.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cVsanDmFabricChangeNotify.setStatus(_A)
h3cVsanDmDomainIdChangeNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,1,1,3,0,4))
h3cVsanDmDomainIdChangeNotify.setObjects(*((_B,_E),(_B,_T),(_B,_I)))
if mibBuilder.loadTexts:h3cVsanDmDomainIdChangeNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSan':h3cSan,'h3cVsan':h3cVsan,'h3cVsanMibObjects':h3cVsanMibObjects,'h3cVsanDmConfiguration':h3cVsanDmConfiguration,'h3cVsanTable':h3cVsanTable,'h3cVsanEntry':h3cVsanEntry,_E:h3cVsanIndex,'h3cVsanCoreSwitchName':h3cVsanCoreSwitchName,'h3cVsanRowStatus':h3cVsanRowStatus,'h3cVsanName':h3cVsanName,'h3cVsanWorkingMode':h3cVsanWorkingMode,'h3cVsanDmTable':h3cVsanDmTable,'h3cVsanDmEntry':h3cVsanDmEntry,'h3cVsanDmDomainConfigureEnable':h3cVsanDmDomainConfigureEnable,'h3cVsanDmFabricNameConfigured':h3cVsanDmFabricNameConfigured,'h3cVsanDmPriorityConfigured':h3cVsanDmPriorityConfigured,'h3cVsanDmAllowedDomainIdList':h3cVsanDmAllowedDomainIdList,'h3cVsanDmDomainIdConfigured':h3cVsanDmDomainIdConfigured,'h3cVsanDmDomainIdTypeConfigured':h3cVsanDmDomainIdTypeConfigured,'h3cVsanDmAutoReconfigureEnable':h3cVsanDmAutoReconfigureEnable,'h3cVsanDmDomainRestart':h3cVsanDmDomainRestart,'h3cVsanDmState':h3cVsanDmState,_T:h3cVsanDmDomainIdAssigned,'h3cVsanDmPrincipalSwitchWWN':h3cVsanDmPrincipalSwitchWWN,_I:h3cVsanDmLocalSwitchWWN,'h3cVsanDmPrincipalSwRunPriority':h3cVsanDmPrincipalSwRunPriority,'h3cVsanDmLocalSwRunPriority':h3cVsanDmLocalSwRunPriority,'h3cVsanDmPrincipalSwSlctCnt':h3cVsanDmPrincipalSwSlctCnt,'h3cVsanDmLocalPrincipalSwSlctCnt':h3cVsanDmLocalPrincipalSwSlctCnt,'h3cVsanDmBFCnt':h3cVsanDmBFCnt,'h3cVsanDmRCFCnt':h3cVsanDmRCFCnt,'h3cVsanDmIfConfigTable':h3cVsanDmIfConfigTable,'h3cVsanDmIfConfigEntry':h3cVsanDmIfConfigEntry,'h3cVsanDmIfConfigRcfReject':h3cVsanDmIfConfigRcfReject,'h3cVsanFcIdTable':h3cVsanFcIdTable,'h3cVsanFcIdEntry':h3cVsanFcIdEntry,'h3cVsanFreeFcIds':h3cVsanFreeFcIds,'h3cVsanAssignedFcIds':h3cVsanAssignedFcIds,'h3cVsanFcIdPersistency':h3cVsanFcIdPersistency,'h3cVsanFcIdPurge':h3cVsanFcIdPurge,'h3cVsanFcIdPersistencyTable':h3cVsanFcIdPersistencyTable,'h3cVsanFcIdPersistencyEntry':h3cVsanFcIdPersistencyEntry,_Q:h3cVsanFcIdPersistencyWwn,'h3cVsanFcIdPersistencyFcId':h3cVsanFcIdPersistencyFcId,'h3cVsanFcIdPersistencyUsed':h3cVsanFcIdPersistencyUsed,'h3cVsanFcIdPersistencyType':h3cVsanFcIdPersistencyType,'h3cVsanFcIdPersistencyRowStatus':h3cVsanFcIdPersistencyRowStatus,'h3cVsanDmInformation':h3cVsanDmInformation,'h3cVsanDmDatabaseTable':h3cVsanDmDatabaseTable,'h3cVsanDmDatabaseEntry':h3cVsanDmDatabaseEntry,_S:h3cVsanDmDatabaseDomainId,'h3cVsanDmDatabaseSwitchWWN':h3cVsanDmDatabaseSwitchWWN,'h3cVsanDmIfInfoTable':h3cVsanDmIfInfoTable,'h3cVsanDmIfInfoEntry':h3cVsanDmIfInfoEntry,'h3cVsanDmIfInfoRole':h3cVsanDmIfInfoRole,'h3cVsanDmNotifications':h3cVsanDmNotifications,'h3cVsanDmNotificationPrefix':h3cVsanDmNotificationPrefix,'h3cVsanDmDomainIdNotAssignedNotify':h3cVsanDmDomainIdNotAssignedNotify,'h3cVsanDmNewPrincipalSwitchNotify':h3cVsanDmNewPrincipalSwitchNotify,'h3cVsanDmFabricChangeNotify':h3cVsanDmFabricChangeNotify,'h3cVsanDmDomainIdChangeNotify':h3cVsanDmDomainIdChangeNotify,'h3cVsanDmNotificationSwitch':h3cVsanDmNotificationSwitch,'h3cVsanDmFabricChangeNotifyEnable':h3cVsanDmFabricChangeNotifyEnable,'h3cVsanDmDomainIdChangeNotifyEnable':h3cVsanDmDomainIdChangeNotifyEnable})