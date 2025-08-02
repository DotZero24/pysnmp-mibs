_U='nbsSlaPerfMonIfIndex'
_T='inProgress'
_S='inactive'
_R='nbsSlaLossGainIfIndex'
_Q='00000000'
_P='000000000000'
_O='nbsSlaTrafficGenIfIndex'
_N='Unsigned32'
_M='increment'
_L='stop'
_K='start'
_J='not-accessible'
_I='NBS-SLA-MIB'
_H='random'
_G='fixed'
_F='OctetString'
_E='notSupported'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsSlaMib=ModuleIdentity((1,3,6,1,4,1,629,216))
_NbsSlaTrafficGenGrp_ObjectIdentity=ObjectIdentity
nbsSlaTrafficGenGrp=_NbsSlaTrafficGenGrp_ObjectIdentity((1,3,6,1,4,1,629,216,1))
if mibBuilder.loadTexts:nbsSlaTrafficGenGrp.setStatus(_A)
_NbsSlaTrafficGenTableSize_Type=Unsigned32
_NbsSlaTrafficGenTableSize_Object=MibScalar
nbsSlaTrafficGenTableSize=_NbsSlaTrafficGenTableSize_Object((1,3,6,1,4,1,629,216,1,1),_NbsSlaTrafficGenTableSize_Type())
nbsSlaTrafficGenTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaTrafficGenTableSize.setStatus(_A)
_NbsSlaTrafficGenTable_Object=MibTable
nbsSlaTrafficGenTable=_NbsSlaTrafficGenTable_Object((1,3,6,1,4,1,629,216,1,2))
if mibBuilder.loadTexts:nbsSlaTrafficGenTable.setStatus(_A)
_NbsSlaTrafficGenEntry_Object=MibTableRow
nbsSlaTrafficGenEntry=_NbsSlaTrafficGenEntry_Object((1,3,6,1,4,1,629,216,1,2,1))
nbsSlaTrafficGenEntry.setIndexNames((0,_I,_O))
if mibBuilder.loadTexts:nbsSlaTrafficGenEntry.setStatus(_A)
_NbsSlaTrafficGenIfIndex_Type=InterfaceIndex
_NbsSlaTrafficGenIfIndex_Object=MibTableColumn
nbsSlaTrafficGenIfIndex=_NbsSlaTrafficGenIfIndex_Object((1,3,6,1,4,1,629,216,1,2,1,1),_NbsSlaTrafficGenIfIndex_Type())
nbsSlaTrafficGenIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsSlaTrafficGenIfIndex.setStatus(_A)
class _NbsSlaTrafficGenAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_K,2),(_L,3)))
_NbsSlaTrafficGenAction_Type.__name__=_D
_NbsSlaTrafficGenAction_Object=MibTableColumn
nbsSlaTrafficGenAction=_NbsSlaTrafficGenAction_Object((1,3,6,1,4,1,629,216,1,2,1,2),_NbsSlaTrafficGenAction_Type())
nbsSlaTrafficGenAction.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenAction.setStatus(_A)
class _NbsSlaTrafficGenFrameSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9600))
_NbsSlaTrafficGenFrameSize_Type.__name__=_D
_NbsSlaTrafficGenFrameSize_Object=MibTableColumn
nbsSlaTrafficGenFrameSize=_NbsSlaTrafficGenFrameSize_Object((1,3,6,1,4,1,629,216,1,2,1,3),_NbsSlaTrafficGenFrameSize_Type())
nbsSlaTrafficGenFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenFrameSize.setStatus(_A)
class _NbsSlaTrafficGenFrameSizeType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_G,3)))
_NbsSlaTrafficGenFrameSizeType_Type.__name__=_D
_NbsSlaTrafficGenFrameSizeType_Object=MibTableColumn
nbsSlaTrafficGenFrameSizeType=_NbsSlaTrafficGenFrameSizeType_Object((1,3,6,1,4,1,629,216,1,2,1,4),_NbsSlaTrafficGenFrameSizeType_Type())
nbsSlaTrafficGenFrameSizeType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenFrameSizeType.setStatus(_A)
class _NbsSlaTrafficGenFrameCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967294))
_NbsSlaTrafficGenFrameCount_Type.__name__=_N
_NbsSlaTrafficGenFrameCount_Object=MibTableColumn
nbsSlaTrafficGenFrameCount=_NbsSlaTrafficGenFrameCount_Object((1,3,6,1,4,1,629,216,1,2,1,5),_NbsSlaTrafficGenFrameCount_Type())
nbsSlaTrafficGenFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenFrameCount.setStatus(_A)
class _NbsSlaTrafficGenFrameCountType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('continuous',2),(_G,3)))
_NbsSlaTrafficGenFrameCountType_Type.__name__=_D
_NbsSlaTrafficGenFrameCountType_Object=MibTableColumn
nbsSlaTrafficGenFrameCountType=_NbsSlaTrafficGenFrameCountType_Object((1,3,6,1,4,1,629,216,1,2,1,6),_NbsSlaTrafficGenFrameCountType_Type())
nbsSlaTrafficGenFrameCountType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenFrameCountType.setStatus(_A)
class _NbsSlaTrafficGenInterPacketGap_Type(Integer32):defaultValue=1249928;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,134217727))
_NbsSlaTrafficGenInterPacketGap_Type.__name__=_D
_NbsSlaTrafficGenInterPacketGap_Object=MibTableColumn
nbsSlaTrafficGenInterPacketGap=_NbsSlaTrafficGenInterPacketGap_Object((1,3,6,1,4,1,629,216,1,2,1,7),_NbsSlaTrafficGenInterPacketGap_Type())
nbsSlaTrafficGenInterPacketGap.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenInterPacketGap.setStatus(_A)
_NbsSlaTrafficGenMaxHeaders_Type=Integer32
_NbsSlaTrafficGenMaxHeaders_Object=MibTableColumn
nbsSlaTrafficGenMaxHeaders=_NbsSlaTrafficGenMaxHeaders_Object((1,3,6,1,4,1,629,216,1,2,1,8),_NbsSlaTrafficGenMaxHeaders_Type())
nbsSlaTrafficGenMaxHeaders.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaTrafficGenMaxHeaders.setStatus(_A)
_NbsSlaTrafficGenMaxPattern_Type=Integer32
_NbsSlaTrafficGenMaxPattern_Object=MibTableColumn
nbsSlaTrafficGenMaxPattern=_NbsSlaTrafficGenMaxPattern_Object((1,3,6,1,4,1,629,216,1,2,1,9),_NbsSlaTrafficGenMaxPattern_Type())
nbsSlaTrafficGenMaxPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaTrafficGenMaxPattern.setStatus(_A)
class _NbsSlaTrafficGenHeaders_Type(OctetString):defaultHexValue='000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(48,48));fixedLength=48
_NbsSlaTrafficGenHeaders_Type.__name__=_F
_NbsSlaTrafficGenHeaders_Object=MibTableColumn
nbsSlaTrafficGenHeaders=_NbsSlaTrafficGenHeaders_Object((1,3,6,1,4,1,629,216,1,2,1,10),_NbsSlaTrafficGenHeaders_Type())
nbsSlaTrafficGenHeaders.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenHeaders.setStatus(_A)
class _NbsSlaTrafficGenDa_Type(OctetString):defaultHexValue=_P;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsSlaTrafficGenDa_Type.__name__=_F
_NbsSlaTrafficGenDa_Object=MibTableColumn
nbsSlaTrafficGenDa=_NbsSlaTrafficGenDa_Object((1,3,6,1,4,1,629,216,1,2,1,11),_NbsSlaTrafficGenDa_Type())
nbsSlaTrafficGenDa.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenDa.setStatus(_A)
class _NbsSlaTrafficGenDaType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_H,2),(_G,3),(_M,4)))
_NbsSlaTrafficGenDaType_Type.__name__=_D
_NbsSlaTrafficGenDaType_Object=MibTableColumn
nbsSlaTrafficGenDaType=_NbsSlaTrafficGenDaType_Object((1,3,6,1,4,1,629,216,1,2,1,12),_NbsSlaTrafficGenDaType_Type())
nbsSlaTrafficGenDaType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenDaType.setStatus(_A)
class _NbsSlaTrafficGenSa_Type(OctetString):defaultHexValue=_P;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsSlaTrafficGenSa_Type.__name__=_F
_NbsSlaTrafficGenSa_Object=MibTableColumn
nbsSlaTrafficGenSa=_NbsSlaTrafficGenSa_Object((1,3,6,1,4,1,629,216,1,2,1,13),_NbsSlaTrafficGenSa_Type())
nbsSlaTrafficGenSa.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenSa.setStatus(_A)
class _NbsSlaTrafficGenSaType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_H,2),(_G,3),(_M,4)))
_NbsSlaTrafficGenSaType_Type.__name__=_D
_NbsSlaTrafficGenSaType_Object=MibTableColumn
nbsSlaTrafficGenSaType=_NbsSlaTrafficGenSaType_Object((1,3,6,1,4,1,629,216,1,2,1,14),_NbsSlaTrafficGenSaType_Type())
nbsSlaTrafficGenSaType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenSaType.setStatus(_A)
class _NbsSlaTrafficGenTag_Type(OctetString):defaultHexValue=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NbsSlaTrafficGenTag_Type.__name__=_F
_NbsSlaTrafficGenTag_Object=MibTableColumn
nbsSlaTrafficGenTag=_NbsSlaTrafficGenTag_Object((1,3,6,1,4,1,629,216,1,2,1,15),_NbsSlaTrafficGenTag_Type())
nbsSlaTrafficGenTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenTag.setStatus(_A)
class _NbsSlaTrafficGenTagType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_H,2),(_G,3),(_M,4)))
_NbsSlaTrafficGenTagType_Type.__name__=_D
_NbsSlaTrafficGenTagType_Object=MibTableColumn
nbsSlaTrafficGenTagType=_NbsSlaTrafficGenTagType_Object((1,3,6,1,4,1,629,216,1,2,1,16),_NbsSlaTrafficGenTagType_Type())
nbsSlaTrafficGenTagType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenTagType.setStatus(_A)
class _NbsSlaTrafficGenPattern_Type(OctetString):defaultHexValue=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NbsSlaTrafficGenPattern_Type.__name__=_F
_NbsSlaTrafficGenPattern_Object=MibTableColumn
nbsSlaTrafficGenPattern=_NbsSlaTrafficGenPattern_Object((1,3,6,1,4,1,629,216,1,2,1,17),_NbsSlaTrafficGenPattern_Type())
nbsSlaTrafficGenPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenPattern.setStatus(_A)
class _NbsSlaTrafficGenPatternType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_G,3)))
_NbsSlaTrafficGenPatternType_Type.__name__=_D
_NbsSlaTrafficGenPatternType_Object=MibTableColumn
nbsSlaTrafficGenPatternType=_NbsSlaTrafficGenPatternType_Object((1,3,6,1,4,1,629,216,1,2,1,18),_NbsSlaTrafficGenPatternType_Type())
nbsSlaTrafficGenPatternType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaTrafficGenPatternType.setStatus(_A)
_NbsSlaLossGainGrp_ObjectIdentity=ObjectIdentity
nbsSlaLossGainGrp=_NbsSlaLossGainGrp_ObjectIdentity((1,3,6,1,4,1,629,216,2))
if mibBuilder.loadTexts:nbsSlaLossGainGrp.setStatus(_A)
_NbsSlaLossGainTableSize_Type=Unsigned32
_NbsSlaLossGainTableSize_Object=MibScalar
nbsSlaLossGainTableSize=_NbsSlaLossGainTableSize_Object((1,3,6,1,4,1,629,216,2,1),_NbsSlaLossGainTableSize_Type())
nbsSlaLossGainTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainTableSize.setStatus(_A)
_NbsSlaLossGainTable_Object=MibTable
nbsSlaLossGainTable=_NbsSlaLossGainTable_Object((1,3,6,1,4,1,629,216,2,2))
if mibBuilder.loadTexts:nbsSlaLossGainTable.setStatus(_A)
_NbsSlaLossGainEntry_Object=MibTableRow
nbsSlaLossGainEntry=_NbsSlaLossGainEntry_Object((1,3,6,1,4,1,629,216,2,2,1))
nbsSlaLossGainEntry.setIndexNames((0,_I,_R))
if mibBuilder.loadTexts:nbsSlaLossGainEntry.setStatus(_A)
_NbsSlaLossGainIfIndex_Type=InterfaceIndex
_NbsSlaLossGainIfIndex_Object=MibTableColumn
nbsSlaLossGainIfIndex=_NbsSlaLossGainIfIndex_Object((1,3,6,1,4,1,629,216,2,2,1,1),_NbsSlaLossGainIfIndex_Type())
nbsSlaLossGainIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsSlaLossGainIfIndex.setStatus(_A)
class _NbsSlaLossGainAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_S,2),(_K,3),(_L,4),(_T,5)))
_NbsSlaLossGainAction_Type.__name__=_D
_NbsSlaLossGainAction_Object=MibTableColumn
nbsSlaLossGainAction=_NbsSlaLossGainAction_Object((1,3,6,1,4,1,629,216,2,2,1,2),_NbsSlaLossGainAction_Type())
nbsSlaLossGainAction.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaLossGainAction.setStatus(_A)
class _NbsSlaLossGainInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_NbsSlaLossGainInterval_Type.__name__=_D
_NbsSlaLossGainInterval_Object=MibTableColumn
nbsSlaLossGainInterval=_NbsSlaLossGainInterval_Object((1,3,6,1,4,1,629,216,2,2,1,3),_NbsSlaLossGainInterval_Type())
nbsSlaLossGainInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaLossGainInterval.setStatus(_A)
class _NbsSlaLossGainEthMax_Type(Integer32):defaultValue=1518
_NbsSlaLossGainEthMax_Type.__name__=_D
_NbsSlaLossGainEthMax_Object=MibTableColumn
nbsSlaLossGainEthMax=_NbsSlaLossGainEthMax_Object((1,3,6,1,4,1,629,216,2,2,1,4),_NbsSlaLossGainEthMax_Type())
nbsSlaLossGainEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainEthMax.setStatus(_A)
_NbsSlaLossGainRdAllFrames_Type=Counter64
_NbsSlaLossGainRdAllFrames_Object=MibTableColumn
nbsSlaLossGainRdAllFrames=_NbsSlaLossGainRdAllFrames_Object((1,3,6,1,4,1,629,216,2,2,1,5),_NbsSlaLossGainRdAllFrames_Type())
nbsSlaLossGainRdAllFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdAllFrames.setStatus(_A)
_NbsSlaLossGainRdBadFrames_Type=Counter64
_NbsSlaLossGainRdBadFrames_Object=MibTableColumn
nbsSlaLossGainRdBadFrames=_NbsSlaLossGainRdBadFrames_Object((1,3,6,1,4,1,629,216,2,2,1,6),_NbsSlaLossGainRdBadFrames_Type())
nbsSlaLossGainRdBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdBadFrames.setStatus(_A)
_NbsSlaLossGainRdDiscards_Type=Counter64
_NbsSlaLossGainRdDiscards_Object=MibTableColumn
nbsSlaLossGainRdDiscards=_NbsSlaLossGainRdDiscards_Object((1,3,6,1,4,1,629,216,2,2,1,7),_NbsSlaLossGainRdDiscards_Type())
nbsSlaLossGainRdDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdDiscards.setStatus(_A)
_NbsSlaLossGainRdUcastFrames_Type=Counter64
_NbsSlaLossGainRdUcastFrames_Object=MibTableColumn
nbsSlaLossGainRdUcastFrames=_NbsSlaLossGainRdUcastFrames_Object((1,3,6,1,4,1,629,216,2,2,1,8),_NbsSlaLossGainRdUcastFrames_Type())
nbsSlaLossGainRdUcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdUcastFrames.setStatus(_A)
_NbsSlaLossGainRdMcastFrames_Type=Counter64
_NbsSlaLossGainRdMcastFrames_Object=MibTableColumn
nbsSlaLossGainRdMcastFrames=_NbsSlaLossGainRdMcastFrames_Object((1,3,6,1,4,1,629,216,2,2,1,9),_NbsSlaLossGainRdMcastFrames_Type())
nbsSlaLossGainRdMcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdMcastFrames.setStatus(_A)
_NbsSlaLossGainRdBcastFrames_Type=Counter64
_NbsSlaLossGainRdBcastFrames_Object=MibTableColumn
nbsSlaLossGainRdBcastFrames=_NbsSlaLossGainRdBcastFrames_Object((1,3,6,1,4,1,629,216,2,2,1,10),_NbsSlaLossGainRdBcastFrames_Type())
nbsSlaLossGainRdBcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdBcastFrames.setStatus(_A)
_NbsSlaLossGainRdSize64_Type=Counter64
_NbsSlaLossGainRdSize64_Object=MibTableColumn
nbsSlaLossGainRdSize64=_NbsSlaLossGainRdSize64_Object((1,3,6,1,4,1,629,216,2,2,1,11),_NbsSlaLossGainRdSize64_Type())
nbsSlaLossGainRdSize64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize64.setStatus(_A)
_NbsSlaLossGainRdSize65to127_Type=Counter64
_NbsSlaLossGainRdSize65to127_Object=MibTableColumn
nbsSlaLossGainRdSize65to127=_NbsSlaLossGainRdSize65to127_Object((1,3,6,1,4,1,629,216,2,2,1,12),_NbsSlaLossGainRdSize65to127_Type())
nbsSlaLossGainRdSize65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize65to127.setStatus(_A)
_NbsSlaLossGainRdSize128to255_Type=Counter64
_NbsSlaLossGainRdSize128to255_Object=MibTableColumn
nbsSlaLossGainRdSize128to255=_NbsSlaLossGainRdSize128to255_Object((1,3,6,1,4,1,629,216,2,2,1,13),_NbsSlaLossGainRdSize128to255_Type())
nbsSlaLossGainRdSize128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize128to255.setStatus(_A)
_NbsSlaLossGainRdSize256to511_Type=Counter64
_NbsSlaLossGainRdSize256to511_Object=MibTableColumn
nbsSlaLossGainRdSize256to511=_NbsSlaLossGainRdSize256to511_Object((1,3,6,1,4,1,629,216,2,2,1,14),_NbsSlaLossGainRdSize256to511_Type())
nbsSlaLossGainRdSize256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize256to511.setStatus(_A)
_NbsSlaLossGainRdSize512to1023_Type=Counter64
_NbsSlaLossGainRdSize512to1023_Object=MibTableColumn
nbsSlaLossGainRdSize512to1023=_NbsSlaLossGainRdSize512to1023_Object((1,3,6,1,4,1,629,216,2,2,1,15),_NbsSlaLossGainRdSize512to1023_Type())
nbsSlaLossGainRdSize512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize512to1023.setStatus(_A)
_NbsSlaLossGainRdSize1024toEthMax_Type=Counter64
_NbsSlaLossGainRdSize1024toEthMax_Object=MibTableColumn
nbsSlaLossGainRdSize1024toEthMax=_NbsSlaLossGainRdSize1024toEthMax_Object((1,3,6,1,4,1,629,216,2,2,1,16),_NbsSlaLossGainRdSize1024toEthMax_Type())
nbsSlaLossGainRdSize1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize1024toEthMax.setStatus(_A)
_NbsSlaLossGainRdSizeEthMaxto2047_Type=Counter64
_NbsSlaLossGainRdSizeEthMaxto2047_Object=MibTableColumn
nbsSlaLossGainRdSizeEthMaxto2047=_NbsSlaLossGainRdSizeEthMaxto2047_Object((1,3,6,1,4,1,629,216,2,2,1,17),_NbsSlaLossGainRdSizeEthMaxto2047_Type())
nbsSlaLossGainRdSizeEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSizeEthMaxto2047.setStatus(_A)
_NbsSlaLossGainRdSize2048to4095_Type=Counter64
_NbsSlaLossGainRdSize2048to4095_Object=MibTableColumn
nbsSlaLossGainRdSize2048to4095=_NbsSlaLossGainRdSize2048to4095_Object((1,3,6,1,4,1,629,216,2,2,1,18),_NbsSlaLossGainRdSize2048to4095_Type())
nbsSlaLossGainRdSize2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize2048to4095.setStatus(_A)
_NbsSlaLossGainRdSize4096to8191_Type=Counter64
_NbsSlaLossGainRdSize4096to8191_Object=MibTableColumn
nbsSlaLossGainRdSize4096to8191=_NbsSlaLossGainRdSize4096to8191_Object((1,3,6,1,4,1,629,216,2,2,1,19),_NbsSlaLossGainRdSize4096to8191_Type())
nbsSlaLossGainRdSize4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize4096to8191.setStatus(_A)
_NbsSlaLossGainRdSize8192orMore_Type=Counter64
_NbsSlaLossGainRdSize8192orMore_Object=MibTableColumn
nbsSlaLossGainRdSize8192orMore=_NbsSlaLossGainRdSize8192orMore_Object((1,3,6,1,4,1,629,216,2,2,1,20),_NbsSlaLossGainRdSize8192orMore_Type())
nbsSlaLossGainRdSize8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdSize8192orMore.setStatus(_A)
_NbsSlaLossGainRdFrameDivisor_Type=Counter64
_NbsSlaLossGainRdFrameDivisor_Object=MibTableColumn
nbsSlaLossGainRdFrameDivisor=_NbsSlaLossGainRdFrameDivisor_Object((1,3,6,1,4,1,629,216,2,2,1,21),_NbsSlaLossGainRdFrameDivisor_Type())
nbsSlaLossGainRdFrameDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdFrameDivisor.setStatus(_A)
_NbsSlaLossGainRdAllOctets_Type=Counter64
_NbsSlaLossGainRdAllOctets_Object=MibTableColumn
nbsSlaLossGainRdAllOctets=_NbsSlaLossGainRdAllOctets_Object((1,3,6,1,4,1,629,216,2,2,1,22),_NbsSlaLossGainRdAllOctets_Type())
nbsSlaLossGainRdAllOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdAllOctets.setStatus(_A)
_NbsSlaLossGainRdBadOctets_Type=Counter64
_NbsSlaLossGainRdBadOctets_Object=MibTableColumn
nbsSlaLossGainRdBadOctets=_NbsSlaLossGainRdBadOctets_Object((1,3,6,1,4,1,629,216,2,2,1,23),_NbsSlaLossGainRdBadOctets_Type())
nbsSlaLossGainRdBadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdBadOctets.setStatus(_A)
_NbsSlaLossGainRdOctetDivisor_Type=Counter64
_NbsSlaLossGainRdOctetDivisor_Object=MibTableColumn
nbsSlaLossGainRdOctetDivisor=_NbsSlaLossGainRdOctetDivisor_Object((1,3,6,1,4,1,629,216,2,2,1,24),_NbsSlaLossGainRdOctetDivisor_Type())
nbsSlaLossGainRdOctetDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdOctetDivisor.setStatus(_A)
_NbsSlaLossGainRdTimeSpan_Type=Counter32
_NbsSlaLossGainRdTimeSpan_Object=MibTableColumn
nbsSlaLossGainRdTimeSpan=_NbsSlaLossGainRdTimeSpan_Object((1,3,6,1,4,1,629,216,2,2,1,25),_NbsSlaLossGainRdTimeSpan_Type())
nbsSlaLossGainRdTimeSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainRdTimeSpan.setStatus(_A)
_NbsSlaLossGainAdAllFrames_Type=Counter64
_NbsSlaLossGainAdAllFrames_Object=MibTableColumn
nbsSlaLossGainAdAllFrames=_NbsSlaLossGainAdAllFrames_Object((1,3,6,1,4,1,629,216,2,2,1,26),_NbsSlaLossGainAdAllFrames_Type())
nbsSlaLossGainAdAllFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdAllFrames.setStatus(_A)
_NbsSlaLossGainAdBadFrames_Type=Counter64
_NbsSlaLossGainAdBadFrames_Object=MibTableColumn
nbsSlaLossGainAdBadFrames=_NbsSlaLossGainAdBadFrames_Object((1,3,6,1,4,1,629,216,2,2,1,27),_NbsSlaLossGainAdBadFrames_Type())
nbsSlaLossGainAdBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdBadFrames.setStatus(_A)
_NbsSlaLossGainAdDiscards_Type=Counter64
_NbsSlaLossGainAdDiscards_Object=MibTableColumn
nbsSlaLossGainAdDiscards=_NbsSlaLossGainAdDiscards_Object((1,3,6,1,4,1,629,216,2,2,1,28),_NbsSlaLossGainAdDiscards_Type())
nbsSlaLossGainAdDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdDiscards.setStatus(_A)
_NbsSlaLossGainAdUcastFrames_Type=Counter64
_NbsSlaLossGainAdUcastFrames_Object=MibTableColumn
nbsSlaLossGainAdUcastFrames=_NbsSlaLossGainAdUcastFrames_Object((1,3,6,1,4,1,629,216,2,2,1,29),_NbsSlaLossGainAdUcastFrames_Type())
nbsSlaLossGainAdUcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdUcastFrames.setStatus(_A)
_NbsSlaLossGainAdMcastFrames_Type=Counter64
_NbsSlaLossGainAdMcastFrames_Object=MibTableColumn
nbsSlaLossGainAdMcastFrames=_NbsSlaLossGainAdMcastFrames_Object((1,3,6,1,4,1,629,216,2,2,1,30),_NbsSlaLossGainAdMcastFrames_Type())
nbsSlaLossGainAdMcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdMcastFrames.setStatus(_A)
_NbsSlaLossGainAdBcastFrames_Type=Counter64
_NbsSlaLossGainAdBcastFrames_Object=MibTableColumn
nbsSlaLossGainAdBcastFrames=_NbsSlaLossGainAdBcastFrames_Object((1,3,6,1,4,1,629,216,2,2,1,31),_NbsSlaLossGainAdBcastFrames_Type())
nbsSlaLossGainAdBcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdBcastFrames.setStatus(_A)
_NbsSlaLossGainAdSize64_Type=Counter64
_NbsSlaLossGainAdSize64_Object=MibTableColumn
nbsSlaLossGainAdSize64=_NbsSlaLossGainAdSize64_Object((1,3,6,1,4,1,629,216,2,2,1,32),_NbsSlaLossGainAdSize64_Type())
nbsSlaLossGainAdSize64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize64.setStatus(_A)
_NbsSlaLossGainAdSize65to127_Type=Counter64
_NbsSlaLossGainAdSize65to127_Object=MibTableColumn
nbsSlaLossGainAdSize65to127=_NbsSlaLossGainAdSize65to127_Object((1,3,6,1,4,1,629,216,2,2,1,33),_NbsSlaLossGainAdSize65to127_Type())
nbsSlaLossGainAdSize65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize65to127.setStatus(_A)
_NbsSlaLossGainAdSize128to255_Type=Counter64
_NbsSlaLossGainAdSize128to255_Object=MibTableColumn
nbsSlaLossGainAdSize128to255=_NbsSlaLossGainAdSize128to255_Object((1,3,6,1,4,1,629,216,2,2,1,34),_NbsSlaLossGainAdSize128to255_Type())
nbsSlaLossGainAdSize128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize128to255.setStatus(_A)
_NbsSlaLossGainAdSize256to511_Type=Counter64
_NbsSlaLossGainAdSize256to511_Object=MibTableColumn
nbsSlaLossGainAdSize256to511=_NbsSlaLossGainAdSize256to511_Object((1,3,6,1,4,1,629,216,2,2,1,35),_NbsSlaLossGainAdSize256to511_Type())
nbsSlaLossGainAdSize256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize256to511.setStatus(_A)
_NbsSlaLossGainAdSize512to1023_Type=Counter64
_NbsSlaLossGainAdSize512to1023_Object=MibTableColumn
nbsSlaLossGainAdSize512to1023=_NbsSlaLossGainAdSize512to1023_Object((1,3,6,1,4,1,629,216,2,2,1,36),_NbsSlaLossGainAdSize512to1023_Type())
nbsSlaLossGainAdSize512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize512to1023.setStatus(_A)
_NbsSlaLossGainAdSize1024toEthMax_Type=Counter64
_NbsSlaLossGainAdSize1024toEthMax_Object=MibTableColumn
nbsSlaLossGainAdSize1024toEthMax=_NbsSlaLossGainAdSize1024toEthMax_Object((1,3,6,1,4,1,629,216,2,2,1,37),_NbsSlaLossGainAdSize1024toEthMax_Type())
nbsSlaLossGainAdSize1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize1024toEthMax.setStatus(_A)
_NbsSlaLossGainAdSizeEthMaxto2047_Type=Counter64
_NbsSlaLossGainAdSizeEthMaxto2047_Object=MibTableColumn
nbsSlaLossGainAdSizeEthMaxto2047=_NbsSlaLossGainAdSizeEthMaxto2047_Object((1,3,6,1,4,1,629,216,2,2,1,38),_NbsSlaLossGainAdSizeEthMaxto2047_Type())
nbsSlaLossGainAdSizeEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSizeEthMaxto2047.setStatus(_A)
_NbsSlaLossGainAdSize2048to4095_Type=Counter64
_NbsSlaLossGainAdSize2048to4095_Object=MibTableColumn
nbsSlaLossGainAdSize2048to4095=_NbsSlaLossGainAdSize2048to4095_Object((1,3,6,1,4,1,629,216,2,2,1,39),_NbsSlaLossGainAdSize2048to4095_Type())
nbsSlaLossGainAdSize2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize2048to4095.setStatus(_A)
_NbsSlaLossGainAdSize4096to8191_Type=Counter64
_NbsSlaLossGainAdSize4096to8191_Object=MibTableColumn
nbsSlaLossGainAdSize4096to8191=_NbsSlaLossGainAdSize4096to8191_Object((1,3,6,1,4,1,629,216,2,2,1,40),_NbsSlaLossGainAdSize4096to8191_Type())
nbsSlaLossGainAdSize4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize4096to8191.setStatus(_A)
_NbsSlaLossGainAdSize8192orMore_Type=Counter64
_NbsSlaLossGainAdSize8192orMore_Object=MibTableColumn
nbsSlaLossGainAdSize8192orMore=_NbsSlaLossGainAdSize8192orMore_Object((1,3,6,1,4,1,629,216,2,2,1,41),_NbsSlaLossGainAdSize8192orMore_Type())
nbsSlaLossGainAdSize8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdSize8192orMore.setStatus(_A)
_NbsSlaLossGainAdFrameDivisor_Type=Counter64
_NbsSlaLossGainAdFrameDivisor_Object=MibTableColumn
nbsSlaLossGainAdFrameDivisor=_NbsSlaLossGainAdFrameDivisor_Object((1,3,6,1,4,1,629,216,2,2,1,42),_NbsSlaLossGainAdFrameDivisor_Type())
nbsSlaLossGainAdFrameDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdFrameDivisor.setStatus(_A)
_NbsSlaLossGainAdAllOctets_Type=Counter64
_NbsSlaLossGainAdAllOctets_Object=MibTableColumn
nbsSlaLossGainAdAllOctets=_NbsSlaLossGainAdAllOctets_Object((1,3,6,1,4,1,629,216,2,2,1,43),_NbsSlaLossGainAdAllOctets_Type())
nbsSlaLossGainAdAllOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdAllOctets.setStatus(_A)
_NbsSlaLossGainAdBadOctets_Type=Counter64
_NbsSlaLossGainAdBadOctets_Object=MibTableColumn
nbsSlaLossGainAdBadOctets=_NbsSlaLossGainAdBadOctets_Object((1,3,6,1,4,1,629,216,2,2,1,44),_NbsSlaLossGainAdBadOctets_Type())
nbsSlaLossGainAdBadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdBadOctets.setStatus(_A)
_NbsSlaLossGainAdOctetDivisor_Type=Counter64
_NbsSlaLossGainAdOctetDivisor_Object=MibTableColumn
nbsSlaLossGainAdOctetDivisor=_NbsSlaLossGainAdOctetDivisor_Object((1,3,6,1,4,1,629,216,2,2,1,45),_NbsSlaLossGainAdOctetDivisor_Type())
nbsSlaLossGainAdOctetDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdOctetDivisor.setStatus(_A)
_NbsSlaLossGainAdTimeSpan_Type=Counter32
_NbsSlaLossGainAdTimeSpan_Object=MibTableColumn
nbsSlaLossGainAdTimeSpan=_NbsSlaLossGainAdTimeSpan_Object((1,3,6,1,4,1,629,216,2,2,1,46),_NbsSlaLossGainAdTimeSpan_Type())
nbsSlaLossGainAdTimeSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaLossGainAdTimeSpan.setStatus(_A)
_NbsSlaPerfMonGrp_ObjectIdentity=ObjectIdentity
nbsSlaPerfMonGrp=_NbsSlaPerfMonGrp_ObjectIdentity((1,3,6,1,4,1,629,216,3))
if mibBuilder.loadTexts:nbsSlaPerfMonGrp.setStatus(_A)
_NbsSlaPerfMonTableSize_Type=Counter32
_NbsSlaPerfMonTableSize_Object=MibScalar
nbsSlaPerfMonTableSize=_NbsSlaPerfMonTableSize_Object((1,3,6,1,4,1,629,216,3,1),_NbsSlaPerfMonTableSize_Type())
nbsSlaPerfMonTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonTableSize.setStatus(_A)
_NbsSlaPerfMonTable_Object=MibTable
nbsSlaPerfMonTable=_NbsSlaPerfMonTable_Object((1,3,6,1,4,1,629,216,3,2))
if mibBuilder.loadTexts:nbsSlaPerfMonTable.setStatus(_A)
_NbsSlaPerfMonEntry_Object=MibTableRow
nbsSlaPerfMonEntry=_NbsSlaPerfMonEntry_Object((1,3,6,1,4,1,629,216,3,2,1))
nbsSlaPerfMonEntry.setIndexNames((0,_I,_U))
if mibBuilder.loadTexts:nbsSlaPerfMonEntry.setStatus(_A)
_NbsSlaPerfMonIfIndex_Type=InterfaceIndex
_NbsSlaPerfMonIfIndex_Object=MibTableColumn
nbsSlaPerfMonIfIndex=_NbsSlaPerfMonIfIndex_Object((1,3,6,1,4,1,629,216,3,2,1,1),_NbsSlaPerfMonIfIndex_Type())
nbsSlaPerfMonIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsSlaPerfMonIfIndex.setStatus(_A)
class _NbsSlaPerfMonAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),(_S,2),(_K,3),(_L,4),('reflect',5),('forward',6),(_T,7),('complete',8),('stopping',9)))
_NbsSlaPerfMonAction_Type.__name__=_D
_NbsSlaPerfMonAction_Object=MibTableColumn
nbsSlaPerfMonAction=_NbsSlaPerfMonAction_Object((1,3,6,1,4,1,629,216,3,2,1,2),_NbsSlaPerfMonAction_Type())
nbsSlaPerfMonAction.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaPerfMonAction.setStatus(_A)
class _NbsSlaPerfMonSize_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9600))
_NbsSlaPerfMonSize_Type.__name__=_D
_NbsSlaPerfMonSize_Object=MibTableColumn
nbsSlaPerfMonSize=_NbsSlaPerfMonSize_Object((1,3,6,1,4,1,629,216,3,2,1,3),_NbsSlaPerfMonSize_Type())
nbsSlaPerfMonSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaPerfMonSize.setStatus(_A)
class _NbsSlaPerfMonDuration_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,604800))
_NbsSlaPerfMonDuration_Type.__name__=_D
_NbsSlaPerfMonDuration_Object=MibTableColumn
nbsSlaPerfMonDuration=_NbsSlaPerfMonDuration_Object((1,3,6,1,4,1,629,216,3,2,1,4),_NbsSlaPerfMonDuration_Type())
nbsSlaPerfMonDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSlaPerfMonDuration.setStatus(_A)
class _NbsSlaPerfMonTimeLeft_Type(Integer32):defaultValue=60
_NbsSlaPerfMonTimeLeft_Type.__name__=_D
_NbsSlaPerfMonTimeLeft_Object=MibTableColumn
nbsSlaPerfMonTimeLeft=_NbsSlaPerfMonTimeLeft_Object((1,3,6,1,4,1,629,216,3,2,1,5),_NbsSlaPerfMonTimeLeft_Type())
nbsSlaPerfMonTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonTimeLeft.setStatus(_A)
class _NbsSlaPerfMonEthMax_Type(Integer32):defaultValue=1518
_NbsSlaPerfMonEthMax_Type.__name__=_D
_NbsSlaPerfMonEthMax_Object=MibTableColumn
nbsSlaPerfMonEthMax=_NbsSlaPerfMonEthMax_Object((1,3,6,1,4,1,629,216,3,2,1,6),_NbsSlaPerfMonEthMax_Type())
nbsSlaPerfMonEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonEthMax.setStatus(_A)
_NbsSlaPerfMonAvgAllSizes_Type=Counter32
_NbsSlaPerfMonAvgAllSizes_Object=MibTableColumn
nbsSlaPerfMonAvgAllSizes=_NbsSlaPerfMonAvgAllSizes_Object((1,3,6,1,4,1,629,216,3,2,1,7),_NbsSlaPerfMonAvgAllSizes_Type())
nbsSlaPerfMonAvgAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvgAllSizes.setStatus(_A)
_NbsSlaPerfMonAvg64_Type=Counter32
_NbsSlaPerfMonAvg64_Object=MibTableColumn
nbsSlaPerfMonAvg64=_NbsSlaPerfMonAvg64_Object((1,3,6,1,4,1,629,216,3,2,1,8),_NbsSlaPerfMonAvg64_Type())
nbsSlaPerfMonAvg64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg64.setStatus(_A)
_NbsSlaPerfMonAvg65to127_Type=Counter32
_NbsSlaPerfMonAvg65to127_Object=MibTableColumn
nbsSlaPerfMonAvg65to127=_NbsSlaPerfMonAvg65to127_Object((1,3,6,1,4,1,629,216,3,2,1,9),_NbsSlaPerfMonAvg65to127_Type())
nbsSlaPerfMonAvg65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg65to127.setStatus(_A)
_NbsSlaPerfMonAvg128to255_Type=Counter32
_NbsSlaPerfMonAvg128to255_Object=MibTableColumn
nbsSlaPerfMonAvg128to255=_NbsSlaPerfMonAvg128to255_Object((1,3,6,1,4,1,629,216,3,2,1,10),_NbsSlaPerfMonAvg128to255_Type())
nbsSlaPerfMonAvg128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg128to255.setStatus(_A)
_NbsSlaPerfMonAvg256to511_Type=Counter32
_NbsSlaPerfMonAvg256to511_Object=MibTableColumn
nbsSlaPerfMonAvg256to511=_NbsSlaPerfMonAvg256to511_Object((1,3,6,1,4,1,629,216,3,2,1,11),_NbsSlaPerfMonAvg256to511_Type())
nbsSlaPerfMonAvg256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg256to511.setStatus(_A)
_NbsSlaPerfMonAvg512to1023_Type=Counter32
_NbsSlaPerfMonAvg512to1023_Object=MibTableColumn
nbsSlaPerfMonAvg512to1023=_NbsSlaPerfMonAvg512to1023_Object((1,3,6,1,4,1,629,216,3,2,1,12),_NbsSlaPerfMonAvg512to1023_Type())
nbsSlaPerfMonAvg512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg512to1023.setStatus(_A)
_NbsSlaPerfMonAvg1024toEthMax_Type=Counter32
_NbsSlaPerfMonAvg1024toEthMax_Object=MibTableColumn
nbsSlaPerfMonAvg1024toEthMax=_NbsSlaPerfMonAvg1024toEthMax_Object((1,3,6,1,4,1,629,216,3,2,1,13),_NbsSlaPerfMonAvg1024toEthMax_Type())
nbsSlaPerfMonAvg1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg1024toEthMax.setStatus(_A)
_NbsSlaPerfMonAvgEthMaxto2047_Type=Counter32
_NbsSlaPerfMonAvgEthMaxto2047_Object=MibTableColumn
nbsSlaPerfMonAvgEthMaxto2047=_NbsSlaPerfMonAvgEthMaxto2047_Object((1,3,6,1,4,1,629,216,3,2,1,14),_NbsSlaPerfMonAvgEthMaxto2047_Type())
nbsSlaPerfMonAvgEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvgEthMaxto2047.setStatus(_A)
_NbsSlaPerfMonAvg2048to4095_Type=Counter32
_NbsSlaPerfMonAvg2048to4095_Object=MibTableColumn
nbsSlaPerfMonAvg2048to4095=_NbsSlaPerfMonAvg2048to4095_Object((1,3,6,1,4,1,629,216,3,2,1,15),_NbsSlaPerfMonAvg2048to4095_Type())
nbsSlaPerfMonAvg2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg2048to4095.setStatus(_A)
_NbsSlaPerfMonAvg4096to8191_Type=Counter32
_NbsSlaPerfMonAvg4096to8191_Object=MibTableColumn
nbsSlaPerfMonAvg4096to8191=_NbsSlaPerfMonAvg4096to8191_Object((1,3,6,1,4,1,629,216,3,2,1,16),_NbsSlaPerfMonAvg4096to8191_Type())
nbsSlaPerfMonAvg4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg4096to8191.setStatus(_A)
_NbsSlaPerfMonAvg8192orMore_Type=Counter32
_NbsSlaPerfMonAvg8192orMore_Object=MibTableColumn
nbsSlaPerfMonAvg8192orMore=_NbsSlaPerfMonAvg8192orMore_Object((1,3,6,1,4,1,629,216,3,2,1,17),_NbsSlaPerfMonAvg8192orMore_Type())
nbsSlaPerfMonAvg8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonAvg8192orMore.setStatus(_A)
_NbsSlaPerfMonMinAllSizes_Type=Counter32
_NbsSlaPerfMonMinAllSizes_Object=MibTableColumn
nbsSlaPerfMonMinAllSizes=_NbsSlaPerfMonMinAllSizes_Object((1,3,6,1,4,1,629,216,3,2,1,18),_NbsSlaPerfMonMinAllSizes_Type())
nbsSlaPerfMonMinAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMinAllSizes.setStatus(_A)
_NbsSlaPerfMonMin64_Type=Counter32
_NbsSlaPerfMonMin64_Object=MibTableColumn
nbsSlaPerfMonMin64=_NbsSlaPerfMonMin64_Object((1,3,6,1,4,1,629,216,3,2,1,19),_NbsSlaPerfMonMin64_Type())
nbsSlaPerfMonMin64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin64.setStatus(_A)
_NbsSlaPerfMonMin65to127_Type=Counter32
_NbsSlaPerfMonMin65to127_Object=MibTableColumn
nbsSlaPerfMonMin65to127=_NbsSlaPerfMonMin65to127_Object((1,3,6,1,4,1,629,216,3,2,1,20),_NbsSlaPerfMonMin65to127_Type())
nbsSlaPerfMonMin65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin65to127.setStatus(_A)
_NbsSlaPerfMonMin128to255_Type=Counter32
_NbsSlaPerfMonMin128to255_Object=MibTableColumn
nbsSlaPerfMonMin128to255=_NbsSlaPerfMonMin128to255_Object((1,3,6,1,4,1,629,216,3,2,1,21),_NbsSlaPerfMonMin128to255_Type())
nbsSlaPerfMonMin128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin128to255.setStatus(_A)
_NbsSlaPerfMonMin256to511_Type=Counter32
_NbsSlaPerfMonMin256to511_Object=MibTableColumn
nbsSlaPerfMonMin256to511=_NbsSlaPerfMonMin256to511_Object((1,3,6,1,4,1,629,216,3,2,1,22),_NbsSlaPerfMonMin256to511_Type())
nbsSlaPerfMonMin256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin256to511.setStatus(_A)
_NbsSlaPerfMonMin512to1023_Type=Counter32
_NbsSlaPerfMonMin512to1023_Object=MibTableColumn
nbsSlaPerfMonMin512to1023=_NbsSlaPerfMonMin512to1023_Object((1,3,6,1,4,1,629,216,3,2,1,23),_NbsSlaPerfMonMin512to1023_Type())
nbsSlaPerfMonMin512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin512to1023.setStatus(_A)
_NbsSlaPerfMonMin1024toEthMax_Type=Counter32
_NbsSlaPerfMonMin1024toEthMax_Object=MibTableColumn
nbsSlaPerfMonMin1024toEthMax=_NbsSlaPerfMonMin1024toEthMax_Object((1,3,6,1,4,1,629,216,3,2,1,24),_NbsSlaPerfMonMin1024toEthMax_Type())
nbsSlaPerfMonMin1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin1024toEthMax.setStatus(_A)
_NbsSlaPerfMonMinEthMaxto2047_Type=Counter32
_NbsSlaPerfMonMinEthMaxto2047_Object=MibTableColumn
nbsSlaPerfMonMinEthMaxto2047=_NbsSlaPerfMonMinEthMaxto2047_Object((1,3,6,1,4,1,629,216,3,2,1,25),_NbsSlaPerfMonMinEthMaxto2047_Type())
nbsSlaPerfMonMinEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMinEthMaxto2047.setStatus(_A)
_NbsSlaPerfMonMin2048to4095_Type=Counter32
_NbsSlaPerfMonMin2048to4095_Object=MibTableColumn
nbsSlaPerfMonMin2048to4095=_NbsSlaPerfMonMin2048to4095_Object((1,3,6,1,4,1,629,216,3,2,1,26),_NbsSlaPerfMonMin2048to4095_Type())
nbsSlaPerfMonMin2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin2048to4095.setStatus(_A)
_NbsSlaPerfMonMin4096to8191_Type=Counter32
_NbsSlaPerfMonMin4096to8191_Object=MibTableColumn
nbsSlaPerfMonMin4096to8191=_NbsSlaPerfMonMin4096to8191_Object((1,3,6,1,4,1,629,216,3,2,1,27),_NbsSlaPerfMonMin4096to8191_Type())
nbsSlaPerfMonMin4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin4096to8191.setStatus(_A)
_NbsSlaPerfMonMin8192orMore_Type=Counter32
_NbsSlaPerfMonMin8192orMore_Object=MibTableColumn
nbsSlaPerfMonMin8192orMore=_NbsSlaPerfMonMin8192orMore_Object((1,3,6,1,4,1,629,216,3,2,1,28),_NbsSlaPerfMonMin8192orMore_Type())
nbsSlaPerfMonMin8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMin8192orMore.setStatus(_A)
_NbsSlaPerfMonMaxAllSizes_Type=Counter32
_NbsSlaPerfMonMaxAllSizes_Object=MibTableColumn
nbsSlaPerfMonMaxAllSizes=_NbsSlaPerfMonMaxAllSizes_Object((1,3,6,1,4,1,629,216,3,2,1,29),_NbsSlaPerfMonMaxAllSizes_Type())
nbsSlaPerfMonMaxAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMaxAllSizes.setStatus(_A)
_NbsSlaPerfMonMax64_Type=Counter32
_NbsSlaPerfMonMax64_Object=MibTableColumn
nbsSlaPerfMonMax64=_NbsSlaPerfMonMax64_Object((1,3,6,1,4,1,629,216,3,2,1,30),_NbsSlaPerfMonMax64_Type())
nbsSlaPerfMonMax64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax64.setStatus(_A)
_NbsSlaPerfMonMax65to127_Type=Counter32
_NbsSlaPerfMonMax65to127_Object=MibTableColumn
nbsSlaPerfMonMax65to127=_NbsSlaPerfMonMax65to127_Object((1,3,6,1,4,1,629,216,3,2,1,31),_NbsSlaPerfMonMax65to127_Type())
nbsSlaPerfMonMax65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax65to127.setStatus(_A)
_NbsSlaPerfMonMax128to255_Type=Counter32
_NbsSlaPerfMonMax128to255_Object=MibTableColumn
nbsSlaPerfMonMax128to255=_NbsSlaPerfMonMax128to255_Object((1,3,6,1,4,1,629,216,3,2,1,32),_NbsSlaPerfMonMax128to255_Type())
nbsSlaPerfMonMax128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax128to255.setStatus(_A)
_NbsSlaPerfMonMax256to511_Type=Counter32
_NbsSlaPerfMonMax256to511_Object=MibTableColumn
nbsSlaPerfMonMax256to511=_NbsSlaPerfMonMax256to511_Object((1,3,6,1,4,1,629,216,3,2,1,33),_NbsSlaPerfMonMax256to511_Type())
nbsSlaPerfMonMax256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax256to511.setStatus(_A)
_NbsSlaPerfMonMax512to1023_Type=Counter32
_NbsSlaPerfMonMax512to1023_Object=MibTableColumn
nbsSlaPerfMonMax512to1023=_NbsSlaPerfMonMax512to1023_Object((1,3,6,1,4,1,629,216,3,2,1,34),_NbsSlaPerfMonMax512to1023_Type())
nbsSlaPerfMonMax512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax512to1023.setStatus(_A)
_NbsSlaPerfMonMax1024toEthMax_Type=Counter32
_NbsSlaPerfMonMax1024toEthMax_Object=MibTableColumn
nbsSlaPerfMonMax1024toEthMax=_NbsSlaPerfMonMax1024toEthMax_Object((1,3,6,1,4,1,629,216,3,2,1,35),_NbsSlaPerfMonMax1024toEthMax_Type())
nbsSlaPerfMonMax1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax1024toEthMax.setStatus(_A)
_NbsSlaPerfMonMaxEthMaxto2047_Type=Counter32
_NbsSlaPerfMonMaxEthMaxto2047_Object=MibTableColumn
nbsSlaPerfMonMaxEthMaxto2047=_NbsSlaPerfMonMaxEthMaxto2047_Object((1,3,6,1,4,1,629,216,3,2,1,36),_NbsSlaPerfMonMaxEthMaxto2047_Type())
nbsSlaPerfMonMaxEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMaxEthMaxto2047.setStatus(_A)
_NbsSlaPerfMonMax2048to4095_Type=Counter32
_NbsSlaPerfMonMax2048to4095_Object=MibTableColumn
nbsSlaPerfMonMax2048to4095=_NbsSlaPerfMonMax2048to4095_Object((1,3,6,1,4,1,629,216,3,2,1,37),_NbsSlaPerfMonMax2048to4095_Type())
nbsSlaPerfMonMax2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax2048to4095.setStatus(_A)
_NbsSlaPerfMonMax4096to8191_Type=Counter32
_NbsSlaPerfMonMax4096to8191_Object=MibTableColumn
nbsSlaPerfMonMax4096to8191=_NbsSlaPerfMonMax4096to8191_Object((1,3,6,1,4,1,629,216,3,2,1,38),_NbsSlaPerfMonMax4096to8191_Type())
nbsSlaPerfMonMax4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax4096to8191.setStatus(_A)
_NbsSlaPerfMonMax8192orMore_Type=Counter32
_NbsSlaPerfMonMax8192orMore_Object=MibTableColumn
nbsSlaPerfMonMax8192orMore=_NbsSlaPerfMonMax8192orMore_Object((1,3,6,1,4,1,629,216,3,2,1,39),_NbsSlaPerfMonMax8192orMore_Type())
nbsSlaPerfMonMax8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonMax8192orMore.setStatus(_A)
_NbsSlaPerfMonFramesAllSizes_Type=Counter64
_NbsSlaPerfMonFramesAllSizes_Object=MibTableColumn
nbsSlaPerfMonFramesAllSizes=_NbsSlaPerfMonFramesAllSizes_Object((1,3,6,1,4,1,629,216,3,2,1,40),_NbsSlaPerfMonFramesAllSizes_Type())
nbsSlaPerfMonFramesAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFramesAllSizes.setStatus(_A)
_NbsSlaPerfMonFrames64_Type=Counter64
_NbsSlaPerfMonFrames64_Object=MibTableColumn
nbsSlaPerfMonFrames64=_NbsSlaPerfMonFrames64_Object((1,3,6,1,4,1,629,216,3,2,1,41),_NbsSlaPerfMonFrames64_Type())
nbsSlaPerfMonFrames64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames64.setStatus(_A)
_NbsSlaPerfMonFrames65to127_Type=Counter64
_NbsSlaPerfMonFrames65to127_Object=MibTableColumn
nbsSlaPerfMonFrames65to127=_NbsSlaPerfMonFrames65to127_Object((1,3,6,1,4,1,629,216,3,2,1,42),_NbsSlaPerfMonFrames65to127_Type())
nbsSlaPerfMonFrames65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames65to127.setStatus(_A)
_NbsSlaPerfMonFrames128to255_Type=Counter64
_NbsSlaPerfMonFrames128to255_Object=MibTableColumn
nbsSlaPerfMonFrames128to255=_NbsSlaPerfMonFrames128to255_Object((1,3,6,1,4,1,629,216,3,2,1,43),_NbsSlaPerfMonFrames128to255_Type())
nbsSlaPerfMonFrames128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames128to255.setStatus(_A)
_NbsSlaPerfMonFrames256to511_Type=Counter64
_NbsSlaPerfMonFrames256to511_Object=MibTableColumn
nbsSlaPerfMonFrames256to511=_NbsSlaPerfMonFrames256to511_Object((1,3,6,1,4,1,629,216,3,2,1,44),_NbsSlaPerfMonFrames256to511_Type())
nbsSlaPerfMonFrames256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames256to511.setStatus(_A)
_NbsSlaPerfMonFrames512to1023_Type=Counter64
_NbsSlaPerfMonFrames512to1023_Object=MibTableColumn
nbsSlaPerfMonFrames512to1023=_NbsSlaPerfMonFrames512to1023_Object((1,3,6,1,4,1,629,216,3,2,1,45),_NbsSlaPerfMonFrames512to1023_Type())
nbsSlaPerfMonFrames512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames512to1023.setStatus(_A)
_NbsSlaPerfMonFrames1024toEthMax_Type=Counter64
_NbsSlaPerfMonFrames1024toEthMax_Object=MibTableColumn
nbsSlaPerfMonFrames1024toEthMax=_NbsSlaPerfMonFrames1024toEthMax_Object((1,3,6,1,4,1,629,216,3,2,1,46),_NbsSlaPerfMonFrames1024toEthMax_Type())
nbsSlaPerfMonFrames1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames1024toEthMax.setStatus(_A)
_NbsSlaPerfMonFramesEthMaxto2047_Type=Counter64
_NbsSlaPerfMonFramesEthMaxto2047_Object=MibTableColumn
nbsSlaPerfMonFramesEthMaxto2047=_NbsSlaPerfMonFramesEthMaxto2047_Object((1,3,6,1,4,1,629,216,3,2,1,47),_NbsSlaPerfMonFramesEthMaxto2047_Type())
nbsSlaPerfMonFramesEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFramesEthMaxto2047.setStatus(_A)
_NbsSlaPerfMonFrames2048to4095_Type=Counter64
_NbsSlaPerfMonFrames2048to4095_Object=MibTableColumn
nbsSlaPerfMonFrames2048to4095=_NbsSlaPerfMonFrames2048to4095_Object((1,3,6,1,4,1,629,216,3,2,1,48),_NbsSlaPerfMonFrames2048to4095_Type())
nbsSlaPerfMonFrames2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames2048to4095.setStatus(_A)
_NbsSlaPerfMonFrames4096to8191_Type=Counter64
_NbsSlaPerfMonFrames4096to8191_Object=MibTableColumn
nbsSlaPerfMonFrames4096to8191=_NbsSlaPerfMonFrames4096to8191_Object((1,3,6,1,4,1,629,216,3,2,1,49),_NbsSlaPerfMonFrames4096to8191_Type())
nbsSlaPerfMonFrames4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames4096to8191.setStatus(_A)
_NbsSlaPerfMonFrames8192orMore_Type=Counter64
_NbsSlaPerfMonFrames8192orMore_Object=MibTableColumn
nbsSlaPerfMonFrames8192orMore=_NbsSlaPerfMonFrames8192orMore_Object((1,3,6,1,4,1,629,216,3,2,1,50),_NbsSlaPerfMonFrames8192orMore_Type())
nbsSlaPerfMonFrames8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonFrames8192orMore.setStatus(_A)
_NbsSlaPerfMonOctetsAllSizes_Type=Counter64
_NbsSlaPerfMonOctetsAllSizes_Object=MibTableColumn
nbsSlaPerfMonOctetsAllSizes=_NbsSlaPerfMonOctetsAllSizes_Object((1,3,6,1,4,1,629,216,3,2,1,51),_NbsSlaPerfMonOctetsAllSizes_Type())
nbsSlaPerfMonOctetsAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctetsAllSizes.setStatus(_A)
_NbsSlaPerfMonOctets64_Type=Counter64
_NbsSlaPerfMonOctets64_Object=MibTableColumn
nbsSlaPerfMonOctets64=_NbsSlaPerfMonOctets64_Object((1,3,6,1,4,1,629,216,3,2,1,52),_NbsSlaPerfMonOctets64_Type())
nbsSlaPerfMonOctets64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets64.setStatus(_A)
_NbsSlaPerfMonOctets65to127_Type=Counter64
_NbsSlaPerfMonOctets65to127_Object=MibTableColumn
nbsSlaPerfMonOctets65to127=_NbsSlaPerfMonOctets65to127_Object((1,3,6,1,4,1,629,216,3,2,1,53),_NbsSlaPerfMonOctets65to127_Type())
nbsSlaPerfMonOctets65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets65to127.setStatus(_A)
_NbsSlaPerfMonOctets128to255_Type=Counter64
_NbsSlaPerfMonOctets128to255_Object=MibTableColumn
nbsSlaPerfMonOctets128to255=_NbsSlaPerfMonOctets128to255_Object((1,3,6,1,4,1,629,216,3,2,1,54),_NbsSlaPerfMonOctets128to255_Type())
nbsSlaPerfMonOctets128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets128to255.setStatus(_A)
_NbsSlaPerfMonOctets256to511_Type=Counter64
_NbsSlaPerfMonOctets256to511_Object=MibTableColumn
nbsSlaPerfMonOctets256to511=_NbsSlaPerfMonOctets256to511_Object((1,3,6,1,4,1,629,216,3,2,1,55),_NbsSlaPerfMonOctets256to511_Type())
nbsSlaPerfMonOctets256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets256to511.setStatus(_A)
_NbsSlaPerfMonOctets512to1023_Type=Counter64
_NbsSlaPerfMonOctets512to1023_Object=MibTableColumn
nbsSlaPerfMonOctets512to1023=_NbsSlaPerfMonOctets512to1023_Object((1,3,6,1,4,1,629,216,3,2,1,56),_NbsSlaPerfMonOctets512to1023_Type())
nbsSlaPerfMonOctets512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets512to1023.setStatus(_A)
_NbsSlaPerfMonOctets1024toEthMax_Type=Counter64
_NbsSlaPerfMonOctets1024toEthMax_Object=MibTableColumn
nbsSlaPerfMonOctets1024toEthMax=_NbsSlaPerfMonOctets1024toEthMax_Object((1,3,6,1,4,1,629,216,3,2,1,57),_NbsSlaPerfMonOctets1024toEthMax_Type())
nbsSlaPerfMonOctets1024toEthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets1024toEthMax.setStatus(_A)
_NbsSlaPerfMonOctetsEthMaxto2047_Type=Counter64
_NbsSlaPerfMonOctetsEthMaxto2047_Object=MibTableColumn
nbsSlaPerfMonOctetsEthMaxto2047=_NbsSlaPerfMonOctetsEthMaxto2047_Object((1,3,6,1,4,1,629,216,3,2,1,58),_NbsSlaPerfMonOctetsEthMaxto2047_Type())
nbsSlaPerfMonOctetsEthMaxto2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctetsEthMaxto2047.setStatus(_A)
_NbsSlaPerfMonOctets2048to4095_Type=Counter64
_NbsSlaPerfMonOctets2048to4095_Object=MibTableColumn
nbsSlaPerfMonOctets2048to4095=_NbsSlaPerfMonOctets2048to4095_Object((1,3,6,1,4,1,629,216,3,2,1,59),_NbsSlaPerfMonOctets2048to4095_Type())
nbsSlaPerfMonOctets2048to4095.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets2048to4095.setStatus(_A)
_NbsSlaPerfMonOctets4096to8191_Type=Counter64
_NbsSlaPerfMonOctets4096to8191_Object=MibTableColumn
nbsSlaPerfMonOctets4096to8191=_NbsSlaPerfMonOctets4096to8191_Object((1,3,6,1,4,1,629,216,3,2,1,60),_NbsSlaPerfMonOctets4096to8191_Type())
nbsSlaPerfMonOctets4096to8191.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets4096to8191.setStatus(_A)
_NbsSlaPerfMonOctets8192orMore_Type=Counter64
_NbsSlaPerfMonOctets8192orMore_Object=MibTableColumn
nbsSlaPerfMonOctets8192orMore=_NbsSlaPerfMonOctets8192orMore_Object((1,3,6,1,4,1,629,216,3,2,1,61),_NbsSlaPerfMonOctets8192orMore_Type())
nbsSlaPerfMonOctets8192orMore.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSlaPerfMonOctets8192orMore.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'nbsSlaMib':nbsSlaMib,'nbsSlaTrafficGenGrp':nbsSlaTrafficGenGrp,'nbsSlaTrafficGenTableSize':nbsSlaTrafficGenTableSize,'nbsSlaTrafficGenTable':nbsSlaTrafficGenTable,'nbsSlaTrafficGenEntry':nbsSlaTrafficGenEntry,_O:nbsSlaTrafficGenIfIndex,'nbsSlaTrafficGenAction':nbsSlaTrafficGenAction,'nbsSlaTrafficGenFrameSize':nbsSlaTrafficGenFrameSize,'nbsSlaTrafficGenFrameSizeType':nbsSlaTrafficGenFrameSizeType,'nbsSlaTrafficGenFrameCount':nbsSlaTrafficGenFrameCount,'nbsSlaTrafficGenFrameCountType':nbsSlaTrafficGenFrameCountType,'nbsSlaTrafficGenInterPacketGap':nbsSlaTrafficGenInterPacketGap,'nbsSlaTrafficGenMaxHeaders':nbsSlaTrafficGenMaxHeaders,'nbsSlaTrafficGenMaxPattern':nbsSlaTrafficGenMaxPattern,'nbsSlaTrafficGenHeaders':nbsSlaTrafficGenHeaders,'nbsSlaTrafficGenDa':nbsSlaTrafficGenDa,'nbsSlaTrafficGenDaType':nbsSlaTrafficGenDaType,'nbsSlaTrafficGenSa':nbsSlaTrafficGenSa,'nbsSlaTrafficGenSaType':nbsSlaTrafficGenSaType,'nbsSlaTrafficGenTag':nbsSlaTrafficGenTag,'nbsSlaTrafficGenTagType':nbsSlaTrafficGenTagType,'nbsSlaTrafficGenPattern':nbsSlaTrafficGenPattern,'nbsSlaTrafficGenPatternType':nbsSlaTrafficGenPatternType,'nbsSlaLossGainGrp':nbsSlaLossGainGrp,'nbsSlaLossGainTableSize':nbsSlaLossGainTableSize,'nbsSlaLossGainTable':nbsSlaLossGainTable,'nbsSlaLossGainEntry':nbsSlaLossGainEntry,_R:nbsSlaLossGainIfIndex,'nbsSlaLossGainAction':nbsSlaLossGainAction,'nbsSlaLossGainInterval':nbsSlaLossGainInterval,'nbsSlaLossGainEthMax':nbsSlaLossGainEthMax,'nbsSlaLossGainRdAllFrames':nbsSlaLossGainRdAllFrames,'nbsSlaLossGainRdBadFrames':nbsSlaLossGainRdBadFrames,'nbsSlaLossGainRdDiscards':nbsSlaLossGainRdDiscards,'nbsSlaLossGainRdUcastFrames':nbsSlaLossGainRdUcastFrames,'nbsSlaLossGainRdMcastFrames':nbsSlaLossGainRdMcastFrames,'nbsSlaLossGainRdBcastFrames':nbsSlaLossGainRdBcastFrames,'nbsSlaLossGainRdSize64':nbsSlaLossGainRdSize64,'nbsSlaLossGainRdSize65to127':nbsSlaLossGainRdSize65to127,'nbsSlaLossGainRdSize128to255':nbsSlaLossGainRdSize128to255,'nbsSlaLossGainRdSize256to511':nbsSlaLossGainRdSize256to511,'nbsSlaLossGainRdSize512to1023':nbsSlaLossGainRdSize512to1023,'nbsSlaLossGainRdSize1024toEthMax':nbsSlaLossGainRdSize1024toEthMax,'nbsSlaLossGainRdSizeEthMaxto2047':nbsSlaLossGainRdSizeEthMaxto2047,'nbsSlaLossGainRdSize2048to4095':nbsSlaLossGainRdSize2048to4095,'nbsSlaLossGainRdSize4096to8191':nbsSlaLossGainRdSize4096to8191,'nbsSlaLossGainRdSize8192orMore':nbsSlaLossGainRdSize8192orMore,'nbsSlaLossGainRdFrameDivisor':nbsSlaLossGainRdFrameDivisor,'nbsSlaLossGainRdAllOctets':nbsSlaLossGainRdAllOctets,'nbsSlaLossGainRdBadOctets':nbsSlaLossGainRdBadOctets,'nbsSlaLossGainRdOctetDivisor':nbsSlaLossGainRdOctetDivisor,'nbsSlaLossGainRdTimeSpan':nbsSlaLossGainRdTimeSpan,'nbsSlaLossGainAdAllFrames':nbsSlaLossGainAdAllFrames,'nbsSlaLossGainAdBadFrames':nbsSlaLossGainAdBadFrames,'nbsSlaLossGainAdDiscards':nbsSlaLossGainAdDiscards,'nbsSlaLossGainAdUcastFrames':nbsSlaLossGainAdUcastFrames,'nbsSlaLossGainAdMcastFrames':nbsSlaLossGainAdMcastFrames,'nbsSlaLossGainAdBcastFrames':nbsSlaLossGainAdBcastFrames,'nbsSlaLossGainAdSize64':nbsSlaLossGainAdSize64,'nbsSlaLossGainAdSize65to127':nbsSlaLossGainAdSize65to127,'nbsSlaLossGainAdSize128to255':nbsSlaLossGainAdSize128to255,'nbsSlaLossGainAdSize256to511':nbsSlaLossGainAdSize256to511,'nbsSlaLossGainAdSize512to1023':nbsSlaLossGainAdSize512to1023,'nbsSlaLossGainAdSize1024toEthMax':nbsSlaLossGainAdSize1024toEthMax,'nbsSlaLossGainAdSizeEthMaxto2047':nbsSlaLossGainAdSizeEthMaxto2047,'nbsSlaLossGainAdSize2048to4095':nbsSlaLossGainAdSize2048to4095,'nbsSlaLossGainAdSize4096to8191':nbsSlaLossGainAdSize4096to8191,'nbsSlaLossGainAdSize8192orMore':nbsSlaLossGainAdSize8192orMore,'nbsSlaLossGainAdFrameDivisor':nbsSlaLossGainAdFrameDivisor,'nbsSlaLossGainAdAllOctets':nbsSlaLossGainAdAllOctets,'nbsSlaLossGainAdBadOctets':nbsSlaLossGainAdBadOctets,'nbsSlaLossGainAdOctetDivisor':nbsSlaLossGainAdOctetDivisor,'nbsSlaLossGainAdTimeSpan':nbsSlaLossGainAdTimeSpan,'nbsSlaPerfMonGrp':nbsSlaPerfMonGrp,'nbsSlaPerfMonTableSize':nbsSlaPerfMonTableSize,'nbsSlaPerfMonTable':nbsSlaPerfMonTable,'nbsSlaPerfMonEntry':nbsSlaPerfMonEntry,_U:nbsSlaPerfMonIfIndex,'nbsSlaPerfMonAction':nbsSlaPerfMonAction,'nbsSlaPerfMonSize':nbsSlaPerfMonSize,'nbsSlaPerfMonDuration':nbsSlaPerfMonDuration,'nbsSlaPerfMonTimeLeft':nbsSlaPerfMonTimeLeft,'nbsSlaPerfMonEthMax':nbsSlaPerfMonEthMax,'nbsSlaPerfMonAvgAllSizes':nbsSlaPerfMonAvgAllSizes,'nbsSlaPerfMonAvg64':nbsSlaPerfMonAvg64,'nbsSlaPerfMonAvg65to127':nbsSlaPerfMonAvg65to127,'nbsSlaPerfMonAvg128to255':nbsSlaPerfMonAvg128to255,'nbsSlaPerfMonAvg256to511':nbsSlaPerfMonAvg256to511,'nbsSlaPerfMonAvg512to1023':nbsSlaPerfMonAvg512to1023,'nbsSlaPerfMonAvg1024toEthMax':nbsSlaPerfMonAvg1024toEthMax,'nbsSlaPerfMonAvgEthMaxto2047':nbsSlaPerfMonAvgEthMaxto2047,'nbsSlaPerfMonAvg2048to4095':nbsSlaPerfMonAvg2048to4095,'nbsSlaPerfMonAvg4096to8191':nbsSlaPerfMonAvg4096to8191,'nbsSlaPerfMonAvg8192orMore':nbsSlaPerfMonAvg8192orMore,'nbsSlaPerfMonMinAllSizes':nbsSlaPerfMonMinAllSizes,'nbsSlaPerfMonMin64':nbsSlaPerfMonMin64,'nbsSlaPerfMonMin65to127':nbsSlaPerfMonMin65to127,'nbsSlaPerfMonMin128to255':nbsSlaPerfMonMin128to255,'nbsSlaPerfMonMin256to511':nbsSlaPerfMonMin256to511,'nbsSlaPerfMonMin512to1023':nbsSlaPerfMonMin512to1023,'nbsSlaPerfMonMin1024toEthMax':nbsSlaPerfMonMin1024toEthMax,'nbsSlaPerfMonMinEthMaxto2047':nbsSlaPerfMonMinEthMaxto2047,'nbsSlaPerfMonMin2048to4095':nbsSlaPerfMonMin2048to4095,'nbsSlaPerfMonMin4096to8191':nbsSlaPerfMonMin4096to8191,'nbsSlaPerfMonMin8192orMore':nbsSlaPerfMonMin8192orMore,'nbsSlaPerfMonMaxAllSizes':nbsSlaPerfMonMaxAllSizes,'nbsSlaPerfMonMax64':nbsSlaPerfMonMax64,'nbsSlaPerfMonMax65to127':nbsSlaPerfMonMax65to127,'nbsSlaPerfMonMax128to255':nbsSlaPerfMonMax128to255,'nbsSlaPerfMonMax256to511':nbsSlaPerfMonMax256to511,'nbsSlaPerfMonMax512to1023':nbsSlaPerfMonMax512to1023,'nbsSlaPerfMonMax1024toEthMax':nbsSlaPerfMonMax1024toEthMax,'nbsSlaPerfMonMaxEthMaxto2047':nbsSlaPerfMonMaxEthMaxto2047,'nbsSlaPerfMonMax2048to4095':nbsSlaPerfMonMax2048to4095,'nbsSlaPerfMonMax4096to8191':nbsSlaPerfMonMax4096to8191,'nbsSlaPerfMonMax8192orMore':nbsSlaPerfMonMax8192orMore,'nbsSlaPerfMonFramesAllSizes':nbsSlaPerfMonFramesAllSizes,'nbsSlaPerfMonFrames64':nbsSlaPerfMonFrames64,'nbsSlaPerfMonFrames65to127':nbsSlaPerfMonFrames65to127,'nbsSlaPerfMonFrames128to255':nbsSlaPerfMonFrames128to255,'nbsSlaPerfMonFrames256to511':nbsSlaPerfMonFrames256to511,'nbsSlaPerfMonFrames512to1023':nbsSlaPerfMonFrames512to1023,'nbsSlaPerfMonFrames1024toEthMax':nbsSlaPerfMonFrames1024toEthMax,'nbsSlaPerfMonFramesEthMaxto2047':nbsSlaPerfMonFramesEthMaxto2047,'nbsSlaPerfMonFrames2048to4095':nbsSlaPerfMonFrames2048to4095,'nbsSlaPerfMonFrames4096to8191':nbsSlaPerfMonFrames4096to8191,'nbsSlaPerfMonFrames8192orMore':nbsSlaPerfMonFrames8192orMore,'nbsSlaPerfMonOctetsAllSizes':nbsSlaPerfMonOctetsAllSizes,'nbsSlaPerfMonOctets64':nbsSlaPerfMonOctets64,'nbsSlaPerfMonOctets65to127':nbsSlaPerfMonOctets65to127,'nbsSlaPerfMonOctets128to255':nbsSlaPerfMonOctets128to255,'nbsSlaPerfMonOctets256to511':nbsSlaPerfMonOctets256to511,'nbsSlaPerfMonOctets512to1023':nbsSlaPerfMonOctets512to1023,'nbsSlaPerfMonOctets1024toEthMax':nbsSlaPerfMonOctets1024toEthMax,'nbsSlaPerfMonOctetsEthMaxto2047':nbsSlaPerfMonOctetsEthMaxto2047,'nbsSlaPerfMonOctets2048to4095':nbsSlaPerfMonOctets2048to4095,'nbsSlaPerfMonOctets4096to8191':nbsSlaPerfMonOctets4096to8191,'nbsSlaPerfMonOctets8192orMore':nbsSlaPerfMonOctets8192orMore})