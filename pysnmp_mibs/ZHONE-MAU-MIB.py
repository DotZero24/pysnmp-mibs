_AK='linkAggLink2Trap'
_AJ='linkAggLink1Trap'
_AI='rprWestSpanTrap'
_AH='rprEastSpanTrap'
_AG='zhoneLinkAggIfIndex'
_AF='linkFailure'
_AE='bFdxBPause'
_AD='bFdxSPause'
_AC='bFdxAPause'
_AB='bFdxPause'
_AA='mau10gBaseEW'
_A9='mau10gBaseER'
_A8='mau10gBaseLW'
_A7='mau10gBaseLR'
_A6='mau10gBaseSW'
_A5='mau10gBaseSR'
_A4='mau10gBaseLX4'
_A3='mau10gBaseW'
_A2='mau10gBaseR'
_A1='mau10gBaseX'
_A0='mau1000BaseTFD'
_z='mau1000BaseTHD'
_y='mau1000BaseSXFD'
_x='mau1000BaseSXHD'
_w='mau1000BaseLXFD'
_v='mau1000BaseLXHD'
_u='mau100BaseTXFD'
_t='mau100BaseTXHD'
_s='mau10BaseTFD'
_r='mau10BaseTHD'
_q='mau10BaseT'
_p='mauOther'
_o='InterfaceIndexOrZero'
_n='OctetString'
_m='b1000baseT'
_l='b1000baseX'
_k='b100baseT2'
_j='b100baseTX'
_i='disabled'
_h='autoNegError'
_g='offline'
_f='unknown'
_e='zhoneMauIfIndex'
_d='ifOperStatus'
_c='ifName'
_b='ifIndex'
_a='ifAdminStatus'
_Z='b10gbaseEW'
_Y='b10gbaseER'
_X='b10gbaseLW'
_W='b10gbaseLR'
_V='b10gbaseSW'
_U='b10gbaseSR'
_T='b10gbaseLX4'
_S='b10gbaseW'
_R='b10gbaseR'
_Q='b10gbaseX'
_P='b1000baseTFD'
_O='b1000baseXFD'
_N='b100baseT2FD'
_M='b100baseTXFD'
_L='b100baseT4'
_K='b10baseTFD'
_J='b10baseT'
_I='bOther'
_H='other'
_G='Bits'
_F='ZHONE-MAU-MIB'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_n,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifAdminStatus,ifIndex,ifName,ifOperStatus=mibBuilder.importSymbols(_E,_o,_a,_b,_c,_d)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
zhoneEnet,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneEnet','zhoneModules')
phyEnetMauMib=ModuleIdentity((1,3,6,1,4,1,5504,6,8))
if mibBuilder.loadTexts:phyEnetMauMib.setRevisions(('2013-10-13 17:08','2012-05-25 14:55','2009-02-03 01:39','2009-01-19 21:44','2008-08-14 07:17','2008-03-10 12:03','2007-11-01 14:37','2007-06-24 23:11','2007-05-22 16:05','2005-10-13 16:55','2000-09-12 18:01'))
_ZhoneIfMauTable_Object=MibTable
zhoneIfMauTable=_ZhoneIfMauTable_Object((1,3,6,1,4,1,5504,5,1,1))
if mibBuilder.loadTexts:zhoneIfMauTable.setStatus(_A)
_ZhoneIfMauEntry_Object=MibTableRow
zhoneIfMauEntry=_ZhoneIfMauEntry_Object((1,3,6,1,4,1,5504,5,1,1,1))
zhoneIfMauEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:zhoneIfMauEntry.setStatus(_A)
class _ZhoneMauIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneMauIfIndex_Type.__name__=_B
_ZhoneMauIfIndex_Object=MibTableColumn
zhoneMauIfIndex=_ZhoneMauIfIndex_Object((1,3,6,1,4,1,5504,5,1,1,1,1),_ZhoneMauIfIndex_Type())
zhoneMauIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauIfIndex.setStatus(_A)
class _ZhoneMauType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,10,11,15,16,22,23,25,26,29,30,31,32,33,34,35,36,37,38,39,40)));namedValues=NamedValues(*((_p,1),(_q,5),(_r,10),(_s,11),(_t,15),(_u,16),(_v,22),(_w,23),(_x,25),(_y,26),(_z,29),(_A0,30),(_A1,31),(_A2,32),(_A3,33),(_A4,34),(_A5,35),(_A6,36),(_A7,37),(_A8,38),(_A9,39),(_AA,40)))
_ZhoneMauType_Type.__name__=_B
_ZhoneMauType_Object=MibTableColumn
zhoneMauType=_ZhoneMauType_Object((1,3,6,1,4,1,5504,5,1,1,1,2),_ZhoneMauType_Type())
zhoneMauType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauType.setStatus(_A)
class _ZhoneMauOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_f,2),('operational',3),('standby',4),('shutdown',5),('reset',6)))
_ZhoneMauOperStatus_Type.__name__=_B
_ZhoneMauOperStatus_Object=MibTableColumn
zhoneMauOperStatus=_ZhoneMauOperStatus_Object((1,3,6,1,4,1,5504,5,1,1,1,3),_ZhoneMauOperStatus_Type())
zhoneMauOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauOperStatus.setStatus(_A)
class _ZhoneMauMediaAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_f,2),('available',3),('notAvailable',4),('remoteFault',5),('invalidSignal',6),('remoteJabber',7),('remoteLinkLoss',8),('remoteTest',9),(_g,10),(_h,11)))
_ZhoneMauMediaAvailable_Type.__name__=_B
_ZhoneMauMediaAvailable_Object=MibTableColumn
zhoneMauMediaAvailable=_ZhoneMauMediaAvailable_Object((1,3,6,1,4,1,5504,5,1,1,1,4),_ZhoneMauMediaAvailable_Type())
zhoneMauMediaAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauMediaAvailable.setStatus(_A)
_ZhoneMauMediaAvailStateExits_Type=Counter32
_ZhoneMauMediaAvailStateExits_Object=MibTableColumn
zhoneMauMediaAvailStateExits=_ZhoneMauMediaAvailStateExits_Object((1,3,6,1,4,1,5504,5,1,1,1,5),_ZhoneMauMediaAvailStateExits_Type())
zhoneMauMediaAvailStateExits.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauMediaAvailStateExits.setStatus(_A)
class _ZhoneMauJabberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_f,2),('noJabber',3),('jabbering',4)))
_ZhoneMauJabberState_Type.__name__=_B
_ZhoneMauJabberState_Object=MibTableColumn
zhoneMauJabberState=_ZhoneMauJabberState_Object((1,3,6,1,4,1,5504,5,1,1,1,6),_ZhoneMauJabberState_Type())
zhoneMauJabberState.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauJabberState.setStatus(_A)
_ZhoneMauJabberingStateEnters_Type=Counter32
_ZhoneMauJabberingStateEnters_Object=MibTableColumn
zhoneMauJabberingStateEnters=_ZhoneMauJabberingStateEnters_Object((1,3,6,1,4,1,5504,5,1,1,1,7),_ZhoneMauJabberingStateEnters_Type())
zhoneMauJabberingStateEnters.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauJabberingStateEnters.setStatus(_A)
_ZhoneMauFalseCarriers_Type=Counter32
_ZhoneMauFalseCarriers_Object=MibTableColumn
zhoneMauFalseCarriers=_ZhoneMauFalseCarriers_Object((1,3,6,1,4,1,5504,5,1,1,1,8),_ZhoneMauFalseCarriers_Type())
zhoneMauFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauFalseCarriers.setStatus(_A)
class _ZhoneMauDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,10,11,15,16,22,23,25,26,29,30,31,32,33,34,35,36,37,38,39,40)));namedValues=NamedValues(*((_p,1),(_q,5),(_r,10),(_s,11),(_t,15),(_u,16),(_v,22),(_w,23),(_x,25),(_y,26),(_z,29),(_A0,30),(_A1,31),(_A2,32),(_A3,33),(_A4,34),(_A5,35),(_A6,36),(_A7,37),(_A8,38),(_A9,39),(_AA,40)))
_ZhoneMauDefaultType_Type.__name__=_B
_ZhoneMauDefaultType_Object=MibTableColumn
zhoneMauDefaultType=_ZhoneMauDefaultType_Object((1,3,6,1,4,1,5504,5,1,1,1,9),_ZhoneMauDefaultType_Type())
zhoneMauDefaultType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauDefaultType.setStatus(_A)
_ZhoneMauAutoNegSupported_Type=TruthValue
_ZhoneMauAutoNegSupported_Object=MibTableColumn
zhoneMauAutoNegSupported=_ZhoneMauAutoNegSupported_Object((1,3,6,1,4,1,5504,5,1,1,1,10),_ZhoneMauAutoNegSupported_Type())
zhoneMauAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauAutoNegSupported.setStatus(_A)
class _ZhoneMauTypeListBits_Type(Bits):namedValues=NamedValues(*((_I,0),('bAUI',1),('b10base5',2),('bFoirl',3),('b10base2',4),(_J,5),('b10baseFP',6),('b10baseFB',7),('b10baseFL',8),('b10broad36',9),('b10baseTHD',10),(_K,11),('b10baseFLHD',12),('b10baseFLFD',13),(_L,14),('b100baseTXHD',15),(_M,16),('b100baseFXHD',17),('b100baseFXFD',18),('b100baseT2HD',19),(_N,20),('b1000baseXHD',21),(_O,22),('b1000baseLXHD',23),('b1000baseLXFD',24),('b1000baseSXHD',25),('b1000baseSXFD',26),('b1000baseCXHD',27),('b1000baseCXFD',28),('b1000baseTHD',29),(_P,30),(_Q,31),(_R,32),(_S,33),(_T,34),(_U,35),(_V,36),(_W,37),(_X,38),(_Y,39),(_Z,40)))
_ZhoneMauTypeListBits_Type.__name__=_G
_ZhoneMauTypeListBits_Object=MibTableColumn
zhoneMauTypeListBits=_ZhoneMauTypeListBits_Object((1,3,6,1,4,1,5504,5,1,1,1,11),_ZhoneMauTypeListBits_Type())
zhoneMauTypeListBits.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauTypeListBits.setStatus(_A)
class _ZhoneMauClkSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unused',1),('automatic',2),('master',3),('slave',4)))
_ZhoneMauClkSrc_Type.__name__=_B
_ZhoneMauClkSrc_Object=MibTableColumn
zhoneMauClkSrc=_ZhoneMauClkSrc_Object((1,3,6,1,4,1,5504,5,1,1,1,12),_ZhoneMauClkSrc_Type())
zhoneMauClkSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauClkSrc.setStatus(_A)
class _ZhoneMauPauseFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_i,1),('asymmetricTx',2),('asymmetricRx',3),('symmetric',4),('passthrough',5)))
_ZhoneMauPauseFlowControl_Type.__name__=_B
_ZhoneMauPauseFlowControl_Object=MibTableColumn
zhoneMauPauseFlowControl=_ZhoneMauPauseFlowControl_Object((1,3,6,1,4,1,5504,5,1,1,1,13),_ZhoneMauPauseFlowControl_Type())
zhoneMauPauseFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauPauseFlowControl.setStatus(_A)
class _ZhoneMauAggregationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),('off',2),('passive',3),('active',4)))
_ZhoneMauAggregationMode_Type.__name__=_B
_ZhoneMauAggregationMode_Object=MibTableColumn
zhoneMauAggregationMode=_ZhoneMauAggregationMode_Object((1,3,6,1,4,1,5504,5,1,1,1,14),_ZhoneMauAggregationMode_Type())
zhoneMauAggregationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauAggregationMode.setStatus(_A)
class _ZhoneMauLinkStateMirror_Type(InterfaceIndexOrZero):defaultValue=0
_ZhoneMauLinkStateMirror_Type.__name__=_o
_ZhoneMauLinkStateMirror_Object=MibTableColumn
zhoneMauLinkStateMirror=_ZhoneMauLinkStateMirror_Object((1,3,6,1,4,1,5504,5,1,1,1,15),_ZhoneMauLinkStateMirror_Type())
zhoneMauLinkStateMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauLinkStateMirror.setStatus(_A)
class _ZhoneMauSetPauseTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhoneMauSetPauseTime_Type.__name__=_B
_ZhoneMauSetPauseTime_Object=MibTableColumn
zhoneMauSetPauseTime=_ZhoneMauSetPauseTime_Object((1,3,6,1,4,1,5504,5,1,1,1,16),_ZhoneMauSetPauseTime_Type())
zhoneMauSetPauseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauSetPauseTime.setStatus(_A)
class _ZhoneMauMaxFrameSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15360))
_ZhoneMauMaxFrameSize_Type.__name__=_B
_ZhoneMauMaxFrameSize_Object=MibTableColumn
zhoneMauMaxFrameSize=_ZhoneMauMaxFrameSize_Object((1,3,6,1,4,1,5504,5,1,1,1,17),_ZhoneMauMaxFrameSize_Type())
zhoneMauMaxFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauMaxFrameSize.setStatus(_A)
class _ZhoneMauIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10240000))
_ZhoneMauIngressRate_Type.__name__=_B
_ZhoneMauIngressRate_Object=MibTableColumn
zhoneMauIngressRate=_ZhoneMauIngressRate_Object((1,3,6,1,4,1,5504,5,1,1,1,18),_ZhoneMauIngressRate_Type())
zhoneMauIngressRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauIngressRate.setStatus(_A)
if mibBuilder.loadTexts:zhoneMauIngressRate.setUnits('Kbps')
class _ZhoneMauIngressBurstSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_ZhoneMauIngressBurstSize_Type.__name__=_B
_ZhoneMauIngressBurstSize_Object=MibTableColumn
zhoneMauIngressBurstSize=_ZhoneMauIngressBurstSize_Object((1,3,6,1,4,1,5504,5,1,1,1,19),_ZhoneMauIngressBurstSize_Type())
zhoneMauIngressBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauIngressBurstSize.setStatus(_A)
if mibBuilder.loadTexts:zhoneMauIngressBurstSize.setUnits('Kbits')
class _ZhoneMauEgressRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10240000))
_ZhoneMauEgressRate_Type.__name__=_B
_ZhoneMauEgressRate_Object=MibTableColumn
zhoneMauEgressRate=_ZhoneMauEgressRate_Object((1,3,6,1,4,1,5504,5,1,1,1,20),_ZhoneMauEgressRate_Type())
zhoneMauEgressRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauEgressRate.setStatus(_A)
if mibBuilder.loadTexts:zhoneMauEgressRate.setUnits('Kbps')
class _ZhoneMauEgressBurstSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_ZhoneMauEgressBurstSize_Type.__name__=_B
_ZhoneMauEgressBurstSize_Object=MibTableColumn
zhoneMauEgressBurstSize=_ZhoneMauEgressBurstSize_Object((1,3,6,1,4,1,5504,5,1,1,1,21),_ZhoneMauEgressBurstSize_Type())
zhoneMauEgressBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauEgressBurstSize.setStatus(_A)
if mibBuilder.loadTexts:zhoneMauEgressBurstSize.setUnits('Kbits')
_ZhoneMauAutoNegTable_Object=MibTable
zhoneMauAutoNegTable=_ZhoneMauAutoNegTable_Object((1,3,6,1,4,1,5504,5,1,2))
if mibBuilder.loadTexts:zhoneMauAutoNegTable.setStatus(_A)
_ZhoneMauAutoNegEntry_Object=MibTableRow
zhoneMauAutoNegEntry=_ZhoneMauAutoNegEntry_Object((1,3,6,1,4,1,5504,5,1,2,1))
zhoneMauAutoNegEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:zhoneMauAutoNegEntry.setStatus(_A)
class _ZhoneMauAutoNegAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_i,2)))
_ZhoneMauAutoNegAdminStatus_Type.__name__=_B
_ZhoneMauAutoNegAdminStatus_Object=MibTableColumn
zhoneMauAutoNegAdminStatus=_ZhoneMauAutoNegAdminStatus_Object((1,3,6,1,4,1,5504,5,1,2,1,1),_ZhoneMauAutoNegAdminStatus_Type())
zhoneMauAutoNegAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauAutoNegAdminStatus.setStatus(_A)
class _ZhoneMauAutoNegRemoteSignaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notdetected',2)))
_ZhoneMauAutoNegRemoteSignaling_Type.__name__=_B
_ZhoneMauAutoNegRemoteSignaling_Object=MibTableColumn
zhoneMauAutoNegRemoteSignaling=_ZhoneMauAutoNegRemoteSignaling_Object((1,3,6,1,4,1,5504,5,1,2,1,2),_ZhoneMauAutoNegRemoteSignaling_Type())
zhoneMauAutoNegRemoteSignaling.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauAutoNegRemoteSignaling.setStatus(_A)
class _ZhoneMauAutoNegConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('configuring',2),('complete',3),(_i,4),('parallelDetectFail',5)))
_ZhoneMauAutoNegConfig_Type.__name__=_B
_ZhoneMauAutoNegConfig_Object=MibTableColumn
zhoneMauAutoNegConfig=_ZhoneMauAutoNegConfig_Object((1,3,6,1,4,1,5504,5,1,2,1,3),_ZhoneMauAutoNegConfig_Type())
zhoneMauAutoNegConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauAutoNegConfig.setStatus(_A)
class _ZhoneMauAutoNegRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('norestart',2)))
_ZhoneMauAutoNegRestart_Type.__name__=_B
_ZhoneMauAutoNegRestart_Object=MibTableColumn
zhoneMauAutoNegRestart=_ZhoneMauAutoNegRestart_Object((1,3,6,1,4,1,5504,5,1,2,1,4),_ZhoneMauAutoNegRestart_Type())
zhoneMauAutoNegRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauAutoNegRestart.setStatus(_A)
class _ZhoneMauAutoNegCapabilityBits_Type(Bits):namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_j,4),(_M,5),(_k,6),(_N,7),('bfdxPause',8),('bfdxAPause',9),('bfdxSPause',10),('bfdxBPause',11),(_l,12),(_O,13),(_m,14),(_P,15),(_Q,16),(_R,17),(_S,18),(_T,19),(_U,20),(_V,21),(_W,22),(_X,23),(_Y,24),(_Z,25)))
_ZhoneMauAutoNegCapabilityBits_Type.__name__=_G
_ZhoneMauAutoNegCapabilityBits_Object=MibTableColumn
zhoneMauAutoNegCapabilityBits=_ZhoneMauAutoNegCapabilityBits_Object((1,3,6,1,4,1,5504,5,1,2,1,5),_ZhoneMauAutoNegCapabilityBits_Type())
zhoneMauAutoNegCapabilityBits.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauAutoNegCapabilityBits.setStatus(_A)
class _ZhoneMauAutoNegCapAdvertBits_Type(Bits):namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_j,4),(_M,5),(_k,6),(_N,7),(_AB,8),(_AC,9),(_AD,10),(_AE,11),(_l,12),(_O,13),(_m,14),(_P,15),(_Q,16),(_R,17),(_S,18),(_T,19),(_U,20),(_V,21),(_W,22),(_X,23),(_Y,24),(_Z,25)))
_ZhoneMauAutoNegCapAdvertBits_Type.__name__=_G
_ZhoneMauAutoNegCapAdvertBits_Object=MibTableColumn
zhoneMauAutoNegCapAdvertBits=_ZhoneMauAutoNegCapAdvertBits_Object((1,3,6,1,4,1,5504,5,1,2,1,6),_ZhoneMauAutoNegCapAdvertBits_Type())
zhoneMauAutoNegCapAdvertBits.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauAutoNegCapAdvertBits.setStatus(_A)
class _ZhoneMauAutoNegCapRecvBits_Type(Bits):namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_j,4),(_M,5),(_k,6),(_N,7),(_AB,8),(_AC,9),(_AD,10),(_AE,11),(_l,12),(_O,13),(_m,14),(_P,15),(_Q,16),(_R,17),(_S,18),(_T,19),(_U,20),(_V,21),(_W,22),(_X,23),(_Y,24),(_Z,25)))
_ZhoneMauAutoNegCapRecvBits_Type.__name__=_G
_ZhoneMauAutoNegCapRecvBits_Object=MibTableColumn
zhoneMauAutoNegCapRecvBits=_ZhoneMauAutoNegCapRecvBits_Object((1,3,6,1,4,1,5504,5,1,2,1,7),_ZhoneMauAutoNegCapRecvBits_Type())
zhoneMauAutoNegCapRecvBits.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauAutoNegCapRecvBits.setStatus(_A)
class _ZhoneMauAutoNegRemoteFaultAdvert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noError',1),(_g,2),(_AF,3),(_h,4)))
_ZhoneMauAutoNegRemoteFaultAdvert_Type.__name__=_B
_ZhoneMauAutoNegRemoteFaultAdvert_Object=MibTableColumn
zhoneMauAutoNegRemoteFaultAdvert=_ZhoneMauAutoNegRemoteFaultAdvert_Object((1,3,6,1,4,1,5504,5,1,2,1,8),_ZhoneMauAutoNegRemoteFaultAdvert_Type())
zhoneMauAutoNegRemoteFaultAdvert.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneMauAutoNegRemoteFaultAdvert.setStatus(_A)
class _ZhoneMauAutoNegRemoteFaultRecv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noError',1),(_g,2),(_AF,3),(_h,4)))
_ZhoneMauAutoNegRemoteFaultRecv_Type.__name__=_B
_ZhoneMauAutoNegRemoteFaultRecv_Object=MibTableColumn
zhoneMauAutoNegRemoteFaultRecv=_ZhoneMauAutoNegRemoteFaultRecv_Object((1,3,6,1,4,1,5504,5,1,2,1,9),_ZhoneMauAutoNegRemoteFaultRecv_Type())
zhoneMauAutoNegRemoteFaultRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneMauAutoNegRemoteFaultRecv.setStatus(_A)
_ZhoneEnetTraps_ObjectIdentity=ObjectIdentity
zhoneEnetTraps=_ZhoneEnetTraps_ObjectIdentity((1,3,6,1,4,1,5504,5,1,3))
if mibBuilder.loadTexts:zhoneEnetTraps.setStatus(_A)
_EnetV2Traps_ObjectIdentity=ObjectIdentity
enetV2Traps=_EnetV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,5,1,3,0))
if mibBuilder.loadTexts:enetV2Traps.setStatus(_A)
_ZhoneLinkAggTable_Object=MibTable
zhoneLinkAggTable=_ZhoneLinkAggTable_Object((1,3,6,1,4,1,5504,5,1,4))
if mibBuilder.loadTexts:zhoneLinkAggTable.setStatus(_A)
_ZhoneLinkAggEntry_Object=MibTableRow
zhoneLinkAggEntry=_ZhoneLinkAggEntry_Object((1,3,6,1,4,1,5504,5,1,4,1))
zhoneLinkAggEntry.setIndexNames((0,_F,_AG))
if mibBuilder.loadTexts:zhoneLinkAggEntry.setStatus(_A)
class _ZhoneLinkAggIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneLinkAggIfIndex_Type.__name__=_B
_ZhoneLinkAggIfIndex_Object=MibTableColumn
zhoneLinkAggIfIndex=_ZhoneLinkAggIfIndex_Object((1,3,6,1,4,1,5504,5,1,4,1,1),_ZhoneLinkAggIfIndex_Type())
zhoneLinkAggIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneLinkAggIfIndex.setStatus(_A)
class _ZhoneLinkAggPartnerSystem_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_ZhoneLinkAggPartnerSystem_Type.__name__=_n
_ZhoneLinkAggPartnerSystem_Object=MibTableColumn
zhoneLinkAggPartnerSystem=_ZhoneLinkAggPartnerSystem_Object((1,3,6,1,4,1,5504,5,1,4,1,2),_ZhoneLinkAggPartnerSystem_Type())
zhoneLinkAggPartnerSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneLinkAggPartnerSystem.setStatus(_A)
_ZhoneLinkAggPartnerSystemPriority_Type=Integer32
_ZhoneLinkAggPartnerSystemPriority_Object=MibTableColumn
zhoneLinkAggPartnerSystemPriority=_ZhoneLinkAggPartnerSystemPriority_Object((1,3,6,1,4,1,5504,5,1,4,1,3),_ZhoneLinkAggPartnerSystemPriority_Type())
zhoneLinkAggPartnerSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneLinkAggPartnerSystemPriority.setStatus(_A)
_ZhoneLinkAggPartnerGroupId_Type=Integer32
_ZhoneLinkAggPartnerGroupId_Object=MibTableColumn
zhoneLinkAggPartnerGroupId=_ZhoneLinkAggPartnerGroupId_Object((1,3,6,1,4,1,5504,5,1,4,1,4),_ZhoneLinkAggPartnerGroupId_Type())
zhoneLinkAggPartnerGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneLinkAggPartnerGroupId.setStatus(_A)
rprEastSpanTrap=NotificationType((1,3,6,1,4,1,5504,5,1,3,0,1))
rprEastSpanTrap.setObjects(*((_E,_b),(_E,_a),(_E,_d),(_E,_c)))
if mibBuilder.loadTexts:rprEastSpanTrap.setStatus(_A)
rprWestSpanTrap=NotificationType((1,3,6,1,4,1,5504,5,1,3,0,2))
rprWestSpanTrap.setObjects(*((_E,_b),(_E,_a),(_E,_d),(_E,_c)))
if mibBuilder.loadTexts:rprWestSpanTrap.setStatus(_A)
linkAggLink1Trap=NotificationType((1,3,6,1,4,1,5504,5,1,3,0,3))
if mibBuilder.loadTexts:linkAggLink1Trap.setStatus(_A)
linkAggLink2Trap=NotificationType((1,3,6,1,4,1,5504,5,1,3,0,4))
if mibBuilder.loadTexts:linkAggLink2Trap.setStatus(_A)
rprSpanGroup=NotificationGroup((1,3,6,1,4,1,5504,5,1,3,2))
rprSpanGroup.setObjects(*((_F,_AH),(_F,_AI)))
if mibBuilder.loadTexts:rprSpanGroup.setStatus(_A)
linkAggLinkGroup=NotificationGroup((1,3,6,1,4,1,5504,5,1,3,3))
linkAggLinkGroup.setObjects(*((_F,_AJ),(_F,_AK)))
if mibBuilder.loadTexts:linkAggLinkGroup.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zhoneIfMauTable':zhoneIfMauTable,'zhoneIfMauEntry':zhoneIfMauEntry,_e:zhoneMauIfIndex,'zhoneMauType':zhoneMauType,'zhoneMauOperStatus':zhoneMauOperStatus,'zhoneMauMediaAvailable':zhoneMauMediaAvailable,'zhoneMauMediaAvailStateExits':zhoneMauMediaAvailStateExits,'zhoneMauJabberState':zhoneMauJabberState,'zhoneMauJabberingStateEnters':zhoneMauJabberingStateEnters,'zhoneMauFalseCarriers':zhoneMauFalseCarriers,'zhoneMauDefaultType':zhoneMauDefaultType,'zhoneMauAutoNegSupported':zhoneMauAutoNegSupported,'zhoneMauTypeListBits':zhoneMauTypeListBits,'zhoneMauClkSrc':zhoneMauClkSrc,'zhoneMauPauseFlowControl':zhoneMauPauseFlowControl,'zhoneMauAggregationMode':zhoneMauAggregationMode,'zhoneMauLinkStateMirror':zhoneMauLinkStateMirror,'zhoneMauSetPauseTime':zhoneMauSetPauseTime,'zhoneMauMaxFrameSize':zhoneMauMaxFrameSize,'zhoneMauIngressRate':zhoneMauIngressRate,'zhoneMauIngressBurstSize':zhoneMauIngressBurstSize,'zhoneMauEgressRate':zhoneMauEgressRate,'zhoneMauEgressBurstSize':zhoneMauEgressBurstSize,'zhoneMauAutoNegTable':zhoneMauAutoNegTable,'zhoneMauAutoNegEntry':zhoneMauAutoNegEntry,'zhoneMauAutoNegAdminStatus':zhoneMauAutoNegAdminStatus,'zhoneMauAutoNegRemoteSignaling':zhoneMauAutoNegRemoteSignaling,'zhoneMauAutoNegConfig':zhoneMauAutoNegConfig,'zhoneMauAutoNegRestart':zhoneMauAutoNegRestart,'zhoneMauAutoNegCapabilityBits':zhoneMauAutoNegCapabilityBits,'zhoneMauAutoNegCapAdvertBits':zhoneMauAutoNegCapAdvertBits,'zhoneMauAutoNegCapRecvBits':zhoneMauAutoNegCapRecvBits,'zhoneMauAutoNegRemoteFaultAdvert':zhoneMauAutoNegRemoteFaultAdvert,'zhoneMauAutoNegRemoteFaultRecv':zhoneMauAutoNegRemoteFaultRecv,'zhoneEnetTraps':zhoneEnetTraps,'enetV2Traps':enetV2Traps,_AH:rprEastSpanTrap,_AI:rprWestSpanTrap,_AJ:linkAggLink1Trap,_AK:linkAggLink2Trap,'rprSpanGroup':rprSpanGroup,'linkAggLinkGroup':linkAggLinkGroup,'zhoneLinkAggTable':zhoneLinkAggTable,'zhoneLinkAggEntry':zhoneLinkAggEntry,_AG:zhoneLinkAggIfIndex,'zhoneLinkAggPartnerSystem':zhoneLinkAggPartnerSystem,'zhoneLinkAggPartnerSystemPriority':zhoneLinkAggPartnerSystemPriority,'zhoneLinkAggPartnerGroupId':zhoneLinkAggPartnerGroupId,'phyEnetMauMib':phyEnetMauMib})