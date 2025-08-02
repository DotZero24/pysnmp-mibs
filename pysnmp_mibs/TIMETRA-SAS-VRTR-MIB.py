_Y='tmnxVRtrMaxRouteDests'
_X='vRtrNetIfIngressFwdOutProfOcts'
_W='vRtrNetIfIngressFwdInProfOcts'
_V='vRtrNetIfIngressFwdOutProfPkts'
_U='vRtrNetIfIngressFwdInProfPkts'
_T='vRtrIfCollectStats'
_S='vRtrIfAcctPolicyId'
_R='vRtrStatExtnEntry'
_Q='vRtrConfExtnEntry'
_P='vRtrIfExtnEntry'
_O='vRtrNetIfIngressMeterIndex'
_N='read-write'
_M='vRtrMaxRoutesType'
_L='vRtrIfIndex'
_K='vRtrID'
_J='TruthValue'
_I='Unsigned32'
_H='Integer32'
_G='vRtrStatCurrNumRouteDests'
_F='vRtrMaxNumRouteDests'
_E='vRtrIfBfdSessExtLclDisc'
_D='read-only'
_C='TIMETRA-VRTR-MIB'
_B='TIMETRA-SAS-VRTR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp',_J)
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
vRtrConfEntry,vRtrID,vRtrIfBfdSessExtLclDisc,vRtrIfEntry,vRtrIfIndex,vRtrMaxRoutesType,vRtrStatEntry=mibBuilder.importSymbols(_C,'vRtrConfEntry',_K,_E,'vRtrIfEntry',_L,_M,'vRtrStatEntry')
TMplsLspExpProfMapID,TNetworkIngressMeterId=mibBuilder.importSymbols('TN-TC-MIB','TMplsLspExpProfMapID','TNetworkIngressMeterId')
timetraSASVRtrMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,8))
if mibBuilder.loadTexts:timetraSASVRtrMIBModule.setRevisions(('1909-01-01 00:00',))
_TmnxSASVRtrGroups_ObjectIdentity=ObjectIdentity
tmnxSASVRtrGroups=_TmnxSASVRtrGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,11))
_TSASVRtrObjects_ObjectIdentity=ObjectIdentity
tSASVRtrObjects=_TSASVRtrObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,7))
_VRtrIfExtnTable_Object=MibTable
vRtrIfExtnTable=_VRtrIfExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,7,1))
if mibBuilder.loadTexts:vRtrIfExtnTable.setStatus(_A)
_VRtrIfExtnEntry_Object=MibTableRow
vRtrIfExtnEntry=_VRtrIfExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,7,1,1))
if mibBuilder.loadTexts:vRtrIfExtnEntry.setStatus(_A)
class _VRtrIfAcctPolicyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_VRtrIfAcctPolicyId_Type.__name__=_I
_VRtrIfAcctPolicyId_Object=MibTableColumn
vRtrIfAcctPolicyId=_VRtrIfAcctPolicyId_Object((1,3,6,1,4,1,6527,6,2,2,2,7,1,1,1),_VRtrIfAcctPolicyId_Type())
vRtrIfAcctPolicyId.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfAcctPolicyId.setStatus(_A)
class _VRtrIfCollectStats_Type(TruthValue):defaultValue=2
_VRtrIfCollectStats_Type.__name__=_J
_VRtrIfCollectStats_Object=MibTableColumn
vRtrIfCollectStats=_VRtrIfCollectStats_Object((1,3,6,1,4,1,6527,6,2,2,2,7,1,1,2),_VRtrIfCollectStats_Type())
vRtrIfCollectStats.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfCollectStats.setStatus(_A)
_VRtrNetIfIngressStatsTable_Object=MibTable
vRtrNetIfIngressStatsTable=_VRtrNetIfIngressStatsTable_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2))
if mibBuilder.loadTexts:vRtrNetIfIngressStatsTable.setStatus(_A)
_VRtrNetIfIngressStatsEntry_Object=MibTableRow
vRtrNetIfIngressStatsEntry=_VRtrNetIfIngressStatsEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2,1))
vRtrNetIfIngressStatsEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_B,_O))
if mibBuilder.loadTexts:vRtrNetIfIngressStatsEntry.setStatus(_A)
_VRtrNetIfIngressMeterIndex_Type=TNetworkIngressMeterId
_VRtrNetIfIngressMeterIndex_Object=MibTableColumn
vRtrNetIfIngressMeterIndex=_VRtrNetIfIngressMeterIndex_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2,1,1),_VRtrNetIfIngressMeterIndex_Type())
vRtrNetIfIngressMeterIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vRtrNetIfIngressMeterIndex.setStatus(_A)
_VRtrNetIfIngressFwdInProfPkts_Type=Counter64
_VRtrNetIfIngressFwdInProfPkts_Object=MibTableColumn
vRtrNetIfIngressFwdInProfPkts=_VRtrNetIfIngressFwdInProfPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2,1,2),_VRtrNetIfIngressFwdInProfPkts_Type())
vRtrNetIfIngressFwdInProfPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrNetIfIngressFwdInProfPkts.setStatus(_A)
_VRtrNetIfIngressFwdOutProfPkts_Type=Counter64
_VRtrNetIfIngressFwdOutProfPkts_Object=MibTableColumn
vRtrNetIfIngressFwdOutProfPkts=_VRtrNetIfIngressFwdOutProfPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2,1,3),_VRtrNetIfIngressFwdOutProfPkts_Type())
vRtrNetIfIngressFwdOutProfPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrNetIfIngressFwdOutProfPkts.setStatus(_A)
_VRtrNetIfIngressFwdInProfOcts_Type=Counter64
_VRtrNetIfIngressFwdInProfOcts_Object=MibTableColumn
vRtrNetIfIngressFwdInProfOcts=_VRtrNetIfIngressFwdInProfOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2,1,4),_VRtrNetIfIngressFwdInProfOcts_Type())
vRtrNetIfIngressFwdInProfOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrNetIfIngressFwdInProfOcts.setStatus(_A)
_VRtrNetIfIngressFwdOutProfOcts_Type=Counter64
_VRtrNetIfIngressFwdOutProfOcts_Object=MibTableColumn
vRtrNetIfIngressFwdOutProfOcts=_VRtrNetIfIngressFwdOutProfOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,7,2,1,5),_VRtrNetIfIngressFwdOutProfOcts_Type())
vRtrNetIfIngressFwdOutProfOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrNetIfIngressFwdOutProfOcts.setStatus(_A)
_VRtrConfExtnTable_Object=MibTable
vRtrConfExtnTable=_VRtrConfExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,7,4))
if mibBuilder.loadTexts:vRtrConfExtnTable.setStatus(_A)
_VRtrConfExtnEntry_Object=MibTableRow
vRtrConfExtnEntry=_VRtrConfExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,7,4,1))
if mibBuilder.loadTexts:vRtrConfExtnEntry.setStatus(_A)
class _VRtrMaxNumRouteDests_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_VRtrMaxNumRouteDests_Type.__name__=_H
_VRtrMaxNumRouteDests_Object=MibTableColumn
vRtrMaxNumRouteDests=_VRtrMaxNumRouteDests_Object((1,3,6,1,4,1,6527,6,2,2,2,7,4,1,1),_VRtrMaxNumRouteDests_Type())
vRtrMaxNumRouteDests.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrMaxNumRouteDests.setStatus(_A)
_VRtrStatExtnTable_Object=MibTable
vRtrStatExtnTable=_VRtrStatExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,7,5))
if mibBuilder.loadTexts:vRtrStatExtnTable.setStatus(_A)
_VRtrStatExtnEntry_Object=MibTableRow
vRtrStatExtnEntry=_VRtrStatExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,7,5,1))
if mibBuilder.loadTexts:vRtrStatExtnEntry.setStatus(_A)
_VRtrStatCurrNumRouteDests_Type=Gauge32
_VRtrStatCurrNumRouteDests_Object=MibTableColumn
vRtrStatCurrNumRouteDests=_VRtrStatCurrNumRouteDests_Object((1,3,6,1,4,1,6527,6,2,2,2,7,5,1,1),_VRtrStatCurrNumRouteDests_Type())
vRtrStatCurrNumRouteDests.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrStatCurrNumRouteDests.setStatus(_A)
_TmnxSASVRtrNotifications_ObjectIdentity=ObjectIdentity
tmnxSASVRtrNotifications=_TmnxSASVRtrNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,7,20))
vRtrIfEntry.registerAugmentions((_B,_P))
vRtrIfExtnEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrConfEntry.registerAugmentions((_B,_Q))
vRtrConfExtnEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
vRtrStatEntry.registerAugmentions((_B,_R))
vRtrStatExtnEntry.setIndexNames(*vRtrStatEntry.getIndexNames())
tmnxSASVRtrV1v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,11,1))
tmnxSASVRtrV1v0Group.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:tmnxSASVRtrV1v0Group.setStatus(_A)
tmnxVRtrMaxRouteDests=NotificationType((1,3,6,1,4,1,6527,6,2,2,2,7,20,1))
tmnxVRtrMaxRouteDests.setObjects(*((_B,_G),(_B,_F),(_C,_M)))
if mibBuilder.loadTexts:tmnxVRtrMaxRouteDests.setStatus(_A)
tmnxVRtrBfdNoBfdHashResources=NotificationType((1,3,6,1,4,1,6527,6,2,2,2,7,20,2))
tmnxVRtrBfdNoBfdHashResources.setObjects((_C,_E))
if mibBuilder.loadTexts:tmnxVRtrBfdNoBfdHashResources.setStatus(_A)
tmnxVRtrBfdNoIomHwResources=NotificationType((1,3,6,1,4,1,6527,6,2,2,2,7,20,3))
tmnxVRtrBfdNoIomHwResources.setObjects((_C,_E))
if mibBuilder.loadTexts:tmnxVRtrBfdNoIomHwResources.setStatus(_A)
tmnxSASVrtrNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,6,2,2,1,11,2))
tmnxSASVrtrNotificationGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:tmnxSASVrtrNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraSASVRtrMIBModule':timetraSASVRtrMIBModule,'tmnxSASVRtrGroups':tmnxSASVRtrGroups,'tmnxSASVRtrV1v0Group':tmnxSASVRtrV1v0Group,'tmnxSASVrtrNotificationGroup':tmnxSASVrtrNotificationGroup,'tSASVRtrObjects':tSASVRtrObjects,'vRtrIfExtnTable':vRtrIfExtnTable,_P:vRtrIfExtnEntry,_S:vRtrIfAcctPolicyId,_T:vRtrIfCollectStats,'vRtrNetIfIngressStatsTable':vRtrNetIfIngressStatsTable,'vRtrNetIfIngressStatsEntry':vRtrNetIfIngressStatsEntry,_O:vRtrNetIfIngressMeterIndex,_U:vRtrNetIfIngressFwdInProfPkts,_V:vRtrNetIfIngressFwdOutProfPkts,_W:vRtrNetIfIngressFwdInProfOcts,_X:vRtrNetIfIngressFwdOutProfOcts,'vRtrConfExtnTable':vRtrConfExtnTable,_Q:vRtrConfExtnEntry,_F:vRtrMaxNumRouteDests,'vRtrStatExtnTable':vRtrStatExtnTable,_R:vRtrStatExtnEntry,_G:vRtrStatCurrNumRouteDests,'tmnxSASVRtrNotifications':tmnxSASVRtrNotifications,_Y:tmnxVRtrMaxRouteDests,'tmnxVRtrBfdNoBfdHashResources':tmnxVRtrBfdNoBfdHashResources,'tmnxVRtrBfdNoIomHwResources':tmnxVRtrBfdNoIomHwResources})