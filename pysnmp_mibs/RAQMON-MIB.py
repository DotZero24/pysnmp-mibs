_AY='raqmonCollectorNotificationsGroup'
_AX='raqmonCollectorGroup'
_AW='raqmonSessionAlarm'
_AV='raqmonConfigRDSTimeout'
_AU='raqmonConfigRaqmonPdus'
_AT='raqmonConfigPduTransport'
_AS='raqmonSessionExceptionRowStatus'
_AR='raqmonSessionExceptionLostPacketsThreshold'
_AQ='raqmonSessionExceptionNetRTTThreshold'
_AP='raqmonSessionExceptionIAJitterThreshold'
_AO='raqmonConfigPort'
_AN='raqmonParticipantAddrEndDate'
_AM='raqmonQosSessionStatus'
_AL='raqmonQosSentOctets'
_AK='raqmonQosSentPackets'
_AJ='raqmonQosRcvdOctets'
_AI='raqmonParticipantDiscardsFrct'
_AH='raqmonParticipantDiscards'
_AG='raqmonParticipantLostPacketsFrct'
_AF='raqmonParticipantLostPackets'
_AE='raqmonParticipantOctetsSent'
_AD='raqmonParticipantOctetsRcvd'
_AC='raqmonParticipantPacketsSent'
_AB='raqmonParticipantPacketsRcvd'
_AA='raqmonParticipantAppDelayMax'
_A9='raqmonParticipantAppDelayMin'
_A8='raqmonParticipantAppDelayMean'
_A7='raqmonParticipantNetOwdMax'
_A6='raqmonParticipantNetOwdMin'
_A5='raqmonParticipantNetOwdMean'
_A4='raqmonParticipantIPDVMax'
_A3='raqmonParticipantIPDVMin'
_A2='raqmonParticipantIPDVMean'
_A1='raqmonParticipantIAJitterMax'
_A0='raqmonParticipantIAJitterMin'
_z='raqmonParticipantIAJitterMean'
_y='raqmonParticipantNetRTTMax'
_x='raqmonParticipantNetRTTMin'
_w='raqmonParticipantNetRTTMean'
_v='raqmonParticipantMemoryMax'
_u='raqmonParticipantMemoryMin'
_t='raqmonParticipantMemoryMean'
_s='raqmonParticipantCpuMax'
_r='raqmonParticipantCpuMin'
_q='raqmonParticipantCpuMean'
_p='raqmonParticipantDestDSCP'
_o='raqmonParticipantSrcDSCP'
_n='raqmonParticipantDestL2Priority'
_m='raqmonParticipantSrcL2Priority'
_l='raqmonParticipantPeer'
_k='raqmonParticipantActive'
_j='raqmonParticipantSrcPayloadType'
_i='raqmonParticipantDestPayloadType'
_h='raqmonParticipantEndDate'
_g='raqmonParticipantQosCount'
_f='raqmonParticipantAppName'
_e='raqmonParticipantSetupDelay'
_d='raqmonParticipantRecvPort'
_c='raqmonParticipantSendPort'
_b='raqmonParticipantReportCaps'
_a='read-write'
_Z='raqmonSessionExceptionIndex'
_Y='octets'
_X='raqmonQosTime'
_W='Octets'
_V='raqmonQosLostPackets'
_U='raqmonQosRcvdPackets'
_T='raqmonQoSInterArrivalJitter'
_S='raqmonQoSEnd2EndNetDelay'
_R='raqmonParticipantPeerAddr'
_Q='raqmonParticipantPeerAddrType'
_P='raqmonParticipantName'
_O='raqmonParticipantAddrType'
_N='Bits'
_M='read-create'
_L='raqmonParticipantAddr'
_K='not-accessible'
_J='raqmonParticipantIndex'
_I='raqmonParticipantStartDate'
_H='Unsigned32'
_G='packets'
_F='percents'
_E='milliseconds'
_D='Integer32'
_C='read-only'
_B='current'
_A='RAQMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
rmon,=mibBuilder.importSymbols('RMON-MIB','rmon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
raqmonMIB=ModuleIdentity((1,3,6,1,2,1,16,31))
if mibBuilder.loadTexts:raqmonMIB.setRevisions(('2006-10-10 00:00',))
_RaqmonNotifications_ObjectIdentity=ObjectIdentity
raqmonNotifications=_RaqmonNotifications_ObjectIdentity((1,3,6,1,2,1,16,31,0))
_RaqmonMIBObjects_ObjectIdentity=ObjectIdentity
raqmonMIBObjects=_RaqmonMIBObjects_ObjectIdentity((1,3,6,1,2,1,16,31,1))
_RaqmonSession_ObjectIdentity=ObjectIdentity
raqmonSession=_RaqmonSession_ObjectIdentity((1,3,6,1,2,1,16,31,1,1))
_RaqmonParticipantTable_Object=MibTable
raqmonParticipantTable=_RaqmonParticipantTable_Object((1,3,6,1,2,1,16,31,1,1,1))
if mibBuilder.loadTexts:raqmonParticipantTable.setStatus(_B)
_RaqmonParticipantEntry_Object=MibTableRow
raqmonParticipantEntry=_RaqmonParticipantEntry_Object((1,3,6,1,2,1,16,31,1,1,1,1))
raqmonParticipantEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:raqmonParticipantEntry.setStatus(_B)
_RaqmonParticipantStartDate_Type=DateAndTime
_RaqmonParticipantStartDate_Object=MibTableColumn
raqmonParticipantStartDate=_RaqmonParticipantStartDate_Object((1,3,6,1,2,1,16,31,1,1,1,1,1),_RaqmonParticipantStartDate_Type())
raqmonParticipantStartDate.setMaxAccess(_K)
if mibBuilder.loadTexts:raqmonParticipantStartDate.setStatus(_B)
class _RaqmonParticipantIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RaqmonParticipantIndex_Type.__name__=_H
_RaqmonParticipantIndex_Object=MibTableColumn
raqmonParticipantIndex=_RaqmonParticipantIndex_Object((1,3,6,1,2,1,16,31,1,1,1,1,2),_RaqmonParticipantIndex_Type())
raqmonParticipantIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:raqmonParticipantIndex.setStatus(_B)
class _RaqmonParticipantReportCaps_Type(Bits):namedValues=NamedValues(*(('raqmonPartRepDsrcName',0),('raqmonPartRepRecvName',1),('raqmonPartRepDsrcPort',2),('raqmonPartRepRecvPort',3),('raqmonPartRepSetupTime',4),('raqmonPartRepSetupDelay',5),('raqmonPartRepSessionDuration',6),('raqmonPartRepSetupStatus',7),('raqmonPartRepRTEnd2EndNetDelay',8),('raqmonPartRepOWEnd2EndNetDelay',9),('raqmonPartApplicationDelay',10),('raqmonPartRepIAJitter',11),('raqmonPartRepIPDV',12),('raqmonPartRepRcvdPackets',13),('raqmonPartRepRcvdOctets',14),('raqmonPartRepSentPackets',15),('raqmonPartRepSentOctets',16),('raqmonPartRepCumPacketsLoss',17),('raqmonPartRepFractionPacketsLoss',18),('raqmonPartRepCumDiscards',19),('raqmonPartRepFractionDiscards',20),('raqmonPartRepSrcPayloadType',21),('raqmonPartRepDestPayloadType',22),('raqmonPartRepSrcLayer2Priority',23),('raqmonPartRepSrcTosDscp',24),('raqmonPartRepDestLayer2Priority',25),('raqmonPartRepDestTosDscp',26),('raqmonPartRepCPU',27),('raqmonPartRepMemory',28),('raqmonPartRepAppName',29)))
_RaqmonParticipantReportCaps_Type.__name__=_N
_RaqmonParticipantReportCaps_Object=MibTableColumn
raqmonParticipantReportCaps=_RaqmonParticipantReportCaps_Object((1,3,6,1,2,1,16,31,1,1,1,1,3),_RaqmonParticipantReportCaps_Type())
raqmonParticipantReportCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantReportCaps.setStatus(_B)
_RaqmonParticipantAddrType_Type=InetAddressType
_RaqmonParticipantAddrType_Object=MibTableColumn
raqmonParticipantAddrType=_RaqmonParticipantAddrType_Object((1,3,6,1,2,1,16,31,1,1,1,1,4),_RaqmonParticipantAddrType_Type())
raqmonParticipantAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAddrType.setStatus(_B)
_RaqmonParticipantAddr_Type=InetAddress
_RaqmonParticipantAddr_Object=MibTableColumn
raqmonParticipantAddr=_RaqmonParticipantAddr_Object((1,3,6,1,2,1,16,31,1,1,1,1,5),_RaqmonParticipantAddr_Type())
raqmonParticipantAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAddr.setStatus(_B)
_RaqmonParticipantSendPort_Type=InetPortNumber
_RaqmonParticipantSendPort_Object=MibTableColumn
raqmonParticipantSendPort=_RaqmonParticipantSendPort_Object((1,3,6,1,2,1,16,31,1,1,1,1,6),_RaqmonParticipantSendPort_Type())
raqmonParticipantSendPort.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantSendPort.setStatus(_B)
_RaqmonParticipantRecvPort_Type=InetPortNumber
_RaqmonParticipantRecvPort_Object=MibTableColumn
raqmonParticipantRecvPort=_RaqmonParticipantRecvPort_Object((1,3,6,1,2,1,16,31,1,1,1,1,7),_RaqmonParticipantRecvPort_Type())
raqmonParticipantRecvPort.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantRecvPort.setStatus(_B)
class _RaqmonParticipantSetupDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantSetupDelay_Type.__name__=_D
_RaqmonParticipantSetupDelay_Object=MibTableColumn
raqmonParticipantSetupDelay=_RaqmonParticipantSetupDelay_Object((1,3,6,1,2,1,16,31,1,1,1,1,8),_RaqmonParticipantSetupDelay_Type())
raqmonParticipantSetupDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantSetupDelay.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantSetupDelay.setUnits(_E)
_RaqmonParticipantName_Type=SnmpAdminString
_RaqmonParticipantName_Object=MibTableColumn
raqmonParticipantName=_RaqmonParticipantName_Object((1,3,6,1,2,1,16,31,1,1,1,1,9),_RaqmonParticipantName_Type())
raqmonParticipantName.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantName.setStatus(_B)
_RaqmonParticipantAppName_Type=SnmpAdminString
_RaqmonParticipantAppName_Object=MibTableColumn
raqmonParticipantAppName=_RaqmonParticipantAppName_Object((1,3,6,1,2,1,16,31,1,1,1,1,10),_RaqmonParticipantAppName_Type())
raqmonParticipantAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAppName.setStatus(_B)
_RaqmonParticipantQosCount_Type=Gauge32
_RaqmonParticipantQosCount_Object=MibTableColumn
raqmonParticipantQosCount=_RaqmonParticipantQosCount_Object((1,3,6,1,2,1,16,31,1,1,1,1,11),_RaqmonParticipantQosCount_Type())
raqmonParticipantQosCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantQosCount.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantQosCount.setUnits('entries')
_RaqmonParticipantEndDate_Type=DateAndTime
_RaqmonParticipantEndDate_Object=MibTableColumn
raqmonParticipantEndDate=_RaqmonParticipantEndDate_Object((1,3,6,1,2,1,16,31,1,1,1,1,12),_RaqmonParticipantEndDate_Type())
raqmonParticipantEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantEndDate.setStatus(_B)
class _RaqmonParticipantDestPayloadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,127))
_RaqmonParticipantDestPayloadType_Type.__name__=_D
_RaqmonParticipantDestPayloadType_Object=MibTableColumn
raqmonParticipantDestPayloadType=_RaqmonParticipantDestPayloadType_Object((1,3,6,1,2,1,16,31,1,1,1,1,13),_RaqmonParticipantDestPayloadType_Type())
raqmonParticipantDestPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantDestPayloadType.setStatus(_B)
class _RaqmonParticipantSrcPayloadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,127))
_RaqmonParticipantSrcPayloadType_Type.__name__=_D
_RaqmonParticipantSrcPayloadType_Object=MibTableColumn
raqmonParticipantSrcPayloadType=_RaqmonParticipantSrcPayloadType_Object((1,3,6,1,2,1,16,31,1,1,1,1,14),_RaqmonParticipantSrcPayloadType_Type())
raqmonParticipantSrcPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantSrcPayloadType.setStatus(_B)
_RaqmonParticipantActive_Type=TruthValue
_RaqmonParticipantActive_Object=MibTableColumn
raqmonParticipantActive=_RaqmonParticipantActive_Object((1,3,6,1,2,1,16,31,1,1,1,1,15),_RaqmonParticipantActive_Type())
raqmonParticipantActive.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantActive.setStatus(_B)
_RaqmonParticipantPeer_Type=RowPointer
_RaqmonParticipantPeer_Object=MibTableColumn
raqmonParticipantPeer=_RaqmonParticipantPeer_Object((1,3,6,1,2,1,16,31,1,1,1,1,16),_RaqmonParticipantPeer_Type())
raqmonParticipantPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantPeer.setStatus(_B)
_RaqmonParticipantPeerAddrType_Type=InetAddressType
_RaqmonParticipantPeerAddrType_Object=MibTableColumn
raqmonParticipantPeerAddrType=_RaqmonParticipantPeerAddrType_Object((1,3,6,1,2,1,16,31,1,1,1,1,17),_RaqmonParticipantPeerAddrType_Type())
raqmonParticipantPeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantPeerAddrType.setStatus(_B)
_RaqmonParticipantPeerAddr_Type=InetAddress
_RaqmonParticipantPeerAddr_Object=MibTableColumn
raqmonParticipantPeerAddr=_RaqmonParticipantPeerAddr_Object((1,3,6,1,2,1,16,31,1,1,1,1,18),_RaqmonParticipantPeerAddr_Type())
raqmonParticipantPeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantPeerAddr.setStatus(_B)
class _RaqmonParticipantSrcL2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_RaqmonParticipantSrcL2Priority_Type.__name__=_D
_RaqmonParticipantSrcL2Priority_Object=MibTableColumn
raqmonParticipantSrcL2Priority=_RaqmonParticipantSrcL2Priority_Object((1,3,6,1,2,1,16,31,1,1,1,1,19),_RaqmonParticipantSrcL2Priority_Type())
raqmonParticipantSrcL2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantSrcL2Priority.setStatus(_B)
class _RaqmonParticipantDestL2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_RaqmonParticipantDestL2Priority_Type.__name__=_D
_RaqmonParticipantDestL2Priority_Object=MibTableColumn
raqmonParticipantDestL2Priority=_RaqmonParticipantDestL2Priority_Object((1,3,6,1,2,1,16,31,1,1,1,1,20),_RaqmonParticipantDestL2Priority_Type())
raqmonParticipantDestL2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantDestL2Priority.setStatus(_B)
class _RaqmonParticipantSrcDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_RaqmonParticipantSrcDSCP_Type.__name__=_D
_RaqmonParticipantSrcDSCP_Object=MibTableColumn
raqmonParticipantSrcDSCP=_RaqmonParticipantSrcDSCP_Object((1,3,6,1,2,1,16,31,1,1,1,1,21),_RaqmonParticipantSrcDSCP_Type())
raqmonParticipantSrcDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantSrcDSCP.setStatus(_B)
class _RaqmonParticipantDestDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_RaqmonParticipantDestDSCP_Type.__name__=_D
_RaqmonParticipantDestDSCP_Object=MibTableColumn
raqmonParticipantDestDSCP=_RaqmonParticipantDestDSCP_Object((1,3,6,1,2,1,16,31,1,1,1,1,22),_RaqmonParticipantDestDSCP_Type())
raqmonParticipantDestDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantDestDSCP.setStatus(_B)
class _RaqmonParticipantCpuMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantCpuMean_Type.__name__=_D
_RaqmonParticipantCpuMean_Object=MibTableColumn
raqmonParticipantCpuMean=_RaqmonParticipantCpuMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,23),_RaqmonParticipantCpuMean_Type())
raqmonParticipantCpuMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantCpuMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantCpuMean.setUnits(_F)
class _RaqmonParticipantCpuMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantCpuMin_Type.__name__=_D
_RaqmonParticipantCpuMin_Object=MibTableColumn
raqmonParticipantCpuMin=_RaqmonParticipantCpuMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,24),_RaqmonParticipantCpuMin_Type())
raqmonParticipantCpuMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantCpuMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantCpuMin.setUnits(_F)
class _RaqmonParticipantCpuMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantCpuMax_Type.__name__=_D
_RaqmonParticipantCpuMax_Object=MibTableColumn
raqmonParticipantCpuMax=_RaqmonParticipantCpuMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,25),_RaqmonParticipantCpuMax_Type())
raqmonParticipantCpuMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantCpuMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantCpuMax.setUnits(_F)
class _RaqmonParticipantMemoryMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantMemoryMean_Type.__name__=_D
_RaqmonParticipantMemoryMean_Object=MibTableColumn
raqmonParticipantMemoryMean=_RaqmonParticipantMemoryMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,26),_RaqmonParticipantMemoryMean_Type())
raqmonParticipantMemoryMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantMemoryMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantMemoryMean.setUnits(_F)
class _RaqmonParticipantMemoryMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantMemoryMin_Type.__name__=_D
_RaqmonParticipantMemoryMin_Object=MibTableColumn
raqmonParticipantMemoryMin=_RaqmonParticipantMemoryMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,27),_RaqmonParticipantMemoryMin_Type())
raqmonParticipantMemoryMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantMemoryMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantMemoryMin.setUnits(_F)
class _RaqmonParticipantMemoryMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantMemoryMax_Type.__name__=_D
_RaqmonParticipantMemoryMax_Object=MibTableColumn
raqmonParticipantMemoryMax=_RaqmonParticipantMemoryMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,28),_RaqmonParticipantMemoryMax_Type())
raqmonParticipantMemoryMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantMemoryMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantMemoryMax.setUnits(_F)
class _RaqmonParticipantNetRTTMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantNetRTTMean_Type.__name__=_D
_RaqmonParticipantNetRTTMean_Object=MibTableColumn
raqmonParticipantNetRTTMean=_RaqmonParticipantNetRTTMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,29),_RaqmonParticipantNetRTTMean_Type())
raqmonParticipantNetRTTMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantNetRTTMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantNetRTTMean.setUnits(_E)
class _RaqmonParticipantNetRTTMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantNetRTTMin_Type.__name__=_D
_RaqmonParticipantNetRTTMin_Object=MibTableColumn
raqmonParticipantNetRTTMin=_RaqmonParticipantNetRTTMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,30),_RaqmonParticipantNetRTTMin_Type())
raqmonParticipantNetRTTMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantNetRTTMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantNetRTTMin.setUnits(_E)
class _RaqmonParticipantNetRTTMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantNetRTTMax_Type.__name__=_D
_RaqmonParticipantNetRTTMax_Object=MibTableColumn
raqmonParticipantNetRTTMax=_RaqmonParticipantNetRTTMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,31),_RaqmonParticipantNetRTTMax_Type())
raqmonParticipantNetRTTMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantNetRTTMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantNetRTTMax.setUnits(_E)
class _RaqmonParticipantIAJitterMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantIAJitterMean_Type.__name__=_D
_RaqmonParticipantIAJitterMean_Object=MibTableColumn
raqmonParticipantIAJitterMean=_RaqmonParticipantIAJitterMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,32),_RaqmonParticipantIAJitterMean_Type())
raqmonParticipantIAJitterMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantIAJitterMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantIAJitterMean.setUnits(_E)
class _RaqmonParticipantIAJitterMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantIAJitterMin_Type.__name__=_D
_RaqmonParticipantIAJitterMin_Object=MibTableColumn
raqmonParticipantIAJitterMin=_RaqmonParticipantIAJitterMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,33),_RaqmonParticipantIAJitterMin_Type())
raqmonParticipantIAJitterMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantIAJitterMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantIAJitterMin.setUnits(_E)
class _RaqmonParticipantIAJitterMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantIAJitterMax_Type.__name__=_D
_RaqmonParticipantIAJitterMax_Object=MibTableColumn
raqmonParticipantIAJitterMax=_RaqmonParticipantIAJitterMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,34),_RaqmonParticipantIAJitterMax_Type())
raqmonParticipantIAJitterMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantIAJitterMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantIAJitterMax.setUnits(_E)
class _RaqmonParticipantIPDVMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantIPDVMean_Type.__name__=_D
_RaqmonParticipantIPDVMean_Object=MibTableColumn
raqmonParticipantIPDVMean=_RaqmonParticipantIPDVMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,35),_RaqmonParticipantIPDVMean_Type())
raqmonParticipantIPDVMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantIPDVMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantIPDVMean.setUnits(_E)
class _RaqmonParticipantIPDVMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantIPDVMin_Type.__name__=_D
_RaqmonParticipantIPDVMin_Object=MibTableColumn
raqmonParticipantIPDVMin=_RaqmonParticipantIPDVMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,36),_RaqmonParticipantIPDVMin_Type())
raqmonParticipantIPDVMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantIPDVMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantIPDVMin.setUnits(_E)
class _RaqmonParticipantIPDVMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantIPDVMax_Type.__name__=_D
_RaqmonParticipantIPDVMax_Object=MibTableColumn
raqmonParticipantIPDVMax=_RaqmonParticipantIPDVMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,37),_RaqmonParticipantIPDVMax_Type())
raqmonParticipantIPDVMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantIPDVMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantIPDVMax.setUnits(_E)
class _RaqmonParticipantNetOwdMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantNetOwdMean_Type.__name__=_D
_RaqmonParticipantNetOwdMean_Object=MibTableColumn
raqmonParticipantNetOwdMean=_RaqmonParticipantNetOwdMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,38),_RaqmonParticipantNetOwdMean_Type())
raqmonParticipantNetOwdMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantNetOwdMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantNetOwdMean.setUnits(_E)
class _RaqmonParticipantNetOwdMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantNetOwdMin_Type.__name__=_D
_RaqmonParticipantNetOwdMin_Object=MibTableColumn
raqmonParticipantNetOwdMin=_RaqmonParticipantNetOwdMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,39),_RaqmonParticipantNetOwdMin_Type())
raqmonParticipantNetOwdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantNetOwdMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantNetOwdMin.setUnits(_E)
class _RaqmonParticipantNetOwdMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantNetOwdMax_Type.__name__=_D
_RaqmonParticipantNetOwdMax_Object=MibTableColumn
raqmonParticipantNetOwdMax=_RaqmonParticipantNetOwdMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,40),_RaqmonParticipantNetOwdMax_Type())
raqmonParticipantNetOwdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantNetOwdMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantNetOwdMax.setUnits(_E)
class _RaqmonParticipantAppDelayMean_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantAppDelayMean_Type.__name__=_D
_RaqmonParticipantAppDelayMean_Object=MibTableColumn
raqmonParticipantAppDelayMean=_RaqmonParticipantAppDelayMean_Object((1,3,6,1,2,1,16,31,1,1,1,1,41),_RaqmonParticipantAppDelayMean_Type())
raqmonParticipantAppDelayMean.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAppDelayMean.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantAppDelayMean.setUnits(_E)
class _RaqmonParticipantAppDelayMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantAppDelayMin_Type.__name__=_D
_RaqmonParticipantAppDelayMin_Object=MibTableColumn
raqmonParticipantAppDelayMin=_RaqmonParticipantAppDelayMin_Object((1,3,6,1,2,1,16,31,1,1,1,1,42),_RaqmonParticipantAppDelayMin_Type())
raqmonParticipantAppDelayMin.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAppDelayMin.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantAppDelayMin.setUnits(_E)
class _RaqmonParticipantAppDelayMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantAppDelayMax_Type.__name__=_D
_RaqmonParticipantAppDelayMax_Object=MibTableColumn
raqmonParticipantAppDelayMax=_RaqmonParticipantAppDelayMax_Object((1,3,6,1,2,1,16,31,1,1,1,1,43),_RaqmonParticipantAppDelayMax_Type())
raqmonParticipantAppDelayMax.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAppDelayMax.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantAppDelayMax.setUnits(_E)
class _RaqmonParticipantPacketsRcvd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantPacketsRcvd_Type.__name__=_D
_RaqmonParticipantPacketsRcvd_Object=MibTableColumn
raqmonParticipantPacketsRcvd=_RaqmonParticipantPacketsRcvd_Object((1,3,6,1,2,1,16,31,1,1,1,1,44),_RaqmonParticipantPacketsRcvd_Type())
raqmonParticipantPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantPacketsRcvd.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantPacketsRcvd.setUnits(_G)
class _RaqmonParticipantPacketsSent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantPacketsSent_Type.__name__=_D
_RaqmonParticipantPacketsSent_Object=MibTableColumn
raqmonParticipantPacketsSent=_RaqmonParticipantPacketsSent_Object((1,3,6,1,2,1,16,31,1,1,1,1,45),_RaqmonParticipantPacketsSent_Type())
raqmonParticipantPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantPacketsSent.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantPacketsSent.setUnits(_G)
class _RaqmonParticipantOctetsRcvd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantOctetsRcvd_Type.__name__=_D
_RaqmonParticipantOctetsRcvd_Object=MibTableColumn
raqmonParticipantOctetsRcvd=_RaqmonParticipantOctetsRcvd_Object((1,3,6,1,2,1,16,31,1,1,1,1,46),_RaqmonParticipantOctetsRcvd_Type())
raqmonParticipantOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantOctetsRcvd.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantOctetsRcvd.setUnits(_W)
class _RaqmonParticipantOctetsSent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantOctetsSent_Type.__name__=_D
_RaqmonParticipantOctetsSent_Object=MibTableColumn
raqmonParticipantOctetsSent=_RaqmonParticipantOctetsSent_Object((1,3,6,1,2,1,16,31,1,1,1,1,47),_RaqmonParticipantOctetsSent_Type())
raqmonParticipantOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantOctetsSent.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantOctetsSent.setUnits(_W)
class _RaqmonParticipantLostPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantLostPackets_Type.__name__=_D
_RaqmonParticipantLostPackets_Object=MibTableColumn
raqmonParticipantLostPackets=_RaqmonParticipantLostPackets_Object((1,3,6,1,2,1,16,31,1,1,1,1,48),_RaqmonParticipantLostPackets_Type())
raqmonParticipantLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantLostPackets.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantLostPackets.setUnits(_G)
class _RaqmonParticipantLostPacketsFrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantLostPacketsFrct_Type.__name__=_D
_RaqmonParticipantLostPacketsFrct_Object=MibTableColumn
raqmonParticipantLostPacketsFrct=_RaqmonParticipantLostPacketsFrct_Object((1,3,6,1,2,1,16,31,1,1,1,1,49),_RaqmonParticipantLostPacketsFrct_Type())
raqmonParticipantLostPacketsFrct.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantLostPacketsFrct.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantLostPacketsFrct.setUnits(_F)
class _RaqmonParticipantDiscards_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonParticipantDiscards_Type.__name__=_D
_RaqmonParticipantDiscards_Object=MibTableColumn
raqmonParticipantDiscards=_RaqmonParticipantDiscards_Object((1,3,6,1,2,1,16,31,1,1,1,1,50),_RaqmonParticipantDiscards_Type())
raqmonParticipantDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantDiscards.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantDiscards.setUnits(_G)
class _RaqmonParticipantDiscardsFrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_RaqmonParticipantDiscardsFrct_Type.__name__=_D
_RaqmonParticipantDiscardsFrct_Object=MibTableColumn
raqmonParticipantDiscardsFrct=_RaqmonParticipantDiscardsFrct_Object((1,3,6,1,2,1,16,31,1,1,1,1,51),_RaqmonParticipantDiscardsFrct_Type())
raqmonParticipantDiscardsFrct.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantDiscardsFrct.setStatus(_B)
if mibBuilder.loadTexts:raqmonParticipantDiscardsFrct.setUnits(_F)
_RaqmonQosTable_Object=MibTable
raqmonQosTable=_RaqmonQosTable_Object((1,3,6,1,2,1,16,31,1,1,2))
if mibBuilder.loadTexts:raqmonQosTable.setStatus(_B)
_RaqmonQosEntry_Object=MibTableRow
raqmonQosEntry=_RaqmonQosEntry_Object((1,3,6,1,2,1,16,31,1,1,2,1))
raqmonQosEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_X))
if mibBuilder.loadTexts:raqmonQosEntry.setStatus(_B)
class _RaqmonQosTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaqmonQosTime_Type.__name__=_H
_RaqmonQosTime_Object=MibTableColumn
raqmonQosTime=_RaqmonQosTime_Object((1,3,6,1,2,1,16,31,1,1,2,1,1),_RaqmonQosTime_Type())
raqmonQosTime.setMaxAccess(_K)
if mibBuilder.loadTexts:raqmonQosTime.setStatus(_B)
if mibBuilder.loadTexts:raqmonQosTime.setUnits('seconds')
class _RaqmonQoSEnd2EndNetDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQoSEnd2EndNetDelay_Type.__name__=_D
_RaqmonQoSEnd2EndNetDelay_Object=MibTableColumn
raqmonQoSEnd2EndNetDelay=_RaqmonQoSEnd2EndNetDelay_Object((1,3,6,1,2,1,16,31,1,1,2,1,2),_RaqmonQoSEnd2EndNetDelay_Type())
raqmonQoSEnd2EndNetDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQoSEnd2EndNetDelay.setStatus(_B)
if mibBuilder.loadTexts:raqmonQoSEnd2EndNetDelay.setUnits(_E)
class _RaqmonQoSInterArrivalJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQoSInterArrivalJitter_Type.__name__=_D
_RaqmonQoSInterArrivalJitter_Object=MibTableColumn
raqmonQoSInterArrivalJitter=_RaqmonQoSInterArrivalJitter_Object((1,3,6,1,2,1,16,31,1,1,2,1,3),_RaqmonQoSInterArrivalJitter_Type())
raqmonQoSInterArrivalJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQoSInterArrivalJitter.setStatus(_B)
if mibBuilder.loadTexts:raqmonQoSInterArrivalJitter.setUnits(_E)
class _RaqmonQosRcvdPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQosRcvdPackets_Type.__name__=_D
_RaqmonQosRcvdPackets_Object=MibTableColumn
raqmonQosRcvdPackets=_RaqmonQosRcvdPackets_Object((1,3,6,1,2,1,16,31,1,1,2,1,4),_RaqmonQosRcvdPackets_Type())
raqmonQosRcvdPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQosRcvdPackets.setStatus(_B)
if mibBuilder.loadTexts:raqmonQosRcvdPackets.setUnits(_G)
class _RaqmonQosRcvdOctets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQosRcvdOctets_Type.__name__=_D
_RaqmonQosRcvdOctets_Object=MibTableColumn
raqmonQosRcvdOctets=_RaqmonQosRcvdOctets_Object((1,3,6,1,2,1,16,31,1,1,2,1,5),_RaqmonQosRcvdOctets_Type())
raqmonQosRcvdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQosRcvdOctets.setStatus(_B)
if mibBuilder.loadTexts:raqmonQosRcvdOctets.setUnits(_Y)
class _RaqmonQosSentPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQosSentPackets_Type.__name__=_D
_RaqmonQosSentPackets_Object=MibTableColumn
raqmonQosSentPackets=_RaqmonQosSentPackets_Object((1,3,6,1,2,1,16,31,1,1,2,1,6),_RaqmonQosSentPackets_Type())
raqmonQosSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQosSentPackets.setStatus(_B)
if mibBuilder.loadTexts:raqmonQosSentPackets.setUnits(_G)
class _RaqmonQosSentOctets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQosSentOctets_Type.__name__=_D
_RaqmonQosSentOctets_Object=MibTableColumn
raqmonQosSentOctets=_RaqmonQosSentOctets_Object((1,3,6,1,2,1,16,31,1,1,2,1,7),_RaqmonQosSentOctets_Type())
raqmonQosSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQosSentOctets.setStatus(_B)
if mibBuilder.loadTexts:raqmonQosSentOctets.setUnits(_Y)
class _RaqmonQosLostPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_RaqmonQosLostPackets_Type.__name__=_D
_RaqmonQosLostPackets_Object=MibTableColumn
raqmonQosLostPackets=_RaqmonQosLostPackets_Object((1,3,6,1,2,1,16,31,1,1,2,1,8),_RaqmonQosLostPackets_Type())
raqmonQosLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQosLostPackets.setStatus(_B)
if mibBuilder.loadTexts:raqmonQosLostPackets.setUnits(_G)
_RaqmonQosSessionStatus_Type=SnmpAdminString
_RaqmonQosSessionStatus_Object=MibTableColumn
raqmonQosSessionStatus=_RaqmonQosSessionStatus_Object((1,3,6,1,2,1,16,31,1,1,2,1,9),_RaqmonQosSessionStatus_Type())
raqmonQosSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonQosSessionStatus.setStatus(_B)
_RaqmonParticipantAddrTable_Object=MibTable
raqmonParticipantAddrTable=_RaqmonParticipantAddrTable_Object((1,3,6,1,2,1,16,31,1,1,3))
if mibBuilder.loadTexts:raqmonParticipantAddrTable.setStatus(_B)
_RaqmonParticipantAddrEntry_Object=MibTableRow
raqmonParticipantAddrEntry=_RaqmonParticipantAddrEntry_Object((1,3,6,1,2,1,16,31,1,1,3,1))
raqmonParticipantAddrEntry.setIndexNames((0,_A,_O),(0,_A,_L),(0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:raqmonParticipantAddrEntry.setStatus(_B)
_RaqmonParticipantAddrEndDate_Type=DateAndTime
_RaqmonParticipantAddrEndDate_Object=MibTableColumn
raqmonParticipantAddrEndDate=_RaqmonParticipantAddrEndDate_Object((1,3,6,1,2,1,16,31,1,1,3,1,1),_RaqmonParticipantAddrEndDate_Type())
raqmonParticipantAddrEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonParticipantAddrEndDate.setStatus(_B)
_RaqmonException_ObjectIdentity=ObjectIdentity
raqmonException=_RaqmonException_ObjectIdentity((1,3,6,1,2,1,16,31,1,2))
_RaqmonSessionExceptionTable_Object=MibTable
raqmonSessionExceptionTable=_RaqmonSessionExceptionTable_Object((1,3,6,1,2,1,16,31,1,2,2))
if mibBuilder.loadTexts:raqmonSessionExceptionTable.setStatus(_B)
_RaqmonSessionExceptionEntry_Object=MibTableRow
raqmonSessionExceptionEntry=_RaqmonSessionExceptionEntry_Object((1,3,6,1,2,1,16,31,1,2,2,1))
raqmonSessionExceptionEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:raqmonSessionExceptionEntry.setStatus(_B)
class _RaqmonSessionExceptionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RaqmonSessionExceptionIndex_Type.__name__=_H
_RaqmonSessionExceptionIndex_Object=MibTableColumn
raqmonSessionExceptionIndex=_RaqmonSessionExceptionIndex_Object((1,3,6,1,2,1,16,31,1,2,2,1,2),_RaqmonSessionExceptionIndex_Type())
raqmonSessionExceptionIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:raqmonSessionExceptionIndex.setStatus(_B)
_RaqmonSessionExceptionIAJitterThreshold_Type=Unsigned32
_RaqmonSessionExceptionIAJitterThreshold_Object=MibTableColumn
raqmonSessionExceptionIAJitterThreshold=_RaqmonSessionExceptionIAJitterThreshold_Object((1,3,6,1,2,1,16,31,1,2,2,1,3),_RaqmonSessionExceptionIAJitterThreshold_Type())
raqmonSessionExceptionIAJitterThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:raqmonSessionExceptionIAJitterThreshold.setStatus(_B)
if mibBuilder.loadTexts:raqmonSessionExceptionIAJitterThreshold.setUnits(_E)
_RaqmonSessionExceptionNetRTTThreshold_Type=Unsigned32
_RaqmonSessionExceptionNetRTTThreshold_Object=MibTableColumn
raqmonSessionExceptionNetRTTThreshold=_RaqmonSessionExceptionNetRTTThreshold_Object((1,3,6,1,2,1,16,31,1,2,2,1,4),_RaqmonSessionExceptionNetRTTThreshold_Type())
raqmonSessionExceptionNetRTTThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:raqmonSessionExceptionNetRTTThreshold.setStatus(_B)
if mibBuilder.loadTexts:raqmonSessionExceptionNetRTTThreshold.setUnits(_E)
class _RaqmonSessionExceptionLostPacketsThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RaqmonSessionExceptionLostPacketsThreshold_Type.__name__=_H
_RaqmonSessionExceptionLostPacketsThreshold_Object=MibTableColumn
raqmonSessionExceptionLostPacketsThreshold=_RaqmonSessionExceptionLostPacketsThreshold_Object((1,3,6,1,2,1,16,31,1,2,2,1,5),_RaqmonSessionExceptionLostPacketsThreshold_Type())
raqmonSessionExceptionLostPacketsThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:raqmonSessionExceptionLostPacketsThreshold.setStatus(_B)
if mibBuilder.loadTexts:raqmonSessionExceptionLostPacketsThreshold.setUnits('tenth of a percent')
_RaqmonSessionExceptionRowStatus_Type=RowStatus
_RaqmonSessionExceptionRowStatus_Object=MibTableColumn
raqmonSessionExceptionRowStatus=_RaqmonSessionExceptionRowStatus_Object((1,3,6,1,2,1,16,31,1,2,2,1,7),_RaqmonSessionExceptionRowStatus_Type())
raqmonSessionExceptionRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:raqmonSessionExceptionRowStatus.setStatus(_B)
_RaqmonConfig_ObjectIdentity=ObjectIdentity
raqmonConfig=_RaqmonConfig_ObjectIdentity((1,3,6,1,2,1,16,31,1,3))
_RaqmonConfigPort_Type=InetPortNumber
_RaqmonConfigPort_Object=MibScalar
raqmonConfigPort=_RaqmonConfigPort_Object((1,3,6,1,2,1,16,31,1,3,1),_RaqmonConfigPort_Type())
raqmonConfigPort.setMaxAccess(_a)
if mibBuilder.loadTexts:raqmonConfigPort.setStatus(_B)
class _RaqmonConfigPduTransport_Type(Bits):namedValues=NamedValues(*(('other',0),('tcp',1),('snmp',2)))
_RaqmonConfigPduTransport_Type.__name__=_N
_RaqmonConfigPduTransport_Object=MibScalar
raqmonConfigPduTransport=_RaqmonConfigPduTransport_Object((1,3,6,1,2,1,16,31,1,3,2),_RaqmonConfigPduTransport_Type())
raqmonConfigPduTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonConfigPduTransport.setStatus(_B)
_RaqmonConfigRaqmonPdus_Type=Counter32
_RaqmonConfigRaqmonPdus_Object=MibScalar
raqmonConfigRaqmonPdus=_RaqmonConfigRaqmonPdus_Object((1,3,6,1,2,1,16,31,1,3,3),_RaqmonConfigRaqmonPdus_Type())
raqmonConfigRaqmonPdus.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonConfigRaqmonPdus.setStatus(_B)
if mibBuilder.loadTexts:raqmonConfigRaqmonPdus.setUnits('PDUs')
_RaqmonConfigRDSTimeout_Type=Unsigned32
_RaqmonConfigRDSTimeout_Object=MibScalar
raqmonConfigRDSTimeout=_RaqmonConfigRDSTimeout_Object((1,3,6,1,2,1,16,31,1,3,4),_RaqmonConfigRDSTimeout_Type())
raqmonConfigRDSTimeout.setMaxAccess(_a)
if mibBuilder.loadTexts:raqmonConfigRDSTimeout.setStatus(_B)
_RaqmonConformance_ObjectIdentity=ObjectIdentity
raqmonConformance=_RaqmonConformance_ObjectIdentity((1,3,6,1,2,1,16,31,2))
_RaqmonCompliances_ObjectIdentity=ObjectIdentity
raqmonCompliances=_RaqmonCompliances_ObjectIdentity((1,3,6,1,2,1,16,31,2,1))
_RaqmonGroups_ObjectIdentity=ObjectIdentity
raqmonGroups=_RaqmonGroups_ObjectIdentity((1,3,6,1,2,1,16,31,2,2))
raqmonCollectorGroup=ObjectGroup((1,3,6,1,2,1,16,31,2,2,1))
raqmonCollectorGroup.setObjects(*((_A,_b),(_A,_O),(_A,_L),(_A,_c),(_A,_d),(_A,_e),(_A,_P),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_Q),(_A,_R),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_S),(_A,_T),(_A,_U),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_V),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:raqmonCollectorGroup.setStatus(_B)
raqmonSessionAlarm=NotificationType((1,3,6,1,2,1,16,31,0,1))
raqmonSessionAlarm.setObjects(*((_A,_L),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_U)))
if mibBuilder.loadTexts:raqmonSessionAlarm.setStatus(_B)
raqmonCollectorNotificationsGroup=NotificationGroup((1,3,6,1,2,1,16,31,2,2,2))
raqmonCollectorNotificationsGroup.setObjects((_A,_AW))
if mibBuilder.loadTexts:raqmonCollectorNotificationsGroup.setStatus(_B)
raqmonCompliance=ModuleCompliance((1,3,6,1,2,1,16,31,2,1,1))
raqmonCompliance.setObjects(*((_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:raqmonCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'raqmonMIB':raqmonMIB,'raqmonNotifications':raqmonNotifications,_AW:raqmonSessionAlarm,'raqmonMIBObjects':raqmonMIBObjects,'raqmonSession':raqmonSession,'raqmonParticipantTable':raqmonParticipantTable,'raqmonParticipantEntry':raqmonParticipantEntry,_I:raqmonParticipantStartDate,_J:raqmonParticipantIndex,_b:raqmonParticipantReportCaps,_O:raqmonParticipantAddrType,_L:raqmonParticipantAddr,_c:raqmonParticipantSendPort,_d:raqmonParticipantRecvPort,_e:raqmonParticipantSetupDelay,_P:raqmonParticipantName,_f:raqmonParticipantAppName,_g:raqmonParticipantQosCount,_h:raqmonParticipantEndDate,_i:raqmonParticipantDestPayloadType,_j:raqmonParticipantSrcPayloadType,_k:raqmonParticipantActive,_l:raqmonParticipantPeer,_Q:raqmonParticipantPeerAddrType,_R:raqmonParticipantPeerAddr,_m:raqmonParticipantSrcL2Priority,_n:raqmonParticipantDestL2Priority,_o:raqmonParticipantSrcDSCP,_p:raqmonParticipantDestDSCP,_q:raqmonParticipantCpuMean,_r:raqmonParticipantCpuMin,_s:raqmonParticipantCpuMax,_t:raqmonParticipantMemoryMean,_u:raqmonParticipantMemoryMin,_v:raqmonParticipantMemoryMax,_w:raqmonParticipantNetRTTMean,_x:raqmonParticipantNetRTTMin,_y:raqmonParticipantNetRTTMax,_z:raqmonParticipantIAJitterMean,_A0:raqmonParticipantIAJitterMin,_A1:raqmonParticipantIAJitterMax,_A2:raqmonParticipantIPDVMean,_A3:raqmonParticipantIPDVMin,_A4:raqmonParticipantIPDVMax,_A5:raqmonParticipantNetOwdMean,_A6:raqmonParticipantNetOwdMin,_A7:raqmonParticipantNetOwdMax,_A8:raqmonParticipantAppDelayMean,_A9:raqmonParticipantAppDelayMin,_AA:raqmonParticipantAppDelayMax,_AB:raqmonParticipantPacketsRcvd,_AC:raqmonParticipantPacketsSent,_AD:raqmonParticipantOctetsRcvd,_AE:raqmonParticipantOctetsSent,_AF:raqmonParticipantLostPackets,_AG:raqmonParticipantLostPacketsFrct,_AH:raqmonParticipantDiscards,_AI:raqmonParticipantDiscardsFrct,'raqmonQosTable':raqmonQosTable,'raqmonQosEntry':raqmonQosEntry,_X:raqmonQosTime,_S:raqmonQoSEnd2EndNetDelay,_T:raqmonQoSInterArrivalJitter,_U:raqmonQosRcvdPackets,_AJ:raqmonQosRcvdOctets,_AK:raqmonQosSentPackets,_AL:raqmonQosSentOctets,_V:raqmonQosLostPackets,_AM:raqmonQosSessionStatus,'raqmonParticipantAddrTable':raqmonParticipantAddrTable,'raqmonParticipantAddrEntry':raqmonParticipantAddrEntry,_AN:raqmonParticipantAddrEndDate,'raqmonException':raqmonException,'raqmonSessionExceptionTable':raqmonSessionExceptionTable,'raqmonSessionExceptionEntry':raqmonSessionExceptionEntry,_Z:raqmonSessionExceptionIndex,_AP:raqmonSessionExceptionIAJitterThreshold,_AQ:raqmonSessionExceptionNetRTTThreshold,_AR:raqmonSessionExceptionLostPacketsThreshold,_AS:raqmonSessionExceptionRowStatus,'raqmonConfig':raqmonConfig,_AO:raqmonConfigPort,_AT:raqmonConfigPduTransport,_AU:raqmonConfigRaqmonPdus,_AV:raqmonConfigRDSTimeout,'raqmonConformance':raqmonConformance,'raqmonCompliances':raqmonCompliances,'raqmonCompliance':raqmonCompliance,'raqmonGroups':raqmonGroups,_AX:raqmonCollectorGroup,_AY:raqmonCollectorNotificationsGroup})