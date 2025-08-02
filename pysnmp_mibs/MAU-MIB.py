_AR='mauIfGrpHCStats'
_AQ='mauBroadBasic'
_AP='mauIfGrpAutoNeg'
_AO='mauIfGrp100Mbs'
_AN='ifMauJabberTrap'
_AM='rpMauJabberTrap'
_AL='ifMauHCFalseCarriers'
_AK='ifMauAutoNegRemoteFaultReceived'
_AJ='ifMauAutoNegRemoteFaultAdvertised'
_AI='ifMauAutoNegCapReceivedBits'
_AH='ifMauAutoNegCapAdvertisedBits'
_AG='ifMauAutoNegCapabilityBits'
_AF='ifMauTypeListBits'
_AE='broadMauTranslationFreq'
_AD='broadMauXmtCarrierFreq'
_AC='broadMauXmtRcvSplitType'
_AB='ifMauAutoNegCapReceived'
_AA='ifMauAutoNegCapAdvertised'
_A9='ifMauAutoNegCapability'
_A8='ifJackType'
_A7='ifMauTypeList'
_A6='ifMauJabberingStateEnters'
_A5='ifMauMediaAvailableStateExits'
_A4='ifMauMediaAvailable'
_A3='ifMauStatus'
_A2='ifMauType'
_A1='rpJackType'
_A0='rpMauFalseCarriers'
_z='rpMauJabberingStateEnters'
_y='rpMauMediaAvailableStateExits'
_x='rpMauMediaAvailable'
_w='rpMauStatus'
_v='rpMauType'
_u='autoNegError'
_t='linkFailure'
_s='offline'
_r='noError'
_q='disabled'
_p='ifJackIndex'
_o='not-accessible'
_n='rpJackIndex'
_m='jabbering'
_l='noJabber'
_k='shutdown'
_j='standby'
_i='operational'
_h='mauIfGrpAutoNeg1000Mbps'
_g='mauIfGrpAutoNeg2'
_f='mauIfGrpHighCapacity'
_e='rpMauNotifications'
_d='mauRpGrpJack'
_c='mauRpGrp100Mbs'
_b='mauRpGrpBasic'
_a='ifMauAutoNegRestart'
_Z='ifMauAutoNegConfig'
_Y='ifMauAutoNegRemoteSignaling'
_X='ifMauAutoNegAdminStatus'
_W='ifMauAutoNegSupported'
_V='ifMauDefaultType'
_U='ifMauFalseCarriers'
_T='ifMauJabberState'
_S='rpMauJabberState'
_R='broadMauIndex'
_Q='broadMauIfIndex'
_P='ifMauNotifications'
_O='mauIfGrpJack'
_N='mauIfGrpBasic'
_M='unknown'
_L='rpMauIndex'
_K='rpMauPortIndex'
_J='rpMauGroupIndex'
_I='ifMauIndex'
_H='ifMauIfIndex'
_G='other'
_F='read-write'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='MAU-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifJackType,IANAifMauAutoNegCapBits,IANAifMauMediaAvailable,IANAifMauTypeListBits=mibBuilder.importSymbols('IANA-MAU-MIB','IANAifJackType','IANAifMauAutoNegCapBits','IANAifMauMediaAvailable','IANAifMauTypeListBits')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TruthValue')
mauMod=ModuleIdentity((1,3,6,1,2,1,26,6))
if mibBuilder.loadTexts:mauMod.setRevisions(('2007-04-21 00:00','2003-09-19 00:00','1999-08-24 04:00','1997-10-31 00:00','1993-09-30 00:00'))
class JackType(TextualConvention,Integer32):status=_E;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,1),('rj45',2),('rj45S',3),('db9',4),('bnc',5),('fAUI',6),('mAUI',7),('fiberSC',8),('fiberMIC',9),('fiberST',10),('telco',11),('mtrj',12),('hssdc',13),('fiberLC',14)))
_SnmpDot3MauMgt_ObjectIdentity=ObjectIdentity
snmpDot3MauMgt=_SnmpDot3MauMgt_ObjectIdentity((1,3,6,1,2,1,26))
_SnmpDot3MauTraps_ObjectIdentity=ObjectIdentity
snmpDot3MauTraps=_SnmpDot3MauTraps_ObjectIdentity((1,3,6,1,2,1,26,0))
_Dot3RpMauBasicGroup_ObjectIdentity=ObjectIdentity
dot3RpMauBasicGroup=_Dot3RpMauBasicGroup_ObjectIdentity((1,3,6,1,2,1,26,1))
_RpMauTable_Object=MibTable
rpMauTable=_RpMauTable_Object((1,3,6,1,2,1,26,1,1))
if mibBuilder.loadTexts:rpMauTable.setStatus(_B)
_RpMauEntry_Object=MibTableRow
rpMauEntry=_RpMauEntry_Object((1,3,6,1,2,1,26,1,1,1))
rpMauEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:rpMauEntry.setStatus(_B)
class _RpMauGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpMauGroupIndex_Type.__name__=_D
_RpMauGroupIndex_Object=MibTableColumn
rpMauGroupIndex=_RpMauGroupIndex_Object((1,3,6,1,2,1,26,1,1,1,1),_RpMauGroupIndex_Type())
rpMauGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauGroupIndex.setStatus(_B)
class _RpMauPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpMauPortIndex_Type.__name__=_D
_RpMauPortIndex_Object=MibTableColumn
rpMauPortIndex=_RpMauPortIndex_Object((1,3,6,1,2,1,26,1,1,1,2),_RpMauPortIndex_Type())
rpMauPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauPortIndex.setStatus(_B)
class _RpMauIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpMauIndex_Type.__name__=_D
_RpMauIndex_Object=MibTableColumn
rpMauIndex=_RpMauIndex_Object((1,3,6,1,2,1,26,1,1,1,3),_RpMauIndex_Type())
rpMauIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauIndex.setStatus(_B)
_RpMauType_Type=AutonomousType
_RpMauType_Object=MibTableColumn
rpMauType=_RpMauType_Object((1,3,6,1,2,1,26,1,1,1,4),_RpMauType_Type())
rpMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauType.setStatus(_B)
class _RpMauStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_M,2),(_i,3),(_j,4),(_k,5),('reset',6)))
_RpMauStatus_Type.__name__=_D
_RpMauStatus_Object=MibTableColumn
rpMauStatus=_RpMauStatus_Object((1,3,6,1,2,1,26,1,1,1,5),_RpMauStatus_Type())
rpMauStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rpMauStatus.setStatus(_B)
_RpMauMediaAvailable_Type=IANAifMauMediaAvailable
_RpMauMediaAvailable_Object=MibTableColumn
rpMauMediaAvailable=_RpMauMediaAvailable_Object((1,3,6,1,2,1,26,1,1,1,6),_RpMauMediaAvailable_Type())
rpMauMediaAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauMediaAvailable.setStatus(_B)
_RpMauMediaAvailableStateExits_Type=Counter32
_RpMauMediaAvailableStateExits_Object=MibTableColumn
rpMauMediaAvailableStateExits=_RpMauMediaAvailableStateExits_Object((1,3,6,1,2,1,26,1,1,1,7),_RpMauMediaAvailableStateExits_Type())
rpMauMediaAvailableStateExits.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauMediaAvailableStateExits.setStatus(_B)
class _RpMauJabberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_M,2),(_l,3),(_m,4)))
_RpMauJabberState_Type.__name__=_D
_RpMauJabberState_Object=MibTableColumn
rpMauJabberState=_RpMauJabberState_Object((1,3,6,1,2,1,26,1,1,1,8),_RpMauJabberState_Type())
rpMauJabberState.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauJabberState.setStatus(_B)
_RpMauJabberingStateEnters_Type=Counter32
_RpMauJabberingStateEnters_Object=MibTableColumn
rpMauJabberingStateEnters=_RpMauJabberingStateEnters_Object((1,3,6,1,2,1,26,1,1,1,9),_RpMauJabberingStateEnters_Type())
rpMauJabberingStateEnters.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauJabberingStateEnters.setStatus(_B)
_RpMauFalseCarriers_Type=Counter32
_RpMauFalseCarriers_Object=MibTableColumn
rpMauFalseCarriers=_RpMauFalseCarriers_Object((1,3,6,1,2,1,26,1,1,1,10),_RpMauFalseCarriers_Type())
rpMauFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauFalseCarriers.setStatus(_B)
_RpJackTable_Object=MibTable
rpJackTable=_RpJackTable_Object((1,3,6,1,2,1,26,1,2))
if mibBuilder.loadTexts:rpJackTable.setStatus(_B)
_RpJackEntry_Object=MibTableRow
rpJackEntry=_RpJackEntry_Object((1,3,6,1,2,1,26,1,2,1))
rpJackEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_n))
if mibBuilder.loadTexts:rpJackEntry.setStatus(_B)
class _RpJackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpJackIndex_Type.__name__=_D
_RpJackIndex_Object=MibTableColumn
rpJackIndex=_RpJackIndex_Object((1,3,6,1,2,1,26,1,2,1,1),_RpJackIndex_Type())
rpJackIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:rpJackIndex.setStatus(_B)
_RpJackType_Type=IANAifJackType
_RpJackType_Object=MibTableColumn
rpJackType=_RpJackType_Object((1,3,6,1,2,1,26,1,2,1,2),_RpJackType_Type())
rpJackType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpJackType.setStatus(_B)
_Dot3IfMauBasicGroup_ObjectIdentity=ObjectIdentity
dot3IfMauBasicGroup=_Dot3IfMauBasicGroup_ObjectIdentity((1,3,6,1,2,1,26,2))
_IfMauTable_Object=MibTable
ifMauTable=_IfMauTable_Object((1,3,6,1,2,1,26,2,1))
if mibBuilder.loadTexts:ifMauTable.setStatus(_B)
_IfMauEntry_Object=MibTableRow
ifMauEntry=_IfMauEntry_Object((1,3,6,1,2,1,26,2,1,1))
ifMauEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:ifMauEntry.setStatus(_B)
_IfMauIfIndex_Type=InterfaceIndex
_IfMauIfIndex_Object=MibTableColumn
ifMauIfIndex=_IfMauIfIndex_Object((1,3,6,1,2,1,26,2,1,1,1),_IfMauIfIndex_Type())
ifMauIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauIfIndex.setStatus(_B)
class _IfMauIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfMauIndex_Type.__name__=_D
_IfMauIndex_Object=MibTableColumn
ifMauIndex=_IfMauIndex_Object((1,3,6,1,2,1,26,2,1,1,2),_IfMauIndex_Type())
ifMauIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauIndex.setStatus(_B)
_IfMauType_Type=AutonomousType
_IfMauType_Object=MibTableColumn
ifMauType=_IfMauType_Object((1,3,6,1,2,1,26,2,1,1,3),_IfMauType_Type())
ifMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauType.setStatus(_B)
class _IfMauStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_M,2),(_i,3),(_j,4),(_k,5),('reset',6)))
_IfMauStatus_Type.__name__=_D
_IfMauStatus_Object=MibTableColumn
ifMauStatus=_IfMauStatus_Object((1,3,6,1,2,1,26,2,1,1,4),_IfMauStatus_Type())
ifMauStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauStatus.setStatus(_B)
_IfMauMediaAvailable_Type=IANAifMauMediaAvailable
_IfMauMediaAvailable_Object=MibTableColumn
ifMauMediaAvailable=_IfMauMediaAvailable_Object((1,3,6,1,2,1,26,2,1,1,5),_IfMauMediaAvailable_Type())
ifMauMediaAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauMediaAvailable.setStatus(_B)
_IfMauMediaAvailableStateExits_Type=Counter32
_IfMauMediaAvailableStateExits_Object=MibTableColumn
ifMauMediaAvailableStateExits=_IfMauMediaAvailableStateExits_Object((1,3,6,1,2,1,26,2,1,1,6),_IfMauMediaAvailableStateExits_Type())
ifMauMediaAvailableStateExits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauMediaAvailableStateExits.setStatus(_B)
class _IfMauJabberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_M,2),(_l,3),(_m,4)))
_IfMauJabberState_Type.__name__=_D
_IfMauJabberState_Object=MibTableColumn
ifMauJabberState=_IfMauJabberState_Object((1,3,6,1,2,1,26,2,1,1,7),_IfMauJabberState_Type())
ifMauJabberState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauJabberState.setStatus(_B)
_IfMauJabberingStateEnters_Type=Counter32
_IfMauJabberingStateEnters_Object=MibTableColumn
ifMauJabberingStateEnters=_IfMauJabberingStateEnters_Object((1,3,6,1,2,1,26,2,1,1,8),_IfMauJabberingStateEnters_Type())
ifMauJabberingStateEnters.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauJabberingStateEnters.setStatus(_B)
_IfMauFalseCarriers_Type=Counter32
_IfMauFalseCarriers_Object=MibTableColumn
ifMauFalseCarriers=_IfMauFalseCarriers_Object((1,3,6,1,2,1,26,2,1,1,9),_IfMauFalseCarriers_Type())
ifMauFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauFalseCarriers.setStatus(_B)
_IfMauTypeList_Type=Integer32
_IfMauTypeList_Object=MibTableColumn
ifMauTypeList=_IfMauTypeList_Object((1,3,6,1,2,1,26,2,1,1,10),_IfMauTypeList_Type())
ifMauTypeList.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTypeList.setStatus(_E)
_IfMauDefaultType_Type=AutonomousType
_IfMauDefaultType_Object=MibTableColumn
ifMauDefaultType=_IfMauDefaultType_Object((1,3,6,1,2,1,26,2,1,1,11),_IfMauDefaultType_Type())
ifMauDefaultType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauDefaultType.setStatus(_B)
_IfMauAutoNegSupported_Type=TruthValue
_IfMauAutoNegSupported_Object=MibTableColumn
ifMauAutoNegSupported=_IfMauAutoNegSupported_Object((1,3,6,1,2,1,26,2,1,1,12),_IfMauAutoNegSupported_Type())
ifMauAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegSupported.setStatus(_B)
_IfMauTypeListBits_Type=IANAifMauTypeListBits
_IfMauTypeListBits_Object=MibTableColumn
ifMauTypeListBits=_IfMauTypeListBits_Object((1,3,6,1,2,1,26,2,1,1,13),_IfMauTypeListBits_Type())
ifMauTypeListBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTypeListBits.setStatus(_B)
_IfMauHCFalseCarriers_Type=Counter64
_IfMauHCFalseCarriers_Object=MibTableColumn
ifMauHCFalseCarriers=_IfMauHCFalseCarriers_Object((1,3,6,1,2,1,26,2,1,1,14),_IfMauHCFalseCarriers_Type())
ifMauHCFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauHCFalseCarriers.setStatus(_B)
_IfJackTable_Object=MibTable
ifJackTable=_IfJackTable_Object((1,3,6,1,2,1,26,2,2))
if mibBuilder.loadTexts:ifJackTable.setStatus(_B)
_IfJackEntry_Object=MibTableRow
ifJackEntry=_IfJackEntry_Object((1,3,6,1,2,1,26,2,2,1))
ifJackEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_p))
if mibBuilder.loadTexts:ifJackEntry.setStatus(_B)
class _IfJackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfJackIndex_Type.__name__=_D
_IfJackIndex_Object=MibTableColumn
ifJackIndex=_IfJackIndex_Object((1,3,6,1,2,1,26,2,2,1,1),_IfJackIndex_Type())
ifJackIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:ifJackIndex.setStatus(_B)
_IfJackType_Type=IANAifJackType
_IfJackType_Object=MibTableColumn
ifJackType=_IfJackType_Object((1,3,6,1,2,1,26,2,2,1,2),_IfJackType_Type())
ifJackType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifJackType.setStatus(_B)
_Dot3BroadMauBasicGroup_ObjectIdentity=ObjectIdentity
dot3BroadMauBasicGroup=_Dot3BroadMauBasicGroup_ObjectIdentity((1,3,6,1,2,1,26,3))
_BroadMauBasicTable_Object=MibTable
broadMauBasicTable=_BroadMauBasicTable_Object((1,3,6,1,2,1,26,3,1))
if mibBuilder.loadTexts:broadMauBasicTable.setStatus(_E)
_BroadMauBasicEntry_Object=MibTableRow
broadMauBasicEntry=_BroadMauBasicEntry_Object((1,3,6,1,2,1,26,3,1,1))
broadMauBasicEntry.setIndexNames((0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:broadMauBasicEntry.setStatus(_E)
_BroadMauIfIndex_Type=InterfaceIndex
_BroadMauIfIndex_Object=MibTableColumn
broadMauIfIndex=_BroadMauIfIndex_Object((1,3,6,1,2,1,26,3,1,1,1),_BroadMauIfIndex_Type())
broadMauIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:broadMauIfIndex.setStatus(_E)
class _BroadMauIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BroadMauIndex_Type.__name__=_D
_BroadMauIndex_Object=MibTableColumn
broadMauIndex=_BroadMauIndex_Object((1,3,6,1,2,1,26,3,1,1,2),_BroadMauIndex_Type())
broadMauIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:broadMauIndex.setStatus(_E)
class _BroadMauXmtRcvSplitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('single',2),('dual',3)))
_BroadMauXmtRcvSplitType_Type.__name__=_D
_BroadMauXmtRcvSplitType_Object=MibTableColumn
broadMauXmtRcvSplitType=_BroadMauXmtRcvSplitType_Object((1,3,6,1,2,1,26,3,1,1,3),_BroadMauXmtRcvSplitType_Type())
broadMauXmtRcvSplitType.setMaxAccess(_C)
if mibBuilder.loadTexts:broadMauXmtRcvSplitType.setStatus(_E)
_BroadMauXmtCarrierFreq_Type=Integer32
_BroadMauXmtCarrierFreq_Object=MibTableColumn
broadMauXmtCarrierFreq=_BroadMauXmtCarrierFreq_Object((1,3,6,1,2,1,26,3,1,1,4),_BroadMauXmtCarrierFreq_Type())
broadMauXmtCarrierFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:broadMauXmtCarrierFreq.setStatus(_E)
_BroadMauTranslationFreq_Type=Integer32
_BroadMauTranslationFreq_Object=MibTableColumn
broadMauTranslationFreq=_BroadMauTranslationFreq_Object((1,3,6,1,2,1,26,3,1,1,5),_BroadMauTranslationFreq_Type())
broadMauTranslationFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:broadMauTranslationFreq.setStatus(_E)
_Dot3IfMauAutoNegGroup_ObjectIdentity=ObjectIdentity
dot3IfMauAutoNegGroup=_Dot3IfMauAutoNegGroup_ObjectIdentity((1,3,6,1,2,1,26,5))
_IfMauAutoNegTable_Object=MibTable
ifMauAutoNegTable=_IfMauAutoNegTable_Object((1,3,6,1,2,1,26,5,1))
if mibBuilder.loadTexts:ifMauAutoNegTable.setStatus(_B)
_IfMauAutoNegEntry_Object=MibTableRow
ifMauAutoNegEntry=_IfMauAutoNegEntry_Object((1,3,6,1,2,1,26,5,1,1))
ifMauAutoNegEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:ifMauAutoNegEntry.setStatus(_B)
class _IfMauAutoNegAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_q,2)))
_IfMauAutoNegAdminStatus_Type.__name__=_D
_IfMauAutoNegAdminStatus_Object=MibTableColumn
ifMauAutoNegAdminStatus=_IfMauAutoNegAdminStatus_Object((1,3,6,1,2,1,26,5,1,1,1),_IfMauAutoNegAdminStatus_Type())
ifMauAutoNegAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegAdminStatus.setStatus(_B)
class _IfMauAutoNegRemoteSignaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notdetected',2)))
_IfMauAutoNegRemoteSignaling_Type.__name__=_D
_IfMauAutoNegRemoteSignaling_Object=MibTableColumn
ifMauAutoNegRemoteSignaling=_IfMauAutoNegRemoteSignaling_Object((1,3,6,1,2,1,26,5,1,1,2),_IfMauAutoNegRemoteSignaling_Type())
ifMauAutoNegRemoteSignaling.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegRemoteSignaling.setStatus(_B)
class _IfMauAutoNegConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('configuring',2),('complete',3),(_q,4),('parallelDetectFail',5)))
_IfMauAutoNegConfig_Type.__name__=_D
_IfMauAutoNegConfig_Object=MibTableColumn
ifMauAutoNegConfig=_IfMauAutoNegConfig_Object((1,3,6,1,2,1,26,5,1,1,4),_IfMauAutoNegConfig_Type())
ifMauAutoNegConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegConfig.setStatus(_B)
_IfMauAutoNegCapability_Type=Integer32
_IfMauAutoNegCapability_Object=MibTableColumn
ifMauAutoNegCapability=_IfMauAutoNegCapability_Object((1,3,6,1,2,1,26,5,1,1,5),_IfMauAutoNegCapability_Type())
ifMauAutoNegCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegCapability.setStatus(_E)
_IfMauAutoNegCapAdvertised_Type=Integer32
_IfMauAutoNegCapAdvertised_Object=MibTableColumn
ifMauAutoNegCapAdvertised=_IfMauAutoNegCapAdvertised_Object((1,3,6,1,2,1,26,5,1,1,6),_IfMauAutoNegCapAdvertised_Type())
ifMauAutoNegCapAdvertised.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegCapAdvertised.setStatus(_E)
_IfMauAutoNegCapReceived_Type=Integer32
_IfMauAutoNegCapReceived_Object=MibTableColumn
ifMauAutoNegCapReceived=_IfMauAutoNegCapReceived_Object((1,3,6,1,2,1,26,5,1,1,7),_IfMauAutoNegCapReceived_Type())
ifMauAutoNegCapReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegCapReceived.setStatus(_E)
class _IfMauAutoNegRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('norestart',2)))
_IfMauAutoNegRestart_Type.__name__=_D
_IfMauAutoNegRestart_Object=MibTableColumn
ifMauAutoNegRestart=_IfMauAutoNegRestart_Object((1,3,6,1,2,1,26,5,1,1,8),_IfMauAutoNegRestart_Type())
ifMauAutoNegRestart.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegRestart.setStatus(_B)
_IfMauAutoNegCapabilityBits_Type=IANAifMauAutoNegCapBits
_IfMauAutoNegCapabilityBits_Object=MibTableColumn
ifMauAutoNegCapabilityBits=_IfMauAutoNegCapabilityBits_Object((1,3,6,1,2,1,26,5,1,1,9),_IfMauAutoNegCapabilityBits_Type())
ifMauAutoNegCapabilityBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegCapabilityBits.setStatus(_B)
_IfMauAutoNegCapAdvertisedBits_Type=IANAifMauAutoNegCapBits
_IfMauAutoNegCapAdvertisedBits_Object=MibTableColumn
ifMauAutoNegCapAdvertisedBits=_IfMauAutoNegCapAdvertisedBits_Object((1,3,6,1,2,1,26,5,1,1,10),_IfMauAutoNegCapAdvertisedBits_Type())
ifMauAutoNegCapAdvertisedBits.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegCapAdvertisedBits.setStatus(_B)
_IfMauAutoNegCapReceivedBits_Type=IANAifMauAutoNegCapBits
_IfMauAutoNegCapReceivedBits_Object=MibTableColumn
ifMauAutoNegCapReceivedBits=_IfMauAutoNegCapReceivedBits_Object((1,3,6,1,2,1,26,5,1,1,11),_IfMauAutoNegCapReceivedBits_Type())
ifMauAutoNegCapReceivedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegCapReceivedBits.setStatus(_B)
class _IfMauAutoNegRemoteFaultAdvertised_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4)))
_IfMauAutoNegRemoteFaultAdvertised_Type.__name__=_D
_IfMauAutoNegRemoteFaultAdvertised_Object=MibTableColumn
ifMauAutoNegRemoteFaultAdvertised=_IfMauAutoNegRemoteFaultAdvertised_Object((1,3,6,1,2,1,26,5,1,1,12),_IfMauAutoNegRemoteFaultAdvertised_Type())
ifMauAutoNegRemoteFaultAdvertised.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegRemoteFaultAdvertised.setStatus(_B)
class _IfMauAutoNegRemoteFaultReceived_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4)))
_IfMauAutoNegRemoteFaultReceived_Type.__name__=_D
_IfMauAutoNegRemoteFaultReceived_Object=MibTableColumn
ifMauAutoNegRemoteFaultReceived=_IfMauAutoNegRemoteFaultReceived_Object((1,3,6,1,2,1,26,5,1,1,13),_IfMauAutoNegRemoteFaultReceived_Type())
ifMauAutoNegRemoteFaultReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegRemoteFaultReceived.setStatus(_B)
_MauModConf_ObjectIdentity=ObjectIdentity
mauModConf=_MauModConf_ObjectIdentity((1,3,6,1,2,1,26,6,1))
_MauModCompls_ObjectIdentity=ObjectIdentity
mauModCompls=_MauModCompls_ObjectIdentity((1,3,6,1,2,1,26,6,1,1))
_MauModObjGrps_ObjectIdentity=ObjectIdentity
mauModObjGrps=_MauModObjGrps_ObjectIdentity((1,3,6,1,2,1,26,6,1,2))
_MauModNotGrps_ObjectIdentity=ObjectIdentity
mauModNotGrps=_MauModNotGrps_ObjectIdentity((1,3,6,1,2,1,26,6,1,3))
mauRpGrpBasic=ObjectGroup((1,3,6,1,2,1,26,6,1,2,1))
mauRpGrpBasic.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_S),(_A,_z)))
if mibBuilder.loadTexts:mauRpGrpBasic.setStatus(_B)
mauRpGrp100Mbs=ObjectGroup((1,3,6,1,2,1,26,6,1,2,2))
mauRpGrp100Mbs.setObjects((_A,_A0))
if mibBuilder.loadTexts:mauRpGrp100Mbs.setStatus(_B)
mauRpGrpJack=ObjectGroup((1,3,6,1,2,1,26,6,1,2,3))
mauRpGrpJack.setObjects((_A,_A1))
if mibBuilder.loadTexts:mauRpGrpJack.setStatus(_B)
mauIfGrpBasic=ObjectGroup((1,3,6,1,2,1,26,6,1,2,4))
mauIfGrpBasic.setObjects(*((_A,_H),(_A,_I),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_T),(_A,_A6)))
if mibBuilder.loadTexts:mauIfGrpBasic.setStatus(_B)
mauIfGrp100Mbs=ObjectGroup((1,3,6,1,2,1,26,6,1,2,5))
mauIfGrp100Mbs.setObjects(*((_A,_U),(_A,_A7),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:mauIfGrp100Mbs.setStatus(_E)
mauIfGrpJack=ObjectGroup((1,3,6,1,2,1,26,6,1,2,6))
mauIfGrpJack.setObjects((_A,_A8))
if mibBuilder.loadTexts:mauIfGrpJack.setStatus(_B)
mauIfGrpAutoNeg=ObjectGroup((1,3,6,1,2,1,26,6,1,2,7))
mauIfGrpAutoNeg.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_a)))
if mibBuilder.loadTexts:mauIfGrpAutoNeg.setStatus(_E)
mauBroadBasic=ObjectGroup((1,3,6,1,2,1,26,6,1,2,8))
mauBroadBasic.setObjects(*((_A,_Q),(_A,_R),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:mauBroadBasic.setStatus(_E)
mauIfGrpHighCapacity=ObjectGroup((1,3,6,1,2,1,26,6,1,2,9))
mauIfGrpHighCapacity.setObjects(*((_A,_U),(_A,_AF),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:mauIfGrpHighCapacity.setStatus(_B)
mauIfGrpAutoNeg2=ObjectGroup((1,3,6,1,2,1,26,6,1,2,10))
mauIfGrpAutoNeg2.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_a)))
if mibBuilder.loadTexts:mauIfGrpAutoNeg2.setStatus(_B)
mauIfGrpAutoNeg1000Mbps=ObjectGroup((1,3,6,1,2,1,26,6,1,2,11))
mauIfGrpAutoNeg1000Mbps.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:mauIfGrpAutoNeg1000Mbps.setStatus(_B)
mauIfGrpHCStats=ObjectGroup((1,3,6,1,2,1,26,6,1,2,12))
mauIfGrpHCStats.setObjects((_A,_AL))
if mibBuilder.loadTexts:mauIfGrpHCStats.setStatus(_B)
rpMauJabberTrap=NotificationType((1,3,6,1,2,1,26,0,1))
rpMauJabberTrap.setObjects((_A,_S))
if mibBuilder.loadTexts:rpMauJabberTrap.setStatus(_B)
ifMauJabberTrap=NotificationType((1,3,6,1,2,1,26,0,2))
ifMauJabberTrap.setObjects((_A,_T))
if mibBuilder.loadTexts:ifMauJabberTrap.setStatus(_B)
rpMauNotifications=NotificationGroup((1,3,6,1,2,1,26,6,1,3,1))
rpMauNotifications.setObjects((_A,_AM))
if mibBuilder.loadTexts:rpMauNotifications.setStatus(_B)
ifMauNotifications=NotificationGroup((1,3,6,1,2,1,26,6,1,3,2))
ifMauNotifications.setObjects((_A,_AN))
if mibBuilder.loadTexts:ifMauNotifications.setStatus(_B)
mauModRpCompl=ModuleCompliance((1,3,6,1,2,1,26,6,1,1,1))
mauModRpCompl.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:mauModRpCompl.setStatus(_E)
mauModIfCompl=ModuleCompliance((1,3,6,1,2,1,26,6,1,1,2))
mauModIfCompl.setObjects(*((_A,_N),(_A,_AO),(_A,_O),(_A,_AP),(_A,_AQ),(_A,_P)))
if mibBuilder.loadTexts:mauModIfCompl.setStatus(_E)
mauModIfCompl2=ModuleCompliance((1,3,6,1,2,1,26,6,1,1,3))
mauModIfCompl2.setObjects(*((_A,_N),(_A,_f),(_A,_O),(_A,_g),(_A,_h),(_A,_P)))
if mibBuilder.loadTexts:mauModIfCompl2.setStatus(_E)
mauModRpCompl2=ModuleCompliance((1,3,6,1,2,1,26,6,1,1,4))
mauModRpCompl2.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:mauModRpCompl2.setStatus(_B)
mauModIfCompl3=ModuleCompliance((1,3,6,1,2,1,26,6,1,1,5))
mauModIfCompl3.setObjects(*((_A,_N),(_A,_f),(_A,_AR),(_A,_O),(_A,_g),(_A,_h),(_A,_P)))
if mibBuilder.loadTexts:mauModIfCompl3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JackType':JackType,'snmpDot3MauMgt':snmpDot3MauMgt,'snmpDot3MauTraps':snmpDot3MauTraps,_AM:rpMauJabberTrap,_AN:ifMauJabberTrap,'dot3RpMauBasicGroup':dot3RpMauBasicGroup,'rpMauTable':rpMauTable,'rpMauEntry':rpMauEntry,_J:rpMauGroupIndex,_K:rpMauPortIndex,_L:rpMauIndex,_v:rpMauType,_w:rpMauStatus,_x:rpMauMediaAvailable,_y:rpMauMediaAvailableStateExits,_S:rpMauJabberState,_z:rpMauJabberingStateEnters,_A0:rpMauFalseCarriers,'rpJackTable':rpJackTable,'rpJackEntry':rpJackEntry,_n:rpJackIndex,_A1:rpJackType,'dot3IfMauBasicGroup':dot3IfMauBasicGroup,'ifMauTable':ifMauTable,'ifMauEntry':ifMauEntry,_H:ifMauIfIndex,_I:ifMauIndex,_A2:ifMauType,_A3:ifMauStatus,_A4:ifMauMediaAvailable,_A5:ifMauMediaAvailableStateExits,_T:ifMauJabberState,_A6:ifMauJabberingStateEnters,_U:ifMauFalseCarriers,_A7:ifMauTypeList,_V:ifMauDefaultType,_W:ifMauAutoNegSupported,_AF:ifMauTypeListBits,_AL:ifMauHCFalseCarriers,'ifJackTable':ifJackTable,'ifJackEntry':ifJackEntry,_p:ifJackIndex,_A8:ifJackType,'dot3BroadMauBasicGroup':dot3BroadMauBasicGroup,'broadMauBasicTable':broadMauBasicTable,'broadMauBasicEntry':broadMauBasicEntry,_Q:broadMauIfIndex,_R:broadMauIndex,_AC:broadMauXmtRcvSplitType,_AD:broadMauXmtCarrierFreq,_AE:broadMauTranslationFreq,'dot3IfMauAutoNegGroup':dot3IfMauAutoNegGroup,'ifMauAutoNegTable':ifMauAutoNegTable,'ifMauAutoNegEntry':ifMauAutoNegEntry,_X:ifMauAutoNegAdminStatus,_Y:ifMauAutoNegRemoteSignaling,_Z:ifMauAutoNegConfig,_A9:ifMauAutoNegCapability,_AA:ifMauAutoNegCapAdvertised,_AB:ifMauAutoNegCapReceived,_a:ifMauAutoNegRestart,_AG:ifMauAutoNegCapabilityBits,_AH:ifMauAutoNegCapAdvertisedBits,_AI:ifMauAutoNegCapReceivedBits,_AJ:ifMauAutoNegRemoteFaultAdvertised,_AK:ifMauAutoNegRemoteFaultReceived,'mauMod':mauMod,'mauModConf':mauModConf,'mauModCompls':mauModCompls,'mauModRpCompl':mauModRpCompl,'mauModIfCompl':mauModIfCompl,'mauModIfCompl2':mauModIfCompl2,'mauModRpCompl2':mauModRpCompl2,'mauModIfCompl3':mauModIfCompl3,'mauModObjGrps':mauModObjGrps,_b:mauRpGrpBasic,_c:mauRpGrp100Mbs,_d:mauRpGrpJack,_N:mauIfGrpBasic,_AO:mauIfGrp100Mbs,_O:mauIfGrpJack,_AP:mauIfGrpAutoNeg,_AQ:mauBroadBasic,_f:mauIfGrpHighCapacity,_g:mauIfGrpAutoNeg2,_h:mauIfGrpAutoNeg1000Mbps,_AR:mauIfGrpHCStats,'mauModNotGrps':mauModNotGrps,_e:rpMauNotifications,_P:ifMauNotifications})