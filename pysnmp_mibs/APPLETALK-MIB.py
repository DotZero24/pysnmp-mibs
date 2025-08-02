_q='atportPtoPIndex'
_p='adspConnLocalConnID'
_o='adspConnRemoteAddress'
_n='adspConnLocalAddress'
_m='closed'
_l='aspConnID'
_k='aspConnRemoteAddress'
_j='aspConnLocalAddress'
_i='papServerIndex'
_h='atpListenerAddress'
_g='nbpIndex'
_f='zipZoneIndex'
_e='zipZoneNetStart'
_d='kipNetStart'
_c='appletalk'
_b='rtmpRangeStart'
_a='ddpForwardingNetEnd'
_Z='ddpListenerAddress'
_Y='atportZoneName'
_X='atportZonePort'
_W='softSeed'
_V='conflictAverseSeed'
_U='guessed'
_T='garnered'
_S='conflictOrientedSeed'
_R='serialNonstandard'
_Q='serialPPP'
_P='aarpNetAddress'
_O='aarpIfIndex'
_N='llapIfIndex'
_M='unconfigured'
_L='ATName'
_K='other'
_J='deprecated'
_I='atportIndex'
_H='valid'
_G='not-accessible'
_F='invalid'
_E='APPLETALK-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class ATNetworkNumber(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class DdpNodeAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class DdpSocketAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class ATName(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Appletalk_ObjectIdentity=ObjectIdentity
appletalk=_Appletalk_ObjectIdentity((1,3,6,1,2,1,13))
_Llap_ObjectIdentity=ObjectIdentity
llap=_Llap_ObjectIdentity((1,3,6,1,2,1,13,1))
_LlapTable_Object=MibTable
llapTable=_LlapTable_Object((1,3,6,1,2,1,13,1,1))
if mibBuilder.loadTexts:llapTable.setStatus(_A)
_LlapEntry_Object=MibTableRow
llapEntry=_LlapEntry_Object((1,3,6,1,2,1,13,1,1,1))
llapEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:llapEntry.setStatus(_A)
_LlapIfIndex_Type=Integer32
_LlapIfIndex_Object=MibTableColumn
llapIfIndex=_LlapIfIndex_Object((1,3,6,1,2,1,13,1,1,1,1),_LlapIfIndex_Type())
llapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llapIfIndex.setStatus(_A)
_LlapInPkts_Type=Counter32
_LlapInPkts_Object=MibTableColumn
llapInPkts=_LlapInPkts_Object((1,3,6,1,2,1,13,1,1,1,2),_LlapInPkts_Type())
llapInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:llapInPkts.setStatus(_J)
_LlapOutPkts_Type=Counter32
_LlapOutPkts_Object=MibTableColumn
llapOutPkts=_LlapOutPkts_Object((1,3,6,1,2,1,13,1,1,1,3),_LlapOutPkts_Type())
llapOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:llapOutPkts.setStatus(_J)
_LlapInNoHandlers_Type=Counter32
_LlapInNoHandlers_Object=MibTableColumn
llapInNoHandlers=_LlapInNoHandlers_Object((1,3,6,1,2,1,13,1,1,1,4),_LlapInNoHandlers_Type())
llapInNoHandlers.setMaxAccess(_B)
if mibBuilder.loadTexts:llapInNoHandlers.setStatus(_J)
_LlapInLengthErrors_Type=Counter32
_LlapInLengthErrors_Object=MibTableColumn
llapInLengthErrors=_LlapInLengthErrors_Object((1,3,6,1,2,1,13,1,1,1,5),_LlapInLengthErrors_Type())
llapInLengthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:llapInLengthErrors.setStatus(_A)
_LlapInErrors_Type=Counter32
_LlapInErrors_Object=MibTableColumn
llapInErrors=_LlapInErrors_Object((1,3,6,1,2,1,13,1,1,1,6),_LlapInErrors_Type())
llapInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:llapInErrors.setStatus(_J)
_LlapCollisions_Type=Counter32
_LlapCollisions_Object=MibTableColumn
llapCollisions=_LlapCollisions_Object((1,3,6,1,2,1,13,1,1,1,7),_LlapCollisions_Type())
llapCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:llapCollisions.setStatus(_A)
_LlapDefers_Type=Counter32
_LlapDefers_Object=MibTableColumn
llapDefers=_LlapDefers_Object((1,3,6,1,2,1,13,1,1,1,8),_LlapDefers_Type())
llapDefers.setMaxAccess(_B)
if mibBuilder.loadTexts:llapDefers.setStatus(_A)
_LlapNoDataErrors_Type=Counter32
_LlapNoDataErrors_Object=MibTableColumn
llapNoDataErrors=_LlapNoDataErrors_Object((1,3,6,1,2,1,13,1,1,1,9),_LlapNoDataErrors_Type())
llapNoDataErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:llapNoDataErrors.setStatus(_A)
_LlapRandomCTSErrors_Type=Counter32
_LlapRandomCTSErrors_Object=MibTableColumn
llapRandomCTSErrors=_LlapRandomCTSErrors_Object((1,3,6,1,2,1,13,1,1,1,10),_LlapRandomCTSErrors_Type())
llapRandomCTSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:llapRandomCTSErrors.setStatus(_A)
_LlapFCSErrors_Type=Counter32
_LlapFCSErrors_Object=MibTableColumn
llapFCSErrors=_LlapFCSErrors_Object((1,3,6,1,2,1,13,1,1,1,11),_LlapFCSErrors_Type())
llapFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:llapFCSErrors.setStatus(_A)
_Aarp_ObjectIdentity=ObjectIdentity
aarp=_Aarp_ObjectIdentity((1,3,6,1,2,1,13,2))
_AarpTable_Object=MibTable
aarpTable=_AarpTable_Object((1,3,6,1,2,1,13,2,1))
if mibBuilder.loadTexts:aarpTable.setStatus(_A)
_AarpEntry_Object=MibTableRow
aarpEntry=_AarpEntry_Object((1,3,6,1,2,1,13,2,1,1))
aarpEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:aarpEntry.setStatus(_A)
_AarpIfIndex_Type=Integer32
_AarpIfIndex_Object=MibTableColumn
aarpIfIndex=_AarpIfIndex_Object((1,3,6,1,2,1,13,2,1,1,1),_AarpIfIndex_Type())
aarpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aarpIfIndex.setStatus(_A)
_AarpPhysAddress_Type=OctetString
_AarpPhysAddress_Object=MibTableColumn
aarpPhysAddress=_AarpPhysAddress_Object((1,3,6,1,2,1,13,2,1,1,2),_AarpPhysAddress_Type())
aarpPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:aarpPhysAddress.setStatus(_A)
_AarpNetAddress_Type=DdpNodeAddress
_AarpNetAddress_Object=MibTableColumn
aarpNetAddress=_AarpNetAddress_Object((1,3,6,1,2,1,13,2,1,1,3),_AarpNetAddress_Type())
aarpNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aarpNetAddress.setStatus(_A)
class _AarpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_AarpStatus_Type.__name__=_D
_AarpStatus_Object=MibTableColumn
aarpStatus=_AarpStatus_Object((1,3,6,1,2,1,13,2,1,1,4),_AarpStatus_Type())
aarpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aarpStatus.setStatus(_A)
_AarpLookups_Type=Counter32
_AarpLookups_Object=MibScalar
aarpLookups=_AarpLookups_Object((1,3,6,1,2,1,13,2,2),_AarpLookups_Type())
aarpLookups.setMaxAccess(_B)
if mibBuilder.loadTexts:aarpLookups.setStatus(_A)
_AarpHits_Type=Counter32
_AarpHits_Object=MibScalar
aarpHits=_AarpHits_Object((1,3,6,1,2,1,13,2,3),_AarpHits_Type())
aarpHits.setMaxAccess(_B)
if mibBuilder.loadTexts:aarpHits.setStatus(_A)
_Atport_ObjectIdentity=ObjectIdentity
atport=_Atport_ObjectIdentity((1,3,6,1,2,1,13,3))
_AtportTable_Object=MibTable
atportTable=_AtportTable_Object((1,3,6,1,2,1,13,3,1))
if mibBuilder.loadTexts:atportTable.setStatus(_A)
_AtportEntry_Object=MibTableRow
atportEntry=_AtportEntry_Object((1,3,6,1,2,1,13,3,1,1))
atportEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:atportEntry.setStatus(_A)
_AtportIndex_Type=Integer32
_AtportIndex_Object=MibTableColumn
atportIndex=_AtportIndex_Object((1,3,6,1,2,1,13,3,1,1,1),_AtportIndex_Type())
atportIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atportIndex.setStatus(_A)
_AtportDescr_Type=DisplayString
_AtportDescr_Object=MibTableColumn
atportDescr=_AtportDescr_Object((1,3,6,1,2,1,13,3,1,1,2),_AtportDescr_Type())
atportDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:atportDescr.setStatus(_A)
class _AtportType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_K,1),('localtalk',2),('ethertalk1',3),('ethertalk2',4),('tokentalk',5),('iptalk',6),(_Q,7),(_R,8),('virtual',9),('fdditalk',10),('arctalk',11),('smdstalk',12),('aurp',13),('frameRelay',14),('x25',15),('ip',16),('osi',17),('decnetIV',18),('arap',19),('isdnInThePacketMode',20),('nonAppleTalk3Com',21),('ipx',22),('arns',23),('hdlc',24)))
_AtportType_Type.__name__=_D
_AtportType_Object=MibTableColumn
atportType=_AtportType_Object((1,3,6,1,2,1,13,3,1,1,3),_AtportType_Type())
atportType.setMaxAccess(_C)
if mibBuilder.loadTexts:atportType.setStatus(_A)
_AtportNetStart_Type=ATNetworkNumber
_AtportNetStart_Object=MibTableColumn
atportNetStart=_AtportNetStart_Object((1,3,6,1,2,1,13,3,1,1,4),_AtportNetStart_Type())
atportNetStart.setMaxAccess(_C)
if mibBuilder.loadTexts:atportNetStart.setStatus(_A)
_AtportNetEnd_Type=ATNetworkNumber
_AtportNetEnd_Object=MibTableColumn
atportNetEnd=_AtportNetEnd_Object((1,3,6,1,2,1,13,3,1,1,5),_AtportNetEnd_Type())
atportNetEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:atportNetEnd.setStatus(_A)
_AtportNetAddress_Type=DdpNodeAddress
_AtportNetAddress_Object=MibTableColumn
atportNetAddress=_AtportNetAddress_Object((1,3,6,1,2,1,13,3,1,1,6),_AtportNetAddress_Type())
atportNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atportNetAddress.setStatus(_A)
class _AtportStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routing',1),(_M,2),('off',3),(_F,4),('endNode',5),('offDueToConflict',6),(_K,7)))
_AtportStatus_Type.__name__=_D
_AtportStatus_Object=MibTableColumn
atportStatus=_AtportStatus_Object((1,3,6,1,2,1,13,3,1,1,7),_AtportStatus_Type())
atportStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atportStatus.setStatus(_A)
class _AtportNetConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_M,4),(_V,5),(_W,6)))
_AtportNetConfig_Type.__name__=_D
_AtportNetConfig_Object=MibTableColumn
atportNetConfig=_AtportNetConfig_Object((1,3,6,1,2,1,13,3,1,1,8),_AtportNetConfig_Type())
atportNetConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atportNetConfig.setStatus(_A)
class _AtportZoneConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_M,4),(_V,5),(_W,6)))
_AtportZoneConfig_Type.__name__=_D
_AtportZoneConfig_Object=MibTableColumn
atportZoneConfig=_AtportZoneConfig_Object((1,3,6,1,2,1,13,3,1,1,9),_AtportZoneConfig_Type())
atportZoneConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atportZoneConfig.setStatus(_A)
_AtportZoneDefault_Type=ATName
_AtportZoneDefault_Object=MibTableColumn
atportZoneDefault=_AtportZoneDefault_Object((1,3,6,1,2,1,13,3,1,1,10),_AtportZoneDefault_Type())
atportZoneDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:atportZoneDefault.setStatus(_A)
_AtportIfIndex_Type=Integer32
_AtportIfIndex_Object=MibTableColumn
atportIfIndex=_AtportIfIndex_Object((1,3,6,1,2,1,13,3,1,1,11),_AtportIfIndex_Type())
atportIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atportIfIndex.setStatus(_A)
_AtportNetFrom_Type=DdpNodeAddress
_AtportNetFrom_Object=MibTableColumn
atportNetFrom=_AtportNetFrom_Object((1,3,6,1,2,1,13,3,1,1,12),_AtportNetFrom_Type())
atportNetFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:atportNetFrom.setStatus(_A)
_AtportZoneFrom_Type=DdpNodeAddress
_AtportZoneFrom_Object=MibTableColumn
atportZoneFrom=_AtportZoneFrom_Object((1,3,6,1,2,1,13,3,1,1,13),_AtportZoneFrom_Type())
atportZoneFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:atportZoneFrom.setStatus(_A)
_AtportInPkts_Type=Counter32
_AtportInPkts_Object=MibTableColumn
atportInPkts=_AtportInPkts_Object((1,3,6,1,2,1,13,3,1,1,14),_AtportInPkts_Type())
atportInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atportInPkts.setStatus(_A)
_AtportOutPkts_Type=Counter32
_AtportOutPkts_Object=MibTableColumn
atportOutPkts=_AtportOutPkts_Object((1,3,6,1,2,1,13,3,1,1,15),_AtportOutPkts_Type())
atportOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atportOutPkts.setStatus(_A)
class _AtportHome_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('home',1),('notHome',2)))
_AtportHome_Type.__name__=_D
_AtportHome_Object=MibTableColumn
atportHome=_AtportHome_Object((1,3,6,1,2,1,13,3,1,1,16),_AtportHome_Type())
atportHome.setMaxAccess(_B)
if mibBuilder.loadTexts:atportHome.setStatus(_A)
_AtportCurrentZone_Type=ATName
_AtportCurrentZone_Object=MibTableColumn
atportCurrentZone=_AtportCurrentZone_Object((1,3,6,1,2,1,13,3,1,1,17),_AtportCurrentZone_Type())
atportCurrentZone.setMaxAccess(_C)
if mibBuilder.loadTexts:atportCurrentZone.setStatus(_A)
_AtportConflictPhysAddr_Type=OctetString
_AtportConflictPhysAddr_Object=MibTableColumn
atportConflictPhysAddr=_AtportConflictPhysAddr_Object((1,3,6,1,2,1,13,3,1,1,18),_AtportConflictPhysAddr_Type())
atportConflictPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atportConflictPhysAddr.setStatus(_A)
_AtportZoneTable_Object=MibTable
atportZoneTable=_AtportZoneTable_Object((1,3,6,1,2,1,13,3,2))
if mibBuilder.loadTexts:atportZoneTable.setStatus(_A)
_AtportZoneEntry_Object=MibTableRow
atportZoneEntry=_AtportZoneEntry_Object((1,3,6,1,2,1,13,3,2,1))
atportZoneEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:atportZoneEntry.setStatus(_A)
_AtportZonePort_Type=Integer32
_AtportZonePort_Object=MibTableColumn
atportZonePort=_AtportZonePort_Object((1,3,6,1,2,1,13,3,2,1,1),_AtportZonePort_Type())
atportZonePort.setMaxAccess(_G)
if mibBuilder.loadTexts:atportZonePort.setStatus(_A)
class _AtportZoneName_Type(ATName):subtypeSpec=ATName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AtportZoneName_Type.__name__=_L
_AtportZoneName_Object=MibTableColumn
atportZoneName=_AtportZoneName_Object((1,3,6,1,2,1,13,3,2,1,2),_AtportZoneName_Type())
atportZoneName.setMaxAccess(_G)
if mibBuilder.loadTexts:atportZoneName.setStatus(_A)
class _AtportZoneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_AtportZoneStatus_Type.__name__=_D
_AtportZoneStatus_Object=MibTableColumn
atportZoneStatus=_AtportZoneStatus_Object((1,3,6,1,2,1,13,3,2,1,3),_AtportZoneStatus_Type())
atportZoneStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atportZoneStatus.setStatus(_A)
_Ddp_ObjectIdentity=ObjectIdentity
ddp=_Ddp_ObjectIdentity((1,3,6,1,2,1,13,4))
_DdpOutRequests_Type=Counter32
_DdpOutRequests_Object=MibScalar
ddpOutRequests=_DdpOutRequests_Object((1,3,6,1,2,1,13,4,1),_DdpOutRequests_Type())
ddpOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpOutRequests.setStatus(_A)
_DdpOutShorts_Type=Counter32
_DdpOutShorts_Object=MibScalar
ddpOutShorts=_DdpOutShorts_Object((1,3,6,1,2,1,13,4,2),_DdpOutShorts_Type())
ddpOutShorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpOutShorts.setStatus(_A)
_DdpOutLongs_Type=Counter32
_DdpOutLongs_Object=MibScalar
ddpOutLongs=_DdpOutLongs_Object((1,3,6,1,2,1,13,4,3),_DdpOutLongs_Type())
ddpOutLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpOutLongs.setStatus(_A)
_DdpInReceives_Type=Counter32
_DdpInReceives_Object=MibScalar
ddpInReceives=_DdpInReceives_Object((1,3,6,1,2,1,13,4,4),_DdpInReceives_Type())
ddpInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpInReceives.setStatus(_A)
_DdpForwRequests_Type=Counter32
_DdpForwRequests_Object=MibScalar
ddpForwRequests=_DdpForwRequests_Object((1,3,6,1,2,1,13,4,5),_DdpForwRequests_Type())
ddpForwRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwRequests.setStatus(_A)
_DdpInLocalDatagrams_Type=Counter32
_DdpInLocalDatagrams_Object=MibScalar
ddpInLocalDatagrams=_DdpInLocalDatagrams_Object((1,3,6,1,2,1,13,4,6),_DdpInLocalDatagrams_Type())
ddpInLocalDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpInLocalDatagrams.setStatus(_A)
_DdpNoProtocolHandlers_Type=Counter32
_DdpNoProtocolHandlers_Object=MibScalar
ddpNoProtocolHandlers=_DdpNoProtocolHandlers_Object((1,3,6,1,2,1,13,4,7),_DdpNoProtocolHandlers_Type())
ddpNoProtocolHandlers.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpNoProtocolHandlers.setStatus(_A)
_DdpOutNoRoutes_Type=Counter32
_DdpOutNoRoutes_Object=MibScalar
ddpOutNoRoutes=_DdpOutNoRoutes_Object((1,3,6,1,2,1,13,4,8),_DdpOutNoRoutes_Type())
ddpOutNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpOutNoRoutes.setStatus(_A)
_DdpTooShortErrors_Type=Counter32
_DdpTooShortErrors_Object=MibScalar
ddpTooShortErrors=_DdpTooShortErrors_Object((1,3,6,1,2,1,13,4,9),_DdpTooShortErrors_Type())
ddpTooShortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpTooShortErrors.setStatus(_A)
_DdpTooLongErrors_Type=Counter32
_DdpTooLongErrors_Object=MibScalar
ddpTooLongErrors=_DdpTooLongErrors_Object((1,3,6,1,2,1,13,4,10),_DdpTooLongErrors_Type())
ddpTooLongErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpTooLongErrors.setStatus(_A)
_DdpBroadcastErrors_Type=Counter32
_DdpBroadcastErrors_Object=MibScalar
ddpBroadcastErrors=_DdpBroadcastErrors_Object((1,3,6,1,2,1,13,4,11),_DdpBroadcastErrors_Type())
ddpBroadcastErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpBroadcastErrors.setStatus(_A)
_DdpShortDDPErrors_Type=Counter32
_DdpShortDDPErrors_Object=MibScalar
ddpShortDDPErrors=_DdpShortDDPErrors_Object((1,3,6,1,2,1,13,4,12),_DdpShortDDPErrors_Type())
ddpShortDDPErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpShortDDPErrors.setStatus(_A)
_DdpHopCountErrors_Type=Counter32
_DdpHopCountErrors_Object=MibScalar
ddpHopCountErrors=_DdpHopCountErrors_Object((1,3,6,1,2,1,13,4,13),_DdpHopCountErrors_Type())
ddpHopCountErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpHopCountErrors.setStatus(_A)
_DdpChecksumErrors_Type=Counter32
_DdpChecksumErrors_Object=MibScalar
ddpChecksumErrors=_DdpChecksumErrors_Object((1,3,6,1,2,1,13,4,14),_DdpChecksumErrors_Type())
ddpChecksumErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpChecksumErrors.setStatus(_A)
_DdpListenerTable_Object=MibTable
ddpListenerTable=_DdpListenerTable_Object((1,3,6,1,2,1,13,4,15))
if mibBuilder.loadTexts:ddpListenerTable.setStatus(_A)
_DdpListenerEntry_Object=MibTableRow
ddpListenerEntry=_DdpListenerEntry_Object((1,3,6,1,2,1,13,4,15,1))
ddpListenerEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:ddpListenerEntry.setStatus(_A)
_DdpListenerAddress_Type=DdpSocketAddress
_DdpListenerAddress_Object=MibTableColumn
ddpListenerAddress=_DdpListenerAddress_Object((1,3,6,1,2,1,13,4,15,1,1),_DdpListenerAddress_Type())
ddpListenerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ddpListenerAddress.setStatus(_A)
_DdpListenerInPkts_Type=Counter32
_DdpListenerInPkts_Object=MibTableColumn
ddpListenerInPkts=_DdpListenerInPkts_Object((1,3,6,1,2,1,13,4,15,1,2),_DdpListenerInPkts_Type())
ddpListenerInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpListenerInPkts.setStatus(_A)
class _DdpListenerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_DdpListenerStatus_Type.__name__=_D
_DdpListenerStatus_Object=MibTableColumn
ddpListenerStatus=_DdpListenerStatus_Object((1,3,6,1,2,1,13,4,15,1,3),_DdpListenerStatus_Type())
ddpListenerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ddpListenerStatus.setStatus(_A)
_DdpForwardingTable_Object=MibTable
ddpForwardingTable=_DdpForwardingTable_Object((1,3,6,1,2,1,13,4,16))
if mibBuilder.loadTexts:ddpForwardingTable.setStatus(_A)
_DdpForwardingEntry_Object=MibTableRow
ddpForwardingEntry=_DdpForwardingEntry_Object((1,3,6,1,2,1,13,4,16,1))
ddpForwardingEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:ddpForwardingEntry.setStatus(_A)
_DdpForwardingNetEnd_Type=ATNetworkNumber
_DdpForwardingNetEnd_Object=MibTableColumn
ddpForwardingNetEnd=_DdpForwardingNetEnd_Object((1,3,6,1,2,1,13,4,16,1,1),_DdpForwardingNetEnd_Type())
ddpForwardingNetEnd.setMaxAccess(_G)
if mibBuilder.loadTexts:ddpForwardingNetEnd.setStatus(_A)
_DdpForwardingNetStart_Type=ATNetworkNumber
_DdpForwardingNetStart_Object=MibTableColumn
ddpForwardingNetStart=_DdpForwardingNetStart_Object((1,3,6,1,2,1,13,4,16,1,2),_DdpForwardingNetStart_Type())
ddpForwardingNetStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingNetStart.setStatus(_A)
_DdpForwardingNextHop_Type=OctetString
_DdpForwardingNextHop_Object=MibTableColumn
ddpForwardingNextHop=_DdpForwardingNextHop_Object((1,3,6,1,2,1,13,4,16,1,3),_DdpForwardingNextHop_Type())
ddpForwardingNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingNextHop.setStatus(_A)
_DdpForwardingProto_Type=ObjectIdentifier
_DdpForwardingProto_Object=MibTableColumn
ddpForwardingProto=_DdpForwardingProto_Object((1,3,6,1,2,1,13,4,16,1,4),_DdpForwardingProto_Type())
ddpForwardingProto.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingProto.setStatus(_A)
_DdpForwardingModifiedTime_Type=TimeTicks
_DdpForwardingModifiedTime_Object=MibTableColumn
ddpForwardingModifiedTime=_DdpForwardingModifiedTime_Object((1,3,6,1,2,1,13,4,16,1,5),_DdpForwardingModifiedTime_Type())
ddpForwardingModifiedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingModifiedTime.setStatus(_A)
_DdpForwardingUseCounts_Type=Counter32
_DdpForwardingUseCounts_Object=MibTableColumn
ddpForwardingUseCounts=_DdpForwardingUseCounts_Object((1,3,6,1,2,1,13,4,16,1,6),_DdpForwardingUseCounts_Type())
ddpForwardingUseCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingUseCounts.setStatus(_A)
_DdpForwardingPort_Type=Integer32
_DdpForwardingPort_Object=MibTableColumn
ddpForwardingPort=_DdpForwardingPort_Object((1,3,6,1,2,1,13,4,16,1,7),_DdpForwardingPort_Type())
ddpForwardingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingPort.setStatus(_A)
_DdpForwProtoOids_ObjectIdentity=ObjectIdentity
ddpForwProtoOids=_DdpForwProtoOids_ObjectIdentity((1,3,6,1,2,1,13,4,17))
_RtmpRoutingProto_ObjectIdentity=ObjectIdentity
rtmpRoutingProto=_RtmpRoutingProto_ObjectIdentity((1,3,6,1,2,1,13,4,17,1))
_KipRoutingProto_ObjectIdentity=ObjectIdentity
kipRoutingProto=_KipRoutingProto_ObjectIdentity((1,3,6,1,2,1,13,4,17,2))
_DdpForwardingTableOverflows_Type=Counter32
_DdpForwardingTableOverflows_Object=MibScalar
ddpForwardingTableOverflows=_DdpForwardingTableOverflows_Object((1,3,6,1,2,1,13,4,18),_DdpForwardingTableOverflows_Type())
ddpForwardingTableOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ddpForwardingTableOverflows.setStatus(_A)
_Rtmp_ObjectIdentity=ObjectIdentity
rtmp=_Rtmp_ObjectIdentity((1,3,6,1,2,1,13,5))
_RtmpTable_Object=MibTable
rtmpTable=_RtmpTable_Object((1,3,6,1,2,1,13,5,1))
if mibBuilder.loadTexts:rtmpTable.setStatus(_A)
_RtmpEntry_Object=MibTableRow
rtmpEntry=_RtmpEntry_Object((1,3,6,1,2,1,13,5,1,1))
rtmpEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:rtmpEntry.setStatus(_A)
_RtmpRangeStart_Type=ATNetworkNumber
_RtmpRangeStart_Object=MibTableColumn
rtmpRangeStart=_RtmpRangeStart_Object((1,3,6,1,2,1,13,5,1,1,1),_RtmpRangeStart_Type())
rtmpRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpRangeStart.setStatus(_A)
_RtmpRangeEnd_Type=ATNetworkNumber
_RtmpRangeEnd_Object=MibTableColumn
rtmpRangeEnd=_RtmpRangeEnd_Object((1,3,6,1,2,1,13,5,1,1,2),_RtmpRangeEnd_Type())
rtmpRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpRangeEnd.setStatus(_A)
_RtmpNextHop_Type=OctetString
_RtmpNextHop_Object=MibTableColumn
rtmpNextHop=_RtmpNextHop_Object((1,3,6,1,2,1,13,5,1,1,3),_RtmpNextHop_Type())
rtmpNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpNextHop.setStatus(_A)
class _RtmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_c,2),(_Q,3),(_R,4)))
_RtmpType_Type.__name__=_D
_RtmpType_Object=MibTableColumn
rtmpType=_RtmpType_Object((1,3,6,1,2,1,13,5,1,1,4),_RtmpType_Type())
rtmpType.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpType.setStatus(_A)
_RtmpPort_Type=Integer32
_RtmpPort_Object=MibTableColumn
rtmpPort=_RtmpPort_Object((1,3,6,1,2,1,13,5,1,1,5),_RtmpPort_Type())
rtmpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpPort.setStatus(_A)
_RtmpHops_Type=Integer32
_RtmpHops_Object=MibTableColumn
rtmpHops=_RtmpHops_Object((1,3,6,1,2,1,13,5,1,1,6),_RtmpHops_Type())
rtmpHops.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpHops.setStatus(_A)
class _RtmpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('good',1),('suspect',2),('badZero',3),('badOne',4),(_F,5)))
_RtmpState_Type.__name__=_D
_RtmpState_Object=MibTableColumn
rtmpState=_RtmpState_Object((1,3,6,1,2,1,13,5,1,1,7),_RtmpState_Type())
rtmpState.setMaxAccess(_C)
if mibBuilder.loadTexts:rtmpState.setStatus(_A)
_RtmpInDataPkts_Type=Counter32
_RtmpInDataPkts_Object=MibScalar
rtmpInDataPkts=_RtmpInDataPkts_Object((1,3,6,1,2,1,13,5,2),_RtmpInDataPkts_Type())
rtmpInDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpInDataPkts.setStatus(_A)
_RtmpOutDataPkts_Type=Counter32
_RtmpOutDataPkts_Object=MibScalar
rtmpOutDataPkts=_RtmpOutDataPkts_Object((1,3,6,1,2,1,13,5,3),_RtmpOutDataPkts_Type())
rtmpOutDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpOutDataPkts.setStatus(_A)
_RtmpInRequestPkts_Type=Counter32
_RtmpInRequestPkts_Object=MibScalar
rtmpInRequestPkts=_RtmpInRequestPkts_Object((1,3,6,1,2,1,13,5,4),_RtmpInRequestPkts_Type())
rtmpInRequestPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpInRequestPkts.setStatus(_A)
_RtmpNextIREqualChanges_Type=Counter32
_RtmpNextIREqualChanges_Object=MibScalar
rtmpNextIREqualChanges=_RtmpNextIREqualChanges_Object((1,3,6,1,2,1,13,5,5),_RtmpNextIREqualChanges_Type())
rtmpNextIREqualChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpNextIREqualChanges.setStatus(_A)
_RtmpNextIRLessChanges_Type=Counter32
_RtmpNextIRLessChanges_Object=MibScalar
rtmpNextIRLessChanges=_RtmpNextIRLessChanges_Object((1,3,6,1,2,1,13,5,6),_RtmpNextIRLessChanges_Type())
rtmpNextIRLessChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpNextIRLessChanges.setStatus(_A)
_RtmpRouteDeletes_Type=Counter32
_RtmpRouteDeletes_Object=MibScalar
rtmpRouteDeletes=_RtmpRouteDeletes_Object((1,3,6,1,2,1,13,5,7),_RtmpRouteDeletes_Type())
rtmpRouteDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpRouteDeletes.setStatus(_A)
_RtmpRoutingTableOverflows_Type=Counter32
_RtmpRoutingTableOverflows_Object=MibScalar
rtmpRoutingTableOverflows=_RtmpRoutingTableOverflows_Object((1,3,6,1,2,1,13,5,8),_RtmpRoutingTableOverflows_Type())
rtmpRoutingTableOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpRoutingTableOverflows.setStatus(_A)
_Kip_ObjectIdentity=ObjectIdentity
kip=_Kip_ObjectIdentity((1,3,6,1,2,1,13,6))
_KipTable_Object=MibTable
kipTable=_KipTable_Object((1,3,6,1,2,1,13,6,1))
if mibBuilder.loadTexts:kipTable.setStatus(_A)
_KipEntry_Object=MibTableRow
kipEntry=_KipEntry_Object((1,3,6,1,2,1,13,6,1,1))
kipEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:kipEntry.setStatus(_A)
_KipNetStart_Type=ATNetworkNumber
_KipNetStart_Object=MibTableColumn
kipNetStart=_KipNetStart_Object((1,3,6,1,2,1,13,6,1,1,1),_KipNetStart_Type())
kipNetStart.setMaxAccess(_B)
if mibBuilder.loadTexts:kipNetStart.setStatus(_A)
_KipNetEnd_Type=ATNetworkNumber
_KipNetEnd_Object=MibTableColumn
kipNetEnd=_KipNetEnd_Object((1,3,6,1,2,1,13,6,1,1,2),_KipNetEnd_Type())
kipNetEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:kipNetEnd.setStatus(_A)
_KipNextHop_Type=IpAddress
_KipNextHop_Object=MibTableColumn
kipNextHop=_KipNextHop_Object((1,3,6,1,2,1,13,6,1,1,3),_KipNextHop_Type())
kipNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:kipNextHop.setStatus(_A)
_KipHopCount_Type=Integer32
_KipHopCount_Object=MibTableColumn
kipHopCount=_KipHopCount_Object((1,3,6,1,2,1,13,6,1,1,4),_KipHopCount_Type())
kipHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:kipHopCount.setStatus(_A)
_KipBCastAddr_Type=IpAddress
_KipBCastAddr_Object=MibTableColumn
kipBCastAddr=_KipBCastAddr_Object((1,3,6,1,2,1,13,6,1,1,5),_KipBCastAddr_Type())
kipBCastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:kipBCastAddr.setStatus(_A)
class _KipCore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('core',1),('notcore',2)))
_KipCore_Type.__name__=_D
_KipCore_Object=MibTableColumn
kipCore=_KipCore_Object((1,3,6,1,2,1,13,6,1,1,6),_KipCore_Type())
kipCore.setMaxAccess(_C)
if mibBuilder.loadTexts:kipCore.setStatus(_A)
class _KipType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kipRouter',1),('net',2),('host',3),(_K,4),('async',5)))
_KipType_Type.__name__=_D
_KipType_Object=MibTableColumn
kipType=_KipType_Object((1,3,6,1,2,1,13,6,1,1,7),_KipType_Type())
kipType.setMaxAccess(_C)
if mibBuilder.loadTexts:kipType.setStatus(_A)
class _KipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('configured',1),('learned',2),(_F,3)))
_KipState_Type.__name__=_D
_KipState_Object=MibTableColumn
kipState=_KipState_Object((1,3,6,1,2,1,13,6,1,1,8),_KipState_Type())
kipState.setMaxAccess(_C)
if mibBuilder.loadTexts:kipState.setStatus(_A)
class _KipShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shared',1),('private',2)))
_KipShare_Type.__name__=_D
_KipShare_Object=MibTableColumn
kipShare=_KipShare_Object((1,3,6,1,2,1,13,6,1,1,9),_KipShare_Type())
kipShare.setMaxAccess(_C)
if mibBuilder.loadTexts:kipShare.setStatus(_A)
_KipFrom_Type=IpAddress
_KipFrom_Object=MibTableColumn
kipFrom=_KipFrom_Object((1,3,6,1,2,1,13,6,1,1,10),_KipFrom_Type())
kipFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:kipFrom.setStatus(_A)
_ZipRouter_ObjectIdentity=ObjectIdentity
zipRouter=_ZipRouter_ObjectIdentity((1,3,6,1,2,1,13,7))
_ZipTable_Object=MibTable
zipTable=_ZipTable_Object((1,3,6,1,2,1,13,7,1))
if mibBuilder.loadTexts:zipTable.setStatus(_A)
_ZipEntry_Object=MibTableRow
zipEntry=_ZipEntry_Object((1,3,6,1,2,1,13,7,1,1))
zipEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:zipEntry.setStatus(_A)
_ZipZoneName_Type=ATName
_ZipZoneName_Object=MibTableColumn
zipZoneName=_ZipZoneName_Object((1,3,6,1,2,1,13,7,1,1,1),_ZipZoneName_Type())
zipZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneName.setStatus(_A)
_ZipZoneIndex_Type=Integer32
_ZipZoneIndex_Object=MibTableColumn
zipZoneIndex=_ZipZoneIndex_Object((1,3,6,1,2,1,13,7,1,1,2),_ZipZoneIndex_Type())
zipZoneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneIndex.setStatus(_A)
_ZipZoneNetStart_Type=ATNetworkNumber
_ZipZoneNetStart_Object=MibTableColumn
zipZoneNetStart=_ZipZoneNetStart_Object((1,3,6,1,2,1,13,7,1,1,3),_ZipZoneNetStart_Type())
zipZoneNetStart.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneNetStart.setStatus(_A)
_ZipZoneNetEnd_Type=ATNetworkNumber
_ZipZoneNetEnd_Object=MibTableColumn
zipZoneNetEnd=_ZipZoneNetEnd_Object((1,3,6,1,2,1,13,7,1,1,4),_ZipZoneNetEnd_Type())
zipZoneNetEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneNetEnd.setStatus(_A)
class _ZipZoneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_ZipZoneState_Type.__name__=_D
_ZipZoneState_Object=MibTableColumn
zipZoneState=_ZipZoneState_Object((1,3,6,1,2,1,13,7,1,1,5),_ZipZoneState_Type())
zipZoneState.setMaxAccess(_C)
if mibBuilder.loadTexts:zipZoneState.setStatus(_A)
_ZipZoneFrom_Type=OctetString
_ZipZoneFrom_Object=MibTableColumn
zipZoneFrom=_ZipZoneFrom_Object((1,3,6,1,2,1,13,7,1,1,6),_ZipZoneFrom_Type())
zipZoneFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneFrom.setStatus(_A)
_ZipZonePort_Type=Integer32
_ZipZonePort_Object=MibTableColumn
zipZonePort=_ZipZonePort_Object((1,3,6,1,2,1,13,7,1,1,7),_ZipZonePort_Type())
zipZonePort.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZonePort.setStatus(_A)
_ZipInZipQueries_Type=Counter32
_ZipInZipQueries_Object=MibScalar
zipInZipQueries=_ZipInZipQueries_Object((1,3,6,1,2,1,13,7,2),_ZipInZipQueries_Type())
zipInZipQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInZipQueries.setStatus(_A)
_ZipInZipReplies_Type=Counter32
_ZipInZipReplies_Object=MibScalar
zipInZipReplies=_ZipInZipReplies_Object((1,3,6,1,2,1,13,7,3),_ZipInZipReplies_Type())
zipInZipReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInZipReplies.setStatus(_A)
_ZipInZipExtendedReplies_Type=Counter32
_ZipInZipExtendedReplies_Object=MibScalar
zipInZipExtendedReplies=_ZipInZipExtendedReplies_Object((1,3,6,1,2,1,13,7,4),_ZipInZipExtendedReplies_Type())
zipInZipExtendedReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInZipExtendedReplies.setStatus(_A)
_ZipZoneConflictErrors_Type=Counter32
_ZipZoneConflictErrors_Object=MibScalar
zipZoneConflictErrors=_ZipZoneConflictErrors_Object((1,3,6,1,2,1,13,7,5),_ZipZoneConflictErrors_Type())
zipZoneConflictErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneConflictErrors.setStatus(_A)
_ZipInObsoletes_Type=Counter32
_ZipInObsoletes_Object=MibScalar
zipInObsoletes=_ZipInObsoletes_Object((1,3,6,1,2,1,13,7,6),_ZipInObsoletes_Type())
zipInObsoletes.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInObsoletes.setStatus(_A)
_ZipRouterNetInfoTable_Object=MibTable
zipRouterNetInfoTable=_ZipRouterNetInfoTable_Object((1,3,6,1,2,1,13,7,7))
if mibBuilder.loadTexts:zipRouterNetInfoTable.setStatus(_A)
_ZipRouterNetInfoEntry_Object=MibTableRow
zipRouterNetInfoEntry=_ZipRouterNetInfoEntry_Object((1,3,6,1,2,1,13,7,7,1))
zipRouterNetInfoEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:zipRouterNetInfoEntry.setStatus(_A)
_ZipInGetNetInfos_Type=Counter32
_ZipInGetNetInfos_Object=MibTableColumn
zipInGetNetInfos=_ZipInGetNetInfos_Object((1,3,6,1,2,1,13,7,7,1,1),_ZipInGetNetInfos_Type())
zipInGetNetInfos.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInGetNetInfos.setStatus(_A)
_ZipOutGetNetInfoReplies_Type=Counter32
_ZipOutGetNetInfoReplies_Object=MibTableColumn
zipOutGetNetInfoReplies=_ZipOutGetNetInfoReplies_Object((1,3,6,1,2,1,13,7,7,1,2),_ZipOutGetNetInfoReplies_Type())
zipOutGetNetInfoReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:zipOutGetNetInfoReplies.setStatus(_A)
_ZipZoneOutInvalids_Type=Counter32
_ZipZoneOutInvalids_Object=MibTableColumn
zipZoneOutInvalids=_ZipZoneOutInvalids_Object((1,3,6,1,2,1,13,7,7,1,3),_ZipZoneOutInvalids_Type())
zipZoneOutInvalids.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneOutInvalids.setStatus(_A)
_ZipAddressInvalids_Type=Counter32
_ZipAddressInvalids_Object=MibTableColumn
zipAddressInvalids=_ZipAddressInvalids_Object((1,3,6,1,2,1,13,7,7,1,4),_ZipAddressInvalids_Type())
zipAddressInvalids.setMaxAccess(_B)
if mibBuilder.loadTexts:zipAddressInvalids.setStatus(_A)
_Nbp_ObjectIdentity=ObjectIdentity
nbp=_Nbp_ObjectIdentity((1,3,6,1,2,1,13,8))
_NbpTable_Object=MibTable
nbpTable=_NbpTable_Object((1,3,6,1,2,1,13,8,1))
if mibBuilder.loadTexts:nbpTable.setStatus(_A)
_NbpEntry_Object=MibTableRow
nbpEntry=_NbpEntry_Object((1,3,6,1,2,1,13,8,1,1))
nbpEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:nbpEntry.setStatus(_A)
_NbpIndex_Type=Integer32
_NbpIndex_Object=MibTableColumn
nbpIndex=_NbpIndex_Object((1,3,6,1,2,1,13,8,1,1,1),_NbpIndex_Type())
nbpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbpIndex.setStatus(_A)
class _NbpObject_Type(ATName):subtypeSpec=ATName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NbpObject_Type.__name__=_L
_NbpObject_Object=MibTableColumn
nbpObject=_NbpObject_Object((1,3,6,1,2,1,13,8,1,1,2),_NbpObject_Type())
nbpObject.setMaxAccess(_C)
if mibBuilder.loadTexts:nbpObject.setStatus(_A)
class _NbpType_Type(ATName):subtypeSpec=ATName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NbpType_Type.__name__=_L
_NbpType_Object=MibTableColumn
nbpType=_NbpType_Object((1,3,6,1,2,1,13,8,1,1,3),_NbpType_Type())
nbpType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbpType.setStatus(_A)
_NbpZone_Type=ATName
_NbpZone_Object=MibTableColumn
nbpZone=_NbpZone_Object((1,3,6,1,2,1,13,8,1,1,4),_NbpZone_Type())
nbpZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nbpZone.setStatus(_A)
class _NbpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('registering',2),('registrationFailed',3),(_F,4)))
_NbpState_Type.__name__=_D
_NbpState_Object=MibTableColumn
nbpState=_NbpState_Object((1,3,6,1,2,1,13,8,1,1,5),_NbpState_Type())
nbpState.setMaxAccess(_C)
if mibBuilder.loadTexts:nbpState.setStatus(_A)
_NbpAddress_Type=DdpSocketAddress
_NbpAddress_Object=MibTableColumn
nbpAddress=_NbpAddress_Object((1,3,6,1,2,1,13,8,1,1,6),_NbpAddress_Type())
nbpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbpAddress.setStatus(_A)
class _NbpEnumerator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NbpEnumerator_Type.__name__=_D
_NbpEnumerator_Object=MibTableColumn
nbpEnumerator=_NbpEnumerator_Object((1,3,6,1,2,1,13,8,1,1,7),_NbpEnumerator_Type())
nbpEnumerator.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpEnumerator.setStatus(_A)
_NbpInLookUpRequests_Type=Counter32
_NbpInLookUpRequests_Object=MibScalar
nbpInLookUpRequests=_NbpInLookUpRequests_Object((1,3,6,1,2,1,13,8,2),_NbpInLookUpRequests_Type())
nbpInLookUpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpInLookUpRequests.setStatus(_A)
_NbpInLookUpReplies_Type=Counter32
_NbpInLookUpReplies_Object=MibScalar
nbpInLookUpReplies=_NbpInLookUpReplies_Object((1,3,6,1,2,1,13,8,3),_NbpInLookUpReplies_Type())
nbpInLookUpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpInLookUpReplies.setStatus(_A)
_NbpInBroadcastRequests_Type=Counter32
_NbpInBroadcastRequests_Object=MibScalar
nbpInBroadcastRequests=_NbpInBroadcastRequests_Object((1,3,6,1,2,1,13,8,4),_NbpInBroadcastRequests_Type())
nbpInBroadcastRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpInBroadcastRequests.setStatus(_A)
_NbpInForwardRequests_Type=Counter32
_NbpInForwardRequests_Object=MibScalar
nbpInForwardRequests=_NbpInForwardRequests_Object((1,3,6,1,2,1,13,8,5),_NbpInForwardRequests_Type())
nbpInForwardRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpInForwardRequests.setStatus(_A)
_NbpOutLookUpReplies_Type=Counter32
_NbpOutLookUpReplies_Object=MibScalar
nbpOutLookUpReplies=_NbpOutLookUpReplies_Object((1,3,6,1,2,1,13,8,6),_NbpOutLookUpReplies_Type())
nbpOutLookUpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpOutLookUpReplies.setStatus(_A)
_NbpRegistrationFailures_Type=Counter32
_NbpRegistrationFailures_Object=MibScalar
nbpRegistrationFailures=_NbpRegistrationFailures_Object((1,3,6,1,2,1,13,8,7),_NbpRegistrationFailures_Type())
nbpRegistrationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpRegistrationFailures.setStatus(_A)
_NbpInErrors_Type=Counter32
_NbpInErrors_Object=MibScalar
nbpInErrors=_NbpInErrors_Object((1,3,6,1,2,1,13,8,8),_NbpInErrors_Type())
nbpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:nbpInErrors.setStatus(_A)
_Atecho_ObjectIdentity=ObjectIdentity
atecho=_Atecho_ObjectIdentity((1,3,6,1,2,1,13,9))
_AtechoRequests_Type=Counter32
_AtechoRequests_Object=MibScalar
atechoRequests=_AtechoRequests_Object((1,3,6,1,2,1,13,9,1),_AtechoRequests_Type())
atechoRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:atechoRequests.setStatus(_A)
_AtechoReplies_Type=Counter32
_AtechoReplies_Object=MibScalar
atechoReplies=_AtechoReplies_Object((1,3,6,1,2,1,13,9,2),_AtechoReplies_Type())
atechoReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:atechoReplies.setStatus(_A)
_AtechoOutRequests_Type=Counter32
_AtechoOutRequests_Object=MibScalar
atechoOutRequests=_AtechoOutRequests_Object((1,3,6,1,2,1,13,9,3),_AtechoOutRequests_Type())
atechoOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:atechoOutRequests.setStatus(_A)
_AtechoInReplies_Type=Counter32
_AtechoInReplies_Object=MibScalar
atechoInReplies=_AtechoInReplies_Object((1,3,6,1,2,1,13,9,4),_AtechoInReplies_Type())
atechoInReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:atechoInReplies.setStatus(_A)
_Atp_ObjectIdentity=ObjectIdentity
atp=_Atp_ObjectIdentity((1,3,6,1,2,1,13,10))
_AtpInPkts_Type=Counter32
_AtpInPkts_Object=MibScalar
atpInPkts=_AtpInPkts_Object((1,3,6,1,2,1,13,10,1),_AtpInPkts_Type())
atpInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atpInPkts.setStatus(_A)
_AtpOutPkts_Type=Counter32
_AtpOutPkts_Object=MibScalar
atpOutPkts=_AtpOutPkts_Object((1,3,6,1,2,1,13,10,2),_AtpOutPkts_Type())
atpOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atpOutPkts.setStatus(_A)
_AtpTRequestRetransmissions_Type=Counter32
_AtpTRequestRetransmissions_Object=MibScalar
atpTRequestRetransmissions=_AtpTRequestRetransmissions_Object((1,3,6,1,2,1,13,10,3),_AtpTRequestRetransmissions_Type())
atpTRequestRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:atpTRequestRetransmissions.setStatus(_A)
_AtpTResponseRetransmissions_Type=Counter32
_AtpTResponseRetransmissions_Object=MibScalar
atpTResponseRetransmissions=_AtpTResponseRetransmissions_Object((1,3,6,1,2,1,13,10,4),_AtpTResponseRetransmissions_Type())
atpTResponseRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:atpTResponseRetransmissions.setStatus(_A)
_AtpReleaseTimerExpiredCounts_Type=Counter32
_AtpReleaseTimerExpiredCounts_Object=MibScalar
atpReleaseTimerExpiredCounts=_AtpReleaseTimerExpiredCounts_Object((1,3,6,1,2,1,13,10,5),_AtpReleaseTimerExpiredCounts_Type())
atpReleaseTimerExpiredCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:atpReleaseTimerExpiredCounts.setStatus(_A)
_AtpRetryCountExceededs_Type=Counter32
_AtpRetryCountExceededs_Object=MibScalar
atpRetryCountExceededs=_AtpRetryCountExceededs_Object((1,3,6,1,2,1,13,10,6),_AtpRetryCountExceededs_Type())
atpRetryCountExceededs.setMaxAccess(_B)
if mibBuilder.loadTexts:atpRetryCountExceededs.setStatus(_A)
_AtpListenerTable_Object=MibTable
atpListenerTable=_AtpListenerTable_Object((1,3,6,1,2,1,13,10,7))
if mibBuilder.loadTexts:atpListenerTable.setStatus(_A)
_AtpListenerEntry_Object=MibTableRow
atpListenerEntry=_AtpListenerEntry_Object((1,3,6,1,2,1,13,10,7,1))
atpListenerEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:atpListenerEntry.setStatus(_A)
_AtpListenerAddress_Type=DdpSocketAddress
_AtpListenerAddress_Object=MibTableColumn
atpListenerAddress=_AtpListenerAddress_Object((1,3,6,1,2,1,13,10,7,1,1),_AtpListenerAddress_Type())
atpListenerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:atpListenerAddress.setStatus(_A)
class _AtpListenerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_AtpListenerStatus_Type.__name__=_D
_AtpListenerStatus_Object=MibTableColumn
atpListenerStatus=_AtpListenerStatus_Object((1,3,6,1,2,1,13,10,7,1,2),_AtpListenerStatus_Type())
atpListenerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atpListenerStatus.setStatus(_A)
_Pap_ObjectIdentity=ObjectIdentity
pap=_Pap_ObjectIdentity((1,3,6,1,2,1,13,11))
_PapInOpenConns_Type=Counter32
_PapInOpenConns_Object=MibScalar
papInOpenConns=_PapInOpenConns_Object((1,3,6,1,2,1,13,11,1),_PapInOpenConns_Type())
papInOpenConns.setMaxAccess(_B)
if mibBuilder.loadTexts:papInOpenConns.setStatus(_A)
_PapOutOpenConns_Type=Counter32
_PapOutOpenConns_Object=MibScalar
papOutOpenConns=_PapOutOpenConns_Object((1,3,6,1,2,1,13,11,2),_PapOutOpenConns_Type())
papOutOpenConns.setMaxAccess(_B)
if mibBuilder.loadTexts:papOutOpenConns.setStatus(_A)
_PapInDatas_Type=Counter32
_PapInDatas_Object=MibScalar
papInDatas=_PapInDatas_Object((1,3,6,1,2,1,13,11,3),_PapInDatas_Type())
papInDatas.setMaxAccess(_B)
if mibBuilder.loadTexts:papInDatas.setStatus(_A)
_PapOutDatas_Type=Counter32
_PapOutDatas_Object=MibScalar
papOutDatas=_PapOutDatas_Object((1,3,6,1,2,1,13,11,4),_PapOutDatas_Type())
papOutDatas.setMaxAccess(_B)
if mibBuilder.loadTexts:papOutDatas.setStatus(_A)
_PapInCloseConns_Type=Counter32
_PapInCloseConns_Object=MibScalar
papInCloseConns=_PapInCloseConns_Object((1,3,6,1,2,1,13,11,5),_PapInCloseConns_Type())
papInCloseConns.setMaxAccess(_B)
if mibBuilder.loadTexts:papInCloseConns.setStatus(_A)
_PapOutCloseConns_Type=Counter32
_PapOutCloseConns_Object=MibScalar
papOutCloseConns=_PapOutCloseConns_Object((1,3,6,1,2,1,13,11,6),_PapOutCloseConns_Type())
papOutCloseConns.setMaxAccess(_B)
if mibBuilder.loadTexts:papOutCloseConns.setStatus(_A)
_PapTickleTimeoutCloses_Type=Counter32
_PapTickleTimeoutCloses_Object=MibScalar
papTickleTimeoutCloses=_PapTickleTimeoutCloses_Object((1,3,6,1,2,1,13,11,7),_PapTickleTimeoutCloses_Type())
papTickleTimeoutCloses.setMaxAccess(_B)
if mibBuilder.loadTexts:papTickleTimeoutCloses.setStatus(_A)
_PapServerTable_Object=MibTable
papServerTable=_PapServerTable_Object((1,3,6,1,2,1,13,11,8))
if mibBuilder.loadTexts:papServerTable.setStatus(_A)
_PapServerEntry_Object=MibTableRow
papServerEntry=_PapServerEntry_Object((1,3,6,1,2,1,13,11,8,1))
papServerEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:papServerEntry.setStatus(_A)
_PapServerIndex_Type=Integer32
_PapServerIndex_Object=MibTableColumn
papServerIndex=_PapServerIndex_Object((1,3,6,1,2,1,13,11,8,1,1),_PapServerIndex_Type())
papServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:papServerIndex.setStatus(_A)
_PapServerListeningSocket_Type=DdpSocketAddress
_PapServerListeningSocket_Object=MibTableColumn
papServerListeningSocket=_PapServerListeningSocket_Object((1,3,6,1,2,1,13,11,8,1,2),_PapServerListeningSocket_Type())
papServerListeningSocket.setMaxAccess(_C)
if mibBuilder.loadTexts:papServerListeningSocket.setStatus(_A)
_PapServerStatus_Type=DisplayString
_PapServerStatus_Object=MibTableColumn
papServerStatus=_PapServerStatus_Object((1,3,6,1,2,1,13,11,8,1,3),_PapServerStatus_Type())
papServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerStatus.setStatus(_A)
_PapServerCompletedJobs_Type=Counter32
_PapServerCompletedJobs_Object=MibTableColumn
papServerCompletedJobs=_PapServerCompletedJobs_Object((1,3,6,1,2,1,13,11,8,1,4),_PapServerCompletedJobs_Type())
papServerCompletedJobs.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerCompletedJobs.setStatus(_A)
_PapServerBusyJobs_Type=Integer32
_PapServerBusyJobs_Object=MibTableColumn
papServerBusyJobs=_PapServerBusyJobs_Object((1,3,6,1,2,1,13,11,8,1,5),_PapServerBusyJobs_Type())
papServerBusyJobs.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerBusyJobs.setStatus(_A)
_PapServerFreeJobs_Type=Integer32
_PapServerFreeJobs_Object=MibTableColumn
papServerFreeJobs=_PapServerFreeJobs_Object((1,3,6,1,2,1,13,11,8,1,6),_PapServerFreeJobs_Type())
papServerFreeJobs.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerFreeJobs.setStatus(_A)
_PapServerAuthenticationFailures_Type=Counter32
_PapServerAuthenticationFailures_Object=MibTableColumn
papServerAuthenticationFailures=_PapServerAuthenticationFailures_Object((1,3,6,1,2,1,13,11,8,1,7),_PapServerAuthenticationFailures_Type())
papServerAuthenticationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerAuthenticationFailures.setStatus(_A)
_PapServerAccountingFailures_Type=Counter32
_PapServerAccountingFailures_Object=MibTableColumn
papServerAccountingFailures=_PapServerAccountingFailures_Object((1,3,6,1,2,1,13,11,8,1,8),_PapServerAccountingFailures_Type())
papServerAccountingFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerAccountingFailures.setStatus(_A)
_PapServerGeneralFailures_Type=Counter32
_PapServerGeneralFailures_Object=MibTableColumn
papServerGeneralFailures=_PapServerGeneralFailures_Object((1,3,6,1,2,1,13,11,8,1,9),_PapServerGeneralFailures_Type())
papServerGeneralFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerGeneralFailures.setStatus(_A)
class _PapServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_PapServerState_Type.__name__=_D
_PapServerState_Object=MibTableColumn
papServerState=_PapServerState_Object((1,3,6,1,2,1,13,11,8,1,10),_PapServerState_Type())
papServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:papServerState.setStatus(_A)
_PapServerLastStatusMsg_Type=DisplayString
_PapServerLastStatusMsg_Object=MibTableColumn
papServerLastStatusMsg=_PapServerLastStatusMsg_Object((1,3,6,1,2,1,13,11,8,1,11),_PapServerLastStatusMsg_Type())
papServerLastStatusMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:papServerLastStatusMsg.setStatus(_A)
_Asp_ObjectIdentity=ObjectIdentity
asp=_Asp_ObjectIdentity((1,3,6,1,2,1,13,12))
_AspInputTransactions_Type=Counter32
_AspInputTransactions_Object=MibScalar
aspInputTransactions=_AspInputTransactions_Object((1,3,6,1,2,1,13,12,1),_AspInputTransactions_Type())
aspInputTransactions.setMaxAccess(_B)
if mibBuilder.loadTexts:aspInputTransactions.setStatus(_A)
_AspOutputTransactions_Type=Counter32
_AspOutputTransactions_Object=MibScalar
aspOutputTransactions=_AspOutputTransactions_Object((1,3,6,1,2,1,13,12,2),_AspOutputTransactions_Type())
aspOutputTransactions.setMaxAccess(_B)
if mibBuilder.loadTexts:aspOutputTransactions.setStatus(_A)
_AspInOpenSessions_Type=Counter32
_AspInOpenSessions_Object=MibScalar
aspInOpenSessions=_AspInOpenSessions_Object((1,3,6,1,2,1,13,12,3),_AspInOpenSessions_Type())
aspInOpenSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:aspInOpenSessions.setStatus(_A)
_AspOutOpenSessions_Type=Counter32
_AspOutOpenSessions_Object=MibScalar
aspOutOpenSessions=_AspOutOpenSessions_Object((1,3,6,1,2,1,13,12,4),_AspOutOpenSessions_Type())
aspOutOpenSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:aspOutOpenSessions.setStatus(_A)
_AspInCloseSessions_Type=Counter32
_AspInCloseSessions_Object=MibScalar
aspInCloseSessions=_AspInCloseSessions_Object((1,3,6,1,2,1,13,12,5),_AspInCloseSessions_Type())
aspInCloseSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:aspInCloseSessions.setStatus(_A)
_AspOutCloseSessions_Type=Counter32
_AspOutCloseSessions_Object=MibScalar
aspOutCloseSessions=_AspOutCloseSessions_Object((1,3,6,1,2,1,13,12,6),_AspOutCloseSessions_Type())
aspOutCloseSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:aspOutCloseSessions.setStatus(_A)
_AspNoMoreSessionsErrors_Type=Counter32
_AspNoMoreSessionsErrors_Object=MibScalar
aspNoMoreSessionsErrors=_AspNoMoreSessionsErrors_Object((1,3,6,1,2,1,13,12,7),_AspNoMoreSessionsErrors_Type())
aspNoMoreSessionsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:aspNoMoreSessionsErrors.setStatus(_A)
_AspTickleTimeOutCloses_Type=Counter32
_AspTickleTimeOutCloses_Object=MibScalar
aspTickleTimeOutCloses=_AspTickleTimeOutCloses_Object((1,3,6,1,2,1,13,12,8),_AspTickleTimeOutCloses_Type())
aspTickleTimeOutCloses.setMaxAccess(_B)
if mibBuilder.loadTexts:aspTickleTimeOutCloses.setStatus(_A)
_AspConnTable_Object=MibTable
aspConnTable=_AspConnTable_Object((1,3,6,1,2,1,13,12,9))
if mibBuilder.loadTexts:aspConnTable.setStatus(_A)
_AspConnEntry_Object=MibTableRow
aspConnEntry=_AspConnEntry_Object((1,3,6,1,2,1,13,12,9,1))
aspConnEntry.setIndexNames((0,_E,_j),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:aspConnEntry.setStatus(_A)
_AspConnLocalAddress_Type=DdpSocketAddress
_AspConnLocalAddress_Object=MibTableColumn
aspConnLocalAddress=_AspConnLocalAddress_Object((1,3,6,1,2,1,13,12,9,1,1),_AspConnLocalAddress_Type())
aspConnLocalAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:aspConnLocalAddress.setStatus(_A)
_AspConnRemoteAddress_Type=DdpSocketAddress
_AspConnRemoteAddress_Object=MibTableColumn
aspConnRemoteAddress=_AspConnRemoteAddress_Object((1,3,6,1,2,1,13,12,9,1,2),_AspConnRemoteAddress_Type())
aspConnRemoteAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:aspConnRemoteAddress.setStatus(_A)
class _AspConnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AspConnID_Type.__name__=_D
_AspConnID_Object=MibTableColumn
aspConnID=_AspConnID_Object((1,3,6,1,2,1,13,12,9,1,3),_AspConnID_Type())
aspConnID.setMaxAccess(_G)
if mibBuilder.loadTexts:aspConnID.setStatus(_A)
class _AspConnLastReqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AspConnLastReqNum_Type.__name__=_D
_AspConnLastReqNum_Object=MibTableColumn
aspConnLastReqNum=_AspConnLastReqNum_Object((1,3,6,1,2,1,13,12,9,1,4),_AspConnLastReqNum_Type())
aspConnLastReqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:aspConnLastReqNum.setStatus(_A)
class _AspConnServerEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sss',1),('wss',2),('sls',3)))
_AspConnServerEnd_Type.__name__=_D
_AspConnServerEnd_Object=MibTableColumn
aspConnServerEnd=_AspConnServerEnd_Object((1,3,6,1,2,1,13,12,9,1,5),_AspConnServerEnd_Type())
aspConnServerEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aspConnServerEnd.setStatus(_A)
class _AspConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),(_m,2),(_F,3)))
_AspConnState_Type.__name__=_D
_AspConnState_Object=MibTableColumn
aspConnState=_AspConnState_Object((1,3,6,1,2,1,13,12,9,1,6),_AspConnState_Type())
aspConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:aspConnState.setStatus(_A)
_Adsp_ObjectIdentity=ObjectIdentity
adsp=_Adsp_ObjectIdentity((1,3,6,1,2,1,13,13))
_AdspInPkts_Type=Counter32
_AdspInPkts_Object=MibScalar
adspInPkts=_AdspInPkts_Object((1,3,6,1,2,1,13,13,1),_AdspInPkts_Type())
adspInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adspInPkts.setStatus(_A)
_AdspOutPkts_Type=Counter32
_AdspOutPkts_Object=MibScalar
adspOutPkts=_AdspOutPkts_Object((1,3,6,1,2,1,13,13,2),_AdspOutPkts_Type())
adspOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adspOutPkts.setStatus(_A)
_AdspInOctets_Type=Counter32
_AdspInOctets_Object=MibScalar
adspInOctets=_AdspInOctets_Object((1,3,6,1,2,1,13,13,3),_AdspInOctets_Type())
adspInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adspInOctets.setStatus(_A)
_AdspOutOctets_Type=Counter32
_AdspOutOctets_Object=MibScalar
adspOutOctets=_AdspOutOctets_Object((1,3,6,1,2,1,13,13,4),_AdspOutOctets_Type())
adspOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adspOutOctets.setStatus(_A)
_AdspInDataPkts_Type=Counter32
_AdspInDataPkts_Object=MibScalar
adspInDataPkts=_AdspInDataPkts_Object((1,3,6,1,2,1,13,13,5),_AdspInDataPkts_Type())
adspInDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adspInDataPkts.setStatus(_A)
_AdspOutDataPkts_Type=Counter32
_AdspOutDataPkts_Object=MibScalar
adspOutDataPkts=_AdspOutDataPkts_Object((1,3,6,1,2,1,13,13,6),_AdspOutDataPkts_Type())
adspOutDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adspOutDataPkts.setStatus(_A)
_AdspTimeoutErrors_Type=Counter32
_AdspTimeoutErrors_Object=MibScalar
adspTimeoutErrors=_AdspTimeoutErrors_Object((1,3,6,1,2,1,13,13,7),_AdspTimeoutErrors_Type())
adspTimeoutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adspTimeoutErrors.setStatus(_A)
_AdspTimeoutCloseErrors_Type=Counter32
_AdspTimeoutCloseErrors_Object=MibScalar
adspTimeoutCloseErrors=_AdspTimeoutCloseErrors_Object((1,3,6,1,2,1,13,13,8),_AdspTimeoutCloseErrors_Type())
adspTimeoutCloseErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adspTimeoutCloseErrors.setStatus(_A)
_AdspConnTable_Object=MibTable
adspConnTable=_AdspConnTable_Object((1,3,6,1,2,1,13,13,9))
if mibBuilder.loadTexts:adspConnTable.setStatus(_A)
_AdspConnEntry_Object=MibTableRow
adspConnEntry=_AdspConnEntry_Object((1,3,6,1,2,1,13,13,9,1))
adspConnEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:adspConnEntry.setStatus(_A)
_AdspConnLocalAddress_Type=DdpSocketAddress
_AdspConnLocalAddress_Object=MibTableColumn
adspConnLocalAddress=_AdspConnLocalAddress_Object((1,3,6,1,2,1,13,13,9,1,1),_AdspConnLocalAddress_Type())
adspConnLocalAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:adspConnLocalAddress.setStatus(_A)
class _AdspConnLocalConnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdspConnLocalConnID_Type.__name__=_D
_AdspConnLocalConnID_Object=MibTableColumn
adspConnLocalConnID=_AdspConnLocalConnID_Object((1,3,6,1,2,1,13,13,9,1,2),_AdspConnLocalConnID_Type())
adspConnLocalConnID.setMaxAccess(_G)
if mibBuilder.loadTexts:adspConnLocalConnID.setStatus(_A)
_AdspConnRemoteAddress_Type=DdpSocketAddress
_AdspConnRemoteAddress_Object=MibTableColumn
adspConnRemoteAddress=_AdspConnRemoteAddress_Object((1,3,6,1,2,1,13,13,9,1,3),_AdspConnRemoteAddress_Type())
adspConnRemoteAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:adspConnRemoteAddress.setStatus(_A)
class _AdspConnRemoteConnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdspConnRemoteConnID_Type.__name__=_D
_AdspConnRemoteConnID_Object=MibTableColumn
adspConnRemoteConnID=_AdspConnRemoteConnID_Object((1,3,6,1,2,1,13,13,9,1,4),_AdspConnRemoteConnID_Type())
adspConnRemoteConnID.setMaxAccess(_B)
if mibBuilder.loadTexts:adspConnRemoteConnID.setStatus(_A)
class _AdspConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('open',1),('localHalfOpen',2),('remoteHalfOpen',3),('listening',4),(_m,5),(_F,6)))
_AdspConnState_Type.__name__=_D
_AdspConnState_Object=MibTableColumn
adspConnState=_AdspConnState_Object((1,3,6,1,2,1,13,13,9,1,5),_AdspConnState_Type())
adspConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:adspConnState.setStatus(_A)
_Atportptop_ObjectIdentity=ObjectIdentity
atportptop=_Atportptop_ObjectIdentity((1,3,6,1,2,1,13,14))
_AtportPtoPTable_Object=MibTable
atportPtoPTable=_AtportPtoPTable_Object((1,3,6,1,2,1,13,14,1))
if mibBuilder.loadTexts:atportPtoPTable.setStatus(_A)
_AtportPtoPEntry_Object=MibTableRow
atportPtoPEntry=_AtportPtoPEntry_Object((1,3,6,1,2,1,13,14,1,1))
atportPtoPEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:atportPtoPEntry.setStatus(_A)
_AtportPtoPIndex_Type=Integer32
_AtportPtoPIndex_Object=MibTableColumn
atportPtoPIndex=_AtportPtoPIndex_Object((1,3,6,1,2,1,13,14,1,1,1),_AtportPtoPIndex_Type())
atportPtoPIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:atportPtoPIndex.setStatus(_A)
_AtportPtoPProtocol_Type=ObjectIdentifier
_AtportPtoPProtocol_Object=MibTableColumn
atportPtoPProtocol=_AtportPtoPProtocol_Object((1,3,6,1,2,1,13,14,1,1,2),_AtportPtoPProtocol_Type())
atportPtoPProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:atportPtoPProtocol.setStatus(_A)
_AtportPtoPRemoteName_Type=DisplayString
_AtportPtoPRemoteName_Object=MibTableColumn
atportPtoPRemoteName=_AtportPtoPRemoteName_Object((1,3,6,1,2,1,13,14,1,1,3),_AtportPtoPRemoteName_Type())
atportPtoPRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:atportPtoPRemoteName.setStatus(_A)
_AtportPtoPRemoteAddress_Type=OctetString
_AtportPtoPRemoteAddress_Object=MibTableColumn
atportPtoPRemoteAddress=_AtportPtoPRemoteAddress_Object((1,3,6,1,2,1,13,14,1,1,4),_AtportPtoPRemoteAddress_Type())
atportPtoPRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atportPtoPRemoteAddress.setStatus(_A)
_AtportPtoPPortIndex_Type=Integer32
_AtportPtoPPortIndex_Object=MibTableColumn
atportPtoPPortIndex=_AtportPtoPPortIndex_Object((1,3,6,1,2,1,13,14,1,1,5),_AtportPtoPPortIndex_Type())
atportPtoPPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atportPtoPPortIndex.setStatus(_A)
class _AtportPtoPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_AtportPtoPStatus_Type.__name__=_D
_AtportPtoPStatus_Object=MibTableColumn
atportPtoPStatus=_AtportPtoPStatus_Object((1,3,6,1,2,1,13,14,1,1,6),_AtportPtoPStatus_Type())
atportPtoPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atportPtoPStatus.setStatus(_A)
_AtportPtoPProtoOids_ObjectIdentity=ObjectIdentity
atportPtoPProtoOids=_AtportPtoPProtoOids_ObjectIdentity((1,3,6,1,2,1,13,14,2))
_PToPProtoOther_ObjectIdentity=ObjectIdentity
pToPProtoOther=_PToPProtoOther_ObjectIdentity((1,3,6,1,2,1,13,14,2,1))
_PToPProtoAurp_ObjectIdentity=ObjectIdentity
pToPProtoAurp=_PToPProtoAurp_ObjectIdentity((1,3,6,1,2,1,13,14,2,2))
_PToPProtoCaymanUdp_ObjectIdentity=ObjectIdentity
pToPProtoCaymanUdp=_PToPProtoCaymanUdp_ObjectIdentity((1,3,6,1,2,1,13,14,2,3))
_PToPProtoAtkvmsDecnetIV_ObjectIdentity=ObjectIdentity
pToPProtoAtkvmsDecnetIV=_PToPProtoAtkvmsDecnetIV_ObjectIdentity((1,3,6,1,2,1,13,14,2,4))
_PToPProtoLiaisonUdp_ObjectIdentity=ObjectIdentity
pToPProtoLiaisonUdp=_PToPProtoLiaisonUdp_ObjectIdentity((1,3,6,1,2,1,13,14,2,5))
_PToPProtoIpx_ObjectIdentity=ObjectIdentity
pToPProtoIpx=_PToPProtoIpx_ObjectIdentity((1,3,6,1,2,1,13,14,2,6))
_PToPProtoShivaIp_ObjectIdentity=ObjectIdentity
pToPProtoShivaIp=_PToPProtoShivaIp_ObjectIdentity((1,3,6,1,2,1,13,14,2,7))
_RtmpStub_ObjectIdentity=ObjectIdentity
rtmpStub=_RtmpStub_ObjectIdentity((1,3,6,1,2,1,13,16))
_RtmpOutRequestPkts_Type=Counter32
_RtmpOutRequestPkts_Object=MibScalar
rtmpOutRequestPkts=_RtmpOutRequestPkts_Object((1,3,6,1,2,1,13,16,1),_RtmpOutRequestPkts_Type())
rtmpOutRequestPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpOutRequestPkts.setStatus(_A)
_RtmpInVersionMismatches_Type=Counter32
_RtmpInVersionMismatches_Object=MibScalar
rtmpInVersionMismatches=_RtmpInVersionMismatches_Object((1,3,6,1,2,1,13,16,2),_RtmpInVersionMismatches_Type())
rtmpInVersionMismatches.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpInVersionMismatches.setStatus(_A)
_RtmpInErrors_Type=Counter32
_RtmpInErrors_Object=MibScalar
rtmpInErrors=_RtmpInErrors_Object((1,3,6,1,2,1,13,16,3),_RtmpInErrors_Type())
rtmpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rtmpInErrors.setStatus(_A)
_ZipEndNode_ObjectIdentity=ObjectIdentity
zipEndNode=_ZipEndNode_ObjectIdentity((1,3,6,1,2,1,13,17))
_ZipNetInfoTable_Object=MibTable
zipNetInfoTable=_ZipNetInfoTable_Object((1,3,6,1,2,1,13,17,1))
if mibBuilder.loadTexts:zipNetInfoTable.setStatus(_A)
_ZipNetInfoEntry_Object=MibTableRow
zipNetInfoEntry=_ZipNetInfoEntry_Object((1,3,6,1,2,1,13,17,1,1))
zipNetInfoEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:zipNetInfoEntry.setStatus(_A)
_ZipOutGetNetInfos_Type=Counter32
_ZipOutGetNetInfos_Object=MibTableColumn
zipOutGetNetInfos=_ZipOutGetNetInfos_Object((1,3,6,1,2,1,13,17,1,1,1),_ZipOutGetNetInfos_Type())
zipOutGetNetInfos.setMaxAccess(_B)
if mibBuilder.loadTexts:zipOutGetNetInfos.setStatus(_A)
_ZipInGetNetInfoReplies_Type=Counter32
_ZipInGetNetInfoReplies_Object=MibTableColumn
zipInGetNetInfoReplies=_ZipInGetNetInfoReplies_Object((1,3,6,1,2,1,13,17,1,1,2),_ZipInGetNetInfoReplies_Type())
zipInGetNetInfoReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInGetNetInfoReplies.setStatus(_A)
_ZipZoneInInvalids_Type=Counter32
_ZipZoneInInvalids_Object=MibTableColumn
zipZoneInInvalids=_ZipZoneInInvalids_Object((1,3,6,1,2,1,13,17,1,1,3),_ZipZoneInInvalids_Type())
zipZoneInInvalids.setMaxAccess(_B)
if mibBuilder.loadTexts:zipZoneInInvalids.setStatus(_A)
_ZipInErrors_Type=Counter32
_ZipInErrors_Object=MibScalar
zipInErrors=_ZipInErrors_Object((1,3,6,1,2,1,13,17,2),_ZipInErrors_Type())
zipInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zipInErrors.setStatus(_A)
_PerPort_ObjectIdentity=ObjectIdentity
perPort=_PerPort_ObjectIdentity((1,3,6,1,2,1,13,18))
_PerPortTable_Object=MibTable
perPortTable=_PerPortTable_Object((1,3,6,1,2,1,13,18,1))
if mibBuilder.loadTexts:perPortTable.setStatus(_A)
_PerPortEntry_Object=MibTableRow
perPortEntry=_PerPortEntry_Object((1,3,6,1,2,1,13,18,1,1))
perPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:perPortEntry.setStatus(_A)
_PerPortAarpInProbes_Type=Counter32
_PerPortAarpInProbes_Object=MibTableColumn
perPortAarpInProbes=_PerPortAarpInProbes_Object((1,3,6,1,2,1,13,18,1,1,1),_PerPortAarpInProbes_Type())
perPortAarpInProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortAarpInProbes.setStatus(_A)
_PerPortAarpOutProbes_Type=Counter32
_PerPortAarpOutProbes_Object=MibTableColumn
perPortAarpOutProbes=_PerPortAarpOutProbes_Object((1,3,6,1,2,1,13,18,1,1,2),_PerPortAarpOutProbes_Type())
perPortAarpOutProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortAarpOutProbes.setStatus(_A)
_PerPortAarpInReqs_Type=Counter32
_PerPortAarpInReqs_Object=MibTableColumn
perPortAarpInReqs=_PerPortAarpInReqs_Object((1,3,6,1,2,1,13,18,1,1,3),_PerPortAarpInReqs_Type())
perPortAarpInReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortAarpInReqs.setStatus(_A)
_PerPortAarpOutReqs_Type=Counter32
_PerPortAarpOutReqs_Object=MibTableColumn
perPortAarpOutReqs=_PerPortAarpOutReqs_Object((1,3,6,1,2,1,13,18,1,1,4),_PerPortAarpOutReqs_Type())
perPortAarpOutReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortAarpOutReqs.setStatus(_A)
_PerPortAarpInRsps_Type=Counter32
_PerPortAarpInRsps_Object=MibTableColumn
perPortAarpInRsps=_PerPortAarpInRsps_Object((1,3,6,1,2,1,13,18,1,1,5),_PerPortAarpInRsps_Type())
perPortAarpInRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortAarpInRsps.setStatus(_A)
_PerPortAarpOutRsps_Type=Counter32
_PerPortAarpOutRsps_Object=MibTableColumn
perPortAarpOutRsps=_PerPortAarpOutRsps_Object((1,3,6,1,2,1,13,18,1,1,6),_PerPortAarpOutRsps_Type())
perPortAarpOutRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortAarpOutRsps.setStatus(_A)
_PerPortDdpInReceives_Type=Counter32
_PerPortDdpInReceives_Object=MibTableColumn
perPortDdpInReceives=_PerPortDdpInReceives_Object((1,3,6,1,2,1,13,18,1,1,7),_PerPortDdpInReceives_Type())
perPortDdpInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpInReceives.setStatus(_A)
_PerPortDdpInLocalDatagrams_Type=Counter32
_PerPortDdpInLocalDatagrams_Object=MibTableColumn
perPortDdpInLocalDatagrams=_PerPortDdpInLocalDatagrams_Object((1,3,6,1,2,1,13,18,1,1,8),_PerPortDdpInLocalDatagrams_Type())
perPortDdpInLocalDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpInLocalDatagrams.setStatus(_A)
_PerPortDdpNoProtocolHandlers_Type=Counter32
_PerPortDdpNoProtocolHandlers_Object=MibTableColumn
perPortDdpNoProtocolHandlers=_PerPortDdpNoProtocolHandlers_Object((1,3,6,1,2,1,13,18,1,1,9),_PerPortDdpNoProtocolHandlers_Type())
perPortDdpNoProtocolHandlers.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpNoProtocolHandlers.setStatus(_A)
_PerPortDdpTooShortErrors_Type=Counter32
_PerPortDdpTooShortErrors_Object=MibTableColumn
perPortDdpTooShortErrors=_PerPortDdpTooShortErrors_Object((1,3,6,1,2,1,13,18,1,1,10),_PerPortDdpTooShortErrors_Type())
perPortDdpTooShortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpTooShortErrors.setStatus(_A)
_PerPortDdpTooLongErrors_Type=Counter32
_PerPortDdpTooLongErrors_Object=MibTableColumn
perPortDdpTooLongErrors=_PerPortDdpTooLongErrors_Object((1,3,6,1,2,1,13,18,1,1,11),_PerPortDdpTooLongErrors_Type())
perPortDdpTooLongErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpTooLongErrors.setStatus(_A)
_PerPortDdpChecksumErrors_Type=Counter32
_PerPortDdpChecksumErrors_Object=MibTableColumn
perPortDdpChecksumErrors=_PerPortDdpChecksumErrors_Object((1,3,6,1,2,1,13,18,1,1,12),_PerPortDdpChecksumErrors_Type())
perPortDdpChecksumErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpChecksumErrors.setStatus(_A)
_PerPortDdpForwRequests_Type=Counter32
_PerPortDdpForwRequests_Object=MibTableColumn
perPortDdpForwRequests=_PerPortDdpForwRequests_Object((1,3,6,1,2,1,13,18,1,1,13),_PerPortDdpForwRequests_Type())
perPortDdpForwRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortDdpForwRequests.setStatus(_A)
_PerPortRtmpInDataPkts_Type=Counter32
_PerPortRtmpInDataPkts_Object=MibTableColumn
perPortRtmpInDataPkts=_PerPortRtmpInDataPkts_Object((1,3,6,1,2,1,13,18,1,1,14),_PerPortRtmpInDataPkts_Type())
perPortRtmpInDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortRtmpInDataPkts.setStatus(_A)
_PerPortRtmpOutDataPkts_Type=Counter32
_PerPortRtmpOutDataPkts_Object=MibTableColumn
perPortRtmpOutDataPkts=_PerPortRtmpOutDataPkts_Object((1,3,6,1,2,1,13,18,1,1,15),_PerPortRtmpOutDataPkts_Type())
perPortRtmpOutDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortRtmpOutDataPkts.setStatus(_A)
_PerPortRtmpInRequestPkts_Type=Counter32
_PerPortRtmpInRequestPkts_Object=MibTableColumn
perPortRtmpInRequestPkts=_PerPortRtmpInRequestPkts_Object((1,3,6,1,2,1,13,18,1,1,16),_PerPortRtmpInRequestPkts_Type())
perPortRtmpInRequestPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortRtmpInRequestPkts.setStatus(_A)
_PerPortRtmpRouteDeletes_Type=Counter32
_PerPortRtmpRouteDeletes_Object=MibTableColumn
perPortRtmpRouteDeletes=_PerPortRtmpRouteDeletes_Object((1,3,6,1,2,1,13,18,1,1,17),_PerPortRtmpRouteDeletes_Type())
perPortRtmpRouteDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortRtmpRouteDeletes.setStatus(_A)
_PerPortZipInZipQueries_Type=Counter32
_PerPortZipInZipQueries_Object=MibTableColumn
perPortZipInZipQueries=_PerPortZipInZipQueries_Object((1,3,6,1,2,1,13,18,1,1,18),_PerPortZipInZipQueries_Type())
perPortZipInZipQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortZipInZipQueries.setStatus(_A)
_PerPortZipInZipReplies_Type=Counter32
_PerPortZipInZipReplies_Object=MibTableColumn
perPortZipInZipReplies=_PerPortZipInZipReplies_Object((1,3,6,1,2,1,13,18,1,1,19),_PerPortZipInZipReplies_Type())
perPortZipInZipReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortZipInZipReplies.setStatus(_A)
_PerPortZipInZipExtendedReplies_Type=Counter32
_PerPortZipInZipExtendedReplies_Object=MibTableColumn
perPortZipInZipExtendedReplies=_PerPortZipInZipExtendedReplies_Object((1,3,6,1,2,1,13,18,1,1,20),_PerPortZipInZipExtendedReplies_Type())
perPortZipInZipExtendedReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortZipInZipExtendedReplies.setStatus(_A)
_PerPortZipZoneConflictErrors_Type=Counter32
_PerPortZipZoneConflictErrors_Object=MibTableColumn
perPortZipZoneConflictErrors=_PerPortZipZoneConflictErrors_Object((1,3,6,1,2,1,13,18,1,1,21),_PerPortZipZoneConflictErrors_Type())
perPortZipZoneConflictErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortZipZoneConflictErrors.setStatus(_A)
_PerPortZipInErrors_Type=Counter32
_PerPortZipInErrors_Object=MibTableColumn
perPortZipInErrors=_PerPortZipInErrors_Object((1,3,6,1,2,1,13,18,1,1,22),_PerPortZipInErrors_Type())
perPortZipInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortZipInErrors.setStatus(_A)
_PerPortNbpInLookUpRequests_Type=Counter32
_PerPortNbpInLookUpRequests_Object=MibTableColumn
perPortNbpInLookUpRequests=_PerPortNbpInLookUpRequests_Object((1,3,6,1,2,1,13,18,1,1,23),_PerPortNbpInLookUpRequests_Type())
perPortNbpInLookUpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpInLookUpRequests.setStatus(_A)
_PerPortNbpInLookUpReplies_Type=Counter32
_PerPortNbpInLookUpReplies_Object=MibTableColumn
perPortNbpInLookUpReplies=_PerPortNbpInLookUpReplies_Object((1,3,6,1,2,1,13,18,1,1,24),_PerPortNbpInLookUpReplies_Type())
perPortNbpInLookUpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpInLookUpReplies.setStatus(_A)
_PerPortNbpInBroadcastRequests_Type=Counter32
_PerPortNbpInBroadcastRequests_Object=MibTableColumn
perPortNbpInBroadcastRequests=_PerPortNbpInBroadcastRequests_Object((1,3,6,1,2,1,13,18,1,1,25),_PerPortNbpInBroadcastRequests_Type())
perPortNbpInBroadcastRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpInBroadcastRequests.setStatus(_A)
_PerPortNbpInForwardRequests_Type=Counter32
_PerPortNbpInForwardRequests_Object=MibTableColumn
perPortNbpInForwardRequests=_PerPortNbpInForwardRequests_Object((1,3,6,1,2,1,13,18,1,1,26),_PerPortNbpInForwardRequests_Type())
perPortNbpInForwardRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpInForwardRequests.setStatus(_A)
_PerPortNbpOutLookUpReplies_Type=Counter32
_PerPortNbpOutLookUpReplies_Object=MibTableColumn
perPortNbpOutLookUpReplies=_PerPortNbpOutLookUpReplies_Object((1,3,6,1,2,1,13,18,1,1,27),_PerPortNbpOutLookUpReplies_Type())
perPortNbpOutLookUpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpOutLookUpReplies.setStatus(_A)
_PerPortNbpRegistrationFailures_Type=Counter32
_PerPortNbpRegistrationFailures_Object=MibTableColumn
perPortNbpRegistrationFailures=_PerPortNbpRegistrationFailures_Object((1,3,6,1,2,1,13,18,1,1,28),_PerPortNbpRegistrationFailures_Type())
perPortNbpRegistrationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpRegistrationFailures.setStatus(_A)
_PerPortNbpInErrors_Type=Counter32
_PerPortNbpInErrors_Object=MibTableColumn
perPortNbpInErrors=_PerPortNbpInErrors_Object((1,3,6,1,2,1,13,18,1,1,29),_PerPortNbpInErrors_Type())
perPortNbpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortNbpInErrors.setStatus(_A)
_PerPortEchoRequests_Type=Counter32
_PerPortEchoRequests_Object=MibTableColumn
perPortEchoRequests=_PerPortEchoRequests_Object((1,3,6,1,2,1,13,18,1,1,30),_PerPortEchoRequests_Type())
perPortEchoRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortEchoRequests.setStatus(_A)
_PerPortEchoReplies_Type=Counter32
_PerPortEchoReplies_Object=MibTableColumn
perPortEchoReplies=_PerPortEchoReplies_Object((1,3,6,1,2,1,13,18,1,1,31),_PerPortEchoReplies_Type())
perPortEchoReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:perPortEchoReplies.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ATNetworkNumber':ATNetworkNumber,'DdpNodeAddress':DdpNodeAddress,'DdpSocketAddress':DdpSocketAddress,_L:ATName,_c:appletalk,'llap':llap,'llapTable':llapTable,'llapEntry':llapEntry,_N:llapIfIndex,'llapInPkts':llapInPkts,'llapOutPkts':llapOutPkts,'llapInNoHandlers':llapInNoHandlers,'llapInLengthErrors':llapInLengthErrors,'llapInErrors':llapInErrors,'llapCollisions':llapCollisions,'llapDefers':llapDefers,'llapNoDataErrors':llapNoDataErrors,'llapRandomCTSErrors':llapRandomCTSErrors,'llapFCSErrors':llapFCSErrors,'aarp':aarp,'aarpTable':aarpTable,'aarpEntry':aarpEntry,_O:aarpIfIndex,'aarpPhysAddress':aarpPhysAddress,_P:aarpNetAddress,'aarpStatus':aarpStatus,'aarpLookups':aarpLookups,'aarpHits':aarpHits,'atport':atport,'atportTable':atportTable,'atportEntry':atportEntry,_I:atportIndex,'atportDescr':atportDescr,'atportType':atportType,'atportNetStart':atportNetStart,'atportNetEnd':atportNetEnd,'atportNetAddress':atportNetAddress,'atportStatus':atportStatus,'atportNetConfig':atportNetConfig,'atportZoneConfig':atportZoneConfig,'atportZoneDefault':atportZoneDefault,'atportIfIndex':atportIfIndex,'atportNetFrom':atportNetFrom,'atportZoneFrom':atportZoneFrom,'atportInPkts':atportInPkts,'atportOutPkts':atportOutPkts,'atportHome':atportHome,'atportCurrentZone':atportCurrentZone,'atportConflictPhysAddr':atportConflictPhysAddr,'atportZoneTable':atportZoneTable,'atportZoneEntry':atportZoneEntry,_X:atportZonePort,_Y:atportZoneName,'atportZoneStatus':atportZoneStatus,'ddp':ddp,'ddpOutRequests':ddpOutRequests,'ddpOutShorts':ddpOutShorts,'ddpOutLongs':ddpOutLongs,'ddpInReceives':ddpInReceives,'ddpForwRequests':ddpForwRequests,'ddpInLocalDatagrams':ddpInLocalDatagrams,'ddpNoProtocolHandlers':ddpNoProtocolHandlers,'ddpOutNoRoutes':ddpOutNoRoutes,'ddpTooShortErrors':ddpTooShortErrors,'ddpTooLongErrors':ddpTooLongErrors,'ddpBroadcastErrors':ddpBroadcastErrors,'ddpShortDDPErrors':ddpShortDDPErrors,'ddpHopCountErrors':ddpHopCountErrors,'ddpChecksumErrors':ddpChecksumErrors,'ddpListenerTable':ddpListenerTable,'ddpListenerEntry':ddpListenerEntry,_Z:ddpListenerAddress,'ddpListenerInPkts':ddpListenerInPkts,'ddpListenerStatus':ddpListenerStatus,'ddpForwardingTable':ddpForwardingTable,'ddpForwardingEntry':ddpForwardingEntry,_a:ddpForwardingNetEnd,'ddpForwardingNetStart':ddpForwardingNetStart,'ddpForwardingNextHop':ddpForwardingNextHop,'ddpForwardingProto':ddpForwardingProto,'ddpForwardingModifiedTime':ddpForwardingModifiedTime,'ddpForwardingUseCounts':ddpForwardingUseCounts,'ddpForwardingPort':ddpForwardingPort,'ddpForwProtoOids':ddpForwProtoOids,'rtmpRoutingProto':rtmpRoutingProto,'kipRoutingProto':kipRoutingProto,'ddpForwardingTableOverflows':ddpForwardingTableOverflows,'rtmp':rtmp,'rtmpTable':rtmpTable,'rtmpEntry':rtmpEntry,_b:rtmpRangeStart,'rtmpRangeEnd':rtmpRangeEnd,'rtmpNextHop':rtmpNextHop,'rtmpType':rtmpType,'rtmpPort':rtmpPort,'rtmpHops':rtmpHops,'rtmpState':rtmpState,'rtmpInDataPkts':rtmpInDataPkts,'rtmpOutDataPkts':rtmpOutDataPkts,'rtmpInRequestPkts':rtmpInRequestPkts,'rtmpNextIREqualChanges':rtmpNextIREqualChanges,'rtmpNextIRLessChanges':rtmpNextIRLessChanges,'rtmpRouteDeletes':rtmpRouteDeletes,'rtmpRoutingTableOverflows':rtmpRoutingTableOverflows,'kip':kip,'kipTable':kipTable,'kipEntry':kipEntry,_d:kipNetStart,'kipNetEnd':kipNetEnd,'kipNextHop':kipNextHop,'kipHopCount':kipHopCount,'kipBCastAddr':kipBCastAddr,'kipCore':kipCore,'kipType':kipType,'kipState':kipState,'kipShare':kipShare,'kipFrom':kipFrom,'zipRouter':zipRouter,'zipTable':zipTable,'zipEntry':zipEntry,'zipZoneName':zipZoneName,_f:zipZoneIndex,_e:zipZoneNetStart,'zipZoneNetEnd':zipZoneNetEnd,'zipZoneState':zipZoneState,'zipZoneFrom':zipZoneFrom,'zipZonePort':zipZonePort,'zipInZipQueries':zipInZipQueries,'zipInZipReplies':zipInZipReplies,'zipInZipExtendedReplies':zipInZipExtendedReplies,'zipZoneConflictErrors':zipZoneConflictErrors,'zipInObsoletes':zipInObsoletes,'zipRouterNetInfoTable':zipRouterNetInfoTable,'zipRouterNetInfoEntry':zipRouterNetInfoEntry,'zipInGetNetInfos':zipInGetNetInfos,'zipOutGetNetInfoReplies':zipOutGetNetInfoReplies,'zipZoneOutInvalids':zipZoneOutInvalids,'zipAddressInvalids':zipAddressInvalids,'nbp':nbp,'nbpTable':nbpTable,'nbpEntry':nbpEntry,_g:nbpIndex,'nbpObject':nbpObject,'nbpType':nbpType,'nbpZone':nbpZone,'nbpState':nbpState,'nbpAddress':nbpAddress,'nbpEnumerator':nbpEnumerator,'nbpInLookUpRequests':nbpInLookUpRequests,'nbpInLookUpReplies':nbpInLookUpReplies,'nbpInBroadcastRequests':nbpInBroadcastRequests,'nbpInForwardRequests':nbpInForwardRequests,'nbpOutLookUpReplies':nbpOutLookUpReplies,'nbpRegistrationFailures':nbpRegistrationFailures,'nbpInErrors':nbpInErrors,'atecho':atecho,'atechoRequests':atechoRequests,'atechoReplies':atechoReplies,'atechoOutRequests':atechoOutRequests,'atechoInReplies':atechoInReplies,'atp':atp,'atpInPkts':atpInPkts,'atpOutPkts':atpOutPkts,'atpTRequestRetransmissions':atpTRequestRetransmissions,'atpTResponseRetransmissions':atpTResponseRetransmissions,'atpReleaseTimerExpiredCounts':atpReleaseTimerExpiredCounts,'atpRetryCountExceededs':atpRetryCountExceededs,'atpListenerTable':atpListenerTable,'atpListenerEntry':atpListenerEntry,_h:atpListenerAddress,'atpListenerStatus':atpListenerStatus,'pap':pap,'papInOpenConns':papInOpenConns,'papOutOpenConns':papOutOpenConns,'papInDatas':papInDatas,'papOutDatas':papOutDatas,'papInCloseConns':papInCloseConns,'papOutCloseConns':papOutCloseConns,'papTickleTimeoutCloses':papTickleTimeoutCloses,'papServerTable':papServerTable,'papServerEntry':papServerEntry,_i:papServerIndex,'papServerListeningSocket':papServerListeningSocket,'papServerStatus':papServerStatus,'papServerCompletedJobs':papServerCompletedJobs,'papServerBusyJobs':papServerBusyJobs,'papServerFreeJobs':papServerFreeJobs,'papServerAuthenticationFailures':papServerAuthenticationFailures,'papServerAccountingFailures':papServerAccountingFailures,'papServerGeneralFailures':papServerGeneralFailures,'papServerState':papServerState,'papServerLastStatusMsg':papServerLastStatusMsg,'asp':asp,'aspInputTransactions':aspInputTransactions,'aspOutputTransactions':aspOutputTransactions,'aspInOpenSessions':aspInOpenSessions,'aspOutOpenSessions':aspOutOpenSessions,'aspInCloseSessions':aspInCloseSessions,'aspOutCloseSessions':aspOutCloseSessions,'aspNoMoreSessionsErrors':aspNoMoreSessionsErrors,'aspTickleTimeOutCloses':aspTickleTimeOutCloses,'aspConnTable':aspConnTable,'aspConnEntry':aspConnEntry,_j:aspConnLocalAddress,_k:aspConnRemoteAddress,_l:aspConnID,'aspConnLastReqNum':aspConnLastReqNum,'aspConnServerEnd':aspConnServerEnd,'aspConnState':aspConnState,'adsp':adsp,'adspInPkts':adspInPkts,'adspOutPkts':adspOutPkts,'adspInOctets':adspInOctets,'adspOutOctets':adspOutOctets,'adspInDataPkts':adspInDataPkts,'adspOutDataPkts':adspOutDataPkts,'adspTimeoutErrors':adspTimeoutErrors,'adspTimeoutCloseErrors':adspTimeoutCloseErrors,'adspConnTable':adspConnTable,'adspConnEntry':adspConnEntry,_n:adspConnLocalAddress,_p:adspConnLocalConnID,_o:adspConnRemoteAddress,'adspConnRemoteConnID':adspConnRemoteConnID,'adspConnState':adspConnState,'atportptop':atportptop,'atportPtoPTable':atportPtoPTable,'atportPtoPEntry':atportPtoPEntry,_q:atportPtoPIndex,'atportPtoPProtocol':atportPtoPProtocol,'atportPtoPRemoteName':atportPtoPRemoteName,'atportPtoPRemoteAddress':atportPtoPRemoteAddress,'atportPtoPPortIndex':atportPtoPPortIndex,'atportPtoPStatus':atportPtoPStatus,'atportPtoPProtoOids':atportPtoPProtoOids,'pToPProtoOther':pToPProtoOther,'pToPProtoAurp':pToPProtoAurp,'pToPProtoCaymanUdp':pToPProtoCaymanUdp,'pToPProtoAtkvmsDecnetIV':pToPProtoAtkvmsDecnetIV,'pToPProtoLiaisonUdp':pToPProtoLiaisonUdp,'pToPProtoIpx':pToPProtoIpx,'pToPProtoShivaIp':pToPProtoShivaIp,'rtmpStub':rtmpStub,'rtmpOutRequestPkts':rtmpOutRequestPkts,'rtmpInVersionMismatches':rtmpInVersionMismatches,'rtmpInErrors':rtmpInErrors,'zipEndNode':zipEndNode,'zipNetInfoTable':zipNetInfoTable,'zipNetInfoEntry':zipNetInfoEntry,'zipOutGetNetInfos':zipOutGetNetInfos,'zipInGetNetInfoReplies':zipInGetNetInfoReplies,'zipZoneInInvalids':zipZoneInInvalids,'zipInErrors':zipInErrors,'perPort':perPort,'perPortTable':perPortTable,'perPortEntry':perPortEntry,'perPortAarpInProbes':perPortAarpInProbes,'perPortAarpOutProbes':perPortAarpOutProbes,'perPortAarpInReqs':perPortAarpInReqs,'perPortAarpOutReqs':perPortAarpOutReqs,'perPortAarpInRsps':perPortAarpInRsps,'perPortAarpOutRsps':perPortAarpOutRsps,'perPortDdpInReceives':perPortDdpInReceives,'perPortDdpInLocalDatagrams':perPortDdpInLocalDatagrams,'perPortDdpNoProtocolHandlers':perPortDdpNoProtocolHandlers,'perPortDdpTooShortErrors':perPortDdpTooShortErrors,'perPortDdpTooLongErrors':perPortDdpTooLongErrors,'perPortDdpChecksumErrors':perPortDdpChecksumErrors,'perPortDdpForwRequests':perPortDdpForwRequests,'perPortRtmpInDataPkts':perPortRtmpInDataPkts,'perPortRtmpOutDataPkts':perPortRtmpOutDataPkts,'perPortRtmpInRequestPkts':perPortRtmpInRequestPkts,'perPortRtmpRouteDeletes':perPortRtmpRouteDeletes,'perPortZipInZipQueries':perPortZipInZipQueries,'perPortZipInZipReplies':perPortZipInZipReplies,'perPortZipInZipExtendedReplies':perPortZipInZipExtendedReplies,'perPortZipZoneConflictErrors':perPortZipZoneConflictErrors,'perPortZipInErrors':perPortZipInErrors,'perPortNbpInLookUpRequests':perPortNbpInLookUpRequests,'perPortNbpInLookUpReplies':perPortNbpInLookUpReplies,'perPortNbpInBroadcastRequests':perPortNbpInBroadcastRequests,'perPortNbpInForwardRequests':perPortNbpInForwardRequests,'perPortNbpOutLookUpReplies':perPortNbpOutLookUpReplies,'perPortNbpRegistrationFailures':perPortNbpRegistrationFailures,'perPortNbpInErrors':perPortNbpInErrors,'perPortEchoRequests':perPortEchoRequests,'perPortEchoReplies':perPortEchoReplies})