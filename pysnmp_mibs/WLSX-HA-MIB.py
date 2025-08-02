_R='wlsxTrapHaStandbyApCnt'
_Q='wlsxTrapHaHbtMissTimeStamp'
_P='wlsxTrapHaIntercontrollerHbtMissCnt'
_O='wlsxTrapHaConnectivityStatus'
_N='wlsxHaV6Role'
_M='wlsxHaV6Status'
_L='wlsxHaV4Role'
_K='wlsxHaV4Status'
_J='haActiveCtrl'
_I='not-accessible'
_H='wlsxHaActiveControllerIp'
_G='wlsxHaStandbyControllerIp'
_F='wlsxHaAPName'
_E='haProfileName'
_D='DisplayString'
_C='WLSX-HA-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaEnableValue,ArubaHaConnectivityStatus,ArubaHaRole=mibBuilder.importSymbols('ARUBA-TC','ArubaEnableValue','ArubaHaConnectivityStatus','ArubaHaRole')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxHaMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,20))
if mibBuilder.loadTexts:wlsxHaMIB.setRevisions(('2020-08-14 17:45',))
_WlsxHighAvalabilityInfoGroup_ObjectIdentity=ObjectIdentity
wlsxHighAvalabilityInfoGroup=_WlsxHighAvalabilityInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,20,1))
_WlsxHighAvalabilityConfigTable_Object=MibTable
wlsxHighAvalabilityConfigTable=_WlsxHighAvalabilityConfigTable_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1))
if mibBuilder.loadTexts:wlsxHighAvalabilityConfigTable.setStatus(_A)
_WlsxHighAvalabilityConfigEntry_Object=MibTableRow
wlsxHighAvalabilityConfigEntry=_WlsxHighAvalabilityConfigEntry_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1))
wlsxHighAvalabilityConfigEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:wlsxHighAvalabilityConfigEntry.setStatus(_A)
class _HaProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HaProfileName_Type.__name__=_D
_HaProfileName_Object=MibTableColumn
haProfileName=_HaProfileName_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,1),_HaProfileName_Type())
haProfileName.setMaxAccess(_I)
if mibBuilder.loadTexts:haProfileName.setStatus(_A)
class _HaMembership_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HaMembership_Type.__name__=_D
_HaMembership_Object=MibTableColumn
haMembership=_HaMembership_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,2),_HaMembership_Type())
haMembership.setMaxAccess(_B)
if mibBuilder.loadTexts:haMembership.setStatus(_A)
_HaState_Type=ArubaEnableValue
_HaState_Object=MibTableColumn
haState=_HaState_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,3),_HaState_Type())
haState.setMaxAccess(_B)
if mibBuilder.loadTexts:haState.setStatus(_A)
_HaRole_Type=ArubaHaRole
_HaRole_Object=MibTableColumn
haRole=_HaRole_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,4),_HaRole_Type())
haRole.setMaxAccess(_B)
if mibBuilder.loadTexts:haRole.setStatus(_A)
_HaPreemption_Type=ArubaEnableValue
_HaPreemption_Object=MibTableColumn
haPreemption=_HaPreemption_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,5),_HaPreemption_Type())
haPreemption.setMaxAccess(_B)
if mibBuilder.loadTexts:haPreemption.setStatus(_A)
_HaOversubscription_Type=ArubaEnableValue
_HaOversubscription_Object=MibTableColumn
haOversubscription=_HaOversubscription_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,6),_HaOversubscription_Type())
haOversubscription.setMaxAccess(_B)
if mibBuilder.loadTexts:haOversubscription.setStatus(_A)
_HaStateSync_Type=ArubaEnableValue
_HaStateSync_Object=MibTableColumn
haStateSync=_HaStateSync_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,7),_HaStateSync_Type())
haStateSync.setMaxAccess(_B)
if mibBuilder.loadTexts:haStateSync.setStatus(_A)
class _HaPresharedKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,32))
_HaPresharedKey_Type.__name__=_D
_HaPresharedKey_Object=MibTableColumn
haPresharedKey=_HaPresharedKey_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,8),_HaPresharedKey_Type())
haPresharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:haPresharedKey.setStatus(_A)
_HaIntercontrollerHbt_Type=ArubaEnableValue
_HaIntercontrollerHbt_Object=MibTableColumn
haIntercontrollerHbt=_HaIntercontrollerHbt_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,9),_HaIntercontrollerHbt_Type())
haIntercontrollerHbt.setMaxAccess(_B)
if mibBuilder.loadTexts:haIntercontrollerHbt.setStatus(_A)
_HaHbtThreshold_Type=Unsigned32
_HaHbtThreshold_Object=MibTableColumn
haHbtThreshold=_HaHbtThreshold_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,10),_HaHbtThreshold_Type())
haHbtThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:haHbtThreshold.setStatus(_A)
_HaHbtInterval_Type=Unsigned32
_HaHbtInterval_Object=MibTableColumn
haHbtInterval=_HaHbtInterval_Object((1,3,6,1,4,1,14823,2,2,1,20,1,1,1,11),_HaHbtInterval_Type())
haHbtInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:haHbtInterval.setStatus(_A)
_WlsxHighAvalabilityApTable_Object=MibTable
wlsxHighAvalabilityApTable=_WlsxHighAvalabilityApTable_Object((1,3,6,1,4,1,14823,2,2,1,20,1,2))
if mibBuilder.loadTexts:wlsxHighAvalabilityApTable.setStatus(_A)
_WlsxHighAvalabilityApEntry_Object=MibTableRow
wlsxHighAvalabilityApEntry=_WlsxHighAvalabilityApEntry_Object((1,3,6,1,4,1,14823,2,2,1,20,1,2,1))
wlsxHighAvalabilityApEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:wlsxHighAvalabilityApEntry.setStatus(_A)
_HaActiveAPs_Type=Gauge32
_HaActiveAPs_Object=MibTableColumn
haActiveAPs=_HaActiveAPs_Object((1,3,6,1,4,1,14823,2,2,1,20,1,2,1,1),_HaActiveAPs_Type())
haActiveAPs.setMaxAccess(_B)
if mibBuilder.loadTexts:haActiveAPs.setStatus(_A)
_HaStandbyAPs_Type=Gauge32
_HaStandbyAPs_Object=MibTableColumn
haStandbyAPs=_HaStandbyAPs_Object((1,3,6,1,4,1,14823,2,2,1,20,1,2,1,2),_HaStandbyAPs_Type())
haStandbyAPs.setMaxAccess(_B)
if mibBuilder.loadTexts:haStandbyAPs.setStatus(_A)
_HaTotalAPs_Type=Gauge32
_HaTotalAPs_Object=MibTableColumn
haTotalAPs=_HaTotalAPs_Object((1,3,6,1,4,1,14823,2,2,1,20,1,2,1,3),_HaTotalAPs_Type())
haTotalAPs.setMaxAccess(_B)
if mibBuilder.loadTexts:haTotalAPs.setStatus(_A)
_WlsxIntercontrollerHbtTable_Object=MibTable
wlsxIntercontrollerHbtTable=_WlsxIntercontrollerHbtTable_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3))
if mibBuilder.loadTexts:wlsxIntercontrollerHbtTable.setStatus(_A)
_WlsxIntercontrollerHbtEntry_Object=MibTableRow
wlsxIntercontrollerHbtEntry=_WlsxIntercontrollerHbtEntry_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1))
wlsxIntercontrollerHbtEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wlsxIntercontrollerHbtEntry.setStatus(_A)
class _HaActiveCtrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HaActiveCtrl_Type.__name__=_D
_HaActiveCtrl_Object=MibTableColumn
haActiveCtrl=_HaActiveCtrl_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,1),_HaActiveCtrl_Type())
haActiveCtrl.setMaxAccess(_I)
if mibBuilder.loadTexts:haActiveCtrl.setStatus(_A)
class _HaActiveCtrlIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HaActiveCtrlIp_Type.__name__=_D
_HaActiveCtrlIp_Object=MibTableColumn
haActiveCtrlIp=_HaActiveCtrlIp_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,2),_HaActiveCtrlIp_Type())
haActiveCtrlIp.setMaxAccess(_B)
if mibBuilder.loadTexts:haActiveCtrlIp.setStatus(_A)
_HaReferenceCnt_Type=Gauge32
_HaReferenceCnt_Object=MibTableColumn
haReferenceCnt=_HaReferenceCnt_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,3),_HaReferenceCnt_Type())
haReferenceCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:haReferenceCnt.setStatus(_A)
_HaTotalHbtRequestsSent_Type=Counter32
_HaTotalHbtRequestsSent_Object=MibTableColumn
haTotalHbtRequestsSent=_HaTotalHbtRequestsSent_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,4),_HaTotalHbtRequestsSent_Type())
haTotalHbtRequestsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:haTotalHbtRequestsSent.setStatus(_A)
_HaTotalHbtResponsesRcvd_Type=Counter32
_HaTotalHbtResponsesRcvd_Object=MibTableColumn
haTotalHbtResponsesRcvd=_HaTotalHbtResponsesRcvd_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,5),_HaTotalHbtResponsesRcvd_Type())
haTotalHbtResponsesRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:haTotalHbtResponsesRcvd.setStatus(_A)
_HaLastMissedHbtCnt_Type=Gauge32
_HaLastMissedHbtCnt_Object=MibTableColumn
haLastMissedHbtCnt=_HaLastMissedHbtCnt_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,6),_HaLastMissedHbtCnt_Type())
haLastMissedHbtCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:haLastMissedHbtCnt.setStatus(_A)
class _HaLastHbtMissedTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HaLastHbtMissedTime_Type.__name__=_D
_HaLastHbtMissedTime_Object=MibTableColumn
haLastHbtMissedTime=_HaLastHbtMissedTime_Object((1,3,6,1,4,1,14823,2,2,1,20,1,3,1,7),_HaLastHbtMissedTime_Type())
haLastHbtMissedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:haLastHbtMissedTime.setStatus(_A)
_WlsxStateSyncTable_Object=MibTable
wlsxStateSyncTable=_WlsxStateSyncTable_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4))
if mibBuilder.loadTexts:wlsxStateSyncTable.setStatus(_A)
_WlsxStateSyncEntry_Object=MibTableRow
wlsxStateSyncEntry=_WlsxStateSyncEntry_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1))
wlsxStateSyncEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:wlsxStateSyncEntry.setStatus(_A)
_HaActivePmkCacheEntries_Type=Gauge32
_HaActivePmkCacheEntries_Object=MibTableColumn
haActivePmkCacheEntries=_HaActivePmkCacheEntries_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1,1),_HaActivePmkCacheEntries_Type())
haActivePmkCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:haActivePmkCacheEntries.setStatus(_A)
_HaReplicatedPmkCacheEntries_Type=Gauge32
_HaReplicatedPmkCacheEntries_Object=MibTableColumn
haReplicatedPmkCacheEntries=_HaReplicatedPmkCacheEntries_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1,2),_HaReplicatedPmkCacheEntries_Type())
haReplicatedPmkCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:haReplicatedPmkCacheEntries.setStatus(_A)
_HaTotalPmkCacheEntries_Type=Gauge32
_HaTotalPmkCacheEntries_Object=MibTableColumn
haTotalPmkCacheEntries=_HaTotalPmkCacheEntries_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1,3),_HaTotalPmkCacheEntries_Type())
haTotalPmkCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:haTotalPmkCacheEntries.setStatus(_A)
_HaActiveKeyCacheEntries_Type=Gauge32
_HaActiveKeyCacheEntries_Object=MibTableColumn
haActiveKeyCacheEntries=_HaActiveKeyCacheEntries_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1,4),_HaActiveKeyCacheEntries_Type())
haActiveKeyCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:haActiveKeyCacheEntries.setStatus(_A)
_HaReplicatedKeyCacheEntries_Type=Gauge32
_HaReplicatedKeyCacheEntries_Object=MibTableColumn
haReplicatedKeyCacheEntries=_HaReplicatedKeyCacheEntries_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1,5),_HaReplicatedKeyCacheEntries_Type())
haReplicatedKeyCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:haReplicatedKeyCacheEntries.setStatus(_A)
_HaTotalKeyCacheEntries_Type=Gauge32
_HaTotalKeyCacheEntries_Object=MibTableColumn
haTotalKeyCacheEntries=_HaTotalKeyCacheEntries_Object((1,3,6,1,4,1,14823,2,2,1,20,1,4,1,6),_HaTotalKeyCacheEntries_Type())
haTotalKeyCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:haTotalKeyCacheEntries.setStatus(_A)
_WlsxHighAvalabilityTunnelTable_Object=MibTable
wlsxHighAvalabilityTunnelTable=_WlsxHighAvalabilityTunnelTable_Object((1,3,6,1,4,1,14823,2,2,1,20,1,5))
if mibBuilder.loadTexts:wlsxHighAvalabilityTunnelTable.setStatus(_A)
_WlsxHighAvalabilityTunnelEntry_Object=MibTableRow
wlsxHighAvalabilityTunnelEntry=_WlsxHighAvalabilityTunnelEntry_Object((1,3,6,1,4,1,14823,2,2,1,20,1,5,1))
wlsxHighAvalabilityTunnelEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:wlsxHighAvalabilityTunnelEntry.setStatus(_A)
_HaActiveVapTunnels_Type=Gauge32
_HaActiveVapTunnels_Object=MibTableColumn
haActiveVapTunnels=_HaActiveVapTunnels_Object((1,3,6,1,4,1,14823,2,2,1,20,1,5,1,1),_HaActiveVapTunnels_Type())
haActiveVapTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:haActiveVapTunnels.setStatus(_A)
_HaStandbyVapTunnels_Type=Gauge32
_HaStandbyVapTunnels_Object=MibTableColumn
haStandbyVapTunnels=_HaStandbyVapTunnels_Object((1,3,6,1,4,1,14823,2,2,1,20,1,5,1,2),_HaStandbyVapTunnels_Type())
haStandbyVapTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:haStandbyVapTunnels.setStatus(_A)
_HaTotalVapTunnels_Type=Gauge32
_HaTotalVapTunnels_Object=MibTableColumn
haTotalVapTunnels=_HaTotalVapTunnels_Object((1,3,6,1,4,1,14823,2,2,1,20,1,5,1,3),_HaTotalVapTunnels_Type())
haTotalVapTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:haTotalVapTunnels.setStatus(_A)
_HaAPHbtTunnels_Type=Gauge32
_HaAPHbtTunnels_Object=MibTableColumn
haAPHbtTunnels=_HaAPHbtTunnels_Object((1,3,6,1,4,1,14823,2,2,1,20,1,5,1,4),_HaAPHbtTunnels_Type())
haAPHbtTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:haAPHbtTunnels.setStatus(_A)
_WlsxHighAvalabilityTraps_ObjectIdentity=ObjectIdentity
wlsxHighAvalabilityTraps=_WlsxHighAvalabilityTraps_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,20,2))
_WlsxHaTrapObjectsGroup_ObjectIdentity=ObjectIdentity
wlsxHaTrapObjectsGroup=_WlsxHaTrapObjectsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,20,2,1))
_WlsxHaV4Status_Type=ArubaEnableValue
_WlsxHaV4Status_Object=MibScalar
wlsxHaV4Status=_WlsxHaV4Status_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,1),_WlsxHaV4Status_Type())
wlsxHaV4Status.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaV4Status.setStatus(_A)
_WlsxHaV4Role_Type=ArubaHaRole
_WlsxHaV4Role_Object=MibScalar
wlsxHaV4Role=_WlsxHaV4Role_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,2),_WlsxHaV4Role_Type())
wlsxHaV4Role.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaV4Role.setStatus(_A)
_WlsxHaV6Status_Type=ArubaEnableValue
_WlsxHaV6Status_Object=MibScalar
wlsxHaV6Status=_WlsxHaV6Status_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,3),_WlsxHaV6Status_Type())
wlsxHaV6Status.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaV6Status.setStatus(_A)
_WlsxHaV6Role_Type=ArubaHaRole
_WlsxHaV6Role_Object=MibScalar
wlsxHaV6Role=_WlsxHaV6Role_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,4),_WlsxHaV6Role_Type())
wlsxHaV6Role.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaV6Role.setStatus(_A)
class _WlsxHaAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_WlsxHaAPName_Type.__name__=_D
_WlsxHaAPName_Object=MibScalar
wlsxHaAPName=_WlsxHaAPName_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,5),_WlsxHaAPName_Type())
wlsxHaAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaAPName.setStatus(_A)
class _WlsxHaActiveControllerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_WlsxHaActiveControllerIp_Type.__name__=_D
_WlsxHaActiveControllerIp_Object=MibScalar
wlsxHaActiveControllerIp=_WlsxHaActiveControllerIp_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,6),_WlsxHaActiveControllerIp_Type())
wlsxHaActiveControllerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaActiveControllerIp.setStatus(_A)
class _WlsxHaStandbyControllerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_WlsxHaStandbyControllerIp_Type.__name__=_D
_WlsxHaStandbyControllerIp_Object=MibScalar
wlsxHaStandbyControllerIp=_WlsxHaStandbyControllerIp_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,7),_WlsxHaStandbyControllerIp_Type())
wlsxHaStandbyControllerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxHaStandbyControllerIp.setStatus(_A)
_WlsxTrapHaConnectivityStatus_Type=ArubaHaConnectivityStatus
_WlsxTrapHaConnectivityStatus_Object=MibScalar
wlsxTrapHaConnectivityStatus=_WlsxTrapHaConnectivityStatus_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,8),_WlsxTrapHaConnectivityStatus_Type())
wlsxTrapHaConnectivityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxTrapHaConnectivityStatus.setStatus(_A)
_WlsxTrapHaIntercontrollerHbtMissCnt_Type=Integer32
_WlsxTrapHaIntercontrollerHbtMissCnt_Object=MibScalar
wlsxTrapHaIntercontrollerHbtMissCnt=_WlsxTrapHaIntercontrollerHbtMissCnt_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,9),_WlsxTrapHaIntercontrollerHbtMissCnt_Type())
wlsxTrapHaIntercontrollerHbtMissCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxTrapHaIntercontrollerHbtMissCnt.setStatus(_A)
class _WlsxTrapHaHbtMissTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_WlsxTrapHaHbtMissTimeStamp_Type.__name__=_D
_WlsxTrapHaHbtMissTimeStamp_Object=MibScalar
wlsxTrapHaHbtMissTimeStamp=_WlsxTrapHaHbtMissTimeStamp_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,10),_WlsxTrapHaHbtMissTimeStamp_Type())
wlsxTrapHaHbtMissTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxTrapHaHbtMissTimeStamp.setStatus(_A)
_WlsxTrapHaStandbyApCnt_Type=Integer32
_WlsxTrapHaStandbyApCnt_Object=MibScalar
wlsxTrapHaStandbyApCnt=_WlsxTrapHaStandbyApCnt_Object((1,3,6,1,4,1,14823,2,2,1,20,2,1,11),_WlsxTrapHaStandbyApCnt_Type())
wlsxTrapHaStandbyApCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxTrapHaStandbyApCnt.setStatus(_A)
_WlsxHaTrapDefinitionGroup_ObjectIdentity=ObjectIdentity
wlsxHaTrapDefinitionGroup=_WlsxHaTrapDefinitionGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,20,2,2))
wlsxHaState=NotificationType((1,3,6,1,4,1,14823,2,2,1,20,2,2,1))
wlsxHaState.setObjects(*((_C,_K),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:wlsxHaState.setStatus(_A)
wlsxHaStandbyIpSentFailed=NotificationType((1,3,6,1,4,1,14823,2,2,1,20,2,2,2))
wlsxHaStandbyIpSentFailed.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:wlsxHaStandbyIpSentFailed.setStatus(_A)
wlsxHaStandbyConnectivityState=NotificationType((1,3,6,1,4,1,14823,2,2,1,20,2,2,3))
wlsxHaStandbyConnectivityState.setObjects(*((_C,_F),(_C,_G),(_C,_O)))
if mibBuilder.loadTexts:wlsxHaStandbyConnectivityState.setStatus(_A)
wlsxHaIntercontrollerHbtMiss=NotificationType((1,3,6,1,4,1,14823,2,2,1,20,2,2,4))
wlsxHaIntercontrollerHbtMiss.setObjects(*((_C,_P),(_C,_H),(_C,_Q)))
if mibBuilder.loadTexts:wlsxHaIntercontrollerHbtMiss.setStatus(_A)
wlsxHaFailoverTrigger=NotificationType((1,3,6,1,4,1,14823,2,2,1,20,2,2,5))
wlsxHaFailoverTrigger.setObjects(*((_C,_H),(_C,_R)))
if mibBuilder.loadTexts:wlsxHaFailoverTrigger.setStatus(_A)
wlsxHaFailoverRequestFromAp=NotificationType((1,3,6,1,4,1,14823,2,2,1,20,2,2,6))
wlsxHaFailoverRequestFromAp.setObjects((_C,_F))
if mibBuilder.loadTexts:wlsxHaFailoverRequestFromAp.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsxHaMIB':wlsxHaMIB,'wlsxHighAvalabilityInfoGroup':wlsxHighAvalabilityInfoGroup,'wlsxHighAvalabilityConfigTable':wlsxHighAvalabilityConfigTable,'wlsxHighAvalabilityConfigEntry':wlsxHighAvalabilityConfigEntry,_E:haProfileName,'haMembership':haMembership,'haState':haState,'haRole':haRole,'haPreemption':haPreemption,'haOversubscription':haOversubscription,'haStateSync':haStateSync,'haPresharedKey':haPresharedKey,'haIntercontrollerHbt':haIntercontrollerHbt,'haHbtThreshold':haHbtThreshold,'haHbtInterval':haHbtInterval,'wlsxHighAvalabilityApTable':wlsxHighAvalabilityApTable,'wlsxHighAvalabilityApEntry':wlsxHighAvalabilityApEntry,'haActiveAPs':haActiveAPs,'haStandbyAPs':haStandbyAPs,'haTotalAPs':haTotalAPs,'wlsxIntercontrollerHbtTable':wlsxIntercontrollerHbtTable,'wlsxIntercontrollerHbtEntry':wlsxIntercontrollerHbtEntry,_J:haActiveCtrl,'haActiveCtrlIp':haActiveCtrlIp,'haReferenceCnt':haReferenceCnt,'haTotalHbtRequestsSent':haTotalHbtRequestsSent,'haTotalHbtResponsesRcvd':haTotalHbtResponsesRcvd,'haLastMissedHbtCnt':haLastMissedHbtCnt,'haLastHbtMissedTime':haLastHbtMissedTime,'wlsxStateSyncTable':wlsxStateSyncTable,'wlsxStateSyncEntry':wlsxStateSyncEntry,'haActivePmkCacheEntries':haActivePmkCacheEntries,'haReplicatedPmkCacheEntries':haReplicatedPmkCacheEntries,'haTotalPmkCacheEntries':haTotalPmkCacheEntries,'haActiveKeyCacheEntries':haActiveKeyCacheEntries,'haReplicatedKeyCacheEntries':haReplicatedKeyCacheEntries,'haTotalKeyCacheEntries':haTotalKeyCacheEntries,'wlsxHighAvalabilityTunnelTable':wlsxHighAvalabilityTunnelTable,'wlsxHighAvalabilityTunnelEntry':wlsxHighAvalabilityTunnelEntry,'haActiveVapTunnels':haActiveVapTunnels,'haStandbyVapTunnels':haStandbyVapTunnels,'haTotalVapTunnels':haTotalVapTunnels,'haAPHbtTunnels':haAPHbtTunnels,'wlsxHighAvalabilityTraps':wlsxHighAvalabilityTraps,'wlsxHaTrapObjectsGroup':wlsxHaTrapObjectsGroup,_K:wlsxHaV4Status,_L:wlsxHaV4Role,_M:wlsxHaV6Status,_N:wlsxHaV6Role,_F:wlsxHaAPName,_H:wlsxHaActiveControllerIp,_G:wlsxHaStandbyControllerIp,_O:wlsxTrapHaConnectivityStatus,_P:wlsxTrapHaIntercontrollerHbtMissCnt,_Q:wlsxTrapHaHbtMissTimeStamp,_R:wlsxTrapHaStandbyApCnt,'wlsxHaTrapDefinitionGroup':wlsxHaTrapDefinitionGroup,'wlsxHaState':wlsxHaState,'wlsxHaStandbyIpSentFailed':wlsxHaStandbyIpSentFailed,'wlsxHaStandbyConnectivityState':wlsxHaStandbyConnectivityState,'wlsxHaIntercontrollerHbtMiss':wlsxHaIntercontrollerHbtMiss,'wlsxHaFailoverTrigger':wlsxHaFailoverTrigger,'wlsxHaFailoverRequestFromAp':wlsxHaFailoverRequestFromAp})