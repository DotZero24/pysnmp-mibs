_M='cucsFcPIoFsmStageInstanceId'
_L='cucsFcPIoFsmInstanceId'
_K='cucsFcSwIfConfigInstanceId'
_J='cucsFcStatsHistInstanceId'
_I='cucsFcStatsInstanceId'
_H='cucsFcPIoInstanceId'
_G='cucsFcNicIfConfigInstanceId'
_F='cucsFcErrStatsHistInstanceId'
_E='cucsFcErrStatsInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-FC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsEquipmentXcvrType,CucsFabricAdminState,CucsFcErrStatsHistThresholded,CucsFcErrStatsThresholded,CucsFcPIoFsmCurrentFsm,CucsFcPIoFsmStageName,CucsFcStatsHistThresholded,CucsFcStatsThresholded,CucsFsmFsmStageStatus,CucsFsmLifecycle,CucsLicenseState,CucsNetworkConnectionType,CucsNetworkLocale,CucsNetworkPhysEpIfType,CucsNetworkPortOperState,CucsNetworkPortRole,CucsNetworkSwitchId,CucsNetworkTransport,CucsPortEncap,CucsPortMode,CucsPortSpeed,CucsPortapiPeerCapability=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsEquipmentXcvrType','CucsFabricAdminState','CucsFcErrStatsHistThresholded','CucsFcErrStatsThresholded','CucsFcPIoFsmCurrentFsm','CucsFcPIoFsmStageName','CucsFcStatsHistThresholded','CucsFcStatsThresholded','CucsFsmFsmStageStatus','CucsFsmLifecycle','CucsLicenseState','CucsNetworkConnectionType','CucsNetworkLocale','CucsNetworkPhysEpIfType','CucsNetworkPortOperState','CucsNetworkPortRole','CucsNetworkSwitchId','CucsNetworkTransport','CucsPortEncap','CucsPortMode','CucsPortSpeed','CucsPortapiPeerCapability')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsFcObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,20))
_CucsFcErrStatsTable_Object=MibTable
cucsFcErrStatsTable=_CucsFcErrStatsTable_Object((1,3,6,1,4,1,9,9,719,1,20,1))
if mibBuilder.loadTexts:cucsFcErrStatsTable.setStatus(_A)
_CucsFcErrStatsEntry_Object=MibTableRow
cucsFcErrStatsEntry=_CucsFcErrStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,20,1,1))
cucsFcErrStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsFcErrStatsEntry.setStatus(_A)
_CucsFcErrStatsInstanceId_Type=CucsManagedObjectId
_CucsFcErrStatsInstanceId_Object=MibTableColumn
cucsFcErrStatsInstanceId=_CucsFcErrStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,1),_CucsFcErrStatsInstanceId_Type())
cucsFcErrStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcErrStatsInstanceId.setStatus(_A)
_CucsFcErrStatsDn_Type=CucsManagedObjectDn
_CucsFcErrStatsDn_Object=MibTableColumn
cucsFcErrStatsDn=_CucsFcErrStatsDn_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,2),_CucsFcErrStatsDn_Type())
cucsFcErrStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDn.setStatus(_A)
_CucsFcErrStatsRn_Type=SnmpAdminString
_CucsFcErrStatsRn_Object=MibTableColumn
cucsFcErrStatsRn=_CucsFcErrStatsRn_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,3),_CucsFcErrStatsRn_Type())
cucsFcErrStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsRn.setStatus(_A)
_CucsFcErrStatsCrcRx_Type=Unsigned64
_CucsFcErrStatsCrcRx_Object=MibTableColumn
cucsFcErrStatsCrcRx=_CucsFcErrStatsCrcRx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,4),_CucsFcErrStatsCrcRx_Type())
cucsFcErrStatsCrcRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsCrcRx.setStatus(_A)
_CucsFcErrStatsCrcRxDelta_Type=Counter64
_CucsFcErrStatsCrcRxDelta_Object=MibTableColumn
cucsFcErrStatsCrcRxDelta=_CucsFcErrStatsCrcRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,5),_CucsFcErrStatsCrcRxDelta_Type())
cucsFcErrStatsCrcRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsCrcRxDelta.setStatus(_A)
_CucsFcErrStatsCrcRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsCrcRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsCrcRxDeltaAvg=_CucsFcErrStatsCrcRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,6),_CucsFcErrStatsCrcRxDeltaAvg_Type())
cucsFcErrStatsCrcRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsCrcRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsCrcRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsCrcRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsCrcRxDeltaMax=_CucsFcErrStatsCrcRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,7),_CucsFcErrStatsCrcRxDeltaMax_Type())
cucsFcErrStatsCrcRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsCrcRxDeltaMax.setStatus(_A)
_CucsFcErrStatsCrcRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsCrcRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsCrcRxDeltaMin=_CucsFcErrStatsCrcRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,8),_CucsFcErrStatsCrcRxDeltaMin_Type())
cucsFcErrStatsCrcRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsCrcRxDeltaMin.setStatus(_A)
_CucsFcErrStatsDiscardRx_Type=Unsigned64
_CucsFcErrStatsDiscardRx_Object=MibTableColumn
cucsFcErrStatsDiscardRx=_CucsFcErrStatsDiscardRx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,9),_CucsFcErrStatsDiscardRx_Type())
cucsFcErrStatsDiscardRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardRx.setStatus(_A)
_CucsFcErrStatsDiscardRxDelta_Type=Counter64
_CucsFcErrStatsDiscardRxDelta_Object=MibTableColumn
cucsFcErrStatsDiscardRxDelta=_CucsFcErrStatsDiscardRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,10),_CucsFcErrStatsDiscardRxDelta_Type())
cucsFcErrStatsDiscardRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardRxDelta.setStatus(_A)
_CucsFcErrStatsDiscardRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsDiscardRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsDiscardRxDeltaAvg=_CucsFcErrStatsDiscardRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,11),_CucsFcErrStatsDiscardRxDeltaAvg_Type())
cucsFcErrStatsDiscardRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsDiscardRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsDiscardRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsDiscardRxDeltaMax=_CucsFcErrStatsDiscardRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,12),_CucsFcErrStatsDiscardRxDeltaMax_Type())
cucsFcErrStatsDiscardRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardRxDeltaMax.setStatus(_A)
_CucsFcErrStatsDiscardRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsDiscardRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsDiscardRxDeltaMin=_CucsFcErrStatsDiscardRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,13),_CucsFcErrStatsDiscardRxDeltaMin_Type())
cucsFcErrStatsDiscardRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardRxDeltaMin.setStatus(_A)
_CucsFcErrStatsDiscardTx_Type=Unsigned64
_CucsFcErrStatsDiscardTx_Object=MibTableColumn
cucsFcErrStatsDiscardTx=_CucsFcErrStatsDiscardTx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,14),_CucsFcErrStatsDiscardTx_Type())
cucsFcErrStatsDiscardTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardTx.setStatus(_A)
_CucsFcErrStatsDiscardTxDelta_Type=Counter64
_CucsFcErrStatsDiscardTxDelta_Object=MibTableColumn
cucsFcErrStatsDiscardTxDelta=_CucsFcErrStatsDiscardTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,15),_CucsFcErrStatsDiscardTxDelta_Type())
cucsFcErrStatsDiscardTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardTxDelta.setStatus(_A)
_CucsFcErrStatsDiscardTxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsDiscardTxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsDiscardTxDeltaAvg=_CucsFcErrStatsDiscardTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,16),_CucsFcErrStatsDiscardTxDeltaAvg_Type())
cucsFcErrStatsDiscardTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardTxDeltaAvg.setStatus(_A)
_CucsFcErrStatsDiscardTxDeltaMax_Type=Unsigned64
_CucsFcErrStatsDiscardTxDeltaMax_Object=MibTableColumn
cucsFcErrStatsDiscardTxDeltaMax=_CucsFcErrStatsDiscardTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,17),_CucsFcErrStatsDiscardTxDeltaMax_Type())
cucsFcErrStatsDiscardTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardTxDeltaMax.setStatus(_A)
_CucsFcErrStatsDiscardTxDeltaMin_Type=Unsigned64
_CucsFcErrStatsDiscardTxDeltaMin_Object=MibTableColumn
cucsFcErrStatsDiscardTxDeltaMin=_CucsFcErrStatsDiscardTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,18),_CucsFcErrStatsDiscardTxDeltaMin_Type())
cucsFcErrStatsDiscardTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsDiscardTxDeltaMin.setStatus(_A)
_CucsFcErrStatsIntervals_Type=Gauge32
_CucsFcErrStatsIntervals_Object=MibTableColumn
cucsFcErrStatsIntervals=_CucsFcErrStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,19),_CucsFcErrStatsIntervals_Type())
cucsFcErrStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsIntervals.setStatus(_A)
_CucsFcErrStatsLinkFailures_Type=Unsigned64
_CucsFcErrStatsLinkFailures_Object=MibTableColumn
cucsFcErrStatsLinkFailures=_CucsFcErrStatsLinkFailures_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,20),_CucsFcErrStatsLinkFailures_Type())
cucsFcErrStatsLinkFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsLinkFailures.setStatus(_A)
_CucsFcErrStatsLinkFailuresDelta_Type=Counter64
_CucsFcErrStatsLinkFailuresDelta_Object=MibTableColumn
cucsFcErrStatsLinkFailuresDelta=_CucsFcErrStatsLinkFailuresDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,21),_CucsFcErrStatsLinkFailuresDelta_Type())
cucsFcErrStatsLinkFailuresDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsLinkFailuresDelta.setStatus(_A)
_CucsFcErrStatsLinkFailuresDeltaAvg_Type=Unsigned64
_CucsFcErrStatsLinkFailuresDeltaAvg_Object=MibTableColumn
cucsFcErrStatsLinkFailuresDeltaAvg=_CucsFcErrStatsLinkFailuresDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,22),_CucsFcErrStatsLinkFailuresDeltaAvg_Type())
cucsFcErrStatsLinkFailuresDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsLinkFailuresDeltaAvg.setStatus(_A)
_CucsFcErrStatsLinkFailuresDeltaMax_Type=Unsigned64
_CucsFcErrStatsLinkFailuresDeltaMax_Object=MibTableColumn
cucsFcErrStatsLinkFailuresDeltaMax=_CucsFcErrStatsLinkFailuresDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,23),_CucsFcErrStatsLinkFailuresDeltaMax_Type())
cucsFcErrStatsLinkFailuresDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsLinkFailuresDeltaMax.setStatus(_A)
_CucsFcErrStatsLinkFailuresDeltaMin_Type=Unsigned64
_CucsFcErrStatsLinkFailuresDeltaMin_Object=MibTableColumn
cucsFcErrStatsLinkFailuresDeltaMin=_CucsFcErrStatsLinkFailuresDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,24),_CucsFcErrStatsLinkFailuresDeltaMin_Type())
cucsFcErrStatsLinkFailuresDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsLinkFailuresDeltaMin.setStatus(_A)
_CucsFcErrStatsRx_Type=Unsigned64
_CucsFcErrStatsRx_Object=MibTableColumn
cucsFcErrStatsRx=_CucsFcErrStatsRx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,25),_CucsFcErrStatsRx_Type())
cucsFcErrStatsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsRx.setStatus(_A)
_CucsFcErrStatsRxDelta_Type=Counter64
_CucsFcErrStatsRxDelta_Object=MibTableColumn
cucsFcErrStatsRxDelta=_CucsFcErrStatsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,26),_CucsFcErrStatsRxDelta_Type())
cucsFcErrStatsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsRxDelta.setStatus(_A)
_CucsFcErrStatsRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsRxDeltaAvg=_CucsFcErrStatsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,27),_CucsFcErrStatsRxDeltaAvg_Type())
cucsFcErrStatsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsRxDeltaMax=_CucsFcErrStatsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,28),_CucsFcErrStatsRxDeltaMax_Type())
cucsFcErrStatsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsRxDeltaMax.setStatus(_A)
_CucsFcErrStatsRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsRxDeltaMin=_CucsFcErrStatsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,29),_CucsFcErrStatsRxDeltaMin_Type())
cucsFcErrStatsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsRxDeltaMin.setStatus(_A)
_CucsFcErrStatsSignalLosses_Type=Unsigned64
_CucsFcErrStatsSignalLosses_Object=MibTableColumn
cucsFcErrStatsSignalLosses=_CucsFcErrStatsSignalLosses_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,30),_CucsFcErrStatsSignalLosses_Type())
cucsFcErrStatsSignalLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSignalLosses.setStatus(_A)
_CucsFcErrStatsSignalLossesDelta_Type=Counter64
_CucsFcErrStatsSignalLossesDelta_Object=MibTableColumn
cucsFcErrStatsSignalLossesDelta=_CucsFcErrStatsSignalLossesDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,31),_CucsFcErrStatsSignalLossesDelta_Type())
cucsFcErrStatsSignalLossesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSignalLossesDelta.setStatus(_A)
_CucsFcErrStatsSignalLossesDeltaAvg_Type=Unsigned64
_CucsFcErrStatsSignalLossesDeltaAvg_Object=MibTableColumn
cucsFcErrStatsSignalLossesDeltaAvg=_CucsFcErrStatsSignalLossesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,32),_CucsFcErrStatsSignalLossesDeltaAvg_Type())
cucsFcErrStatsSignalLossesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSignalLossesDeltaAvg.setStatus(_A)
_CucsFcErrStatsSignalLossesDeltaMax_Type=Unsigned64
_CucsFcErrStatsSignalLossesDeltaMax_Object=MibTableColumn
cucsFcErrStatsSignalLossesDeltaMax=_CucsFcErrStatsSignalLossesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,33),_CucsFcErrStatsSignalLossesDeltaMax_Type())
cucsFcErrStatsSignalLossesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSignalLossesDeltaMax.setStatus(_A)
_CucsFcErrStatsSignalLossesDeltaMin_Type=Unsigned64
_CucsFcErrStatsSignalLossesDeltaMin_Object=MibTableColumn
cucsFcErrStatsSignalLossesDeltaMin=_CucsFcErrStatsSignalLossesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,34),_CucsFcErrStatsSignalLossesDeltaMin_Type())
cucsFcErrStatsSignalLossesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSignalLossesDeltaMin.setStatus(_A)
_CucsFcErrStatsSuspect_Type=TruthValue
_CucsFcErrStatsSuspect_Object=MibTableColumn
cucsFcErrStatsSuspect=_CucsFcErrStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,35),_CucsFcErrStatsSuspect_Type())
cucsFcErrStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSuspect.setStatus(_A)
_CucsFcErrStatsSyncLosses_Type=Unsigned64
_CucsFcErrStatsSyncLosses_Object=MibTableColumn
cucsFcErrStatsSyncLosses=_CucsFcErrStatsSyncLosses_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,36),_CucsFcErrStatsSyncLosses_Type())
cucsFcErrStatsSyncLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSyncLosses.setStatus(_A)
_CucsFcErrStatsSyncLossesDelta_Type=Counter64
_CucsFcErrStatsSyncLossesDelta_Object=MibTableColumn
cucsFcErrStatsSyncLossesDelta=_CucsFcErrStatsSyncLossesDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,37),_CucsFcErrStatsSyncLossesDelta_Type())
cucsFcErrStatsSyncLossesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSyncLossesDelta.setStatus(_A)
_CucsFcErrStatsSyncLossesDeltaAvg_Type=Unsigned64
_CucsFcErrStatsSyncLossesDeltaAvg_Object=MibTableColumn
cucsFcErrStatsSyncLossesDeltaAvg=_CucsFcErrStatsSyncLossesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,38),_CucsFcErrStatsSyncLossesDeltaAvg_Type())
cucsFcErrStatsSyncLossesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSyncLossesDeltaAvg.setStatus(_A)
_CucsFcErrStatsSyncLossesDeltaMax_Type=Unsigned64
_CucsFcErrStatsSyncLossesDeltaMax_Object=MibTableColumn
cucsFcErrStatsSyncLossesDeltaMax=_CucsFcErrStatsSyncLossesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,39),_CucsFcErrStatsSyncLossesDeltaMax_Type())
cucsFcErrStatsSyncLossesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSyncLossesDeltaMax.setStatus(_A)
_CucsFcErrStatsSyncLossesDeltaMin_Type=Unsigned64
_CucsFcErrStatsSyncLossesDeltaMin_Object=MibTableColumn
cucsFcErrStatsSyncLossesDeltaMin=_CucsFcErrStatsSyncLossesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,40),_CucsFcErrStatsSyncLossesDeltaMin_Type())
cucsFcErrStatsSyncLossesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsSyncLossesDeltaMin.setStatus(_A)
_CucsFcErrStatsThresholded_Type=CucsFcErrStatsThresholded
_CucsFcErrStatsThresholded_Object=MibTableColumn
cucsFcErrStatsThresholded=_CucsFcErrStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,41),_CucsFcErrStatsThresholded_Type())
cucsFcErrStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsThresholded.setStatus(_A)
_CucsFcErrStatsTimeCollected_Type=DateAndTime
_CucsFcErrStatsTimeCollected_Object=MibTableColumn
cucsFcErrStatsTimeCollected=_CucsFcErrStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,42),_CucsFcErrStatsTimeCollected_Type())
cucsFcErrStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTimeCollected.setStatus(_A)
_CucsFcErrStatsTooLongRx_Type=Unsigned64
_CucsFcErrStatsTooLongRx_Object=MibTableColumn
cucsFcErrStatsTooLongRx=_CucsFcErrStatsTooLongRx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,43),_CucsFcErrStatsTooLongRx_Type())
cucsFcErrStatsTooLongRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooLongRx.setStatus(_A)
_CucsFcErrStatsTooLongRxDelta_Type=Counter64
_CucsFcErrStatsTooLongRxDelta_Object=MibTableColumn
cucsFcErrStatsTooLongRxDelta=_CucsFcErrStatsTooLongRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,44),_CucsFcErrStatsTooLongRxDelta_Type())
cucsFcErrStatsTooLongRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooLongRxDelta.setStatus(_A)
_CucsFcErrStatsTooLongRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsTooLongRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsTooLongRxDeltaAvg=_CucsFcErrStatsTooLongRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,45),_CucsFcErrStatsTooLongRxDeltaAvg_Type())
cucsFcErrStatsTooLongRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooLongRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsTooLongRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsTooLongRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsTooLongRxDeltaMax=_CucsFcErrStatsTooLongRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,46),_CucsFcErrStatsTooLongRxDeltaMax_Type())
cucsFcErrStatsTooLongRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooLongRxDeltaMax.setStatus(_A)
_CucsFcErrStatsTooLongRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsTooLongRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsTooLongRxDeltaMin=_CucsFcErrStatsTooLongRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,47),_CucsFcErrStatsTooLongRxDeltaMin_Type())
cucsFcErrStatsTooLongRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooLongRxDeltaMin.setStatus(_A)
_CucsFcErrStatsTooShortRx_Type=Unsigned64
_CucsFcErrStatsTooShortRx_Object=MibTableColumn
cucsFcErrStatsTooShortRx=_CucsFcErrStatsTooShortRx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,48),_CucsFcErrStatsTooShortRx_Type())
cucsFcErrStatsTooShortRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooShortRx.setStatus(_A)
_CucsFcErrStatsTooShortRxDelta_Type=Counter64
_CucsFcErrStatsTooShortRxDelta_Object=MibTableColumn
cucsFcErrStatsTooShortRxDelta=_CucsFcErrStatsTooShortRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,49),_CucsFcErrStatsTooShortRxDelta_Type())
cucsFcErrStatsTooShortRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooShortRxDelta.setStatus(_A)
_CucsFcErrStatsTooShortRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsTooShortRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsTooShortRxDeltaAvg=_CucsFcErrStatsTooShortRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,50),_CucsFcErrStatsTooShortRxDeltaAvg_Type())
cucsFcErrStatsTooShortRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooShortRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsTooShortRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsTooShortRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsTooShortRxDeltaMax=_CucsFcErrStatsTooShortRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,51),_CucsFcErrStatsTooShortRxDeltaMax_Type())
cucsFcErrStatsTooShortRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooShortRxDeltaMax.setStatus(_A)
_CucsFcErrStatsTooShortRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsTooShortRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsTooShortRxDeltaMin=_CucsFcErrStatsTooShortRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,52),_CucsFcErrStatsTooShortRxDeltaMin_Type())
cucsFcErrStatsTooShortRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTooShortRxDeltaMin.setStatus(_A)
_CucsFcErrStatsTx_Type=Unsigned64
_CucsFcErrStatsTx_Object=MibTableColumn
cucsFcErrStatsTx=_CucsFcErrStatsTx_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,53),_CucsFcErrStatsTx_Type())
cucsFcErrStatsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTx.setStatus(_A)
_CucsFcErrStatsTxDelta_Type=Counter64
_CucsFcErrStatsTxDelta_Object=MibTableColumn
cucsFcErrStatsTxDelta=_CucsFcErrStatsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,54),_CucsFcErrStatsTxDelta_Type())
cucsFcErrStatsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTxDelta.setStatus(_A)
_CucsFcErrStatsTxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsTxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsTxDeltaAvg=_CucsFcErrStatsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,55),_CucsFcErrStatsTxDeltaAvg_Type())
cucsFcErrStatsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTxDeltaAvg.setStatus(_A)
_CucsFcErrStatsTxDeltaMax_Type=Unsigned64
_CucsFcErrStatsTxDeltaMax_Object=MibTableColumn
cucsFcErrStatsTxDeltaMax=_CucsFcErrStatsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,56),_CucsFcErrStatsTxDeltaMax_Type())
cucsFcErrStatsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTxDeltaMax.setStatus(_A)
_CucsFcErrStatsTxDeltaMin_Type=Unsigned64
_CucsFcErrStatsTxDeltaMin_Object=MibTableColumn
cucsFcErrStatsTxDeltaMin=_CucsFcErrStatsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,57),_CucsFcErrStatsTxDeltaMin_Type())
cucsFcErrStatsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsTxDeltaMin.setStatus(_A)
_CucsFcErrStatsUpdate_Type=Gauge32
_CucsFcErrStatsUpdate_Object=MibTableColumn
cucsFcErrStatsUpdate=_CucsFcErrStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,20,1,1,58),_CucsFcErrStatsUpdate_Type())
cucsFcErrStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsUpdate.setStatus(_A)
_CucsFcErrStatsHistTable_Object=MibTable
cucsFcErrStatsHistTable=_CucsFcErrStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,20,2))
if mibBuilder.loadTexts:cucsFcErrStatsHistTable.setStatus(_A)
_CucsFcErrStatsHistEntry_Object=MibTableRow
cucsFcErrStatsHistEntry=_CucsFcErrStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,20,2,1))
cucsFcErrStatsHistEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsFcErrStatsHistEntry.setStatus(_A)
_CucsFcErrStatsHistInstanceId_Type=CucsManagedObjectId
_CucsFcErrStatsHistInstanceId_Object=MibTableColumn
cucsFcErrStatsHistInstanceId=_CucsFcErrStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,1),_CucsFcErrStatsHistInstanceId_Type())
cucsFcErrStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcErrStatsHistInstanceId.setStatus(_A)
_CucsFcErrStatsHistDn_Type=CucsManagedObjectDn
_CucsFcErrStatsHistDn_Object=MibTableColumn
cucsFcErrStatsHistDn=_CucsFcErrStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,2),_CucsFcErrStatsHistDn_Type())
cucsFcErrStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDn.setStatus(_A)
_CucsFcErrStatsHistRn_Type=SnmpAdminString
_CucsFcErrStatsHistRn_Object=MibTableColumn
cucsFcErrStatsHistRn=_CucsFcErrStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,3),_CucsFcErrStatsHistRn_Type())
cucsFcErrStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistRn.setStatus(_A)
_CucsFcErrStatsHistCrcRx_Type=Unsigned64
_CucsFcErrStatsHistCrcRx_Object=MibTableColumn
cucsFcErrStatsHistCrcRx=_CucsFcErrStatsHistCrcRx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,4),_CucsFcErrStatsHistCrcRx_Type())
cucsFcErrStatsHistCrcRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistCrcRx.setStatus(_A)
_CucsFcErrStatsHistCrcRxDelta_Type=Unsigned64
_CucsFcErrStatsHistCrcRxDelta_Object=MibTableColumn
cucsFcErrStatsHistCrcRxDelta=_CucsFcErrStatsHistCrcRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,5),_CucsFcErrStatsHistCrcRxDelta_Type())
cucsFcErrStatsHistCrcRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistCrcRxDelta.setStatus(_A)
_CucsFcErrStatsHistCrcRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistCrcRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistCrcRxDeltaAvg=_CucsFcErrStatsHistCrcRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,6),_CucsFcErrStatsHistCrcRxDeltaAvg_Type())
cucsFcErrStatsHistCrcRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistCrcRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistCrcRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistCrcRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistCrcRxDeltaMax=_CucsFcErrStatsHistCrcRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,7),_CucsFcErrStatsHistCrcRxDeltaMax_Type())
cucsFcErrStatsHistCrcRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistCrcRxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistCrcRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistCrcRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistCrcRxDeltaMin=_CucsFcErrStatsHistCrcRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,8),_CucsFcErrStatsHistCrcRxDeltaMin_Type())
cucsFcErrStatsHistCrcRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistCrcRxDeltaMin.setStatus(_A)
_CucsFcErrStatsHistDiscardRx_Type=Unsigned64
_CucsFcErrStatsHistDiscardRx_Object=MibTableColumn
cucsFcErrStatsHistDiscardRx=_CucsFcErrStatsHistDiscardRx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,9),_CucsFcErrStatsHistDiscardRx_Type())
cucsFcErrStatsHistDiscardRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardRx.setStatus(_A)
_CucsFcErrStatsHistDiscardRxDelta_Type=Unsigned64
_CucsFcErrStatsHistDiscardRxDelta_Object=MibTableColumn
cucsFcErrStatsHistDiscardRxDelta=_CucsFcErrStatsHistDiscardRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,10),_CucsFcErrStatsHistDiscardRxDelta_Type())
cucsFcErrStatsHistDiscardRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardRxDelta.setStatus(_A)
_CucsFcErrStatsHistDiscardRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistDiscardRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistDiscardRxDeltaAvg=_CucsFcErrStatsHistDiscardRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,11),_CucsFcErrStatsHistDiscardRxDeltaAvg_Type())
cucsFcErrStatsHistDiscardRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistDiscardRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistDiscardRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistDiscardRxDeltaMax=_CucsFcErrStatsHistDiscardRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,12),_CucsFcErrStatsHistDiscardRxDeltaMax_Type())
cucsFcErrStatsHistDiscardRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardRxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistDiscardRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistDiscardRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistDiscardRxDeltaMin=_CucsFcErrStatsHistDiscardRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,13),_CucsFcErrStatsHistDiscardRxDeltaMin_Type())
cucsFcErrStatsHistDiscardRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardRxDeltaMin.setStatus(_A)
_CucsFcErrStatsHistDiscardTx_Type=Unsigned64
_CucsFcErrStatsHistDiscardTx_Object=MibTableColumn
cucsFcErrStatsHistDiscardTx=_CucsFcErrStatsHistDiscardTx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,14),_CucsFcErrStatsHistDiscardTx_Type())
cucsFcErrStatsHistDiscardTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardTx.setStatus(_A)
_CucsFcErrStatsHistDiscardTxDelta_Type=Unsigned64
_CucsFcErrStatsHistDiscardTxDelta_Object=MibTableColumn
cucsFcErrStatsHistDiscardTxDelta=_CucsFcErrStatsHistDiscardTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,15),_CucsFcErrStatsHistDiscardTxDelta_Type())
cucsFcErrStatsHistDiscardTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardTxDelta.setStatus(_A)
_CucsFcErrStatsHistDiscardTxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistDiscardTxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistDiscardTxDeltaAvg=_CucsFcErrStatsHistDiscardTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,16),_CucsFcErrStatsHistDiscardTxDeltaAvg_Type())
cucsFcErrStatsHistDiscardTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardTxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistDiscardTxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistDiscardTxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistDiscardTxDeltaMax=_CucsFcErrStatsHistDiscardTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,17),_CucsFcErrStatsHistDiscardTxDeltaMax_Type())
cucsFcErrStatsHistDiscardTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardTxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistDiscardTxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistDiscardTxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistDiscardTxDeltaMin=_CucsFcErrStatsHistDiscardTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,18),_CucsFcErrStatsHistDiscardTxDeltaMin_Type())
cucsFcErrStatsHistDiscardTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistDiscardTxDeltaMin.setStatus(_A)
_CucsFcErrStatsHistId_Type=Unsigned64
_CucsFcErrStatsHistId_Object=MibTableColumn
cucsFcErrStatsHistId=_CucsFcErrStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,19),_CucsFcErrStatsHistId_Type())
cucsFcErrStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistId.setStatus(_A)
_CucsFcErrStatsHistLinkFailures_Type=Unsigned64
_CucsFcErrStatsHistLinkFailures_Object=MibTableColumn
cucsFcErrStatsHistLinkFailures=_CucsFcErrStatsHistLinkFailures_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,20),_CucsFcErrStatsHistLinkFailures_Type())
cucsFcErrStatsHistLinkFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistLinkFailures.setStatus(_A)
_CucsFcErrStatsHistLinkFailuresDelta_Type=Unsigned64
_CucsFcErrStatsHistLinkFailuresDelta_Object=MibTableColumn
cucsFcErrStatsHistLinkFailuresDelta=_CucsFcErrStatsHistLinkFailuresDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,21),_CucsFcErrStatsHistLinkFailuresDelta_Type())
cucsFcErrStatsHistLinkFailuresDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistLinkFailuresDelta.setStatus(_A)
_CucsFcErrStatsHistLinkFailuresDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistLinkFailuresDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistLinkFailuresDeltaAvg=_CucsFcErrStatsHistLinkFailuresDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,22),_CucsFcErrStatsHistLinkFailuresDeltaAvg_Type())
cucsFcErrStatsHistLinkFailuresDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistLinkFailuresDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistLinkFailuresDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistLinkFailuresDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistLinkFailuresDeltaMax=_CucsFcErrStatsHistLinkFailuresDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,23),_CucsFcErrStatsHistLinkFailuresDeltaMax_Type())
cucsFcErrStatsHistLinkFailuresDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistLinkFailuresDeltaMax.setStatus(_A)
_CucsFcErrStatsHistLinkFailuresDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistLinkFailuresDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistLinkFailuresDeltaMin=_CucsFcErrStatsHistLinkFailuresDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,24),_CucsFcErrStatsHistLinkFailuresDeltaMin_Type())
cucsFcErrStatsHistLinkFailuresDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistLinkFailuresDeltaMin.setStatus(_A)
_CucsFcErrStatsHistMostRecent_Type=TruthValue
_CucsFcErrStatsHistMostRecent_Object=MibTableColumn
cucsFcErrStatsHistMostRecent=_CucsFcErrStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,25),_CucsFcErrStatsHistMostRecent_Type())
cucsFcErrStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistMostRecent.setStatus(_A)
_CucsFcErrStatsHistRx_Type=Unsigned64
_CucsFcErrStatsHistRx_Object=MibTableColumn
cucsFcErrStatsHistRx=_CucsFcErrStatsHistRx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,26),_CucsFcErrStatsHistRx_Type())
cucsFcErrStatsHistRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistRx.setStatus(_A)
_CucsFcErrStatsHistRxDelta_Type=Unsigned64
_CucsFcErrStatsHistRxDelta_Object=MibTableColumn
cucsFcErrStatsHistRxDelta=_CucsFcErrStatsHistRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,27),_CucsFcErrStatsHistRxDelta_Type())
cucsFcErrStatsHistRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistRxDelta.setStatus(_A)
_CucsFcErrStatsHistRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistRxDeltaAvg=_CucsFcErrStatsHistRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,28),_CucsFcErrStatsHistRxDeltaAvg_Type())
cucsFcErrStatsHistRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistRxDeltaMax=_CucsFcErrStatsHistRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,29),_CucsFcErrStatsHistRxDeltaMax_Type())
cucsFcErrStatsHistRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistRxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistRxDeltaMin=_CucsFcErrStatsHistRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,30),_CucsFcErrStatsHistRxDeltaMin_Type())
cucsFcErrStatsHistRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistRxDeltaMin.setStatus(_A)
_CucsFcErrStatsHistSignalLosses_Type=Unsigned64
_CucsFcErrStatsHistSignalLosses_Object=MibTableColumn
cucsFcErrStatsHistSignalLosses=_CucsFcErrStatsHistSignalLosses_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,31),_CucsFcErrStatsHistSignalLosses_Type())
cucsFcErrStatsHistSignalLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSignalLosses.setStatus(_A)
_CucsFcErrStatsHistSignalLossesDelta_Type=Unsigned64
_CucsFcErrStatsHistSignalLossesDelta_Object=MibTableColumn
cucsFcErrStatsHistSignalLossesDelta=_CucsFcErrStatsHistSignalLossesDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,32),_CucsFcErrStatsHistSignalLossesDelta_Type())
cucsFcErrStatsHistSignalLossesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSignalLossesDelta.setStatus(_A)
_CucsFcErrStatsHistSignalLossesDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistSignalLossesDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistSignalLossesDeltaAvg=_CucsFcErrStatsHistSignalLossesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,33),_CucsFcErrStatsHistSignalLossesDeltaAvg_Type())
cucsFcErrStatsHistSignalLossesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSignalLossesDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistSignalLossesDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistSignalLossesDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistSignalLossesDeltaMax=_CucsFcErrStatsHistSignalLossesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,34),_CucsFcErrStatsHistSignalLossesDeltaMax_Type())
cucsFcErrStatsHistSignalLossesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSignalLossesDeltaMax.setStatus(_A)
_CucsFcErrStatsHistSignalLossesDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistSignalLossesDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistSignalLossesDeltaMin=_CucsFcErrStatsHistSignalLossesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,35),_CucsFcErrStatsHistSignalLossesDeltaMin_Type())
cucsFcErrStatsHistSignalLossesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSignalLossesDeltaMin.setStatus(_A)
_CucsFcErrStatsHistSuspect_Type=TruthValue
_CucsFcErrStatsHistSuspect_Object=MibTableColumn
cucsFcErrStatsHistSuspect=_CucsFcErrStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,36),_CucsFcErrStatsHistSuspect_Type())
cucsFcErrStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSuspect.setStatus(_A)
_CucsFcErrStatsHistSyncLosses_Type=Unsigned64
_CucsFcErrStatsHistSyncLosses_Object=MibTableColumn
cucsFcErrStatsHistSyncLosses=_CucsFcErrStatsHistSyncLosses_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,37),_CucsFcErrStatsHistSyncLosses_Type())
cucsFcErrStatsHistSyncLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSyncLosses.setStatus(_A)
_CucsFcErrStatsHistSyncLossesDelta_Type=Unsigned64
_CucsFcErrStatsHistSyncLossesDelta_Object=MibTableColumn
cucsFcErrStatsHistSyncLossesDelta=_CucsFcErrStatsHistSyncLossesDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,38),_CucsFcErrStatsHistSyncLossesDelta_Type())
cucsFcErrStatsHistSyncLossesDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSyncLossesDelta.setStatus(_A)
_CucsFcErrStatsHistSyncLossesDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistSyncLossesDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistSyncLossesDeltaAvg=_CucsFcErrStatsHistSyncLossesDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,39),_CucsFcErrStatsHistSyncLossesDeltaAvg_Type())
cucsFcErrStatsHistSyncLossesDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSyncLossesDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistSyncLossesDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistSyncLossesDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistSyncLossesDeltaMax=_CucsFcErrStatsHistSyncLossesDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,40),_CucsFcErrStatsHistSyncLossesDeltaMax_Type())
cucsFcErrStatsHistSyncLossesDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSyncLossesDeltaMax.setStatus(_A)
_CucsFcErrStatsHistSyncLossesDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistSyncLossesDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistSyncLossesDeltaMin=_CucsFcErrStatsHistSyncLossesDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,41),_CucsFcErrStatsHistSyncLossesDeltaMin_Type())
cucsFcErrStatsHistSyncLossesDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistSyncLossesDeltaMin.setStatus(_A)
_CucsFcErrStatsHistThresholded_Type=CucsFcErrStatsHistThresholded
_CucsFcErrStatsHistThresholded_Object=MibTableColumn
cucsFcErrStatsHistThresholded=_CucsFcErrStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,42),_CucsFcErrStatsHistThresholded_Type())
cucsFcErrStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistThresholded.setStatus(_A)
_CucsFcErrStatsHistTimeCollected_Type=DateAndTime
_CucsFcErrStatsHistTimeCollected_Object=MibTableColumn
cucsFcErrStatsHistTimeCollected=_CucsFcErrStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,43),_CucsFcErrStatsHistTimeCollected_Type())
cucsFcErrStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTimeCollected.setStatus(_A)
_CucsFcErrStatsHistTooLongRx_Type=Unsigned64
_CucsFcErrStatsHistTooLongRx_Object=MibTableColumn
cucsFcErrStatsHistTooLongRx=_CucsFcErrStatsHistTooLongRx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,44),_CucsFcErrStatsHistTooLongRx_Type())
cucsFcErrStatsHistTooLongRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooLongRx.setStatus(_A)
_CucsFcErrStatsHistTooLongRxDelta_Type=Unsigned64
_CucsFcErrStatsHistTooLongRxDelta_Object=MibTableColumn
cucsFcErrStatsHistTooLongRxDelta=_CucsFcErrStatsHistTooLongRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,45),_CucsFcErrStatsHistTooLongRxDelta_Type())
cucsFcErrStatsHistTooLongRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooLongRxDelta.setStatus(_A)
_CucsFcErrStatsHistTooLongRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistTooLongRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistTooLongRxDeltaAvg=_CucsFcErrStatsHistTooLongRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,46),_CucsFcErrStatsHistTooLongRxDeltaAvg_Type())
cucsFcErrStatsHistTooLongRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooLongRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistTooLongRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistTooLongRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistTooLongRxDeltaMax=_CucsFcErrStatsHistTooLongRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,47),_CucsFcErrStatsHistTooLongRxDeltaMax_Type())
cucsFcErrStatsHistTooLongRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooLongRxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistTooLongRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistTooLongRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistTooLongRxDeltaMin=_CucsFcErrStatsHistTooLongRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,48),_CucsFcErrStatsHistTooLongRxDeltaMin_Type())
cucsFcErrStatsHistTooLongRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooLongRxDeltaMin.setStatus(_A)
_CucsFcErrStatsHistTooShortRx_Type=Unsigned64
_CucsFcErrStatsHistTooShortRx_Object=MibTableColumn
cucsFcErrStatsHistTooShortRx=_CucsFcErrStatsHistTooShortRx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,49),_CucsFcErrStatsHistTooShortRx_Type())
cucsFcErrStatsHistTooShortRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooShortRx.setStatus(_A)
_CucsFcErrStatsHistTooShortRxDelta_Type=Unsigned64
_CucsFcErrStatsHistTooShortRxDelta_Object=MibTableColumn
cucsFcErrStatsHistTooShortRxDelta=_CucsFcErrStatsHistTooShortRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,50),_CucsFcErrStatsHistTooShortRxDelta_Type())
cucsFcErrStatsHistTooShortRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooShortRxDelta.setStatus(_A)
_CucsFcErrStatsHistTooShortRxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistTooShortRxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistTooShortRxDeltaAvg=_CucsFcErrStatsHistTooShortRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,51),_CucsFcErrStatsHistTooShortRxDeltaAvg_Type())
cucsFcErrStatsHistTooShortRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooShortRxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistTooShortRxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistTooShortRxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistTooShortRxDeltaMax=_CucsFcErrStatsHistTooShortRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,52),_CucsFcErrStatsHistTooShortRxDeltaMax_Type())
cucsFcErrStatsHistTooShortRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooShortRxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistTooShortRxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistTooShortRxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistTooShortRxDeltaMin=_CucsFcErrStatsHistTooShortRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,53),_CucsFcErrStatsHistTooShortRxDeltaMin_Type())
cucsFcErrStatsHistTooShortRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTooShortRxDeltaMin.setStatus(_A)
_CucsFcErrStatsHistTx_Type=Unsigned64
_CucsFcErrStatsHistTx_Object=MibTableColumn
cucsFcErrStatsHistTx=_CucsFcErrStatsHistTx_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,54),_CucsFcErrStatsHistTx_Type())
cucsFcErrStatsHistTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTx.setStatus(_A)
_CucsFcErrStatsHistTxDelta_Type=Unsigned64
_CucsFcErrStatsHistTxDelta_Object=MibTableColumn
cucsFcErrStatsHistTxDelta=_CucsFcErrStatsHistTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,55),_CucsFcErrStatsHistTxDelta_Type())
cucsFcErrStatsHistTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTxDelta.setStatus(_A)
_CucsFcErrStatsHistTxDeltaAvg_Type=Unsigned64
_CucsFcErrStatsHistTxDeltaAvg_Object=MibTableColumn
cucsFcErrStatsHistTxDeltaAvg=_CucsFcErrStatsHistTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,56),_CucsFcErrStatsHistTxDeltaAvg_Type())
cucsFcErrStatsHistTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTxDeltaAvg.setStatus(_A)
_CucsFcErrStatsHistTxDeltaMax_Type=Unsigned64
_CucsFcErrStatsHistTxDeltaMax_Object=MibTableColumn
cucsFcErrStatsHistTxDeltaMax=_CucsFcErrStatsHistTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,57),_CucsFcErrStatsHistTxDeltaMax_Type())
cucsFcErrStatsHistTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTxDeltaMax.setStatus(_A)
_CucsFcErrStatsHistTxDeltaMin_Type=Unsigned64
_CucsFcErrStatsHistTxDeltaMin_Object=MibTableColumn
cucsFcErrStatsHistTxDeltaMin=_CucsFcErrStatsHistTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,2,1,58),_CucsFcErrStatsHistTxDeltaMin_Type())
cucsFcErrStatsHistTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcErrStatsHistTxDeltaMin.setStatus(_A)
_CucsFcNicIfConfigTable_Object=MibTable
cucsFcNicIfConfigTable=_CucsFcNicIfConfigTable_Object((1,3,6,1,4,1,9,9,719,1,20,3))
if mibBuilder.loadTexts:cucsFcNicIfConfigTable.setStatus(_A)
_CucsFcNicIfConfigEntry_Object=MibTableRow
cucsFcNicIfConfigEntry=_CucsFcNicIfConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,20,3,1))
cucsFcNicIfConfigEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsFcNicIfConfigEntry.setStatus(_A)
_CucsFcNicIfConfigInstanceId_Type=CucsManagedObjectId
_CucsFcNicIfConfigInstanceId_Object=MibTableColumn
cucsFcNicIfConfigInstanceId=_CucsFcNicIfConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,3,1,1),_CucsFcNicIfConfigInstanceId_Type())
cucsFcNicIfConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcNicIfConfigInstanceId.setStatus(_A)
_CucsFcNicIfConfigDn_Type=CucsManagedObjectDn
_CucsFcNicIfConfigDn_Object=MibTableColumn
cucsFcNicIfConfigDn=_CucsFcNicIfConfigDn_Object((1,3,6,1,4,1,9,9,719,1,20,3,1,2),_CucsFcNicIfConfigDn_Type())
cucsFcNicIfConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcNicIfConfigDn.setStatus(_A)
_CucsFcNicIfConfigRn_Type=SnmpAdminString
_CucsFcNicIfConfigRn_Object=MibTableColumn
cucsFcNicIfConfigRn=_CucsFcNicIfConfigRn_Object((1,3,6,1,4,1,9,9,719,1,20,3,1,3),_CucsFcNicIfConfigRn_Type())
cucsFcNicIfConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcNicIfConfigRn.setStatus(_A)
_CucsFcPIoTable_Object=MibTable
cucsFcPIoTable=_CucsFcPIoTable_Object((1,3,6,1,4,1,9,9,719,1,20,4))
if mibBuilder.loadTexts:cucsFcPIoTable.setStatus(_A)
_CucsFcPIoEntry_Object=MibTableRow
cucsFcPIoEntry=_CucsFcPIoEntry_Object((1,3,6,1,4,1,9,9,719,1,20,4,1))
cucsFcPIoEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsFcPIoEntry.setStatus(_A)
_CucsFcPIoInstanceId_Type=CucsManagedObjectId
_CucsFcPIoInstanceId_Object=MibTableColumn
cucsFcPIoInstanceId=_CucsFcPIoInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,1),_CucsFcPIoInstanceId_Type())
cucsFcPIoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcPIoInstanceId.setStatus(_A)
_CucsFcPIoDn_Type=CucsManagedObjectDn
_CucsFcPIoDn_Object=MibTableColumn
cucsFcPIoDn=_CucsFcPIoDn_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,2),_CucsFcPIoDn_Type())
cucsFcPIoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoDn.setStatus(_A)
_CucsFcPIoRn_Type=SnmpAdminString
_CucsFcPIoRn_Object=MibTableColumn
cucsFcPIoRn=_CucsFcPIoRn_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,3),_CucsFcPIoRn_Type())
cucsFcPIoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoRn.setStatus(_A)
_CucsFcPIoAdminState_Type=CucsFabricAdminState
_CucsFcPIoAdminState_Object=MibTableColumn
cucsFcPIoAdminState=_CucsFcPIoAdminState_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,4),_CucsFcPIoAdminState_Type())
cucsFcPIoAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoAdminState.setStatus(_A)
_CucsFcPIoChassisId_Type=Gauge32
_CucsFcPIoChassisId_Object=MibTableColumn
cucsFcPIoChassisId=_CucsFcPIoChassisId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,5),_CucsFcPIoChassisId_Type())
cucsFcPIoChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoChassisId.setStatus(_A)
_CucsFcPIoEncap_Type=CucsPortEncap
_CucsFcPIoEncap_Object=MibTableColumn
cucsFcPIoEncap=_CucsFcPIoEncap_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,6),_CucsFcPIoEncap_Type())
cucsFcPIoEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoEncap.setStatus(_A)
_CucsFcPIoEpDn_Type=SnmpAdminString
_CucsFcPIoEpDn_Object=MibTableColumn
cucsFcPIoEpDn=_CucsFcPIoEpDn_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,7),_CucsFcPIoEpDn_Type())
cucsFcPIoEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoEpDn.setStatus(_A)
_CucsFcPIoFltAggr_Type=Unsigned64
_CucsFcPIoFltAggr_Object=MibTableColumn
cucsFcPIoFltAggr=_CucsFcPIoFltAggr_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,8),_CucsFcPIoFltAggr_Type())
cucsFcPIoFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFltAggr.setStatus(_A)
_CucsFcPIoIfRole_Type=CucsNetworkPortRole
_CucsFcPIoIfRole_Object=MibTableColumn
cucsFcPIoIfRole=_CucsFcPIoIfRole_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,9),_CucsFcPIoIfRole_Type())
cucsFcPIoIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoIfRole.setStatus(_A)
_CucsFcPIoIfType_Type=CucsNetworkPhysEpIfType
_CucsFcPIoIfType_Object=MibTableColumn
cucsFcPIoIfType=_CucsFcPIoIfType_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,10),_CucsFcPIoIfType_Type())
cucsFcPIoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoIfType.setStatus(_A)
_CucsFcPIoLocale_Type=CucsNetworkLocale
_CucsFcPIoLocale_Object=MibTableColumn
cucsFcPIoLocale=_CucsFcPIoLocale_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,11),_CucsFcPIoLocale_Type())
cucsFcPIoLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoLocale.setStatus(_A)
_CucsFcPIoMode_Type=CucsPortMode
_CucsFcPIoMode_Object=MibTableColumn
cucsFcPIoMode=_CucsFcPIoMode_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,12),_CucsFcPIoMode_Type())
cucsFcPIoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoMode.setStatus(_A)
_CucsFcPIoModel_Type=SnmpAdminString
_CucsFcPIoModel_Object=MibTableColumn
cucsFcPIoModel=_CucsFcPIoModel_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,13),_CucsFcPIoModel_Type())
cucsFcPIoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoModel.setStatus(_A)
_CucsFcPIoName_Type=SnmpAdminString
_CucsFcPIoName_Object=MibTableColumn
cucsFcPIoName=_CucsFcPIoName_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,14),_CucsFcPIoName_Type())
cucsFcPIoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoName.setStatus(_A)
_CucsFcPIoOperSpeed_Type=CucsPortSpeed
_CucsFcPIoOperSpeed_Object=MibTableColumn
cucsFcPIoOperSpeed=_CucsFcPIoOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,15),_CucsFcPIoOperSpeed_Type())
cucsFcPIoOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoOperSpeed.setStatus(_A)
_CucsFcPIoOperState_Type=CucsNetworkPortOperState
_CucsFcPIoOperState_Object=MibTableColumn
cucsFcPIoOperState=_CucsFcPIoOperState_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,16),_CucsFcPIoOperState_Type())
cucsFcPIoOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoOperState.setStatus(_A)
_CucsFcPIoPeerDn_Type=SnmpAdminString
_CucsFcPIoPeerDn_Object=MibTableColumn
cucsFcPIoPeerDn=_CucsFcPIoPeerDn_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,17),_CucsFcPIoPeerDn_Type())
cucsFcPIoPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPeerDn.setStatus(_A)
_CucsFcPIoPeerPortId_Type=Gauge32
_CucsFcPIoPeerPortId_Object=MibTableColumn
cucsFcPIoPeerPortId=_CucsFcPIoPeerPortId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,18),_CucsFcPIoPeerPortId_Type())
cucsFcPIoPeerPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPeerPortId.setStatus(_A)
_CucsFcPIoPeerSlotId_Type=Gauge32
_CucsFcPIoPeerSlotId_Object=MibTableColumn
cucsFcPIoPeerSlotId=_CucsFcPIoPeerSlotId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,19),_CucsFcPIoPeerSlotId_Type())
cucsFcPIoPeerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPeerSlotId.setStatus(_A)
_CucsFcPIoPortId_Type=Gauge32
_CucsFcPIoPortId_Object=MibTableColumn
cucsFcPIoPortId=_CucsFcPIoPortId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,20),_CucsFcPIoPortId_Type())
cucsFcPIoPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPortId.setStatus(_A)
_CucsFcPIoRevision_Type=SnmpAdminString
_CucsFcPIoRevision_Object=MibTableColumn
cucsFcPIoRevision=_CucsFcPIoRevision_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,21),_CucsFcPIoRevision_Type())
cucsFcPIoRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoRevision.setStatus(_A)
_CucsFcPIoSerial_Type=SnmpAdminString
_CucsFcPIoSerial_Object=MibTableColumn
cucsFcPIoSerial=_CucsFcPIoSerial_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,22),_CucsFcPIoSerial_Type())
cucsFcPIoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoSerial.setStatus(_A)
_CucsFcPIoSlotId_Type=Gauge32
_CucsFcPIoSlotId_Object=MibTableColumn
cucsFcPIoSlotId=_CucsFcPIoSlotId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,23),_CucsFcPIoSlotId_Type())
cucsFcPIoSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoSlotId.setStatus(_A)
_CucsFcPIoStateQual_Type=SnmpAdminString
_CucsFcPIoStateQual_Object=MibTableColumn
cucsFcPIoStateQual=_CucsFcPIoStateQual_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,24),_CucsFcPIoStateQual_Type())
cucsFcPIoStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoStateQual.setStatus(_A)
_CucsFcPIoSwitchId_Type=CucsNetworkSwitchId
_CucsFcPIoSwitchId_Object=MibTableColumn
cucsFcPIoSwitchId=_CucsFcPIoSwitchId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,25),_CucsFcPIoSwitchId_Type())
cucsFcPIoSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoSwitchId.setStatus(_A)
_CucsFcPIoTransport_Type=CucsNetworkTransport
_CucsFcPIoTransport_Object=MibTableColumn
cucsFcPIoTransport=_CucsFcPIoTransport_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,26),_CucsFcPIoTransport_Type())
cucsFcPIoTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoTransport.setStatus(_A)
_CucsFcPIoTs_Type=DateAndTime
_CucsFcPIoTs_Object=MibTableColumn
cucsFcPIoTs=_CucsFcPIoTs_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,27),_CucsFcPIoTs_Type())
cucsFcPIoTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoTs.setStatus(_A)
_CucsFcPIoType_Type=CucsNetworkConnectionType
_CucsFcPIoType_Object=MibTableColumn
cucsFcPIoType=_CucsFcPIoType_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,28),_CucsFcPIoType_Type())
cucsFcPIoType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoType.setStatus(_A)
_CucsFcPIoUsrLbl_Type=SnmpAdminString
_CucsFcPIoUsrLbl_Object=MibTableColumn
cucsFcPIoUsrLbl=_CucsFcPIoUsrLbl_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,29),_CucsFcPIoUsrLbl_Type())
cucsFcPIoUsrLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoUsrLbl.setStatus(_A)
_CucsFcPIoVendor_Type=SnmpAdminString
_CucsFcPIoVendor_Object=MibTableColumn
cucsFcPIoVendor=_CucsFcPIoVendor_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,30),_CucsFcPIoVendor_Type())
cucsFcPIoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoVendor.setStatus(_A)
_CucsFcPIoWwn_Type=Unsigned64
_CucsFcPIoWwn_Object=MibTableColumn
cucsFcPIoWwn=_CucsFcPIoWwn_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,31),_CucsFcPIoWwn_Type())
cucsFcPIoWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoWwn.setStatus(_A)
_CucsFcPIoFsmDescr_Type=SnmpAdminString
_CucsFcPIoFsmDescr_Object=MibTableColumn
cucsFcPIoFsmDescr=_CucsFcPIoFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,32),_CucsFcPIoFsmDescr_Type())
cucsFcPIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmDescr.setStatus(_A)
_CucsFcPIoFsmPrev_Type=SnmpAdminString
_CucsFcPIoFsmPrev_Object=MibTableColumn
cucsFcPIoFsmPrev=_CucsFcPIoFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,33),_CucsFcPIoFsmPrev_Type())
cucsFcPIoFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmPrev.setStatus(_A)
_CucsFcPIoFsmProgr_Type=Gauge32
_CucsFcPIoFsmProgr_Object=MibTableColumn
cucsFcPIoFsmProgr=_CucsFcPIoFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,34),_CucsFcPIoFsmProgr_Type())
cucsFcPIoFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmProgr.setStatus(_A)
_CucsFcPIoFsmRmtInvErrCode_Type=Gauge32
_CucsFcPIoFsmRmtInvErrCode_Object=MibTableColumn
cucsFcPIoFsmRmtInvErrCode=_CucsFcPIoFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,35),_CucsFcPIoFsmRmtInvErrCode_Type())
cucsFcPIoFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRmtInvErrCode.setStatus(_A)
_CucsFcPIoFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsFcPIoFsmRmtInvErrDescr_Object=MibTableColumn
cucsFcPIoFsmRmtInvErrDescr=_CucsFcPIoFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,36),_CucsFcPIoFsmRmtInvErrDescr_Type())
cucsFcPIoFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRmtInvErrDescr.setStatus(_A)
_CucsFcPIoFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsFcPIoFsmRmtInvRslt_Object=MibTableColumn
cucsFcPIoFsmRmtInvRslt=_CucsFcPIoFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,37),_CucsFcPIoFsmRmtInvRslt_Type())
cucsFcPIoFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRmtInvRslt.setStatus(_A)
_CucsFcPIoFsmStageDescr_Type=SnmpAdminString
_CucsFcPIoFsmStageDescr_Object=MibTableColumn
cucsFcPIoFsmStageDescr=_CucsFcPIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,38),_CucsFcPIoFsmStageDescr_Type())
cucsFcPIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageDescr.setStatus(_A)
_CucsFcPIoFsmStamp_Type=DateAndTime
_CucsFcPIoFsmStamp_Object=MibTableColumn
cucsFcPIoFsmStamp=_CucsFcPIoFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,39),_CucsFcPIoFsmStamp_Type())
cucsFcPIoFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStamp.setStatus(_A)
_CucsFcPIoFsmStatus_Type=SnmpAdminString
_CucsFcPIoFsmStatus_Object=MibTableColumn
cucsFcPIoFsmStatus=_CucsFcPIoFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,40),_CucsFcPIoFsmStatus_Type())
cucsFcPIoFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStatus.setStatus(_A)
_CucsFcPIoFsmTry_Type=Gauge32
_CucsFcPIoFsmTry_Object=MibTableColumn
cucsFcPIoFsmTry=_CucsFcPIoFsmTry_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,41),_CucsFcPIoFsmTry_Type())
cucsFcPIoFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmTry.setStatus(_A)
_CucsFcPIoLicGP_Type=Unsigned64
_CucsFcPIoLicGP_Object=MibTableColumn
cucsFcPIoLicGP=_CucsFcPIoLicGP_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,42),_CucsFcPIoLicGP_Type())
cucsFcPIoLicGP.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoLicGP.setStatus(_A)
_CucsFcPIoLicState_Type=CucsLicenseState
_CucsFcPIoLicState_Object=MibTableColumn
cucsFcPIoLicState=_CucsFcPIoLicState_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,43),_CucsFcPIoLicState_Type())
cucsFcPIoLicState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoLicState.setStatus(_A)
_CucsFcPIoXcvrType_Type=CucsEquipmentXcvrType
_CucsFcPIoXcvrType_Object=MibTableColumn
cucsFcPIoXcvrType=_CucsFcPIoXcvrType_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,44),_CucsFcPIoXcvrType_Type())
cucsFcPIoXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoXcvrType.setStatus(_A)
_CucsFcPIoPeerChassisId_Type=Gauge32
_CucsFcPIoPeerChassisId_Object=MibTableColumn
cucsFcPIoPeerChassisId=_CucsFcPIoPeerChassisId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,45),_CucsFcPIoPeerChassisId_Type())
cucsFcPIoPeerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPeerChassisId.setStatus(_A)
_CucsFcPIoAdminTransport_Type=CucsNetworkTransport
_CucsFcPIoAdminTransport_Object=MibTableColumn
cucsFcPIoAdminTransport=_CucsFcPIoAdminTransport_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,46),_CucsFcPIoAdminTransport_Type())
cucsFcPIoAdminTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoAdminTransport.setStatus(_A)
_CucsFcPIoLc_Type=CucsFsmLifecycle
_CucsFcPIoLc_Object=MibTableColumn
cucsFcPIoLc=_CucsFcPIoLc_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,47),_CucsFcPIoLc_Type())
cucsFcPIoLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoLc.setStatus(_A)
_CucsFcPIoUnifiedPort_Type=TruthValue
_CucsFcPIoUnifiedPort_Object=MibTableColumn
cucsFcPIoUnifiedPort=_CucsFcPIoUnifiedPort_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,48),_CucsFcPIoUnifiedPort_Type())
cucsFcPIoUnifiedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoUnifiedPort.setStatus(_A)
_CucsFcPIoMaxSpeed_Type=CucsPortSpeed
_CucsFcPIoMaxSpeed_Object=MibTableColumn
cucsFcPIoMaxSpeed=_CucsFcPIoMaxSpeed_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,49),_CucsFcPIoMaxSpeed_Type())
cucsFcPIoMaxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoMaxSpeed.setStatus(_A)
_CucsFcPIoIsPortChannelMember_Type=TruthValue
_CucsFcPIoIsPortChannelMember_Object=MibTableColumn
cucsFcPIoIsPortChannelMember=_CucsFcPIoIsPortChannelMember_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,50),_CucsFcPIoIsPortChannelMember_Type())
cucsFcPIoIsPortChannelMember.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoIsPortChannelMember.setStatus(_A)
_CucsFcPIoAggrPortId_Type=Gauge32
_CucsFcPIoAggrPortId_Object=MibTableColumn
cucsFcPIoAggrPortId=_CucsFcPIoAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,51),_CucsFcPIoAggrPortId_Type())
cucsFcPIoAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoAggrPortId.setStatus(_A)
_CucsFcPIoPeerAggrPortId_Type=Gauge32
_CucsFcPIoPeerAggrPortId_Object=MibTableColumn
cucsFcPIoPeerAggrPortId=_CucsFcPIoPeerAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,52),_CucsFcPIoPeerAggrPortId_Type())
cucsFcPIoPeerAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPeerAggrPortId.setStatus(_A)
_CucsFcPIoIsBreakoutXcvr_Type=TruthValue
_CucsFcPIoIsBreakoutXcvr_Object=MibTableColumn
cucsFcPIoIsBreakoutXcvr=_CucsFcPIoIsBreakoutXcvr_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,53),_CucsFcPIoIsBreakoutXcvr_Type())
cucsFcPIoIsBreakoutXcvr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoIsBreakoutXcvr.setStatus(_A)
_CucsFcPIoPortCapability_Type=CucsPortapiPeerCapability
_CucsFcPIoPortCapability_Object=MibTableColumn
cucsFcPIoPortCapability=_CucsFcPIoPortCapability_Object((1,3,6,1,4,1,9,9,719,1,20,4,1,54),_CucsFcPIoPortCapability_Type())
cucsFcPIoPortCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoPortCapability.setStatus(_A)
_CucsFcStatsTable_Object=MibTable
cucsFcStatsTable=_CucsFcStatsTable_Object((1,3,6,1,4,1,9,9,719,1,20,5))
if mibBuilder.loadTexts:cucsFcStatsTable.setStatus(_A)
_CucsFcStatsEntry_Object=MibTableRow
cucsFcStatsEntry=_CucsFcStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,20,5,1))
cucsFcStatsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsFcStatsEntry.setStatus(_A)
_CucsFcStatsInstanceId_Type=CucsManagedObjectId
_CucsFcStatsInstanceId_Object=MibTableColumn
cucsFcStatsInstanceId=_CucsFcStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,1),_CucsFcStatsInstanceId_Type())
cucsFcStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcStatsInstanceId.setStatus(_A)
_CucsFcStatsDn_Type=CucsManagedObjectDn
_CucsFcStatsDn_Object=MibTableColumn
cucsFcStatsDn=_CucsFcStatsDn_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,2),_CucsFcStatsDn_Type())
cucsFcStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsDn.setStatus(_A)
_CucsFcStatsRn_Type=SnmpAdminString
_CucsFcStatsRn_Object=MibTableColumn
cucsFcStatsRn=_CucsFcStatsRn_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,3),_CucsFcStatsRn_Type())
cucsFcStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsRn.setStatus(_A)
_CucsFcStatsBytesRx_Type=Unsigned64
_CucsFcStatsBytesRx_Object=MibTableColumn
cucsFcStatsBytesRx=_CucsFcStatsBytesRx_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,4),_CucsFcStatsBytesRx_Type())
cucsFcStatsBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesRx.setStatus(_A)
_CucsFcStatsBytesRxDelta_Type=Counter64
_CucsFcStatsBytesRxDelta_Object=MibTableColumn
cucsFcStatsBytesRxDelta=_CucsFcStatsBytesRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,5),_CucsFcStatsBytesRxDelta_Type())
cucsFcStatsBytesRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesRxDelta.setStatus(_A)
_CucsFcStatsBytesRxDeltaAvg_Type=Unsigned64
_CucsFcStatsBytesRxDeltaAvg_Object=MibTableColumn
cucsFcStatsBytesRxDeltaAvg=_CucsFcStatsBytesRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,6),_CucsFcStatsBytesRxDeltaAvg_Type())
cucsFcStatsBytesRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesRxDeltaAvg.setStatus(_A)
_CucsFcStatsBytesRxDeltaMax_Type=Unsigned64
_CucsFcStatsBytesRxDeltaMax_Object=MibTableColumn
cucsFcStatsBytesRxDeltaMax=_CucsFcStatsBytesRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,7),_CucsFcStatsBytesRxDeltaMax_Type())
cucsFcStatsBytesRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesRxDeltaMax.setStatus(_A)
_CucsFcStatsBytesRxDeltaMin_Type=Unsigned64
_CucsFcStatsBytesRxDeltaMin_Object=MibTableColumn
cucsFcStatsBytesRxDeltaMin=_CucsFcStatsBytesRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,8),_CucsFcStatsBytesRxDeltaMin_Type())
cucsFcStatsBytesRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesRxDeltaMin.setStatus(_A)
_CucsFcStatsBytesTx_Type=Unsigned64
_CucsFcStatsBytesTx_Object=MibTableColumn
cucsFcStatsBytesTx=_CucsFcStatsBytesTx_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,9),_CucsFcStatsBytesTx_Type())
cucsFcStatsBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesTx.setStatus(_A)
_CucsFcStatsBytesTxDelta_Type=Counter64
_CucsFcStatsBytesTxDelta_Object=MibTableColumn
cucsFcStatsBytesTxDelta=_CucsFcStatsBytesTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,10),_CucsFcStatsBytesTxDelta_Type())
cucsFcStatsBytesTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesTxDelta.setStatus(_A)
_CucsFcStatsBytesTxDeltaAvg_Type=Unsigned64
_CucsFcStatsBytesTxDeltaAvg_Object=MibTableColumn
cucsFcStatsBytesTxDeltaAvg=_CucsFcStatsBytesTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,11),_CucsFcStatsBytesTxDeltaAvg_Type())
cucsFcStatsBytesTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesTxDeltaAvg.setStatus(_A)
_CucsFcStatsBytesTxDeltaMax_Type=Unsigned64
_CucsFcStatsBytesTxDeltaMax_Object=MibTableColumn
cucsFcStatsBytesTxDeltaMax=_CucsFcStatsBytesTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,12),_CucsFcStatsBytesTxDeltaMax_Type())
cucsFcStatsBytesTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesTxDeltaMax.setStatus(_A)
_CucsFcStatsBytesTxDeltaMin_Type=Unsigned64
_CucsFcStatsBytesTxDeltaMin_Object=MibTableColumn
cucsFcStatsBytesTxDeltaMin=_CucsFcStatsBytesTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,13),_CucsFcStatsBytesTxDeltaMin_Type())
cucsFcStatsBytesTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsBytesTxDeltaMin.setStatus(_A)
_CucsFcStatsIntervals_Type=Gauge32
_CucsFcStatsIntervals_Object=MibTableColumn
cucsFcStatsIntervals=_CucsFcStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,14),_CucsFcStatsIntervals_Type())
cucsFcStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsIntervals.setStatus(_A)
_CucsFcStatsPacketsRx_Type=Unsigned64
_CucsFcStatsPacketsRx_Object=MibTableColumn
cucsFcStatsPacketsRx=_CucsFcStatsPacketsRx_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,15),_CucsFcStatsPacketsRx_Type())
cucsFcStatsPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsRx.setStatus(_A)
_CucsFcStatsPacketsRxDelta_Type=Counter64
_CucsFcStatsPacketsRxDelta_Object=MibTableColumn
cucsFcStatsPacketsRxDelta=_CucsFcStatsPacketsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,16),_CucsFcStatsPacketsRxDelta_Type())
cucsFcStatsPacketsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsRxDelta.setStatus(_A)
_CucsFcStatsPacketsRxDeltaAvg_Type=Unsigned64
_CucsFcStatsPacketsRxDeltaAvg_Object=MibTableColumn
cucsFcStatsPacketsRxDeltaAvg=_CucsFcStatsPacketsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,17),_CucsFcStatsPacketsRxDeltaAvg_Type())
cucsFcStatsPacketsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsRxDeltaAvg.setStatus(_A)
_CucsFcStatsPacketsRxDeltaMax_Type=Unsigned64
_CucsFcStatsPacketsRxDeltaMax_Object=MibTableColumn
cucsFcStatsPacketsRxDeltaMax=_CucsFcStatsPacketsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,18),_CucsFcStatsPacketsRxDeltaMax_Type())
cucsFcStatsPacketsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsRxDeltaMax.setStatus(_A)
_CucsFcStatsPacketsRxDeltaMin_Type=Unsigned64
_CucsFcStatsPacketsRxDeltaMin_Object=MibTableColumn
cucsFcStatsPacketsRxDeltaMin=_CucsFcStatsPacketsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,19),_CucsFcStatsPacketsRxDeltaMin_Type())
cucsFcStatsPacketsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsRxDeltaMin.setStatus(_A)
_CucsFcStatsPacketsTx_Type=Unsigned64
_CucsFcStatsPacketsTx_Object=MibTableColumn
cucsFcStatsPacketsTx=_CucsFcStatsPacketsTx_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,20),_CucsFcStatsPacketsTx_Type())
cucsFcStatsPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsTx.setStatus(_A)
_CucsFcStatsPacketsTxDelta_Type=Counter64
_CucsFcStatsPacketsTxDelta_Object=MibTableColumn
cucsFcStatsPacketsTxDelta=_CucsFcStatsPacketsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,21),_CucsFcStatsPacketsTxDelta_Type())
cucsFcStatsPacketsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsTxDelta.setStatus(_A)
_CucsFcStatsPacketsTxDeltaAvg_Type=Unsigned64
_CucsFcStatsPacketsTxDeltaAvg_Object=MibTableColumn
cucsFcStatsPacketsTxDeltaAvg=_CucsFcStatsPacketsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,22),_CucsFcStatsPacketsTxDeltaAvg_Type())
cucsFcStatsPacketsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsTxDeltaAvg.setStatus(_A)
_CucsFcStatsPacketsTxDeltaMax_Type=Unsigned64
_CucsFcStatsPacketsTxDeltaMax_Object=MibTableColumn
cucsFcStatsPacketsTxDeltaMax=_CucsFcStatsPacketsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,23),_CucsFcStatsPacketsTxDeltaMax_Type())
cucsFcStatsPacketsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsTxDeltaMax.setStatus(_A)
_CucsFcStatsPacketsTxDeltaMin_Type=Unsigned64
_CucsFcStatsPacketsTxDeltaMin_Object=MibTableColumn
cucsFcStatsPacketsTxDeltaMin=_CucsFcStatsPacketsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,24),_CucsFcStatsPacketsTxDeltaMin_Type())
cucsFcStatsPacketsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsPacketsTxDeltaMin.setStatus(_A)
_CucsFcStatsSuspect_Type=TruthValue
_CucsFcStatsSuspect_Object=MibTableColumn
cucsFcStatsSuspect=_CucsFcStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,25),_CucsFcStatsSuspect_Type())
cucsFcStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsSuspect.setStatus(_A)
_CucsFcStatsThresholded_Type=CucsFcStatsThresholded
_CucsFcStatsThresholded_Object=MibTableColumn
cucsFcStatsThresholded=_CucsFcStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,26),_CucsFcStatsThresholded_Type())
cucsFcStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsThresholded.setStatus(_A)
_CucsFcStatsTimeCollected_Type=DateAndTime
_CucsFcStatsTimeCollected_Object=MibTableColumn
cucsFcStatsTimeCollected=_CucsFcStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,27),_CucsFcStatsTimeCollected_Type())
cucsFcStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsTimeCollected.setStatus(_A)
_CucsFcStatsUpdate_Type=Gauge32
_CucsFcStatsUpdate_Object=MibTableColumn
cucsFcStatsUpdate=_CucsFcStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,20,5,1,28),_CucsFcStatsUpdate_Type())
cucsFcStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsUpdate.setStatus(_A)
_CucsFcStatsHistTable_Object=MibTable
cucsFcStatsHistTable=_CucsFcStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,20,6))
if mibBuilder.loadTexts:cucsFcStatsHistTable.setStatus(_A)
_CucsFcStatsHistEntry_Object=MibTableRow
cucsFcStatsHistEntry=_CucsFcStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,20,6,1))
cucsFcStatsHistEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsFcStatsHistEntry.setStatus(_A)
_CucsFcStatsHistInstanceId_Type=CucsManagedObjectId
_CucsFcStatsHistInstanceId_Object=MibTableColumn
cucsFcStatsHistInstanceId=_CucsFcStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,1),_CucsFcStatsHistInstanceId_Type())
cucsFcStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcStatsHistInstanceId.setStatus(_A)
_CucsFcStatsHistDn_Type=CucsManagedObjectDn
_CucsFcStatsHistDn_Object=MibTableColumn
cucsFcStatsHistDn=_CucsFcStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,2),_CucsFcStatsHistDn_Type())
cucsFcStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistDn.setStatus(_A)
_CucsFcStatsHistRn_Type=SnmpAdminString
_CucsFcStatsHistRn_Object=MibTableColumn
cucsFcStatsHistRn=_CucsFcStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,3),_CucsFcStatsHistRn_Type())
cucsFcStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistRn.setStatus(_A)
_CucsFcStatsHistBytesRx_Type=Unsigned64
_CucsFcStatsHistBytesRx_Object=MibTableColumn
cucsFcStatsHistBytesRx=_CucsFcStatsHistBytesRx_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,4),_CucsFcStatsHistBytesRx_Type())
cucsFcStatsHistBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesRx.setStatus(_A)
_CucsFcStatsHistBytesRxDelta_Type=Unsigned64
_CucsFcStatsHistBytesRxDelta_Object=MibTableColumn
cucsFcStatsHistBytesRxDelta=_CucsFcStatsHistBytesRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,5),_CucsFcStatsHistBytesRxDelta_Type())
cucsFcStatsHistBytesRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesRxDelta.setStatus(_A)
_CucsFcStatsHistBytesRxDeltaAvg_Type=Unsigned64
_CucsFcStatsHistBytesRxDeltaAvg_Object=MibTableColumn
cucsFcStatsHistBytesRxDeltaAvg=_CucsFcStatsHistBytesRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,6),_CucsFcStatsHistBytesRxDeltaAvg_Type())
cucsFcStatsHistBytesRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesRxDeltaAvg.setStatus(_A)
_CucsFcStatsHistBytesRxDeltaMax_Type=Unsigned64
_CucsFcStatsHistBytesRxDeltaMax_Object=MibTableColumn
cucsFcStatsHistBytesRxDeltaMax=_CucsFcStatsHistBytesRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,7),_CucsFcStatsHistBytesRxDeltaMax_Type())
cucsFcStatsHistBytesRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesRxDeltaMax.setStatus(_A)
_CucsFcStatsHistBytesRxDeltaMin_Type=Unsigned64
_CucsFcStatsHistBytesRxDeltaMin_Object=MibTableColumn
cucsFcStatsHistBytesRxDeltaMin=_CucsFcStatsHistBytesRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,8),_CucsFcStatsHistBytesRxDeltaMin_Type())
cucsFcStatsHistBytesRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesRxDeltaMin.setStatus(_A)
_CucsFcStatsHistBytesTx_Type=Unsigned64
_CucsFcStatsHistBytesTx_Object=MibTableColumn
cucsFcStatsHistBytesTx=_CucsFcStatsHistBytesTx_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,9),_CucsFcStatsHistBytesTx_Type())
cucsFcStatsHistBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesTx.setStatus(_A)
_CucsFcStatsHistBytesTxDelta_Type=Unsigned64
_CucsFcStatsHistBytesTxDelta_Object=MibTableColumn
cucsFcStatsHistBytesTxDelta=_CucsFcStatsHistBytesTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,10),_CucsFcStatsHistBytesTxDelta_Type())
cucsFcStatsHistBytesTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesTxDelta.setStatus(_A)
_CucsFcStatsHistBytesTxDeltaAvg_Type=Unsigned64
_CucsFcStatsHistBytesTxDeltaAvg_Object=MibTableColumn
cucsFcStatsHistBytesTxDeltaAvg=_CucsFcStatsHistBytesTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,11),_CucsFcStatsHistBytesTxDeltaAvg_Type())
cucsFcStatsHistBytesTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesTxDeltaAvg.setStatus(_A)
_CucsFcStatsHistBytesTxDeltaMax_Type=Unsigned64
_CucsFcStatsHistBytesTxDeltaMax_Object=MibTableColumn
cucsFcStatsHistBytesTxDeltaMax=_CucsFcStatsHistBytesTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,12),_CucsFcStatsHistBytesTxDeltaMax_Type())
cucsFcStatsHistBytesTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesTxDeltaMax.setStatus(_A)
_CucsFcStatsHistBytesTxDeltaMin_Type=Unsigned64
_CucsFcStatsHistBytesTxDeltaMin_Object=MibTableColumn
cucsFcStatsHistBytesTxDeltaMin=_CucsFcStatsHistBytesTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,13),_CucsFcStatsHistBytesTxDeltaMin_Type())
cucsFcStatsHistBytesTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistBytesTxDeltaMin.setStatus(_A)
_CucsFcStatsHistId_Type=Unsigned64
_CucsFcStatsHistId_Object=MibTableColumn
cucsFcStatsHistId=_CucsFcStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,14),_CucsFcStatsHistId_Type())
cucsFcStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistId.setStatus(_A)
_CucsFcStatsHistMostRecent_Type=TruthValue
_CucsFcStatsHistMostRecent_Object=MibTableColumn
cucsFcStatsHistMostRecent=_CucsFcStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,15),_CucsFcStatsHistMostRecent_Type())
cucsFcStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistMostRecent.setStatus(_A)
_CucsFcStatsHistPacketsRx_Type=Unsigned64
_CucsFcStatsHistPacketsRx_Object=MibTableColumn
cucsFcStatsHistPacketsRx=_CucsFcStatsHistPacketsRx_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,16),_CucsFcStatsHistPacketsRx_Type())
cucsFcStatsHistPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsRx.setStatus(_A)
_CucsFcStatsHistPacketsRxDelta_Type=Unsigned64
_CucsFcStatsHistPacketsRxDelta_Object=MibTableColumn
cucsFcStatsHistPacketsRxDelta=_CucsFcStatsHistPacketsRxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,17),_CucsFcStatsHistPacketsRxDelta_Type())
cucsFcStatsHistPacketsRxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsRxDelta.setStatus(_A)
_CucsFcStatsHistPacketsRxDeltaAvg_Type=Unsigned64
_CucsFcStatsHistPacketsRxDeltaAvg_Object=MibTableColumn
cucsFcStatsHistPacketsRxDeltaAvg=_CucsFcStatsHistPacketsRxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,18),_CucsFcStatsHistPacketsRxDeltaAvg_Type())
cucsFcStatsHistPacketsRxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsRxDeltaAvg.setStatus(_A)
_CucsFcStatsHistPacketsRxDeltaMax_Type=Unsigned64
_CucsFcStatsHistPacketsRxDeltaMax_Object=MibTableColumn
cucsFcStatsHistPacketsRxDeltaMax=_CucsFcStatsHistPacketsRxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,19),_CucsFcStatsHistPacketsRxDeltaMax_Type())
cucsFcStatsHistPacketsRxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsRxDeltaMax.setStatus(_A)
_CucsFcStatsHistPacketsRxDeltaMin_Type=Unsigned64
_CucsFcStatsHistPacketsRxDeltaMin_Object=MibTableColumn
cucsFcStatsHistPacketsRxDeltaMin=_CucsFcStatsHistPacketsRxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,20),_CucsFcStatsHistPacketsRxDeltaMin_Type())
cucsFcStatsHistPacketsRxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsRxDeltaMin.setStatus(_A)
_CucsFcStatsHistPacketsTx_Type=Unsigned64
_CucsFcStatsHistPacketsTx_Object=MibTableColumn
cucsFcStatsHistPacketsTx=_CucsFcStatsHistPacketsTx_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,21),_CucsFcStatsHistPacketsTx_Type())
cucsFcStatsHistPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsTx.setStatus(_A)
_CucsFcStatsHistPacketsTxDelta_Type=Unsigned64
_CucsFcStatsHistPacketsTxDelta_Object=MibTableColumn
cucsFcStatsHistPacketsTxDelta=_CucsFcStatsHistPacketsTxDelta_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,22),_CucsFcStatsHistPacketsTxDelta_Type())
cucsFcStatsHistPacketsTxDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsTxDelta.setStatus(_A)
_CucsFcStatsHistPacketsTxDeltaAvg_Type=Unsigned64
_CucsFcStatsHistPacketsTxDeltaAvg_Object=MibTableColumn
cucsFcStatsHistPacketsTxDeltaAvg=_CucsFcStatsHistPacketsTxDeltaAvg_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,23),_CucsFcStatsHistPacketsTxDeltaAvg_Type())
cucsFcStatsHistPacketsTxDeltaAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsTxDeltaAvg.setStatus(_A)
_CucsFcStatsHistPacketsTxDeltaMax_Type=Unsigned64
_CucsFcStatsHistPacketsTxDeltaMax_Object=MibTableColumn
cucsFcStatsHistPacketsTxDeltaMax=_CucsFcStatsHistPacketsTxDeltaMax_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,24),_CucsFcStatsHistPacketsTxDeltaMax_Type())
cucsFcStatsHistPacketsTxDeltaMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsTxDeltaMax.setStatus(_A)
_CucsFcStatsHistPacketsTxDeltaMin_Type=Unsigned64
_CucsFcStatsHistPacketsTxDeltaMin_Object=MibTableColumn
cucsFcStatsHistPacketsTxDeltaMin=_CucsFcStatsHistPacketsTxDeltaMin_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,25),_CucsFcStatsHistPacketsTxDeltaMin_Type())
cucsFcStatsHistPacketsTxDeltaMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistPacketsTxDeltaMin.setStatus(_A)
_CucsFcStatsHistSuspect_Type=TruthValue
_CucsFcStatsHistSuspect_Object=MibTableColumn
cucsFcStatsHistSuspect=_CucsFcStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,26),_CucsFcStatsHistSuspect_Type())
cucsFcStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistSuspect.setStatus(_A)
_CucsFcStatsHistThresholded_Type=CucsFcStatsHistThresholded
_CucsFcStatsHistThresholded_Object=MibTableColumn
cucsFcStatsHistThresholded=_CucsFcStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,27),_CucsFcStatsHistThresholded_Type())
cucsFcStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistThresholded.setStatus(_A)
_CucsFcStatsHistTimeCollected_Type=DateAndTime
_CucsFcStatsHistTimeCollected_Object=MibTableColumn
cucsFcStatsHistTimeCollected=_CucsFcStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,20,6,1,28),_CucsFcStatsHistTimeCollected_Type())
cucsFcStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcStatsHistTimeCollected.setStatus(_A)
_CucsFcSwIfConfigTable_Object=MibTable
cucsFcSwIfConfigTable=_CucsFcSwIfConfigTable_Object((1,3,6,1,4,1,9,9,719,1,20,7))
if mibBuilder.loadTexts:cucsFcSwIfConfigTable.setStatus(_A)
_CucsFcSwIfConfigEntry_Object=MibTableRow
cucsFcSwIfConfigEntry=_CucsFcSwIfConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,20,7,1))
cucsFcSwIfConfigEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsFcSwIfConfigEntry.setStatus(_A)
_CucsFcSwIfConfigInstanceId_Type=CucsManagedObjectId
_CucsFcSwIfConfigInstanceId_Object=MibTableColumn
cucsFcSwIfConfigInstanceId=_CucsFcSwIfConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,7,1,1),_CucsFcSwIfConfigInstanceId_Type())
cucsFcSwIfConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcSwIfConfigInstanceId.setStatus(_A)
_CucsFcSwIfConfigDn_Type=CucsManagedObjectDn
_CucsFcSwIfConfigDn_Object=MibTableColumn
cucsFcSwIfConfigDn=_CucsFcSwIfConfigDn_Object((1,3,6,1,4,1,9,9,719,1,20,7,1,2),_CucsFcSwIfConfigDn_Type())
cucsFcSwIfConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcSwIfConfigDn.setStatus(_A)
_CucsFcSwIfConfigRn_Type=SnmpAdminString
_CucsFcSwIfConfigRn_Object=MibTableColumn
cucsFcSwIfConfigRn=_CucsFcSwIfConfigRn_Object((1,3,6,1,4,1,9,9,719,1,20,7,1,3),_CucsFcSwIfConfigRn_Type())
cucsFcSwIfConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcSwIfConfigRn.setStatus(_A)
_CucsFcPIoFsmTable_Object=MibTable
cucsFcPIoFsmTable=_CucsFcPIoFsmTable_Object((1,3,6,1,4,1,9,9,719,1,20,8))
if mibBuilder.loadTexts:cucsFcPIoFsmTable.setStatus(_A)
_CucsFcPIoFsmEntry_Object=MibTableRow
cucsFcPIoFsmEntry=_CucsFcPIoFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,20,8,1))
cucsFcPIoFsmEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsFcPIoFsmEntry.setStatus(_A)
_CucsFcPIoFsmInstanceId_Type=CucsManagedObjectId
_CucsFcPIoFsmInstanceId_Object=MibTableColumn
cucsFcPIoFsmInstanceId=_CucsFcPIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,1),_CucsFcPIoFsmInstanceId_Type())
cucsFcPIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcPIoFsmInstanceId.setStatus(_A)
_CucsFcPIoFsmDn_Type=CucsManagedObjectDn
_CucsFcPIoFsmDn_Object=MibTableColumn
cucsFcPIoFsmDn=_CucsFcPIoFsmDn_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,2),_CucsFcPIoFsmDn_Type())
cucsFcPIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmDn.setStatus(_A)
_CucsFcPIoFsmRn_Type=SnmpAdminString
_CucsFcPIoFsmRn_Object=MibTableColumn
cucsFcPIoFsmRn=_CucsFcPIoFsmRn_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,3),_CucsFcPIoFsmRn_Type())
cucsFcPIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRn.setStatus(_A)
_CucsFcPIoFsmCompletionTime_Type=DateAndTime
_CucsFcPIoFsmCompletionTime_Object=MibTableColumn
cucsFcPIoFsmCompletionTime=_CucsFcPIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,4),_CucsFcPIoFsmCompletionTime_Type())
cucsFcPIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmCompletionTime.setStatus(_A)
_CucsFcPIoFsmCurrentFsm_Type=CucsFcPIoFsmCurrentFsm
_CucsFcPIoFsmCurrentFsm_Object=MibTableColumn
cucsFcPIoFsmCurrentFsm=_CucsFcPIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,5),_CucsFcPIoFsmCurrentFsm_Type())
cucsFcPIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmCurrentFsm.setStatus(_A)
_CucsFcPIoFsmDescrData_Type=SnmpAdminString
_CucsFcPIoFsmDescrData_Object=MibTableColumn
cucsFcPIoFsmDescrData=_CucsFcPIoFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,6),_CucsFcPIoFsmDescrData_Type())
cucsFcPIoFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmDescrData.setStatus(_A)
_CucsFcPIoFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsFcPIoFsmFsmStatus_Object=MibTableColumn
cucsFcPIoFsmFsmStatus=_CucsFcPIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,7),_CucsFcPIoFsmFsmStatus_Type())
cucsFcPIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmFsmStatus.setStatus(_A)
_CucsFcPIoFsmProgress_Type=Gauge32
_CucsFcPIoFsmProgress_Object=MibTableColumn
cucsFcPIoFsmProgress=_CucsFcPIoFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,8),_CucsFcPIoFsmProgress_Type())
cucsFcPIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmProgress.setStatus(_A)
_CucsFcPIoFsmRmtErrCode_Type=Gauge32
_CucsFcPIoFsmRmtErrCode_Object=MibTableColumn
cucsFcPIoFsmRmtErrCode=_CucsFcPIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,9),_CucsFcPIoFsmRmtErrCode_Type())
cucsFcPIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRmtErrCode.setStatus(_A)
_CucsFcPIoFsmRmtErrDescr_Type=SnmpAdminString
_CucsFcPIoFsmRmtErrDescr_Object=MibTableColumn
cucsFcPIoFsmRmtErrDescr=_CucsFcPIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,10),_CucsFcPIoFsmRmtErrDescr_Type())
cucsFcPIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRmtErrDescr.setStatus(_A)
_CucsFcPIoFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsFcPIoFsmRmtRslt_Object=MibTableColumn
cucsFcPIoFsmRmtRslt=_CucsFcPIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,20,8,1,11),_CucsFcPIoFsmRmtRslt_Type())
cucsFcPIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmRmtRslt.setStatus(_A)
_CucsFcPIoFsmStageTable_Object=MibTable
cucsFcPIoFsmStageTable=_CucsFcPIoFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,20,9))
if mibBuilder.loadTexts:cucsFcPIoFsmStageTable.setStatus(_A)
_CucsFcPIoFsmStageEntry_Object=MibTableRow
cucsFcPIoFsmStageEntry=_CucsFcPIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,20,9,1))
cucsFcPIoFsmStageEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsFcPIoFsmStageEntry.setStatus(_A)
_CucsFcPIoFsmStageInstanceId_Type=CucsManagedObjectId
_CucsFcPIoFsmStageInstanceId_Object=MibTableColumn
cucsFcPIoFsmStageInstanceId=_CucsFcPIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,1),_CucsFcPIoFsmStageInstanceId_Type())
cucsFcPIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcPIoFsmStageInstanceId.setStatus(_A)
_CucsFcPIoFsmStageDn_Type=CucsManagedObjectDn
_CucsFcPIoFsmStageDn_Object=MibTableColumn
cucsFcPIoFsmStageDn=_CucsFcPIoFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,2),_CucsFcPIoFsmStageDn_Type())
cucsFcPIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageDn.setStatus(_A)
_CucsFcPIoFsmStageRn_Type=SnmpAdminString
_CucsFcPIoFsmStageRn_Object=MibTableColumn
cucsFcPIoFsmStageRn=_CucsFcPIoFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,3),_CucsFcPIoFsmStageRn_Type())
cucsFcPIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageRn.setStatus(_A)
_CucsFcPIoFsmStageDescrData_Type=SnmpAdminString
_CucsFcPIoFsmStageDescrData_Object=MibTableColumn
cucsFcPIoFsmStageDescrData=_CucsFcPIoFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,4),_CucsFcPIoFsmStageDescrData_Type())
cucsFcPIoFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageDescrData.setStatus(_A)
_CucsFcPIoFsmStageLastUpdateTime_Type=DateAndTime
_CucsFcPIoFsmStageLastUpdateTime_Object=MibTableColumn
cucsFcPIoFsmStageLastUpdateTime=_CucsFcPIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,5),_CucsFcPIoFsmStageLastUpdateTime_Type())
cucsFcPIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageLastUpdateTime.setStatus(_A)
_CucsFcPIoFsmStageName_Type=CucsFcPIoFsmStageName
_CucsFcPIoFsmStageName_Object=MibTableColumn
cucsFcPIoFsmStageName=_CucsFcPIoFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,6),_CucsFcPIoFsmStageName_Type())
cucsFcPIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageName.setStatus(_A)
_CucsFcPIoFsmStageOrder_Type=Gauge32
_CucsFcPIoFsmStageOrder_Object=MibTableColumn
cucsFcPIoFsmStageOrder=_CucsFcPIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,7),_CucsFcPIoFsmStageOrder_Type())
cucsFcPIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageOrder.setStatus(_A)
_CucsFcPIoFsmStageRetry_Type=Gauge32
_CucsFcPIoFsmStageRetry_Object=MibTableColumn
cucsFcPIoFsmStageRetry=_CucsFcPIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,8),_CucsFcPIoFsmStageRetry_Type())
cucsFcPIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageRetry.setStatus(_A)
_CucsFcPIoFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsFcPIoFsmStageStageStatus_Object=MibTableColumn
cucsFcPIoFsmStageStageStatus=_CucsFcPIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,20,9,1,9),_CucsFcPIoFsmStageStageStatus_Type())
cucsFcPIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcPIoFsmStageStageStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsFcObjects':cucsFcObjects,'cucsFcErrStatsTable':cucsFcErrStatsTable,'cucsFcErrStatsEntry':cucsFcErrStatsEntry,_E:cucsFcErrStatsInstanceId,'cucsFcErrStatsDn':cucsFcErrStatsDn,'cucsFcErrStatsRn':cucsFcErrStatsRn,'cucsFcErrStatsCrcRx':cucsFcErrStatsCrcRx,'cucsFcErrStatsCrcRxDelta':cucsFcErrStatsCrcRxDelta,'cucsFcErrStatsCrcRxDeltaAvg':cucsFcErrStatsCrcRxDeltaAvg,'cucsFcErrStatsCrcRxDeltaMax':cucsFcErrStatsCrcRxDeltaMax,'cucsFcErrStatsCrcRxDeltaMin':cucsFcErrStatsCrcRxDeltaMin,'cucsFcErrStatsDiscardRx':cucsFcErrStatsDiscardRx,'cucsFcErrStatsDiscardRxDelta':cucsFcErrStatsDiscardRxDelta,'cucsFcErrStatsDiscardRxDeltaAvg':cucsFcErrStatsDiscardRxDeltaAvg,'cucsFcErrStatsDiscardRxDeltaMax':cucsFcErrStatsDiscardRxDeltaMax,'cucsFcErrStatsDiscardRxDeltaMin':cucsFcErrStatsDiscardRxDeltaMin,'cucsFcErrStatsDiscardTx':cucsFcErrStatsDiscardTx,'cucsFcErrStatsDiscardTxDelta':cucsFcErrStatsDiscardTxDelta,'cucsFcErrStatsDiscardTxDeltaAvg':cucsFcErrStatsDiscardTxDeltaAvg,'cucsFcErrStatsDiscardTxDeltaMax':cucsFcErrStatsDiscardTxDeltaMax,'cucsFcErrStatsDiscardTxDeltaMin':cucsFcErrStatsDiscardTxDeltaMin,'cucsFcErrStatsIntervals':cucsFcErrStatsIntervals,'cucsFcErrStatsLinkFailures':cucsFcErrStatsLinkFailures,'cucsFcErrStatsLinkFailuresDelta':cucsFcErrStatsLinkFailuresDelta,'cucsFcErrStatsLinkFailuresDeltaAvg':cucsFcErrStatsLinkFailuresDeltaAvg,'cucsFcErrStatsLinkFailuresDeltaMax':cucsFcErrStatsLinkFailuresDeltaMax,'cucsFcErrStatsLinkFailuresDeltaMin':cucsFcErrStatsLinkFailuresDeltaMin,'cucsFcErrStatsRx':cucsFcErrStatsRx,'cucsFcErrStatsRxDelta':cucsFcErrStatsRxDelta,'cucsFcErrStatsRxDeltaAvg':cucsFcErrStatsRxDeltaAvg,'cucsFcErrStatsRxDeltaMax':cucsFcErrStatsRxDeltaMax,'cucsFcErrStatsRxDeltaMin':cucsFcErrStatsRxDeltaMin,'cucsFcErrStatsSignalLosses':cucsFcErrStatsSignalLosses,'cucsFcErrStatsSignalLossesDelta':cucsFcErrStatsSignalLossesDelta,'cucsFcErrStatsSignalLossesDeltaAvg':cucsFcErrStatsSignalLossesDeltaAvg,'cucsFcErrStatsSignalLossesDeltaMax':cucsFcErrStatsSignalLossesDeltaMax,'cucsFcErrStatsSignalLossesDeltaMin':cucsFcErrStatsSignalLossesDeltaMin,'cucsFcErrStatsSuspect':cucsFcErrStatsSuspect,'cucsFcErrStatsSyncLosses':cucsFcErrStatsSyncLosses,'cucsFcErrStatsSyncLossesDelta':cucsFcErrStatsSyncLossesDelta,'cucsFcErrStatsSyncLossesDeltaAvg':cucsFcErrStatsSyncLossesDeltaAvg,'cucsFcErrStatsSyncLossesDeltaMax':cucsFcErrStatsSyncLossesDeltaMax,'cucsFcErrStatsSyncLossesDeltaMin':cucsFcErrStatsSyncLossesDeltaMin,'cucsFcErrStatsThresholded':cucsFcErrStatsThresholded,'cucsFcErrStatsTimeCollected':cucsFcErrStatsTimeCollected,'cucsFcErrStatsTooLongRx':cucsFcErrStatsTooLongRx,'cucsFcErrStatsTooLongRxDelta':cucsFcErrStatsTooLongRxDelta,'cucsFcErrStatsTooLongRxDeltaAvg':cucsFcErrStatsTooLongRxDeltaAvg,'cucsFcErrStatsTooLongRxDeltaMax':cucsFcErrStatsTooLongRxDeltaMax,'cucsFcErrStatsTooLongRxDeltaMin':cucsFcErrStatsTooLongRxDeltaMin,'cucsFcErrStatsTooShortRx':cucsFcErrStatsTooShortRx,'cucsFcErrStatsTooShortRxDelta':cucsFcErrStatsTooShortRxDelta,'cucsFcErrStatsTooShortRxDeltaAvg':cucsFcErrStatsTooShortRxDeltaAvg,'cucsFcErrStatsTooShortRxDeltaMax':cucsFcErrStatsTooShortRxDeltaMax,'cucsFcErrStatsTooShortRxDeltaMin':cucsFcErrStatsTooShortRxDeltaMin,'cucsFcErrStatsTx':cucsFcErrStatsTx,'cucsFcErrStatsTxDelta':cucsFcErrStatsTxDelta,'cucsFcErrStatsTxDeltaAvg':cucsFcErrStatsTxDeltaAvg,'cucsFcErrStatsTxDeltaMax':cucsFcErrStatsTxDeltaMax,'cucsFcErrStatsTxDeltaMin':cucsFcErrStatsTxDeltaMin,'cucsFcErrStatsUpdate':cucsFcErrStatsUpdate,'cucsFcErrStatsHistTable':cucsFcErrStatsHistTable,'cucsFcErrStatsHistEntry':cucsFcErrStatsHistEntry,_F:cucsFcErrStatsHistInstanceId,'cucsFcErrStatsHistDn':cucsFcErrStatsHistDn,'cucsFcErrStatsHistRn':cucsFcErrStatsHistRn,'cucsFcErrStatsHistCrcRx':cucsFcErrStatsHistCrcRx,'cucsFcErrStatsHistCrcRxDelta':cucsFcErrStatsHistCrcRxDelta,'cucsFcErrStatsHistCrcRxDeltaAvg':cucsFcErrStatsHistCrcRxDeltaAvg,'cucsFcErrStatsHistCrcRxDeltaMax':cucsFcErrStatsHistCrcRxDeltaMax,'cucsFcErrStatsHistCrcRxDeltaMin':cucsFcErrStatsHistCrcRxDeltaMin,'cucsFcErrStatsHistDiscardRx':cucsFcErrStatsHistDiscardRx,'cucsFcErrStatsHistDiscardRxDelta':cucsFcErrStatsHistDiscardRxDelta,'cucsFcErrStatsHistDiscardRxDeltaAvg':cucsFcErrStatsHistDiscardRxDeltaAvg,'cucsFcErrStatsHistDiscardRxDeltaMax':cucsFcErrStatsHistDiscardRxDeltaMax,'cucsFcErrStatsHistDiscardRxDeltaMin':cucsFcErrStatsHistDiscardRxDeltaMin,'cucsFcErrStatsHistDiscardTx':cucsFcErrStatsHistDiscardTx,'cucsFcErrStatsHistDiscardTxDelta':cucsFcErrStatsHistDiscardTxDelta,'cucsFcErrStatsHistDiscardTxDeltaAvg':cucsFcErrStatsHistDiscardTxDeltaAvg,'cucsFcErrStatsHistDiscardTxDeltaMax':cucsFcErrStatsHistDiscardTxDeltaMax,'cucsFcErrStatsHistDiscardTxDeltaMin':cucsFcErrStatsHistDiscardTxDeltaMin,'cucsFcErrStatsHistId':cucsFcErrStatsHistId,'cucsFcErrStatsHistLinkFailures':cucsFcErrStatsHistLinkFailures,'cucsFcErrStatsHistLinkFailuresDelta':cucsFcErrStatsHistLinkFailuresDelta,'cucsFcErrStatsHistLinkFailuresDeltaAvg':cucsFcErrStatsHistLinkFailuresDeltaAvg,'cucsFcErrStatsHistLinkFailuresDeltaMax':cucsFcErrStatsHistLinkFailuresDeltaMax,'cucsFcErrStatsHistLinkFailuresDeltaMin':cucsFcErrStatsHistLinkFailuresDeltaMin,'cucsFcErrStatsHistMostRecent':cucsFcErrStatsHistMostRecent,'cucsFcErrStatsHistRx':cucsFcErrStatsHistRx,'cucsFcErrStatsHistRxDelta':cucsFcErrStatsHistRxDelta,'cucsFcErrStatsHistRxDeltaAvg':cucsFcErrStatsHistRxDeltaAvg,'cucsFcErrStatsHistRxDeltaMax':cucsFcErrStatsHistRxDeltaMax,'cucsFcErrStatsHistRxDeltaMin':cucsFcErrStatsHistRxDeltaMin,'cucsFcErrStatsHistSignalLosses':cucsFcErrStatsHistSignalLosses,'cucsFcErrStatsHistSignalLossesDelta':cucsFcErrStatsHistSignalLossesDelta,'cucsFcErrStatsHistSignalLossesDeltaAvg':cucsFcErrStatsHistSignalLossesDeltaAvg,'cucsFcErrStatsHistSignalLossesDeltaMax':cucsFcErrStatsHistSignalLossesDeltaMax,'cucsFcErrStatsHistSignalLossesDeltaMin':cucsFcErrStatsHistSignalLossesDeltaMin,'cucsFcErrStatsHistSuspect':cucsFcErrStatsHistSuspect,'cucsFcErrStatsHistSyncLosses':cucsFcErrStatsHistSyncLosses,'cucsFcErrStatsHistSyncLossesDelta':cucsFcErrStatsHistSyncLossesDelta,'cucsFcErrStatsHistSyncLossesDeltaAvg':cucsFcErrStatsHistSyncLossesDeltaAvg,'cucsFcErrStatsHistSyncLossesDeltaMax':cucsFcErrStatsHistSyncLossesDeltaMax,'cucsFcErrStatsHistSyncLossesDeltaMin':cucsFcErrStatsHistSyncLossesDeltaMin,'cucsFcErrStatsHistThresholded':cucsFcErrStatsHistThresholded,'cucsFcErrStatsHistTimeCollected':cucsFcErrStatsHistTimeCollected,'cucsFcErrStatsHistTooLongRx':cucsFcErrStatsHistTooLongRx,'cucsFcErrStatsHistTooLongRxDelta':cucsFcErrStatsHistTooLongRxDelta,'cucsFcErrStatsHistTooLongRxDeltaAvg':cucsFcErrStatsHistTooLongRxDeltaAvg,'cucsFcErrStatsHistTooLongRxDeltaMax':cucsFcErrStatsHistTooLongRxDeltaMax,'cucsFcErrStatsHistTooLongRxDeltaMin':cucsFcErrStatsHistTooLongRxDeltaMin,'cucsFcErrStatsHistTooShortRx':cucsFcErrStatsHistTooShortRx,'cucsFcErrStatsHistTooShortRxDelta':cucsFcErrStatsHistTooShortRxDelta,'cucsFcErrStatsHistTooShortRxDeltaAvg':cucsFcErrStatsHistTooShortRxDeltaAvg,'cucsFcErrStatsHistTooShortRxDeltaMax':cucsFcErrStatsHistTooShortRxDeltaMax,'cucsFcErrStatsHistTooShortRxDeltaMin':cucsFcErrStatsHistTooShortRxDeltaMin,'cucsFcErrStatsHistTx':cucsFcErrStatsHistTx,'cucsFcErrStatsHistTxDelta':cucsFcErrStatsHistTxDelta,'cucsFcErrStatsHistTxDeltaAvg':cucsFcErrStatsHistTxDeltaAvg,'cucsFcErrStatsHistTxDeltaMax':cucsFcErrStatsHistTxDeltaMax,'cucsFcErrStatsHistTxDeltaMin':cucsFcErrStatsHistTxDeltaMin,'cucsFcNicIfConfigTable':cucsFcNicIfConfigTable,'cucsFcNicIfConfigEntry':cucsFcNicIfConfigEntry,_G:cucsFcNicIfConfigInstanceId,'cucsFcNicIfConfigDn':cucsFcNicIfConfigDn,'cucsFcNicIfConfigRn':cucsFcNicIfConfigRn,'cucsFcPIoTable':cucsFcPIoTable,'cucsFcPIoEntry':cucsFcPIoEntry,_H:cucsFcPIoInstanceId,'cucsFcPIoDn':cucsFcPIoDn,'cucsFcPIoRn':cucsFcPIoRn,'cucsFcPIoAdminState':cucsFcPIoAdminState,'cucsFcPIoChassisId':cucsFcPIoChassisId,'cucsFcPIoEncap':cucsFcPIoEncap,'cucsFcPIoEpDn':cucsFcPIoEpDn,'cucsFcPIoFltAggr':cucsFcPIoFltAggr,'cucsFcPIoIfRole':cucsFcPIoIfRole,'cucsFcPIoIfType':cucsFcPIoIfType,'cucsFcPIoLocale':cucsFcPIoLocale,'cucsFcPIoMode':cucsFcPIoMode,'cucsFcPIoModel':cucsFcPIoModel,'cucsFcPIoName':cucsFcPIoName,'cucsFcPIoOperSpeed':cucsFcPIoOperSpeed,'cucsFcPIoOperState':cucsFcPIoOperState,'cucsFcPIoPeerDn':cucsFcPIoPeerDn,'cucsFcPIoPeerPortId':cucsFcPIoPeerPortId,'cucsFcPIoPeerSlotId':cucsFcPIoPeerSlotId,'cucsFcPIoPortId':cucsFcPIoPortId,'cucsFcPIoRevision':cucsFcPIoRevision,'cucsFcPIoSerial':cucsFcPIoSerial,'cucsFcPIoSlotId':cucsFcPIoSlotId,'cucsFcPIoStateQual':cucsFcPIoStateQual,'cucsFcPIoSwitchId':cucsFcPIoSwitchId,'cucsFcPIoTransport':cucsFcPIoTransport,'cucsFcPIoTs':cucsFcPIoTs,'cucsFcPIoType':cucsFcPIoType,'cucsFcPIoUsrLbl':cucsFcPIoUsrLbl,'cucsFcPIoVendor':cucsFcPIoVendor,'cucsFcPIoWwn':cucsFcPIoWwn,'cucsFcPIoFsmDescr':cucsFcPIoFsmDescr,'cucsFcPIoFsmPrev':cucsFcPIoFsmPrev,'cucsFcPIoFsmProgr':cucsFcPIoFsmProgr,'cucsFcPIoFsmRmtInvErrCode':cucsFcPIoFsmRmtInvErrCode,'cucsFcPIoFsmRmtInvErrDescr':cucsFcPIoFsmRmtInvErrDescr,'cucsFcPIoFsmRmtInvRslt':cucsFcPIoFsmRmtInvRslt,'cucsFcPIoFsmStageDescr':cucsFcPIoFsmStageDescr,'cucsFcPIoFsmStamp':cucsFcPIoFsmStamp,'cucsFcPIoFsmStatus':cucsFcPIoFsmStatus,'cucsFcPIoFsmTry':cucsFcPIoFsmTry,'cucsFcPIoLicGP':cucsFcPIoLicGP,'cucsFcPIoLicState':cucsFcPIoLicState,'cucsFcPIoXcvrType':cucsFcPIoXcvrType,'cucsFcPIoPeerChassisId':cucsFcPIoPeerChassisId,'cucsFcPIoAdminTransport':cucsFcPIoAdminTransport,'cucsFcPIoLc':cucsFcPIoLc,'cucsFcPIoUnifiedPort':cucsFcPIoUnifiedPort,'cucsFcPIoMaxSpeed':cucsFcPIoMaxSpeed,'cucsFcPIoIsPortChannelMember':cucsFcPIoIsPortChannelMember,'cucsFcPIoAggrPortId':cucsFcPIoAggrPortId,'cucsFcPIoPeerAggrPortId':cucsFcPIoPeerAggrPortId,'cucsFcPIoIsBreakoutXcvr':cucsFcPIoIsBreakoutXcvr,'cucsFcPIoPortCapability':cucsFcPIoPortCapability,'cucsFcStatsTable':cucsFcStatsTable,'cucsFcStatsEntry':cucsFcStatsEntry,_I:cucsFcStatsInstanceId,'cucsFcStatsDn':cucsFcStatsDn,'cucsFcStatsRn':cucsFcStatsRn,'cucsFcStatsBytesRx':cucsFcStatsBytesRx,'cucsFcStatsBytesRxDelta':cucsFcStatsBytesRxDelta,'cucsFcStatsBytesRxDeltaAvg':cucsFcStatsBytesRxDeltaAvg,'cucsFcStatsBytesRxDeltaMax':cucsFcStatsBytesRxDeltaMax,'cucsFcStatsBytesRxDeltaMin':cucsFcStatsBytesRxDeltaMin,'cucsFcStatsBytesTx':cucsFcStatsBytesTx,'cucsFcStatsBytesTxDelta':cucsFcStatsBytesTxDelta,'cucsFcStatsBytesTxDeltaAvg':cucsFcStatsBytesTxDeltaAvg,'cucsFcStatsBytesTxDeltaMax':cucsFcStatsBytesTxDeltaMax,'cucsFcStatsBytesTxDeltaMin':cucsFcStatsBytesTxDeltaMin,'cucsFcStatsIntervals':cucsFcStatsIntervals,'cucsFcStatsPacketsRx':cucsFcStatsPacketsRx,'cucsFcStatsPacketsRxDelta':cucsFcStatsPacketsRxDelta,'cucsFcStatsPacketsRxDeltaAvg':cucsFcStatsPacketsRxDeltaAvg,'cucsFcStatsPacketsRxDeltaMax':cucsFcStatsPacketsRxDeltaMax,'cucsFcStatsPacketsRxDeltaMin':cucsFcStatsPacketsRxDeltaMin,'cucsFcStatsPacketsTx':cucsFcStatsPacketsTx,'cucsFcStatsPacketsTxDelta':cucsFcStatsPacketsTxDelta,'cucsFcStatsPacketsTxDeltaAvg':cucsFcStatsPacketsTxDeltaAvg,'cucsFcStatsPacketsTxDeltaMax':cucsFcStatsPacketsTxDeltaMax,'cucsFcStatsPacketsTxDeltaMin':cucsFcStatsPacketsTxDeltaMin,'cucsFcStatsSuspect':cucsFcStatsSuspect,'cucsFcStatsThresholded':cucsFcStatsThresholded,'cucsFcStatsTimeCollected':cucsFcStatsTimeCollected,'cucsFcStatsUpdate':cucsFcStatsUpdate,'cucsFcStatsHistTable':cucsFcStatsHistTable,'cucsFcStatsHistEntry':cucsFcStatsHistEntry,_J:cucsFcStatsHistInstanceId,'cucsFcStatsHistDn':cucsFcStatsHistDn,'cucsFcStatsHistRn':cucsFcStatsHistRn,'cucsFcStatsHistBytesRx':cucsFcStatsHistBytesRx,'cucsFcStatsHistBytesRxDelta':cucsFcStatsHistBytesRxDelta,'cucsFcStatsHistBytesRxDeltaAvg':cucsFcStatsHistBytesRxDeltaAvg,'cucsFcStatsHistBytesRxDeltaMax':cucsFcStatsHistBytesRxDeltaMax,'cucsFcStatsHistBytesRxDeltaMin':cucsFcStatsHistBytesRxDeltaMin,'cucsFcStatsHistBytesTx':cucsFcStatsHistBytesTx,'cucsFcStatsHistBytesTxDelta':cucsFcStatsHistBytesTxDelta,'cucsFcStatsHistBytesTxDeltaAvg':cucsFcStatsHistBytesTxDeltaAvg,'cucsFcStatsHistBytesTxDeltaMax':cucsFcStatsHistBytesTxDeltaMax,'cucsFcStatsHistBytesTxDeltaMin':cucsFcStatsHistBytesTxDeltaMin,'cucsFcStatsHistId':cucsFcStatsHistId,'cucsFcStatsHistMostRecent':cucsFcStatsHistMostRecent,'cucsFcStatsHistPacketsRx':cucsFcStatsHistPacketsRx,'cucsFcStatsHistPacketsRxDelta':cucsFcStatsHistPacketsRxDelta,'cucsFcStatsHistPacketsRxDeltaAvg':cucsFcStatsHistPacketsRxDeltaAvg,'cucsFcStatsHistPacketsRxDeltaMax':cucsFcStatsHistPacketsRxDeltaMax,'cucsFcStatsHistPacketsRxDeltaMin':cucsFcStatsHistPacketsRxDeltaMin,'cucsFcStatsHistPacketsTx':cucsFcStatsHistPacketsTx,'cucsFcStatsHistPacketsTxDelta':cucsFcStatsHistPacketsTxDelta,'cucsFcStatsHistPacketsTxDeltaAvg':cucsFcStatsHistPacketsTxDeltaAvg,'cucsFcStatsHistPacketsTxDeltaMax':cucsFcStatsHistPacketsTxDeltaMax,'cucsFcStatsHistPacketsTxDeltaMin':cucsFcStatsHistPacketsTxDeltaMin,'cucsFcStatsHistSuspect':cucsFcStatsHistSuspect,'cucsFcStatsHistThresholded':cucsFcStatsHistThresholded,'cucsFcStatsHistTimeCollected':cucsFcStatsHistTimeCollected,'cucsFcSwIfConfigTable':cucsFcSwIfConfigTable,'cucsFcSwIfConfigEntry':cucsFcSwIfConfigEntry,_K:cucsFcSwIfConfigInstanceId,'cucsFcSwIfConfigDn':cucsFcSwIfConfigDn,'cucsFcSwIfConfigRn':cucsFcSwIfConfigRn,'cucsFcPIoFsmTable':cucsFcPIoFsmTable,'cucsFcPIoFsmEntry':cucsFcPIoFsmEntry,_L:cucsFcPIoFsmInstanceId,'cucsFcPIoFsmDn':cucsFcPIoFsmDn,'cucsFcPIoFsmRn':cucsFcPIoFsmRn,'cucsFcPIoFsmCompletionTime':cucsFcPIoFsmCompletionTime,'cucsFcPIoFsmCurrentFsm':cucsFcPIoFsmCurrentFsm,'cucsFcPIoFsmDescrData':cucsFcPIoFsmDescrData,'cucsFcPIoFsmFsmStatus':cucsFcPIoFsmFsmStatus,'cucsFcPIoFsmProgress':cucsFcPIoFsmProgress,'cucsFcPIoFsmRmtErrCode':cucsFcPIoFsmRmtErrCode,'cucsFcPIoFsmRmtErrDescr':cucsFcPIoFsmRmtErrDescr,'cucsFcPIoFsmRmtRslt':cucsFcPIoFsmRmtRslt,'cucsFcPIoFsmStageTable':cucsFcPIoFsmStageTable,'cucsFcPIoFsmStageEntry':cucsFcPIoFsmStageEntry,_M:cucsFcPIoFsmStageInstanceId,'cucsFcPIoFsmStageDn':cucsFcPIoFsmStageDn,'cucsFcPIoFsmStageRn':cucsFcPIoFsmStageRn,'cucsFcPIoFsmStageDescrData':cucsFcPIoFsmStageDescrData,'cucsFcPIoFsmStageLastUpdateTime':cucsFcPIoFsmStageLastUpdateTime,'cucsFcPIoFsmStageName':cucsFcPIoFsmStageName,'cucsFcPIoFsmStageOrder':cucsFcPIoFsmStageOrder,'cucsFcPIoFsmStageRetry':cucsFcPIoFsmStageRetry,'cucsFcPIoFsmStageStageStatus':cucsFcPIoFsmStageStageStatus})