_N='netDeviceEntryIndex'
_M='not-accessible'
_L='fd10000'
_K='fd1000'
_J='linkdown'
_I='fd-10000'
_H='fd-1000'
_G='fd-100'
_F='hd-100'
_E='channelInfoEntryIndex'
_D='PACKETLOGIC-CHANNEL-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
packetlogic2,=mibBuilder.importSymbols('PACKETLOGIC-MIB','packetlogic2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
channelstats=ModuleIdentity((1,3,6,1,4,1,15397,2,2))
if mibBuilder.loadTexts:channelstats.setRevisions(('2012-12-13 13:22',))
_ChannelCfg_ObjectIdentity=ObjectIdentity
channelCfg=_ChannelCfg_ObjectIdentity((1,3,6,1,4,1,15397,2,2,8))
_ChannelNumber_Type=Unsigned32
_ChannelNumber_Object=MibScalar
channelNumber=_ChannelNumber_Object((1,3,6,1,4,1,15397,2,2,8,1),_ChannelNumber_Type())
channelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:channelNumber.setStatus(_A)
_ChannelInfoTable_Object=MibTable
channelInfoTable=_ChannelInfoTable_Object((1,3,6,1,4,1,15397,2,2,17))
if mibBuilder.loadTexts:channelInfoTable.setStatus(_A)
_ChannelInfoEntry_Object=MibTableRow
channelInfoEntry=_ChannelInfoEntry_Object((1,3,6,1,4,1,15397,2,2,17,1))
channelInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:channelInfoEntry.setStatus(_A)
class _ChannelInternalMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',0),('hd-10',1),('fd-10',2),(_F,3),(_G,4),(_H,5),(_I,6)))
_ChannelInternalMedia_Type.__name__=_C
_ChannelInternalMedia_Object=MibTableColumn
channelInternalMedia=_ChannelInternalMedia_Object((1,3,6,1,4,1,15397,2,2,17,1,1),_ChannelInternalMedia_Type())
channelInternalMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalMedia.setStatus(_A)
class _ChannelExternalMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',0),('hd-10',1),('fd-10',2),(_F,3),(_G,4),(_H,5),(_I,6)))
_ChannelExternalMedia_Type.__name__=_C
_ChannelExternalMedia_Object=MibTableColumn
channelExternalMedia=_ChannelExternalMedia_Object((1,3,6,1,4,1,15397,2,2,17,1,2),_ChannelExternalMedia_Type())
channelExternalMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalMedia.setStatus(_A)
class _ChannelInternalNegotiatedMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),('hd10',1),('fd10',2),('hd100',3),('fd100',4),(_K,5),(_L,6)))
_ChannelInternalNegotiatedMedia_Type.__name__=_C
_ChannelInternalNegotiatedMedia_Object=MibTableColumn
channelInternalNegotiatedMedia=_ChannelInternalNegotiatedMedia_Object((1,3,6,1,4,1,15397,2,2,17,1,3),_ChannelInternalNegotiatedMedia_Type())
channelInternalNegotiatedMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalNegotiatedMedia.setStatus(_A)
class _ChannelExternalNegotiatedMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),('hd10',1),('fd10',2),('hd100',3),('fd100',4),(_K,5),(_L,6)))
_ChannelExternalNegotiatedMedia_Type.__name__=_C
_ChannelExternalNegotiatedMedia_Object=MibTableColumn
channelExternalNegotiatedMedia=_ChannelExternalNegotiatedMedia_Object((1,3,6,1,4,1,15397,2,2,17,1,4),_ChannelExternalNegotiatedMedia_Type())
channelExternalNegotiatedMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalNegotiatedMedia.setStatus(_A)
class _ChannelActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_ChannelActive_Type.__name__=_C
_ChannelActive_Object=MibTableColumn
channelActive=_ChannelActive_Object((1,3,6,1,4,1,15397,2,2,17,1,5),_ChannelActive_Type())
channelActive.setMaxAccess(_B)
if mibBuilder.loadTexts:channelActive.setStatus(_A)
_ChannelName_Type=DisplayString
_ChannelName_Object=MibTableColumn
channelName=_ChannelName_Object((1,3,6,1,4,1,15397,2,2,17,1,6),_ChannelName_Type())
channelName.setMaxAccess(_B)
if mibBuilder.loadTexts:channelName.setStatus(_A)
_ChannelInternalNegotiatedMediaTime_Type=Unsigned32
_ChannelInternalNegotiatedMediaTime_Object=MibTableColumn
channelInternalNegotiatedMediaTime=_ChannelInternalNegotiatedMediaTime_Object((1,3,6,1,4,1,15397,2,2,17,1,7),_ChannelInternalNegotiatedMediaTime_Type())
channelInternalNegotiatedMediaTime.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalNegotiatedMediaTime.setStatus(_A)
_ChannelexternalNegotiatedMediaTime_Type=Unsigned32
_ChannelexternalNegotiatedMediaTime_Object=MibTableColumn
channelexternalNegotiatedMediaTime=_ChannelexternalNegotiatedMediaTime_Object((1,3,6,1,4,1,15397,2,2,17,1,8),_ChannelexternalNegotiatedMediaTime_Type())
channelexternalNegotiatedMediaTime.setMaxAccess(_B)
if mibBuilder.loadTexts:channelexternalNegotiatedMediaTime.setStatus(_A)
class _ChannelInfoEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ChannelInfoEntryIndex_Type.__name__=_C
_ChannelInfoEntryIndex_Object=MibTableColumn
channelInfoEntryIndex=_ChannelInfoEntryIndex_Object((1,3,6,1,4,1,15397,2,2,17,1,999),_ChannelInfoEntryIndex_Type())
channelInfoEntryIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:channelInfoEntryIndex.setStatus(_A)
_NetDeviceTable_Object=MibTable
netDeviceTable=_NetDeviceTable_Object((1,3,6,1,4,1,15397,2,2,25))
if mibBuilder.loadTexts:netDeviceTable.setStatus(_A)
_NetDeviceEntry_Object=MibTableRow
netDeviceEntry=_NetDeviceEntry_Object((1,3,6,1,4,1,15397,2,2,25,1))
netDeviceEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:netDeviceEntry.setStatus(_A)
_ChannelRxPackets_ObjectIdentity=ObjectIdentity
channelRxPackets=_ChannelRxPackets_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,1))
_ChannelInternalRxPackets_Type=Counter64
_ChannelInternalRxPackets_Object=MibScalar
channelInternalRxPackets=_ChannelInternalRxPackets_Object((1,3,6,1,4,1,15397,2,2,25,1,1,1),_ChannelInternalRxPackets_Type())
channelInternalRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxPackets.setStatus(_A)
_ChannelExternalRxPackets_Type=Counter64
_ChannelExternalRxPackets_Object=MibScalar
channelExternalRxPackets=_ChannelExternalRxPackets_Object((1,3,6,1,4,1,15397,2,2,25,1,1,2),_ChannelExternalRxPackets_Type())
channelExternalRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxPackets.setStatus(_A)
_ChannelTxPackets_ObjectIdentity=ObjectIdentity
channelTxPackets=_ChannelTxPackets_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,2))
_ChannelInternalTxPackets_Type=Counter64
_ChannelInternalTxPackets_Object=MibScalar
channelInternalTxPackets=_ChannelInternalTxPackets_Object((1,3,6,1,4,1,15397,2,2,25,1,2,1),_ChannelInternalTxPackets_Type())
channelInternalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxPackets.setStatus(_A)
_ChannelExternalTxPackets_Type=Counter64
_ChannelExternalTxPackets_Object=MibScalar
channelExternalTxPackets=_ChannelExternalTxPackets_Object((1,3,6,1,4,1,15397,2,2,25,1,2,2),_ChannelExternalTxPackets_Type())
channelExternalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxPackets.setStatus(_A)
_ChannelRxBytes_ObjectIdentity=ObjectIdentity
channelRxBytes=_ChannelRxBytes_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,3))
_ChannelInternalRxBytes_Type=Counter64
_ChannelInternalRxBytes_Object=MibScalar
channelInternalRxBytes=_ChannelInternalRxBytes_Object((1,3,6,1,4,1,15397,2,2,25,1,3,1),_ChannelInternalRxBytes_Type())
channelInternalRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxBytes.setStatus(_A)
_ChannelExternalRxBytes_Type=Counter64
_ChannelExternalRxBytes_Object=MibScalar
channelExternalRxBytes=_ChannelExternalRxBytes_Object((1,3,6,1,4,1,15397,2,2,25,1,3,2),_ChannelExternalRxBytes_Type())
channelExternalRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxBytes.setStatus(_A)
_ChannelTxBytes_ObjectIdentity=ObjectIdentity
channelTxBytes=_ChannelTxBytes_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,4))
_ChannelInternalTxBytes_Type=Counter64
_ChannelInternalTxBytes_Object=MibScalar
channelInternalTxBytes=_ChannelInternalTxBytes_Object((1,3,6,1,4,1,15397,2,2,25,1,4,1),_ChannelInternalTxBytes_Type())
channelInternalTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxBytes.setStatus(_A)
_ChannelExternalTxBytes_Type=Counter64
_ChannelExternalTxBytes_Object=MibScalar
channelExternalTxBytes=_ChannelExternalTxBytes_Object((1,3,6,1,4,1,15397,2,2,25,1,4,2),_ChannelExternalTxBytes_Type())
channelExternalTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxBytes.setStatus(_A)
_ChannelRxErrors_ObjectIdentity=ObjectIdentity
channelRxErrors=_ChannelRxErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,5))
_ChannelInternalRxErrors_Type=Counter64
_ChannelInternalRxErrors_Object=MibScalar
channelInternalRxErrors=_ChannelInternalRxErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,5,1),_ChannelInternalRxErrors_Type())
channelInternalRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxErrors.setStatus(_A)
_ChannelExternalRxErrors_Type=Counter64
_ChannelExternalRxErrors_Object=MibScalar
channelExternalRxErrors=_ChannelExternalRxErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,5,2),_ChannelExternalRxErrors_Type())
channelExternalRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxErrors.setStatus(_A)
_ChannelTxErrors_ObjectIdentity=ObjectIdentity
channelTxErrors=_ChannelTxErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,6))
_ChannelInternalTxErrors_Type=Counter64
_ChannelInternalTxErrors_Object=MibScalar
channelInternalTxErrors=_ChannelInternalTxErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,6,1),_ChannelInternalTxErrors_Type())
channelInternalTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxErrors.setStatus(_A)
_ChannelExternalTxErrors_Type=Counter64
_ChannelExternalTxErrors_Object=MibScalar
channelExternalTxErrors=_ChannelExternalTxErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,6,2),_ChannelExternalTxErrors_Type())
channelExternalTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxErrors.setStatus(_A)
_ChannelRxDrops_ObjectIdentity=ObjectIdentity
channelRxDrops=_ChannelRxDrops_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,7))
_ChannelInternalRxDrops_Type=Counter64
_ChannelInternalRxDrops_Object=MibScalar
channelInternalRxDrops=_ChannelInternalRxDrops_Object((1,3,6,1,4,1,15397,2,2,25,1,7,1),_ChannelInternalRxDrops_Type())
channelInternalRxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxDrops.setStatus(_A)
_ChannelExternalRxDrops_Type=Counter64
_ChannelExternalRxDrops_Object=MibScalar
channelExternalRxDrops=_ChannelExternalRxDrops_Object((1,3,6,1,4,1,15397,2,2,25,1,7,2),_ChannelExternalRxDrops_Type())
channelExternalRxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxDrops.setStatus(_A)
_ChannelTxDrops_ObjectIdentity=ObjectIdentity
channelTxDrops=_ChannelTxDrops_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,8))
_ChannelInternalTxDrops_Type=Counter64
_ChannelInternalTxDrops_Object=MibScalar
channelInternalTxDrops=_ChannelInternalTxDrops_Object((1,3,6,1,4,1,15397,2,2,25,1,8,1),_ChannelInternalTxDrops_Type())
channelInternalTxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxDrops.setStatus(_A)
_ChannelExternalTxDrops_Type=Counter64
_ChannelExternalTxDrops_Object=MibScalar
channelExternalTxDrops=_ChannelExternalTxDrops_Object((1,3,6,1,4,1,15397,2,2,25,1,8,2),_ChannelExternalTxDrops_Type())
channelExternalTxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxDrops.setStatus(_A)
_ChannelCollisions_ObjectIdentity=ObjectIdentity
channelCollisions=_ChannelCollisions_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,9))
_ChannelInternalCollisions_Type=Counter64
_ChannelInternalCollisions_Object=MibScalar
channelInternalCollisions=_ChannelInternalCollisions_Object((1,3,6,1,4,1,15397,2,2,25,1,9,1),_ChannelInternalCollisions_Type())
channelInternalCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalCollisions.setStatus(_A)
_ChannelExternalCollisions_Type=Counter64
_ChannelExternalCollisions_Object=MibScalar
channelExternalCollisions=_ChannelExternalCollisions_Object((1,3,6,1,4,1,15397,2,2,25,1,9,2),_ChannelExternalCollisions_Type())
channelExternalCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalCollisions.setStatus(_A)
_ChannelMulticast_ObjectIdentity=ObjectIdentity
channelMulticast=_ChannelMulticast_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,10))
_ChannelInternalMulticast_Type=Counter64
_ChannelInternalMulticast_Object=MibScalar
channelInternalMulticast=_ChannelInternalMulticast_Object((1,3,6,1,4,1,15397,2,2,25,1,10,1),_ChannelInternalMulticast_Type())
channelInternalMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalMulticast.setStatus(_A)
_ChannelExternalMulticast_Type=Counter64
_ChannelExternalMulticast_Object=MibScalar
channelExternalMulticast=_ChannelExternalMulticast_Object((1,3,6,1,4,1,15397,2,2,25,1,10,2),_ChannelExternalMulticast_Type())
channelExternalMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalMulticast.setStatus(_A)
_ChannelRxLengthErrors_ObjectIdentity=ObjectIdentity
channelRxLengthErrors=_ChannelRxLengthErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,11))
_ChannelInternalRxLengthErrors_Type=Counter64
_ChannelInternalRxLengthErrors_Object=MibScalar
channelInternalRxLengthErrors=_ChannelInternalRxLengthErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,11,1),_ChannelInternalRxLengthErrors_Type())
channelInternalRxLengthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxLengthErrors.setStatus(_A)
_ChannelExternalRxLengthErrors_Type=Counter64
_ChannelExternalRxLengthErrors_Object=MibScalar
channelExternalRxLengthErrors=_ChannelExternalRxLengthErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,11,2),_ChannelExternalRxLengthErrors_Type())
channelExternalRxLengthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxLengthErrors.setStatus(_A)
_ChannelRxCrcErrors_ObjectIdentity=ObjectIdentity
channelRxCrcErrors=_ChannelRxCrcErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,12))
_ChannelInternalRxCrcErrors_Type=Counter64
_ChannelInternalRxCrcErrors_Object=MibScalar
channelInternalRxCrcErrors=_ChannelInternalRxCrcErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,12,1),_ChannelInternalRxCrcErrors_Type())
channelInternalRxCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxCrcErrors.setStatus(_A)
_ChannelExternalRxCrcErrors_Type=Counter64
_ChannelExternalRxCrcErrors_Object=MibScalar
channelExternalRxCrcErrors=_ChannelExternalRxCrcErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,12,2),_ChannelExternalRxCrcErrors_Type())
channelExternalRxCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxCrcErrors.setStatus(_A)
_ChannelRxFrameErrors_ObjectIdentity=ObjectIdentity
channelRxFrameErrors=_ChannelRxFrameErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,13))
_ChannelInternalRxFrameErrors_Type=Counter64
_ChannelInternalRxFrameErrors_Object=MibScalar
channelInternalRxFrameErrors=_ChannelInternalRxFrameErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,13,1),_ChannelInternalRxFrameErrors_Type())
channelInternalRxFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxFrameErrors.setStatus(_A)
_ChannelExternalRxFrameErrors_Type=Counter64
_ChannelExternalRxFrameErrors_Object=MibScalar
channelExternalRxFrameErrors=_ChannelExternalRxFrameErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,13,2),_ChannelExternalRxFrameErrors_Type())
channelExternalRxFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxFrameErrors.setStatus(_A)
_ChannelRxFifoErrors_ObjectIdentity=ObjectIdentity
channelRxFifoErrors=_ChannelRxFifoErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,14))
_ChannelINternalRxFifoErrors_Type=Counter64
_ChannelINternalRxFifoErrors_Object=MibScalar
channelINternalRxFifoErrors=_ChannelINternalRxFifoErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,14,1),_ChannelINternalRxFifoErrors_Type())
channelINternalRxFifoErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelINternalRxFifoErrors.setStatus(_A)
_ChannelExternalRxFifoErrors_Type=Counter64
_ChannelExternalRxFifoErrors_Object=MibScalar
channelExternalRxFifoErrors=_ChannelExternalRxFifoErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,14,2),_ChannelExternalRxFifoErrors_Type())
channelExternalRxFifoErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxFifoErrors.setStatus(_A)
_ChannelRxMissedErrors_ObjectIdentity=ObjectIdentity
channelRxMissedErrors=_ChannelRxMissedErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,15))
_ChannelInternalRxMissedErrors_Type=Counter64
_ChannelInternalRxMissedErrors_Object=MibScalar
channelInternalRxMissedErrors=_ChannelInternalRxMissedErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,15,1),_ChannelInternalRxMissedErrors_Type())
channelInternalRxMissedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalRxMissedErrors.setStatus(_A)
_ChannelExternalRxMissedErrors_Type=Counter64
_ChannelExternalRxMissedErrors_Object=MibScalar
channelExternalRxMissedErrors=_ChannelExternalRxMissedErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,15,2),_ChannelExternalRxMissedErrors_Type())
channelExternalRxMissedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalRxMissedErrors.setStatus(_A)
_ChannelTxAborted_ObjectIdentity=ObjectIdentity
channelTxAborted=_ChannelTxAborted_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,16))
_ChannelInternalTxAborted_Type=Counter64
_ChannelInternalTxAborted_Object=MibScalar
channelInternalTxAborted=_ChannelInternalTxAborted_Object((1,3,6,1,4,1,15397,2,2,25,1,16,1),_ChannelInternalTxAborted_Type())
channelInternalTxAborted.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxAborted.setStatus(_A)
_ChannelExternalTxAborted_Type=Counter64
_ChannelExternalTxAborted_Object=MibScalar
channelExternalTxAborted=_ChannelExternalTxAborted_Object((1,3,6,1,4,1,15397,2,2,25,1,16,2),_ChannelExternalTxAborted_Type())
channelExternalTxAborted.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxAborted.setStatus(_A)
_ChannelTxWindowErrors_ObjectIdentity=ObjectIdentity
channelTxWindowErrors=_ChannelTxWindowErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,17))
_ChannelInternalTxWindowErrors_Type=Counter64
_ChannelInternalTxWindowErrors_Object=MibScalar
channelInternalTxWindowErrors=_ChannelInternalTxWindowErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,17,1),_ChannelInternalTxWindowErrors_Type())
channelInternalTxWindowErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxWindowErrors.setStatus(_A)
_ChannelExternalTxWindowErrors_Type=Counter64
_ChannelExternalTxWindowErrors_Object=MibScalar
channelExternalTxWindowErrors=_ChannelExternalTxWindowErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,17,2),_ChannelExternalTxWindowErrors_Type())
channelExternalTxWindowErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxWindowErrors.setStatus(_A)
_ChannelTxCarrierErrors_ObjectIdentity=ObjectIdentity
channelTxCarrierErrors=_ChannelTxCarrierErrors_ObjectIdentity((1,3,6,1,4,1,15397,2,2,25,1,18))
_ChannelInternalTxCarrierErrors_Type=Counter64
_ChannelInternalTxCarrierErrors_Object=MibScalar
channelInternalTxCarrierErrors=_ChannelInternalTxCarrierErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,18,1),_ChannelInternalTxCarrierErrors_Type())
channelInternalTxCarrierErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInternalTxCarrierErrors.setStatus(_A)
_ChannelExternalTxCarrierErrors_Type=Counter64
_ChannelExternalTxCarrierErrors_Object=MibScalar
channelExternalTxCarrierErrors=_ChannelExternalTxCarrierErrors_Object((1,3,6,1,4,1,15397,2,2,25,1,18,2),_ChannelExternalTxCarrierErrors_Type())
channelExternalTxCarrierErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:channelExternalTxCarrierErrors.setStatus(_A)
class _NetDeviceEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NetDeviceEntryIndex_Type.__name__=_C
_NetDeviceEntryIndex_Object=MibTableColumn
netDeviceEntryIndex=_NetDeviceEntryIndex_Object((1,3,6,1,4,1,15397,2,2,25,1,999),_NetDeviceEntryIndex_Type())
netDeviceEntryIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:netDeviceEntryIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'channelstats':channelstats,'channelCfg':channelCfg,'channelNumber':channelNumber,'channelInfoTable':channelInfoTable,'channelInfoEntry':channelInfoEntry,'channelInternalMedia':channelInternalMedia,'channelExternalMedia':channelExternalMedia,'channelInternalNegotiatedMedia':channelInternalNegotiatedMedia,'channelExternalNegotiatedMedia':channelExternalNegotiatedMedia,'channelActive':channelActive,'channelName':channelName,'channelInternalNegotiatedMediaTime':channelInternalNegotiatedMediaTime,'channelexternalNegotiatedMediaTime':channelexternalNegotiatedMediaTime,_E:channelInfoEntryIndex,'netDeviceTable':netDeviceTable,'netDeviceEntry':netDeviceEntry,'channelRxPackets':channelRxPackets,'channelInternalRxPackets':channelInternalRxPackets,'channelExternalRxPackets':channelExternalRxPackets,'channelTxPackets':channelTxPackets,'channelInternalTxPackets':channelInternalTxPackets,'channelExternalTxPackets':channelExternalTxPackets,'channelRxBytes':channelRxBytes,'channelInternalRxBytes':channelInternalRxBytes,'channelExternalRxBytes':channelExternalRxBytes,'channelTxBytes':channelTxBytes,'channelInternalTxBytes':channelInternalTxBytes,'channelExternalTxBytes':channelExternalTxBytes,'channelRxErrors':channelRxErrors,'channelInternalRxErrors':channelInternalRxErrors,'channelExternalRxErrors':channelExternalRxErrors,'channelTxErrors':channelTxErrors,'channelInternalTxErrors':channelInternalTxErrors,'channelExternalTxErrors':channelExternalTxErrors,'channelRxDrops':channelRxDrops,'channelInternalRxDrops':channelInternalRxDrops,'channelExternalRxDrops':channelExternalRxDrops,'channelTxDrops':channelTxDrops,'channelInternalTxDrops':channelInternalTxDrops,'channelExternalTxDrops':channelExternalTxDrops,'channelCollisions':channelCollisions,'channelInternalCollisions':channelInternalCollisions,'channelExternalCollisions':channelExternalCollisions,'channelMulticast':channelMulticast,'channelInternalMulticast':channelInternalMulticast,'channelExternalMulticast':channelExternalMulticast,'channelRxLengthErrors':channelRxLengthErrors,'channelInternalRxLengthErrors':channelInternalRxLengthErrors,'channelExternalRxLengthErrors':channelExternalRxLengthErrors,'channelRxCrcErrors':channelRxCrcErrors,'channelInternalRxCrcErrors':channelInternalRxCrcErrors,'channelExternalRxCrcErrors':channelExternalRxCrcErrors,'channelRxFrameErrors':channelRxFrameErrors,'channelInternalRxFrameErrors':channelInternalRxFrameErrors,'channelExternalRxFrameErrors':channelExternalRxFrameErrors,'channelRxFifoErrors':channelRxFifoErrors,'channelINternalRxFifoErrors':channelINternalRxFifoErrors,'channelExternalRxFifoErrors':channelExternalRxFifoErrors,'channelRxMissedErrors':channelRxMissedErrors,'channelInternalRxMissedErrors':channelInternalRxMissedErrors,'channelExternalRxMissedErrors':channelExternalRxMissedErrors,'channelTxAborted':channelTxAborted,'channelInternalTxAborted':channelInternalTxAborted,'channelExternalTxAborted':channelExternalTxAborted,'channelTxWindowErrors':channelTxWindowErrors,'channelInternalTxWindowErrors':channelInternalTxWindowErrors,'channelExternalTxWindowErrors':channelExternalTxWindowErrors,'channelTxCarrierErrors':channelTxCarrierErrors,'channelInternalTxCarrierErrors':channelInternalTxCarrierErrors,'channelExternalTxCarrierErrors':channelExternalTxCarrierErrors,_N:netDeviceEntryIndex})