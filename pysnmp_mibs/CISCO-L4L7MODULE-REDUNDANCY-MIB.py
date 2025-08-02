_A8='clrRedundancyStatsGroup'
_A7='clrRedConfigGroup'
_A6='clrPeerConfigGroup'
_A5='clrRedundancyStateChange'
_A4='clrLBStatsReceiveFailures'
_A3='clrLBStatsReceivedPackets'
_A2='clrLBStatsDroppedEntries'
_A1='clrLBStatsSendFailures'
_A0='clrLBStatsSentPackets'
_z='clrLBStatsSharedStickyEntries'
_y='clrHAStatsPeerDownEvents'
_x='clrHAStatsPeerUpEvents'
_w='clrHAStatsHeartBeatTimeoutMismatches'
_v='clrHAStatsRxUniDirectionalHeartBeatMsgs'
_u='clrHAStatsMissedHeartBeatMsgs'
_t='clrHAStatsRxHeartBeatMsgs'
_s='clrHAStatsTxHeartBeatMsgs'
_r='clrStateChangeNotifEnabled'
_q='clrRedundancyIpAddress'
_p='clrRedundancyIpAddressType'
_o='clrRedundancyStateChangeTime'
_n='clrRedundancyState'
_m='clrRedundancyPriority'
_l='clrRedContext'
_k='clrRedRowStatus'
_j='clrRedStorageType'
_i='clrRedFailOverTime'
_h='clrRedPreempt'
_g='clrRedPriority'
_f='clrPeerRedGroups'
_e='clrPeerLicenseCompatibility'
_d='clrPeerSoftwareCompatibilty'
_c='clrPeerRowStatus'
_b='clrPeerStorageType'
_a='clrPeerIpAddress'
_Z='clrPeerIpAddressType'
_Y='clrPeerOperStatus'
_X='clrPeerHeartBeatCount'
_W='clrPeerHeartBeatTime'
_V='clrPeerBackupInterface'
_U='clrPeerInterface'
_T='inCompatible'
_S='not-accessible'
_R='InterfaceIndexOrZero'
_Q='clrRedStateChangeTime'
_P='clrRedState'
_O='clrRedPeerId'
_N='compatible'
_M='init'
_L='TruthValue'
_K='StorageType'
_J='clrRedGroupId'
_I='clrPeerId'
_H='Integer32'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='CISCO-L4L7MODULE-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_R)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_K,'TextualConvention','TimeStamp',_L)
ciscoL4L7moduleRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,650))
if mibBuilder.loadTexts:ciscoL4L7moduleRedundancyMIB.setRevisions(('2008-04-04 00:00','2008-03-13 00:00'))
class CiscoL4L7RedState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('nonRedundant',2),('initializing',3),('negotiation',4),('active',5),('standbyCold',6),('standbyConfig',7),('standbyBulk',8),('standbyHot',9),('standbyWarm',10)))
_CiscoLmRedundancyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLmRedundancyMIBNotifs=_CiscoLmRedundancyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,650,0))
_CiscoLmRedundancyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLmRedundancyMIBObjects=_CiscoLmRedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,650,1))
_ClrConfig_ObjectIdentity=ObjectIdentity
clrConfig=_ClrConfig_ObjectIdentity((1,3,6,1,4,1,9,9,650,1,1))
_ClrPeerConfigTable_Object=MibTable
clrPeerConfigTable=_ClrPeerConfigTable_Object((1,3,6,1,4,1,9,9,650,1,1,1))
if mibBuilder.loadTexts:clrPeerConfigTable.setStatus(_A)
_ClrPeerConfigEntry_Object=MibTableRow
clrPeerConfigEntry=_ClrPeerConfigEntry_Object((1,3,6,1,4,1,9,9,650,1,1,1,1))
clrPeerConfigEntry.setIndexNames((0,_F,_G),(0,_B,_I))
if mibBuilder.loadTexts:clrPeerConfigEntry.setStatus(_A)
class _ClrPeerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ClrPeerId_Type.__name__=_E
_ClrPeerId_Object=MibTableColumn
clrPeerId=_ClrPeerId_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,1),_ClrPeerId_Type())
clrPeerId.setMaxAccess(_S)
if mibBuilder.loadTexts:clrPeerId.setStatus(_A)
_ClrPeerInterface_Type=InterfaceIndex
_ClrPeerInterface_Object=MibTableColumn
clrPeerInterface=_ClrPeerInterface_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,2),_ClrPeerInterface_Type())
clrPeerInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:clrPeerInterface.setStatus(_A)
class _ClrPeerBackupInterface_Type(InterfaceIndexOrZero):defaultValue=0
_ClrPeerBackupInterface_Type.__name__=_R
_ClrPeerBackupInterface_Object=MibTableColumn
clrPeerBackupInterface=_ClrPeerBackupInterface_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,3),_ClrPeerBackupInterface_Type())
clrPeerBackupInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:clrPeerBackupInterface.setStatus(_A)
class _ClrPeerHeartBeatTime_Type(Unsigned32):defaultValue=1
_ClrPeerHeartBeatTime_Type.__name__=_E
_ClrPeerHeartBeatTime_Object=MibTableColumn
clrPeerHeartBeatTime=_ClrPeerHeartBeatTime_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,4),_ClrPeerHeartBeatTime_Type())
clrPeerHeartBeatTime.setMaxAccess(_D)
if mibBuilder.loadTexts:clrPeerHeartBeatTime.setStatus(_A)
if mibBuilder.loadTexts:clrPeerHeartBeatTime.setUnits('milliseconds')
class _ClrPeerHeartBeatCount_Type(Unsigned32):defaultValue=1
_ClrPeerHeartBeatCount_Type.__name__=_E
_ClrPeerHeartBeatCount_Object=MibTableColumn
clrPeerHeartBeatCount=_ClrPeerHeartBeatCount_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,5),_ClrPeerHeartBeatCount_Type())
clrPeerHeartBeatCount.setMaxAccess(_D)
if mibBuilder.loadTexts:clrPeerHeartBeatCount.setStatus(_A)
class _ClrPeerStorageType_Type(StorageType):defaultValue=3
_ClrPeerStorageType_Type.__name__=_K
_ClrPeerStorageType_Object=MibTableColumn
clrPeerStorageType=_ClrPeerStorageType_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,6),_ClrPeerStorageType_Type())
clrPeerStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:clrPeerStorageType.setStatus(_A)
_ClrPeerRowStatus_Type=RowStatus
_ClrPeerRowStatus_Object=MibTableColumn
clrPeerRowStatus=_ClrPeerRowStatus_Object((1,3,6,1,4,1,9,9,650,1,1,1,1,7),_ClrPeerRowStatus_Type())
clrPeerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clrPeerRowStatus.setStatus(_A)
_ClrPeerInfoTable_Object=MibTable
clrPeerInfoTable=_ClrPeerInfoTable_Object((1,3,6,1,4,1,9,9,650,1,1,2))
if mibBuilder.loadTexts:clrPeerInfoTable.setStatus(_A)
_ClrPeerInfoEntry_Object=MibTableRow
clrPeerInfoEntry=_ClrPeerInfoEntry_Object((1,3,6,1,4,1,9,9,650,1,1,2,1))
clrPeerInfoEntry.setIndexNames((0,_F,_G),(0,_B,_I))
if mibBuilder.loadTexts:clrPeerInfoEntry.setStatus(_A)
class _ClrPeerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_M,1),('localIPaddr',2),('peerIPAddr',3),('startHB',4),('tcpSetup',5),('srgCheck',6),('licCheck',7),(_N,8),('peerInterfaceDown',9),('down',10),('error',11)))
_ClrPeerOperStatus_Type.__name__=_H
_ClrPeerOperStatus_Object=MibTableColumn
clrPeerOperStatus=_ClrPeerOperStatus_Object((1,3,6,1,4,1,9,9,650,1,1,2,1,1),_ClrPeerOperStatus_Type())
clrPeerOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clrPeerOperStatus.setStatus(_A)
_ClrPeerIpAddressType_Type=InetAddressType
_ClrPeerIpAddressType_Object=MibTableColumn
clrPeerIpAddressType=_ClrPeerIpAddressType_Object((1,3,6,1,4,1,9,9,650,1,1,2,1,2),_ClrPeerIpAddressType_Type())
clrPeerIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:clrPeerIpAddressType.setStatus(_A)
_ClrPeerIpAddress_Type=InetAddress
_ClrPeerIpAddress_Object=MibTableColumn
clrPeerIpAddress=_ClrPeerIpAddress_Object((1,3,6,1,4,1,9,9,650,1,1,2,1,3),_ClrPeerIpAddress_Type())
clrPeerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:clrPeerIpAddress.setStatus(_A)
class _ClrPeerSoftwareCompatibilty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_T,3),('warmCompatible',4)))
_ClrPeerSoftwareCompatibilty_Type.__name__=_H
_ClrPeerSoftwareCompatibilty_Object=MibTableColumn
clrPeerSoftwareCompatibilty=_ClrPeerSoftwareCompatibilty_Object((1,3,6,1,4,1,9,9,650,1,1,2,1,4),_ClrPeerSoftwareCompatibilty_Type())
clrPeerSoftwareCompatibilty.setMaxAccess(_C)
if mibBuilder.loadTexts:clrPeerSoftwareCompatibilty.setStatus(_A)
class _ClrPeerLicenseCompatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_T,3)))
_ClrPeerLicenseCompatibility_Type.__name__=_H
_ClrPeerLicenseCompatibility_Object=MibTableColumn
clrPeerLicenseCompatibility=_ClrPeerLicenseCompatibility_Object((1,3,6,1,4,1,9,9,650,1,1,2,1,5),_ClrPeerLicenseCompatibility_Type())
clrPeerLicenseCompatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:clrPeerLicenseCompatibility.setStatus(_A)
class _ClrPeerRedGroups_Type(Unsigned32):defaultValue=0
_ClrPeerRedGroups_Type.__name__=_E
_ClrPeerRedGroups_Object=MibTableColumn
clrPeerRedGroups=_ClrPeerRedGroups_Object((1,3,6,1,4,1,9,9,650,1,1,2,1,6),_ClrPeerRedGroups_Type())
clrPeerRedGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:clrPeerRedGroups.setStatus(_A)
_ClrRedundancyConfigTable_Object=MibTable
clrRedundancyConfigTable=_ClrRedundancyConfigTable_Object((1,3,6,1,4,1,9,9,650,1,1,3))
if mibBuilder.loadTexts:clrRedundancyConfigTable.setStatus(_A)
_ClrRedundancyConfigEntry_Object=MibTableRow
clrRedundancyConfigEntry=_ClrRedundancyConfigEntry_Object((1,3,6,1,4,1,9,9,650,1,1,3,1))
clrRedundancyConfigEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:clrRedundancyConfigEntry.setStatus(_A)
class _ClrRedGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_ClrRedGroupId_Type.__name__=_E
_ClrRedGroupId_Object=MibTableColumn
clrRedGroupId=_ClrRedGroupId_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,1),_ClrRedGroupId_Type())
clrRedGroupId.setMaxAccess(_S)
if mibBuilder.loadTexts:clrRedGroupId.setStatus(_A)
class _ClrRedPeerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ClrRedPeerId_Type.__name__=_E
_ClrRedPeerId_Object=MibTableColumn
clrRedPeerId=_ClrRedPeerId_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,2),_ClrRedPeerId_Type())
clrRedPeerId.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedPeerId.setStatus(_A)
class _ClrRedPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ClrRedPriority_Type.__name__=_E
_ClrRedPriority_Object=MibTableColumn
clrRedPriority=_ClrRedPriority_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,3),_ClrRedPriority_Type())
clrRedPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedPriority.setStatus(_A)
class _ClrRedPreempt_Type(TruthValue):defaultValue=1
_ClrRedPreempt_Type.__name__=_L
_ClrRedPreempt_Object=MibTableColumn
clrRedPreempt=_ClrRedPreempt_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,4),_ClrRedPreempt_Type())
clrRedPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedPreempt.setStatus(_A)
class _ClrRedFailOverTime_Type(Unsigned32):defaultValue=3
_ClrRedFailOverTime_Type.__name__=_E
_ClrRedFailOverTime_Object=MibTableColumn
clrRedFailOverTime=_ClrRedFailOverTime_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,5),_ClrRedFailOverTime_Type())
clrRedFailOverTime.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedFailOverTime.setStatus(_A)
_ClrRedState_Type=CiscoL4L7RedState
_ClrRedState_Object=MibTableColumn
clrRedState=_ClrRedState_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,6),_ClrRedState_Type())
clrRedState.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedState.setStatus(_A)
_ClrRedStateChangeTime_Type=TimeStamp
_ClrRedStateChangeTime_Object=MibTableColumn
clrRedStateChangeTime=_ClrRedStateChangeTime_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,7),_ClrRedStateChangeTime_Type())
clrRedStateChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedStateChangeTime.setStatus(_A)
_ClrRedContext_Type=OctetString
_ClrRedContext_Object=MibTableColumn
clrRedContext=_ClrRedContext_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,8),_ClrRedContext_Type())
clrRedContext.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedContext.setStatus(_A)
class _ClrRedStorageType_Type(StorageType):defaultValue=3
_ClrRedStorageType_Type.__name__=_K
_ClrRedStorageType_Object=MibTableColumn
clrRedStorageType=_ClrRedStorageType_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,9),_ClrRedStorageType_Type())
clrRedStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedStorageType.setStatus(_A)
_ClrRedRowStatus_Type=RowStatus
_ClrRedRowStatus_Object=MibTableColumn
clrRedRowStatus=_ClrRedRowStatus_Object((1,3,6,1,4,1,9,9,650,1,1,3,1,10),_ClrRedRowStatus_Type())
clrRedRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clrRedRowStatus.setStatus(_A)
_ClrRedundancyInfoTable_Object=MibTable
clrRedundancyInfoTable=_ClrRedundancyInfoTable_Object((1,3,6,1,4,1,9,9,650,1,1,4))
if mibBuilder.loadTexts:clrRedundancyInfoTable.setStatus(_A)
_ClrRedundancyInfoEntry_Object=MibTableRow
clrRedundancyInfoEntry=_ClrRedundancyInfoEntry_Object((1,3,6,1,4,1,9,9,650,1,1,4,1))
clrRedundancyInfoEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:clrRedundancyInfoEntry.setStatus(_A)
class _ClrRedundancyPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ClrRedundancyPriority_Type.__name__=_E
_ClrRedundancyPriority_Object=MibTableColumn
clrRedundancyPriority=_ClrRedundancyPriority_Object((1,3,6,1,4,1,9,9,650,1,1,4,1,1),_ClrRedundancyPriority_Type())
clrRedundancyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedundancyPriority.setStatus(_A)
_ClrRedundancyState_Type=CiscoL4L7RedState
_ClrRedundancyState_Object=MibTableColumn
clrRedundancyState=_ClrRedundancyState_Object((1,3,6,1,4,1,9,9,650,1,1,4,1,2),_ClrRedundancyState_Type())
clrRedundancyState.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedundancyState.setStatus(_A)
_ClrRedundancyStateChangeTime_Type=TimeStamp
_ClrRedundancyStateChangeTime_Object=MibTableColumn
clrRedundancyStateChangeTime=_ClrRedundancyStateChangeTime_Object((1,3,6,1,4,1,9,9,650,1,1,4,1,3),_ClrRedundancyStateChangeTime_Type())
clrRedundancyStateChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedundancyStateChangeTime.setStatus(_A)
_ClrRedundancyIpAddressType_Type=InetAddressType
_ClrRedundancyIpAddressType_Object=MibTableColumn
clrRedundancyIpAddressType=_ClrRedundancyIpAddressType_Object((1,3,6,1,4,1,9,9,650,1,1,4,1,4),_ClrRedundancyIpAddressType_Type())
clrRedundancyIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedundancyIpAddressType.setStatus(_A)
_ClrRedundancyIpAddress_Type=InetAddress
_ClrRedundancyIpAddress_Object=MibTableColumn
clrRedundancyIpAddress=_ClrRedundancyIpAddress_Object((1,3,6,1,4,1,9,9,650,1,1,4,1,5),_ClrRedundancyIpAddress_Type())
clrRedundancyIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:clrRedundancyIpAddress.setStatus(_A)
_ClrStats_ObjectIdentity=ObjectIdentity
clrStats=_ClrStats_ObjectIdentity((1,3,6,1,4,1,9,9,650,1,2))
_ClrLBStatsTable_Object=MibTable
clrLBStatsTable=_ClrLBStatsTable_Object((1,3,6,1,4,1,9,9,650,1,2,1))
if mibBuilder.loadTexts:clrLBStatsTable.setStatus(_A)
_ClrLBStatsEntry_Object=MibTableRow
clrLBStatsEntry=_ClrLBStatsEntry_Object((1,3,6,1,4,1,9,9,650,1,2,1,1))
clrLBStatsEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:clrLBStatsEntry.setStatus(_A)
_ClrLBStatsSharedStickyEntries_Type=Counter64
_ClrLBStatsSharedStickyEntries_Object=MibTableColumn
clrLBStatsSharedStickyEntries=_ClrLBStatsSharedStickyEntries_Object((1,3,6,1,4,1,9,9,650,1,2,1,1,1),_ClrLBStatsSharedStickyEntries_Type())
clrLBStatsSharedStickyEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:clrLBStatsSharedStickyEntries.setStatus(_A)
_ClrLBStatsSentPackets_Type=Counter64
_ClrLBStatsSentPackets_Object=MibTableColumn
clrLBStatsSentPackets=_ClrLBStatsSentPackets_Object((1,3,6,1,4,1,9,9,650,1,2,1,1,2),_ClrLBStatsSentPackets_Type())
clrLBStatsSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:clrLBStatsSentPackets.setStatus(_A)
_ClrLBStatsSendFailures_Type=Counter64
_ClrLBStatsSendFailures_Object=MibTableColumn
clrLBStatsSendFailures=_ClrLBStatsSendFailures_Object((1,3,6,1,4,1,9,9,650,1,2,1,1,3),_ClrLBStatsSendFailures_Type())
clrLBStatsSendFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:clrLBStatsSendFailures.setStatus(_A)
_ClrLBStatsDroppedEntries_Type=Counter64
_ClrLBStatsDroppedEntries_Object=MibTableColumn
clrLBStatsDroppedEntries=_ClrLBStatsDroppedEntries_Object((1,3,6,1,4,1,9,9,650,1,2,1,1,4),_ClrLBStatsDroppedEntries_Type())
clrLBStatsDroppedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:clrLBStatsDroppedEntries.setStatus(_A)
_ClrLBStatsReceivedPackets_Type=Counter64
_ClrLBStatsReceivedPackets_Object=MibTableColumn
clrLBStatsReceivedPackets=_ClrLBStatsReceivedPackets_Object((1,3,6,1,4,1,9,9,650,1,2,1,1,5),_ClrLBStatsReceivedPackets_Type())
clrLBStatsReceivedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:clrLBStatsReceivedPackets.setStatus(_A)
_ClrLBStatsReceiveFailures_Type=Counter64
_ClrLBStatsReceiveFailures_Object=MibTableColumn
clrLBStatsReceiveFailures=_ClrLBStatsReceiveFailures_Object((1,3,6,1,4,1,9,9,650,1,2,1,1,6),_ClrLBStatsReceiveFailures_Type())
clrLBStatsReceiveFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:clrLBStatsReceiveFailures.setStatus(_A)
_ClrHAStatsTable_Object=MibTable
clrHAStatsTable=_ClrHAStatsTable_Object((1,3,6,1,4,1,9,9,650,1,2,2))
if mibBuilder.loadTexts:clrHAStatsTable.setStatus(_A)
_ClrHAStatsEntry_Object=MibTableRow
clrHAStatsEntry=_ClrHAStatsEntry_Object((1,3,6,1,4,1,9,9,650,1,2,2,1))
clrHAStatsEntry.setIndexNames((0,_F,_G),(0,_B,_I))
if mibBuilder.loadTexts:clrHAStatsEntry.setStatus(_A)
_ClrHAStatsTxHeartBeatMsgs_Type=Counter64
_ClrHAStatsTxHeartBeatMsgs_Object=MibTableColumn
clrHAStatsTxHeartBeatMsgs=_ClrHAStatsTxHeartBeatMsgs_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,1),_ClrHAStatsTxHeartBeatMsgs_Type())
clrHAStatsTxHeartBeatMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsTxHeartBeatMsgs.setStatus(_A)
_ClrHAStatsRxHeartBeatMsgs_Type=Counter64
_ClrHAStatsRxHeartBeatMsgs_Object=MibTableColumn
clrHAStatsRxHeartBeatMsgs=_ClrHAStatsRxHeartBeatMsgs_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,2),_ClrHAStatsRxHeartBeatMsgs_Type())
clrHAStatsRxHeartBeatMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsRxHeartBeatMsgs.setStatus(_A)
_ClrHAStatsMissedHeartBeatMsgs_Type=Counter64
_ClrHAStatsMissedHeartBeatMsgs_Object=MibTableColumn
clrHAStatsMissedHeartBeatMsgs=_ClrHAStatsMissedHeartBeatMsgs_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,3),_ClrHAStatsMissedHeartBeatMsgs_Type())
clrHAStatsMissedHeartBeatMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsMissedHeartBeatMsgs.setStatus(_A)
_ClrHAStatsRxUniDirectionalHeartBeatMsgs_Type=Counter64
_ClrHAStatsRxUniDirectionalHeartBeatMsgs_Object=MibTableColumn
clrHAStatsRxUniDirectionalHeartBeatMsgs=_ClrHAStatsRxUniDirectionalHeartBeatMsgs_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,4),_ClrHAStatsRxUniDirectionalHeartBeatMsgs_Type())
clrHAStatsRxUniDirectionalHeartBeatMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsRxUniDirectionalHeartBeatMsgs.setStatus(_A)
_ClrHAStatsHeartBeatTimeoutMismatches_Type=Counter64
_ClrHAStatsHeartBeatTimeoutMismatches_Object=MibTableColumn
clrHAStatsHeartBeatTimeoutMismatches=_ClrHAStatsHeartBeatTimeoutMismatches_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,5),_ClrHAStatsHeartBeatTimeoutMismatches_Type())
clrHAStatsHeartBeatTimeoutMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsHeartBeatTimeoutMismatches.setStatus(_A)
_ClrHAStatsPeerUpEvents_Type=Counter64
_ClrHAStatsPeerUpEvents_Object=MibTableColumn
clrHAStatsPeerUpEvents=_ClrHAStatsPeerUpEvents_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,6),_ClrHAStatsPeerUpEvents_Type())
clrHAStatsPeerUpEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsPeerUpEvents.setStatus(_A)
_ClrHAStatsPeerDownEvents_Type=Counter64
_ClrHAStatsPeerDownEvents_Object=MibTableColumn
clrHAStatsPeerDownEvents=_ClrHAStatsPeerDownEvents_Object((1,3,6,1,4,1,9,9,650,1,2,2,1,7),_ClrHAStatsPeerDownEvents_Type())
clrHAStatsPeerDownEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:clrHAStatsPeerDownEvents.setStatus(_A)
_ClrNotifObjects_ObjectIdentity=ObjectIdentity
clrNotifObjects=_ClrNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,650,1,3))
class _ClrStateChangeNotifEnabled_Type(TruthValue):defaultValue=2
_ClrStateChangeNotifEnabled_Type.__name__=_L
_ClrStateChangeNotifEnabled_Object=MibScalar
clrStateChangeNotifEnabled=_ClrStateChangeNotifEnabled_Object((1,3,6,1,4,1,9,9,650,1,3,1),_ClrStateChangeNotifEnabled_Type())
clrStateChangeNotifEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:clrStateChangeNotifEnabled.setStatus(_A)
_CiscoLmRedundancyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoLmRedundancyMIBConformance=_CiscoLmRedundancyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,650,2))
_CiscoLmRedundancyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLmRedundancyMIBCompliances=_CiscoLmRedundancyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,650,2,1))
_CiscoLmRedundancyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLmRedundancyMIBGroups=_CiscoLmRedundancyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,650,2,2))
clrPeerConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,650,2,2,1))
clrPeerConfigGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:clrPeerConfigGroup.setStatus(_A)
clrRedConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,650,2,2,2))
clrRedConfigGroup.setObjects(*((_B,_O),(_B,_g),(_B,_h),(_B,_i),(_B,_P),(_B,_Q),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:clrRedConfigGroup.setStatus(_A)
clrRedInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,650,2,2,3))
clrRedInfoGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:clrRedInfoGroup.setStatus(_A)
cslbxNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,650,2,2,4))
cslbxNotifControlGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:cslbxNotifControlGroup.setStatus(_A)
clrRedundancyStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,650,2,2,6))
clrRedundancyStatsGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:clrRedundancyStatsGroup.setStatus(_A)
clrRedundancyStateChange=NotificationType((1,3,6,1,4,1,9,9,650,0,1))
clrRedundancyStateChange.setObjects(*((_B,_P),(_B,_Q),(_B,_O)))
if mibBuilder.loadTexts:clrRedundancyStateChange.setStatus(_A)
cslbxNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,650,2,2,5))
cslbxNotifGroup.setObjects((_B,_A5))
if mibBuilder.loadTexts:cslbxNotifGroup.setStatus(_A)
ciscoLmRedundancyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,650,2,1,1))
ciscoLmRedundancyMIBCompliance.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ciscoLmRedundancyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoL4L7RedState':CiscoL4L7RedState,'ciscoL4L7moduleRedundancyMIB':ciscoL4L7moduleRedundancyMIB,'ciscoLmRedundancyMIBNotifs':ciscoLmRedundancyMIBNotifs,_A5:clrRedundancyStateChange,'ciscoLmRedundancyMIBObjects':ciscoLmRedundancyMIBObjects,'clrConfig':clrConfig,'clrPeerConfigTable':clrPeerConfigTable,'clrPeerConfigEntry':clrPeerConfigEntry,_I:clrPeerId,_U:clrPeerInterface,_V:clrPeerBackupInterface,_W:clrPeerHeartBeatTime,_X:clrPeerHeartBeatCount,_b:clrPeerStorageType,_c:clrPeerRowStatus,'clrPeerInfoTable':clrPeerInfoTable,'clrPeerInfoEntry':clrPeerInfoEntry,_Y:clrPeerOperStatus,_Z:clrPeerIpAddressType,_a:clrPeerIpAddress,_d:clrPeerSoftwareCompatibilty,_e:clrPeerLicenseCompatibility,_f:clrPeerRedGroups,'clrRedundancyConfigTable':clrRedundancyConfigTable,'clrRedundancyConfigEntry':clrRedundancyConfigEntry,_J:clrRedGroupId,_O:clrRedPeerId,_g:clrRedPriority,_h:clrRedPreempt,_i:clrRedFailOverTime,_P:clrRedState,_Q:clrRedStateChangeTime,_l:clrRedContext,_j:clrRedStorageType,_k:clrRedRowStatus,'clrRedundancyInfoTable':clrRedundancyInfoTable,'clrRedundancyInfoEntry':clrRedundancyInfoEntry,_m:clrRedundancyPriority,_n:clrRedundancyState,_o:clrRedundancyStateChangeTime,_p:clrRedundancyIpAddressType,_q:clrRedundancyIpAddress,'clrStats':clrStats,'clrLBStatsTable':clrLBStatsTable,'clrLBStatsEntry':clrLBStatsEntry,_z:clrLBStatsSharedStickyEntries,_A0:clrLBStatsSentPackets,_A1:clrLBStatsSendFailures,_A2:clrLBStatsDroppedEntries,_A3:clrLBStatsReceivedPackets,_A4:clrLBStatsReceiveFailures,'clrHAStatsTable':clrHAStatsTable,'clrHAStatsEntry':clrHAStatsEntry,_s:clrHAStatsTxHeartBeatMsgs,_t:clrHAStatsRxHeartBeatMsgs,_u:clrHAStatsMissedHeartBeatMsgs,_v:clrHAStatsRxUniDirectionalHeartBeatMsgs,_w:clrHAStatsHeartBeatTimeoutMismatches,_x:clrHAStatsPeerUpEvents,_y:clrHAStatsPeerDownEvents,'clrNotifObjects':clrNotifObjects,_r:clrStateChangeNotifEnabled,'ciscoLmRedundancyMIBConformance':ciscoLmRedundancyMIBConformance,'ciscoLmRedundancyMIBCompliances':ciscoLmRedundancyMIBCompliances,'ciscoLmRedundancyMIBCompliance':ciscoLmRedundancyMIBCompliance,'ciscoLmRedundancyMIBGroups':ciscoLmRedundancyMIBGroups,_A6:clrPeerConfigGroup,_A7:clrRedConfigGroup,'clrRedInfoGroup':clrRedInfoGroup,'cslbxNotifControlGroup':cslbxNotifControlGroup,'cslbxNotifGroup':cslbxNotifGroup,_A8:clrRedundancyStatsGroup})