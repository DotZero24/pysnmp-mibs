_Q='nbsPALPortIndex'
_P='nbsPortIndex2'
_O='nbsPortIndex'
_N='forward'
_M='nbsPortIndex1'
_L='NotificationType'
_K='OctetString'
_J='nbsAddrIndex'
_I='discard'
_H='normal'
_G='GSWITCH-MIB'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Gswitch_ObjectIdentity=ObjectIdentity
gswitch=_Gswitch_ObjectIdentity((1,3,6,1,4,1,629,2))
_NbsNPorts_Type=Integer32
_NbsNPorts_Object=MibScalar
nbsNPorts=_NbsNPorts_Object((1,3,6,1,4,1,629,2,1),_NbsNPorts_Type())
nbsNPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsNPorts.setStatus(_A)
_NbsDevIdentify_ObjectIdentity=ObjectIdentity
nbsDevIdentify=_NbsDevIdentify_ObjectIdentity((1,3,6,1,4,1,629,2,2))
class _NbsUpLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('notExist',1),('fast2Ethernet100BaseTX',2),('fast2Ethernet100BaseTxFx',3),('fast2Ethernet100BaseFX',4),('atm',5),('fast8Ethernet100BaseTX',6),('fast8Ethernet10or100BaseTX',7),('fast5Ethernet100BaseTX',8),('fast5Ethernet100BaseFX',9),('fast8Ethernet100BaseTP',10),('fast4Ethernet100BaseFO',11),('ISDN',12),('VPN',13),('fast1Ethernet1000BaseGE',14),('FDDI',15),('fast2Ethernet1000BaseGE',16)))
_NbsUpLinkType_Type.__name__=_C
_NbsUpLinkType_Object=MibScalar
nbsUpLinkType=_NbsUpLinkType_Object((1,3,6,1,4,1,629,2,2,1),_NbsUpLinkType_Type())
nbsUpLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUpLinkType.setStatus(_A)
_NbsBaseHardVers_Type=Integer32
_NbsBaseHardVers_Object=MibScalar
nbsBaseHardVers=_NbsBaseHardVers_Object((1,3,6,1,4,1,629,2,2,3),_NbsBaseHardVers_Type())
nbsBaseHardVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsBaseHardVers.setStatus(_A)
_NbsCardHardVers_Type=Integer32
_NbsCardHardVers_Object=MibScalar
nbsCardHardVers=_NbsCardHardVers_Object((1,3,6,1,4,1,629,2,2,4),_NbsCardHardVers_Type())
nbsCardHardVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCardHardVers.setStatus(_A)
_NbsUpLinkHardVers_Type=Integer32
_NbsUpLinkHardVers_Object=MibScalar
nbsUpLinkHardVers=_NbsUpLinkHardVers_Object((1,3,6,1,4,1,629,2,2,5),_NbsUpLinkHardVers_Type())
nbsUpLinkHardVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUpLinkHardVers.setStatus(_A)
_NbsSoftVers_Type=Integer32
_NbsSoftVers_Object=MibScalar
nbsSoftVers=_NbsSoftVers_Object((1,3,6,1,4,1,629,2,2,6),_NbsSoftVers_Type())
nbsSoftVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSoftVers.setStatus(_A)
_NbsSnifferPort_Type=Integer32
_NbsSnifferPort_Object=MibScalar
nbsSnifferPort=_NbsSnifferPort_Object((1,3,6,1,4,1,629,2,2,9),_NbsSnifferPort_Type())
nbsSnifferPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSnifferPort.setStatus(_A)
_NbsCreatinDate_Type=DisplayString
_NbsCreatinDate_Object=MibScalar
nbsCreatinDate=_NbsCreatinDate_Object((1,3,6,1,4,1,629,2,2,10),_NbsCreatinDate_Type())
nbsCreatinDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCreatinDate.setStatus(_A)
_NbsDeviceControl_ObjectIdentity=ObjectIdentity
nbsDeviceControl=_NbsDeviceControl_ObjectIdentity((1,3,6,1,4,1,629,2,3))
class _NbsSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_NbsSpanningTree_Type.__name__=_C
_NbsSpanningTree_Object=MibScalar
nbsSpanningTree=_NbsSpanningTree_Object((1,3,6,1,4,1,629,2,3,6),_NbsSpanningTree_Type())
nbsSpanningTree.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsSpanningTree.setStatus(_A)
class _NbsLearningProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsLearningProcess_Type.__name__=_C
_NbsLearningProcess_Object=MibScalar
nbsLearningProcess=_NbsLearningProcess_Object((1,3,6,1,4,1,629,2,3,7),_NbsLearningProcess_Type())
nbsLearningProcess.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsLearningProcess.setStatus(_A)
class _NbsParitionEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsParitionEnable_Type.__name__=_C
_NbsParitionEnable_Object=MibScalar
nbsParitionEnable=_NbsParitionEnable_Object((1,3,6,1,4,1,629,2,3,8),_NbsParitionEnable_Type())
nbsParitionEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsParitionEnable.setStatus(_A)
class _NbsRMONmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsRMONmode_Type.__name__=_C
_NbsRMONmode_Object=MibScalar
nbsRMONmode=_NbsRMONmode_Object((1,3,6,1,4,1,629,2,3,9),_NbsRMONmode_Type())
nbsRMONmode.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRMONmode.setStatus(_A)
class _NbsBufferThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('limited',1),('not-limited',2)))
_NbsBufferThreshold_Type.__name__=_C
_NbsBufferThreshold_Object=MibScalar
nbsBufferThreshold=_NbsBufferThreshold_Object((1,3,6,1,4,1,629,2,3,10),_NbsBufferThreshold_Type())
nbsBufferThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsBufferThreshold.setStatus(_A)
class _NbsForwardMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsForwardMulticast_Type.__name__=_C
_NbsForwardMulticast_Object=MibScalar
nbsForwardMulticast=_NbsForwardMulticast_Object((1,3,6,1,4,1,629,2,3,12),_NbsForwardMulticast_Type())
nbsForwardMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsForwardMulticast.setStatus(_A)
class _NbsForwardUnkPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsForwardUnkPkts_Type.__name__=_C
_NbsForwardUnkPkts_Object=MibScalar
nbsForwardUnkPkts=_NbsForwardUnkPkts_Object((1,3,6,1,4,1,629,2,3,15),_NbsForwardUnkPkts_Type())
nbsForwardUnkPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsForwardUnkPkts.setStatus(_A)
class _NbsBackOffMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('aggressive',2)))
_NbsBackOffMode_Type.__name__=_C
_NbsBackOffMode_Object=MibScalar
nbsBackOffMode=_NbsBackOffMode_Object((1,3,6,1,4,1,629,2,3,16),_NbsBackOffMode_Type())
nbsBackOffMode.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsBackOffMode.setStatus(_A)
_NbsPortsControl_ObjectIdentity=ObjectIdentity
nbsPortsControl=_NbsPortsControl_ObjectIdentity((1,3,6,1,4,1,629,2,5))
_NbsPortsContTable_Object=MibTable
nbsPortsContTable=_NbsPortsContTable_Object((1,3,6,1,4,1,629,2,5,1))
if mibBuilder.loadTexts:nbsPortsContTable.setStatus(_A)
_NbsPortsContEntry_Object=MibTableRow
nbsPortsContEntry=_NbsPortsContEntry_Object((1,3,6,1,4,1,629,2,5,1,1))
nbsPortsContEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:nbsPortsContEntry.setStatus(_A)
_NbsPortIndex1_Type=Integer32
_NbsPortIndex1_Object=MibTableColumn
nbsPortIndex1=_NbsPortIndex1_Object((1,3,6,1,4,1,629,2,5,1,1,1),_NbsPortIndex1_Type())
nbsPortIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortIndex1.setStatus(_A)
class _NbsPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsPortEnable_Type.__name__=_C
_NbsPortEnable_Object=MibTableColumn
nbsPortEnable=_NbsPortEnable_Object((1,3,6,1,4,1,629,2,5,1,1,2),_NbsPortEnable_Type())
nbsPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortEnable.setStatus(_A)
class _NbsPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_NbsPortDuplex_Type.__name__=_C
_NbsPortDuplex_Object=MibTableColumn
nbsPortDuplex=_NbsPortDuplex_Object((1,3,6,1,4,1,629,2,5,1,1,3),_NbsPortDuplex_Type())
nbsPortDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortDuplex.setStatus(_A)
class _NbsPortMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('sniffer',2)))
_NbsPortMonitor_Type.__name__=_C
_NbsPortMonitor_Object=MibTableColumn
nbsPortMonitor=_NbsPortMonitor_Object((1,3,6,1,4,1,629,2,5,1,1,5),_NbsPortMonitor_Type())
nbsPortMonitor.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortMonitor.setStatus(_A)
class _NbsPortPolDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('disabel',2)))
_NbsPortPolDetection_Type.__name__=_C
_NbsPortPolDetection_Object=MibTableColumn
nbsPortPolDetection=_NbsPortPolDetection_Object((1,3,6,1,4,1,629,2,5,1,1,6),_NbsPortPolDetection_Type())
nbsPortPolDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortPolDetection.setStatus(_A)
class _NbsPortBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_I,2)))
_NbsPortBroadcast_Type.__name__=_C
_NbsPortBroadcast_Object=MibTableColumn
nbsPortBroadcast=_NbsPortBroadcast_Object((1,3,6,1,4,1,629,2,5,1,1,7),_NbsPortBroadcast_Type())
nbsPortBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortBroadcast.setStatus(_A)
class _NbsPortForwardUnk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_I,2)))
_NbsPortForwardUnk_Type.__name__=_C
_NbsPortForwardUnk_Object=MibTableColumn
nbsPortForwardUnk=_NbsPortForwardUnk_Object((1,3,6,1,4,1,629,2,5,1,1,8),_NbsPortForwardUnk_Type())
nbsPortForwardUnk.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortForwardUnk.setStatus(_A)
class _NbsPortSpaning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accept',1),(_I,2)))
_NbsPortSpaning_Type.__name__=_C
_NbsPortSpaning_Object=MibTableColumn
nbsPortSpaning=_NbsPortSpaning_Object((1,3,6,1,4,1,629,2,5,1,1,9),_NbsPortSpaning_Type())
nbsPortSpaning.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortSpaning.setStatus(_A)
class _NbsPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('s10MBps',2),('s100MBps',3),('s1000MBps',4),('s10000MBps',5)))
_NbsPortSpeed_Type.__name__=_C
_NbsPortSpeed_Object=MibTableColumn
nbsPortSpeed=_NbsPortSpeed_Object((1,3,6,1,4,1,629,2,5,1,1,10),_NbsPortSpeed_Type())
nbsPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsPortSpeed.setStatus(_A)
_NbsPortsStatus_ObjectIdentity=ObjectIdentity
nbsPortsStatus=_NbsPortsStatus_ObjectIdentity((1,3,6,1,4,1,629,2,6))
_NbsPortsStatTable_Object=MibTable
nbsPortsStatTable=_NbsPortsStatTable_Object((1,3,6,1,4,1,629,2,6,1))
if mibBuilder.loadTexts:nbsPortsStatTable.setStatus(_A)
_NbsPortsStatEntry_Object=MibTableRow
nbsPortsStatEntry=_NbsPortsStatEntry_Object((1,3,6,1,4,1,629,2,6,1,1))
nbsPortsStatEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:nbsPortsStatEntry.setStatus(_A)
_NbsPortIndex_Type=Integer32
_NbsPortIndex_Object=MibTableColumn
nbsPortIndex=_NbsPortIndex_Object((1,3,6,1,4,1,629,2,6,1,1,1),_NbsPortIndex_Type())
nbsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortIndex.setStatus(_A)
class _NbsPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('empty',1),(_H,2),('fastCopper',3),('fastFiber',4),('slowFiber',5),('gigaCopper',6)))
_NbsPortType_Type.__name__=_C
_NbsPortType_Object=MibTableColumn
nbsPortType=_NbsPortType_Object((1,3,6,1,4,1,629,2,6,1,1,2),_NbsPortType_Type())
nbsPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortType.setStatus(_A)
class _NbsPartition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_NbsPartition_Type.__name__=_C
_NbsPartition_Object=MibTableColumn
nbsPartition=_NbsPartition_Object((1,3,6,1,4,1,629,2,6,1,1,3),_NbsPartition_Type())
nbsPartition.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartition.setStatus(_A)
class _NbsLinkTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pass',1),('fail',2)))
_NbsLinkTest_Type.__name__=_C
_NbsLinkTest_Object=MibTableColumn
nbsLinkTest=_NbsLinkTest_Object((1,3,6,1,4,1,629,2,6,1,1,4),_NbsLinkTest_Type())
nbsLinkTest.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsLinkTest.setStatus(_A)
_NbsPortsCounters_ObjectIdentity=ObjectIdentity
nbsPortsCounters=_NbsPortsCounters_ObjectIdentity((1,3,6,1,4,1,629,2,7))
_NbsPortsCountTable_Object=MibTable
nbsPortsCountTable=_NbsPortsCountTable_Object((1,3,6,1,4,1,629,2,7,1))
if mibBuilder.loadTexts:nbsPortsCountTable.setStatus(_A)
_NbsPortsCountEntry_Object=MibTableRow
nbsPortsCountEntry=_NbsPortsCountEntry_Object((1,3,6,1,4,1,629,2,7,1,1))
nbsPortsCountEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:nbsPortsCountEntry.setStatus(_A)
_NbsPortIndex2_Type=Integer32
_NbsPortIndex2_Object=MibTableColumn
nbsPortIndex2=_NbsPortIndex2_Object((1,3,6,1,4,1,629,2,7,1,1,1),_NbsPortIndex2_Type())
nbsPortIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortIndex2.setStatus(_A)
_NbsPortByteRec_Type=Counter32
_NbsPortByteRec_Object=MibTableColumn
nbsPortByteRec=_NbsPortByteRec_Object((1,3,6,1,4,1,629,2,7,1,1,2),_NbsPortByteRec_Type())
nbsPortByteRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortByteRec.setStatus(_A)
_NbsPortMulByteRec_Type=Counter32
_NbsPortMulByteRec_Object=MibTableColumn
nbsPortMulByteRec=_NbsPortMulByteRec_Object((1,3,6,1,4,1,629,2,7,1,1,3),_NbsPortMulByteRec_Type())
nbsPortMulByteRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortMulByteRec.setStatus(_A)
_NbsPortBroadByteRec_Type=Counter32
_NbsPortBroadByteRec_Object=MibTableColumn
nbsPortBroadByteRec=_NbsPortBroadByteRec_Object((1,3,6,1,4,1,629,2,7,1,1,4),_NbsPortBroadByteRec_Type())
nbsPortBroadByteRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortBroadByteRec.setStatus(_A)
_NbsPortByteSent_Type=Counter32
_NbsPortByteSent_Object=MibTableColumn
nbsPortByteSent=_NbsPortByteSent_Object((1,3,6,1,4,1,629,2,7,1,1,5),_NbsPortByteSent_Type())
nbsPortByteSent.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortByteSent.setStatus(_A)
_NbsPortFramesRec_Type=Counter32
_NbsPortFramesRec_Object=MibTableColumn
nbsPortFramesRec=_NbsPortFramesRec_Object((1,3,6,1,4,1,629,2,7,1,1,6),_NbsPortFramesRec_Type())
nbsPortFramesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFramesRec.setStatus(_A)
_NbsPortMulFramesRec_Type=Counter32
_NbsPortMulFramesRec_Object=MibTableColumn
nbsPortMulFramesRec=_NbsPortMulFramesRec_Object((1,3,6,1,4,1,629,2,7,1,1,7),_NbsPortMulFramesRec_Type())
nbsPortMulFramesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortMulFramesRec.setStatus(_A)
_NbsPortBroadFramesRec_Type=Counter32
_NbsPortBroadFramesRec_Object=MibTableColumn
nbsPortBroadFramesRec=_NbsPortBroadFramesRec_Object((1,3,6,1,4,1,629,2,7,1,1,8),_NbsPortBroadFramesRec_Type())
nbsPortBroadFramesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortBroadFramesRec.setStatus(_A)
_NbsPortFramesSent_Type=Counter32
_NbsPortFramesSent_Object=MibTableColumn
nbsPortFramesSent=_NbsPortFramesSent_Object((1,3,6,1,4,1,629,2,7,1,1,9),_NbsPortFramesSent_Type())
nbsPortFramesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFramesSent.setStatus(_A)
_NbsPortCollisions_Type=Counter32
_NbsPortCollisions_Object=MibTableColumn
nbsPortCollisions=_NbsPortCollisions_Object((1,3,6,1,4,1,629,2,7,1,1,10),_NbsPortCollisions_Type())
nbsPortCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortCollisions.setStatus(_A)
_NbsPortLateColl_Type=Counter32
_NbsPortLateColl_Object=MibTableColumn
nbsPortLateColl=_NbsPortLateColl_Object((1,3,6,1,4,1,629,2,7,1,1,11),_NbsPortLateColl_Type())
nbsPortLateColl.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortLateColl.setStatus(_A)
_NbsPortCRCAligErr_Type=Counter32
_NbsPortCRCAligErr_Object=MibTableColumn
nbsPortCRCAligErr=_NbsPortCRCAligErr_Object((1,3,6,1,4,1,629,2,7,1,1,12),_NbsPortCRCAligErr_Type())
nbsPortCRCAligErr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortCRCAligErr.setStatus(_A)
_NbsPortFramesShort_Type=Counter32
_NbsPortFramesShort_Object=MibTableColumn
nbsPortFramesShort=_NbsPortFramesShort_Object((1,3,6,1,4,1,629,2,7,1,1,13),_NbsPortFramesShort_Type())
nbsPortFramesShort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFramesShort.setStatus(_A)
_NbsPortFrameLong_Type=Counter32
_NbsPortFrameLong_Object=MibTableColumn
nbsPortFrameLong=_NbsPortFrameLong_Object((1,3,6,1,4,1,629,2,7,1,1,14),_NbsPortFrameLong_Type())
nbsPortFrameLong.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFrameLong.setStatus(_A)
_NbsPortJabber_Type=Counter32
_NbsPortJabber_Object=MibTableColumn
nbsPortJabber=_NbsPortJabber_Object((1,3,6,1,4,1,629,2,7,1,1,15),_NbsPortJabber_Type())
nbsPortJabber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortJabber.setStatus(_A)
_NbsPortBadByteRec_Type=Counter32
_NbsPortBadByteRec_Object=MibTableColumn
nbsPortBadByteRec=_NbsPortBadByteRec_Object((1,3,6,1,4,1,629,2,7,1,1,16),_NbsPortBadByteRec_Type())
nbsPortBadByteRec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortBadByteRec.setStatus(_A)
_NbsAddressTable_ObjectIdentity=ObjectIdentity
nbsAddressTable=_NbsAddressTable_ObjectIdentity((1,3,6,1,4,1,629,2,8))
_NbsMACAddrTable_Object=MibTable
nbsMACAddrTable=_NbsMACAddrTable_Object((1,3,6,1,4,1,629,2,8,1))
if mibBuilder.loadTexts:nbsMACAddrTable.setStatus(_A)
_NbsMACAddrEntry_Object=MibTableRow
nbsMACAddrEntry=_NbsMACAddrEntry_Object((1,3,6,1,4,1,629,2,8,1,1))
nbsMACAddrEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:nbsMACAddrEntry.setStatus(_A)
_NbsAddrIndex_Type=Integer32
_NbsAddrIndex_Object=MibTableColumn
nbsAddrIndex=_NbsAddrIndex_Object((1,3,6,1,4,1,629,2,8,1,1,1),_NbsAddrIndex_Type())
nbsAddrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsAddrIndex.setStatus(_A)
class _NbsMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsMACAddress_Type.__name__=_K
_NbsMACAddress_Object=MibTableColumn
nbsMACAddress=_NbsMACAddress_Object((1,3,6,1,4,1,629,2,8,1,1,3),_NbsMACAddress_Type())
nbsMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsMACAddress.setStatus(_A)
_NbsAddrPort_Type=Integer32
_NbsAddrPort_Object=MibTableColumn
nbsAddrPort=_NbsAddrPort_Object((1,3,6,1,4,1,629,2,8,1,1,4),_NbsAddrPort_Type())
nbsAddrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsAddrPort.setStatus(_A)
class _NbsAddrStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_NbsAddrStatic_Type.__name__=_C
_NbsAddrStatic_Object=MibTableColumn
nbsAddrStatic=_NbsAddrStatic_Object((1,3,6,1,4,1,629,2,8,1,1,5),_NbsAddrStatic_Type())
nbsAddrStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsAddrStatic.setStatus(_A)
class _NbsAddrForwardTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('destination-port',1),('all-ports',2)))
_NbsAddrForwardTo_Type.__name__=_C
_NbsAddrForwardTo_Object=MibTableColumn
nbsAddrForwardTo=_NbsAddrForwardTo_Object((1,3,6,1,4,1,629,2,8,1,1,6),_NbsAddrForwardTo_Type())
nbsAddrForwardTo.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsAddrForwardTo.setStatus(_A)
_NbsSlotsTable_ObjectIdentity=ObjectIdentity
nbsSlotsTable=_NbsSlotsTable_ObjectIdentity((1,3,6,1,4,1,629,2,9))
_NbsCardsTable_Object=MibTable
nbsCardsTable=_NbsCardsTable_Object((1,3,6,1,4,1,629,2,9,1))
if mibBuilder.loadTexts:nbsCardsTable.setStatus(_A)
_NbsCardsEntry_Object=MibTableRow
nbsCardsEntry=_NbsCardsEntry_Object((1,3,6,1,4,1,629,2,9,1,1))
nbsCardsEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:nbsCardsEntry.setStatus(_A)
_NbsCardIndex_Type=Integer32
_NbsCardIndex_Object=MibTableColumn
nbsCardIndex=_NbsCardIndex_Object((1,3,6,1,4,1,629,2,9,1,1,1),_NbsCardIndex_Type())
nbsCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCardIndex.setStatus(_A)
class _NbsCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('emptySlot',1),('copper20Ethernet10or100Base',2),('copper40Ethernet10Base',3),('powerSupplyError',4),('powerSupplyOK',5),('fibre10Ethernet100Base',6),('fansUnitError',7),('fansUnitOK',8),('universal',9)))
_NbsCardType_Type.__name__=_C
_NbsCardType_Object=MibTableColumn
nbsCardType=_NbsCardType_Object((1,3,6,1,4,1,629,2,9,1,1,2),_NbsCardType_Type())
nbsCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCardType.setStatus(_A)
_NbsNMacRecords_Type=Integer32
_NbsNMacRecords_Object=MibScalar
nbsNMacRecords=_NbsNMacRecords_Object((1,3,6,1,4,1,629,2,10),_NbsNMacRecords_Type())
nbsNMacRecords.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsNMacRecords.setStatus(_A)
_NbsMacFirstGap_Type=Integer32
_NbsMacFirstGap_Object=MibScalar
nbsMacFirstGap=_NbsMacFirstGap_Object((1,3,6,1,4,1,629,2,11),_NbsMacFirstGap_Type())
nbsMacFirstGap.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMacFirstGap.setStatus(_A)
_NbsPALPorts_ObjectIdentity=ObjectIdentity
nbsPALPorts=_NbsPALPorts_ObjectIdentity((1,3,6,1,4,1,629,2,12))
_NbsPALPortsTable_Object=MibTable
nbsPALPortsTable=_NbsPALPortsTable_Object((1,3,6,1,4,1,629,2,12,1))
if mibBuilder.loadTexts:nbsPALPortsTable.setStatus(_A)
_NbsPALPortsEntry_Object=MibTableRow
nbsPALPortsEntry=_NbsPALPortsEntry_Object((1,3,6,1,4,1,629,2,12,1,1))
nbsPALPortsEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:nbsPALPortsEntry.setStatus(_A)
_NbsPALPortIndex_Type=Integer32
_NbsPALPortIndex_Object=MibTableColumn
nbsPALPortIndex=_NbsPALPortIndex_Object((1,3,6,1,4,1,629,2,12,1,1,1),_NbsPALPortIndex_Type())
nbsPALPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPALPortIndex.setStatus(_A)
_NbsPALPortOpticPower_Type=Integer32
_NbsPALPortOpticPower_Object=MibTableColumn
nbsPALPortOpticPower=_NbsPALPortOpticPower_Object((1,3,6,1,4,1,629,2,12,1,1,2),_NbsPALPortOpticPower_Type())
nbsPALPortOpticPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPALPortOpticPower.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'nbase':nbase,'gswitch':gswitch,'nbsNPorts':nbsNPorts,'nbsDevIdentify':nbsDevIdentify,'nbsUpLinkType':nbsUpLinkType,'nbsBaseHardVers':nbsBaseHardVers,'nbsCardHardVers':nbsCardHardVers,'nbsUpLinkHardVers':nbsUpLinkHardVers,'nbsSoftVers':nbsSoftVers,'nbsSnifferPort':nbsSnifferPort,'nbsCreatinDate':nbsCreatinDate,'nbsDeviceControl':nbsDeviceControl,'nbsSpanningTree':nbsSpanningTree,'nbsLearningProcess':nbsLearningProcess,'nbsParitionEnable':nbsParitionEnable,'nbsRMONmode':nbsRMONmode,'nbsBufferThreshold':nbsBufferThreshold,'nbsForwardMulticast':nbsForwardMulticast,'nbsForwardUnkPkts':nbsForwardUnkPkts,'nbsBackOffMode':nbsBackOffMode,'nbsPortsControl':nbsPortsControl,'nbsPortsContTable':nbsPortsContTable,'nbsPortsContEntry':nbsPortsContEntry,_M:nbsPortIndex1,'nbsPortEnable':nbsPortEnable,'nbsPortDuplex':nbsPortDuplex,'nbsPortMonitor':nbsPortMonitor,'nbsPortPolDetection':nbsPortPolDetection,'nbsPortBroadcast':nbsPortBroadcast,'nbsPortForwardUnk':nbsPortForwardUnk,'nbsPortSpaning':nbsPortSpaning,'nbsPortSpeed':nbsPortSpeed,'nbsPortsStatus':nbsPortsStatus,'nbsPortsStatTable':nbsPortsStatTable,'nbsPortsStatEntry':nbsPortsStatEntry,_O:nbsPortIndex,'nbsPortType':nbsPortType,'nbsPartition':nbsPartition,'nbsLinkTest':nbsLinkTest,'nbsPortsCounters':nbsPortsCounters,'nbsPortsCountTable':nbsPortsCountTable,'nbsPortsCountEntry':nbsPortsCountEntry,_P:nbsPortIndex2,'nbsPortByteRec':nbsPortByteRec,'nbsPortMulByteRec':nbsPortMulByteRec,'nbsPortBroadByteRec':nbsPortBroadByteRec,'nbsPortByteSent':nbsPortByteSent,'nbsPortFramesRec':nbsPortFramesRec,'nbsPortMulFramesRec':nbsPortMulFramesRec,'nbsPortBroadFramesRec':nbsPortBroadFramesRec,'nbsPortFramesSent':nbsPortFramesSent,'nbsPortCollisions':nbsPortCollisions,'nbsPortLateColl':nbsPortLateColl,'nbsPortCRCAligErr':nbsPortCRCAligErr,'nbsPortFramesShort':nbsPortFramesShort,'nbsPortFrameLong':nbsPortFrameLong,'nbsPortJabber':nbsPortJabber,'nbsPortBadByteRec':nbsPortBadByteRec,'nbsAddressTable':nbsAddressTable,'nbsMACAddrTable':nbsMACAddrTable,'nbsMACAddrEntry':nbsMACAddrEntry,_J:nbsAddrIndex,'nbsMACAddress':nbsMACAddress,'nbsAddrPort':nbsAddrPort,'nbsAddrStatic':nbsAddrStatic,'nbsAddrForwardTo':nbsAddrForwardTo,'nbsSlotsTable':nbsSlotsTable,'nbsCardsTable':nbsCardsTable,'nbsCardsEntry':nbsCardsEntry,'nbsCardIndex':nbsCardIndex,'nbsCardType':nbsCardType,'nbsNMacRecords':nbsNMacRecords,'nbsMacFirstGap':nbsMacFirstGap,'nbsPALPorts':nbsPALPorts,'nbsPALPortsTable':nbsPALPortsTable,'nbsPALPortsEntry':nbsPALPortsEntry,_Q:nbsPALPortIndex,'nbsPALPortOpticPower':nbsPALPortOpticPower})