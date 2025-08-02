_Q='fsMIStdOspfTrapEntry'
_P='fsMIStdOspfVirtNbrState'
_O='fsMIStdOspfVirtIfState'
_N='fsMIStdOspfNbrState'
_M='fsMIStdOspfIfState'
_L='OctetString'
_K='read-only'
_J='Integer32'
_I='fsMIStdOspfNbrRtrId'
_H='fsMIStdOspfExtLsdbLimit'
_G='fsMIStdOspfPacketSrc'
_F='fsMIStdOspfConfigErrorType'
_E='fsMIStdOspfPacketType'
_D='ARICENT-OSPFMI-TRAP-MIB'
_C='fsMIStdOspfRouterId'
_B='current'
_A='ARICENT-MISTDOSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMIStdOspfEntry,fsMIStdOspfExtLsdbLimit,fsMIStdOspfIfState,fsMIStdOspfNbrRtrId,fsMIStdOspfNbrState,fsMIStdOspfRouterId,fsMIStdOspfVirtIfState,fsMIStdOspfVirtNbrState=mibBuilder.importSymbols(_A,'fsMIStdOspfEntry',_H,_M,_I,_N,_C,_O,_P)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsMIStdOspfTrap=ModuleIdentity((1,3,6,1,4,1,2076,148))
if mibBuilder.loadTexts:fsMIStdOspfTrap.setRevisions(('2012-09-05 00:00',))
_FsMIStdOspfTraps_ObjectIdentity=ObjectIdentity
fsMIStdOspfTraps=_FsMIStdOspfTraps_ObjectIdentity((1,3,6,1,4,1,2076,148,0))
_FsMIStdOspfTrapControl_ObjectIdentity=ObjectIdentity
fsMIStdOspfTrapControl=_FsMIStdOspfTrapControl_ObjectIdentity((1,3,6,1,4,1,2076,148,1))
_FsMIStdOspfTrapTable_Object=MibTable
fsMIStdOspfTrapTable=_FsMIStdOspfTrapTable_Object((1,3,6,1,4,1,2076,148,1,1))
if mibBuilder.loadTexts:fsMIStdOspfTrapTable.setStatus(_B)
_FsMIStdOspfTrapEntry_Object=MibTableRow
fsMIStdOspfTrapEntry=_FsMIStdOspfTrapEntry_Object((1,3,6,1,4,1,2076,148,1,1,1))
if mibBuilder.loadTexts:fsMIStdOspfTrapEntry.setStatus(_B)
class _FsMIStdOspfSetTrap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FsMIStdOspfSetTrap_Type.__name__=_L
_FsMIStdOspfSetTrap_Object=MibTableColumn
fsMIStdOspfSetTrap=_FsMIStdOspfSetTrap_Object((1,3,6,1,4,1,2076,148,1,1,1,1),_FsMIStdOspfSetTrap_Type())
fsMIStdOspfSetTrap.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsMIStdOspfSetTrap.setStatus(_B)
class _FsMIStdOspfConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('authTypeMismatch',5),('authFailure',6),('netMaskMismatch',7),('helloIntervalMismatch',8),('deadIntervalMismatch',9),('optionMismatch',10)))
_FsMIStdOspfConfigErrorType_Type.__name__=_J
_FsMIStdOspfConfigErrorType_Object=MibTableColumn
fsMIStdOspfConfigErrorType=_FsMIStdOspfConfigErrorType_Object((1,3,6,1,4,1,2076,148,1,1,1,2),_FsMIStdOspfConfigErrorType_Type())
fsMIStdOspfConfigErrorType.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIStdOspfConfigErrorType.setStatus(_B)
class _FsMIStdOspfPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('hello',1),('dbDescript',2),('lsReq',3),('lsUpdate',4),('lsAck',5)))
_FsMIStdOspfPacketType_Type.__name__=_J
_FsMIStdOspfPacketType_Object=MibTableColumn
fsMIStdOspfPacketType=_FsMIStdOspfPacketType_Object((1,3,6,1,4,1,2076,148,1,1,1,3),_FsMIStdOspfPacketType_Type())
fsMIStdOspfPacketType.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIStdOspfPacketType.setStatus(_B)
_FsMIStdOspfPacketSrc_Type=IpAddress
_FsMIStdOspfPacketSrc_Object=MibTableColumn
fsMIStdOspfPacketSrc=_FsMIStdOspfPacketSrc_Object((1,3,6,1,4,1,2076,148,1,1,1,4),_FsMIStdOspfPacketSrc_Type())
fsMIStdOspfPacketSrc.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIStdOspfPacketSrc.setStatus(_B)
fsMIStdOspfEntry.registerAugmentions((_D,_Q))
fsMIStdOspfTrapEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
ospfVirtIfStateChange=NotificationType((1,3,6,1,4,1,2076,148,0,1))
ospfVirtIfStateChange.setObjects(*((_A,_C),(_A,_O)))
if mibBuilder.loadTexts:ospfVirtIfStateChange.setStatus(_B)
ospfNbrStateChange=NotificationType((1,3,6,1,4,1,2076,148,0,2))
ospfNbrStateChange.setObjects(*((_A,_C),(_A,_I),(_A,_N)))
if mibBuilder.loadTexts:ospfNbrStateChange.setStatus(_B)
ospfVirtNbrStateChange=NotificationType((1,3,6,1,4,1,2076,148,0,3))
ospfVirtNbrStateChange.setObjects(*((_A,_C),(_A,_P)))
if mibBuilder.loadTexts:ospfVirtNbrStateChange.setStatus(_B)
ospfIfConfigError=NotificationType((1,3,6,1,4,1,2076,148,0,4))
ospfIfConfigError.setObjects(*((_A,_C),(_D,_G),(_D,_F),(_D,_E)))
if mibBuilder.loadTexts:ospfIfConfigError.setStatus(_B)
ospfVirtIfConfigError=NotificationType((1,3,6,1,4,1,2076,148,0,5))
ospfVirtIfConfigError.setObjects(*((_A,_C),(_D,_F),(_D,_E)))
if mibBuilder.loadTexts:ospfVirtIfConfigError.setStatus(_B)
ospfIfAuthFailure=NotificationType((1,3,6,1,4,1,2076,148,0,6))
ospfIfAuthFailure.setObjects(*((_A,_C),(_D,_G),(_D,_F),(_D,_E)))
if mibBuilder.loadTexts:ospfIfAuthFailure.setStatus(_B)
ospfVirtIfAuthFailure=NotificationType((1,3,6,1,4,1,2076,148,0,7))
ospfVirtIfAuthFailure.setObjects(*((_A,_C),(_D,_F),(_D,_E)))
if mibBuilder.loadTexts:ospfVirtIfAuthFailure.setStatus(_B)
ospfIfRxBadPacket=NotificationType((1,3,6,1,4,1,2076,148,0,8))
ospfIfRxBadPacket.setObjects(*((_A,_C),(_D,_G),(_D,_E)))
if mibBuilder.loadTexts:ospfIfRxBadPacket.setStatus(_B)
ospfVirtIfRxBadPacket=NotificationType((1,3,6,1,4,1,2076,148,0,9))
ospfVirtIfRxBadPacket.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:ospfVirtIfRxBadPacket.setStatus(_B)
ospfTxRetransmit=NotificationType((1,3,6,1,4,1,2076,148,0,10))
ospfTxRetransmit.setObjects(*((_A,_C),(_A,_I),(_D,_E)))
if mibBuilder.loadTexts:ospfTxRetransmit.setStatus(_B)
ospfVirtIfTxRetransmit=NotificationType((1,3,6,1,4,1,2076,148,0,11))
ospfVirtIfTxRetransmit.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:ospfVirtIfTxRetransmit.setStatus(_B)
ospfOriginateLsa=NotificationType((1,3,6,1,4,1,2076,148,0,12))
ospfOriginateLsa.setObjects((_A,_C))
if mibBuilder.loadTexts:ospfOriginateLsa.setStatus(_B)
ospfMaxAgeLsa=NotificationType((1,3,6,1,4,1,2076,148,0,13))
ospfMaxAgeLsa.setObjects((_A,_C))
if mibBuilder.loadTexts:ospfMaxAgeLsa.setStatus(_B)
ospfLsdbOverflow=NotificationType((1,3,6,1,4,1,2076,148,0,14))
ospfLsdbOverflow.setObjects(*((_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ospfLsdbOverflow.setStatus(_B)
ospfLsdbApproachingOverflow=NotificationType((1,3,6,1,4,1,2076,148,0,15))
ospfLsdbApproachingOverflow.setObjects(*((_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ospfLsdbApproachingOverflow.setStatus(_B)
ospfIfStateChange=NotificationType((1,3,6,1,4,1,2076,148,0,16))
ospfIfStateChange.setObjects(*((_A,_C),(_A,_M)))
if mibBuilder.loadTexts:ospfIfStateChange.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'fsMIStdOspfTrap':fsMIStdOspfTrap,'fsMIStdOspfTraps':fsMIStdOspfTraps,'ospfVirtIfStateChange':ospfVirtIfStateChange,'ospfNbrStateChange':ospfNbrStateChange,'ospfVirtNbrStateChange':ospfVirtNbrStateChange,'ospfIfConfigError':ospfIfConfigError,'ospfVirtIfConfigError':ospfVirtIfConfigError,'ospfIfAuthFailure':ospfIfAuthFailure,'ospfVirtIfAuthFailure':ospfVirtIfAuthFailure,'ospfIfRxBadPacket':ospfIfRxBadPacket,'ospfVirtIfRxBadPacket':ospfVirtIfRxBadPacket,'ospfTxRetransmit':ospfTxRetransmit,'ospfVirtIfTxRetransmit':ospfVirtIfTxRetransmit,'ospfOriginateLsa':ospfOriginateLsa,'ospfMaxAgeLsa':ospfMaxAgeLsa,'ospfLsdbOverflow':ospfLsdbOverflow,'ospfLsdbApproachingOverflow':ospfLsdbApproachingOverflow,'ospfIfStateChange':ospfIfStateChange,'fsMIStdOspfTrapControl':fsMIStdOspfTrapControl,'fsMIStdOspfTrapTable':fsMIStdOspfTrapTable,_Q:fsMIStdOspfTrapEntry,'fsMIStdOspfSetTrap':fsMIStdOspfSetTrap,_F:fsMIStdOspfConfigErrorType,_E:fsMIStdOspfPacketType,_G:fsMIStdOspfPacketSrc})