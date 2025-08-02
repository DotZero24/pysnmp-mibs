_b='cesOverWlanUnit0PacketJitterStatusChange'
_a='cesOverWlanUnit0PacketMalformedPackets'
_Z='cesOverWlanUnit0PacketDuplicatePackets'
_Y='cesOverWlanUnit0PacketInvalidSequencePackets'
_X='cesOverWlanUnit0PacketOverrunPackets'
_W='cesOverWlanUnit0PacketUnderrunPackets'
_V='cesOverWlanUnit0PacketOutOfOrderPackets'
_U='cesOverWlanUnit0PacketLostPackets'
_T='cesOverWlanUnit0PacketLatePackets'
_S='cesOverWlanUnit0PacketLbitPackets'
_R='cesOverWlanUnit0PacketRbitPackets'
_Q='cesOverWlanUnit0PacketValidPackets'
_P='cesOverWlanUnit0PacketTotalInPackets'
_O='cesOverWlanUnit0PacketJitterMax'
_N='cesOverWlanUnit0PacketJitterMin'
_M='cesOverWlanUnit0PacketJitterCur'
_L='cesOverWlanUnit0PacketRxRestarts'
_K='cesOverWlanUnit0PacketTxRestarts'
_J='cesOverWlanUnit0PacketRxState'
_I='cesOverWlanUnit0PacketTxState'
_H='cesOverWlanUnit0PacketJitterBufferStatusLastChange'
_G='cesOverWlanUnit0PacketJitterBufferStatus'
_F='microseconds'
_E='cesOverWlanUnit0PacketPortNumber'
_D='Integer32'
_C='read-only'
_B='INFINET-EXTCES-UNIT0-PACKET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cesOverWlanUnit0,=mibBuilder.importSymbols('INFINET-EXTCES-MIB','cesOverWlanUnit0')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
cesOverWlanUnit0Packet=ModuleIdentity((1,3,6,1,4,1,3942,2,1,1,3))
if mibBuilder.loadTexts:cesOverWlanUnit0Packet.setRevisions(('2004-08-16 19:10',))
_CesOverWlanUnit0PacketTable_Object=MibTable
cesOverWlanUnit0PacketTable=_CesOverWlanUnit0PacketTable_Object((1,3,6,1,4,1,3942,2,1,1,3,1))
if mibBuilder.loadTexts:cesOverWlanUnit0PacketTable.setStatus(_A)
_CesOverWlanUnit0PacketEntry_Object=MibTableRow
cesOverWlanUnit0PacketEntry=_CesOverWlanUnit0PacketEntry_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1))
cesOverWlanUnit0PacketEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cesOverWlanUnit0PacketEntry.setStatus(_A)
_CesOverWlanUnit0PacketPortNumber_Type=Unsigned32
_CesOverWlanUnit0PacketPortNumber_Object=MibTableColumn
cesOverWlanUnit0PacketPortNumber=_CesOverWlanUnit0PacketPortNumber_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,1),_CesOverWlanUnit0PacketPortNumber_Type())
cesOverWlanUnit0PacketPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketPortNumber.setStatus(_A)
class _CesOverWlanUnit0PacketTxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CesOverWlanUnit0PacketTxState_Type.__name__=_D
_CesOverWlanUnit0PacketTxState_Object=MibTableColumn
cesOverWlanUnit0PacketTxState=_CesOverWlanUnit0PacketTxState_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,2),_CesOverWlanUnit0PacketTxState_Type())
cesOverWlanUnit0PacketTxState.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketTxState.setStatus(_A)
class _CesOverWlanUnit0PacketRxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CesOverWlanUnit0PacketRxState_Type.__name__=_D
_CesOverWlanUnit0PacketRxState_Object=MibTableColumn
cesOverWlanUnit0PacketRxState=_CesOverWlanUnit0PacketRxState_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,3),_CesOverWlanUnit0PacketRxState_Type())
cesOverWlanUnit0PacketRxState.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketRxState.setStatus(_A)
_CesOverWlanUnit0PacketTxRestarts_Type=Counter32
_CesOverWlanUnit0PacketTxRestarts_Object=MibTableColumn
cesOverWlanUnit0PacketTxRestarts=_CesOverWlanUnit0PacketTxRestarts_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,4),_CesOverWlanUnit0PacketTxRestarts_Type())
cesOverWlanUnit0PacketTxRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketTxRestarts.setStatus(_A)
_CesOverWlanUnit0PacketRxRestarts_Type=Counter32
_CesOverWlanUnit0PacketRxRestarts_Object=MibTableColumn
cesOverWlanUnit0PacketRxRestarts=_CesOverWlanUnit0PacketRxRestarts_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,5),_CesOverWlanUnit0PacketRxRestarts_Type())
cesOverWlanUnit0PacketRxRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketRxRestarts.setStatus(_A)
_CesOverWlanUnit0PacketJitterCur_Type=Integer32
_CesOverWlanUnit0PacketJitterCur_Object=MibTableColumn
cesOverWlanUnit0PacketJitterCur=_CesOverWlanUnit0PacketJitterCur_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,6),_CesOverWlanUnit0PacketJitterCur_Type())
cesOverWlanUnit0PacketJitterCur.setMaxAccess('read-write')
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterCur.setStatus(_A)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterCur.setUnits(_F)
_CesOverWlanUnit0PacketJitterMin_Type=Integer32
_CesOverWlanUnit0PacketJitterMin_Object=MibTableColumn
cesOverWlanUnit0PacketJitterMin=_CesOverWlanUnit0PacketJitterMin_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,7),_CesOverWlanUnit0PacketJitterMin_Type())
cesOverWlanUnit0PacketJitterMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterMin.setStatus(_A)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterMin.setUnits(_F)
_CesOverWlanUnit0PacketJitterMax_Type=Integer32
_CesOverWlanUnit0PacketJitterMax_Object=MibTableColumn
cesOverWlanUnit0PacketJitterMax=_CesOverWlanUnit0PacketJitterMax_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,8),_CesOverWlanUnit0PacketJitterMax_Type())
cesOverWlanUnit0PacketJitterMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterMax.setStatus(_A)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterMax.setUnits(_F)
_CesOverWlanUnit0PacketTotalInPackets_Type=Counter32
_CesOverWlanUnit0PacketTotalInPackets_Object=MibTableColumn
cesOverWlanUnit0PacketTotalInPackets=_CesOverWlanUnit0PacketTotalInPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,9),_CesOverWlanUnit0PacketTotalInPackets_Type())
cesOverWlanUnit0PacketTotalInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketTotalInPackets.setStatus(_A)
_CesOverWlanUnit0PacketValidPackets_Type=Counter32
_CesOverWlanUnit0PacketValidPackets_Object=MibTableColumn
cesOverWlanUnit0PacketValidPackets=_CesOverWlanUnit0PacketValidPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,10),_CesOverWlanUnit0PacketValidPackets_Type())
cesOverWlanUnit0PacketValidPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketValidPackets.setStatus(_A)
_CesOverWlanUnit0PacketRbitPackets_Type=Counter32
_CesOverWlanUnit0PacketRbitPackets_Object=MibTableColumn
cesOverWlanUnit0PacketRbitPackets=_CesOverWlanUnit0PacketRbitPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,11),_CesOverWlanUnit0PacketRbitPackets_Type())
cesOverWlanUnit0PacketRbitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketRbitPackets.setStatus(_A)
_CesOverWlanUnit0PacketLbitPackets_Type=Counter32
_CesOverWlanUnit0PacketLbitPackets_Object=MibTableColumn
cesOverWlanUnit0PacketLbitPackets=_CesOverWlanUnit0PacketLbitPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,12),_CesOverWlanUnit0PacketLbitPackets_Type())
cesOverWlanUnit0PacketLbitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketLbitPackets.setStatus(_A)
_CesOverWlanUnit0PacketLatePackets_Type=Counter32
_CesOverWlanUnit0PacketLatePackets_Object=MibTableColumn
cesOverWlanUnit0PacketLatePackets=_CesOverWlanUnit0PacketLatePackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,13),_CesOverWlanUnit0PacketLatePackets_Type())
cesOverWlanUnit0PacketLatePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketLatePackets.setStatus(_A)
_CesOverWlanUnit0PacketLostPackets_Type=Counter32
_CesOverWlanUnit0PacketLostPackets_Object=MibTableColumn
cesOverWlanUnit0PacketLostPackets=_CesOverWlanUnit0PacketLostPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,14),_CesOverWlanUnit0PacketLostPackets_Type())
cesOverWlanUnit0PacketLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketLostPackets.setStatus(_A)
_CesOverWlanUnit0PacketOutOfOrderPackets_Type=Counter32
_CesOverWlanUnit0PacketOutOfOrderPackets_Object=MibTableColumn
cesOverWlanUnit0PacketOutOfOrderPackets=_CesOverWlanUnit0PacketOutOfOrderPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,15),_CesOverWlanUnit0PacketOutOfOrderPackets_Type())
cesOverWlanUnit0PacketOutOfOrderPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketOutOfOrderPackets.setStatus(_A)
_CesOverWlanUnit0PacketUnderrunPackets_Type=Counter32
_CesOverWlanUnit0PacketUnderrunPackets_Object=MibTableColumn
cesOverWlanUnit0PacketUnderrunPackets=_CesOverWlanUnit0PacketUnderrunPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,16),_CesOverWlanUnit0PacketUnderrunPackets_Type())
cesOverWlanUnit0PacketUnderrunPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketUnderrunPackets.setStatus(_A)
_CesOverWlanUnit0PacketOverrunPackets_Type=Counter32
_CesOverWlanUnit0PacketOverrunPackets_Object=MibTableColumn
cesOverWlanUnit0PacketOverrunPackets=_CesOverWlanUnit0PacketOverrunPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,17),_CesOverWlanUnit0PacketOverrunPackets_Type())
cesOverWlanUnit0PacketOverrunPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketOverrunPackets.setStatus(_A)
_CesOverWlanUnit0PacketInvalidSequencePackets_Type=Counter32
_CesOverWlanUnit0PacketInvalidSequencePackets_Object=MibTableColumn
cesOverWlanUnit0PacketInvalidSequencePackets=_CesOverWlanUnit0PacketInvalidSequencePackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,18),_CesOverWlanUnit0PacketInvalidSequencePackets_Type())
cesOverWlanUnit0PacketInvalidSequencePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketInvalidSequencePackets.setStatus(_A)
_CesOverWlanUnit0PacketDuplicatePackets_Type=Counter32
_CesOverWlanUnit0PacketDuplicatePackets_Object=MibTableColumn
cesOverWlanUnit0PacketDuplicatePackets=_CesOverWlanUnit0PacketDuplicatePackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,19),_CesOverWlanUnit0PacketDuplicatePackets_Type())
cesOverWlanUnit0PacketDuplicatePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketDuplicatePackets.setStatus(_A)
_CesOverWlanUnit0PacketMalformedPackets_Type=Counter32
_CesOverWlanUnit0PacketMalformedPackets_Object=MibTableColumn
cesOverWlanUnit0PacketMalformedPackets=_CesOverWlanUnit0PacketMalformedPackets_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,20),_CesOverWlanUnit0PacketMalformedPackets_Type())
cesOverWlanUnit0PacketMalformedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketMalformedPackets.setStatus(_A)
class _CesOverWlanUnit0PacketJitterBufferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('undeflow',1),('overflow',2),('normal',3)))
_CesOverWlanUnit0PacketJitterBufferStatus_Type.__name__=_D
_CesOverWlanUnit0PacketJitterBufferStatus_Object=MibTableColumn
cesOverWlanUnit0PacketJitterBufferStatus=_CesOverWlanUnit0PacketJitterBufferStatus_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,21),_CesOverWlanUnit0PacketJitterBufferStatus_Type())
cesOverWlanUnit0PacketJitterBufferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterBufferStatus.setStatus(_A)
_CesOverWlanUnit0PacketJitterBufferStatusLastChange_Type=TimeStamp
_CesOverWlanUnit0PacketJitterBufferStatusLastChange_Object=MibTableColumn
cesOverWlanUnit0PacketJitterBufferStatusLastChange=_CesOverWlanUnit0PacketJitterBufferStatusLastChange_Object((1,3,6,1,4,1,3942,2,1,1,3,1,1,22),_CesOverWlanUnit0PacketJitterBufferStatusLastChange_Type())
cesOverWlanUnit0PacketJitterBufferStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterBufferStatusLastChange.setStatus(_A)
_CesOverWlanUnit0PacketTrapsPrefix_ObjectIdentity=ObjectIdentity
cesOverWlanUnit0PacketTrapsPrefix=_CesOverWlanUnit0PacketTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,3942,2,1,1,3,2))
_CesOverWlanUnit0PacketTraps_ObjectIdentity=ObjectIdentity
cesOverWlanUnit0PacketTraps=_CesOverWlanUnit0PacketTraps_ObjectIdentity((1,3,6,1,4,1,3942,2,1,1,3,2,0))
_CesOverWlanUnit0PacketMIBConformance_ObjectIdentity=ObjectIdentity
cesOverWlanUnit0PacketMIBConformance=_CesOverWlanUnit0PacketMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,2,1,1,3,4))
cesOverWlanUnit0PacketGroup=ObjectGroup((1,3,6,1,4,1,3942,2,1,1,3,4,2))
cesOverWlanUnit0PacketGroup.setObjects(*((_B,_E),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cesOverWlanUnit0PacketGroup.setStatus(_A)
cesOverWlanUnit0PacketJitterStatusChange=NotificationType((1,3,6,1,4,1,3942,2,1,1,3,2,0,1))
cesOverWlanUnit0PacketJitterStatusChange.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cesOverWlanUnit0PacketJitterStatusChange.setStatus(_A)
cesOverWlanUnit0PacketNotifications=NotificationGroup((1,3,6,1,4,1,3942,2,1,1,3,4,1))
cesOverWlanUnit0PacketNotifications.setObjects((_B,_b))
if mibBuilder.loadTexts:cesOverWlanUnit0PacketNotifications.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cesOverWlanUnit0Packet':cesOverWlanUnit0Packet,'cesOverWlanUnit0PacketTable':cesOverWlanUnit0PacketTable,'cesOverWlanUnit0PacketEntry':cesOverWlanUnit0PacketEntry,_E:cesOverWlanUnit0PacketPortNumber,_I:cesOverWlanUnit0PacketTxState,_J:cesOverWlanUnit0PacketRxState,_K:cesOverWlanUnit0PacketTxRestarts,_L:cesOverWlanUnit0PacketRxRestarts,_M:cesOverWlanUnit0PacketJitterCur,_N:cesOverWlanUnit0PacketJitterMin,_O:cesOverWlanUnit0PacketJitterMax,_P:cesOverWlanUnit0PacketTotalInPackets,_Q:cesOverWlanUnit0PacketValidPackets,_R:cesOverWlanUnit0PacketRbitPackets,_S:cesOverWlanUnit0PacketLbitPackets,_T:cesOverWlanUnit0PacketLatePackets,_U:cesOverWlanUnit0PacketLostPackets,_V:cesOverWlanUnit0PacketOutOfOrderPackets,_W:cesOverWlanUnit0PacketUnderrunPackets,_X:cesOverWlanUnit0PacketOverrunPackets,_Y:cesOverWlanUnit0PacketInvalidSequencePackets,_Z:cesOverWlanUnit0PacketDuplicatePackets,_a:cesOverWlanUnit0PacketMalformedPackets,_G:cesOverWlanUnit0PacketJitterBufferStatus,_H:cesOverWlanUnit0PacketJitterBufferStatusLastChange,'cesOverWlanUnit0PacketTrapsPrefix':cesOverWlanUnit0PacketTrapsPrefix,'cesOverWlanUnit0PacketTraps':cesOverWlanUnit0PacketTraps,_b:cesOverWlanUnit0PacketJitterStatusChange,'cesOverWlanUnit0PacketMIBConformance':cesOverWlanUnit0PacketMIBConformance,'cesOverWlanUnit0PacketNotifications':cesOverWlanUnit0PacketNotifications,'cesOverWlanUnit0PacketGroup':cesOverWlanUnit0PacketGroup})