_V='NotificationType'
_U='snOspfVirtNbrState'
_T='snOspfVirtNbrRtrId'
_S='snOspfVirtNbrArea'
_R='snOspfVirtIfStatusState'
_Q='snOspfNbrState'
_P='snOspfNbrIpAddr'
_O='snOspfIfStatusState'
_N='snOspfNbrRtrId'
_M='snOspfLsdbAreaId'
_L='snOspfExtLsdbLimit'
_K='snOspfPacketSrc'
_J='snOspfLsdbType'
_I='snOspfLsdbRouterId'
_H='snOspfLsdbLsId'
_G='snOspfConfigErrorType'
_F='snOspfVirtIfStatusNeighbor'
_E='snOspfVirtIfStatusAreaID'
_D='snOspfIfStatusIpAddress'
_C='snOspfPacketType'
_B='snOspfRouterId'
_A='HP-SN-OSPF-GROUP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snOspfConfigErrorType,snOspfExtLsdbLimit,snOspfIfStatusIpAddress,snOspfIfStatusState,snOspfLsdbAreaId,snOspfLsdbLsId,snOspfLsdbRouterId,snOspfLsdbType,snOspfNbrIpAddr,snOspfNbrRtrId,snOspfNbrState,snOspfPacketSrc,snOspfPacketType,snOspfRouterId,snOspfVirtIfStatusAreaID,snOspfVirtIfStatusNeighbor,snOspfVirtIfStatusState,snOspfVirtNbrArea,snOspfVirtNbrRtrId,snOspfVirtNbrState=mibBuilder.importSymbols(_A,_G,_L,_D,_O,_M,_H,_I,_J,_P,_N,_Q,_K,_C,_B,_E,_F,_R,_S,_T,_U)
hp,=mibBuilder.importSymbols('HP-SN-ROOT-MIB','hp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_V,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_V,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snTrapOspfIfStateChange=NotificationType((1,3,6,1,4,1,11,0,3))
snTrapOspfIfStateChange.setObjects(*((_A,_B),(_A,_D),(_A,_O)))
if mibBuilder.loadTexts:snTrapOspfIfStateChange.setStatus('')
snTrapOspfVirtIfStateChange=NotificationType((1,3,6,1,4,1,11,0,4))
snTrapOspfVirtIfStateChange.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:snTrapOspfVirtIfStateChange.setStatus('')
snOspfNbrStateChange=NotificationType((1,3,6,1,4,1,11,0,5))
snOspfNbrStateChange.setObjects(*((_A,_B),(_A,_P),(_A,_N),(_A,_Q)))
if mibBuilder.loadTexts:snOspfNbrStateChange.setStatus('')
snOspfVirtNbrStateChange=NotificationType((1,3,6,1,4,1,11,0,6))
snOspfVirtNbrStateChange.setObjects(*((_A,_B),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:snOspfVirtNbrStateChange.setStatus('')
snOspfIfConfigError=NotificationType((1,3,6,1,4,1,11,0,7))
snOspfIfConfigError.setObjects(*((_A,_B),(_A,_D),(_A,_K),(_A,_G),(_A,_C)))
if mibBuilder.loadTexts:snOspfIfConfigError.setStatus('')
snOspfVirtIfConfigError=NotificationType((1,3,6,1,4,1,11,0,8))
snOspfVirtIfConfigError.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_C)))
if mibBuilder.loadTexts:snOspfVirtIfConfigError.setStatus('')
snOspfIfAuthFailure=NotificationType((1,3,6,1,4,1,11,0,9))
snOspfIfAuthFailure.setObjects(*((_A,_B),(_A,_D),(_A,_K),(_A,_G),(_A,_C)))
if mibBuilder.loadTexts:snOspfIfAuthFailure.setStatus('')
snOspfVirtIfAuthFailure=NotificationType((1,3,6,1,4,1,11,0,10))
snOspfVirtIfAuthFailure.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_C)))
if mibBuilder.loadTexts:snOspfVirtIfAuthFailure.setStatus('')
snOspfIfRxBadPacket=NotificationType((1,3,6,1,4,1,11,0,11))
snOspfIfRxBadPacket.setObjects(*((_A,_B),(_A,_D),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:snOspfIfRxBadPacket.setStatus('')
snOspfVirtIfRxBadPacket=NotificationType((1,3,6,1,4,1,11,0,12))
snOspfVirtIfRxBadPacket.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:snOspfVirtIfRxBadPacket.setStatus('')
snOspfTxRetransmit=NotificationType((1,3,6,1,4,1,11,0,13))
snOspfTxRetransmit.setObjects(*((_A,_B),(_A,_D),(_A,_N),(_A,_C),(_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:snOspfTxRetransmit.setStatus('')
ospfVirtIfTxRetransmit=NotificationType((1,3,6,1,4,1,11,0,14))
ospfVirtIfTxRetransmit.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_C),(_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ospfVirtIfTxRetransmit.setStatus('')
snOspfOriginateLsa=NotificationType((1,3,6,1,4,1,11,0,15))
snOspfOriginateLsa.setObjects(*((_A,_B),(_A,_M),(_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:snOspfOriginateLsa.setStatus('')
snOspfMaxAgeLsa=NotificationType((1,3,6,1,4,1,11,0,16))
snOspfMaxAgeLsa.setObjects(*((_A,_B),(_A,_M),(_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:snOspfMaxAgeLsa.setStatus('')
snOspfLsdbOverflow=NotificationType((1,3,6,1,4,1,11,0,17))
snOspfLsdbOverflow.setObjects(*((_A,_B),(_A,_L)))
if mibBuilder.loadTexts:snOspfLsdbOverflow.setStatus('')
snOspfLsdbApproachingOverflow=NotificationType((1,3,6,1,4,1,11,0,18))
snOspfLsdbApproachingOverflow.setObjects(*((_A,_B),(_A,_L)))
if mibBuilder.loadTexts:snOspfLsdbApproachingOverflow.setStatus('')
mibBuilder.exportSymbols('HP-SN-ROUTER-TRAP-MIB',**{'snTrapOspfIfStateChange':snTrapOspfIfStateChange,'snTrapOspfVirtIfStateChange':snTrapOspfVirtIfStateChange,'snOspfNbrStateChange':snOspfNbrStateChange,'snOspfVirtNbrStateChange':snOspfVirtNbrStateChange,'snOspfIfConfigError':snOspfIfConfigError,'snOspfVirtIfConfigError':snOspfVirtIfConfigError,'snOspfIfAuthFailure':snOspfIfAuthFailure,'snOspfVirtIfAuthFailure':snOspfVirtIfAuthFailure,'snOspfIfRxBadPacket':snOspfIfRxBadPacket,'snOspfVirtIfRxBadPacket':snOspfVirtIfRxBadPacket,'snOspfTxRetransmit':snOspfTxRetransmit,'ospfVirtIfTxRetransmit':ospfVirtIfTxRetransmit,'snOspfOriginateLsa':snOspfOriginateLsa,'snOspfMaxAgeLsa':snOspfMaxAgeLsa,'snOspfLsdbOverflow':snOspfLsdbOverflow,'snOspfLsdbApproachingOverflow':snOspfLsdbApproachingOverflow})