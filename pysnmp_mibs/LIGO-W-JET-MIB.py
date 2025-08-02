_W='wJetP2pTxTotalRetries'
_V='wJetP2pRxDropped'
_U='wJetP2pRssi'
_T='retries'
_S='timeouts'
_R='wJetP2pEndpointType'
_Q='wJetP2pLocalIfIndex'
_P='microseconds'
_O='kbit/s'
_N='wJetIfIndex'
_M='Integer32'
_L='dBm'
_K='bytes'
_J='not-accessible'
_I='wJetP2pMacAddress'
_H='sysLocation'
_G='SNMPv2-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='LIGO-W-JET-MIB'
_C='packets'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ligoMgmt,=mibBuilder.importSymbols('LIGOWAVE-MIB','ligoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ligoWJetMIB=ModuleIdentity((1,3,6,1,4,1,32750,3,6))
if mibBuilder.loadTexts:ligoWJetMIB.setRevisions(('2009-07-16 00:00','2008-11-27 00:00'))
_LigoWJetMIBObjects_ObjectIdentity=ObjectIdentity
ligoWJetMIBObjects=_LigoWJetMIBObjects_ObjectIdentity((1,3,6,1,4,1,32750,3,6,1))
_LigoWJetNotifs_ObjectIdentity=ObjectIdentity
ligoWJetNotifs=_LigoWJetNotifs_ObjectIdentity((1,3,6,1,4,1,32750,3,6,1,0))
_LigoWJetInfo_ObjectIdentity=ObjectIdentity
ligoWJetInfo=_LigoWJetInfo_ObjectIdentity((1,3,6,1,4,1,32750,3,6,1,1))
_LigoWJetConf_ObjectIdentity=ObjectIdentity
ligoWJetConf=_LigoWJetConf_ObjectIdentity((1,3,6,1,4,1,32750,3,6,1,2))
_WJetWrlssIfConfTable_Object=MibTable
wJetWrlssIfConfTable=_WJetWrlssIfConfTable_Object((1,3,6,1,4,1,32750,3,6,1,2,1))
if mibBuilder.loadTexts:wJetWrlssIfConfTable.setStatus(_A)
_WJetWrlssIfConfEntry_Object=MibTableRow
wJetWrlssIfConfEntry=_WJetWrlssIfConfEntry_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1))
wJetWrlssIfConfEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:wJetWrlssIfConfEntry.setStatus(_A)
_WJetIfIndex_Type=InterfaceIndex
_WJetIfIndex_Object=MibTableColumn
wJetIfIndex=_WJetIfIndex_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,1),_WJetIfIndex_Type())
wJetIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:wJetIfIndex.setStatus(_A)
_WJetIfProtoEnabled_Type=TruthValue
_WJetIfProtoEnabled_Object=MibTableColumn
wJetIfProtoEnabled=_WJetIfProtoEnabled_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,2),_WJetIfProtoEnabled_Type())
wJetIfProtoEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfProtoEnabled.setStatus(_A)
_WJetIfDataRate_Type=Integer32
_WJetIfDataRate_Object=MibTableColumn
wJetIfDataRate=_WJetIfDataRate_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,3),_WJetIfDataRate_Type())
wJetIfDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfDataRate.setStatus(_A)
if mibBuilder.loadTexts:wJetIfDataRate.setUnits(_O)
_WJetIfAckRate_Type=Integer32
_WJetIfAckRate_Object=MibTableColumn
wJetIfAckRate=_WJetIfAckRate_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,4),_WJetIfAckRate_Type())
wJetIfAckRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfAckRate.setStatus(_A)
if mibBuilder.loadTexts:wJetIfAckRate.setUnits(_O)
_WJetIfAckTimeout_Type=Integer32
_WJetIfAckTimeout_Object=MibTableColumn
wJetIfAckTimeout=_WJetIfAckTimeout_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,5),_WJetIfAckTimeout_Type())
wJetIfAckTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfAckTimeout.setStatus(_A)
if mibBuilder.loadTexts:wJetIfAckTimeout.setUnits(_P)
_WJetIfTxQueueMaxLength_Type=Integer32
_WJetIfTxQueueMaxLength_Object=MibTableColumn
wJetIfTxQueueMaxLength=_WJetIfTxQueueMaxLength_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,6),_WJetIfTxQueueMaxLength_Type())
wJetIfTxQueueMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfTxQueueMaxLength.setStatus(_A)
if mibBuilder.loadTexts:wJetIfTxQueueMaxLength.setUnits('frames')
_WJetIfRxTimeout_Type=Integer32
_WJetIfRxTimeout_Object=MibTableColumn
wJetIfRxTimeout=_WJetIfRxTimeout_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,7),_WJetIfRxTimeout_Type())
wJetIfRxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfRxTimeout.setStatus(_A)
if mibBuilder.loadTexts:wJetIfRxTimeout.setUnits(_P)
_WJetIfMaxAggregBytes_Type=Integer32
_WJetIfMaxAggregBytes_Object=MibTableColumn
wJetIfMaxAggregBytes=_WJetIfMaxAggregBytes_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,8),_WJetIfMaxAggregBytes_Type())
wJetIfMaxAggregBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfMaxAggregBytes.setStatus(_A)
if mibBuilder.loadTexts:wJetIfMaxAggregBytes.setUnits(_K)
_WJetIfMaxAggregPackets_Type=Integer32
_WJetIfMaxAggregPackets_Object=MibTableColumn
wJetIfMaxAggregPackets=_WJetIfMaxAggregPackets_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,9),_WJetIfMaxAggregPackets_Type())
wJetIfMaxAggregPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfMaxAggregPackets.setStatus(_A)
if mibBuilder.loadTexts:wJetIfMaxAggregPackets.setUnits(_C)
_WJetIfCcaThreshold_Type=Integer32
_WJetIfCcaThreshold_Object=MibTableColumn
wJetIfCcaThreshold=_WJetIfCcaThreshold_Object((1,3,6,1,4,1,32750,3,6,1,2,1,1,10),_WJetIfCcaThreshold_Type())
wJetIfCcaThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetIfCcaThreshold.setStatus(_A)
_LigoWJetStats_ObjectIdentity=ObjectIdentity
ligoWJetStats=_LigoWJetStats_ObjectIdentity((1,3,6,1,4,1,32750,3,6,1,3))
_WJetP2pEndpStatsTable_Object=MibTable
wJetP2pEndpStatsTable=_WJetP2pEndpStatsTable_Object((1,3,6,1,4,1,32750,3,6,1,3,1))
if mibBuilder.loadTexts:wJetP2pEndpStatsTable.setStatus(_A)
_WJetP2pEndpStatsEntry_Object=MibTableRow
wJetP2pEndpStatsEntry=_WJetP2pEndpStatsEntry_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1))
wJetP2pEndpStatsEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:wJetP2pEndpStatsEntry.setStatus(_A)
_WJetP2pLocalIfIndex_Type=InterfaceIndex
_WJetP2pLocalIfIndex_Object=MibTableColumn
wJetP2pLocalIfIndex=_WJetP2pLocalIfIndex_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,1),_WJetP2pLocalIfIndex_Type())
wJetP2pLocalIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:wJetP2pLocalIfIndex.setStatus(_A)
class _WJetP2pEndpointType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('local',0),('remote',1)))
_WJetP2pEndpointType_Type.__name__=_M
_WJetP2pEndpointType_Object=MibTableColumn
wJetP2pEndpointType=_WJetP2pEndpointType_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,2),_WJetP2pEndpointType_Type())
wJetP2pEndpointType.setMaxAccess(_J)
if mibBuilder.loadTexts:wJetP2pEndpointType.setStatus(_A)
_WJetP2pMacAddress_Type=MacAddress
_WJetP2pMacAddress_Object=MibTableColumn
wJetP2pMacAddress=_WJetP2pMacAddress_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,3),_WJetP2pMacAddress_Type())
wJetP2pMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pMacAddress.setStatus(_A)
_WJetP2pRssi_Type=Gauge32
_WJetP2pRssi_Object=MibTableColumn
wJetP2pRssi=_WJetP2pRssi_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,4),_WJetP2pRssi_Type())
wJetP2pRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRssi.setStatus(_A)
_WJetP2pMaxRssi_Type=Gauge32
_WJetP2pMaxRssi_Object=MibTableColumn
wJetP2pMaxRssi=_WJetP2pMaxRssi_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,5),_WJetP2pMaxRssi_Type())
wJetP2pMaxRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pMaxRssi.setStatus(_A)
_WJetP2pSignalLevel_Type=Integer32
_WJetP2pSignalLevel_Object=MibTableColumn
wJetP2pSignalLevel=_WJetP2pSignalLevel_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,6),_WJetP2pSignalLevel_Type())
wJetP2pSignalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pSignalLevel.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pSignalLevel.setUnits(_L)
_WJetP2pNoiseLevel_Type=Integer32
_WJetP2pNoiseLevel_Object=MibTableColumn
wJetP2pNoiseLevel=_WJetP2pNoiseLevel_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,7),_WJetP2pNoiseLevel_Type())
wJetP2pNoiseLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pNoiseLevel.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pNoiseLevel.setUnits(_L)
_WJetP2pTxPower_Type=Gauge32
_WJetP2pTxPower_Object=MibTableColumn
wJetP2pTxPower=_WJetP2pTxPower_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,8),_WJetP2pTxPower_Type())
wJetP2pTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxPower.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxPower.setUnits(_L)
_WJetP2pRxStart_Type=Counter32
_WJetP2pRxStart_Object=MibTableColumn
wJetP2pRxStart=_WJetP2pRxStart_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,9),_WJetP2pRxStart_Type())
wJetP2pRxStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxStart.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxStart.setUnits(_C)
_WJetP2pTxStart_Type=Counter32
_WJetP2pTxStart_Object=MibTableColumn
wJetP2pTxStart=_WJetP2pTxStart_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,10),_WJetP2pTxStart_Type())
wJetP2pTxStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxStart.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxStart.setUnits(_C)
_WJetP2pRxStop_Type=Counter32
_WJetP2pRxStop_Object=MibTableColumn
wJetP2pRxStop=_WJetP2pRxStop_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,11),_WJetP2pRxStop_Type())
wJetP2pRxStop.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxStop.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxStop.setUnits(_C)
_WJetP2pRxBytes_Type=Counter32
_WJetP2pRxBytes_Object=MibTableColumn
wJetP2pRxBytes=_WJetP2pRxBytes_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,12),_WJetP2pRxBytes_Type())
wJetP2pRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxBytes.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxBytes.setUnits(_K)
_WJetP2pTxBytes_Type=Counter32
_WJetP2pTxBytes_Object=MibTableColumn
wJetP2pTxBytes=_WJetP2pTxBytes_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,13),_WJetP2pTxBytes_Type())
wJetP2pTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxBytes.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxBytes.setUnits(_K)
_WJetP2pRxPackets_Type=Counter32
_WJetP2pRxPackets_Object=MibTableColumn
wJetP2pRxPackets=_WJetP2pRxPackets_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,14),_WJetP2pRxPackets_Type())
wJetP2pRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxPackets.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxPackets.setUnits(_C)
_WJetP2pTxPackets_Type=Counter32
_WJetP2pTxPackets_Object=MibTableColumn
wJetP2pTxPackets=_WJetP2pTxPackets_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,15),_WJetP2pTxPackets_Type())
wJetP2pTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxPackets.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxPackets.setUnits(_C)
_WJetP2pTxAcked_Type=Counter32
_WJetP2pTxAcked_Object=MibTableColumn
wJetP2pTxAcked=_WJetP2pTxAcked_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,16),_WJetP2pTxAcked_Type())
wJetP2pTxAcked.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxAcked.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxAcked.setUnits(_C)
_WJetP2pRxDuplicated_Type=Counter32
_WJetP2pRxDuplicated_Object=MibTableColumn
wJetP2pRxDuplicated=_WJetP2pRxDuplicated_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,17),_WJetP2pRxDuplicated_Type())
wJetP2pRxDuplicated.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxDuplicated.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxDuplicated.setUnits(_C)
_WJetP2pRxDropped_Type=Counter32
_WJetP2pRxDropped_Object=MibTableColumn
wJetP2pRxDropped=_WJetP2pRxDropped_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,18),_WJetP2pRxDropped_Type())
wJetP2pRxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxDropped.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxDropped.setUnits(_C)
_WJetP2pRxTimeouts_Type=Counter32
_WJetP2pRxTimeouts_Object=MibTableColumn
wJetP2pRxTimeouts=_WJetP2pRxTimeouts_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,19),_WJetP2pRxTimeouts_Type())
wJetP2pRxTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxTimeouts.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxTimeouts.setUnits(_S)
_WJetP2pTxTimeouts_Type=Counter32
_WJetP2pTxTimeouts_Object=MibTableColumn
wJetP2pTxTimeouts=_WJetP2pTxTimeouts_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,20),_WJetP2pTxTimeouts_Type())
wJetP2pTxTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxTimeouts.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxTimeouts.setUnits(_S)
_WJetP2pRxNoRetries_Type=Counter32
_WJetP2pRxNoRetries_Object=MibTableColumn
wJetP2pRxNoRetries=_WJetP2pRxNoRetries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,21),_WJetP2pRxNoRetries_Type())
wJetP2pRxNoRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRxNoRetries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRxNoRetries.setUnits(_C)
_WJetP2pTxNoRetries_Type=Counter32
_WJetP2pTxNoRetries_Object=MibTableColumn
wJetP2pTxNoRetries=_WJetP2pTxNoRetries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,22),_WJetP2pTxNoRetries_Type())
wJetP2pTxNoRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxNoRetries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxNoRetries.setUnits(_C)
_WJetP2pRx1Retry_Type=Counter32
_WJetP2pRx1Retry_Object=MibTableColumn
wJetP2pRx1Retry=_WJetP2pRx1Retry_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,23),_WJetP2pRx1Retry_Type())
wJetP2pRx1Retry.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRx1Retry.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRx1Retry.setUnits(_C)
_WJetP2pTx1Retry_Type=Counter32
_WJetP2pTx1Retry_Object=MibTableColumn
wJetP2pTx1Retry=_WJetP2pTx1Retry_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,24),_WJetP2pTx1Retry_Type())
wJetP2pTx1Retry.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTx1Retry.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTx1Retry.setUnits(_C)
_WJetP2pRx2Retries_Type=Counter32
_WJetP2pRx2Retries_Object=MibTableColumn
wJetP2pRx2Retries=_WJetP2pRx2Retries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,25),_WJetP2pRx2Retries_Type())
wJetP2pRx2Retries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRx2Retries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRx2Retries.setUnits(_C)
_WJetP2pTx2Retries_Type=Counter32
_WJetP2pTx2Retries_Object=MibTableColumn
wJetP2pTx2Retries=_WJetP2pTx2Retries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,26),_WJetP2pTx2Retries_Type())
wJetP2pTx2Retries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTx2Retries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTx2Retries.setUnits(_C)
_WJetP2pRx3Retries_Type=Counter32
_WJetP2pRx3Retries_Object=MibTableColumn
wJetP2pRx3Retries=_WJetP2pRx3Retries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,27),_WJetP2pRx3Retries_Type())
wJetP2pRx3Retries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pRx3Retries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pRx3Retries.setUnits(_C)
_WJetP2pTx3Retries_Type=Counter32
_WJetP2pTx3Retries_Object=MibTableColumn
wJetP2pTx3Retries=_WJetP2pTx3Retries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,28),_WJetP2pTx3Retries_Type())
wJetP2pTx3Retries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTx3Retries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTx3Retries.setUnits(_C)
_WJetP2pTxTotalRetries_Type=Counter32
_WJetP2pTxTotalRetries_Object=MibTableColumn
wJetP2pTxTotalRetries=_WJetP2pTxTotalRetries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,29),_WJetP2pTxTotalRetries_Type())
wJetP2pTxTotalRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxTotalRetries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxTotalRetries.setUnits(_T)
_WJetP2pTxMaxRetries_Type=Counter32
_WJetP2pTxMaxRetries_Object=MibTableColumn
wJetP2pTxMaxRetries=_WJetP2pTxMaxRetries_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,30),_WJetP2pTxMaxRetries_Type())
wJetP2pTxMaxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pTxMaxRetries.setStatus(_A)
if mibBuilder.loadTexts:wJetP2pTxMaxRetries.setUnits(_T)
_WJetP2pIpAddress_Type=IpAddress
_WJetP2pIpAddress_Object=MibTableColumn
wJetP2pIpAddress=_WJetP2pIpAddress_Object((1,3,6,1,4,1,32750,3,6,1,3,1,1,31),_WJetP2pIpAddress_Type())
wJetP2pIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetP2pIpAddress.setStatus(_A)
wJetNodeConnected=NotificationType((1,3,6,1,4,1,32750,3,6,1,0,1))
wJetNodeConnected.setObjects(*((_G,_H),(_E,_F),(_D,_I)))
if mibBuilder.loadTexts:wJetNodeConnected.setStatus(_A)
wJetNodeDisconnected=NotificationType((1,3,6,1,4,1,32750,3,6,1,0,2))
wJetNodeDisconnected.setObjects(*((_G,_H),(_E,_F),(_D,_I)))
if mibBuilder.loadTexts:wJetNodeDisconnected.setStatus(_A)
wJetLowSignalStrength=NotificationType((1,3,6,1,4,1,32750,3,6,1,0,3))
wJetLowSignalStrength.setObjects(*((_G,_H),(_E,_F),(_D,_I),(_D,_U)))
if mibBuilder.loadTexts:wJetLowSignalStrength.setStatus(_A)
wJetRxDroppedThresholdReached=NotificationType((1,3,6,1,4,1,32750,3,6,1,0,4))
wJetRxDroppedThresholdReached.setObjects(*((_G,_H),(_E,_F),(_D,_I),(_D,_V)))
if mibBuilder.loadTexts:wJetRxDroppedThresholdReached.setStatus(_A)
wJetTxRetriesThresholdReached=NotificationType((1,3,6,1,4,1,32750,3,6,1,0,5))
wJetTxRetriesThresholdReached.setObjects(*((_G,_H),(_E,_F),(_D,_I),(_D,_W)))
if mibBuilder.loadTexts:wJetTxRetriesThresholdReached.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ligoWJetMIB':ligoWJetMIB,'ligoWJetMIBObjects':ligoWJetMIBObjects,'ligoWJetNotifs':ligoWJetNotifs,'wJetNodeConnected':wJetNodeConnected,'wJetNodeDisconnected':wJetNodeDisconnected,'wJetLowSignalStrength':wJetLowSignalStrength,'wJetRxDroppedThresholdReached':wJetRxDroppedThresholdReached,'wJetTxRetriesThresholdReached':wJetTxRetriesThresholdReached,'ligoWJetInfo':ligoWJetInfo,'ligoWJetConf':ligoWJetConf,'wJetWrlssIfConfTable':wJetWrlssIfConfTable,'wJetWrlssIfConfEntry':wJetWrlssIfConfEntry,_N:wJetIfIndex,'wJetIfProtoEnabled':wJetIfProtoEnabled,'wJetIfDataRate':wJetIfDataRate,'wJetIfAckRate':wJetIfAckRate,'wJetIfAckTimeout':wJetIfAckTimeout,'wJetIfTxQueueMaxLength':wJetIfTxQueueMaxLength,'wJetIfRxTimeout':wJetIfRxTimeout,'wJetIfMaxAggregBytes':wJetIfMaxAggregBytes,'wJetIfMaxAggregPackets':wJetIfMaxAggregPackets,'wJetIfCcaThreshold':wJetIfCcaThreshold,'ligoWJetStats':ligoWJetStats,'wJetP2pEndpStatsTable':wJetP2pEndpStatsTable,'wJetP2pEndpStatsEntry':wJetP2pEndpStatsEntry,_Q:wJetP2pLocalIfIndex,_R:wJetP2pEndpointType,_I:wJetP2pMacAddress,_U:wJetP2pRssi,'wJetP2pMaxRssi':wJetP2pMaxRssi,'wJetP2pSignalLevel':wJetP2pSignalLevel,'wJetP2pNoiseLevel':wJetP2pNoiseLevel,'wJetP2pTxPower':wJetP2pTxPower,'wJetP2pRxStart':wJetP2pRxStart,'wJetP2pTxStart':wJetP2pTxStart,'wJetP2pRxStop':wJetP2pRxStop,'wJetP2pRxBytes':wJetP2pRxBytes,'wJetP2pTxBytes':wJetP2pTxBytes,'wJetP2pRxPackets':wJetP2pRxPackets,'wJetP2pTxPackets':wJetP2pTxPackets,'wJetP2pTxAcked':wJetP2pTxAcked,'wJetP2pRxDuplicated':wJetP2pRxDuplicated,_V:wJetP2pRxDropped,'wJetP2pRxTimeouts':wJetP2pRxTimeouts,'wJetP2pTxTimeouts':wJetP2pTxTimeouts,'wJetP2pRxNoRetries':wJetP2pRxNoRetries,'wJetP2pTxNoRetries':wJetP2pTxNoRetries,'wJetP2pRx1Retry':wJetP2pRx1Retry,'wJetP2pTx1Retry':wJetP2pTx1Retry,'wJetP2pRx2Retries':wJetP2pRx2Retries,'wJetP2pTx2Retries':wJetP2pTx2Retries,'wJetP2pRx3Retries':wJetP2pRx3Retries,'wJetP2pTx3Retries':wJetP2pTx3Retries,_W:wJetP2pTxTotalRetries,'wJetP2pTxMaxRetries':wJetP2pTxMaxRetries,'wJetP2pIpAddress':wJetP2pIpAddress})