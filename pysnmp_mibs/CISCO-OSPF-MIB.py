_Ai='cospfShamLinkNbrGroup'
_Ah='cospfShamLinksGroup'
_Ag='cospfShamLinkGroup'
_Af='cospfShamLinksMetric'
_Ae='cospfShamLinksEvents'
_Ad='cospfShamLinksState'
_Ac='cospfShamLinksRtrDeadInterval'
_Ab='cospfShamLinksHelloInterval'
_Aa='cospfShamLinksRetransInterval'
_AZ='cospfShamLinkNbrHelloSuppressed'
_AY='cospfShamLinkNbrLsRetransQLen'
_AX='cospfShamLinkNbrEvents'
_AW='cospfShamLinkNbrState'
_AV='cospfShamLinkNbrOptions'
_AU='cospfShamLinkNbrRtrId'
_AT='cospfShamLinkMetric'
_AS='cospfShamLinkEvents'
_AR='cospfShamLinkState'
_AQ='cospfShamLinkRtrDeadInterval'
_AP='cospfShamLinkHelloInterval'
_AO='cospfShamLinkRetransInterval'
_AN='cospfVirtIfLsaCksumSum'
_AM='cospfVirtIfLsaCount'
_AL='cospfIfLsaCksumSum'
_AK='cospfIfLsaCount'
_AJ='cospfAreaNssaTranslatorEvents'
_AI='cospfAreaNssaTranslatorState'
_AH='cospfAreaNssaTranslatorRole'
_AG='cospfOpaqueAreaLsaCksumSum'
_AF='cospfOpaqueAreaLsaCount'
_AE='cospfOpaqueASLsaCksumSum'
_AD='cospfOpaqueASLsaCount'
_AC='cospfTrafficEngineeringSupport'
_AB='cospfOpaqueLsaSupport'
_AA='cospfRFC1583Compatibility'
_A9='cospfVirtLocalLsdbAdvertisement'
_A8='cospfVirtLocalLsdbChecksum'
_A7='cospfVirtLocalLsdbAge'
_A6='cospfVirtLocalLsdbSequence'
_A5='cospfLocalLsdbAdvertisement'
_A4='cospfLocalLsdbChecksum'
_A3='cospfLocalLsdbAge'
_A2='cospfLocalLsdbSequence'
_A1='cospfLsdbAdvertisement'
_A0='cospfLsdbChecksum'
_z='cospfLsdbAge'
_y='cospfLsdbSequence'
_x='cospfVirtIfEntry'
_w='cospfIfEntry'
_v='cospfAreaEntry'
_u='cospfShamLinksRemoteIpAddr'
_t='cospfShamLinksRemoteIpAddrType'
_s='cospfShamLinksAreaId'
_r='cospfShamLinkNbrIpAddr'
_q='cospfShamLinkNbrIpAddrType'
_p='cospfShamLinkNbrArea'
_o='cospfVirtLocalLsdbRouterId'
_n='cospfVirtLocalLsdbLsid'
_m='cospfVirtLocalLsdbType'
_l='cospfVirtLocalLsdbNeighbor'
_k='cospfVirtLocalLsdbTransitArea'
_j='localOpaqueLink'
_i='cospfLocalLsdbRouterId'
_h='cospfLocalLsdbLsid'
_g='cospfLocalLsdbType'
_f='cospfLocalLsdbAddressLessIf'
_e='cospfLocalLsdbIpAddress'
_d='pointToPoint'
_c='cospfShamLinkNeighborId'
_b='cospfShamLinkLocalIpAddress'
_a='cospfShamLinkAreaId'
_Z='cospfLsdbType'
_Y='ospfLsdbRouterId'
_X='ospfLsdbLsid'
_W='ospfLsdbAreaId'
_V='cospfVirtLocalLsdbGroup'
_U='cospfLocalLsdbGroup'
_T='cospfLsdbGroup'
_S='cospfVirtIfGroup'
_R='cospfIfGroup'
_Q='cospfAreaGroup'
_P='cospfBasicGroup'
_O='cospfShamLinksLocalIpAddr'
_N='cospfShamLinksLocalIpAddrType'
_M='down'
_L='UpToMaxAge'
_K='PositiveInteger'
_J='HelloRange'
_I='OSPF-MIB'
_H='OctetString'
_G='Unsigned32'
_F='deprecated'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-OSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
AreaID,HelloRange,Metric,PositiveInteger,RouterID,UpToMaxAge,ospfAreaEntry,ospfIfEntry,ospfLsdbAreaId,ospfLsdbLsid,ospfLsdbRouterId,ospfVirtIfEntry=mibBuilder.importSymbols(_I,'AreaID',_J,'Metric',_K,'RouterID',_L,'ospfAreaEntry','ospfIfEntry',_W,_X,_Y,'ospfVirtIfEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cospf=ModuleIdentity((1,3,6,1,4,1,9,10,99))
if mibBuilder.loadTexts:cospf.setRevisions(('2003-07-18 00:00','2003-01-28 00:00'))
_CospfGeneralGroup_ObjectIdentity=ObjectIdentity
cospfGeneralGroup=_CospfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,9,10,99,1))
_CospfRFC1583Compatibility_Type=TruthValue
_CospfRFC1583Compatibility_Object=MibScalar
cospfRFC1583Compatibility=_CospfRFC1583Compatibility_Object((1,3,6,1,4,1,9,10,99,1,1),_CospfRFC1583Compatibility_Type())
cospfRFC1583Compatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfRFC1583Compatibility.setStatus(_B)
_CospfOpaqueLsaSupport_Type=TruthValue
_CospfOpaqueLsaSupport_Object=MibScalar
cospfOpaqueLsaSupport=_CospfOpaqueLsaSupport_Object((1,3,6,1,4,1,9,10,99,1,2),_CospfOpaqueLsaSupport_Type())
cospfOpaqueLsaSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfOpaqueLsaSupport.setStatus(_B)
_CospfTrafficEngineeringSupport_Type=TruthValue
_CospfTrafficEngineeringSupport_Object=MibScalar
cospfTrafficEngineeringSupport=_CospfTrafficEngineeringSupport_Object((1,3,6,1,4,1,9,10,99,1,3),_CospfTrafficEngineeringSupport_Type())
cospfTrafficEngineeringSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfTrafficEngineeringSupport.setStatus(_B)
_CospfOpaqueASLsaCount_Type=Gauge32
_CospfOpaqueASLsaCount_Object=MibScalar
cospfOpaqueASLsaCount=_CospfOpaqueASLsaCount_Object((1,3,6,1,4,1,9,10,99,1,4),_CospfOpaqueASLsaCount_Type())
cospfOpaqueASLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfOpaqueASLsaCount.setStatus(_B)
class _CospfOpaqueASLsaCksumSum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CospfOpaqueASLsaCksumSum_Type.__name__=_G
_CospfOpaqueASLsaCksumSum_Object=MibScalar
cospfOpaqueASLsaCksumSum=_CospfOpaqueASLsaCksumSum_Object((1,3,6,1,4,1,9,10,99,1,5),_CospfOpaqueASLsaCksumSum_Type())
cospfOpaqueASLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfOpaqueASLsaCksumSum.setStatus(_B)
_CospfAreaTable_Object=MibTable
cospfAreaTable=_CospfAreaTable_Object((1,3,6,1,4,1,9,10,99,2))
if mibBuilder.loadTexts:cospfAreaTable.setStatus(_B)
_CospfAreaEntry_Object=MibTableRow
cospfAreaEntry=_CospfAreaEntry_Object((1,3,6,1,4,1,9,10,99,2,1))
if mibBuilder.loadTexts:cospfAreaEntry.setStatus(_B)
_CospfOpaqueAreaLsaCount_Type=Gauge32
_CospfOpaqueAreaLsaCount_Object=MibTableColumn
cospfOpaqueAreaLsaCount=_CospfOpaqueAreaLsaCount_Object((1,3,6,1,4,1,9,10,99,2,1,1),_CospfOpaqueAreaLsaCount_Type())
cospfOpaqueAreaLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfOpaqueAreaLsaCount.setStatus(_B)
class _CospfOpaqueAreaLsaCksumSum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CospfOpaqueAreaLsaCksumSum_Type.__name__=_G
_CospfOpaqueAreaLsaCksumSum_Object=MibTableColumn
cospfOpaqueAreaLsaCksumSum=_CospfOpaqueAreaLsaCksumSum_Object((1,3,6,1,4,1,9,10,99,2,1,2),_CospfOpaqueAreaLsaCksumSum_Type())
cospfOpaqueAreaLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfOpaqueAreaLsaCksumSum.setStatus(_B)
class _CospfAreaNssaTranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_CospfAreaNssaTranslatorRole_Type.__name__=_E
_CospfAreaNssaTranslatorRole_Object=MibTableColumn
cospfAreaNssaTranslatorRole=_CospfAreaNssaTranslatorRole_Object((1,3,6,1,4,1,9,10,99,2,1,3),_CospfAreaNssaTranslatorRole_Type())
cospfAreaNssaTranslatorRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfAreaNssaTranslatorRole.setStatus(_B)
class _CospfAreaNssaTranslatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('elected',2),('disabled',3)))
_CospfAreaNssaTranslatorState_Type.__name__=_E
_CospfAreaNssaTranslatorState_Object=MibTableColumn
cospfAreaNssaTranslatorState=_CospfAreaNssaTranslatorState_Object((1,3,6,1,4,1,9,10,99,2,1,4),_CospfAreaNssaTranslatorState_Type())
cospfAreaNssaTranslatorState.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfAreaNssaTranslatorState.setStatus(_B)
_CospfAreaNssaTranslatorEvents_Type=Counter32
_CospfAreaNssaTranslatorEvents_Object=MibTableColumn
cospfAreaNssaTranslatorEvents=_CospfAreaNssaTranslatorEvents_Object((1,3,6,1,4,1,9,10,99,2,1,5),_CospfAreaNssaTranslatorEvents_Type())
cospfAreaNssaTranslatorEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfAreaNssaTranslatorEvents.setStatus(_B)
_CospfLsdbTable_Object=MibTable
cospfLsdbTable=_CospfLsdbTable_Object((1,3,6,1,4,1,9,10,99,3))
if mibBuilder.loadTexts:cospfLsdbTable.setStatus(_B)
_CospfLsdbEntry_Object=MibTableRow
cospfLsdbEntry=_CospfLsdbEntry_Object((1,3,6,1,4,1,9,10,99,3,1))
cospfLsdbEntry.setIndexNames((0,_I,_W),(0,_A,_Z),(0,_I,_X),(0,_I,_Y))
if mibBuilder.loadTexts:cospfLsdbEntry.setStatus(_B)
class _CospfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11)));namedValues=NamedValues(*(('areaOpaqueLink',10),('asOpaqueLink',11)))
_CospfLsdbType_Type.__name__=_E
_CospfLsdbType_Object=MibTableColumn
cospfLsdbType=_CospfLsdbType_Object((1,3,6,1,4,1,9,10,99,3,1,1),_CospfLsdbType_Type())
cospfLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfLsdbType.setStatus(_B)
class _CospfLsdbSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,147483647))
_CospfLsdbSequence_Type.__name__=_E
_CospfLsdbSequence_Object=MibTableColumn
cospfLsdbSequence=_CospfLsdbSequence_Object((1,3,6,1,4,1,9,10,99,3,1,2),_CospfLsdbSequence_Type())
cospfLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLsdbSequence.setStatus(_B)
class _CospfLsdbAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CospfLsdbAge_Type.__name__=_E
_CospfLsdbAge_Object=MibTableColumn
cospfLsdbAge=_CospfLsdbAge_Object((1,3,6,1,4,1,9,10,99,3,1,3),_CospfLsdbAge_Type())
cospfLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLsdbAge.setStatus(_B)
class _CospfLsdbChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CospfLsdbChecksum_Type.__name__=_E
_CospfLsdbChecksum_Object=MibTableColumn
cospfLsdbChecksum=_CospfLsdbChecksum_Object((1,3,6,1,4,1,9,10,99,3,1,4),_CospfLsdbChecksum_Type())
cospfLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLsdbChecksum.setStatus(_B)
class _CospfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_CospfLsdbAdvertisement_Type.__name__=_H
_CospfLsdbAdvertisement_Object=MibTableColumn
cospfLsdbAdvertisement=_CospfLsdbAdvertisement_Object((1,3,6,1,4,1,9,10,99,3,1,5),_CospfLsdbAdvertisement_Type())
cospfLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLsdbAdvertisement.setStatus(_B)
_CospfIfTable_Object=MibTable
cospfIfTable=_CospfIfTable_Object((1,3,6,1,4,1,9,10,99,4))
if mibBuilder.loadTexts:cospfIfTable.setStatus(_B)
_CospfIfEntry_Object=MibTableRow
cospfIfEntry=_CospfIfEntry_Object((1,3,6,1,4,1,9,10,99,4,1))
if mibBuilder.loadTexts:cospfIfEntry.setStatus(_B)
_CospfIfLsaCount_Type=Gauge32
_CospfIfLsaCount_Object=MibTableColumn
cospfIfLsaCount=_CospfIfLsaCount_Object((1,3,6,1,4,1,9,10,99,4,1,1),_CospfIfLsaCount_Type())
cospfIfLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfIfLsaCount.setStatus(_B)
class _CospfIfLsaCksumSum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CospfIfLsaCksumSum_Type.__name__=_G
_CospfIfLsaCksumSum_Object=MibTableColumn
cospfIfLsaCksumSum=_CospfIfLsaCksumSum_Object((1,3,6,1,4,1,9,10,99,4,1,2),_CospfIfLsaCksumSum_Type())
cospfIfLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfIfLsaCksumSum.setStatus(_B)
_CospfVirtIfTable_Object=MibTable
cospfVirtIfTable=_CospfVirtIfTable_Object((1,3,6,1,4,1,9,10,99,5))
if mibBuilder.loadTexts:cospfVirtIfTable.setStatus(_B)
_CospfVirtIfEntry_Object=MibTableRow
cospfVirtIfEntry=_CospfVirtIfEntry_Object((1,3,6,1,4,1,9,10,99,5,1))
if mibBuilder.loadTexts:cospfVirtIfEntry.setStatus(_B)
_CospfVirtIfLsaCount_Type=Gauge32
_CospfVirtIfLsaCount_Object=MibTableColumn
cospfVirtIfLsaCount=_CospfVirtIfLsaCount_Object((1,3,6,1,4,1,9,10,99,5,1,1),_CospfVirtIfLsaCount_Type())
cospfVirtIfLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfVirtIfLsaCount.setStatus(_B)
class _CospfVirtIfLsaCksumSum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CospfVirtIfLsaCksumSum_Type.__name__=_G
_CospfVirtIfLsaCksumSum_Object=MibTableColumn
cospfVirtIfLsaCksumSum=_CospfVirtIfLsaCksumSum_Object((1,3,6,1,4,1,9,10,99,5,1,2),_CospfVirtIfLsaCksumSum_Type())
cospfVirtIfLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfVirtIfLsaCksumSum.setStatus(_B)
_CospfShamLinkTable_Object=MibTable
cospfShamLinkTable=_CospfShamLinkTable_Object((1,3,6,1,4,1,9,10,99,6))
if mibBuilder.loadTexts:cospfShamLinkTable.setStatus(_F)
_CospfShamLinkEntry_Object=MibTableRow
cospfShamLinkEntry=_CospfShamLinkEntry_Object((1,3,6,1,4,1,9,10,99,6,1))
cospfShamLinkEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:cospfShamLinkEntry.setStatus(_F)
_CospfShamLinkAreaId_Type=AreaID
_CospfShamLinkAreaId_Object=MibTableColumn
cospfShamLinkAreaId=_CospfShamLinkAreaId_Object((1,3,6,1,4,1,9,10,99,6,1,1),_CospfShamLinkAreaId_Type())
cospfShamLinkAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinkAreaId.setStatus(_F)
_CospfShamLinkLocalIpAddress_Type=IpAddress
_CospfShamLinkLocalIpAddress_Object=MibTableColumn
cospfShamLinkLocalIpAddress=_CospfShamLinkLocalIpAddress_Object((1,3,6,1,4,1,9,10,99,6,1,2),_CospfShamLinkLocalIpAddress_Type())
cospfShamLinkLocalIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinkLocalIpAddress.setStatus(_F)
_CospfShamLinkNeighborId_Type=RouterID
_CospfShamLinkNeighborId_Object=MibTableColumn
cospfShamLinkNeighborId=_CospfShamLinkNeighborId_Object((1,3,6,1,4,1,9,10,99,6,1,3),_CospfShamLinkNeighborId_Type())
cospfShamLinkNeighborId.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinkNeighborId.setStatus(_F)
class _CospfShamLinkRetransInterval_Type(UpToMaxAge):defaultValue=5
_CospfShamLinkRetransInterval_Type.__name__=_L
_CospfShamLinkRetransInterval_Object=MibTableColumn
cospfShamLinkRetransInterval=_CospfShamLinkRetransInterval_Object((1,3,6,1,4,1,9,10,99,6,1,4),_CospfShamLinkRetransInterval_Type())
cospfShamLinkRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkRetransInterval.setStatus(_F)
class _CospfShamLinkHelloInterval_Type(HelloRange):defaultValue=10
_CospfShamLinkHelloInterval_Type.__name__=_J
_CospfShamLinkHelloInterval_Object=MibTableColumn
cospfShamLinkHelloInterval=_CospfShamLinkHelloInterval_Object((1,3,6,1,4,1,9,10,99,6,1,5),_CospfShamLinkHelloInterval_Type())
cospfShamLinkHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkHelloInterval.setStatus(_F)
class _CospfShamLinkRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_CospfShamLinkRtrDeadInterval_Type.__name__=_K
_CospfShamLinkRtrDeadInterval_Object=MibTableColumn
cospfShamLinkRtrDeadInterval=_CospfShamLinkRtrDeadInterval_Object((1,3,6,1,4,1,9,10,99,6,1,6),_CospfShamLinkRtrDeadInterval_Type())
cospfShamLinkRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkRtrDeadInterval.setStatus(_F)
class _CospfShamLinkState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_M,1),(_d,4)))
_CospfShamLinkState_Type.__name__=_E
_CospfShamLinkState_Object=MibTableColumn
cospfShamLinkState=_CospfShamLinkState_Object((1,3,6,1,4,1,9,10,99,6,1,7),_CospfShamLinkState_Type())
cospfShamLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkState.setStatus(_F)
_CospfShamLinkEvents_Type=Counter32
_CospfShamLinkEvents_Object=MibTableColumn
cospfShamLinkEvents=_CospfShamLinkEvents_Object((1,3,6,1,4,1,9,10,99,6,1,8),_CospfShamLinkEvents_Type())
cospfShamLinkEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkEvents.setStatus(_F)
_CospfShamLinkMetric_Type=Metric
_CospfShamLinkMetric_Object=MibTableColumn
cospfShamLinkMetric=_CospfShamLinkMetric_Object((1,3,6,1,4,1,9,10,99,6,1,9),_CospfShamLinkMetric_Type())
cospfShamLinkMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkMetric.setStatus(_F)
_CospfLocalLsdbTable_Object=MibTable
cospfLocalLsdbTable=_CospfLocalLsdbTable_Object((1,3,6,1,4,1,9,10,99,7))
if mibBuilder.loadTexts:cospfLocalLsdbTable.setStatus(_B)
_CospfLocalLsdbEntry_Object=MibTableRow
cospfLocalLsdbEntry=_CospfLocalLsdbEntry_Object((1,3,6,1,4,1,9,10,99,7,1))
cospfLocalLsdbEntry.setIndexNames((0,_A,_e),(0,_A,_f),(0,_A,_g),(0,_A,_h),(0,_A,_i))
if mibBuilder.loadTexts:cospfLocalLsdbEntry.setStatus(_B)
_CospfLocalLsdbIpAddress_Type=IpAddress
_CospfLocalLsdbIpAddress_Object=MibTableColumn
cospfLocalLsdbIpAddress=_CospfLocalLsdbIpAddress_Object((1,3,6,1,4,1,9,10,99,7,1,1),_CospfLocalLsdbIpAddress_Type())
cospfLocalLsdbIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfLocalLsdbIpAddress.setStatus(_B)
_CospfLocalLsdbAddressLessIf_Type=InterfaceIndexOrZero
_CospfLocalLsdbAddressLessIf_Object=MibTableColumn
cospfLocalLsdbAddressLessIf=_CospfLocalLsdbAddressLessIf_Object((1,3,6,1,4,1,9,10,99,7,1,2),_CospfLocalLsdbAddressLessIf_Type())
cospfLocalLsdbAddressLessIf.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfLocalLsdbAddressLessIf.setStatus(_B)
class _CospfLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues((_j,9))
_CospfLocalLsdbType_Type.__name__=_E
_CospfLocalLsdbType_Object=MibTableColumn
cospfLocalLsdbType=_CospfLocalLsdbType_Object((1,3,6,1,4,1,9,10,99,7,1,3),_CospfLocalLsdbType_Type())
cospfLocalLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfLocalLsdbType.setStatus(_B)
_CospfLocalLsdbLsid_Type=IpAddress
_CospfLocalLsdbLsid_Object=MibTableColumn
cospfLocalLsdbLsid=_CospfLocalLsdbLsid_Object((1,3,6,1,4,1,9,10,99,7,1,4),_CospfLocalLsdbLsid_Type())
cospfLocalLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfLocalLsdbLsid.setStatus(_B)
_CospfLocalLsdbRouterId_Type=RouterID
_CospfLocalLsdbRouterId_Object=MibTableColumn
cospfLocalLsdbRouterId=_CospfLocalLsdbRouterId_Object((1,3,6,1,4,1,9,10,99,7,1,5),_CospfLocalLsdbRouterId_Type())
cospfLocalLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfLocalLsdbRouterId.setStatus(_B)
class _CospfLocalLsdbSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CospfLocalLsdbSequence_Type.__name__=_E
_CospfLocalLsdbSequence_Object=MibTableColumn
cospfLocalLsdbSequence=_CospfLocalLsdbSequence_Object((1,3,6,1,4,1,9,10,99,7,1,6),_CospfLocalLsdbSequence_Type())
cospfLocalLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLocalLsdbSequence.setStatus(_B)
class _CospfLocalLsdbAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CospfLocalLsdbAge_Type.__name__=_E
_CospfLocalLsdbAge_Object=MibTableColumn
cospfLocalLsdbAge=_CospfLocalLsdbAge_Object((1,3,6,1,4,1,9,10,99,7,1,7),_CospfLocalLsdbAge_Type())
cospfLocalLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLocalLsdbAge.setStatus(_B)
class _CospfLocalLsdbChecksum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CospfLocalLsdbChecksum_Type.__name__=_G
_CospfLocalLsdbChecksum_Object=MibTableColumn
cospfLocalLsdbChecksum=_CospfLocalLsdbChecksum_Object((1,3,6,1,4,1,9,10,99,7,1,8),_CospfLocalLsdbChecksum_Type())
cospfLocalLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLocalLsdbChecksum.setStatus(_B)
class _CospfLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_CospfLocalLsdbAdvertisement_Type.__name__=_H
_CospfLocalLsdbAdvertisement_Object=MibTableColumn
cospfLocalLsdbAdvertisement=_CospfLocalLsdbAdvertisement_Object((1,3,6,1,4,1,9,10,99,7,1,9),_CospfLocalLsdbAdvertisement_Type())
cospfLocalLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfLocalLsdbAdvertisement.setStatus(_B)
_CospfVirtLocalLsdbTable_Object=MibTable
cospfVirtLocalLsdbTable=_CospfVirtLocalLsdbTable_Object((1,3,6,1,4,1,9,10,99,8))
if mibBuilder.loadTexts:cospfVirtLocalLsdbTable.setStatus(_B)
_CospfVirtLocalLsdbEntry_Object=MibTableRow
cospfVirtLocalLsdbEntry=_CospfVirtLocalLsdbEntry_Object((1,3,6,1,4,1,9,10,99,8,1))
cospfVirtLocalLsdbEntry.setIndexNames((0,_A,_k),(0,_A,_l),(0,_A,_m),(0,_A,_n),(0,_A,_o))
if mibBuilder.loadTexts:cospfVirtLocalLsdbEntry.setStatus(_B)
_CospfVirtLocalLsdbTransitArea_Type=AreaID
_CospfVirtLocalLsdbTransitArea_Object=MibTableColumn
cospfVirtLocalLsdbTransitArea=_CospfVirtLocalLsdbTransitArea_Object((1,3,6,1,4,1,9,10,99,8,1,1),_CospfVirtLocalLsdbTransitArea_Type())
cospfVirtLocalLsdbTransitArea.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfVirtLocalLsdbTransitArea.setStatus(_B)
_CospfVirtLocalLsdbNeighbor_Type=RouterID
_CospfVirtLocalLsdbNeighbor_Object=MibTableColumn
cospfVirtLocalLsdbNeighbor=_CospfVirtLocalLsdbNeighbor_Object((1,3,6,1,4,1,9,10,99,8,1,2),_CospfVirtLocalLsdbNeighbor_Type())
cospfVirtLocalLsdbNeighbor.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfVirtLocalLsdbNeighbor.setStatus(_B)
class _CospfVirtLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues((_j,9))
_CospfVirtLocalLsdbType_Type.__name__=_E
_CospfVirtLocalLsdbType_Object=MibTableColumn
cospfVirtLocalLsdbType=_CospfVirtLocalLsdbType_Object((1,3,6,1,4,1,9,10,99,8,1,3),_CospfVirtLocalLsdbType_Type())
cospfVirtLocalLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfVirtLocalLsdbType.setStatus(_B)
_CospfVirtLocalLsdbLsid_Type=IpAddress
_CospfVirtLocalLsdbLsid_Object=MibTableColumn
cospfVirtLocalLsdbLsid=_CospfVirtLocalLsdbLsid_Object((1,3,6,1,4,1,9,10,99,8,1,4),_CospfVirtLocalLsdbLsid_Type())
cospfVirtLocalLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfVirtLocalLsdbLsid.setStatus(_B)
_CospfVirtLocalLsdbRouterId_Type=RouterID
_CospfVirtLocalLsdbRouterId_Object=MibTableColumn
cospfVirtLocalLsdbRouterId=_CospfVirtLocalLsdbRouterId_Object((1,3,6,1,4,1,9,10,99,8,1,5),_CospfVirtLocalLsdbRouterId_Type())
cospfVirtLocalLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfVirtLocalLsdbRouterId.setStatus(_B)
class _CospfVirtLocalLsdbSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CospfVirtLocalLsdbSequence_Type.__name__=_E
_CospfVirtLocalLsdbSequence_Object=MibTableColumn
cospfVirtLocalLsdbSequence=_CospfVirtLocalLsdbSequence_Object((1,3,6,1,4,1,9,10,99,8,1,6),_CospfVirtLocalLsdbSequence_Type())
cospfVirtLocalLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfVirtLocalLsdbSequence.setStatus(_B)
class _CospfVirtLocalLsdbAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CospfVirtLocalLsdbAge_Type.__name__=_E
_CospfVirtLocalLsdbAge_Object=MibTableColumn
cospfVirtLocalLsdbAge=_CospfVirtLocalLsdbAge_Object((1,3,6,1,4,1,9,10,99,8,1,7),_CospfVirtLocalLsdbAge_Type())
cospfVirtLocalLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfVirtLocalLsdbAge.setStatus(_B)
class _CospfVirtLocalLsdbChecksum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CospfVirtLocalLsdbChecksum_Type.__name__=_G
_CospfVirtLocalLsdbChecksum_Object=MibTableColumn
cospfVirtLocalLsdbChecksum=_CospfVirtLocalLsdbChecksum_Object((1,3,6,1,4,1,9,10,99,8,1,8),_CospfVirtLocalLsdbChecksum_Type())
cospfVirtLocalLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfVirtLocalLsdbChecksum.setStatus(_B)
class _CospfVirtLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_CospfVirtLocalLsdbAdvertisement_Type.__name__=_H
_CospfVirtLocalLsdbAdvertisement_Object=MibTableColumn
cospfVirtLocalLsdbAdvertisement=_CospfVirtLocalLsdbAdvertisement_Object((1,3,6,1,4,1,9,10,99,8,1,9),_CospfVirtLocalLsdbAdvertisement_Type())
cospfVirtLocalLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfVirtLocalLsdbAdvertisement.setStatus(_B)
_CospfConformance_ObjectIdentity=ObjectIdentity
cospfConformance=_CospfConformance_ObjectIdentity((1,3,6,1,4,1,9,10,99,9))
_CospfGroups_ObjectIdentity=ObjectIdentity
cospfGroups=_CospfGroups_ObjectIdentity((1,3,6,1,4,1,9,10,99,9,1))
_CospfCompliances_ObjectIdentity=ObjectIdentity
cospfCompliances=_CospfCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,99,9,2))
_CospfShamLinkNbrTable_Object=MibTable
cospfShamLinkNbrTable=_CospfShamLinkNbrTable_Object((1,3,6,1,4,1,9,10,99,10))
if mibBuilder.loadTexts:cospfShamLinkNbrTable.setStatus(_B)
_CospfShamLinkNbrEntry_Object=MibTableRow
cospfShamLinkNbrEntry=_CospfShamLinkNbrEntry_Object((1,3,6,1,4,1,9,10,99,10,1))
cospfShamLinkNbrEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_A,_p),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:cospfShamLinkNbrEntry.setStatus(_B)
_CospfShamLinkNbrArea_Type=AreaID
_CospfShamLinkNbrArea_Object=MibTableColumn
cospfShamLinkNbrArea=_CospfShamLinkNbrArea_Object((1,3,6,1,4,1,9,10,99,10,1,1),_CospfShamLinkNbrArea_Type())
cospfShamLinkNbrArea.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinkNbrArea.setStatus(_B)
_CospfShamLinkNbrIpAddrType_Type=InetAddressType
_CospfShamLinkNbrIpAddrType_Object=MibTableColumn
cospfShamLinkNbrIpAddrType=_CospfShamLinkNbrIpAddrType_Object((1,3,6,1,4,1,9,10,99,10,1,2),_CospfShamLinkNbrIpAddrType_Type())
cospfShamLinkNbrIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinkNbrIpAddrType.setStatus(_B)
_CospfShamLinkNbrIpAddr_Type=InetAddress
_CospfShamLinkNbrIpAddr_Object=MibTableColumn
cospfShamLinkNbrIpAddr=_CospfShamLinkNbrIpAddr_Object((1,3,6,1,4,1,9,10,99,10,1,3),_CospfShamLinkNbrIpAddr_Type())
cospfShamLinkNbrIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinkNbrIpAddr.setStatus(_B)
_CospfShamLinkNbrRtrId_Type=RouterID
_CospfShamLinkNbrRtrId_Object=MibTableColumn
cospfShamLinkNbrRtrId=_CospfShamLinkNbrRtrId_Object((1,3,6,1,4,1,9,10,99,10,1,4),_CospfShamLinkNbrRtrId_Type())
cospfShamLinkNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkNbrRtrId.setStatus(_B)
class _CospfShamLinkNbrOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CospfShamLinkNbrOptions_Type.__name__=_E
_CospfShamLinkNbrOptions_Object=MibTableColumn
cospfShamLinkNbrOptions=_CospfShamLinkNbrOptions_Object((1,3,6,1,4,1,9,10,99,10,1,5),_CospfShamLinkNbrOptions_Type())
cospfShamLinkNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkNbrOptions.setStatus(_B)
class _CospfShamLinkNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('attempt',2),('init',3),('twoWay',4),('exchangeStart',5),('exchange',6),('loading',7),('full',8)))
_CospfShamLinkNbrState_Type.__name__=_E
_CospfShamLinkNbrState_Object=MibTableColumn
cospfShamLinkNbrState=_CospfShamLinkNbrState_Object((1,3,6,1,4,1,9,10,99,10,1,6),_CospfShamLinkNbrState_Type())
cospfShamLinkNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkNbrState.setStatus(_B)
_CospfShamLinkNbrEvents_Type=Counter32
_CospfShamLinkNbrEvents_Object=MibTableColumn
cospfShamLinkNbrEvents=_CospfShamLinkNbrEvents_Object((1,3,6,1,4,1,9,10,99,10,1,7),_CospfShamLinkNbrEvents_Type())
cospfShamLinkNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkNbrEvents.setStatus(_B)
_CospfShamLinkNbrLsRetransQLen_Type=Gauge32
_CospfShamLinkNbrLsRetransQLen_Object=MibTableColumn
cospfShamLinkNbrLsRetransQLen=_CospfShamLinkNbrLsRetransQLen_Object((1,3,6,1,4,1,9,10,99,10,1,8),_CospfShamLinkNbrLsRetransQLen_Type())
cospfShamLinkNbrLsRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkNbrLsRetransQLen.setStatus(_B)
_CospfShamLinkNbrHelloSuppressed_Type=TruthValue
_CospfShamLinkNbrHelloSuppressed_Object=MibTableColumn
cospfShamLinkNbrHelloSuppressed=_CospfShamLinkNbrHelloSuppressed_Object((1,3,6,1,4,1,9,10,99,10,1,9),_CospfShamLinkNbrHelloSuppressed_Type())
cospfShamLinkNbrHelloSuppressed.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinkNbrHelloSuppressed.setStatus(_B)
_CospfShamLinksTable_Object=MibTable
cospfShamLinksTable=_CospfShamLinksTable_Object((1,3,6,1,4,1,9,10,99,11))
if mibBuilder.loadTexts:cospfShamLinksTable.setStatus(_B)
_CospfShamLinksEntry_Object=MibTableRow
cospfShamLinksEntry=_CospfShamLinksEntry_Object((1,3,6,1,4,1,9,10,99,11,1))
cospfShamLinksEntry.setIndexNames((0,_A,_s),(0,_A,_N),(0,_A,_O),(0,_A,_t),(0,_A,_u))
if mibBuilder.loadTexts:cospfShamLinksEntry.setStatus(_B)
_CospfShamLinksAreaId_Type=AreaID
_CospfShamLinksAreaId_Object=MibTableColumn
cospfShamLinksAreaId=_CospfShamLinksAreaId_Object((1,3,6,1,4,1,9,10,99,11,1,1),_CospfShamLinksAreaId_Type())
cospfShamLinksAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinksAreaId.setStatus(_B)
_CospfShamLinksLocalIpAddrType_Type=InetAddressType
_CospfShamLinksLocalIpAddrType_Object=MibTableColumn
cospfShamLinksLocalIpAddrType=_CospfShamLinksLocalIpAddrType_Object((1,3,6,1,4,1,9,10,99,11,1,2),_CospfShamLinksLocalIpAddrType_Type())
cospfShamLinksLocalIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinksLocalIpAddrType.setStatus(_B)
_CospfShamLinksLocalIpAddr_Type=InetAddress
_CospfShamLinksLocalIpAddr_Object=MibTableColumn
cospfShamLinksLocalIpAddr=_CospfShamLinksLocalIpAddr_Object((1,3,6,1,4,1,9,10,99,11,1,3),_CospfShamLinksLocalIpAddr_Type())
cospfShamLinksLocalIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinksLocalIpAddr.setStatus(_B)
_CospfShamLinksRemoteIpAddrType_Type=InetAddressType
_CospfShamLinksRemoteIpAddrType_Object=MibTableColumn
cospfShamLinksRemoteIpAddrType=_CospfShamLinksRemoteIpAddrType_Object((1,3,6,1,4,1,9,10,99,11,1,4),_CospfShamLinksRemoteIpAddrType_Type())
cospfShamLinksRemoteIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinksRemoteIpAddrType.setStatus(_B)
_CospfShamLinksRemoteIpAddr_Type=InetAddress
_CospfShamLinksRemoteIpAddr_Object=MibTableColumn
cospfShamLinksRemoteIpAddr=_CospfShamLinksRemoteIpAddr_Object((1,3,6,1,4,1,9,10,99,11,1,5),_CospfShamLinksRemoteIpAddr_Type())
cospfShamLinksRemoteIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cospfShamLinksRemoteIpAddr.setStatus(_B)
class _CospfShamLinksRetransInterval_Type(UpToMaxAge):defaultValue=5
_CospfShamLinksRetransInterval_Type.__name__=_L
_CospfShamLinksRetransInterval_Object=MibTableColumn
cospfShamLinksRetransInterval=_CospfShamLinksRetransInterval_Object((1,3,6,1,4,1,9,10,99,11,1,6),_CospfShamLinksRetransInterval_Type())
cospfShamLinksRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinksRetransInterval.setStatus(_B)
class _CospfShamLinksHelloInterval_Type(HelloRange):defaultValue=10
_CospfShamLinksHelloInterval_Type.__name__=_J
_CospfShamLinksHelloInterval_Object=MibTableColumn
cospfShamLinksHelloInterval=_CospfShamLinksHelloInterval_Object((1,3,6,1,4,1,9,10,99,11,1,7),_CospfShamLinksHelloInterval_Type())
cospfShamLinksHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinksHelloInterval.setStatus(_B)
class _CospfShamLinksRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_CospfShamLinksRtrDeadInterval_Type.__name__=_K
_CospfShamLinksRtrDeadInterval_Object=MibTableColumn
cospfShamLinksRtrDeadInterval=_CospfShamLinksRtrDeadInterval_Object((1,3,6,1,4,1,9,10,99,11,1,8),_CospfShamLinksRtrDeadInterval_Type())
cospfShamLinksRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinksRtrDeadInterval.setStatus(_B)
class _CospfShamLinksState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_M,1),(_d,4)))
_CospfShamLinksState_Type.__name__=_E
_CospfShamLinksState_Object=MibTableColumn
cospfShamLinksState=_CospfShamLinksState_Object((1,3,6,1,4,1,9,10,99,11,1,9),_CospfShamLinksState_Type())
cospfShamLinksState.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinksState.setStatus(_B)
_CospfShamLinksEvents_Type=Counter32
_CospfShamLinksEvents_Object=MibTableColumn
cospfShamLinksEvents=_CospfShamLinksEvents_Object((1,3,6,1,4,1,9,10,99,11,1,10),_CospfShamLinksEvents_Type())
cospfShamLinksEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinksEvents.setStatus(_B)
_CospfShamLinksMetric_Type=Metric
_CospfShamLinksMetric_Object=MibTableColumn
cospfShamLinksMetric=_CospfShamLinksMetric_Object((1,3,6,1,4,1,9,10,99,11,1,11),_CospfShamLinksMetric_Type())
cospfShamLinksMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cospfShamLinksMetric.setStatus(_B)
ospfAreaEntry.registerAugmentions((_A,_v))
cospfAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_A,_w))
cospfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_A,_x))
cospfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
cospfLsdbGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,1))
cospfLsdbGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:cospfLsdbGroup.setStatus(_B)
cospfLocalLsdbGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,2))
cospfLocalLsdbGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cospfLocalLsdbGroup.setStatus(_B)
cospfVirtLocalLsdbGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,3))
cospfVirtLocalLsdbGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cospfVirtLocalLsdbGroup.setStatus(_B)
cospfBasicGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,4))
cospfBasicGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:cospfBasicGroup.setStatus(_B)
cospfAreaGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,5))
cospfAreaGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:cospfAreaGroup.setStatus(_B)
cospfIfGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,6))
cospfIfGroup.setObjects(*((_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:cospfIfGroup.setStatus(_B)
cospfVirtIfGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,7))
cospfVirtIfGroup.setObjects(*((_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cospfVirtIfGroup.setStatus(_B)
cospfShamLinkGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,8))
cospfShamLinkGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:cospfShamLinkGroup.setStatus(_F)
cospfShamLinkNbrGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,9))
cospfShamLinkNbrGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:cospfShamLinkNbrGroup.setStatus(_B)
cospfShamLinksGroup=ObjectGroup((1,3,6,1,4,1,9,10,99,9,1,10))
cospfShamLinksGroup.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:cospfShamLinksGroup.setStatus(_B)
cospfCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,99,9,2,1))
cospfCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_Ag),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cospfCompliance.setStatus(_F)
cospfComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,99,9,2,2))
cospfComplianceRev1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_Ah),(_A,_Ai),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cospfComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cospf':cospf,'cospfGeneralGroup':cospfGeneralGroup,_AA:cospfRFC1583Compatibility,_AB:cospfOpaqueLsaSupport,_AC:cospfTrafficEngineeringSupport,_AD:cospfOpaqueASLsaCount,_AE:cospfOpaqueASLsaCksumSum,'cospfAreaTable':cospfAreaTable,_v:cospfAreaEntry,_AF:cospfOpaqueAreaLsaCount,_AG:cospfOpaqueAreaLsaCksumSum,_AH:cospfAreaNssaTranslatorRole,_AI:cospfAreaNssaTranslatorState,_AJ:cospfAreaNssaTranslatorEvents,'cospfLsdbTable':cospfLsdbTable,'cospfLsdbEntry':cospfLsdbEntry,_Z:cospfLsdbType,_y:cospfLsdbSequence,_z:cospfLsdbAge,_A0:cospfLsdbChecksum,_A1:cospfLsdbAdvertisement,'cospfIfTable':cospfIfTable,_w:cospfIfEntry,_AK:cospfIfLsaCount,_AL:cospfIfLsaCksumSum,'cospfVirtIfTable':cospfVirtIfTable,_x:cospfVirtIfEntry,_AM:cospfVirtIfLsaCount,_AN:cospfVirtIfLsaCksumSum,'cospfShamLinkTable':cospfShamLinkTable,'cospfShamLinkEntry':cospfShamLinkEntry,_a:cospfShamLinkAreaId,_b:cospfShamLinkLocalIpAddress,_c:cospfShamLinkNeighborId,_AO:cospfShamLinkRetransInterval,_AP:cospfShamLinkHelloInterval,_AQ:cospfShamLinkRtrDeadInterval,_AR:cospfShamLinkState,_AS:cospfShamLinkEvents,_AT:cospfShamLinkMetric,'cospfLocalLsdbTable':cospfLocalLsdbTable,'cospfLocalLsdbEntry':cospfLocalLsdbEntry,_e:cospfLocalLsdbIpAddress,_f:cospfLocalLsdbAddressLessIf,_g:cospfLocalLsdbType,_h:cospfLocalLsdbLsid,_i:cospfLocalLsdbRouterId,_A2:cospfLocalLsdbSequence,_A3:cospfLocalLsdbAge,_A4:cospfLocalLsdbChecksum,_A5:cospfLocalLsdbAdvertisement,'cospfVirtLocalLsdbTable':cospfVirtLocalLsdbTable,'cospfVirtLocalLsdbEntry':cospfVirtLocalLsdbEntry,_k:cospfVirtLocalLsdbTransitArea,_l:cospfVirtLocalLsdbNeighbor,_m:cospfVirtLocalLsdbType,_n:cospfVirtLocalLsdbLsid,_o:cospfVirtLocalLsdbRouterId,_A6:cospfVirtLocalLsdbSequence,_A7:cospfVirtLocalLsdbAge,_A8:cospfVirtLocalLsdbChecksum,_A9:cospfVirtLocalLsdbAdvertisement,'cospfConformance':cospfConformance,'cospfGroups':cospfGroups,_T:cospfLsdbGroup,_U:cospfLocalLsdbGroup,_V:cospfVirtLocalLsdbGroup,_P:cospfBasicGroup,_Q:cospfAreaGroup,_R:cospfIfGroup,_S:cospfVirtIfGroup,_Ag:cospfShamLinkGroup,_Ai:cospfShamLinkNbrGroup,_Ah:cospfShamLinksGroup,'cospfCompliances':cospfCompliances,'cospfCompliance':cospfCompliance,'cospfComplianceRev1':cospfComplianceRev1,'cospfShamLinkNbrTable':cospfShamLinkNbrTable,'cospfShamLinkNbrEntry':cospfShamLinkNbrEntry,_p:cospfShamLinkNbrArea,_q:cospfShamLinkNbrIpAddrType,_r:cospfShamLinkNbrIpAddr,_AU:cospfShamLinkNbrRtrId,_AV:cospfShamLinkNbrOptions,_AW:cospfShamLinkNbrState,_AX:cospfShamLinkNbrEvents,_AY:cospfShamLinkNbrLsRetransQLen,_AZ:cospfShamLinkNbrHelloSuppressed,'cospfShamLinksTable':cospfShamLinksTable,'cospfShamLinksEntry':cospfShamLinksEntry,_s:cospfShamLinksAreaId,_N:cospfShamLinksLocalIpAddrType,_O:cospfShamLinksLocalIpAddr,_t:cospfShamLinksRemoteIpAddrType,_u:cospfShamLinksRemoteIpAddr,_Aa:cospfShamLinksRetransInterval,_Ab:cospfShamLinksHelloInterval,_Ac:cospfShamLinksRtrDeadInterval,_Ad:cospfShamLinksState,_Ae:cospfShamLinksEvents,_Af:cospfShamLinksMetric})