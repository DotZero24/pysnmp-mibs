_L='pptpCallType'
_K='established'
_J='pptpCtlConnOriginator'
_I='disabled'
_H='enabled'
_G='pptpProfileId'
_F='delete'
_E='BIANCA-BRICK-PPTP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Vpn_ObjectIdentity=ObjectIdentity
vpn=_Vpn_ObjectIdentity((1,3,6,1,4,1,272,4,23))
_PptpProfileTable_Object=MibTable
pptpProfileTable=_PptpProfileTable_Object((1,3,6,1,4,1,272,4,23,1))
if mibBuilder.loadTexts:pptpProfileTable.setStatus(_A)
_PptpProfileEntry_Object=MibTableRow
pptpProfileEntry=_PptpProfileEntry_Object((1,3,6,1,4,1,272,4,23,1,1))
pptpProfileEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:pptpProfileEntry.setStatus(_A)
class _PptpProfileId_Type(Integer32):defaultValue=0
_PptpProfileId_Type.__name__=_C
_PptpProfileId_Object=MibTableColumn
pptpProfileId=_PptpProfileId_Object((1,3,6,1,4,1,272,4,23,1,1,1),_PptpProfileId_Type())
pptpProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileId.setStatus(_A)
class _PptpProfileKeepalive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),(_F,3)))
_PptpProfileKeepalive_Type.__name__=_C
_PptpProfileKeepalive_Object=MibTableColumn
pptpProfileKeepalive=_PptpProfileKeepalive_Object((1,3,6,1,4,1,272,4,23,1,1,2),_PptpProfileKeepalive_Type())
pptpProfileKeepalive.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileKeepalive.setStatus(_A)
class _PptpProfileMaxRequests_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PptpProfileMaxRequests_Type.__name__=_C
_PptpProfileMaxRequests_Object=MibTableColumn
pptpProfileMaxRequests=_PptpProfileMaxRequests_Object((1,3,6,1,4,1,272,4,23,1,1,3),_PptpProfileMaxRequests_Type())
pptpProfileMaxRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileMaxRequests.setStatus(_A)
class _PptpProfileMaxBlockTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_PptpProfileMaxBlockTime_Type.__name__=_C
_PptpProfileMaxBlockTime_Object=MibTableColumn
pptpProfileMaxBlockTime=_PptpProfileMaxBlockTime_Object((1,3,6,1,4,1,272,4,23,1,1,4),_PptpProfileMaxBlockTime_Type())
pptpProfileMaxBlockTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileMaxBlockTime.setStatus(_A)
class _PptpProfileMaxAckTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,5000))
_PptpProfileMaxAckTimeout_Type.__name__=_C
_PptpProfileMaxAckTimeout_Object=MibTableColumn
pptpProfileMaxAckTimeout=_PptpProfileMaxAckTimeout_Object((1,3,6,1,4,1,272,4,23,1,1,5),_PptpProfileMaxAckTimeout_Type())
pptpProfileMaxAckTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileMaxAckTimeout.setStatus(_A)
class _PptpProfileReassemblyTimeout_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_PptpProfileReassemblyTimeout_Type.__name__=_C
_PptpProfileReassemblyTimeout_Object=MibTableColumn
pptpProfileReassemblyTimeout=_PptpProfileReassemblyTimeout_Object((1,3,6,1,4,1,272,4,23,1,1,6),_PptpProfileReassemblyTimeout_Type())
pptpProfileReassemblyTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileReassemblyTimeout.setStatus(_A)
class _PptpProfileMaxSWin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_PptpProfileMaxSWin_Type.__name__=_C
_PptpProfileMaxSWin_Object=MibTableColumn
pptpProfileMaxSWin=_PptpProfileMaxSWin_Object((1,3,6,1,4,1,272,4,23,1,1,7),_PptpProfileMaxSWin_Type())
pptpProfileMaxSWin.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileMaxSWin.setStatus(_A)
class _PptpProfileXmitWaitTime_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_PptpProfileXmitWaitTime_Type.__name__=_C
_PptpProfileXmitWaitTime_Object=MibTableColumn
pptpProfileXmitWaitTime=_PptpProfileXmitWaitTime_Object((1,3,6,1,4,1,272,4,23,1,1,8),_PptpProfileXmitWaitTime_Type())
pptpProfileXmitWaitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileXmitWaitTime.setStatus(_A)
class _PptpProfileMaxCtlConn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_PptpProfileMaxCtlConn_Type.__name__=_C
_PptpProfileMaxCtlConn_Object=MibTableColumn
pptpProfileMaxCtlConn=_PptpProfileMaxCtlConn_Object((1,3,6,1,4,1,272,4,23,1,1,9),_PptpProfileMaxCtlConn_Type())
pptpProfileMaxCtlConn.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileMaxCtlConn.setStatus(_A)
class _PptpProfileGreWindowAdaption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PptpProfileGreWindowAdaption_Type.__name__=_C
_PptpProfileGreWindowAdaption_Object=MibTableColumn
pptpProfileGreWindowAdaption=_PptpProfileGreWindowAdaption_Object((1,3,6,1,4,1,272,4,23,1,1,10),_PptpProfileGreWindowAdaption_Type())
pptpProfileGreWindowAdaption.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileGreWindowAdaption.setStatus(_A)
_PptpProfileHost_Type=DisplayString
_PptpProfileHost_Object=MibTableColumn
pptpProfileHost=_PptpProfileHost_Object((1,3,6,1,4,1,272,4,23,1,1,11),_PptpProfileHost_Type())
pptpProfileHost.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileHost.setStatus(_A)
_PptpProfileVendor_Type=DisplayString
_PptpProfileVendor_Object=MibTableColumn
pptpProfileVendor=_PptpProfileVendor_Object((1,3,6,1,4,1,272,4,23,1,1,12),_PptpProfileVendor_Type())
pptpProfileVendor.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileVendor.setStatus(_A)
class _PptpProfileFirmRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,999))
_PptpProfileFirmRev_Type.__name__=_C
_PptpProfileFirmRev_Object=MibTableColumn
pptpProfileFirmRev=_PptpProfileFirmRev_Object((1,3,6,1,4,1,272,4,23,1,1,13),_PptpProfileFirmRev_Type())
pptpProfileFirmRev.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpProfileFirmRev.setStatus(_A)
_PptpCtlConnTable_Object=MibTable
pptpCtlConnTable=_PptpCtlConnTable_Object((1,3,6,1,4,1,272,4,23,2))
if mibBuilder.loadTexts:pptpCtlConnTable.setStatus(_A)
_PptpCtlConnEntry_Object=MibTableRow
pptpCtlConnEntry=_PptpCtlConnEntry_Object((1,3,6,1,4,1,272,4,23,2,1))
pptpCtlConnEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:pptpCtlConnEntry.setStatus(_A)
class _PptpCtlConnOriginator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_PptpCtlConnOriginator_Type.__name__=_C
_PptpCtlConnOriginator_Object=MibTableColumn
pptpCtlConnOriginator=_PptpCtlConnOriginator_Object((1,3,6,1,4,1,272,4,23,2,1,1),_PptpCtlConnOriginator_Type())
pptpCtlConnOriginator.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnOriginator.setStatus(_A)
_PptpCtlConnAge_Type=TimeTicks
_PptpCtlConnAge_Object=MibTableColumn
pptpCtlConnAge=_PptpCtlConnAge_Object((1,3,6,1,4,1,272,4,23,2,1,2),_PptpCtlConnAge_Type())
pptpCtlConnAge.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnAge.setStatus(_A)
class _PptpCtlConnState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('wait-ctl-reply',2),(_K,3),('wait-stop-reply',4),('close',5),(_F,6)))
_PptpCtlConnState_Type.__name__=_C
_PptpCtlConnState_Object=MibTableColumn
pptpCtlConnState=_PptpCtlConnState_Object((1,3,6,1,4,1,272,4,23,2,1,3),_PptpCtlConnState_Type())
pptpCtlConnState.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpCtlConnState.setStatus(_A)
_PptpCtlConnRemoteIpAddress_Type=IpAddress
_PptpCtlConnRemoteIpAddress_Object=MibTableColumn
pptpCtlConnRemoteIpAddress=_PptpCtlConnRemoteIpAddress_Object((1,3,6,1,4,1,272,4,23,2,1,4),_PptpCtlConnRemoteIpAddress_Type())
pptpCtlConnRemoteIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnRemoteIpAddress.setStatus(_A)
_PptpCtlConnLocalIpAddress_Type=IpAddress
_PptpCtlConnLocalIpAddress_Object=MibTableColumn
pptpCtlConnLocalIpAddress=_PptpCtlConnLocalIpAddress_Object((1,3,6,1,4,1,272,4,23,2,1,5),_PptpCtlConnLocalIpAddress_Type())
pptpCtlConnLocalIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnLocalIpAddress.setStatus(_A)
_PptpCtlConnVersion_Type=Integer32
_PptpCtlConnVersion_Object=MibTableColumn
pptpCtlConnVersion=_PptpCtlConnVersion_Object((1,3,6,1,4,1,272,4,23,2,1,6),_PptpCtlConnVersion_Type())
pptpCtlConnVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnVersion.setStatus(_A)
_PptpCtlConnHost_Type=DisplayString
_PptpCtlConnHost_Object=MibTableColumn
pptpCtlConnHost=_PptpCtlConnHost_Object((1,3,6,1,4,1,272,4,23,2,1,7),_PptpCtlConnHost_Type())
pptpCtlConnHost.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnHost.setStatus(_A)
_PptpCtlConnVendor_Type=DisplayString
_PptpCtlConnVendor_Object=MibTableColumn
pptpCtlConnVendor=_PptpCtlConnVendor_Object((1,3,6,1,4,1,272,4,23,2,1,8),_PptpCtlConnVendor_Type())
pptpCtlConnVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnVendor.setStatus(_A)
_PptpCtlConnFirmRev_Type=Integer32
_PptpCtlConnFirmRev_Object=MibTableColumn
pptpCtlConnFirmRev=_PptpCtlConnFirmRev_Object((1,3,6,1,4,1,272,4,23,2,1,9),_PptpCtlConnFirmRev_Type())
pptpCtlConnFirmRev.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnFirmRev.setStatus(_A)
_PptpCtlConnMaxChan_Type=Integer32
_PptpCtlConnMaxChan_Object=MibTableColumn
pptpCtlConnMaxChan=_PptpCtlConnMaxChan_Object((1,3,6,1,4,1,272,4,23,2,1,10),_PptpCtlConnMaxChan_Type())
pptpCtlConnMaxChan.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnMaxChan.setStatus(_A)
_PptpCtlConnOutgoingCalls_Type=Integer32
_PptpCtlConnOutgoingCalls_Object=MibTableColumn
pptpCtlConnOutgoingCalls=_PptpCtlConnOutgoingCalls_Object((1,3,6,1,4,1,272,4,23,2,1,11),_PptpCtlConnOutgoingCalls_Type())
pptpCtlConnOutgoingCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnOutgoingCalls.setStatus(_A)
_PptpCtlConnIncomingCalls_Type=Integer32
_PptpCtlConnIncomingCalls_Object=MibTableColumn
pptpCtlConnIncomingCalls=_PptpCtlConnIncomingCalls_Object((1,3,6,1,4,1,272,4,23,2,1,12),_PptpCtlConnIncomingCalls_Type())
pptpCtlConnIncomingCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnIncomingCalls.setStatus(_A)
_PptpCtlConnOutgoingFails_Type=Integer32
_PptpCtlConnOutgoingFails_Object=MibTableColumn
pptpCtlConnOutgoingFails=_PptpCtlConnOutgoingFails_Object((1,3,6,1,4,1,272,4,23,2,1,13),_PptpCtlConnOutgoingFails_Type())
pptpCtlConnOutgoingFails.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnOutgoingFails.setStatus(_A)
_PptpCtlConnIncomingFails_Type=Integer32
_PptpCtlConnIncomingFails_Object=MibTableColumn
pptpCtlConnIncomingFails=_PptpCtlConnIncomingFails_Object((1,3,6,1,4,1,272,4,23,2,1,14),_PptpCtlConnIncomingFails_Type())
pptpCtlConnIncomingFails.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnIncomingFails.setStatus(_A)
_PptpCtlConnEchoReqSent_Type=Integer32
_PptpCtlConnEchoReqSent_Object=MibTableColumn
pptpCtlConnEchoReqSent=_PptpCtlConnEchoReqSent_Object((1,3,6,1,4,1,272,4,23,2,1,15),_PptpCtlConnEchoReqSent_Type())
pptpCtlConnEchoReqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnEchoReqSent.setStatus(_A)
_PptpCtlConnEchoReqRcvd_Type=Integer32
_PptpCtlConnEchoReqRcvd_Object=MibTableColumn
pptpCtlConnEchoReqRcvd=_PptpCtlConnEchoReqRcvd_Object((1,3,6,1,4,1,272,4,23,2,1,16),_PptpCtlConnEchoReqRcvd_Type())
pptpCtlConnEchoReqRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnEchoReqRcvd.setStatus(_A)
_PptpCtlConnEchoRepSent_Type=Integer32
_PptpCtlConnEchoRepSent_Object=MibTableColumn
pptpCtlConnEchoRepSent=_PptpCtlConnEchoRepSent_Object((1,3,6,1,4,1,272,4,23,2,1,17),_PptpCtlConnEchoRepSent_Type())
pptpCtlConnEchoRepSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnEchoRepSent.setStatus(_A)
_PptpCtlConnEchoRepRcvd_Type=Integer32
_PptpCtlConnEchoRepRcvd_Object=MibTableColumn
pptpCtlConnEchoRepRcvd=_PptpCtlConnEchoRepRcvd_Object((1,3,6,1,4,1,272,4,23,2,1,18),_PptpCtlConnEchoRepRcvd_Type())
pptpCtlConnEchoRepRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnEchoRepRcvd.setStatus(_A)
_PptpCtlConnEchoReqPending_Type=Integer32
_PptpCtlConnEchoReqPending_Object=MibTableColumn
pptpCtlConnEchoReqPending=_PptpCtlConnEchoReqPending_Object((1,3,6,1,4,1,272,4,23,2,1,19),_PptpCtlConnEchoReqPending_Type())
pptpCtlConnEchoReqPending.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCtlConnEchoReqPending.setStatus(_A)
_PptpCallTable_Object=MibTable
pptpCallTable=_PptpCallTable_Object((1,3,6,1,4,1,272,4,23,3))
if mibBuilder.loadTexts:pptpCallTable.setStatus(_A)
_PptpCallEntry_Object=MibTableRow
pptpCallEntry=_PptpCallEntry_Object((1,3,6,1,4,1,272,4,23,3,1))
pptpCallEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:pptpCallEntry.setStatus(_A)
class _PptpCallType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pac',1),('pns',2)))
_PptpCallType_Type.__name__=_C
_PptpCallType_Object=MibTableColumn
pptpCallType=_PptpCallType_Object((1,3,6,1,4,1,272,4,23,3,1,1),_PptpCallType_Type())
pptpCallType.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallType.setStatus(_A)
class _PptpCallDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('incoming',1),('outgoing',2)))
_PptpCallDirection_Type.__name__=_C
_PptpCallDirection_Object=MibTableColumn
pptpCallDirection=_PptpCallDirection_Object((1,3,6,1,4,1,272,4,23,3,1,2),_PptpCallDirection_Type())
pptpCallDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallDirection.setStatus(_A)
_PptpCallAge_Type=TimeTicks
_PptpCallAge_Object=MibTableColumn
pptpCallAge=_PptpCallAge_Object((1,3,6,1,4,1,272,4,23,3,1,3),_PptpCallAge_Type())
pptpCallAge.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallAge.setStatus(_A)
class _PptpCallState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('idle',1),('wait-cs-ans',2),('wait-reply',3),('wait-connect',4),(_K,5),('wait-disc',6),('close',7),(_F,8)))
_PptpCallState_Type.__name__=_C
_PptpCallState_Object=MibTableColumn
pptpCallState=_PptpCallState_Object((1,3,6,1,4,1,272,4,23,3,1,4),_PptpCallState_Type())
pptpCallState.setMaxAccess(_D)
if mibBuilder.loadTexts:pptpCallState.setStatus(_A)
_PptpCallRemoteIpAddress_Type=IpAddress
_PptpCallRemoteIpAddress_Object=MibTableColumn
pptpCallRemoteIpAddress=_PptpCallRemoteIpAddress_Object((1,3,6,1,4,1,272,4,23,3,1,5),_PptpCallRemoteIpAddress_Type())
pptpCallRemoteIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallRemoteIpAddress.setStatus(_A)
_PptpCallLocalIpAddress_Type=IpAddress
_PptpCallLocalIpAddress_Object=MibTableColumn
pptpCallLocalIpAddress=_PptpCallLocalIpAddress_Object((1,3,6,1,4,1,272,4,23,3,1,6),_PptpCallLocalIpAddress_Type())
pptpCallLocalIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallLocalIpAddress.setStatus(_A)
_PptpCallReceivedPackets_Type=Counter32
_PptpCallReceivedPackets_Object=MibTableColumn
pptpCallReceivedPackets=_PptpCallReceivedPackets_Object((1,3,6,1,4,1,272,4,23,3,1,7),_PptpCallReceivedPackets_Type())
pptpCallReceivedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallReceivedPackets.setStatus(_A)
_PptpCallReceivedOctets_Type=Counter32
_PptpCallReceivedOctets_Object=MibTableColumn
pptpCallReceivedOctets=_PptpCallReceivedOctets_Object((1,3,6,1,4,1,272,4,23,3,1,8),_PptpCallReceivedOctets_Type())
pptpCallReceivedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallReceivedOctets.setStatus(_A)
_PptpCallReceivedErrors_Type=Counter32
_PptpCallReceivedErrors_Object=MibTableColumn
pptpCallReceivedErrors=_PptpCallReceivedErrors_Object((1,3,6,1,4,1,272,4,23,3,1,9),_PptpCallReceivedErrors_Type())
pptpCallReceivedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallReceivedErrors.setStatus(_A)
_PptpCallTransmitPackets_Type=Counter32
_PptpCallTransmitPackets_Object=MibTableColumn
pptpCallTransmitPackets=_PptpCallTransmitPackets_Object((1,3,6,1,4,1,272,4,23,3,1,10),_PptpCallTransmitPackets_Type())
pptpCallTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallTransmitPackets.setStatus(_A)
_PptpCallTransmitOctets_Type=Counter32
_PptpCallTransmitOctets_Object=MibTableColumn
pptpCallTransmitOctets=_PptpCallTransmitOctets_Object((1,3,6,1,4,1,272,4,23,3,1,11),_PptpCallTransmitOctets_Type())
pptpCallTransmitOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallTransmitOctets.setStatus(_A)
_PptpCallTransmitErrors_Type=Counter32
_PptpCallTransmitErrors_Object=MibTableColumn
pptpCallTransmitErrors=_PptpCallTransmitErrors_Object((1,3,6,1,4,1,272,4,23,3,1,12),_PptpCallTransmitErrors_Type())
pptpCallTransmitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallTransmitErrors.setStatus(_A)
_PptpCallInfo_Type=DisplayString
_PptpCallInfo_Object=MibTableColumn
pptpCallInfo=_PptpCallInfo_Object((1,3,6,1,4,1,272,4,23,3,1,13),_PptpCallInfo_Type())
pptpCallInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallInfo.setStatus(_A)
_PptpCallLocId_Type=Integer32
_PptpCallLocId_Object=MibTableColumn
pptpCallLocId=_PptpCallLocId_Object((1,3,6,1,4,1,272,4,23,3,1,14),_PptpCallLocId_Type())
pptpCallLocId.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallLocId.setStatus(_A)
_PptpCallRemId_Type=Integer32
_PptpCallRemId_Object=MibTableColumn
pptpCallRemId=_PptpCallRemId_Object((1,3,6,1,4,1,272,4,23,3,1,15),_PptpCallRemId_Type())
pptpCallRemId.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallRemId.setStatus(_A)
_PptpCallSerial_Type=Integer32
_PptpCallSerial_Object=MibTableColumn
pptpCallSerial=_PptpCallSerial_Object((1,3,6,1,4,1,272,4,23,3,1,16),_PptpCallSerial_Type())
pptpCallSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallSerial.setStatus(_A)
class _PptpCallSWin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_PptpCallSWin_Type.__name__=_C
_PptpCallSWin_Object=MibTableColumn
pptpCallSWin=_PptpCallSWin_Object((1,3,6,1,4,1,272,4,23,3,1,17),_PptpCallSWin_Type())
pptpCallSWin.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallSWin.setStatus(_A)
class _PptpCallGreWindowAdaption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PptpCallGreWindowAdaption_Type.__name__=_C
_PptpCallGreWindowAdaption_Object=MibTableColumn
pptpCallGreWindowAdaption=_PptpCallGreWindowAdaption_Object((1,3,6,1,4,1,272,4,23,3,1,18),_PptpCallGreWindowAdaption_Type())
pptpCallGreWindowAdaption.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallGreWindowAdaption.setStatus(_A)
_PptpCallAssociatedIfIndex_Type=Integer32
_PptpCallAssociatedIfIndex_Object=MibTableColumn
pptpCallAssociatedIfIndex=_PptpCallAssociatedIfIndex_Object((1,3,6,1,4,1,272,4,23,3,1,19),_PptpCallAssociatedIfIndex_Type())
pptpCallAssociatedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pptpCallAssociatedIfIndex.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'vpn':vpn,'pptpProfileTable':pptpProfileTable,'pptpProfileEntry':pptpProfileEntry,_G:pptpProfileId,'pptpProfileKeepalive':pptpProfileKeepalive,'pptpProfileMaxRequests':pptpProfileMaxRequests,'pptpProfileMaxBlockTime':pptpProfileMaxBlockTime,'pptpProfileMaxAckTimeout':pptpProfileMaxAckTimeout,'pptpProfileReassemblyTimeout':pptpProfileReassemblyTimeout,'pptpProfileMaxSWin':pptpProfileMaxSWin,'pptpProfileXmitWaitTime':pptpProfileXmitWaitTime,'pptpProfileMaxCtlConn':pptpProfileMaxCtlConn,'pptpProfileGreWindowAdaption':pptpProfileGreWindowAdaption,'pptpProfileHost':pptpProfileHost,'pptpProfileVendor':pptpProfileVendor,'pptpProfileFirmRev':pptpProfileFirmRev,'pptpCtlConnTable':pptpCtlConnTable,'pptpCtlConnEntry':pptpCtlConnEntry,_J:pptpCtlConnOriginator,'pptpCtlConnAge':pptpCtlConnAge,'pptpCtlConnState':pptpCtlConnState,'pptpCtlConnRemoteIpAddress':pptpCtlConnRemoteIpAddress,'pptpCtlConnLocalIpAddress':pptpCtlConnLocalIpAddress,'pptpCtlConnVersion':pptpCtlConnVersion,'pptpCtlConnHost':pptpCtlConnHost,'pptpCtlConnVendor':pptpCtlConnVendor,'pptpCtlConnFirmRev':pptpCtlConnFirmRev,'pptpCtlConnMaxChan':pptpCtlConnMaxChan,'pptpCtlConnOutgoingCalls':pptpCtlConnOutgoingCalls,'pptpCtlConnIncomingCalls':pptpCtlConnIncomingCalls,'pptpCtlConnOutgoingFails':pptpCtlConnOutgoingFails,'pptpCtlConnIncomingFails':pptpCtlConnIncomingFails,'pptpCtlConnEchoReqSent':pptpCtlConnEchoReqSent,'pptpCtlConnEchoReqRcvd':pptpCtlConnEchoReqRcvd,'pptpCtlConnEchoRepSent':pptpCtlConnEchoRepSent,'pptpCtlConnEchoRepRcvd':pptpCtlConnEchoRepRcvd,'pptpCtlConnEchoReqPending':pptpCtlConnEchoReqPending,'pptpCallTable':pptpCallTable,'pptpCallEntry':pptpCallEntry,_L:pptpCallType,'pptpCallDirection':pptpCallDirection,'pptpCallAge':pptpCallAge,'pptpCallState':pptpCallState,'pptpCallRemoteIpAddress':pptpCallRemoteIpAddress,'pptpCallLocalIpAddress':pptpCallLocalIpAddress,'pptpCallReceivedPackets':pptpCallReceivedPackets,'pptpCallReceivedOctets':pptpCallReceivedOctets,'pptpCallReceivedErrors':pptpCallReceivedErrors,'pptpCallTransmitPackets':pptpCallTransmitPackets,'pptpCallTransmitOctets':pptpCallTransmitOctets,'pptpCallTransmitErrors':pptpCallTransmitErrors,'pptpCallInfo':pptpCallInfo,'pptpCallLocId':pptpCallLocId,'pptpCallRemId':pptpCallRemId,'pptpCallSerial':pptpCallSerial,'pptpCallSWin':pptpCallSWin,'pptpCallGreWindowAdaption':pptpCallGreWindowAdaption,'pptpCallAssociatedIfIndex':pptpCallAssociatedIfIndex})