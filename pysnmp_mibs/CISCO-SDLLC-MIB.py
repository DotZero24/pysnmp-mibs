_W='convSdllcAddrGroup'
_V='convSdllcPortGroup'
_U='convSdllcAddrMaxSdlcFrameSize'
_T='convSdllcAddrXID'
_S='convSdllcAddrPartnerMacAddr'
_R='convSdllcPortMaxLlc2FrameSize'
_Q='convSdllcPortLocalAckState'
_P='convSdllcPortLocalAck'
_O='convSdllcPortLlc2Ring'
_N='convSdllcPortBridge'
_M='convSdllcPortVirtRing'
_L='convSdllcPortVirtMacAddr'
_K='convSdllcAddrSdlcAddr'
_J='connected'
_I='disconnected'
_H='OctetString'
_G='convSdllcAddrState'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-SDLLC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ciscoSnaSdllcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,28))
if mibBuilder.loadTexts:ciscoSnaSdllcMIB.setRevisions(('1995-08-21 00:00','1998-12-17 00:00'))
_ConvSdllcObjects_ObjectIdentity=ObjectIdentity
convSdllcObjects=_ConvSdllcObjects_ObjectIdentity((1,3,6,1,4,1,9,9,28,1))
_ConvSdllcPorts_ObjectIdentity=ObjectIdentity
convSdllcPorts=_ConvSdllcPorts_ObjectIdentity((1,3,6,1,4,1,9,9,28,1,1))
_ConvSdllcPortTable_Object=MibTable
convSdllcPortTable=_ConvSdllcPortTable_Object((1,3,6,1,4,1,9,9,28,1,1,1))
if mibBuilder.loadTexts:convSdllcPortTable.setStatus(_A)
_ConvSdllcPortEntry_Object=MibTableRow
convSdllcPortEntry=_ConvSdllcPortEntry_Object((1,3,6,1,4,1,9,9,28,1,1,1,1))
convSdllcPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:convSdllcPortEntry.setStatus(_A)
_ConvSdllcPortVirtMacAddr_Type=MacAddress
_ConvSdllcPortVirtMacAddr_Object=MibTableColumn
convSdllcPortVirtMacAddr=_ConvSdllcPortVirtMacAddr_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,1),_ConvSdllcPortVirtMacAddr_Type())
convSdllcPortVirtMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortVirtMacAddr.setStatus(_A)
_ConvSdllcPortVirtRing_Type=Integer32
_ConvSdllcPortVirtRing_Object=MibTableColumn
convSdllcPortVirtRing=_ConvSdllcPortVirtRing_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,2),_ConvSdllcPortVirtRing_Type())
convSdllcPortVirtRing.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortVirtRing.setStatus(_A)
_ConvSdllcPortBridge_Type=Integer32
_ConvSdllcPortBridge_Object=MibTableColumn
convSdllcPortBridge=_ConvSdllcPortBridge_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,3),_ConvSdllcPortBridge_Type())
convSdllcPortBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortBridge.setStatus(_A)
_ConvSdllcPortLlc2Ring_Type=Integer32
_ConvSdllcPortLlc2Ring_Object=MibTableColumn
convSdllcPortLlc2Ring=_ConvSdllcPortLlc2Ring_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,4),_ConvSdllcPortLlc2Ring_Type())
convSdllcPortLlc2Ring.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortLlc2Ring.setStatus(_A)
_ConvSdllcPortLocalAck_Type=TruthValue
_ConvSdllcPortLocalAck_Object=MibTableColumn
convSdllcPortLocalAck=_ConvSdllcPortLocalAck_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,5),_ConvSdllcPortLocalAck_Type())
convSdllcPortLocalAck.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortLocalAck.setStatus(_A)
class _ConvSdllcPortLocalAckState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,255)));namedValues=NamedValues(*((_I,1),('localDiscWait',2),('remDiscWait',3),('remWait',4),('localWait',5),('connectPending',6),(_J,7),('remQOnWait',8),('remQOffWait',9),('quenched',10),('unknown',255)))
_ConvSdllcPortLocalAckState_Type.__name__=_D
_ConvSdllcPortLocalAckState_Object=MibTableColumn
convSdllcPortLocalAckState=_ConvSdllcPortLocalAckState_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,6),_ConvSdllcPortLocalAckState_Type())
convSdllcPortLocalAckState.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortLocalAckState.setStatus(_A)
_ConvSdllcPortMaxLlc2FrameSize_Type=Integer32
_ConvSdllcPortMaxLlc2FrameSize_Object=MibTableColumn
convSdllcPortMaxLlc2FrameSize=_ConvSdllcPortMaxLlc2FrameSize_Object((1,3,6,1,4,1,9,9,28,1,1,1,1,7),_ConvSdllcPortMaxLlc2FrameSize_Type())
convSdllcPortMaxLlc2FrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcPortMaxLlc2FrameSize.setStatus(_A)
_ConvSdllcAddrs_ObjectIdentity=ObjectIdentity
convSdllcAddrs=_ConvSdllcAddrs_ObjectIdentity((1,3,6,1,4,1,9,9,28,1,2))
_ConvSdllcAddrTable_Object=MibTable
convSdllcAddrTable=_ConvSdllcAddrTable_Object((1,3,6,1,4,1,9,9,28,1,2,1))
if mibBuilder.loadTexts:convSdllcAddrTable.setStatus(_A)
_ConvSdllcAddrEntry_Object=MibTableRow
convSdllcAddrEntry=_ConvSdllcAddrEntry_Object((1,3,6,1,4,1,9,9,28,1,2,1,1))
convSdllcAddrEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:convSdllcAddrEntry.setStatus(_A)
class _ConvSdllcAddrSdlcAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConvSdllcAddrSdlcAddr_Type.__name__=_D
_ConvSdllcAddrSdlcAddr_Object=MibTableColumn
convSdllcAddrSdlcAddr=_ConvSdllcAddrSdlcAddr_Object((1,3,6,1,4,1,9,9,28,1,2,1,1,1),_ConvSdllcAddrSdlcAddr_Type())
convSdllcAddrSdlcAddr.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:convSdllcAddrSdlcAddr.setStatus(_A)
_ConvSdllcAddrPartnerMacAddr_Type=MacAddress
_ConvSdllcAddrPartnerMacAddr_Object=MibTableColumn
convSdllcAddrPartnerMacAddr=_ConvSdllcAddrPartnerMacAddr_Object((1,3,6,1,4,1,9,9,28,1,2,1,1,2),_ConvSdllcAddrPartnerMacAddr_Type())
convSdllcAddrPartnerMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcAddrPartnerMacAddr.setStatus(_A)
class _ConvSdllcAddrXID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ConvSdllcAddrXID_Type.__name__=_H
_ConvSdllcAddrXID_Object=MibTableColumn
convSdllcAddrXID=_ConvSdllcAddrXID_Object((1,3,6,1,4,1,9,9,28,1,2,1,1,3),_ConvSdllcAddrXID_Type())
convSdllcAddrXID.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcAddrXID.setStatus(_A)
class _ConvSdllcAddrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),('sdlcDisconnecting',2),('sdlcPriConnecting',3),('netDisconnecting',4),('netConnecting',5),('sdlcSecConnecting',6),(_J,7)))
_ConvSdllcAddrState_Type.__name__=_D
_ConvSdllcAddrState_Object=MibTableColumn
convSdllcAddrState=_ConvSdllcAddrState_Object((1,3,6,1,4,1,9,9,28,1,2,1,1,4),_ConvSdllcAddrState_Type())
convSdllcAddrState.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcAddrState.setStatus(_A)
_ConvSdllcAddrMaxSdlcFrameSize_Type=Integer32
_ConvSdllcAddrMaxSdlcFrameSize_Object=MibTableColumn
convSdllcAddrMaxSdlcFrameSize=_ConvSdllcAddrMaxSdlcFrameSize_Object((1,3,6,1,4,1,9,9,28,1,2,1,1,5),_ConvSdllcAddrMaxSdlcFrameSize_Type())
convSdllcAddrMaxSdlcFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:convSdllcAddrMaxSdlcFrameSize.setStatus(_A)
_ConvSdllcNotificationPrefix_ObjectIdentity=ObjectIdentity
convSdllcNotificationPrefix=_ConvSdllcNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,28,2))
_ConvSdllcNotifications_ObjectIdentity=ObjectIdentity
convSdllcNotifications=_ConvSdllcNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,28,2,0))
_SdllcMibConformance_ObjectIdentity=ObjectIdentity
sdllcMibConformance=_SdllcMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,28,3))
_SdllcMibCompliances_ObjectIdentity=ObjectIdentity
sdllcMibCompliances=_SdllcMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,28,3,1))
_SdllcMibGroups_ObjectIdentity=ObjectIdentity
sdllcMibGroups=_SdllcMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,28,3,2))
convSdllcPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,28,3,2,1))
convSdllcPortGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:convSdllcPortGroup.setStatus(_A)
convSdllcAddrGroup=ObjectGroup((1,3,6,1,4,1,9,9,28,3,2,2))
convSdllcAddrGroup.setObjects(*((_B,_S),(_B,_T),(_B,_G),(_B,_U)))
if mibBuilder.loadTexts:convSdllcAddrGroup.setStatus(_A)
convSdllcPeerStateChangeNotification=NotificationType((1,3,6,1,4,1,9,9,28,2,0,1))
convSdllcPeerStateChangeNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:convSdllcPeerStateChangeNotification.setStatus(_A)
sdllcMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,28,3,1,1))
sdllcMibCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:sdllcMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSnaSdllcMIB':ciscoSnaSdllcMIB,'convSdllcObjects':convSdllcObjects,'convSdllcPorts':convSdllcPorts,'convSdllcPortTable':convSdllcPortTable,'convSdllcPortEntry':convSdllcPortEntry,_L:convSdllcPortVirtMacAddr,_M:convSdllcPortVirtRing,_N:convSdllcPortBridge,_O:convSdllcPortLlc2Ring,_P:convSdllcPortLocalAck,_Q:convSdllcPortLocalAckState,_R:convSdllcPortMaxLlc2FrameSize,'convSdllcAddrs':convSdllcAddrs,'convSdllcAddrTable':convSdllcAddrTable,'convSdllcAddrEntry':convSdllcAddrEntry,_K:convSdllcAddrSdlcAddr,_S:convSdllcAddrPartnerMacAddr,_T:convSdllcAddrXID,_G:convSdllcAddrState,_U:convSdllcAddrMaxSdlcFrameSize,'convSdllcNotificationPrefix':convSdllcNotificationPrefix,'convSdllcNotifications':convSdllcNotifications,'convSdllcPeerStateChangeNotification':convSdllcPeerStateChangeNotification,'sdllcMibConformance':sdllcMibConformance,'sdllcMibCompliances':sdllcMibCompliances,'sdllcMibCompliance':sdllcMibCompliance,'sdllcMibGroups':sdllcMibGroups,_V:convSdllcPortGroup,_W:convSdllcAddrGroup})