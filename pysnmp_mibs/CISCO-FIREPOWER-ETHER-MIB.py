_n='cfprEtherFtwPortPairFsmTaskInstanceId'
_m='cfprEtherFtwPortPairFsmStageInstanceId'
_l='cfprEtherFtwPortPairFsmInstanceId'
_k='cfprEtherFtwPortPairInstanceId'
_j='cfprEtherFailToWireInstanceId'
_i='cfprEtherTxStatsHistInstanceId'
_h='cfprEtherTxStatsInstanceId'
_g='cfprEtherSwitchIntFIoPcEpInstanceId'
_f='cfprEtherSwitchIntFIoPcInstanceId'
_e='cfprEtherSwitchIntFIoInstanceId'
_d='cfprEtherSwIfConfigInstanceId'
_c='cfprEtherServerIntFIoPcEpInstanceId'
_b='cfprEtherServerIntFIoPcInstanceId'
_a='cfprEtherServerIntFIoFsmTaskInstanceId'
_Z='cfprEtherServerIntFIoFsmStageInstanceId'
_Y='cfprEtherServerIntFIoFsmInstanceId'
_X='cfprEtherServerIntFIoInstanceId'
_W='cfprEtherRxStatsHistInstanceId'
_V='cfprEtherRxStatsInstanceId'
_U='cfprEtherPortChanIdUniverseInstanceId'
_T='cfprEtherPortChanIdElemInstanceId'
_S='cfprEtherPauseStatsHistInstanceId'
_R='cfprEtherPauseStatsInstanceId'
_Q='cfprEtherPIoFsmStageInstanceId'
_P='cfprEtherPIoFsmInstanceId'
_O='cfprEtherPIoEndPointInstanceId'
_N='cfprEtherPIoInstanceId'
_M='cfprEtherNicIfConfigInstanceId'
_L='cfprEtherNiErrStatsHistInstanceId'
_K='cfprEtherNiErrStatsInstanceId'
_J='cfprEtherLossStatsHistInstanceId'
_I='cfprEtherLossStatsInstanceId'
_H='cfprEtherFcoeInterfaceStatsHistInstanceId'
_G='cfprEtherFcoeInterfaceStatsInstanceId'
_F='cfprEtherErrStatsHistInstanceId'
_E='cfprEtherErrStatsInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-ETHER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprEquipmentChassisConfigState,CfprEquipmentXcvrType,CfprEtherCIoEpIfType,CfprEtherCloudType,CfprEtherErrStatsHistThresholded,CfprEtherErrStatsThresholded,CfprEtherExternalEpAdminState,CfprEtherExternalEpLocale,CfprEtherExternalPcAdminState,CfprEtherExternalPcLocale,CfprEtherFcoeInterfaceStatsHistThresholded,CfprEtherFcoeInterfaceStatsThresholded,CfprEtherFtwOperMode,CfprEtherFtwPortPairFsmCurrentFsm,CfprEtherFtwPortPairFsmStageName,CfprEtherFtwPortPairFsmTaskItem,CfprEtherFtwPortPairMode,CfprEtherFtwPortPairWdtState,CfprEtherIntFIoEpType,CfprEtherInternalPcLocale,CfprEtherLossStatsHistThresholded,CfprEtherLossStatsThresholded,CfprEtherNiErrStatsHistThresholded,CfprEtherNiErrStatsThresholded,CfprEtherPIoEpIfType,CfprEtherPIoFsmCurrentFsm,CfprEtherPIoFsmStageName,CfprEtherPauseStatsHistThresholded,CfprEtherPauseStatsThresholded,CfprEtherRxStatsHistThresholded,CfprEtherRxStatsThresholded,CfprEtherSatelliteConnectionDisc,CfprEtherServerIntFIoAdminState,CfprEtherServerIntFIoFsmCurrentFsm,CfprEtherServerIntFIoFsmStageName,CfprEtherServerIntFIoFsmTaskItem,CfprEtherServerIntFIoIfRole,CfprEtherServerIntFIoLocale,CfprEtherServerIntFIoPcEpIfRole,CfprEtherServerIntFIoPcEpPortId,CfprEtherServerIntFIoPcIfRole,CfprEtherServerIntFIoPcPortId,CfprEtherServerIntFIoPcTransport,CfprEtherServerIntFIoPcType,CfprEtherServerIntFIoTransport,CfprEtherServerIntFIoType,CfprEtherSwitchIntFIoAck,CfprEtherSwitchIntFIoIfRole,CfprEtherSwitchIntFIoLocale,CfprEtherSwitchIntFIoPcEpIfRole,CfprEtherSwitchIntFIoPcEpPortId,CfprEtherSwitchIntFIoPcIfRole,CfprEtherSwitchIntFIoPcPortId,CfprEtherSwitchIntFIoPcTransport,CfprEtherSwitchIntFIoPcType,CfprEtherSwitchIntFIoTransport,CfprEtherSwitchIntFIoType,CfprEtherTxStatsHistThresholded,CfprEtherTxStatsThresholded,CfprFabricAdminState,CfprFabricMembershipStatus,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprFsmLifecycle,CfprLicenseState,CfprNetworkConnectionType,CfprNetworkLocale,CfprNetworkPhysEpIfType,CfprNetworkPortOperState,CfprNetworkPortRole,CfprNetworkSwitchId,CfprNetworkTransport,CfprPortDuplex,CfprPortEncap,CfprPortEthSpeed,CfprPortMode=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprEquipmentChassisConfigState','CfprEquipmentXcvrType','CfprEtherCIoEpIfType','CfprEtherCloudType','CfprEtherErrStatsHistThresholded','CfprEtherErrStatsThresholded','CfprEtherExternalEpAdminState','CfprEtherExternalEpLocale','CfprEtherExternalPcAdminState','CfprEtherExternalPcLocale','CfprEtherFcoeInterfaceStatsHistThresholded','CfprEtherFcoeInterfaceStatsThresholded','CfprEtherFtwOperMode','CfprEtherFtwPortPairFsmCurrentFsm','CfprEtherFtwPortPairFsmStageName','CfprEtherFtwPortPairFsmTaskItem','CfprEtherFtwPortPairMode','CfprEtherFtwPortPairWdtState','CfprEtherIntFIoEpType','CfprEtherInternalPcLocale','CfprEtherLossStatsHistThresholded','CfprEtherLossStatsThresholded','CfprEtherNiErrStatsHistThresholded','CfprEtherNiErrStatsThresholded','CfprEtherPIoEpIfType','CfprEtherPIoFsmCurrentFsm','CfprEtherPIoFsmStageName','CfprEtherPauseStatsHistThresholded','CfprEtherPauseStatsThresholded','CfprEtherRxStatsHistThresholded','CfprEtherRxStatsThresholded','CfprEtherSatelliteConnectionDisc','CfprEtherServerIntFIoAdminState','CfprEtherServerIntFIoFsmCurrentFsm','CfprEtherServerIntFIoFsmStageName','CfprEtherServerIntFIoFsmTaskItem','CfprEtherServerIntFIoIfRole','CfprEtherServerIntFIoLocale','CfprEtherServerIntFIoPcEpIfRole','CfprEtherServerIntFIoPcEpPortId','CfprEtherServerIntFIoPcIfRole','CfprEtherServerIntFIoPcPortId','CfprEtherServerIntFIoPcTransport','CfprEtherServerIntFIoPcType','CfprEtherServerIntFIoTransport','CfprEtherServerIntFIoType','CfprEtherSwitchIntFIoAck','CfprEtherSwitchIntFIoIfRole','CfprEtherSwitchIntFIoLocale','CfprEtherSwitchIntFIoPcEpIfRole','CfprEtherSwitchIntFIoPcEpPortId','CfprEtherSwitchIntFIoPcIfRole','CfprEtherSwitchIntFIoPcPortId','CfprEtherSwitchIntFIoPcTransport','CfprEtherSwitchIntFIoPcType','CfprEtherSwitchIntFIoTransport','CfprEtherSwitchIntFIoType','CfprEtherTxStatsHistThresholded','CfprEtherTxStatsThresholded','CfprFabricAdminState','CfprFabricMembershipStatus','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprFsmLifecycle','CfprLicenseState','CfprNetworkConnectionType','CfprNetworkLocale','CfprNetworkPhysEpIfType','CfprNetworkPortOperState','CfprNetworkPortRole','CfprNetworkSwitchId','CfprNetworkTransport','CfprPortDuplex','CfprPortEncap','CfprPortEthSpeed','CfprPortMode')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprEtherObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,21))
_CfprEtherErrStatsTable_Object=MibTable
cfprEtherErrStatsTable=_CfprEtherErrStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,1))
if mibBuilder.loadTexts:cfprEtherErrStatsTable.setStatus(_A)
_CfprEtherErrStatsEntry_Object=MibTableRow
cfprEtherErrStatsEntry=_CfprEtherErrStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,1,1))
cfprEtherErrStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprEtherErrStatsEntry.setStatus(_A)
_CfprEtherErrStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherErrStatsInstanceId_Object=MibTableColumn
cfprEtherErrStatsInstanceId=_CfprEtherErrStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,1),_CfprEtherErrStatsInstanceId_Type())
cfprEtherErrStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherErrStatsInstanceId.setStatus(_A)
_CfprEtherErrStatsDn_Type=CfprManagedObjectDn
_CfprEtherErrStatsDn_Object=MibTableColumn
cfprEtherErrStatsDn=_CfprEtherErrStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,2),_CfprEtherErrStatsDn_Type())
cfprEtherErrStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsDn.setStatus(_A)
_CfprEtherErrStatsRn_Type=SnmpAdminString
_CfprEtherErrStatsRn_Object=MibTableColumn
cfprEtherErrStatsRn=_CfprEtherErrStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,3),_CfprEtherErrStatsRn_Type())
cfprEtherErrStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsRn.setStatus(_A)
_CfprEtherErrStatsAlign_Type=Unsigned64
_CfprEtherErrStatsAlign_Object=MibTableColumn
cfprEtherErrStatsAlign=_CfprEtherErrStatsAlign_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,4),_CfprEtherErrStatsAlign_Type())
cfprEtherErrStatsAlign.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsAlign.setStatus(_A)
_CfprEtherErrStatsAlignDelta_Type=Counter64
_CfprEtherErrStatsAlignDelta_Object=MibTableColumn
cfprEtherErrStatsAlignDelta=_CfprEtherErrStatsAlignDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,5),_CfprEtherErrStatsAlignDelta_Type())
cfprEtherErrStatsAlignDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsAlignDelta.setStatus(_A)
_CfprEtherErrStatsAlignDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsAlignDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsAlignDeltaAvg=_CfprEtherErrStatsAlignDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,6),_CfprEtherErrStatsAlignDeltaAvg_Type())
cfprEtherErrStatsAlignDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsAlignDeltaAvg.setStatus(_A)
_CfprEtherErrStatsAlignDeltaMax_Type=Unsigned64
_CfprEtherErrStatsAlignDeltaMax_Object=MibTableColumn
cfprEtherErrStatsAlignDeltaMax=_CfprEtherErrStatsAlignDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,7),_CfprEtherErrStatsAlignDeltaMax_Type())
cfprEtherErrStatsAlignDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsAlignDeltaMax.setStatus(_A)
_CfprEtherErrStatsAlignDeltaMin_Type=Unsigned64
_CfprEtherErrStatsAlignDeltaMin_Object=MibTableColumn
cfprEtherErrStatsAlignDeltaMin=_CfprEtherErrStatsAlignDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,8),_CfprEtherErrStatsAlignDeltaMin_Type())
cfprEtherErrStatsAlignDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsAlignDeltaMin.setStatus(_A)
_CfprEtherErrStatsDeferredTx_Type=Unsigned64
_CfprEtherErrStatsDeferredTx_Object=MibTableColumn
cfprEtherErrStatsDeferredTx=_CfprEtherErrStatsDeferredTx_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,9),_CfprEtherErrStatsDeferredTx_Type())
cfprEtherErrStatsDeferredTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsDeferredTx.setStatus(_A)
_CfprEtherErrStatsDeferredTxDelta_Type=Counter64
_CfprEtherErrStatsDeferredTxDelta_Object=MibTableColumn
cfprEtherErrStatsDeferredTxDelta=_CfprEtherErrStatsDeferredTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,10),_CfprEtherErrStatsDeferredTxDelta_Type())
cfprEtherErrStatsDeferredTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsDeferredTxDelta.setStatus(_A)
_CfprEtherErrStatsDeferredTxDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsDeferredTxDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsDeferredTxDeltaAvg=_CfprEtherErrStatsDeferredTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,11),_CfprEtherErrStatsDeferredTxDeltaAvg_Type())
cfprEtherErrStatsDeferredTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsDeferredTxDeltaAvg.setStatus(_A)
_CfprEtherErrStatsDeferredTxDeltaMax_Type=Unsigned64
_CfprEtherErrStatsDeferredTxDeltaMax_Object=MibTableColumn
cfprEtherErrStatsDeferredTxDeltaMax=_CfprEtherErrStatsDeferredTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,12),_CfprEtherErrStatsDeferredTxDeltaMax_Type())
cfprEtherErrStatsDeferredTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsDeferredTxDeltaMax.setStatus(_A)
_CfprEtherErrStatsDeferredTxDeltaMin_Type=Unsigned64
_CfprEtherErrStatsDeferredTxDeltaMin_Object=MibTableColumn
cfprEtherErrStatsDeferredTxDeltaMin=_CfprEtherErrStatsDeferredTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,13),_CfprEtherErrStatsDeferredTxDeltaMin_Type())
cfprEtherErrStatsDeferredTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsDeferredTxDeltaMin.setStatus(_A)
_CfprEtherErrStatsFcs_Type=Unsigned64
_CfprEtherErrStatsFcs_Object=MibTableColumn
cfprEtherErrStatsFcs=_CfprEtherErrStatsFcs_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,14),_CfprEtherErrStatsFcs_Type())
cfprEtherErrStatsFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsFcs.setStatus(_A)
_CfprEtherErrStatsFcsDelta_Type=Counter64
_CfprEtherErrStatsFcsDelta_Object=MibTableColumn
cfprEtherErrStatsFcsDelta=_CfprEtherErrStatsFcsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,15),_CfprEtherErrStatsFcsDelta_Type())
cfprEtherErrStatsFcsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsFcsDelta.setStatus(_A)
_CfprEtherErrStatsFcsDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsFcsDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsFcsDeltaAvg=_CfprEtherErrStatsFcsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,16),_CfprEtherErrStatsFcsDeltaAvg_Type())
cfprEtherErrStatsFcsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsFcsDeltaAvg.setStatus(_A)
_CfprEtherErrStatsFcsDeltaMax_Type=Unsigned64
_CfprEtherErrStatsFcsDeltaMax_Object=MibTableColumn
cfprEtherErrStatsFcsDeltaMax=_CfprEtherErrStatsFcsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,17),_CfprEtherErrStatsFcsDeltaMax_Type())
cfprEtherErrStatsFcsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsFcsDeltaMax.setStatus(_A)
_CfprEtherErrStatsFcsDeltaMin_Type=Unsigned64
_CfprEtherErrStatsFcsDeltaMin_Object=MibTableColumn
cfprEtherErrStatsFcsDeltaMin=_CfprEtherErrStatsFcsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,18),_CfprEtherErrStatsFcsDeltaMin_Type())
cfprEtherErrStatsFcsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsFcsDeltaMin.setStatus(_A)
_CfprEtherErrStatsIntMacRx_Type=Unsigned64
_CfprEtherErrStatsIntMacRx_Object=MibTableColumn
cfprEtherErrStatsIntMacRx=_CfprEtherErrStatsIntMacRx_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,19),_CfprEtherErrStatsIntMacRx_Type())
cfprEtherErrStatsIntMacRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacRx.setStatus(_A)
_CfprEtherErrStatsIntMacRxDelta_Type=Counter64
_CfprEtherErrStatsIntMacRxDelta_Object=MibTableColumn
cfprEtherErrStatsIntMacRxDelta=_CfprEtherErrStatsIntMacRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,20),_CfprEtherErrStatsIntMacRxDelta_Type())
cfprEtherErrStatsIntMacRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacRxDelta.setStatus(_A)
_CfprEtherErrStatsIntMacRxDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsIntMacRxDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsIntMacRxDeltaAvg=_CfprEtherErrStatsIntMacRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,21),_CfprEtherErrStatsIntMacRxDeltaAvg_Type())
cfprEtherErrStatsIntMacRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacRxDeltaAvg.setStatus(_A)
_CfprEtherErrStatsIntMacRxDeltaMax_Type=Unsigned64
_CfprEtherErrStatsIntMacRxDeltaMax_Object=MibTableColumn
cfprEtherErrStatsIntMacRxDeltaMax=_CfprEtherErrStatsIntMacRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,22),_CfprEtherErrStatsIntMacRxDeltaMax_Type())
cfprEtherErrStatsIntMacRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacRxDeltaMax.setStatus(_A)
_CfprEtherErrStatsIntMacRxDeltaMin_Type=Unsigned64
_CfprEtherErrStatsIntMacRxDeltaMin_Object=MibTableColumn
cfprEtherErrStatsIntMacRxDeltaMin=_CfprEtherErrStatsIntMacRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,23),_CfprEtherErrStatsIntMacRxDeltaMin_Type())
cfprEtherErrStatsIntMacRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacRxDeltaMin.setStatus(_A)
_CfprEtherErrStatsIntMacTx_Type=Unsigned64
_CfprEtherErrStatsIntMacTx_Object=MibTableColumn
cfprEtherErrStatsIntMacTx=_CfprEtherErrStatsIntMacTx_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,24),_CfprEtherErrStatsIntMacTx_Type())
cfprEtherErrStatsIntMacTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacTx.setStatus(_A)
_CfprEtherErrStatsIntMacTxDelta_Type=Counter64
_CfprEtherErrStatsIntMacTxDelta_Object=MibTableColumn
cfprEtherErrStatsIntMacTxDelta=_CfprEtherErrStatsIntMacTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,25),_CfprEtherErrStatsIntMacTxDelta_Type())
cfprEtherErrStatsIntMacTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacTxDelta.setStatus(_A)
_CfprEtherErrStatsIntMacTxDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsIntMacTxDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsIntMacTxDeltaAvg=_CfprEtherErrStatsIntMacTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,26),_CfprEtherErrStatsIntMacTxDeltaAvg_Type())
cfprEtherErrStatsIntMacTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacTxDeltaAvg.setStatus(_A)
_CfprEtherErrStatsIntMacTxDeltaMax_Type=Unsigned64
_CfprEtherErrStatsIntMacTxDeltaMax_Object=MibTableColumn
cfprEtherErrStatsIntMacTxDeltaMax=_CfprEtherErrStatsIntMacTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,27),_CfprEtherErrStatsIntMacTxDeltaMax_Type())
cfprEtherErrStatsIntMacTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacTxDeltaMax.setStatus(_A)
_CfprEtherErrStatsIntMacTxDeltaMin_Type=Unsigned64
_CfprEtherErrStatsIntMacTxDeltaMin_Object=MibTableColumn
cfprEtherErrStatsIntMacTxDeltaMin=_CfprEtherErrStatsIntMacTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,28),_CfprEtherErrStatsIntMacTxDeltaMin_Type())
cfprEtherErrStatsIntMacTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntMacTxDeltaMin.setStatus(_A)
_CfprEtherErrStatsIntervals_Type=Gauge32
_CfprEtherErrStatsIntervals_Object=MibTableColumn
cfprEtherErrStatsIntervals=_CfprEtherErrStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,29),_CfprEtherErrStatsIntervals_Type())
cfprEtherErrStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsIntervals.setStatus(_A)
_CfprEtherErrStatsOutDiscard_Type=Unsigned64
_CfprEtherErrStatsOutDiscard_Object=MibTableColumn
cfprEtherErrStatsOutDiscard=_CfprEtherErrStatsOutDiscard_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,30),_CfprEtherErrStatsOutDiscard_Type())
cfprEtherErrStatsOutDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsOutDiscard.setStatus(_A)
_CfprEtherErrStatsOutDiscardDelta_Type=Counter64
_CfprEtherErrStatsOutDiscardDelta_Object=MibTableColumn
cfprEtherErrStatsOutDiscardDelta=_CfprEtherErrStatsOutDiscardDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,31),_CfprEtherErrStatsOutDiscardDelta_Type())
cfprEtherErrStatsOutDiscardDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsOutDiscardDelta.setStatus(_A)
_CfprEtherErrStatsOutDiscardDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsOutDiscardDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsOutDiscardDeltaAvg=_CfprEtherErrStatsOutDiscardDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,32),_CfprEtherErrStatsOutDiscardDeltaAvg_Type())
cfprEtherErrStatsOutDiscardDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsOutDiscardDeltaAvg.setStatus(_A)
_CfprEtherErrStatsOutDiscardDeltaMax_Type=Unsigned64
_CfprEtherErrStatsOutDiscardDeltaMax_Object=MibTableColumn
cfprEtherErrStatsOutDiscardDeltaMax=_CfprEtherErrStatsOutDiscardDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,33),_CfprEtherErrStatsOutDiscardDeltaMax_Type())
cfprEtherErrStatsOutDiscardDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsOutDiscardDeltaMax.setStatus(_A)
_CfprEtherErrStatsOutDiscardDeltaMin_Type=Unsigned64
_CfprEtherErrStatsOutDiscardDeltaMin_Object=MibTableColumn
cfprEtherErrStatsOutDiscardDeltaMin=_CfprEtherErrStatsOutDiscardDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,34),_CfprEtherErrStatsOutDiscardDeltaMin_Type())
cfprEtherErrStatsOutDiscardDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsOutDiscardDeltaMin.setStatus(_A)
_CfprEtherErrStatsRcv_Type=Unsigned64
_CfprEtherErrStatsRcv_Object=MibTableColumn
cfprEtherErrStatsRcv=_CfprEtherErrStatsRcv_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,35),_CfprEtherErrStatsRcv_Type())
cfprEtherErrStatsRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsRcv.setStatus(_A)
_CfprEtherErrStatsRcvDelta_Type=Counter64
_CfprEtherErrStatsRcvDelta_Object=MibTableColumn
cfprEtherErrStatsRcvDelta=_CfprEtherErrStatsRcvDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,36),_CfprEtherErrStatsRcvDelta_Type())
cfprEtherErrStatsRcvDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsRcvDelta.setStatus(_A)
_CfprEtherErrStatsRcvDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsRcvDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsRcvDeltaAvg=_CfprEtherErrStatsRcvDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,37),_CfprEtherErrStatsRcvDeltaAvg_Type())
cfprEtherErrStatsRcvDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsRcvDeltaAvg.setStatus(_A)
_CfprEtherErrStatsRcvDeltaMax_Type=Unsigned64
_CfprEtherErrStatsRcvDeltaMax_Object=MibTableColumn
cfprEtherErrStatsRcvDeltaMax=_CfprEtherErrStatsRcvDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,38),_CfprEtherErrStatsRcvDeltaMax_Type())
cfprEtherErrStatsRcvDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsRcvDeltaMax.setStatus(_A)
_CfprEtherErrStatsRcvDeltaMin_Type=Unsigned64
_CfprEtherErrStatsRcvDeltaMin_Object=MibTableColumn
cfprEtherErrStatsRcvDeltaMin=_CfprEtherErrStatsRcvDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,39),_CfprEtherErrStatsRcvDeltaMin_Type())
cfprEtherErrStatsRcvDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsRcvDeltaMin.setStatus(_A)
_CfprEtherErrStatsSuspect_Type=TruthValue
_CfprEtherErrStatsSuspect_Object=MibTableColumn
cfprEtherErrStatsSuspect=_CfprEtherErrStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,40),_CfprEtherErrStatsSuspect_Type())
cfprEtherErrStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsSuspect.setStatus(_A)
_CfprEtherErrStatsThresholded_Type=CfprEtherErrStatsThresholded
_CfprEtherErrStatsThresholded_Object=MibTableColumn
cfprEtherErrStatsThresholded=_CfprEtherErrStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,41),_CfprEtherErrStatsThresholded_Type())
cfprEtherErrStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsThresholded.setStatus(_A)
_CfprEtherErrStatsTimeCollected_Type=DateAndTime
_CfprEtherErrStatsTimeCollected_Object=MibTableColumn
cfprEtherErrStatsTimeCollected=_CfprEtherErrStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,42),_CfprEtherErrStatsTimeCollected_Type())
cfprEtherErrStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsTimeCollected.setStatus(_A)
_CfprEtherErrStatsUnderSize_Type=Unsigned64
_CfprEtherErrStatsUnderSize_Object=MibTableColumn
cfprEtherErrStatsUnderSize=_CfprEtherErrStatsUnderSize_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,43),_CfprEtherErrStatsUnderSize_Type())
cfprEtherErrStatsUnderSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsUnderSize.setStatus(_A)
_CfprEtherErrStatsUnderSizeDelta_Type=Counter64
_CfprEtherErrStatsUnderSizeDelta_Object=MibTableColumn
cfprEtherErrStatsUnderSizeDelta=_CfprEtherErrStatsUnderSizeDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,44),_CfprEtherErrStatsUnderSizeDelta_Type())
cfprEtherErrStatsUnderSizeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsUnderSizeDelta.setStatus(_A)
_CfprEtherErrStatsUnderSizeDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsUnderSizeDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsUnderSizeDeltaAvg=_CfprEtherErrStatsUnderSizeDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,45),_CfprEtherErrStatsUnderSizeDeltaAvg_Type())
cfprEtherErrStatsUnderSizeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsUnderSizeDeltaAvg.setStatus(_A)
_CfprEtherErrStatsUnderSizeDeltaMax_Type=Unsigned64
_CfprEtherErrStatsUnderSizeDeltaMax_Object=MibTableColumn
cfprEtherErrStatsUnderSizeDeltaMax=_CfprEtherErrStatsUnderSizeDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,46),_CfprEtherErrStatsUnderSizeDeltaMax_Type())
cfprEtherErrStatsUnderSizeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsUnderSizeDeltaMax.setStatus(_A)
_CfprEtherErrStatsUnderSizeDeltaMin_Type=Unsigned64
_CfprEtherErrStatsUnderSizeDeltaMin_Object=MibTableColumn
cfprEtherErrStatsUnderSizeDeltaMin=_CfprEtherErrStatsUnderSizeDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,47),_CfprEtherErrStatsUnderSizeDeltaMin_Type())
cfprEtherErrStatsUnderSizeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsUnderSizeDeltaMin.setStatus(_A)
_CfprEtherErrStatsUpdate_Type=Gauge32
_CfprEtherErrStatsUpdate_Object=MibTableColumn
cfprEtherErrStatsUpdate=_CfprEtherErrStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,48),_CfprEtherErrStatsUpdate_Type())
cfprEtherErrStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsUpdate.setStatus(_A)
_CfprEtherErrStatsXmit_Type=Unsigned64
_CfprEtherErrStatsXmit_Object=MibTableColumn
cfprEtherErrStatsXmit=_CfprEtherErrStatsXmit_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,49),_CfprEtherErrStatsXmit_Type())
cfprEtherErrStatsXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsXmit.setStatus(_A)
_CfprEtherErrStatsXmitDelta_Type=Counter64
_CfprEtherErrStatsXmitDelta_Object=MibTableColumn
cfprEtherErrStatsXmitDelta=_CfprEtherErrStatsXmitDelta_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,50),_CfprEtherErrStatsXmitDelta_Type())
cfprEtherErrStatsXmitDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsXmitDelta.setStatus(_A)
_CfprEtherErrStatsXmitDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsXmitDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsXmitDeltaAvg=_CfprEtherErrStatsXmitDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,51),_CfprEtherErrStatsXmitDeltaAvg_Type())
cfprEtherErrStatsXmitDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsXmitDeltaAvg.setStatus(_A)
_CfprEtherErrStatsXmitDeltaMax_Type=Unsigned64
_CfprEtherErrStatsXmitDeltaMax_Object=MibTableColumn
cfprEtherErrStatsXmitDeltaMax=_CfprEtherErrStatsXmitDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,52),_CfprEtherErrStatsXmitDeltaMax_Type())
cfprEtherErrStatsXmitDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsXmitDeltaMax.setStatus(_A)
_CfprEtherErrStatsXmitDeltaMin_Type=Unsigned64
_CfprEtherErrStatsXmitDeltaMin_Object=MibTableColumn
cfprEtherErrStatsXmitDeltaMin=_CfprEtherErrStatsXmitDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,1,1,53),_CfprEtherErrStatsXmitDeltaMin_Type())
cfprEtherErrStatsXmitDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsXmitDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistTable_Object=MibTable
cfprEtherErrStatsHistTable=_CfprEtherErrStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,2))
if mibBuilder.loadTexts:cfprEtherErrStatsHistTable.setStatus(_A)
_CfprEtherErrStatsHistEntry_Object=MibTableRow
cfprEtherErrStatsHistEntry=_CfprEtherErrStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,2,1))
cfprEtherErrStatsHistEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprEtherErrStatsHistEntry.setStatus(_A)
_CfprEtherErrStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherErrStatsHistInstanceId_Object=MibTableColumn
cfprEtherErrStatsHistInstanceId=_CfprEtherErrStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,1),_CfprEtherErrStatsHistInstanceId_Type())
cfprEtherErrStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherErrStatsHistInstanceId.setStatus(_A)
_CfprEtherErrStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherErrStatsHistDn_Object=MibTableColumn
cfprEtherErrStatsHistDn=_CfprEtherErrStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,2),_CfprEtherErrStatsHistDn_Type())
cfprEtherErrStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistDn.setStatus(_A)
_CfprEtherErrStatsHistRn_Type=SnmpAdminString
_CfprEtherErrStatsHistRn_Object=MibTableColumn
cfprEtherErrStatsHistRn=_CfprEtherErrStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,3),_CfprEtherErrStatsHistRn_Type())
cfprEtherErrStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistRn.setStatus(_A)
_CfprEtherErrStatsHistAlign_Type=Unsigned64
_CfprEtherErrStatsHistAlign_Object=MibTableColumn
cfprEtherErrStatsHistAlign=_CfprEtherErrStatsHistAlign_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,4),_CfprEtherErrStatsHistAlign_Type())
cfprEtherErrStatsHistAlign.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistAlign.setStatus(_A)
_CfprEtherErrStatsHistAlignDelta_Type=Unsigned64
_CfprEtherErrStatsHistAlignDelta_Object=MibTableColumn
cfprEtherErrStatsHistAlignDelta=_CfprEtherErrStatsHistAlignDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,5),_CfprEtherErrStatsHistAlignDelta_Type())
cfprEtherErrStatsHistAlignDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistAlignDelta.setStatus(_A)
_CfprEtherErrStatsHistAlignDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistAlignDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistAlignDeltaAvg=_CfprEtherErrStatsHistAlignDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,6),_CfprEtherErrStatsHistAlignDeltaAvg_Type())
cfprEtherErrStatsHistAlignDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistAlignDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistAlignDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistAlignDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistAlignDeltaMax=_CfprEtherErrStatsHistAlignDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,7),_CfprEtherErrStatsHistAlignDeltaMax_Type())
cfprEtherErrStatsHistAlignDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistAlignDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistAlignDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistAlignDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistAlignDeltaMin=_CfprEtherErrStatsHistAlignDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,8),_CfprEtherErrStatsHistAlignDeltaMin_Type())
cfprEtherErrStatsHistAlignDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistAlignDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistDeferredTx_Type=Unsigned64
_CfprEtherErrStatsHistDeferredTx_Object=MibTableColumn
cfprEtherErrStatsHistDeferredTx=_CfprEtherErrStatsHistDeferredTx_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,9),_CfprEtherErrStatsHistDeferredTx_Type())
cfprEtherErrStatsHistDeferredTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistDeferredTx.setStatus(_A)
_CfprEtherErrStatsHistDeferredTxDelta_Type=Unsigned64
_CfprEtherErrStatsHistDeferredTxDelta_Object=MibTableColumn
cfprEtherErrStatsHistDeferredTxDelta=_CfprEtherErrStatsHistDeferredTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,10),_CfprEtherErrStatsHistDeferredTxDelta_Type())
cfprEtherErrStatsHistDeferredTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistDeferredTxDelta.setStatus(_A)
_CfprEtherErrStatsHistDeferredTxDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistDeferredTxDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistDeferredTxDeltaAvg=_CfprEtherErrStatsHistDeferredTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,11),_CfprEtherErrStatsHistDeferredTxDeltaAvg_Type())
cfprEtherErrStatsHistDeferredTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistDeferredTxDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistDeferredTxDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistDeferredTxDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistDeferredTxDeltaMax=_CfprEtherErrStatsHistDeferredTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,12),_CfprEtherErrStatsHistDeferredTxDeltaMax_Type())
cfprEtherErrStatsHistDeferredTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistDeferredTxDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistDeferredTxDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistDeferredTxDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistDeferredTxDeltaMin=_CfprEtherErrStatsHistDeferredTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,13),_CfprEtherErrStatsHistDeferredTxDeltaMin_Type())
cfprEtherErrStatsHistDeferredTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistDeferredTxDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistFcs_Type=Unsigned64
_CfprEtherErrStatsHistFcs_Object=MibTableColumn
cfprEtherErrStatsHistFcs=_CfprEtherErrStatsHistFcs_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,14),_CfprEtherErrStatsHistFcs_Type())
cfprEtherErrStatsHistFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistFcs.setStatus(_A)
_CfprEtherErrStatsHistFcsDelta_Type=Unsigned64
_CfprEtherErrStatsHistFcsDelta_Object=MibTableColumn
cfprEtherErrStatsHistFcsDelta=_CfprEtherErrStatsHistFcsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,15),_CfprEtherErrStatsHistFcsDelta_Type())
cfprEtherErrStatsHistFcsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistFcsDelta.setStatus(_A)
_CfprEtherErrStatsHistFcsDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistFcsDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistFcsDeltaAvg=_CfprEtherErrStatsHistFcsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,16),_CfprEtherErrStatsHistFcsDeltaAvg_Type())
cfprEtherErrStatsHistFcsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistFcsDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistFcsDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistFcsDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistFcsDeltaMax=_CfprEtherErrStatsHistFcsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,17),_CfprEtherErrStatsHistFcsDeltaMax_Type())
cfprEtherErrStatsHistFcsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistFcsDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistFcsDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistFcsDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistFcsDeltaMin=_CfprEtherErrStatsHistFcsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,18),_CfprEtherErrStatsHistFcsDeltaMin_Type())
cfprEtherErrStatsHistFcsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistFcsDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistId_Type=Unsigned64
_CfprEtherErrStatsHistId_Object=MibTableColumn
cfprEtherErrStatsHistId=_CfprEtherErrStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,19),_CfprEtherErrStatsHistId_Type())
cfprEtherErrStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistId.setStatus(_A)
_CfprEtherErrStatsHistIntMacRx_Type=Unsigned64
_CfprEtherErrStatsHistIntMacRx_Object=MibTableColumn
cfprEtherErrStatsHistIntMacRx=_CfprEtherErrStatsHistIntMacRx_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,20),_CfprEtherErrStatsHistIntMacRx_Type())
cfprEtherErrStatsHistIntMacRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacRx.setStatus(_A)
_CfprEtherErrStatsHistIntMacRxDelta_Type=Unsigned64
_CfprEtherErrStatsHistIntMacRxDelta_Object=MibTableColumn
cfprEtherErrStatsHistIntMacRxDelta=_CfprEtherErrStatsHistIntMacRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,21),_CfprEtherErrStatsHistIntMacRxDelta_Type())
cfprEtherErrStatsHistIntMacRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacRxDelta.setStatus(_A)
_CfprEtherErrStatsHistIntMacRxDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistIntMacRxDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistIntMacRxDeltaAvg=_CfprEtherErrStatsHistIntMacRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,22),_CfprEtherErrStatsHistIntMacRxDeltaAvg_Type())
cfprEtherErrStatsHistIntMacRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacRxDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistIntMacRxDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistIntMacRxDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistIntMacRxDeltaMax=_CfprEtherErrStatsHistIntMacRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,23),_CfprEtherErrStatsHistIntMacRxDeltaMax_Type())
cfprEtherErrStatsHistIntMacRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacRxDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistIntMacRxDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistIntMacRxDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistIntMacRxDeltaMin=_CfprEtherErrStatsHistIntMacRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,24),_CfprEtherErrStatsHistIntMacRxDeltaMin_Type())
cfprEtherErrStatsHistIntMacRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacRxDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistIntMacTx_Type=Unsigned64
_CfprEtherErrStatsHistIntMacTx_Object=MibTableColumn
cfprEtherErrStatsHistIntMacTx=_CfprEtherErrStatsHistIntMacTx_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,25),_CfprEtherErrStatsHistIntMacTx_Type())
cfprEtherErrStatsHistIntMacTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacTx.setStatus(_A)
_CfprEtherErrStatsHistIntMacTxDelta_Type=Unsigned64
_CfprEtherErrStatsHistIntMacTxDelta_Object=MibTableColumn
cfprEtherErrStatsHistIntMacTxDelta=_CfprEtherErrStatsHistIntMacTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,26),_CfprEtherErrStatsHistIntMacTxDelta_Type())
cfprEtherErrStatsHistIntMacTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacTxDelta.setStatus(_A)
_CfprEtherErrStatsHistIntMacTxDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistIntMacTxDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistIntMacTxDeltaAvg=_CfprEtherErrStatsHistIntMacTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,27),_CfprEtherErrStatsHistIntMacTxDeltaAvg_Type())
cfprEtherErrStatsHistIntMacTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacTxDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistIntMacTxDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistIntMacTxDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistIntMacTxDeltaMax=_CfprEtherErrStatsHistIntMacTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,28),_CfprEtherErrStatsHistIntMacTxDeltaMax_Type())
cfprEtherErrStatsHistIntMacTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacTxDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistIntMacTxDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistIntMacTxDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistIntMacTxDeltaMin=_CfprEtherErrStatsHistIntMacTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,29),_CfprEtherErrStatsHistIntMacTxDeltaMin_Type())
cfprEtherErrStatsHistIntMacTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistIntMacTxDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistMostRecent_Type=TruthValue
_CfprEtherErrStatsHistMostRecent_Object=MibTableColumn
cfprEtherErrStatsHistMostRecent=_CfprEtherErrStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,30),_CfprEtherErrStatsHistMostRecent_Type())
cfprEtherErrStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistMostRecent.setStatus(_A)
_CfprEtherErrStatsHistOutDiscard_Type=Unsigned64
_CfprEtherErrStatsHistOutDiscard_Object=MibTableColumn
cfprEtherErrStatsHistOutDiscard=_CfprEtherErrStatsHistOutDiscard_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,31),_CfprEtherErrStatsHistOutDiscard_Type())
cfprEtherErrStatsHistOutDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistOutDiscard.setStatus(_A)
_CfprEtherErrStatsHistOutDiscardDelta_Type=Unsigned64
_CfprEtherErrStatsHistOutDiscardDelta_Object=MibTableColumn
cfprEtherErrStatsHistOutDiscardDelta=_CfprEtherErrStatsHistOutDiscardDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,32),_CfprEtherErrStatsHistOutDiscardDelta_Type())
cfprEtherErrStatsHistOutDiscardDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistOutDiscardDelta.setStatus(_A)
_CfprEtherErrStatsHistOutDiscardDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistOutDiscardDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistOutDiscardDeltaAvg=_CfprEtherErrStatsHistOutDiscardDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,33),_CfprEtherErrStatsHistOutDiscardDeltaAvg_Type())
cfprEtherErrStatsHistOutDiscardDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistOutDiscardDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistOutDiscardDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistOutDiscardDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistOutDiscardDeltaMax=_CfprEtherErrStatsHistOutDiscardDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,34),_CfprEtherErrStatsHistOutDiscardDeltaMax_Type())
cfprEtherErrStatsHistOutDiscardDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistOutDiscardDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistOutDiscardDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistOutDiscardDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistOutDiscardDeltaMin=_CfprEtherErrStatsHistOutDiscardDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,35),_CfprEtherErrStatsHistOutDiscardDeltaMin_Type())
cfprEtherErrStatsHistOutDiscardDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistOutDiscardDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistRcv_Type=Unsigned64
_CfprEtherErrStatsHistRcv_Object=MibTableColumn
cfprEtherErrStatsHistRcv=_CfprEtherErrStatsHistRcv_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,36),_CfprEtherErrStatsHistRcv_Type())
cfprEtherErrStatsHistRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistRcv.setStatus(_A)
_CfprEtherErrStatsHistRcvDelta_Type=Unsigned64
_CfprEtherErrStatsHistRcvDelta_Object=MibTableColumn
cfprEtherErrStatsHistRcvDelta=_CfprEtherErrStatsHistRcvDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,37),_CfprEtherErrStatsHistRcvDelta_Type())
cfprEtherErrStatsHistRcvDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistRcvDelta.setStatus(_A)
_CfprEtherErrStatsHistRcvDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistRcvDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistRcvDeltaAvg=_CfprEtherErrStatsHistRcvDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,38),_CfprEtherErrStatsHistRcvDeltaAvg_Type())
cfprEtherErrStatsHistRcvDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistRcvDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistRcvDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistRcvDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistRcvDeltaMax=_CfprEtherErrStatsHistRcvDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,39),_CfprEtherErrStatsHistRcvDeltaMax_Type())
cfprEtherErrStatsHistRcvDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistRcvDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistRcvDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistRcvDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistRcvDeltaMin=_CfprEtherErrStatsHistRcvDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,40),_CfprEtherErrStatsHistRcvDeltaMin_Type())
cfprEtherErrStatsHistRcvDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistRcvDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistSuspect_Type=TruthValue
_CfprEtherErrStatsHistSuspect_Object=MibTableColumn
cfprEtherErrStatsHistSuspect=_CfprEtherErrStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,41),_CfprEtherErrStatsHistSuspect_Type())
cfprEtherErrStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistSuspect.setStatus(_A)
_CfprEtherErrStatsHistThresholded_Type=CfprEtherErrStatsHistThresholded
_CfprEtherErrStatsHistThresholded_Object=MibTableColumn
cfprEtherErrStatsHistThresholded=_CfprEtherErrStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,42),_CfprEtherErrStatsHistThresholded_Type())
cfprEtherErrStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistThresholded.setStatus(_A)
_CfprEtherErrStatsHistTimeCollected_Type=DateAndTime
_CfprEtherErrStatsHistTimeCollected_Object=MibTableColumn
cfprEtherErrStatsHistTimeCollected=_CfprEtherErrStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,43),_CfprEtherErrStatsHistTimeCollected_Type())
cfprEtherErrStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistTimeCollected.setStatus(_A)
_CfprEtherErrStatsHistUnderSize_Type=Unsigned64
_CfprEtherErrStatsHistUnderSize_Object=MibTableColumn
cfprEtherErrStatsHistUnderSize=_CfprEtherErrStatsHistUnderSize_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,44),_CfprEtherErrStatsHistUnderSize_Type())
cfprEtherErrStatsHistUnderSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistUnderSize.setStatus(_A)
_CfprEtherErrStatsHistUnderSizeDelta_Type=Unsigned64
_CfprEtherErrStatsHistUnderSizeDelta_Object=MibTableColumn
cfprEtherErrStatsHistUnderSizeDelta=_CfprEtherErrStatsHistUnderSizeDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,45),_CfprEtherErrStatsHistUnderSizeDelta_Type())
cfprEtherErrStatsHistUnderSizeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistUnderSizeDelta.setStatus(_A)
_CfprEtherErrStatsHistUnderSizeDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistUnderSizeDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistUnderSizeDeltaAvg=_CfprEtherErrStatsHistUnderSizeDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,46),_CfprEtherErrStatsHistUnderSizeDeltaAvg_Type())
cfprEtherErrStatsHistUnderSizeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistUnderSizeDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistUnderSizeDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistUnderSizeDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistUnderSizeDeltaMax=_CfprEtherErrStatsHistUnderSizeDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,47),_CfprEtherErrStatsHistUnderSizeDeltaMax_Type())
cfprEtherErrStatsHistUnderSizeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistUnderSizeDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistUnderSizeDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistUnderSizeDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistUnderSizeDeltaMin=_CfprEtherErrStatsHistUnderSizeDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,48),_CfprEtherErrStatsHistUnderSizeDeltaMin_Type())
cfprEtherErrStatsHistUnderSizeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistUnderSizeDeltaMin.setStatus(_A)
_CfprEtherErrStatsHistXmit_Type=Unsigned64
_CfprEtherErrStatsHistXmit_Object=MibTableColumn
cfprEtherErrStatsHistXmit=_CfprEtherErrStatsHistXmit_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,49),_CfprEtherErrStatsHistXmit_Type())
cfprEtherErrStatsHistXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistXmit.setStatus(_A)
_CfprEtherErrStatsHistXmitDelta_Type=Unsigned64
_CfprEtherErrStatsHistXmitDelta_Object=MibTableColumn
cfprEtherErrStatsHistXmitDelta=_CfprEtherErrStatsHistXmitDelta_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,50),_CfprEtherErrStatsHistXmitDelta_Type())
cfprEtherErrStatsHistXmitDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistXmitDelta.setStatus(_A)
_CfprEtherErrStatsHistXmitDeltaAvg_Type=Unsigned64
_CfprEtherErrStatsHistXmitDeltaAvg_Object=MibTableColumn
cfprEtherErrStatsHistXmitDeltaAvg=_CfprEtherErrStatsHistXmitDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,51),_CfprEtherErrStatsHistXmitDeltaAvg_Type())
cfprEtherErrStatsHistXmitDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistXmitDeltaAvg.setStatus(_A)
_CfprEtherErrStatsHistXmitDeltaMax_Type=Unsigned64
_CfprEtherErrStatsHistXmitDeltaMax_Object=MibTableColumn
cfprEtherErrStatsHistXmitDeltaMax=_CfprEtherErrStatsHistXmitDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,52),_CfprEtherErrStatsHistXmitDeltaMax_Type())
cfprEtherErrStatsHistXmitDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistXmitDeltaMax.setStatus(_A)
_CfprEtherErrStatsHistXmitDeltaMin_Type=Unsigned64
_CfprEtherErrStatsHistXmitDeltaMin_Object=MibTableColumn
cfprEtherErrStatsHistXmitDeltaMin=_CfprEtherErrStatsHistXmitDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,2,1,53),_CfprEtherErrStatsHistXmitDeltaMin_Type())
cfprEtherErrStatsHistXmitDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherErrStatsHistXmitDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsTable_Object=MibTable
cfprEtherFcoeInterfaceStatsTable=_CfprEtherFcoeInterfaceStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,3))
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsTable.setStatus(_A)
_CfprEtherFcoeInterfaceStatsEntry_Object=MibTableRow
cfprEtherFcoeInterfaceStatsEntry=_CfprEtherFcoeInterfaceStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,3,1))
cfprEtherFcoeInterfaceStatsEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsEntry.setStatus(_A)
_CfprEtherFcoeInterfaceStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherFcoeInterfaceStatsInstanceId_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsInstanceId=_CfprEtherFcoeInterfaceStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,1),_CfprEtherFcoeInterfaceStatsInstanceId_Type())
cfprEtherFcoeInterfaceStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsInstanceId.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDn_Type=CfprManagedObjectDn
_CfprEtherFcoeInterfaceStatsDn_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDn=_CfprEtherFcoeInterfaceStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,2),_CfprEtherFcoeInterfaceStatsDn_Type())
cfprEtherFcoeInterfaceStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDn.setStatus(_A)
_CfprEtherFcoeInterfaceStatsRn_Type=SnmpAdminString
_CfprEtherFcoeInterfaceStatsRn_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsRn=_CfprEtherFcoeInterfaceStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,3),_CfprEtherFcoeInterfaceStatsRn_Type())
cfprEtherFcoeInterfaceStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsRn.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRx=_CfprEtherFcoeInterfaceStatsBytesRx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,4),_CfprEtherFcoeInterfaceStatsBytesRx_Type())
cfprEtherFcoeInterfaceStatsBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesRxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsBytesRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDelta=_CfprEtherFcoeInterfaceStatsBytesRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,5),_CfprEtherFcoeInterfaceStatsBytesRxDelta_Type())
cfprEtherFcoeInterfaceStatsBytesRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg=_CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,6),_CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDeltaMax=_CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,7),_CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsBytesRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDeltaMin=_CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,8),_CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsBytesRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTx=_CfprEtherFcoeInterfaceStatsBytesTx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,9),_CfprEtherFcoeInterfaceStatsBytesTx_Type())
cfprEtherFcoeInterfaceStatsBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesTxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsBytesTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDelta=_CfprEtherFcoeInterfaceStatsBytesTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,10),_CfprEtherFcoeInterfaceStatsBytesTxDelta_Type())
cfprEtherFcoeInterfaceStatsBytesTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg=_CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,11),_CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDeltaMax=_CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,12),_CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsBytesTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDeltaMin=_CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,13),_CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsBytesTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsBytesTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRx=_CfprEtherFcoeInterfaceStatsDroppedRx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,14),_CfprEtherFcoeInterfaceStatsDroppedRx_Type())
cfprEtherFcoeInterfaceStatsDroppedRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedRxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsDroppedRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDelta=_CfprEtherFcoeInterfaceStatsDroppedRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,15),_CfprEtherFcoeInterfaceStatsDroppedRxDelta_Type())
cfprEtherFcoeInterfaceStatsDroppedRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg=_CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,16),_CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax=_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,17),_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin=_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,18),_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTx=_CfprEtherFcoeInterfaceStatsDroppedTx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,19),_CfprEtherFcoeInterfaceStatsDroppedTx_Type())
cfprEtherFcoeInterfaceStatsDroppedTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedTxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsDroppedTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDelta=_CfprEtherFcoeInterfaceStatsDroppedTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,20),_CfprEtherFcoeInterfaceStatsDroppedTxDelta_Type())
cfprEtherFcoeInterfaceStatsDroppedTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg=_CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,21),_CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax=_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,22),_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin=_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,23),_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRx=_CfprEtherFcoeInterfaceStatsErrorsRx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,24),_CfprEtherFcoeInterfaceStatsErrorsRx_Type())
cfprEtherFcoeInterfaceStatsErrorsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsRxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsErrorsRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDelta=_CfprEtherFcoeInterfaceStatsErrorsRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,25),_CfprEtherFcoeInterfaceStatsErrorsRxDelta_Type())
cfprEtherFcoeInterfaceStatsErrorsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg=_CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,26),_CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax=_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,27),_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin=_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,28),_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTx=_CfprEtherFcoeInterfaceStatsErrorsTx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,29),_CfprEtherFcoeInterfaceStatsErrorsTx_Type())
cfprEtherFcoeInterfaceStatsErrorsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsTxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsErrorsTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDelta=_CfprEtherFcoeInterfaceStatsErrorsTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,30),_CfprEtherFcoeInterfaceStatsErrorsTxDelta_Type())
cfprEtherFcoeInterfaceStatsErrorsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg=_CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,31),_CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax=_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,32),_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin=_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,33),_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsIntervals_Type=Gauge32
_CfprEtherFcoeInterfaceStatsIntervals_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsIntervals=_CfprEtherFcoeInterfaceStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,34),_CfprEtherFcoeInterfaceStatsIntervals_Type())
cfprEtherFcoeInterfaceStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsIntervals.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRx=_CfprEtherFcoeInterfaceStatsPacketsRx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,35),_CfprEtherFcoeInterfaceStatsPacketsRx_Type())
cfprEtherFcoeInterfaceStatsPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsRxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsPacketsRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDelta=_CfprEtherFcoeInterfaceStatsPacketsRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,36),_CfprEtherFcoeInterfaceStatsPacketsRxDelta_Type())
cfprEtherFcoeInterfaceStatsPacketsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg=_CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,37),_CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax=_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,38),_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin=_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,39),_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTx=_CfprEtherFcoeInterfaceStatsPacketsTx_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,40),_CfprEtherFcoeInterfaceStatsPacketsTx_Type())
cfprEtherFcoeInterfaceStatsPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsTxDelta_Type=Counter64
_CfprEtherFcoeInterfaceStatsPacketsTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDelta=_CfprEtherFcoeInterfaceStatsPacketsTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,41),_CfprEtherFcoeInterfaceStatsPacketsTxDelta_Type())
cfprEtherFcoeInterfaceStatsPacketsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg=_CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,42),_CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax=_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,43),_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin=_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,44),_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsSuspect_Type=TruthValue
_CfprEtherFcoeInterfaceStatsSuspect_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsSuspect=_CfprEtherFcoeInterfaceStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,45),_CfprEtherFcoeInterfaceStatsSuspect_Type())
cfprEtherFcoeInterfaceStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsSuspect.setStatus(_A)
_CfprEtherFcoeInterfaceStatsThresholded_Type=CfprEtherFcoeInterfaceStatsThresholded
_CfprEtherFcoeInterfaceStatsThresholded_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsThresholded=_CfprEtherFcoeInterfaceStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,46),_CfprEtherFcoeInterfaceStatsThresholded_Type())
cfprEtherFcoeInterfaceStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsThresholded.setStatus(_A)
_CfprEtherFcoeInterfaceStatsTimeCollected_Type=DateAndTime
_CfprEtherFcoeInterfaceStatsTimeCollected_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsTimeCollected=_CfprEtherFcoeInterfaceStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,47),_CfprEtherFcoeInterfaceStatsTimeCollected_Type())
cfprEtherFcoeInterfaceStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsTimeCollected.setStatus(_A)
_CfprEtherFcoeInterfaceStatsUpdate_Type=Gauge32
_CfprEtherFcoeInterfaceStatsUpdate_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsUpdate=_CfprEtherFcoeInterfaceStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,3,1,48),_CfprEtherFcoeInterfaceStatsUpdate_Type())
cfprEtherFcoeInterfaceStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsUpdate.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistTable_Object=MibTable
cfprEtherFcoeInterfaceStatsHistTable=_CfprEtherFcoeInterfaceStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,4))
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistTable.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistEntry_Object=MibTableRow
cfprEtherFcoeInterfaceStatsHistEntry=_CfprEtherFcoeInterfaceStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,4,1))
cfprEtherFcoeInterfaceStatsHistEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistEntry.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherFcoeInterfaceStatsHistInstanceId_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistInstanceId=_CfprEtherFcoeInterfaceStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,1),_CfprEtherFcoeInterfaceStatsHistInstanceId_Type())
cfprEtherFcoeInterfaceStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistInstanceId.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherFcoeInterfaceStatsHistDn_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDn=_CfprEtherFcoeInterfaceStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,2),_CfprEtherFcoeInterfaceStatsHistDn_Type())
cfprEtherFcoeInterfaceStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDn.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistRn_Type=SnmpAdminString
_CfprEtherFcoeInterfaceStatsHistRn_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistRn=_CfprEtherFcoeInterfaceStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,3),_CfprEtherFcoeInterfaceStatsHistRn_Type())
cfprEtherFcoeInterfaceStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistRn.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRx=_CfprEtherFcoeInterfaceStatsHistBytesRx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,4),_CfprEtherFcoeInterfaceStatsHistBytesRx_Type())
cfprEtherFcoeInterfaceStatsHistBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDelta=_CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,5),_CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Type())
cfprEtherFcoeInterfaceStatsHistBytesRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,6),_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax=_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,7),_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin=_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,8),_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTx=_CfprEtherFcoeInterfaceStatsHistBytesTx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,9),_CfprEtherFcoeInterfaceStatsHistBytesTx_Type())
cfprEtherFcoeInterfaceStatsHistBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDelta=_CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,10),_CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Type())
cfprEtherFcoeInterfaceStatsHistBytesTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,11),_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax=_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,12),_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin=_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,13),_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRx=_CfprEtherFcoeInterfaceStatsHistDroppedRx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,14),_CfprEtherFcoeInterfaceStatsHistDroppedRx_Type())
cfprEtherFcoeInterfaceStatsHistDroppedRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDelta=_CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,15),_CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Type())
cfprEtherFcoeInterfaceStatsHistDroppedRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,16),_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax=_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,17),_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin=_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,18),_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTx=_CfprEtherFcoeInterfaceStatsHistDroppedTx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,19),_CfprEtherFcoeInterfaceStatsHistDroppedTx_Type())
cfprEtherFcoeInterfaceStatsHistDroppedTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDelta=_CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,20),_CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Type())
cfprEtherFcoeInterfaceStatsHistDroppedTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,21),_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax=_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,22),_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin=_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,23),_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRx=_CfprEtherFcoeInterfaceStatsHistErrorsRx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,24),_CfprEtherFcoeInterfaceStatsHistErrorsRx_Type())
cfprEtherFcoeInterfaceStatsHistErrorsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDelta=_CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,25),_CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Type())
cfprEtherFcoeInterfaceStatsHistErrorsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,26),_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax=_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,27),_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin=_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,28),_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTx=_CfprEtherFcoeInterfaceStatsHistErrorsTx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,29),_CfprEtherFcoeInterfaceStatsHistErrorsTx_Type())
cfprEtherFcoeInterfaceStatsHistErrorsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDelta=_CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,30),_CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Type())
cfprEtherFcoeInterfaceStatsHistErrorsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,31),_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax=_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,32),_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin=_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,33),_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistId_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistId_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistId=_CfprEtherFcoeInterfaceStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,34),_CfprEtherFcoeInterfaceStatsHistId_Type())
cfprEtherFcoeInterfaceStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistId.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistMostRecent_Type=TruthValue
_CfprEtherFcoeInterfaceStatsHistMostRecent_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistMostRecent=_CfprEtherFcoeInterfaceStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,35),_CfprEtherFcoeInterfaceStatsHistMostRecent_Type())
cfprEtherFcoeInterfaceStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistMostRecent.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsRx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRx=_CfprEtherFcoeInterfaceStatsHistPacketsRx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,36),_CfprEtherFcoeInterfaceStatsHistPacketsRx_Type())
cfprEtherFcoeInterfaceStatsHistPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsRx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDelta=_CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,37),_CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Type())
cfprEtherFcoeInterfaceStatsHistPacketsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsRxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,38),_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax=_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,39),_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin=_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,40),_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsTx_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTx_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTx=_CfprEtherFcoeInterfaceStatsHistPacketsTx_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,41),_CfprEtherFcoeInterfaceStatsHistPacketsTx_Type())
cfprEtherFcoeInterfaceStatsHistPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsTx.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDelta=_CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,42),_CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Type())
cfprEtherFcoeInterfaceStatsHistPacketsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsTxDelta.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg=_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,43),_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type())
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax=_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,44),_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type())
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type=Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin=_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,45),_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type())
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistSuspect_Type=TruthValue
_CfprEtherFcoeInterfaceStatsHistSuspect_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistSuspect=_CfprEtherFcoeInterfaceStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,46),_CfprEtherFcoeInterfaceStatsHistSuspect_Type())
cfprEtherFcoeInterfaceStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistSuspect.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistThresholded_Type=CfprEtherFcoeInterfaceStatsHistThresholded
_CfprEtherFcoeInterfaceStatsHistThresholded_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistThresholded=_CfprEtherFcoeInterfaceStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,47),_CfprEtherFcoeInterfaceStatsHistThresholded_Type())
cfprEtherFcoeInterfaceStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistThresholded.setStatus(_A)
_CfprEtherFcoeInterfaceStatsHistTimeCollected_Type=DateAndTime
_CfprEtherFcoeInterfaceStatsHistTimeCollected_Object=MibTableColumn
cfprEtherFcoeInterfaceStatsHistTimeCollected=_CfprEtherFcoeInterfaceStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,4,1,48),_CfprEtherFcoeInterfaceStatsHistTimeCollected_Type())
cfprEtherFcoeInterfaceStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFcoeInterfaceStatsHistTimeCollected.setStatus(_A)
_CfprEtherLossStatsTable_Object=MibTable
cfprEtherLossStatsTable=_CfprEtherLossStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,5))
if mibBuilder.loadTexts:cfprEtherLossStatsTable.setStatus(_A)
_CfprEtherLossStatsEntry_Object=MibTableRow
cfprEtherLossStatsEntry=_CfprEtherLossStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,5,1))
cfprEtherLossStatsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprEtherLossStatsEntry.setStatus(_A)
_CfprEtherLossStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherLossStatsInstanceId_Object=MibTableColumn
cfprEtherLossStatsInstanceId=_CfprEtherLossStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,1),_CfprEtherLossStatsInstanceId_Type())
cfprEtherLossStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherLossStatsInstanceId.setStatus(_A)
_CfprEtherLossStatsDn_Type=CfprManagedObjectDn
_CfprEtherLossStatsDn_Object=MibTableColumn
cfprEtherLossStatsDn=_CfprEtherLossStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,2),_CfprEtherLossStatsDn_Type())
cfprEtherLossStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsDn.setStatus(_A)
_CfprEtherLossStatsRn_Type=SnmpAdminString
_CfprEtherLossStatsRn_Object=MibTableColumn
cfprEtherLossStatsRn=_CfprEtherLossStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,3),_CfprEtherLossStatsRn_Type())
cfprEtherLossStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsRn.setStatus(_A)
_CfprEtherLossStatsSQETest_Type=Unsigned64
_CfprEtherLossStatsSQETest_Object=MibTableColumn
cfprEtherLossStatsSQETest=_CfprEtherLossStatsSQETest_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,4),_CfprEtherLossStatsSQETest_Type())
cfprEtherLossStatsSQETest.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSQETest.setStatus(_A)
_CfprEtherLossStatsSQETestDelta_Type=Counter64
_CfprEtherLossStatsSQETestDelta_Object=MibTableColumn
cfprEtherLossStatsSQETestDelta=_CfprEtherLossStatsSQETestDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,5),_CfprEtherLossStatsSQETestDelta_Type())
cfprEtherLossStatsSQETestDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSQETestDelta.setStatus(_A)
_CfprEtherLossStatsSQETestDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsSQETestDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsSQETestDeltaAvg=_CfprEtherLossStatsSQETestDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,6),_CfprEtherLossStatsSQETestDeltaAvg_Type())
cfprEtherLossStatsSQETestDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSQETestDeltaAvg.setStatus(_A)
_CfprEtherLossStatsSQETestDeltaMax_Type=Unsigned64
_CfprEtherLossStatsSQETestDeltaMax_Object=MibTableColumn
cfprEtherLossStatsSQETestDeltaMax=_CfprEtherLossStatsSQETestDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,7),_CfprEtherLossStatsSQETestDeltaMax_Type())
cfprEtherLossStatsSQETestDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSQETestDeltaMax.setStatus(_A)
_CfprEtherLossStatsSQETestDeltaMin_Type=Unsigned64
_CfprEtherLossStatsSQETestDeltaMin_Object=MibTableColumn
cfprEtherLossStatsSQETestDeltaMin=_CfprEtherLossStatsSQETestDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,8),_CfprEtherLossStatsSQETestDeltaMin_Type())
cfprEtherLossStatsSQETestDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSQETestDeltaMin.setStatus(_A)
_CfprEtherLossStatsCarrierSense_Type=Unsigned64
_CfprEtherLossStatsCarrierSense_Object=MibTableColumn
cfprEtherLossStatsCarrierSense=_CfprEtherLossStatsCarrierSense_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,9),_CfprEtherLossStatsCarrierSense_Type())
cfprEtherLossStatsCarrierSense.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsCarrierSense.setStatus(_A)
_CfprEtherLossStatsCarrierSenseDelta_Type=Counter64
_CfprEtherLossStatsCarrierSenseDelta_Object=MibTableColumn
cfprEtherLossStatsCarrierSenseDelta=_CfprEtherLossStatsCarrierSenseDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,10),_CfprEtherLossStatsCarrierSenseDelta_Type())
cfprEtherLossStatsCarrierSenseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsCarrierSenseDelta.setStatus(_A)
_CfprEtherLossStatsCarrierSenseDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsCarrierSenseDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsCarrierSenseDeltaAvg=_CfprEtherLossStatsCarrierSenseDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,11),_CfprEtherLossStatsCarrierSenseDeltaAvg_Type())
cfprEtherLossStatsCarrierSenseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsCarrierSenseDeltaAvg.setStatus(_A)
_CfprEtherLossStatsCarrierSenseDeltaMax_Type=Unsigned64
_CfprEtherLossStatsCarrierSenseDeltaMax_Object=MibTableColumn
cfprEtherLossStatsCarrierSenseDeltaMax=_CfprEtherLossStatsCarrierSenseDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,12),_CfprEtherLossStatsCarrierSenseDeltaMax_Type())
cfprEtherLossStatsCarrierSenseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsCarrierSenseDeltaMax.setStatus(_A)
_CfprEtherLossStatsCarrierSenseDeltaMin_Type=Unsigned64
_CfprEtherLossStatsCarrierSenseDeltaMin_Object=MibTableColumn
cfprEtherLossStatsCarrierSenseDeltaMin=_CfprEtherLossStatsCarrierSenseDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,13),_CfprEtherLossStatsCarrierSenseDeltaMin_Type())
cfprEtherLossStatsCarrierSenseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsCarrierSenseDeltaMin.setStatus(_A)
_CfprEtherLossStatsExcessCollision_Type=Unsigned64
_CfprEtherLossStatsExcessCollision_Object=MibTableColumn
cfprEtherLossStatsExcessCollision=_CfprEtherLossStatsExcessCollision_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,14),_CfprEtherLossStatsExcessCollision_Type())
cfprEtherLossStatsExcessCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsExcessCollision.setStatus(_A)
_CfprEtherLossStatsExcessCollisionDelta_Type=Counter64
_CfprEtherLossStatsExcessCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsExcessCollisionDelta=_CfprEtherLossStatsExcessCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,15),_CfprEtherLossStatsExcessCollisionDelta_Type())
cfprEtherLossStatsExcessCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsExcessCollisionDelta.setStatus(_A)
_CfprEtherLossStatsExcessCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsExcessCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsExcessCollisionDeltaAvg=_CfprEtherLossStatsExcessCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,16),_CfprEtherLossStatsExcessCollisionDeltaAvg_Type())
cfprEtherLossStatsExcessCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsExcessCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsExcessCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsExcessCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsExcessCollisionDeltaMax=_CfprEtherLossStatsExcessCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,17),_CfprEtherLossStatsExcessCollisionDeltaMax_Type())
cfprEtherLossStatsExcessCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsExcessCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsExcessCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsExcessCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsExcessCollisionDeltaMin=_CfprEtherLossStatsExcessCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,18),_CfprEtherLossStatsExcessCollisionDeltaMin_Type())
cfprEtherLossStatsExcessCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsExcessCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsGiants_Type=Unsigned64
_CfprEtherLossStatsGiants_Object=MibTableColumn
cfprEtherLossStatsGiants=_CfprEtherLossStatsGiants_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,19),_CfprEtherLossStatsGiants_Type())
cfprEtherLossStatsGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsGiants.setStatus(_A)
_CfprEtherLossStatsGiantsDelta_Type=Counter64
_CfprEtherLossStatsGiantsDelta_Object=MibTableColumn
cfprEtherLossStatsGiantsDelta=_CfprEtherLossStatsGiantsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,20),_CfprEtherLossStatsGiantsDelta_Type())
cfprEtherLossStatsGiantsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsGiantsDelta.setStatus(_A)
_CfprEtherLossStatsGiantsDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsGiantsDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsGiantsDeltaAvg=_CfprEtherLossStatsGiantsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,21),_CfprEtherLossStatsGiantsDeltaAvg_Type())
cfprEtherLossStatsGiantsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsGiantsDeltaAvg.setStatus(_A)
_CfprEtherLossStatsGiantsDeltaMax_Type=Unsigned64
_CfprEtherLossStatsGiantsDeltaMax_Object=MibTableColumn
cfprEtherLossStatsGiantsDeltaMax=_CfprEtherLossStatsGiantsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,22),_CfprEtherLossStatsGiantsDeltaMax_Type())
cfprEtherLossStatsGiantsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsGiantsDeltaMax.setStatus(_A)
_CfprEtherLossStatsGiantsDeltaMin_Type=Unsigned64
_CfprEtherLossStatsGiantsDeltaMin_Object=MibTableColumn
cfprEtherLossStatsGiantsDeltaMin=_CfprEtherLossStatsGiantsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,23),_CfprEtherLossStatsGiantsDeltaMin_Type())
cfprEtherLossStatsGiantsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsGiantsDeltaMin.setStatus(_A)
_CfprEtherLossStatsIntervals_Type=Gauge32
_CfprEtherLossStatsIntervals_Object=MibTableColumn
cfprEtherLossStatsIntervals=_CfprEtherLossStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,24),_CfprEtherLossStatsIntervals_Type())
cfprEtherLossStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsIntervals.setStatus(_A)
_CfprEtherLossStatsLateCollision_Type=Unsigned64
_CfprEtherLossStatsLateCollision_Object=MibTableColumn
cfprEtherLossStatsLateCollision=_CfprEtherLossStatsLateCollision_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,25),_CfprEtherLossStatsLateCollision_Type())
cfprEtherLossStatsLateCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsLateCollision.setStatus(_A)
_CfprEtherLossStatsLateCollisionDelta_Type=Counter64
_CfprEtherLossStatsLateCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsLateCollisionDelta=_CfprEtherLossStatsLateCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,26),_CfprEtherLossStatsLateCollisionDelta_Type())
cfprEtherLossStatsLateCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsLateCollisionDelta.setStatus(_A)
_CfprEtherLossStatsLateCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsLateCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsLateCollisionDeltaAvg=_CfprEtherLossStatsLateCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,27),_CfprEtherLossStatsLateCollisionDeltaAvg_Type())
cfprEtherLossStatsLateCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsLateCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsLateCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsLateCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsLateCollisionDeltaMax=_CfprEtherLossStatsLateCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,28),_CfprEtherLossStatsLateCollisionDeltaMax_Type())
cfprEtherLossStatsLateCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsLateCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsLateCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsLateCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsLateCollisionDeltaMin=_CfprEtherLossStatsLateCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,29),_CfprEtherLossStatsLateCollisionDeltaMin_Type())
cfprEtherLossStatsLateCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsLateCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsMultiCollision_Type=Unsigned64
_CfprEtherLossStatsMultiCollision_Object=MibTableColumn
cfprEtherLossStatsMultiCollision=_CfprEtherLossStatsMultiCollision_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,30),_CfprEtherLossStatsMultiCollision_Type())
cfprEtherLossStatsMultiCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsMultiCollision.setStatus(_A)
_CfprEtherLossStatsMultiCollisionDelta_Type=Counter64
_CfprEtherLossStatsMultiCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsMultiCollisionDelta=_CfprEtherLossStatsMultiCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,31),_CfprEtherLossStatsMultiCollisionDelta_Type())
cfprEtherLossStatsMultiCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsMultiCollisionDelta.setStatus(_A)
_CfprEtherLossStatsMultiCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsMultiCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsMultiCollisionDeltaAvg=_CfprEtherLossStatsMultiCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,32),_CfprEtherLossStatsMultiCollisionDeltaAvg_Type())
cfprEtherLossStatsMultiCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsMultiCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsMultiCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsMultiCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsMultiCollisionDeltaMax=_CfprEtherLossStatsMultiCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,33),_CfprEtherLossStatsMultiCollisionDeltaMax_Type())
cfprEtherLossStatsMultiCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsMultiCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsMultiCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsMultiCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsMultiCollisionDeltaMin=_CfprEtherLossStatsMultiCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,34),_CfprEtherLossStatsMultiCollisionDeltaMin_Type())
cfprEtherLossStatsMultiCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsMultiCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsSingleCollision_Type=Unsigned64
_CfprEtherLossStatsSingleCollision_Object=MibTableColumn
cfprEtherLossStatsSingleCollision=_CfprEtherLossStatsSingleCollision_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,35),_CfprEtherLossStatsSingleCollision_Type())
cfprEtherLossStatsSingleCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSingleCollision.setStatus(_A)
_CfprEtherLossStatsSingleCollisionDelta_Type=Counter64
_CfprEtherLossStatsSingleCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsSingleCollisionDelta=_CfprEtherLossStatsSingleCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,36),_CfprEtherLossStatsSingleCollisionDelta_Type())
cfprEtherLossStatsSingleCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSingleCollisionDelta.setStatus(_A)
_CfprEtherLossStatsSingleCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsSingleCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsSingleCollisionDeltaAvg=_CfprEtherLossStatsSingleCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,37),_CfprEtherLossStatsSingleCollisionDeltaAvg_Type())
cfprEtherLossStatsSingleCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSingleCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsSingleCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsSingleCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsSingleCollisionDeltaMax=_CfprEtherLossStatsSingleCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,38),_CfprEtherLossStatsSingleCollisionDeltaMax_Type())
cfprEtherLossStatsSingleCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSingleCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsSingleCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsSingleCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsSingleCollisionDeltaMin=_CfprEtherLossStatsSingleCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,39),_CfprEtherLossStatsSingleCollisionDeltaMin_Type())
cfprEtherLossStatsSingleCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSingleCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsSuspect_Type=TruthValue
_CfprEtherLossStatsSuspect_Object=MibTableColumn
cfprEtherLossStatsSuspect=_CfprEtherLossStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,40),_CfprEtherLossStatsSuspect_Type())
cfprEtherLossStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSuspect.setStatus(_A)
_CfprEtherLossStatsSymbol_Type=Unsigned64
_CfprEtherLossStatsSymbol_Object=MibTableColumn
cfprEtherLossStatsSymbol=_CfprEtherLossStatsSymbol_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,41),_CfprEtherLossStatsSymbol_Type())
cfprEtherLossStatsSymbol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSymbol.setStatus(_A)
_CfprEtherLossStatsSymbolDelta_Type=Counter64
_CfprEtherLossStatsSymbolDelta_Object=MibTableColumn
cfprEtherLossStatsSymbolDelta=_CfprEtherLossStatsSymbolDelta_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,42),_CfprEtherLossStatsSymbolDelta_Type())
cfprEtherLossStatsSymbolDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSymbolDelta.setStatus(_A)
_CfprEtherLossStatsSymbolDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsSymbolDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsSymbolDeltaAvg=_CfprEtherLossStatsSymbolDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,43),_CfprEtherLossStatsSymbolDeltaAvg_Type())
cfprEtherLossStatsSymbolDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSymbolDeltaAvg.setStatus(_A)
_CfprEtherLossStatsSymbolDeltaMax_Type=Unsigned64
_CfprEtherLossStatsSymbolDeltaMax_Object=MibTableColumn
cfprEtherLossStatsSymbolDeltaMax=_CfprEtherLossStatsSymbolDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,44),_CfprEtherLossStatsSymbolDeltaMax_Type())
cfprEtherLossStatsSymbolDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSymbolDeltaMax.setStatus(_A)
_CfprEtherLossStatsSymbolDeltaMin_Type=Unsigned64
_CfprEtherLossStatsSymbolDeltaMin_Object=MibTableColumn
cfprEtherLossStatsSymbolDeltaMin=_CfprEtherLossStatsSymbolDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,45),_CfprEtherLossStatsSymbolDeltaMin_Type())
cfprEtherLossStatsSymbolDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsSymbolDeltaMin.setStatus(_A)
_CfprEtherLossStatsThresholded_Type=CfprEtherLossStatsThresholded
_CfprEtherLossStatsThresholded_Object=MibTableColumn
cfprEtherLossStatsThresholded=_CfprEtherLossStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,46),_CfprEtherLossStatsThresholded_Type())
cfprEtherLossStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsThresholded.setStatus(_A)
_CfprEtherLossStatsTimeCollected_Type=DateAndTime
_CfprEtherLossStatsTimeCollected_Object=MibTableColumn
cfprEtherLossStatsTimeCollected=_CfprEtherLossStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,47),_CfprEtherLossStatsTimeCollected_Type())
cfprEtherLossStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsTimeCollected.setStatus(_A)
_CfprEtherLossStatsUpdate_Type=Gauge32
_CfprEtherLossStatsUpdate_Object=MibTableColumn
cfprEtherLossStatsUpdate=_CfprEtherLossStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,5,1,48),_CfprEtherLossStatsUpdate_Type())
cfprEtherLossStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsUpdate.setStatus(_A)
_CfprEtherLossStatsHistTable_Object=MibTable
cfprEtherLossStatsHistTable=_CfprEtherLossStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,6))
if mibBuilder.loadTexts:cfprEtherLossStatsHistTable.setStatus(_A)
_CfprEtherLossStatsHistEntry_Object=MibTableRow
cfprEtherLossStatsHistEntry=_CfprEtherLossStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,6,1))
cfprEtherLossStatsHistEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprEtherLossStatsHistEntry.setStatus(_A)
_CfprEtherLossStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherLossStatsHistInstanceId_Object=MibTableColumn
cfprEtherLossStatsHistInstanceId=_CfprEtherLossStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,1),_CfprEtherLossStatsHistInstanceId_Type())
cfprEtherLossStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherLossStatsHistInstanceId.setStatus(_A)
_CfprEtherLossStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherLossStatsHistDn_Object=MibTableColumn
cfprEtherLossStatsHistDn=_CfprEtherLossStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,2),_CfprEtherLossStatsHistDn_Type())
cfprEtherLossStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistDn.setStatus(_A)
_CfprEtherLossStatsHistRn_Type=SnmpAdminString
_CfprEtherLossStatsHistRn_Object=MibTableColumn
cfprEtherLossStatsHistRn=_CfprEtherLossStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,3),_CfprEtherLossStatsHistRn_Type())
cfprEtherLossStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistRn.setStatus(_A)
_CfprEtherLossStatsHistSQETest_Type=Unsigned64
_CfprEtherLossStatsHistSQETest_Object=MibTableColumn
cfprEtherLossStatsHistSQETest=_CfprEtherLossStatsHistSQETest_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,4),_CfprEtherLossStatsHistSQETest_Type())
cfprEtherLossStatsHistSQETest.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSQETest.setStatus(_A)
_CfprEtherLossStatsHistSQETestDelta_Type=Unsigned64
_CfprEtherLossStatsHistSQETestDelta_Object=MibTableColumn
cfprEtherLossStatsHistSQETestDelta=_CfprEtherLossStatsHistSQETestDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,5),_CfprEtherLossStatsHistSQETestDelta_Type())
cfprEtherLossStatsHistSQETestDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSQETestDelta.setStatus(_A)
_CfprEtherLossStatsHistSQETestDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistSQETestDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistSQETestDeltaAvg=_CfprEtherLossStatsHistSQETestDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,6),_CfprEtherLossStatsHistSQETestDeltaAvg_Type())
cfprEtherLossStatsHistSQETestDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSQETestDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistSQETestDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistSQETestDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistSQETestDeltaMax=_CfprEtherLossStatsHistSQETestDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,7),_CfprEtherLossStatsHistSQETestDeltaMax_Type())
cfprEtherLossStatsHistSQETestDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSQETestDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistSQETestDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistSQETestDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistSQETestDeltaMin=_CfprEtherLossStatsHistSQETestDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,8),_CfprEtherLossStatsHistSQETestDeltaMin_Type())
cfprEtherLossStatsHistSQETestDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSQETestDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistCarrierSense_Type=Unsigned64
_CfprEtherLossStatsHistCarrierSense_Object=MibTableColumn
cfprEtherLossStatsHistCarrierSense=_CfprEtherLossStatsHistCarrierSense_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,9),_CfprEtherLossStatsHistCarrierSense_Type())
cfprEtherLossStatsHistCarrierSense.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistCarrierSense.setStatus(_A)
_CfprEtherLossStatsHistCarrierSenseDelta_Type=Unsigned64
_CfprEtherLossStatsHistCarrierSenseDelta_Object=MibTableColumn
cfprEtherLossStatsHistCarrierSenseDelta=_CfprEtherLossStatsHistCarrierSenseDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,10),_CfprEtherLossStatsHistCarrierSenseDelta_Type())
cfprEtherLossStatsHistCarrierSenseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistCarrierSenseDelta.setStatus(_A)
_CfprEtherLossStatsHistCarrierSenseDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistCarrierSenseDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistCarrierSenseDeltaAvg=_CfprEtherLossStatsHistCarrierSenseDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,11),_CfprEtherLossStatsHistCarrierSenseDeltaAvg_Type())
cfprEtherLossStatsHistCarrierSenseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistCarrierSenseDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistCarrierSenseDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistCarrierSenseDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistCarrierSenseDeltaMax=_CfprEtherLossStatsHistCarrierSenseDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,12),_CfprEtherLossStatsHistCarrierSenseDeltaMax_Type())
cfprEtherLossStatsHistCarrierSenseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistCarrierSenseDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistCarrierSenseDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistCarrierSenseDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistCarrierSenseDeltaMin=_CfprEtherLossStatsHistCarrierSenseDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,13),_CfprEtherLossStatsHistCarrierSenseDeltaMin_Type())
cfprEtherLossStatsHistCarrierSenseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistCarrierSenseDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistExcessCollision_Type=Unsigned64
_CfprEtherLossStatsHistExcessCollision_Object=MibTableColumn
cfprEtherLossStatsHistExcessCollision=_CfprEtherLossStatsHistExcessCollision_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,14),_CfprEtherLossStatsHistExcessCollision_Type())
cfprEtherLossStatsHistExcessCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistExcessCollision.setStatus(_A)
_CfprEtherLossStatsHistExcessCollisionDelta_Type=Unsigned64
_CfprEtherLossStatsHistExcessCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsHistExcessCollisionDelta=_CfprEtherLossStatsHistExcessCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,15),_CfprEtherLossStatsHistExcessCollisionDelta_Type())
cfprEtherLossStatsHistExcessCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistExcessCollisionDelta.setStatus(_A)
_CfprEtherLossStatsHistExcessCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistExcessCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistExcessCollisionDeltaAvg=_CfprEtherLossStatsHistExcessCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,16),_CfprEtherLossStatsHistExcessCollisionDeltaAvg_Type())
cfprEtherLossStatsHistExcessCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistExcessCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistExcessCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistExcessCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistExcessCollisionDeltaMax=_CfprEtherLossStatsHistExcessCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,17),_CfprEtherLossStatsHistExcessCollisionDeltaMax_Type())
cfprEtherLossStatsHistExcessCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistExcessCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistExcessCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistExcessCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistExcessCollisionDeltaMin=_CfprEtherLossStatsHistExcessCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,18),_CfprEtherLossStatsHistExcessCollisionDeltaMin_Type())
cfprEtherLossStatsHistExcessCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistExcessCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistGiants_Type=Unsigned64
_CfprEtherLossStatsHistGiants_Object=MibTableColumn
cfprEtherLossStatsHistGiants=_CfprEtherLossStatsHistGiants_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,19),_CfprEtherLossStatsHistGiants_Type())
cfprEtherLossStatsHistGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistGiants.setStatus(_A)
_CfprEtherLossStatsHistGiantsDelta_Type=Unsigned64
_CfprEtherLossStatsHistGiantsDelta_Object=MibTableColumn
cfprEtherLossStatsHistGiantsDelta=_CfprEtherLossStatsHistGiantsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,20),_CfprEtherLossStatsHistGiantsDelta_Type())
cfprEtherLossStatsHistGiantsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistGiantsDelta.setStatus(_A)
_CfprEtherLossStatsHistGiantsDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistGiantsDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistGiantsDeltaAvg=_CfprEtherLossStatsHistGiantsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,21),_CfprEtherLossStatsHistGiantsDeltaAvg_Type())
cfprEtherLossStatsHistGiantsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistGiantsDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistGiantsDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistGiantsDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistGiantsDeltaMax=_CfprEtherLossStatsHistGiantsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,22),_CfprEtherLossStatsHistGiantsDeltaMax_Type())
cfprEtherLossStatsHistGiantsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistGiantsDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistGiantsDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistGiantsDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistGiantsDeltaMin=_CfprEtherLossStatsHistGiantsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,23),_CfprEtherLossStatsHistGiantsDeltaMin_Type())
cfprEtherLossStatsHistGiantsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistGiantsDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistId_Type=Unsigned64
_CfprEtherLossStatsHistId_Object=MibTableColumn
cfprEtherLossStatsHistId=_CfprEtherLossStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,24),_CfprEtherLossStatsHistId_Type())
cfprEtherLossStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistId.setStatus(_A)
_CfprEtherLossStatsHistLateCollision_Type=Unsigned64
_CfprEtherLossStatsHistLateCollision_Object=MibTableColumn
cfprEtherLossStatsHistLateCollision=_CfprEtherLossStatsHistLateCollision_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,25),_CfprEtherLossStatsHistLateCollision_Type())
cfprEtherLossStatsHistLateCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistLateCollision.setStatus(_A)
_CfprEtherLossStatsHistLateCollisionDelta_Type=Unsigned64
_CfprEtherLossStatsHistLateCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsHistLateCollisionDelta=_CfprEtherLossStatsHistLateCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,26),_CfprEtherLossStatsHistLateCollisionDelta_Type())
cfprEtherLossStatsHistLateCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistLateCollisionDelta.setStatus(_A)
_CfprEtherLossStatsHistLateCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistLateCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistLateCollisionDeltaAvg=_CfprEtherLossStatsHistLateCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,27),_CfprEtherLossStatsHistLateCollisionDeltaAvg_Type())
cfprEtherLossStatsHistLateCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistLateCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistLateCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistLateCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistLateCollisionDeltaMax=_CfprEtherLossStatsHistLateCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,28),_CfprEtherLossStatsHistLateCollisionDeltaMax_Type())
cfprEtherLossStatsHistLateCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistLateCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistLateCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistLateCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistLateCollisionDeltaMin=_CfprEtherLossStatsHistLateCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,29),_CfprEtherLossStatsHistLateCollisionDeltaMin_Type())
cfprEtherLossStatsHistLateCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistLateCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistMostRecent_Type=TruthValue
_CfprEtherLossStatsHistMostRecent_Object=MibTableColumn
cfprEtherLossStatsHistMostRecent=_CfprEtherLossStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,30),_CfprEtherLossStatsHistMostRecent_Type())
cfprEtherLossStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistMostRecent.setStatus(_A)
_CfprEtherLossStatsHistMultiCollision_Type=Unsigned64
_CfprEtherLossStatsHistMultiCollision_Object=MibTableColumn
cfprEtherLossStatsHistMultiCollision=_CfprEtherLossStatsHistMultiCollision_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,31),_CfprEtherLossStatsHistMultiCollision_Type())
cfprEtherLossStatsHistMultiCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistMultiCollision.setStatus(_A)
_CfprEtherLossStatsHistMultiCollisionDelta_Type=Unsigned64
_CfprEtherLossStatsHistMultiCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsHistMultiCollisionDelta=_CfprEtherLossStatsHistMultiCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,32),_CfprEtherLossStatsHistMultiCollisionDelta_Type())
cfprEtherLossStatsHistMultiCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistMultiCollisionDelta.setStatus(_A)
_CfprEtherLossStatsHistMultiCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistMultiCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistMultiCollisionDeltaAvg=_CfprEtherLossStatsHistMultiCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,33),_CfprEtherLossStatsHistMultiCollisionDeltaAvg_Type())
cfprEtherLossStatsHistMultiCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistMultiCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistMultiCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistMultiCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistMultiCollisionDeltaMax=_CfprEtherLossStatsHistMultiCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,34),_CfprEtherLossStatsHistMultiCollisionDeltaMax_Type())
cfprEtherLossStatsHistMultiCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistMultiCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistMultiCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistMultiCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistMultiCollisionDeltaMin=_CfprEtherLossStatsHistMultiCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,35),_CfprEtherLossStatsHistMultiCollisionDeltaMin_Type())
cfprEtherLossStatsHistMultiCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistMultiCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistSingleCollision_Type=Unsigned64
_CfprEtherLossStatsHistSingleCollision_Object=MibTableColumn
cfprEtherLossStatsHistSingleCollision=_CfprEtherLossStatsHistSingleCollision_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,36),_CfprEtherLossStatsHistSingleCollision_Type())
cfprEtherLossStatsHistSingleCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSingleCollision.setStatus(_A)
_CfprEtherLossStatsHistSingleCollisionDelta_Type=Unsigned64
_CfprEtherLossStatsHistSingleCollisionDelta_Object=MibTableColumn
cfprEtherLossStatsHistSingleCollisionDelta=_CfprEtherLossStatsHistSingleCollisionDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,37),_CfprEtherLossStatsHistSingleCollisionDelta_Type())
cfprEtherLossStatsHistSingleCollisionDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSingleCollisionDelta.setStatus(_A)
_CfprEtherLossStatsHistSingleCollisionDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistSingleCollisionDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistSingleCollisionDeltaAvg=_CfprEtherLossStatsHistSingleCollisionDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,38),_CfprEtherLossStatsHistSingleCollisionDeltaAvg_Type())
cfprEtherLossStatsHistSingleCollisionDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSingleCollisionDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistSingleCollisionDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistSingleCollisionDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistSingleCollisionDeltaMax=_CfprEtherLossStatsHistSingleCollisionDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,39),_CfprEtherLossStatsHistSingleCollisionDeltaMax_Type())
cfprEtherLossStatsHistSingleCollisionDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSingleCollisionDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistSingleCollisionDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistSingleCollisionDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistSingleCollisionDeltaMin=_CfprEtherLossStatsHistSingleCollisionDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,40),_CfprEtherLossStatsHistSingleCollisionDeltaMin_Type())
cfprEtherLossStatsHistSingleCollisionDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSingleCollisionDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistSuspect_Type=TruthValue
_CfprEtherLossStatsHistSuspect_Object=MibTableColumn
cfprEtherLossStatsHistSuspect=_CfprEtherLossStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,41),_CfprEtherLossStatsHistSuspect_Type())
cfprEtherLossStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSuspect.setStatus(_A)
_CfprEtherLossStatsHistSymbol_Type=Unsigned64
_CfprEtherLossStatsHistSymbol_Object=MibTableColumn
cfprEtherLossStatsHistSymbol=_CfprEtherLossStatsHistSymbol_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,42),_CfprEtherLossStatsHistSymbol_Type())
cfprEtherLossStatsHistSymbol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSymbol.setStatus(_A)
_CfprEtherLossStatsHistSymbolDelta_Type=Unsigned64
_CfprEtherLossStatsHistSymbolDelta_Object=MibTableColumn
cfprEtherLossStatsHistSymbolDelta=_CfprEtherLossStatsHistSymbolDelta_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,43),_CfprEtherLossStatsHistSymbolDelta_Type())
cfprEtherLossStatsHistSymbolDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSymbolDelta.setStatus(_A)
_CfprEtherLossStatsHistSymbolDeltaAvg_Type=Unsigned64
_CfprEtherLossStatsHistSymbolDeltaAvg_Object=MibTableColumn
cfprEtherLossStatsHistSymbolDeltaAvg=_CfprEtherLossStatsHistSymbolDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,44),_CfprEtherLossStatsHistSymbolDeltaAvg_Type())
cfprEtherLossStatsHistSymbolDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSymbolDeltaAvg.setStatus(_A)
_CfprEtherLossStatsHistSymbolDeltaMax_Type=Unsigned64
_CfprEtherLossStatsHistSymbolDeltaMax_Object=MibTableColumn
cfprEtherLossStatsHistSymbolDeltaMax=_CfprEtherLossStatsHistSymbolDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,45),_CfprEtherLossStatsHistSymbolDeltaMax_Type())
cfprEtherLossStatsHistSymbolDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSymbolDeltaMax.setStatus(_A)
_CfprEtherLossStatsHistSymbolDeltaMin_Type=Unsigned64
_CfprEtherLossStatsHistSymbolDeltaMin_Object=MibTableColumn
cfprEtherLossStatsHistSymbolDeltaMin=_CfprEtherLossStatsHistSymbolDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,46),_CfprEtherLossStatsHistSymbolDeltaMin_Type())
cfprEtherLossStatsHistSymbolDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistSymbolDeltaMin.setStatus(_A)
_CfprEtherLossStatsHistThresholded_Type=CfprEtherLossStatsHistThresholded
_CfprEtherLossStatsHistThresholded_Object=MibTableColumn
cfprEtherLossStatsHistThresholded=_CfprEtherLossStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,47),_CfprEtherLossStatsHistThresholded_Type())
cfprEtherLossStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistThresholded.setStatus(_A)
_CfprEtherLossStatsHistTimeCollected_Type=DateAndTime
_CfprEtherLossStatsHistTimeCollected_Object=MibTableColumn
cfprEtherLossStatsHistTimeCollected=_CfprEtherLossStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,6,1,48),_CfprEtherLossStatsHistTimeCollected_Type())
cfprEtherLossStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherLossStatsHistTimeCollected.setStatus(_A)
_CfprEtherNiErrStatsTable_Object=MibTable
cfprEtherNiErrStatsTable=_CfprEtherNiErrStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,7))
if mibBuilder.loadTexts:cfprEtherNiErrStatsTable.setStatus(_A)
_CfprEtherNiErrStatsEntry_Object=MibTableRow
cfprEtherNiErrStatsEntry=_CfprEtherNiErrStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,7,1))
cfprEtherNiErrStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprEtherNiErrStatsEntry.setStatus(_A)
_CfprEtherNiErrStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherNiErrStatsInstanceId_Object=MibTableColumn
cfprEtherNiErrStatsInstanceId=_CfprEtherNiErrStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,1),_CfprEtherNiErrStatsInstanceId_Type())
cfprEtherNiErrStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherNiErrStatsInstanceId.setStatus(_A)
_CfprEtherNiErrStatsDn_Type=CfprManagedObjectDn
_CfprEtherNiErrStatsDn_Object=MibTableColumn
cfprEtherNiErrStatsDn=_CfprEtherNiErrStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,2),_CfprEtherNiErrStatsDn_Type())
cfprEtherNiErrStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsDn.setStatus(_A)
_CfprEtherNiErrStatsRn_Type=SnmpAdminString
_CfprEtherNiErrStatsRn_Object=MibTableColumn
cfprEtherNiErrStatsRn=_CfprEtherNiErrStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,3),_CfprEtherNiErrStatsRn_Type())
cfprEtherNiErrStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsRn.setStatus(_A)
_CfprEtherNiErrStatsCrc_Type=Unsigned64
_CfprEtherNiErrStatsCrc_Object=MibTableColumn
cfprEtherNiErrStatsCrc=_CfprEtherNiErrStatsCrc_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,4),_CfprEtherNiErrStatsCrc_Type())
cfprEtherNiErrStatsCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsCrc.setStatus(_A)
_CfprEtherNiErrStatsCrcDelta_Type=Counter64
_CfprEtherNiErrStatsCrcDelta_Object=MibTableColumn
cfprEtherNiErrStatsCrcDelta=_CfprEtherNiErrStatsCrcDelta_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,5),_CfprEtherNiErrStatsCrcDelta_Type())
cfprEtherNiErrStatsCrcDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsCrcDelta.setStatus(_A)
_CfprEtherNiErrStatsCrcDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsCrcDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsCrcDeltaAvg=_CfprEtherNiErrStatsCrcDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,6),_CfprEtherNiErrStatsCrcDeltaAvg_Type())
cfprEtherNiErrStatsCrcDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsCrcDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsCrcDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsCrcDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsCrcDeltaMax=_CfprEtherNiErrStatsCrcDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,7),_CfprEtherNiErrStatsCrcDeltaMax_Type())
cfprEtherNiErrStatsCrcDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsCrcDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsCrcDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsCrcDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsCrcDeltaMin=_CfprEtherNiErrStatsCrcDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,8),_CfprEtherNiErrStatsCrcDeltaMin_Type())
cfprEtherNiErrStatsCrcDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsCrcDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsFrameTx_Type=Unsigned64
_CfprEtherNiErrStatsFrameTx_Object=MibTableColumn
cfprEtherNiErrStatsFrameTx=_CfprEtherNiErrStatsFrameTx_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,9),_CfprEtherNiErrStatsFrameTx_Type())
cfprEtherNiErrStatsFrameTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsFrameTx.setStatus(_A)
_CfprEtherNiErrStatsFrameTxDelta_Type=Counter64
_CfprEtherNiErrStatsFrameTxDelta_Object=MibTableColumn
cfprEtherNiErrStatsFrameTxDelta=_CfprEtherNiErrStatsFrameTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,10),_CfprEtherNiErrStatsFrameTxDelta_Type())
cfprEtherNiErrStatsFrameTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsFrameTxDelta.setStatus(_A)
_CfprEtherNiErrStatsFrameTxDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsFrameTxDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsFrameTxDeltaAvg=_CfprEtherNiErrStatsFrameTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,11),_CfprEtherNiErrStatsFrameTxDeltaAvg_Type())
cfprEtherNiErrStatsFrameTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsFrameTxDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsFrameTxDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsFrameTxDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsFrameTxDeltaMax=_CfprEtherNiErrStatsFrameTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,12),_CfprEtherNiErrStatsFrameTxDeltaMax_Type())
cfprEtherNiErrStatsFrameTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsFrameTxDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsFrameTxDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsFrameTxDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsFrameTxDeltaMin=_CfprEtherNiErrStatsFrameTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,13),_CfprEtherNiErrStatsFrameTxDeltaMin_Type())
cfprEtherNiErrStatsFrameTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsFrameTxDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsInRange_Type=Unsigned64
_CfprEtherNiErrStatsInRange_Object=MibTableColumn
cfprEtherNiErrStatsInRange=_CfprEtherNiErrStatsInRange_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,14),_CfprEtherNiErrStatsInRange_Type())
cfprEtherNiErrStatsInRange.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsInRange.setStatus(_A)
_CfprEtherNiErrStatsInRangeDelta_Type=Counter64
_CfprEtherNiErrStatsInRangeDelta_Object=MibTableColumn
cfprEtherNiErrStatsInRangeDelta=_CfprEtherNiErrStatsInRangeDelta_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,15),_CfprEtherNiErrStatsInRangeDelta_Type())
cfprEtherNiErrStatsInRangeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsInRangeDelta.setStatus(_A)
_CfprEtherNiErrStatsInRangeDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsInRangeDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsInRangeDeltaAvg=_CfprEtherNiErrStatsInRangeDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,16),_CfprEtherNiErrStatsInRangeDeltaAvg_Type())
cfprEtherNiErrStatsInRangeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsInRangeDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsInRangeDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsInRangeDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsInRangeDeltaMax=_CfprEtherNiErrStatsInRangeDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,17),_CfprEtherNiErrStatsInRangeDeltaMax_Type())
cfprEtherNiErrStatsInRangeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsInRangeDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsInRangeDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsInRangeDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsInRangeDeltaMin=_CfprEtherNiErrStatsInRangeDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,18),_CfprEtherNiErrStatsInRangeDeltaMin_Type())
cfprEtherNiErrStatsInRangeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsInRangeDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsIntervals_Type=Gauge32
_CfprEtherNiErrStatsIntervals_Object=MibTableColumn
cfprEtherNiErrStatsIntervals=_CfprEtherNiErrStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,19),_CfprEtherNiErrStatsIntervals_Type())
cfprEtherNiErrStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsIntervals.setStatus(_A)
_CfprEtherNiErrStatsSuspect_Type=TruthValue
_CfprEtherNiErrStatsSuspect_Object=MibTableColumn
cfprEtherNiErrStatsSuspect=_CfprEtherNiErrStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,20),_CfprEtherNiErrStatsSuspect_Type())
cfprEtherNiErrStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsSuspect.setStatus(_A)
_CfprEtherNiErrStatsThresholded_Type=CfprEtherNiErrStatsThresholded
_CfprEtherNiErrStatsThresholded_Object=MibTableColumn
cfprEtherNiErrStatsThresholded=_CfprEtherNiErrStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,21),_CfprEtherNiErrStatsThresholded_Type())
cfprEtherNiErrStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsThresholded.setStatus(_A)
_CfprEtherNiErrStatsTimeCollected_Type=DateAndTime
_CfprEtherNiErrStatsTimeCollected_Object=MibTableColumn
cfprEtherNiErrStatsTimeCollected=_CfprEtherNiErrStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,22),_CfprEtherNiErrStatsTimeCollected_Type())
cfprEtherNiErrStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTimeCollected.setStatus(_A)
_CfprEtherNiErrStatsTooLong_Type=Unsigned64
_CfprEtherNiErrStatsTooLong_Object=MibTableColumn
cfprEtherNiErrStatsTooLong=_CfprEtherNiErrStatsTooLong_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,23),_CfprEtherNiErrStatsTooLong_Type())
cfprEtherNiErrStatsTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooLong.setStatus(_A)
_CfprEtherNiErrStatsTooLongDelta_Type=Counter64
_CfprEtherNiErrStatsTooLongDelta_Object=MibTableColumn
cfprEtherNiErrStatsTooLongDelta=_CfprEtherNiErrStatsTooLongDelta_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,24),_CfprEtherNiErrStatsTooLongDelta_Type())
cfprEtherNiErrStatsTooLongDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooLongDelta.setStatus(_A)
_CfprEtherNiErrStatsTooLongDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsTooLongDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsTooLongDeltaAvg=_CfprEtherNiErrStatsTooLongDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,25),_CfprEtherNiErrStatsTooLongDeltaAvg_Type())
cfprEtherNiErrStatsTooLongDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooLongDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsTooLongDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsTooLongDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsTooLongDeltaMax=_CfprEtherNiErrStatsTooLongDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,26),_CfprEtherNiErrStatsTooLongDeltaMax_Type())
cfprEtherNiErrStatsTooLongDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooLongDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsTooLongDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsTooLongDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsTooLongDeltaMin=_CfprEtherNiErrStatsTooLongDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,27),_CfprEtherNiErrStatsTooLongDeltaMin_Type())
cfprEtherNiErrStatsTooLongDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooLongDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsTooShort_Type=Unsigned64
_CfprEtherNiErrStatsTooShort_Object=MibTableColumn
cfprEtherNiErrStatsTooShort=_CfprEtherNiErrStatsTooShort_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,28),_CfprEtherNiErrStatsTooShort_Type())
cfprEtherNiErrStatsTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooShort.setStatus(_A)
_CfprEtherNiErrStatsTooShortDelta_Type=Counter64
_CfprEtherNiErrStatsTooShortDelta_Object=MibTableColumn
cfprEtherNiErrStatsTooShortDelta=_CfprEtherNiErrStatsTooShortDelta_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,29),_CfprEtherNiErrStatsTooShortDelta_Type())
cfprEtherNiErrStatsTooShortDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooShortDelta.setStatus(_A)
_CfprEtherNiErrStatsTooShortDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsTooShortDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsTooShortDeltaAvg=_CfprEtherNiErrStatsTooShortDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,30),_CfprEtherNiErrStatsTooShortDeltaAvg_Type())
cfprEtherNiErrStatsTooShortDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooShortDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsTooShortDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsTooShortDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsTooShortDeltaMax=_CfprEtherNiErrStatsTooShortDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,31),_CfprEtherNiErrStatsTooShortDeltaMax_Type())
cfprEtherNiErrStatsTooShortDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooShortDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsTooShortDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsTooShortDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsTooShortDeltaMin=_CfprEtherNiErrStatsTooShortDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,32),_CfprEtherNiErrStatsTooShortDeltaMin_Type())
cfprEtherNiErrStatsTooShortDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsTooShortDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsUpdate_Type=Gauge32
_CfprEtherNiErrStatsUpdate_Object=MibTableColumn
cfprEtherNiErrStatsUpdate=_CfprEtherNiErrStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,7,1,33),_CfprEtherNiErrStatsUpdate_Type())
cfprEtherNiErrStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsUpdate.setStatus(_A)
_CfprEtherNiErrStatsHistTable_Object=MibTable
cfprEtherNiErrStatsHistTable=_CfprEtherNiErrStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,8))
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTable.setStatus(_A)
_CfprEtherNiErrStatsHistEntry_Object=MibTableRow
cfprEtherNiErrStatsHistEntry=_CfprEtherNiErrStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,8,1))
cfprEtherNiErrStatsHistEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistEntry.setStatus(_A)
_CfprEtherNiErrStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherNiErrStatsHistInstanceId_Object=MibTableColumn
cfprEtherNiErrStatsHistInstanceId=_CfprEtherNiErrStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,1),_CfprEtherNiErrStatsHistInstanceId_Type())
cfprEtherNiErrStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistInstanceId.setStatus(_A)
_CfprEtherNiErrStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherNiErrStatsHistDn_Object=MibTableColumn
cfprEtherNiErrStatsHistDn=_CfprEtherNiErrStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,2),_CfprEtherNiErrStatsHistDn_Type())
cfprEtherNiErrStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistDn.setStatus(_A)
_CfprEtherNiErrStatsHistRn_Type=SnmpAdminString
_CfprEtherNiErrStatsHistRn_Object=MibTableColumn
cfprEtherNiErrStatsHistRn=_CfprEtherNiErrStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,3),_CfprEtherNiErrStatsHistRn_Type())
cfprEtherNiErrStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistRn.setStatus(_A)
_CfprEtherNiErrStatsHistCrc_Type=Unsigned64
_CfprEtherNiErrStatsHistCrc_Object=MibTableColumn
cfprEtherNiErrStatsHistCrc=_CfprEtherNiErrStatsHistCrc_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,4),_CfprEtherNiErrStatsHistCrc_Type())
cfprEtherNiErrStatsHistCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistCrc.setStatus(_A)
_CfprEtherNiErrStatsHistCrcDelta_Type=Unsigned64
_CfprEtherNiErrStatsHistCrcDelta_Object=MibTableColumn
cfprEtherNiErrStatsHistCrcDelta=_CfprEtherNiErrStatsHistCrcDelta_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,5),_CfprEtherNiErrStatsHistCrcDelta_Type())
cfprEtherNiErrStatsHistCrcDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistCrcDelta.setStatus(_A)
_CfprEtherNiErrStatsHistCrcDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsHistCrcDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsHistCrcDeltaAvg=_CfprEtherNiErrStatsHistCrcDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,6),_CfprEtherNiErrStatsHistCrcDeltaAvg_Type())
cfprEtherNiErrStatsHistCrcDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistCrcDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsHistCrcDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsHistCrcDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsHistCrcDeltaMax=_CfprEtherNiErrStatsHistCrcDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,7),_CfprEtherNiErrStatsHistCrcDeltaMax_Type())
cfprEtherNiErrStatsHistCrcDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistCrcDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsHistCrcDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsHistCrcDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsHistCrcDeltaMin=_CfprEtherNiErrStatsHistCrcDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,8),_CfprEtherNiErrStatsHistCrcDeltaMin_Type())
cfprEtherNiErrStatsHistCrcDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistCrcDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsHistFrameTx_Type=Unsigned64
_CfprEtherNiErrStatsHistFrameTx_Object=MibTableColumn
cfprEtherNiErrStatsHistFrameTx=_CfprEtherNiErrStatsHistFrameTx_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,9),_CfprEtherNiErrStatsHistFrameTx_Type())
cfprEtherNiErrStatsHistFrameTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistFrameTx.setStatus(_A)
_CfprEtherNiErrStatsHistFrameTxDelta_Type=Unsigned64
_CfprEtherNiErrStatsHistFrameTxDelta_Object=MibTableColumn
cfprEtherNiErrStatsHistFrameTxDelta=_CfprEtherNiErrStatsHistFrameTxDelta_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,10),_CfprEtherNiErrStatsHistFrameTxDelta_Type())
cfprEtherNiErrStatsHistFrameTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistFrameTxDelta.setStatus(_A)
_CfprEtherNiErrStatsHistFrameTxDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsHistFrameTxDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsHistFrameTxDeltaAvg=_CfprEtherNiErrStatsHistFrameTxDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,11),_CfprEtherNiErrStatsHistFrameTxDeltaAvg_Type())
cfprEtherNiErrStatsHistFrameTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistFrameTxDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsHistFrameTxDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsHistFrameTxDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsHistFrameTxDeltaMax=_CfprEtherNiErrStatsHistFrameTxDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,12),_CfprEtherNiErrStatsHistFrameTxDeltaMax_Type())
cfprEtherNiErrStatsHistFrameTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistFrameTxDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsHistFrameTxDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsHistFrameTxDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsHistFrameTxDeltaMin=_CfprEtherNiErrStatsHistFrameTxDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,13),_CfprEtherNiErrStatsHistFrameTxDeltaMin_Type())
cfprEtherNiErrStatsHistFrameTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistFrameTxDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsHistId_Type=Unsigned64
_CfprEtherNiErrStatsHistId_Object=MibTableColumn
cfprEtherNiErrStatsHistId=_CfprEtherNiErrStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,14),_CfprEtherNiErrStatsHistId_Type())
cfprEtherNiErrStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistId.setStatus(_A)
_CfprEtherNiErrStatsHistInRange_Type=Unsigned64
_CfprEtherNiErrStatsHistInRange_Object=MibTableColumn
cfprEtherNiErrStatsHistInRange=_CfprEtherNiErrStatsHistInRange_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,15),_CfprEtherNiErrStatsHistInRange_Type())
cfprEtherNiErrStatsHistInRange.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistInRange.setStatus(_A)
_CfprEtherNiErrStatsHistInRangeDelta_Type=Unsigned64
_CfprEtherNiErrStatsHistInRangeDelta_Object=MibTableColumn
cfprEtherNiErrStatsHistInRangeDelta=_CfprEtherNiErrStatsHistInRangeDelta_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,16),_CfprEtherNiErrStatsHistInRangeDelta_Type())
cfprEtherNiErrStatsHistInRangeDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistInRangeDelta.setStatus(_A)
_CfprEtherNiErrStatsHistInRangeDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsHistInRangeDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsHistInRangeDeltaAvg=_CfprEtherNiErrStatsHistInRangeDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,17),_CfprEtherNiErrStatsHistInRangeDeltaAvg_Type())
cfprEtherNiErrStatsHistInRangeDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistInRangeDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsHistInRangeDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsHistInRangeDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsHistInRangeDeltaMax=_CfprEtherNiErrStatsHistInRangeDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,18),_CfprEtherNiErrStatsHistInRangeDeltaMax_Type())
cfprEtherNiErrStatsHistInRangeDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistInRangeDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsHistInRangeDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsHistInRangeDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsHistInRangeDeltaMin=_CfprEtherNiErrStatsHistInRangeDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,19),_CfprEtherNiErrStatsHistInRangeDeltaMin_Type())
cfprEtherNiErrStatsHistInRangeDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistInRangeDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsHistMostRecent_Type=TruthValue
_CfprEtherNiErrStatsHistMostRecent_Object=MibTableColumn
cfprEtherNiErrStatsHistMostRecent=_CfprEtherNiErrStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,20),_CfprEtherNiErrStatsHistMostRecent_Type())
cfprEtherNiErrStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistMostRecent.setStatus(_A)
_CfprEtherNiErrStatsHistSuspect_Type=TruthValue
_CfprEtherNiErrStatsHistSuspect_Object=MibTableColumn
cfprEtherNiErrStatsHistSuspect=_CfprEtherNiErrStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,21),_CfprEtherNiErrStatsHistSuspect_Type())
cfprEtherNiErrStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistSuspect.setStatus(_A)
_CfprEtherNiErrStatsHistThresholded_Type=CfprEtherNiErrStatsHistThresholded
_CfprEtherNiErrStatsHistThresholded_Object=MibTableColumn
cfprEtherNiErrStatsHistThresholded=_CfprEtherNiErrStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,22),_CfprEtherNiErrStatsHistThresholded_Type())
cfprEtherNiErrStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistThresholded.setStatus(_A)
_CfprEtherNiErrStatsHistTimeCollected_Type=DateAndTime
_CfprEtherNiErrStatsHistTimeCollected_Object=MibTableColumn
cfprEtherNiErrStatsHistTimeCollected=_CfprEtherNiErrStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,23),_CfprEtherNiErrStatsHistTimeCollected_Type())
cfprEtherNiErrStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTimeCollected.setStatus(_A)
_CfprEtherNiErrStatsHistTooLong_Type=Unsigned64
_CfprEtherNiErrStatsHistTooLong_Object=MibTableColumn
cfprEtherNiErrStatsHistTooLong=_CfprEtherNiErrStatsHistTooLong_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,24),_CfprEtherNiErrStatsHistTooLong_Type())
cfprEtherNiErrStatsHistTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooLong.setStatus(_A)
_CfprEtherNiErrStatsHistTooLongDelta_Type=Unsigned64
_CfprEtherNiErrStatsHistTooLongDelta_Object=MibTableColumn
cfprEtherNiErrStatsHistTooLongDelta=_CfprEtherNiErrStatsHistTooLongDelta_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,25),_CfprEtherNiErrStatsHistTooLongDelta_Type())
cfprEtherNiErrStatsHistTooLongDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooLongDelta.setStatus(_A)
_CfprEtherNiErrStatsHistTooLongDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsHistTooLongDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsHistTooLongDeltaAvg=_CfprEtherNiErrStatsHistTooLongDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,26),_CfprEtherNiErrStatsHistTooLongDeltaAvg_Type())
cfprEtherNiErrStatsHistTooLongDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooLongDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsHistTooLongDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsHistTooLongDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsHistTooLongDeltaMax=_CfprEtherNiErrStatsHistTooLongDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,27),_CfprEtherNiErrStatsHistTooLongDeltaMax_Type())
cfprEtherNiErrStatsHistTooLongDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooLongDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsHistTooLongDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsHistTooLongDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsHistTooLongDeltaMin=_CfprEtherNiErrStatsHistTooLongDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,28),_CfprEtherNiErrStatsHistTooLongDeltaMin_Type())
cfprEtherNiErrStatsHistTooLongDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooLongDeltaMin.setStatus(_A)
_CfprEtherNiErrStatsHistTooShort_Type=Unsigned64
_CfprEtherNiErrStatsHistTooShort_Object=MibTableColumn
cfprEtherNiErrStatsHistTooShort=_CfprEtherNiErrStatsHistTooShort_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,29),_CfprEtherNiErrStatsHistTooShort_Type())
cfprEtherNiErrStatsHistTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooShort.setStatus(_A)
_CfprEtherNiErrStatsHistTooShortDelta_Type=Unsigned64
_CfprEtherNiErrStatsHistTooShortDelta_Object=MibTableColumn
cfprEtherNiErrStatsHistTooShortDelta=_CfprEtherNiErrStatsHistTooShortDelta_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,30),_CfprEtherNiErrStatsHistTooShortDelta_Type())
cfprEtherNiErrStatsHistTooShortDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooShortDelta.setStatus(_A)
_CfprEtherNiErrStatsHistTooShortDeltaAvg_Type=Unsigned64
_CfprEtherNiErrStatsHistTooShortDeltaAvg_Object=MibTableColumn
cfprEtherNiErrStatsHistTooShortDeltaAvg=_CfprEtherNiErrStatsHistTooShortDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,31),_CfprEtherNiErrStatsHistTooShortDeltaAvg_Type())
cfprEtherNiErrStatsHistTooShortDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooShortDeltaAvg.setStatus(_A)
_CfprEtherNiErrStatsHistTooShortDeltaMax_Type=Unsigned64
_CfprEtherNiErrStatsHistTooShortDeltaMax_Object=MibTableColumn
cfprEtherNiErrStatsHistTooShortDeltaMax=_CfprEtherNiErrStatsHistTooShortDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,32),_CfprEtherNiErrStatsHistTooShortDeltaMax_Type())
cfprEtherNiErrStatsHistTooShortDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooShortDeltaMax.setStatus(_A)
_CfprEtherNiErrStatsHistTooShortDeltaMin_Type=Unsigned64
_CfprEtherNiErrStatsHistTooShortDeltaMin_Object=MibTableColumn
cfprEtherNiErrStatsHistTooShortDeltaMin=_CfprEtherNiErrStatsHistTooShortDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,8,1,33),_CfprEtherNiErrStatsHistTooShortDeltaMin_Type())
cfprEtherNiErrStatsHistTooShortDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNiErrStatsHistTooShortDeltaMin.setStatus(_A)
_CfprEtherNicIfConfigTable_Object=MibTable
cfprEtherNicIfConfigTable=_CfprEtherNicIfConfigTable_Object((1,3,6,1,4,1,9,9,826,1,21,9))
if mibBuilder.loadTexts:cfprEtherNicIfConfigTable.setStatus(_A)
_CfprEtherNicIfConfigEntry_Object=MibTableRow
cfprEtherNicIfConfigEntry=_CfprEtherNicIfConfigEntry_Object((1,3,6,1,4,1,9,9,826,1,21,9,1))
cfprEtherNicIfConfigEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprEtherNicIfConfigEntry.setStatus(_A)
_CfprEtherNicIfConfigInstanceId_Type=CfprManagedObjectId
_CfprEtherNicIfConfigInstanceId_Object=MibTableColumn
cfprEtherNicIfConfigInstanceId=_CfprEtherNicIfConfigInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,9,1,1),_CfprEtherNicIfConfigInstanceId_Type())
cfprEtherNicIfConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherNicIfConfigInstanceId.setStatus(_A)
_CfprEtherNicIfConfigDn_Type=CfprManagedObjectDn
_CfprEtherNicIfConfigDn_Object=MibTableColumn
cfprEtherNicIfConfigDn=_CfprEtherNicIfConfigDn_Object((1,3,6,1,4,1,9,9,826,1,21,9,1,2),_CfprEtherNicIfConfigDn_Type())
cfprEtherNicIfConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNicIfConfigDn.setStatus(_A)
_CfprEtherNicIfConfigRn_Type=SnmpAdminString
_CfprEtherNicIfConfigRn_Object=MibTableColumn
cfprEtherNicIfConfigRn=_CfprEtherNicIfConfigRn_Object((1,3,6,1,4,1,9,9,826,1,21,9,1,3),_CfprEtherNicIfConfigRn_Type())
cfprEtherNicIfConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherNicIfConfigRn.setStatus(_A)
_CfprEtherPIoTable_Object=MibTable
cfprEtherPIoTable=_CfprEtherPIoTable_Object((1,3,6,1,4,1,9,9,826,1,21,10))
if mibBuilder.loadTexts:cfprEtherPIoTable.setStatus(_A)
_CfprEtherPIoEntry_Object=MibTableRow
cfprEtherPIoEntry=_CfprEtherPIoEntry_Object((1,3,6,1,4,1,9,9,826,1,21,10,1))
cfprEtherPIoEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprEtherPIoEntry.setStatus(_A)
_CfprEtherPIoInstanceId_Type=CfprManagedObjectId
_CfprEtherPIoInstanceId_Object=MibTableColumn
cfprEtherPIoInstanceId=_CfprEtherPIoInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,1),_CfprEtherPIoInstanceId_Type())
cfprEtherPIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPIoInstanceId.setStatus(_A)
_CfprEtherPIoDn_Type=CfprManagedObjectDn
_CfprEtherPIoDn_Object=MibTableColumn
cfprEtherPIoDn=_CfprEtherPIoDn_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,2),_CfprEtherPIoDn_Type())
cfprEtherPIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoDn.setStatus(_A)
_CfprEtherPIoRn_Type=SnmpAdminString
_CfprEtherPIoRn_Object=MibTableColumn
cfprEtherPIoRn=_CfprEtherPIoRn_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,3),_CfprEtherPIoRn_Type())
cfprEtherPIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoRn.setStatus(_A)
_CfprEtherPIoAdminState_Type=CfprFabricAdminState
_CfprEtherPIoAdminState_Object=MibTableColumn
cfprEtherPIoAdminState=_CfprEtherPIoAdminState_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,4),_CfprEtherPIoAdminState_Type())
cfprEtherPIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoAdminState.setStatus(_A)
_CfprEtherPIoAdminTransport_Type=CfprNetworkTransport
_CfprEtherPIoAdminTransport_Object=MibTableColumn
cfprEtherPIoAdminTransport=_CfprEtherPIoAdminTransport_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,5),_CfprEtherPIoAdminTransport_Type())
cfprEtherPIoAdminTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoAdminTransport.setStatus(_A)
_CfprEtherPIoAggrPortId_Type=Gauge32
_CfprEtherPIoAggrPortId_Object=MibTableColumn
cfprEtherPIoAggrPortId=_CfprEtherPIoAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,6),_CfprEtherPIoAggrPortId_Type())
cfprEtherPIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoAggrPortId.setStatus(_A)
_CfprEtherPIoChassisId_Type=Gauge32
_CfprEtherPIoChassisId_Object=MibTableColumn
cfprEtherPIoChassisId=_CfprEtherPIoChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,7),_CfprEtherPIoChassisId_Type())
cfprEtherPIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoChassisId.setStatus(_A)
_CfprEtherPIoEncap_Type=CfprPortEncap
_CfprEtherPIoEncap_Object=MibTableColumn
cfprEtherPIoEncap=_CfprEtherPIoEncap_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,8),_CfprEtherPIoEncap_Type())
cfprEtherPIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEncap.setStatus(_A)
_CfprEtherPIoEpDn_Type=SnmpAdminString
_CfprEtherPIoEpDn_Object=MibTableColumn
cfprEtherPIoEpDn=_CfprEtherPIoEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,9),_CfprEtherPIoEpDn_Type())
cfprEtherPIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEpDn.setStatus(_A)
_CfprEtherPIoFltAggr_Type=Unsigned64
_CfprEtherPIoFltAggr_Object=MibTableColumn
cfprEtherPIoFltAggr=_CfprEtherPIoFltAggr_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,10),_CfprEtherPIoFltAggr_Type())
cfprEtherPIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFltAggr.setStatus(_A)
_CfprEtherPIoFsmDescr_Type=SnmpAdminString
_CfprEtherPIoFsmDescr_Object=MibTableColumn
cfprEtherPIoFsmDescr=_CfprEtherPIoFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,11),_CfprEtherPIoFsmDescr_Type())
cfprEtherPIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmDescr.setStatus(_A)
_CfprEtherPIoFsmPrev_Type=SnmpAdminString
_CfprEtherPIoFsmPrev_Object=MibTableColumn
cfprEtherPIoFsmPrev=_CfprEtherPIoFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,12),_CfprEtherPIoFsmPrev_Type())
cfprEtherPIoFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmPrev.setStatus(_A)
_CfprEtherPIoFsmProgr_Type=Gauge32
_CfprEtherPIoFsmProgr_Object=MibTableColumn
cfprEtherPIoFsmProgr=_CfprEtherPIoFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,13),_CfprEtherPIoFsmProgr_Type())
cfprEtherPIoFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmProgr.setStatus(_A)
_CfprEtherPIoFsmRmtInvErrCode_Type=Gauge32
_CfprEtherPIoFsmRmtInvErrCode_Object=MibTableColumn
cfprEtherPIoFsmRmtInvErrCode=_CfprEtherPIoFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,14),_CfprEtherPIoFsmRmtInvErrCode_Type())
cfprEtherPIoFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRmtInvErrCode.setStatus(_A)
_CfprEtherPIoFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprEtherPIoFsmRmtInvErrDescr_Object=MibTableColumn
cfprEtherPIoFsmRmtInvErrDescr=_CfprEtherPIoFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,15),_CfprEtherPIoFsmRmtInvErrDescr_Type())
cfprEtherPIoFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRmtInvErrDescr.setStatus(_A)
_CfprEtherPIoFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprEtherPIoFsmRmtInvRslt_Object=MibTableColumn
cfprEtherPIoFsmRmtInvRslt=_CfprEtherPIoFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,16),_CfprEtherPIoFsmRmtInvRslt_Type())
cfprEtherPIoFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRmtInvRslt.setStatus(_A)
_CfprEtherPIoFsmStageDescr_Type=SnmpAdminString
_CfprEtherPIoFsmStageDescr_Object=MibTableColumn
cfprEtherPIoFsmStageDescr=_CfprEtherPIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,17),_CfprEtherPIoFsmStageDescr_Type())
cfprEtherPIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageDescr.setStatus(_A)
_CfprEtherPIoFsmStamp_Type=DateAndTime
_CfprEtherPIoFsmStamp_Object=MibTableColumn
cfprEtherPIoFsmStamp=_CfprEtherPIoFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,18),_CfprEtherPIoFsmStamp_Type())
cfprEtherPIoFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStamp.setStatus(_A)
_CfprEtherPIoFsmStatus_Type=SnmpAdminString
_CfprEtherPIoFsmStatus_Object=MibTableColumn
cfprEtherPIoFsmStatus=_CfprEtherPIoFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,19),_CfprEtherPIoFsmStatus_Type())
cfprEtherPIoFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStatus.setStatus(_A)
_CfprEtherPIoFsmTry_Type=Gauge32
_CfprEtherPIoFsmTry_Object=MibTableColumn
cfprEtherPIoFsmTry=_CfprEtherPIoFsmTry_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,20),_CfprEtherPIoFsmTry_Type())
cfprEtherPIoFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmTry.setStatus(_A)
_CfprEtherPIoIfRole_Type=CfprNetworkPortRole
_CfprEtherPIoIfRole_Object=MibTableColumn
cfprEtherPIoIfRole=_CfprEtherPIoIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,21),_CfprEtherPIoIfRole_Type())
cfprEtherPIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoIfRole.setStatus(_A)
_CfprEtherPIoIfType_Type=CfprNetworkPhysEpIfType
_CfprEtherPIoIfType_Object=MibTableColumn
cfprEtherPIoIfType=_CfprEtherPIoIfType_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,22),_CfprEtherPIoIfType_Type())
cfprEtherPIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoIfType.setStatus(_A)
_CfprEtherPIoIsPortChannelMember_Type=TruthValue
_CfprEtherPIoIsPortChannelMember_Object=MibTableColumn
cfprEtherPIoIsPortChannelMember=_CfprEtherPIoIsPortChannelMember_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,23),_CfprEtherPIoIsPortChannelMember_Type())
cfprEtherPIoIsPortChannelMember.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoIsPortChannelMember.setStatus(_A)
_CfprEtherPIoLc_Type=CfprFsmLifecycle
_CfprEtherPIoLc_Object=MibTableColumn
cfprEtherPIoLc=_CfprEtherPIoLc_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,24),_CfprEtherPIoLc_Type())
cfprEtherPIoLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoLc.setStatus(_A)
_CfprEtherPIoLicGP_Type=Unsigned64
_CfprEtherPIoLicGP_Object=MibTableColumn
cfprEtherPIoLicGP=_CfprEtherPIoLicGP_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,25),_CfprEtherPIoLicGP_Type())
cfprEtherPIoLicGP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoLicGP.setStatus(_A)
_CfprEtherPIoLicState_Type=CfprLicenseState
_CfprEtherPIoLicState_Object=MibTableColumn
cfprEtherPIoLicState=_CfprEtherPIoLicState_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,26),_CfprEtherPIoLicState_Type())
cfprEtherPIoLicState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoLicState.setStatus(_A)
_CfprEtherPIoLocale_Type=CfprNetworkLocale
_CfprEtherPIoLocale_Object=MibTableColumn
cfprEtherPIoLocale=_CfprEtherPIoLocale_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,27),_CfprEtherPIoLocale_Type())
cfprEtherPIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoLocale.setStatus(_A)
_CfprEtherPIoMac_Type=MacAddress
_CfprEtherPIoMac_Object=MibTableColumn
cfprEtherPIoMac=_CfprEtherPIoMac_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,28),_CfprEtherPIoMac_Type())
cfprEtherPIoMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoMac.setStatus(_A)
_CfprEtherPIoMode_Type=CfprPortMode
_CfprEtherPIoMode_Object=MibTableColumn
cfprEtherPIoMode=_CfprEtherPIoMode_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,29),_CfprEtherPIoMode_Type())
cfprEtherPIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoMode.setStatus(_A)
_CfprEtherPIoModel_Type=SnmpAdminString
_CfprEtherPIoModel_Object=MibTableColumn
cfprEtherPIoModel=_CfprEtherPIoModel_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,30),_CfprEtherPIoModel_Type())
cfprEtherPIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoModel.setStatus(_A)
_CfprEtherPIoName_Type=SnmpAdminString
_CfprEtherPIoName_Object=MibTableColumn
cfprEtherPIoName=_CfprEtherPIoName_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,31),_CfprEtherPIoName_Type())
cfprEtherPIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoName.setStatus(_A)
_CfprEtherPIoOperSpeed_Type=CfprPortEthSpeed
_CfprEtherPIoOperSpeed_Object=MibTableColumn
cfprEtherPIoOperSpeed=_CfprEtherPIoOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,32),_CfprEtherPIoOperSpeed_Type())
cfprEtherPIoOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoOperSpeed.setStatus(_A)
_CfprEtherPIoOperState_Type=CfprNetworkPortOperState
_CfprEtherPIoOperState_Object=MibTableColumn
cfprEtherPIoOperState=_CfprEtherPIoOperState_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,33),_CfprEtherPIoOperState_Type())
cfprEtherPIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoOperState.setStatus(_A)
_CfprEtherPIoPeerAggrPortId_Type=Gauge32
_CfprEtherPIoPeerAggrPortId_Object=MibTableColumn
cfprEtherPIoPeerAggrPortId=_CfprEtherPIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,34),_CfprEtherPIoPeerAggrPortId_Type())
cfprEtherPIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoPeerAggrPortId.setStatus(_A)
_CfprEtherPIoPeerChassisId_Type=Gauge32
_CfprEtherPIoPeerChassisId_Object=MibTableColumn
cfprEtherPIoPeerChassisId=_CfprEtherPIoPeerChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,35),_CfprEtherPIoPeerChassisId_Type())
cfprEtherPIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoPeerChassisId.setStatus(_A)
_CfprEtherPIoPeerDn_Type=SnmpAdminString
_CfprEtherPIoPeerDn_Object=MibTableColumn
cfprEtherPIoPeerDn=_CfprEtherPIoPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,36),_CfprEtherPIoPeerDn_Type())
cfprEtherPIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoPeerDn.setStatus(_A)
_CfprEtherPIoPeerPortId_Type=Gauge32
_CfprEtherPIoPeerPortId_Object=MibTableColumn
cfprEtherPIoPeerPortId=_CfprEtherPIoPeerPortId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,37),_CfprEtherPIoPeerPortId_Type())
cfprEtherPIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoPeerPortId.setStatus(_A)
_CfprEtherPIoPeerSlotId_Type=Gauge32
_CfprEtherPIoPeerSlotId_Object=MibTableColumn
cfprEtherPIoPeerSlotId=_CfprEtherPIoPeerSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,38),_CfprEtherPIoPeerSlotId_Type())
cfprEtherPIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoPeerSlotId.setStatus(_A)
_CfprEtherPIoPortId_Type=Gauge32
_CfprEtherPIoPortId_Object=MibTableColumn
cfprEtherPIoPortId=_CfprEtherPIoPortId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,39),_CfprEtherPIoPortId_Type())
cfprEtherPIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoPortId.setStatus(_A)
_CfprEtherPIoRevision_Type=SnmpAdminString
_CfprEtherPIoRevision_Object=MibTableColumn
cfprEtherPIoRevision=_CfprEtherPIoRevision_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,40),_CfprEtherPIoRevision_Type())
cfprEtherPIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoRevision.setStatus(_A)
_CfprEtherPIoSerial_Type=SnmpAdminString
_CfprEtherPIoSerial_Object=MibTableColumn
cfprEtherPIoSerial=_CfprEtherPIoSerial_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,41),_CfprEtherPIoSerial_Type())
cfprEtherPIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoSerial.setStatus(_A)
_CfprEtherPIoSlotId_Type=Gauge32
_CfprEtherPIoSlotId_Object=MibTableColumn
cfprEtherPIoSlotId=_CfprEtherPIoSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,42),_CfprEtherPIoSlotId_Type())
cfprEtherPIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoSlotId.setStatus(_A)
_CfprEtherPIoStateQual_Type=SnmpAdminString
_CfprEtherPIoStateQual_Object=MibTableColumn
cfprEtherPIoStateQual=_CfprEtherPIoStateQual_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,43),_CfprEtherPIoStateQual_Type())
cfprEtherPIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoStateQual.setStatus(_A)
_CfprEtherPIoSwitchId_Type=CfprNetworkSwitchId
_CfprEtherPIoSwitchId_Object=MibTableColumn
cfprEtherPIoSwitchId=_CfprEtherPIoSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,44),_CfprEtherPIoSwitchId_Type())
cfprEtherPIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoSwitchId.setStatus(_A)
_CfprEtherPIoTransport_Type=CfprNetworkTransport
_CfprEtherPIoTransport_Object=MibTableColumn
cfprEtherPIoTransport=_CfprEtherPIoTransport_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,45),_CfprEtherPIoTransport_Type())
cfprEtherPIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoTransport.setStatus(_A)
_CfprEtherPIoTs_Type=DateAndTime
_CfprEtherPIoTs_Object=MibTableColumn
cfprEtherPIoTs=_CfprEtherPIoTs_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,46),_CfprEtherPIoTs_Type())
cfprEtherPIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoTs.setStatus(_A)
_CfprEtherPIoType_Type=CfprNetworkConnectionType
_CfprEtherPIoType_Object=MibTableColumn
cfprEtherPIoType=_CfprEtherPIoType_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,47),_CfprEtherPIoType_Type())
cfprEtherPIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoType.setStatus(_A)
_CfprEtherPIoUnifiedPort_Type=TruthValue
_CfprEtherPIoUnifiedPort_Object=MibTableColumn
cfprEtherPIoUnifiedPort=_CfprEtherPIoUnifiedPort_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,48),_CfprEtherPIoUnifiedPort_Type())
cfprEtherPIoUnifiedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoUnifiedPort.setStatus(_A)
_CfprEtherPIoUsrLbl_Type=SnmpAdminString
_CfprEtherPIoUsrLbl_Object=MibTableColumn
cfprEtherPIoUsrLbl=_CfprEtherPIoUsrLbl_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,49),_CfprEtherPIoUsrLbl_Type())
cfprEtherPIoUsrLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoUsrLbl.setStatus(_A)
_CfprEtherPIoVendor_Type=SnmpAdminString
_CfprEtherPIoVendor_Object=MibTableColumn
cfprEtherPIoVendor=_CfprEtherPIoVendor_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,50),_CfprEtherPIoVendor_Type())
cfprEtherPIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoVendor.setStatus(_A)
_CfprEtherPIoXcvrType_Type=CfprEquipmentXcvrType
_CfprEtherPIoXcvrType_Object=MibTableColumn
cfprEtherPIoXcvrType=_CfprEtherPIoXcvrType_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,51),_CfprEtherPIoXcvrType_Type())
cfprEtherPIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoXcvrType.setStatus(_A)
_CfprEtherPIoFtwPhyDn_Type=SnmpAdminString
_CfprEtherPIoFtwPhyDn_Object=MibTableColumn
cfprEtherPIoFtwPhyDn=_CfprEtherPIoFtwPhyDn_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,52),_CfprEtherPIoFtwPhyDn_Type())
cfprEtherPIoFtwPhyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFtwPhyDn.setStatus(_A)
_CfprEtherPIoOperDuplex_Type=CfprPortDuplex
_CfprEtherPIoOperDuplex_Object=MibTableColumn
cfprEtherPIoOperDuplex=_CfprEtherPIoOperDuplex_Object((1,3,6,1,4,1,9,9,826,1,21,10,1,53),_CfprEtherPIoOperDuplex_Type())
cfprEtherPIoOperDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoOperDuplex.setStatus(_A)
_CfprEtherPIoEndPointTable_Object=MibTable
cfprEtherPIoEndPointTable=_CfprEtherPIoEndPointTable_Object((1,3,6,1,4,1,9,9,826,1,21,11))
if mibBuilder.loadTexts:cfprEtherPIoEndPointTable.setStatus(_A)
_CfprEtherPIoEndPointEntry_Object=MibTableRow
cfprEtherPIoEndPointEntry=_CfprEtherPIoEndPointEntry_Object((1,3,6,1,4,1,9,9,826,1,21,11,1))
cfprEtherPIoEndPointEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprEtherPIoEndPointEntry.setStatus(_A)
_CfprEtherPIoEndPointInstanceId_Type=CfprManagedObjectId
_CfprEtherPIoEndPointInstanceId_Object=MibTableColumn
cfprEtherPIoEndPointInstanceId=_CfprEtherPIoEndPointInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,11,1,1),_CfprEtherPIoEndPointInstanceId_Type())
cfprEtherPIoEndPointInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPIoEndPointInstanceId.setStatus(_A)
_CfprEtherPIoEndPointDn_Type=CfprManagedObjectDn
_CfprEtherPIoEndPointDn_Object=MibTableColumn
cfprEtherPIoEndPointDn=_CfprEtherPIoEndPointDn_Object((1,3,6,1,4,1,9,9,826,1,21,11,1,2),_CfprEtherPIoEndPointDn_Type())
cfprEtherPIoEndPointDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEndPointDn.setStatus(_A)
_CfprEtherPIoEndPointRn_Type=SnmpAdminString
_CfprEtherPIoEndPointRn_Object=MibTableColumn
cfprEtherPIoEndPointRn=_CfprEtherPIoEndPointRn_Object((1,3,6,1,4,1,9,9,826,1,21,11,1,3),_CfprEtherPIoEndPointRn_Type())
cfprEtherPIoEndPointRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEndPointRn.setStatus(_A)
_CfprEtherPIoEndPointEndPointDn_Type=SnmpAdminString
_CfprEtherPIoEndPointEndPointDn_Object=MibTableColumn
cfprEtherPIoEndPointEndPointDn=_CfprEtherPIoEndPointEndPointDn_Object((1,3,6,1,4,1,9,9,826,1,21,11,1,4),_CfprEtherPIoEndPointEndPointDn_Type())
cfprEtherPIoEndPointEndPointDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEndPointEndPointDn.setStatus(_A)
_CfprEtherPIoEndPointEpCloudType_Type=CfprEtherCloudType
_CfprEtherPIoEndPointEpCloudType_Object=MibTableColumn
cfprEtherPIoEndPointEpCloudType=_CfprEtherPIoEndPointEpCloudType_Object((1,3,6,1,4,1,9,9,826,1,21,11,1,5),_CfprEtherPIoEndPointEpCloudType_Type())
cfprEtherPIoEndPointEpCloudType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEndPointEpCloudType.setStatus(_A)
_CfprEtherPIoEndPointUsrLbl_Type=SnmpAdminString
_CfprEtherPIoEndPointUsrLbl_Object=MibTableColumn
cfprEtherPIoEndPointUsrLbl=_CfprEtherPIoEndPointUsrLbl_Object((1,3,6,1,4,1,9,9,826,1,21,11,1,6),_CfprEtherPIoEndPointUsrLbl_Type())
cfprEtherPIoEndPointUsrLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoEndPointUsrLbl.setStatus(_A)
_CfprEtherPIoFsmTable_Object=MibTable
cfprEtherPIoFsmTable=_CfprEtherPIoFsmTable_Object((1,3,6,1,4,1,9,9,826,1,21,12))
if mibBuilder.loadTexts:cfprEtherPIoFsmTable.setStatus(_A)
_CfprEtherPIoFsmEntry_Object=MibTableRow
cfprEtherPIoFsmEntry=_CfprEtherPIoFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,21,12,1))
cfprEtherPIoFsmEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprEtherPIoFsmEntry.setStatus(_A)
_CfprEtherPIoFsmInstanceId_Type=CfprManagedObjectId
_CfprEtherPIoFsmInstanceId_Object=MibTableColumn
cfprEtherPIoFsmInstanceId=_CfprEtherPIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,1),_CfprEtherPIoFsmInstanceId_Type())
cfprEtherPIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPIoFsmInstanceId.setStatus(_A)
_CfprEtherPIoFsmDn_Type=CfprManagedObjectDn
_CfprEtherPIoFsmDn_Object=MibTableColumn
cfprEtherPIoFsmDn=_CfprEtherPIoFsmDn_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,2),_CfprEtherPIoFsmDn_Type())
cfprEtherPIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmDn.setStatus(_A)
_CfprEtherPIoFsmRn_Type=SnmpAdminString
_CfprEtherPIoFsmRn_Object=MibTableColumn
cfprEtherPIoFsmRn=_CfprEtherPIoFsmRn_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,3),_CfprEtherPIoFsmRn_Type())
cfprEtherPIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRn.setStatus(_A)
_CfprEtherPIoFsmCompletionTime_Type=DateAndTime
_CfprEtherPIoFsmCompletionTime_Object=MibTableColumn
cfprEtherPIoFsmCompletionTime=_CfprEtherPIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,4),_CfprEtherPIoFsmCompletionTime_Type())
cfprEtherPIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmCompletionTime.setStatus(_A)
_CfprEtherPIoFsmCurrentFsm_Type=CfprEtherPIoFsmCurrentFsm
_CfprEtherPIoFsmCurrentFsm_Object=MibTableColumn
cfprEtherPIoFsmCurrentFsm=_CfprEtherPIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,5),_CfprEtherPIoFsmCurrentFsm_Type())
cfprEtherPIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmCurrentFsm.setStatus(_A)
_CfprEtherPIoFsmDescrData_Type=SnmpAdminString
_CfprEtherPIoFsmDescrData_Object=MibTableColumn
cfprEtherPIoFsmDescrData=_CfprEtherPIoFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,6),_CfprEtherPIoFsmDescrData_Type())
cfprEtherPIoFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmDescrData.setStatus(_A)
_CfprEtherPIoFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprEtherPIoFsmFsmStatus_Object=MibTableColumn
cfprEtherPIoFsmFsmStatus=_CfprEtherPIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,7),_CfprEtherPIoFsmFsmStatus_Type())
cfprEtherPIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmFsmStatus.setStatus(_A)
_CfprEtherPIoFsmProgress_Type=Gauge32
_CfprEtherPIoFsmProgress_Object=MibTableColumn
cfprEtherPIoFsmProgress=_CfprEtherPIoFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,8),_CfprEtherPIoFsmProgress_Type())
cfprEtherPIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmProgress.setStatus(_A)
_CfprEtherPIoFsmRmtErrCode_Type=Gauge32
_CfprEtherPIoFsmRmtErrCode_Object=MibTableColumn
cfprEtherPIoFsmRmtErrCode=_CfprEtherPIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,9),_CfprEtherPIoFsmRmtErrCode_Type())
cfprEtherPIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRmtErrCode.setStatus(_A)
_CfprEtherPIoFsmRmtErrDescr_Type=SnmpAdminString
_CfprEtherPIoFsmRmtErrDescr_Object=MibTableColumn
cfprEtherPIoFsmRmtErrDescr=_CfprEtherPIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,10),_CfprEtherPIoFsmRmtErrDescr_Type())
cfprEtherPIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRmtErrDescr.setStatus(_A)
_CfprEtherPIoFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprEtherPIoFsmRmtRslt_Object=MibTableColumn
cfprEtherPIoFsmRmtRslt=_CfprEtherPIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,21,12,1,11),_CfprEtherPIoFsmRmtRslt_Type())
cfprEtherPIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmRmtRslt.setStatus(_A)
_CfprEtherPIoFsmStageTable_Object=MibTable
cfprEtherPIoFsmStageTable=_CfprEtherPIoFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,21,13))
if mibBuilder.loadTexts:cfprEtherPIoFsmStageTable.setStatus(_A)
_CfprEtherPIoFsmStageEntry_Object=MibTableRow
cfprEtherPIoFsmStageEntry=_CfprEtherPIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,21,13,1))
cfprEtherPIoFsmStageEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprEtherPIoFsmStageEntry.setStatus(_A)
_CfprEtherPIoFsmStageInstanceId_Type=CfprManagedObjectId
_CfprEtherPIoFsmStageInstanceId_Object=MibTableColumn
cfprEtherPIoFsmStageInstanceId=_CfprEtherPIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,1),_CfprEtherPIoFsmStageInstanceId_Type())
cfprEtherPIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageInstanceId.setStatus(_A)
_CfprEtherPIoFsmStageDn_Type=CfprManagedObjectDn
_CfprEtherPIoFsmStageDn_Object=MibTableColumn
cfprEtherPIoFsmStageDn=_CfprEtherPIoFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,2),_CfprEtherPIoFsmStageDn_Type())
cfprEtherPIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageDn.setStatus(_A)
_CfprEtherPIoFsmStageRn_Type=SnmpAdminString
_CfprEtherPIoFsmStageRn_Object=MibTableColumn
cfprEtherPIoFsmStageRn=_CfprEtherPIoFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,3),_CfprEtherPIoFsmStageRn_Type())
cfprEtherPIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageRn.setStatus(_A)
_CfprEtherPIoFsmStageDescrData_Type=SnmpAdminString
_CfprEtherPIoFsmStageDescrData_Object=MibTableColumn
cfprEtherPIoFsmStageDescrData=_CfprEtherPIoFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,4),_CfprEtherPIoFsmStageDescrData_Type())
cfprEtherPIoFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageDescrData.setStatus(_A)
_CfprEtherPIoFsmStageLastUpdateTime_Type=DateAndTime
_CfprEtherPIoFsmStageLastUpdateTime_Object=MibTableColumn
cfprEtherPIoFsmStageLastUpdateTime=_CfprEtherPIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,5),_CfprEtherPIoFsmStageLastUpdateTime_Type())
cfprEtherPIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageLastUpdateTime.setStatus(_A)
_CfprEtherPIoFsmStageName_Type=CfprEtherPIoFsmStageName
_CfprEtherPIoFsmStageName_Object=MibTableColumn
cfprEtherPIoFsmStageName=_CfprEtherPIoFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,6),_CfprEtherPIoFsmStageName_Type())
cfprEtherPIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageName.setStatus(_A)
_CfprEtherPIoFsmStageOrder_Type=Gauge32
_CfprEtherPIoFsmStageOrder_Object=MibTableColumn
cfprEtherPIoFsmStageOrder=_CfprEtherPIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,7),_CfprEtherPIoFsmStageOrder_Type())
cfprEtherPIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageOrder.setStatus(_A)
_CfprEtherPIoFsmStageRetry_Type=Gauge32
_CfprEtherPIoFsmStageRetry_Object=MibTableColumn
cfprEtherPIoFsmStageRetry=_CfprEtherPIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,8),_CfprEtherPIoFsmStageRetry_Type())
cfprEtherPIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageRetry.setStatus(_A)
_CfprEtherPIoFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprEtherPIoFsmStageStageStatus_Object=MibTableColumn
cfprEtherPIoFsmStageStageStatus=_CfprEtherPIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,21,13,1,9),_CfprEtherPIoFsmStageStageStatus_Type())
cfprEtherPIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPIoFsmStageStageStatus.setStatus(_A)
_CfprEtherPauseStatsTable_Object=MibTable
cfprEtherPauseStatsTable=_CfprEtherPauseStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,14))
if mibBuilder.loadTexts:cfprEtherPauseStatsTable.setStatus(_A)
_CfprEtherPauseStatsEntry_Object=MibTableRow
cfprEtherPauseStatsEntry=_CfprEtherPauseStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,14,1))
cfprEtherPauseStatsEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cfprEtherPauseStatsEntry.setStatus(_A)
_CfprEtherPauseStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherPauseStatsInstanceId_Object=MibTableColumn
cfprEtherPauseStatsInstanceId=_CfprEtherPauseStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,1),_CfprEtherPauseStatsInstanceId_Type())
cfprEtherPauseStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPauseStatsInstanceId.setStatus(_A)
_CfprEtherPauseStatsDn_Type=CfprManagedObjectDn
_CfprEtherPauseStatsDn_Object=MibTableColumn
cfprEtherPauseStatsDn=_CfprEtherPauseStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,2),_CfprEtherPauseStatsDn_Type())
cfprEtherPauseStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsDn.setStatus(_A)
_CfprEtherPauseStatsRn_Type=SnmpAdminString
_CfprEtherPauseStatsRn_Object=MibTableColumn
cfprEtherPauseStatsRn=_CfprEtherPauseStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,3),_CfprEtherPauseStatsRn_Type())
cfprEtherPauseStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsRn.setStatus(_A)
_CfprEtherPauseStatsIntervals_Type=Gauge32
_CfprEtherPauseStatsIntervals_Object=MibTableColumn
cfprEtherPauseStatsIntervals=_CfprEtherPauseStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,4),_CfprEtherPauseStatsIntervals_Type())
cfprEtherPauseStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsIntervals.setStatus(_A)
_CfprEtherPauseStatsRecvPause_Type=Unsigned64
_CfprEtherPauseStatsRecvPause_Object=MibTableColumn
cfprEtherPauseStatsRecvPause=_CfprEtherPauseStatsRecvPause_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,5),_CfprEtherPauseStatsRecvPause_Type())
cfprEtherPauseStatsRecvPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsRecvPause.setStatus(_A)
_CfprEtherPauseStatsRecvPauseDelta_Type=Counter64
_CfprEtherPauseStatsRecvPauseDelta_Object=MibTableColumn
cfprEtherPauseStatsRecvPauseDelta=_CfprEtherPauseStatsRecvPauseDelta_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,6),_CfprEtherPauseStatsRecvPauseDelta_Type())
cfprEtherPauseStatsRecvPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsRecvPauseDelta.setStatus(_A)
_CfprEtherPauseStatsRecvPauseDeltaAvg_Type=Unsigned64
_CfprEtherPauseStatsRecvPauseDeltaAvg_Object=MibTableColumn
cfprEtherPauseStatsRecvPauseDeltaAvg=_CfprEtherPauseStatsRecvPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,7),_CfprEtherPauseStatsRecvPauseDeltaAvg_Type())
cfprEtherPauseStatsRecvPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsRecvPauseDeltaAvg.setStatus(_A)
_CfprEtherPauseStatsRecvPauseDeltaMax_Type=Unsigned64
_CfprEtherPauseStatsRecvPauseDeltaMax_Object=MibTableColumn
cfprEtherPauseStatsRecvPauseDeltaMax=_CfprEtherPauseStatsRecvPauseDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,8),_CfprEtherPauseStatsRecvPauseDeltaMax_Type())
cfprEtherPauseStatsRecvPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsRecvPauseDeltaMax.setStatus(_A)
_CfprEtherPauseStatsRecvPauseDeltaMin_Type=Unsigned64
_CfprEtherPauseStatsRecvPauseDeltaMin_Object=MibTableColumn
cfprEtherPauseStatsRecvPauseDeltaMin=_CfprEtherPauseStatsRecvPauseDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,9),_CfprEtherPauseStatsRecvPauseDeltaMin_Type())
cfprEtherPauseStatsRecvPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsRecvPauseDeltaMin.setStatus(_A)
_CfprEtherPauseStatsResets_Type=Unsigned64
_CfprEtherPauseStatsResets_Object=MibTableColumn
cfprEtherPauseStatsResets=_CfprEtherPauseStatsResets_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,10),_CfprEtherPauseStatsResets_Type())
cfprEtherPauseStatsResets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsResets.setStatus(_A)
_CfprEtherPauseStatsResetsDelta_Type=Counter64
_CfprEtherPauseStatsResetsDelta_Object=MibTableColumn
cfprEtherPauseStatsResetsDelta=_CfprEtherPauseStatsResetsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,11),_CfprEtherPauseStatsResetsDelta_Type())
cfprEtherPauseStatsResetsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsResetsDelta.setStatus(_A)
_CfprEtherPauseStatsResetsDeltaAvg_Type=Unsigned64
_CfprEtherPauseStatsResetsDeltaAvg_Object=MibTableColumn
cfprEtherPauseStatsResetsDeltaAvg=_CfprEtherPauseStatsResetsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,12),_CfprEtherPauseStatsResetsDeltaAvg_Type())
cfprEtherPauseStatsResetsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsResetsDeltaAvg.setStatus(_A)
_CfprEtherPauseStatsResetsDeltaMax_Type=Unsigned64
_CfprEtherPauseStatsResetsDeltaMax_Object=MibTableColumn
cfprEtherPauseStatsResetsDeltaMax=_CfprEtherPauseStatsResetsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,13),_CfprEtherPauseStatsResetsDeltaMax_Type())
cfprEtherPauseStatsResetsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsResetsDeltaMax.setStatus(_A)
_CfprEtherPauseStatsResetsDeltaMin_Type=Unsigned64
_CfprEtherPauseStatsResetsDeltaMin_Object=MibTableColumn
cfprEtherPauseStatsResetsDeltaMin=_CfprEtherPauseStatsResetsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,14),_CfprEtherPauseStatsResetsDeltaMin_Type())
cfprEtherPauseStatsResetsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsResetsDeltaMin.setStatus(_A)
_CfprEtherPauseStatsSuspect_Type=TruthValue
_CfprEtherPauseStatsSuspect_Object=MibTableColumn
cfprEtherPauseStatsSuspect=_CfprEtherPauseStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,15),_CfprEtherPauseStatsSuspect_Type())
cfprEtherPauseStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsSuspect.setStatus(_A)
_CfprEtherPauseStatsThresholded_Type=CfprEtherPauseStatsThresholded
_CfprEtherPauseStatsThresholded_Object=MibTableColumn
cfprEtherPauseStatsThresholded=_CfprEtherPauseStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,16),_CfprEtherPauseStatsThresholded_Type())
cfprEtherPauseStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsThresholded.setStatus(_A)
_CfprEtherPauseStatsTimeCollected_Type=DateAndTime
_CfprEtherPauseStatsTimeCollected_Object=MibTableColumn
cfprEtherPauseStatsTimeCollected=_CfprEtherPauseStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,17),_CfprEtherPauseStatsTimeCollected_Type())
cfprEtherPauseStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsTimeCollected.setStatus(_A)
_CfprEtherPauseStatsUpdate_Type=Gauge32
_CfprEtherPauseStatsUpdate_Object=MibTableColumn
cfprEtherPauseStatsUpdate=_CfprEtherPauseStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,18),_CfprEtherPauseStatsUpdate_Type())
cfprEtherPauseStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsUpdate.setStatus(_A)
_CfprEtherPauseStatsXmitPause_Type=Unsigned64
_CfprEtherPauseStatsXmitPause_Object=MibTableColumn
cfprEtherPauseStatsXmitPause=_CfprEtherPauseStatsXmitPause_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,19),_CfprEtherPauseStatsXmitPause_Type())
cfprEtherPauseStatsXmitPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsXmitPause.setStatus(_A)
_CfprEtherPauseStatsXmitPauseDelta_Type=Counter64
_CfprEtherPauseStatsXmitPauseDelta_Object=MibTableColumn
cfprEtherPauseStatsXmitPauseDelta=_CfprEtherPauseStatsXmitPauseDelta_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,20),_CfprEtherPauseStatsXmitPauseDelta_Type())
cfprEtherPauseStatsXmitPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsXmitPauseDelta.setStatus(_A)
_CfprEtherPauseStatsXmitPauseDeltaAvg_Type=Unsigned64
_CfprEtherPauseStatsXmitPauseDeltaAvg_Object=MibTableColumn
cfprEtherPauseStatsXmitPauseDeltaAvg=_CfprEtherPauseStatsXmitPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,21),_CfprEtherPauseStatsXmitPauseDeltaAvg_Type())
cfprEtherPauseStatsXmitPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsXmitPauseDeltaAvg.setStatus(_A)
_CfprEtherPauseStatsXmitPauseDeltaMax_Type=Unsigned64
_CfprEtherPauseStatsXmitPauseDeltaMax_Object=MibTableColumn
cfprEtherPauseStatsXmitPauseDeltaMax=_CfprEtherPauseStatsXmitPauseDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,22),_CfprEtherPauseStatsXmitPauseDeltaMax_Type())
cfprEtherPauseStatsXmitPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsXmitPauseDeltaMax.setStatus(_A)
_CfprEtherPauseStatsXmitPauseDeltaMin_Type=Unsigned64
_CfprEtherPauseStatsXmitPauseDeltaMin_Object=MibTableColumn
cfprEtherPauseStatsXmitPauseDeltaMin=_CfprEtherPauseStatsXmitPauseDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,14,1,23),_CfprEtherPauseStatsXmitPauseDeltaMin_Type())
cfprEtherPauseStatsXmitPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsXmitPauseDeltaMin.setStatus(_A)
_CfprEtherPauseStatsHistTable_Object=MibTable
cfprEtherPauseStatsHistTable=_CfprEtherPauseStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,15))
if mibBuilder.loadTexts:cfprEtherPauseStatsHistTable.setStatus(_A)
_CfprEtherPauseStatsHistEntry_Object=MibTableRow
cfprEtherPauseStatsHistEntry=_CfprEtherPauseStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,15,1))
cfprEtherPauseStatsHistEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cfprEtherPauseStatsHistEntry.setStatus(_A)
_CfprEtherPauseStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherPauseStatsHistInstanceId_Object=MibTableColumn
cfprEtherPauseStatsHistInstanceId=_CfprEtherPauseStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,1),_CfprEtherPauseStatsHistInstanceId_Type())
cfprEtherPauseStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistInstanceId.setStatus(_A)
_CfprEtherPauseStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherPauseStatsHistDn_Object=MibTableColumn
cfprEtherPauseStatsHistDn=_CfprEtherPauseStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,2),_CfprEtherPauseStatsHistDn_Type())
cfprEtherPauseStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistDn.setStatus(_A)
_CfprEtherPauseStatsHistRn_Type=SnmpAdminString
_CfprEtherPauseStatsHistRn_Object=MibTableColumn
cfprEtherPauseStatsHistRn=_CfprEtherPauseStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,3),_CfprEtherPauseStatsHistRn_Type())
cfprEtherPauseStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistRn.setStatus(_A)
_CfprEtherPauseStatsHistId_Type=Unsigned64
_CfprEtherPauseStatsHistId_Object=MibTableColumn
cfprEtherPauseStatsHistId=_CfprEtherPauseStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,4),_CfprEtherPauseStatsHistId_Type())
cfprEtherPauseStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistId.setStatus(_A)
_CfprEtherPauseStatsHistMostRecent_Type=TruthValue
_CfprEtherPauseStatsHistMostRecent_Object=MibTableColumn
cfprEtherPauseStatsHistMostRecent=_CfprEtherPauseStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,5),_CfprEtherPauseStatsHistMostRecent_Type())
cfprEtherPauseStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistMostRecent.setStatus(_A)
_CfprEtherPauseStatsHistRecvPause_Type=Unsigned64
_CfprEtherPauseStatsHistRecvPause_Object=MibTableColumn
cfprEtherPauseStatsHistRecvPause=_CfprEtherPauseStatsHistRecvPause_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,6),_CfprEtherPauseStatsHistRecvPause_Type())
cfprEtherPauseStatsHistRecvPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistRecvPause.setStatus(_A)
_CfprEtherPauseStatsHistRecvPauseDelta_Type=Unsigned64
_CfprEtherPauseStatsHistRecvPauseDelta_Object=MibTableColumn
cfprEtherPauseStatsHistRecvPauseDelta=_CfprEtherPauseStatsHistRecvPauseDelta_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,7),_CfprEtherPauseStatsHistRecvPauseDelta_Type())
cfprEtherPauseStatsHistRecvPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistRecvPauseDelta.setStatus(_A)
_CfprEtherPauseStatsHistRecvPauseDeltaAvg_Type=Unsigned64
_CfprEtherPauseStatsHistRecvPauseDeltaAvg_Object=MibTableColumn
cfprEtherPauseStatsHistRecvPauseDeltaAvg=_CfprEtherPauseStatsHistRecvPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,8),_CfprEtherPauseStatsHistRecvPauseDeltaAvg_Type())
cfprEtherPauseStatsHistRecvPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistRecvPauseDeltaAvg.setStatus(_A)
_CfprEtherPauseStatsHistRecvPauseDeltaMax_Type=Unsigned64
_CfprEtherPauseStatsHistRecvPauseDeltaMax_Object=MibTableColumn
cfprEtherPauseStatsHistRecvPauseDeltaMax=_CfprEtherPauseStatsHistRecvPauseDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,9),_CfprEtherPauseStatsHistRecvPauseDeltaMax_Type())
cfprEtherPauseStatsHistRecvPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistRecvPauseDeltaMax.setStatus(_A)
_CfprEtherPauseStatsHistRecvPauseDeltaMin_Type=Unsigned64
_CfprEtherPauseStatsHistRecvPauseDeltaMin_Object=MibTableColumn
cfprEtherPauseStatsHistRecvPauseDeltaMin=_CfprEtherPauseStatsHistRecvPauseDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,10),_CfprEtherPauseStatsHistRecvPauseDeltaMin_Type())
cfprEtherPauseStatsHistRecvPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistRecvPauseDeltaMin.setStatus(_A)
_CfprEtherPauseStatsHistResets_Type=Unsigned64
_CfprEtherPauseStatsHistResets_Object=MibTableColumn
cfprEtherPauseStatsHistResets=_CfprEtherPauseStatsHistResets_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,11),_CfprEtherPauseStatsHistResets_Type())
cfprEtherPauseStatsHistResets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistResets.setStatus(_A)
_CfprEtherPauseStatsHistResetsDelta_Type=Unsigned64
_CfprEtherPauseStatsHistResetsDelta_Object=MibTableColumn
cfprEtherPauseStatsHistResetsDelta=_CfprEtherPauseStatsHistResetsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,12),_CfprEtherPauseStatsHistResetsDelta_Type())
cfprEtherPauseStatsHistResetsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistResetsDelta.setStatus(_A)
_CfprEtherPauseStatsHistResetsDeltaAvg_Type=Unsigned64
_CfprEtherPauseStatsHistResetsDeltaAvg_Object=MibTableColumn
cfprEtherPauseStatsHistResetsDeltaAvg=_CfprEtherPauseStatsHistResetsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,13),_CfprEtherPauseStatsHistResetsDeltaAvg_Type())
cfprEtherPauseStatsHistResetsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistResetsDeltaAvg.setStatus(_A)
_CfprEtherPauseStatsHistResetsDeltaMax_Type=Unsigned64
_CfprEtherPauseStatsHistResetsDeltaMax_Object=MibTableColumn
cfprEtherPauseStatsHistResetsDeltaMax=_CfprEtherPauseStatsHistResetsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,14),_CfprEtherPauseStatsHistResetsDeltaMax_Type())
cfprEtherPauseStatsHistResetsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistResetsDeltaMax.setStatus(_A)
_CfprEtherPauseStatsHistResetsDeltaMin_Type=Unsigned64
_CfprEtherPauseStatsHistResetsDeltaMin_Object=MibTableColumn
cfprEtherPauseStatsHistResetsDeltaMin=_CfprEtherPauseStatsHistResetsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,15),_CfprEtherPauseStatsHistResetsDeltaMin_Type())
cfprEtherPauseStatsHistResetsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistResetsDeltaMin.setStatus(_A)
_CfprEtherPauseStatsHistSuspect_Type=TruthValue
_CfprEtherPauseStatsHistSuspect_Object=MibTableColumn
cfprEtherPauseStatsHistSuspect=_CfprEtherPauseStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,16),_CfprEtherPauseStatsHistSuspect_Type())
cfprEtherPauseStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistSuspect.setStatus(_A)
_CfprEtherPauseStatsHistThresholded_Type=CfprEtherPauseStatsHistThresholded
_CfprEtherPauseStatsHistThresholded_Object=MibTableColumn
cfprEtherPauseStatsHistThresholded=_CfprEtherPauseStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,17),_CfprEtherPauseStatsHistThresholded_Type())
cfprEtherPauseStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistThresholded.setStatus(_A)
_CfprEtherPauseStatsHistTimeCollected_Type=DateAndTime
_CfprEtherPauseStatsHistTimeCollected_Object=MibTableColumn
cfprEtherPauseStatsHistTimeCollected=_CfprEtherPauseStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,18),_CfprEtherPauseStatsHistTimeCollected_Type())
cfprEtherPauseStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistTimeCollected.setStatus(_A)
_CfprEtherPauseStatsHistXmitPause_Type=Unsigned64
_CfprEtherPauseStatsHistXmitPause_Object=MibTableColumn
cfprEtherPauseStatsHistXmitPause=_CfprEtherPauseStatsHistXmitPause_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,19),_CfprEtherPauseStatsHistXmitPause_Type())
cfprEtherPauseStatsHistXmitPause.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistXmitPause.setStatus(_A)
_CfprEtherPauseStatsHistXmitPauseDelta_Type=Unsigned64
_CfprEtherPauseStatsHistXmitPauseDelta_Object=MibTableColumn
cfprEtherPauseStatsHistXmitPauseDelta=_CfprEtherPauseStatsHistXmitPauseDelta_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,20),_CfprEtherPauseStatsHistXmitPauseDelta_Type())
cfprEtherPauseStatsHistXmitPauseDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistXmitPauseDelta.setStatus(_A)
_CfprEtherPauseStatsHistXmitPauseDeltaAvg_Type=Unsigned64
_CfprEtherPauseStatsHistXmitPauseDeltaAvg_Object=MibTableColumn
cfprEtherPauseStatsHistXmitPauseDeltaAvg=_CfprEtherPauseStatsHistXmitPauseDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,21),_CfprEtherPauseStatsHistXmitPauseDeltaAvg_Type())
cfprEtherPauseStatsHistXmitPauseDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistXmitPauseDeltaAvg.setStatus(_A)
_CfprEtherPauseStatsHistXmitPauseDeltaMax_Type=Unsigned64
_CfprEtherPauseStatsHistXmitPauseDeltaMax_Object=MibTableColumn
cfprEtherPauseStatsHistXmitPauseDeltaMax=_CfprEtherPauseStatsHistXmitPauseDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,22),_CfprEtherPauseStatsHistXmitPauseDeltaMax_Type())
cfprEtherPauseStatsHistXmitPauseDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistXmitPauseDeltaMax.setStatus(_A)
_CfprEtherPauseStatsHistXmitPauseDeltaMin_Type=Unsigned64
_CfprEtherPauseStatsHistXmitPauseDeltaMin_Object=MibTableColumn
cfprEtherPauseStatsHistXmitPauseDeltaMin=_CfprEtherPauseStatsHistXmitPauseDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,15,1,23),_CfprEtherPauseStatsHistXmitPauseDeltaMin_Type())
cfprEtherPauseStatsHistXmitPauseDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPauseStatsHistXmitPauseDeltaMin.setStatus(_A)
_CfprEtherPortChanIdElemTable_Object=MibTable
cfprEtherPortChanIdElemTable=_CfprEtherPortChanIdElemTable_Object((1,3,6,1,4,1,9,9,826,1,21,16))
if mibBuilder.loadTexts:cfprEtherPortChanIdElemTable.setStatus(_A)
_CfprEtherPortChanIdElemEntry_Object=MibTableRow
cfprEtherPortChanIdElemEntry=_CfprEtherPortChanIdElemEntry_Object((1,3,6,1,4,1,9,9,826,1,21,16,1))
cfprEtherPortChanIdElemEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cfprEtherPortChanIdElemEntry.setStatus(_A)
_CfprEtherPortChanIdElemInstanceId_Type=CfprManagedObjectId
_CfprEtherPortChanIdElemInstanceId_Object=MibTableColumn
cfprEtherPortChanIdElemInstanceId=_CfprEtherPortChanIdElemInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,16,1,1),_CfprEtherPortChanIdElemInstanceId_Type())
cfprEtherPortChanIdElemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPortChanIdElemInstanceId.setStatus(_A)
_CfprEtherPortChanIdElemDn_Type=CfprManagedObjectDn
_CfprEtherPortChanIdElemDn_Object=MibTableColumn
cfprEtherPortChanIdElemDn=_CfprEtherPortChanIdElemDn_Object((1,3,6,1,4,1,9,9,826,1,21,16,1,2),_CfprEtherPortChanIdElemDn_Type())
cfprEtherPortChanIdElemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPortChanIdElemDn.setStatus(_A)
_CfprEtherPortChanIdElemRn_Type=SnmpAdminString
_CfprEtherPortChanIdElemRn_Object=MibTableColumn
cfprEtherPortChanIdElemRn=_CfprEtherPortChanIdElemRn_Object((1,3,6,1,4,1,9,9,826,1,21,16,1,3),_CfprEtherPortChanIdElemRn_Type())
cfprEtherPortChanIdElemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPortChanIdElemRn.setStatus(_A)
_CfprEtherPortChanIdElemId_Type=Gauge32
_CfprEtherPortChanIdElemId_Object=MibTableColumn
cfprEtherPortChanIdElemId=_CfprEtherPortChanIdElemId_Object((1,3,6,1,4,1,9,9,826,1,21,16,1,4),_CfprEtherPortChanIdElemId_Type())
cfprEtherPortChanIdElemId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPortChanIdElemId.setStatus(_A)
_CfprEtherPortChanIdUniverseTable_Object=MibTable
cfprEtherPortChanIdUniverseTable=_CfprEtherPortChanIdUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,21,17))
if mibBuilder.loadTexts:cfprEtherPortChanIdUniverseTable.setStatus(_A)
_CfprEtherPortChanIdUniverseEntry_Object=MibTableRow
cfprEtherPortChanIdUniverseEntry=_CfprEtherPortChanIdUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,21,17,1))
cfprEtherPortChanIdUniverseEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cfprEtherPortChanIdUniverseEntry.setStatus(_A)
_CfprEtherPortChanIdUniverseInstanceId_Type=CfprManagedObjectId
_CfprEtherPortChanIdUniverseInstanceId_Object=MibTableColumn
cfprEtherPortChanIdUniverseInstanceId=_CfprEtherPortChanIdUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,17,1,1),_CfprEtherPortChanIdUniverseInstanceId_Type())
cfprEtherPortChanIdUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherPortChanIdUniverseInstanceId.setStatus(_A)
_CfprEtherPortChanIdUniverseDn_Type=CfprManagedObjectDn
_CfprEtherPortChanIdUniverseDn_Object=MibTableColumn
cfprEtherPortChanIdUniverseDn=_CfprEtherPortChanIdUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,21,17,1,2),_CfprEtherPortChanIdUniverseDn_Type())
cfprEtherPortChanIdUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPortChanIdUniverseDn.setStatus(_A)
_CfprEtherPortChanIdUniverseRn_Type=SnmpAdminString
_CfprEtherPortChanIdUniverseRn_Object=MibTableColumn
cfprEtherPortChanIdUniverseRn=_CfprEtherPortChanIdUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,21,17,1,3),_CfprEtherPortChanIdUniverseRn_Type())
cfprEtherPortChanIdUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherPortChanIdUniverseRn.setStatus(_A)
_CfprEtherRxStatsTable_Object=MibTable
cfprEtherRxStatsTable=_CfprEtherRxStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,18))
if mibBuilder.loadTexts:cfprEtherRxStatsTable.setStatus(_A)
_CfprEtherRxStatsEntry_Object=MibTableRow
cfprEtherRxStatsEntry=_CfprEtherRxStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,18,1))
cfprEtherRxStatsEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cfprEtherRxStatsEntry.setStatus(_A)
_CfprEtherRxStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherRxStatsInstanceId_Object=MibTableColumn
cfprEtherRxStatsInstanceId=_CfprEtherRxStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,1),_CfprEtherRxStatsInstanceId_Type())
cfprEtherRxStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherRxStatsInstanceId.setStatus(_A)
_CfprEtherRxStatsDn_Type=CfprManagedObjectDn
_CfprEtherRxStatsDn_Object=MibTableColumn
cfprEtherRxStatsDn=_CfprEtherRxStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,2),_CfprEtherRxStatsDn_Type())
cfprEtherRxStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsDn.setStatus(_A)
_CfprEtherRxStatsRn_Type=SnmpAdminString
_CfprEtherRxStatsRn_Object=MibTableColumn
cfprEtherRxStatsRn=_CfprEtherRxStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,3),_CfprEtherRxStatsRn_Type())
cfprEtherRxStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsRn.setStatus(_A)
_CfprEtherRxStatsBroadcastPackets_Type=Unsigned64
_CfprEtherRxStatsBroadcastPackets_Object=MibTableColumn
cfprEtherRxStatsBroadcastPackets=_CfprEtherRxStatsBroadcastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,4),_CfprEtherRxStatsBroadcastPackets_Type())
cfprEtherRxStatsBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsBroadcastPackets.setStatus(_A)
_CfprEtherRxStatsBroadcastPacketsDelta_Type=Counter64
_CfprEtherRxStatsBroadcastPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsBroadcastPacketsDelta=_CfprEtherRxStatsBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,5),_CfprEtherRxStatsBroadcastPacketsDelta_Type())
cfprEtherRxStatsBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsBroadcastPacketsDelta.setStatus(_A)
_CfprEtherRxStatsBroadcastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsBroadcastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsBroadcastPacketsDeltaAvg=_CfprEtherRxStatsBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,6),_CfprEtherRxStatsBroadcastPacketsDeltaAvg_Type())
cfprEtherRxStatsBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsBroadcastPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsBroadcastPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsBroadcastPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsBroadcastPacketsDeltaMax=_CfprEtherRxStatsBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,7),_CfprEtherRxStatsBroadcastPacketsDeltaMax_Type())
cfprEtherRxStatsBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsBroadcastPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsBroadcastPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsBroadcastPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsBroadcastPacketsDeltaMin=_CfprEtherRxStatsBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,8),_CfprEtherRxStatsBroadcastPacketsDeltaMin_Type())
cfprEtherRxStatsBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsBroadcastPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsIntervals_Type=Gauge32
_CfprEtherRxStatsIntervals_Object=MibTableColumn
cfprEtherRxStatsIntervals=_CfprEtherRxStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,9),_CfprEtherRxStatsIntervals_Type())
cfprEtherRxStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsIntervals.setStatus(_A)
_CfprEtherRxStatsJumboPackets_Type=Unsigned64
_CfprEtherRxStatsJumboPackets_Object=MibTableColumn
cfprEtherRxStatsJumboPackets=_CfprEtherRxStatsJumboPackets_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,10),_CfprEtherRxStatsJumboPackets_Type())
cfprEtherRxStatsJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsJumboPackets.setStatus(_A)
_CfprEtherRxStatsJumboPacketsDelta_Type=Counter64
_CfprEtherRxStatsJumboPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsJumboPacketsDelta=_CfprEtherRxStatsJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,11),_CfprEtherRxStatsJumboPacketsDelta_Type())
cfprEtherRxStatsJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsJumboPacketsDelta.setStatus(_A)
_CfprEtherRxStatsJumboPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsJumboPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsJumboPacketsDeltaAvg=_CfprEtherRxStatsJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,12),_CfprEtherRxStatsJumboPacketsDeltaAvg_Type())
cfprEtherRxStatsJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsJumboPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsJumboPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsJumboPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsJumboPacketsDeltaMax=_CfprEtherRxStatsJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,13),_CfprEtherRxStatsJumboPacketsDeltaMax_Type())
cfprEtherRxStatsJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsJumboPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsJumboPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsJumboPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsJumboPacketsDeltaMin=_CfprEtherRxStatsJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,14),_CfprEtherRxStatsJumboPacketsDeltaMin_Type())
cfprEtherRxStatsJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsJumboPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsMulticastPackets_Type=Unsigned64
_CfprEtherRxStatsMulticastPackets_Object=MibTableColumn
cfprEtherRxStatsMulticastPackets=_CfprEtherRxStatsMulticastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,15),_CfprEtherRxStatsMulticastPackets_Type())
cfprEtherRxStatsMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsMulticastPackets.setStatus(_A)
_CfprEtherRxStatsMulticastPacketsDelta_Type=Counter64
_CfprEtherRxStatsMulticastPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsMulticastPacketsDelta=_CfprEtherRxStatsMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,16),_CfprEtherRxStatsMulticastPacketsDelta_Type())
cfprEtherRxStatsMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsMulticastPacketsDelta.setStatus(_A)
_CfprEtherRxStatsMulticastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsMulticastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsMulticastPacketsDeltaAvg=_CfprEtherRxStatsMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,17),_CfprEtherRxStatsMulticastPacketsDeltaAvg_Type())
cfprEtherRxStatsMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsMulticastPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsMulticastPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsMulticastPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsMulticastPacketsDeltaMax=_CfprEtherRxStatsMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,18),_CfprEtherRxStatsMulticastPacketsDeltaMax_Type())
cfprEtherRxStatsMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsMulticastPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsMulticastPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsMulticastPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsMulticastPacketsDeltaMin=_CfprEtherRxStatsMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,19),_CfprEtherRxStatsMulticastPacketsDeltaMin_Type())
cfprEtherRxStatsMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsMulticastPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsSuspect_Type=TruthValue
_CfprEtherRxStatsSuspect_Object=MibTableColumn
cfprEtherRxStatsSuspect=_CfprEtherRxStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,20),_CfprEtherRxStatsSuspect_Type())
cfprEtherRxStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsSuspect.setStatus(_A)
_CfprEtherRxStatsThresholded_Type=CfprEtherRxStatsThresholded
_CfprEtherRxStatsThresholded_Object=MibTableColumn
cfprEtherRxStatsThresholded=_CfprEtherRxStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,21),_CfprEtherRxStatsThresholded_Type())
cfprEtherRxStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsThresholded.setStatus(_A)
_CfprEtherRxStatsTimeCollected_Type=DateAndTime
_CfprEtherRxStatsTimeCollected_Object=MibTableColumn
cfprEtherRxStatsTimeCollected=_CfprEtherRxStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,22),_CfprEtherRxStatsTimeCollected_Type())
cfprEtherRxStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTimeCollected.setStatus(_A)
_CfprEtherRxStatsTotalBytes_Type=Unsigned64
_CfprEtherRxStatsTotalBytes_Object=MibTableColumn
cfprEtherRxStatsTotalBytes=_CfprEtherRxStatsTotalBytes_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,23),_CfprEtherRxStatsTotalBytes_Type())
cfprEtherRxStatsTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalBytes.setStatus(_A)
_CfprEtherRxStatsTotalBytesDelta_Type=Counter64
_CfprEtherRxStatsTotalBytesDelta_Object=MibTableColumn
cfprEtherRxStatsTotalBytesDelta=_CfprEtherRxStatsTotalBytesDelta_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,24),_CfprEtherRxStatsTotalBytesDelta_Type())
cfprEtherRxStatsTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalBytesDelta.setStatus(_A)
_CfprEtherRxStatsTotalBytesDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsTotalBytesDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsTotalBytesDeltaAvg=_CfprEtherRxStatsTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,25),_CfprEtherRxStatsTotalBytesDeltaAvg_Type())
cfprEtherRxStatsTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalBytesDeltaAvg.setStatus(_A)
_CfprEtherRxStatsTotalBytesDeltaMax_Type=Unsigned64
_CfprEtherRxStatsTotalBytesDeltaMax_Object=MibTableColumn
cfprEtherRxStatsTotalBytesDeltaMax=_CfprEtherRxStatsTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,26),_CfprEtherRxStatsTotalBytesDeltaMax_Type())
cfprEtherRxStatsTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalBytesDeltaMax.setStatus(_A)
_CfprEtherRxStatsTotalBytesDeltaMin_Type=Unsigned64
_CfprEtherRxStatsTotalBytesDeltaMin_Object=MibTableColumn
cfprEtherRxStatsTotalBytesDeltaMin=_CfprEtherRxStatsTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,27),_CfprEtherRxStatsTotalBytesDeltaMin_Type())
cfprEtherRxStatsTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalBytesDeltaMin.setStatus(_A)
_CfprEtherRxStatsTotalPackets_Type=Unsigned64
_CfprEtherRxStatsTotalPackets_Object=MibTableColumn
cfprEtherRxStatsTotalPackets=_CfprEtherRxStatsTotalPackets_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,28),_CfprEtherRxStatsTotalPackets_Type())
cfprEtherRxStatsTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalPackets.setStatus(_A)
_CfprEtherRxStatsTotalPacketsDelta_Type=Counter64
_CfprEtherRxStatsTotalPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsTotalPacketsDelta=_CfprEtherRxStatsTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,29),_CfprEtherRxStatsTotalPacketsDelta_Type())
cfprEtherRxStatsTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalPacketsDelta.setStatus(_A)
_CfprEtherRxStatsTotalPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsTotalPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsTotalPacketsDeltaAvg=_CfprEtherRxStatsTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,30),_CfprEtherRxStatsTotalPacketsDeltaAvg_Type())
cfprEtherRxStatsTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsTotalPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsTotalPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsTotalPacketsDeltaMax=_CfprEtherRxStatsTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,31),_CfprEtherRxStatsTotalPacketsDeltaMax_Type())
cfprEtherRxStatsTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsTotalPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsTotalPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsTotalPacketsDeltaMin=_CfprEtherRxStatsTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,32),_CfprEtherRxStatsTotalPacketsDeltaMin_Type())
cfprEtherRxStatsTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsTotalPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsUnicastPackets_Type=Unsigned64
_CfprEtherRxStatsUnicastPackets_Object=MibTableColumn
cfprEtherRxStatsUnicastPackets=_CfprEtherRxStatsUnicastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,33),_CfprEtherRxStatsUnicastPackets_Type())
cfprEtherRxStatsUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsUnicastPackets.setStatus(_A)
_CfprEtherRxStatsUnicastPacketsDelta_Type=Counter64
_CfprEtherRxStatsUnicastPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsUnicastPacketsDelta=_CfprEtherRxStatsUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,34),_CfprEtherRxStatsUnicastPacketsDelta_Type())
cfprEtherRxStatsUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsUnicastPacketsDelta.setStatus(_A)
_CfprEtherRxStatsUnicastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsUnicastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsUnicastPacketsDeltaAvg=_CfprEtherRxStatsUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,35),_CfprEtherRxStatsUnicastPacketsDeltaAvg_Type())
cfprEtherRxStatsUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsUnicastPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsUnicastPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsUnicastPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsUnicastPacketsDeltaMax=_CfprEtherRxStatsUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,36),_CfprEtherRxStatsUnicastPacketsDeltaMax_Type())
cfprEtherRxStatsUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsUnicastPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsUnicastPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsUnicastPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsUnicastPacketsDeltaMin=_CfprEtherRxStatsUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,37),_CfprEtherRxStatsUnicastPacketsDeltaMin_Type())
cfprEtherRxStatsUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsUnicastPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsUpdate_Type=Gauge32
_CfprEtherRxStatsUpdate_Object=MibTableColumn
cfprEtherRxStatsUpdate=_CfprEtherRxStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,18,1,38),_CfprEtherRxStatsUpdate_Type())
cfprEtherRxStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsUpdate.setStatus(_A)
_CfprEtherRxStatsHistTable_Object=MibTable
cfprEtherRxStatsHistTable=_CfprEtherRxStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,19))
if mibBuilder.loadTexts:cfprEtherRxStatsHistTable.setStatus(_A)
_CfprEtherRxStatsHistEntry_Object=MibTableRow
cfprEtherRxStatsHistEntry=_CfprEtherRxStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,19,1))
cfprEtherRxStatsHistEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cfprEtherRxStatsHistEntry.setStatus(_A)
_CfprEtherRxStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherRxStatsHistInstanceId_Object=MibTableColumn
cfprEtherRxStatsHistInstanceId=_CfprEtherRxStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,1),_CfprEtherRxStatsHistInstanceId_Type())
cfprEtherRxStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherRxStatsHistInstanceId.setStatus(_A)
_CfprEtherRxStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherRxStatsHistDn_Object=MibTableColumn
cfprEtherRxStatsHistDn=_CfprEtherRxStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,2),_CfprEtherRxStatsHistDn_Type())
cfprEtherRxStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistDn.setStatus(_A)
_CfprEtherRxStatsHistRn_Type=SnmpAdminString
_CfprEtherRxStatsHistRn_Object=MibTableColumn
cfprEtherRxStatsHistRn=_CfprEtherRxStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,3),_CfprEtherRxStatsHistRn_Type())
cfprEtherRxStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistRn.setStatus(_A)
_CfprEtherRxStatsHistBroadcastPackets_Type=Unsigned64
_CfprEtherRxStatsHistBroadcastPackets_Object=MibTableColumn
cfprEtherRxStatsHistBroadcastPackets=_CfprEtherRxStatsHistBroadcastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,4),_CfprEtherRxStatsHistBroadcastPackets_Type())
cfprEtherRxStatsHistBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistBroadcastPackets.setStatus(_A)
_CfprEtherRxStatsHistBroadcastPacketsDelta_Type=Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDelta=_CfprEtherRxStatsHistBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,5),_CfprEtherRxStatsHistBroadcastPacketsDelta_Type())
cfprEtherRxStatsHistBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistBroadcastPacketsDelta.setStatus(_A)
_CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDeltaAvg=_CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,6),_CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Type())
cfprEtherRxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistBroadcastPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDeltaMax=_CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,7),_CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Type())
cfprEtherRxStatsHistBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistBroadcastPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDeltaMin=_CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,8),_CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Type())
cfprEtherRxStatsHistBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistBroadcastPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsHistId_Type=Unsigned64
_CfprEtherRxStatsHistId_Object=MibTableColumn
cfprEtherRxStatsHistId=_CfprEtherRxStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,9),_CfprEtherRxStatsHistId_Type())
cfprEtherRxStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistId.setStatus(_A)
_CfprEtherRxStatsHistJumboPackets_Type=Unsigned64
_CfprEtherRxStatsHistJumboPackets_Object=MibTableColumn
cfprEtherRxStatsHistJumboPackets=_CfprEtherRxStatsHistJumboPackets_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,10),_CfprEtherRxStatsHistJumboPackets_Type())
cfprEtherRxStatsHistJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistJumboPackets.setStatus(_A)
_CfprEtherRxStatsHistJumboPacketsDelta_Type=Unsigned64
_CfprEtherRxStatsHistJumboPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsHistJumboPacketsDelta=_CfprEtherRxStatsHistJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,11),_CfprEtherRxStatsHistJumboPacketsDelta_Type())
cfprEtherRxStatsHistJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistJumboPacketsDelta.setStatus(_A)
_CfprEtherRxStatsHistJumboPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsHistJumboPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsHistJumboPacketsDeltaAvg=_CfprEtherRxStatsHistJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,12),_CfprEtherRxStatsHistJumboPacketsDeltaAvg_Type())
cfprEtherRxStatsHistJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistJumboPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsHistJumboPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsHistJumboPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsHistJumboPacketsDeltaMax=_CfprEtherRxStatsHistJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,13),_CfprEtherRxStatsHistJumboPacketsDeltaMax_Type())
cfprEtherRxStatsHistJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistJumboPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsHistJumboPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsHistJumboPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsHistJumboPacketsDeltaMin=_CfprEtherRxStatsHistJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,14),_CfprEtherRxStatsHistJumboPacketsDeltaMin_Type())
cfprEtherRxStatsHistJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistJumboPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsHistMostRecent_Type=TruthValue
_CfprEtherRxStatsHistMostRecent_Object=MibTableColumn
cfprEtherRxStatsHistMostRecent=_CfprEtherRxStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,15),_CfprEtherRxStatsHistMostRecent_Type())
cfprEtherRxStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistMostRecent.setStatus(_A)
_CfprEtherRxStatsHistMulticastPackets_Type=Unsigned64
_CfprEtherRxStatsHistMulticastPackets_Object=MibTableColumn
cfprEtherRxStatsHistMulticastPackets=_CfprEtherRxStatsHistMulticastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,16),_CfprEtherRxStatsHistMulticastPackets_Type())
cfprEtherRxStatsHistMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistMulticastPackets.setStatus(_A)
_CfprEtherRxStatsHistMulticastPacketsDelta_Type=Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDelta=_CfprEtherRxStatsHistMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,17),_CfprEtherRxStatsHistMulticastPacketsDelta_Type())
cfprEtherRxStatsHistMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistMulticastPacketsDelta.setStatus(_A)
_CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDeltaAvg=_CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,18),_CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Type())
cfprEtherRxStatsHistMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistMulticastPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsHistMulticastPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDeltaMax=_CfprEtherRxStatsHistMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,19),_CfprEtherRxStatsHistMulticastPacketsDeltaMax_Type())
cfprEtherRxStatsHistMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistMulticastPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsHistMulticastPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDeltaMin=_CfprEtherRxStatsHistMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,20),_CfprEtherRxStatsHistMulticastPacketsDeltaMin_Type())
cfprEtherRxStatsHistMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistMulticastPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsHistSuspect_Type=TruthValue
_CfprEtherRxStatsHistSuspect_Object=MibTableColumn
cfprEtherRxStatsHistSuspect=_CfprEtherRxStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,21),_CfprEtherRxStatsHistSuspect_Type())
cfprEtherRxStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistSuspect.setStatus(_A)
_CfprEtherRxStatsHistThresholded_Type=CfprEtherRxStatsHistThresholded
_CfprEtherRxStatsHistThresholded_Object=MibTableColumn
cfprEtherRxStatsHistThresholded=_CfprEtherRxStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,22),_CfprEtherRxStatsHistThresholded_Type())
cfprEtherRxStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistThresholded.setStatus(_A)
_CfprEtherRxStatsHistTimeCollected_Type=DateAndTime
_CfprEtherRxStatsHistTimeCollected_Object=MibTableColumn
cfprEtherRxStatsHistTimeCollected=_CfprEtherRxStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,23),_CfprEtherRxStatsHistTimeCollected_Type())
cfprEtherRxStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTimeCollected.setStatus(_A)
_CfprEtherRxStatsHistTotalBytes_Type=Unsigned64
_CfprEtherRxStatsHistTotalBytes_Object=MibTableColumn
cfprEtherRxStatsHistTotalBytes=_CfprEtherRxStatsHistTotalBytes_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,24),_CfprEtherRxStatsHistTotalBytes_Type())
cfprEtherRxStatsHistTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalBytes.setStatus(_A)
_CfprEtherRxStatsHistTotalBytesDelta_Type=Unsigned64
_CfprEtherRxStatsHistTotalBytesDelta_Object=MibTableColumn
cfprEtherRxStatsHistTotalBytesDelta=_CfprEtherRxStatsHistTotalBytesDelta_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,25),_CfprEtherRxStatsHistTotalBytesDelta_Type())
cfprEtherRxStatsHistTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalBytesDelta.setStatus(_A)
_CfprEtherRxStatsHistTotalBytesDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsHistTotalBytesDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsHistTotalBytesDeltaAvg=_CfprEtherRxStatsHistTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,26),_CfprEtherRxStatsHistTotalBytesDeltaAvg_Type())
cfprEtherRxStatsHistTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalBytesDeltaAvg.setStatus(_A)
_CfprEtherRxStatsHistTotalBytesDeltaMax_Type=Unsigned64
_CfprEtherRxStatsHistTotalBytesDeltaMax_Object=MibTableColumn
cfprEtherRxStatsHistTotalBytesDeltaMax=_CfprEtherRxStatsHistTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,27),_CfprEtherRxStatsHistTotalBytesDeltaMax_Type())
cfprEtherRxStatsHistTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalBytesDeltaMax.setStatus(_A)
_CfprEtherRxStatsHistTotalBytesDeltaMin_Type=Unsigned64
_CfprEtherRxStatsHistTotalBytesDeltaMin_Object=MibTableColumn
cfprEtherRxStatsHistTotalBytesDeltaMin=_CfprEtherRxStatsHistTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,28),_CfprEtherRxStatsHistTotalBytesDeltaMin_Type())
cfprEtherRxStatsHistTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalBytesDeltaMin.setStatus(_A)
_CfprEtherRxStatsHistTotalPackets_Type=Unsigned64
_CfprEtherRxStatsHistTotalPackets_Object=MibTableColumn
cfprEtherRxStatsHistTotalPackets=_CfprEtherRxStatsHistTotalPackets_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,29),_CfprEtherRxStatsHistTotalPackets_Type())
cfprEtherRxStatsHistTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalPackets.setStatus(_A)
_CfprEtherRxStatsHistTotalPacketsDelta_Type=Unsigned64
_CfprEtherRxStatsHistTotalPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsHistTotalPacketsDelta=_CfprEtherRxStatsHistTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,30),_CfprEtherRxStatsHistTotalPacketsDelta_Type())
cfprEtherRxStatsHistTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalPacketsDelta.setStatus(_A)
_CfprEtherRxStatsHistTotalPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsHistTotalPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsHistTotalPacketsDeltaAvg=_CfprEtherRxStatsHistTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,31),_CfprEtherRxStatsHistTotalPacketsDeltaAvg_Type())
cfprEtherRxStatsHistTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsHistTotalPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsHistTotalPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsHistTotalPacketsDeltaMax=_CfprEtherRxStatsHistTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,32),_CfprEtherRxStatsHistTotalPacketsDeltaMax_Type())
cfprEtherRxStatsHistTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsHistTotalPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsHistTotalPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsHistTotalPacketsDeltaMin=_CfprEtherRxStatsHistTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,33),_CfprEtherRxStatsHistTotalPacketsDeltaMin_Type())
cfprEtherRxStatsHistTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistTotalPacketsDeltaMin.setStatus(_A)
_CfprEtherRxStatsHistUnicastPackets_Type=Unsigned64
_CfprEtherRxStatsHistUnicastPackets_Object=MibTableColumn
cfprEtherRxStatsHistUnicastPackets=_CfprEtherRxStatsHistUnicastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,34),_CfprEtherRxStatsHistUnicastPackets_Type())
cfprEtherRxStatsHistUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistUnicastPackets.setStatus(_A)
_CfprEtherRxStatsHistUnicastPacketsDelta_Type=Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDelta_Object=MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDelta=_CfprEtherRxStatsHistUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,35),_CfprEtherRxStatsHistUnicastPacketsDelta_Type())
cfprEtherRxStatsHistUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistUnicastPacketsDelta.setStatus(_A)
_CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDeltaAvg=_CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,36),_CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Type())
cfprEtherRxStatsHistUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistUnicastPacketsDeltaAvg.setStatus(_A)
_CfprEtherRxStatsHistUnicastPacketsDeltaMax_Type=Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDeltaMax_Object=MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDeltaMax=_CfprEtherRxStatsHistUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,37),_CfprEtherRxStatsHistUnicastPacketsDeltaMax_Type())
cfprEtherRxStatsHistUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistUnicastPacketsDeltaMax.setStatus(_A)
_CfprEtherRxStatsHistUnicastPacketsDeltaMin_Type=Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDeltaMin_Object=MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDeltaMin=_CfprEtherRxStatsHistUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,19,1,38),_CfprEtherRxStatsHistUnicastPacketsDeltaMin_Type())
cfprEtherRxStatsHistUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherRxStatsHistUnicastPacketsDeltaMin.setStatus(_A)
_CfprEtherServerIntFIoTable_Object=MibTable
cfprEtherServerIntFIoTable=_CfprEtherServerIntFIoTable_Object((1,3,6,1,4,1,9,9,826,1,21,20))
if mibBuilder.loadTexts:cfprEtherServerIntFIoTable.setStatus(_A)
_CfprEtherServerIntFIoEntry_Object=MibTableRow
cfprEtherServerIntFIoEntry=_CfprEtherServerIntFIoEntry_Object((1,3,6,1,4,1,9,9,826,1,21,20,1))
cfprEtherServerIntFIoEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cfprEtherServerIntFIoEntry.setStatus(_A)
_CfprEtherServerIntFIoInstanceId_Type=CfprManagedObjectId
_CfprEtherServerIntFIoInstanceId_Object=MibTableColumn
cfprEtherServerIntFIoInstanceId=_CfprEtherServerIntFIoInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,1),_CfprEtherServerIntFIoInstanceId_Type())
cfprEtherServerIntFIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherServerIntFIoInstanceId.setStatus(_A)
_CfprEtherServerIntFIoDn_Type=CfprManagedObjectDn
_CfprEtherServerIntFIoDn_Object=MibTableColumn
cfprEtherServerIntFIoDn=_CfprEtherServerIntFIoDn_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,2),_CfprEtherServerIntFIoDn_Type())
cfprEtherServerIntFIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoDn.setStatus(_A)
_CfprEtherServerIntFIoRn_Type=SnmpAdminString
_CfprEtherServerIntFIoRn_Object=MibTableColumn
cfprEtherServerIntFIoRn=_CfprEtherServerIntFIoRn_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,3),_CfprEtherServerIntFIoRn_Type())
cfprEtherServerIntFIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoRn.setStatus(_A)
_CfprEtherServerIntFIoAdminSpeed_Type=CfprPortEthSpeed
_CfprEtherServerIntFIoAdminSpeed_Object=MibTableColumn
cfprEtherServerIntFIoAdminSpeed=_CfprEtherServerIntFIoAdminSpeed_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,4),_CfprEtherServerIntFIoAdminSpeed_Type())
cfprEtherServerIntFIoAdminSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoAdminSpeed.setStatus(_A)
_CfprEtherServerIntFIoAdminState_Type=CfprEtherServerIntFIoAdminState
_CfprEtherServerIntFIoAdminState_Object=MibTableColumn
cfprEtherServerIntFIoAdminState=_CfprEtherServerIntFIoAdminState_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,5),_CfprEtherServerIntFIoAdminState_Type())
cfprEtherServerIntFIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoAdminState.setStatus(_A)
_CfprEtherServerIntFIoAggrPortId_Type=Gauge32
_CfprEtherServerIntFIoAggrPortId_Object=MibTableColumn
cfprEtherServerIntFIoAggrPortId=_CfprEtherServerIntFIoAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,6),_CfprEtherServerIntFIoAggrPortId_Type())
cfprEtherServerIntFIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoAggrPortId.setStatus(_A)
_CfprEtherServerIntFIoChassisId_Type=Gauge32
_CfprEtherServerIntFIoChassisId_Object=MibTableColumn
cfprEtherServerIntFIoChassisId=_CfprEtherServerIntFIoChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,7),_CfprEtherServerIntFIoChassisId_Type())
cfprEtherServerIntFIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoChassisId.setStatus(_A)
_CfprEtherServerIntFIoEncap_Type=CfprPortEncap
_CfprEtherServerIntFIoEncap_Object=MibTableColumn
cfprEtherServerIntFIoEncap=_CfprEtherServerIntFIoEncap_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,8),_CfprEtherServerIntFIoEncap_Type())
cfprEtherServerIntFIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoEncap.setStatus(_A)
_CfprEtherServerIntFIoEpDn_Type=SnmpAdminString
_CfprEtherServerIntFIoEpDn_Object=MibTableColumn
cfprEtherServerIntFIoEpDn=_CfprEtherServerIntFIoEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,9),_CfprEtherServerIntFIoEpDn_Type())
cfprEtherServerIntFIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoEpDn.setStatus(_A)
_CfprEtherServerIntFIoFltAggr_Type=Unsigned64
_CfprEtherServerIntFIoFltAggr_Object=MibTableColumn
cfprEtherServerIntFIoFltAggr=_CfprEtherServerIntFIoFltAggr_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,10),_CfprEtherServerIntFIoFltAggr_Type())
cfprEtherServerIntFIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFltAggr.setStatus(_A)
_CfprEtherServerIntFIoFsmDescr_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmDescr_Object=MibTableColumn
cfprEtherServerIntFIoFsmDescr=_CfprEtherServerIntFIoFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,11),_CfprEtherServerIntFIoFsmDescr_Type())
cfprEtherServerIntFIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmDescr.setStatus(_A)
_CfprEtherServerIntFIoFsmPrev_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmPrev_Object=MibTableColumn
cfprEtherServerIntFIoFsmPrev=_CfprEtherServerIntFIoFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,12),_CfprEtherServerIntFIoFsmPrev_Type())
cfprEtherServerIntFIoFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmPrev.setStatus(_A)
_CfprEtherServerIntFIoFsmProgr_Type=Gauge32
_CfprEtherServerIntFIoFsmProgr_Object=MibTableColumn
cfprEtherServerIntFIoFsmProgr=_CfprEtherServerIntFIoFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,13),_CfprEtherServerIntFIoFsmProgr_Type())
cfprEtherServerIntFIoFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmProgr.setStatus(_A)
_CfprEtherServerIntFIoFsmRmtInvErrCode_Type=Gauge32
_CfprEtherServerIntFIoFsmRmtInvErrCode_Object=MibTableColumn
cfprEtherServerIntFIoFsmRmtInvErrCode=_CfprEtherServerIntFIoFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,14),_CfprEtherServerIntFIoFsmRmtInvErrCode_Type())
cfprEtherServerIntFIoFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRmtInvErrCode.setStatus(_A)
_CfprEtherServerIntFIoFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmRmtInvErrDescr_Object=MibTableColumn
cfprEtherServerIntFIoFsmRmtInvErrDescr=_CfprEtherServerIntFIoFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,15),_CfprEtherServerIntFIoFsmRmtInvErrDescr_Type())
cfprEtherServerIntFIoFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRmtInvErrDescr.setStatus(_A)
_CfprEtherServerIntFIoFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprEtherServerIntFIoFsmRmtInvRslt_Object=MibTableColumn
cfprEtherServerIntFIoFsmRmtInvRslt=_CfprEtherServerIntFIoFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,16),_CfprEtherServerIntFIoFsmRmtInvRslt_Type())
cfprEtherServerIntFIoFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRmtInvRslt.setStatus(_A)
_CfprEtherServerIntFIoFsmStageDescr_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmStageDescr_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageDescr=_CfprEtherServerIntFIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,17),_CfprEtherServerIntFIoFsmStageDescr_Type())
cfprEtherServerIntFIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageDescr.setStatus(_A)
_CfprEtherServerIntFIoFsmStamp_Type=DateAndTime
_CfprEtherServerIntFIoFsmStamp_Object=MibTableColumn
cfprEtherServerIntFIoFsmStamp=_CfprEtherServerIntFIoFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,18),_CfprEtherServerIntFIoFsmStamp_Type())
cfprEtherServerIntFIoFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStamp.setStatus(_A)
_CfprEtherServerIntFIoFsmStatus_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmStatus_Object=MibTableColumn
cfprEtherServerIntFIoFsmStatus=_CfprEtherServerIntFIoFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,19),_CfprEtherServerIntFIoFsmStatus_Type())
cfprEtherServerIntFIoFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStatus.setStatus(_A)
_CfprEtherServerIntFIoFsmTry_Type=Gauge32
_CfprEtherServerIntFIoFsmTry_Object=MibTableColumn
cfprEtherServerIntFIoFsmTry=_CfprEtherServerIntFIoFsmTry_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,20),_CfprEtherServerIntFIoFsmTry_Type())
cfprEtherServerIntFIoFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTry.setStatus(_A)
_CfprEtherServerIntFIoIfRole_Type=CfprEtherServerIntFIoIfRole
_CfprEtherServerIntFIoIfRole_Object=MibTableColumn
cfprEtherServerIntFIoIfRole=_CfprEtherServerIntFIoIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,21),_CfprEtherServerIntFIoIfRole_Type())
cfprEtherServerIntFIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoIfRole.setStatus(_A)
_CfprEtherServerIntFIoIfType_Type=CfprNetworkPhysEpIfType
_CfprEtherServerIntFIoIfType_Object=MibTableColumn
cfprEtherServerIntFIoIfType=_CfprEtherServerIntFIoIfType_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,22),_CfprEtherServerIntFIoIfType_Type())
cfprEtherServerIntFIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoIfType.setStatus(_A)
_CfprEtherServerIntFIoLocale_Type=CfprEtherServerIntFIoLocale
_CfprEtherServerIntFIoLocale_Object=MibTableColumn
cfprEtherServerIntFIoLocale=_CfprEtherServerIntFIoLocale_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,23),_CfprEtherServerIntFIoLocale_Type())
cfprEtherServerIntFIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoLocale.setStatus(_A)
_CfprEtherServerIntFIoMac_Type=MacAddress
_CfprEtherServerIntFIoMac_Object=MibTableColumn
cfprEtherServerIntFIoMac=_CfprEtherServerIntFIoMac_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,24),_CfprEtherServerIntFIoMac_Type())
cfprEtherServerIntFIoMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoMac.setStatus(_A)
_CfprEtherServerIntFIoMode_Type=CfprPortMode
_CfprEtherServerIntFIoMode_Object=MibTableColumn
cfprEtherServerIntFIoMode=_CfprEtherServerIntFIoMode_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,25),_CfprEtherServerIntFIoMode_Type())
cfprEtherServerIntFIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoMode.setStatus(_A)
_CfprEtherServerIntFIoModel_Type=SnmpAdminString
_CfprEtherServerIntFIoModel_Object=MibTableColumn
cfprEtherServerIntFIoModel=_CfprEtherServerIntFIoModel_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,26),_CfprEtherServerIntFIoModel_Type())
cfprEtherServerIntFIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoModel.setStatus(_A)
_CfprEtherServerIntFIoName_Type=SnmpAdminString
_CfprEtherServerIntFIoName_Object=MibTableColumn
cfprEtherServerIntFIoName=_CfprEtherServerIntFIoName_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,27),_CfprEtherServerIntFIoName_Type())
cfprEtherServerIntFIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoName.setStatus(_A)
_CfprEtherServerIntFIoNsSize_Type=Gauge32
_CfprEtherServerIntFIoNsSize_Object=MibTableColumn
cfprEtherServerIntFIoNsSize=_CfprEtherServerIntFIoNsSize_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,28),_CfprEtherServerIntFIoNsSize_Type())
cfprEtherServerIntFIoNsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoNsSize.setStatus(_A)
_CfprEtherServerIntFIoOperBorderAggrPortId_Type=Gauge32
_CfprEtherServerIntFIoOperBorderAggrPortId_Object=MibTableColumn
cfprEtherServerIntFIoOperBorderAggrPortId=_CfprEtherServerIntFIoOperBorderAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,29),_CfprEtherServerIntFIoOperBorderAggrPortId_Type())
cfprEtherServerIntFIoOperBorderAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoOperBorderAggrPortId.setStatus(_A)
_CfprEtherServerIntFIoOperBorderPortId_Type=Gauge32
_CfprEtherServerIntFIoOperBorderPortId_Object=MibTableColumn
cfprEtherServerIntFIoOperBorderPortId=_CfprEtherServerIntFIoOperBorderPortId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,30),_CfprEtherServerIntFIoOperBorderPortId_Type())
cfprEtherServerIntFIoOperBorderPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoOperBorderPortId.setStatus(_A)
_CfprEtherServerIntFIoOperBorderSlotId_Type=Gauge32
_CfprEtherServerIntFIoOperBorderSlotId_Object=MibTableColumn
cfprEtherServerIntFIoOperBorderSlotId=_CfprEtherServerIntFIoOperBorderSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,31),_CfprEtherServerIntFIoOperBorderSlotId_Type())
cfprEtherServerIntFIoOperBorderSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoOperBorderSlotId.setStatus(_A)
_CfprEtherServerIntFIoOperState_Type=CfprNetworkPortOperState
_CfprEtherServerIntFIoOperState_Object=MibTableColumn
cfprEtherServerIntFIoOperState=_CfprEtherServerIntFIoOperState_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,32),_CfprEtherServerIntFIoOperState_Type())
cfprEtherServerIntFIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoOperState.setStatus(_A)
_CfprEtherServerIntFIoPeerAggrPortId_Type=Gauge32
_CfprEtherServerIntFIoPeerAggrPortId_Object=MibTableColumn
cfprEtherServerIntFIoPeerAggrPortId=_CfprEtherServerIntFIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,33),_CfprEtherServerIntFIoPeerAggrPortId_Type())
cfprEtherServerIntFIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPeerAggrPortId.setStatus(_A)
_CfprEtherServerIntFIoPeerChassisId_Type=Gauge32
_CfprEtherServerIntFIoPeerChassisId_Object=MibTableColumn
cfprEtherServerIntFIoPeerChassisId=_CfprEtherServerIntFIoPeerChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,34),_CfprEtherServerIntFIoPeerChassisId_Type())
cfprEtherServerIntFIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPeerChassisId.setStatus(_A)
_CfprEtherServerIntFIoPeerDn_Type=SnmpAdminString
_CfprEtherServerIntFIoPeerDn_Object=MibTableColumn
cfprEtherServerIntFIoPeerDn=_CfprEtherServerIntFIoPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,35),_CfprEtherServerIntFIoPeerDn_Type())
cfprEtherServerIntFIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPeerDn.setStatus(_A)
_CfprEtherServerIntFIoPeerEncap_Type=Gauge32
_CfprEtherServerIntFIoPeerEncap_Object=MibTableColumn
cfprEtherServerIntFIoPeerEncap=_CfprEtherServerIntFIoPeerEncap_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,36),_CfprEtherServerIntFIoPeerEncap_Type())
cfprEtherServerIntFIoPeerEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPeerEncap.setStatus(_A)
_CfprEtherServerIntFIoPeerPortId_Type=Gauge32
_CfprEtherServerIntFIoPeerPortId_Object=MibTableColumn
cfprEtherServerIntFIoPeerPortId=_CfprEtherServerIntFIoPeerPortId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,37),_CfprEtherServerIntFIoPeerPortId_Type())
cfprEtherServerIntFIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPeerPortId.setStatus(_A)
_CfprEtherServerIntFIoPeerSlotId_Type=Gauge32
_CfprEtherServerIntFIoPeerSlotId_Object=MibTableColumn
cfprEtherServerIntFIoPeerSlotId=_CfprEtherServerIntFIoPeerSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,38),_CfprEtherServerIntFIoPeerSlotId_Type())
cfprEtherServerIntFIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPeerSlotId.setStatus(_A)
_CfprEtherServerIntFIoPortId_Type=Gauge32
_CfprEtherServerIntFIoPortId_Object=MibTableColumn
cfprEtherServerIntFIoPortId=_CfprEtherServerIntFIoPortId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,39),_CfprEtherServerIntFIoPortId_Type())
cfprEtherServerIntFIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPortId.setStatus(_A)
_CfprEtherServerIntFIoRevision_Type=SnmpAdminString
_CfprEtherServerIntFIoRevision_Object=MibTableColumn
cfprEtherServerIntFIoRevision=_CfprEtherServerIntFIoRevision_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,40),_CfprEtherServerIntFIoRevision_Type())
cfprEtherServerIntFIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoRevision.setStatus(_A)
_CfprEtherServerIntFIoSerial_Type=SnmpAdminString
_CfprEtherServerIntFIoSerial_Object=MibTableColumn
cfprEtherServerIntFIoSerial=_CfprEtherServerIntFIoSerial_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,41),_CfprEtherServerIntFIoSerial_Type())
cfprEtherServerIntFIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoSerial.setStatus(_A)
_CfprEtherServerIntFIoSlotId_Type=Gauge32
_CfprEtherServerIntFIoSlotId_Object=MibTableColumn
cfprEtherServerIntFIoSlotId=_CfprEtherServerIntFIoSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,42),_CfprEtherServerIntFIoSlotId_Type())
cfprEtherServerIntFIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoSlotId.setStatus(_A)
_CfprEtherServerIntFIoStateQual_Type=SnmpAdminString
_CfprEtherServerIntFIoStateQual_Object=MibTableColumn
cfprEtherServerIntFIoStateQual=_CfprEtherServerIntFIoStateQual_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,43),_CfprEtherServerIntFIoStateQual_Type())
cfprEtherServerIntFIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoStateQual.setStatus(_A)
_CfprEtherServerIntFIoSwitchId_Type=CfprNetworkSwitchId
_CfprEtherServerIntFIoSwitchId_Object=MibTableColumn
cfprEtherServerIntFIoSwitchId=_CfprEtherServerIntFIoSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,44),_CfprEtherServerIntFIoSwitchId_Type())
cfprEtherServerIntFIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoSwitchId.setStatus(_A)
_CfprEtherServerIntFIoTransport_Type=CfprEtherServerIntFIoTransport
_CfprEtherServerIntFIoTransport_Object=MibTableColumn
cfprEtherServerIntFIoTransport=_CfprEtherServerIntFIoTransport_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,45),_CfprEtherServerIntFIoTransport_Type())
cfprEtherServerIntFIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoTransport.setStatus(_A)
_CfprEtherServerIntFIoTs_Type=DateAndTime
_CfprEtherServerIntFIoTs_Object=MibTableColumn
cfprEtherServerIntFIoTs=_CfprEtherServerIntFIoTs_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,46),_CfprEtherServerIntFIoTs_Type())
cfprEtherServerIntFIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoTs.setStatus(_A)
_CfprEtherServerIntFIoType_Type=CfprEtherServerIntFIoType
_CfprEtherServerIntFIoType_Object=MibTableColumn
cfprEtherServerIntFIoType=_CfprEtherServerIntFIoType_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,47),_CfprEtherServerIntFIoType_Type())
cfprEtherServerIntFIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoType.setStatus(_A)
_CfprEtherServerIntFIoVendor_Type=SnmpAdminString
_CfprEtherServerIntFIoVendor_Object=MibTableColumn
cfprEtherServerIntFIoVendor=_CfprEtherServerIntFIoVendor_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,48),_CfprEtherServerIntFIoVendor_Type())
cfprEtherServerIntFIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoVendor.setStatus(_A)
_CfprEtherServerIntFIoXcvrType_Type=CfprEquipmentXcvrType
_CfprEtherServerIntFIoXcvrType_Object=MibTableColumn
cfprEtherServerIntFIoXcvrType=_CfprEtherServerIntFIoXcvrType_Object((1,3,6,1,4,1,9,9,826,1,21,20,1,49),_CfprEtherServerIntFIoXcvrType_Type())
cfprEtherServerIntFIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoXcvrType.setStatus(_A)
_CfprEtherServerIntFIoFsmTable_Object=MibTable
cfprEtherServerIntFIoFsmTable=_CfprEtherServerIntFIoFsmTable_Object((1,3,6,1,4,1,9,9,826,1,21,21))
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTable.setStatus(_A)
_CfprEtherServerIntFIoFsmEntry_Object=MibTableRow
cfprEtherServerIntFIoFsmEntry=_CfprEtherServerIntFIoFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,21,21,1))
cfprEtherServerIntFIoFsmEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmEntry.setStatus(_A)
_CfprEtherServerIntFIoFsmInstanceId_Type=CfprManagedObjectId
_CfprEtherServerIntFIoFsmInstanceId_Object=MibTableColumn
cfprEtherServerIntFIoFsmInstanceId=_CfprEtherServerIntFIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,1),_CfprEtherServerIntFIoFsmInstanceId_Type())
cfprEtherServerIntFIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmInstanceId.setStatus(_A)
_CfprEtherServerIntFIoFsmDn_Type=CfprManagedObjectDn
_CfprEtherServerIntFIoFsmDn_Object=MibTableColumn
cfprEtherServerIntFIoFsmDn=_CfprEtherServerIntFIoFsmDn_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,2),_CfprEtherServerIntFIoFsmDn_Type())
cfprEtherServerIntFIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmDn.setStatus(_A)
_CfprEtherServerIntFIoFsmRn_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmRn_Object=MibTableColumn
cfprEtherServerIntFIoFsmRn=_CfprEtherServerIntFIoFsmRn_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,3),_CfprEtherServerIntFIoFsmRn_Type())
cfprEtherServerIntFIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRn.setStatus(_A)
_CfprEtherServerIntFIoFsmCompletionTime_Type=DateAndTime
_CfprEtherServerIntFIoFsmCompletionTime_Object=MibTableColumn
cfprEtherServerIntFIoFsmCompletionTime=_CfprEtherServerIntFIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,4),_CfprEtherServerIntFIoFsmCompletionTime_Type())
cfprEtherServerIntFIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmCompletionTime.setStatus(_A)
_CfprEtherServerIntFIoFsmCurrentFsm_Type=CfprEtherServerIntFIoFsmCurrentFsm
_CfprEtherServerIntFIoFsmCurrentFsm_Object=MibTableColumn
cfprEtherServerIntFIoFsmCurrentFsm=_CfprEtherServerIntFIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,5),_CfprEtherServerIntFIoFsmCurrentFsm_Type())
cfprEtherServerIntFIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmCurrentFsm.setStatus(_A)
_CfprEtherServerIntFIoFsmDescrData_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmDescrData_Object=MibTableColumn
cfprEtherServerIntFIoFsmDescrData=_CfprEtherServerIntFIoFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,6),_CfprEtherServerIntFIoFsmDescrData_Type())
cfprEtherServerIntFIoFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmDescrData.setStatus(_A)
_CfprEtherServerIntFIoFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprEtherServerIntFIoFsmFsmStatus_Object=MibTableColumn
cfprEtherServerIntFIoFsmFsmStatus=_CfprEtherServerIntFIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,7),_CfprEtherServerIntFIoFsmFsmStatus_Type())
cfprEtherServerIntFIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmFsmStatus.setStatus(_A)
_CfprEtherServerIntFIoFsmProgress_Type=Gauge32
_CfprEtherServerIntFIoFsmProgress_Object=MibTableColumn
cfprEtherServerIntFIoFsmProgress=_CfprEtherServerIntFIoFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,8),_CfprEtherServerIntFIoFsmProgress_Type())
cfprEtherServerIntFIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmProgress.setStatus(_A)
_CfprEtherServerIntFIoFsmRmtErrCode_Type=Gauge32
_CfprEtherServerIntFIoFsmRmtErrCode_Object=MibTableColumn
cfprEtherServerIntFIoFsmRmtErrCode=_CfprEtherServerIntFIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,9),_CfprEtherServerIntFIoFsmRmtErrCode_Type())
cfprEtherServerIntFIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRmtErrCode.setStatus(_A)
_CfprEtherServerIntFIoFsmRmtErrDescr_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmRmtErrDescr_Object=MibTableColumn
cfprEtherServerIntFIoFsmRmtErrDescr=_CfprEtherServerIntFIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,10),_CfprEtherServerIntFIoFsmRmtErrDescr_Type())
cfprEtherServerIntFIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRmtErrDescr.setStatus(_A)
_CfprEtherServerIntFIoFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprEtherServerIntFIoFsmRmtRslt_Object=MibTableColumn
cfprEtherServerIntFIoFsmRmtRslt=_CfprEtherServerIntFIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,21,21,1,11),_CfprEtherServerIntFIoFsmRmtRslt_Type())
cfprEtherServerIntFIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmRmtRslt.setStatus(_A)
_CfprEtherServerIntFIoFsmStageTable_Object=MibTable
cfprEtherServerIntFIoFsmStageTable=_CfprEtherServerIntFIoFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,21,22))
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageTable.setStatus(_A)
_CfprEtherServerIntFIoFsmStageEntry_Object=MibTableRow
cfprEtherServerIntFIoFsmStageEntry=_CfprEtherServerIntFIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,21,22,1))
cfprEtherServerIntFIoFsmStageEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageEntry.setStatus(_A)
_CfprEtherServerIntFIoFsmStageInstanceId_Type=CfprManagedObjectId
_CfprEtherServerIntFIoFsmStageInstanceId_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageInstanceId=_CfprEtherServerIntFIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,1),_CfprEtherServerIntFIoFsmStageInstanceId_Type())
cfprEtherServerIntFIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageInstanceId.setStatus(_A)
_CfprEtherServerIntFIoFsmStageDn_Type=CfprManagedObjectDn
_CfprEtherServerIntFIoFsmStageDn_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageDn=_CfprEtherServerIntFIoFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,2),_CfprEtherServerIntFIoFsmStageDn_Type())
cfprEtherServerIntFIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageDn.setStatus(_A)
_CfprEtherServerIntFIoFsmStageRn_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmStageRn_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageRn=_CfprEtherServerIntFIoFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,3),_CfprEtherServerIntFIoFsmStageRn_Type())
cfprEtherServerIntFIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageRn.setStatus(_A)
_CfprEtherServerIntFIoFsmStageDescrData_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmStageDescrData_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageDescrData=_CfprEtherServerIntFIoFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,4),_CfprEtherServerIntFIoFsmStageDescrData_Type())
cfprEtherServerIntFIoFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageDescrData.setStatus(_A)
_CfprEtherServerIntFIoFsmStageLastUpdateTime_Type=DateAndTime
_CfprEtherServerIntFIoFsmStageLastUpdateTime_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageLastUpdateTime=_CfprEtherServerIntFIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,5),_CfprEtherServerIntFIoFsmStageLastUpdateTime_Type())
cfprEtherServerIntFIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageLastUpdateTime.setStatus(_A)
_CfprEtherServerIntFIoFsmStageName_Type=CfprEtherServerIntFIoFsmStageName
_CfprEtherServerIntFIoFsmStageName_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageName=_CfprEtherServerIntFIoFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,6),_CfprEtherServerIntFIoFsmStageName_Type())
cfprEtherServerIntFIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageName.setStatus(_A)
_CfprEtherServerIntFIoFsmStageOrder_Type=Gauge32
_CfprEtherServerIntFIoFsmStageOrder_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageOrder=_CfprEtherServerIntFIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,7),_CfprEtherServerIntFIoFsmStageOrder_Type())
cfprEtherServerIntFIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageOrder.setStatus(_A)
_CfprEtherServerIntFIoFsmStageRetry_Type=Gauge32
_CfprEtherServerIntFIoFsmStageRetry_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageRetry=_CfprEtherServerIntFIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,8),_CfprEtherServerIntFIoFsmStageRetry_Type())
cfprEtherServerIntFIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageRetry.setStatus(_A)
_CfprEtherServerIntFIoFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprEtherServerIntFIoFsmStageStageStatus_Object=MibTableColumn
cfprEtherServerIntFIoFsmStageStageStatus=_CfprEtherServerIntFIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,21,22,1,9),_CfprEtherServerIntFIoFsmStageStageStatus_Type())
cfprEtherServerIntFIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmStageStageStatus.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskTable_Object=MibTable
cfprEtherServerIntFIoFsmTaskTable=_CfprEtherServerIntFIoFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,21,23))
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskTable.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskEntry_Object=MibTableRow
cfprEtherServerIntFIoFsmTaskEntry=_CfprEtherServerIntFIoFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,21,23,1))
cfprEtherServerIntFIoFsmTaskEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskEntry.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprEtherServerIntFIoFsmTaskInstanceId_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskInstanceId=_CfprEtherServerIntFIoFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,1),_CfprEtherServerIntFIoFsmTaskInstanceId_Type())
cfprEtherServerIntFIoFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskInstanceId.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskDn_Type=CfprManagedObjectDn
_CfprEtherServerIntFIoFsmTaskDn_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskDn=_CfprEtherServerIntFIoFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,2),_CfprEtherServerIntFIoFsmTaskDn_Type())
cfprEtherServerIntFIoFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskDn.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskRn_Type=SnmpAdminString
_CfprEtherServerIntFIoFsmTaskRn_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskRn=_CfprEtherServerIntFIoFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,3),_CfprEtherServerIntFIoFsmTaskRn_Type())
cfprEtherServerIntFIoFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskRn.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskCompletion_Type=CfprFsmCompletion
_CfprEtherServerIntFIoFsmTaskCompletion_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskCompletion=_CfprEtherServerIntFIoFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,4),_CfprEtherServerIntFIoFsmTaskCompletion_Type())
cfprEtherServerIntFIoFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskCompletion.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskFlags_Type=CfprFsmFlags
_CfprEtherServerIntFIoFsmTaskFlags_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskFlags=_CfprEtherServerIntFIoFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,5),_CfprEtherServerIntFIoFsmTaskFlags_Type())
cfprEtherServerIntFIoFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskFlags.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskItem_Type=CfprEtherServerIntFIoFsmTaskItem
_CfprEtherServerIntFIoFsmTaskItem_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskItem=_CfprEtherServerIntFIoFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,6),_CfprEtherServerIntFIoFsmTaskItem_Type())
cfprEtherServerIntFIoFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskItem.setStatus(_A)
_CfprEtherServerIntFIoFsmTaskSeqId_Type=Gauge32
_CfprEtherServerIntFIoFsmTaskSeqId_Object=MibTableColumn
cfprEtherServerIntFIoFsmTaskSeqId=_CfprEtherServerIntFIoFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,21,23,1,7),_CfprEtherServerIntFIoFsmTaskSeqId_Type())
cfprEtherServerIntFIoFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoFsmTaskSeqId.setStatus(_A)
_CfprEtherServerIntFIoPcTable_Object=MibTable
cfprEtherServerIntFIoPcTable=_CfprEtherServerIntFIoPcTable_Object((1,3,6,1,4,1,9,9,826,1,21,24))
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcTable.setStatus(_A)
_CfprEtherServerIntFIoPcEntry_Object=MibTableRow
cfprEtherServerIntFIoPcEntry=_CfprEtherServerIntFIoPcEntry_Object((1,3,6,1,4,1,9,9,826,1,21,24,1))
cfprEtherServerIntFIoPcEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEntry.setStatus(_A)
_CfprEtherServerIntFIoPcInstanceId_Type=CfprManagedObjectId
_CfprEtherServerIntFIoPcInstanceId_Object=MibTableColumn
cfprEtherServerIntFIoPcInstanceId=_CfprEtherServerIntFIoPcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,1),_CfprEtherServerIntFIoPcInstanceId_Type())
cfprEtherServerIntFIoPcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcInstanceId.setStatus(_A)
_CfprEtherServerIntFIoPcDn_Type=CfprManagedObjectDn
_CfprEtherServerIntFIoPcDn_Object=MibTableColumn
cfprEtherServerIntFIoPcDn=_CfprEtherServerIntFIoPcDn_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,2),_CfprEtherServerIntFIoPcDn_Type())
cfprEtherServerIntFIoPcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcDn.setStatus(_A)
_CfprEtherServerIntFIoPcRn_Type=SnmpAdminString
_CfprEtherServerIntFIoPcRn_Object=MibTableColumn
cfprEtherServerIntFIoPcRn=_CfprEtherServerIntFIoPcRn_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,3),_CfprEtherServerIntFIoPcRn_Type())
cfprEtherServerIntFIoPcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcRn.setStatus(_A)
_CfprEtherServerIntFIoPcChassisId_Type=Gauge32
_CfprEtherServerIntFIoPcChassisId_Object=MibTableColumn
cfprEtherServerIntFIoPcChassisId=_CfprEtherServerIntFIoPcChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,4),_CfprEtherServerIntFIoPcChassisId_Type())
cfprEtherServerIntFIoPcChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcChassisId.setStatus(_A)
_CfprEtherServerIntFIoPcEpDn_Type=SnmpAdminString
_CfprEtherServerIntFIoPcEpDn_Object=MibTableColumn
cfprEtherServerIntFIoPcEpDn=_CfprEtherServerIntFIoPcEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,5),_CfprEtherServerIntFIoPcEpDn_Type())
cfprEtherServerIntFIoPcEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpDn.setStatus(_A)
_CfprEtherServerIntFIoPcFltAggr_Type=Unsigned64
_CfprEtherServerIntFIoPcFltAggr_Object=MibTableColumn
cfprEtherServerIntFIoPcFltAggr=_CfprEtherServerIntFIoPcFltAggr_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,6),_CfprEtherServerIntFIoPcFltAggr_Type())
cfprEtherServerIntFIoPcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcFltAggr.setStatus(_A)
_CfprEtherServerIntFIoPcIfRole_Type=CfprEtherServerIntFIoPcIfRole
_CfprEtherServerIntFIoPcIfRole_Object=MibTableColumn
cfprEtherServerIntFIoPcIfRole=_CfprEtherServerIntFIoPcIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,7),_CfprEtherServerIntFIoPcIfRole_Type())
cfprEtherServerIntFIoPcIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcIfRole.setStatus(_A)
_CfprEtherServerIntFIoPcIfType_Type=CfprEtherCIoEpIfType
_CfprEtherServerIntFIoPcIfType_Object=MibTableColumn
cfprEtherServerIntFIoPcIfType=_CfprEtherServerIntFIoPcIfType_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,8),_CfprEtherServerIntFIoPcIfType_Type())
cfprEtherServerIntFIoPcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcIfType.setStatus(_A)
_CfprEtherServerIntFIoPcLocale_Type=CfprEtherInternalPcLocale
_CfprEtherServerIntFIoPcLocale_Object=MibTableColumn
cfprEtherServerIntFIoPcLocale=_CfprEtherServerIntFIoPcLocale_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,9),_CfprEtherServerIntFIoPcLocale_Type())
cfprEtherServerIntFIoPcLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcLocale.setStatus(_A)
_CfprEtherServerIntFIoPcName_Type=SnmpAdminString
_CfprEtherServerIntFIoPcName_Object=MibTableColumn
cfprEtherServerIntFIoPcName=_CfprEtherServerIntFIoPcName_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,10),_CfprEtherServerIntFIoPcName_Type())
cfprEtherServerIntFIoPcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcName.setStatus(_A)
_CfprEtherServerIntFIoPcOperSpeed_Type=CfprPortEthSpeed
_CfprEtherServerIntFIoPcOperSpeed_Object=MibTableColumn
cfprEtherServerIntFIoPcOperSpeed=_CfprEtherServerIntFIoPcOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,11),_CfprEtherServerIntFIoPcOperSpeed_Type())
cfprEtherServerIntFIoPcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcOperSpeed.setStatus(_A)
_CfprEtherServerIntFIoPcOperState_Type=CfprNetworkPortOperState
_CfprEtherServerIntFIoPcOperState_Object=MibTableColumn
cfprEtherServerIntFIoPcOperState=_CfprEtherServerIntFIoPcOperState_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,12),_CfprEtherServerIntFIoPcOperState_Type())
cfprEtherServerIntFIoPcOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcOperState.setStatus(_A)
_CfprEtherServerIntFIoPcPeerDn_Type=SnmpAdminString
_CfprEtherServerIntFIoPcPeerDn_Object=MibTableColumn
cfprEtherServerIntFIoPcPeerDn=_CfprEtherServerIntFIoPcPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,13),_CfprEtherServerIntFIoPcPeerDn_Type())
cfprEtherServerIntFIoPcPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcPeerDn.setStatus(_A)
_CfprEtherServerIntFIoPcPortId_Type=CfprEtherServerIntFIoPcPortId
_CfprEtherServerIntFIoPcPortId_Object=MibTableColumn
cfprEtherServerIntFIoPcPortId=_CfprEtherServerIntFIoPcPortId_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,14),_CfprEtherServerIntFIoPcPortId_Type())
cfprEtherServerIntFIoPcPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcPortId.setStatus(_A)
_CfprEtherServerIntFIoPcStateQual_Type=SnmpAdminString
_CfprEtherServerIntFIoPcStateQual_Object=MibTableColumn
cfprEtherServerIntFIoPcStateQual=_CfprEtherServerIntFIoPcStateQual_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,15),_CfprEtherServerIntFIoPcStateQual_Type())
cfprEtherServerIntFIoPcStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcStateQual.setStatus(_A)
_CfprEtherServerIntFIoPcSwitchId_Type=CfprNetworkSwitchId
_CfprEtherServerIntFIoPcSwitchId_Object=MibTableColumn
cfprEtherServerIntFIoPcSwitchId=_CfprEtherServerIntFIoPcSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,16),_CfprEtherServerIntFIoPcSwitchId_Type())
cfprEtherServerIntFIoPcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcSwitchId.setStatus(_A)
_CfprEtherServerIntFIoPcTransport_Type=CfprEtherServerIntFIoPcTransport
_CfprEtherServerIntFIoPcTransport_Object=MibTableColumn
cfprEtherServerIntFIoPcTransport=_CfprEtherServerIntFIoPcTransport_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,17),_CfprEtherServerIntFIoPcTransport_Type())
cfprEtherServerIntFIoPcTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcTransport.setStatus(_A)
_CfprEtherServerIntFIoPcType_Type=CfprEtherServerIntFIoPcType
_CfprEtherServerIntFIoPcType_Object=MibTableColumn
cfprEtherServerIntFIoPcType=_CfprEtherServerIntFIoPcType_Object((1,3,6,1,4,1,9,9,826,1,21,24,1,18),_CfprEtherServerIntFIoPcType_Type())
cfprEtherServerIntFIoPcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcType.setStatus(_A)
_CfprEtherServerIntFIoPcEpTable_Object=MibTable
cfprEtherServerIntFIoPcEpTable=_CfprEtherServerIntFIoPcEpTable_Object((1,3,6,1,4,1,9,9,826,1,21,25))
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpTable.setStatus(_A)
_CfprEtherServerIntFIoPcEpEntry_Object=MibTableRow
cfprEtherServerIntFIoPcEpEntry=_CfprEtherServerIntFIoPcEpEntry_Object((1,3,6,1,4,1,9,9,826,1,21,25,1))
cfprEtherServerIntFIoPcEpEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpEntry.setStatus(_A)
_CfprEtherServerIntFIoPcEpInstanceId_Type=CfprManagedObjectId
_CfprEtherServerIntFIoPcEpInstanceId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpInstanceId=_CfprEtherServerIntFIoPcEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,1),_CfprEtherServerIntFIoPcEpInstanceId_Type())
cfprEtherServerIntFIoPcEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpInstanceId.setStatus(_A)
_CfprEtherServerIntFIoPcEpDnData_Type=CfprManagedObjectDn
_CfprEtherServerIntFIoPcEpDnData_Object=MibTableColumn
cfprEtherServerIntFIoPcEpDnData=_CfprEtherServerIntFIoPcEpDnData_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,2),_CfprEtherServerIntFIoPcEpDnData_Type())
cfprEtherServerIntFIoPcEpDnData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpDnData.setStatus(_A)
_CfprEtherServerIntFIoPcEpRn_Type=SnmpAdminString
_CfprEtherServerIntFIoPcEpRn_Object=MibTableColumn
cfprEtherServerIntFIoPcEpRn=_CfprEtherServerIntFIoPcEpRn_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,3),_CfprEtherServerIntFIoPcEpRn_Type())
cfprEtherServerIntFIoPcEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpRn.setStatus(_A)
_CfprEtherServerIntFIoPcEpAdminState_Type=CfprEtherExternalEpAdminState
_CfprEtherServerIntFIoPcEpAdminState_Object=MibTableColumn
cfprEtherServerIntFIoPcEpAdminState=_CfprEtherServerIntFIoPcEpAdminState_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,4),_CfprEtherServerIntFIoPcEpAdminState_Type())
cfprEtherServerIntFIoPcEpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpAdminState.setStatus(_A)
_CfprEtherServerIntFIoPcEpAggrPortId_Type=Gauge32
_CfprEtherServerIntFIoPcEpAggrPortId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpAggrPortId=_CfprEtherServerIntFIoPcEpAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,5),_CfprEtherServerIntFIoPcEpAggrPortId_Type())
cfprEtherServerIntFIoPcEpAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpAggrPortId.setStatus(_A)
_CfprEtherServerIntFIoPcEpChassisId_Type=Gauge32
_CfprEtherServerIntFIoPcEpChassisId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpChassisId=_CfprEtherServerIntFIoPcEpChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,6),_CfprEtherServerIntFIoPcEpChassisId_Type())
cfprEtherServerIntFIoPcEpChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpChassisId.setStatus(_A)
_CfprEtherServerIntFIoPcEpEpDn_Type=SnmpAdminString
_CfprEtherServerIntFIoPcEpEpDn_Object=MibTableColumn
cfprEtherServerIntFIoPcEpEpDn=_CfprEtherServerIntFIoPcEpEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,7),_CfprEtherServerIntFIoPcEpEpDn_Type())
cfprEtherServerIntFIoPcEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpEpDn.setStatus(_A)
_CfprEtherServerIntFIoPcEpIfRole_Type=CfprEtherServerIntFIoPcEpIfRole
_CfprEtherServerIntFIoPcEpIfRole_Object=MibTableColumn
cfprEtherServerIntFIoPcEpIfRole=_CfprEtherServerIntFIoPcEpIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,8),_CfprEtherServerIntFIoPcEpIfRole_Type())
cfprEtherServerIntFIoPcEpIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpIfRole.setStatus(_A)
_CfprEtherServerIntFIoPcEpIfType_Type=CfprEtherPIoEpIfType
_CfprEtherServerIntFIoPcEpIfType_Object=MibTableColumn
cfprEtherServerIntFIoPcEpIfType=_CfprEtherServerIntFIoPcEpIfType_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,9),_CfprEtherServerIntFIoPcEpIfType_Type())
cfprEtherServerIntFIoPcEpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpIfType.setStatus(_A)
_CfprEtherServerIntFIoPcEpLocale_Type=CfprEtherExternalEpLocale
_CfprEtherServerIntFIoPcEpLocale_Object=MibTableColumn
cfprEtherServerIntFIoPcEpLocale=_CfprEtherServerIntFIoPcEpLocale_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,10),_CfprEtherServerIntFIoPcEpLocale_Type())
cfprEtherServerIntFIoPcEpLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpLocale.setStatus(_A)
_CfprEtherServerIntFIoPcEpMembership_Type=CfprFabricMembershipStatus
_CfprEtherServerIntFIoPcEpMembership_Object=MibTableColumn
cfprEtherServerIntFIoPcEpMembership=_CfprEtherServerIntFIoPcEpMembership_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,11),_CfprEtherServerIntFIoPcEpMembership_Type())
cfprEtherServerIntFIoPcEpMembership.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpMembership.setStatus(_A)
_CfprEtherServerIntFIoPcEpName_Type=SnmpAdminString
_CfprEtherServerIntFIoPcEpName_Object=MibTableColumn
cfprEtherServerIntFIoPcEpName=_CfprEtherServerIntFIoPcEpName_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,12),_CfprEtherServerIntFIoPcEpName_Type())
cfprEtherServerIntFIoPcEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpName.setStatus(_A)
_CfprEtherServerIntFIoPcEpPeerAggrPortId_Type=Gauge32
_CfprEtherServerIntFIoPcEpPeerAggrPortId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpPeerAggrPortId=_CfprEtherServerIntFIoPcEpPeerAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,13),_CfprEtherServerIntFIoPcEpPeerAggrPortId_Type())
cfprEtherServerIntFIoPcEpPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpPeerAggrPortId.setStatus(_A)
_CfprEtherServerIntFIoPcEpPeerChassisId_Type=Gauge32
_CfprEtherServerIntFIoPcEpPeerChassisId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpPeerChassisId=_CfprEtherServerIntFIoPcEpPeerChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,14),_CfprEtherServerIntFIoPcEpPeerChassisId_Type())
cfprEtherServerIntFIoPcEpPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpPeerChassisId.setStatus(_A)
_CfprEtherServerIntFIoPcEpPeerDn_Type=SnmpAdminString
_CfprEtherServerIntFIoPcEpPeerDn_Object=MibTableColumn
cfprEtherServerIntFIoPcEpPeerDn=_CfprEtherServerIntFIoPcEpPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,15),_CfprEtherServerIntFIoPcEpPeerDn_Type())
cfprEtherServerIntFIoPcEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpPeerDn.setStatus(_A)
_CfprEtherServerIntFIoPcEpPeerPortId_Type=Gauge32
_CfprEtherServerIntFIoPcEpPeerPortId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpPeerPortId=_CfprEtherServerIntFIoPcEpPeerPortId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,16),_CfprEtherServerIntFIoPcEpPeerPortId_Type())
cfprEtherServerIntFIoPcEpPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpPeerPortId.setStatus(_A)
_CfprEtherServerIntFIoPcEpPeerSlotId_Type=Gauge32
_CfprEtherServerIntFIoPcEpPeerSlotId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpPeerSlotId=_CfprEtherServerIntFIoPcEpPeerSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,17),_CfprEtherServerIntFIoPcEpPeerSlotId_Type())
cfprEtherServerIntFIoPcEpPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpPeerSlotId.setStatus(_A)
_CfprEtherServerIntFIoPcEpPortId_Type=CfprEtherServerIntFIoPcEpPortId
_CfprEtherServerIntFIoPcEpPortId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpPortId=_CfprEtherServerIntFIoPcEpPortId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,18),_CfprEtherServerIntFIoPcEpPortId_Type())
cfprEtherServerIntFIoPcEpPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpPortId.setStatus(_A)
_CfprEtherServerIntFIoPcEpSlotId_Type=Gauge32
_CfprEtherServerIntFIoPcEpSlotId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpSlotId=_CfprEtherServerIntFIoPcEpSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,19),_CfprEtherServerIntFIoPcEpSlotId_Type())
cfprEtherServerIntFIoPcEpSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpSlotId.setStatus(_A)
_CfprEtherServerIntFIoPcEpSwitchId_Type=CfprNetworkSwitchId
_CfprEtherServerIntFIoPcEpSwitchId_Object=MibTableColumn
cfprEtherServerIntFIoPcEpSwitchId=_CfprEtherServerIntFIoPcEpSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,20),_CfprEtherServerIntFIoPcEpSwitchId_Type())
cfprEtherServerIntFIoPcEpSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpSwitchId.setStatus(_A)
_CfprEtherServerIntFIoPcEpTransport_Type=CfprNetworkTransport
_CfprEtherServerIntFIoPcEpTransport_Object=MibTableColumn
cfprEtherServerIntFIoPcEpTransport=_CfprEtherServerIntFIoPcEpTransport_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,21),_CfprEtherServerIntFIoPcEpTransport_Type())
cfprEtherServerIntFIoPcEpTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpTransport.setStatus(_A)
_CfprEtherServerIntFIoPcEpType_Type=CfprEtherIntFIoEpType
_CfprEtherServerIntFIoPcEpType_Object=MibTableColumn
cfprEtherServerIntFIoPcEpType=_CfprEtherServerIntFIoPcEpType_Object((1,3,6,1,4,1,9,9,826,1,21,25,1,22),_CfprEtherServerIntFIoPcEpType_Type())
cfprEtherServerIntFIoPcEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherServerIntFIoPcEpType.setStatus(_A)
_CfprEtherSwIfConfigTable_Object=MibTable
cfprEtherSwIfConfigTable=_CfprEtherSwIfConfigTable_Object((1,3,6,1,4,1,9,9,826,1,21,26))
if mibBuilder.loadTexts:cfprEtherSwIfConfigTable.setStatus(_A)
_CfprEtherSwIfConfigEntry_Object=MibTableRow
cfprEtherSwIfConfigEntry=_CfprEtherSwIfConfigEntry_Object((1,3,6,1,4,1,9,9,826,1,21,26,1))
cfprEtherSwIfConfigEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cfprEtherSwIfConfigEntry.setStatus(_A)
_CfprEtherSwIfConfigInstanceId_Type=CfprManagedObjectId
_CfprEtherSwIfConfigInstanceId_Object=MibTableColumn
cfprEtherSwIfConfigInstanceId=_CfprEtherSwIfConfigInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,26,1,1),_CfprEtherSwIfConfigInstanceId_Type())
cfprEtherSwIfConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherSwIfConfigInstanceId.setStatus(_A)
_CfprEtherSwIfConfigDn_Type=CfprManagedObjectDn
_CfprEtherSwIfConfigDn_Object=MibTableColumn
cfprEtherSwIfConfigDn=_CfprEtherSwIfConfigDn_Object((1,3,6,1,4,1,9,9,826,1,21,26,1,2),_CfprEtherSwIfConfigDn_Type())
cfprEtherSwIfConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwIfConfigDn.setStatus(_A)
_CfprEtherSwIfConfigRn_Type=SnmpAdminString
_CfprEtherSwIfConfigRn_Object=MibTableColumn
cfprEtherSwIfConfigRn=_CfprEtherSwIfConfigRn_Object((1,3,6,1,4,1,9,9,826,1,21,26,1,3),_CfprEtherSwIfConfigRn_Type())
cfprEtherSwIfConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwIfConfigRn.setStatus(_A)
_CfprEtherSwitchIntFIoTable_Object=MibTable
cfprEtherSwitchIntFIoTable=_CfprEtherSwitchIntFIoTable_Object((1,3,6,1,4,1,9,9,826,1,21,27))
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoTable.setStatus(_A)
_CfprEtherSwitchIntFIoEntry_Object=MibTableRow
cfprEtherSwitchIntFIoEntry=_CfprEtherSwitchIntFIoEntry_Object((1,3,6,1,4,1,9,9,826,1,21,27,1))
cfprEtherSwitchIntFIoEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoEntry.setStatus(_A)
_CfprEtherSwitchIntFIoInstanceId_Type=CfprManagedObjectId
_CfprEtherSwitchIntFIoInstanceId_Object=MibTableColumn
cfprEtherSwitchIntFIoInstanceId=_CfprEtherSwitchIntFIoInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,1),_CfprEtherSwitchIntFIoInstanceId_Type())
cfprEtherSwitchIntFIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoInstanceId.setStatus(_A)
_CfprEtherSwitchIntFIoDn_Type=CfprManagedObjectDn
_CfprEtherSwitchIntFIoDn_Object=MibTableColumn
cfprEtherSwitchIntFIoDn=_CfprEtherSwitchIntFIoDn_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,2),_CfprEtherSwitchIntFIoDn_Type())
cfprEtherSwitchIntFIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoDn.setStatus(_A)
_CfprEtherSwitchIntFIoRn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoRn_Object=MibTableColumn
cfprEtherSwitchIntFIoRn=_CfprEtherSwitchIntFIoRn_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,3),_CfprEtherSwitchIntFIoRn_Type())
cfprEtherSwitchIntFIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoRn.setStatus(_A)
_CfprEtherSwitchIntFIoAck_Type=CfprEtherSwitchIntFIoAck
_CfprEtherSwitchIntFIoAck_Object=MibTableColumn
cfprEtherSwitchIntFIoAck=_CfprEtherSwitchIntFIoAck_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,4),_CfprEtherSwitchIntFIoAck_Type())
cfprEtherSwitchIntFIoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoAck.setStatus(_A)
_CfprEtherSwitchIntFIoAdminState_Type=CfprFabricAdminState
_CfprEtherSwitchIntFIoAdminState_Object=MibTableColumn
cfprEtherSwitchIntFIoAdminState=_CfprEtherSwitchIntFIoAdminState_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,5),_CfprEtherSwitchIntFIoAdminState_Type())
cfprEtherSwitchIntFIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoAdminState.setStatus(_A)
_CfprEtherSwitchIntFIoAggrPortId_Type=Gauge32
_CfprEtherSwitchIntFIoAggrPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoAggrPortId=_CfprEtherSwitchIntFIoAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,6),_CfprEtherSwitchIntFIoAggrPortId_Type())
cfprEtherSwitchIntFIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoAggrPortId.setStatus(_A)
_CfprEtherSwitchIntFIoChassisId_Type=Gauge32
_CfprEtherSwitchIntFIoChassisId_Object=MibTableColumn
cfprEtherSwitchIntFIoChassisId=_CfprEtherSwitchIntFIoChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,7),_CfprEtherSwitchIntFIoChassisId_Type())
cfprEtherSwitchIntFIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoChassisId.setStatus(_A)
_CfprEtherSwitchIntFIoDelFeTs_Type=Unsigned64
_CfprEtherSwitchIntFIoDelFeTs_Object=MibTableColumn
cfprEtherSwitchIntFIoDelFeTs=_CfprEtherSwitchIntFIoDelFeTs_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,8),_CfprEtherSwitchIntFIoDelFeTs_Type())
cfprEtherSwitchIntFIoDelFeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoDelFeTs.setStatus(_A)
_CfprEtherSwitchIntFIoDiscovery_Type=CfprEtherSatelliteConnectionDisc
_CfprEtherSwitchIntFIoDiscovery_Object=MibTableColumn
cfprEtherSwitchIntFIoDiscovery=_CfprEtherSwitchIntFIoDiscovery_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,9),_CfprEtherSwitchIntFIoDiscovery_Type())
cfprEtherSwitchIntFIoDiscovery.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoDiscovery.setStatus(_A)
_CfprEtherSwitchIntFIoEncap_Type=CfprPortEncap
_CfprEtherSwitchIntFIoEncap_Object=MibTableColumn
cfprEtherSwitchIntFIoEncap=_CfprEtherSwitchIntFIoEncap_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,10),_CfprEtherSwitchIntFIoEncap_Type())
cfprEtherSwitchIntFIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoEncap.setStatus(_A)
_CfprEtherSwitchIntFIoEpDn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoEpDn_Object=MibTableColumn
cfprEtherSwitchIntFIoEpDn=_CfprEtherSwitchIntFIoEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,11),_CfprEtherSwitchIntFIoEpDn_Type())
cfprEtherSwitchIntFIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoEpDn.setStatus(_A)
_CfprEtherSwitchIntFIoFltAggr_Type=Unsigned64
_CfprEtherSwitchIntFIoFltAggr_Object=MibTableColumn
cfprEtherSwitchIntFIoFltAggr=_CfprEtherSwitchIntFIoFltAggr_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,12),_CfprEtherSwitchIntFIoFltAggr_Type())
cfprEtherSwitchIntFIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoFltAggr.setStatus(_A)
_CfprEtherSwitchIntFIoIfRole_Type=CfprEtherSwitchIntFIoIfRole
_CfprEtherSwitchIntFIoIfRole_Object=MibTableColumn
cfprEtherSwitchIntFIoIfRole=_CfprEtherSwitchIntFIoIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,13),_CfprEtherSwitchIntFIoIfRole_Type())
cfprEtherSwitchIntFIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoIfRole.setStatus(_A)
_CfprEtherSwitchIntFIoIfType_Type=CfprNetworkPhysEpIfType
_CfprEtherSwitchIntFIoIfType_Object=MibTableColumn
cfprEtherSwitchIntFIoIfType=_CfprEtherSwitchIntFIoIfType_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,14),_CfprEtherSwitchIntFIoIfType_Type())
cfprEtherSwitchIntFIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoIfType.setStatus(_A)
_CfprEtherSwitchIntFIoLocale_Type=CfprEtherSwitchIntFIoLocale
_CfprEtherSwitchIntFIoLocale_Object=MibTableColumn
cfprEtherSwitchIntFIoLocale=_CfprEtherSwitchIntFIoLocale_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,15),_CfprEtherSwitchIntFIoLocale_Type())
cfprEtherSwitchIntFIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoLocale.setStatus(_A)
_CfprEtherSwitchIntFIoMode_Type=CfprPortMode
_CfprEtherSwitchIntFIoMode_Object=MibTableColumn
cfprEtherSwitchIntFIoMode=_CfprEtherSwitchIntFIoMode_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,16),_CfprEtherSwitchIntFIoMode_Type())
cfprEtherSwitchIntFIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoMode.setStatus(_A)
_CfprEtherSwitchIntFIoModel_Type=SnmpAdminString
_CfprEtherSwitchIntFIoModel_Object=MibTableColumn
cfprEtherSwitchIntFIoModel=_CfprEtherSwitchIntFIoModel_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,17),_CfprEtherSwitchIntFIoModel_Type())
cfprEtherSwitchIntFIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoModel.setStatus(_A)
_CfprEtherSwitchIntFIoName_Type=SnmpAdminString
_CfprEtherSwitchIntFIoName_Object=MibTableColumn
cfprEtherSwitchIntFIoName=_CfprEtherSwitchIntFIoName_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,18),_CfprEtherSwitchIntFIoName_Type())
cfprEtherSwitchIntFIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoName.setStatus(_A)
_CfprEtherSwitchIntFIoNewFeTs_Type=Unsigned64
_CfprEtherSwitchIntFIoNewFeTs_Object=MibTableColumn
cfprEtherSwitchIntFIoNewFeTs=_CfprEtherSwitchIntFIoNewFeTs_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,19),_CfprEtherSwitchIntFIoNewFeTs_Type())
cfprEtherSwitchIntFIoNewFeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoNewFeTs.setStatus(_A)
_CfprEtherSwitchIntFIoOperState_Type=CfprNetworkPortOperState
_CfprEtherSwitchIntFIoOperState_Object=MibTableColumn
cfprEtherSwitchIntFIoOperState=_CfprEtherSwitchIntFIoOperState_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,20),_CfprEtherSwitchIntFIoOperState_Type())
cfprEtherSwitchIntFIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoOperState.setStatus(_A)
_CfprEtherSwitchIntFIoPeerAggrPortId_Type=Gauge32
_CfprEtherSwitchIntFIoPeerAggrPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPeerAggrPortId=_CfprEtherSwitchIntFIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,21),_CfprEtherSwitchIntFIoPeerAggrPortId_Type())
cfprEtherSwitchIntFIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPeerAggrPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPeerChassisId_Type=Gauge32
_CfprEtherSwitchIntFIoPeerChassisId_Object=MibTableColumn
cfprEtherSwitchIntFIoPeerChassisId=_CfprEtherSwitchIntFIoPeerChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,22),_CfprEtherSwitchIntFIoPeerChassisId_Type())
cfprEtherSwitchIntFIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPeerChassisId.setStatus(_A)
_CfprEtherSwitchIntFIoPeerDn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPeerDn_Object=MibTableColumn
cfprEtherSwitchIntFIoPeerDn=_CfprEtherSwitchIntFIoPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,23),_CfprEtherSwitchIntFIoPeerDn_Type())
cfprEtherSwitchIntFIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPeerDn.setStatus(_A)
_CfprEtherSwitchIntFIoPeerPortId_Type=Gauge32
_CfprEtherSwitchIntFIoPeerPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPeerPortId=_CfprEtherSwitchIntFIoPeerPortId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,24),_CfprEtherSwitchIntFIoPeerPortId_Type())
cfprEtherSwitchIntFIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPeerPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPeerSlotId_Type=Gauge32
_CfprEtherSwitchIntFIoPeerSlotId_Object=MibTableColumn
cfprEtherSwitchIntFIoPeerSlotId=_CfprEtherSwitchIntFIoPeerSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,25),_CfprEtherSwitchIntFIoPeerSlotId_Type())
cfprEtherSwitchIntFIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPeerSlotId.setStatus(_A)
_CfprEtherSwitchIntFIoPortId_Type=Gauge32
_CfprEtherSwitchIntFIoPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPortId=_CfprEtherSwitchIntFIoPortId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,26),_CfprEtherSwitchIntFIoPortId_Type())
cfprEtherSwitchIntFIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPortId.setStatus(_A)
_CfprEtherSwitchIntFIoRevision_Type=SnmpAdminString
_CfprEtherSwitchIntFIoRevision_Object=MibTableColumn
cfprEtherSwitchIntFIoRevision=_CfprEtherSwitchIntFIoRevision_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,27),_CfprEtherSwitchIntFIoRevision_Type())
cfprEtherSwitchIntFIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoRevision.setStatus(_A)
_CfprEtherSwitchIntFIoSerial_Type=SnmpAdminString
_CfprEtherSwitchIntFIoSerial_Object=MibTableColumn
cfprEtherSwitchIntFIoSerial=_CfprEtherSwitchIntFIoSerial_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,28),_CfprEtherSwitchIntFIoSerial_Type())
cfprEtherSwitchIntFIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoSerial.setStatus(_A)
_CfprEtherSwitchIntFIoSlotId_Type=Gauge32
_CfprEtherSwitchIntFIoSlotId_Object=MibTableColumn
cfprEtherSwitchIntFIoSlotId=_CfprEtherSwitchIntFIoSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,29),_CfprEtherSwitchIntFIoSlotId_Type())
cfprEtherSwitchIntFIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoSlotId.setStatus(_A)
_CfprEtherSwitchIntFIoStateQual_Type=SnmpAdminString
_CfprEtherSwitchIntFIoStateQual_Object=MibTableColumn
cfprEtherSwitchIntFIoStateQual=_CfprEtherSwitchIntFIoStateQual_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,30),_CfprEtherSwitchIntFIoStateQual_Type())
cfprEtherSwitchIntFIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoStateQual.setStatus(_A)
_CfprEtherSwitchIntFIoSwitchId_Type=CfprNetworkSwitchId
_CfprEtherSwitchIntFIoSwitchId_Object=MibTableColumn
cfprEtherSwitchIntFIoSwitchId=_CfprEtherSwitchIntFIoSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,31),_CfprEtherSwitchIntFIoSwitchId_Type())
cfprEtherSwitchIntFIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoSwitchId.setStatus(_A)
_CfprEtherSwitchIntFIoTransport_Type=CfprEtherSwitchIntFIoTransport
_CfprEtherSwitchIntFIoTransport_Object=MibTableColumn
cfprEtherSwitchIntFIoTransport=_CfprEtherSwitchIntFIoTransport_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,32),_CfprEtherSwitchIntFIoTransport_Type())
cfprEtherSwitchIntFIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoTransport.setStatus(_A)
_CfprEtherSwitchIntFIoTs_Type=DateAndTime
_CfprEtherSwitchIntFIoTs_Object=MibTableColumn
cfprEtherSwitchIntFIoTs=_CfprEtherSwitchIntFIoTs_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,33),_CfprEtherSwitchIntFIoTs_Type())
cfprEtherSwitchIntFIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoTs.setStatus(_A)
_CfprEtherSwitchIntFIoType_Type=CfprEtherSwitchIntFIoType
_CfprEtherSwitchIntFIoType_Object=MibTableColumn
cfprEtherSwitchIntFIoType=_CfprEtherSwitchIntFIoType_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,34),_CfprEtherSwitchIntFIoType_Type())
cfprEtherSwitchIntFIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoType.setStatus(_A)
_CfprEtherSwitchIntFIoVendor_Type=SnmpAdminString
_CfprEtherSwitchIntFIoVendor_Object=MibTableColumn
cfprEtherSwitchIntFIoVendor=_CfprEtherSwitchIntFIoVendor_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,35),_CfprEtherSwitchIntFIoVendor_Type())
cfprEtherSwitchIntFIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoVendor.setStatus(_A)
_CfprEtherSwitchIntFIoXcvrType_Type=CfprEquipmentXcvrType
_CfprEtherSwitchIntFIoXcvrType_Object=MibTableColumn
cfprEtherSwitchIntFIoXcvrType=_CfprEtherSwitchIntFIoXcvrType_Object((1,3,6,1,4,1,9,9,826,1,21,27,1,36),_CfprEtherSwitchIntFIoXcvrType_Type())
cfprEtherSwitchIntFIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoXcvrType.setStatus(_A)
_CfprEtherSwitchIntFIoPcTable_Object=MibTable
cfprEtherSwitchIntFIoPcTable=_CfprEtherSwitchIntFIoPcTable_Object((1,3,6,1,4,1,9,9,826,1,21,28))
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcTable.setStatus(_A)
_CfprEtherSwitchIntFIoPcEntry_Object=MibTableRow
cfprEtherSwitchIntFIoPcEntry=_CfprEtherSwitchIntFIoPcEntry_Object((1,3,6,1,4,1,9,9,826,1,21,28,1))
cfprEtherSwitchIntFIoPcEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEntry.setStatus(_A)
_CfprEtherSwitchIntFIoPcInstanceId_Type=CfprManagedObjectId
_CfprEtherSwitchIntFIoPcInstanceId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcInstanceId=_CfprEtherSwitchIntFIoPcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,1),_CfprEtherSwitchIntFIoPcInstanceId_Type())
cfprEtherSwitchIntFIoPcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcInstanceId.setStatus(_A)
_CfprEtherSwitchIntFIoPcDn_Type=CfprManagedObjectDn
_CfprEtherSwitchIntFIoPcDn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcDn=_CfprEtherSwitchIntFIoPcDn_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,2),_CfprEtherSwitchIntFIoPcDn_Type())
cfprEtherSwitchIntFIoPcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcDn.setStatus(_A)
_CfprEtherSwitchIntFIoPcRn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcRn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcRn=_CfprEtherSwitchIntFIoPcRn_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,3),_CfprEtherSwitchIntFIoPcRn_Type())
cfprEtherSwitchIntFIoPcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcRn.setStatus(_A)
_CfprEtherSwitchIntFIoPcAdminState_Type=CfprEtherExternalPcAdminState
_CfprEtherSwitchIntFIoPcAdminState_Object=MibTableColumn
cfprEtherSwitchIntFIoPcAdminState=_CfprEtherSwitchIntFIoPcAdminState_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,4),_CfprEtherSwitchIntFIoPcAdminState_Type())
cfprEtherSwitchIntFIoPcAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcAdminState.setStatus(_A)
_CfprEtherSwitchIntFIoPcChassisId_Type=Gauge32
_CfprEtherSwitchIntFIoPcChassisId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcChassisId=_CfprEtherSwitchIntFIoPcChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,5),_CfprEtherSwitchIntFIoPcChassisId_Type())
cfprEtherSwitchIntFIoPcChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcChassisId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpDn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcEpDn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpDn=_CfprEtherSwitchIntFIoPcEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,6),_CfprEtherSwitchIntFIoPcEpDn_Type())
cfprEtherSwitchIntFIoPcEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpDn.setStatus(_A)
_CfprEtherSwitchIntFIoPcFltAggr_Type=Unsigned64
_CfprEtherSwitchIntFIoPcFltAggr_Object=MibTableColumn
cfprEtherSwitchIntFIoPcFltAggr=_CfprEtherSwitchIntFIoPcFltAggr_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,7),_CfprEtherSwitchIntFIoPcFltAggr_Type())
cfprEtherSwitchIntFIoPcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcFltAggr.setStatus(_A)
_CfprEtherSwitchIntFIoPcIfRole_Type=CfprEtherSwitchIntFIoPcIfRole
_CfprEtherSwitchIntFIoPcIfRole_Object=MibTableColumn
cfprEtherSwitchIntFIoPcIfRole=_CfprEtherSwitchIntFIoPcIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,8),_CfprEtherSwitchIntFIoPcIfRole_Type())
cfprEtherSwitchIntFIoPcIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcIfRole.setStatus(_A)
_CfprEtherSwitchIntFIoPcIfType_Type=CfprEtherCIoEpIfType
_CfprEtherSwitchIntFIoPcIfType_Object=MibTableColumn
cfprEtherSwitchIntFIoPcIfType=_CfprEtherSwitchIntFIoPcIfType_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,9),_CfprEtherSwitchIntFIoPcIfType_Type())
cfprEtherSwitchIntFIoPcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcIfType.setStatus(_A)
_CfprEtherSwitchIntFIoPcLocale_Type=CfprEtherExternalPcLocale
_CfprEtherSwitchIntFIoPcLocale_Object=MibTableColumn
cfprEtherSwitchIntFIoPcLocale=_CfprEtherSwitchIntFIoPcLocale_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,10),_CfprEtherSwitchIntFIoPcLocale_Type())
cfprEtherSwitchIntFIoPcLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcLocale.setStatus(_A)
_CfprEtherSwitchIntFIoPcName_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcName_Object=MibTableColumn
cfprEtherSwitchIntFIoPcName=_CfprEtherSwitchIntFIoPcName_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,11),_CfprEtherSwitchIntFIoPcName_Type())
cfprEtherSwitchIntFIoPcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcName.setStatus(_A)
_CfprEtherSwitchIntFIoPcOperSpeed_Type=CfprPortEthSpeed
_CfprEtherSwitchIntFIoPcOperSpeed_Object=MibTableColumn
cfprEtherSwitchIntFIoPcOperSpeed=_CfprEtherSwitchIntFIoPcOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,12),_CfprEtherSwitchIntFIoPcOperSpeed_Type())
cfprEtherSwitchIntFIoPcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcOperSpeed.setStatus(_A)
_CfprEtherSwitchIntFIoPcOperState_Type=CfprNetworkPortOperState
_CfprEtherSwitchIntFIoPcOperState_Object=MibTableColumn
cfprEtherSwitchIntFIoPcOperState=_CfprEtherSwitchIntFIoPcOperState_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,13),_CfprEtherSwitchIntFIoPcOperState_Type())
cfprEtherSwitchIntFIoPcOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcOperState.setStatus(_A)
_CfprEtherSwitchIntFIoPcPeerDn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcPeerDn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcPeerDn=_CfprEtherSwitchIntFIoPcPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,14),_CfprEtherSwitchIntFIoPcPeerDn_Type())
cfprEtherSwitchIntFIoPcPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcPeerDn.setStatus(_A)
_CfprEtherSwitchIntFIoPcPortId_Type=CfprEtherSwitchIntFIoPcPortId
_CfprEtherSwitchIntFIoPcPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcPortId=_CfprEtherSwitchIntFIoPcPortId_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,15),_CfprEtherSwitchIntFIoPcPortId_Type())
cfprEtherSwitchIntFIoPcPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPcStateQual_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcStateQual_Object=MibTableColumn
cfprEtherSwitchIntFIoPcStateQual=_CfprEtherSwitchIntFIoPcStateQual_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,16),_CfprEtherSwitchIntFIoPcStateQual_Type())
cfprEtherSwitchIntFIoPcStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcStateQual.setStatus(_A)
_CfprEtherSwitchIntFIoPcSwitchId_Type=CfprNetworkSwitchId
_CfprEtherSwitchIntFIoPcSwitchId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcSwitchId=_CfprEtherSwitchIntFIoPcSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,17),_CfprEtherSwitchIntFIoPcSwitchId_Type())
cfprEtherSwitchIntFIoPcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcSwitchId.setStatus(_A)
_CfprEtherSwitchIntFIoPcTransport_Type=CfprEtherSwitchIntFIoPcTransport
_CfprEtherSwitchIntFIoPcTransport_Object=MibTableColumn
cfprEtherSwitchIntFIoPcTransport=_CfprEtherSwitchIntFIoPcTransport_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,18),_CfprEtherSwitchIntFIoPcTransport_Type())
cfprEtherSwitchIntFIoPcTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcTransport.setStatus(_A)
_CfprEtherSwitchIntFIoPcType_Type=CfprEtherSwitchIntFIoPcType
_CfprEtherSwitchIntFIoPcType_Object=MibTableColumn
cfprEtherSwitchIntFIoPcType=_CfprEtherSwitchIntFIoPcType_Object((1,3,6,1,4,1,9,9,826,1,21,28,1,19),_CfprEtherSwitchIntFIoPcType_Type())
cfprEtherSwitchIntFIoPcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcType.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpTable_Object=MibTable
cfprEtherSwitchIntFIoPcEpTable=_CfprEtherSwitchIntFIoPcEpTable_Object((1,3,6,1,4,1,9,9,826,1,21,29))
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpTable.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpEntry_Object=MibTableRow
cfprEtherSwitchIntFIoPcEpEntry=_CfprEtherSwitchIntFIoPcEpEntry_Object((1,3,6,1,4,1,9,9,826,1,21,29,1))
cfprEtherSwitchIntFIoPcEpEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpEntry.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpInstanceId_Type=CfprManagedObjectId
_CfprEtherSwitchIntFIoPcEpInstanceId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpInstanceId=_CfprEtherSwitchIntFIoPcEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,1),_CfprEtherSwitchIntFIoPcEpInstanceId_Type())
cfprEtherSwitchIntFIoPcEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpInstanceId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpDnData_Type=CfprManagedObjectDn
_CfprEtherSwitchIntFIoPcEpDnData_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpDnData=_CfprEtherSwitchIntFIoPcEpDnData_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,2),_CfprEtherSwitchIntFIoPcEpDnData_Type())
cfprEtherSwitchIntFIoPcEpDnData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpDnData.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpRn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcEpRn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpRn=_CfprEtherSwitchIntFIoPcEpRn_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,3),_CfprEtherSwitchIntFIoPcEpRn_Type())
cfprEtherSwitchIntFIoPcEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpRn.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpAckState_Type=CfprEquipmentChassisConfigState
_CfprEtherSwitchIntFIoPcEpAckState_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpAckState=_CfprEtherSwitchIntFIoPcEpAckState_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,4),_CfprEtherSwitchIntFIoPcEpAckState_Type())
cfprEtherSwitchIntFIoPcEpAckState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpAckState.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpAdminState_Type=CfprEtherExternalEpAdminState
_CfprEtherSwitchIntFIoPcEpAdminState_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpAdminState=_CfprEtherSwitchIntFIoPcEpAdminState_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,5),_CfprEtherSwitchIntFIoPcEpAdminState_Type())
cfprEtherSwitchIntFIoPcEpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpAdminState.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpAggrPortId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpAggrPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpAggrPortId=_CfprEtherSwitchIntFIoPcEpAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,6),_CfprEtherSwitchIntFIoPcEpAggrPortId_Type())
cfprEtherSwitchIntFIoPcEpAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpAggrPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpChassisId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpChassisId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpChassisId=_CfprEtherSwitchIntFIoPcEpChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,7),_CfprEtherSwitchIntFIoPcEpChassisId_Type())
cfprEtherSwitchIntFIoPcEpChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpChassisId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpEpDn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcEpEpDn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpEpDn=_CfprEtherSwitchIntFIoPcEpEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,8),_CfprEtherSwitchIntFIoPcEpEpDn_Type())
cfprEtherSwitchIntFIoPcEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpEpDn.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpIfRole_Type=CfprEtherSwitchIntFIoPcEpIfRole
_CfprEtherSwitchIntFIoPcEpIfRole_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpIfRole=_CfprEtherSwitchIntFIoPcEpIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,9),_CfprEtherSwitchIntFIoPcEpIfRole_Type())
cfprEtherSwitchIntFIoPcEpIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpIfRole.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpIfType_Type=CfprEtherPIoEpIfType
_CfprEtherSwitchIntFIoPcEpIfType_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpIfType=_CfprEtherSwitchIntFIoPcEpIfType_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,10),_CfprEtherSwitchIntFIoPcEpIfType_Type())
cfprEtherSwitchIntFIoPcEpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpIfType.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpLocale_Type=CfprEtherExternalEpLocale
_CfprEtherSwitchIntFIoPcEpLocale_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpLocale=_CfprEtherSwitchIntFIoPcEpLocale_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,11),_CfprEtherSwitchIntFIoPcEpLocale_Type())
cfprEtherSwitchIntFIoPcEpLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpLocale.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpMembership_Type=CfprFabricMembershipStatus
_CfprEtherSwitchIntFIoPcEpMembership_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpMembership=_CfprEtherSwitchIntFIoPcEpMembership_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,12),_CfprEtherSwitchIntFIoPcEpMembership_Type())
cfprEtherSwitchIntFIoPcEpMembership.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpMembership.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpName_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcEpName_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpName=_CfprEtherSwitchIntFIoPcEpName_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,13),_CfprEtherSwitchIntFIoPcEpName_Type())
cfprEtherSwitchIntFIoPcEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpName.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerAggrPortId=_CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,14),_CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Type())
cfprEtherSwitchIntFIoPcEpPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpPeerAggrPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpPeerChassisId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpPeerChassisId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerChassisId=_CfprEtherSwitchIntFIoPcEpPeerChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,15),_CfprEtherSwitchIntFIoPcEpPeerChassisId_Type())
cfprEtherSwitchIntFIoPcEpPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpPeerChassisId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpPeerDn_Type=SnmpAdminString
_CfprEtherSwitchIntFIoPcEpPeerDn_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerDn=_CfprEtherSwitchIntFIoPcEpPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,16),_CfprEtherSwitchIntFIoPcEpPeerDn_Type())
cfprEtherSwitchIntFIoPcEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpPeerDn.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpPeerPortId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpPeerPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerPortId=_CfprEtherSwitchIntFIoPcEpPeerPortId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,17),_CfprEtherSwitchIntFIoPcEpPeerPortId_Type())
cfprEtherSwitchIntFIoPcEpPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpPeerPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpPeerSlotId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpPeerSlotId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerSlotId=_CfprEtherSwitchIntFIoPcEpPeerSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,18),_CfprEtherSwitchIntFIoPcEpPeerSlotId_Type())
cfprEtherSwitchIntFIoPcEpPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpPeerSlotId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpPortId_Type=CfprEtherSwitchIntFIoPcEpPortId
_CfprEtherSwitchIntFIoPcEpPortId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpPortId=_CfprEtherSwitchIntFIoPcEpPortId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,19),_CfprEtherSwitchIntFIoPcEpPortId_Type())
cfprEtherSwitchIntFIoPcEpPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpPortId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpSlotId_Type=Gauge32
_CfprEtherSwitchIntFIoPcEpSlotId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpSlotId=_CfprEtherSwitchIntFIoPcEpSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,20),_CfprEtherSwitchIntFIoPcEpSlotId_Type())
cfprEtherSwitchIntFIoPcEpSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpSlotId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpStatusChangeTs_Type=DateAndTime
_CfprEtherSwitchIntFIoPcEpStatusChangeTs_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpStatusChangeTs=_CfprEtherSwitchIntFIoPcEpStatusChangeTs_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,21),_CfprEtherSwitchIntFIoPcEpStatusChangeTs_Type())
cfprEtherSwitchIntFIoPcEpStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpStatusChangeTs.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpSwitchId_Type=CfprNetworkSwitchId
_CfprEtherSwitchIntFIoPcEpSwitchId_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpSwitchId=_CfprEtherSwitchIntFIoPcEpSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,22),_CfprEtherSwitchIntFIoPcEpSwitchId_Type())
cfprEtherSwitchIntFIoPcEpSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpSwitchId.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpTransport_Type=CfprNetworkTransport
_CfprEtherSwitchIntFIoPcEpTransport_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpTransport=_CfprEtherSwitchIntFIoPcEpTransport_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,23),_CfprEtherSwitchIntFIoPcEpTransport_Type())
cfprEtherSwitchIntFIoPcEpTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpTransport.setStatus(_A)
_CfprEtherSwitchIntFIoPcEpType_Type=CfprEtherIntFIoEpType
_CfprEtherSwitchIntFIoPcEpType_Object=MibTableColumn
cfprEtherSwitchIntFIoPcEpType=_CfprEtherSwitchIntFIoPcEpType_Object((1,3,6,1,4,1,9,9,826,1,21,29,1,24),_CfprEtherSwitchIntFIoPcEpType_Type())
cfprEtherSwitchIntFIoPcEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherSwitchIntFIoPcEpType.setStatus(_A)
_CfprEtherTxStatsTable_Object=MibTable
cfprEtherTxStatsTable=_CfprEtherTxStatsTable_Object((1,3,6,1,4,1,9,9,826,1,21,30))
if mibBuilder.loadTexts:cfprEtherTxStatsTable.setStatus(_A)
_CfprEtherTxStatsEntry_Object=MibTableRow
cfprEtherTxStatsEntry=_CfprEtherTxStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,21,30,1))
cfprEtherTxStatsEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cfprEtherTxStatsEntry.setStatus(_A)
_CfprEtherTxStatsInstanceId_Type=CfprManagedObjectId
_CfprEtherTxStatsInstanceId_Object=MibTableColumn
cfprEtherTxStatsInstanceId=_CfprEtherTxStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,1),_CfprEtherTxStatsInstanceId_Type())
cfprEtherTxStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherTxStatsInstanceId.setStatus(_A)
_CfprEtherTxStatsDn_Type=CfprManagedObjectDn
_CfprEtherTxStatsDn_Object=MibTableColumn
cfprEtherTxStatsDn=_CfprEtherTxStatsDn_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,2),_CfprEtherTxStatsDn_Type())
cfprEtherTxStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsDn.setStatus(_A)
_CfprEtherTxStatsRn_Type=SnmpAdminString
_CfprEtherTxStatsRn_Object=MibTableColumn
cfprEtherTxStatsRn=_CfprEtherTxStatsRn_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,3),_CfprEtherTxStatsRn_Type())
cfprEtherTxStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsRn.setStatus(_A)
_CfprEtherTxStatsBroadcastPackets_Type=Unsigned64
_CfprEtherTxStatsBroadcastPackets_Object=MibTableColumn
cfprEtherTxStatsBroadcastPackets=_CfprEtherTxStatsBroadcastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,4),_CfprEtherTxStatsBroadcastPackets_Type())
cfprEtherTxStatsBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsBroadcastPackets.setStatus(_A)
_CfprEtherTxStatsBroadcastPacketsDelta_Type=Counter64
_CfprEtherTxStatsBroadcastPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsBroadcastPacketsDelta=_CfprEtherTxStatsBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,5),_CfprEtherTxStatsBroadcastPacketsDelta_Type())
cfprEtherTxStatsBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsBroadcastPacketsDelta.setStatus(_A)
_CfprEtherTxStatsBroadcastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsBroadcastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsBroadcastPacketsDeltaAvg=_CfprEtherTxStatsBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,6),_CfprEtherTxStatsBroadcastPacketsDeltaAvg_Type())
cfprEtherTxStatsBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsBroadcastPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsBroadcastPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsBroadcastPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsBroadcastPacketsDeltaMax=_CfprEtherTxStatsBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,7),_CfprEtherTxStatsBroadcastPacketsDeltaMax_Type())
cfprEtherTxStatsBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsBroadcastPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsBroadcastPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsBroadcastPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsBroadcastPacketsDeltaMin=_CfprEtherTxStatsBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,8),_CfprEtherTxStatsBroadcastPacketsDeltaMin_Type())
cfprEtherTxStatsBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsBroadcastPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsIntervals_Type=Gauge32
_CfprEtherTxStatsIntervals_Object=MibTableColumn
cfprEtherTxStatsIntervals=_CfprEtherTxStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,9),_CfprEtherTxStatsIntervals_Type())
cfprEtherTxStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsIntervals.setStatus(_A)
_CfprEtherTxStatsJumboPackets_Type=Unsigned64
_CfprEtherTxStatsJumboPackets_Object=MibTableColumn
cfprEtherTxStatsJumboPackets=_CfprEtherTxStatsJumboPackets_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,10),_CfprEtherTxStatsJumboPackets_Type())
cfprEtherTxStatsJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsJumboPackets.setStatus(_A)
_CfprEtherTxStatsJumboPacketsDelta_Type=Counter64
_CfprEtherTxStatsJumboPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsJumboPacketsDelta=_CfprEtherTxStatsJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,11),_CfprEtherTxStatsJumboPacketsDelta_Type())
cfprEtherTxStatsJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsJumboPacketsDelta.setStatus(_A)
_CfprEtherTxStatsJumboPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsJumboPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsJumboPacketsDeltaAvg=_CfprEtherTxStatsJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,12),_CfprEtherTxStatsJumboPacketsDeltaAvg_Type())
cfprEtherTxStatsJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsJumboPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsJumboPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsJumboPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsJumboPacketsDeltaMax=_CfprEtherTxStatsJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,13),_CfprEtherTxStatsJumboPacketsDeltaMax_Type())
cfprEtherTxStatsJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsJumboPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsJumboPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsJumboPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsJumboPacketsDeltaMin=_CfprEtherTxStatsJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,14),_CfprEtherTxStatsJumboPacketsDeltaMin_Type())
cfprEtherTxStatsJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsJumboPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsMulticastPackets_Type=Unsigned64
_CfprEtherTxStatsMulticastPackets_Object=MibTableColumn
cfprEtherTxStatsMulticastPackets=_CfprEtherTxStatsMulticastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,15),_CfprEtherTxStatsMulticastPackets_Type())
cfprEtherTxStatsMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsMulticastPackets.setStatus(_A)
_CfprEtherTxStatsMulticastPacketsDelta_Type=Counter64
_CfprEtherTxStatsMulticastPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsMulticastPacketsDelta=_CfprEtherTxStatsMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,16),_CfprEtherTxStatsMulticastPacketsDelta_Type())
cfprEtherTxStatsMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsMulticastPacketsDelta.setStatus(_A)
_CfprEtherTxStatsMulticastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsMulticastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsMulticastPacketsDeltaAvg=_CfprEtherTxStatsMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,17),_CfprEtherTxStatsMulticastPacketsDeltaAvg_Type())
cfprEtherTxStatsMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsMulticastPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsMulticastPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsMulticastPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsMulticastPacketsDeltaMax=_CfprEtherTxStatsMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,18),_CfprEtherTxStatsMulticastPacketsDeltaMax_Type())
cfprEtherTxStatsMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsMulticastPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsMulticastPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsMulticastPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsMulticastPacketsDeltaMin=_CfprEtherTxStatsMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,19),_CfprEtherTxStatsMulticastPacketsDeltaMin_Type())
cfprEtherTxStatsMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsMulticastPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsSuspect_Type=TruthValue
_CfprEtherTxStatsSuspect_Object=MibTableColumn
cfprEtherTxStatsSuspect=_CfprEtherTxStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,20),_CfprEtherTxStatsSuspect_Type())
cfprEtherTxStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsSuspect.setStatus(_A)
_CfprEtherTxStatsThresholded_Type=CfprEtherTxStatsThresholded
_CfprEtherTxStatsThresholded_Object=MibTableColumn
cfprEtherTxStatsThresholded=_CfprEtherTxStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,21),_CfprEtherTxStatsThresholded_Type())
cfprEtherTxStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsThresholded.setStatus(_A)
_CfprEtherTxStatsTimeCollected_Type=DateAndTime
_CfprEtherTxStatsTimeCollected_Object=MibTableColumn
cfprEtherTxStatsTimeCollected=_CfprEtherTxStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,22),_CfprEtherTxStatsTimeCollected_Type())
cfprEtherTxStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTimeCollected.setStatus(_A)
_CfprEtherTxStatsTotalBytes_Type=Unsigned64
_CfprEtherTxStatsTotalBytes_Object=MibTableColumn
cfprEtherTxStatsTotalBytes=_CfprEtherTxStatsTotalBytes_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,23),_CfprEtherTxStatsTotalBytes_Type())
cfprEtherTxStatsTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalBytes.setStatus(_A)
_CfprEtherTxStatsTotalBytesDelta_Type=Counter64
_CfprEtherTxStatsTotalBytesDelta_Object=MibTableColumn
cfprEtherTxStatsTotalBytesDelta=_CfprEtherTxStatsTotalBytesDelta_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,24),_CfprEtherTxStatsTotalBytesDelta_Type())
cfprEtherTxStatsTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalBytesDelta.setStatus(_A)
_CfprEtherTxStatsTotalBytesDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsTotalBytesDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsTotalBytesDeltaAvg=_CfprEtherTxStatsTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,25),_CfprEtherTxStatsTotalBytesDeltaAvg_Type())
cfprEtherTxStatsTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalBytesDeltaAvg.setStatus(_A)
_CfprEtherTxStatsTotalBytesDeltaMax_Type=Unsigned64
_CfprEtherTxStatsTotalBytesDeltaMax_Object=MibTableColumn
cfprEtherTxStatsTotalBytesDeltaMax=_CfprEtherTxStatsTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,26),_CfprEtherTxStatsTotalBytesDeltaMax_Type())
cfprEtherTxStatsTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalBytesDeltaMax.setStatus(_A)
_CfprEtherTxStatsTotalBytesDeltaMin_Type=Unsigned64
_CfprEtherTxStatsTotalBytesDeltaMin_Object=MibTableColumn
cfprEtherTxStatsTotalBytesDeltaMin=_CfprEtherTxStatsTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,27),_CfprEtherTxStatsTotalBytesDeltaMin_Type())
cfprEtherTxStatsTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalBytesDeltaMin.setStatus(_A)
_CfprEtherTxStatsTotalPackets_Type=Unsigned64
_CfprEtherTxStatsTotalPackets_Object=MibTableColumn
cfprEtherTxStatsTotalPackets=_CfprEtherTxStatsTotalPackets_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,28),_CfprEtherTxStatsTotalPackets_Type())
cfprEtherTxStatsTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalPackets.setStatus(_A)
_CfprEtherTxStatsTotalPacketsDelta_Type=Counter64
_CfprEtherTxStatsTotalPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsTotalPacketsDelta=_CfprEtherTxStatsTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,29),_CfprEtherTxStatsTotalPacketsDelta_Type())
cfprEtherTxStatsTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalPacketsDelta.setStatus(_A)
_CfprEtherTxStatsTotalPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsTotalPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsTotalPacketsDeltaAvg=_CfprEtherTxStatsTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,30),_CfprEtherTxStatsTotalPacketsDeltaAvg_Type())
cfprEtherTxStatsTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsTotalPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsTotalPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsTotalPacketsDeltaMax=_CfprEtherTxStatsTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,31),_CfprEtherTxStatsTotalPacketsDeltaMax_Type())
cfprEtherTxStatsTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsTotalPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsTotalPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsTotalPacketsDeltaMin=_CfprEtherTxStatsTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,32),_CfprEtherTxStatsTotalPacketsDeltaMin_Type())
cfprEtherTxStatsTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsTotalPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsUnicastPackets_Type=Unsigned64
_CfprEtherTxStatsUnicastPackets_Object=MibTableColumn
cfprEtherTxStatsUnicastPackets=_CfprEtherTxStatsUnicastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,33),_CfprEtherTxStatsUnicastPackets_Type())
cfprEtherTxStatsUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsUnicastPackets.setStatus(_A)
_CfprEtherTxStatsUnicastPacketsDelta_Type=Counter64
_CfprEtherTxStatsUnicastPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsUnicastPacketsDelta=_CfprEtherTxStatsUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,34),_CfprEtherTxStatsUnicastPacketsDelta_Type())
cfprEtherTxStatsUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsUnicastPacketsDelta.setStatus(_A)
_CfprEtherTxStatsUnicastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsUnicastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsUnicastPacketsDeltaAvg=_CfprEtherTxStatsUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,35),_CfprEtherTxStatsUnicastPacketsDeltaAvg_Type())
cfprEtherTxStatsUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsUnicastPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsUnicastPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsUnicastPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsUnicastPacketsDeltaMax=_CfprEtherTxStatsUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,36),_CfprEtherTxStatsUnicastPacketsDeltaMax_Type())
cfprEtherTxStatsUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsUnicastPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsUnicastPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsUnicastPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsUnicastPacketsDeltaMin=_CfprEtherTxStatsUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,37),_CfprEtherTxStatsUnicastPacketsDeltaMin_Type())
cfprEtherTxStatsUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsUnicastPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsUpdate_Type=Gauge32
_CfprEtherTxStatsUpdate_Object=MibTableColumn
cfprEtherTxStatsUpdate=_CfprEtherTxStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,21,30,1,38),_CfprEtherTxStatsUpdate_Type())
cfprEtherTxStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsUpdate.setStatus(_A)
_CfprEtherTxStatsHistTable_Object=MibTable
cfprEtherTxStatsHistTable=_CfprEtherTxStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,21,31))
if mibBuilder.loadTexts:cfprEtherTxStatsHistTable.setStatus(_A)
_CfprEtherTxStatsHistEntry_Object=MibTableRow
cfprEtherTxStatsHistEntry=_CfprEtherTxStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,21,31,1))
cfprEtherTxStatsHistEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cfprEtherTxStatsHistEntry.setStatus(_A)
_CfprEtherTxStatsHistInstanceId_Type=CfprManagedObjectId
_CfprEtherTxStatsHistInstanceId_Object=MibTableColumn
cfprEtherTxStatsHistInstanceId=_CfprEtherTxStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,1),_CfprEtherTxStatsHistInstanceId_Type())
cfprEtherTxStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherTxStatsHistInstanceId.setStatus(_A)
_CfprEtherTxStatsHistDn_Type=CfprManagedObjectDn
_CfprEtherTxStatsHistDn_Object=MibTableColumn
cfprEtherTxStatsHistDn=_CfprEtherTxStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,2),_CfprEtherTxStatsHistDn_Type())
cfprEtherTxStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistDn.setStatus(_A)
_CfprEtherTxStatsHistRn_Type=SnmpAdminString
_CfprEtherTxStatsHistRn_Object=MibTableColumn
cfprEtherTxStatsHistRn=_CfprEtherTxStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,3),_CfprEtherTxStatsHistRn_Type())
cfprEtherTxStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistRn.setStatus(_A)
_CfprEtherTxStatsHistBroadcastPackets_Type=Unsigned64
_CfprEtherTxStatsHistBroadcastPackets_Object=MibTableColumn
cfprEtherTxStatsHistBroadcastPackets=_CfprEtherTxStatsHistBroadcastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,4),_CfprEtherTxStatsHistBroadcastPackets_Type())
cfprEtherTxStatsHistBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistBroadcastPackets.setStatus(_A)
_CfprEtherTxStatsHistBroadcastPacketsDelta_Type=Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDelta=_CfprEtherTxStatsHistBroadcastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,5),_CfprEtherTxStatsHistBroadcastPacketsDelta_Type())
cfprEtherTxStatsHistBroadcastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistBroadcastPacketsDelta.setStatus(_A)
_CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDeltaAvg=_CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,6),_CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Type())
cfprEtherTxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistBroadcastPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDeltaMax=_CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,7),_CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Type())
cfprEtherTxStatsHistBroadcastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistBroadcastPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDeltaMin=_CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,8),_CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Type())
cfprEtherTxStatsHistBroadcastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistBroadcastPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsHistId_Type=Unsigned64
_CfprEtherTxStatsHistId_Object=MibTableColumn
cfprEtherTxStatsHistId=_CfprEtherTxStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,9),_CfprEtherTxStatsHistId_Type())
cfprEtherTxStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistId.setStatus(_A)
_CfprEtherTxStatsHistJumboPackets_Type=Unsigned64
_CfprEtherTxStatsHistJumboPackets_Object=MibTableColumn
cfprEtherTxStatsHistJumboPackets=_CfprEtherTxStatsHistJumboPackets_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,10),_CfprEtherTxStatsHistJumboPackets_Type())
cfprEtherTxStatsHistJumboPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistJumboPackets.setStatus(_A)
_CfprEtherTxStatsHistJumboPacketsDelta_Type=Unsigned64
_CfprEtherTxStatsHistJumboPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsHistJumboPacketsDelta=_CfprEtherTxStatsHistJumboPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,11),_CfprEtherTxStatsHistJumboPacketsDelta_Type())
cfprEtherTxStatsHistJumboPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistJumboPacketsDelta.setStatus(_A)
_CfprEtherTxStatsHistJumboPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsHistJumboPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsHistJumboPacketsDeltaAvg=_CfprEtherTxStatsHistJumboPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,12),_CfprEtherTxStatsHistJumboPacketsDeltaAvg_Type())
cfprEtherTxStatsHistJumboPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistJumboPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsHistJumboPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsHistJumboPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsHistJumboPacketsDeltaMax=_CfprEtherTxStatsHistJumboPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,13),_CfprEtherTxStatsHistJumboPacketsDeltaMax_Type())
cfprEtherTxStatsHistJumboPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistJumboPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsHistJumboPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsHistJumboPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsHistJumboPacketsDeltaMin=_CfprEtherTxStatsHistJumboPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,14),_CfprEtherTxStatsHistJumboPacketsDeltaMin_Type())
cfprEtherTxStatsHistJumboPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistJumboPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsHistMostRecent_Type=TruthValue
_CfprEtherTxStatsHistMostRecent_Object=MibTableColumn
cfprEtherTxStatsHistMostRecent=_CfprEtherTxStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,15),_CfprEtherTxStatsHistMostRecent_Type())
cfprEtherTxStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistMostRecent.setStatus(_A)
_CfprEtherTxStatsHistMulticastPackets_Type=Unsigned64
_CfprEtherTxStatsHistMulticastPackets_Object=MibTableColumn
cfprEtherTxStatsHistMulticastPackets=_CfprEtherTxStatsHistMulticastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,16),_CfprEtherTxStatsHistMulticastPackets_Type())
cfprEtherTxStatsHistMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistMulticastPackets.setStatus(_A)
_CfprEtherTxStatsHistMulticastPacketsDelta_Type=Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDelta=_CfprEtherTxStatsHistMulticastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,17),_CfprEtherTxStatsHistMulticastPacketsDelta_Type())
cfprEtherTxStatsHistMulticastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistMulticastPacketsDelta.setStatus(_A)
_CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDeltaAvg=_CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,18),_CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Type())
cfprEtherTxStatsHistMulticastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistMulticastPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsHistMulticastPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDeltaMax=_CfprEtherTxStatsHistMulticastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,19),_CfprEtherTxStatsHistMulticastPacketsDeltaMax_Type())
cfprEtherTxStatsHistMulticastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistMulticastPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsHistMulticastPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDeltaMin=_CfprEtherTxStatsHistMulticastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,20),_CfprEtherTxStatsHistMulticastPacketsDeltaMin_Type())
cfprEtherTxStatsHistMulticastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistMulticastPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsHistSuspect_Type=TruthValue
_CfprEtherTxStatsHistSuspect_Object=MibTableColumn
cfprEtherTxStatsHistSuspect=_CfprEtherTxStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,21),_CfprEtherTxStatsHistSuspect_Type())
cfprEtherTxStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistSuspect.setStatus(_A)
_CfprEtherTxStatsHistThresholded_Type=CfprEtherTxStatsHistThresholded
_CfprEtherTxStatsHistThresholded_Object=MibTableColumn
cfprEtherTxStatsHistThresholded=_CfprEtherTxStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,22),_CfprEtherTxStatsHistThresholded_Type())
cfprEtherTxStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistThresholded.setStatus(_A)
_CfprEtherTxStatsHistTimeCollected_Type=DateAndTime
_CfprEtherTxStatsHistTimeCollected_Object=MibTableColumn
cfprEtherTxStatsHistTimeCollected=_CfprEtherTxStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,23),_CfprEtherTxStatsHistTimeCollected_Type())
cfprEtherTxStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTimeCollected.setStatus(_A)
_CfprEtherTxStatsHistTotalBytes_Type=Unsigned64
_CfprEtherTxStatsHistTotalBytes_Object=MibTableColumn
cfprEtherTxStatsHistTotalBytes=_CfprEtherTxStatsHistTotalBytes_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,24),_CfprEtherTxStatsHistTotalBytes_Type())
cfprEtherTxStatsHistTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalBytes.setStatus(_A)
_CfprEtherTxStatsHistTotalBytesDelta_Type=Unsigned64
_CfprEtherTxStatsHistTotalBytesDelta_Object=MibTableColumn
cfprEtherTxStatsHistTotalBytesDelta=_CfprEtherTxStatsHistTotalBytesDelta_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,25),_CfprEtherTxStatsHistTotalBytesDelta_Type())
cfprEtherTxStatsHistTotalBytesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalBytesDelta.setStatus(_A)
_CfprEtherTxStatsHistTotalBytesDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsHistTotalBytesDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsHistTotalBytesDeltaAvg=_CfprEtherTxStatsHistTotalBytesDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,26),_CfprEtherTxStatsHistTotalBytesDeltaAvg_Type())
cfprEtherTxStatsHistTotalBytesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalBytesDeltaAvg.setStatus(_A)
_CfprEtherTxStatsHistTotalBytesDeltaMax_Type=Unsigned64
_CfprEtherTxStatsHistTotalBytesDeltaMax_Object=MibTableColumn
cfprEtherTxStatsHistTotalBytesDeltaMax=_CfprEtherTxStatsHistTotalBytesDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,27),_CfprEtherTxStatsHistTotalBytesDeltaMax_Type())
cfprEtherTxStatsHistTotalBytesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalBytesDeltaMax.setStatus(_A)
_CfprEtherTxStatsHistTotalBytesDeltaMin_Type=Unsigned64
_CfprEtherTxStatsHistTotalBytesDeltaMin_Object=MibTableColumn
cfprEtherTxStatsHistTotalBytesDeltaMin=_CfprEtherTxStatsHistTotalBytesDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,28),_CfprEtherTxStatsHistTotalBytesDeltaMin_Type())
cfprEtherTxStatsHistTotalBytesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalBytesDeltaMin.setStatus(_A)
_CfprEtherTxStatsHistTotalPackets_Type=Unsigned64
_CfprEtherTxStatsHistTotalPackets_Object=MibTableColumn
cfprEtherTxStatsHistTotalPackets=_CfprEtherTxStatsHistTotalPackets_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,29),_CfprEtherTxStatsHistTotalPackets_Type())
cfprEtherTxStatsHistTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalPackets.setStatus(_A)
_CfprEtherTxStatsHistTotalPacketsDelta_Type=Unsigned64
_CfprEtherTxStatsHistTotalPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsHistTotalPacketsDelta=_CfprEtherTxStatsHistTotalPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,30),_CfprEtherTxStatsHistTotalPacketsDelta_Type())
cfprEtherTxStatsHistTotalPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalPacketsDelta.setStatus(_A)
_CfprEtherTxStatsHistTotalPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsHistTotalPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsHistTotalPacketsDeltaAvg=_CfprEtherTxStatsHistTotalPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,31),_CfprEtherTxStatsHistTotalPacketsDeltaAvg_Type())
cfprEtherTxStatsHistTotalPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsHistTotalPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsHistTotalPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsHistTotalPacketsDeltaMax=_CfprEtherTxStatsHistTotalPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,32),_CfprEtherTxStatsHistTotalPacketsDeltaMax_Type())
cfprEtherTxStatsHistTotalPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsHistTotalPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsHistTotalPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsHistTotalPacketsDeltaMin=_CfprEtherTxStatsHistTotalPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,33),_CfprEtherTxStatsHistTotalPacketsDeltaMin_Type())
cfprEtherTxStatsHistTotalPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistTotalPacketsDeltaMin.setStatus(_A)
_CfprEtherTxStatsHistUnicastPackets_Type=Unsigned64
_CfprEtherTxStatsHistUnicastPackets_Object=MibTableColumn
cfprEtherTxStatsHistUnicastPackets=_CfprEtherTxStatsHistUnicastPackets_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,34),_CfprEtherTxStatsHistUnicastPackets_Type())
cfprEtherTxStatsHistUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistUnicastPackets.setStatus(_A)
_CfprEtherTxStatsHistUnicastPacketsDelta_Type=Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDelta_Object=MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDelta=_CfprEtherTxStatsHistUnicastPacketsDelta_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,35),_CfprEtherTxStatsHistUnicastPacketsDelta_Type())
cfprEtherTxStatsHistUnicastPacketsDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistUnicastPacketsDelta.setStatus(_A)
_CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Type=Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Object=MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDeltaAvg=_CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,36),_CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Type())
cfprEtherTxStatsHistUnicastPacketsDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistUnicastPacketsDeltaAvg.setStatus(_A)
_CfprEtherTxStatsHistUnicastPacketsDeltaMax_Type=Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDeltaMax_Object=MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDeltaMax=_CfprEtherTxStatsHistUnicastPacketsDeltaMax_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,37),_CfprEtherTxStatsHistUnicastPacketsDeltaMax_Type())
cfprEtherTxStatsHistUnicastPacketsDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistUnicastPacketsDeltaMax.setStatus(_A)
_CfprEtherTxStatsHistUnicastPacketsDeltaMin_Type=Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDeltaMin_Object=MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDeltaMin=_CfprEtherTxStatsHistUnicastPacketsDeltaMin_Object((1,3,6,1,4,1,9,9,826,1,21,31,1,38),_CfprEtherTxStatsHistUnicastPacketsDeltaMin_Type())
cfprEtherTxStatsHistUnicastPacketsDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherTxStatsHistUnicastPacketsDeltaMin.setStatus(_A)
_CfprEtherFailToWireTable_Object=MibTable
cfprEtherFailToWireTable=_CfprEtherFailToWireTable_Object((1,3,6,1,4,1,9,9,826,1,21,32))
if mibBuilder.loadTexts:cfprEtherFailToWireTable.setStatus(_A)
_CfprEtherFailToWireEntry_Object=MibTableRow
cfprEtherFailToWireEntry=_CfprEtherFailToWireEntry_Object((1,3,6,1,4,1,9,9,826,1,21,32,1))
cfprEtherFailToWireEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:cfprEtherFailToWireEntry.setStatus(_A)
_CfprEtherFailToWireInstanceId_Type=CfprManagedObjectId
_CfprEtherFailToWireInstanceId_Object=MibTableColumn
cfprEtherFailToWireInstanceId=_CfprEtherFailToWireInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,1),_CfprEtherFailToWireInstanceId_Type())
cfprEtherFailToWireInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFailToWireInstanceId.setStatus(_A)
_CfprEtherFailToWireDn_Type=CfprManagedObjectDn
_CfprEtherFailToWireDn_Object=MibTableColumn
cfprEtherFailToWireDn=_CfprEtherFailToWireDn_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,2),_CfprEtherFailToWireDn_Type())
cfprEtherFailToWireDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFailToWireDn.setStatus(_A)
_CfprEtherFailToWireRn_Type=SnmpAdminString
_CfprEtherFailToWireRn_Object=MibTableColumn
cfprEtherFailToWireRn=_CfprEtherFailToWireRn_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,3),_CfprEtherFailToWireRn_Type())
cfprEtherFailToWireRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFailToWireRn.setStatus(_A)
_CfprEtherFailToWireLocale_Type=CfprNetworkLocale
_CfprEtherFailToWireLocale_Object=MibTableColumn
cfprEtherFailToWireLocale=_CfprEtherFailToWireLocale_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,4),_CfprEtherFailToWireLocale_Type())
cfprEtherFailToWireLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFailToWireLocale.setStatus(_A)
_CfprEtherFailToWireName_Type=SnmpAdminString
_CfprEtherFailToWireName_Object=MibTableColumn
cfprEtherFailToWireName=_CfprEtherFailToWireName_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,5),_CfprEtherFailToWireName_Type())
cfprEtherFailToWireName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFailToWireName.setStatus(_A)
_CfprEtherFailToWireTransport_Type=CfprNetworkTransport
_CfprEtherFailToWireTransport_Object=MibTableColumn
cfprEtherFailToWireTransport=_CfprEtherFailToWireTransport_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,6),_CfprEtherFailToWireTransport_Type())
cfprEtherFailToWireTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFailToWireTransport.setStatus(_A)
_CfprEtherFailToWireType_Type=CfprNetworkConnectionType
_CfprEtherFailToWireType_Object=MibTableColumn
cfprEtherFailToWireType=_CfprEtherFailToWireType_Object((1,3,6,1,4,1,9,9,826,1,21,32,1,7),_CfprEtherFailToWireType_Type())
cfprEtherFailToWireType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFailToWireType.setStatus(_A)
_CfprEtherFtwPortPairTable_Object=MibTable
cfprEtherFtwPortPairTable=_CfprEtherFtwPortPairTable_Object((1,3,6,1,4,1,9,9,826,1,21,33))
if mibBuilder.loadTexts:cfprEtherFtwPortPairTable.setStatus(_A)
_CfprEtherFtwPortPairEntry_Object=MibTableRow
cfprEtherFtwPortPairEntry=_CfprEtherFtwPortPairEntry_Object((1,3,6,1,4,1,9,9,826,1,21,33,1))
cfprEtherFtwPortPairEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cfprEtherFtwPortPairEntry.setStatus(_A)
_CfprEtherFtwPortPairInstanceId_Type=CfprManagedObjectId
_CfprEtherFtwPortPairInstanceId_Object=MibTableColumn
cfprEtherFtwPortPairInstanceId=_CfprEtherFtwPortPairInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,1),_CfprEtherFtwPortPairInstanceId_Type())
cfprEtherFtwPortPairInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFtwPortPairInstanceId.setStatus(_A)
_CfprEtherFtwPortPairDn_Type=CfprManagedObjectDn
_CfprEtherFtwPortPairDn_Object=MibTableColumn
cfprEtherFtwPortPairDn=_CfprEtherFtwPortPairDn_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,2),_CfprEtherFtwPortPairDn_Type())
cfprEtherFtwPortPairDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairDn.setStatus(_A)
_CfprEtherFtwPortPairRn_Type=SnmpAdminString
_CfprEtherFtwPortPairRn_Object=MibTableColumn
cfprEtherFtwPortPairRn=_CfprEtherFtwPortPairRn_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,3),_CfprEtherFtwPortPairRn_Type())
cfprEtherFtwPortPairRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairRn.setStatus(_A)
_CfprEtherFtwPortPairAggrPortId_Type=Gauge32
_CfprEtherFtwPortPairAggrPortId_Object=MibTableColumn
cfprEtherFtwPortPairAggrPortId=_CfprEtherFtwPortPairAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,4),_CfprEtherFtwPortPairAggrPortId_Type())
cfprEtherFtwPortPairAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairAggrPortId.setStatus(_A)
_CfprEtherFtwPortPairChassisId_Type=Gauge32
_CfprEtherFtwPortPairChassisId_Object=MibTableColumn
cfprEtherFtwPortPairChassisId=_CfprEtherFtwPortPairChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,5),_CfprEtherFtwPortPairChassisId_Type())
cfprEtherFtwPortPairChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairChassisId.setStatus(_A)
_CfprEtherFtwPortPairEpDn_Type=SnmpAdminString
_CfprEtherFtwPortPairEpDn_Object=MibTableColumn
cfprEtherFtwPortPairEpDn=_CfprEtherFtwPortPairEpDn_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,6),_CfprEtherFtwPortPairEpDn_Type())
cfprEtherFtwPortPairEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairEpDn.setStatus(_A)
_CfprEtherFtwPortPairFsmDescr_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmDescr_Object=MibTableColumn
cfprEtherFtwPortPairFsmDescr=_CfprEtherFtwPortPairFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,7),_CfprEtherFtwPortPairFsmDescr_Type())
cfprEtherFtwPortPairFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmDescr.setStatus(_A)
_CfprEtherFtwPortPairFsmPrev_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmPrev_Object=MibTableColumn
cfprEtherFtwPortPairFsmPrev=_CfprEtherFtwPortPairFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,8),_CfprEtherFtwPortPairFsmPrev_Type())
cfprEtherFtwPortPairFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmPrev.setStatus(_A)
_CfprEtherFtwPortPairFsmProgr_Type=Gauge32
_CfprEtherFtwPortPairFsmProgr_Object=MibTableColumn
cfprEtherFtwPortPairFsmProgr=_CfprEtherFtwPortPairFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,9),_CfprEtherFtwPortPairFsmProgr_Type())
cfprEtherFtwPortPairFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmProgr.setStatus(_A)
_CfprEtherFtwPortPairFsmRmtInvErrCode_Type=Gauge32
_CfprEtherFtwPortPairFsmRmtInvErrCode_Object=MibTableColumn
cfprEtherFtwPortPairFsmRmtInvErrCode=_CfprEtherFtwPortPairFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,10),_CfprEtherFtwPortPairFsmRmtInvErrCode_Type())
cfprEtherFtwPortPairFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRmtInvErrCode.setStatus(_A)
_CfprEtherFtwPortPairFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmRmtInvErrDescr_Object=MibTableColumn
cfprEtherFtwPortPairFsmRmtInvErrDescr=_CfprEtherFtwPortPairFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,11),_CfprEtherFtwPortPairFsmRmtInvErrDescr_Type())
cfprEtherFtwPortPairFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRmtInvErrDescr.setStatus(_A)
_CfprEtherFtwPortPairFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprEtherFtwPortPairFsmRmtInvRslt_Object=MibTableColumn
cfprEtherFtwPortPairFsmRmtInvRslt=_CfprEtherFtwPortPairFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,12),_CfprEtherFtwPortPairFsmRmtInvRslt_Type())
cfprEtherFtwPortPairFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRmtInvRslt.setStatus(_A)
_CfprEtherFtwPortPairFsmStageDescr_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmStageDescr_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageDescr=_CfprEtherFtwPortPairFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,13),_CfprEtherFtwPortPairFsmStageDescr_Type())
cfprEtherFtwPortPairFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageDescr.setStatus(_A)
_CfprEtherFtwPortPairFsmStamp_Type=DateAndTime
_CfprEtherFtwPortPairFsmStamp_Object=MibTableColumn
cfprEtherFtwPortPairFsmStamp=_CfprEtherFtwPortPairFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,14),_CfprEtherFtwPortPairFsmStamp_Type())
cfprEtherFtwPortPairFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStamp.setStatus(_A)
_CfprEtherFtwPortPairFsmStatus_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmStatus_Object=MibTableColumn
cfprEtherFtwPortPairFsmStatus=_CfprEtherFtwPortPairFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,15),_CfprEtherFtwPortPairFsmStatus_Type())
cfprEtherFtwPortPairFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStatus.setStatus(_A)
_CfprEtherFtwPortPairFsmTry_Type=Gauge32
_CfprEtherFtwPortPairFsmTry_Object=MibTableColumn
cfprEtherFtwPortPairFsmTry=_CfprEtherFtwPortPairFsmTry_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,16),_CfprEtherFtwPortPairFsmTry_Type())
cfprEtherFtwPortPairFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTry.setStatus(_A)
_CfprEtherFtwPortPairIfRole_Type=CfprNetworkPortRole
_CfprEtherFtwPortPairIfRole_Object=MibTableColumn
cfprEtherFtwPortPairIfRole=_CfprEtherFtwPortPairIfRole_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,17),_CfprEtherFtwPortPairIfRole_Type())
cfprEtherFtwPortPairIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairIfRole.setStatus(_A)
_CfprEtherFtwPortPairIfType_Type=CfprNetworkPhysEpIfType
_CfprEtherFtwPortPairIfType_Object=MibTableColumn
cfprEtherFtwPortPairIfType=_CfprEtherFtwPortPairIfType_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,18),_CfprEtherFtwPortPairIfType_Type())
cfprEtherFtwPortPairIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairIfType.setStatus(_A)
_CfprEtherFtwPortPairLocale_Type=CfprNetworkLocale
_CfprEtherFtwPortPairLocale_Object=MibTableColumn
cfprEtherFtwPortPairLocale=_CfprEtherFtwPortPairLocale_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,19),_CfprEtherFtwPortPairLocale_Type())
cfprEtherFtwPortPairLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairLocale.setStatus(_A)
_CfprEtherFtwPortPairMode_Type=CfprEtherFtwPortPairMode
_CfprEtherFtwPortPairMode_Object=MibTableColumn
cfprEtherFtwPortPairMode=_CfprEtherFtwPortPairMode_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,20),_CfprEtherFtwPortPairMode_Type())
cfprEtherFtwPortPairMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairMode.setStatus(_A)
_CfprEtherFtwPortPairName_Type=SnmpAdminString
_CfprEtherFtwPortPairName_Object=MibTableColumn
cfprEtherFtwPortPairName=_CfprEtherFtwPortPairName_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,21),_CfprEtherFtwPortPairName_Type())
cfprEtherFtwPortPairName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairName.setStatus(_A)
_CfprEtherFtwPortPairOperMode_Type=CfprEtherFtwOperMode
_CfprEtherFtwPortPairOperMode_Object=MibTableColumn
cfprEtherFtwPortPairOperMode=_CfprEtherFtwPortPairOperMode_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,22),_CfprEtherFtwPortPairOperMode_Type())
cfprEtherFtwPortPairOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairOperMode.setStatus(_A)
_CfprEtherFtwPortPairPeerAggrPortId_Type=Gauge32
_CfprEtherFtwPortPairPeerAggrPortId_Object=MibTableColumn
cfprEtherFtwPortPairPeerAggrPortId=_CfprEtherFtwPortPairPeerAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,23),_CfprEtherFtwPortPairPeerAggrPortId_Type())
cfprEtherFtwPortPairPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPeerAggrPortId.setStatus(_A)
_CfprEtherFtwPortPairPeerChassisId_Type=Gauge32
_CfprEtherFtwPortPairPeerChassisId_Object=MibTableColumn
cfprEtherFtwPortPairPeerChassisId=_CfprEtherFtwPortPairPeerChassisId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,24),_CfprEtherFtwPortPairPeerChassisId_Type())
cfprEtherFtwPortPairPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPeerChassisId.setStatus(_A)
_CfprEtherFtwPortPairPeerDn_Type=SnmpAdminString
_CfprEtherFtwPortPairPeerDn_Object=MibTableColumn
cfprEtherFtwPortPairPeerDn=_CfprEtherFtwPortPairPeerDn_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,25),_CfprEtherFtwPortPairPeerDn_Type())
cfprEtherFtwPortPairPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPeerDn.setStatus(_A)
_CfprEtherFtwPortPairPeerPortId_Type=Gauge32
_CfprEtherFtwPortPairPeerPortId_Object=MibTableColumn
cfprEtherFtwPortPairPeerPortId=_CfprEtherFtwPortPairPeerPortId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,26),_CfprEtherFtwPortPairPeerPortId_Type())
cfprEtherFtwPortPairPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPeerPortId.setStatus(_A)
_CfprEtherFtwPortPairPeerPortName_Type=SnmpAdminString
_CfprEtherFtwPortPairPeerPortName_Object=MibTableColumn
cfprEtherFtwPortPairPeerPortName=_CfprEtherFtwPortPairPeerPortName_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,27),_CfprEtherFtwPortPairPeerPortName_Type())
cfprEtherFtwPortPairPeerPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPeerPortName.setStatus(_A)
_CfprEtherFtwPortPairPeerSlotId_Type=Gauge32
_CfprEtherFtwPortPairPeerSlotId_Object=MibTableColumn
cfprEtherFtwPortPairPeerSlotId=_CfprEtherFtwPortPairPeerSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,28),_CfprEtherFtwPortPairPeerSlotId_Type())
cfprEtherFtwPortPairPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPeerSlotId.setStatus(_A)
_CfprEtherFtwPortPairPortId_Type=Gauge32
_CfprEtherFtwPortPairPortId_Object=MibTableColumn
cfprEtherFtwPortPairPortId=_CfprEtherFtwPortPairPortId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,29),_CfprEtherFtwPortPairPortId_Type())
cfprEtherFtwPortPairPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPortId.setStatus(_A)
_CfprEtherFtwPortPairPortName_Type=SnmpAdminString
_CfprEtherFtwPortPairPortName_Object=MibTableColumn
cfprEtherFtwPortPairPortName=_CfprEtherFtwPortPairPortName_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,30),_CfprEtherFtwPortPairPortName_Type())
cfprEtherFtwPortPairPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairPortName.setStatus(_A)
_CfprEtherFtwPortPairSlotId_Type=Gauge32
_CfprEtherFtwPortPairSlotId_Object=MibTableColumn
cfprEtherFtwPortPairSlotId=_CfprEtherFtwPortPairSlotId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,31),_CfprEtherFtwPortPairSlotId_Type())
cfprEtherFtwPortPairSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairSlotId.setStatus(_A)
_CfprEtherFtwPortPairSwitchId_Type=CfprNetworkSwitchId
_CfprEtherFtwPortPairSwitchId_Object=MibTableColumn
cfprEtherFtwPortPairSwitchId=_CfprEtherFtwPortPairSwitchId_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,32),_CfprEtherFtwPortPairSwitchId_Type())
cfprEtherFtwPortPairSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairSwitchId.setStatus(_A)
_CfprEtherFtwPortPairTransport_Type=CfprNetworkTransport
_CfprEtherFtwPortPairTransport_Object=MibTableColumn
cfprEtherFtwPortPairTransport=_CfprEtherFtwPortPairTransport_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,33),_CfprEtherFtwPortPairTransport_Type())
cfprEtherFtwPortPairTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairTransport.setStatus(_A)
_CfprEtherFtwPortPairTs_Type=DateAndTime
_CfprEtherFtwPortPairTs_Object=MibTableColumn
cfprEtherFtwPortPairTs=_CfprEtherFtwPortPairTs_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,34),_CfprEtherFtwPortPairTs_Type())
cfprEtherFtwPortPairTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairTs.setStatus(_A)
_CfprEtherFtwPortPairType_Type=CfprNetworkConnectionType
_CfprEtherFtwPortPairType_Object=MibTableColumn
cfprEtherFtwPortPairType=_CfprEtherFtwPortPairType_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,35),_CfprEtherFtwPortPairType_Type())
cfprEtherFtwPortPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairType.setStatus(_A)
_CfprEtherFtwPortPairWdtStart_Type=Gauge32
_CfprEtherFtwPortPairWdtStart_Object=MibTableColumn
cfprEtherFtwPortPairWdtStart=_CfprEtherFtwPortPairWdtStart_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,36),_CfprEtherFtwPortPairWdtStart_Type())
cfprEtherFtwPortPairWdtStart.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairWdtStart.setStatus(_A)
_CfprEtherFtwPortPairWdtState_Type=CfprEtherFtwPortPairWdtState
_CfprEtherFtwPortPairWdtState_Object=MibTableColumn
cfprEtherFtwPortPairWdtState=_CfprEtherFtwPortPairWdtState_Object((1,3,6,1,4,1,9,9,826,1,21,33,1,37),_CfprEtherFtwPortPairWdtState_Type())
cfprEtherFtwPortPairWdtState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairWdtState.setStatus(_A)
_CfprEtherFtwPortPairFsmTable_Object=MibTable
cfprEtherFtwPortPairFsmTable=_CfprEtherFtwPortPairFsmTable_Object((1,3,6,1,4,1,9,9,826,1,21,34))
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTable.setStatus(_A)
_CfprEtherFtwPortPairFsmEntry_Object=MibTableRow
cfprEtherFtwPortPairFsmEntry=_CfprEtherFtwPortPairFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,21,34,1))
cfprEtherFtwPortPairFsmEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmEntry.setStatus(_A)
_CfprEtherFtwPortPairFsmInstanceId_Type=CfprManagedObjectId
_CfprEtherFtwPortPairFsmInstanceId_Object=MibTableColumn
cfprEtherFtwPortPairFsmInstanceId=_CfprEtherFtwPortPairFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,1),_CfprEtherFtwPortPairFsmInstanceId_Type())
cfprEtherFtwPortPairFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmInstanceId.setStatus(_A)
_CfprEtherFtwPortPairFsmDn_Type=CfprManagedObjectDn
_CfprEtherFtwPortPairFsmDn_Object=MibTableColumn
cfprEtherFtwPortPairFsmDn=_CfprEtherFtwPortPairFsmDn_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,2),_CfprEtherFtwPortPairFsmDn_Type())
cfprEtherFtwPortPairFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmDn.setStatus(_A)
_CfprEtherFtwPortPairFsmRn_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmRn_Object=MibTableColumn
cfprEtherFtwPortPairFsmRn=_CfprEtherFtwPortPairFsmRn_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,3),_CfprEtherFtwPortPairFsmRn_Type())
cfprEtherFtwPortPairFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRn.setStatus(_A)
_CfprEtherFtwPortPairFsmCompletionTime_Type=DateAndTime
_CfprEtherFtwPortPairFsmCompletionTime_Object=MibTableColumn
cfprEtherFtwPortPairFsmCompletionTime=_CfprEtherFtwPortPairFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,4),_CfprEtherFtwPortPairFsmCompletionTime_Type())
cfprEtherFtwPortPairFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmCompletionTime.setStatus(_A)
_CfprEtherFtwPortPairFsmCurrentFsm_Type=CfprEtherFtwPortPairFsmCurrentFsm
_CfprEtherFtwPortPairFsmCurrentFsm_Object=MibTableColumn
cfprEtherFtwPortPairFsmCurrentFsm=_CfprEtherFtwPortPairFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,5),_CfprEtherFtwPortPairFsmCurrentFsm_Type())
cfprEtherFtwPortPairFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmCurrentFsm.setStatus(_A)
_CfprEtherFtwPortPairFsmDescrData_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmDescrData_Object=MibTableColumn
cfprEtherFtwPortPairFsmDescrData=_CfprEtherFtwPortPairFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,6),_CfprEtherFtwPortPairFsmDescrData_Type())
cfprEtherFtwPortPairFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmDescrData.setStatus(_A)
_CfprEtherFtwPortPairFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprEtherFtwPortPairFsmFsmStatus_Object=MibTableColumn
cfprEtherFtwPortPairFsmFsmStatus=_CfprEtherFtwPortPairFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,7),_CfprEtherFtwPortPairFsmFsmStatus_Type())
cfprEtherFtwPortPairFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmFsmStatus.setStatus(_A)
_CfprEtherFtwPortPairFsmProgress_Type=Gauge32
_CfprEtherFtwPortPairFsmProgress_Object=MibTableColumn
cfprEtherFtwPortPairFsmProgress=_CfprEtherFtwPortPairFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,8),_CfprEtherFtwPortPairFsmProgress_Type())
cfprEtherFtwPortPairFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmProgress.setStatus(_A)
_CfprEtherFtwPortPairFsmRmtErrCode_Type=Gauge32
_CfprEtherFtwPortPairFsmRmtErrCode_Object=MibTableColumn
cfprEtherFtwPortPairFsmRmtErrCode=_CfprEtherFtwPortPairFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,9),_CfprEtherFtwPortPairFsmRmtErrCode_Type())
cfprEtherFtwPortPairFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRmtErrCode.setStatus(_A)
_CfprEtherFtwPortPairFsmRmtErrDescr_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmRmtErrDescr_Object=MibTableColumn
cfprEtherFtwPortPairFsmRmtErrDescr=_CfprEtherFtwPortPairFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,10),_CfprEtherFtwPortPairFsmRmtErrDescr_Type())
cfprEtherFtwPortPairFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRmtErrDescr.setStatus(_A)
_CfprEtherFtwPortPairFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprEtherFtwPortPairFsmRmtRslt_Object=MibTableColumn
cfprEtherFtwPortPairFsmRmtRslt=_CfprEtherFtwPortPairFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,21,34,1,11),_CfprEtherFtwPortPairFsmRmtRslt_Type())
cfprEtherFtwPortPairFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmRmtRslt.setStatus(_A)
_CfprEtherFtwPortPairFsmStageTable_Object=MibTable
cfprEtherFtwPortPairFsmStageTable=_CfprEtherFtwPortPairFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,21,35))
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageTable.setStatus(_A)
_CfprEtherFtwPortPairFsmStageEntry_Object=MibTableRow
cfprEtherFtwPortPairFsmStageEntry=_CfprEtherFtwPortPairFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,21,35,1))
cfprEtherFtwPortPairFsmStageEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageEntry.setStatus(_A)
_CfprEtherFtwPortPairFsmStageInstanceId_Type=CfprManagedObjectId
_CfprEtherFtwPortPairFsmStageInstanceId_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageInstanceId=_CfprEtherFtwPortPairFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,1),_CfprEtherFtwPortPairFsmStageInstanceId_Type())
cfprEtherFtwPortPairFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageInstanceId.setStatus(_A)
_CfprEtherFtwPortPairFsmStageDn_Type=CfprManagedObjectDn
_CfprEtherFtwPortPairFsmStageDn_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageDn=_CfprEtherFtwPortPairFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,2),_CfprEtherFtwPortPairFsmStageDn_Type())
cfprEtherFtwPortPairFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageDn.setStatus(_A)
_CfprEtherFtwPortPairFsmStageRn_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmStageRn_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageRn=_CfprEtherFtwPortPairFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,3),_CfprEtherFtwPortPairFsmStageRn_Type())
cfprEtherFtwPortPairFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageRn.setStatus(_A)
_CfprEtherFtwPortPairFsmStageDescrData_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmStageDescrData_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageDescrData=_CfprEtherFtwPortPairFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,4),_CfprEtherFtwPortPairFsmStageDescrData_Type())
cfprEtherFtwPortPairFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageDescrData.setStatus(_A)
_CfprEtherFtwPortPairFsmStageLastUpdateTime_Type=DateAndTime
_CfprEtherFtwPortPairFsmStageLastUpdateTime_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageLastUpdateTime=_CfprEtherFtwPortPairFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,5),_CfprEtherFtwPortPairFsmStageLastUpdateTime_Type())
cfprEtherFtwPortPairFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageLastUpdateTime.setStatus(_A)
_CfprEtherFtwPortPairFsmStageName_Type=CfprEtherFtwPortPairFsmStageName
_CfprEtherFtwPortPairFsmStageName_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageName=_CfprEtherFtwPortPairFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,6),_CfprEtherFtwPortPairFsmStageName_Type())
cfprEtherFtwPortPairFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageName.setStatus(_A)
_CfprEtherFtwPortPairFsmStageOrder_Type=Gauge32
_CfprEtherFtwPortPairFsmStageOrder_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageOrder=_CfprEtherFtwPortPairFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,7),_CfprEtherFtwPortPairFsmStageOrder_Type())
cfprEtherFtwPortPairFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageOrder.setStatus(_A)
_CfprEtherFtwPortPairFsmStageRetry_Type=Gauge32
_CfprEtherFtwPortPairFsmStageRetry_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageRetry=_CfprEtherFtwPortPairFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,8),_CfprEtherFtwPortPairFsmStageRetry_Type())
cfprEtherFtwPortPairFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageRetry.setStatus(_A)
_CfprEtherFtwPortPairFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprEtherFtwPortPairFsmStageStageStatus_Object=MibTableColumn
cfprEtherFtwPortPairFsmStageStageStatus=_CfprEtherFtwPortPairFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,21,35,1,9),_CfprEtherFtwPortPairFsmStageStageStatus_Type())
cfprEtherFtwPortPairFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmStageStageStatus.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskTable_Object=MibTable
cfprEtherFtwPortPairFsmTaskTable=_CfprEtherFtwPortPairFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,21,36))
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskTable.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskEntry_Object=MibTableRow
cfprEtherFtwPortPairFsmTaskEntry=_CfprEtherFtwPortPairFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,21,36,1))
cfprEtherFtwPortPairFsmTaskEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskEntry.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprEtherFtwPortPairFsmTaskInstanceId_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskInstanceId=_CfprEtherFtwPortPairFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,1),_CfprEtherFtwPortPairFsmTaskInstanceId_Type())
cfprEtherFtwPortPairFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskInstanceId.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskDn_Type=CfprManagedObjectDn
_CfprEtherFtwPortPairFsmTaskDn_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskDn=_CfprEtherFtwPortPairFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,2),_CfprEtherFtwPortPairFsmTaskDn_Type())
cfprEtherFtwPortPairFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskDn.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskRn_Type=SnmpAdminString
_CfprEtherFtwPortPairFsmTaskRn_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskRn=_CfprEtherFtwPortPairFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,3),_CfprEtherFtwPortPairFsmTaskRn_Type())
cfprEtherFtwPortPairFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskRn.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskCompletion_Type=CfprFsmCompletion
_CfprEtherFtwPortPairFsmTaskCompletion_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskCompletion=_CfprEtherFtwPortPairFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,4),_CfprEtherFtwPortPairFsmTaskCompletion_Type())
cfprEtherFtwPortPairFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskCompletion.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskFlags_Type=CfprFsmFlags
_CfprEtherFtwPortPairFsmTaskFlags_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskFlags=_CfprEtherFtwPortPairFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,5),_CfprEtherFtwPortPairFsmTaskFlags_Type())
cfprEtherFtwPortPairFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskFlags.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskItem_Type=CfprEtherFtwPortPairFsmTaskItem
_CfprEtherFtwPortPairFsmTaskItem_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskItem=_CfprEtherFtwPortPairFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,6),_CfprEtherFtwPortPairFsmTaskItem_Type())
cfprEtherFtwPortPairFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskItem.setStatus(_A)
_CfprEtherFtwPortPairFsmTaskSeqId_Type=Gauge32
_CfprEtherFtwPortPairFsmTaskSeqId_Object=MibTableColumn
cfprEtherFtwPortPairFsmTaskSeqId=_CfprEtherFtwPortPairFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,21,36,1,7),_CfprEtherFtwPortPairFsmTaskSeqId_Type())
cfprEtherFtwPortPairFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprEtherFtwPortPairFsmTaskSeqId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprEtherObjects':cfprEtherObjects,'cfprEtherErrStatsTable':cfprEtherErrStatsTable,'cfprEtherErrStatsEntry':cfprEtherErrStatsEntry,_E:cfprEtherErrStatsInstanceId,'cfprEtherErrStatsDn':cfprEtherErrStatsDn,'cfprEtherErrStatsRn':cfprEtherErrStatsRn,'cfprEtherErrStatsAlign':cfprEtherErrStatsAlign,'cfprEtherErrStatsAlignDelta':cfprEtherErrStatsAlignDelta,'cfprEtherErrStatsAlignDeltaAvg':cfprEtherErrStatsAlignDeltaAvg,'cfprEtherErrStatsAlignDeltaMax':cfprEtherErrStatsAlignDeltaMax,'cfprEtherErrStatsAlignDeltaMin':cfprEtherErrStatsAlignDeltaMin,'cfprEtherErrStatsDeferredTx':cfprEtherErrStatsDeferredTx,'cfprEtherErrStatsDeferredTxDelta':cfprEtherErrStatsDeferredTxDelta,'cfprEtherErrStatsDeferredTxDeltaAvg':cfprEtherErrStatsDeferredTxDeltaAvg,'cfprEtherErrStatsDeferredTxDeltaMax':cfprEtherErrStatsDeferredTxDeltaMax,'cfprEtherErrStatsDeferredTxDeltaMin':cfprEtherErrStatsDeferredTxDeltaMin,'cfprEtherErrStatsFcs':cfprEtherErrStatsFcs,'cfprEtherErrStatsFcsDelta':cfprEtherErrStatsFcsDelta,'cfprEtherErrStatsFcsDeltaAvg':cfprEtherErrStatsFcsDeltaAvg,'cfprEtherErrStatsFcsDeltaMax':cfprEtherErrStatsFcsDeltaMax,'cfprEtherErrStatsFcsDeltaMin':cfprEtherErrStatsFcsDeltaMin,'cfprEtherErrStatsIntMacRx':cfprEtherErrStatsIntMacRx,'cfprEtherErrStatsIntMacRxDelta':cfprEtherErrStatsIntMacRxDelta,'cfprEtherErrStatsIntMacRxDeltaAvg':cfprEtherErrStatsIntMacRxDeltaAvg,'cfprEtherErrStatsIntMacRxDeltaMax':cfprEtherErrStatsIntMacRxDeltaMax,'cfprEtherErrStatsIntMacRxDeltaMin':cfprEtherErrStatsIntMacRxDeltaMin,'cfprEtherErrStatsIntMacTx':cfprEtherErrStatsIntMacTx,'cfprEtherErrStatsIntMacTxDelta':cfprEtherErrStatsIntMacTxDelta,'cfprEtherErrStatsIntMacTxDeltaAvg':cfprEtherErrStatsIntMacTxDeltaAvg,'cfprEtherErrStatsIntMacTxDeltaMax':cfprEtherErrStatsIntMacTxDeltaMax,'cfprEtherErrStatsIntMacTxDeltaMin':cfprEtherErrStatsIntMacTxDeltaMin,'cfprEtherErrStatsIntervals':cfprEtherErrStatsIntervals,'cfprEtherErrStatsOutDiscard':cfprEtherErrStatsOutDiscard,'cfprEtherErrStatsOutDiscardDelta':cfprEtherErrStatsOutDiscardDelta,'cfprEtherErrStatsOutDiscardDeltaAvg':cfprEtherErrStatsOutDiscardDeltaAvg,'cfprEtherErrStatsOutDiscardDeltaMax':cfprEtherErrStatsOutDiscardDeltaMax,'cfprEtherErrStatsOutDiscardDeltaMin':cfprEtherErrStatsOutDiscardDeltaMin,'cfprEtherErrStatsRcv':cfprEtherErrStatsRcv,'cfprEtherErrStatsRcvDelta':cfprEtherErrStatsRcvDelta,'cfprEtherErrStatsRcvDeltaAvg':cfprEtherErrStatsRcvDeltaAvg,'cfprEtherErrStatsRcvDeltaMax':cfprEtherErrStatsRcvDeltaMax,'cfprEtherErrStatsRcvDeltaMin':cfprEtherErrStatsRcvDeltaMin,'cfprEtherErrStatsSuspect':cfprEtherErrStatsSuspect,'cfprEtherErrStatsThresholded':cfprEtherErrStatsThresholded,'cfprEtherErrStatsTimeCollected':cfprEtherErrStatsTimeCollected,'cfprEtherErrStatsUnderSize':cfprEtherErrStatsUnderSize,'cfprEtherErrStatsUnderSizeDelta':cfprEtherErrStatsUnderSizeDelta,'cfprEtherErrStatsUnderSizeDeltaAvg':cfprEtherErrStatsUnderSizeDeltaAvg,'cfprEtherErrStatsUnderSizeDeltaMax':cfprEtherErrStatsUnderSizeDeltaMax,'cfprEtherErrStatsUnderSizeDeltaMin':cfprEtherErrStatsUnderSizeDeltaMin,'cfprEtherErrStatsUpdate':cfprEtherErrStatsUpdate,'cfprEtherErrStatsXmit':cfprEtherErrStatsXmit,'cfprEtherErrStatsXmitDelta':cfprEtherErrStatsXmitDelta,'cfprEtherErrStatsXmitDeltaAvg':cfprEtherErrStatsXmitDeltaAvg,'cfprEtherErrStatsXmitDeltaMax':cfprEtherErrStatsXmitDeltaMax,'cfprEtherErrStatsXmitDeltaMin':cfprEtherErrStatsXmitDeltaMin,'cfprEtherErrStatsHistTable':cfprEtherErrStatsHistTable,'cfprEtherErrStatsHistEntry':cfprEtherErrStatsHistEntry,_F:cfprEtherErrStatsHistInstanceId,'cfprEtherErrStatsHistDn':cfprEtherErrStatsHistDn,'cfprEtherErrStatsHistRn':cfprEtherErrStatsHistRn,'cfprEtherErrStatsHistAlign':cfprEtherErrStatsHistAlign,'cfprEtherErrStatsHistAlignDelta':cfprEtherErrStatsHistAlignDelta,'cfprEtherErrStatsHistAlignDeltaAvg':cfprEtherErrStatsHistAlignDeltaAvg,'cfprEtherErrStatsHistAlignDeltaMax':cfprEtherErrStatsHistAlignDeltaMax,'cfprEtherErrStatsHistAlignDeltaMin':cfprEtherErrStatsHistAlignDeltaMin,'cfprEtherErrStatsHistDeferredTx':cfprEtherErrStatsHistDeferredTx,'cfprEtherErrStatsHistDeferredTxDelta':cfprEtherErrStatsHistDeferredTxDelta,'cfprEtherErrStatsHistDeferredTxDeltaAvg':cfprEtherErrStatsHistDeferredTxDeltaAvg,'cfprEtherErrStatsHistDeferredTxDeltaMax':cfprEtherErrStatsHistDeferredTxDeltaMax,'cfprEtherErrStatsHistDeferredTxDeltaMin':cfprEtherErrStatsHistDeferredTxDeltaMin,'cfprEtherErrStatsHistFcs':cfprEtherErrStatsHistFcs,'cfprEtherErrStatsHistFcsDelta':cfprEtherErrStatsHistFcsDelta,'cfprEtherErrStatsHistFcsDeltaAvg':cfprEtherErrStatsHistFcsDeltaAvg,'cfprEtherErrStatsHistFcsDeltaMax':cfprEtherErrStatsHistFcsDeltaMax,'cfprEtherErrStatsHistFcsDeltaMin':cfprEtherErrStatsHistFcsDeltaMin,'cfprEtherErrStatsHistId':cfprEtherErrStatsHistId,'cfprEtherErrStatsHistIntMacRx':cfprEtherErrStatsHistIntMacRx,'cfprEtherErrStatsHistIntMacRxDelta':cfprEtherErrStatsHistIntMacRxDelta,'cfprEtherErrStatsHistIntMacRxDeltaAvg':cfprEtherErrStatsHistIntMacRxDeltaAvg,'cfprEtherErrStatsHistIntMacRxDeltaMax':cfprEtherErrStatsHistIntMacRxDeltaMax,'cfprEtherErrStatsHistIntMacRxDeltaMin':cfprEtherErrStatsHistIntMacRxDeltaMin,'cfprEtherErrStatsHistIntMacTx':cfprEtherErrStatsHistIntMacTx,'cfprEtherErrStatsHistIntMacTxDelta':cfprEtherErrStatsHistIntMacTxDelta,'cfprEtherErrStatsHistIntMacTxDeltaAvg':cfprEtherErrStatsHistIntMacTxDeltaAvg,'cfprEtherErrStatsHistIntMacTxDeltaMax':cfprEtherErrStatsHistIntMacTxDeltaMax,'cfprEtherErrStatsHistIntMacTxDeltaMin':cfprEtherErrStatsHistIntMacTxDeltaMin,'cfprEtherErrStatsHistMostRecent':cfprEtherErrStatsHistMostRecent,'cfprEtherErrStatsHistOutDiscard':cfprEtherErrStatsHistOutDiscard,'cfprEtherErrStatsHistOutDiscardDelta':cfprEtherErrStatsHistOutDiscardDelta,'cfprEtherErrStatsHistOutDiscardDeltaAvg':cfprEtherErrStatsHistOutDiscardDeltaAvg,'cfprEtherErrStatsHistOutDiscardDeltaMax':cfprEtherErrStatsHistOutDiscardDeltaMax,'cfprEtherErrStatsHistOutDiscardDeltaMin':cfprEtherErrStatsHistOutDiscardDeltaMin,'cfprEtherErrStatsHistRcv':cfprEtherErrStatsHistRcv,'cfprEtherErrStatsHistRcvDelta':cfprEtherErrStatsHistRcvDelta,'cfprEtherErrStatsHistRcvDeltaAvg':cfprEtherErrStatsHistRcvDeltaAvg,'cfprEtherErrStatsHistRcvDeltaMax':cfprEtherErrStatsHistRcvDeltaMax,'cfprEtherErrStatsHistRcvDeltaMin':cfprEtherErrStatsHistRcvDeltaMin,'cfprEtherErrStatsHistSuspect':cfprEtherErrStatsHistSuspect,'cfprEtherErrStatsHistThresholded':cfprEtherErrStatsHistThresholded,'cfprEtherErrStatsHistTimeCollected':cfprEtherErrStatsHistTimeCollected,'cfprEtherErrStatsHistUnderSize':cfprEtherErrStatsHistUnderSize,'cfprEtherErrStatsHistUnderSizeDelta':cfprEtherErrStatsHistUnderSizeDelta,'cfprEtherErrStatsHistUnderSizeDeltaAvg':cfprEtherErrStatsHistUnderSizeDeltaAvg,'cfprEtherErrStatsHistUnderSizeDeltaMax':cfprEtherErrStatsHistUnderSizeDeltaMax,'cfprEtherErrStatsHistUnderSizeDeltaMin':cfprEtherErrStatsHistUnderSizeDeltaMin,'cfprEtherErrStatsHistXmit':cfprEtherErrStatsHistXmit,'cfprEtherErrStatsHistXmitDelta':cfprEtherErrStatsHistXmitDelta,'cfprEtherErrStatsHistXmitDeltaAvg':cfprEtherErrStatsHistXmitDeltaAvg,'cfprEtherErrStatsHistXmitDeltaMax':cfprEtherErrStatsHistXmitDeltaMax,'cfprEtherErrStatsHistXmitDeltaMin':cfprEtherErrStatsHistXmitDeltaMin,'cfprEtherFcoeInterfaceStatsTable':cfprEtherFcoeInterfaceStatsTable,'cfprEtherFcoeInterfaceStatsEntry':cfprEtherFcoeInterfaceStatsEntry,_G:cfprEtherFcoeInterfaceStatsInstanceId,'cfprEtherFcoeInterfaceStatsDn':cfprEtherFcoeInterfaceStatsDn,'cfprEtherFcoeInterfaceStatsRn':cfprEtherFcoeInterfaceStatsRn,'cfprEtherFcoeInterfaceStatsBytesRx':cfprEtherFcoeInterfaceStatsBytesRx,'cfprEtherFcoeInterfaceStatsBytesRxDelta':cfprEtherFcoeInterfaceStatsBytesRxDelta,'cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg':cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg,'cfprEtherFcoeInterfaceStatsBytesRxDeltaMax':cfprEtherFcoeInterfaceStatsBytesRxDeltaMax,'cfprEtherFcoeInterfaceStatsBytesRxDeltaMin':cfprEtherFcoeInterfaceStatsBytesRxDeltaMin,'cfprEtherFcoeInterfaceStatsBytesTx':cfprEtherFcoeInterfaceStatsBytesTx,'cfprEtherFcoeInterfaceStatsBytesTxDelta':cfprEtherFcoeInterfaceStatsBytesTxDelta,'cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg':cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg,'cfprEtherFcoeInterfaceStatsBytesTxDeltaMax':cfprEtherFcoeInterfaceStatsBytesTxDeltaMax,'cfprEtherFcoeInterfaceStatsBytesTxDeltaMin':cfprEtherFcoeInterfaceStatsBytesTxDeltaMin,'cfprEtherFcoeInterfaceStatsDroppedRx':cfprEtherFcoeInterfaceStatsDroppedRx,'cfprEtherFcoeInterfaceStatsDroppedRxDelta':cfprEtherFcoeInterfaceStatsDroppedRxDelta,'cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg':cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg,'cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax':cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax,'cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin':cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin,'cfprEtherFcoeInterfaceStatsDroppedTx':cfprEtherFcoeInterfaceStatsDroppedTx,'cfprEtherFcoeInterfaceStatsDroppedTxDelta':cfprEtherFcoeInterfaceStatsDroppedTxDelta,'cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg':cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg,'cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax':cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax,'cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin':cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin,'cfprEtherFcoeInterfaceStatsErrorsRx':cfprEtherFcoeInterfaceStatsErrorsRx,'cfprEtherFcoeInterfaceStatsErrorsRxDelta':cfprEtherFcoeInterfaceStatsErrorsRxDelta,'cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg':cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg,'cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax':cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax,'cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin':cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin,'cfprEtherFcoeInterfaceStatsErrorsTx':cfprEtherFcoeInterfaceStatsErrorsTx,'cfprEtherFcoeInterfaceStatsErrorsTxDelta':cfprEtherFcoeInterfaceStatsErrorsTxDelta,'cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg':cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg,'cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax':cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax,'cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin':cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin,'cfprEtherFcoeInterfaceStatsIntervals':cfprEtherFcoeInterfaceStatsIntervals,'cfprEtherFcoeInterfaceStatsPacketsRx':cfprEtherFcoeInterfaceStatsPacketsRx,'cfprEtherFcoeInterfaceStatsPacketsRxDelta':cfprEtherFcoeInterfaceStatsPacketsRxDelta,'cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg':cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg,'cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax':cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax,'cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin':cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin,'cfprEtherFcoeInterfaceStatsPacketsTx':cfprEtherFcoeInterfaceStatsPacketsTx,'cfprEtherFcoeInterfaceStatsPacketsTxDelta':cfprEtherFcoeInterfaceStatsPacketsTxDelta,'cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg':cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg,'cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax':cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax,'cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin':cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin,'cfprEtherFcoeInterfaceStatsSuspect':cfprEtherFcoeInterfaceStatsSuspect,'cfprEtherFcoeInterfaceStatsThresholded':cfprEtherFcoeInterfaceStatsThresholded,'cfprEtherFcoeInterfaceStatsTimeCollected':cfprEtherFcoeInterfaceStatsTimeCollected,'cfprEtherFcoeInterfaceStatsUpdate':cfprEtherFcoeInterfaceStatsUpdate,'cfprEtherFcoeInterfaceStatsHistTable':cfprEtherFcoeInterfaceStatsHistTable,'cfprEtherFcoeInterfaceStatsHistEntry':cfprEtherFcoeInterfaceStatsHistEntry,_H:cfprEtherFcoeInterfaceStatsHistInstanceId,'cfprEtherFcoeInterfaceStatsHistDn':cfprEtherFcoeInterfaceStatsHistDn,'cfprEtherFcoeInterfaceStatsHistRn':cfprEtherFcoeInterfaceStatsHistRn,'cfprEtherFcoeInterfaceStatsHistBytesRx':cfprEtherFcoeInterfaceStatsHistBytesRx,'cfprEtherFcoeInterfaceStatsHistBytesRxDelta':cfprEtherFcoeInterfaceStatsHistBytesRxDelta,'cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg':cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax':cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax,'cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin':cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin,'cfprEtherFcoeInterfaceStatsHistBytesTx':cfprEtherFcoeInterfaceStatsHistBytesTx,'cfprEtherFcoeInterfaceStatsHistBytesTxDelta':cfprEtherFcoeInterfaceStatsHistBytesTxDelta,'cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg':cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax':cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax,'cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin':cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin,'cfprEtherFcoeInterfaceStatsHistDroppedRx':cfprEtherFcoeInterfaceStatsHistDroppedRx,'cfprEtherFcoeInterfaceStatsHistDroppedRxDelta':cfprEtherFcoeInterfaceStatsHistDroppedRxDelta,'cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg':cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax':cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax,'cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin':cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin,'cfprEtherFcoeInterfaceStatsHistDroppedTx':cfprEtherFcoeInterfaceStatsHistDroppedTx,'cfprEtherFcoeInterfaceStatsHistDroppedTxDelta':cfprEtherFcoeInterfaceStatsHistDroppedTxDelta,'cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg':cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax':cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax,'cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin':cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin,'cfprEtherFcoeInterfaceStatsHistErrorsRx':cfprEtherFcoeInterfaceStatsHistErrorsRx,'cfprEtherFcoeInterfaceStatsHistErrorsRxDelta':cfprEtherFcoeInterfaceStatsHistErrorsRxDelta,'cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg':cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax':cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax,'cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin':cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin,'cfprEtherFcoeInterfaceStatsHistErrorsTx':cfprEtherFcoeInterfaceStatsHistErrorsTx,'cfprEtherFcoeInterfaceStatsHistErrorsTxDelta':cfprEtherFcoeInterfaceStatsHistErrorsTxDelta,'cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg':cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax':cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax,'cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin':cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin,'cfprEtherFcoeInterfaceStatsHistId':cfprEtherFcoeInterfaceStatsHistId,'cfprEtherFcoeInterfaceStatsHistMostRecent':cfprEtherFcoeInterfaceStatsHistMostRecent,'cfprEtherFcoeInterfaceStatsHistPacketsRx':cfprEtherFcoeInterfaceStatsHistPacketsRx,'cfprEtherFcoeInterfaceStatsHistPacketsRxDelta':cfprEtherFcoeInterfaceStatsHistPacketsRxDelta,'cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg':cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax':cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax,'cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin':cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin,'cfprEtherFcoeInterfaceStatsHistPacketsTx':cfprEtherFcoeInterfaceStatsHistPacketsTx,'cfprEtherFcoeInterfaceStatsHistPacketsTxDelta':cfprEtherFcoeInterfaceStatsHistPacketsTxDelta,'cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg':cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg,'cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax':cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax,'cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin':cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin,'cfprEtherFcoeInterfaceStatsHistSuspect':cfprEtherFcoeInterfaceStatsHistSuspect,'cfprEtherFcoeInterfaceStatsHistThresholded':cfprEtherFcoeInterfaceStatsHistThresholded,'cfprEtherFcoeInterfaceStatsHistTimeCollected':cfprEtherFcoeInterfaceStatsHistTimeCollected,'cfprEtherLossStatsTable':cfprEtherLossStatsTable,'cfprEtherLossStatsEntry':cfprEtherLossStatsEntry,_I:cfprEtherLossStatsInstanceId,'cfprEtherLossStatsDn':cfprEtherLossStatsDn,'cfprEtherLossStatsRn':cfprEtherLossStatsRn,'cfprEtherLossStatsSQETest':cfprEtherLossStatsSQETest,'cfprEtherLossStatsSQETestDelta':cfprEtherLossStatsSQETestDelta,'cfprEtherLossStatsSQETestDeltaAvg':cfprEtherLossStatsSQETestDeltaAvg,'cfprEtherLossStatsSQETestDeltaMax':cfprEtherLossStatsSQETestDeltaMax,'cfprEtherLossStatsSQETestDeltaMin':cfprEtherLossStatsSQETestDeltaMin,'cfprEtherLossStatsCarrierSense':cfprEtherLossStatsCarrierSense,'cfprEtherLossStatsCarrierSenseDelta':cfprEtherLossStatsCarrierSenseDelta,'cfprEtherLossStatsCarrierSenseDeltaAvg':cfprEtherLossStatsCarrierSenseDeltaAvg,'cfprEtherLossStatsCarrierSenseDeltaMax':cfprEtherLossStatsCarrierSenseDeltaMax,'cfprEtherLossStatsCarrierSenseDeltaMin':cfprEtherLossStatsCarrierSenseDeltaMin,'cfprEtherLossStatsExcessCollision':cfprEtherLossStatsExcessCollision,'cfprEtherLossStatsExcessCollisionDelta':cfprEtherLossStatsExcessCollisionDelta,'cfprEtherLossStatsExcessCollisionDeltaAvg':cfprEtherLossStatsExcessCollisionDeltaAvg,'cfprEtherLossStatsExcessCollisionDeltaMax':cfprEtherLossStatsExcessCollisionDeltaMax,'cfprEtherLossStatsExcessCollisionDeltaMin':cfprEtherLossStatsExcessCollisionDeltaMin,'cfprEtherLossStatsGiants':cfprEtherLossStatsGiants,'cfprEtherLossStatsGiantsDelta':cfprEtherLossStatsGiantsDelta,'cfprEtherLossStatsGiantsDeltaAvg':cfprEtherLossStatsGiantsDeltaAvg,'cfprEtherLossStatsGiantsDeltaMax':cfprEtherLossStatsGiantsDeltaMax,'cfprEtherLossStatsGiantsDeltaMin':cfprEtherLossStatsGiantsDeltaMin,'cfprEtherLossStatsIntervals':cfprEtherLossStatsIntervals,'cfprEtherLossStatsLateCollision':cfprEtherLossStatsLateCollision,'cfprEtherLossStatsLateCollisionDelta':cfprEtherLossStatsLateCollisionDelta,'cfprEtherLossStatsLateCollisionDeltaAvg':cfprEtherLossStatsLateCollisionDeltaAvg,'cfprEtherLossStatsLateCollisionDeltaMax':cfprEtherLossStatsLateCollisionDeltaMax,'cfprEtherLossStatsLateCollisionDeltaMin':cfprEtherLossStatsLateCollisionDeltaMin,'cfprEtherLossStatsMultiCollision':cfprEtherLossStatsMultiCollision,'cfprEtherLossStatsMultiCollisionDelta':cfprEtherLossStatsMultiCollisionDelta,'cfprEtherLossStatsMultiCollisionDeltaAvg':cfprEtherLossStatsMultiCollisionDeltaAvg,'cfprEtherLossStatsMultiCollisionDeltaMax':cfprEtherLossStatsMultiCollisionDeltaMax,'cfprEtherLossStatsMultiCollisionDeltaMin':cfprEtherLossStatsMultiCollisionDeltaMin,'cfprEtherLossStatsSingleCollision':cfprEtherLossStatsSingleCollision,'cfprEtherLossStatsSingleCollisionDelta':cfprEtherLossStatsSingleCollisionDelta,'cfprEtherLossStatsSingleCollisionDeltaAvg':cfprEtherLossStatsSingleCollisionDeltaAvg,'cfprEtherLossStatsSingleCollisionDeltaMax':cfprEtherLossStatsSingleCollisionDeltaMax,'cfprEtherLossStatsSingleCollisionDeltaMin':cfprEtherLossStatsSingleCollisionDeltaMin,'cfprEtherLossStatsSuspect':cfprEtherLossStatsSuspect,'cfprEtherLossStatsSymbol':cfprEtherLossStatsSymbol,'cfprEtherLossStatsSymbolDelta':cfprEtherLossStatsSymbolDelta,'cfprEtherLossStatsSymbolDeltaAvg':cfprEtherLossStatsSymbolDeltaAvg,'cfprEtherLossStatsSymbolDeltaMax':cfprEtherLossStatsSymbolDeltaMax,'cfprEtherLossStatsSymbolDeltaMin':cfprEtherLossStatsSymbolDeltaMin,'cfprEtherLossStatsThresholded':cfprEtherLossStatsThresholded,'cfprEtherLossStatsTimeCollected':cfprEtherLossStatsTimeCollected,'cfprEtherLossStatsUpdate':cfprEtherLossStatsUpdate,'cfprEtherLossStatsHistTable':cfprEtherLossStatsHistTable,'cfprEtherLossStatsHistEntry':cfprEtherLossStatsHistEntry,_J:cfprEtherLossStatsHistInstanceId,'cfprEtherLossStatsHistDn':cfprEtherLossStatsHistDn,'cfprEtherLossStatsHistRn':cfprEtherLossStatsHistRn,'cfprEtherLossStatsHistSQETest':cfprEtherLossStatsHistSQETest,'cfprEtherLossStatsHistSQETestDelta':cfprEtherLossStatsHistSQETestDelta,'cfprEtherLossStatsHistSQETestDeltaAvg':cfprEtherLossStatsHistSQETestDeltaAvg,'cfprEtherLossStatsHistSQETestDeltaMax':cfprEtherLossStatsHistSQETestDeltaMax,'cfprEtherLossStatsHistSQETestDeltaMin':cfprEtherLossStatsHistSQETestDeltaMin,'cfprEtherLossStatsHistCarrierSense':cfprEtherLossStatsHistCarrierSense,'cfprEtherLossStatsHistCarrierSenseDelta':cfprEtherLossStatsHistCarrierSenseDelta,'cfprEtherLossStatsHistCarrierSenseDeltaAvg':cfprEtherLossStatsHistCarrierSenseDeltaAvg,'cfprEtherLossStatsHistCarrierSenseDeltaMax':cfprEtherLossStatsHistCarrierSenseDeltaMax,'cfprEtherLossStatsHistCarrierSenseDeltaMin':cfprEtherLossStatsHistCarrierSenseDeltaMin,'cfprEtherLossStatsHistExcessCollision':cfprEtherLossStatsHistExcessCollision,'cfprEtherLossStatsHistExcessCollisionDelta':cfprEtherLossStatsHistExcessCollisionDelta,'cfprEtherLossStatsHistExcessCollisionDeltaAvg':cfprEtherLossStatsHistExcessCollisionDeltaAvg,'cfprEtherLossStatsHistExcessCollisionDeltaMax':cfprEtherLossStatsHistExcessCollisionDeltaMax,'cfprEtherLossStatsHistExcessCollisionDeltaMin':cfprEtherLossStatsHistExcessCollisionDeltaMin,'cfprEtherLossStatsHistGiants':cfprEtherLossStatsHistGiants,'cfprEtherLossStatsHistGiantsDelta':cfprEtherLossStatsHistGiantsDelta,'cfprEtherLossStatsHistGiantsDeltaAvg':cfprEtherLossStatsHistGiantsDeltaAvg,'cfprEtherLossStatsHistGiantsDeltaMax':cfprEtherLossStatsHistGiantsDeltaMax,'cfprEtherLossStatsHistGiantsDeltaMin':cfprEtherLossStatsHistGiantsDeltaMin,'cfprEtherLossStatsHistId':cfprEtherLossStatsHistId,'cfprEtherLossStatsHistLateCollision':cfprEtherLossStatsHistLateCollision,'cfprEtherLossStatsHistLateCollisionDelta':cfprEtherLossStatsHistLateCollisionDelta,'cfprEtherLossStatsHistLateCollisionDeltaAvg':cfprEtherLossStatsHistLateCollisionDeltaAvg,'cfprEtherLossStatsHistLateCollisionDeltaMax':cfprEtherLossStatsHistLateCollisionDeltaMax,'cfprEtherLossStatsHistLateCollisionDeltaMin':cfprEtherLossStatsHistLateCollisionDeltaMin,'cfprEtherLossStatsHistMostRecent':cfprEtherLossStatsHistMostRecent,'cfprEtherLossStatsHistMultiCollision':cfprEtherLossStatsHistMultiCollision,'cfprEtherLossStatsHistMultiCollisionDelta':cfprEtherLossStatsHistMultiCollisionDelta,'cfprEtherLossStatsHistMultiCollisionDeltaAvg':cfprEtherLossStatsHistMultiCollisionDeltaAvg,'cfprEtherLossStatsHistMultiCollisionDeltaMax':cfprEtherLossStatsHistMultiCollisionDeltaMax,'cfprEtherLossStatsHistMultiCollisionDeltaMin':cfprEtherLossStatsHistMultiCollisionDeltaMin,'cfprEtherLossStatsHistSingleCollision':cfprEtherLossStatsHistSingleCollision,'cfprEtherLossStatsHistSingleCollisionDelta':cfprEtherLossStatsHistSingleCollisionDelta,'cfprEtherLossStatsHistSingleCollisionDeltaAvg':cfprEtherLossStatsHistSingleCollisionDeltaAvg,'cfprEtherLossStatsHistSingleCollisionDeltaMax':cfprEtherLossStatsHistSingleCollisionDeltaMax,'cfprEtherLossStatsHistSingleCollisionDeltaMin':cfprEtherLossStatsHistSingleCollisionDeltaMin,'cfprEtherLossStatsHistSuspect':cfprEtherLossStatsHistSuspect,'cfprEtherLossStatsHistSymbol':cfprEtherLossStatsHistSymbol,'cfprEtherLossStatsHistSymbolDelta':cfprEtherLossStatsHistSymbolDelta,'cfprEtherLossStatsHistSymbolDeltaAvg':cfprEtherLossStatsHistSymbolDeltaAvg,'cfprEtherLossStatsHistSymbolDeltaMax':cfprEtherLossStatsHistSymbolDeltaMax,'cfprEtherLossStatsHistSymbolDeltaMin':cfprEtherLossStatsHistSymbolDeltaMin,'cfprEtherLossStatsHistThresholded':cfprEtherLossStatsHistThresholded,'cfprEtherLossStatsHistTimeCollected':cfprEtherLossStatsHistTimeCollected,'cfprEtherNiErrStatsTable':cfprEtherNiErrStatsTable,'cfprEtherNiErrStatsEntry':cfprEtherNiErrStatsEntry,_K:cfprEtherNiErrStatsInstanceId,'cfprEtherNiErrStatsDn':cfprEtherNiErrStatsDn,'cfprEtherNiErrStatsRn':cfprEtherNiErrStatsRn,'cfprEtherNiErrStatsCrc':cfprEtherNiErrStatsCrc,'cfprEtherNiErrStatsCrcDelta':cfprEtherNiErrStatsCrcDelta,'cfprEtherNiErrStatsCrcDeltaAvg':cfprEtherNiErrStatsCrcDeltaAvg,'cfprEtherNiErrStatsCrcDeltaMax':cfprEtherNiErrStatsCrcDeltaMax,'cfprEtherNiErrStatsCrcDeltaMin':cfprEtherNiErrStatsCrcDeltaMin,'cfprEtherNiErrStatsFrameTx':cfprEtherNiErrStatsFrameTx,'cfprEtherNiErrStatsFrameTxDelta':cfprEtherNiErrStatsFrameTxDelta,'cfprEtherNiErrStatsFrameTxDeltaAvg':cfprEtherNiErrStatsFrameTxDeltaAvg,'cfprEtherNiErrStatsFrameTxDeltaMax':cfprEtherNiErrStatsFrameTxDeltaMax,'cfprEtherNiErrStatsFrameTxDeltaMin':cfprEtherNiErrStatsFrameTxDeltaMin,'cfprEtherNiErrStatsInRange':cfprEtherNiErrStatsInRange,'cfprEtherNiErrStatsInRangeDelta':cfprEtherNiErrStatsInRangeDelta,'cfprEtherNiErrStatsInRangeDeltaAvg':cfprEtherNiErrStatsInRangeDeltaAvg,'cfprEtherNiErrStatsInRangeDeltaMax':cfprEtherNiErrStatsInRangeDeltaMax,'cfprEtherNiErrStatsInRangeDeltaMin':cfprEtherNiErrStatsInRangeDeltaMin,'cfprEtherNiErrStatsIntervals':cfprEtherNiErrStatsIntervals,'cfprEtherNiErrStatsSuspect':cfprEtherNiErrStatsSuspect,'cfprEtherNiErrStatsThresholded':cfprEtherNiErrStatsThresholded,'cfprEtherNiErrStatsTimeCollected':cfprEtherNiErrStatsTimeCollected,'cfprEtherNiErrStatsTooLong':cfprEtherNiErrStatsTooLong,'cfprEtherNiErrStatsTooLongDelta':cfprEtherNiErrStatsTooLongDelta,'cfprEtherNiErrStatsTooLongDeltaAvg':cfprEtherNiErrStatsTooLongDeltaAvg,'cfprEtherNiErrStatsTooLongDeltaMax':cfprEtherNiErrStatsTooLongDeltaMax,'cfprEtherNiErrStatsTooLongDeltaMin':cfprEtherNiErrStatsTooLongDeltaMin,'cfprEtherNiErrStatsTooShort':cfprEtherNiErrStatsTooShort,'cfprEtherNiErrStatsTooShortDelta':cfprEtherNiErrStatsTooShortDelta,'cfprEtherNiErrStatsTooShortDeltaAvg':cfprEtherNiErrStatsTooShortDeltaAvg,'cfprEtherNiErrStatsTooShortDeltaMax':cfprEtherNiErrStatsTooShortDeltaMax,'cfprEtherNiErrStatsTooShortDeltaMin':cfprEtherNiErrStatsTooShortDeltaMin,'cfprEtherNiErrStatsUpdate':cfprEtherNiErrStatsUpdate,'cfprEtherNiErrStatsHistTable':cfprEtherNiErrStatsHistTable,'cfprEtherNiErrStatsHistEntry':cfprEtherNiErrStatsHistEntry,_L:cfprEtherNiErrStatsHistInstanceId,'cfprEtherNiErrStatsHistDn':cfprEtherNiErrStatsHistDn,'cfprEtherNiErrStatsHistRn':cfprEtherNiErrStatsHistRn,'cfprEtherNiErrStatsHistCrc':cfprEtherNiErrStatsHistCrc,'cfprEtherNiErrStatsHistCrcDelta':cfprEtherNiErrStatsHistCrcDelta,'cfprEtherNiErrStatsHistCrcDeltaAvg':cfprEtherNiErrStatsHistCrcDeltaAvg,'cfprEtherNiErrStatsHistCrcDeltaMax':cfprEtherNiErrStatsHistCrcDeltaMax,'cfprEtherNiErrStatsHistCrcDeltaMin':cfprEtherNiErrStatsHistCrcDeltaMin,'cfprEtherNiErrStatsHistFrameTx':cfprEtherNiErrStatsHistFrameTx,'cfprEtherNiErrStatsHistFrameTxDelta':cfprEtherNiErrStatsHistFrameTxDelta,'cfprEtherNiErrStatsHistFrameTxDeltaAvg':cfprEtherNiErrStatsHistFrameTxDeltaAvg,'cfprEtherNiErrStatsHistFrameTxDeltaMax':cfprEtherNiErrStatsHistFrameTxDeltaMax,'cfprEtherNiErrStatsHistFrameTxDeltaMin':cfprEtherNiErrStatsHistFrameTxDeltaMin,'cfprEtherNiErrStatsHistId':cfprEtherNiErrStatsHistId,'cfprEtherNiErrStatsHistInRange':cfprEtherNiErrStatsHistInRange,'cfprEtherNiErrStatsHistInRangeDelta':cfprEtherNiErrStatsHistInRangeDelta,'cfprEtherNiErrStatsHistInRangeDeltaAvg':cfprEtherNiErrStatsHistInRangeDeltaAvg,'cfprEtherNiErrStatsHistInRangeDeltaMax':cfprEtherNiErrStatsHistInRangeDeltaMax,'cfprEtherNiErrStatsHistInRangeDeltaMin':cfprEtherNiErrStatsHistInRangeDeltaMin,'cfprEtherNiErrStatsHistMostRecent':cfprEtherNiErrStatsHistMostRecent,'cfprEtherNiErrStatsHistSuspect':cfprEtherNiErrStatsHistSuspect,'cfprEtherNiErrStatsHistThresholded':cfprEtherNiErrStatsHistThresholded,'cfprEtherNiErrStatsHistTimeCollected':cfprEtherNiErrStatsHistTimeCollected,'cfprEtherNiErrStatsHistTooLong':cfprEtherNiErrStatsHistTooLong,'cfprEtherNiErrStatsHistTooLongDelta':cfprEtherNiErrStatsHistTooLongDelta,'cfprEtherNiErrStatsHistTooLongDeltaAvg':cfprEtherNiErrStatsHistTooLongDeltaAvg,'cfprEtherNiErrStatsHistTooLongDeltaMax':cfprEtherNiErrStatsHistTooLongDeltaMax,'cfprEtherNiErrStatsHistTooLongDeltaMin':cfprEtherNiErrStatsHistTooLongDeltaMin,'cfprEtherNiErrStatsHistTooShort':cfprEtherNiErrStatsHistTooShort,'cfprEtherNiErrStatsHistTooShortDelta':cfprEtherNiErrStatsHistTooShortDelta,'cfprEtherNiErrStatsHistTooShortDeltaAvg':cfprEtherNiErrStatsHistTooShortDeltaAvg,'cfprEtherNiErrStatsHistTooShortDeltaMax':cfprEtherNiErrStatsHistTooShortDeltaMax,'cfprEtherNiErrStatsHistTooShortDeltaMin':cfprEtherNiErrStatsHistTooShortDeltaMin,'cfprEtherNicIfConfigTable':cfprEtherNicIfConfigTable,'cfprEtherNicIfConfigEntry':cfprEtherNicIfConfigEntry,_M:cfprEtherNicIfConfigInstanceId,'cfprEtherNicIfConfigDn':cfprEtherNicIfConfigDn,'cfprEtherNicIfConfigRn':cfprEtherNicIfConfigRn,'cfprEtherPIoTable':cfprEtherPIoTable,'cfprEtherPIoEntry':cfprEtherPIoEntry,_N:cfprEtherPIoInstanceId,'cfprEtherPIoDn':cfprEtherPIoDn,'cfprEtherPIoRn':cfprEtherPIoRn,'cfprEtherPIoAdminState':cfprEtherPIoAdminState,'cfprEtherPIoAdminTransport':cfprEtherPIoAdminTransport,'cfprEtherPIoAggrPortId':cfprEtherPIoAggrPortId,'cfprEtherPIoChassisId':cfprEtherPIoChassisId,'cfprEtherPIoEncap':cfprEtherPIoEncap,'cfprEtherPIoEpDn':cfprEtherPIoEpDn,'cfprEtherPIoFltAggr':cfprEtherPIoFltAggr,'cfprEtherPIoFsmDescr':cfprEtherPIoFsmDescr,'cfprEtherPIoFsmPrev':cfprEtherPIoFsmPrev,'cfprEtherPIoFsmProgr':cfprEtherPIoFsmProgr,'cfprEtherPIoFsmRmtInvErrCode':cfprEtherPIoFsmRmtInvErrCode,'cfprEtherPIoFsmRmtInvErrDescr':cfprEtherPIoFsmRmtInvErrDescr,'cfprEtherPIoFsmRmtInvRslt':cfprEtherPIoFsmRmtInvRslt,'cfprEtherPIoFsmStageDescr':cfprEtherPIoFsmStageDescr,'cfprEtherPIoFsmStamp':cfprEtherPIoFsmStamp,'cfprEtherPIoFsmStatus':cfprEtherPIoFsmStatus,'cfprEtherPIoFsmTry':cfprEtherPIoFsmTry,'cfprEtherPIoIfRole':cfprEtherPIoIfRole,'cfprEtherPIoIfType':cfprEtherPIoIfType,'cfprEtherPIoIsPortChannelMember':cfprEtherPIoIsPortChannelMember,'cfprEtherPIoLc':cfprEtherPIoLc,'cfprEtherPIoLicGP':cfprEtherPIoLicGP,'cfprEtherPIoLicState':cfprEtherPIoLicState,'cfprEtherPIoLocale':cfprEtherPIoLocale,'cfprEtherPIoMac':cfprEtherPIoMac,'cfprEtherPIoMode':cfprEtherPIoMode,'cfprEtherPIoModel':cfprEtherPIoModel,'cfprEtherPIoName':cfprEtherPIoName,'cfprEtherPIoOperSpeed':cfprEtherPIoOperSpeed,'cfprEtherPIoOperState':cfprEtherPIoOperState,'cfprEtherPIoPeerAggrPortId':cfprEtherPIoPeerAggrPortId,'cfprEtherPIoPeerChassisId':cfprEtherPIoPeerChassisId,'cfprEtherPIoPeerDn':cfprEtherPIoPeerDn,'cfprEtherPIoPeerPortId':cfprEtherPIoPeerPortId,'cfprEtherPIoPeerSlotId':cfprEtherPIoPeerSlotId,'cfprEtherPIoPortId':cfprEtherPIoPortId,'cfprEtherPIoRevision':cfprEtherPIoRevision,'cfprEtherPIoSerial':cfprEtherPIoSerial,'cfprEtherPIoSlotId':cfprEtherPIoSlotId,'cfprEtherPIoStateQual':cfprEtherPIoStateQual,'cfprEtherPIoSwitchId':cfprEtherPIoSwitchId,'cfprEtherPIoTransport':cfprEtherPIoTransport,'cfprEtherPIoTs':cfprEtherPIoTs,'cfprEtherPIoType':cfprEtherPIoType,'cfprEtherPIoUnifiedPort':cfprEtherPIoUnifiedPort,'cfprEtherPIoUsrLbl':cfprEtherPIoUsrLbl,'cfprEtherPIoVendor':cfprEtherPIoVendor,'cfprEtherPIoXcvrType':cfprEtherPIoXcvrType,'cfprEtherPIoFtwPhyDn':cfprEtherPIoFtwPhyDn,'cfprEtherPIoOperDuplex':cfprEtherPIoOperDuplex,'cfprEtherPIoEndPointTable':cfprEtherPIoEndPointTable,'cfprEtherPIoEndPointEntry':cfprEtherPIoEndPointEntry,_O:cfprEtherPIoEndPointInstanceId,'cfprEtherPIoEndPointDn':cfprEtherPIoEndPointDn,'cfprEtherPIoEndPointRn':cfprEtherPIoEndPointRn,'cfprEtherPIoEndPointEndPointDn':cfprEtherPIoEndPointEndPointDn,'cfprEtherPIoEndPointEpCloudType':cfprEtherPIoEndPointEpCloudType,'cfprEtherPIoEndPointUsrLbl':cfprEtherPIoEndPointUsrLbl,'cfprEtherPIoFsmTable':cfprEtherPIoFsmTable,'cfprEtherPIoFsmEntry':cfprEtherPIoFsmEntry,_P:cfprEtherPIoFsmInstanceId,'cfprEtherPIoFsmDn':cfprEtherPIoFsmDn,'cfprEtherPIoFsmRn':cfprEtherPIoFsmRn,'cfprEtherPIoFsmCompletionTime':cfprEtherPIoFsmCompletionTime,'cfprEtherPIoFsmCurrentFsm':cfprEtherPIoFsmCurrentFsm,'cfprEtherPIoFsmDescrData':cfprEtherPIoFsmDescrData,'cfprEtherPIoFsmFsmStatus':cfprEtherPIoFsmFsmStatus,'cfprEtherPIoFsmProgress':cfprEtherPIoFsmProgress,'cfprEtherPIoFsmRmtErrCode':cfprEtherPIoFsmRmtErrCode,'cfprEtherPIoFsmRmtErrDescr':cfprEtherPIoFsmRmtErrDescr,'cfprEtherPIoFsmRmtRslt':cfprEtherPIoFsmRmtRslt,'cfprEtherPIoFsmStageTable':cfprEtherPIoFsmStageTable,'cfprEtherPIoFsmStageEntry':cfprEtherPIoFsmStageEntry,_Q:cfprEtherPIoFsmStageInstanceId,'cfprEtherPIoFsmStageDn':cfprEtherPIoFsmStageDn,'cfprEtherPIoFsmStageRn':cfprEtherPIoFsmStageRn,'cfprEtherPIoFsmStageDescrData':cfprEtherPIoFsmStageDescrData,'cfprEtherPIoFsmStageLastUpdateTime':cfprEtherPIoFsmStageLastUpdateTime,'cfprEtherPIoFsmStageName':cfprEtherPIoFsmStageName,'cfprEtherPIoFsmStageOrder':cfprEtherPIoFsmStageOrder,'cfprEtherPIoFsmStageRetry':cfprEtherPIoFsmStageRetry,'cfprEtherPIoFsmStageStageStatus':cfprEtherPIoFsmStageStageStatus,'cfprEtherPauseStatsTable':cfprEtherPauseStatsTable,'cfprEtherPauseStatsEntry':cfprEtherPauseStatsEntry,_R:cfprEtherPauseStatsInstanceId,'cfprEtherPauseStatsDn':cfprEtherPauseStatsDn,'cfprEtherPauseStatsRn':cfprEtherPauseStatsRn,'cfprEtherPauseStatsIntervals':cfprEtherPauseStatsIntervals,'cfprEtherPauseStatsRecvPause':cfprEtherPauseStatsRecvPause,'cfprEtherPauseStatsRecvPauseDelta':cfprEtherPauseStatsRecvPauseDelta,'cfprEtherPauseStatsRecvPauseDeltaAvg':cfprEtherPauseStatsRecvPauseDeltaAvg,'cfprEtherPauseStatsRecvPauseDeltaMax':cfprEtherPauseStatsRecvPauseDeltaMax,'cfprEtherPauseStatsRecvPauseDeltaMin':cfprEtherPauseStatsRecvPauseDeltaMin,'cfprEtherPauseStatsResets':cfprEtherPauseStatsResets,'cfprEtherPauseStatsResetsDelta':cfprEtherPauseStatsResetsDelta,'cfprEtherPauseStatsResetsDeltaAvg':cfprEtherPauseStatsResetsDeltaAvg,'cfprEtherPauseStatsResetsDeltaMax':cfprEtherPauseStatsResetsDeltaMax,'cfprEtherPauseStatsResetsDeltaMin':cfprEtherPauseStatsResetsDeltaMin,'cfprEtherPauseStatsSuspect':cfprEtherPauseStatsSuspect,'cfprEtherPauseStatsThresholded':cfprEtherPauseStatsThresholded,'cfprEtherPauseStatsTimeCollected':cfprEtherPauseStatsTimeCollected,'cfprEtherPauseStatsUpdate':cfprEtherPauseStatsUpdate,'cfprEtherPauseStatsXmitPause':cfprEtherPauseStatsXmitPause,'cfprEtherPauseStatsXmitPauseDelta':cfprEtherPauseStatsXmitPauseDelta,'cfprEtherPauseStatsXmitPauseDeltaAvg':cfprEtherPauseStatsXmitPauseDeltaAvg,'cfprEtherPauseStatsXmitPauseDeltaMax':cfprEtherPauseStatsXmitPauseDeltaMax,'cfprEtherPauseStatsXmitPauseDeltaMin':cfprEtherPauseStatsXmitPauseDeltaMin,'cfprEtherPauseStatsHistTable':cfprEtherPauseStatsHistTable,'cfprEtherPauseStatsHistEntry':cfprEtherPauseStatsHistEntry,_S:cfprEtherPauseStatsHistInstanceId,'cfprEtherPauseStatsHistDn':cfprEtherPauseStatsHistDn,'cfprEtherPauseStatsHistRn':cfprEtherPauseStatsHistRn,'cfprEtherPauseStatsHistId':cfprEtherPauseStatsHistId,'cfprEtherPauseStatsHistMostRecent':cfprEtherPauseStatsHistMostRecent,'cfprEtherPauseStatsHistRecvPause':cfprEtherPauseStatsHistRecvPause,'cfprEtherPauseStatsHistRecvPauseDelta':cfprEtherPauseStatsHistRecvPauseDelta,'cfprEtherPauseStatsHistRecvPauseDeltaAvg':cfprEtherPauseStatsHistRecvPauseDeltaAvg,'cfprEtherPauseStatsHistRecvPauseDeltaMax':cfprEtherPauseStatsHistRecvPauseDeltaMax,'cfprEtherPauseStatsHistRecvPauseDeltaMin':cfprEtherPauseStatsHistRecvPauseDeltaMin,'cfprEtherPauseStatsHistResets':cfprEtherPauseStatsHistResets,'cfprEtherPauseStatsHistResetsDelta':cfprEtherPauseStatsHistResetsDelta,'cfprEtherPauseStatsHistResetsDeltaAvg':cfprEtherPauseStatsHistResetsDeltaAvg,'cfprEtherPauseStatsHistResetsDeltaMax':cfprEtherPauseStatsHistResetsDeltaMax,'cfprEtherPauseStatsHistResetsDeltaMin':cfprEtherPauseStatsHistResetsDeltaMin,'cfprEtherPauseStatsHistSuspect':cfprEtherPauseStatsHistSuspect,'cfprEtherPauseStatsHistThresholded':cfprEtherPauseStatsHistThresholded,'cfprEtherPauseStatsHistTimeCollected':cfprEtherPauseStatsHistTimeCollected,'cfprEtherPauseStatsHistXmitPause':cfprEtherPauseStatsHistXmitPause,'cfprEtherPauseStatsHistXmitPauseDelta':cfprEtherPauseStatsHistXmitPauseDelta,'cfprEtherPauseStatsHistXmitPauseDeltaAvg':cfprEtherPauseStatsHistXmitPauseDeltaAvg,'cfprEtherPauseStatsHistXmitPauseDeltaMax':cfprEtherPauseStatsHistXmitPauseDeltaMax,'cfprEtherPauseStatsHistXmitPauseDeltaMin':cfprEtherPauseStatsHistXmitPauseDeltaMin,'cfprEtherPortChanIdElemTable':cfprEtherPortChanIdElemTable,'cfprEtherPortChanIdElemEntry':cfprEtherPortChanIdElemEntry,_T:cfprEtherPortChanIdElemInstanceId,'cfprEtherPortChanIdElemDn':cfprEtherPortChanIdElemDn,'cfprEtherPortChanIdElemRn':cfprEtherPortChanIdElemRn,'cfprEtherPortChanIdElemId':cfprEtherPortChanIdElemId,'cfprEtherPortChanIdUniverseTable':cfprEtherPortChanIdUniverseTable,'cfprEtherPortChanIdUniverseEntry':cfprEtherPortChanIdUniverseEntry,_U:cfprEtherPortChanIdUniverseInstanceId,'cfprEtherPortChanIdUniverseDn':cfprEtherPortChanIdUniverseDn,'cfprEtherPortChanIdUniverseRn':cfprEtherPortChanIdUniverseRn,'cfprEtherRxStatsTable':cfprEtherRxStatsTable,'cfprEtherRxStatsEntry':cfprEtherRxStatsEntry,_V:cfprEtherRxStatsInstanceId,'cfprEtherRxStatsDn':cfprEtherRxStatsDn,'cfprEtherRxStatsRn':cfprEtherRxStatsRn,'cfprEtherRxStatsBroadcastPackets':cfprEtherRxStatsBroadcastPackets,'cfprEtherRxStatsBroadcastPacketsDelta':cfprEtherRxStatsBroadcastPacketsDelta,'cfprEtherRxStatsBroadcastPacketsDeltaAvg':cfprEtherRxStatsBroadcastPacketsDeltaAvg,'cfprEtherRxStatsBroadcastPacketsDeltaMax':cfprEtherRxStatsBroadcastPacketsDeltaMax,'cfprEtherRxStatsBroadcastPacketsDeltaMin':cfprEtherRxStatsBroadcastPacketsDeltaMin,'cfprEtherRxStatsIntervals':cfprEtherRxStatsIntervals,'cfprEtherRxStatsJumboPackets':cfprEtherRxStatsJumboPackets,'cfprEtherRxStatsJumboPacketsDelta':cfprEtherRxStatsJumboPacketsDelta,'cfprEtherRxStatsJumboPacketsDeltaAvg':cfprEtherRxStatsJumboPacketsDeltaAvg,'cfprEtherRxStatsJumboPacketsDeltaMax':cfprEtherRxStatsJumboPacketsDeltaMax,'cfprEtherRxStatsJumboPacketsDeltaMin':cfprEtherRxStatsJumboPacketsDeltaMin,'cfprEtherRxStatsMulticastPackets':cfprEtherRxStatsMulticastPackets,'cfprEtherRxStatsMulticastPacketsDelta':cfprEtherRxStatsMulticastPacketsDelta,'cfprEtherRxStatsMulticastPacketsDeltaAvg':cfprEtherRxStatsMulticastPacketsDeltaAvg,'cfprEtherRxStatsMulticastPacketsDeltaMax':cfprEtherRxStatsMulticastPacketsDeltaMax,'cfprEtherRxStatsMulticastPacketsDeltaMin':cfprEtherRxStatsMulticastPacketsDeltaMin,'cfprEtherRxStatsSuspect':cfprEtherRxStatsSuspect,'cfprEtherRxStatsThresholded':cfprEtherRxStatsThresholded,'cfprEtherRxStatsTimeCollected':cfprEtherRxStatsTimeCollected,'cfprEtherRxStatsTotalBytes':cfprEtherRxStatsTotalBytes,'cfprEtherRxStatsTotalBytesDelta':cfprEtherRxStatsTotalBytesDelta,'cfprEtherRxStatsTotalBytesDeltaAvg':cfprEtherRxStatsTotalBytesDeltaAvg,'cfprEtherRxStatsTotalBytesDeltaMax':cfprEtherRxStatsTotalBytesDeltaMax,'cfprEtherRxStatsTotalBytesDeltaMin':cfprEtherRxStatsTotalBytesDeltaMin,'cfprEtherRxStatsTotalPackets':cfprEtherRxStatsTotalPackets,'cfprEtherRxStatsTotalPacketsDelta':cfprEtherRxStatsTotalPacketsDelta,'cfprEtherRxStatsTotalPacketsDeltaAvg':cfprEtherRxStatsTotalPacketsDeltaAvg,'cfprEtherRxStatsTotalPacketsDeltaMax':cfprEtherRxStatsTotalPacketsDeltaMax,'cfprEtherRxStatsTotalPacketsDeltaMin':cfprEtherRxStatsTotalPacketsDeltaMin,'cfprEtherRxStatsUnicastPackets':cfprEtherRxStatsUnicastPackets,'cfprEtherRxStatsUnicastPacketsDelta':cfprEtherRxStatsUnicastPacketsDelta,'cfprEtherRxStatsUnicastPacketsDeltaAvg':cfprEtherRxStatsUnicastPacketsDeltaAvg,'cfprEtherRxStatsUnicastPacketsDeltaMax':cfprEtherRxStatsUnicastPacketsDeltaMax,'cfprEtherRxStatsUnicastPacketsDeltaMin':cfprEtherRxStatsUnicastPacketsDeltaMin,'cfprEtherRxStatsUpdate':cfprEtherRxStatsUpdate,'cfprEtherRxStatsHistTable':cfprEtherRxStatsHistTable,'cfprEtherRxStatsHistEntry':cfprEtherRxStatsHistEntry,_W:cfprEtherRxStatsHistInstanceId,'cfprEtherRxStatsHistDn':cfprEtherRxStatsHistDn,'cfprEtherRxStatsHistRn':cfprEtherRxStatsHistRn,'cfprEtherRxStatsHistBroadcastPackets':cfprEtherRxStatsHistBroadcastPackets,'cfprEtherRxStatsHistBroadcastPacketsDelta':cfprEtherRxStatsHistBroadcastPacketsDelta,'cfprEtherRxStatsHistBroadcastPacketsDeltaAvg':cfprEtherRxStatsHistBroadcastPacketsDeltaAvg,'cfprEtherRxStatsHistBroadcastPacketsDeltaMax':cfprEtherRxStatsHistBroadcastPacketsDeltaMax,'cfprEtherRxStatsHistBroadcastPacketsDeltaMin':cfprEtherRxStatsHistBroadcastPacketsDeltaMin,'cfprEtherRxStatsHistId':cfprEtherRxStatsHistId,'cfprEtherRxStatsHistJumboPackets':cfprEtherRxStatsHistJumboPackets,'cfprEtherRxStatsHistJumboPacketsDelta':cfprEtherRxStatsHistJumboPacketsDelta,'cfprEtherRxStatsHistJumboPacketsDeltaAvg':cfprEtherRxStatsHistJumboPacketsDeltaAvg,'cfprEtherRxStatsHistJumboPacketsDeltaMax':cfprEtherRxStatsHistJumboPacketsDeltaMax,'cfprEtherRxStatsHistJumboPacketsDeltaMin':cfprEtherRxStatsHistJumboPacketsDeltaMin,'cfprEtherRxStatsHistMostRecent':cfprEtherRxStatsHistMostRecent,'cfprEtherRxStatsHistMulticastPackets':cfprEtherRxStatsHistMulticastPackets,'cfprEtherRxStatsHistMulticastPacketsDelta':cfprEtherRxStatsHistMulticastPacketsDelta,'cfprEtherRxStatsHistMulticastPacketsDeltaAvg':cfprEtherRxStatsHistMulticastPacketsDeltaAvg,'cfprEtherRxStatsHistMulticastPacketsDeltaMax':cfprEtherRxStatsHistMulticastPacketsDeltaMax,'cfprEtherRxStatsHistMulticastPacketsDeltaMin':cfprEtherRxStatsHistMulticastPacketsDeltaMin,'cfprEtherRxStatsHistSuspect':cfprEtherRxStatsHistSuspect,'cfprEtherRxStatsHistThresholded':cfprEtherRxStatsHistThresholded,'cfprEtherRxStatsHistTimeCollected':cfprEtherRxStatsHistTimeCollected,'cfprEtherRxStatsHistTotalBytes':cfprEtherRxStatsHistTotalBytes,'cfprEtherRxStatsHistTotalBytesDelta':cfprEtherRxStatsHistTotalBytesDelta,'cfprEtherRxStatsHistTotalBytesDeltaAvg':cfprEtherRxStatsHistTotalBytesDeltaAvg,'cfprEtherRxStatsHistTotalBytesDeltaMax':cfprEtherRxStatsHistTotalBytesDeltaMax,'cfprEtherRxStatsHistTotalBytesDeltaMin':cfprEtherRxStatsHistTotalBytesDeltaMin,'cfprEtherRxStatsHistTotalPackets':cfprEtherRxStatsHistTotalPackets,'cfprEtherRxStatsHistTotalPacketsDelta':cfprEtherRxStatsHistTotalPacketsDelta,'cfprEtherRxStatsHistTotalPacketsDeltaAvg':cfprEtherRxStatsHistTotalPacketsDeltaAvg,'cfprEtherRxStatsHistTotalPacketsDeltaMax':cfprEtherRxStatsHistTotalPacketsDeltaMax,'cfprEtherRxStatsHistTotalPacketsDeltaMin':cfprEtherRxStatsHistTotalPacketsDeltaMin,'cfprEtherRxStatsHistUnicastPackets':cfprEtherRxStatsHistUnicastPackets,'cfprEtherRxStatsHistUnicastPacketsDelta':cfprEtherRxStatsHistUnicastPacketsDelta,'cfprEtherRxStatsHistUnicastPacketsDeltaAvg':cfprEtherRxStatsHistUnicastPacketsDeltaAvg,'cfprEtherRxStatsHistUnicastPacketsDeltaMax':cfprEtherRxStatsHistUnicastPacketsDeltaMax,'cfprEtherRxStatsHistUnicastPacketsDeltaMin':cfprEtherRxStatsHistUnicastPacketsDeltaMin,'cfprEtherServerIntFIoTable':cfprEtherServerIntFIoTable,'cfprEtherServerIntFIoEntry':cfprEtherServerIntFIoEntry,_X:cfprEtherServerIntFIoInstanceId,'cfprEtherServerIntFIoDn':cfprEtherServerIntFIoDn,'cfprEtherServerIntFIoRn':cfprEtherServerIntFIoRn,'cfprEtherServerIntFIoAdminSpeed':cfprEtherServerIntFIoAdminSpeed,'cfprEtherServerIntFIoAdminState':cfprEtherServerIntFIoAdminState,'cfprEtherServerIntFIoAggrPortId':cfprEtherServerIntFIoAggrPortId,'cfprEtherServerIntFIoChassisId':cfprEtherServerIntFIoChassisId,'cfprEtherServerIntFIoEncap':cfprEtherServerIntFIoEncap,'cfprEtherServerIntFIoEpDn':cfprEtherServerIntFIoEpDn,'cfprEtherServerIntFIoFltAggr':cfprEtherServerIntFIoFltAggr,'cfprEtherServerIntFIoFsmDescr':cfprEtherServerIntFIoFsmDescr,'cfprEtherServerIntFIoFsmPrev':cfprEtherServerIntFIoFsmPrev,'cfprEtherServerIntFIoFsmProgr':cfprEtherServerIntFIoFsmProgr,'cfprEtherServerIntFIoFsmRmtInvErrCode':cfprEtherServerIntFIoFsmRmtInvErrCode,'cfprEtherServerIntFIoFsmRmtInvErrDescr':cfprEtherServerIntFIoFsmRmtInvErrDescr,'cfprEtherServerIntFIoFsmRmtInvRslt':cfprEtherServerIntFIoFsmRmtInvRslt,'cfprEtherServerIntFIoFsmStageDescr':cfprEtherServerIntFIoFsmStageDescr,'cfprEtherServerIntFIoFsmStamp':cfprEtherServerIntFIoFsmStamp,'cfprEtherServerIntFIoFsmStatus':cfprEtherServerIntFIoFsmStatus,'cfprEtherServerIntFIoFsmTry':cfprEtherServerIntFIoFsmTry,'cfprEtherServerIntFIoIfRole':cfprEtherServerIntFIoIfRole,'cfprEtherServerIntFIoIfType':cfprEtherServerIntFIoIfType,'cfprEtherServerIntFIoLocale':cfprEtherServerIntFIoLocale,'cfprEtherServerIntFIoMac':cfprEtherServerIntFIoMac,'cfprEtherServerIntFIoMode':cfprEtherServerIntFIoMode,'cfprEtherServerIntFIoModel':cfprEtherServerIntFIoModel,'cfprEtherServerIntFIoName':cfprEtherServerIntFIoName,'cfprEtherServerIntFIoNsSize':cfprEtherServerIntFIoNsSize,'cfprEtherServerIntFIoOperBorderAggrPortId':cfprEtherServerIntFIoOperBorderAggrPortId,'cfprEtherServerIntFIoOperBorderPortId':cfprEtherServerIntFIoOperBorderPortId,'cfprEtherServerIntFIoOperBorderSlotId':cfprEtherServerIntFIoOperBorderSlotId,'cfprEtherServerIntFIoOperState':cfprEtherServerIntFIoOperState,'cfprEtherServerIntFIoPeerAggrPortId':cfprEtherServerIntFIoPeerAggrPortId,'cfprEtherServerIntFIoPeerChassisId':cfprEtherServerIntFIoPeerChassisId,'cfprEtherServerIntFIoPeerDn':cfprEtherServerIntFIoPeerDn,'cfprEtherServerIntFIoPeerEncap':cfprEtherServerIntFIoPeerEncap,'cfprEtherServerIntFIoPeerPortId':cfprEtherServerIntFIoPeerPortId,'cfprEtherServerIntFIoPeerSlotId':cfprEtherServerIntFIoPeerSlotId,'cfprEtherServerIntFIoPortId':cfprEtherServerIntFIoPortId,'cfprEtherServerIntFIoRevision':cfprEtherServerIntFIoRevision,'cfprEtherServerIntFIoSerial':cfprEtherServerIntFIoSerial,'cfprEtherServerIntFIoSlotId':cfprEtherServerIntFIoSlotId,'cfprEtherServerIntFIoStateQual':cfprEtherServerIntFIoStateQual,'cfprEtherServerIntFIoSwitchId':cfprEtherServerIntFIoSwitchId,'cfprEtherServerIntFIoTransport':cfprEtherServerIntFIoTransport,'cfprEtherServerIntFIoTs':cfprEtherServerIntFIoTs,'cfprEtherServerIntFIoType':cfprEtherServerIntFIoType,'cfprEtherServerIntFIoVendor':cfprEtherServerIntFIoVendor,'cfprEtherServerIntFIoXcvrType':cfprEtherServerIntFIoXcvrType,'cfprEtherServerIntFIoFsmTable':cfprEtherServerIntFIoFsmTable,'cfprEtherServerIntFIoFsmEntry':cfprEtherServerIntFIoFsmEntry,_Y:cfprEtherServerIntFIoFsmInstanceId,'cfprEtherServerIntFIoFsmDn':cfprEtherServerIntFIoFsmDn,'cfprEtherServerIntFIoFsmRn':cfprEtherServerIntFIoFsmRn,'cfprEtherServerIntFIoFsmCompletionTime':cfprEtherServerIntFIoFsmCompletionTime,'cfprEtherServerIntFIoFsmCurrentFsm':cfprEtherServerIntFIoFsmCurrentFsm,'cfprEtherServerIntFIoFsmDescrData':cfprEtherServerIntFIoFsmDescrData,'cfprEtherServerIntFIoFsmFsmStatus':cfprEtherServerIntFIoFsmFsmStatus,'cfprEtherServerIntFIoFsmProgress':cfprEtherServerIntFIoFsmProgress,'cfprEtherServerIntFIoFsmRmtErrCode':cfprEtherServerIntFIoFsmRmtErrCode,'cfprEtherServerIntFIoFsmRmtErrDescr':cfprEtherServerIntFIoFsmRmtErrDescr,'cfprEtherServerIntFIoFsmRmtRslt':cfprEtherServerIntFIoFsmRmtRslt,'cfprEtherServerIntFIoFsmStageTable':cfprEtherServerIntFIoFsmStageTable,'cfprEtherServerIntFIoFsmStageEntry':cfprEtherServerIntFIoFsmStageEntry,_Z:cfprEtherServerIntFIoFsmStageInstanceId,'cfprEtherServerIntFIoFsmStageDn':cfprEtherServerIntFIoFsmStageDn,'cfprEtherServerIntFIoFsmStageRn':cfprEtherServerIntFIoFsmStageRn,'cfprEtherServerIntFIoFsmStageDescrData':cfprEtherServerIntFIoFsmStageDescrData,'cfprEtherServerIntFIoFsmStageLastUpdateTime':cfprEtherServerIntFIoFsmStageLastUpdateTime,'cfprEtherServerIntFIoFsmStageName':cfprEtherServerIntFIoFsmStageName,'cfprEtherServerIntFIoFsmStageOrder':cfprEtherServerIntFIoFsmStageOrder,'cfprEtherServerIntFIoFsmStageRetry':cfprEtherServerIntFIoFsmStageRetry,'cfprEtherServerIntFIoFsmStageStageStatus':cfprEtherServerIntFIoFsmStageStageStatus,'cfprEtherServerIntFIoFsmTaskTable':cfprEtherServerIntFIoFsmTaskTable,'cfprEtherServerIntFIoFsmTaskEntry':cfprEtherServerIntFIoFsmTaskEntry,_a:cfprEtherServerIntFIoFsmTaskInstanceId,'cfprEtherServerIntFIoFsmTaskDn':cfprEtherServerIntFIoFsmTaskDn,'cfprEtherServerIntFIoFsmTaskRn':cfprEtherServerIntFIoFsmTaskRn,'cfprEtherServerIntFIoFsmTaskCompletion':cfprEtherServerIntFIoFsmTaskCompletion,'cfprEtherServerIntFIoFsmTaskFlags':cfprEtherServerIntFIoFsmTaskFlags,'cfprEtherServerIntFIoFsmTaskItem':cfprEtherServerIntFIoFsmTaskItem,'cfprEtherServerIntFIoFsmTaskSeqId':cfprEtherServerIntFIoFsmTaskSeqId,'cfprEtherServerIntFIoPcTable':cfprEtherServerIntFIoPcTable,'cfprEtherServerIntFIoPcEntry':cfprEtherServerIntFIoPcEntry,_b:cfprEtherServerIntFIoPcInstanceId,'cfprEtherServerIntFIoPcDn':cfprEtherServerIntFIoPcDn,'cfprEtherServerIntFIoPcRn':cfprEtherServerIntFIoPcRn,'cfprEtherServerIntFIoPcChassisId':cfprEtherServerIntFIoPcChassisId,'cfprEtherServerIntFIoPcEpDn':cfprEtherServerIntFIoPcEpDn,'cfprEtherServerIntFIoPcFltAggr':cfprEtherServerIntFIoPcFltAggr,'cfprEtherServerIntFIoPcIfRole':cfprEtherServerIntFIoPcIfRole,'cfprEtherServerIntFIoPcIfType':cfprEtherServerIntFIoPcIfType,'cfprEtherServerIntFIoPcLocale':cfprEtherServerIntFIoPcLocale,'cfprEtherServerIntFIoPcName':cfprEtherServerIntFIoPcName,'cfprEtherServerIntFIoPcOperSpeed':cfprEtherServerIntFIoPcOperSpeed,'cfprEtherServerIntFIoPcOperState':cfprEtherServerIntFIoPcOperState,'cfprEtherServerIntFIoPcPeerDn':cfprEtherServerIntFIoPcPeerDn,'cfprEtherServerIntFIoPcPortId':cfprEtherServerIntFIoPcPortId,'cfprEtherServerIntFIoPcStateQual':cfprEtherServerIntFIoPcStateQual,'cfprEtherServerIntFIoPcSwitchId':cfprEtherServerIntFIoPcSwitchId,'cfprEtherServerIntFIoPcTransport':cfprEtherServerIntFIoPcTransport,'cfprEtherServerIntFIoPcType':cfprEtherServerIntFIoPcType,'cfprEtherServerIntFIoPcEpTable':cfprEtherServerIntFIoPcEpTable,'cfprEtherServerIntFIoPcEpEntry':cfprEtherServerIntFIoPcEpEntry,_c:cfprEtherServerIntFIoPcEpInstanceId,'cfprEtherServerIntFIoPcEpDnData':cfprEtherServerIntFIoPcEpDnData,'cfprEtherServerIntFIoPcEpRn':cfprEtherServerIntFIoPcEpRn,'cfprEtherServerIntFIoPcEpAdminState':cfprEtherServerIntFIoPcEpAdminState,'cfprEtherServerIntFIoPcEpAggrPortId':cfprEtherServerIntFIoPcEpAggrPortId,'cfprEtherServerIntFIoPcEpChassisId':cfprEtherServerIntFIoPcEpChassisId,'cfprEtherServerIntFIoPcEpEpDn':cfprEtherServerIntFIoPcEpEpDn,'cfprEtherServerIntFIoPcEpIfRole':cfprEtherServerIntFIoPcEpIfRole,'cfprEtherServerIntFIoPcEpIfType':cfprEtherServerIntFIoPcEpIfType,'cfprEtherServerIntFIoPcEpLocale':cfprEtherServerIntFIoPcEpLocale,'cfprEtherServerIntFIoPcEpMembership':cfprEtherServerIntFIoPcEpMembership,'cfprEtherServerIntFIoPcEpName':cfprEtherServerIntFIoPcEpName,'cfprEtherServerIntFIoPcEpPeerAggrPortId':cfprEtherServerIntFIoPcEpPeerAggrPortId,'cfprEtherServerIntFIoPcEpPeerChassisId':cfprEtherServerIntFIoPcEpPeerChassisId,'cfprEtherServerIntFIoPcEpPeerDn':cfprEtherServerIntFIoPcEpPeerDn,'cfprEtherServerIntFIoPcEpPeerPortId':cfprEtherServerIntFIoPcEpPeerPortId,'cfprEtherServerIntFIoPcEpPeerSlotId':cfprEtherServerIntFIoPcEpPeerSlotId,'cfprEtherServerIntFIoPcEpPortId':cfprEtherServerIntFIoPcEpPortId,'cfprEtherServerIntFIoPcEpSlotId':cfprEtherServerIntFIoPcEpSlotId,'cfprEtherServerIntFIoPcEpSwitchId':cfprEtherServerIntFIoPcEpSwitchId,'cfprEtherServerIntFIoPcEpTransport':cfprEtherServerIntFIoPcEpTransport,'cfprEtherServerIntFIoPcEpType':cfprEtherServerIntFIoPcEpType,'cfprEtherSwIfConfigTable':cfprEtherSwIfConfigTable,'cfprEtherSwIfConfigEntry':cfprEtherSwIfConfigEntry,_d:cfprEtherSwIfConfigInstanceId,'cfprEtherSwIfConfigDn':cfprEtherSwIfConfigDn,'cfprEtherSwIfConfigRn':cfprEtherSwIfConfigRn,'cfprEtherSwitchIntFIoTable':cfprEtherSwitchIntFIoTable,'cfprEtherSwitchIntFIoEntry':cfprEtherSwitchIntFIoEntry,_e:cfprEtherSwitchIntFIoInstanceId,'cfprEtherSwitchIntFIoDn':cfprEtherSwitchIntFIoDn,'cfprEtherSwitchIntFIoRn':cfprEtherSwitchIntFIoRn,'cfprEtherSwitchIntFIoAck':cfprEtherSwitchIntFIoAck,'cfprEtherSwitchIntFIoAdminState':cfprEtherSwitchIntFIoAdminState,'cfprEtherSwitchIntFIoAggrPortId':cfprEtherSwitchIntFIoAggrPortId,'cfprEtherSwitchIntFIoChassisId':cfprEtherSwitchIntFIoChassisId,'cfprEtherSwitchIntFIoDelFeTs':cfprEtherSwitchIntFIoDelFeTs,'cfprEtherSwitchIntFIoDiscovery':cfprEtherSwitchIntFIoDiscovery,'cfprEtherSwitchIntFIoEncap':cfprEtherSwitchIntFIoEncap,'cfprEtherSwitchIntFIoEpDn':cfprEtherSwitchIntFIoEpDn,'cfprEtherSwitchIntFIoFltAggr':cfprEtherSwitchIntFIoFltAggr,'cfprEtherSwitchIntFIoIfRole':cfprEtherSwitchIntFIoIfRole,'cfprEtherSwitchIntFIoIfType':cfprEtherSwitchIntFIoIfType,'cfprEtherSwitchIntFIoLocale':cfprEtherSwitchIntFIoLocale,'cfprEtherSwitchIntFIoMode':cfprEtherSwitchIntFIoMode,'cfprEtherSwitchIntFIoModel':cfprEtherSwitchIntFIoModel,'cfprEtherSwitchIntFIoName':cfprEtherSwitchIntFIoName,'cfprEtherSwitchIntFIoNewFeTs':cfprEtherSwitchIntFIoNewFeTs,'cfprEtherSwitchIntFIoOperState':cfprEtherSwitchIntFIoOperState,'cfprEtherSwitchIntFIoPeerAggrPortId':cfprEtherSwitchIntFIoPeerAggrPortId,'cfprEtherSwitchIntFIoPeerChassisId':cfprEtherSwitchIntFIoPeerChassisId,'cfprEtherSwitchIntFIoPeerDn':cfprEtherSwitchIntFIoPeerDn,'cfprEtherSwitchIntFIoPeerPortId':cfprEtherSwitchIntFIoPeerPortId,'cfprEtherSwitchIntFIoPeerSlotId':cfprEtherSwitchIntFIoPeerSlotId,'cfprEtherSwitchIntFIoPortId':cfprEtherSwitchIntFIoPortId,'cfprEtherSwitchIntFIoRevision':cfprEtherSwitchIntFIoRevision,'cfprEtherSwitchIntFIoSerial':cfprEtherSwitchIntFIoSerial,'cfprEtherSwitchIntFIoSlotId':cfprEtherSwitchIntFIoSlotId,'cfprEtherSwitchIntFIoStateQual':cfprEtherSwitchIntFIoStateQual,'cfprEtherSwitchIntFIoSwitchId':cfprEtherSwitchIntFIoSwitchId,'cfprEtherSwitchIntFIoTransport':cfprEtherSwitchIntFIoTransport,'cfprEtherSwitchIntFIoTs':cfprEtherSwitchIntFIoTs,'cfprEtherSwitchIntFIoType':cfprEtherSwitchIntFIoType,'cfprEtherSwitchIntFIoVendor':cfprEtherSwitchIntFIoVendor,'cfprEtherSwitchIntFIoXcvrType':cfprEtherSwitchIntFIoXcvrType,'cfprEtherSwitchIntFIoPcTable':cfprEtherSwitchIntFIoPcTable,'cfprEtherSwitchIntFIoPcEntry':cfprEtherSwitchIntFIoPcEntry,_f:cfprEtherSwitchIntFIoPcInstanceId,'cfprEtherSwitchIntFIoPcDn':cfprEtherSwitchIntFIoPcDn,'cfprEtherSwitchIntFIoPcRn':cfprEtherSwitchIntFIoPcRn,'cfprEtherSwitchIntFIoPcAdminState':cfprEtherSwitchIntFIoPcAdminState,'cfprEtherSwitchIntFIoPcChassisId':cfprEtherSwitchIntFIoPcChassisId,'cfprEtherSwitchIntFIoPcEpDn':cfprEtherSwitchIntFIoPcEpDn,'cfprEtherSwitchIntFIoPcFltAggr':cfprEtherSwitchIntFIoPcFltAggr,'cfprEtherSwitchIntFIoPcIfRole':cfprEtherSwitchIntFIoPcIfRole,'cfprEtherSwitchIntFIoPcIfType':cfprEtherSwitchIntFIoPcIfType,'cfprEtherSwitchIntFIoPcLocale':cfprEtherSwitchIntFIoPcLocale,'cfprEtherSwitchIntFIoPcName':cfprEtherSwitchIntFIoPcName,'cfprEtherSwitchIntFIoPcOperSpeed':cfprEtherSwitchIntFIoPcOperSpeed,'cfprEtherSwitchIntFIoPcOperState':cfprEtherSwitchIntFIoPcOperState,'cfprEtherSwitchIntFIoPcPeerDn':cfprEtherSwitchIntFIoPcPeerDn,'cfprEtherSwitchIntFIoPcPortId':cfprEtherSwitchIntFIoPcPortId,'cfprEtherSwitchIntFIoPcStateQual':cfprEtherSwitchIntFIoPcStateQual,'cfprEtherSwitchIntFIoPcSwitchId':cfprEtherSwitchIntFIoPcSwitchId,'cfprEtherSwitchIntFIoPcTransport':cfprEtherSwitchIntFIoPcTransport,'cfprEtherSwitchIntFIoPcType':cfprEtherSwitchIntFIoPcType,'cfprEtherSwitchIntFIoPcEpTable':cfprEtherSwitchIntFIoPcEpTable,'cfprEtherSwitchIntFIoPcEpEntry':cfprEtherSwitchIntFIoPcEpEntry,_g:cfprEtherSwitchIntFIoPcEpInstanceId,'cfprEtherSwitchIntFIoPcEpDnData':cfprEtherSwitchIntFIoPcEpDnData,'cfprEtherSwitchIntFIoPcEpRn':cfprEtherSwitchIntFIoPcEpRn,'cfprEtherSwitchIntFIoPcEpAckState':cfprEtherSwitchIntFIoPcEpAckState,'cfprEtherSwitchIntFIoPcEpAdminState':cfprEtherSwitchIntFIoPcEpAdminState,'cfprEtherSwitchIntFIoPcEpAggrPortId':cfprEtherSwitchIntFIoPcEpAggrPortId,'cfprEtherSwitchIntFIoPcEpChassisId':cfprEtherSwitchIntFIoPcEpChassisId,'cfprEtherSwitchIntFIoPcEpEpDn':cfprEtherSwitchIntFIoPcEpEpDn,'cfprEtherSwitchIntFIoPcEpIfRole':cfprEtherSwitchIntFIoPcEpIfRole,'cfprEtherSwitchIntFIoPcEpIfType':cfprEtherSwitchIntFIoPcEpIfType,'cfprEtherSwitchIntFIoPcEpLocale':cfprEtherSwitchIntFIoPcEpLocale,'cfprEtherSwitchIntFIoPcEpMembership':cfprEtherSwitchIntFIoPcEpMembership,'cfprEtherSwitchIntFIoPcEpName':cfprEtherSwitchIntFIoPcEpName,'cfprEtherSwitchIntFIoPcEpPeerAggrPortId':cfprEtherSwitchIntFIoPcEpPeerAggrPortId,'cfprEtherSwitchIntFIoPcEpPeerChassisId':cfprEtherSwitchIntFIoPcEpPeerChassisId,'cfprEtherSwitchIntFIoPcEpPeerDn':cfprEtherSwitchIntFIoPcEpPeerDn,'cfprEtherSwitchIntFIoPcEpPeerPortId':cfprEtherSwitchIntFIoPcEpPeerPortId,'cfprEtherSwitchIntFIoPcEpPeerSlotId':cfprEtherSwitchIntFIoPcEpPeerSlotId,'cfprEtherSwitchIntFIoPcEpPortId':cfprEtherSwitchIntFIoPcEpPortId,'cfprEtherSwitchIntFIoPcEpSlotId':cfprEtherSwitchIntFIoPcEpSlotId,'cfprEtherSwitchIntFIoPcEpStatusChangeTs':cfprEtherSwitchIntFIoPcEpStatusChangeTs,'cfprEtherSwitchIntFIoPcEpSwitchId':cfprEtherSwitchIntFIoPcEpSwitchId,'cfprEtherSwitchIntFIoPcEpTransport':cfprEtherSwitchIntFIoPcEpTransport,'cfprEtherSwitchIntFIoPcEpType':cfprEtherSwitchIntFIoPcEpType,'cfprEtherTxStatsTable':cfprEtherTxStatsTable,'cfprEtherTxStatsEntry':cfprEtherTxStatsEntry,_h:cfprEtherTxStatsInstanceId,'cfprEtherTxStatsDn':cfprEtherTxStatsDn,'cfprEtherTxStatsRn':cfprEtherTxStatsRn,'cfprEtherTxStatsBroadcastPackets':cfprEtherTxStatsBroadcastPackets,'cfprEtherTxStatsBroadcastPacketsDelta':cfprEtherTxStatsBroadcastPacketsDelta,'cfprEtherTxStatsBroadcastPacketsDeltaAvg':cfprEtherTxStatsBroadcastPacketsDeltaAvg,'cfprEtherTxStatsBroadcastPacketsDeltaMax':cfprEtherTxStatsBroadcastPacketsDeltaMax,'cfprEtherTxStatsBroadcastPacketsDeltaMin':cfprEtherTxStatsBroadcastPacketsDeltaMin,'cfprEtherTxStatsIntervals':cfprEtherTxStatsIntervals,'cfprEtherTxStatsJumboPackets':cfprEtherTxStatsJumboPackets,'cfprEtherTxStatsJumboPacketsDelta':cfprEtherTxStatsJumboPacketsDelta,'cfprEtherTxStatsJumboPacketsDeltaAvg':cfprEtherTxStatsJumboPacketsDeltaAvg,'cfprEtherTxStatsJumboPacketsDeltaMax':cfprEtherTxStatsJumboPacketsDeltaMax,'cfprEtherTxStatsJumboPacketsDeltaMin':cfprEtherTxStatsJumboPacketsDeltaMin,'cfprEtherTxStatsMulticastPackets':cfprEtherTxStatsMulticastPackets,'cfprEtherTxStatsMulticastPacketsDelta':cfprEtherTxStatsMulticastPacketsDelta,'cfprEtherTxStatsMulticastPacketsDeltaAvg':cfprEtherTxStatsMulticastPacketsDeltaAvg,'cfprEtherTxStatsMulticastPacketsDeltaMax':cfprEtherTxStatsMulticastPacketsDeltaMax,'cfprEtherTxStatsMulticastPacketsDeltaMin':cfprEtherTxStatsMulticastPacketsDeltaMin,'cfprEtherTxStatsSuspect':cfprEtherTxStatsSuspect,'cfprEtherTxStatsThresholded':cfprEtherTxStatsThresholded,'cfprEtherTxStatsTimeCollected':cfprEtherTxStatsTimeCollected,'cfprEtherTxStatsTotalBytes':cfprEtherTxStatsTotalBytes,'cfprEtherTxStatsTotalBytesDelta':cfprEtherTxStatsTotalBytesDelta,'cfprEtherTxStatsTotalBytesDeltaAvg':cfprEtherTxStatsTotalBytesDeltaAvg,'cfprEtherTxStatsTotalBytesDeltaMax':cfprEtherTxStatsTotalBytesDeltaMax,'cfprEtherTxStatsTotalBytesDeltaMin':cfprEtherTxStatsTotalBytesDeltaMin,'cfprEtherTxStatsTotalPackets':cfprEtherTxStatsTotalPackets,'cfprEtherTxStatsTotalPacketsDelta':cfprEtherTxStatsTotalPacketsDelta,'cfprEtherTxStatsTotalPacketsDeltaAvg':cfprEtherTxStatsTotalPacketsDeltaAvg,'cfprEtherTxStatsTotalPacketsDeltaMax':cfprEtherTxStatsTotalPacketsDeltaMax,'cfprEtherTxStatsTotalPacketsDeltaMin':cfprEtherTxStatsTotalPacketsDeltaMin,'cfprEtherTxStatsUnicastPackets':cfprEtherTxStatsUnicastPackets,'cfprEtherTxStatsUnicastPacketsDelta':cfprEtherTxStatsUnicastPacketsDelta,'cfprEtherTxStatsUnicastPacketsDeltaAvg':cfprEtherTxStatsUnicastPacketsDeltaAvg,'cfprEtherTxStatsUnicastPacketsDeltaMax':cfprEtherTxStatsUnicastPacketsDeltaMax,'cfprEtherTxStatsUnicastPacketsDeltaMin':cfprEtherTxStatsUnicastPacketsDeltaMin,'cfprEtherTxStatsUpdate':cfprEtherTxStatsUpdate,'cfprEtherTxStatsHistTable':cfprEtherTxStatsHistTable,'cfprEtherTxStatsHistEntry':cfprEtherTxStatsHistEntry,_i:cfprEtherTxStatsHistInstanceId,'cfprEtherTxStatsHistDn':cfprEtherTxStatsHistDn,'cfprEtherTxStatsHistRn':cfprEtherTxStatsHistRn,'cfprEtherTxStatsHistBroadcastPackets':cfprEtherTxStatsHistBroadcastPackets,'cfprEtherTxStatsHistBroadcastPacketsDelta':cfprEtherTxStatsHistBroadcastPacketsDelta,'cfprEtherTxStatsHistBroadcastPacketsDeltaAvg':cfprEtherTxStatsHistBroadcastPacketsDeltaAvg,'cfprEtherTxStatsHistBroadcastPacketsDeltaMax':cfprEtherTxStatsHistBroadcastPacketsDeltaMax,'cfprEtherTxStatsHistBroadcastPacketsDeltaMin':cfprEtherTxStatsHistBroadcastPacketsDeltaMin,'cfprEtherTxStatsHistId':cfprEtherTxStatsHistId,'cfprEtherTxStatsHistJumboPackets':cfprEtherTxStatsHistJumboPackets,'cfprEtherTxStatsHistJumboPacketsDelta':cfprEtherTxStatsHistJumboPacketsDelta,'cfprEtherTxStatsHistJumboPacketsDeltaAvg':cfprEtherTxStatsHistJumboPacketsDeltaAvg,'cfprEtherTxStatsHistJumboPacketsDeltaMax':cfprEtherTxStatsHistJumboPacketsDeltaMax,'cfprEtherTxStatsHistJumboPacketsDeltaMin':cfprEtherTxStatsHistJumboPacketsDeltaMin,'cfprEtherTxStatsHistMostRecent':cfprEtherTxStatsHistMostRecent,'cfprEtherTxStatsHistMulticastPackets':cfprEtherTxStatsHistMulticastPackets,'cfprEtherTxStatsHistMulticastPacketsDelta':cfprEtherTxStatsHistMulticastPacketsDelta,'cfprEtherTxStatsHistMulticastPacketsDeltaAvg':cfprEtherTxStatsHistMulticastPacketsDeltaAvg,'cfprEtherTxStatsHistMulticastPacketsDeltaMax':cfprEtherTxStatsHistMulticastPacketsDeltaMax,'cfprEtherTxStatsHistMulticastPacketsDeltaMin':cfprEtherTxStatsHistMulticastPacketsDeltaMin,'cfprEtherTxStatsHistSuspect':cfprEtherTxStatsHistSuspect,'cfprEtherTxStatsHistThresholded':cfprEtherTxStatsHistThresholded,'cfprEtherTxStatsHistTimeCollected':cfprEtherTxStatsHistTimeCollected,'cfprEtherTxStatsHistTotalBytes':cfprEtherTxStatsHistTotalBytes,'cfprEtherTxStatsHistTotalBytesDelta':cfprEtherTxStatsHistTotalBytesDelta,'cfprEtherTxStatsHistTotalBytesDeltaAvg':cfprEtherTxStatsHistTotalBytesDeltaAvg,'cfprEtherTxStatsHistTotalBytesDeltaMax':cfprEtherTxStatsHistTotalBytesDeltaMax,'cfprEtherTxStatsHistTotalBytesDeltaMin':cfprEtherTxStatsHistTotalBytesDeltaMin,'cfprEtherTxStatsHistTotalPackets':cfprEtherTxStatsHistTotalPackets,'cfprEtherTxStatsHistTotalPacketsDelta':cfprEtherTxStatsHistTotalPacketsDelta,'cfprEtherTxStatsHistTotalPacketsDeltaAvg':cfprEtherTxStatsHistTotalPacketsDeltaAvg,'cfprEtherTxStatsHistTotalPacketsDeltaMax':cfprEtherTxStatsHistTotalPacketsDeltaMax,'cfprEtherTxStatsHistTotalPacketsDeltaMin':cfprEtherTxStatsHistTotalPacketsDeltaMin,'cfprEtherTxStatsHistUnicastPackets':cfprEtherTxStatsHistUnicastPackets,'cfprEtherTxStatsHistUnicastPacketsDelta':cfprEtherTxStatsHistUnicastPacketsDelta,'cfprEtherTxStatsHistUnicastPacketsDeltaAvg':cfprEtherTxStatsHistUnicastPacketsDeltaAvg,'cfprEtherTxStatsHistUnicastPacketsDeltaMax':cfprEtherTxStatsHistUnicastPacketsDeltaMax,'cfprEtherTxStatsHistUnicastPacketsDeltaMin':cfprEtherTxStatsHistUnicastPacketsDeltaMin,'cfprEtherFailToWireTable':cfprEtherFailToWireTable,'cfprEtherFailToWireEntry':cfprEtherFailToWireEntry,_j:cfprEtherFailToWireInstanceId,'cfprEtherFailToWireDn':cfprEtherFailToWireDn,'cfprEtherFailToWireRn':cfprEtherFailToWireRn,'cfprEtherFailToWireLocale':cfprEtherFailToWireLocale,'cfprEtherFailToWireName':cfprEtherFailToWireName,'cfprEtherFailToWireTransport':cfprEtherFailToWireTransport,'cfprEtherFailToWireType':cfprEtherFailToWireType,'cfprEtherFtwPortPairTable':cfprEtherFtwPortPairTable,'cfprEtherFtwPortPairEntry':cfprEtherFtwPortPairEntry,_k:cfprEtherFtwPortPairInstanceId,'cfprEtherFtwPortPairDn':cfprEtherFtwPortPairDn,'cfprEtherFtwPortPairRn':cfprEtherFtwPortPairRn,'cfprEtherFtwPortPairAggrPortId':cfprEtherFtwPortPairAggrPortId,'cfprEtherFtwPortPairChassisId':cfprEtherFtwPortPairChassisId,'cfprEtherFtwPortPairEpDn':cfprEtherFtwPortPairEpDn,'cfprEtherFtwPortPairFsmDescr':cfprEtherFtwPortPairFsmDescr,'cfprEtherFtwPortPairFsmPrev':cfprEtherFtwPortPairFsmPrev,'cfprEtherFtwPortPairFsmProgr':cfprEtherFtwPortPairFsmProgr,'cfprEtherFtwPortPairFsmRmtInvErrCode':cfprEtherFtwPortPairFsmRmtInvErrCode,'cfprEtherFtwPortPairFsmRmtInvErrDescr':cfprEtherFtwPortPairFsmRmtInvErrDescr,'cfprEtherFtwPortPairFsmRmtInvRslt':cfprEtherFtwPortPairFsmRmtInvRslt,'cfprEtherFtwPortPairFsmStageDescr':cfprEtherFtwPortPairFsmStageDescr,'cfprEtherFtwPortPairFsmStamp':cfprEtherFtwPortPairFsmStamp,'cfprEtherFtwPortPairFsmStatus':cfprEtherFtwPortPairFsmStatus,'cfprEtherFtwPortPairFsmTry':cfprEtherFtwPortPairFsmTry,'cfprEtherFtwPortPairIfRole':cfprEtherFtwPortPairIfRole,'cfprEtherFtwPortPairIfType':cfprEtherFtwPortPairIfType,'cfprEtherFtwPortPairLocale':cfprEtherFtwPortPairLocale,'cfprEtherFtwPortPairMode':cfprEtherFtwPortPairMode,'cfprEtherFtwPortPairName':cfprEtherFtwPortPairName,'cfprEtherFtwPortPairOperMode':cfprEtherFtwPortPairOperMode,'cfprEtherFtwPortPairPeerAggrPortId':cfprEtherFtwPortPairPeerAggrPortId,'cfprEtherFtwPortPairPeerChassisId':cfprEtherFtwPortPairPeerChassisId,'cfprEtherFtwPortPairPeerDn':cfprEtherFtwPortPairPeerDn,'cfprEtherFtwPortPairPeerPortId':cfprEtherFtwPortPairPeerPortId,'cfprEtherFtwPortPairPeerPortName':cfprEtherFtwPortPairPeerPortName,'cfprEtherFtwPortPairPeerSlotId':cfprEtherFtwPortPairPeerSlotId,'cfprEtherFtwPortPairPortId':cfprEtherFtwPortPairPortId,'cfprEtherFtwPortPairPortName':cfprEtherFtwPortPairPortName,'cfprEtherFtwPortPairSlotId':cfprEtherFtwPortPairSlotId,'cfprEtherFtwPortPairSwitchId':cfprEtherFtwPortPairSwitchId,'cfprEtherFtwPortPairTransport':cfprEtherFtwPortPairTransport,'cfprEtherFtwPortPairTs':cfprEtherFtwPortPairTs,'cfprEtherFtwPortPairType':cfprEtherFtwPortPairType,'cfprEtherFtwPortPairWdtStart':cfprEtherFtwPortPairWdtStart,'cfprEtherFtwPortPairWdtState':cfprEtherFtwPortPairWdtState,'cfprEtherFtwPortPairFsmTable':cfprEtherFtwPortPairFsmTable,'cfprEtherFtwPortPairFsmEntry':cfprEtherFtwPortPairFsmEntry,_l:cfprEtherFtwPortPairFsmInstanceId,'cfprEtherFtwPortPairFsmDn':cfprEtherFtwPortPairFsmDn,'cfprEtherFtwPortPairFsmRn':cfprEtherFtwPortPairFsmRn,'cfprEtherFtwPortPairFsmCompletionTime':cfprEtherFtwPortPairFsmCompletionTime,'cfprEtherFtwPortPairFsmCurrentFsm':cfprEtherFtwPortPairFsmCurrentFsm,'cfprEtherFtwPortPairFsmDescrData':cfprEtherFtwPortPairFsmDescrData,'cfprEtherFtwPortPairFsmFsmStatus':cfprEtherFtwPortPairFsmFsmStatus,'cfprEtherFtwPortPairFsmProgress':cfprEtherFtwPortPairFsmProgress,'cfprEtherFtwPortPairFsmRmtErrCode':cfprEtherFtwPortPairFsmRmtErrCode,'cfprEtherFtwPortPairFsmRmtErrDescr':cfprEtherFtwPortPairFsmRmtErrDescr,'cfprEtherFtwPortPairFsmRmtRslt':cfprEtherFtwPortPairFsmRmtRslt,'cfprEtherFtwPortPairFsmStageTable':cfprEtherFtwPortPairFsmStageTable,'cfprEtherFtwPortPairFsmStageEntry':cfprEtherFtwPortPairFsmStageEntry,_m:cfprEtherFtwPortPairFsmStageInstanceId,'cfprEtherFtwPortPairFsmStageDn':cfprEtherFtwPortPairFsmStageDn,'cfprEtherFtwPortPairFsmStageRn':cfprEtherFtwPortPairFsmStageRn,'cfprEtherFtwPortPairFsmStageDescrData':cfprEtherFtwPortPairFsmStageDescrData,'cfprEtherFtwPortPairFsmStageLastUpdateTime':cfprEtherFtwPortPairFsmStageLastUpdateTime,'cfprEtherFtwPortPairFsmStageName':cfprEtherFtwPortPairFsmStageName,'cfprEtherFtwPortPairFsmStageOrder':cfprEtherFtwPortPairFsmStageOrder,'cfprEtherFtwPortPairFsmStageRetry':cfprEtherFtwPortPairFsmStageRetry,'cfprEtherFtwPortPairFsmStageStageStatus':cfprEtherFtwPortPairFsmStageStageStatus,'cfprEtherFtwPortPairFsmTaskTable':cfprEtherFtwPortPairFsmTaskTable,'cfprEtherFtwPortPairFsmTaskEntry':cfprEtherFtwPortPairFsmTaskEntry,_n:cfprEtherFtwPortPairFsmTaskInstanceId,'cfprEtherFtwPortPairFsmTaskDn':cfprEtherFtwPortPairFsmTaskDn,'cfprEtherFtwPortPairFsmTaskRn':cfprEtherFtwPortPairFsmTaskRn,'cfprEtherFtwPortPairFsmTaskCompletion':cfprEtherFtwPortPairFsmTaskCompletion,'cfprEtherFtwPortPairFsmTaskFlags':cfprEtherFtwPortPairFsmTaskFlags,'cfprEtherFtwPortPairFsmTaskItem':cfprEtherFtwPortPairFsmTaskItem,'cfprEtherFtwPortPairFsmTaskSeqId':cfprEtherFtwPortPairFsmTaskSeqId})