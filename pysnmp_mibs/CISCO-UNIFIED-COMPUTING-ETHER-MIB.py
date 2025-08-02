_i='cucsEtherNiErrStatsHistInstanceId'
_h='cucsEtherNiErrStatsInstanceId'
_g='cucsEtherServerIntFIoFsmStageInstanceId'
_f='cucsEtherServerIntFIoFsmInstanceId'
_e='cucsEtherPIoFsmStageInstanceId'
_d='cucsEtherPIoFsmInstanceId'
_c='cucsEtherPIoEndPointInstanceId'
_b='cucsEtherFcoeInterfaceStatsHistInstanceId'
_a='cucsEtherFcoeInterfaceStatsInstanceId'
_Z='cucsEtherServerIntFIoFsmTaskInstanceId'
_Y='cucsEtherSwitchIntFIoPcEpInstanceId'
_X='cucsEtherSwitchIntFIoPcInstanceId'
_W='cucsEtherServerIntFIoPcEpInstanceId'
_V='cucsEtherServerIntFIoPcInstanceId'
_U='cucsEtherPortChanIdUniverseInstanceId'
_T='cucsEtherPortChanIdElemInstanceId'
_S='cucsEtherTxStatsHistInstanceId'
_R='cucsEtherTxStatsInstanceId'
_Q='cucsEtherSwitchIntFIoInstanceId'
_P='cucsEtherSwIfConfigInstanceId'
_O='cucsEtherServerIntFIoInstanceId'
_N='cucsEtherRxStatsHistInstanceId'
_M='cucsEtherRxStatsInstanceId'
_L='cucsEtherPauseStatsHistInstanceId'
_K='cucsEtherPauseStatsInstanceId'
_J='cucsEtherPIoInstanceId'
_I='cucsEtherNicIfConfigInstanceId'
_H='cucsEtherLossStatsHistInstanceId'
_G='cucsEtherLossStatsInstanceId'
_F='cucsEtherErrStatsHistInstanceId'
_E='cucsEtherErrStatsInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-ETHER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsEquipmentChassisConfigState,CucsEquipmentXcvrType,CucsEtherCIoEpIfType,CucsEtherCloudType,CucsEtherErrStatsHistThresholded,CucsEtherErrStatsThresholded,CucsEtherExternalEpAdminState,CucsEtherExternalEpLocale,CucsEtherExternalPcAdminState,CucsEtherExternalPcLocale,CucsEtherFcoeInterfaceStatsHistThresholded,CucsEtherFcoeInterfaceStatsThresholded,CucsEtherIntFIoEpType,CucsEtherInternalPcLocale,CucsEtherLossStatsHistThresholded,CucsEtherLossStatsThresholded,CucsEtherNiErrStatsHistThresholded,CucsEtherNiErrStatsThresholded,CucsEtherPIoEpIfType,CucsEtherPIoFsmCurrentFsm,CucsEtherPIoFsmStageName,CucsEtherPauseStatsHistThresholded,CucsEtherPauseStatsThresholded,CucsEtherRxStatsHistThresholded,CucsEtherRxStatsThresholded,CucsEtherSatelliteConnectionDisc,CucsEtherServerIntFIoAdminState,CucsEtherServerIntFIoFsmCurrentFsm,CucsEtherServerIntFIoFsmStageName,CucsEtherServerIntFIoFsmTaskItem,CucsEtherServerIntFIoIfRole,CucsEtherServerIntFIoLocale,CucsEtherServerIntFIoPcEpIfRole,CucsEtherServerIntFIoPcEpPortId,CucsEtherServerIntFIoPcIfRole,CucsEtherServerIntFIoPcPortId,CucsEtherServerIntFIoPcTransport,CucsEtherServerIntFIoPcType,CucsEtherServerIntFIoTransport,CucsEtherServerIntFIoType,CucsEtherSwitchIntFIoAck,CucsEtherSwitchIntFIoIfRole,CucsEtherSwitchIntFIoLocale,CucsEtherSwitchIntFIoPcEpIfRole,CucsEtherSwitchIntFIoPcEpPortId,CucsEtherSwitchIntFIoPcIfRole,CucsEtherSwitchIntFIoPcMulticastHwHash,CucsEtherSwitchIntFIoPcPortId,CucsEtherSwitchIntFIoPcTransport,CucsEtherSwitchIntFIoPcType,CucsEtherSwitchIntFIoTransport,CucsEtherSwitchIntFIoType,CucsEtherTxStatsHistThresholded,CucsEtherTxStatsThresholded,CucsEtherUserRecoveryOperation,CucsFabricAdminState,CucsFabricMembershipStatus,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsFsmLifecycle,CucsLicenseState,CucsNetworkConnectionType,CucsNetworkLocale,CucsNetworkPhysEpIfType,CucsNetworkPortOperState,CucsNetworkPortRole,CucsNetworkSwitchId,CucsNetworkTransport,CucsPortEncap,CucsPortEthSpeed,CucsPortMode,CucsPortapiPeerCapability=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsEquipmentChassisConfigState','CucsEquipmentXcvrType','CucsEtherCIoEpIfType','CucsEtherCloudType','CucsEtherErrStatsHistThresholded','CucsEtherErrStatsThresholded','CucsEtherExternalEpAdminState','CucsEtherExternalEpLocale','CucsEtherExternalPcAdminState','CucsEtherExternalPcLocale','CucsEtherFcoeInterfaceStatsHistThresholded','CucsEtherFcoeInterfaceStatsThresholded','CucsEtherIntFIoEpType','CucsEtherInternalPcLocale','CucsEtherLossStatsHistThresholded','CucsEtherLossStatsThresholded','CucsEtherNiErrStatsHistThresholded','CucsEtherNiErrStatsThresholded','CucsEtherPIoEpIfType','CucsEtherPIoFsmCurrentFsm','CucsEtherPIoFsmStageName','CucsEtherPauseStatsHistThresholded','CucsEtherPauseStatsThresholded','CucsEtherRxStatsHistThresholded','CucsEtherRxStatsThresholded','CucsEtherSatelliteConnectionDisc','CucsEtherServerIntFIoAdminState','CucsEtherServerIntFIoFsmCurrentFsm','CucsEtherServerIntFIoFsmStageName','CucsEtherServerIntFIoFsmTaskItem','CucsEtherServerIntFIoIfRole','CucsEtherServerIntFIoLocale','CucsEtherServerIntFIoPcEpIfRole','CucsEtherServerIntFIoPcEpPortId','CucsEtherServerIntFIoPcIfRole','CucsEtherServerIntFIoPcPortId','CucsEtherServerIntFIoPcTransport','CucsEtherServerIntFIoPcType','CucsEtherServerIntFIoTransport','CucsEtherServerIntFIoType','CucsEtherSwitchIntFIoAck','CucsEtherSwitchIntFIoIfRole','CucsEtherSwitchIntFIoLocale','CucsEtherSwitchIntFIoPcEpIfRole','CucsEtherSwitchIntFIoPcEpPortId','CucsEtherSwitchIntFIoPcIfRole','CucsEtherSwitchIntFIoPcMulticastHwHash','CucsEtherSwitchIntFIoPcPortId','CucsEtherSwitchIntFIoPcTransport','CucsEtherSwitchIntFIoPcType','CucsEtherSwitchIntFIoTransport','CucsEtherSwitchIntFIoType','CucsEtherTxStatsHistThresholded','CucsEtherTxStatsThresholded','CucsEtherUserRecoveryOperation','CucsFabricAdminState','CucsFabricMembershipStatus','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsFsmLifecycle','CucsLicenseState','CucsNetworkConnectionType','CucsNetworkLocale','CucsNetworkPhysEpIfType','CucsNetworkPortOperState','CucsNetworkPortRole','CucsNetworkSwitchId','CucsNetworkTransport','CucsPortEncap','CucsPortEthSpeed','CucsPortMode','CucsPortapiPeerCapability')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsEtherObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,16))
_CucsEtherErrStatsTable_Object=MibTable
cucsEtherErrStatsTable=_CucsEtherErrStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,1))
if mibBuilder.loadTexts:cucsEtherErrStatsTable.setStatus(_A)
_CucsEtherErrStatsEntry_Object=MibTableRow
cucsEtherErrStatsEntry=_CucsEtherErrStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,1,1))
cucsEtherErrStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsEtherErrStatsEntry.setStatus(_A)
_CucsEtherErrStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherErrStatsInstanceId_Object=MibTableColumn
cucsEtherErrStatsInstanceId=_CucsEtherErrStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,1),_CucsEtherErrStatsInstanceId_Type())
cucsEtherErrStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherErrStatsInstanceId.setStatus(_A)
_CucsEtherErrStatsDn_Type=CucsManagedObjectDn
_CucsEtherErrStatsDn_Object=MibTableColumn
cucsEtherErrStatsDn=_CucsEtherErrStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,2),_CucsEtherErrStatsDn_Type())
cucsEtherErrStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsDn.setStatus(_A)
_CucsEtherErrStatsRn_Type=SnmpAdminString
_CucsEtherErrStatsRn_Object=MibTableColumn
cucsEtherErrStatsRn=_CucsEtherErrStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,3),_CucsEtherErrStatsRn_Type())
cucsEtherErrStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsRn.setStatus(_A)
_CucsEtherErrStatsAlign_Type=Unsigned64
_CucsEtherErrStatsAlign_Object=MibTableColumn
cucsEtherErrStatsAlign=_CucsEtherErrStatsAlign_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,4),_CucsEtherErrStatsAlign_Type())
cucsEtherErrStatsAlign.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsAlign.setStatus(_A)
_CucsEtherErrStatsAlignDelta_Type=Counter64
_CucsEtherErrStatsAlignDelta_Object=MibTableColumn
cucsEtherErrStatsAlignDelta=_CucsEtherErrStatsAlignDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,5),_CucsEtherErrStatsAlignDelta_Type())
cucsEtherErrStatsAlignDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsAlignDelta.setStatus(_A)
_CucsEtherErrStatsAlignDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsAlignDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsAlignDeltaAvg=_CucsEtherErrStatsAlignDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,6),_CucsEtherErrStatsAlignDeltaAvg_Type())
cucsEtherErrStatsAlignDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsAlignDeltaAvg.setStatus(_A)
_CucsEtherErrStatsAlignDeltaMax_Type=Unsigned64
_CucsEtherErrStatsAlignDeltaMax_Object=MibTableColumn
cucsEtherErrStatsAlignDeltaMax=_CucsEtherErrStatsAlignDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,7),_CucsEtherErrStatsAlignDeltaMax_Type())
cucsEtherErrStatsAlignDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsAlignDeltaMax.setStatus(_A)
_CucsEtherErrStatsAlignDeltaMin_Type=Unsigned64
_CucsEtherErrStatsAlignDeltaMin_Object=MibTableColumn
cucsEtherErrStatsAlignDeltaMin=_CucsEtherErrStatsAlignDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,8),_CucsEtherErrStatsAlignDeltaMin_Type())
cucsEtherErrStatsAlignDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsAlignDeltaMin.setStatus(_A)
_CucsEtherErrStatsDeferredTx_Type=Unsigned64
_CucsEtherErrStatsDeferredTx_Object=MibTableColumn
cucsEtherErrStatsDeferredTx=_CucsEtherErrStatsDeferredTx_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,9),_CucsEtherErrStatsDeferredTx_Type())
cucsEtherErrStatsDeferredTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsDeferredTx.setStatus(_A)
_CucsEtherErrStatsDeferredTxDelta_Type=Counter64
_CucsEtherErrStatsDeferredTxDelta_Object=MibTableColumn
cucsEtherErrStatsDeferredTxDelta=_CucsEtherErrStatsDeferredTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,10),_CucsEtherErrStatsDeferredTxDelta_Type())
cucsEtherErrStatsDeferredTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsDeferredTxDelta.setStatus(_A)
_CucsEtherErrStatsDeferredTxDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsDeferredTxDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsDeferredTxDeltaAvg=_CucsEtherErrStatsDeferredTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,11),_CucsEtherErrStatsDeferredTxDeltaAvg_Type())
cucsEtherErrStatsDeferredTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsDeferredTxDeltaAvg.setStatus(_A)
_CucsEtherErrStatsDeferredTxDeltaMax_Type=Unsigned64
_CucsEtherErrStatsDeferredTxDeltaMax_Object=MibTableColumn
cucsEtherErrStatsDeferredTxDeltaMax=_CucsEtherErrStatsDeferredTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,12),_CucsEtherErrStatsDeferredTxDeltaMax_Type())
cucsEtherErrStatsDeferredTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsDeferredTxDeltaMax.setStatus(_A)
_CucsEtherErrStatsDeferredTxDeltaMin_Type=Unsigned64
_CucsEtherErrStatsDeferredTxDeltaMin_Object=MibTableColumn
cucsEtherErrStatsDeferredTxDeltaMin=_CucsEtherErrStatsDeferredTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,13),_CucsEtherErrStatsDeferredTxDeltaMin_Type())
cucsEtherErrStatsDeferredTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsDeferredTxDeltaMin.setStatus(_A)
_CucsEtherErrStatsFcs_Type=Unsigned64
_CucsEtherErrStatsFcs_Object=MibTableColumn
cucsEtherErrStatsFcs=_CucsEtherErrStatsFcs_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,14),_CucsEtherErrStatsFcs_Type())
cucsEtherErrStatsFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsFcs.setStatus(_A)
_CucsEtherErrStatsFcsDelta_Type=Counter64
_CucsEtherErrStatsFcsDelta_Object=MibTableColumn
cucsEtherErrStatsFcsDelta=_CucsEtherErrStatsFcsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,15),_CucsEtherErrStatsFcsDelta_Type())
cucsEtherErrStatsFcsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsFcsDelta.setStatus(_A)
_CucsEtherErrStatsFcsDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsFcsDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsFcsDeltaAvg=_CucsEtherErrStatsFcsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,16),_CucsEtherErrStatsFcsDeltaAvg_Type())
cucsEtherErrStatsFcsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsFcsDeltaAvg.setStatus(_A)
_CucsEtherErrStatsFcsDeltaMax_Type=Unsigned64
_CucsEtherErrStatsFcsDeltaMax_Object=MibTableColumn
cucsEtherErrStatsFcsDeltaMax=_CucsEtherErrStatsFcsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,17),_CucsEtherErrStatsFcsDeltaMax_Type())
cucsEtherErrStatsFcsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsFcsDeltaMax.setStatus(_A)
_CucsEtherErrStatsFcsDeltaMin_Type=Unsigned64
_CucsEtherErrStatsFcsDeltaMin_Object=MibTableColumn
cucsEtherErrStatsFcsDeltaMin=_CucsEtherErrStatsFcsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,18),_CucsEtherErrStatsFcsDeltaMin_Type())
cucsEtherErrStatsFcsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsFcsDeltaMin.setStatus(_A)
_CucsEtherErrStatsIntMacRx_Type=Unsigned64
_CucsEtherErrStatsIntMacRx_Object=MibTableColumn
cucsEtherErrStatsIntMacRx=_CucsEtherErrStatsIntMacRx_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,19),_CucsEtherErrStatsIntMacRx_Type())
cucsEtherErrStatsIntMacRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacRx.setStatus(_A)
_CucsEtherErrStatsIntMacRxDelta_Type=Counter64
_CucsEtherErrStatsIntMacRxDelta_Object=MibTableColumn
cucsEtherErrStatsIntMacRxDelta=_CucsEtherErrStatsIntMacRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,20),_CucsEtherErrStatsIntMacRxDelta_Type())
cucsEtherErrStatsIntMacRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacRxDelta.setStatus(_A)
_CucsEtherErrStatsIntMacRxDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsIntMacRxDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsIntMacRxDeltaAvg=_CucsEtherErrStatsIntMacRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,21),_CucsEtherErrStatsIntMacRxDeltaAvg_Type())
cucsEtherErrStatsIntMacRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacRxDeltaAvg.setStatus(_A)
_CucsEtherErrStatsIntMacRxDeltaMax_Type=Unsigned64
_CucsEtherErrStatsIntMacRxDeltaMax_Object=MibTableColumn
cucsEtherErrStatsIntMacRxDeltaMax=_CucsEtherErrStatsIntMacRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,22),_CucsEtherErrStatsIntMacRxDeltaMax_Type())
cucsEtherErrStatsIntMacRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacRxDeltaMax.setStatus(_A)
_CucsEtherErrStatsIntMacRxDeltaMin_Type=Unsigned64
_CucsEtherErrStatsIntMacRxDeltaMin_Object=MibTableColumn
cucsEtherErrStatsIntMacRxDeltaMin=_CucsEtherErrStatsIntMacRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,23),_CucsEtherErrStatsIntMacRxDeltaMin_Type())
cucsEtherErrStatsIntMacRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacRxDeltaMin.setStatus(_A)
_CucsEtherErrStatsIntMacTx_Type=Unsigned64
_CucsEtherErrStatsIntMacTx_Object=MibTableColumn
cucsEtherErrStatsIntMacTx=_CucsEtherErrStatsIntMacTx_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,24),_CucsEtherErrStatsIntMacTx_Type())
cucsEtherErrStatsIntMacTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacTx.setStatus(_A)
_CucsEtherErrStatsIntMacTxDelta_Type=Counter64
_CucsEtherErrStatsIntMacTxDelta_Object=MibTableColumn
cucsEtherErrStatsIntMacTxDelta=_CucsEtherErrStatsIntMacTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,25),_CucsEtherErrStatsIntMacTxDelta_Type())
cucsEtherErrStatsIntMacTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacTxDelta.setStatus(_A)
_CucsEtherErrStatsIntMacTxDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsIntMacTxDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsIntMacTxDeltaAvg=_CucsEtherErrStatsIntMacTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,26),_CucsEtherErrStatsIntMacTxDeltaAvg_Type())
cucsEtherErrStatsIntMacTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacTxDeltaAvg.setStatus(_A)
_CucsEtherErrStatsIntMacTxDeltaMax_Type=Unsigned64
_CucsEtherErrStatsIntMacTxDeltaMax_Object=MibTableColumn
cucsEtherErrStatsIntMacTxDeltaMax=_CucsEtherErrStatsIntMacTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,27),_CucsEtherErrStatsIntMacTxDeltaMax_Type())
cucsEtherErrStatsIntMacTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacTxDeltaMax.setStatus(_A)
_CucsEtherErrStatsIntMacTxDeltaMin_Type=Unsigned64
_CucsEtherErrStatsIntMacTxDeltaMin_Object=MibTableColumn
cucsEtherErrStatsIntMacTxDeltaMin=_CucsEtherErrStatsIntMacTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,28),_CucsEtherErrStatsIntMacTxDeltaMin_Type())
cucsEtherErrStatsIntMacTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntMacTxDeltaMin.setStatus(_A)
_CucsEtherErrStatsIntervals_Type=Gauge32
_CucsEtherErrStatsIntervals_Object=MibTableColumn
cucsEtherErrStatsIntervals=_CucsEtherErrStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,29),_CucsEtherErrStatsIntervals_Type())
cucsEtherErrStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsIntervals.setStatus(_A)
_CucsEtherErrStatsOutDiscard_Type=Unsigned64
_CucsEtherErrStatsOutDiscard_Object=MibTableColumn
cucsEtherErrStatsOutDiscard=_CucsEtherErrStatsOutDiscard_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,30),_CucsEtherErrStatsOutDiscard_Type())
cucsEtherErrStatsOutDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsOutDiscard.setStatus(_A)
_CucsEtherErrStatsOutDiscardDelta_Type=Counter64
_CucsEtherErrStatsOutDiscardDelta_Object=MibTableColumn
cucsEtherErrStatsOutDiscardDelta=_CucsEtherErrStatsOutDiscardDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,31),_CucsEtherErrStatsOutDiscardDelta_Type())
cucsEtherErrStatsOutDiscardDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsOutDiscardDelta.setStatus(_A)
_CucsEtherErrStatsOutDiscardDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsOutDiscardDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsOutDiscardDeltaAvg=_CucsEtherErrStatsOutDiscardDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,32),_CucsEtherErrStatsOutDiscardDeltaAvg_Type())
cucsEtherErrStatsOutDiscardDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsOutDiscardDeltaAvg.setStatus(_A)
_CucsEtherErrStatsOutDiscardDeltaMax_Type=Unsigned64
_CucsEtherErrStatsOutDiscardDeltaMax_Object=MibTableColumn
cucsEtherErrStatsOutDiscardDeltaMax=_CucsEtherErrStatsOutDiscardDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,33),_CucsEtherErrStatsOutDiscardDeltaMax_Type())
cucsEtherErrStatsOutDiscardDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsOutDiscardDeltaMax.setStatus(_A)
_CucsEtherErrStatsOutDiscardDeltaMin_Type=Unsigned64
_CucsEtherErrStatsOutDiscardDeltaMin_Object=MibTableColumn
cucsEtherErrStatsOutDiscardDeltaMin=_CucsEtherErrStatsOutDiscardDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,34),_CucsEtherErrStatsOutDiscardDeltaMin_Type())
cucsEtherErrStatsOutDiscardDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsOutDiscardDeltaMin.setStatus(_A)
_CucsEtherErrStatsRcv_Type=Unsigned64
_CucsEtherErrStatsRcv_Object=MibTableColumn
cucsEtherErrStatsRcv=_CucsEtherErrStatsRcv_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,35),_CucsEtherErrStatsRcv_Type())
cucsEtherErrStatsRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsRcv.setStatus(_A)
_CucsEtherErrStatsRcvDelta_Type=Counter64
_CucsEtherErrStatsRcvDelta_Object=MibTableColumn
cucsEtherErrStatsRcvDelta=_CucsEtherErrStatsRcvDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,36),_CucsEtherErrStatsRcvDelta_Type())
cucsEtherErrStatsRcvDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsRcvDelta.setStatus(_A)
_CucsEtherErrStatsRcvDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsRcvDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsRcvDeltaAvg=_CucsEtherErrStatsRcvDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,37),_CucsEtherErrStatsRcvDeltaAvg_Type())
cucsEtherErrStatsRcvDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsRcvDeltaAvg.setStatus(_A)
_CucsEtherErrStatsRcvDeltaMax_Type=Unsigned64
_CucsEtherErrStatsRcvDeltaMax_Object=MibTableColumn
cucsEtherErrStatsRcvDeltaMax=_CucsEtherErrStatsRcvDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,38),_CucsEtherErrStatsRcvDeltaMax_Type())
cucsEtherErrStatsRcvDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsRcvDeltaMax.setStatus(_A)
_CucsEtherErrStatsRcvDeltaMin_Type=Unsigned64
_CucsEtherErrStatsRcvDeltaMin_Object=MibTableColumn
cucsEtherErrStatsRcvDeltaMin=_CucsEtherErrStatsRcvDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,39),_CucsEtherErrStatsRcvDeltaMin_Type())
cucsEtherErrStatsRcvDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsRcvDeltaMin.setStatus(_A)
_CucsEtherErrStatsSuspect_Type=TruthValue
_CucsEtherErrStatsSuspect_Object=MibTableColumn
cucsEtherErrStatsSuspect=_CucsEtherErrStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,40),_CucsEtherErrStatsSuspect_Type())
cucsEtherErrStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsSuspect.setStatus(_A)
_CucsEtherErrStatsThresholded_Type=CucsEtherErrStatsThresholded
_CucsEtherErrStatsThresholded_Object=MibTableColumn
cucsEtherErrStatsThresholded=_CucsEtherErrStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,41),_CucsEtherErrStatsThresholded_Type())
cucsEtherErrStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsThresholded.setStatus(_A)
_CucsEtherErrStatsTimeCollected_Type=DateAndTime
_CucsEtherErrStatsTimeCollected_Object=MibTableColumn
cucsEtherErrStatsTimeCollected=_CucsEtherErrStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,42),_CucsEtherErrStatsTimeCollected_Type())
cucsEtherErrStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsTimeCollected.setStatus(_A)
_CucsEtherErrStatsUnderSize_Type=Unsigned64
_CucsEtherErrStatsUnderSize_Object=MibTableColumn
cucsEtherErrStatsUnderSize=_CucsEtherErrStatsUnderSize_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,43),_CucsEtherErrStatsUnderSize_Type())
cucsEtherErrStatsUnderSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsUnderSize.setStatus(_A)
_CucsEtherErrStatsUnderSizeDelta_Type=Counter64
_CucsEtherErrStatsUnderSizeDelta_Object=MibTableColumn
cucsEtherErrStatsUnderSizeDelta=_CucsEtherErrStatsUnderSizeDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,44),_CucsEtherErrStatsUnderSizeDelta_Type())
cucsEtherErrStatsUnderSizeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsUnderSizeDelta.setStatus(_A)
_CucsEtherErrStatsUnderSizeDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsUnderSizeDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsUnderSizeDeltaAvg=_CucsEtherErrStatsUnderSizeDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,45),_CucsEtherErrStatsUnderSizeDeltaAvg_Type())
cucsEtherErrStatsUnderSizeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsUnderSizeDeltaAvg.setStatus(_A)
_CucsEtherErrStatsUnderSizeDeltaMax_Type=Unsigned64
_CucsEtherErrStatsUnderSizeDeltaMax_Object=MibTableColumn
cucsEtherErrStatsUnderSizeDeltaMax=_CucsEtherErrStatsUnderSizeDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,46),_CucsEtherErrStatsUnderSizeDeltaMax_Type())
cucsEtherErrStatsUnderSizeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsUnderSizeDeltaMax.setStatus(_A)
_CucsEtherErrStatsUnderSizeDeltaMin_Type=Unsigned64
_CucsEtherErrStatsUnderSizeDeltaMin_Object=MibTableColumn
cucsEtherErrStatsUnderSizeDeltaMin=_CucsEtherErrStatsUnderSizeDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,47),_CucsEtherErrStatsUnderSizeDeltaMin_Type())
cucsEtherErrStatsUnderSizeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsUnderSizeDeltaMin.setStatus(_A)
_CucsEtherErrStatsUpdate_Type=Gauge32
_CucsEtherErrStatsUpdate_Object=MibTableColumn
cucsEtherErrStatsUpdate=_CucsEtherErrStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,48),_CucsEtherErrStatsUpdate_Type())
cucsEtherErrStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsUpdate.setStatus(_A)
_CucsEtherErrStatsXmit_Type=Unsigned64
_CucsEtherErrStatsXmit_Object=MibTableColumn
cucsEtherErrStatsXmit=_CucsEtherErrStatsXmit_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,49),_CucsEtherErrStatsXmit_Type())
cucsEtherErrStatsXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsXmit.setStatus(_A)
_CucsEtherErrStatsXmitDelta_Type=Counter64
_CucsEtherErrStatsXmitDelta_Object=MibTableColumn
cucsEtherErrStatsXmitDelta=_CucsEtherErrStatsXmitDelta_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,50),_CucsEtherErrStatsXmitDelta_Type())
cucsEtherErrStatsXmitDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsXmitDelta.setStatus(_A)
_CucsEtherErrStatsXmitDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsXmitDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsXmitDeltaAvg=_CucsEtherErrStatsXmitDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,51),_CucsEtherErrStatsXmitDeltaAvg_Type())
cucsEtherErrStatsXmitDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsXmitDeltaAvg.setStatus(_A)
_CucsEtherErrStatsXmitDeltaMax_Type=Unsigned64
_CucsEtherErrStatsXmitDeltaMax_Object=MibTableColumn
cucsEtherErrStatsXmitDeltaMax=_CucsEtherErrStatsXmitDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,52),_CucsEtherErrStatsXmitDeltaMax_Type())
cucsEtherErrStatsXmitDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsXmitDeltaMax.setStatus(_A)
_CucsEtherErrStatsXmitDeltaMin_Type=Unsigned64
_CucsEtherErrStatsXmitDeltaMin_Object=MibTableColumn
cucsEtherErrStatsXmitDeltaMin=_CucsEtherErrStatsXmitDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,1,1,53),_CucsEtherErrStatsXmitDeltaMin_Type())
cucsEtherErrStatsXmitDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsXmitDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistTable_Object=MibTable
cucsEtherErrStatsHistTable=_CucsEtherErrStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,2))
if mibBuilder.loadTexts:cucsEtherErrStatsHistTable.setStatus(_A)
_CucsEtherErrStatsHistEntry_Object=MibTableRow
cucsEtherErrStatsHistEntry=_CucsEtherErrStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,2,1))
cucsEtherErrStatsHistEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsEtherErrStatsHistEntry.setStatus(_A)
_CucsEtherErrStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherErrStatsHistInstanceId_Object=MibTableColumn
cucsEtherErrStatsHistInstanceId=_CucsEtherErrStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,1),_CucsEtherErrStatsHistInstanceId_Type())
cucsEtherErrStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherErrStatsHistInstanceId.setStatus(_A)
_CucsEtherErrStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherErrStatsHistDn_Object=MibTableColumn
cucsEtherErrStatsHistDn=_CucsEtherErrStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,2),_CucsEtherErrStatsHistDn_Type())
cucsEtherErrStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistDn.setStatus(_A)
_CucsEtherErrStatsHistRn_Type=SnmpAdminString
_CucsEtherErrStatsHistRn_Object=MibTableColumn
cucsEtherErrStatsHistRn=_CucsEtherErrStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,3),_CucsEtherErrStatsHistRn_Type())
cucsEtherErrStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistRn.setStatus(_A)
_CucsEtherErrStatsHistAlign_Type=Unsigned64
_CucsEtherErrStatsHistAlign_Object=MibTableColumn
cucsEtherErrStatsHistAlign=_CucsEtherErrStatsHistAlign_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,4),_CucsEtherErrStatsHistAlign_Type())
cucsEtherErrStatsHistAlign.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistAlign.setStatus(_A)
_CucsEtherErrStatsHistAlignDelta_Type=Unsigned64
_CucsEtherErrStatsHistAlignDelta_Object=MibTableColumn
cucsEtherErrStatsHistAlignDelta=_CucsEtherErrStatsHistAlignDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,5),_CucsEtherErrStatsHistAlignDelta_Type())
cucsEtherErrStatsHistAlignDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistAlignDelta.setStatus(_A)
_CucsEtherErrStatsHistAlignDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistAlignDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistAlignDeltaAvg=_CucsEtherErrStatsHistAlignDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,6),_CucsEtherErrStatsHistAlignDeltaAvg_Type())
cucsEtherErrStatsHistAlignDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistAlignDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistAlignDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistAlignDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistAlignDeltaMax=_CucsEtherErrStatsHistAlignDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,7),_CucsEtherErrStatsHistAlignDeltaMax_Type())
cucsEtherErrStatsHistAlignDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistAlignDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistAlignDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistAlignDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistAlignDeltaMin=_CucsEtherErrStatsHistAlignDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,8),_CucsEtherErrStatsHistAlignDeltaMin_Type())
cucsEtherErrStatsHistAlignDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistAlignDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistDeferredTx_Type=Unsigned64
_CucsEtherErrStatsHistDeferredTx_Object=MibTableColumn
cucsEtherErrStatsHistDeferredTx=_CucsEtherErrStatsHistDeferredTx_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,9),_CucsEtherErrStatsHistDeferredTx_Type())
cucsEtherErrStatsHistDeferredTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistDeferredTx.setStatus(_A)
_CucsEtherErrStatsHistDeferredTxDelta_Type=Unsigned64
_CucsEtherErrStatsHistDeferredTxDelta_Object=MibTableColumn
cucsEtherErrStatsHistDeferredTxDelta=_CucsEtherErrStatsHistDeferredTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,10),_CucsEtherErrStatsHistDeferredTxDelta_Type())
cucsEtherErrStatsHistDeferredTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistDeferredTxDelta.setStatus(_A)
_CucsEtherErrStatsHistDeferredTxDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistDeferredTxDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistDeferredTxDeltaAvg=_CucsEtherErrStatsHistDeferredTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,11),_CucsEtherErrStatsHistDeferredTxDeltaAvg_Type())
cucsEtherErrStatsHistDeferredTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistDeferredTxDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistDeferredTxDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistDeferredTxDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistDeferredTxDeltaMax=_CucsEtherErrStatsHistDeferredTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,12),_CucsEtherErrStatsHistDeferredTxDeltaMax_Type())
cucsEtherErrStatsHistDeferredTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistDeferredTxDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistDeferredTxDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistDeferredTxDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistDeferredTxDeltaMin=_CucsEtherErrStatsHistDeferredTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,13),_CucsEtherErrStatsHistDeferredTxDeltaMin_Type())
cucsEtherErrStatsHistDeferredTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistDeferredTxDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistFcs_Type=Unsigned64
_CucsEtherErrStatsHistFcs_Object=MibTableColumn
cucsEtherErrStatsHistFcs=_CucsEtherErrStatsHistFcs_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,14),_CucsEtherErrStatsHistFcs_Type())
cucsEtherErrStatsHistFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistFcs.setStatus(_A)
_CucsEtherErrStatsHistFcsDelta_Type=Unsigned64
_CucsEtherErrStatsHistFcsDelta_Object=MibTableColumn
cucsEtherErrStatsHistFcsDelta=_CucsEtherErrStatsHistFcsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,15),_CucsEtherErrStatsHistFcsDelta_Type())
cucsEtherErrStatsHistFcsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistFcsDelta.setStatus(_A)
_CucsEtherErrStatsHistFcsDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistFcsDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistFcsDeltaAvg=_CucsEtherErrStatsHistFcsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,16),_CucsEtherErrStatsHistFcsDeltaAvg_Type())
cucsEtherErrStatsHistFcsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistFcsDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistFcsDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistFcsDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistFcsDeltaMax=_CucsEtherErrStatsHistFcsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,17),_CucsEtherErrStatsHistFcsDeltaMax_Type())
cucsEtherErrStatsHistFcsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistFcsDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistFcsDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistFcsDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistFcsDeltaMin=_CucsEtherErrStatsHistFcsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,18),_CucsEtherErrStatsHistFcsDeltaMin_Type())
cucsEtherErrStatsHistFcsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistFcsDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistId_Type=Unsigned64
_CucsEtherErrStatsHistId_Object=MibTableColumn
cucsEtherErrStatsHistId=_CucsEtherErrStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,19),_CucsEtherErrStatsHistId_Type())
cucsEtherErrStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistId.setStatus(_A)
_CucsEtherErrStatsHistIntMacRx_Type=Unsigned64
_CucsEtherErrStatsHistIntMacRx_Object=MibTableColumn
cucsEtherErrStatsHistIntMacRx=_CucsEtherErrStatsHistIntMacRx_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,20),_CucsEtherErrStatsHistIntMacRx_Type())
cucsEtherErrStatsHistIntMacRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacRx.setStatus(_A)
_CucsEtherErrStatsHistIntMacRxDelta_Type=Unsigned64
_CucsEtherErrStatsHistIntMacRxDelta_Object=MibTableColumn
cucsEtherErrStatsHistIntMacRxDelta=_CucsEtherErrStatsHistIntMacRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,21),_CucsEtherErrStatsHistIntMacRxDelta_Type())
cucsEtherErrStatsHistIntMacRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacRxDelta.setStatus(_A)
_CucsEtherErrStatsHistIntMacRxDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistIntMacRxDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistIntMacRxDeltaAvg=_CucsEtherErrStatsHistIntMacRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,22),_CucsEtherErrStatsHistIntMacRxDeltaAvg_Type())
cucsEtherErrStatsHistIntMacRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacRxDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistIntMacRxDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistIntMacRxDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistIntMacRxDeltaMax=_CucsEtherErrStatsHistIntMacRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,23),_CucsEtherErrStatsHistIntMacRxDeltaMax_Type())
cucsEtherErrStatsHistIntMacRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacRxDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistIntMacRxDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistIntMacRxDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistIntMacRxDeltaMin=_CucsEtherErrStatsHistIntMacRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,24),_CucsEtherErrStatsHistIntMacRxDeltaMin_Type())
cucsEtherErrStatsHistIntMacRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacRxDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistIntMacTx_Type=Unsigned64
_CucsEtherErrStatsHistIntMacTx_Object=MibTableColumn
cucsEtherErrStatsHistIntMacTx=_CucsEtherErrStatsHistIntMacTx_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,25),_CucsEtherErrStatsHistIntMacTx_Type())
cucsEtherErrStatsHistIntMacTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacTx.setStatus(_A)
_CucsEtherErrStatsHistIntMacTxDelta_Type=Unsigned64
_CucsEtherErrStatsHistIntMacTxDelta_Object=MibTableColumn
cucsEtherErrStatsHistIntMacTxDelta=_CucsEtherErrStatsHistIntMacTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,26),_CucsEtherErrStatsHistIntMacTxDelta_Type())
cucsEtherErrStatsHistIntMacTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacTxDelta.setStatus(_A)
_CucsEtherErrStatsHistIntMacTxDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistIntMacTxDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistIntMacTxDeltaAvg=_CucsEtherErrStatsHistIntMacTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,27),_CucsEtherErrStatsHistIntMacTxDeltaAvg_Type())
cucsEtherErrStatsHistIntMacTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacTxDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistIntMacTxDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistIntMacTxDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistIntMacTxDeltaMax=_CucsEtherErrStatsHistIntMacTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,28),_CucsEtherErrStatsHistIntMacTxDeltaMax_Type())
cucsEtherErrStatsHistIntMacTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacTxDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistIntMacTxDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistIntMacTxDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistIntMacTxDeltaMin=_CucsEtherErrStatsHistIntMacTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,29),_CucsEtherErrStatsHistIntMacTxDeltaMin_Type())
cucsEtherErrStatsHistIntMacTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistIntMacTxDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistMostRecent_Type=TruthValue
_CucsEtherErrStatsHistMostRecent_Object=MibTableColumn
cucsEtherErrStatsHistMostRecent=_CucsEtherErrStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,30),_CucsEtherErrStatsHistMostRecent_Type())
cucsEtherErrStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistMostRecent.setStatus(_A)
_CucsEtherErrStatsHistOutDiscard_Type=Unsigned64
_CucsEtherErrStatsHistOutDiscard_Object=MibTableColumn
cucsEtherErrStatsHistOutDiscard=_CucsEtherErrStatsHistOutDiscard_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,31),_CucsEtherErrStatsHistOutDiscard_Type())
cucsEtherErrStatsHistOutDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistOutDiscard.setStatus(_A)
_CucsEtherErrStatsHistOutDiscardDelta_Type=Unsigned64
_CucsEtherErrStatsHistOutDiscardDelta_Object=MibTableColumn
cucsEtherErrStatsHistOutDiscardDelta=_CucsEtherErrStatsHistOutDiscardDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,32),_CucsEtherErrStatsHistOutDiscardDelta_Type())
cucsEtherErrStatsHistOutDiscardDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistOutDiscardDelta.setStatus(_A)
_CucsEtherErrStatsHistOutDiscardDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistOutDiscardDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistOutDiscardDeltaAvg=_CucsEtherErrStatsHistOutDiscardDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,33),_CucsEtherErrStatsHistOutDiscardDeltaAvg_Type())
cucsEtherErrStatsHistOutDiscardDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistOutDiscardDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistOutDiscardDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistOutDiscardDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistOutDiscardDeltaMax=_CucsEtherErrStatsHistOutDiscardDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,34),_CucsEtherErrStatsHistOutDiscardDeltaMax_Type())
cucsEtherErrStatsHistOutDiscardDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistOutDiscardDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistOutDiscardDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistOutDiscardDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistOutDiscardDeltaMin=_CucsEtherErrStatsHistOutDiscardDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,35),_CucsEtherErrStatsHistOutDiscardDeltaMin_Type())
cucsEtherErrStatsHistOutDiscardDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistOutDiscardDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistRcv_Type=Unsigned64
_CucsEtherErrStatsHistRcv_Object=MibTableColumn
cucsEtherErrStatsHistRcv=_CucsEtherErrStatsHistRcv_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,36),_CucsEtherErrStatsHistRcv_Type())
cucsEtherErrStatsHistRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistRcv.setStatus(_A)
_CucsEtherErrStatsHistRcvDelta_Type=Unsigned64
_CucsEtherErrStatsHistRcvDelta_Object=MibTableColumn
cucsEtherErrStatsHistRcvDelta=_CucsEtherErrStatsHistRcvDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,37),_CucsEtherErrStatsHistRcvDelta_Type())
cucsEtherErrStatsHistRcvDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistRcvDelta.setStatus(_A)
_CucsEtherErrStatsHistRcvDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistRcvDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistRcvDeltaAvg=_CucsEtherErrStatsHistRcvDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,38),_CucsEtherErrStatsHistRcvDeltaAvg_Type())
cucsEtherErrStatsHistRcvDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistRcvDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistRcvDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistRcvDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistRcvDeltaMax=_CucsEtherErrStatsHistRcvDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,39),_CucsEtherErrStatsHistRcvDeltaMax_Type())
cucsEtherErrStatsHistRcvDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistRcvDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistRcvDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistRcvDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistRcvDeltaMin=_CucsEtherErrStatsHistRcvDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,40),_CucsEtherErrStatsHistRcvDeltaMin_Type())
cucsEtherErrStatsHistRcvDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistRcvDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistSuspect_Type=TruthValue
_CucsEtherErrStatsHistSuspect_Object=MibTableColumn
cucsEtherErrStatsHistSuspect=_CucsEtherErrStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,41),_CucsEtherErrStatsHistSuspect_Type())
cucsEtherErrStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistSuspect.setStatus(_A)
_CucsEtherErrStatsHistThresholded_Type=CucsEtherErrStatsHistThresholded
_CucsEtherErrStatsHistThresholded_Object=MibTableColumn
cucsEtherErrStatsHistThresholded=_CucsEtherErrStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,42),_CucsEtherErrStatsHistThresholded_Type())
cucsEtherErrStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistThresholded.setStatus(_A)
_CucsEtherErrStatsHistTimeCollected_Type=DateAndTime
_CucsEtherErrStatsHistTimeCollected_Object=MibTableColumn
cucsEtherErrStatsHistTimeCollected=_CucsEtherErrStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,43),_CucsEtherErrStatsHistTimeCollected_Type())
cucsEtherErrStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistTimeCollected.setStatus(_A)
_CucsEtherErrStatsHistUnderSize_Type=Unsigned64
_CucsEtherErrStatsHistUnderSize_Object=MibTableColumn
cucsEtherErrStatsHistUnderSize=_CucsEtherErrStatsHistUnderSize_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,44),_CucsEtherErrStatsHistUnderSize_Type())
cucsEtherErrStatsHistUnderSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistUnderSize.setStatus(_A)
_CucsEtherErrStatsHistUnderSizeDelta_Type=Unsigned64
_CucsEtherErrStatsHistUnderSizeDelta_Object=MibTableColumn
cucsEtherErrStatsHistUnderSizeDelta=_CucsEtherErrStatsHistUnderSizeDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,45),_CucsEtherErrStatsHistUnderSizeDelta_Type())
cucsEtherErrStatsHistUnderSizeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistUnderSizeDelta.setStatus(_A)
_CucsEtherErrStatsHistUnderSizeDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistUnderSizeDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistUnderSizeDeltaAvg=_CucsEtherErrStatsHistUnderSizeDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,46),_CucsEtherErrStatsHistUnderSizeDeltaAvg_Type())
cucsEtherErrStatsHistUnderSizeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistUnderSizeDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistUnderSizeDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistUnderSizeDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistUnderSizeDeltaMax=_CucsEtherErrStatsHistUnderSizeDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,47),_CucsEtherErrStatsHistUnderSizeDeltaMax_Type())
cucsEtherErrStatsHistUnderSizeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistUnderSizeDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistUnderSizeDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistUnderSizeDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistUnderSizeDeltaMin=_CucsEtherErrStatsHistUnderSizeDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,48),_CucsEtherErrStatsHistUnderSizeDeltaMin_Type())
cucsEtherErrStatsHistUnderSizeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistUnderSizeDeltaMin.setStatus(_A)
_CucsEtherErrStatsHistXmit_Type=Unsigned64
_CucsEtherErrStatsHistXmit_Object=MibTableColumn
cucsEtherErrStatsHistXmit=_CucsEtherErrStatsHistXmit_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,49),_CucsEtherErrStatsHistXmit_Type())
cucsEtherErrStatsHistXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistXmit.setStatus(_A)
_CucsEtherErrStatsHistXmitDelta_Type=Unsigned64
_CucsEtherErrStatsHistXmitDelta_Object=MibTableColumn
cucsEtherErrStatsHistXmitDelta=_CucsEtherErrStatsHistXmitDelta_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,50),_CucsEtherErrStatsHistXmitDelta_Type())
cucsEtherErrStatsHistXmitDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistXmitDelta.setStatus(_A)
_CucsEtherErrStatsHistXmitDeltaAvg_Type=Unsigned64
_CucsEtherErrStatsHistXmitDeltaAvg_Object=MibTableColumn
cucsEtherErrStatsHistXmitDeltaAvg=_CucsEtherErrStatsHistXmitDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,51),_CucsEtherErrStatsHistXmitDeltaAvg_Type())
cucsEtherErrStatsHistXmitDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistXmitDeltaAvg.setStatus(_A)
_CucsEtherErrStatsHistXmitDeltaMax_Type=Unsigned64
_CucsEtherErrStatsHistXmitDeltaMax_Object=MibTableColumn
cucsEtherErrStatsHistXmitDeltaMax=_CucsEtherErrStatsHistXmitDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,52),_CucsEtherErrStatsHistXmitDeltaMax_Type())
cucsEtherErrStatsHistXmitDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistXmitDeltaMax.setStatus(_A)
_CucsEtherErrStatsHistXmitDeltaMin_Type=Unsigned64
_CucsEtherErrStatsHistXmitDeltaMin_Object=MibTableColumn
cucsEtherErrStatsHistXmitDeltaMin=_CucsEtherErrStatsHistXmitDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,2,1,53),_CucsEtherErrStatsHistXmitDeltaMin_Type())
cucsEtherErrStatsHistXmitDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherErrStatsHistXmitDeltaMin.setStatus(_A)
_CucsEtherLossStatsTable_Object=MibTable
cucsEtherLossStatsTable=_CucsEtherLossStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,3))
if mibBuilder.loadTexts:cucsEtherLossStatsTable.setStatus(_A)
_CucsEtherLossStatsEntry_Object=MibTableRow
cucsEtherLossStatsEntry=_CucsEtherLossStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,3,1))
cucsEtherLossStatsEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsEtherLossStatsEntry.setStatus(_A)
_CucsEtherLossStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherLossStatsInstanceId_Object=MibTableColumn
cucsEtherLossStatsInstanceId=_CucsEtherLossStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,1),_CucsEtherLossStatsInstanceId_Type())
cucsEtherLossStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherLossStatsInstanceId.setStatus(_A)
_CucsEtherLossStatsDn_Type=CucsManagedObjectDn
_CucsEtherLossStatsDn_Object=MibTableColumn
cucsEtherLossStatsDn=_CucsEtherLossStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,2),_CucsEtherLossStatsDn_Type())
cucsEtherLossStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsDn.setStatus(_A)
_CucsEtherLossStatsRn_Type=SnmpAdminString
_CucsEtherLossStatsRn_Object=MibTableColumn
cucsEtherLossStatsRn=_CucsEtherLossStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,3),_CucsEtherLossStatsRn_Type())
cucsEtherLossStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsRn.setStatus(_A)
_CucsEtherLossStatsSQETest_Type=Unsigned64
_CucsEtherLossStatsSQETest_Object=MibTableColumn
cucsEtherLossStatsSQETest=_CucsEtherLossStatsSQETest_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,4),_CucsEtherLossStatsSQETest_Type())
cucsEtherLossStatsSQETest.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSQETest.setStatus(_A)
_CucsEtherLossStatsSQETestDelta_Type=Counter64
_CucsEtherLossStatsSQETestDelta_Object=MibTableColumn
cucsEtherLossStatsSQETestDelta=_CucsEtherLossStatsSQETestDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,5),_CucsEtherLossStatsSQETestDelta_Type())
cucsEtherLossStatsSQETestDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSQETestDelta.setStatus(_A)
_CucsEtherLossStatsSQETestDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsSQETestDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsSQETestDeltaAvg=_CucsEtherLossStatsSQETestDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,6),_CucsEtherLossStatsSQETestDeltaAvg_Type())
cucsEtherLossStatsSQETestDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSQETestDeltaAvg.setStatus(_A)
_CucsEtherLossStatsSQETestDeltaMax_Type=Unsigned64
_CucsEtherLossStatsSQETestDeltaMax_Object=MibTableColumn
cucsEtherLossStatsSQETestDeltaMax=_CucsEtherLossStatsSQETestDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,7),_CucsEtherLossStatsSQETestDeltaMax_Type())
cucsEtherLossStatsSQETestDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSQETestDeltaMax.setStatus(_A)
_CucsEtherLossStatsSQETestDeltaMin_Type=Unsigned64
_CucsEtherLossStatsSQETestDeltaMin_Object=MibTableColumn
cucsEtherLossStatsSQETestDeltaMin=_CucsEtherLossStatsSQETestDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,8),_CucsEtherLossStatsSQETestDeltaMin_Type())
cucsEtherLossStatsSQETestDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSQETestDeltaMin.setStatus(_A)
_CucsEtherLossStatsCarrierSense_Type=Unsigned64
_CucsEtherLossStatsCarrierSense_Object=MibTableColumn
cucsEtherLossStatsCarrierSense=_CucsEtherLossStatsCarrierSense_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,9),_CucsEtherLossStatsCarrierSense_Type())
cucsEtherLossStatsCarrierSense.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsCarrierSense.setStatus(_A)
_CucsEtherLossStatsCarrierSenseDelta_Type=Counter64
_CucsEtherLossStatsCarrierSenseDelta_Object=MibTableColumn
cucsEtherLossStatsCarrierSenseDelta=_CucsEtherLossStatsCarrierSenseDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,10),_CucsEtherLossStatsCarrierSenseDelta_Type())
cucsEtherLossStatsCarrierSenseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsCarrierSenseDelta.setStatus(_A)
_CucsEtherLossStatsCarrierSenseDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsCarrierSenseDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsCarrierSenseDeltaAvg=_CucsEtherLossStatsCarrierSenseDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,11),_CucsEtherLossStatsCarrierSenseDeltaAvg_Type())
cucsEtherLossStatsCarrierSenseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsCarrierSenseDeltaAvg.setStatus(_A)
_CucsEtherLossStatsCarrierSenseDeltaMax_Type=Unsigned64
_CucsEtherLossStatsCarrierSenseDeltaMax_Object=MibTableColumn
cucsEtherLossStatsCarrierSenseDeltaMax=_CucsEtherLossStatsCarrierSenseDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,12),_CucsEtherLossStatsCarrierSenseDeltaMax_Type())
cucsEtherLossStatsCarrierSenseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsCarrierSenseDeltaMax.setStatus(_A)
_CucsEtherLossStatsCarrierSenseDeltaMin_Type=Unsigned64
_CucsEtherLossStatsCarrierSenseDeltaMin_Object=MibTableColumn
cucsEtherLossStatsCarrierSenseDeltaMin=_CucsEtherLossStatsCarrierSenseDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,13),_CucsEtherLossStatsCarrierSenseDeltaMin_Type())
cucsEtherLossStatsCarrierSenseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsCarrierSenseDeltaMin.setStatus(_A)
_CucsEtherLossStatsExcessCollision_Type=Unsigned64
_CucsEtherLossStatsExcessCollision_Object=MibTableColumn
cucsEtherLossStatsExcessCollision=_CucsEtherLossStatsExcessCollision_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,14),_CucsEtherLossStatsExcessCollision_Type())
cucsEtherLossStatsExcessCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsExcessCollision.setStatus(_A)
_CucsEtherLossStatsExcessCollisionDelta_Type=Counter64
_CucsEtherLossStatsExcessCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsExcessCollisionDelta=_CucsEtherLossStatsExcessCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,15),_CucsEtherLossStatsExcessCollisionDelta_Type())
cucsEtherLossStatsExcessCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsExcessCollisionDelta.setStatus(_A)
_CucsEtherLossStatsExcessCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsExcessCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsExcessCollisionDeltaAvg=_CucsEtherLossStatsExcessCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,16),_CucsEtherLossStatsExcessCollisionDeltaAvg_Type())
cucsEtherLossStatsExcessCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsExcessCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsExcessCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsExcessCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsExcessCollisionDeltaMax=_CucsEtherLossStatsExcessCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,17),_CucsEtherLossStatsExcessCollisionDeltaMax_Type())
cucsEtherLossStatsExcessCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsExcessCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsExcessCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsExcessCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsExcessCollisionDeltaMin=_CucsEtherLossStatsExcessCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,18),_CucsEtherLossStatsExcessCollisionDeltaMin_Type())
cucsEtherLossStatsExcessCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsExcessCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsGiants_Type=Unsigned64
_CucsEtherLossStatsGiants_Object=MibTableColumn
cucsEtherLossStatsGiants=_CucsEtherLossStatsGiants_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,19),_CucsEtherLossStatsGiants_Type())
cucsEtherLossStatsGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsGiants.setStatus(_A)
_CucsEtherLossStatsGiantsDelta_Type=Counter64
_CucsEtherLossStatsGiantsDelta_Object=MibTableColumn
cucsEtherLossStatsGiantsDelta=_CucsEtherLossStatsGiantsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,20),_CucsEtherLossStatsGiantsDelta_Type())
cucsEtherLossStatsGiantsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsGiantsDelta.setStatus(_A)
_CucsEtherLossStatsGiantsDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsGiantsDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsGiantsDeltaAvg=_CucsEtherLossStatsGiantsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,21),_CucsEtherLossStatsGiantsDeltaAvg_Type())
cucsEtherLossStatsGiantsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsGiantsDeltaAvg.setStatus(_A)
_CucsEtherLossStatsGiantsDeltaMax_Type=Unsigned64
_CucsEtherLossStatsGiantsDeltaMax_Object=MibTableColumn
cucsEtherLossStatsGiantsDeltaMax=_CucsEtherLossStatsGiantsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,22),_CucsEtherLossStatsGiantsDeltaMax_Type())
cucsEtherLossStatsGiantsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsGiantsDeltaMax.setStatus(_A)
_CucsEtherLossStatsGiantsDeltaMin_Type=Unsigned64
_CucsEtherLossStatsGiantsDeltaMin_Object=MibTableColumn
cucsEtherLossStatsGiantsDeltaMin=_CucsEtherLossStatsGiantsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,23),_CucsEtherLossStatsGiantsDeltaMin_Type())
cucsEtherLossStatsGiantsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsGiantsDeltaMin.setStatus(_A)
_CucsEtherLossStatsIntervals_Type=Gauge32
_CucsEtherLossStatsIntervals_Object=MibTableColumn
cucsEtherLossStatsIntervals=_CucsEtherLossStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,24),_CucsEtherLossStatsIntervals_Type())
cucsEtherLossStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsIntervals.setStatus(_A)
_CucsEtherLossStatsLateCollision_Type=Unsigned64
_CucsEtherLossStatsLateCollision_Object=MibTableColumn
cucsEtherLossStatsLateCollision=_CucsEtherLossStatsLateCollision_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,25),_CucsEtherLossStatsLateCollision_Type())
cucsEtherLossStatsLateCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsLateCollision.setStatus(_A)
_CucsEtherLossStatsLateCollisionDelta_Type=Counter64
_CucsEtherLossStatsLateCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsLateCollisionDelta=_CucsEtherLossStatsLateCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,26),_CucsEtherLossStatsLateCollisionDelta_Type())
cucsEtherLossStatsLateCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsLateCollisionDelta.setStatus(_A)
_CucsEtherLossStatsLateCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsLateCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsLateCollisionDeltaAvg=_CucsEtherLossStatsLateCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,27),_CucsEtherLossStatsLateCollisionDeltaAvg_Type())
cucsEtherLossStatsLateCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsLateCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsLateCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsLateCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsLateCollisionDeltaMax=_CucsEtherLossStatsLateCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,28),_CucsEtherLossStatsLateCollisionDeltaMax_Type())
cucsEtherLossStatsLateCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsLateCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsLateCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsLateCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsLateCollisionDeltaMin=_CucsEtherLossStatsLateCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,29),_CucsEtherLossStatsLateCollisionDeltaMin_Type())
cucsEtherLossStatsLateCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsLateCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsMultiCollision_Type=Unsigned64
_CucsEtherLossStatsMultiCollision_Object=MibTableColumn
cucsEtherLossStatsMultiCollision=_CucsEtherLossStatsMultiCollision_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,30),_CucsEtherLossStatsMultiCollision_Type())
cucsEtherLossStatsMultiCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsMultiCollision.setStatus(_A)
_CucsEtherLossStatsMultiCollisionDelta_Type=Counter64
_CucsEtherLossStatsMultiCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsMultiCollisionDelta=_CucsEtherLossStatsMultiCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,31),_CucsEtherLossStatsMultiCollisionDelta_Type())
cucsEtherLossStatsMultiCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsMultiCollisionDelta.setStatus(_A)
_CucsEtherLossStatsMultiCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsMultiCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsMultiCollisionDeltaAvg=_CucsEtherLossStatsMultiCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,32),_CucsEtherLossStatsMultiCollisionDeltaAvg_Type())
cucsEtherLossStatsMultiCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsMultiCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsMultiCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsMultiCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsMultiCollisionDeltaMax=_CucsEtherLossStatsMultiCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,33),_CucsEtherLossStatsMultiCollisionDeltaMax_Type())
cucsEtherLossStatsMultiCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsMultiCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsMultiCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsMultiCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsMultiCollisionDeltaMin=_CucsEtherLossStatsMultiCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,34),_CucsEtherLossStatsMultiCollisionDeltaMin_Type())
cucsEtherLossStatsMultiCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsMultiCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsSingleCollision_Type=Unsigned64
_CucsEtherLossStatsSingleCollision_Object=MibTableColumn
cucsEtherLossStatsSingleCollision=_CucsEtherLossStatsSingleCollision_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,35),_CucsEtherLossStatsSingleCollision_Type())
cucsEtherLossStatsSingleCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSingleCollision.setStatus(_A)
_CucsEtherLossStatsSingleCollisionDelta_Type=Counter64
_CucsEtherLossStatsSingleCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsSingleCollisionDelta=_CucsEtherLossStatsSingleCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,36),_CucsEtherLossStatsSingleCollisionDelta_Type())
cucsEtherLossStatsSingleCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSingleCollisionDelta.setStatus(_A)
_CucsEtherLossStatsSingleCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsSingleCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsSingleCollisionDeltaAvg=_CucsEtherLossStatsSingleCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,37),_CucsEtherLossStatsSingleCollisionDeltaAvg_Type())
cucsEtherLossStatsSingleCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSingleCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsSingleCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsSingleCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsSingleCollisionDeltaMax=_CucsEtherLossStatsSingleCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,38),_CucsEtherLossStatsSingleCollisionDeltaMax_Type())
cucsEtherLossStatsSingleCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSingleCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsSingleCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsSingleCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsSingleCollisionDeltaMin=_CucsEtherLossStatsSingleCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,39),_CucsEtherLossStatsSingleCollisionDeltaMin_Type())
cucsEtherLossStatsSingleCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSingleCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsSuspect_Type=TruthValue
_CucsEtherLossStatsSuspect_Object=MibTableColumn
cucsEtherLossStatsSuspect=_CucsEtherLossStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,40),_CucsEtherLossStatsSuspect_Type())
cucsEtherLossStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSuspect.setStatus(_A)
_CucsEtherLossStatsSymbol_Type=Unsigned64
_CucsEtherLossStatsSymbol_Object=MibTableColumn
cucsEtherLossStatsSymbol=_CucsEtherLossStatsSymbol_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,41),_CucsEtherLossStatsSymbol_Type())
cucsEtherLossStatsSymbol.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSymbol.setStatus(_A)
_CucsEtherLossStatsSymbolDelta_Type=Counter64
_CucsEtherLossStatsSymbolDelta_Object=MibTableColumn
cucsEtherLossStatsSymbolDelta=_CucsEtherLossStatsSymbolDelta_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,42),_CucsEtherLossStatsSymbolDelta_Type())
cucsEtherLossStatsSymbolDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSymbolDelta.setStatus(_A)
_CucsEtherLossStatsSymbolDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsSymbolDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsSymbolDeltaAvg=_CucsEtherLossStatsSymbolDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,43),_CucsEtherLossStatsSymbolDeltaAvg_Type())
cucsEtherLossStatsSymbolDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSymbolDeltaAvg.setStatus(_A)
_CucsEtherLossStatsSymbolDeltaMax_Type=Unsigned64
_CucsEtherLossStatsSymbolDeltaMax_Object=MibTableColumn
cucsEtherLossStatsSymbolDeltaMax=_CucsEtherLossStatsSymbolDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,44),_CucsEtherLossStatsSymbolDeltaMax_Type())
cucsEtherLossStatsSymbolDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSymbolDeltaMax.setStatus(_A)
_CucsEtherLossStatsSymbolDeltaMin_Type=Unsigned64
_CucsEtherLossStatsSymbolDeltaMin_Object=MibTableColumn
cucsEtherLossStatsSymbolDeltaMin=_CucsEtherLossStatsSymbolDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,45),_CucsEtherLossStatsSymbolDeltaMin_Type())
cucsEtherLossStatsSymbolDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsSymbolDeltaMin.setStatus(_A)
_CucsEtherLossStatsThresholded_Type=CucsEtherLossStatsThresholded
_CucsEtherLossStatsThresholded_Object=MibTableColumn
cucsEtherLossStatsThresholded=_CucsEtherLossStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,46),_CucsEtherLossStatsThresholded_Type())
cucsEtherLossStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsThresholded.setStatus(_A)
_CucsEtherLossStatsTimeCollected_Type=DateAndTime
_CucsEtherLossStatsTimeCollected_Object=MibTableColumn
cucsEtherLossStatsTimeCollected=_CucsEtherLossStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,47),_CucsEtherLossStatsTimeCollected_Type())
cucsEtherLossStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsTimeCollected.setStatus(_A)
_CucsEtherLossStatsUpdate_Type=Gauge32
_CucsEtherLossStatsUpdate_Object=MibTableColumn
cucsEtherLossStatsUpdate=_CucsEtherLossStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,3,1,48),_CucsEtherLossStatsUpdate_Type())
cucsEtherLossStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsUpdate.setStatus(_A)
_CucsEtherLossStatsHistTable_Object=MibTable
cucsEtherLossStatsHistTable=_CucsEtherLossStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,4))
if mibBuilder.loadTexts:cucsEtherLossStatsHistTable.setStatus(_A)
_CucsEtherLossStatsHistEntry_Object=MibTableRow
cucsEtherLossStatsHistEntry=_CucsEtherLossStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,4,1))
cucsEtherLossStatsHistEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsEtherLossStatsHistEntry.setStatus(_A)
_CucsEtherLossStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherLossStatsHistInstanceId_Object=MibTableColumn
cucsEtherLossStatsHistInstanceId=_CucsEtherLossStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,1),_CucsEtherLossStatsHistInstanceId_Type())
cucsEtherLossStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherLossStatsHistInstanceId.setStatus(_A)
_CucsEtherLossStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherLossStatsHistDn_Object=MibTableColumn
cucsEtherLossStatsHistDn=_CucsEtherLossStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,2),_CucsEtherLossStatsHistDn_Type())
cucsEtherLossStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistDn.setStatus(_A)
_CucsEtherLossStatsHistRn_Type=SnmpAdminString
_CucsEtherLossStatsHistRn_Object=MibTableColumn
cucsEtherLossStatsHistRn=_CucsEtherLossStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,3),_CucsEtherLossStatsHistRn_Type())
cucsEtherLossStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistRn.setStatus(_A)
_CucsEtherLossStatsHistSQETest_Type=Unsigned64
_CucsEtherLossStatsHistSQETest_Object=MibTableColumn
cucsEtherLossStatsHistSQETest=_CucsEtherLossStatsHistSQETest_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,4),_CucsEtherLossStatsHistSQETest_Type())
cucsEtherLossStatsHistSQETest.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSQETest.setStatus(_A)
_CucsEtherLossStatsHistSQETestDelta_Type=Unsigned64
_CucsEtherLossStatsHistSQETestDelta_Object=MibTableColumn
cucsEtherLossStatsHistSQETestDelta=_CucsEtherLossStatsHistSQETestDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,5),_CucsEtherLossStatsHistSQETestDelta_Type())
cucsEtherLossStatsHistSQETestDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSQETestDelta.setStatus(_A)
_CucsEtherLossStatsHistSQETestDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistSQETestDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistSQETestDeltaAvg=_CucsEtherLossStatsHistSQETestDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,6),_CucsEtherLossStatsHistSQETestDeltaAvg_Type())
cucsEtherLossStatsHistSQETestDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSQETestDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistSQETestDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistSQETestDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistSQETestDeltaMax=_CucsEtherLossStatsHistSQETestDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,7),_CucsEtherLossStatsHistSQETestDeltaMax_Type())
cucsEtherLossStatsHistSQETestDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSQETestDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistSQETestDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistSQETestDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistSQETestDeltaMin=_CucsEtherLossStatsHistSQETestDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,8),_CucsEtherLossStatsHistSQETestDeltaMin_Type())
cucsEtherLossStatsHistSQETestDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSQETestDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistCarrierSense_Type=Unsigned64
_CucsEtherLossStatsHistCarrierSense_Object=MibTableColumn
cucsEtherLossStatsHistCarrierSense=_CucsEtherLossStatsHistCarrierSense_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,9),_CucsEtherLossStatsHistCarrierSense_Type())
cucsEtherLossStatsHistCarrierSense.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistCarrierSense.setStatus(_A)
_CucsEtherLossStatsHistCarrierSenseDelta_Type=Unsigned64
_CucsEtherLossStatsHistCarrierSenseDelta_Object=MibTableColumn
cucsEtherLossStatsHistCarrierSenseDelta=_CucsEtherLossStatsHistCarrierSenseDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,10),_CucsEtherLossStatsHistCarrierSenseDelta_Type())
cucsEtherLossStatsHistCarrierSenseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistCarrierSenseDelta.setStatus(_A)
_CucsEtherLossStatsHistCarrierSenseDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistCarrierSenseDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistCarrierSenseDeltaAvg=_CucsEtherLossStatsHistCarrierSenseDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,11),_CucsEtherLossStatsHistCarrierSenseDeltaAvg_Type())
cucsEtherLossStatsHistCarrierSenseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistCarrierSenseDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistCarrierSenseDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistCarrierSenseDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistCarrierSenseDeltaMax=_CucsEtherLossStatsHistCarrierSenseDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,12),_CucsEtherLossStatsHistCarrierSenseDeltaMax_Type())
cucsEtherLossStatsHistCarrierSenseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistCarrierSenseDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistCarrierSenseDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistCarrierSenseDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistCarrierSenseDeltaMin=_CucsEtherLossStatsHistCarrierSenseDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,13),_CucsEtherLossStatsHistCarrierSenseDeltaMin_Type())
cucsEtherLossStatsHistCarrierSenseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistCarrierSenseDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistExcessCollision_Type=Unsigned64
_CucsEtherLossStatsHistExcessCollision_Object=MibTableColumn
cucsEtherLossStatsHistExcessCollision=_CucsEtherLossStatsHistExcessCollision_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,14),_CucsEtherLossStatsHistExcessCollision_Type())
cucsEtherLossStatsHistExcessCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistExcessCollision.setStatus(_A)
_CucsEtherLossStatsHistExcessCollisionDelta_Type=Unsigned64
_CucsEtherLossStatsHistExcessCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsHistExcessCollisionDelta=_CucsEtherLossStatsHistExcessCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,15),_CucsEtherLossStatsHistExcessCollisionDelta_Type())
cucsEtherLossStatsHistExcessCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistExcessCollisionDelta.setStatus(_A)
_CucsEtherLossStatsHistExcessCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistExcessCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistExcessCollisionDeltaAvg=_CucsEtherLossStatsHistExcessCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,16),_CucsEtherLossStatsHistExcessCollisionDeltaAvg_Type())
cucsEtherLossStatsHistExcessCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistExcessCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistExcessCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistExcessCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistExcessCollisionDeltaMax=_CucsEtherLossStatsHistExcessCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,17),_CucsEtherLossStatsHistExcessCollisionDeltaMax_Type())
cucsEtherLossStatsHistExcessCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistExcessCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistExcessCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistExcessCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistExcessCollisionDeltaMin=_CucsEtherLossStatsHistExcessCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,18),_CucsEtherLossStatsHistExcessCollisionDeltaMin_Type())
cucsEtherLossStatsHistExcessCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistExcessCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistGiants_Type=Unsigned64
_CucsEtherLossStatsHistGiants_Object=MibTableColumn
cucsEtherLossStatsHistGiants=_CucsEtherLossStatsHistGiants_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,19),_CucsEtherLossStatsHistGiants_Type())
cucsEtherLossStatsHistGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistGiants.setStatus(_A)
_CucsEtherLossStatsHistGiantsDelta_Type=Unsigned64
_CucsEtherLossStatsHistGiantsDelta_Object=MibTableColumn
cucsEtherLossStatsHistGiantsDelta=_CucsEtherLossStatsHistGiantsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,20),_CucsEtherLossStatsHistGiantsDelta_Type())
cucsEtherLossStatsHistGiantsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistGiantsDelta.setStatus(_A)
_CucsEtherLossStatsHistGiantsDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistGiantsDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistGiantsDeltaAvg=_CucsEtherLossStatsHistGiantsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,21),_CucsEtherLossStatsHistGiantsDeltaAvg_Type())
cucsEtherLossStatsHistGiantsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistGiantsDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistGiantsDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistGiantsDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistGiantsDeltaMax=_CucsEtherLossStatsHistGiantsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,22),_CucsEtherLossStatsHistGiantsDeltaMax_Type())
cucsEtherLossStatsHistGiantsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistGiantsDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistGiantsDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistGiantsDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistGiantsDeltaMin=_CucsEtherLossStatsHistGiantsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,23),_CucsEtherLossStatsHistGiantsDeltaMin_Type())
cucsEtherLossStatsHistGiantsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistGiantsDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistId_Type=Unsigned64
_CucsEtherLossStatsHistId_Object=MibTableColumn
cucsEtherLossStatsHistId=_CucsEtherLossStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,24),_CucsEtherLossStatsHistId_Type())
cucsEtherLossStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistId.setStatus(_A)
_CucsEtherLossStatsHistLateCollision_Type=Unsigned64
_CucsEtherLossStatsHistLateCollision_Object=MibTableColumn
cucsEtherLossStatsHistLateCollision=_CucsEtherLossStatsHistLateCollision_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,25),_CucsEtherLossStatsHistLateCollision_Type())
cucsEtherLossStatsHistLateCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistLateCollision.setStatus(_A)
_CucsEtherLossStatsHistLateCollisionDelta_Type=Unsigned64
_CucsEtherLossStatsHistLateCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsHistLateCollisionDelta=_CucsEtherLossStatsHistLateCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,26),_CucsEtherLossStatsHistLateCollisionDelta_Type())
cucsEtherLossStatsHistLateCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistLateCollisionDelta.setStatus(_A)
_CucsEtherLossStatsHistLateCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistLateCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistLateCollisionDeltaAvg=_CucsEtherLossStatsHistLateCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,27),_CucsEtherLossStatsHistLateCollisionDeltaAvg_Type())
cucsEtherLossStatsHistLateCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistLateCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistLateCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistLateCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistLateCollisionDeltaMax=_CucsEtherLossStatsHistLateCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,28),_CucsEtherLossStatsHistLateCollisionDeltaMax_Type())
cucsEtherLossStatsHistLateCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistLateCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistLateCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistLateCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistLateCollisionDeltaMin=_CucsEtherLossStatsHistLateCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,29),_CucsEtherLossStatsHistLateCollisionDeltaMin_Type())
cucsEtherLossStatsHistLateCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistLateCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistMostRecent_Type=TruthValue
_CucsEtherLossStatsHistMostRecent_Object=MibTableColumn
cucsEtherLossStatsHistMostRecent=_CucsEtherLossStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,30),_CucsEtherLossStatsHistMostRecent_Type())
cucsEtherLossStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistMostRecent.setStatus(_A)
_CucsEtherLossStatsHistMultiCollision_Type=Unsigned64
_CucsEtherLossStatsHistMultiCollision_Object=MibTableColumn
cucsEtherLossStatsHistMultiCollision=_CucsEtherLossStatsHistMultiCollision_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,31),_CucsEtherLossStatsHistMultiCollision_Type())
cucsEtherLossStatsHistMultiCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistMultiCollision.setStatus(_A)
_CucsEtherLossStatsHistMultiCollisionDelta_Type=Unsigned64
_CucsEtherLossStatsHistMultiCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsHistMultiCollisionDelta=_CucsEtherLossStatsHistMultiCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,32),_CucsEtherLossStatsHistMultiCollisionDelta_Type())
cucsEtherLossStatsHistMultiCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistMultiCollisionDelta.setStatus(_A)
_CucsEtherLossStatsHistMultiCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistMultiCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistMultiCollisionDeltaAvg=_CucsEtherLossStatsHistMultiCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,33),_CucsEtherLossStatsHistMultiCollisionDeltaAvg_Type())
cucsEtherLossStatsHistMultiCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistMultiCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistMultiCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistMultiCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistMultiCollisionDeltaMax=_CucsEtherLossStatsHistMultiCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,34),_CucsEtherLossStatsHistMultiCollisionDeltaMax_Type())
cucsEtherLossStatsHistMultiCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistMultiCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistMultiCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistMultiCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistMultiCollisionDeltaMin=_CucsEtherLossStatsHistMultiCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,35),_CucsEtherLossStatsHistMultiCollisionDeltaMin_Type())
cucsEtherLossStatsHistMultiCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistMultiCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistSingleCollision_Type=Unsigned64
_CucsEtherLossStatsHistSingleCollision_Object=MibTableColumn
cucsEtherLossStatsHistSingleCollision=_CucsEtherLossStatsHistSingleCollision_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,36),_CucsEtherLossStatsHistSingleCollision_Type())
cucsEtherLossStatsHistSingleCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSingleCollision.setStatus(_A)
_CucsEtherLossStatsHistSingleCollisionDelta_Type=Unsigned64
_CucsEtherLossStatsHistSingleCollisionDelta_Object=MibTableColumn
cucsEtherLossStatsHistSingleCollisionDelta=_CucsEtherLossStatsHistSingleCollisionDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,37),_CucsEtherLossStatsHistSingleCollisionDelta_Type())
cucsEtherLossStatsHistSingleCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSingleCollisionDelta.setStatus(_A)
_CucsEtherLossStatsHistSingleCollisionDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistSingleCollisionDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistSingleCollisionDeltaAvg=_CucsEtherLossStatsHistSingleCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,38),_CucsEtherLossStatsHistSingleCollisionDeltaAvg_Type())
cucsEtherLossStatsHistSingleCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSingleCollisionDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistSingleCollisionDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistSingleCollisionDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistSingleCollisionDeltaMax=_CucsEtherLossStatsHistSingleCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,39),_CucsEtherLossStatsHistSingleCollisionDeltaMax_Type())
cucsEtherLossStatsHistSingleCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSingleCollisionDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistSingleCollisionDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistSingleCollisionDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistSingleCollisionDeltaMin=_CucsEtherLossStatsHistSingleCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,40),_CucsEtherLossStatsHistSingleCollisionDeltaMin_Type())
cucsEtherLossStatsHistSingleCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSingleCollisionDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistSuspect_Type=TruthValue
_CucsEtherLossStatsHistSuspect_Object=MibTableColumn
cucsEtherLossStatsHistSuspect=_CucsEtherLossStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,41),_CucsEtherLossStatsHistSuspect_Type())
cucsEtherLossStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSuspect.setStatus(_A)
_CucsEtherLossStatsHistSymbol_Type=Unsigned64
_CucsEtherLossStatsHistSymbol_Object=MibTableColumn
cucsEtherLossStatsHistSymbol=_CucsEtherLossStatsHistSymbol_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,42),_CucsEtherLossStatsHistSymbol_Type())
cucsEtherLossStatsHistSymbol.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSymbol.setStatus(_A)
_CucsEtherLossStatsHistSymbolDelta_Type=Unsigned64
_CucsEtherLossStatsHistSymbolDelta_Object=MibTableColumn
cucsEtherLossStatsHistSymbolDelta=_CucsEtherLossStatsHistSymbolDelta_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,43),_CucsEtherLossStatsHistSymbolDelta_Type())
cucsEtherLossStatsHistSymbolDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSymbolDelta.setStatus(_A)
_CucsEtherLossStatsHistSymbolDeltaAvg_Type=Unsigned64
_CucsEtherLossStatsHistSymbolDeltaAvg_Object=MibTableColumn
cucsEtherLossStatsHistSymbolDeltaAvg=_CucsEtherLossStatsHistSymbolDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,44),_CucsEtherLossStatsHistSymbolDeltaAvg_Type())
cucsEtherLossStatsHistSymbolDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSymbolDeltaAvg.setStatus(_A)
_CucsEtherLossStatsHistSymbolDeltaMax_Type=Unsigned64
_CucsEtherLossStatsHistSymbolDeltaMax_Object=MibTableColumn
cucsEtherLossStatsHistSymbolDeltaMax=_CucsEtherLossStatsHistSymbolDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,45),_CucsEtherLossStatsHistSymbolDeltaMax_Type())
cucsEtherLossStatsHistSymbolDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSymbolDeltaMax.setStatus(_A)
_CucsEtherLossStatsHistSymbolDeltaMin_Type=Unsigned64
_CucsEtherLossStatsHistSymbolDeltaMin_Object=MibTableColumn
cucsEtherLossStatsHistSymbolDeltaMin=_CucsEtherLossStatsHistSymbolDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,46),_CucsEtherLossStatsHistSymbolDeltaMin_Type())
cucsEtherLossStatsHistSymbolDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistSymbolDeltaMin.setStatus(_A)
_CucsEtherLossStatsHistThresholded_Type=CucsEtherLossStatsHistThresholded
_CucsEtherLossStatsHistThresholded_Object=MibTableColumn
cucsEtherLossStatsHistThresholded=_CucsEtherLossStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,47),_CucsEtherLossStatsHistThresholded_Type())
cucsEtherLossStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistThresholded.setStatus(_A)
_CucsEtherLossStatsHistTimeCollected_Type=DateAndTime
_CucsEtherLossStatsHistTimeCollected_Object=MibTableColumn
cucsEtherLossStatsHistTimeCollected=_CucsEtherLossStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,4,1,48),_CucsEtherLossStatsHistTimeCollected_Type())
cucsEtherLossStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherLossStatsHistTimeCollected.setStatus(_A)
_CucsEtherNicIfConfigTable_Object=MibTable
cucsEtherNicIfConfigTable=_CucsEtherNicIfConfigTable_Object((1,3,6,1,4,1,9,9,719,1,16,5))
if mibBuilder.loadTexts:cucsEtherNicIfConfigTable.setStatus(_A)
_CucsEtherNicIfConfigEntry_Object=MibTableRow
cucsEtherNicIfConfigEntry=_CucsEtherNicIfConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,16,5,1))
cucsEtherNicIfConfigEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsEtherNicIfConfigEntry.setStatus(_A)
_CucsEtherNicIfConfigInstanceId_Type=CucsManagedObjectId
_CucsEtherNicIfConfigInstanceId_Object=MibTableColumn
cucsEtherNicIfConfigInstanceId=_CucsEtherNicIfConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,5,1,1),_CucsEtherNicIfConfigInstanceId_Type())
cucsEtherNicIfConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherNicIfConfigInstanceId.setStatus(_A)
_CucsEtherNicIfConfigDn_Type=CucsManagedObjectDn
_CucsEtherNicIfConfigDn_Object=MibTableColumn
cucsEtherNicIfConfigDn=_CucsEtherNicIfConfigDn_Object((1,3,6,1,4,1,9,9,719,1,16,5,1,2),_CucsEtherNicIfConfigDn_Type())
cucsEtherNicIfConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNicIfConfigDn.setStatus(_A)
_CucsEtherNicIfConfigRn_Type=SnmpAdminString
_CucsEtherNicIfConfigRn_Object=MibTableColumn
cucsEtherNicIfConfigRn=_CucsEtherNicIfConfigRn_Object((1,3,6,1,4,1,9,9,719,1,16,5,1,3),_CucsEtherNicIfConfigRn_Type())
cucsEtherNicIfConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNicIfConfigRn.setStatus(_A)
_CucsEtherPIoTable_Object=MibTable
cucsEtherPIoTable=_CucsEtherPIoTable_Object((1,3,6,1,4,1,9,9,719,1,16,6))
if mibBuilder.loadTexts:cucsEtherPIoTable.setStatus(_A)
_CucsEtherPIoEntry_Object=MibTableRow
cucsEtherPIoEntry=_CucsEtherPIoEntry_Object((1,3,6,1,4,1,9,9,719,1,16,6,1))
cucsEtherPIoEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsEtherPIoEntry.setStatus(_A)
_CucsEtherPIoInstanceId_Type=CucsManagedObjectId
_CucsEtherPIoInstanceId_Object=MibTableColumn
cucsEtherPIoInstanceId=_CucsEtherPIoInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,1),_CucsEtherPIoInstanceId_Type())
cucsEtherPIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPIoInstanceId.setStatus(_A)
_CucsEtherPIoDn_Type=CucsManagedObjectDn
_CucsEtherPIoDn_Object=MibTableColumn
cucsEtherPIoDn=_CucsEtherPIoDn_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,2),_CucsEtherPIoDn_Type())
cucsEtherPIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoDn.setStatus(_A)
_CucsEtherPIoRn_Type=SnmpAdminString
_CucsEtherPIoRn_Object=MibTableColumn
cucsEtherPIoRn=_CucsEtherPIoRn_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,3),_CucsEtherPIoRn_Type())
cucsEtherPIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoRn.setStatus(_A)
_CucsEtherPIoAdminState_Type=CucsFabricAdminState
_CucsEtherPIoAdminState_Object=MibTableColumn
cucsEtherPIoAdminState=_CucsEtherPIoAdminState_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,4),_CucsEtherPIoAdminState_Type())
cucsEtherPIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoAdminState.setStatus(_A)
_CucsEtherPIoChassisId_Type=Gauge32
_CucsEtherPIoChassisId_Object=MibTableColumn
cucsEtherPIoChassisId=_CucsEtherPIoChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,5),_CucsEtherPIoChassisId_Type())
cucsEtherPIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoChassisId.setStatus(_A)
_CucsEtherPIoEncap_Type=CucsPortEncap
_CucsEtherPIoEncap_Object=MibTableColumn
cucsEtherPIoEncap=_CucsEtherPIoEncap_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,6),_CucsEtherPIoEncap_Type())
cucsEtherPIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEncap.setStatus(_A)
_CucsEtherPIoEpDn_Type=SnmpAdminString
_CucsEtherPIoEpDn_Object=MibTableColumn
cucsEtherPIoEpDn=_CucsEtherPIoEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,7),_CucsEtherPIoEpDn_Type())
cucsEtherPIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEpDn.setStatus(_A)
_CucsEtherPIoFltAggr_Type=Unsigned64
_CucsEtherPIoFltAggr_Object=MibTableColumn
cucsEtherPIoFltAggr=_CucsEtherPIoFltAggr_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,8),_CucsEtherPIoFltAggr_Type())
cucsEtherPIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFltAggr.setStatus(_A)
_CucsEtherPIoIfRole_Type=CucsNetworkPortRole
_CucsEtherPIoIfRole_Object=MibTableColumn
cucsEtherPIoIfRole=_CucsEtherPIoIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,9),_CucsEtherPIoIfRole_Type())
cucsEtherPIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoIfRole.setStatus(_A)
_CucsEtherPIoIfType_Type=CucsNetworkPhysEpIfType
_CucsEtherPIoIfType_Object=MibTableColumn
cucsEtherPIoIfType=_CucsEtherPIoIfType_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,10),_CucsEtherPIoIfType_Type())
cucsEtherPIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoIfType.setStatus(_A)
_CucsEtherPIoLocale_Type=CucsNetworkLocale
_CucsEtherPIoLocale_Object=MibTableColumn
cucsEtherPIoLocale=_CucsEtherPIoLocale_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,11),_CucsEtherPIoLocale_Type())
cucsEtherPIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoLocale.setStatus(_A)
_CucsEtherPIoMac_Type=MacAddress
_CucsEtherPIoMac_Object=MibTableColumn
cucsEtherPIoMac=_CucsEtherPIoMac_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,12),_CucsEtherPIoMac_Type())
cucsEtherPIoMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoMac.setStatus(_A)
_CucsEtherPIoMode_Type=CucsPortMode
_CucsEtherPIoMode_Object=MibTableColumn
cucsEtherPIoMode=_CucsEtherPIoMode_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,13),_CucsEtherPIoMode_Type())
cucsEtherPIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoMode.setStatus(_A)
_CucsEtherPIoModel_Type=SnmpAdminString
_CucsEtherPIoModel_Object=MibTableColumn
cucsEtherPIoModel=_CucsEtherPIoModel_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,14),_CucsEtherPIoModel_Type())
cucsEtherPIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoModel.setStatus(_A)
_CucsEtherPIoName_Type=SnmpAdminString
_CucsEtherPIoName_Object=MibTableColumn
cucsEtherPIoName=_CucsEtherPIoName_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,15),_CucsEtherPIoName_Type())
cucsEtherPIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoName.setStatus(_A)
_CucsEtherPIoOperSpeed_Type=CucsPortEthSpeed
_CucsEtherPIoOperSpeed_Object=MibTableColumn
cucsEtherPIoOperSpeed=_CucsEtherPIoOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,16),_CucsEtherPIoOperSpeed_Type())
cucsEtherPIoOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoOperSpeed.setStatus(_A)
_CucsEtherPIoOperState_Type=CucsNetworkPortOperState
_CucsEtherPIoOperState_Object=MibTableColumn
cucsEtherPIoOperState=_CucsEtherPIoOperState_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,17),_CucsEtherPIoOperState_Type())
cucsEtherPIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoOperState.setStatus(_A)
_CucsEtherPIoPeerDn_Type=SnmpAdminString
_CucsEtherPIoPeerDn_Object=MibTableColumn
cucsEtherPIoPeerDn=_CucsEtherPIoPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,18),_CucsEtherPIoPeerDn_Type())
cucsEtherPIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPeerDn.setStatus(_A)
_CucsEtherPIoPeerPortId_Type=Gauge32
_CucsEtherPIoPeerPortId_Object=MibTableColumn
cucsEtherPIoPeerPortId=_CucsEtherPIoPeerPortId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,19),_CucsEtherPIoPeerPortId_Type())
cucsEtherPIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPeerPortId.setStatus(_A)
_CucsEtherPIoPeerSlotId_Type=Gauge32
_CucsEtherPIoPeerSlotId_Object=MibTableColumn
cucsEtherPIoPeerSlotId=_CucsEtherPIoPeerSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,20),_CucsEtherPIoPeerSlotId_Type())
cucsEtherPIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPeerSlotId.setStatus(_A)
_CucsEtherPIoPortId_Type=Gauge32
_CucsEtherPIoPortId_Object=MibTableColumn
cucsEtherPIoPortId=_CucsEtherPIoPortId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,21),_CucsEtherPIoPortId_Type())
cucsEtherPIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPortId.setStatus(_A)
_CucsEtherPIoRevision_Type=SnmpAdminString
_CucsEtherPIoRevision_Object=MibTableColumn
cucsEtherPIoRevision=_CucsEtherPIoRevision_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,22),_CucsEtherPIoRevision_Type())
cucsEtherPIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoRevision.setStatus(_A)
_CucsEtherPIoSerial_Type=SnmpAdminString
_CucsEtherPIoSerial_Object=MibTableColumn
cucsEtherPIoSerial=_CucsEtherPIoSerial_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,23),_CucsEtherPIoSerial_Type())
cucsEtherPIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoSerial.setStatus(_A)
_CucsEtherPIoSlotId_Type=Gauge32
_CucsEtherPIoSlotId_Object=MibTableColumn
cucsEtherPIoSlotId=_CucsEtherPIoSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,24),_CucsEtherPIoSlotId_Type())
cucsEtherPIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoSlotId.setStatus(_A)
_CucsEtherPIoStateQual_Type=SnmpAdminString
_CucsEtherPIoStateQual_Object=MibTableColumn
cucsEtherPIoStateQual=_CucsEtherPIoStateQual_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,25),_CucsEtherPIoStateQual_Type())
cucsEtherPIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoStateQual.setStatus(_A)
_CucsEtherPIoSwitchId_Type=CucsNetworkSwitchId
_CucsEtherPIoSwitchId_Object=MibTableColumn
cucsEtherPIoSwitchId=_CucsEtherPIoSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,26),_CucsEtherPIoSwitchId_Type())
cucsEtherPIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoSwitchId.setStatus(_A)
_CucsEtherPIoTransport_Type=CucsNetworkTransport
_CucsEtherPIoTransport_Object=MibTableColumn
cucsEtherPIoTransport=_CucsEtherPIoTransport_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,27),_CucsEtherPIoTransport_Type())
cucsEtherPIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoTransport.setStatus(_A)
_CucsEtherPIoTs_Type=DateAndTime
_CucsEtherPIoTs_Object=MibTableColumn
cucsEtherPIoTs=_CucsEtherPIoTs_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,28),_CucsEtherPIoTs_Type())
cucsEtherPIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoTs.setStatus(_A)
_CucsEtherPIoType_Type=CucsNetworkConnectionType
_CucsEtherPIoType_Object=MibTableColumn
cucsEtherPIoType=_CucsEtherPIoType_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,29),_CucsEtherPIoType_Type())
cucsEtherPIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoType.setStatus(_A)
_CucsEtherPIoUsrLbl_Type=SnmpAdminString
_CucsEtherPIoUsrLbl_Object=MibTableColumn
cucsEtherPIoUsrLbl=_CucsEtherPIoUsrLbl_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,30),_CucsEtherPIoUsrLbl_Type())
cucsEtherPIoUsrLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoUsrLbl.setStatus(_A)
_CucsEtherPIoVendor_Type=SnmpAdminString
_CucsEtherPIoVendor_Object=MibTableColumn
cucsEtherPIoVendor=_CucsEtherPIoVendor_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,31),_CucsEtherPIoVendor_Type())
cucsEtherPIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoVendor.setStatus(_A)
_CucsEtherPIoFsmDescr_Type=SnmpAdminString
_CucsEtherPIoFsmDescr_Object=MibTableColumn
cucsEtherPIoFsmDescr=_CucsEtherPIoFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,32),_CucsEtherPIoFsmDescr_Type())
cucsEtherPIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmDescr.setStatus(_A)
_CucsEtherPIoFsmPrev_Type=SnmpAdminString
_CucsEtherPIoFsmPrev_Object=MibTableColumn
cucsEtherPIoFsmPrev=_CucsEtherPIoFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,33),_CucsEtherPIoFsmPrev_Type())
cucsEtherPIoFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmPrev.setStatus(_A)
_CucsEtherPIoFsmProgr_Type=Gauge32
_CucsEtherPIoFsmProgr_Object=MibTableColumn
cucsEtherPIoFsmProgr=_CucsEtherPIoFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,34),_CucsEtherPIoFsmProgr_Type())
cucsEtherPIoFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmProgr.setStatus(_A)
_CucsEtherPIoFsmRmtInvErrCode_Type=Gauge32
_CucsEtherPIoFsmRmtInvErrCode_Object=MibTableColumn
cucsEtherPIoFsmRmtInvErrCode=_CucsEtherPIoFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,35),_CucsEtherPIoFsmRmtInvErrCode_Type())
cucsEtherPIoFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRmtInvErrCode.setStatus(_A)
_CucsEtherPIoFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsEtherPIoFsmRmtInvErrDescr_Object=MibTableColumn
cucsEtherPIoFsmRmtInvErrDescr=_CucsEtherPIoFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,36),_CucsEtherPIoFsmRmtInvErrDescr_Type())
cucsEtherPIoFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRmtInvErrDescr.setStatus(_A)
_CucsEtherPIoFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsEtherPIoFsmRmtInvRslt_Object=MibTableColumn
cucsEtherPIoFsmRmtInvRslt=_CucsEtherPIoFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,37),_CucsEtherPIoFsmRmtInvRslt_Type())
cucsEtherPIoFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRmtInvRslt.setStatus(_A)
_CucsEtherPIoFsmStageDescr_Type=SnmpAdminString
_CucsEtherPIoFsmStageDescr_Object=MibTableColumn
cucsEtherPIoFsmStageDescr=_CucsEtherPIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,38),_CucsEtherPIoFsmStageDescr_Type())
cucsEtherPIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageDescr.setStatus(_A)
_CucsEtherPIoFsmStamp_Type=DateAndTime
_CucsEtherPIoFsmStamp_Object=MibTableColumn
cucsEtherPIoFsmStamp=_CucsEtherPIoFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,39),_CucsEtherPIoFsmStamp_Type())
cucsEtherPIoFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStamp.setStatus(_A)
_CucsEtherPIoFsmStatus_Type=SnmpAdminString
_CucsEtherPIoFsmStatus_Object=MibTableColumn
cucsEtherPIoFsmStatus=_CucsEtherPIoFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,40),_CucsEtherPIoFsmStatus_Type())
cucsEtherPIoFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStatus.setStatus(_A)
_CucsEtherPIoFsmTry_Type=Gauge32
_CucsEtherPIoFsmTry_Object=MibTableColumn
cucsEtherPIoFsmTry=_CucsEtherPIoFsmTry_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,41),_CucsEtherPIoFsmTry_Type())
cucsEtherPIoFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmTry.setStatus(_A)
_CucsEtherPIoLicGP_Type=Unsigned64
_CucsEtherPIoLicGP_Object=MibTableColumn
cucsEtherPIoLicGP=_CucsEtherPIoLicGP_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,42),_CucsEtherPIoLicGP_Type())
cucsEtherPIoLicGP.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoLicGP.setStatus(_A)
_CucsEtherPIoLicState_Type=CucsLicenseState
_CucsEtherPIoLicState_Object=MibTableColumn
cucsEtherPIoLicState=_CucsEtherPIoLicState_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,43),_CucsEtherPIoLicState_Type())
cucsEtherPIoLicState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoLicState.setStatus(_A)
_CucsEtherPIoXcvrType_Type=CucsEquipmentXcvrType
_CucsEtherPIoXcvrType_Object=MibTableColumn
cucsEtherPIoXcvrType=_CucsEtherPIoXcvrType_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,44),_CucsEtherPIoXcvrType_Type())
cucsEtherPIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoXcvrType.setStatus(_A)
_CucsEtherPIoPeerChassisId_Type=Gauge32
_CucsEtherPIoPeerChassisId_Object=MibTableColumn
cucsEtherPIoPeerChassisId=_CucsEtherPIoPeerChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,45),_CucsEtherPIoPeerChassisId_Type())
cucsEtherPIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPeerChassisId.setStatus(_A)
_CucsEtherPIoAdminTransport_Type=CucsNetworkTransport
_CucsEtherPIoAdminTransport_Object=MibTableColumn
cucsEtherPIoAdminTransport=_CucsEtherPIoAdminTransport_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,46),_CucsEtherPIoAdminTransport_Type())
cucsEtherPIoAdminTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoAdminTransport.setStatus(_A)
_CucsEtherPIoLc_Type=CucsFsmLifecycle
_CucsEtherPIoLc_Object=MibTableColumn
cucsEtherPIoLc=_CucsEtherPIoLc_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,47),_CucsEtherPIoLc_Type())
cucsEtherPIoLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoLc.setStatus(_A)
_CucsEtherPIoUnifiedPort_Type=TruthValue
_CucsEtherPIoUnifiedPort_Object=MibTableColumn
cucsEtherPIoUnifiedPort=_CucsEtherPIoUnifiedPort_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,48),_CucsEtherPIoUnifiedPort_Type())
cucsEtherPIoUnifiedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoUnifiedPort.setStatus(_A)
_CucsEtherPIoIsPortChannelMember_Type=TruthValue
_CucsEtherPIoIsPortChannelMember_Object=MibTableColumn
cucsEtherPIoIsPortChannelMember=_CucsEtherPIoIsPortChannelMember_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,49),_CucsEtherPIoIsPortChannelMember_Type())
cucsEtherPIoIsPortChannelMember.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoIsPortChannelMember.setStatus(_A)
_CucsEtherPIoAggrPortId_Type=Gauge32
_CucsEtherPIoAggrPortId_Object=MibTableColumn
cucsEtherPIoAggrPortId=_CucsEtherPIoAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,50),_CucsEtherPIoAggrPortId_Type())
cucsEtherPIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoAggrPortId.setStatus(_A)
_CucsEtherPIoPeerAggrPortId_Type=Gauge32
_CucsEtherPIoPeerAggrPortId_Object=MibTableColumn
cucsEtherPIoPeerAggrPortId=_CucsEtherPIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,51),_CucsEtherPIoPeerAggrPortId_Type())
cucsEtherPIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPeerAggrPortId.setStatus(_A)
_CucsEtherPIoNonCR4_Type=TruthValue
_CucsEtherPIoNonCR4_Object=MibTableColumn
cucsEtherPIoNonCR4=_CucsEtherPIoNonCR4_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,52),_CucsEtherPIoNonCR4_Type())
cucsEtherPIoNonCR4.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoNonCR4.setStatus(_A)
_CucsEtherPIoIsBreakoutXcvr_Type=TruthValue
_CucsEtherPIoIsBreakoutXcvr_Object=MibTableColumn
cucsEtherPIoIsBreakoutXcvr=_CucsEtherPIoIsBreakoutXcvr_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,53),_CucsEtherPIoIsBreakoutXcvr_Type())
cucsEtherPIoIsBreakoutXcvr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoIsBreakoutXcvr.setStatus(_A)
_CucsEtherPIoPortCapability_Type=CucsPortapiPeerCapability
_CucsEtherPIoPortCapability_Object=MibTableColumn
cucsEtherPIoPortCapability=_CucsEtherPIoPortCapability_Object((1,3,6,1,4,1,9,9,719,1,16,6,1,54),_CucsEtherPIoPortCapability_Type())
cucsEtherPIoPortCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoPortCapability.setStatus(_A)
_CucsEtherPauseStatsTable_Object=MibTable
cucsEtherPauseStatsTable=_CucsEtherPauseStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,7))
if mibBuilder.loadTexts:cucsEtherPauseStatsTable.setStatus(_A)
_CucsEtherPauseStatsEntry_Object=MibTableRow
cucsEtherPauseStatsEntry=_CucsEtherPauseStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,7,1))
cucsEtherPauseStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsEtherPauseStatsEntry.setStatus(_A)
_CucsEtherPauseStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherPauseStatsInstanceId_Object=MibTableColumn
cucsEtherPauseStatsInstanceId=_CucsEtherPauseStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,1),_CucsEtherPauseStatsInstanceId_Type())
cucsEtherPauseStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPauseStatsInstanceId.setStatus(_A)
_CucsEtherPauseStatsDn_Type=CucsManagedObjectDn
_CucsEtherPauseStatsDn_Object=MibTableColumn
cucsEtherPauseStatsDn=_CucsEtherPauseStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,2),_CucsEtherPauseStatsDn_Type())
cucsEtherPauseStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsDn.setStatus(_A)
_CucsEtherPauseStatsRn_Type=SnmpAdminString
_CucsEtherPauseStatsRn_Object=MibTableColumn
cucsEtherPauseStatsRn=_CucsEtherPauseStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,3),_CucsEtherPauseStatsRn_Type())
cucsEtherPauseStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsRn.setStatus(_A)
_CucsEtherPauseStatsIntervals_Type=Gauge32
_CucsEtherPauseStatsIntervals_Object=MibTableColumn
cucsEtherPauseStatsIntervals=_CucsEtherPauseStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,4),_CucsEtherPauseStatsIntervals_Type())
cucsEtherPauseStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsIntervals.setStatus(_A)
_CucsEtherPauseStatsRecvPause_Type=Unsigned64
_CucsEtherPauseStatsRecvPause_Object=MibTableColumn
cucsEtherPauseStatsRecvPause=_CucsEtherPauseStatsRecvPause_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,5),_CucsEtherPauseStatsRecvPause_Type())
cucsEtherPauseStatsRecvPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsRecvPause.setStatus(_A)
_CucsEtherPauseStatsRecvPauseDelta_Type=Counter64
_CucsEtherPauseStatsRecvPauseDelta_Object=MibTableColumn
cucsEtherPauseStatsRecvPauseDelta=_CucsEtherPauseStatsRecvPauseDelta_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,6),_CucsEtherPauseStatsRecvPauseDelta_Type())
cucsEtherPauseStatsRecvPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsRecvPauseDelta.setStatus(_A)
_CucsEtherPauseStatsRecvPauseDeltaAvg_Type=Unsigned64
_CucsEtherPauseStatsRecvPauseDeltaAvg_Object=MibTableColumn
cucsEtherPauseStatsRecvPauseDeltaAvg=_CucsEtherPauseStatsRecvPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,7),_CucsEtherPauseStatsRecvPauseDeltaAvg_Type())
cucsEtherPauseStatsRecvPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsRecvPauseDeltaAvg.setStatus(_A)
_CucsEtherPauseStatsRecvPauseDeltaMax_Type=Unsigned64
_CucsEtherPauseStatsRecvPauseDeltaMax_Object=MibTableColumn
cucsEtherPauseStatsRecvPauseDeltaMax=_CucsEtherPauseStatsRecvPauseDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,8),_CucsEtherPauseStatsRecvPauseDeltaMax_Type())
cucsEtherPauseStatsRecvPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsRecvPauseDeltaMax.setStatus(_A)
_CucsEtherPauseStatsRecvPauseDeltaMin_Type=Unsigned64
_CucsEtherPauseStatsRecvPauseDeltaMin_Object=MibTableColumn
cucsEtherPauseStatsRecvPauseDeltaMin=_CucsEtherPauseStatsRecvPauseDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,9),_CucsEtherPauseStatsRecvPauseDeltaMin_Type())
cucsEtherPauseStatsRecvPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsRecvPauseDeltaMin.setStatus(_A)
_CucsEtherPauseStatsResets_Type=Unsigned64
_CucsEtherPauseStatsResets_Object=MibTableColumn
cucsEtherPauseStatsResets=_CucsEtherPauseStatsResets_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,10),_CucsEtherPauseStatsResets_Type())
cucsEtherPauseStatsResets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsResets.setStatus(_A)
_CucsEtherPauseStatsResetsDelta_Type=Counter64
_CucsEtherPauseStatsResetsDelta_Object=MibTableColumn
cucsEtherPauseStatsResetsDelta=_CucsEtherPauseStatsResetsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,11),_CucsEtherPauseStatsResetsDelta_Type())
cucsEtherPauseStatsResetsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsResetsDelta.setStatus(_A)
_CucsEtherPauseStatsResetsDeltaAvg_Type=Unsigned64
_CucsEtherPauseStatsResetsDeltaAvg_Object=MibTableColumn
cucsEtherPauseStatsResetsDeltaAvg=_CucsEtherPauseStatsResetsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,12),_CucsEtherPauseStatsResetsDeltaAvg_Type())
cucsEtherPauseStatsResetsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsResetsDeltaAvg.setStatus(_A)
_CucsEtherPauseStatsResetsDeltaMax_Type=Unsigned64
_CucsEtherPauseStatsResetsDeltaMax_Object=MibTableColumn
cucsEtherPauseStatsResetsDeltaMax=_CucsEtherPauseStatsResetsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,13),_CucsEtherPauseStatsResetsDeltaMax_Type())
cucsEtherPauseStatsResetsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsResetsDeltaMax.setStatus(_A)
_CucsEtherPauseStatsResetsDeltaMin_Type=Unsigned64
_CucsEtherPauseStatsResetsDeltaMin_Object=MibTableColumn
cucsEtherPauseStatsResetsDeltaMin=_CucsEtherPauseStatsResetsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,14),_CucsEtherPauseStatsResetsDeltaMin_Type())
cucsEtherPauseStatsResetsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsResetsDeltaMin.setStatus(_A)
_CucsEtherPauseStatsSuspect_Type=TruthValue
_CucsEtherPauseStatsSuspect_Object=MibTableColumn
cucsEtherPauseStatsSuspect=_CucsEtherPauseStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,15),_CucsEtherPauseStatsSuspect_Type())
cucsEtherPauseStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsSuspect.setStatus(_A)
_CucsEtherPauseStatsThresholded_Type=CucsEtherPauseStatsThresholded
_CucsEtherPauseStatsThresholded_Object=MibTableColumn
cucsEtherPauseStatsThresholded=_CucsEtherPauseStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,16),_CucsEtherPauseStatsThresholded_Type())
cucsEtherPauseStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsThresholded.setStatus(_A)
_CucsEtherPauseStatsTimeCollected_Type=DateAndTime
_CucsEtherPauseStatsTimeCollected_Object=MibTableColumn
cucsEtherPauseStatsTimeCollected=_CucsEtherPauseStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,17),_CucsEtherPauseStatsTimeCollected_Type())
cucsEtherPauseStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsTimeCollected.setStatus(_A)
_CucsEtherPauseStatsUpdate_Type=Gauge32
_CucsEtherPauseStatsUpdate_Object=MibTableColumn
cucsEtherPauseStatsUpdate=_CucsEtherPauseStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,18),_CucsEtherPauseStatsUpdate_Type())
cucsEtherPauseStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsUpdate.setStatus(_A)
_CucsEtherPauseStatsXmitPause_Type=Unsigned64
_CucsEtherPauseStatsXmitPause_Object=MibTableColumn
cucsEtherPauseStatsXmitPause=_CucsEtherPauseStatsXmitPause_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,19),_CucsEtherPauseStatsXmitPause_Type())
cucsEtherPauseStatsXmitPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsXmitPause.setStatus(_A)
_CucsEtherPauseStatsXmitPauseDelta_Type=Counter64
_CucsEtherPauseStatsXmitPauseDelta_Object=MibTableColumn
cucsEtherPauseStatsXmitPauseDelta=_CucsEtherPauseStatsXmitPauseDelta_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,20),_CucsEtherPauseStatsXmitPauseDelta_Type())
cucsEtherPauseStatsXmitPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsXmitPauseDelta.setStatus(_A)
_CucsEtherPauseStatsXmitPauseDeltaAvg_Type=Unsigned64
_CucsEtherPauseStatsXmitPauseDeltaAvg_Object=MibTableColumn
cucsEtherPauseStatsXmitPauseDeltaAvg=_CucsEtherPauseStatsXmitPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,21),_CucsEtherPauseStatsXmitPauseDeltaAvg_Type())
cucsEtherPauseStatsXmitPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsXmitPauseDeltaAvg.setStatus(_A)
_CucsEtherPauseStatsXmitPauseDeltaMax_Type=Unsigned64
_CucsEtherPauseStatsXmitPauseDeltaMax_Object=MibTableColumn
cucsEtherPauseStatsXmitPauseDeltaMax=_CucsEtherPauseStatsXmitPauseDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,22),_CucsEtherPauseStatsXmitPauseDeltaMax_Type())
cucsEtherPauseStatsXmitPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsXmitPauseDeltaMax.setStatus(_A)
_CucsEtherPauseStatsXmitPauseDeltaMin_Type=Unsigned64
_CucsEtherPauseStatsXmitPauseDeltaMin_Object=MibTableColumn
cucsEtherPauseStatsXmitPauseDeltaMin=_CucsEtherPauseStatsXmitPauseDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,7,1,23),_CucsEtherPauseStatsXmitPauseDeltaMin_Type())
cucsEtherPauseStatsXmitPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsXmitPauseDeltaMin.setStatus(_A)
_CucsEtherPauseStatsHistTable_Object=MibTable
cucsEtherPauseStatsHistTable=_CucsEtherPauseStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,8))
if mibBuilder.loadTexts:cucsEtherPauseStatsHistTable.setStatus(_A)
_CucsEtherPauseStatsHistEntry_Object=MibTableRow
cucsEtherPauseStatsHistEntry=_CucsEtherPauseStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,8,1))
cucsEtherPauseStatsHistEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsEtherPauseStatsHistEntry.setStatus(_A)
_CucsEtherPauseStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherPauseStatsHistInstanceId_Object=MibTableColumn
cucsEtherPauseStatsHistInstanceId=_CucsEtherPauseStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,1),_CucsEtherPauseStatsHistInstanceId_Type())
cucsEtherPauseStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistInstanceId.setStatus(_A)
_CucsEtherPauseStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherPauseStatsHistDn_Object=MibTableColumn
cucsEtherPauseStatsHistDn=_CucsEtherPauseStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,2),_CucsEtherPauseStatsHistDn_Type())
cucsEtherPauseStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistDn.setStatus(_A)
_CucsEtherPauseStatsHistRn_Type=SnmpAdminString
_CucsEtherPauseStatsHistRn_Object=MibTableColumn
cucsEtherPauseStatsHistRn=_CucsEtherPauseStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,3),_CucsEtherPauseStatsHistRn_Type())
cucsEtherPauseStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistRn.setStatus(_A)
_CucsEtherPauseStatsHistId_Type=Unsigned64
_CucsEtherPauseStatsHistId_Object=MibTableColumn
cucsEtherPauseStatsHistId=_CucsEtherPauseStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,4),_CucsEtherPauseStatsHistId_Type())
cucsEtherPauseStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistId.setStatus(_A)
_CucsEtherPauseStatsHistMostRecent_Type=TruthValue
_CucsEtherPauseStatsHistMostRecent_Object=MibTableColumn
cucsEtherPauseStatsHistMostRecent=_CucsEtherPauseStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,5),_CucsEtherPauseStatsHistMostRecent_Type())
cucsEtherPauseStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistMostRecent.setStatus(_A)
_CucsEtherPauseStatsHistRecvPause_Type=Unsigned64
_CucsEtherPauseStatsHistRecvPause_Object=MibTableColumn
cucsEtherPauseStatsHistRecvPause=_CucsEtherPauseStatsHistRecvPause_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,6),_CucsEtherPauseStatsHistRecvPause_Type())
cucsEtherPauseStatsHistRecvPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistRecvPause.setStatus(_A)
_CucsEtherPauseStatsHistRecvPauseDelta_Type=Unsigned64
_CucsEtherPauseStatsHistRecvPauseDelta_Object=MibTableColumn
cucsEtherPauseStatsHistRecvPauseDelta=_CucsEtherPauseStatsHistRecvPauseDelta_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,7),_CucsEtherPauseStatsHistRecvPauseDelta_Type())
cucsEtherPauseStatsHistRecvPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistRecvPauseDelta.setStatus(_A)
_CucsEtherPauseStatsHistRecvPauseDeltaAvg_Type=Unsigned64
_CucsEtherPauseStatsHistRecvPauseDeltaAvg_Object=MibTableColumn
cucsEtherPauseStatsHistRecvPauseDeltaAvg=_CucsEtherPauseStatsHistRecvPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,8),_CucsEtherPauseStatsHistRecvPauseDeltaAvg_Type())
cucsEtherPauseStatsHistRecvPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistRecvPauseDeltaAvg.setStatus(_A)
_CucsEtherPauseStatsHistRecvPauseDeltaMax_Type=Unsigned64
_CucsEtherPauseStatsHistRecvPauseDeltaMax_Object=MibTableColumn
cucsEtherPauseStatsHistRecvPauseDeltaMax=_CucsEtherPauseStatsHistRecvPauseDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,9),_CucsEtherPauseStatsHistRecvPauseDeltaMax_Type())
cucsEtherPauseStatsHistRecvPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistRecvPauseDeltaMax.setStatus(_A)
_CucsEtherPauseStatsHistRecvPauseDeltaMin_Type=Unsigned64
_CucsEtherPauseStatsHistRecvPauseDeltaMin_Object=MibTableColumn
cucsEtherPauseStatsHistRecvPauseDeltaMin=_CucsEtherPauseStatsHistRecvPauseDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,10),_CucsEtherPauseStatsHistRecvPauseDeltaMin_Type())
cucsEtherPauseStatsHistRecvPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistRecvPauseDeltaMin.setStatus(_A)
_CucsEtherPauseStatsHistResets_Type=Unsigned64
_CucsEtherPauseStatsHistResets_Object=MibTableColumn
cucsEtherPauseStatsHistResets=_CucsEtherPauseStatsHistResets_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,11),_CucsEtherPauseStatsHistResets_Type())
cucsEtherPauseStatsHistResets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistResets.setStatus(_A)
_CucsEtherPauseStatsHistResetsDelta_Type=Unsigned64
_CucsEtherPauseStatsHistResetsDelta_Object=MibTableColumn
cucsEtherPauseStatsHistResetsDelta=_CucsEtherPauseStatsHistResetsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,12),_CucsEtherPauseStatsHistResetsDelta_Type())
cucsEtherPauseStatsHistResetsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistResetsDelta.setStatus(_A)
_CucsEtherPauseStatsHistResetsDeltaAvg_Type=Unsigned64
_CucsEtherPauseStatsHistResetsDeltaAvg_Object=MibTableColumn
cucsEtherPauseStatsHistResetsDeltaAvg=_CucsEtherPauseStatsHistResetsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,13),_CucsEtherPauseStatsHistResetsDeltaAvg_Type())
cucsEtherPauseStatsHistResetsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistResetsDeltaAvg.setStatus(_A)
_CucsEtherPauseStatsHistResetsDeltaMax_Type=Unsigned64
_CucsEtherPauseStatsHistResetsDeltaMax_Object=MibTableColumn
cucsEtherPauseStatsHistResetsDeltaMax=_CucsEtherPauseStatsHistResetsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,14),_CucsEtherPauseStatsHistResetsDeltaMax_Type())
cucsEtherPauseStatsHistResetsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistResetsDeltaMax.setStatus(_A)
_CucsEtherPauseStatsHistResetsDeltaMin_Type=Unsigned64
_CucsEtherPauseStatsHistResetsDeltaMin_Object=MibTableColumn
cucsEtherPauseStatsHistResetsDeltaMin=_CucsEtherPauseStatsHistResetsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,15),_CucsEtherPauseStatsHistResetsDeltaMin_Type())
cucsEtherPauseStatsHistResetsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistResetsDeltaMin.setStatus(_A)
_CucsEtherPauseStatsHistSuspect_Type=TruthValue
_CucsEtherPauseStatsHistSuspect_Object=MibTableColumn
cucsEtherPauseStatsHistSuspect=_CucsEtherPauseStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,16),_CucsEtherPauseStatsHistSuspect_Type())
cucsEtherPauseStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistSuspect.setStatus(_A)
_CucsEtherPauseStatsHistThresholded_Type=CucsEtherPauseStatsHistThresholded
_CucsEtherPauseStatsHistThresholded_Object=MibTableColumn
cucsEtherPauseStatsHistThresholded=_CucsEtherPauseStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,17),_CucsEtherPauseStatsHistThresholded_Type())
cucsEtherPauseStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistThresholded.setStatus(_A)
_CucsEtherPauseStatsHistTimeCollected_Type=DateAndTime
_CucsEtherPauseStatsHistTimeCollected_Object=MibTableColumn
cucsEtherPauseStatsHistTimeCollected=_CucsEtherPauseStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,18),_CucsEtherPauseStatsHistTimeCollected_Type())
cucsEtherPauseStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistTimeCollected.setStatus(_A)
_CucsEtherPauseStatsHistXmitPause_Type=Unsigned64
_CucsEtherPauseStatsHistXmitPause_Object=MibTableColumn
cucsEtherPauseStatsHistXmitPause=_CucsEtherPauseStatsHistXmitPause_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,19),_CucsEtherPauseStatsHistXmitPause_Type())
cucsEtherPauseStatsHistXmitPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistXmitPause.setStatus(_A)
_CucsEtherPauseStatsHistXmitPauseDelta_Type=Unsigned64
_CucsEtherPauseStatsHistXmitPauseDelta_Object=MibTableColumn
cucsEtherPauseStatsHistXmitPauseDelta=_CucsEtherPauseStatsHistXmitPauseDelta_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,20),_CucsEtherPauseStatsHistXmitPauseDelta_Type())
cucsEtherPauseStatsHistXmitPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistXmitPauseDelta.setStatus(_A)
_CucsEtherPauseStatsHistXmitPauseDeltaAvg_Type=Unsigned64
_CucsEtherPauseStatsHistXmitPauseDeltaAvg_Object=MibTableColumn
cucsEtherPauseStatsHistXmitPauseDeltaAvg=_CucsEtherPauseStatsHistXmitPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,21),_CucsEtherPauseStatsHistXmitPauseDeltaAvg_Type())
cucsEtherPauseStatsHistXmitPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistXmitPauseDeltaAvg.setStatus(_A)
_CucsEtherPauseStatsHistXmitPauseDeltaMax_Type=Unsigned64
_CucsEtherPauseStatsHistXmitPauseDeltaMax_Object=MibTableColumn
cucsEtherPauseStatsHistXmitPauseDeltaMax=_CucsEtherPauseStatsHistXmitPauseDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,22),_CucsEtherPauseStatsHistXmitPauseDeltaMax_Type())
cucsEtherPauseStatsHistXmitPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistXmitPauseDeltaMax.setStatus(_A)
_CucsEtherPauseStatsHistXmitPauseDeltaMin_Type=Unsigned64
_CucsEtherPauseStatsHistXmitPauseDeltaMin_Object=MibTableColumn
cucsEtherPauseStatsHistXmitPauseDeltaMin=_CucsEtherPauseStatsHistXmitPauseDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,8,1,23),_CucsEtherPauseStatsHistXmitPauseDeltaMin_Type())
cucsEtherPauseStatsHistXmitPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPauseStatsHistXmitPauseDeltaMin.setStatus(_A)
_CucsEtherRxStatsTable_Object=MibTable
cucsEtherRxStatsTable=_CucsEtherRxStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,9))
if mibBuilder.loadTexts:cucsEtherRxStatsTable.setStatus(_A)
_CucsEtherRxStatsEntry_Object=MibTableRow
cucsEtherRxStatsEntry=_CucsEtherRxStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,9,1))
cucsEtherRxStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsEtherRxStatsEntry.setStatus(_A)
_CucsEtherRxStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherRxStatsInstanceId_Object=MibTableColumn
cucsEtherRxStatsInstanceId=_CucsEtherRxStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,1),_CucsEtherRxStatsInstanceId_Type())
cucsEtherRxStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherRxStatsInstanceId.setStatus(_A)
_CucsEtherRxStatsDn_Type=CucsManagedObjectDn
_CucsEtherRxStatsDn_Object=MibTableColumn
cucsEtherRxStatsDn=_CucsEtherRxStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,2),_CucsEtherRxStatsDn_Type())
cucsEtherRxStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsDn.setStatus(_A)
_CucsEtherRxStatsRn_Type=SnmpAdminString
_CucsEtherRxStatsRn_Object=MibTableColumn
cucsEtherRxStatsRn=_CucsEtherRxStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,3),_CucsEtherRxStatsRn_Type())
cucsEtherRxStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsRn.setStatus(_A)
_CucsEtherRxStatsBroadcastPackets_Type=Unsigned64
_CucsEtherRxStatsBroadcastPackets_Object=MibTableColumn
cucsEtherRxStatsBroadcastPackets=_CucsEtherRxStatsBroadcastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,4),_CucsEtherRxStatsBroadcastPackets_Type())
cucsEtherRxStatsBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsBroadcastPackets.setStatus(_A)
_CucsEtherRxStatsBroadcastPacketsDelta_Type=Counter64
_CucsEtherRxStatsBroadcastPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsBroadcastPacketsDelta=_CucsEtherRxStatsBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,5),_CucsEtherRxStatsBroadcastPacketsDelta_Type())
cucsEtherRxStatsBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsBroadcastPacketsDelta.setStatus(_A)
_CucsEtherRxStatsBroadcastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsBroadcastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsBroadcastPacketsDeltaAvg=_CucsEtherRxStatsBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,6),_CucsEtherRxStatsBroadcastPacketsDeltaAvg_Type())
cucsEtherRxStatsBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsBroadcastPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsBroadcastPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsBroadcastPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsBroadcastPacketsDeltaMax=_CucsEtherRxStatsBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,7),_CucsEtherRxStatsBroadcastPacketsDeltaMax_Type())
cucsEtherRxStatsBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsBroadcastPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsBroadcastPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsBroadcastPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsBroadcastPacketsDeltaMin=_CucsEtherRxStatsBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,8),_CucsEtherRxStatsBroadcastPacketsDeltaMin_Type())
cucsEtherRxStatsBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsBroadcastPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsIntervals_Type=Gauge32
_CucsEtherRxStatsIntervals_Object=MibTableColumn
cucsEtherRxStatsIntervals=_CucsEtherRxStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,9),_CucsEtherRxStatsIntervals_Type())
cucsEtherRxStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsIntervals.setStatus(_A)
_CucsEtherRxStatsJumboPackets_Type=Unsigned64
_CucsEtherRxStatsJumboPackets_Object=MibTableColumn
cucsEtherRxStatsJumboPackets=_CucsEtherRxStatsJumboPackets_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,10),_CucsEtherRxStatsJumboPackets_Type())
cucsEtherRxStatsJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsJumboPackets.setStatus(_A)
_CucsEtherRxStatsJumboPacketsDelta_Type=Counter64
_CucsEtherRxStatsJumboPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsJumboPacketsDelta=_CucsEtherRxStatsJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,11),_CucsEtherRxStatsJumboPacketsDelta_Type())
cucsEtherRxStatsJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsJumboPacketsDelta.setStatus(_A)
_CucsEtherRxStatsJumboPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsJumboPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsJumboPacketsDeltaAvg=_CucsEtherRxStatsJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,12),_CucsEtherRxStatsJumboPacketsDeltaAvg_Type())
cucsEtherRxStatsJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsJumboPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsJumboPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsJumboPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsJumboPacketsDeltaMax=_CucsEtherRxStatsJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,13),_CucsEtherRxStatsJumboPacketsDeltaMax_Type())
cucsEtherRxStatsJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsJumboPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsJumboPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsJumboPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsJumboPacketsDeltaMin=_CucsEtherRxStatsJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,14),_CucsEtherRxStatsJumboPacketsDeltaMin_Type())
cucsEtherRxStatsJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsJumboPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsMulticastPackets_Type=Unsigned64
_CucsEtherRxStatsMulticastPackets_Object=MibTableColumn
cucsEtherRxStatsMulticastPackets=_CucsEtherRxStatsMulticastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,15),_CucsEtherRxStatsMulticastPackets_Type())
cucsEtherRxStatsMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsMulticastPackets.setStatus(_A)
_CucsEtherRxStatsMulticastPacketsDelta_Type=Counter64
_CucsEtherRxStatsMulticastPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsMulticastPacketsDelta=_CucsEtherRxStatsMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,16),_CucsEtherRxStatsMulticastPacketsDelta_Type())
cucsEtherRxStatsMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsMulticastPacketsDelta.setStatus(_A)
_CucsEtherRxStatsMulticastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsMulticastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsMulticastPacketsDeltaAvg=_CucsEtherRxStatsMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,17),_CucsEtherRxStatsMulticastPacketsDeltaAvg_Type())
cucsEtherRxStatsMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsMulticastPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsMulticastPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsMulticastPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsMulticastPacketsDeltaMax=_CucsEtherRxStatsMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,18),_CucsEtherRxStatsMulticastPacketsDeltaMax_Type())
cucsEtherRxStatsMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsMulticastPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsMulticastPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsMulticastPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsMulticastPacketsDeltaMin=_CucsEtherRxStatsMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,19),_CucsEtherRxStatsMulticastPacketsDeltaMin_Type())
cucsEtherRxStatsMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsMulticastPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsSuspect_Type=TruthValue
_CucsEtherRxStatsSuspect_Object=MibTableColumn
cucsEtherRxStatsSuspect=_CucsEtherRxStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,20),_CucsEtherRxStatsSuspect_Type())
cucsEtherRxStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsSuspect.setStatus(_A)
_CucsEtherRxStatsThresholded_Type=CucsEtherRxStatsThresholded
_CucsEtherRxStatsThresholded_Object=MibTableColumn
cucsEtherRxStatsThresholded=_CucsEtherRxStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,21),_CucsEtherRxStatsThresholded_Type())
cucsEtherRxStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsThresholded.setStatus(_A)
_CucsEtherRxStatsTimeCollected_Type=DateAndTime
_CucsEtherRxStatsTimeCollected_Object=MibTableColumn
cucsEtherRxStatsTimeCollected=_CucsEtherRxStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,22),_CucsEtherRxStatsTimeCollected_Type())
cucsEtherRxStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTimeCollected.setStatus(_A)
_CucsEtherRxStatsTotalBytes_Type=Unsigned64
_CucsEtherRxStatsTotalBytes_Object=MibTableColumn
cucsEtherRxStatsTotalBytes=_CucsEtherRxStatsTotalBytes_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,23),_CucsEtherRxStatsTotalBytes_Type())
cucsEtherRxStatsTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalBytes.setStatus(_A)
_CucsEtherRxStatsTotalBytesDelta_Type=Counter64
_CucsEtherRxStatsTotalBytesDelta_Object=MibTableColumn
cucsEtherRxStatsTotalBytesDelta=_CucsEtherRxStatsTotalBytesDelta_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,24),_CucsEtherRxStatsTotalBytesDelta_Type())
cucsEtherRxStatsTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalBytesDelta.setStatus(_A)
_CucsEtherRxStatsTotalBytesDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsTotalBytesDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsTotalBytesDeltaAvg=_CucsEtherRxStatsTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,25),_CucsEtherRxStatsTotalBytesDeltaAvg_Type())
cucsEtherRxStatsTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalBytesDeltaAvg.setStatus(_A)
_CucsEtherRxStatsTotalBytesDeltaMax_Type=Unsigned64
_CucsEtherRxStatsTotalBytesDeltaMax_Object=MibTableColumn
cucsEtherRxStatsTotalBytesDeltaMax=_CucsEtherRxStatsTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,26),_CucsEtherRxStatsTotalBytesDeltaMax_Type())
cucsEtherRxStatsTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalBytesDeltaMax.setStatus(_A)
_CucsEtherRxStatsTotalBytesDeltaMin_Type=Unsigned64
_CucsEtherRxStatsTotalBytesDeltaMin_Object=MibTableColumn
cucsEtherRxStatsTotalBytesDeltaMin=_CucsEtherRxStatsTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,27),_CucsEtherRxStatsTotalBytesDeltaMin_Type())
cucsEtherRxStatsTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalBytesDeltaMin.setStatus(_A)
_CucsEtherRxStatsTotalPackets_Type=Unsigned64
_CucsEtherRxStatsTotalPackets_Object=MibTableColumn
cucsEtherRxStatsTotalPackets=_CucsEtherRxStatsTotalPackets_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,28),_CucsEtherRxStatsTotalPackets_Type())
cucsEtherRxStatsTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalPackets.setStatus(_A)
_CucsEtherRxStatsTotalPacketsDelta_Type=Counter64
_CucsEtherRxStatsTotalPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsTotalPacketsDelta=_CucsEtherRxStatsTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,29),_CucsEtherRxStatsTotalPacketsDelta_Type())
cucsEtherRxStatsTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalPacketsDelta.setStatus(_A)
_CucsEtherRxStatsTotalPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsTotalPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsTotalPacketsDeltaAvg=_CucsEtherRxStatsTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,30),_CucsEtherRxStatsTotalPacketsDeltaAvg_Type())
cucsEtherRxStatsTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsTotalPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsTotalPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsTotalPacketsDeltaMax=_CucsEtherRxStatsTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,31),_CucsEtherRxStatsTotalPacketsDeltaMax_Type())
cucsEtherRxStatsTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsTotalPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsTotalPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsTotalPacketsDeltaMin=_CucsEtherRxStatsTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,32),_CucsEtherRxStatsTotalPacketsDeltaMin_Type())
cucsEtherRxStatsTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsTotalPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsUnicastPackets_Type=Unsigned64
_CucsEtherRxStatsUnicastPackets_Object=MibTableColumn
cucsEtherRxStatsUnicastPackets=_CucsEtherRxStatsUnicastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,33),_CucsEtherRxStatsUnicastPackets_Type())
cucsEtherRxStatsUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsUnicastPackets.setStatus(_A)
_CucsEtherRxStatsUnicastPacketsDelta_Type=Counter64
_CucsEtherRxStatsUnicastPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsUnicastPacketsDelta=_CucsEtherRxStatsUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,34),_CucsEtherRxStatsUnicastPacketsDelta_Type())
cucsEtherRxStatsUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsUnicastPacketsDelta.setStatus(_A)
_CucsEtherRxStatsUnicastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsUnicastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsUnicastPacketsDeltaAvg=_CucsEtherRxStatsUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,35),_CucsEtherRxStatsUnicastPacketsDeltaAvg_Type())
cucsEtherRxStatsUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsUnicastPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsUnicastPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsUnicastPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsUnicastPacketsDeltaMax=_CucsEtherRxStatsUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,36),_CucsEtherRxStatsUnicastPacketsDeltaMax_Type())
cucsEtherRxStatsUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsUnicastPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsUnicastPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsUnicastPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsUnicastPacketsDeltaMin=_CucsEtherRxStatsUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,37),_CucsEtherRxStatsUnicastPacketsDeltaMin_Type())
cucsEtherRxStatsUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsUnicastPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsUpdate_Type=Gauge32
_CucsEtherRxStatsUpdate_Object=MibTableColumn
cucsEtherRxStatsUpdate=_CucsEtherRxStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,9,1,38),_CucsEtherRxStatsUpdate_Type())
cucsEtherRxStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsUpdate.setStatus(_A)
_CucsEtherRxStatsHistTable_Object=MibTable
cucsEtherRxStatsHistTable=_CucsEtherRxStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,10))
if mibBuilder.loadTexts:cucsEtherRxStatsHistTable.setStatus(_A)
_CucsEtherRxStatsHistEntry_Object=MibTableRow
cucsEtherRxStatsHistEntry=_CucsEtherRxStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,10,1))
cucsEtherRxStatsHistEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsEtherRxStatsHistEntry.setStatus(_A)
_CucsEtherRxStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherRxStatsHistInstanceId_Object=MibTableColumn
cucsEtherRxStatsHistInstanceId=_CucsEtherRxStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,1),_CucsEtherRxStatsHistInstanceId_Type())
cucsEtherRxStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherRxStatsHistInstanceId.setStatus(_A)
_CucsEtherRxStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherRxStatsHistDn_Object=MibTableColumn
cucsEtherRxStatsHistDn=_CucsEtherRxStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,2),_CucsEtherRxStatsHistDn_Type())
cucsEtherRxStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistDn.setStatus(_A)
_CucsEtherRxStatsHistRn_Type=SnmpAdminString
_CucsEtherRxStatsHistRn_Object=MibTableColumn
cucsEtherRxStatsHistRn=_CucsEtherRxStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,3),_CucsEtherRxStatsHistRn_Type())
cucsEtherRxStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistRn.setStatus(_A)
_CucsEtherRxStatsHistBroadcastPackets_Type=Unsigned64
_CucsEtherRxStatsHistBroadcastPackets_Object=MibTableColumn
cucsEtherRxStatsHistBroadcastPackets=_CucsEtherRxStatsHistBroadcastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,4),_CucsEtherRxStatsHistBroadcastPackets_Type())
cucsEtherRxStatsHistBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistBroadcastPackets.setStatus(_A)
_CucsEtherRxStatsHistBroadcastPacketsDelta_Type=Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDelta=_CucsEtherRxStatsHistBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,5),_CucsEtherRxStatsHistBroadcastPacketsDelta_Type())
cucsEtherRxStatsHistBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistBroadcastPacketsDelta.setStatus(_A)
_CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDeltaAvg=_CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,6),_CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Type())
cucsEtherRxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistBroadcastPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDeltaMax=_CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,7),_CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Type())
cucsEtherRxStatsHistBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistBroadcastPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDeltaMin=_CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,8),_CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Type())
cucsEtherRxStatsHistBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistBroadcastPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsHistId_Type=Unsigned64
_CucsEtherRxStatsHistId_Object=MibTableColumn
cucsEtherRxStatsHistId=_CucsEtherRxStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,9),_CucsEtherRxStatsHistId_Type())
cucsEtherRxStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistId.setStatus(_A)
_CucsEtherRxStatsHistJumboPackets_Type=Unsigned64
_CucsEtherRxStatsHistJumboPackets_Object=MibTableColumn
cucsEtherRxStatsHistJumboPackets=_CucsEtherRxStatsHistJumboPackets_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,10),_CucsEtherRxStatsHistJumboPackets_Type())
cucsEtherRxStatsHistJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistJumboPackets.setStatus(_A)
_CucsEtherRxStatsHistJumboPacketsDelta_Type=Unsigned64
_CucsEtherRxStatsHistJumboPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsHistJumboPacketsDelta=_CucsEtherRxStatsHistJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,11),_CucsEtherRxStatsHistJumboPacketsDelta_Type())
cucsEtherRxStatsHistJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistJumboPacketsDelta.setStatus(_A)
_CucsEtherRxStatsHistJumboPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsHistJumboPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsHistJumboPacketsDeltaAvg=_CucsEtherRxStatsHistJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,12),_CucsEtherRxStatsHistJumboPacketsDeltaAvg_Type())
cucsEtherRxStatsHistJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistJumboPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsHistJumboPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsHistJumboPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsHistJumboPacketsDeltaMax=_CucsEtherRxStatsHistJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,13),_CucsEtherRxStatsHistJumboPacketsDeltaMax_Type())
cucsEtherRxStatsHistJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistJumboPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsHistJumboPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsHistJumboPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsHistJumboPacketsDeltaMin=_CucsEtherRxStatsHistJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,14),_CucsEtherRxStatsHistJumboPacketsDeltaMin_Type())
cucsEtherRxStatsHistJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistJumboPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsHistMostRecent_Type=TruthValue
_CucsEtherRxStatsHistMostRecent_Object=MibTableColumn
cucsEtherRxStatsHistMostRecent=_CucsEtherRxStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,15),_CucsEtherRxStatsHistMostRecent_Type())
cucsEtherRxStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistMostRecent.setStatus(_A)
_CucsEtherRxStatsHistMulticastPackets_Type=Unsigned64
_CucsEtherRxStatsHistMulticastPackets_Object=MibTableColumn
cucsEtherRxStatsHistMulticastPackets=_CucsEtherRxStatsHistMulticastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,16),_CucsEtherRxStatsHistMulticastPackets_Type())
cucsEtherRxStatsHistMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistMulticastPackets.setStatus(_A)
_CucsEtherRxStatsHistMulticastPacketsDelta_Type=Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDelta=_CucsEtherRxStatsHistMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,17),_CucsEtherRxStatsHistMulticastPacketsDelta_Type())
cucsEtherRxStatsHistMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistMulticastPacketsDelta.setStatus(_A)
_CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDeltaAvg=_CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,18),_CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Type())
cucsEtherRxStatsHistMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistMulticastPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsHistMulticastPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDeltaMax=_CucsEtherRxStatsHistMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,19),_CucsEtherRxStatsHistMulticastPacketsDeltaMax_Type())
cucsEtherRxStatsHistMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistMulticastPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsHistMulticastPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDeltaMin=_CucsEtherRxStatsHistMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,20),_CucsEtherRxStatsHistMulticastPacketsDeltaMin_Type())
cucsEtherRxStatsHistMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistMulticastPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsHistSuspect_Type=TruthValue
_CucsEtherRxStatsHistSuspect_Object=MibTableColumn
cucsEtherRxStatsHistSuspect=_CucsEtherRxStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,21),_CucsEtherRxStatsHistSuspect_Type())
cucsEtherRxStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistSuspect.setStatus(_A)
_CucsEtherRxStatsHistThresholded_Type=CucsEtherRxStatsHistThresholded
_CucsEtherRxStatsHistThresholded_Object=MibTableColumn
cucsEtherRxStatsHistThresholded=_CucsEtherRxStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,22),_CucsEtherRxStatsHistThresholded_Type())
cucsEtherRxStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistThresholded.setStatus(_A)
_CucsEtherRxStatsHistTimeCollected_Type=DateAndTime
_CucsEtherRxStatsHistTimeCollected_Object=MibTableColumn
cucsEtherRxStatsHistTimeCollected=_CucsEtherRxStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,23),_CucsEtherRxStatsHistTimeCollected_Type())
cucsEtherRxStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTimeCollected.setStatus(_A)
_CucsEtherRxStatsHistTotalBytes_Type=Unsigned64
_CucsEtherRxStatsHistTotalBytes_Object=MibTableColumn
cucsEtherRxStatsHistTotalBytes=_CucsEtherRxStatsHistTotalBytes_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,24),_CucsEtherRxStatsHistTotalBytes_Type())
cucsEtherRxStatsHistTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalBytes.setStatus(_A)
_CucsEtherRxStatsHistTotalBytesDelta_Type=Unsigned64
_CucsEtherRxStatsHistTotalBytesDelta_Object=MibTableColumn
cucsEtherRxStatsHistTotalBytesDelta=_CucsEtherRxStatsHistTotalBytesDelta_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,25),_CucsEtherRxStatsHistTotalBytesDelta_Type())
cucsEtherRxStatsHistTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalBytesDelta.setStatus(_A)
_CucsEtherRxStatsHistTotalBytesDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsHistTotalBytesDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsHistTotalBytesDeltaAvg=_CucsEtherRxStatsHistTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,26),_CucsEtherRxStatsHistTotalBytesDeltaAvg_Type())
cucsEtherRxStatsHistTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalBytesDeltaAvg.setStatus(_A)
_CucsEtherRxStatsHistTotalBytesDeltaMax_Type=Unsigned64
_CucsEtherRxStatsHistTotalBytesDeltaMax_Object=MibTableColumn
cucsEtherRxStatsHistTotalBytesDeltaMax=_CucsEtherRxStatsHistTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,27),_CucsEtherRxStatsHistTotalBytesDeltaMax_Type())
cucsEtherRxStatsHistTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalBytesDeltaMax.setStatus(_A)
_CucsEtherRxStatsHistTotalBytesDeltaMin_Type=Unsigned64
_CucsEtherRxStatsHistTotalBytesDeltaMin_Object=MibTableColumn
cucsEtherRxStatsHistTotalBytesDeltaMin=_CucsEtherRxStatsHistTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,28),_CucsEtherRxStatsHistTotalBytesDeltaMin_Type())
cucsEtherRxStatsHistTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalBytesDeltaMin.setStatus(_A)
_CucsEtherRxStatsHistTotalPackets_Type=Unsigned64
_CucsEtherRxStatsHistTotalPackets_Object=MibTableColumn
cucsEtherRxStatsHistTotalPackets=_CucsEtherRxStatsHistTotalPackets_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,29),_CucsEtherRxStatsHistTotalPackets_Type())
cucsEtherRxStatsHistTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalPackets.setStatus(_A)
_CucsEtherRxStatsHistTotalPacketsDelta_Type=Unsigned64
_CucsEtherRxStatsHistTotalPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsHistTotalPacketsDelta=_CucsEtherRxStatsHistTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,30),_CucsEtherRxStatsHistTotalPacketsDelta_Type())
cucsEtherRxStatsHistTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalPacketsDelta.setStatus(_A)
_CucsEtherRxStatsHistTotalPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsHistTotalPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsHistTotalPacketsDeltaAvg=_CucsEtherRxStatsHistTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,31),_CucsEtherRxStatsHistTotalPacketsDeltaAvg_Type())
cucsEtherRxStatsHistTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsHistTotalPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsHistTotalPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsHistTotalPacketsDeltaMax=_CucsEtherRxStatsHistTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,32),_CucsEtherRxStatsHistTotalPacketsDeltaMax_Type())
cucsEtherRxStatsHistTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsHistTotalPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsHistTotalPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsHistTotalPacketsDeltaMin=_CucsEtherRxStatsHistTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,33),_CucsEtherRxStatsHistTotalPacketsDeltaMin_Type())
cucsEtherRxStatsHistTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistTotalPacketsDeltaMin.setStatus(_A)
_CucsEtherRxStatsHistUnicastPackets_Type=Unsigned64
_CucsEtherRxStatsHistUnicastPackets_Object=MibTableColumn
cucsEtherRxStatsHistUnicastPackets=_CucsEtherRxStatsHistUnicastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,34),_CucsEtherRxStatsHistUnicastPackets_Type())
cucsEtherRxStatsHistUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistUnicastPackets.setStatus(_A)
_CucsEtherRxStatsHistUnicastPacketsDelta_Type=Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDelta_Object=MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDelta=_CucsEtherRxStatsHistUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,35),_CucsEtherRxStatsHistUnicastPacketsDelta_Type())
cucsEtherRxStatsHistUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistUnicastPacketsDelta.setStatus(_A)
_CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDeltaAvg=_CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,36),_CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Type())
cucsEtherRxStatsHistUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistUnicastPacketsDeltaAvg.setStatus(_A)
_CucsEtherRxStatsHistUnicastPacketsDeltaMax_Type=Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDeltaMax_Object=MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDeltaMax=_CucsEtherRxStatsHistUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,37),_CucsEtherRxStatsHistUnicastPacketsDeltaMax_Type())
cucsEtherRxStatsHistUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistUnicastPacketsDeltaMax.setStatus(_A)
_CucsEtherRxStatsHistUnicastPacketsDeltaMin_Type=Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDeltaMin_Object=MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDeltaMin=_CucsEtherRxStatsHistUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,10,1,38),_CucsEtherRxStatsHistUnicastPacketsDeltaMin_Type())
cucsEtherRxStatsHistUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherRxStatsHistUnicastPacketsDeltaMin.setStatus(_A)
_CucsEtherServerIntFIoTable_Object=MibTable
cucsEtherServerIntFIoTable=_CucsEtherServerIntFIoTable_Object((1,3,6,1,4,1,9,9,719,1,16,11))
if mibBuilder.loadTexts:cucsEtherServerIntFIoTable.setStatus(_A)
_CucsEtherServerIntFIoEntry_Object=MibTableRow
cucsEtherServerIntFIoEntry=_CucsEtherServerIntFIoEntry_Object((1,3,6,1,4,1,9,9,719,1,16,11,1))
cucsEtherServerIntFIoEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsEtherServerIntFIoEntry.setStatus(_A)
_CucsEtherServerIntFIoInstanceId_Type=CucsManagedObjectId
_CucsEtherServerIntFIoInstanceId_Object=MibTableColumn
cucsEtherServerIntFIoInstanceId=_CucsEtherServerIntFIoInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,1),_CucsEtherServerIntFIoInstanceId_Type())
cucsEtherServerIntFIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherServerIntFIoInstanceId.setStatus(_A)
_CucsEtherServerIntFIoDn_Type=CucsManagedObjectDn
_CucsEtherServerIntFIoDn_Object=MibTableColumn
cucsEtherServerIntFIoDn=_CucsEtherServerIntFIoDn_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,2),_CucsEtherServerIntFIoDn_Type())
cucsEtherServerIntFIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoDn.setStatus(_A)
_CucsEtherServerIntFIoRn_Type=SnmpAdminString
_CucsEtherServerIntFIoRn_Object=MibTableColumn
cucsEtherServerIntFIoRn=_CucsEtherServerIntFIoRn_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,3),_CucsEtherServerIntFIoRn_Type())
cucsEtherServerIntFIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoRn.setStatus(_A)
_CucsEtherServerIntFIoAdminState_Type=CucsEtherServerIntFIoAdminState
_CucsEtherServerIntFIoAdminState_Object=MibTableColumn
cucsEtherServerIntFIoAdminState=_CucsEtherServerIntFIoAdminState_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,4),_CucsEtherServerIntFIoAdminState_Type())
cucsEtherServerIntFIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoAdminState.setStatus(_A)
_CucsEtherServerIntFIoChassisId_Type=Gauge32
_CucsEtherServerIntFIoChassisId_Object=MibTableColumn
cucsEtherServerIntFIoChassisId=_CucsEtherServerIntFIoChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,5),_CucsEtherServerIntFIoChassisId_Type())
cucsEtherServerIntFIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoChassisId.setStatus(_A)
_CucsEtherServerIntFIoEncap_Type=CucsPortEncap
_CucsEtherServerIntFIoEncap_Object=MibTableColumn
cucsEtherServerIntFIoEncap=_CucsEtherServerIntFIoEncap_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,6),_CucsEtherServerIntFIoEncap_Type())
cucsEtherServerIntFIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoEncap.setStatus(_A)
_CucsEtherServerIntFIoEpDn_Type=SnmpAdminString
_CucsEtherServerIntFIoEpDn_Object=MibTableColumn
cucsEtherServerIntFIoEpDn=_CucsEtherServerIntFIoEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,7),_CucsEtherServerIntFIoEpDn_Type())
cucsEtherServerIntFIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoEpDn.setStatus(_A)
_CucsEtherServerIntFIoFltAggr_Type=Unsigned64
_CucsEtherServerIntFIoFltAggr_Object=MibTableColumn
cucsEtherServerIntFIoFltAggr=_CucsEtherServerIntFIoFltAggr_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,8),_CucsEtherServerIntFIoFltAggr_Type())
cucsEtherServerIntFIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFltAggr.setStatus(_A)
_CucsEtherServerIntFIoIfRole_Type=CucsEtherServerIntFIoIfRole
_CucsEtherServerIntFIoIfRole_Object=MibTableColumn
cucsEtherServerIntFIoIfRole=_CucsEtherServerIntFIoIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,9),_CucsEtherServerIntFIoIfRole_Type())
cucsEtherServerIntFIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoIfRole.setStatus(_A)
_CucsEtherServerIntFIoIfType_Type=CucsNetworkPhysEpIfType
_CucsEtherServerIntFIoIfType_Object=MibTableColumn
cucsEtherServerIntFIoIfType=_CucsEtherServerIntFIoIfType_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,10),_CucsEtherServerIntFIoIfType_Type())
cucsEtherServerIntFIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoIfType.setStatus(_A)
_CucsEtherServerIntFIoLocale_Type=CucsEtherServerIntFIoLocale
_CucsEtherServerIntFIoLocale_Object=MibTableColumn
cucsEtherServerIntFIoLocale=_CucsEtherServerIntFIoLocale_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,11),_CucsEtherServerIntFIoLocale_Type())
cucsEtherServerIntFIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoLocale.setStatus(_A)
_CucsEtherServerIntFIoMode_Type=CucsPortMode
_CucsEtherServerIntFIoMode_Object=MibTableColumn
cucsEtherServerIntFIoMode=_CucsEtherServerIntFIoMode_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,12),_CucsEtherServerIntFIoMode_Type())
cucsEtherServerIntFIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoMode.setStatus(_A)
_CucsEtherServerIntFIoModel_Type=SnmpAdminString
_CucsEtherServerIntFIoModel_Object=MibTableColumn
cucsEtherServerIntFIoModel=_CucsEtherServerIntFIoModel_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,13),_CucsEtherServerIntFIoModel_Type())
cucsEtherServerIntFIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoModel.setStatus(_A)
_CucsEtherServerIntFIoName_Type=SnmpAdminString
_CucsEtherServerIntFIoName_Object=MibTableColumn
cucsEtherServerIntFIoName=_CucsEtherServerIntFIoName_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,14),_CucsEtherServerIntFIoName_Type())
cucsEtherServerIntFIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoName.setStatus(_A)
_CucsEtherServerIntFIoOperBorderPortId_Type=Gauge32
_CucsEtherServerIntFIoOperBorderPortId_Object=MibTableColumn
cucsEtherServerIntFIoOperBorderPortId=_CucsEtherServerIntFIoOperBorderPortId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,15),_CucsEtherServerIntFIoOperBorderPortId_Type())
cucsEtherServerIntFIoOperBorderPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoOperBorderPortId.setStatus(_A)
_CucsEtherServerIntFIoOperBorderSlotId_Type=Gauge32
_CucsEtherServerIntFIoOperBorderSlotId_Object=MibTableColumn
cucsEtherServerIntFIoOperBorderSlotId=_CucsEtherServerIntFIoOperBorderSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,16),_CucsEtherServerIntFIoOperBorderSlotId_Type())
cucsEtherServerIntFIoOperBorderSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoOperBorderSlotId.setStatus(_A)
_CucsEtherServerIntFIoOperState_Type=CucsNetworkPortOperState
_CucsEtherServerIntFIoOperState_Object=MibTableColumn
cucsEtherServerIntFIoOperState=_CucsEtherServerIntFIoOperState_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,17),_CucsEtherServerIntFIoOperState_Type())
cucsEtherServerIntFIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoOperState.setStatus(_A)
_CucsEtherServerIntFIoPeerDn_Type=SnmpAdminString
_CucsEtherServerIntFIoPeerDn_Object=MibTableColumn
cucsEtherServerIntFIoPeerDn=_CucsEtherServerIntFIoPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,18),_CucsEtherServerIntFIoPeerDn_Type())
cucsEtherServerIntFIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPeerDn.setStatus(_A)
_CucsEtherServerIntFIoPeerPortId_Type=Gauge32
_CucsEtherServerIntFIoPeerPortId_Object=MibTableColumn
cucsEtherServerIntFIoPeerPortId=_CucsEtherServerIntFIoPeerPortId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,19),_CucsEtherServerIntFIoPeerPortId_Type())
cucsEtherServerIntFIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPeerPortId.setStatus(_A)
_CucsEtherServerIntFIoPeerSlotId_Type=Gauge32
_CucsEtherServerIntFIoPeerSlotId_Object=MibTableColumn
cucsEtherServerIntFIoPeerSlotId=_CucsEtherServerIntFIoPeerSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,20),_CucsEtherServerIntFIoPeerSlotId_Type())
cucsEtherServerIntFIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPeerSlotId.setStatus(_A)
_CucsEtherServerIntFIoPortId_Type=Gauge32
_CucsEtherServerIntFIoPortId_Object=MibTableColumn
cucsEtherServerIntFIoPortId=_CucsEtherServerIntFIoPortId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,21),_CucsEtherServerIntFIoPortId_Type())
cucsEtherServerIntFIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPortId.setStatus(_A)
_CucsEtherServerIntFIoRevision_Type=SnmpAdminString
_CucsEtherServerIntFIoRevision_Object=MibTableColumn
cucsEtherServerIntFIoRevision=_CucsEtherServerIntFIoRevision_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,22),_CucsEtherServerIntFIoRevision_Type())
cucsEtherServerIntFIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoRevision.setStatus(_A)
_CucsEtherServerIntFIoSerial_Type=SnmpAdminString
_CucsEtherServerIntFIoSerial_Object=MibTableColumn
cucsEtherServerIntFIoSerial=_CucsEtherServerIntFIoSerial_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,23),_CucsEtherServerIntFIoSerial_Type())
cucsEtherServerIntFIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoSerial.setStatus(_A)
_CucsEtherServerIntFIoSlotId_Type=Gauge32
_CucsEtherServerIntFIoSlotId_Object=MibTableColumn
cucsEtherServerIntFIoSlotId=_CucsEtherServerIntFIoSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,24),_CucsEtherServerIntFIoSlotId_Type())
cucsEtherServerIntFIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoSlotId.setStatus(_A)
_CucsEtherServerIntFIoStateQual_Type=SnmpAdminString
_CucsEtherServerIntFIoStateQual_Object=MibTableColumn
cucsEtherServerIntFIoStateQual=_CucsEtherServerIntFIoStateQual_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,25),_CucsEtherServerIntFIoStateQual_Type())
cucsEtherServerIntFIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoStateQual.setStatus(_A)
_CucsEtherServerIntFIoSwitchId_Type=CucsNetworkSwitchId
_CucsEtherServerIntFIoSwitchId_Object=MibTableColumn
cucsEtherServerIntFIoSwitchId=_CucsEtherServerIntFIoSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,26),_CucsEtherServerIntFIoSwitchId_Type())
cucsEtherServerIntFIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoSwitchId.setStatus(_A)
_CucsEtherServerIntFIoTransport_Type=CucsEtherServerIntFIoTransport
_CucsEtherServerIntFIoTransport_Object=MibTableColumn
cucsEtherServerIntFIoTransport=_CucsEtherServerIntFIoTransport_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,27),_CucsEtherServerIntFIoTransport_Type())
cucsEtherServerIntFIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoTransport.setStatus(_A)
_CucsEtherServerIntFIoTs_Type=DateAndTime
_CucsEtherServerIntFIoTs_Object=MibTableColumn
cucsEtherServerIntFIoTs=_CucsEtherServerIntFIoTs_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,28),_CucsEtherServerIntFIoTs_Type())
cucsEtherServerIntFIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoTs.setStatus(_A)
_CucsEtherServerIntFIoType_Type=CucsEtherServerIntFIoType
_CucsEtherServerIntFIoType_Object=MibTableColumn
cucsEtherServerIntFIoType=_CucsEtherServerIntFIoType_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,29),_CucsEtherServerIntFIoType_Type())
cucsEtherServerIntFIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoType.setStatus(_A)
_CucsEtherServerIntFIoVendor_Type=SnmpAdminString
_CucsEtherServerIntFIoVendor_Object=MibTableColumn
cucsEtherServerIntFIoVendor=_CucsEtherServerIntFIoVendor_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,30),_CucsEtherServerIntFIoVendor_Type())
cucsEtherServerIntFIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoVendor.setStatus(_A)
_CucsEtherServerIntFIoMac_Type=MacAddress
_CucsEtherServerIntFIoMac_Object=MibTableColumn
cucsEtherServerIntFIoMac=_CucsEtherServerIntFIoMac_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,31),_CucsEtherServerIntFIoMac_Type())
cucsEtherServerIntFIoMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoMac.setStatus(_A)
_CucsEtherServerIntFIoPeerChassisId_Type=Gauge32
_CucsEtherServerIntFIoPeerChassisId_Object=MibTableColumn
cucsEtherServerIntFIoPeerChassisId=_CucsEtherServerIntFIoPeerChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,32),_CucsEtherServerIntFIoPeerChassisId_Type())
cucsEtherServerIntFIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPeerChassisId.setStatus(_A)
_CucsEtherServerIntFIoXcvrType_Type=CucsEquipmentXcvrType
_CucsEtherServerIntFIoXcvrType_Object=MibTableColumn
cucsEtherServerIntFIoXcvrType=_CucsEtherServerIntFIoXcvrType_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,33),_CucsEtherServerIntFIoXcvrType_Type())
cucsEtherServerIntFIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoXcvrType.setStatus(_A)
_CucsEtherServerIntFIoAdminSpeed_Type=CucsPortEthSpeed
_CucsEtherServerIntFIoAdminSpeed_Object=MibTableColumn
cucsEtherServerIntFIoAdminSpeed=_CucsEtherServerIntFIoAdminSpeed_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,34),_CucsEtherServerIntFIoAdminSpeed_Type())
cucsEtherServerIntFIoAdminSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoAdminSpeed.setStatus(_A)
_CucsEtherServerIntFIoFsmDescr_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmDescr_Object=MibTableColumn
cucsEtherServerIntFIoFsmDescr=_CucsEtherServerIntFIoFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,35),_CucsEtherServerIntFIoFsmDescr_Type())
cucsEtherServerIntFIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmDescr.setStatus(_A)
_CucsEtherServerIntFIoFsmPrev_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmPrev_Object=MibTableColumn
cucsEtherServerIntFIoFsmPrev=_CucsEtherServerIntFIoFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,36),_CucsEtherServerIntFIoFsmPrev_Type())
cucsEtherServerIntFIoFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmPrev.setStatus(_A)
_CucsEtherServerIntFIoFsmProgr_Type=Gauge32
_CucsEtherServerIntFIoFsmProgr_Object=MibTableColumn
cucsEtherServerIntFIoFsmProgr=_CucsEtherServerIntFIoFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,37),_CucsEtherServerIntFIoFsmProgr_Type())
cucsEtherServerIntFIoFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmProgr.setStatus(_A)
_CucsEtherServerIntFIoFsmRmtInvErrCode_Type=Gauge32
_CucsEtherServerIntFIoFsmRmtInvErrCode_Object=MibTableColumn
cucsEtherServerIntFIoFsmRmtInvErrCode=_CucsEtherServerIntFIoFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,38),_CucsEtherServerIntFIoFsmRmtInvErrCode_Type())
cucsEtherServerIntFIoFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRmtInvErrCode.setStatus(_A)
_CucsEtherServerIntFIoFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmRmtInvErrDescr_Object=MibTableColumn
cucsEtherServerIntFIoFsmRmtInvErrDescr=_CucsEtherServerIntFIoFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,39),_CucsEtherServerIntFIoFsmRmtInvErrDescr_Type())
cucsEtherServerIntFIoFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRmtInvErrDescr.setStatus(_A)
_CucsEtherServerIntFIoFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsEtherServerIntFIoFsmRmtInvRslt_Object=MibTableColumn
cucsEtherServerIntFIoFsmRmtInvRslt=_CucsEtherServerIntFIoFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,40),_CucsEtherServerIntFIoFsmRmtInvRslt_Type())
cucsEtherServerIntFIoFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRmtInvRslt.setStatus(_A)
_CucsEtherServerIntFIoFsmStageDescr_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmStageDescr_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageDescr=_CucsEtherServerIntFIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,41),_CucsEtherServerIntFIoFsmStageDescr_Type())
cucsEtherServerIntFIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageDescr.setStatus(_A)
_CucsEtherServerIntFIoFsmStamp_Type=DateAndTime
_CucsEtherServerIntFIoFsmStamp_Object=MibTableColumn
cucsEtherServerIntFIoFsmStamp=_CucsEtherServerIntFIoFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,42),_CucsEtherServerIntFIoFsmStamp_Type())
cucsEtherServerIntFIoFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStamp.setStatus(_A)
_CucsEtherServerIntFIoFsmStatus_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmStatus_Object=MibTableColumn
cucsEtherServerIntFIoFsmStatus=_CucsEtherServerIntFIoFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,43),_CucsEtherServerIntFIoFsmStatus_Type())
cucsEtherServerIntFIoFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStatus.setStatus(_A)
_CucsEtherServerIntFIoFsmTry_Type=Gauge32
_CucsEtherServerIntFIoFsmTry_Object=MibTableColumn
cucsEtherServerIntFIoFsmTry=_CucsEtherServerIntFIoFsmTry_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,44),_CucsEtherServerIntFIoFsmTry_Type())
cucsEtherServerIntFIoFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTry.setStatus(_A)
_CucsEtherServerIntFIoNsSize_Type=Gauge32
_CucsEtherServerIntFIoNsSize_Object=MibTableColumn
cucsEtherServerIntFIoNsSize=_CucsEtherServerIntFIoNsSize_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,45),_CucsEtherServerIntFIoNsSize_Type())
cucsEtherServerIntFIoNsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoNsSize.setStatus(_A)
_CucsEtherServerIntFIoPeerEncap_Type=Gauge32
_CucsEtherServerIntFIoPeerEncap_Object=MibTableColumn
cucsEtherServerIntFIoPeerEncap=_CucsEtherServerIntFIoPeerEncap_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,46),_CucsEtherServerIntFIoPeerEncap_Type())
cucsEtherServerIntFIoPeerEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPeerEncap.setStatus(_A)
_CucsEtherServerIntFIoAggrPortId_Type=Gauge32
_CucsEtherServerIntFIoAggrPortId_Object=MibTableColumn
cucsEtherServerIntFIoAggrPortId=_CucsEtherServerIntFIoAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,47),_CucsEtherServerIntFIoAggrPortId_Type())
cucsEtherServerIntFIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoAggrPortId.setStatus(_A)
_CucsEtherServerIntFIoPeerAggrPortId_Type=Gauge32
_CucsEtherServerIntFIoPeerAggrPortId_Object=MibTableColumn
cucsEtherServerIntFIoPeerAggrPortId=_CucsEtherServerIntFIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,48),_CucsEtherServerIntFIoPeerAggrPortId_Type())
cucsEtherServerIntFIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPeerAggrPortId.setStatus(_A)
_CucsEtherServerIntFIoMacAddr_Type=MacAddress
_CucsEtherServerIntFIoMacAddr_Object=MibTableColumn
cucsEtherServerIntFIoMacAddr=_CucsEtherServerIntFIoMacAddr_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,49),_CucsEtherServerIntFIoMacAddr_Type())
cucsEtherServerIntFIoMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoMacAddr.setStatus(_A)
_CucsEtherServerIntFIoOperBorderAggrPortId_Type=Gauge32
_CucsEtherServerIntFIoOperBorderAggrPortId_Object=MibTableColumn
cucsEtherServerIntFIoOperBorderAggrPortId=_CucsEtherServerIntFIoOperBorderAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,50),_CucsEtherServerIntFIoOperBorderAggrPortId_Type())
cucsEtherServerIntFIoOperBorderAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoOperBorderAggrPortId.setStatus(_A)
_CucsEtherServerIntFIoUserRecoveryOperation_Type=CucsEtherUserRecoveryOperation
_CucsEtherServerIntFIoUserRecoveryOperation_Object=MibTableColumn
cucsEtherServerIntFIoUserRecoveryOperation=_CucsEtherServerIntFIoUserRecoveryOperation_Object((1,3,6,1,4,1,9,9,719,1,16,11,1,51),_CucsEtherServerIntFIoUserRecoveryOperation_Type())
cucsEtherServerIntFIoUserRecoveryOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoUserRecoveryOperation.setStatus(_A)
_CucsEtherSwIfConfigTable_Object=MibTable
cucsEtherSwIfConfigTable=_CucsEtherSwIfConfigTable_Object((1,3,6,1,4,1,9,9,719,1,16,12))
if mibBuilder.loadTexts:cucsEtherSwIfConfigTable.setStatus(_A)
_CucsEtherSwIfConfigEntry_Object=MibTableRow
cucsEtherSwIfConfigEntry=_CucsEtherSwIfConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,16,12,1))
cucsEtherSwIfConfigEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsEtherSwIfConfigEntry.setStatus(_A)
_CucsEtherSwIfConfigInstanceId_Type=CucsManagedObjectId
_CucsEtherSwIfConfigInstanceId_Object=MibTableColumn
cucsEtherSwIfConfigInstanceId=_CucsEtherSwIfConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,12,1,1),_CucsEtherSwIfConfigInstanceId_Type())
cucsEtherSwIfConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherSwIfConfigInstanceId.setStatus(_A)
_CucsEtherSwIfConfigDn_Type=CucsManagedObjectDn
_CucsEtherSwIfConfigDn_Object=MibTableColumn
cucsEtherSwIfConfigDn=_CucsEtherSwIfConfigDn_Object((1,3,6,1,4,1,9,9,719,1,16,12,1,2),_CucsEtherSwIfConfigDn_Type())
cucsEtherSwIfConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwIfConfigDn.setStatus(_A)
_CucsEtherSwIfConfigRn_Type=SnmpAdminString
_CucsEtherSwIfConfigRn_Object=MibTableColumn
cucsEtherSwIfConfigRn=_CucsEtherSwIfConfigRn_Object((1,3,6,1,4,1,9,9,719,1,16,12,1,3),_CucsEtherSwIfConfigRn_Type())
cucsEtherSwIfConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwIfConfigRn.setStatus(_A)
_CucsEtherSwitchIntFIoTable_Object=MibTable
cucsEtherSwitchIntFIoTable=_CucsEtherSwitchIntFIoTable_Object((1,3,6,1,4,1,9,9,719,1,16,13))
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoTable.setStatus(_A)
_CucsEtherSwitchIntFIoEntry_Object=MibTableRow
cucsEtherSwitchIntFIoEntry=_CucsEtherSwitchIntFIoEntry_Object((1,3,6,1,4,1,9,9,719,1,16,13,1))
cucsEtherSwitchIntFIoEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoEntry.setStatus(_A)
_CucsEtherSwitchIntFIoInstanceId_Type=CucsManagedObjectId
_CucsEtherSwitchIntFIoInstanceId_Object=MibTableColumn
cucsEtherSwitchIntFIoInstanceId=_CucsEtherSwitchIntFIoInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,1),_CucsEtherSwitchIntFIoInstanceId_Type())
cucsEtherSwitchIntFIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoInstanceId.setStatus(_A)
_CucsEtherSwitchIntFIoDn_Type=CucsManagedObjectDn
_CucsEtherSwitchIntFIoDn_Object=MibTableColumn
cucsEtherSwitchIntFIoDn=_CucsEtherSwitchIntFIoDn_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,2),_CucsEtherSwitchIntFIoDn_Type())
cucsEtherSwitchIntFIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoDn.setStatus(_A)
_CucsEtherSwitchIntFIoRn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoRn_Object=MibTableColumn
cucsEtherSwitchIntFIoRn=_CucsEtherSwitchIntFIoRn_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,3),_CucsEtherSwitchIntFIoRn_Type())
cucsEtherSwitchIntFIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoRn.setStatus(_A)
_CucsEtherSwitchIntFIoAck_Type=CucsEtherSwitchIntFIoAck
_CucsEtherSwitchIntFIoAck_Object=MibTableColumn
cucsEtherSwitchIntFIoAck=_CucsEtherSwitchIntFIoAck_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,4),_CucsEtherSwitchIntFIoAck_Type())
cucsEtherSwitchIntFIoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoAck.setStatus(_A)
_CucsEtherSwitchIntFIoAdminState_Type=CucsFabricAdminState
_CucsEtherSwitchIntFIoAdminState_Object=MibTableColumn
cucsEtherSwitchIntFIoAdminState=_CucsEtherSwitchIntFIoAdminState_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,5),_CucsEtherSwitchIntFIoAdminState_Type())
cucsEtherSwitchIntFIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoAdminState.setStatus(_A)
_CucsEtherSwitchIntFIoChassisId_Type=Gauge32
_CucsEtherSwitchIntFIoChassisId_Object=MibTableColumn
cucsEtherSwitchIntFIoChassisId=_CucsEtherSwitchIntFIoChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,6),_CucsEtherSwitchIntFIoChassisId_Type())
cucsEtherSwitchIntFIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoChassisId.setStatus(_A)
_CucsEtherSwitchIntFIoDiscovery_Type=CucsEtherSatelliteConnectionDisc
_CucsEtherSwitchIntFIoDiscovery_Object=MibTableColumn
cucsEtherSwitchIntFIoDiscovery=_CucsEtherSwitchIntFIoDiscovery_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,7),_CucsEtherSwitchIntFIoDiscovery_Type())
cucsEtherSwitchIntFIoDiscovery.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoDiscovery.setStatus(_A)
_CucsEtherSwitchIntFIoEncap_Type=CucsPortEncap
_CucsEtherSwitchIntFIoEncap_Object=MibTableColumn
cucsEtherSwitchIntFIoEncap=_CucsEtherSwitchIntFIoEncap_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,8),_CucsEtherSwitchIntFIoEncap_Type())
cucsEtherSwitchIntFIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoEncap.setStatus(_A)
_CucsEtherSwitchIntFIoEpDn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoEpDn_Object=MibTableColumn
cucsEtherSwitchIntFIoEpDn=_CucsEtherSwitchIntFIoEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,9),_CucsEtherSwitchIntFIoEpDn_Type())
cucsEtherSwitchIntFIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoEpDn.setStatus(_A)
_CucsEtherSwitchIntFIoFltAggr_Type=Unsigned64
_CucsEtherSwitchIntFIoFltAggr_Object=MibTableColumn
cucsEtherSwitchIntFIoFltAggr=_CucsEtherSwitchIntFIoFltAggr_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,10),_CucsEtherSwitchIntFIoFltAggr_Type())
cucsEtherSwitchIntFIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoFltAggr.setStatus(_A)
_CucsEtherSwitchIntFIoIfRole_Type=CucsEtherSwitchIntFIoIfRole
_CucsEtherSwitchIntFIoIfRole_Object=MibTableColumn
cucsEtherSwitchIntFIoIfRole=_CucsEtherSwitchIntFIoIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,11),_CucsEtherSwitchIntFIoIfRole_Type())
cucsEtherSwitchIntFIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoIfRole.setStatus(_A)
_CucsEtherSwitchIntFIoIfType_Type=CucsNetworkPhysEpIfType
_CucsEtherSwitchIntFIoIfType_Object=MibTableColumn
cucsEtherSwitchIntFIoIfType=_CucsEtherSwitchIntFIoIfType_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,12),_CucsEtherSwitchIntFIoIfType_Type())
cucsEtherSwitchIntFIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoIfType.setStatus(_A)
_CucsEtherSwitchIntFIoLocale_Type=CucsEtherSwitchIntFIoLocale
_CucsEtherSwitchIntFIoLocale_Object=MibTableColumn
cucsEtherSwitchIntFIoLocale=_CucsEtherSwitchIntFIoLocale_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,13),_CucsEtherSwitchIntFIoLocale_Type())
cucsEtherSwitchIntFIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoLocale.setStatus(_A)
_CucsEtherSwitchIntFIoMode_Type=CucsPortMode
_CucsEtherSwitchIntFIoMode_Object=MibTableColumn
cucsEtherSwitchIntFIoMode=_CucsEtherSwitchIntFIoMode_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,14),_CucsEtherSwitchIntFIoMode_Type())
cucsEtherSwitchIntFIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoMode.setStatus(_A)
_CucsEtherSwitchIntFIoModel_Type=SnmpAdminString
_CucsEtherSwitchIntFIoModel_Object=MibTableColumn
cucsEtherSwitchIntFIoModel=_CucsEtherSwitchIntFIoModel_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,15),_CucsEtherSwitchIntFIoModel_Type())
cucsEtherSwitchIntFIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoModel.setStatus(_A)
_CucsEtherSwitchIntFIoName_Type=SnmpAdminString
_CucsEtherSwitchIntFIoName_Object=MibTableColumn
cucsEtherSwitchIntFIoName=_CucsEtherSwitchIntFIoName_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,16),_CucsEtherSwitchIntFIoName_Type())
cucsEtherSwitchIntFIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoName.setStatus(_A)
_CucsEtherSwitchIntFIoOperState_Type=CucsNetworkPortOperState
_CucsEtherSwitchIntFIoOperState_Object=MibTableColumn
cucsEtherSwitchIntFIoOperState=_CucsEtherSwitchIntFIoOperState_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,17),_CucsEtherSwitchIntFIoOperState_Type())
cucsEtherSwitchIntFIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoOperState.setStatus(_A)
_CucsEtherSwitchIntFIoPeerDn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPeerDn_Object=MibTableColumn
cucsEtherSwitchIntFIoPeerDn=_CucsEtherSwitchIntFIoPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,18),_CucsEtherSwitchIntFIoPeerDn_Type())
cucsEtherSwitchIntFIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPeerDn.setStatus(_A)
_CucsEtherSwitchIntFIoPeerPortId_Type=Gauge32
_CucsEtherSwitchIntFIoPeerPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPeerPortId=_CucsEtherSwitchIntFIoPeerPortId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,19),_CucsEtherSwitchIntFIoPeerPortId_Type())
cucsEtherSwitchIntFIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPeerPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPeerSlotId_Type=Gauge32
_CucsEtherSwitchIntFIoPeerSlotId_Object=MibTableColumn
cucsEtherSwitchIntFIoPeerSlotId=_CucsEtherSwitchIntFIoPeerSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,20),_CucsEtherSwitchIntFIoPeerSlotId_Type())
cucsEtherSwitchIntFIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPeerSlotId.setStatus(_A)
_CucsEtherSwitchIntFIoPortId_Type=Gauge32
_CucsEtherSwitchIntFIoPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPortId=_CucsEtherSwitchIntFIoPortId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,21),_CucsEtherSwitchIntFIoPortId_Type())
cucsEtherSwitchIntFIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPortId.setStatus(_A)
_CucsEtherSwitchIntFIoRevision_Type=SnmpAdminString
_CucsEtherSwitchIntFIoRevision_Object=MibTableColumn
cucsEtherSwitchIntFIoRevision=_CucsEtherSwitchIntFIoRevision_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,22),_CucsEtherSwitchIntFIoRevision_Type())
cucsEtherSwitchIntFIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoRevision.setStatus(_A)
_CucsEtherSwitchIntFIoSerial_Type=SnmpAdminString
_CucsEtherSwitchIntFIoSerial_Object=MibTableColumn
cucsEtherSwitchIntFIoSerial=_CucsEtherSwitchIntFIoSerial_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,23),_CucsEtherSwitchIntFIoSerial_Type())
cucsEtherSwitchIntFIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoSerial.setStatus(_A)
_CucsEtherSwitchIntFIoSlotId_Type=Gauge32
_CucsEtherSwitchIntFIoSlotId_Object=MibTableColumn
cucsEtherSwitchIntFIoSlotId=_CucsEtherSwitchIntFIoSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,24),_CucsEtherSwitchIntFIoSlotId_Type())
cucsEtherSwitchIntFIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoSlotId.setStatus(_A)
_CucsEtherSwitchIntFIoStateQual_Type=SnmpAdminString
_CucsEtherSwitchIntFIoStateQual_Object=MibTableColumn
cucsEtherSwitchIntFIoStateQual=_CucsEtherSwitchIntFIoStateQual_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,25),_CucsEtherSwitchIntFIoStateQual_Type())
cucsEtherSwitchIntFIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoStateQual.setStatus(_A)
_CucsEtherSwitchIntFIoSwitchId_Type=CucsNetworkSwitchId
_CucsEtherSwitchIntFIoSwitchId_Object=MibTableColumn
cucsEtherSwitchIntFIoSwitchId=_CucsEtherSwitchIntFIoSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,26),_CucsEtherSwitchIntFIoSwitchId_Type())
cucsEtherSwitchIntFIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoSwitchId.setStatus(_A)
_CucsEtherSwitchIntFIoTransport_Type=CucsEtherSwitchIntFIoTransport
_CucsEtherSwitchIntFIoTransport_Object=MibTableColumn
cucsEtherSwitchIntFIoTransport=_CucsEtherSwitchIntFIoTransport_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,27),_CucsEtherSwitchIntFIoTransport_Type())
cucsEtherSwitchIntFIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoTransport.setStatus(_A)
_CucsEtherSwitchIntFIoTs_Type=DateAndTime
_CucsEtherSwitchIntFIoTs_Object=MibTableColumn
cucsEtherSwitchIntFIoTs=_CucsEtherSwitchIntFIoTs_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,28),_CucsEtherSwitchIntFIoTs_Type())
cucsEtherSwitchIntFIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoTs.setStatus(_A)
_CucsEtherSwitchIntFIoType_Type=CucsEtherSwitchIntFIoType
_CucsEtherSwitchIntFIoType_Object=MibTableColumn
cucsEtherSwitchIntFIoType=_CucsEtherSwitchIntFIoType_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,29),_CucsEtherSwitchIntFIoType_Type())
cucsEtherSwitchIntFIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoType.setStatus(_A)
_CucsEtherSwitchIntFIoVendor_Type=SnmpAdminString
_CucsEtherSwitchIntFIoVendor_Object=MibTableColumn
cucsEtherSwitchIntFIoVendor=_CucsEtherSwitchIntFIoVendor_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,30),_CucsEtherSwitchIntFIoVendor_Type())
cucsEtherSwitchIntFIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoVendor.setStatus(_A)
_CucsEtherSwitchIntFIoPeerChassisId_Type=Gauge32
_CucsEtherSwitchIntFIoPeerChassisId_Object=MibTableColumn
cucsEtherSwitchIntFIoPeerChassisId=_CucsEtherSwitchIntFIoPeerChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,31),_CucsEtherSwitchIntFIoPeerChassisId_Type())
cucsEtherSwitchIntFIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPeerChassisId.setStatus(_A)
_CucsEtherSwitchIntFIoXcvrType_Type=CucsEquipmentXcvrType
_CucsEtherSwitchIntFIoXcvrType_Object=MibTableColumn
cucsEtherSwitchIntFIoXcvrType=_CucsEtherSwitchIntFIoXcvrType_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,32),_CucsEtherSwitchIntFIoXcvrType_Type())
cucsEtherSwitchIntFIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoXcvrType.setStatus(_A)
_CucsEtherSwitchIntFIoDelFeTs_Type=Unsigned64
_CucsEtherSwitchIntFIoDelFeTs_Object=MibTableColumn
cucsEtherSwitchIntFIoDelFeTs=_CucsEtherSwitchIntFIoDelFeTs_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,33),_CucsEtherSwitchIntFIoDelFeTs_Type())
cucsEtherSwitchIntFIoDelFeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoDelFeTs.setStatus(_A)
_CucsEtherSwitchIntFIoNewFeTs_Type=Unsigned64
_CucsEtherSwitchIntFIoNewFeTs_Object=MibTableColumn
cucsEtherSwitchIntFIoNewFeTs=_CucsEtherSwitchIntFIoNewFeTs_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,34),_CucsEtherSwitchIntFIoNewFeTs_Type())
cucsEtherSwitchIntFIoNewFeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoNewFeTs.setStatus(_A)
_CucsEtherSwitchIntFIoAggrPortId_Type=Gauge32
_CucsEtherSwitchIntFIoAggrPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoAggrPortId=_CucsEtherSwitchIntFIoAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,35),_CucsEtherSwitchIntFIoAggrPortId_Type())
cucsEtherSwitchIntFIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoAggrPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPeerAggrPortId_Type=Gauge32
_CucsEtherSwitchIntFIoPeerAggrPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPeerAggrPortId=_CucsEtherSwitchIntFIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,36),_CucsEtherSwitchIntFIoPeerAggrPortId_Type())
cucsEtherSwitchIntFIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPeerAggrPortId.setStatus(_A)
_CucsEtherSwitchIntFIoMacAddr_Type=MacAddress
_CucsEtherSwitchIntFIoMacAddr_Object=MibTableColumn
cucsEtherSwitchIntFIoMacAddr=_CucsEtherSwitchIntFIoMacAddr_Object((1,3,6,1,4,1,9,9,719,1,16,13,1,37),_CucsEtherSwitchIntFIoMacAddr_Type())
cucsEtherSwitchIntFIoMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoMacAddr.setStatus(_A)
_CucsEtherTxStatsTable_Object=MibTable
cucsEtherTxStatsTable=_CucsEtherTxStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,14))
if mibBuilder.loadTexts:cucsEtherTxStatsTable.setStatus(_A)
_CucsEtherTxStatsEntry_Object=MibTableRow
cucsEtherTxStatsEntry=_CucsEtherTxStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,14,1))
cucsEtherTxStatsEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsEtherTxStatsEntry.setStatus(_A)
_CucsEtherTxStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherTxStatsInstanceId_Object=MibTableColumn
cucsEtherTxStatsInstanceId=_CucsEtherTxStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,1),_CucsEtherTxStatsInstanceId_Type())
cucsEtherTxStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherTxStatsInstanceId.setStatus(_A)
_CucsEtherTxStatsDn_Type=CucsManagedObjectDn
_CucsEtherTxStatsDn_Object=MibTableColumn
cucsEtherTxStatsDn=_CucsEtherTxStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,2),_CucsEtherTxStatsDn_Type())
cucsEtherTxStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsDn.setStatus(_A)
_CucsEtherTxStatsRn_Type=SnmpAdminString
_CucsEtherTxStatsRn_Object=MibTableColumn
cucsEtherTxStatsRn=_CucsEtherTxStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,3),_CucsEtherTxStatsRn_Type())
cucsEtherTxStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsRn.setStatus(_A)
_CucsEtherTxStatsBroadcastPackets_Type=Unsigned64
_CucsEtherTxStatsBroadcastPackets_Object=MibTableColumn
cucsEtherTxStatsBroadcastPackets=_CucsEtherTxStatsBroadcastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,4),_CucsEtherTxStatsBroadcastPackets_Type())
cucsEtherTxStatsBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsBroadcastPackets.setStatus(_A)
_CucsEtherTxStatsBroadcastPacketsDelta_Type=Counter64
_CucsEtherTxStatsBroadcastPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsBroadcastPacketsDelta=_CucsEtherTxStatsBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,5),_CucsEtherTxStatsBroadcastPacketsDelta_Type())
cucsEtherTxStatsBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsBroadcastPacketsDelta.setStatus(_A)
_CucsEtherTxStatsBroadcastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsBroadcastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsBroadcastPacketsDeltaAvg=_CucsEtherTxStatsBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,6),_CucsEtherTxStatsBroadcastPacketsDeltaAvg_Type())
cucsEtherTxStatsBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsBroadcastPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsBroadcastPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsBroadcastPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsBroadcastPacketsDeltaMax=_CucsEtherTxStatsBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,7),_CucsEtherTxStatsBroadcastPacketsDeltaMax_Type())
cucsEtherTxStatsBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsBroadcastPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsBroadcastPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsBroadcastPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsBroadcastPacketsDeltaMin=_CucsEtherTxStatsBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,8),_CucsEtherTxStatsBroadcastPacketsDeltaMin_Type())
cucsEtherTxStatsBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsBroadcastPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsIntervals_Type=Gauge32
_CucsEtherTxStatsIntervals_Object=MibTableColumn
cucsEtherTxStatsIntervals=_CucsEtherTxStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,9),_CucsEtherTxStatsIntervals_Type())
cucsEtherTxStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsIntervals.setStatus(_A)
_CucsEtherTxStatsJumboPackets_Type=Unsigned64
_CucsEtherTxStatsJumboPackets_Object=MibTableColumn
cucsEtherTxStatsJumboPackets=_CucsEtherTxStatsJumboPackets_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,10),_CucsEtherTxStatsJumboPackets_Type())
cucsEtherTxStatsJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsJumboPackets.setStatus(_A)
_CucsEtherTxStatsJumboPacketsDelta_Type=Counter64
_CucsEtherTxStatsJumboPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsJumboPacketsDelta=_CucsEtherTxStatsJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,11),_CucsEtherTxStatsJumboPacketsDelta_Type())
cucsEtherTxStatsJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsJumboPacketsDelta.setStatus(_A)
_CucsEtherTxStatsJumboPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsJumboPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsJumboPacketsDeltaAvg=_CucsEtherTxStatsJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,12),_CucsEtherTxStatsJumboPacketsDeltaAvg_Type())
cucsEtherTxStatsJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsJumboPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsJumboPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsJumboPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsJumboPacketsDeltaMax=_CucsEtherTxStatsJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,13),_CucsEtherTxStatsJumboPacketsDeltaMax_Type())
cucsEtherTxStatsJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsJumboPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsJumboPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsJumboPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsJumboPacketsDeltaMin=_CucsEtherTxStatsJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,14),_CucsEtherTxStatsJumboPacketsDeltaMin_Type())
cucsEtherTxStatsJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsJumboPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsMulticastPackets_Type=Unsigned64
_CucsEtherTxStatsMulticastPackets_Object=MibTableColumn
cucsEtherTxStatsMulticastPackets=_CucsEtherTxStatsMulticastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,15),_CucsEtherTxStatsMulticastPackets_Type())
cucsEtherTxStatsMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsMulticastPackets.setStatus(_A)
_CucsEtherTxStatsMulticastPacketsDelta_Type=Counter64
_CucsEtherTxStatsMulticastPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsMulticastPacketsDelta=_CucsEtherTxStatsMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,16),_CucsEtherTxStatsMulticastPacketsDelta_Type())
cucsEtherTxStatsMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsMulticastPacketsDelta.setStatus(_A)
_CucsEtherTxStatsMulticastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsMulticastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsMulticastPacketsDeltaAvg=_CucsEtherTxStatsMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,17),_CucsEtherTxStatsMulticastPacketsDeltaAvg_Type())
cucsEtherTxStatsMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsMulticastPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsMulticastPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsMulticastPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsMulticastPacketsDeltaMax=_CucsEtherTxStatsMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,18),_CucsEtherTxStatsMulticastPacketsDeltaMax_Type())
cucsEtherTxStatsMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsMulticastPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsMulticastPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsMulticastPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsMulticastPacketsDeltaMin=_CucsEtherTxStatsMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,19),_CucsEtherTxStatsMulticastPacketsDeltaMin_Type())
cucsEtherTxStatsMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsMulticastPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsSuspect_Type=TruthValue
_CucsEtherTxStatsSuspect_Object=MibTableColumn
cucsEtherTxStatsSuspect=_CucsEtherTxStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,20),_CucsEtherTxStatsSuspect_Type())
cucsEtherTxStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsSuspect.setStatus(_A)
_CucsEtherTxStatsThresholded_Type=CucsEtherTxStatsThresholded
_CucsEtherTxStatsThresholded_Object=MibTableColumn
cucsEtherTxStatsThresholded=_CucsEtherTxStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,21),_CucsEtherTxStatsThresholded_Type())
cucsEtherTxStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsThresholded.setStatus(_A)
_CucsEtherTxStatsTimeCollected_Type=DateAndTime
_CucsEtherTxStatsTimeCollected_Object=MibTableColumn
cucsEtherTxStatsTimeCollected=_CucsEtherTxStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,22),_CucsEtherTxStatsTimeCollected_Type())
cucsEtherTxStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTimeCollected.setStatus(_A)
_CucsEtherTxStatsTotalBytes_Type=Unsigned64
_CucsEtherTxStatsTotalBytes_Object=MibTableColumn
cucsEtherTxStatsTotalBytes=_CucsEtherTxStatsTotalBytes_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,23),_CucsEtherTxStatsTotalBytes_Type())
cucsEtherTxStatsTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalBytes.setStatus(_A)
_CucsEtherTxStatsTotalBytesDelta_Type=Counter64
_CucsEtherTxStatsTotalBytesDelta_Object=MibTableColumn
cucsEtherTxStatsTotalBytesDelta=_CucsEtherTxStatsTotalBytesDelta_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,24),_CucsEtherTxStatsTotalBytesDelta_Type())
cucsEtherTxStatsTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalBytesDelta.setStatus(_A)
_CucsEtherTxStatsTotalBytesDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsTotalBytesDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsTotalBytesDeltaAvg=_CucsEtherTxStatsTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,25),_CucsEtherTxStatsTotalBytesDeltaAvg_Type())
cucsEtherTxStatsTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalBytesDeltaAvg.setStatus(_A)
_CucsEtherTxStatsTotalBytesDeltaMax_Type=Unsigned64
_CucsEtherTxStatsTotalBytesDeltaMax_Object=MibTableColumn
cucsEtherTxStatsTotalBytesDeltaMax=_CucsEtherTxStatsTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,26),_CucsEtherTxStatsTotalBytesDeltaMax_Type())
cucsEtherTxStatsTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalBytesDeltaMax.setStatus(_A)
_CucsEtherTxStatsTotalBytesDeltaMin_Type=Unsigned64
_CucsEtherTxStatsTotalBytesDeltaMin_Object=MibTableColumn
cucsEtherTxStatsTotalBytesDeltaMin=_CucsEtherTxStatsTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,27),_CucsEtherTxStatsTotalBytesDeltaMin_Type())
cucsEtherTxStatsTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalBytesDeltaMin.setStatus(_A)
_CucsEtherTxStatsTotalPackets_Type=Unsigned64
_CucsEtherTxStatsTotalPackets_Object=MibTableColumn
cucsEtherTxStatsTotalPackets=_CucsEtherTxStatsTotalPackets_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,28),_CucsEtherTxStatsTotalPackets_Type())
cucsEtherTxStatsTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalPackets.setStatus(_A)
_CucsEtherTxStatsTotalPacketsDelta_Type=Counter64
_CucsEtherTxStatsTotalPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsTotalPacketsDelta=_CucsEtherTxStatsTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,29),_CucsEtherTxStatsTotalPacketsDelta_Type())
cucsEtherTxStatsTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalPacketsDelta.setStatus(_A)
_CucsEtherTxStatsTotalPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsTotalPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsTotalPacketsDeltaAvg=_CucsEtherTxStatsTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,30),_CucsEtherTxStatsTotalPacketsDeltaAvg_Type())
cucsEtherTxStatsTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsTotalPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsTotalPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsTotalPacketsDeltaMax=_CucsEtherTxStatsTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,31),_CucsEtherTxStatsTotalPacketsDeltaMax_Type())
cucsEtherTxStatsTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsTotalPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsTotalPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsTotalPacketsDeltaMin=_CucsEtherTxStatsTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,32),_CucsEtherTxStatsTotalPacketsDeltaMin_Type())
cucsEtherTxStatsTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsTotalPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsUnicastPackets_Type=Unsigned64
_CucsEtherTxStatsUnicastPackets_Object=MibTableColumn
cucsEtherTxStatsUnicastPackets=_CucsEtherTxStatsUnicastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,33),_CucsEtherTxStatsUnicastPackets_Type())
cucsEtherTxStatsUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsUnicastPackets.setStatus(_A)
_CucsEtherTxStatsUnicastPacketsDelta_Type=Counter64
_CucsEtherTxStatsUnicastPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsUnicastPacketsDelta=_CucsEtherTxStatsUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,34),_CucsEtherTxStatsUnicastPacketsDelta_Type())
cucsEtherTxStatsUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsUnicastPacketsDelta.setStatus(_A)
_CucsEtherTxStatsUnicastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsUnicastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsUnicastPacketsDeltaAvg=_CucsEtherTxStatsUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,35),_CucsEtherTxStatsUnicastPacketsDeltaAvg_Type())
cucsEtherTxStatsUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsUnicastPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsUnicastPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsUnicastPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsUnicastPacketsDeltaMax=_CucsEtherTxStatsUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,36),_CucsEtherTxStatsUnicastPacketsDeltaMax_Type())
cucsEtherTxStatsUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsUnicastPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsUnicastPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsUnicastPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsUnicastPacketsDeltaMin=_CucsEtherTxStatsUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,37),_CucsEtherTxStatsUnicastPacketsDeltaMin_Type())
cucsEtherTxStatsUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsUnicastPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsUpdate_Type=Gauge32
_CucsEtherTxStatsUpdate_Object=MibTableColumn
cucsEtherTxStatsUpdate=_CucsEtherTxStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,14,1,38),_CucsEtherTxStatsUpdate_Type())
cucsEtherTxStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsUpdate.setStatus(_A)
_CucsEtherTxStatsHistTable_Object=MibTable
cucsEtherTxStatsHistTable=_CucsEtherTxStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,15))
if mibBuilder.loadTexts:cucsEtherTxStatsHistTable.setStatus(_A)
_CucsEtherTxStatsHistEntry_Object=MibTableRow
cucsEtherTxStatsHistEntry=_CucsEtherTxStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,15,1))
cucsEtherTxStatsHistEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsEtherTxStatsHistEntry.setStatus(_A)
_CucsEtherTxStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherTxStatsHistInstanceId_Object=MibTableColumn
cucsEtherTxStatsHistInstanceId=_CucsEtherTxStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,1),_CucsEtherTxStatsHistInstanceId_Type())
cucsEtherTxStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherTxStatsHistInstanceId.setStatus(_A)
_CucsEtherTxStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherTxStatsHistDn_Object=MibTableColumn
cucsEtherTxStatsHistDn=_CucsEtherTxStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,2),_CucsEtherTxStatsHistDn_Type())
cucsEtherTxStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistDn.setStatus(_A)
_CucsEtherTxStatsHistRn_Type=SnmpAdminString
_CucsEtherTxStatsHistRn_Object=MibTableColumn
cucsEtherTxStatsHistRn=_CucsEtherTxStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,3),_CucsEtherTxStatsHistRn_Type())
cucsEtherTxStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistRn.setStatus(_A)
_CucsEtherTxStatsHistBroadcastPackets_Type=Unsigned64
_CucsEtherTxStatsHistBroadcastPackets_Object=MibTableColumn
cucsEtherTxStatsHistBroadcastPackets=_CucsEtherTxStatsHistBroadcastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,4),_CucsEtherTxStatsHistBroadcastPackets_Type())
cucsEtherTxStatsHistBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistBroadcastPackets.setStatus(_A)
_CucsEtherTxStatsHistBroadcastPacketsDelta_Type=Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDelta=_CucsEtherTxStatsHistBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,5),_CucsEtherTxStatsHistBroadcastPacketsDelta_Type())
cucsEtherTxStatsHistBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistBroadcastPacketsDelta.setStatus(_A)
_CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDeltaAvg=_CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,6),_CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Type())
cucsEtherTxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistBroadcastPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDeltaMax=_CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,7),_CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Type())
cucsEtherTxStatsHistBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistBroadcastPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDeltaMin=_CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,8),_CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Type())
cucsEtherTxStatsHistBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistBroadcastPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsHistId_Type=Unsigned64
_CucsEtherTxStatsHistId_Object=MibTableColumn
cucsEtherTxStatsHistId=_CucsEtherTxStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,9),_CucsEtherTxStatsHistId_Type())
cucsEtherTxStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistId.setStatus(_A)
_CucsEtherTxStatsHistJumboPackets_Type=Unsigned64
_CucsEtherTxStatsHistJumboPackets_Object=MibTableColumn
cucsEtherTxStatsHistJumboPackets=_CucsEtherTxStatsHistJumboPackets_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,10),_CucsEtherTxStatsHistJumboPackets_Type())
cucsEtherTxStatsHistJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistJumboPackets.setStatus(_A)
_CucsEtherTxStatsHistJumboPacketsDelta_Type=Unsigned64
_CucsEtherTxStatsHistJumboPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsHistJumboPacketsDelta=_CucsEtherTxStatsHistJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,11),_CucsEtherTxStatsHistJumboPacketsDelta_Type())
cucsEtherTxStatsHistJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistJumboPacketsDelta.setStatus(_A)
_CucsEtherTxStatsHistJumboPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsHistJumboPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsHistJumboPacketsDeltaAvg=_CucsEtherTxStatsHistJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,12),_CucsEtherTxStatsHistJumboPacketsDeltaAvg_Type())
cucsEtherTxStatsHistJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistJumboPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsHistJumboPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsHistJumboPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsHistJumboPacketsDeltaMax=_CucsEtherTxStatsHistJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,13),_CucsEtherTxStatsHistJumboPacketsDeltaMax_Type())
cucsEtherTxStatsHistJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistJumboPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsHistJumboPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsHistJumboPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsHistJumboPacketsDeltaMin=_CucsEtherTxStatsHistJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,14),_CucsEtherTxStatsHistJumboPacketsDeltaMin_Type())
cucsEtherTxStatsHistJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistJumboPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsHistMostRecent_Type=TruthValue
_CucsEtherTxStatsHistMostRecent_Object=MibTableColumn
cucsEtherTxStatsHistMostRecent=_CucsEtherTxStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,15),_CucsEtherTxStatsHistMostRecent_Type())
cucsEtherTxStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistMostRecent.setStatus(_A)
_CucsEtherTxStatsHistMulticastPackets_Type=Unsigned64
_CucsEtherTxStatsHistMulticastPackets_Object=MibTableColumn
cucsEtherTxStatsHistMulticastPackets=_CucsEtherTxStatsHistMulticastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,16),_CucsEtherTxStatsHistMulticastPackets_Type())
cucsEtherTxStatsHistMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistMulticastPackets.setStatus(_A)
_CucsEtherTxStatsHistMulticastPacketsDelta_Type=Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDelta=_CucsEtherTxStatsHistMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,17),_CucsEtherTxStatsHistMulticastPacketsDelta_Type())
cucsEtherTxStatsHistMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistMulticastPacketsDelta.setStatus(_A)
_CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDeltaAvg=_CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,18),_CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Type())
cucsEtherTxStatsHistMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistMulticastPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsHistMulticastPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDeltaMax=_CucsEtherTxStatsHistMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,19),_CucsEtherTxStatsHistMulticastPacketsDeltaMax_Type())
cucsEtherTxStatsHistMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistMulticastPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsHistMulticastPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDeltaMin=_CucsEtherTxStatsHistMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,20),_CucsEtherTxStatsHistMulticastPacketsDeltaMin_Type())
cucsEtherTxStatsHistMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistMulticastPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsHistSuspect_Type=TruthValue
_CucsEtherTxStatsHistSuspect_Object=MibTableColumn
cucsEtherTxStatsHistSuspect=_CucsEtherTxStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,21),_CucsEtherTxStatsHistSuspect_Type())
cucsEtherTxStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistSuspect.setStatus(_A)
_CucsEtherTxStatsHistThresholded_Type=CucsEtherTxStatsHistThresholded
_CucsEtherTxStatsHistThresholded_Object=MibTableColumn
cucsEtherTxStatsHistThresholded=_CucsEtherTxStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,22),_CucsEtherTxStatsHistThresholded_Type())
cucsEtherTxStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistThresholded.setStatus(_A)
_CucsEtherTxStatsHistTimeCollected_Type=DateAndTime
_CucsEtherTxStatsHistTimeCollected_Object=MibTableColumn
cucsEtherTxStatsHistTimeCollected=_CucsEtherTxStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,23),_CucsEtherTxStatsHistTimeCollected_Type())
cucsEtherTxStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTimeCollected.setStatus(_A)
_CucsEtherTxStatsHistTotalBytes_Type=Unsigned64
_CucsEtherTxStatsHistTotalBytes_Object=MibTableColumn
cucsEtherTxStatsHistTotalBytes=_CucsEtherTxStatsHistTotalBytes_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,24),_CucsEtherTxStatsHistTotalBytes_Type())
cucsEtherTxStatsHistTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalBytes.setStatus(_A)
_CucsEtherTxStatsHistTotalBytesDelta_Type=Unsigned64
_CucsEtherTxStatsHistTotalBytesDelta_Object=MibTableColumn
cucsEtherTxStatsHistTotalBytesDelta=_CucsEtherTxStatsHistTotalBytesDelta_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,25),_CucsEtherTxStatsHistTotalBytesDelta_Type())
cucsEtherTxStatsHistTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalBytesDelta.setStatus(_A)
_CucsEtherTxStatsHistTotalBytesDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsHistTotalBytesDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsHistTotalBytesDeltaAvg=_CucsEtherTxStatsHistTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,26),_CucsEtherTxStatsHistTotalBytesDeltaAvg_Type())
cucsEtherTxStatsHistTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalBytesDeltaAvg.setStatus(_A)
_CucsEtherTxStatsHistTotalBytesDeltaMax_Type=Unsigned64
_CucsEtherTxStatsHistTotalBytesDeltaMax_Object=MibTableColumn
cucsEtherTxStatsHistTotalBytesDeltaMax=_CucsEtherTxStatsHistTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,27),_CucsEtherTxStatsHistTotalBytesDeltaMax_Type())
cucsEtherTxStatsHistTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalBytesDeltaMax.setStatus(_A)
_CucsEtherTxStatsHistTotalBytesDeltaMin_Type=Unsigned64
_CucsEtherTxStatsHistTotalBytesDeltaMin_Object=MibTableColumn
cucsEtherTxStatsHistTotalBytesDeltaMin=_CucsEtherTxStatsHistTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,28),_CucsEtherTxStatsHistTotalBytesDeltaMin_Type())
cucsEtherTxStatsHistTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalBytesDeltaMin.setStatus(_A)
_CucsEtherTxStatsHistTotalPackets_Type=Unsigned64
_CucsEtherTxStatsHistTotalPackets_Object=MibTableColumn
cucsEtherTxStatsHistTotalPackets=_CucsEtherTxStatsHistTotalPackets_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,29),_CucsEtherTxStatsHistTotalPackets_Type())
cucsEtherTxStatsHistTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalPackets.setStatus(_A)
_CucsEtherTxStatsHistTotalPacketsDelta_Type=Unsigned64
_CucsEtherTxStatsHistTotalPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsHistTotalPacketsDelta=_CucsEtherTxStatsHistTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,30),_CucsEtherTxStatsHistTotalPacketsDelta_Type())
cucsEtherTxStatsHistTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalPacketsDelta.setStatus(_A)
_CucsEtherTxStatsHistTotalPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsHistTotalPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsHistTotalPacketsDeltaAvg=_CucsEtherTxStatsHistTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,31),_CucsEtherTxStatsHistTotalPacketsDeltaAvg_Type())
cucsEtherTxStatsHistTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsHistTotalPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsHistTotalPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsHistTotalPacketsDeltaMax=_CucsEtherTxStatsHistTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,32),_CucsEtherTxStatsHistTotalPacketsDeltaMax_Type())
cucsEtherTxStatsHistTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsHistTotalPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsHistTotalPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsHistTotalPacketsDeltaMin=_CucsEtherTxStatsHistTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,33),_CucsEtherTxStatsHistTotalPacketsDeltaMin_Type())
cucsEtherTxStatsHistTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistTotalPacketsDeltaMin.setStatus(_A)
_CucsEtherTxStatsHistUnicastPackets_Type=Unsigned64
_CucsEtherTxStatsHistUnicastPackets_Object=MibTableColumn
cucsEtherTxStatsHistUnicastPackets=_CucsEtherTxStatsHistUnicastPackets_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,34),_CucsEtherTxStatsHistUnicastPackets_Type())
cucsEtherTxStatsHistUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistUnicastPackets.setStatus(_A)
_CucsEtherTxStatsHistUnicastPacketsDelta_Type=Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDelta_Object=MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDelta=_CucsEtherTxStatsHistUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,35),_CucsEtherTxStatsHistUnicastPacketsDelta_Type())
cucsEtherTxStatsHistUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistUnicastPacketsDelta.setStatus(_A)
_CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Type=Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Object=MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDeltaAvg=_CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,36),_CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Type())
cucsEtherTxStatsHistUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistUnicastPacketsDeltaAvg.setStatus(_A)
_CucsEtherTxStatsHistUnicastPacketsDeltaMax_Type=Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDeltaMax_Object=MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDeltaMax=_CucsEtherTxStatsHistUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,37),_CucsEtherTxStatsHistUnicastPacketsDeltaMax_Type())
cucsEtherTxStatsHistUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistUnicastPacketsDeltaMax.setStatus(_A)
_CucsEtherTxStatsHistUnicastPacketsDeltaMin_Type=Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDeltaMin_Object=MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDeltaMin=_CucsEtherTxStatsHistUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,15,1,38),_CucsEtherTxStatsHistUnicastPacketsDeltaMin_Type())
cucsEtherTxStatsHistUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherTxStatsHistUnicastPacketsDeltaMin.setStatus(_A)
_CucsEtherPortChanIdElemTable_Object=MibTable
cucsEtherPortChanIdElemTable=_CucsEtherPortChanIdElemTable_Object((1,3,6,1,4,1,9,9,719,1,16,16))
if mibBuilder.loadTexts:cucsEtherPortChanIdElemTable.setStatus(_A)
_CucsEtherPortChanIdElemEntry_Object=MibTableRow
cucsEtherPortChanIdElemEntry=_CucsEtherPortChanIdElemEntry_Object((1,3,6,1,4,1,9,9,719,1,16,16,1))
cucsEtherPortChanIdElemEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsEtherPortChanIdElemEntry.setStatus(_A)
_CucsEtherPortChanIdElemInstanceId_Type=CucsManagedObjectId
_CucsEtherPortChanIdElemInstanceId_Object=MibTableColumn
cucsEtherPortChanIdElemInstanceId=_CucsEtherPortChanIdElemInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,1),_CucsEtherPortChanIdElemInstanceId_Type())
cucsEtherPortChanIdElemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemInstanceId.setStatus(_A)
_CucsEtherPortChanIdElemDn_Type=CucsManagedObjectDn
_CucsEtherPortChanIdElemDn_Object=MibTableColumn
cucsEtherPortChanIdElemDn=_CucsEtherPortChanIdElemDn_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,2),_CucsEtherPortChanIdElemDn_Type())
cucsEtherPortChanIdElemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemDn.setStatus(_A)
_CucsEtherPortChanIdElemRn_Type=SnmpAdminString
_CucsEtherPortChanIdElemRn_Object=MibTableColumn
cucsEtherPortChanIdElemRn=_CucsEtherPortChanIdElemRn_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,3),_CucsEtherPortChanIdElemRn_Type())
cucsEtherPortChanIdElemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemRn.setStatus(_A)
_CucsEtherPortChanIdElemId_Type=Gauge32
_CucsEtherPortChanIdElemId_Object=MibTableColumn
cucsEtherPortChanIdElemId=_CucsEtherPortChanIdElemId_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,4),_CucsEtherPortChanIdElemId_Type())
cucsEtherPortChanIdElemId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemId.setStatus(_A)
_CucsEtherPortChanIdElemAssignedToDn_Type=SnmpAdminString
_CucsEtherPortChanIdElemAssignedToDn_Object=MibTableColumn
cucsEtherPortChanIdElemAssignedToDn=_CucsEtherPortChanIdElemAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,5),_CucsEtherPortChanIdElemAssignedToDn_Type())
cucsEtherPortChanIdElemAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemAssignedToDn.setStatus(_A)
_CucsEtherPortChanIdElemPrevAssignedToDn_Type=SnmpAdminString
_CucsEtherPortChanIdElemPrevAssignedToDn_Object=MibTableColumn
cucsEtherPortChanIdElemPrevAssignedToDn=_CucsEtherPortChanIdElemPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,6),_CucsEtherPortChanIdElemPrevAssignedToDn_Type())
cucsEtherPortChanIdElemPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemPrevAssignedToDn.setStatus(_A)
_CucsEtherPortChanIdElemReserved_Type=TruthValue
_CucsEtherPortChanIdElemReserved_Object=MibTableColumn
cucsEtherPortChanIdElemReserved=_CucsEtherPortChanIdElemReserved_Object((1,3,6,1,4,1,9,9,719,1,16,16,1,7),_CucsEtherPortChanIdElemReserved_Type())
cucsEtherPortChanIdElemReserved.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdElemReserved.setStatus(_A)
_CucsEtherPortChanIdUniverseTable_Object=MibTable
cucsEtherPortChanIdUniverseTable=_CucsEtherPortChanIdUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,16,17))
if mibBuilder.loadTexts:cucsEtherPortChanIdUniverseTable.setStatus(_A)
_CucsEtherPortChanIdUniverseEntry_Object=MibTableRow
cucsEtherPortChanIdUniverseEntry=_CucsEtherPortChanIdUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,16,17,1))
cucsEtherPortChanIdUniverseEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cucsEtherPortChanIdUniverseEntry.setStatus(_A)
_CucsEtherPortChanIdUniverseInstanceId_Type=CucsManagedObjectId
_CucsEtherPortChanIdUniverseInstanceId_Object=MibTableColumn
cucsEtherPortChanIdUniverseInstanceId=_CucsEtherPortChanIdUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,17,1,1),_CucsEtherPortChanIdUniverseInstanceId_Type())
cucsEtherPortChanIdUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPortChanIdUniverseInstanceId.setStatus(_A)
_CucsEtherPortChanIdUniverseDn_Type=CucsManagedObjectDn
_CucsEtherPortChanIdUniverseDn_Object=MibTableColumn
cucsEtherPortChanIdUniverseDn=_CucsEtherPortChanIdUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,16,17,1,2),_CucsEtherPortChanIdUniverseDn_Type())
cucsEtherPortChanIdUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdUniverseDn.setStatus(_A)
_CucsEtherPortChanIdUniverseRn_Type=SnmpAdminString
_CucsEtherPortChanIdUniverseRn_Object=MibTableColumn
cucsEtherPortChanIdUniverseRn=_CucsEtherPortChanIdUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,16,17,1,3),_CucsEtherPortChanIdUniverseRn_Type())
cucsEtherPortChanIdUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPortChanIdUniverseRn.setStatus(_A)
_CucsEtherServerIntFIoPcTable_Object=MibTable
cucsEtherServerIntFIoPcTable=_CucsEtherServerIntFIoPcTable_Object((1,3,6,1,4,1,9,9,719,1,16,18))
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcTable.setStatus(_A)
_CucsEtherServerIntFIoPcEntry_Object=MibTableRow
cucsEtherServerIntFIoPcEntry=_CucsEtherServerIntFIoPcEntry_Object((1,3,6,1,4,1,9,9,719,1,16,18,1))
cucsEtherServerIntFIoPcEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEntry.setStatus(_A)
_CucsEtherServerIntFIoPcInstanceId_Type=CucsManagedObjectId
_CucsEtherServerIntFIoPcInstanceId_Object=MibTableColumn
cucsEtherServerIntFIoPcInstanceId=_CucsEtherServerIntFIoPcInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,1),_CucsEtherServerIntFIoPcInstanceId_Type())
cucsEtherServerIntFIoPcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcInstanceId.setStatus(_A)
_CucsEtherServerIntFIoPcDn_Type=CucsManagedObjectDn
_CucsEtherServerIntFIoPcDn_Object=MibTableColumn
cucsEtherServerIntFIoPcDn=_CucsEtherServerIntFIoPcDn_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,2),_CucsEtherServerIntFIoPcDn_Type())
cucsEtherServerIntFIoPcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcDn.setStatus(_A)
_CucsEtherServerIntFIoPcRn_Type=SnmpAdminString
_CucsEtherServerIntFIoPcRn_Object=MibTableColumn
cucsEtherServerIntFIoPcRn=_CucsEtherServerIntFIoPcRn_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,3),_CucsEtherServerIntFIoPcRn_Type())
cucsEtherServerIntFIoPcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcRn.setStatus(_A)
_CucsEtherServerIntFIoPcChassisId_Type=Gauge32
_CucsEtherServerIntFIoPcChassisId_Object=MibTableColumn
cucsEtherServerIntFIoPcChassisId=_CucsEtherServerIntFIoPcChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,4),_CucsEtherServerIntFIoPcChassisId_Type())
cucsEtherServerIntFIoPcChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcChassisId.setStatus(_A)
_CucsEtherServerIntFIoPcEpDn_Type=SnmpAdminString
_CucsEtherServerIntFIoPcEpDn_Object=MibTableColumn
cucsEtherServerIntFIoPcEpDn=_CucsEtherServerIntFIoPcEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,5),_CucsEtherServerIntFIoPcEpDn_Type())
cucsEtherServerIntFIoPcEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpDn.setStatus(_A)
_CucsEtherServerIntFIoPcFltAggr_Type=Unsigned64
_CucsEtherServerIntFIoPcFltAggr_Object=MibTableColumn
cucsEtherServerIntFIoPcFltAggr=_CucsEtherServerIntFIoPcFltAggr_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,6),_CucsEtherServerIntFIoPcFltAggr_Type())
cucsEtherServerIntFIoPcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcFltAggr.setStatus(_A)
_CucsEtherServerIntFIoPcIfRole_Type=CucsEtherServerIntFIoPcIfRole
_CucsEtherServerIntFIoPcIfRole_Object=MibTableColumn
cucsEtherServerIntFIoPcIfRole=_CucsEtherServerIntFIoPcIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,7),_CucsEtherServerIntFIoPcIfRole_Type())
cucsEtherServerIntFIoPcIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcIfRole.setStatus(_A)
_CucsEtherServerIntFIoPcIfType_Type=CucsEtherCIoEpIfType
_CucsEtherServerIntFIoPcIfType_Object=MibTableColumn
cucsEtherServerIntFIoPcIfType=_CucsEtherServerIntFIoPcIfType_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,8),_CucsEtherServerIntFIoPcIfType_Type())
cucsEtherServerIntFIoPcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcIfType.setStatus(_A)
_CucsEtherServerIntFIoPcLocale_Type=CucsEtherInternalPcLocale
_CucsEtherServerIntFIoPcLocale_Object=MibTableColumn
cucsEtherServerIntFIoPcLocale=_CucsEtherServerIntFIoPcLocale_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,9),_CucsEtherServerIntFIoPcLocale_Type())
cucsEtherServerIntFIoPcLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcLocale.setStatus(_A)
_CucsEtherServerIntFIoPcName_Type=SnmpAdminString
_CucsEtherServerIntFIoPcName_Object=MibTableColumn
cucsEtherServerIntFIoPcName=_CucsEtherServerIntFIoPcName_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,10),_CucsEtherServerIntFIoPcName_Type())
cucsEtherServerIntFIoPcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcName.setStatus(_A)
_CucsEtherServerIntFIoPcOperSpeed_Type=CucsPortEthSpeed
_CucsEtherServerIntFIoPcOperSpeed_Object=MibTableColumn
cucsEtherServerIntFIoPcOperSpeed=_CucsEtherServerIntFIoPcOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,11),_CucsEtherServerIntFIoPcOperSpeed_Type())
cucsEtherServerIntFIoPcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcOperSpeed.setStatus(_A)
_CucsEtherServerIntFIoPcOperState_Type=CucsNetworkPortOperState
_CucsEtherServerIntFIoPcOperState_Object=MibTableColumn
cucsEtherServerIntFIoPcOperState=_CucsEtherServerIntFIoPcOperState_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,12),_CucsEtherServerIntFIoPcOperState_Type())
cucsEtherServerIntFIoPcOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcOperState.setStatus(_A)
_CucsEtherServerIntFIoPcPeerDn_Type=SnmpAdminString
_CucsEtherServerIntFIoPcPeerDn_Object=MibTableColumn
cucsEtherServerIntFIoPcPeerDn=_CucsEtherServerIntFIoPcPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,13),_CucsEtherServerIntFIoPcPeerDn_Type())
cucsEtherServerIntFIoPcPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcPeerDn.setStatus(_A)
_CucsEtherServerIntFIoPcPortId_Type=CucsEtherServerIntFIoPcPortId
_CucsEtherServerIntFIoPcPortId_Object=MibTableColumn
cucsEtherServerIntFIoPcPortId=_CucsEtherServerIntFIoPcPortId_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,14),_CucsEtherServerIntFIoPcPortId_Type())
cucsEtherServerIntFIoPcPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcPortId.setStatus(_A)
_CucsEtherServerIntFIoPcStateQual_Type=SnmpAdminString
_CucsEtherServerIntFIoPcStateQual_Object=MibTableColumn
cucsEtherServerIntFIoPcStateQual=_CucsEtherServerIntFIoPcStateQual_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,15),_CucsEtherServerIntFIoPcStateQual_Type())
cucsEtherServerIntFIoPcStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcStateQual.setStatus(_A)
_CucsEtherServerIntFIoPcSwitchId_Type=CucsNetworkSwitchId
_CucsEtherServerIntFIoPcSwitchId_Object=MibTableColumn
cucsEtherServerIntFIoPcSwitchId=_CucsEtherServerIntFIoPcSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,16),_CucsEtherServerIntFIoPcSwitchId_Type())
cucsEtherServerIntFIoPcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcSwitchId.setStatus(_A)
_CucsEtherServerIntFIoPcTransport_Type=CucsEtherServerIntFIoPcTransport
_CucsEtherServerIntFIoPcTransport_Object=MibTableColumn
cucsEtherServerIntFIoPcTransport=_CucsEtherServerIntFIoPcTransport_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,17),_CucsEtherServerIntFIoPcTransport_Type())
cucsEtherServerIntFIoPcTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcTransport.setStatus(_A)
_CucsEtherServerIntFIoPcType_Type=CucsEtherServerIntFIoPcType
_CucsEtherServerIntFIoPcType_Object=MibTableColumn
cucsEtherServerIntFIoPcType=_CucsEtherServerIntFIoPcType_Object((1,3,6,1,4,1,9,9,719,1,16,18,1,18),_CucsEtherServerIntFIoPcType_Type())
cucsEtherServerIntFIoPcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcType.setStatus(_A)
_CucsEtherServerIntFIoPcEpTable_Object=MibTable
cucsEtherServerIntFIoPcEpTable=_CucsEtherServerIntFIoPcEpTable_Object((1,3,6,1,4,1,9,9,719,1,16,19))
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpTable.setStatus(_A)
_CucsEtherServerIntFIoPcEpEntry_Object=MibTableRow
cucsEtherServerIntFIoPcEpEntry=_CucsEtherServerIntFIoPcEpEntry_Object((1,3,6,1,4,1,9,9,719,1,16,19,1))
cucsEtherServerIntFIoPcEpEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpEntry.setStatus(_A)
_CucsEtherServerIntFIoPcEpInstanceId_Type=CucsManagedObjectId
_CucsEtherServerIntFIoPcEpInstanceId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpInstanceId=_CucsEtherServerIntFIoPcEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,1),_CucsEtherServerIntFIoPcEpInstanceId_Type())
cucsEtherServerIntFIoPcEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpInstanceId.setStatus(_A)
_CucsEtherServerIntFIoPcEpDnData_Type=CucsManagedObjectDn
_CucsEtherServerIntFIoPcEpDnData_Object=MibTableColumn
cucsEtherServerIntFIoPcEpDnData=_CucsEtherServerIntFIoPcEpDnData_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,2),_CucsEtherServerIntFIoPcEpDnData_Type())
cucsEtherServerIntFIoPcEpDnData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpDnData.setStatus(_A)
_CucsEtherServerIntFIoPcEpRn_Type=SnmpAdminString
_CucsEtherServerIntFIoPcEpRn_Object=MibTableColumn
cucsEtherServerIntFIoPcEpRn=_CucsEtherServerIntFIoPcEpRn_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,3),_CucsEtherServerIntFIoPcEpRn_Type())
cucsEtherServerIntFIoPcEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpRn.setStatus(_A)
_CucsEtherServerIntFIoPcEpAdminState_Type=CucsEtherExternalEpAdminState
_CucsEtherServerIntFIoPcEpAdminState_Object=MibTableColumn
cucsEtherServerIntFIoPcEpAdminState=_CucsEtherServerIntFIoPcEpAdminState_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,4),_CucsEtherServerIntFIoPcEpAdminState_Type())
cucsEtherServerIntFIoPcEpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpAdminState.setStatus(_A)
_CucsEtherServerIntFIoPcEpChassisId_Type=Gauge32
_CucsEtherServerIntFIoPcEpChassisId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpChassisId=_CucsEtherServerIntFIoPcEpChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,5),_CucsEtherServerIntFIoPcEpChassisId_Type())
cucsEtherServerIntFIoPcEpChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpChassisId.setStatus(_A)
_CucsEtherServerIntFIoPcEpEpDn_Type=SnmpAdminString
_CucsEtherServerIntFIoPcEpEpDn_Object=MibTableColumn
cucsEtherServerIntFIoPcEpEpDn=_CucsEtherServerIntFIoPcEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,6),_CucsEtherServerIntFIoPcEpEpDn_Type())
cucsEtherServerIntFIoPcEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpEpDn.setStatus(_A)
_CucsEtherServerIntFIoPcEpIfRole_Type=CucsEtherServerIntFIoPcEpIfRole
_CucsEtherServerIntFIoPcEpIfRole_Object=MibTableColumn
cucsEtherServerIntFIoPcEpIfRole=_CucsEtherServerIntFIoPcEpIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,7),_CucsEtherServerIntFIoPcEpIfRole_Type())
cucsEtherServerIntFIoPcEpIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpIfRole.setStatus(_A)
_CucsEtherServerIntFIoPcEpIfType_Type=CucsEtherPIoEpIfType
_CucsEtherServerIntFIoPcEpIfType_Object=MibTableColumn
cucsEtherServerIntFIoPcEpIfType=_CucsEtherServerIntFIoPcEpIfType_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,8),_CucsEtherServerIntFIoPcEpIfType_Type())
cucsEtherServerIntFIoPcEpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpIfType.setStatus(_A)
_CucsEtherServerIntFIoPcEpLocale_Type=CucsEtherExternalEpLocale
_CucsEtherServerIntFIoPcEpLocale_Object=MibTableColumn
cucsEtherServerIntFIoPcEpLocale=_CucsEtherServerIntFIoPcEpLocale_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,9),_CucsEtherServerIntFIoPcEpLocale_Type())
cucsEtherServerIntFIoPcEpLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpLocale.setStatus(_A)
_CucsEtherServerIntFIoPcEpMembership_Type=CucsFabricMembershipStatus
_CucsEtherServerIntFIoPcEpMembership_Object=MibTableColumn
cucsEtherServerIntFIoPcEpMembership=_CucsEtherServerIntFIoPcEpMembership_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,10),_CucsEtherServerIntFIoPcEpMembership_Type())
cucsEtherServerIntFIoPcEpMembership.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpMembership.setStatus(_A)
_CucsEtherServerIntFIoPcEpName_Type=SnmpAdminString
_CucsEtherServerIntFIoPcEpName_Object=MibTableColumn
cucsEtherServerIntFIoPcEpName=_CucsEtherServerIntFIoPcEpName_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,11),_CucsEtherServerIntFIoPcEpName_Type())
cucsEtherServerIntFIoPcEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpName.setStatus(_A)
_CucsEtherServerIntFIoPcEpPeerChassisId_Type=Gauge32
_CucsEtherServerIntFIoPcEpPeerChassisId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpPeerChassisId=_CucsEtherServerIntFIoPcEpPeerChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,12),_CucsEtherServerIntFIoPcEpPeerChassisId_Type())
cucsEtherServerIntFIoPcEpPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpPeerChassisId.setStatus(_A)
_CucsEtherServerIntFIoPcEpPeerDn_Type=SnmpAdminString
_CucsEtherServerIntFIoPcEpPeerDn_Object=MibTableColumn
cucsEtherServerIntFIoPcEpPeerDn=_CucsEtherServerIntFIoPcEpPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,13),_CucsEtherServerIntFIoPcEpPeerDn_Type())
cucsEtherServerIntFIoPcEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpPeerDn.setStatus(_A)
_CucsEtherServerIntFIoPcEpPeerPortId_Type=Gauge32
_CucsEtherServerIntFIoPcEpPeerPortId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpPeerPortId=_CucsEtherServerIntFIoPcEpPeerPortId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,14),_CucsEtherServerIntFIoPcEpPeerPortId_Type())
cucsEtherServerIntFIoPcEpPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpPeerPortId.setStatus(_A)
_CucsEtherServerIntFIoPcEpPeerSlotId_Type=Gauge32
_CucsEtherServerIntFIoPcEpPeerSlotId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpPeerSlotId=_CucsEtherServerIntFIoPcEpPeerSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,15),_CucsEtherServerIntFIoPcEpPeerSlotId_Type())
cucsEtherServerIntFIoPcEpPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpPeerSlotId.setStatus(_A)
_CucsEtherServerIntFIoPcEpPortId_Type=CucsEtherServerIntFIoPcEpPortId
_CucsEtherServerIntFIoPcEpPortId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpPortId=_CucsEtherServerIntFIoPcEpPortId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,16),_CucsEtherServerIntFIoPcEpPortId_Type())
cucsEtherServerIntFIoPcEpPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpPortId.setStatus(_A)
_CucsEtherServerIntFIoPcEpSlotId_Type=Gauge32
_CucsEtherServerIntFIoPcEpSlotId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpSlotId=_CucsEtherServerIntFIoPcEpSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,17),_CucsEtherServerIntFIoPcEpSlotId_Type())
cucsEtherServerIntFIoPcEpSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpSlotId.setStatus(_A)
_CucsEtherServerIntFIoPcEpSwitchId_Type=CucsNetworkSwitchId
_CucsEtherServerIntFIoPcEpSwitchId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpSwitchId=_CucsEtherServerIntFIoPcEpSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,18),_CucsEtherServerIntFIoPcEpSwitchId_Type())
cucsEtherServerIntFIoPcEpSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpSwitchId.setStatus(_A)
_CucsEtherServerIntFIoPcEpTransport_Type=CucsNetworkTransport
_CucsEtherServerIntFIoPcEpTransport_Object=MibTableColumn
cucsEtherServerIntFIoPcEpTransport=_CucsEtherServerIntFIoPcEpTransport_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,19),_CucsEtherServerIntFIoPcEpTransport_Type())
cucsEtherServerIntFIoPcEpTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpTransport.setStatus(_A)
_CucsEtherServerIntFIoPcEpType_Type=CucsEtherIntFIoEpType
_CucsEtherServerIntFIoPcEpType_Object=MibTableColumn
cucsEtherServerIntFIoPcEpType=_CucsEtherServerIntFIoPcEpType_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,20),_CucsEtherServerIntFIoPcEpType_Type())
cucsEtherServerIntFIoPcEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpType.setStatus(_A)
_CucsEtherServerIntFIoPcEpAggrPortId_Type=Gauge32
_CucsEtherServerIntFIoPcEpAggrPortId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpAggrPortId=_CucsEtherServerIntFIoPcEpAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,21),_CucsEtherServerIntFIoPcEpAggrPortId_Type())
cucsEtherServerIntFIoPcEpAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpAggrPortId.setStatus(_A)
_CucsEtherServerIntFIoPcEpPeerAggrPortId_Type=Gauge32
_CucsEtherServerIntFIoPcEpPeerAggrPortId_Object=MibTableColumn
cucsEtherServerIntFIoPcEpPeerAggrPortId=_CucsEtherServerIntFIoPcEpPeerAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,19,1,22),_CucsEtherServerIntFIoPcEpPeerAggrPortId_Type())
cucsEtherServerIntFIoPcEpPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoPcEpPeerAggrPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPcTable_Object=MibTable
cucsEtherSwitchIntFIoPcTable=_CucsEtherSwitchIntFIoPcTable_Object((1,3,6,1,4,1,9,9,719,1,16,20))
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcTable.setStatus(_A)
_CucsEtherSwitchIntFIoPcEntry_Object=MibTableRow
cucsEtherSwitchIntFIoPcEntry=_CucsEtherSwitchIntFIoPcEntry_Object((1,3,6,1,4,1,9,9,719,1,16,20,1))
cucsEtherSwitchIntFIoPcEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEntry.setStatus(_A)
_CucsEtherSwitchIntFIoPcInstanceId_Type=CucsManagedObjectId
_CucsEtherSwitchIntFIoPcInstanceId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcInstanceId=_CucsEtherSwitchIntFIoPcInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,1),_CucsEtherSwitchIntFIoPcInstanceId_Type())
cucsEtherSwitchIntFIoPcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcInstanceId.setStatus(_A)
_CucsEtherSwitchIntFIoPcDn_Type=CucsManagedObjectDn
_CucsEtherSwitchIntFIoPcDn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcDn=_CucsEtherSwitchIntFIoPcDn_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,2),_CucsEtherSwitchIntFIoPcDn_Type())
cucsEtherSwitchIntFIoPcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcDn.setStatus(_A)
_CucsEtherSwitchIntFIoPcRn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcRn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcRn=_CucsEtherSwitchIntFIoPcRn_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,3),_CucsEtherSwitchIntFIoPcRn_Type())
cucsEtherSwitchIntFIoPcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcRn.setStatus(_A)
_CucsEtherSwitchIntFIoPcAdminState_Type=CucsEtherExternalPcAdminState
_CucsEtherSwitchIntFIoPcAdminState_Object=MibTableColumn
cucsEtherSwitchIntFIoPcAdminState=_CucsEtherSwitchIntFIoPcAdminState_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,4),_CucsEtherSwitchIntFIoPcAdminState_Type())
cucsEtherSwitchIntFIoPcAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcAdminState.setStatus(_A)
_CucsEtherSwitchIntFIoPcChassisId_Type=Gauge32
_CucsEtherSwitchIntFIoPcChassisId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcChassisId=_CucsEtherSwitchIntFIoPcChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,5),_CucsEtherSwitchIntFIoPcChassisId_Type())
cucsEtherSwitchIntFIoPcChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcChassisId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpDn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcEpDn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpDn=_CucsEtherSwitchIntFIoPcEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,6),_CucsEtherSwitchIntFIoPcEpDn_Type())
cucsEtherSwitchIntFIoPcEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpDn.setStatus(_A)
_CucsEtherSwitchIntFIoPcFltAggr_Type=Unsigned64
_CucsEtherSwitchIntFIoPcFltAggr_Object=MibTableColumn
cucsEtherSwitchIntFIoPcFltAggr=_CucsEtherSwitchIntFIoPcFltAggr_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,7),_CucsEtherSwitchIntFIoPcFltAggr_Type())
cucsEtherSwitchIntFIoPcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcFltAggr.setStatus(_A)
_CucsEtherSwitchIntFIoPcIfRole_Type=CucsEtherSwitchIntFIoPcIfRole
_CucsEtherSwitchIntFIoPcIfRole_Object=MibTableColumn
cucsEtherSwitchIntFIoPcIfRole=_CucsEtherSwitchIntFIoPcIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,8),_CucsEtherSwitchIntFIoPcIfRole_Type())
cucsEtherSwitchIntFIoPcIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcIfRole.setStatus(_A)
_CucsEtherSwitchIntFIoPcIfType_Type=CucsEtherCIoEpIfType
_CucsEtherSwitchIntFIoPcIfType_Object=MibTableColumn
cucsEtherSwitchIntFIoPcIfType=_CucsEtherSwitchIntFIoPcIfType_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,9),_CucsEtherSwitchIntFIoPcIfType_Type())
cucsEtherSwitchIntFIoPcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcIfType.setStatus(_A)
_CucsEtherSwitchIntFIoPcLocale_Type=CucsEtherExternalPcLocale
_CucsEtherSwitchIntFIoPcLocale_Object=MibTableColumn
cucsEtherSwitchIntFIoPcLocale=_CucsEtherSwitchIntFIoPcLocale_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,10),_CucsEtherSwitchIntFIoPcLocale_Type())
cucsEtherSwitchIntFIoPcLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcLocale.setStatus(_A)
_CucsEtherSwitchIntFIoPcName_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcName_Object=MibTableColumn
cucsEtherSwitchIntFIoPcName=_CucsEtherSwitchIntFIoPcName_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,11),_CucsEtherSwitchIntFIoPcName_Type())
cucsEtherSwitchIntFIoPcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcName.setStatus(_A)
_CucsEtherSwitchIntFIoPcOperSpeed_Type=CucsPortEthSpeed
_CucsEtherSwitchIntFIoPcOperSpeed_Object=MibTableColumn
cucsEtherSwitchIntFIoPcOperSpeed=_CucsEtherSwitchIntFIoPcOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,12),_CucsEtherSwitchIntFIoPcOperSpeed_Type())
cucsEtherSwitchIntFIoPcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcOperSpeed.setStatus(_A)
_CucsEtherSwitchIntFIoPcOperState_Type=CucsNetworkPortOperState
_CucsEtherSwitchIntFIoPcOperState_Object=MibTableColumn
cucsEtherSwitchIntFIoPcOperState=_CucsEtherSwitchIntFIoPcOperState_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,13),_CucsEtherSwitchIntFIoPcOperState_Type())
cucsEtherSwitchIntFIoPcOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcOperState.setStatus(_A)
_CucsEtherSwitchIntFIoPcPeerDn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcPeerDn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcPeerDn=_CucsEtherSwitchIntFIoPcPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,14),_CucsEtherSwitchIntFIoPcPeerDn_Type())
cucsEtherSwitchIntFIoPcPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcPeerDn.setStatus(_A)
_CucsEtherSwitchIntFIoPcPortId_Type=CucsEtherSwitchIntFIoPcPortId
_CucsEtherSwitchIntFIoPcPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcPortId=_CucsEtherSwitchIntFIoPcPortId_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,15),_CucsEtherSwitchIntFIoPcPortId_Type())
cucsEtherSwitchIntFIoPcPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPcStateQual_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcStateQual_Object=MibTableColumn
cucsEtherSwitchIntFIoPcStateQual=_CucsEtherSwitchIntFIoPcStateQual_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,16),_CucsEtherSwitchIntFIoPcStateQual_Type())
cucsEtherSwitchIntFIoPcStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcStateQual.setStatus(_A)
_CucsEtherSwitchIntFIoPcSwitchId_Type=CucsNetworkSwitchId
_CucsEtherSwitchIntFIoPcSwitchId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcSwitchId=_CucsEtherSwitchIntFIoPcSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,17),_CucsEtherSwitchIntFIoPcSwitchId_Type())
cucsEtherSwitchIntFIoPcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcSwitchId.setStatus(_A)
_CucsEtherSwitchIntFIoPcTransport_Type=CucsEtherSwitchIntFIoPcTransport
_CucsEtherSwitchIntFIoPcTransport_Object=MibTableColumn
cucsEtherSwitchIntFIoPcTransport=_CucsEtherSwitchIntFIoPcTransport_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,18),_CucsEtherSwitchIntFIoPcTransport_Type())
cucsEtherSwitchIntFIoPcTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcTransport.setStatus(_A)
_CucsEtherSwitchIntFIoPcType_Type=CucsEtherSwitchIntFIoPcType
_CucsEtherSwitchIntFIoPcType_Object=MibTableColumn
cucsEtherSwitchIntFIoPcType=_CucsEtherSwitchIntFIoPcType_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,19),_CucsEtherSwitchIntFIoPcType_Type())
cucsEtherSwitchIntFIoPcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcType.setStatus(_A)
_CucsEtherSwitchIntFIoPcMulticastHwHash_Type=CucsEtherSwitchIntFIoPcMulticastHwHash
_CucsEtherSwitchIntFIoPcMulticastHwHash_Object=MibTableColumn
cucsEtherSwitchIntFIoPcMulticastHwHash=_CucsEtherSwitchIntFIoPcMulticastHwHash_Object((1,3,6,1,4,1,9,9,719,1,16,20,1,20),_CucsEtherSwitchIntFIoPcMulticastHwHash_Type())
cucsEtherSwitchIntFIoPcMulticastHwHash.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcMulticastHwHash.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpTable_Object=MibTable
cucsEtherSwitchIntFIoPcEpTable=_CucsEtherSwitchIntFIoPcEpTable_Object((1,3,6,1,4,1,9,9,719,1,16,21))
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpTable.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpEntry_Object=MibTableRow
cucsEtherSwitchIntFIoPcEpEntry=_CucsEtherSwitchIntFIoPcEpEntry_Object((1,3,6,1,4,1,9,9,719,1,16,21,1))
cucsEtherSwitchIntFIoPcEpEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpEntry.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpInstanceId_Type=CucsManagedObjectId
_CucsEtherSwitchIntFIoPcEpInstanceId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpInstanceId=_CucsEtherSwitchIntFIoPcEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,1),_CucsEtherSwitchIntFIoPcEpInstanceId_Type())
cucsEtherSwitchIntFIoPcEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpInstanceId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpDnData_Type=CucsManagedObjectDn
_CucsEtherSwitchIntFIoPcEpDnData_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpDnData=_CucsEtherSwitchIntFIoPcEpDnData_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,2),_CucsEtherSwitchIntFIoPcEpDnData_Type())
cucsEtherSwitchIntFIoPcEpDnData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpDnData.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpRn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcEpRn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpRn=_CucsEtherSwitchIntFIoPcEpRn_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,3),_CucsEtherSwitchIntFIoPcEpRn_Type())
cucsEtherSwitchIntFIoPcEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpRn.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpAdminState_Type=CucsEtherExternalEpAdminState
_CucsEtherSwitchIntFIoPcEpAdminState_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpAdminState=_CucsEtherSwitchIntFIoPcEpAdminState_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,4),_CucsEtherSwitchIntFIoPcEpAdminState_Type())
cucsEtherSwitchIntFIoPcEpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpAdminState.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpChassisId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpChassisId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpChassisId=_CucsEtherSwitchIntFIoPcEpChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,5),_CucsEtherSwitchIntFIoPcEpChassisId_Type())
cucsEtherSwitchIntFIoPcEpChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpChassisId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpEpDn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcEpEpDn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpEpDn=_CucsEtherSwitchIntFIoPcEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,6),_CucsEtherSwitchIntFIoPcEpEpDn_Type())
cucsEtherSwitchIntFIoPcEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpEpDn.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpIfRole_Type=CucsEtherSwitchIntFIoPcEpIfRole
_CucsEtherSwitchIntFIoPcEpIfRole_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpIfRole=_CucsEtherSwitchIntFIoPcEpIfRole_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,7),_CucsEtherSwitchIntFIoPcEpIfRole_Type())
cucsEtherSwitchIntFIoPcEpIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpIfRole.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpIfType_Type=CucsEtherPIoEpIfType
_CucsEtherSwitchIntFIoPcEpIfType_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpIfType=_CucsEtherSwitchIntFIoPcEpIfType_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,8),_CucsEtherSwitchIntFIoPcEpIfType_Type())
cucsEtherSwitchIntFIoPcEpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpIfType.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpLocale_Type=CucsEtherExternalEpLocale
_CucsEtherSwitchIntFIoPcEpLocale_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpLocale=_CucsEtherSwitchIntFIoPcEpLocale_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,9),_CucsEtherSwitchIntFIoPcEpLocale_Type())
cucsEtherSwitchIntFIoPcEpLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpLocale.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpMembership_Type=CucsFabricMembershipStatus
_CucsEtherSwitchIntFIoPcEpMembership_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpMembership=_CucsEtherSwitchIntFIoPcEpMembership_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,10),_CucsEtherSwitchIntFIoPcEpMembership_Type())
cucsEtherSwitchIntFIoPcEpMembership.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpMembership.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpName_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcEpName_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpName=_CucsEtherSwitchIntFIoPcEpName_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,11),_CucsEtherSwitchIntFIoPcEpName_Type())
cucsEtherSwitchIntFIoPcEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpName.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpPeerChassisId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpPeerChassisId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerChassisId=_CucsEtherSwitchIntFIoPcEpPeerChassisId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,12),_CucsEtherSwitchIntFIoPcEpPeerChassisId_Type())
cucsEtherSwitchIntFIoPcEpPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpPeerChassisId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpPeerDn_Type=SnmpAdminString
_CucsEtherSwitchIntFIoPcEpPeerDn_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerDn=_CucsEtherSwitchIntFIoPcEpPeerDn_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,13),_CucsEtherSwitchIntFIoPcEpPeerDn_Type())
cucsEtherSwitchIntFIoPcEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpPeerDn.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpPeerPortId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpPeerPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerPortId=_CucsEtherSwitchIntFIoPcEpPeerPortId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,14),_CucsEtherSwitchIntFIoPcEpPeerPortId_Type())
cucsEtherSwitchIntFIoPcEpPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpPeerPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpPeerSlotId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpPeerSlotId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerSlotId=_CucsEtherSwitchIntFIoPcEpPeerSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,15),_CucsEtherSwitchIntFIoPcEpPeerSlotId_Type())
cucsEtherSwitchIntFIoPcEpPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpPeerSlotId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpPortId_Type=CucsEtherSwitchIntFIoPcEpPortId
_CucsEtherSwitchIntFIoPcEpPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpPortId=_CucsEtherSwitchIntFIoPcEpPortId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,16),_CucsEtherSwitchIntFIoPcEpPortId_Type())
cucsEtherSwitchIntFIoPcEpPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpSlotId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpSlotId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpSlotId=_CucsEtherSwitchIntFIoPcEpSlotId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,17),_CucsEtherSwitchIntFIoPcEpSlotId_Type())
cucsEtherSwitchIntFIoPcEpSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpSlotId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpStatusChangeTs_Type=DateAndTime
_CucsEtherSwitchIntFIoPcEpStatusChangeTs_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpStatusChangeTs=_CucsEtherSwitchIntFIoPcEpStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,18),_CucsEtherSwitchIntFIoPcEpStatusChangeTs_Type())
cucsEtherSwitchIntFIoPcEpStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpStatusChangeTs.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpSwitchId_Type=CucsNetworkSwitchId
_CucsEtherSwitchIntFIoPcEpSwitchId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpSwitchId=_CucsEtherSwitchIntFIoPcEpSwitchId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,19),_CucsEtherSwitchIntFIoPcEpSwitchId_Type())
cucsEtherSwitchIntFIoPcEpSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpSwitchId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpTransport_Type=CucsNetworkTransport
_CucsEtherSwitchIntFIoPcEpTransport_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpTransport=_CucsEtherSwitchIntFIoPcEpTransport_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,20),_CucsEtherSwitchIntFIoPcEpTransport_Type())
cucsEtherSwitchIntFIoPcEpTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpTransport.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpType_Type=CucsEtherIntFIoEpType
_CucsEtherSwitchIntFIoPcEpType_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpType=_CucsEtherSwitchIntFIoPcEpType_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,21),_CucsEtherSwitchIntFIoPcEpType_Type())
cucsEtherSwitchIntFIoPcEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpType.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpAckState_Type=CucsEquipmentChassisConfigState
_CucsEtherSwitchIntFIoPcEpAckState_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpAckState=_CucsEtherSwitchIntFIoPcEpAckState_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,22),_CucsEtherSwitchIntFIoPcEpAckState_Type())
cucsEtherSwitchIntFIoPcEpAckState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpAckState.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpAggrPortId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpAggrPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpAggrPortId=_CucsEtherSwitchIntFIoPcEpAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,23),_CucsEtherSwitchIntFIoPcEpAggrPortId_Type())
cucsEtherSwitchIntFIoPcEpAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpAggrPortId.setStatus(_A)
_CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Type=Gauge32
_CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Object=MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerAggrPortId=_CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,16,21,1,24),_CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Type())
cucsEtherSwitchIntFIoPcEpPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherSwitchIntFIoPcEpPeerAggrPortId.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskTable_Object=MibTable
cucsEtherServerIntFIoFsmTaskTable=_CucsEtherServerIntFIoFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,16,22))
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskTable.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskEntry_Object=MibTableRow
cucsEtherServerIntFIoFsmTaskEntry=_CucsEtherServerIntFIoFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,16,22,1))
cucsEtherServerIntFIoFsmTaskEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskEntry.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsEtherServerIntFIoFsmTaskInstanceId_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskInstanceId=_CucsEtherServerIntFIoFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,1),_CucsEtherServerIntFIoFsmTaskInstanceId_Type())
cucsEtherServerIntFIoFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskInstanceId.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskDn_Type=CucsManagedObjectDn
_CucsEtherServerIntFIoFsmTaskDn_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskDn=_CucsEtherServerIntFIoFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,2),_CucsEtherServerIntFIoFsmTaskDn_Type())
cucsEtherServerIntFIoFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskDn.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskRn_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmTaskRn_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskRn=_CucsEtherServerIntFIoFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,3),_CucsEtherServerIntFIoFsmTaskRn_Type())
cucsEtherServerIntFIoFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskRn.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskCompletion_Type=CucsFsmCompletion
_CucsEtherServerIntFIoFsmTaskCompletion_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskCompletion=_CucsEtherServerIntFIoFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,4),_CucsEtherServerIntFIoFsmTaskCompletion_Type())
cucsEtherServerIntFIoFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskCompletion.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskFlags_Type=CucsFsmFlags
_CucsEtherServerIntFIoFsmTaskFlags_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskFlags=_CucsEtherServerIntFIoFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,5),_CucsEtherServerIntFIoFsmTaskFlags_Type())
cucsEtherServerIntFIoFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskFlags.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskItem_Type=CucsEtherServerIntFIoFsmTaskItem
_CucsEtherServerIntFIoFsmTaskItem_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskItem=_CucsEtherServerIntFIoFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,6),_CucsEtherServerIntFIoFsmTaskItem_Type())
cucsEtherServerIntFIoFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskItem.setStatus(_A)
_CucsEtherServerIntFIoFsmTaskSeqId_Type=Gauge32
_CucsEtherServerIntFIoFsmTaskSeqId_Object=MibTableColumn
cucsEtherServerIntFIoFsmTaskSeqId=_CucsEtherServerIntFIoFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,16,22,1,7),_CucsEtherServerIntFIoFsmTaskSeqId_Type())
cucsEtherServerIntFIoFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTaskSeqId.setStatus(_A)
_CucsEtherFcoeInterfaceStatsTable_Object=MibTable
cucsEtherFcoeInterfaceStatsTable=_CucsEtherFcoeInterfaceStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,23))
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsTable.setStatus(_A)
_CucsEtherFcoeInterfaceStatsEntry_Object=MibTableRow
cucsEtherFcoeInterfaceStatsEntry=_CucsEtherFcoeInterfaceStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,23,1))
cucsEtherFcoeInterfaceStatsEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsEntry.setStatus(_A)
_CucsEtherFcoeInterfaceStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherFcoeInterfaceStatsInstanceId_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsInstanceId=_CucsEtherFcoeInterfaceStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,1),_CucsEtherFcoeInterfaceStatsInstanceId_Type())
cucsEtherFcoeInterfaceStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsInstanceId.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDn_Type=CucsManagedObjectDn
_CucsEtherFcoeInterfaceStatsDn_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDn=_CucsEtherFcoeInterfaceStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,2),_CucsEtherFcoeInterfaceStatsDn_Type())
cucsEtherFcoeInterfaceStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDn.setStatus(_A)
_CucsEtherFcoeInterfaceStatsRn_Type=SnmpAdminString
_CucsEtherFcoeInterfaceStatsRn_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsRn=_CucsEtherFcoeInterfaceStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,3),_CucsEtherFcoeInterfaceStatsRn_Type())
cucsEtherFcoeInterfaceStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsRn.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRx=_CucsEtherFcoeInterfaceStatsBytesRx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,4),_CucsEtherFcoeInterfaceStatsBytesRx_Type())
cucsEtherFcoeInterfaceStatsBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesRxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsBytesRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDelta=_CucsEtherFcoeInterfaceStatsBytesRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,5),_CucsEtherFcoeInterfaceStatsBytesRxDelta_Type())
cucsEtherFcoeInterfaceStatsBytesRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg=_CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,6),_CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDeltaMax=_CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,7),_CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsBytesRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDeltaMin=_CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,8),_CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsBytesRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTx=_CucsEtherFcoeInterfaceStatsBytesTx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,9),_CucsEtherFcoeInterfaceStatsBytesTx_Type())
cucsEtherFcoeInterfaceStatsBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesTxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsBytesTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDelta=_CucsEtherFcoeInterfaceStatsBytesTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,10),_CucsEtherFcoeInterfaceStatsBytesTxDelta_Type())
cucsEtherFcoeInterfaceStatsBytesTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg=_CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,11),_CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDeltaMax=_CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,12),_CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsBytesTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDeltaMin=_CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,13),_CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsBytesTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsBytesTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRx=_CucsEtherFcoeInterfaceStatsDroppedRx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,14),_CucsEtherFcoeInterfaceStatsDroppedRx_Type())
cucsEtherFcoeInterfaceStatsDroppedRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedRxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsDroppedRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDelta=_CucsEtherFcoeInterfaceStatsDroppedRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,15),_CucsEtherFcoeInterfaceStatsDroppedRxDelta_Type())
cucsEtherFcoeInterfaceStatsDroppedRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg=_CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,16),_CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax=_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,17),_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin=_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,18),_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTx=_CucsEtherFcoeInterfaceStatsDroppedTx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,19),_CucsEtherFcoeInterfaceStatsDroppedTx_Type())
cucsEtherFcoeInterfaceStatsDroppedTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedTxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsDroppedTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDelta=_CucsEtherFcoeInterfaceStatsDroppedTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,20),_CucsEtherFcoeInterfaceStatsDroppedTxDelta_Type())
cucsEtherFcoeInterfaceStatsDroppedTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg=_CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,21),_CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax=_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,22),_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin=_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,23),_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRx=_CucsEtherFcoeInterfaceStatsErrorsRx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,24),_CucsEtherFcoeInterfaceStatsErrorsRx_Type())
cucsEtherFcoeInterfaceStatsErrorsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsRxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsErrorsRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDelta=_CucsEtherFcoeInterfaceStatsErrorsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,25),_CucsEtherFcoeInterfaceStatsErrorsRxDelta_Type())
cucsEtherFcoeInterfaceStatsErrorsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg=_CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,26),_CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax=_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,27),_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin=_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,28),_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTx=_CucsEtherFcoeInterfaceStatsErrorsTx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,29),_CucsEtherFcoeInterfaceStatsErrorsTx_Type())
cucsEtherFcoeInterfaceStatsErrorsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsTxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsErrorsTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDelta=_CucsEtherFcoeInterfaceStatsErrorsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,30),_CucsEtherFcoeInterfaceStatsErrorsTxDelta_Type())
cucsEtherFcoeInterfaceStatsErrorsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg=_CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,31),_CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax=_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,32),_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin=_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,33),_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsIntervals_Type=Gauge32
_CucsEtherFcoeInterfaceStatsIntervals_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsIntervals=_CucsEtherFcoeInterfaceStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,34),_CucsEtherFcoeInterfaceStatsIntervals_Type())
cucsEtherFcoeInterfaceStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsIntervals.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRx=_CucsEtherFcoeInterfaceStatsPacketsRx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,35),_CucsEtherFcoeInterfaceStatsPacketsRx_Type())
cucsEtherFcoeInterfaceStatsPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsRxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsPacketsRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDelta=_CucsEtherFcoeInterfaceStatsPacketsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,36),_CucsEtherFcoeInterfaceStatsPacketsRxDelta_Type())
cucsEtherFcoeInterfaceStatsPacketsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg=_CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,37),_CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax=_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,38),_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin=_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,39),_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTx=_CucsEtherFcoeInterfaceStatsPacketsTx_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,40),_CucsEtherFcoeInterfaceStatsPacketsTx_Type())
cucsEtherFcoeInterfaceStatsPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsTxDelta_Type=Counter64
_CucsEtherFcoeInterfaceStatsPacketsTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDelta=_CucsEtherFcoeInterfaceStatsPacketsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,41),_CucsEtherFcoeInterfaceStatsPacketsTxDelta_Type())
cucsEtherFcoeInterfaceStatsPacketsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg=_CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,42),_CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax=_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,43),_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin=_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,44),_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsSuspect_Type=TruthValue
_CucsEtherFcoeInterfaceStatsSuspect_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsSuspect=_CucsEtherFcoeInterfaceStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,45),_CucsEtherFcoeInterfaceStatsSuspect_Type())
cucsEtherFcoeInterfaceStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsSuspect.setStatus(_A)
_CucsEtherFcoeInterfaceStatsThresholded_Type=CucsEtherFcoeInterfaceStatsThresholded
_CucsEtherFcoeInterfaceStatsThresholded_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsThresholded=_CucsEtherFcoeInterfaceStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,46),_CucsEtherFcoeInterfaceStatsThresholded_Type())
cucsEtherFcoeInterfaceStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsThresholded.setStatus(_A)
_CucsEtherFcoeInterfaceStatsTimeCollected_Type=DateAndTime
_CucsEtherFcoeInterfaceStatsTimeCollected_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsTimeCollected=_CucsEtherFcoeInterfaceStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,47),_CucsEtherFcoeInterfaceStatsTimeCollected_Type())
cucsEtherFcoeInterfaceStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsTimeCollected.setStatus(_A)
_CucsEtherFcoeInterfaceStatsUpdate_Type=Gauge32
_CucsEtherFcoeInterfaceStatsUpdate_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsUpdate=_CucsEtherFcoeInterfaceStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,23,1,48),_CucsEtherFcoeInterfaceStatsUpdate_Type())
cucsEtherFcoeInterfaceStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsUpdate.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistTable_Object=MibTable
cucsEtherFcoeInterfaceStatsHistTable=_CucsEtherFcoeInterfaceStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,24))
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistTable.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistEntry_Object=MibTableRow
cucsEtherFcoeInterfaceStatsHistEntry=_CucsEtherFcoeInterfaceStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,24,1))
cucsEtherFcoeInterfaceStatsHistEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistEntry.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherFcoeInterfaceStatsHistInstanceId_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistInstanceId=_CucsEtherFcoeInterfaceStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,1),_CucsEtherFcoeInterfaceStatsHistInstanceId_Type())
cucsEtherFcoeInterfaceStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistInstanceId.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherFcoeInterfaceStatsHistDn_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDn=_CucsEtherFcoeInterfaceStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,2),_CucsEtherFcoeInterfaceStatsHistDn_Type())
cucsEtherFcoeInterfaceStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDn.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistRn_Type=SnmpAdminString
_CucsEtherFcoeInterfaceStatsHistRn_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistRn=_CucsEtherFcoeInterfaceStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,3),_CucsEtherFcoeInterfaceStatsHistRn_Type())
cucsEtherFcoeInterfaceStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistRn.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRx=_CucsEtherFcoeInterfaceStatsHistBytesRx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,4),_CucsEtherFcoeInterfaceStatsHistBytesRx_Type())
cucsEtherFcoeInterfaceStatsHistBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDelta=_CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,5),_CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Type())
cucsEtherFcoeInterfaceStatsHistBytesRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,6),_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax=_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,7),_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin=_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,8),_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTx=_CucsEtherFcoeInterfaceStatsHistBytesTx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,9),_CucsEtherFcoeInterfaceStatsHistBytesTx_Type())
cucsEtherFcoeInterfaceStatsHistBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDelta=_CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,10),_CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Type())
cucsEtherFcoeInterfaceStatsHistBytesTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,11),_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax=_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,12),_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin=_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,13),_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRx=_CucsEtherFcoeInterfaceStatsHistDroppedRx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,14),_CucsEtherFcoeInterfaceStatsHistDroppedRx_Type())
cucsEtherFcoeInterfaceStatsHistDroppedRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDelta=_CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,15),_CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Type())
cucsEtherFcoeInterfaceStatsHistDroppedRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,16),_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax=_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,17),_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin=_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,18),_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTx=_CucsEtherFcoeInterfaceStatsHistDroppedTx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,19),_CucsEtherFcoeInterfaceStatsHistDroppedTx_Type())
cucsEtherFcoeInterfaceStatsHistDroppedTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDelta=_CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,20),_CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Type())
cucsEtherFcoeInterfaceStatsHistDroppedTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,21),_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax=_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,22),_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin=_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,23),_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRx=_CucsEtherFcoeInterfaceStatsHistErrorsRx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,24),_CucsEtherFcoeInterfaceStatsHistErrorsRx_Type())
cucsEtherFcoeInterfaceStatsHistErrorsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDelta=_CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,25),_CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Type())
cucsEtherFcoeInterfaceStatsHistErrorsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,26),_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax=_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,27),_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin=_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,28),_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTx=_CucsEtherFcoeInterfaceStatsHistErrorsTx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,29),_CucsEtherFcoeInterfaceStatsHistErrorsTx_Type())
cucsEtherFcoeInterfaceStatsHistErrorsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDelta=_CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,30),_CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Type())
cucsEtherFcoeInterfaceStatsHistErrorsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,31),_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax=_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,32),_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin=_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,33),_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistId_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistId_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistId=_CucsEtherFcoeInterfaceStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,34),_CucsEtherFcoeInterfaceStatsHistId_Type())
cucsEtherFcoeInterfaceStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistId.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistMostRecent_Type=TruthValue
_CucsEtherFcoeInterfaceStatsHistMostRecent_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistMostRecent=_CucsEtherFcoeInterfaceStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,35),_CucsEtherFcoeInterfaceStatsHistMostRecent_Type())
cucsEtherFcoeInterfaceStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistMostRecent.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsRx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRx=_CucsEtherFcoeInterfaceStatsHistPacketsRx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,36),_CucsEtherFcoeInterfaceStatsHistPacketsRx_Type())
cucsEtherFcoeInterfaceStatsHistPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsRx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDelta=_CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,37),_CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Type())
cucsEtherFcoeInterfaceStatsHistPacketsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsRxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,38),_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax=_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,39),_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin=_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,40),_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsTx_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTx_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTx=_CucsEtherFcoeInterfaceStatsHistPacketsTx_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,41),_CucsEtherFcoeInterfaceStatsHistPacketsTx_Type())
cucsEtherFcoeInterfaceStatsHistPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsTx.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDelta=_CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,42),_CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Type())
cucsEtherFcoeInterfaceStatsHistPacketsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsTxDelta.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg=_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,43),_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type())
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax=_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,44),_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type())
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type=Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin=_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,45),_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type())
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistSuspect_Type=TruthValue
_CucsEtherFcoeInterfaceStatsHistSuspect_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistSuspect=_CucsEtherFcoeInterfaceStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,46),_CucsEtherFcoeInterfaceStatsHistSuspect_Type())
cucsEtherFcoeInterfaceStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistSuspect.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistThresholded_Type=CucsEtherFcoeInterfaceStatsHistThresholded
_CucsEtherFcoeInterfaceStatsHistThresholded_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistThresholded=_CucsEtherFcoeInterfaceStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,47),_CucsEtherFcoeInterfaceStatsHistThresholded_Type())
cucsEtherFcoeInterfaceStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistThresholded.setStatus(_A)
_CucsEtherFcoeInterfaceStatsHistTimeCollected_Type=DateAndTime
_CucsEtherFcoeInterfaceStatsHistTimeCollected_Object=MibTableColumn
cucsEtherFcoeInterfaceStatsHistTimeCollected=_CucsEtherFcoeInterfaceStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,24,1,48),_CucsEtherFcoeInterfaceStatsHistTimeCollected_Type())
cucsEtherFcoeInterfaceStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherFcoeInterfaceStatsHistTimeCollected.setStatus(_A)
_CucsEtherPIoEndPointTable_Object=MibTable
cucsEtherPIoEndPointTable=_CucsEtherPIoEndPointTable_Object((1,3,6,1,4,1,9,9,719,1,16,25))
if mibBuilder.loadTexts:cucsEtherPIoEndPointTable.setStatus(_A)
_CucsEtherPIoEndPointEntry_Object=MibTableRow
cucsEtherPIoEndPointEntry=_CucsEtherPIoEndPointEntry_Object((1,3,6,1,4,1,9,9,719,1,16,25,1))
cucsEtherPIoEndPointEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cucsEtherPIoEndPointEntry.setStatus(_A)
_CucsEtherPIoEndPointInstanceId_Type=CucsManagedObjectId
_CucsEtherPIoEndPointInstanceId_Object=MibTableColumn
cucsEtherPIoEndPointInstanceId=_CucsEtherPIoEndPointInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,25,1,1),_CucsEtherPIoEndPointInstanceId_Type())
cucsEtherPIoEndPointInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPIoEndPointInstanceId.setStatus(_A)
_CucsEtherPIoEndPointDn_Type=CucsManagedObjectDn
_CucsEtherPIoEndPointDn_Object=MibTableColumn
cucsEtherPIoEndPointDn=_CucsEtherPIoEndPointDn_Object((1,3,6,1,4,1,9,9,719,1,16,25,1,2),_CucsEtherPIoEndPointDn_Type())
cucsEtherPIoEndPointDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEndPointDn.setStatus(_A)
_CucsEtherPIoEndPointRn_Type=SnmpAdminString
_CucsEtherPIoEndPointRn_Object=MibTableColumn
cucsEtherPIoEndPointRn=_CucsEtherPIoEndPointRn_Object((1,3,6,1,4,1,9,9,719,1,16,25,1,3),_CucsEtherPIoEndPointRn_Type())
cucsEtherPIoEndPointRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEndPointRn.setStatus(_A)
_CucsEtherPIoEndPointEndPointDn_Type=SnmpAdminString
_CucsEtherPIoEndPointEndPointDn_Object=MibTableColumn
cucsEtherPIoEndPointEndPointDn=_CucsEtherPIoEndPointEndPointDn_Object((1,3,6,1,4,1,9,9,719,1,16,25,1,4),_CucsEtherPIoEndPointEndPointDn_Type())
cucsEtherPIoEndPointEndPointDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEndPointEndPointDn.setStatus(_A)
_CucsEtherPIoEndPointEpCloudType_Type=CucsEtherCloudType
_CucsEtherPIoEndPointEpCloudType_Object=MibTableColumn
cucsEtherPIoEndPointEpCloudType=_CucsEtherPIoEndPointEpCloudType_Object((1,3,6,1,4,1,9,9,719,1,16,25,1,5),_CucsEtherPIoEndPointEpCloudType_Type())
cucsEtherPIoEndPointEpCloudType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEndPointEpCloudType.setStatus(_A)
_CucsEtherPIoEndPointUsrLbl_Type=SnmpAdminString
_CucsEtherPIoEndPointUsrLbl_Object=MibTableColumn
cucsEtherPIoEndPointUsrLbl=_CucsEtherPIoEndPointUsrLbl_Object((1,3,6,1,4,1,9,9,719,1,16,25,1,6),_CucsEtherPIoEndPointUsrLbl_Type())
cucsEtherPIoEndPointUsrLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoEndPointUsrLbl.setStatus(_A)
_CucsEtherPIoFsmTable_Object=MibTable
cucsEtherPIoFsmTable=_CucsEtherPIoFsmTable_Object((1,3,6,1,4,1,9,9,719,1,16,26))
if mibBuilder.loadTexts:cucsEtherPIoFsmTable.setStatus(_A)
_CucsEtherPIoFsmEntry_Object=MibTableRow
cucsEtherPIoFsmEntry=_CucsEtherPIoFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,16,26,1))
cucsEtherPIoFsmEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cucsEtherPIoFsmEntry.setStatus(_A)
_CucsEtherPIoFsmInstanceId_Type=CucsManagedObjectId
_CucsEtherPIoFsmInstanceId_Object=MibTableColumn
cucsEtherPIoFsmInstanceId=_CucsEtherPIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,1),_CucsEtherPIoFsmInstanceId_Type())
cucsEtherPIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPIoFsmInstanceId.setStatus(_A)
_CucsEtherPIoFsmDn_Type=CucsManagedObjectDn
_CucsEtherPIoFsmDn_Object=MibTableColumn
cucsEtherPIoFsmDn=_CucsEtherPIoFsmDn_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,2),_CucsEtherPIoFsmDn_Type())
cucsEtherPIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmDn.setStatus(_A)
_CucsEtherPIoFsmRn_Type=SnmpAdminString
_CucsEtherPIoFsmRn_Object=MibTableColumn
cucsEtherPIoFsmRn=_CucsEtherPIoFsmRn_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,3),_CucsEtherPIoFsmRn_Type())
cucsEtherPIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRn.setStatus(_A)
_CucsEtherPIoFsmCompletionTime_Type=DateAndTime
_CucsEtherPIoFsmCompletionTime_Object=MibTableColumn
cucsEtherPIoFsmCompletionTime=_CucsEtherPIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,4),_CucsEtherPIoFsmCompletionTime_Type())
cucsEtherPIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmCompletionTime.setStatus(_A)
_CucsEtherPIoFsmCurrentFsm_Type=CucsEtherPIoFsmCurrentFsm
_CucsEtherPIoFsmCurrentFsm_Object=MibTableColumn
cucsEtherPIoFsmCurrentFsm=_CucsEtherPIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,5),_CucsEtherPIoFsmCurrentFsm_Type())
cucsEtherPIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmCurrentFsm.setStatus(_A)
_CucsEtherPIoFsmDescrData_Type=SnmpAdminString
_CucsEtherPIoFsmDescrData_Object=MibTableColumn
cucsEtherPIoFsmDescrData=_CucsEtherPIoFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,6),_CucsEtherPIoFsmDescrData_Type())
cucsEtherPIoFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmDescrData.setStatus(_A)
_CucsEtherPIoFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsEtherPIoFsmFsmStatus_Object=MibTableColumn
cucsEtherPIoFsmFsmStatus=_CucsEtherPIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,7),_CucsEtherPIoFsmFsmStatus_Type())
cucsEtherPIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmFsmStatus.setStatus(_A)
_CucsEtherPIoFsmProgress_Type=Gauge32
_CucsEtherPIoFsmProgress_Object=MibTableColumn
cucsEtherPIoFsmProgress=_CucsEtherPIoFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,8),_CucsEtherPIoFsmProgress_Type())
cucsEtherPIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmProgress.setStatus(_A)
_CucsEtherPIoFsmRmtErrCode_Type=Gauge32
_CucsEtherPIoFsmRmtErrCode_Object=MibTableColumn
cucsEtherPIoFsmRmtErrCode=_CucsEtherPIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,9),_CucsEtherPIoFsmRmtErrCode_Type())
cucsEtherPIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRmtErrCode.setStatus(_A)
_CucsEtherPIoFsmRmtErrDescr_Type=SnmpAdminString
_CucsEtherPIoFsmRmtErrDescr_Object=MibTableColumn
cucsEtherPIoFsmRmtErrDescr=_CucsEtherPIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,10),_CucsEtherPIoFsmRmtErrDescr_Type())
cucsEtherPIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRmtErrDescr.setStatus(_A)
_CucsEtherPIoFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsEtherPIoFsmRmtRslt_Object=MibTableColumn
cucsEtherPIoFsmRmtRslt=_CucsEtherPIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,16,26,1,11),_CucsEtherPIoFsmRmtRslt_Type())
cucsEtherPIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmRmtRslt.setStatus(_A)
_CucsEtherPIoFsmStageTable_Object=MibTable
cucsEtherPIoFsmStageTable=_CucsEtherPIoFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,16,27))
if mibBuilder.loadTexts:cucsEtherPIoFsmStageTable.setStatus(_A)
_CucsEtherPIoFsmStageEntry_Object=MibTableRow
cucsEtherPIoFsmStageEntry=_CucsEtherPIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,16,27,1))
cucsEtherPIoFsmStageEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cucsEtherPIoFsmStageEntry.setStatus(_A)
_CucsEtherPIoFsmStageInstanceId_Type=CucsManagedObjectId
_CucsEtherPIoFsmStageInstanceId_Object=MibTableColumn
cucsEtherPIoFsmStageInstanceId=_CucsEtherPIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,1),_CucsEtherPIoFsmStageInstanceId_Type())
cucsEtherPIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageInstanceId.setStatus(_A)
_CucsEtherPIoFsmStageDn_Type=CucsManagedObjectDn
_CucsEtherPIoFsmStageDn_Object=MibTableColumn
cucsEtherPIoFsmStageDn=_CucsEtherPIoFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,2),_CucsEtherPIoFsmStageDn_Type())
cucsEtherPIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageDn.setStatus(_A)
_CucsEtherPIoFsmStageRn_Type=SnmpAdminString
_CucsEtherPIoFsmStageRn_Object=MibTableColumn
cucsEtherPIoFsmStageRn=_CucsEtherPIoFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,3),_CucsEtherPIoFsmStageRn_Type())
cucsEtherPIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageRn.setStatus(_A)
_CucsEtherPIoFsmStageDescrData_Type=SnmpAdminString
_CucsEtherPIoFsmStageDescrData_Object=MibTableColumn
cucsEtherPIoFsmStageDescrData=_CucsEtherPIoFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,4),_CucsEtherPIoFsmStageDescrData_Type())
cucsEtherPIoFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageDescrData.setStatus(_A)
_CucsEtherPIoFsmStageLastUpdateTime_Type=DateAndTime
_CucsEtherPIoFsmStageLastUpdateTime_Object=MibTableColumn
cucsEtherPIoFsmStageLastUpdateTime=_CucsEtherPIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,5),_CucsEtherPIoFsmStageLastUpdateTime_Type())
cucsEtherPIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageLastUpdateTime.setStatus(_A)
_CucsEtherPIoFsmStageName_Type=CucsEtherPIoFsmStageName
_CucsEtherPIoFsmStageName_Object=MibTableColumn
cucsEtherPIoFsmStageName=_CucsEtherPIoFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,6),_CucsEtherPIoFsmStageName_Type())
cucsEtherPIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageName.setStatus(_A)
_CucsEtherPIoFsmStageOrder_Type=Gauge32
_CucsEtherPIoFsmStageOrder_Object=MibTableColumn
cucsEtherPIoFsmStageOrder=_CucsEtherPIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,7),_CucsEtherPIoFsmStageOrder_Type())
cucsEtherPIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageOrder.setStatus(_A)
_CucsEtherPIoFsmStageRetry_Type=Gauge32
_CucsEtherPIoFsmStageRetry_Object=MibTableColumn
cucsEtherPIoFsmStageRetry=_CucsEtherPIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,8),_CucsEtherPIoFsmStageRetry_Type())
cucsEtherPIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageRetry.setStatus(_A)
_CucsEtherPIoFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsEtherPIoFsmStageStageStatus_Object=MibTableColumn
cucsEtherPIoFsmStageStageStatus=_CucsEtherPIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,16,27,1,9),_CucsEtherPIoFsmStageStageStatus_Type())
cucsEtherPIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherPIoFsmStageStageStatus.setStatus(_A)
_CucsEtherServerIntFIoFsmTable_Object=MibTable
cucsEtherServerIntFIoFsmTable=_CucsEtherServerIntFIoFsmTable_Object((1,3,6,1,4,1,9,9,719,1,16,28))
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmTable.setStatus(_A)
_CucsEtherServerIntFIoFsmEntry_Object=MibTableRow
cucsEtherServerIntFIoFsmEntry=_CucsEtherServerIntFIoFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,16,28,1))
cucsEtherServerIntFIoFsmEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmEntry.setStatus(_A)
_CucsEtherServerIntFIoFsmInstanceId_Type=CucsManagedObjectId
_CucsEtherServerIntFIoFsmInstanceId_Object=MibTableColumn
cucsEtherServerIntFIoFsmInstanceId=_CucsEtherServerIntFIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,1),_CucsEtherServerIntFIoFsmInstanceId_Type())
cucsEtherServerIntFIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmInstanceId.setStatus(_A)
_CucsEtherServerIntFIoFsmDn_Type=CucsManagedObjectDn
_CucsEtherServerIntFIoFsmDn_Object=MibTableColumn
cucsEtherServerIntFIoFsmDn=_CucsEtherServerIntFIoFsmDn_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,2),_CucsEtherServerIntFIoFsmDn_Type())
cucsEtherServerIntFIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmDn.setStatus(_A)
_CucsEtherServerIntFIoFsmRn_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmRn_Object=MibTableColumn
cucsEtherServerIntFIoFsmRn=_CucsEtherServerIntFIoFsmRn_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,3),_CucsEtherServerIntFIoFsmRn_Type())
cucsEtherServerIntFIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRn.setStatus(_A)
_CucsEtherServerIntFIoFsmCompletionTime_Type=DateAndTime
_CucsEtherServerIntFIoFsmCompletionTime_Object=MibTableColumn
cucsEtherServerIntFIoFsmCompletionTime=_CucsEtherServerIntFIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,4),_CucsEtherServerIntFIoFsmCompletionTime_Type())
cucsEtherServerIntFIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmCompletionTime.setStatus(_A)
_CucsEtherServerIntFIoFsmCurrentFsm_Type=CucsEtherServerIntFIoFsmCurrentFsm
_CucsEtherServerIntFIoFsmCurrentFsm_Object=MibTableColumn
cucsEtherServerIntFIoFsmCurrentFsm=_CucsEtherServerIntFIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,5),_CucsEtherServerIntFIoFsmCurrentFsm_Type())
cucsEtherServerIntFIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmCurrentFsm.setStatus(_A)
_CucsEtherServerIntFIoFsmDescrData_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmDescrData_Object=MibTableColumn
cucsEtherServerIntFIoFsmDescrData=_CucsEtherServerIntFIoFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,6),_CucsEtherServerIntFIoFsmDescrData_Type())
cucsEtherServerIntFIoFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmDescrData.setStatus(_A)
_CucsEtherServerIntFIoFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsEtherServerIntFIoFsmFsmStatus_Object=MibTableColumn
cucsEtherServerIntFIoFsmFsmStatus=_CucsEtherServerIntFIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,7),_CucsEtherServerIntFIoFsmFsmStatus_Type())
cucsEtherServerIntFIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmFsmStatus.setStatus(_A)
_CucsEtherServerIntFIoFsmProgress_Type=Gauge32
_CucsEtherServerIntFIoFsmProgress_Object=MibTableColumn
cucsEtherServerIntFIoFsmProgress=_CucsEtherServerIntFIoFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,8),_CucsEtherServerIntFIoFsmProgress_Type())
cucsEtherServerIntFIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmProgress.setStatus(_A)
_CucsEtherServerIntFIoFsmRmtErrCode_Type=Gauge32
_CucsEtherServerIntFIoFsmRmtErrCode_Object=MibTableColumn
cucsEtherServerIntFIoFsmRmtErrCode=_CucsEtherServerIntFIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,9),_CucsEtherServerIntFIoFsmRmtErrCode_Type())
cucsEtherServerIntFIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRmtErrCode.setStatus(_A)
_CucsEtherServerIntFIoFsmRmtErrDescr_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmRmtErrDescr_Object=MibTableColumn
cucsEtherServerIntFIoFsmRmtErrDescr=_CucsEtherServerIntFIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,10),_CucsEtherServerIntFIoFsmRmtErrDescr_Type())
cucsEtherServerIntFIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRmtErrDescr.setStatus(_A)
_CucsEtherServerIntFIoFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsEtherServerIntFIoFsmRmtRslt_Object=MibTableColumn
cucsEtherServerIntFIoFsmRmtRslt=_CucsEtherServerIntFIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,16,28,1,11),_CucsEtherServerIntFIoFsmRmtRslt_Type())
cucsEtherServerIntFIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmRmtRslt.setStatus(_A)
_CucsEtherServerIntFIoFsmStageTable_Object=MibTable
cucsEtherServerIntFIoFsmStageTable=_CucsEtherServerIntFIoFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,16,29))
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageTable.setStatus(_A)
_CucsEtherServerIntFIoFsmStageEntry_Object=MibTableRow
cucsEtherServerIntFIoFsmStageEntry=_CucsEtherServerIntFIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,16,29,1))
cucsEtherServerIntFIoFsmStageEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageEntry.setStatus(_A)
_CucsEtherServerIntFIoFsmStageInstanceId_Type=CucsManagedObjectId
_CucsEtherServerIntFIoFsmStageInstanceId_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageInstanceId=_CucsEtherServerIntFIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,1),_CucsEtherServerIntFIoFsmStageInstanceId_Type())
cucsEtherServerIntFIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageInstanceId.setStatus(_A)
_CucsEtherServerIntFIoFsmStageDn_Type=CucsManagedObjectDn
_CucsEtherServerIntFIoFsmStageDn_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageDn=_CucsEtherServerIntFIoFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,2),_CucsEtherServerIntFIoFsmStageDn_Type())
cucsEtherServerIntFIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageDn.setStatus(_A)
_CucsEtherServerIntFIoFsmStageRn_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmStageRn_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageRn=_CucsEtherServerIntFIoFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,3),_CucsEtherServerIntFIoFsmStageRn_Type())
cucsEtherServerIntFIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageRn.setStatus(_A)
_CucsEtherServerIntFIoFsmStageDescrData_Type=SnmpAdminString
_CucsEtherServerIntFIoFsmStageDescrData_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageDescrData=_CucsEtherServerIntFIoFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,4),_CucsEtherServerIntFIoFsmStageDescrData_Type())
cucsEtherServerIntFIoFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageDescrData.setStatus(_A)
_CucsEtherServerIntFIoFsmStageLastUpdateTime_Type=DateAndTime
_CucsEtherServerIntFIoFsmStageLastUpdateTime_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageLastUpdateTime=_CucsEtherServerIntFIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,5),_CucsEtherServerIntFIoFsmStageLastUpdateTime_Type())
cucsEtherServerIntFIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageLastUpdateTime.setStatus(_A)
_CucsEtherServerIntFIoFsmStageName_Type=CucsEtherServerIntFIoFsmStageName
_CucsEtherServerIntFIoFsmStageName_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageName=_CucsEtherServerIntFIoFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,6),_CucsEtherServerIntFIoFsmStageName_Type())
cucsEtherServerIntFIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageName.setStatus(_A)
_CucsEtherServerIntFIoFsmStageOrder_Type=Gauge32
_CucsEtherServerIntFIoFsmStageOrder_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageOrder=_CucsEtherServerIntFIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,7),_CucsEtherServerIntFIoFsmStageOrder_Type())
cucsEtherServerIntFIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageOrder.setStatus(_A)
_CucsEtherServerIntFIoFsmStageRetry_Type=Gauge32
_CucsEtherServerIntFIoFsmStageRetry_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageRetry=_CucsEtherServerIntFIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,8),_CucsEtherServerIntFIoFsmStageRetry_Type())
cucsEtherServerIntFIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageRetry.setStatus(_A)
_CucsEtherServerIntFIoFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsEtherServerIntFIoFsmStageStageStatus_Object=MibTableColumn
cucsEtherServerIntFIoFsmStageStageStatus=_CucsEtherServerIntFIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,16,29,1,9),_CucsEtherServerIntFIoFsmStageStageStatus_Type())
cucsEtherServerIntFIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherServerIntFIoFsmStageStageStatus.setStatus(_A)
_CucsEtherNiErrStatsTable_Object=MibTable
cucsEtherNiErrStatsTable=_CucsEtherNiErrStatsTable_Object((1,3,6,1,4,1,9,9,719,1,16,30))
if mibBuilder.loadTexts:cucsEtherNiErrStatsTable.setStatus(_A)
_CucsEtherNiErrStatsEntry_Object=MibTableRow
cucsEtherNiErrStatsEntry=_CucsEtherNiErrStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,16,30,1))
cucsEtherNiErrStatsEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cucsEtherNiErrStatsEntry.setStatus(_A)
_CucsEtherNiErrStatsInstanceId_Type=CucsManagedObjectId
_CucsEtherNiErrStatsInstanceId_Object=MibTableColumn
cucsEtherNiErrStatsInstanceId=_CucsEtherNiErrStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,1),_CucsEtherNiErrStatsInstanceId_Type())
cucsEtherNiErrStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherNiErrStatsInstanceId.setStatus(_A)
_CucsEtherNiErrStatsDn_Type=CucsManagedObjectDn
_CucsEtherNiErrStatsDn_Object=MibTableColumn
cucsEtherNiErrStatsDn=_CucsEtherNiErrStatsDn_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,2),_CucsEtherNiErrStatsDn_Type())
cucsEtherNiErrStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsDn.setStatus(_A)
_CucsEtherNiErrStatsRn_Type=SnmpAdminString
_CucsEtherNiErrStatsRn_Object=MibTableColumn
cucsEtherNiErrStatsRn=_CucsEtherNiErrStatsRn_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,3),_CucsEtherNiErrStatsRn_Type())
cucsEtherNiErrStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsRn.setStatus(_A)
_CucsEtherNiErrStatsCrc_Type=Unsigned64
_CucsEtherNiErrStatsCrc_Object=MibTableColumn
cucsEtherNiErrStatsCrc=_CucsEtherNiErrStatsCrc_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,4),_CucsEtherNiErrStatsCrc_Type())
cucsEtherNiErrStatsCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsCrc.setStatus(_A)
_CucsEtherNiErrStatsCrcDelta_Type=Counter64
_CucsEtherNiErrStatsCrcDelta_Object=MibTableColumn
cucsEtherNiErrStatsCrcDelta=_CucsEtherNiErrStatsCrcDelta_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,5),_CucsEtherNiErrStatsCrcDelta_Type())
cucsEtherNiErrStatsCrcDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsCrcDelta.setStatus(_A)
_CucsEtherNiErrStatsCrcDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsCrcDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsCrcDeltaAvg=_CucsEtherNiErrStatsCrcDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,6),_CucsEtherNiErrStatsCrcDeltaAvg_Type())
cucsEtherNiErrStatsCrcDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsCrcDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsCrcDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsCrcDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsCrcDeltaMax=_CucsEtherNiErrStatsCrcDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,7),_CucsEtherNiErrStatsCrcDeltaMax_Type())
cucsEtherNiErrStatsCrcDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsCrcDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsCrcDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsCrcDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsCrcDeltaMin=_CucsEtherNiErrStatsCrcDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,8),_CucsEtherNiErrStatsCrcDeltaMin_Type())
cucsEtherNiErrStatsCrcDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsCrcDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsFrameTx_Type=Unsigned64
_CucsEtherNiErrStatsFrameTx_Object=MibTableColumn
cucsEtherNiErrStatsFrameTx=_CucsEtherNiErrStatsFrameTx_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,9),_CucsEtherNiErrStatsFrameTx_Type())
cucsEtherNiErrStatsFrameTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsFrameTx.setStatus(_A)
_CucsEtherNiErrStatsFrameTxDelta_Type=Counter64
_CucsEtherNiErrStatsFrameTxDelta_Object=MibTableColumn
cucsEtherNiErrStatsFrameTxDelta=_CucsEtherNiErrStatsFrameTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,10),_CucsEtherNiErrStatsFrameTxDelta_Type())
cucsEtherNiErrStatsFrameTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsFrameTxDelta.setStatus(_A)
_CucsEtherNiErrStatsFrameTxDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsFrameTxDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsFrameTxDeltaAvg=_CucsEtherNiErrStatsFrameTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,11),_CucsEtherNiErrStatsFrameTxDeltaAvg_Type())
cucsEtherNiErrStatsFrameTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsFrameTxDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsFrameTxDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsFrameTxDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsFrameTxDeltaMax=_CucsEtherNiErrStatsFrameTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,12),_CucsEtherNiErrStatsFrameTxDeltaMax_Type())
cucsEtherNiErrStatsFrameTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsFrameTxDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsFrameTxDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsFrameTxDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsFrameTxDeltaMin=_CucsEtherNiErrStatsFrameTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,13),_CucsEtherNiErrStatsFrameTxDeltaMin_Type())
cucsEtherNiErrStatsFrameTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsFrameTxDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsInRange_Type=Unsigned64
_CucsEtherNiErrStatsInRange_Object=MibTableColumn
cucsEtherNiErrStatsInRange=_CucsEtherNiErrStatsInRange_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,14),_CucsEtherNiErrStatsInRange_Type())
cucsEtherNiErrStatsInRange.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsInRange.setStatus(_A)
_CucsEtherNiErrStatsInRangeDelta_Type=Counter64
_CucsEtherNiErrStatsInRangeDelta_Object=MibTableColumn
cucsEtherNiErrStatsInRangeDelta=_CucsEtherNiErrStatsInRangeDelta_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,15),_CucsEtherNiErrStatsInRangeDelta_Type())
cucsEtherNiErrStatsInRangeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsInRangeDelta.setStatus(_A)
_CucsEtherNiErrStatsInRangeDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsInRangeDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsInRangeDeltaAvg=_CucsEtherNiErrStatsInRangeDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,16),_CucsEtherNiErrStatsInRangeDeltaAvg_Type())
cucsEtherNiErrStatsInRangeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsInRangeDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsInRangeDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsInRangeDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsInRangeDeltaMax=_CucsEtherNiErrStatsInRangeDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,17),_CucsEtherNiErrStatsInRangeDeltaMax_Type())
cucsEtherNiErrStatsInRangeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsInRangeDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsInRangeDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsInRangeDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsInRangeDeltaMin=_CucsEtherNiErrStatsInRangeDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,18),_CucsEtherNiErrStatsInRangeDeltaMin_Type())
cucsEtherNiErrStatsInRangeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsInRangeDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsIntervals_Type=Gauge32
_CucsEtherNiErrStatsIntervals_Object=MibTableColumn
cucsEtherNiErrStatsIntervals=_CucsEtherNiErrStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,19),_CucsEtherNiErrStatsIntervals_Type())
cucsEtherNiErrStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsIntervals.setStatus(_A)
_CucsEtherNiErrStatsSuspect_Type=TruthValue
_CucsEtherNiErrStatsSuspect_Object=MibTableColumn
cucsEtherNiErrStatsSuspect=_CucsEtherNiErrStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,20),_CucsEtherNiErrStatsSuspect_Type())
cucsEtherNiErrStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsSuspect.setStatus(_A)
_CucsEtherNiErrStatsThresholded_Type=CucsEtherNiErrStatsThresholded
_CucsEtherNiErrStatsThresholded_Object=MibTableColumn
cucsEtherNiErrStatsThresholded=_CucsEtherNiErrStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,21),_CucsEtherNiErrStatsThresholded_Type())
cucsEtherNiErrStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsThresholded.setStatus(_A)
_CucsEtherNiErrStatsTimeCollected_Type=DateAndTime
_CucsEtherNiErrStatsTimeCollected_Object=MibTableColumn
cucsEtherNiErrStatsTimeCollected=_CucsEtherNiErrStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,22),_CucsEtherNiErrStatsTimeCollected_Type())
cucsEtherNiErrStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTimeCollected.setStatus(_A)
_CucsEtherNiErrStatsTooLong_Type=Unsigned64
_CucsEtherNiErrStatsTooLong_Object=MibTableColumn
cucsEtherNiErrStatsTooLong=_CucsEtherNiErrStatsTooLong_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,23),_CucsEtherNiErrStatsTooLong_Type())
cucsEtherNiErrStatsTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooLong.setStatus(_A)
_CucsEtherNiErrStatsTooLongDelta_Type=Counter64
_CucsEtherNiErrStatsTooLongDelta_Object=MibTableColumn
cucsEtherNiErrStatsTooLongDelta=_CucsEtherNiErrStatsTooLongDelta_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,24),_CucsEtherNiErrStatsTooLongDelta_Type())
cucsEtherNiErrStatsTooLongDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooLongDelta.setStatus(_A)
_CucsEtherNiErrStatsTooLongDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsTooLongDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsTooLongDeltaAvg=_CucsEtherNiErrStatsTooLongDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,25),_CucsEtherNiErrStatsTooLongDeltaAvg_Type())
cucsEtherNiErrStatsTooLongDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooLongDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsTooLongDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsTooLongDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsTooLongDeltaMax=_CucsEtherNiErrStatsTooLongDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,26),_CucsEtherNiErrStatsTooLongDeltaMax_Type())
cucsEtherNiErrStatsTooLongDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooLongDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsTooLongDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsTooLongDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsTooLongDeltaMin=_CucsEtherNiErrStatsTooLongDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,27),_CucsEtherNiErrStatsTooLongDeltaMin_Type())
cucsEtherNiErrStatsTooLongDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooLongDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsTooShort_Type=Unsigned64
_CucsEtherNiErrStatsTooShort_Object=MibTableColumn
cucsEtherNiErrStatsTooShort=_CucsEtherNiErrStatsTooShort_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,28),_CucsEtherNiErrStatsTooShort_Type())
cucsEtherNiErrStatsTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooShort.setStatus(_A)
_CucsEtherNiErrStatsTooShortDelta_Type=Counter64
_CucsEtherNiErrStatsTooShortDelta_Object=MibTableColumn
cucsEtherNiErrStatsTooShortDelta=_CucsEtherNiErrStatsTooShortDelta_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,29),_CucsEtherNiErrStatsTooShortDelta_Type())
cucsEtherNiErrStatsTooShortDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooShortDelta.setStatus(_A)
_CucsEtherNiErrStatsTooShortDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsTooShortDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsTooShortDeltaAvg=_CucsEtherNiErrStatsTooShortDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,30),_CucsEtherNiErrStatsTooShortDeltaAvg_Type())
cucsEtherNiErrStatsTooShortDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooShortDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsTooShortDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsTooShortDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsTooShortDeltaMax=_CucsEtherNiErrStatsTooShortDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,31),_CucsEtherNiErrStatsTooShortDeltaMax_Type())
cucsEtherNiErrStatsTooShortDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooShortDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsTooShortDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsTooShortDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsTooShortDeltaMin=_CucsEtherNiErrStatsTooShortDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,32),_CucsEtherNiErrStatsTooShortDeltaMin_Type())
cucsEtherNiErrStatsTooShortDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsTooShortDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsUpdate_Type=Gauge32
_CucsEtherNiErrStatsUpdate_Object=MibTableColumn
cucsEtherNiErrStatsUpdate=_CucsEtherNiErrStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,16,30,1,33),_CucsEtherNiErrStatsUpdate_Type())
cucsEtherNiErrStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsUpdate.setStatus(_A)
_CucsEtherNiErrStatsHistTable_Object=MibTable
cucsEtherNiErrStatsHistTable=_CucsEtherNiErrStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,16,31))
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTable.setStatus(_A)
_CucsEtherNiErrStatsHistEntry_Object=MibTableRow
cucsEtherNiErrStatsHistEntry=_CucsEtherNiErrStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,16,31,1))
cucsEtherNiErrStatsHistEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistEntry.setStatus(_A)
_CucsEtherNiErrStatsHistInstanceId_Type=CucsManagedObjectId
_CucsEtherNiErrStatsHistInstanceId_Object=MibTableColumn
cucsEtherNiErrStatsHistInstanceId=_CucsEtherNiErrStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,1),_CucsEtherNiErrStatsHistInstanceId_Type())
cucsEtherNiErrStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistInstanceId.setStatus(_A)
_CucsEtherNiErrStatsHistDn_Type=CucsManagedObjectDn
_CucsEtherNiErrStatsHistDn_Object=MibTableColumn
cucsEtherNiErrStatsHistDn=_CucsEtherNiErrStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,2),_CucsEtherNiErrStatsHistDn_Type())
cucsEtherNiErrStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistDn.setStatus(_A)
_CucsEtherNiErrStatsHistRn_Type=SnmpAdminString
_CucsEtherNiErrStatsHistRn_Object=MibTableColumn
cucsEtherNiErrStatsHistRn=_CucsEtherNiErrStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,3),_CucsEtherNiErrStatsHistRn_Type())
cucsEtherNiErrStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistRn.setStatus(_A)
_CucsEtherNiErrStatsHistCrc_Type=Unsigned64
_CucsEtherNiErrStatsHistCrc_Object=MibTableColumn
cucsEtherNiErrStatsHistCrc=_CucsEtherNiErrStatsHistCrc_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,4),_CucsEtherNiErrStatsHistCrc_Type())
cucsEtherNiErrStatsHistCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistCrc.setStatus(_A)
_CucsEtherNiErrStatsHistCrcDelta_Type=Unsigned64
_CucsEtherNiErrStatsHistCrcDelta_Object=MibTableColumn
cucsEtherNiErrStatsHistCrcDelta=_CucsEtherNiErrStatsHistCrcDelta_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,5),_CucsEtherNiErrStatsHistCrcDelta_Type())
cucsEtherNiErrStatsHistCrcDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistCrcDelta.setStatus(_A)
_CucsEtherNiErrStatsHistCrcDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsHistCrcDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsHistCrcDeltaAvg=_CucsEtherNiErrStatsHistCrcDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,6),_CucsEtherNiErrStatsHistCrcDeltaAvg_Type())
cucsEtherNiErrStatsHistCrcDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistCrcDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsHistCrcDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsHistCrcDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsHistCrcDeltaMax=_CucsEtherNiErrStatsHistCrcDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,7),_CucsEtherNiErrStatsHistCrcDeltaMax_Type())
cucsEtherNiErrStatsHistCrcDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistCrcDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsHistCrcDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsHistCrcDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsHistCrcDeltaMin=_CucsEtherNiErrStatsHistCrcDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,8),_CucsEtherNiErrStatsHistCrcDeltaMin_Type())
cucsEtherNiErrStatsHistCrcDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistCrcDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsHistFrameTx_Type=Unsigned64
_CucsEtherNiErrStatsHistFrameTx_Object=MibTableColumn
cucsEtherNiErrStatsHistFrameTx=_CucsEtherNiErrStatsHistFrameTx_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,9),_CucsEtherNiErrStatsHistFrameTx_Type())
cucsEtherNiErrStatsHistFrameTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistFrameTx.setStatus(_A)
_CucsEtherNiErrStatsHistFrameTxDelta_Type=Unsigned64
_CucsEtherNiErrStatsHistFrameTxDelta_Object=MibTableColumn
cucsEtherNiErrStatsHistFrameTxDelta=_CucsEtherNiErrStatsHistFrameTxDelta_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,10),_CucsEtherNiErrStatsHistFrameTxDelta_Type())
cucsEtherNiErrStatsHistFrameTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistFrameTxDelta.setStatus(_A)
_CucsEtherNiErrStatsHistFrameTxDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsHistFrameTxDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsHistFrameTxDeltaAvg=_CucsEtherNiErrStatsHistFrameTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,11),_CucsEtherNiErrStatsHistFrameTxDeltaAvg_Type())
cucsEtherNiErrStatsHistFrameTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistFrameTxDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsHistFrameTxDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsHistFrameTxDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsHistFrameTxDeltaMax=_CucsEtherNiErrStatsHistFrameTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,12),_CucsEtherNiErrStatsHistFrameTxDeltaMax_Type())
cucsEtherNiErrStatsHistFrameTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistFrameTxDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsHistFrameTxDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsHistFrameTxDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsHistFrameTxDeltaMin=_CucsEtherNiErrStatsHistFrameTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,13),_CucsEtherNiErrStatsHistFrameTxDeltaMin_Type())
cucsEtherNiErrStatsHistFrameTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistFrameTxDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsHistId_Type=Unsigned64
_CucsEtherNiErrStatsHistId_Object=MibTableColumn
cucsEtherNiErrStatsHistId=_CucsEtherNiErrStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,14),_CucsEtherNiErrStatsHistId_Type())
cucsEtherNiErrStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistId.setStatus(_A)
_CucsEtherNiErrStatsHistInRange_Type=Unsigned64
_CucsEtherNiErrStatsHistInRange_Object=MibTableColumn
cucsEtherNiErrStatsHistInRange=_CucsEtherNiErrStatsHistInRange_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,15),_CucsEtherNiErrStatsHistInRange_Type())
cucsEtherNiErrStatsHistInRange.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistInRange.setStatus(_A)
_CucsEtherNiErrStatsHistInRangeDelta_Type=Unsigned64
_CucsEtherNiErrStatsHistInRangeDelta_Object=MibTableColumn
cucsEtherNiErrStatsHistInRangeDelta=_CucsEtherNiErrStatsHistInRangeDelta_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,16),_CucsEtherNiErrStatsHistInRangeDelta_Type())
cucsEtherNiErrStatsHistInRangeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistInRangeDelta.setStatus(_A)
_CucsEtherNiErrStatsHistInRangeDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsHistInRangeDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsHistInRangeDeltaAvg=_CucsEtherNiErrStatsHistInRangeDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,17),_CucsEtherNiErrStatsHistInRangeDeltaAvg_Type())
cucsEtherNiErrStatsHistInRangeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistInRangeDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsHistInRangeDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsHistInRangeDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsHistInRangeDeltaMax=_CucsEtherNiErrStatsHistInRangeDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,18),_CucsEtherNiErrStatsHistInRangeDeltaMax_Type())
cucsEtherNiErrStatsHistInRangeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistInRangeDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsHistInRangeDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsHistInRangeDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsHistInRangeDeltaMin=_CucsEtherNiErrStatsHistInRangeDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,19),_CucsEtherNiErrStatsHistInRangeDeltaMin_Type())
cucsEtherNiErrStatsHistInRangeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistInRangeDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsHistMostRecent_Type=TruthValue
_CucsEtherNiErrStatsHistMostRecent_Object=MibTableColumn
cucsEtherNiErrStatsHistMostRecent=_CucsEtherNiErrStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,20),_CucsEtherNiErrStatsHistMostRecent_Type())
cucsEtherNiErrStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistMostRecent.setStatus(_A)
_CucsEtherNiErrStatsHistSuspect_Type=TruthValue
_CucsEtherNiErrStatsHistSuspect_Object=MibTableColumn
cucsEtherNiErrStatsHistSuspect=_CucsEtherNiErrStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,21),_CucsEtherNiErrStatsHistSuspect_Type())
cucsEtherNiErrStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistSuspect.setStatus(_A)
_CucsEtherNiErrStatsHistThresholded_Type=CucsEtherNiErrStatsHistThresholded
_CucsEtherNiErrStatsHistThresholded_Object=MibTableColumn
cucsEtherNiErrStatsHistThresholded=_CucsEtherNiErrStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,22),_CucsEtherNiErrStatsHistThresholded_Type())
cucsEtherNiErrStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistThresholded.setStatus(_A)
_CucsEtherNiErrStatsHistTimeCollected_Type=DateAndTime
_CucsEtherNiErrStatsHistTimeCollected_Object=MibTableColumn
cucsEtherNiErrStatsHistTimeCollected=_CucsEtherNiErrStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,23),_CucsEtherNiErrStatsHistTimeCollected_Type())
cucsEtherNiErrStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTimeCollected.setStatus(_A)
_CucsEtherNiErrStatsHistTooLong_Type=Unsigned64
_CucsEtherNiErrStatsHistTooLong_Object=MibTableColumn
cucsEtherNiErrStatsHistTooLong=_CucsEtherNiErrStatsHistTooLong_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,24),_CucsEtherNiErrStatsHistTooLong_Type())
cucsEtherNiErrStatsHistTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooLong.setStatus(_A)
_CucsEtherNiErrStatsHistTooLongDelta_Type=Unsigned64
_CucsEtherNiErrStatsHistTooLongDelta_Object=MibTableColumn
cucsEtherNiErrStatsHistTooLongDelta=_CucsEtherNiErrStatsHistTooLongDelta_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,25),_CucsEtherNiErrStatsHistTooLongDelta_Type())
cucsEtherNiErrStatsHistTooLongDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooLongDelta.setStatus(_A)
_CucsEtherNiErrStatsHistTooLongDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsHistTooLongDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsHistTooLongDeltaAvg=_CucsEtherNiErrStatsHistTooLongDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,26),_CucsEtherNiErrStatsHistTooLongDeltaAvg_Type())
cucsEtherNiErrStatsHistTooLongDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooLongDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsHistTooLongDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsHistTooLongDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsHistTooLongDeltaMax=_CucsEtherNiErrStatsHistTooLongDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,27),_CucsEtherNiErrStatsHistTooLongDeltaMax_Type())
cucsEtherNiErrStatsHistTooLongDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooLongDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsHistTooLongDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsHistTooLongDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsHistTooLongDeltaMin=_CucsEtherNiErrStatsHistTooLongDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,28),_CucsEtherNiErrStatsHistTooLongDeltaMin_Type())
cucsEtherNiErrStatsHistTooLongDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooLongDeltaMin.setStatus(_A)
_CucsEtherNiErrStatsHistTooShort_Type=Unsigned64
_CucsEtherNiErrStatsHistTooShort_Object=MibTableColumn
cucsEtherNiErrStatsHistTooShort=_CucsEtherNiErrStatsHistTooShort_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,29),_CucsEtherNiErrStatsHistTooShort_Type())
cucsEtherNiErrStatsHistTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooShort.setStatus(_A)
_CucsEtherNiErrStatsHistTooShortDelta_Type=Unsigned64
_CucsEtherNiErrStatsHistTooShortDelta_Object=MibTableColumn
cucsEtherNiErrStatsHistTooShortDelta=_CucsEtherNiErrStatsHistTooShortDelta_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,30),_CucsEtherNiErrStatsHistTooShortDelta_Type())
cucsEtherNiErrStatsHistTooShortDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooShortDelta.setStatus(_A)
_CucsEtherNiErrStatsHistTooShortDeltaAvg_Type=Unsigned64
_CucsEtherNiErrStatsHistTooShortDeltaAvg_Object=MibTableColumn
cucsEtherNiErrStatsHistTooShortDeltaAvg=_CucsEtherNiErrStatsHistTooShortDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,31),_CucsEtherNiErrStatsHistTooShortDeltaAvg_Type())
cucsEtherNiErrStatsHistTooShortDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooShortDeltaAvg.setStatus(_A)
_CucsEtherNiErrStatsHistTooShortDeltaMax_Type=Unsigned64
_CucsEtherNiErrStatsHistTooShortDeltaMax_Object=MibTableColumn
cucsEtherNiErrStatsHistTooShortDeltaMax=_CucsEtherNiErrStatsHistTooShortDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,32),_CucsEtherNiErrStatsHistTooShortDeltaMax_Type())
cucsEtherNiErrStatsHistTooShortDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooShortDeltaMax.setStatus(_A)
_CucsEtherNiErrStatsHistTooShortDeltaMin_Type=Unsigned64
_CucsEtherNiErrStatsHistTooShortDeltaMin_Object=MibTableColumn
cucsEtherNiErrStatsHistTooShortDeltaMin=_CucsEtherNiErrStatsHistTooShortDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,16,31,1,33),_CucsEtherNiErrStatsHistTooShortDeltaMin_Type())
cucsEtherNiErrStatsHistTooShortDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEtherNiErrStatsHistTooShortDeltaMin.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsEtherObjects':cucsEtherObjects,'cucsEtherErrStatsTable':cucsEtherErrStatsTable,'cucsEtherErrStatsEntry':cucsEtherErrStatsEntry,_E:cucsEtherErrStatsInstanceId,'cucsEtherErrStatsDn':cucsEtherErrStatsDn,'cucsEtherErrStatsRn':cucsEtherErrStatsRn,'cucsEtherErrStatsAlign':cucsEtherErrStatsAlign,'cucsEtherErrStatsAlignDelta':cucsEtherErrStatsAlignDelta,'cucsEtherErrStatsAlignDeltaAvg':cucsEtherErrStatsAlignDeltaAvg,'cucsEtherErrStatsAlignDeltaMax':cucsEtherErrStatsAlignDeltaMax,'cucsEtherErrStatsAlignDeltaMin':cucsEtherErrStatsAlignDeltaMin,'cucsEtherErrStatsDeferredTx':cucsEtherErrStatsDeferredTx,'cucsEtherErrStatsDeferredTxDelta':cucsEtherErrStatsDeferredTxDelta,'cucsEtherErrStatsDeferredTxDeltaAvg':cucsEtherErrStatsDeferredTxDeltaAvg,'cucsEtherErrStatsDeferredTxDeltaMax':cucsEtherErrStatsDeferredTxDeltaMax,'cucsEtherErrStatsDeferredTxDeltaMin':cucsEtherErrStatsDeferredTxDeltaMin,'cucsEtherErrStatsFcs':cucsEtherErrStatsFcs,'cucsEtherErrStatsFcsDelta':cucsEtherErrStatsFcsDelta,'cucsEtherErrStatsFcsDeltaAvg':cucsEtherErrStatsFcsDeltaAvg,'cucsEtherErrStatsFcsDeltaMax':cucsEtherErrStatsFcsDeltaMax,'cucsEtherErrStatsFcsDeltaMin':cucsEtherErrStatsFcsDeltaMin,'cucsEtherErrStatsIntMacRx':cucsEtherErrStatsIntMacRx,'cucsEtherErrStatsIntMacRxDelta':cucsEtherErrStatsIntMacRxDelta,'cucsEtherErrStatsIntMacRxDeltaAvg':cucsEtherErrStatsIntMacRxDeltaAvg,'cucsEtherErrStatsIntMacRxDeltaMax':cucsEtherErrStatsIntMacRxDeltaMax,'cucsEtherErrStatsIntMacRxDeltaMin':cucsEtherErrStatsIntMacRxDeltaMin,'cucsEtherErrStatsIntMacTx':cucsEtherErrStatsIntMacTx,'cucsEtherErrStatsIntMacTxDelta':cucsEtherErrStatsIntMacTxDelta,'cucsEtherErrStatsIntMacTxDeltaAvg':cucsEtherErrStatsIntMacTxDeltaAvg,'cucsEtherErrStatsIntMacTxDeltaMax':cucsEtherErrStatsIntMacTxDeltaMax,'cucsEtherErrStatsIntMacTxDeltaMin':cucsEtherErrStatsIntMacTxDeltaMin,'cucsEtherErrStatsIntervals':cucsEtherErrStatsIntervals,'cucsEtherErrStatsOutDiscard':cucsEtherErrStatsOutDiscard,'cucsEtherErrStatsOutDiscardDelta':cucsEtherErrStatsOutDiscardDelta,'cucsEtherErrStatsOutDiscardDeltaAvg':cucsEtherErrStatsOutDiscardDeltaAvg,'cucsEtherErrStatsOutDiscardDeltaMax':cucsEtherErrStatsOutDiscardDeltaMax,'cucsEtherErrStatsOutDiscardDeltaMin':cucsEtherErrStatsOutDiscardDeltaMin,'cucsEtherErrStatsRcv':cucsEtherErrStatsRcv,'cucsEtherErrStatsRcvDelta':cucsEtherErrStatsRcvDelta,'cucsEtherErrStatsRcvDeltaAvg':cucsEtherErrStatsRcvDeltaAvg,'cucsEtherErrStatsRcvDeltaMax':cucsEtherErrStatsRcvDeltaMax,'cucsEtherErrStatsRcvDeltaMin':cucsEtherErrStatsRcvDeltaMin,'cucsEtherErrStatsSuspect':cucsEtherErrStatsSuspect,'cucsEtherErrStatsThresholded':cucsEtherErrStatsThresholded,'cucsEtherErrStatsTimeCollected':cucsEtherErrStatsTimeCollected,'cucsEtherErrStatsUnderSize':cucsEtherErrStatsUnderSize,'cucsEtherErrStatsUnderSizeDelta':cucsEtherErrStatsUnderSizeDelta,'cucsEtherErrStatsUnderSizeDeltaAvg':cucsEtherErrStatsUnderSizeDeltaAvg,'cucsEtherErrStatsUnderSizeDeltaMax':cucsEtherErrStatsUnderSizeDeltaMax,'cucsEtherErrStatsUnderSizeDeltaMin':cucsEtherErrStatsUnderSizeDeltaMin,'cucsEtherErrStatsUpdate':cucsEtherErrStatsUpdate,'cucsEtherErrStatsXmit':cucsEtherErrStatsXmit,'cucsEtherErrStatsXmitDelta':cucsEtherErrStatsXmitDelta,'cucsEtherErrStatsXmitDeltaAvg':cucsEtherErrStatsXmitDeltaAvg,'cucsEtherErrStatsXmitDeltaMax':cucsEtherErrStatsXmitDeltaMax,'cucsEtherErrStatsXmitDeltaMin':cucsEtherErrStatsXmitDeltaMin,'cucsEtherErrStatsHistTable':cucsEtherErrStatsHistTable,'cucsEtherErrStatsHistEntry':cucsEtherErrStatsHistEntry,_F:cucsEtherErrStatsHistInstanceId,'cucsEtherErrStatsHistDn':cucsEtherErrStatsHistDn,'cucsEtherErrStatsHistRn':cucsEtherErrStatsHistRn,'cucsEtherErrStatsHistAlign':cucsEtherErrStatsHistAlign,'cucsEtherErrStatsHistAlignDelta':cucsEtherErrStatsHistAlignDelta,'cucsEtherErrStatsHistAlignDeltaAvg':cucsEtherErrStatsHistAlignDeltaAvg,'cucsEtherErrStatsHistAlignDeltaMax':cucsEtherErrStatsHistAlignDeltaMax,'cucsEtherErrStatsHistAlignDeltaMin':cucsEtherErrStatsHistAlignDeltaMin,'cucsEtherErrStatsHistDeferredTx':cucsEtherErrStatsHistDeferredTx,'cucsEtherErrStatsHistDeferredTxDelta':cucsEtherErrStatsHistDeferredTxDelta,'cucsEtherErrStatsHistDeferredTxDeltaAvg':cucsEtherErrStatsHistDeferredTxDeltaAvg,'cucsEtherErrStatsHistDeferredTxDeltaMax':cucsEtherErrStatsHistDeferredTxDeltaMax,'cucsEtherErrStatsHistDeferredTxDeltaMin':cucsEtherErrStatsHistDeferredTxDeltaMin,'cucsEtherErrStatsHistFcs':cucsEtherErrStatsHistFcs,'cucsEtherErrStatsHistFcsDelta':cucsEtherErrStatsHistFcsDelta,'cucsEtherErrStatsHistFcsDeltaAvg':cucsEtherErrStatsHistFcsDeltaAvg,'cucsEtherErrStatsHistFcsDeltaMax':cucsEtherErrStatsHistFcsDeltaMax,'cucsEtherErrStatsHistFcsDeltaMin':cucsEtherErrStatsHistFcsDeltaMin,'cucsEtherErrStatsHistId':cucsEtherErrStatsHistId,'cucsEtherErrStatsHistIntMacRx':cucsEtherErrStatsHistIntMacRx,'cucsEtherErrStatsHistIntMacRxDelta':cucsEtherErrStatsHistIntMacRxDelta,'cucsEtherErrStatsHistIntMacRxDeltaAvg':cucsEtherErrStatsHistIntMacRxDeltaAvg,'cucsEtherErrStatsHistIntMacRxDeltaMax':cucsEtherErrStatsHistIntMacRxDeltaMax,'cucsEtherErrStatsHistIntMacRxDeltaMin':cucsEtherErrStatsHistIntMacRxDeltaMin,'cucsEtherErrStatsHistIntMacTx':cucsEtherErrStatsHistIntMacTx,'cucsEtherErrStatsHistIntMacTxDelta':cucsEtherErrStatsHistIntMacTxDelta,'cucsEtherErrStatsHistIntMacTxDeltaAvg':cucsEtherErrStatsHistIntMacTxDeltaAvg,'cucsEtherErrStatsHistIntMacTxDeltaMax':cucsEtherErrStatsHistIntMacTxDeltaMax,'cucsEtherErrStatsHistIntMacTxDeltaMin':cucsEtherErrStatsHistIntMacTxDeltaMin,'cucsEtherErrStatsHistMostRecent':cucsEtherErrStatsHistMostRecent,'cucsEtherErrStatsHistOutDiscard':cucsEtherErrStatsHistOutDiscard,'cucsEtherErrStatsHistOutDiscardDelta':cucsEtherErrStatsHistOutDiscardDelta,'cucsEtherErrStatsHistOutDiscardDeltaAvg':cucsEtherErrStatsHistOutDiscardDeltaAvg,'cucsEtherErrStatsHistOutDiscardDeltaMax':cucsEtherErrStatsHistOutDiscardDeltaMax,'cucsEtherErrStatsHistOutDiscardDeltaMin':cucsEtherErrStatsHistOutDiscardDeltaMin,'cucsEtherErrStatsHistRcv':cucsEtherErrStatsHistRcv,'cucsEtherErrStatsHistRcvDelta':cucsEtherErrStatsHistRcvDelta,'cucsEtherErrStatsHistRcvDeltaAvg':cucsEtherErrStatsHistRcvDeltaAvg,'cucsEtherErrStatsHistRcvDeltaMax':cucsEtherErrStatsHistRcvDeltaMax,'cucsEtherErrStatsHistRcvDeltaMin':cucsEtherErrStatsHistRcvDeltaMin,'cucsEtherErrStatsHistSuspect':cucsEtherErrStatsHistSuspect,'cucsEtherErrStatsHistThresholded':cucsEtherErrStatsHistThresholded,'cucsEtherErrStatsHistTimeCollected':cucsEtherErrStatsHistTimeCollected,'cucsEtherErrStatsHistUnderSize':cucsEtherErrStatsHistUnderSize,'cucsEtherErrStatsHistUnderSizeDelta':cucsEtherErrStatsHistUnderSizeDelta,'cucsEtherErrStatsHistUnderSizeDeltaAvg':cucsEtherErrStatsHistUnderSizeDeltaAvg,'cucsEtherErrStatsHistUnderSizeDeltaMax':cucsEtherErrStatsHistUnderSizeDeltaMax,'cucsEtherErrStatsHistUnderSizeDeltaMin':cucsEtherErrStatsHistUnderSizeDeltaMin,'cucsEtherErrStatsHistXmit':cucsEtherErrStatsHistXmit,'cucsEtherErrStatsHistXmitDelta':cucsEtherErrStatsHistXmitDelta,'cucsEtherErrStatsHistXmitDeltaAvg':cucsEtherErrStatsHistXmitDeltaAvg,'cucsEtherErrStatsHistXmitDeltaMax':cucsEtherErrStatsHistXmitDeltaMax,'cucsEtherErrStatsHistXmitDeltaMin':cucsEtherErrStatsHistXmitDeltaMin,'cucsEtherLossStatsTable':cucsEtherLossStatsTable,'cucsEtherLossStatsEntry':cucsEtherLossStatsEntry,_G:cucsEtherLossStatsInstanceId,'cucsEtherLossStatsDn':cucsEtherLossStatsDn,'cucsEtherLossStatsRn':cucsEtherLossStatsRn,'cucsEtherLossStatsSQETest':cucsEtherLossStatsSQETest,'cucsEtherLossStatsSQETestDelta':cucsEtherLossStatsSQETestDelta,'cucsEtherLossStatsSQETestDeltaAvg':cucsEtherLossStatsSQETestDeltaAvg,'cucsEtherLossStatsSQETestDeltaMax':cucsEtherLossStatsSQETestDeltaMax,'cucsEtherLossStatsSQETestDeltaMin':cucsEtherLossStatsSQETestDeltaMin,'cucsEtherLossStatsCarrierSense':cucsEtherLossStatsCarrierSense,'cucsEtherLossStatsCarrierSenseDelta':cucsEtherLossStatsCarrierSenseDelta,'cucsEtherLossStatsCarrierSenseDeltaAvg':cucsEtherLossStatsCarrierSenseDeltaAvg,'cucsEtherLossStatsCarrierSenseDeltaMax':cucsEtherLossStatsCarrierSenseDeltaMax,'cucsEtherLossStatsCarrierSenseDeltaMin':cucsEtherLossStatsCarrierSenseDeltaMin,'cucsEtherLossStatsExcessCollision':cucsEtherLossStatsExcessCollision,'cucsEtherLossStatsExcessCollisionDelta':cucsEtherLossStatsExcessCollisionDelta,'cucsEtherLossStatsExcessCollisionDeltaAvg':cucsEtherLossStatsExcessCollisionDeltaAvg,'cucsEtherLossStatsExcessCollisionDeltaMax':cucsEtherLossStatsExcessCollisionDeltaMax,'cucsEtherLossStatsExcessCollisionDeltaMin':cucsEtherLossStatsExcessCollisionDeltaMin,'cucsEtherLossStatsGiants':cucsEtherLossStatsGiants,'cucsEtherLossStatsGiantsDelta':cucsEtherLossStatsGiantsDelta,'cucsEtherLossStatsGiantsDeltaAvg':cucsEtherLossStatsGiantsDeltaAvg,'cucsEtherLossStatsGiantsDeltaMax':cucsEtherLossStatsGiantsDeltaMax,'cucsEtherLossStatsGiantsDeltaMin':cucsEtherLossStatsGiantsDeltaMin,'cucsEtherLossStatsIntervals':cucsEtherLossStatsIntervals,'cucsEtherLossStatsLateCollision':cucsEtherLossStatsLateCollision,'cucsEtherLossStatsLateCollisionDelta':cucsEtherLossStatsLateCollisionDelta,'cucsEtherLossStatsLateCollisionDeltaAvg':cucsEtherLossStatsLateCollisionDeltaAvg,'cucsEtherLossStatsLateCollisionDeltaMax':cucsEtherLossStatsLateCollisionDeltaMax,'cucsEtherLossStatsLateCollisionDeltaMin':cucsEtherLossStatsLateCollisionDeltaMin,'cucsEtherLossStatsMultiCollision':cucsEtherLossStatsMultiCollision,'cucsEtherLossStatsMultiCollisionDelta':cucsEtherLossStatsMultiCollisionDelta,'cucsEtherLossStatsMultiCollisionDeltaAvg':cucsEtherLossStatsMultiCollisionDeltaAvg,'cucsEtherLossStatsMultiCollisionDeltaMax':cucsEtherLossStatsMultiCollisionDeltaMax,'cucsEtherLossStatsMultiCollisionDeltaMin':cucsEtherLossStatsMultiCollisionDeltaMin,'cucsEtherLossStatsSingleCollision':cucsEtherLossStatsSingleCollision,'cucsEtherLossStatsSingleCollisionDelta':cucsEtherLossStatsSingleCollisionDelta,'cucsEtherLossStatsSingleCollisionDeltaAvg':cucsEtherLossStatsSingleCollisionDeltaAvg,'cucsEtherLossStatsSingleCollisionDeltaMax':cucsEtherLossStatsSingleCollisionDeltaMax,'cucsEtherLossStatsSingleCollisionDeltaMin':cucsEtherLossStatsSingleCollisionDeltaMin,'cucsEtherLossStatsSuspect':cucsEtherLossStatsSuspect,'cucsEtherLossStatsSymbol':cucsEtherLossStatsSymbol,'cucsEtherLossStatsSymbolDelta':cucsEtherLossStatsSymbolDelta,'cucsEtherLossStatsSymbolDeltaAvg':cucsEtherLossStatsSymbolDeltaAvg,'cucsEtherLossStatsSymbolDeltaMax':cucsEtherLossStatsSymbolDeltaMax,'cucsEtherLossStatsSymbolDeltaMin':cucsEtherLossStatsSymbolDeltaMin,'cucsEtherLossStatsThresholded':cucsEtherLossStatsThresholded,'cucsEtherLossStatsTimeCollected':cucsEtherLossStatsTimeCollected,'cucsEtherLossStatsUpdate':cucsEtherLossStatsUpdate,'cucsEtherLossStatsHistTable':cucsEtherLossStatsHistTable,'cucsEtherLossStatsHistEntry':cucsEtherLossStatsHistEntry,_H:cucsEtherLossStatsHistInstanceId,'cucsEtherLossStatsHistDn':cucsEtherLossStatsHistDn,'cucsEtherLossStatsHistRn':cucsEtherLossStatsHistRn,'cucsEtherLossStatsHistSQETest':cucsEtherLossStatsHistSQETest,'cucsEtherLossStatsHistSQETestDelta':cucsEtherLossStatsHistSQETestDelta,'cucsEtherLossStatsHistSQETestDeltaAvg':cucsEtherLossStatsHistSQETestDeltaAvg,'cucsEtherLossStatsHistSQETestDeltaMax':cucsEtherLossStatsHistSQETestDeltaMax,'cucsEtherLossStatsHistSQETestDeltaMin':cucsEtherLossStatsHistSQETestDeltaMin,'cucsEtherLossStatsHistCarrierSense':cucsEtherLossStatsHistCarrierSense,'cucsEtherLossStatsHistCarrierSenseDelta':cucsEtherLossStatsHistCarrierSenseDelta,'cucsEtherLossStatsHistCarrierSenseDeltaAvg':cucsEtherLossStatsHistCarrierSenseDeltaAvg,'cucsEtherLossStatsHistCarrierSenseDeltaMax':cucsEtherLossStatsHistCarrierSenseDeltaMax,'cucsEtherLossStatsHistCarrierSenseDeltaMin':cucsEtherLossStatsHistCarrierSenseDeltaMin,'cucsEtherLossStatsHistExcessCollision':cucsEtherLossStatsHistExcessCollision,'cucsEtherLossStatsHistExcessCollisionDelta':cucsEtherLossStatsHistExcessCollisionDelta,'cucsEtherLossStatsHistExcessCollisionDeltaAvg':cucsEtherLossStatsHistExcessCollisionDeltaAvg,'cucsEtherLossStatsHistExcessCollisionDeltaMax':cucsEtherLossStatsHistExcessCollisionDeltaMax,'cucsEtherLossStatsHistExcessCollisionDeltaMin':cucsEtherLossStatsHistExcessCollisionDeltaMin,'cucsEtherLossStatsHistGiants':cucsEtherLossStatsHistGiants,'cucsEtherLossStatsHistGiantsDelta':cucsEtherLossStatsHistGiantsDelta,'cucsEtherLossStatsHistGiantsDeltaAvg':cucsEtherLossStatsHistGiantsDeltaAvg,'cucsEtherLossStatsHistGiantsDeltaMax':cucsEtherLossStatsHistGiantsDeltaMax,'cucsEtherLossStatsHistGiantsDeltaMin':cucsEtherLossStatsHistGiantsDeltaMin,'cucsEtherLossStatsHistId':cucsEtherLossStatsHistId,'cucsEtherLossStatsHistLateCollision':cucsEtherLossStatsHistLateCollision,'cucsEtherLossStatsHistLateCollisionDelta':cucsEtherLossStatsHistLateCollisionDelta,'cucsEtherLossStatsHistLateCollisionDeltaAvg':cucsEtherLossStatsHistLateCollisionDeltaAvg,'cucsEtherLossStatsHistLateCollisionDeltaMax':cucsEtherLossStatsHistLateCollisionDeltaMax,'cucsEtherLossStatsHistLateCollisionDeltaMin':cucsEtherLossStatsHistLateCollisionDeltaMin,'cucsEtherLossStatsHistMostRecent':cucsEtherLossStatsHistMostRecent,'cucsEtherLossStatsHistMultiCollision':cucsEtherLossStatsHistMultiCollision,'cucsEtherLossStatsHistMultiCollisionDelta':cucsEtherLossStatsHistMultiCollisionDelta,'cucsEtherLossStatsHistMultiCollisionDeltaAvg':cucsEtherLossStatsHistMultiCollisionDeltaAvg,'cucsEtherLossStatsHistMultiCollisionDeltaMax':cucsEtherLossStatsHistMultiCollisionDeltaMax,'cucsEtherLossStatsHistMultiCollisionDeltaMin':cucsEtherLossStatsHistMultiCollisionDeltaMin,'cucsEtherLossStatsHistSingleCollision':cucsEtherLossStatsHistSingleCollision,'cucsEtherLossStatsHistSingleCollisionDelta':cucsEtherLossStatsHistSingleCollisionDelta,'cucsEtherLossStatsHistSingleCollisionDeltaAvg':cucsEtherLossStatsHistSingleCollisionDeltaAvg,'cucsEtherLossStatsHistSingleCollisionDeltaMax':cucsEtherLossStatsHistSingleCollisionDeltaMax,'cucsEtherLossStatsHistSingleCollisionDeltaMin':cucsEtherLossStatsHistSingleCollisionDeltaMin,'cucsEtherLossStatsHistSuspect':cucsEtherLossStatsHistSuspect,'cucsEtherLossStatsHistSymbol':cucsEtherLossStatsHistSymbol,'cucsEtherLossStatsHistSymbolDelta':cucsEtherLossStatsHistSymbolDelta,'cucsEtherLossStatsHistSymbolDeltaAvg':cucsEtherLossStatsHistSymbolDeltaAvg,'cucsEtherLossStatsHistSymbolDeltaMax':cucsEtherLossStatsHistSymbolDeltaMax,'cucsEtherLossStatsHistSymbolDeltaMin':cucsEtherLossStatsHistSymbolDeltaMin,'cucsEtherLossStatsHistThresholded':cucsEtherLossStatsHistThresholded,'cucsEtherLossStatsHistTimeCollected':cucsEtherLossStatsHistTimeCollected,'cucsEtherNicIfConfigTable':cucsEtherNicIfConfigTable,'cucsEtherNicIfConfigEntry':cucsEtherNicIfConfigEntry,_I:cucsEtherNicIfConfigInstanceId,'cucsEtherNicIfConfigDn':cucsEtherNicIfConfigDn,'cucsEtherNicIfConfigRn':cucsEtherNicIfConfigRn,'cucsEtherPIoTable':cucsEtherPIoTable,'cucsEtherPIoEntry':cucsEtherPIoEntry,_J:cucsEtherPIoInstanceId,'cucsEtherPIoDn':cucsEtherPIoDn,'cucsEtherPIoRn':cucsEtherPIoRn,'cucsEtherPIoAdminState':cucsEtherPIoAdminState,'cucsEtherPIoChassisId':cucsEtherPIoChassisId,'cucsEtherPIoEncap':cucsEtherPIoEncap,'cucsEtherPIoEpDn':cucsEtherPIoEpDn,'cucsEtherPIoFltAggr':cucsEtherPIoFltAggr,'cucsEtherPIoIfRole':cucsEtherPIoIfRole,'cucsEtherPIoIfType':cucsEtherPIoIfType,'cucsEtherPIoLocale':cucsEtherPIoLocale,'cucsEtherPIoMac':cucsEtherPIoMac,'cucsEtherPIoMode':cucsEtherPIoMode,'cucsEtherPIoModel':cucsEtherPIoModel,'cucsEtherPIoName':cucsEtherPIoName,'cucsEtherPIoOperSpeed':cucsEtherPIoOperSpeed,'cucsEtherPIoOperState':cucsEtherPIoOperState,'cucsEtherPIoPeerDn':cucsEtherPIoPeerDn,'cucsEtherPIoPeerPortId':cucsEtherPIoPeerPortId,'cucsEtherPIoPeerSlotId':cucsEtherPIoPeerSlotId,'cucsEtherPIoPortId':cucsEtherPIoPortId,'cucsEtherPIoRevision':cucsEtherPIoRevision,'cucsEtherPIoSerial':cucsEtherPIoSerial,'cucsEtherPIoSlotId':cucsEtherPIoSlotId,'cucsEtherPIoStateQual':cucsEtherPIoStateQual,'cucsEtherPIoSwitchId':cucsEtherPIoSwitchId,'cucsEtherPIoTransport':cucsEtherPIoTransport,'cucsEtherPIoTs':cucsEtherPIoTs,'cucsEtherPIoType':cucsEtherPIoType,'cucsEtherPIoUsrLbl':cucsEtherPIoUsrLbl,'cucsEtherPIoVendor':cucsEtherPIoVendor,'cucsEtherPIoFsmDescr':cucsEtherPIoFsmDescr,'cucsEtherPIoFsmPrev':cucsEtherPIoFsmPrev,'cucsEtherPIoFsmProgr':cucsEtherPIoFsmProgr,'cucsEtherPIoFsmRmtInvErrCode':cucsEtherPIoFsmRmtInvErrCode,'cucsEtherPIoFsmRmtInvErrDescr':cucsEtherPIoFsmRmtInvErrDescr,'cucsEtherPIoFsmRmtInvRslt':cucsEtherPIoFsmRmtInvRslt,'cucsEtherPIoFsmStageDescr':cucsEtherPIoFsmStageDescr,'cucsEtherPIoFsmStamp':cucsEtherPIoFsmStamp,'cucsEtherPIoFsmStatus':cucsEtherPIoFsmStatus,'cucsEtherPIoFsmTry':cucsEtherPIoFsmTry,'cucsEtherPIoLicGP':cucsEtherPIoLicGP,'cucsEtherPIoLicState':cucsEtherPIoLicState,'cucsEtherPIoXcvrType':cucsEtherPIoXcvrType,'cucsEtherPIoPeerChassisId':cucsEtherPIoPeerChassisId,'cucsEtherPIoAdminTransport':cucsEtherPIoAdminTransport,'cucsEtherPIoLc':cucsEtherPIoLc,'cucsEtherPIoUnifiedPort':cucsEtherPIoUnifiedPort,'cucsEtherPIoIsPortChannelMember':cucsEtherPIoIsPortChannelMember,'cucsEtherPIoAggrPortId':cucsEtherPIoAggrPortId,'cucsEtherPIoPeerAggrPortId':cucsEtherPIoPeerAggrPortId,'cucsEtherPIoNonCR4':cucsEtherPIoNonCR4,'cucsEtherPIoIsBreakoutXcvr':cucsEtherPIoIsBreakoutXcvr,'cucsEtherPIoPortCapability':cucsEtherPIoPortCapability,'cucsEtherPauseStatsTable':cucsEtherPauseStatsTable,'cucsEtherPauseStatsEntry':cucsEtherPauseStatsEntry,_K:cucsEtherPauseStatsInstanceId,'cucsEtherPauseStatsDn':cucsEtherPauseStatsDn,'cucsEtherPauseStatsRn':cucsEtherPauseStatsRn,'cucsEtherPauseStatsIntervals':cucsEtherPauseStatsIntervals,'cucsEtherPauseStatsRecvPause':cucsEtherPauseStatsRecvPause,'cucsEtherPauseStatsRecvPauseDelta':cucsEtherPauseStatsRecvPauseDelta,'cucsEtherPauseStatsRecvPauseDeltaAvg':cucsEtherPauseStatsRecvPauseDeltaAvg,'cucsEtherPauseStatsRecvPauseDeltaMax':cucsEtherPauseStatsRecvPauseDeltaMax,'cucsEtherPauseStatsRecvPauseDeltaMin':cucsEtherPauseStatsRecvPauseDeltaMin,'cucsEtherPauseStatsResets':cucsEtherPauseStatsResets,'cucsEtherPauseStatsResetsDelta':cucsEtherPauseStatsResetsDelta,'cucsEtherPauseStatsResetsDeltaAvg':cucsEtherPauseStatsResetsDeltaAvg,'cucsEtherPauseStatsResetsDeltaMax':cucsEtherPauseStatsResetsDeltaMax,'cucsEtherPauseStatsResetsDeltaMin':cucsEtherPauseStatsResetsDeltaMin,'cucsEtherPauseStatsSuspect':cucsEtherPauseStatsSuspect,'cucsEtherPauseStatsThresholded':cucsEtherPauseStatsThresholded,'cucsEtherPauseStatsTimeCollected':cucsEtherPauseStatsTimeCollected,'cucsEtherPauseStatsUpdate':cucsEtherPauseStatsUpdate,'cucsEtherPauseStatsXmitPause':cucsEtherPauseStatsXmitPause,'cucsEtherPauseStatsXmitPauseDelta':cucsEtherPauseStatsXmitPauseDelta,'cucsEtherPauseStatsXmitPauseDeltaAvg':cucsEtherPauseStatsXmitPauseDeltaAvg,'cucsEtherPauseStatsXmitPauseDeltaMax':cucsEtherPauseStatsXmitPauseDeltaMax,'cucsEtherPauseStatsXmitPauseDeltaMin':cucsEtherPauseStatsXmitPauseDeltaMin,'cucsEtherPauseStatsHistTable':cucsEtherPauseStatsHistTable,'cucsEtherPauseStatsHistEntry':cucsEtherPauseStatsHistEntry,_L:cucsEtherPauseStatsHistInstanceId,'cucsEtherPauseStatsHistDn':cucsEtherPauseStatsHistDn,'cucsEtherPauseStatsHistRn':cucsEtherPauseStatsHistRn,'cucsEtherPauseStatsHistId':cucsEtherPauseStatsHistId,'cucsEtherPauseStatsHistMostRecent':cucsEtherPauseStatsHistMostRecent,'cucsEtherPauseStatsHistRecvPause':cucsEtherPauseStatsHistRecvPause,'cucsEtherPauseStatsHistRecvPauseDelta':cucsEtherPauseStatsHistRecvPauseDelta,'cucsEtherPauseStatsHistRecvPauseDeltaAvg':cucsEtherPauseStatsHistRecvPauseDeltaAvg,'cucsEtherPauseStatsHistRecvPauseDeltaMax':cucsEtherPauseStatsHistRecvPauseDeltaMax,'cucsEtherPauseStatsHistRecvPauseDeltaMin':cucsEtherPauseStatsHistRecvPauseDeltaMin,'cucsEtherPauseStatsHistResets':cucsEtherPauseStatsHistResets,'cucsEtherPauseStatsHistResetsDelta':cucsEtherPauseStatsHistResetsDelta,'cucsEtherPauseStatsHistResetsDeltaAvg':cucsEtherPauseStatsHistResetsDeltaAvg,'cucsEtherPauseStatsHistResetsDeltaMax':cucsEtherPauseStatsHistResetsDeltaMax,'cucsEtherPauseStatsHistResetsDeltaMin':cucsEtherPauseStatsHistResetsDeltaMin,'cucsEtherPauseStatsHistSuspect':cucsEtherPauseStatsHistSuspect,'cucsEtherPauseStatsHistThresholded':cucsEtherPauseStatsHistThresholded,'cucsEtherPauseStatsHistTimeCollected':cucsEtherPauseStatsHistTimeCollected,'cucsEtherPauseStatsHistXmitPause':cucsEtherPauseStatsHistXmitPause,'cucsEtherPauseStatsHistXmitPauseDelta':cucsEtherPauseStatsHistXmitPauseDelta,'cucsEtherPauseStatsHistXmitPauseDeltaAvg':cucsEtherPauseStatsHistXmitPauseDeltaAvg,'cucsEtherPauseStatsHistXmitPauseDeltaMax':cucsEtherPauseStatsHistXmitPauseDeltaMax,'cucsEtherPauseStatsHistXmitPauseDeltaMin':cucsEtherPauseStatsHistXmitPauseDeltaMin,'cucsEtherRxStatsTable':cucsEtherRxStatsTable,'cucsEtherRxStatsEntry':cucsEtherRxStatsEntry,_M:cucsEtherRxStatsInstanceId,'cucsEtherRxStatsDn':cucsEtherRxStatsDn,'cucsEtherRxStatsRn':cucsEtherRxStatsRn,'cucsEtherRxStatsBroadcastPackets':cucsEtherRxStatsBroadcastPackets,'cucsEtherRxStatsBroadcastPacketsDelta':cucsEtherRxStatsBroadcastPacketsDelta,'cucsEtherRxStatsBroadcastPacketsDeltaAvg':cucsEtherRxStatsBroadcastPacketsDeltaAvg,'cucsEtherRxStatsBroadcastPacketsDeltaMax':cucsEtherRxStatsBroadcastPacketsDeltaMax,'cucsEtherRxStatsBroadcastPacketsDeltaMin':cucsEtherRxStatsBroadcastPacketsDeltaMin,'cucsEtherRxStatsIntervals':cucsEtherRxStatsIntervals,'cucsEtherRxStatsJumboPackets':cucsEtherRxStatsJumboPackets,'cucsEtherRxStatsJumboPacketsDelta':cucsEtherRxStatsJumboPacketsDelta,'cucsEtherRxStatsJumboPacketsDeltaAvg':cucsEtherRxStatsJumboPacketsDeltaAvg,'cucsEtherRxStatsJumboPacketsDeltaMax':cucsEtherRxStatsJumboPacketsDeltaMax,'cucsEtherRxStatsJumboPacketsDeltaMin':cucsEtherRxStatsJumboPacketsDeltaMin,'cucsEtherRxStatsMulticastPackets':cucsEtherRxStatsMulticastPackets,'cucsEtherRxStatsMulticastPacketsDelta':cucsEtherRxStatsMulticastPacketsDelta,'cucsEtherRxStatsMulticastPacketsDeltaAvg':cucsEtherRxStatsMulticastPacketsDeltaAvg,'cucsEtherRxStatsMulticastPacketsDeltaMax':cucsEtherRxStatsMulticastPacketsDeltaMax,'cucsEtherRxStatsMulticastPacketsDeltaMin':cucsEtherRxStatsMulticastPacketsDeltaMin,'cucsEtherRxStatsSuspect':cucsEtherRxStatsSuspect,'cucsEtherRxStatsThresholded':cucsEtherRxStatsThresholded,'cucsEtherRxStatsTimeCollected':cucsEtherRxStatsTimeCollected,'cucsEtherRxStatsTotalBytes':cucsEtherRxStatsTotalBytes,'cucsEtherRxStatsTotalBytesDelta':cucsEtherRxStatsTotalBytesDelta,'cucsEtherRxStatsTotalBytesDeltaAvg':cucsEtherRxStatsTotalBytesDeltaAvg,'cucsEtherRxStatsTotalBytesDeltaMax':cucsEtherRxStatsTotalBytesDeltaMax,'cucsEtherRxStatsTotalBytesDeltaMin':cucsEtherRxStatsTotalBytesDeltaMin,'cucsEtherRxStatsTotalPackets':cucsEtherRxStatsTotalPackets,'cucsEtherRxStatsTotalPacketsDelta':cucsEtherRxStatsTotalPacketsDelta,'cucsEtherRxStatsTotalPacketsDeltaAvg':cucsEtherRxStatsTotalPacketsDeltaAvg,'cucsEtherRxStatsTotalPacketsDeltaMax':cucsEtherRxStatsTotalPacketsDeltaMax,'cucsEtherRxStatsTotalPacketsDeltaMin':cucsEtherRxStatsTotalPacketsDeltaMin,'cucsEtherRxStatsUnicastPackets':cucsEtherRxStatsUnicastPackets,'cucsEtherRxStatsUnicastPacketsDelta':cucsEtherRxStatsUnicastPacketsDelta,'cucsEtherRxStatsUnicastPacketsDeltaAvg':cucsEtherRxStatsUnicastPacketsDeltaAvg,'cucsEtherRxStatsUnicastPacketsDeltaMax':cucsEtherRxStatsUnicastPacketsDeltaMax,'cucsEtherRxStatsUnicastPacketsDeltaMin':cucsEtherRxStatsUnicastPacketsDeltaMin,'cucsEtherRxStatsUpdate':cucsEtherRxStatsUpdate,'cucsEtherRxStatsHistTable':cucsEtherRxStatsHistTable,'cucsEtherRxStatsHistEntry':cucsEtherRxStatsHistEntry,_N:cucsEtherRxStatsHistInstanceId,'cucsEtherRxStatsHistDn':cucsEtherRxStatsHistDn,'cucsEtherRxStatsHistRn':cucsEtherRxStatsHistRn,'cucsEtherRxStatsHistBroadcastPackets':cucsEtherRxStatsHistBroadcastPackets,'cucsEtherRxStatsHistBroadcastPacketsDelta':cucsEtherRxStatsHistBroadcastPacketsDelta,'cucsEtherRxStatsHistBroadcastPacketsDeltaAvg':cucsEtherRxStatsHistBroadcastPacketsDeltaAvg,'cucsEtherRxStatsHistBroadcastPacketsDeltaMax':cucsEtherRxStatsHistBroadcastPacketsDeltaMax,'cucsEtherRxStatsHistBroadcastPacketsDeltaMin':cucsEtherRxStatsHistBroadcastPacketsDeltaMin,'cucsEtherRxStatsHistId':cucsEtherRxStatsHistId,'cucsEtherRxStatsHistJumboPackets':cucsEtherRxStatsHistJumboPackets,'cucsEtherRxStatsHistJumboPacketsDelta':cucsEtherRxStatsHistJumboPacketsDelta,'cucsEtherRxStatsHistJumboPacketsDeltaAvg':cucsEtherRxStatsHistJumboPacketsDeltaAvg,'cucsEtherRxStatsHistJumboPacketsDeltaMax':cucsEtherRxStatsHistJumboPacketsDeltaMax,'cucsEtherRxStatsHistJumboPacketsDeltaMin':cucsEtherRxStatsHistJumboPacketsDeltaMin,'cucsEtherRxStatsHistMostRecent':cucsEtherRxStatsHistMostRecent,'cucsEtherRxStatsHistMulticastPackets':cucsEtherRxStatsHistMulticastPackets,'cucsEtherRxStatsHistMulticastPacketsDelta':cucsEtherRxStatsHistMulticastPacketsDelta,'cucsEtherRxStatsHistMulticastPacketsDeltaAvg':cucsEtherRxStatsHistMulticastPacketsDeltaAvg,'cucsEtherRxStatsHistMulticastPacketsDeltaMax':cucsEtherRxStatsHistMulticastPacketsDeltaMax,'cucsEtherRxStatsHistMulticastPacketsDeltaMin':cucsEtherRxStatsHistMulticastPacketsDeltaMin,'cucsEtherRxStatsHistSuspect':cucsEtherRxStatsHistSuspect,'cucsEtherRxStatsHistThresholded':cucsEtherRxStatsHistThresholded,'cucsEtherRxStatsHistTimeCollected':cucsEtherRxStatsHistTimeCollected,'cucsEtherRxStatsHistTotalBytes':cucsEtherRxStatsHistTotalBytes,'cucsEtherRxStatsHistTotalBytesDelta':cucsEtherRxStatsHistTotalBytesDelta,'cucsEtherRxStatsHistTotalBytesDeltaAvg':cucsEtherRxStatsHistTotalBytesDeltaAvg,'cucsEtherRxStatsHistTotalBytesDeltaMax':cucsEtherRxStatsHistTotalBytesDeltaMax,'cucsEtherRxStatsHistTotalBytesDeltaMin':cucsEtherRxStatsHistTotalBytesDeltaMin,'cucsEtherRxStatsHistTotalPackets':cucsEtherRxStatsHistTotalPackets,'cucsEtherRxStatsHistTotalPacketsDelta':cucsEtherRxStatsHistTotalPacketsDelta,'cucsEtherRxStatsHistTotalPacketsDeltaAvg':cucsEtherRxStatsHistTotalPacketsDeltaAvg,'cucsEtherRxStatsHistTotalPacketsDeltaMax':cucsEtherRxStatsHistTotalPacketsDeltaMax,'cucsEtherRxStatsHistTotalPacketsDeltaMin':cucsEtherRxStatsHistTotalPacketsDeltaMin,'cucsEtherRxStatsHistUnicastPackets':cucsEtherRxStatsHistUnicastPackets,'cucsEtherRxStatsHistUnicastPacketsDelta':cucsEtherRxStatsHistUnicastPacketsDelta,'cucsEtherRxStatsHistUnicastPacketsDeltaAvg':cucsEtherRxStatsHistUnicastPacketsDeltaAvg,'cucsEtherRxStatsHistUnicastPacketsDeltaMax':cucsEtherRxStatsHistUnicastPacketsDeltaMax,'cucsEtherRxStatsHistUnicastPacketsDeltaMin':cucsEtherRxStatsHistUnicastPacketsDeltaMin,'cucsEtherServerIntFIoTable':cucsEtherServerIntFIoTable,'cucsEtherServerIntFIoEntry':cucsEtherServerIntFIoEntry,_O:cucsEtherServerIntFIoInstanceId,'cucsEtherServerIntFIoDn':cucsEtherServerIntFIoDn,'cucsEtherServerIntFIoRn':cucsEtherServerIntFIoRn,'cucsEtherServerIntFIoAdminState':cucsEtherServerIntFIoAdminState,'cucsEtherServerIntFIoChassisId':cucsEtherServerIntFIoChassisId,'cucsEtherServerIntFIoEncap':cucsEtherServerIntFIoEncap,'cucsEtherServerIntFIoEpDn':cucsEtherServerIntFIoEpDn,'cucsEtherServerIntFIoFltAggr':cucsEtherServerIntFIoFltAggr,'cucsEtherServerIntFIoIfRole':cucsEtherServerIntFIoIfRole,'cucsEtherServerIntFIoIfType':cucsEtherServerIntFIoIfType,'cucsEtherServerIntFIoLocale':cucsEtherServerIntFIoLocale,'cucsEtherServerIntFIoMode':cucsEtherServerIntFIoMode,'cucsEtherServerIntFIoModel':cucsEtherServerIntFIoModel,'cucsEtherServerIntFIoName':cucsEtherServerIntFIoName,'cucsEtherServerIntFIoOperBorderPortId':cucsEtherServerIntFIoOperBorderPortId,'cucsEtherServerIntFIoOperBorderSlotId':cucsEtherServerIntFIoOperBorderSlotId,'cucsEtherServerIntFIoOperState':cucsEtherServerIntFIoOperState,'cucsEtherServerIntFIoPeerDn':cucsEtherServerIntFIoPeerDn,'cucsEtherServerIntFIoPeerPortId':cucsEtherServerIntFIoPeerPortId,'cucsEtherServerIntFIoPeerSlotId':cucsEtherServerIntFIoPeerSlotId,'cucsEtherServerIntFIoPortId':cucsEtherServerIntFIoPortId,'cucsEtherServerIntFIoRevision':cucsEtherServerIntFIoRevision,'cucsEtherServerIntFIoSerial':cucsEtherServerIntFIoSerial,'cucsEtherServerIntFIoSlotId':cucsEtherServerIntFIoSlotId,'cucsEtherServerIntFIoStateQual':cucsEtherServerIntFIoStateQual,'cucsEtherServerIntFIoSwitchId':cucsEtherServerIntFIoSwitchId,'cucsEtherServerIntFIoTransport':cucsEtherServerIntFIoTransport,'cucsEtherServerIntFIoTs':cucsEtherServerIntFIoTs,'cucsEtherServerIntFIoType':cucsEtherServerIntFIoType,'cucsEtherServerIntFIoVendor':cucsEtherServerIntFIoVendor,'cucsEtherServerIntFIoMac':cucsEtherServerIntFIoMac,'cucsEtherServerIntFIoPeerChassisId':cucsEtherServerIntFIoPeerChassisId,'cucsEtherServerIntFIoXcvrType':cucsEtherServerIntFIoXcvrType,'cucsEtherServerIntFIoAdminSpeed':cucsEtherServerIntFIoAdminSpeed,'cucsEtherServerIntFIoFsmDescr':cucsEtherServerIntFIoFsmDescr,'cucsEtherServerIntFIoFsmPrev':cucsEtherServerIntFIoFsmPrev,'cucsEtherServerIntFIoFsmProgr':cucsEtherServerIntFIoFsmProgr,'cucsEtherServerIntFIoFsmRmtInvErrCode':cucsEtherServerIntFIoFsmRmtInvErrCode,'cucsEtherServerIntFIoFsmRmtInvErrDescr':cucsEtherServerIntFIoFsmRmtInvErrDescr,'cucsEtherServerIntFIoFsmRmtInvRslt':cucsEtherServerIntFIoFsmRmtInvRslt,'cucsEtherServerIntFIoFsmStageDescr':cucsEtherServerIntFIoFsmStageDescr,'cucsEtherServerIntFIoFsmStamp':cucsEtherServerIntFIoFsmStamp,'cucsEtherServerIntFIoFsmStatus':cucsEtherServerIntFIoFsmStatus,'cucsEtherServerIntFIoFsmTry':cucsEtherServerIntFIoFsmTry,'cucsEtherServerIntFIoNsSize':cucsEtherServerIntFIoNsSize,'cucsEtherServerIntFIoPeerEncap':cucsEtherServerIntFIoPeerEncap,'cucsEtherServerIntFIoAggrPortId':cucsEtherServerIntFIoAggrPortId,'cucsEtherServerIntFIoPeerAggrPortId':cucsEtherServerIntFIoPeerAggrPortId,'cucsEtherServerIntFIoMacAddr':cucsEtherServerIntFIoMacAddr,'cucsEtherServerIntFIoOperBorderAggrPortId':cucsEtherServerIntFIoOperBorderAggrPortId,'cucsEtherServerIntFIoUserRecoveryOperation':cucsEtherServerIntFIoUserRecoveryOperation,'cucsEtherSwIfConfigTable':cucsEtherSwIfConfigTable,'cucsEtherSwIfConfigEntry':cucsEtherSwIfConfigEntry,_P:cucsEtherSwIfConfigInstanceId,'cucsEtherSwIfConfigDn':cucsEtherSwIfConfigDn,'cucsEtherSwIfConfigRn':cucsEtherSwIfConfigRn,'cucsEtherSwitchIntFIoTable':cucsEtherSwitchIntFIoTable,'cucsEtherSwitchIntFIoEntry':cucsEtherSwitchIntFIoEntry,_Q:cucsEtherSwitchIntFIoInstanceId,'cucsEtherSwitchIntFIoDn':cucsEtherSwitchIntFIoDn,'cucsEtherSwitchIntFIoRn':cucsEtherSwitchIntFIoRn,'cucsEtherSwitchIntFIoAck':cucsEtherSwitchIntFIoAck,'cucsEtherSwitchIntFIoAdminState':cucsEtherSwitchIntFIoAdminState,'cucsEtherSwitchIntFIoChassisId':cucsEtherSwitchIntFIoChassisId,'cucsEtherSwitchIntFIoDiscovery':cucsEtherSwitchIntFIoDiscovery,'cucsEtherSwitchIntFIoEncap':cucsEtherSwitchIntFIoEncap,'cucsEtherSwitchIntFIoEpDn':cucsEtherSwitchIntFIoEpDn,'cucsEtherSwitchIntFIoFltAggr':cucsEtherSwitchIntFIoFltAggr,'cucsEtherSwitchIntFIoIfRole':cucsEtherSwitchIntFIoIfRole,'cucsEtherSwitchIntFIoIfType':cucsEtherSwitchIntFIoIfType,'cucsEtherSwitchIntFIoLocale':cucsEtherSwitchIntFIoLocale,'cucsEtherSwitchIntFIoMode':cucsEtherSwitchIntFIoMode,'cucsEtherSwitchIntFIoModel':cucsEtherSwitchIntFIoModel,'cucsEtherSwitchIntFIoName':cucsEtherSwitchIntFIoName,'cucsEtherSwitchIntFIoOperState':cucsEtherSwitchIntFIoOperState,'cucsEtherSwitchIntFIoPeerDn':cucsEtherSwitchIntFIoPeerDn,'cucsEtherSwitchIntFIoPeerPortId':cucsEtherSwitchIntFIoPeerPortId,'cucsEtherSwitchIntFIoPeerSlotId':cucsEtherSwitchIntFIoPeerSlotId,'cucsEtherSwitchIntFIoPortId':cucsEtherSwitchIntFIoPortId,'cucsEtherSwitchIntFIoRevision':cucsEtherSwitchIntFIoRevision,'cucsEtherSwitchIntFIoSerial':cucsEtherSwitchIntFIoSerial,'cucsEtherSwitchIntFIoSlotId':cucsEtherSwitchIntFIoSlotId,'cucsEtherSwitchIntFIoStateQual':cucsEtherSwitchIntFIoStateQual,'cucsEtherSwitchIntFIoSwitchId':cucsEtherSwitchIntFIoSwitchId,'cucsEtherSwitchIntFIoTransport':cucsEtherSwitchIntFIoTransport,'cucsEtherSwitchIntFIoTs':cucsEtherSwitchIntFIoTs,'cucsEtherSwitchIntFIoType':cucsEtherSwitchIntFIoType,'cucsEtherSwitchIntFIoVendor':cucsEtherSwitchIntFIoVendor,'cucsEtherSwitchIntFIoPeerChassisId':cucsEtherSwitchIntFIoPeerChassisId,'cucsEtherSwitchIntFIoXcvrType':cucsEtherSwitchIntFIoXcvrType,'cucsEtherSwitchIntFIoDelFeTs':cucsEtherSwitchIntFIoDelFeTs,'cucsEtherSwitchIntFIoNewFeTs':cucsEtherSwitchIntFIoNewFeTs,'cucsEtherSwitchIntFIoAggrPortId':cucsEtherSwitchIntFIoAggrPortId,'cucsEtherSwitchIntFIoPeerAggrPortId':cucsEtherSwitchIntFIoPeerAggrPortId,'cucsEtherSwitchIntFIoMacAddr':cucsEtherSwitchIntFIoMacAddr,'cucsEtherTxStatsTable':cucsEtherTxStatsTable,'cucsEtherTxStatsEntry':cucsEtherTxStatsEntry,_R:cucsEtherTxStatsInstanceId,'cucsEtherTxStatsDn':cucsEtherTxStatsDn,'cucsEtherTxStatsRn':cucsEtherTxStatsRn,'cucsEtherTxStatsBroadcastPackets':cucsEtherTxStatsBroadcastPackets,'cucsEtherTxStatsBroadcastPacketsDelta':cucsEtherTxStatsBroadcastPacketsDelta,'cucsEtherTxStatsBroadcastPacketsDeltaAvg':cucsEtherTxStatsBroadcastPacketsDeltaAvg,'cucsEtherTxStatsBroadcastPacketsDeltaMax':cucsEtherTxStatsBroadcastPacketsDeltaMax,'cucsEtherTxStatsBroadcastPacketsDeltaMin':cucsEtherTxStatsBroadcastPacketsDeltaMin,'cucsEtherTxStatsIntervals':cucsEtherTxStatsIntervals,'cucsEtherTxStatsJumboPackets':cucsEtherTxStatsJumboPackets,'cucsEtherTxStatsJumboPacketsDelta':cucsEtherTxStatsJumboPacketsDelta,'cucsEtherTxStatsJumboPacketsDeltaAvg':cucsEtherTxStatsJumboPacketsDeltaAvg,'cucsEtherTxStatsJumboPacketsDeltaMax':cucsEtherTxStatsJumboPacketsDeltaMax,'cucsEtherTxStatsJumboPacketsDeltaMin':cucsEtherTxStatsJumboPacketsDeltaMin,'cucsEtherTxStatsMulticastPackets':cucsEtherTxStatsMulticastPackets,'cucsEtherTxStatsMulticastPacketsDelta':cucsEtherTxStatsMulticastPacketsDelta,'cucsEtherTxStatsMulticastPacketsDeltaAvg':cucsEtherTxStatsMulticastPacketsDeltaAvg,'cucsEtherTxStatsMulticastPacketsDeltaMax':cucsEtherTxStatsMulticastPacketsDeltaMax,'cucsEtherTxStatsMulticastPacketsDeltaMin':cucsEtherTxStatsMulticastPacketsDeltaMin,'cucsEtherTxStatsSuspect':cucsEtherTxStatsSuspect,'cucsEtherTxStatsThresholded':cucsEtherTxStatsThresholded,'cucsEtherTxStatsTimeCollected':cucsEtherTxStatsTimeCollected,'cucsEtherTxStatsTotalBytes':cucsEtherTxStatsTotalBytes,'cucsEtherTxStatsTotalBytesDelta':cucsEtherTxStatsTotalBytesDelta,'cucsEtherTxStatsTotalBytesDeltaAvg':cucsEtherTxStatsTotalBytesDeltaAvg,'cucsEtherTxStatsTotalBytesDeltaMax':cucsEtherTxStatsTotalBytesDeltaMax,'cucsEtherTxStatsTotalBytesDeltaMin':cucsEtherTxStatsTotalBytesDeltaMin,'cucsEtherTxStatsTotalPackets':cucsEtherTxStatsTotalPackets,'cucsEtherTxStatsTotalPacketsDelta':cucsEtherTxStatsTotalPacketsDelta,'cucsEtherTxStatsTotalPacketsDeltaAvg':cucsEtherTxStatsTotalPacketsDeltaAvg,'cucsEtherTxStatsTotalPacketsDeltaMax':cucsEtherTxStatsTotalPacketsDeltaMax,'cucsEtherTxStatsTotalPacketsDeltaMin':cucsEtherTxStatsTotalPacketsDeltaMin,'cucsEtherTxStatsUnicastPackets':cucsEtherTxStatsUnicastPackets,'cucsEtherTxStatsUnicastPacketsDelta':cucsEtherTxStatsUnicastPacketsDelta,'cucsEtherTxStatsUnicastPacketsDeltaAvg':cucsEtherTxStatsUnicastPacketsDeltaAvg,'cucsEtherTxStatsUnicastPacketsDeltaMax':cucsEtherTxStatsUnicastPacketsDeltaMax,'cucsEtherTxStatsUnicastPacketsDeltaMin':cucsEtherTxStatsUnicastPacketsDeltaMin,'cucsEtherTxStatsUpdate':cucsEtherTxStatsUpdate,'cucsEtherTxStatsHistTable':cucsEtherTxStatsHistTable,'cucsEtherTxStatsHistEntry':cucsEtherTxStatsHistEntry,_S:cucsEtherTxStatsHistInstanceId,'cucsEtherTxStatsHistDn':cucsEtherTxStatsHistDn,'cucsEtherTxStatsHistRn':cucsEtherTxStatsHistRn,'cucsEtherTxStatsHistBroadcastPackets':cucsEtherTxStatsHistBroadcastPackets,'cucsEtherTxStatsHistBroadcastPacketsDelta':cucsEtherTxStatsHistBroadcastPacketsDelta,'cucsEtherTxStatsHistBroadcastPacketsDeltaAvg':cucsEtherTxStatsHistBroadcastPacketsDeltaAvg,'cucsEtherTxStatsHistBroadcastPacketsDeltaMax':cucsEtherTxStatsHistBroadcastPacketsDeltaMax,'cucsEtherTxStatsHistBroadcastPacketsDeltaMin':cucsEtherTxStatsHistBroadcastPacketsDeltaMin,'cucsEtherTxStatsHistId':cucsEtherTxStatsHistId,'cucsEtherTxStatsHistJumboPackets':cucsEtherTxStatsHistJumboPackets,'cucsEtherTxStatsHistJumboPacketsDelta':cucsEtherTxStatsHistJumboPacketsDelta,'cucsEtherTxStatsHistJumboPacketsDeltaAvg':cucsEtherTxStatsHistJumboPacketsDeltaAvg,'cucsEtherTxStatsHistJumboPacketsDeltaMax':cucsEtherTxStatsHistJumboPacketsDeltaMax,'cucsEtherTxStatsHistJumboPacketsDeltaMin':cucsEtherTxStatsHistJumboPacketsDeltaMin,'cucsEtherTxStatsHistMostRecent':cucsEtherTxStatsHistMostRecent,'cucsEtherTxStatsHistMulticastPackets':cucsEtherTxStatsHistMulticastPackets,'cucsEtherTxStatsHistMulticastPacketsDelta':cucsEtherTxStatsHistMulticastPacketsDelta,'cucsEtherTxStatsHistMulticastPacketsDeltaAvg':cucsEtherTxStatsHistMulticastPacketsDeltaAvg,'cucsEtherTxStatsHistMulticastPacketsDeltaMax':cucsEtherTxStatsHistMulticastPacketsDeltaMax,'cucsEtherTxStatsHistMulticastPacketsDeltaMin':cucsEtherTxStatsHistMulticastPacketsDeltaMin,'cucsEtherTxStatsHistSuspect':cucsEtherTxStatsHistSuspect,'cucsEtherTxStatsHistThresholded':cucsEtherTxStatsHistThresholded,'cucsEtherTxStatsHistTimeCollected':cucsEtherTxStatsHistTimeCollected,'cucsEtherTxStatsHistTotalBytes':cucsEtherTxStatsHistTotalBytes,'cucsEtherTxStatsHistTotalBytesDelta':cucsEtherTxStatsHistTotalBytesDelta,'cucsEtherTxStatsHistTotalBytesDeltaAvg':cucsEtherTxStatsHistTotalBytesDeltaAvg,'cucsEtherTxStatsHistTotalBytesDeltaMax':cucsEtherTxStatsHistTotalBytesDeltaMax,'cucsEtherTxStatsHistTotalBytesDeltaMin':cucsEtherTxStatsHistTotalBytesDeltaMin,'cucsEtherTxStatsHistTotalPackets':cucsEtherTxStatsHistTotalPackets,'cucsEtherTxStatsHistTotalPacketsDelta':cucsEtherTxStatsHistTotalPacketsDelta,'cucsEtherTxStatsHistTotalPacketsDeltaAvg':cucsEtherTxStatsHistTotalPacketsDeltaAvg,'cucsEtherTxStatsHistTotalPacketsDeltaMax':cucsEtherTxStatsHistTotalPacketsDeltaMax,'cucsEtherTxStatsHistTotalPacketsDeltaMin':cucsEtherTxStatsHistTotalPacketsDeltaMin,'cucsEtherTxStatsHistUnicastPackets':cucsEtherTxStatsHistUnicastPackets,'cucsEtherTxStatsHistUnicastPacketsDelta':cucsEtherTxStatsHistUnicastPacketsDelta,'cucsEtherTxStatsHistUnicastPacketsDeltaAvg':cucsEtherTxStatsHistUnicastPacketsDeltaAvg,'cucsEtherTxStatsHistUnicastPacketsDeltaMax':cucsEtherTxStatsHistUnicastPacketsDeltaMax,'cucsEtherTxStatsHistUnicastPacketsDeltaMin':cucsEtherTxStatsHistUnicastPacketsDeltaMin,'cucsEtherPortChanIdElemTable':cucsEtherPortChanIdElemTable,'cucsEtherPortChanIdElemEntry':cucsEtherPortChanIdElemEntry,_T:cucsEtherPortChanIdElemInstanceId,'cucsEtherPortChanIdElemDn':cucsEtherPortChanIdElemDn,'cucsEtherPortChanIdElemRn':cucsEtherPortChanIdElemRn,'cucsEtherPortChanIdElemId':cucsEtherPortChanIdElemId,'cucsEtherPortChanIdElemAssignedToDn':cucsEtherPortChanIdElemAssignedToDn,'cucsEtherPortChanIdElemPrevAssignedToDn':cucsEtherPortChanIdElemPrevAssignedToDn,'cucsEtherPortChanIdElemReserved':cucsEtherPortChanIdElemReserved,'cucsEtherPortChanIdUniverseTable':cucsEtherPortChanIdUniverseTable,'cucsEtherPortChanIdUniverseEntry':cucsEtherPortChanIdUniverseEntry,_U:cucsEtherPortChanIdUniverseInstanceId,'cucsEtherPortChanIdUniverseDn':cucsEtherPortChanIdUniverseDn,'cucsEtherPortChanIdUniverseRn':cucsEtherPortChanIdUniverseRn,'cucsEtherServerIntFIoPcTable':cucsEtherServerIntFIoPcTable,'cucsEtherServerIntFIoPcEntry':cucsEtherServerIntFIoPcEntry,_V:cucsEtherServerIntFIoPcInstanceId,'cucsEtherServerIntFIoPcDn':cucsEtherServerIntFIoPcDn,'cucsEtherServerIntFIoPcRn':cucsEtherServerIntFIoPcRn,'cucsEtherServerIntFIoPcChassisId':cucsEtherServerIntFIoPcChassisId,'cucsEtherServerIntFIoPcEpDn':cucsEtherServerIntFIoPcEpDn,'cucsEtherServerIntFIoPcFltAggr':cucsEtherServerIntFIoPcFltAggr,'cucsEtherServerIntFIoPcIfRole':cucsEtherServerIntFIoPcIfRole,'cucsEtherServerIntFIoPcIfType':cucsEtherServerIntFIoPcIfType,'cucsEtherServerIntFIoPcLocale':cucsEtherServerIntFIoPcLocale,'cucsEtherServerIntFIoPcName':cucsEtherServerIntFIoPcName,'cucsEtherServerIntFIoPcOperSpeed':cucsEtherServerIntFIoPcOperSpeed,'cucsEtherServerIntFIoPcOperState':cucsEtherServerIntFIoPcOperState,'cucsEtherServerIntFIoPcPeerDn':cucsEtherServerIntFIoPcPeerDn,'cucsEtherServerIntFIoPcPortId':cucsEtherServerIntFIoPcPortId,'cucsEtherServerIntFIoPcStateQual':cucsEtherServerIntFIoPcStateQual,'cucsEtherServerIntFIoPcSwitchId':cucsEtherServerIntFIoPcSwitchId,'cucsEtherServerIntFIoPcTransport':cucsEtherServerIntFIoPcTransport,'cucsEtherServerIntFIoPcType':cucsEtherServerIntFIoPcType,'cucsEtherServerIntFIoPcEpTable':cucsEtherServerIntFIoPcEpTable,'cucsEtherServerIntFIoPcEpEntry':cucsEtherServerIntFIoPcEpEntry,_W:cucsEtherServerIntFIoPcEpInstanceId,'cucsEtherServerIntFIoPcEpDnData':cucsEtherServerIntFIoPcEpDnData,'cucsEtherServerIntFIoPcEpRn':cucsEtherServerIntFIoPcEpRn,'cucsEtherServerIntFIoPcEpAdminState':cucsEtherServerIntFIoPcEpAdminState,'cucsEtherServerIntFIoPcEpChassisId':cucsEtherServerIntFIoPcEpChassisId,'cucsEtherServerIntFIoPcEpEpDn':cucsEtherServerIntFIoPcEpEpDn,'cucsEtherServerIntFIoPcEpIfRole':cucsEtherServerIntFIoPcEpIfRole,'cucsEtherServerIntFIoPcEpIfType':cucsEtherServerIntFIoPcEpIfType,'cucsEtherServerIntFIoPcEpLocale':cucsEtherServerIntFIoPcEpLocale,'cucsEtherServerIntFIoPcEpMembership':cucsEtherServerIntFIoPcEpMembership,'cucsEtherServerIntFIoPcEpName':cucsEtherServerIntFIoPcEpName,'cucsEtherServerIntFIoPcEpPeerChassisId':cucsEtherServerIntFIoPcEpPeerChassisId,'cucsEtherServerIntFIoPcEpPeerDn':cucsEtherServerIntFIoPcEpPeerDn,'cucsEtherServerIntFIoPcEpPeerPortId':cucsEtherServerIntFIoPcEpPeerPortId,'cucsEtherServerIntFIoPcEpPeerSlotId':cucsEtherServerIntFIoPcEpPeerSlotId,'cucsEtherServerIntFIoPcEpPortId':cucsEtherServerIntFIoPcEpPortId,'cucsEtherServerIntFIoPcEpSlotId':cucsEtherServerIntFIoPcEpSlotId,'cucsEtherServerIntFIoPcEpSwitchId':cucsEtherServerIntFIoPcEpSwitchId,'cucsEtherServerIntFIoPcEpTransport':cucsEtherServerIntFIoPcEpTransport,'cucsEtherServerIntFIoPcEpType':cucsEtherServerIntFIoPcEpType,'cucsEtherServerIntFIoPcEpAggrPortId':cucsEtherServerIntFIoPcEpAggrPortId,'cucsEtherServerIntFIoPcEpPeerAggrPortId':cucsEtherServerIntFIoPcEpPeerAggrPortId,'cucsEtherSwitchIntFIoPcTable':cucsEtherSwitchIntFIoPcTable,'cucsEtherSwitchIntFIoPcEntry':cucsEtherSwitchIntFIoPcEntry,_X:cucsEtherSwitchIntFIoPcInstanceId,'cucsEtherSwitchIntFIoPcDn':cucsEtherSwitchIntFIoPcDn,'cucsEtherSwitchIntFIoPcRn':cucsEtherSwitchIntFIoPcRn,'cucsEtherSwitchIntFIoPcAdminState':cucsEtherSwitchIntFIoPcAdminState,'cucsEtherSwitchIntFIoPcChassisId':cucsEtherSwitchIntFIoPcChassisId,'cucsEtherSwitchIntFIoPcEpDn':cucsEtherSwitchIntFIoPcEpDn,'cucsEtherSwitchIntFIoPcFltAggr':cucsEtherSwitchIntFIoPcFltAggr,'cucsEtherSwitchIntFIoPcIfRole':cucsEtherSwitchIntFIoPcIfRole,'cucsEtherSwitchIntFIoPcIfType':cucsEtherSwitchIntFIoPcIfType,'cucsEtherSwitchIntFIoPcLocale':cucsEtherSwitchIntFIoPcLocale,'cucsEtherSwitchIntFIoPcName':cucsEtherSwitchIntFIoPcName,'cucsEtherSwitchIntFIoPcOperSpeed':cucsEtherSwitchIntFIoPcOperSpeed,'cucsEtherSwitchIntFIoPcOperState':cucsEtherSwitchIntFIoPcOperState,'cucsEtherSwitchIntFIoPcPeerDn':cucsEtherSwitchIntFIoPcPeerDn,'cucsEtherSwitchIntFIoPcPortId':cucsEtherSwitchIntFIoPcPortId,'cucsEtherSwitchIntFIoPcStateQual':cucsEtherSwitchIntFIoPcStateQual,'cucsEtherSwitchIntFIoPcSwitchId':cucsEtherSwitchIntFIoPcSwitchId,'cucsEtherSwitchIntFIoPcTransport':cucsEtherSwitchIntFIoPcTransport,'cucsEtherSwitchIntFIoPcType':cucsEtherSwitchIntFIoPcType,'cucsEtherSwitchIntFIoPcMulticastHwHash':cucsEtherSwitchIntFIoPcMulticastHwHash,'cucsEtherSwitchIntFIoPcEpTable':cucsEtherSwitchIntFIoPcEpTable,'cucsEtherSwitchIntFIoPcEpEntry':cucsEtherSwitchIntFIoPcEpEntry,_Y:cucsEtherSwitchIntFIoPcEpInstanceId,'cucsEtherSwitchIntFIoPcEpDnData':cucsEtherSwitchIntFIoPcEpDnData,'cucsEtherSwitchIntFIoPcEpRn':cucsEtherSwitchIntFIoPcEpRn,'cucsEtherSwitchIntFIoPcEpAdminState':cucsEtherSwitchIntFIoPcEpAdminState,'cucsEtherSwitchIntFIoPcEpChassisId':cucsEtherSwitchIntFIoPcEpChassisId,'cucsEtherSwitchIntFIoPcEpEpDn':cucsEtherSwitchIntFIoPcEpEpDn,'cucsEtherSwitchIntFIoPcEpIfRole':cucsEtherSwitchIntFIoPcEpIfRole,'cucsEtherSwitchIntFIoPcEpIfType':cucsEtherSwitchIntFIoPcEpIfType,'cucsEtherSwitchIntFIoPcEpLocale':cucsEtherSwitchIntFIoPcEpLocale,'cucsEtherSwitchIntFIoPcEpMembership':cucsEtherSwitchIntFIoPcEpMembership,'cucsEtherSwitchIntFIoPcEpName':cucsEtherSwitchIntFIoPcEpName,'cucsEtherSwitchIntFIoPcEpPeerChassisId':cucsEtherSwitchIntFIoPcEpPeerChassisId,'cucsEtherSwitchIntFIoPcEpPeerDn':cucsEtherSwitchIntFIoPcEpPeerDn,'cucsEtherSwitchIntFIoPcEpPeerPortId':cucsEtherSwitchIntFIoPcEpPeerPortId,'cucsEtherSwitchIntFIoPcEpPeerSlotId':cucsEtherSwitchIntFIoPcEpPeerSlotId,'cucsEtherSwitchIntFIoPcEpPortId':cucsEtherSwitchIntFIoPcEpPortId,'cucsEtherSwitchIntFIoPcEpSlotId':cucsEtherSwitchIntFIoPcEpSlotId,'cucsEtherSwitchIntFIoPcEpStatusChangeTs':cucsEtherSwitchIntFIoPcEpStatusChangeTs,'cucsEtherSwitchIntFIoPcEpSwitchId':cucsEtherSwitchIntFIoPcEpSwitchId,'cucsEtherSwitchIntFIoPcEpTransport':cucsEtherSwitchIntFIoPcEpTransport,'cucsEtherSwitchIntFIoPcEpType':cucsEtherSwitchIntFIoPcEpType,'cucsEtherSwitchIntFIoPcEpAckState':cucsEtherSwitchIntFIoPcEpAckState,'cucsEtherSwitchIntFIoPcEpAggrPortId':cucsEtherSwitchIntFIoPcEpAggrPortId,'cucsEtherSwitchIntFIoPcEpPeerAggrPortId':cucsEtherSwitchIntFIoPcEpPeerAggrPortId,'cucsEtherServerIntFIoFsmTaskTable':cucsEtherServerIntFIoFsmTaskTable,'cucsEtherServerIntFIoFsmTaskEntry':cucsEtherServerIntFIoFsmTaskEntry,_Z:cucsEtherServerIntFIoFsmTaskInstanceId,'cucsEtherServerIntFIoFsmTaskDn':cucsEtherServerIntFIoFsmTaskDn,'cucsEtherServerIntFIoFsmTaskRn':cucsEtherServerIntFIoFsmTaskRn,'cucsEtherServerIntFIoFsmTaskCompletion':cucsEtherServerIntFIoFsmTaskCompletion,'cucsEtherServerIntFIoFsmTaskFlags':cucsEtherServerIntFIoFsmTaskFlags,'cucsEtherServerIntFIoFsmTaskItem':cucsEtherServerIntFIoFsmTaskItem,'cucsEtherServerIntFIoFsmTaskSeqId':cucsEtherServerIntFIoFsmTaskSeqId,'cucsEtherFcoeInterfaceStatsTable':cucsEtherFcoeInterfaceStatsTable,'cucsEtherFcoeInterfaceStatsEntry':cucsEtherFcoeInterfaceStatsEntry,_a:cucsEtherFcoeInterfaceStatsInstanceId,'cucsEtherFcoeInterfaceStatsDn':cucsEtherFcoeInterfaceStatsDn,'cucsEtherFcoeInterfaceStatsRn':cucsEtherFcoeInterfaceStatsRn,'cucsEtherFcoeInterfaceStatsBytesRx':cucsEtherFcoeInterfaceStatsBytesRx,'cucsEtherFcoeInterfaceStatsBytesRxDelta':cucsEtherFcoeInterfaceStatsBytesRxDelta,'cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg':cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg,'cucsEtherFcoeInterfaceStatsBytesRxDeltaMax':cucsEtherFcoeInterfaceStatsBytesRxDeltaMax,'cucsEtherFcoeInterfaceStatsBytesRxDeltaMin':cucsEtherFcoeInterfaceStatsBytesRxDeltaMin,'cucsEtherFcoeInterfaceStatsBytesTx':cucsEtherFcoeInterfaceStatsBytesTx,'cucsEtherFcoeInterfaceStatsBytesTxDelta':cucsEtherFcoeInterfaceStatsBytesTxDelta,'cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg':cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg,'cucsEtherFcoeInterfaceStatsBytesTxDeltaMax':cucsEtherFcoeInterfaceStatsBytesTxDeltaMax,'cucsEtherFcoeInterfaceStatsBytesTxDeltaMin':cucsEtherFcoeInterfaceStatsBytesTxDeltaMin,'cucsEtherFcoeInterfaceStatsDroppedRx':cucsEtherFcoeInterfaceStatsDroppedRx,'cucsEtherFcoeInterfaceStatsDroppedRxDelta':cucsEtherFcoeInterfaceStatsDroppedRxDelta,'cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg':cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg,'cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax':cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax,'cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin':cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin,'cucsEtherFcoeInterfaceStatsDroppedTx':cucsEtherFcoeInterfaceStatsDroppedTx,'cucsEtherFcoeInterfaceStatsDroppedTxDelta':cucsEtherFcoeInterfaceStatsDroppedTxDelta,'cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg':cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg,'cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax':cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax,'cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin':cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin,'cucsEtherFcoeInterfaceStatsErrorsRx':cucsEtherFcoeInterfaceStatsErrorsRx,'cucsEtherFcoeInterfaceStatsErrorsRxDelta':cucsEtherFcoeInterfaceStatsErrorsRxDelta,'cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg':cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg,'cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax':cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax,'cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin':cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin,'cucsEtherFcoeInterfaceStatsErrorsTx':cucsEtherFcoeInterfaceStatsErrorsTx,'cucsEtherFcoeInterfaceStatsErrorsTxDelta':cucsEtherFcoeInterfaceStatsErrorsTxDelta,'cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg':cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg,'cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax':cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax,'cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin':cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin,'cucsEtherFcoeInterfaceStatsIntervals':cucsEtherFcoeInterfaceStatsIntervals,'cucsEtherFcoeInterfaceStatsPacketsRx':cucsEtherFcoeInterfaceStatsPacketsRx,'cucsEtherFcoeInterfaceStatsPacketsRxDelta':cucsEtherFcoeInterfaceStatsPacketsRxDelta,'cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg':cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg,'cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax':cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax,'cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin':cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin,'cucsEtherFcoeInterfaceStatsPacketsTx':cucsEtherFcoeInterfaceStatsPacketsTx,'cucsEtherFcoeInterfaceStatsPacketsTxDelta':cucsEtherFcoeInterfaceStatsPacketsTxDelta,'cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg':cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg,'cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax':cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax,'cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin':cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin,'cucsEtherFcoeInterfaceStatsSuspect':cucsEtherFcoeInterfaceStatsSuspect,'cucsEtherFcoeInterfaceStatsThresholded':cucsEtherFcoeInterfaceStatsThresholded,'cucsEtherFcoeInterfaceStatsTimeCollected':cucsEtherFcoeInterfaceStatsTimeCollected,'cucsEtherFcoeInterfaceStatsUpdate':cucsEtherFcoeInterfaceStatsUpdate,'cucsEtherFcoeInterfaceStatsHistTable':cucsEtherFcoeInterfaceStatsHistTable,'cucsEtherFcoeInterfaceStatsHistEntry':cucsEtherFcoeInterfaceStatsHistEntry,_b:cucsEtherFcoeInterfaceStatsHistInstanceId,'cucsEtherFcoeInterfaceStatsHistDn':cucsEtherFcoeInterfaceStatsHistDn,'cucsEtherFcoeInterfaceStatsHistRn':cucsEtherFcoeInterfaceStatsHistRn,'cucsEtherFcoeInterfaceStatsHistBytesRx':cucsEtherFcoeInterfaceStatsHistBytesRx,'cucsEtherFcoeInterfaceStatsHistBytesRxDelta':cucsEtherFcoeInterfaceStatsHistBytesRxDelta,'cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg':cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax':cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax,'cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin':cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin,'cucsEtherFcoeInterfaceStatsHistBytesTx':cucsEtherFcoeInterfaceStatsHistBytesTx,'cucsEtherFcoeInterfaceStatsHistBytesTxDelta':cucsEtherFcoeInterfaceStatsHistBytesTxDelta,'cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg':cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax':cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax,'cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin':cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin,'cucsEtherFcoeInterfaceStatsHistDroppedRx':cucsEtherFcoeInterfaceStatsHistDroppedRx,'cucsEtherFcoeInterfaceStatsHistDroppedRxDelta':cucsEtherFcoeInterfaceStatsHistDroppedRxDelta,'cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg':cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax':cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax,'cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin':cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin,'cucsEtherFcoeInterfaceStatsHistDroppedTx':cucsEtherFcoeInterfaceStatsHistDroppedTx,'cucsEtherFcoeInterfaceStatsHistDroppedTxDelta':cucsEtherFcoeInterfaceStatsHistDroppedTxDelta,'cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg':cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax':cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax,'cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin':cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin,'cucsEtherFcoeInterfaceStatsHistErrorsRx':cucsEtherFcoeInterfaceStatsHistErrorsRx,'cucsEtherFcoeInterfaceStatsHistErrorsRxDelta':cucsEtherFcoeInterfaceStatsHistErrorsRxDelta,'cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg':cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax':cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax,'cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin':cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin,'cucsEtherFcoeInterfaceStatsHistErrorsTx':cucsEtherFcoeInterfaceStatsHistErrorsTx,'cucsEtherFcoeInterfaceStatsHistErrorsTxDelta':cucsEtherFcoeInterfaceStatsHistErrorsTxDelta,'cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg':cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax':cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax,'cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin':cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin,'cucsEtherFcoeInterfaceStatsHistId':cucsEtherFcoeInterfaceStatsHistId,'cucsEtherFcoeInterfaceStatsHistMostRecent':cucsEtherFcoeInterfaceStatsHistMostRecent,'cucsEtherFcoeInterfaceStatsHistPacketsRx':cucsEtherFcoeInterfaceStatsHistPacketsRx,'cucsEtherFcoeInterfaceStatsHistPacketsRxDelta':cucsEtherFcoeInterfaceStatsHistPacketsRxDelta,'cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg':cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax':cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax,'cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin':cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin,'cucsEtherFcoeInterfaceStatsHistPacketsTx':cucsEtherFcoeInterfaceStatsHistPacketsTx,'cucsEtherFcoeInterfaceStatsHistPacketsTxDelta':cucsEtherFcoeInterfaceStatsHistPacketsTxDelta,'cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg':cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg,'cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax':cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax,'cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin':cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin,'cucsEtherFcoeInterfaceStatsHistSuspect':cucsEtherFcoeInterfaceStatsHistSuspect,'cucsEtherFcoeInterfaceStatsHistThresholded':cucsEtherFcoeInterfaceStatsHistThresholded,'cucsEtherFcoeInterfaceStatsHistTimeCollected':cucsEtherFcoeInterfaceStatsHistTimeCollected,'cucsEtherPIoEndPointTable':cucsEtherPIoEndPointTable,'cucsEtherPIoEndPointEntry':cucsEtherPIoEndPointEntry,_c:cucsEtherPIoEndPointInstanceId,'cucsEtherPIoEndPointDn':cucsEtherPIoEndPointDn,'cucsEtherPIoEndPointRn':cucsEtherPIoEndPointRn,'cucsEtherPIoEndPointEndPointDn':cucsEtherPIoEndPointEndPointDn,'cucsEtherPIoEndPointEpCloudType':cucsEtherPIoEndPointEpCloudType,'cucsEtherPIoEndPointUsrLbl':cucsEtherPIoEndPointUsrLbl,'cucsEtherPIoFsmTable':cucsEtherPIoFsmTable,'cucsEtherPIoFsmEntry':cucsEtherPIoFsmEntry,_d:cucsEtherPIoFsmInstanceId,'cucsEtherPIoFsmDn':cucsEtherPIoFsmDn,'cucsEtherPIoFsmRn':cucsEtherPIoFsmRn,'cucsEtherPIoFsmCompletionTime':cucsEtherPIoFsmCompletionTime,'cucsEtherPIoFsmCurrentFsm':cucsEtherPIoFsmCurrentFsm,'cucsEtherPIoFsmDescrData':cucsEtherPIoFsmDescrData,'cucsEtherPIoFsmFsmStatus':cucsEtherPIoFsmFsmStatus,'cucsEtherPIoFsmProgress':cucsEtherPIoFsmProgress,'cucsEtherPIoFsmRmtErrCode':cucsEtherPIoFsmRmtErrCode,'cucsEtherPIoFsmRmtErrDescr':cucsEtherPIoFsmRmtErrDescr,'cucsEtherPIoFsmRmtRslt':cucsEtherPIoFsmRmtRslt,'cucsEtherPIoFsmStageTable':cucsEtherPIoFsmStageTable,'cucsEtherPIoFsmStageEntry':cucsEtherPIoFsmStageEntry,_e:cucsEtherPIoFsmStageInstanceId,'cucsEtherPIoFsmStageDn':cucsEtherPIoFsmStageDn,'cucsEtherPIoFsmStageRn':cucsEtherPIoFsmStageRn,'cucsEtherPIoFsmStageDescrData':cucsEtherPIoFsmStageDescrData,'cucsEtherPIoFsmStageLastUpdateTime':cucsEtherPIoFsmStageLastUpdateTime,'cucsEtherPIoFsmStageName':cucsEtherPIoFsmStageName,'cucsEtherPIoFsmStageOrder':cucsEtherPIoFsmStageOrder,'cucsEtherPIoFsmStageRetry':cucsEtherPIoFsmStageRetry,'cucsEtherPIoFsmStageStageStatus':cucsEtherPIoFsmStageStageStatus,'cucsEtherServerIntFIoFsmTable':cucsEtherServerIntFIoFsmTable,'cucsEtherServerIntFIoFsmEntry':cucsEtherServerIntFIoFsmEntry,_f:cucsEtherServerIntFIoFsmInstanceId,'cucsEtherServerIntFIoFsmDn':cucsEtherServerIntFIoFsmDn,'cucsEtherServerIntFIoFsmRn':cucsEtherServerIntFIoFsmRn,'cucsEtherServerIntFIoFsmCompletionTime':cucsEtherServerIntFIoFsmCompletionTime,'cucsEtherServerIntFIoFsmCurrentFsm':cucsEtherServerIntFIoFsmCurrentFsm,'cucsEtherServerIntFIoFsmDescrData':cucsEtherServerIntFIoFsmDescrData,'cucsEtherServerIntFIoFsmFsmStatus':cucsEtherServerIntFIoFsmFsmStatus,'cucsEtherServerIntFIoFsmProgress':cucsEtherServerIntFIoFsmProgress,'cucsEtherServerIntFIoFsmRmtErrCode':cucsEtherServerIntFIoFsmRmtErrCode,'cucsEtherServerIntFIoFsmRmtErrDescr':cucsEtherServerIntFIoFsmRmtErrDescr,'cucsEtherServerIntFIoFsmRmtRslt':cucsEtherServerIntFIoFsmRmtRslt,'cucsEtherServerIntFIoFsmStageTable':cucsEtherServerIntFIoFsmStageTable,'cucsEtherServerIntFIoFsmStageEntry':cucsEtherServerIntFIoFsmStageEntry,_g:cucsEtherServerIntFIoFsmStageInstanceId,'cucsEtherServerIntFIoFsmStageDn':cucsEtherServerIntFIoFsmStageDn,'cucsEtherServerIntFIoFsmStageRn':cucsEtherServerIntFIoFsmStageRn,'cucsEtherServerIntFIoFsmStageDescrData':cucsEtherServerIntFIoFsmStageDescrData,'cucsEtherServerIntFIoFsmStageLastUpdateTime':cucsEtherServerIntFIoFsmStageLastUpdateTime,'cucsEtherServerIntFIoFsmStageName':cucsEtherServerIntFIoFsmStageName,'cucsEtherServerIntFIoFsmStageOrder':cucsEtherServerIntFIoFsmStageOrder,'cucsEtherServerIntFIoFsmStageRetry':cucsEtherServerIntFIoFsmStageRetry,'cucsEtherServerIntFIoFsmStageStageStatus':cucsEtherServerIntFIoFsmStageStageStatus,'cucsEtherNiErrStatsTable':cucsEtherNiErrStatsTable,'cucsEtherNiErrStatsEntry':cucsEtherNiErrStatsEntry,_h:cucsEtherNiErrStatsInstanceId,'cucsEtherNiErrStatsDn':cucsEtherNiErrStatsDn,'cucsEtherNiErrStatsRn':cucsEtherNiErrStatsRn,'cucsEtherNiErrStatsCrc':cucsEtherNiErrStatsCrc,'cucsEtherNiErrStatsCrcDelta':cucsEtherNiErrStatsCrcDelta,'cucsEtherNiErrStatsCrcDeltaAvg':cucsEtherNiErrStatsCrcDeltaAvg,'cucsEtherNiErrStatsCrcDeltaMax':cucsEtherNiErrStatsCrcDeltaMax,'cucsEtherNiErrStatsCrcDeltaMin':cucsEtherNiErrStatsCrcDeltaMin,'cucsEtherNiErrStatsFrameTx':cucsEtherNiErrStatsFrameTx,'cucsEtherNiErrStatsFrameTxDelta':cucsEtherNiErrStatsFrameTxDelta,'cucsEtherNiErrStatsFrameTxDeltaAvg':cucsEtherNiErrStatsFrameTxDeltaAvg,'cucsEtherNiErrStatsFrameTxDeltaMax':cucsEtherNiErrStatsFrameTxDeltaMax,'cucsEtherNiErrStatsFrameTxDeltaMin':cucsEtherNiErrStatsFrameTxDeltaMin,'cucsEtherNiErrStatsInRange':cucsEtherNiErrStatsInRange,'cucsEtherNiErrStatsInRangeDelta':cucsEtherNiErrStatsInRangeDelta,'cucsEtherNiErrStatsInRangeDeltaAvg':cucsEtherNiErrStatsInRangeDeltaAvg,'cucsEtherNiErrStatsInRangeDeltaMax':cucsEtherNiErrStatsInRangeDeltaMax,'cucsEtherNiErrStatsInRangeDeltaMin':cucsEtherNiErrStatsInRangeDeltaMin,'cucsEtherNiErrStatsIntervals':cucsEtherNiErrStatsIntervals,'cucsEtherNiErrStatsSuspect':cucsEtherNiErrStatsSuspect,'cucsEtherNiErrStatsThresholded':cucsEtherNiErrStatsThresholded,'cucsEtherNiErrStatsTimeCollected':cucsEtherNiErrStatsTimeCollected,'cucsEtherNiErrStatsTooLong':cucsEtherNiErrStatsTooLong,'cucsEtherNiErrStatsTooLongDelta':cucsEtherNiErrStatsTooLongDelta,'cucsEtherNiErrStatsTooLongDeltaAvg':cucsEtherNiErrStatsTooLongDeltaAvg,'cucsEtherNiErrStatsTooLongDeltaMax':cucsEtherNiErrStatsTooLongDeltaMax,'cucsEtherNiErrStatsTooLongDeltaMin':cucsEtherNiErrStatsTooLongDeltaMin,'cucsEtherNiErrStatsTooShort':cucsEtherNiErrStatsTooShort,'cucsEtherNiErrStatsTooShortDelta':cucsEtherNiErrStatsTooShortDelta,'cucsEtherNiErrStatsTooShortDeltaAvg':cucsEtherNiErrStatsTooShortDeltaAvg,'cucsEtherNiErrStatsTooShortDeltaMax':cucsEtherNiErrStatsTooShortDeltaMax,'cucsEtherNiErrStatsTooShortDeltaMin':cucsEtherNiErrStatsTooShortDeltaMin,'cucsEtherNiErrStatsUpdate':cucsEtherNiErrStatsUpdate,'cucsEtherNiErrStatsHistTable':cucsEtherNiErrStatsHistTable,'cucsEtherNiErrStatsHistEntry':cucsEtherNiErrStatsHistEntry,_i:cucsEtherNiErrStatsHistInstanceId,'cucsEtherNiErrStatsHistDn':cucsEtherNiErrStatsHistDn,'cucsEtherNiErrStatsHistRn':cucsEtherNiErrStatsHistRn,'cucsEtherNiErrStatsHistCrc':cucsEtherNiErrStatsHistCrc,'cucsEtherNiErrStatsHistCrcDelta':cucsEtherNiErrStatsHistCrcDelta,'cucsEtherNiErrStatsHistCrcDeltaAvg':cucsEtherNiErrStatsHistCrcDeltaAvg,'cucsEtherNiErrStatsHistCrcDeltaMax':cucsEtherNiErrStatsHistCrcDeltaMax,'cucsEtherNiErrStatsHistCrcDeltaMin':cucsEtherNiErrStatsHistCrcDeltaMin,'cucsEtherNiErrStatsHistFrameTx':cucsEtherNiErrStatsHistFrameTx,'cucsEtherNiErrStatsHistFrameTxDelta':cucsEtherNiErrStatsHistFrameTxDelta,'cucsEtherNiErrStatsHistFrameTxDeltaAvg':cucsEtherNiErrStatsHistFrameTxDeltaAvg,'cucsEtherNiErrStatsHistFrameTxDeltaMax':cucsEtherNiErrStatsHistFrameTxDeltaMax,'cucsEtherNiErrStatsHistFrameTxDeltaMin':cucsEtherNiErrStatsHistFrameTxDeltaMin,'cucsEtherNiErrStatsHistId':cucsEtherNiErrStatsHistId,'cucsEtherNiErrStatsHistInRange':cucsEtherNiErrStatsHistInRange,'cucsEtherNiErrStatsHistInRangeDelta':cucsEtherNiErrStatsHistInRangeDelta,'cucsEtherNiErrStatsHistInRangeDeltaAvg':cucsEtherNiErrStatsHistInRangeDeltaAvg,'cucsEtherNiErrStatsHistInRangeDeltaMax':cucsEtherNiErrStatsHistInRangeDeltaMax,'cucsEtherNiErrStatsHistInRangeDeltaMin':cucsEtherNiErrStatsHistInRangeDeltaMin,'cucsEtherNiErrStatsHistMostRecent':cucsEtherNiErrStatsHistMostRecent,'cucsEtherNiErrStatsHistSuspect':cucsEtherNiErrStatsHistSuspect,'cucsEtherNiErrStatsHistThresholded':cucsEtherNiErrStatsHistThresholded,'cucsEtherNiErrStatsHistTimeCollected':cucsEtherNiErrStatsHistTimeCollected,'cucsEtherNiErrStatsHistTooLong':cucsEtherNiErrStatsHistTooLong,'cucsEtherNiErrStatsHistTooLongDelta':cucsEtherNiErrStatsHistTooLongDelta,'cucsEtherNiErrStatsHistTooLongDeltaAvg':cucsEtherNiErrStatsHistTooLongDeltaAvg,'cucsEtherNiErrStatsHistTooLongDeltaMax':cucsEtherNiErrStatsHistTooLongDeltaMax,'cucsEtherNiErrStatsHistTooLongDeltaMin':cucsEtherNiErrStatsHistTooLongDeltaMin,'cucsEtherNiErrStatsHistTooShort':cucsEtherNiErrStatsHistTooShort,'cucsEtherNiErrStatsHistTooShortDelta':cucsEtherNiErrStatsHistTooShortDelta,'cucsEtherNiErrStatsHistTooShortDeltaAvg':cucsEtherNiErrStatsHistTooShortDeltaAvg,'cucsEtherNiErrStatsHistTooShortDeltaMax':cucsEtherNiErrStatsHistTooShortDeltaMax,'cucsEtherNiErrStatsHistTooShortDeltaMin':cucsEtherNiErrStatsHistTooShortDeltaMin})