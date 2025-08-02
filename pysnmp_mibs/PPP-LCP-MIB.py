_J='ffffffff'
_I='disabled'
_H='enabled'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ppp_ObjectIdentity=ObjectIdentity
ppp=_Ppp_ObjectIdentity((1,3,6,1,2,1,10,23))
_PppLcp_ObjectIdentity=ObjectIdentity
pppLcp=_PppLcp_ObjectIdentity((1,3,6,1,2,1,10,23,1))
_PppLink_ObjectIdentity=ObjectIdentity
pppLink=_PppLink_ObjectIdentity((1,3,6,1,2,1,10,23,1,1))
_PppLinkStatusTable_Object=MibTable
pppLinkStatusTable=_PppLinkStatusTable_Object((1,3,6,1,2,1,10,23,1,1,1))
if mibBuilder.loadTexts:pppLinkStatusTable.setStatus(_A)
_PppLinkStatusEntry_Object=MibTableRow
pppLinkStatusEntry=_PppLinkStatusEntry_Object((1,3,6,1,2,1,10,23,1,1,1,1))
pppLinkStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pppLinkStatusEntry.setStatus(_A)
class _PppLinkStatusPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppLinkStatusPhysicalIndex_Type.__name__=_C
_PppLinkStatusPhysicalIndex_Object=MibTableColumn
pppLinkStatusPhysicalIndex=_PppLinkStatusPhysicalIndex_Object((1,3,6,1,2,1,10,23,1,1,1,1,1),_PppLinkStatusPhysicalIndex_Type())
pppLinkStatusPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusPhysicalIndex.setStatus(_A)
_PppLinkStatusBadAddresses_Type=Counter32
_PppLinkStatusBadAddresses_Object=MibTableColumn
pppLinkStatusBadAddresses=_PppLinkStatusBadAddresses_Object((1,3,6,1,2,1,10,23,1,1,1,1,2),_PppLinkStatusBadAddresses_Type())
pppLinkStatusBadAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusBadAddresses.setStatus(_A)
_PppLinkStatusBadControls_Type=Counter32
_PppLinkStatusBadControls_Object=MibTableColumn
pppLinkStatusBadControls=_PppLinkStatusBadControls_Object((1,3,6,1,2,1,10,23,1,1,1,1,3),_PppLinkStatusBadControls_Type())
pppLinkStatusBadControls.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusBadControls.setStatus(_A)
_PppLinkStatusPacketTooLongs_Type=Counter32
_PppLinkStatusPacketTooLongs_Object=MibTableColumn
pppLinkStatusPacketTooLongs=_PppLinkStatusPacketTooLongs_Object((1,3,6,1,2,1,10,23,1,1,1,1,4),_PppLinkStatusPacketTooLongs_Type())
pppLinkStatusPacketTooLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusPacketTooLongs.setStatus(_A)
_PppLinkStatusBadFCSs_Type=Counter32
_PppLinkStatusBadFCSs_Object=MibTableColumn
pppLinkStatusBadFCSs=_PppLinkStatusBadFCSs_Object((1,3,6,1,2,1,10,23,1,1,1,1,5),_PppLinkStatusBadFCSs_Type())
pppLinkStatusBadFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusBadFCSs.setStatus(_A)
class _PppLinkStatusLocalMRU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PppLinkStatusLocalMRU_Type.__name__=_C
_PppLinkStatusLocalMRU_Object=MibTableColumn
pppLinkStatusLocalMRU=_PppLinkStatusLocalMRU_Object((1,3,6,1,2,1,10,23,1,1,1,1,6),_PppLinkStatusLocalMRU_Type())
pppLinkStatusLocalMRU.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusLocalMRU.setStatus(_A)
class _PppLinkStatusRemoteMRU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PppLinkStatusRemoteMRU_Type.__name__=_C
_PppLinkStatusRemoteMRU_Object=MibTableColumn
pppLinkStatusRemoteMRU=_PppLinkStatusRemoteMRU_Object((1,3,6,1,2,1,10,23,1,1,1,1,7),_PppLinkStatusRemoteMRU_Type())
pppLinkStatusRemoteMRU.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusRemoteMRU.setStatus(_A)
class _PppLinkStatusLocalToPeerACCMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PppLinkStatusLocalToPeerACCMap_Type.__name__=_E
_PppLinkStatusLocalToPeerACCMap_Object=MibTableColumn
pppLinkStatusLocalToPeerACCMap=_PppLinkStatusLocalToPeerACCMap_Object((1,3,6,1,2,1,10,23,1,1,1,1,8),_PppLinkStatusLocalToPeerACCMap_Type())
pppLinkStatusLocalToPeerACCMap.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusLocalToPeerACCMap.setStatus(_A)
class _PppLinkStatusPeerToLocalACCMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PppLinkStatusPeerToLocalACCMap_Type.__name__=_E
_PppLinkStatusPeerToLocalACCMap_Object=MibTableColumn
pppLinkStatusPeerToLocalACCMap=_PppLinkStatusPeerToLocalACCMap_Object((1,3,6,1,2,1,10,23,1,1,1,1,9),_PppLinkStatusPeerToLocalACCMap_Type())
pppLinkStatusPeerToLocalACCMap.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusPeerToLocalACCMap.setStatus(_A)
class _PppLinkStatusLocalToRemoteProtocolCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PppLinkStatusLocalToRemoteProtocolCompression_Type.__name__=_C
_PppLinkStatusLocalToRemoteProtocolCompression_Object=MibTableColumn
pppLinkStatusLocalToRemoteProtocolCompression=_PppLinkStatusLocalToRemoteProtocolCompression_Object((1,3,6,1,2,1,10,23,1,1,1,1,10),_PppLinkStatusLocalToRemoteProtocolCompression_Type())
pppLinkStatusLocalToRemoteProtocolCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusLocalToRemoteProtocolCompression.setStatus(_A)
class _PppLinkStatusRemoteToLocalProtocolCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PppLinkStatusRemoteToLocalProtocolCompression_Type.__name__=_C
_PppLinkStatusRemoteToLocalProtocolCompression_Object=MibTableColumn
pppLinkStatusRemoteToLocalProtocolCompression=_PppLinkStatusRemoteToLocalProtocolCompression_Object((1,3,6,1,2,1,10,23,1,1,1,1,11),_PppLinkStatusRemoteToLocalProtocolCompression_Type())
pppLinkStatusRemoteToLocalProtocolCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusRemoteToLocalProtocolCompression.setStatus(_A)
class _PppLinkStatusLocalToRemoteACCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PppLinkStatusLocalToRemoteACCompression_Type.__name__=_C
_PppLinkStatusLocalToRemoteACCompression_Object=MibTableColumn
pppLinkStatusLocalToRemoteACCompression=_PppLinkStatusLocalToRemoteACCompression_Object((1,3,6,1,2,1,10,23,1,1,1,1,12),_PppLinkStatusLocalToRemoteACCompression_Type())
pppLinkStatusLocalToRemoteACCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusLocalToRemoteACCompression.setStatus(_A)
class _PppLinkStatusRemoteToLocalACCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PppLinkStatusRemoteToLocalACCompression_Type.__name__=_C
_PppLinkStatusRemoteToLocalACCompression_Object=MibTableColumn
pppLinkStatusRemoteToLocalACCompression=_PppLinkStatusRemoteToLocalACCompression_Object((1,3,6,1,2,1,10,23,1,1,1,1,13),_PppLinkStatusRemoteToLocalACCompression_Type())
pppLinkStatusRemoteToLocalACCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusRemoteToLocalACCompression.setStatus(_A)
class _PppLinkStatusTransmitFcsSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PppLinkStatusTransmitFcsSize_Type.__name__=_C
_PppLinkStatusTransmitFcsSize_Object=MibTableColumn
pppLinkStatusTransmitFcsSize=_PppLinkStatusTransmitFcsSize_Object((1,3,6,1,2,1,10,23,1,1,1,1,14),_PppLinkStatusTransmitFcsSize_Type())
pppLinkStatusTransmitFcsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusTransmitFcsSize.setStatus(_A)
class _PppLinkStatusReceiveFcsSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PppLinkStatusReceiveFcsSize_Type.__name__=_C
_PppLinkStatusReceiveFcsSize_Object=MibTableColumn
pppLinkStatusReceiveFcsSize=_PppLinkStatusReceiveFcsSize_Object((1,3,6,1,2,1,10,23,1,1,1,1,15),_PppLinkStatusReceiveFcsSize_Type())
pppLinkStatusReceiveFcsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusReceiveFcsSize.setStatus(_A)
_PppLinkConfigTable_Object=MibTable
pppLinkConfigTable=_PppLinkConfigTable_Object((1,3,6,1,2,1,10,23,1,1,2))
if mibBuilder.loadTexts:pppLinkConfigTable.setStatus(_A)
_PppLinkConfigEntry_Object=MibTableRow
pppLinkConfigEntry=_PppLinkConfigEntry_Object((1,3,6,1,2,1,10,23,1,1,2,1))
pppLinkConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pppLinkConfigEntry.setStatus(_A)
class _PppLinkConfigInitialMRU_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppLinkConfigInitialMRU_Type.__name__=_C
_PppLinkConfigInitialMRU_Object=MibTableColumn
pppLinkConfigInitialMRU=_PppLinkConfigInitialMRU_Object((1,3,6,1,2,1,10,23,1,1,2,1,1),_PppLinkConfigInitialMRU_Type())
pppLinkConfigInitialMRU.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLinkConfigInitialMRU.setStatus(_A)
class _PppLinkConfigReceiveACCMap_Type(OctetString):defaultHexValue=_J;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PppLinkConfigReceiveACCMap_Type.__name__=_E
_PppLinkConfigReceiveACCMap_Object=MibTableColumn
pppLinkConfigReceiveACCMap=_PppLinkConfigReceiveACCMap_Object((1,3,6,1,2,1,10,23,1,1,2,1,2),_PppLinkConfigReceiveACCMap_Type())
pppLinkConfigReceiveACCMap.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLinkConfigReceiveACCMap.setStatus(_A)
class _PppLinkConfigTransmitACCMap_Type(OctetString):defaultHexValue=_J;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PppLinkConfigTransmitACCMap_Type.__name__=_E
_PppLinkConfigTransmitACCMap_Object=MibTableColumn
pppLinkConfigTransmitACCMap=_PppLinkConfigTransmitACCMap_Object((1,3,6,1,2,1,10,23,1,1,2,1,3),_PppLinkConfigTransmitACCMap_Type())
pppLinkConfigTransmitACCMap.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLinkConfigTransmitACCMap.setStatus(_A)
class _PppLinkConfigMagicNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_PppLinkConfigMagicNumber_Type.__name__=_C
_PppLinkConfigMagicNumber_Object=MibTableColumn
pppLinkConfigMagicNumber=_PppLinkConfigMagicNumber_Object((1,3,6,1,2,1,10,23,1,1,2,1,4),_PppLinkConfigMagicNumber_Type())
pppLinkConfigMagicNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLinkConfigMagicNumber.setStatus(_A)
class _PppLinkConfigFcsSize_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PppLinkConfigFcsSize_Type.__name__=_C
_PppLinkConfigFcsSize_Object=MibTableColumn
pppLinkConfigFcsSize=_PppLinkConfigFcsSize_Object((1,3,6,1,2,1,10,23,1,1,2,1,5),_PppLinkConfigFcsSize_Type())
pppLinkConfigFcsSize.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLinkConfigFcsSize.setStatus(_A)
_PppLqr_ObjectIdentity=ObjectIdentity
pppLqr=_PppLqr_ObjectIdentity((1,3,6,1,2,1,10,23,1,2))
_PppLqrTable_Object=MibTable
pppLqrTable=_PppLqrTable_Object((1,3,6,1,2,1,10,23,1,2,1))
if mibBuilder.loadTexts:pppLqrTable.setStatus(_A)
_PppLqrEntry_Object=MibTableRow
pppLqrEntry=_PppLqrEntry_Object((1,3,6,1,2,1,10,23,1,2,1,1))
pppLqrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pppLqrEntry.setStatus(_A)
class _PppLqrQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('good',1),('bad',2),('not-determined',3)))
_PppLqrQuality_Type.__name__=_C
_PppLqrQuality_Object=MibTableColumn
pppLqrQuality=_PppLqrQuality_Object((1,3,6,1,2,1,10,23,1,2,1,1,1),_PppLqrQuality_Type())
pppLqrQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrQuality.setStatus(_A)
_PppLqrInGoodOctets_Type=Counter32
_PppLqrInGoodOctets_Object=MibTableColumn
pppLqrInGoodOctets=_PppLqrInGoodOctets_Object((1,3,6,1,2,1,10,23,1,2,1,1,2),_PppLqrInGoodOctets_Type())
pppLqrInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrInGoodOctets.setStatus(_A)
class _PppLqrLocalPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PppLqrLocalPeriod_Type.__name__=_C
_PppLqrLocalPeriod_Object=MibTableColumn
pppLqrLocalPeriod=_PppLqrLocalPeriod_Object((1,3,6,1,2,1,10,23,1,2,1,1,3),_PppLqrLocalPeriod_Type())
pppLqrLocalPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrLocalPeriod.setStatus(_A)
class _PppLqrRemotePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PppLqrRemotePeriod_Type.__name__=_C
_PppLqrRemotePeriod_Object=MibTableColumn
pppLqrRemotePeriod=_PppLqrRemotePeriod_Object((1,3,6,1,2,1,10,23,1,2,1,1,4),_PppLqrRemotePeriod_Type())
pppLqrRemotePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrRemotePeriod.setStatus(_A)
_PppLqrOutLQRs_Type=Counter32
_PppLqrOutLQRs_Object=MibTableColumn
pppLqrOutLQRs=_PppLqrOutLQRs_Object((1,3,6,1,2,1,10,23,1,2,1,1,5),_PppLqrOutLQRs_Type())
pppLqrOutLQRs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrOutLQRs.setStatus(_A)
_PppLqrInLQRs_Type=Counter32
_PppLqrInLQRs_Object=MibTableColumn
pppLqrInLQRs=_PppLqrInLQRs_Object((1,3,6,1,2,1,10,23,1,2,1,1,6),_PppLqrInLQRs_Type())
pppLqrInLQRs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrInLQRs.setStatus(_A)
_PppLqrConfigTable_Object=MibTable
pppLqrConfigTable=_PppLqrConfigTable_Object((1,3,6,1,2,1,10,23,1,2,2))
if mibBuilder.loadTexts:pppLqrConfigTable.setStatus(_A)
_PppLqrConfigEntry_Object=MibTableRow
pppLqrConfigEntry=_PppLqrConfigEntry_Object((1,3,6,1,2,1,10,23,1,2,2,1))
pppLqrConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pppLqrConfigEntry.setStatus(_A)
class _PppLqrConfigPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppLqrConfigPeriod_Type.__name__=_C
_PppLqrConfigPeriod_Object=MibTableColumn
pppLqrConfigPeriod=_PppLqrConfigPeriod_Object((1,3,6,1,2,1,10,23,1,2,2,1,1),_PppLqrConfigPeriod_Type())
pppLqrConfigPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLqrConfigPeriod.setStatus(_A)
class _PppLqrConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_PppLqrConfigStatus_Type.__name__=_C
_PppLqrConfigStatus_Object=MibTableColumn
pppLqrConfigStatus=_PppLqrConfigStatus_Object((1,3,6,1,2,1,10,23,1,2,2,1,2),_PppLqrConfigStatus_Type())
pppLqrConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pppLqrConfigStatus.setStatus(_A)
_PppLqrExtnsTable_Object=MibTable
pppLqrExtnsTable=_PppLqrExtnsTable_Object((1,3,6,1,2,1,10,23,1,2,3))
if mibBuilder.loadTexts:pppLqrExtnsTable.setStatus(_A)
_PppLqrExtnsEntry_Object=MibTableRow
pppLqrExtnsEntry=_PppLqrExtnsEntry_Object((1,3,6,1,2,1,10,23,1,2,3,1))
pppLqrExtnsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pppLqrExtnsEntry.setStatus(_A)
class _PppLqrExtnsLastReceivedLqrPacket_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(68,68));fixedLength=68
_PppLqrExtnsLastReceivedLqrPacket_Type.__name__=_E
_PppLqrExtnsLastReceivedLqrPacket_Object=MibTableColumn
pppLqrExtnsLastReceivedLqrPacket=_PppLqrExtnsLastReceivedLqrPacket_Object((1,3,6,1,2,1,10,23,1,2,3,1,1),_PppLqrExtnsLastReceivedLqrPacket_Type())
pppLqrExtnsLastReceivedLqrPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLqrExtnsLastReceivedLqrPacket.setStatus(_A)
_PppTests_ObjectIdentity=ObjectIdentity
pppTests=_PppTests_ObjectIdentity((1,3,6,1,2,1,10,23,1,3))
_PppEchoTest_ObjectIdentity=ObjectIdentity
pppEchoTest=_PppEchoTest_ObjectIdentity((1,3,6,1,2,1,10,23,1,3,1))
_PppDiscardTest_ObjectIdentity=ObjectIdentity
pppDiscardTest=_PppDiscardTest_ObjectIdentity((1,3,6,1,2,1,10,23,1,3,2))
mibBuilder.exportSymbols('PPP-LCP-MIB',**{'ppp':ppp,'pppLcp':pppLcp,'pppLink':pppLink,'pppLinkStatusTable':pppLinkStatusTable,'pppLinkStatusEntry':pppLinkStatusEntry,'pppLinkStatusPhysicalIndex':pppLinkStatusPhysicalIndex,'pppLinkStatusBadAddresses':pppLinkStatusBadAddresses,'pppLinkStatusBadControls':pppLinkStatusBadControls,'pppLinkStatusPacketTooLongs':pppLinkStatusPacketTooLongs,'pppLinkStatusBadFCSs':pppLinkStatusBadFCSs,'pppLinkStatusLocalMRU':pppLinkStatusLocalMRU,'pppLinkStatusRemoteMRU':pppLinkStatusRemoteMRU,'pppLinkStatusLocalToPeerACCMap':pppLinkStatusLocalToPeerACCMap,'pppLinkStatusPeerToLocalACCMap':pppLinkStatusPeerToLocalACCMap,'pppLinkStatusLocalToRemoteProtocolCompression':pppLinkStatusLocalToRemoteProtocolCompression,'pppLinkStatusRemoteToLocalProtocolCompression':pppLinkStatusRemoteToLocalProtocolCompression,'pppLinkStatusLocalToRemoteACCompression':pppLinkStatusLocalToRemoteACCompression,'pppLinkStatusRemoteToLocalACCompression':pppLinkStatusRemoteToLocalACCompression,'pppLinkStatusTransmitFcsSize':pppLinkStatusTransmitFcsSize,'pppLinkStatusReceiveFcsSize':pppLinkStatusReceiveFcsSize,'pppLinkConfigTable':pppLinkConfigTable,'pppLinkConfigEntry':pppLinkConfigEntry,'pppLinkConfigInitialMRU':pppLinkConfigInitialMRU,'pppLinkConfigReceiveACCMap':pppLinkConfigReceiveACCMap,'pppLinkConfigTransmitACCMap':pppLinkConfigTransmitACCMap,'pppLinkConfigMagicNumber':pppLinkConfigMagicNumber,'pppLinkConfigFcsSize':pppLinkConfigFcsSize,'pppLqr':pppLqr,'pppLqrTable':pppLqrTable,'pppLqrEntry':pppLqrEntry,'pppLqrQuality':pppLqrQuality,'pppLqrInGoodOctets':pppLqrInGoodOctets,'pppLqrLocalPeriod':pppLqrLocalPeriod,'pppLqrRemotePeriod':pppLqrRemotePeriod,'pppLqrOutLQRs':pppLqrOutLQRs,'pppLqrInLQRs':pppLqrInLQRs,'pppLqrConfigTable':pppLqrConfigTable,'pppLqrConfigEntry':pppLqrConfigEntry,'pppLqrConfigPeriod':pppLqrConfigPeriod,'pppLqrConfigStatus':pppLqrConfigStatus,'pppLqrExtnsTable':pppLqrExtnsTable,'pppLqrExtnsEntry':pppLqrExtnsEntry,'pppLqrExtnsLastReceivedLqrPacket':pppLqrExtnsLastReceivedLqrPacket,'pppTests':pppTests,'pppEchoTest':pppEchoTest,'pppDiscardTest':pppDiscardTest})