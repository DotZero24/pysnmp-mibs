_Z='nbsRoadmCommonCommittedChannels'
_Y='nbsRoadmCommonCommittedGridType'
_X='nbsRoadmCommittedCenterline'
_W='nbsRoadmCommittedIfIndex'
_V='nbsRoadmStagingCenterline'
_U='nbsRoadmStagingIfIndex'
_T='nbsRoadmFlexgridIfIndex'
_S='capable'
_R='read-write'
_Q='std50Ghz'
_P='std100Ghz'
_O='RowStatus'
_N='ifAlias'
_M='IF-MIB'
_L='nbsRoadmRedundantCenterline'
_K='nbsRoadmRedundantIfIndex'
_J='nbsRoadmCommonIfIndex'
_I='notSupported'
_H='NbsTcMilliDb'
_G='DisplayString'
_F='Integer32'
_E='read-create'
_D='NbsTcMHz'
_C='NBS-ROADM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_M,'InterfaceIndex',_N)
NbsTcMHz,NbsTcMilliDb,NbsTcStagingCommit,nbs=mibBuilder.importSymbols('NBS-MIB',_D,_H,'NbsTcStagingCommit','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress',_O,'TextualConvention')
nbsRoadmMib=ModuleIdentity((1,3,6,1,4,1,629,235))
_NbsRoadmCommonGrp_ObjectIdentity=ObjectIdentity
nbsRoadmCommonGrp=_NbsRoadmCommonGrp_ObjectIdentity((1,3,6,1,4,1,629,235,10))
if mibBuilder.loadTexts:nbsRoadmCommonGrp.setStatus(_A)
_NbsRoadmCommonTableSize_Type=Unsigned32
_NbsRoadmCommonTableSize_Object=MibScalar
nbsRoadmCommonTableSize=_NbsRoadmCommonTableSize_Object((1,3,6,1,4,1,629,235,10,1),_NbsRoadmCommonTableSize_Type())
nbsRoadmCommonTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommonTableSize.setStatus(_A)
_NbsRoadmCommonTable_Object=MibTable
nbsRoadmCommonTable=_NbsRoadmCommonTable_Object((1,3,6,1,4,1,629,235,10,2))
if mibBuilder.loadTexts:nbsRoadmCommonTable.setStatus(_A)
_NbsRoadmCommonEntry_Object=MibTableRow
nbsRoadmCommonEntry=_NbsRoadmCommonEntry_Object((1,3,6,1,4,1,629,235,10,2,1))
nbsRoadmCommonEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:nbsRoadmCommonEntry.setStatus(_A)
_NbsRoadmCommonIfIndex_Type=InterfaceIndex
_NbsRoadmCommonIfIndex_Object=MibTableColumn
nbsRoadmCommonIfIndex=_NbsRoadmCommonIfIndex_Object((1,3,6,1,4,1,629,235,10,2,1,1),_NbsRoadmCommonIfIndex_Type())
nbsRoadmCommonIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommonIfIndex.setStatus(_A)
class _NbsRoadmCommonStagingQuickCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('supported',2),(_P,3),(_Q,4)))
_NbsRoadmCommonStagingQuickCfg_Type.__name__=_F
_NbsRoadmCommonStagingQuickCfg_Object=MibTableColumn
nbsRoadmCommonStagingQuickCfg=_NbsRoadmCommonStagingQuickCfg_Object((1,3,6,1,4,1,629,235,10,2,1,10),_NbsRoadmCommonStagingQuickCfg_Type())
nbsRoadmCommonStagingQuickCfg.setMaxAccess(_R)
if mibBuilder.loadTexts:nbsRoadmCommonStagingQuickCfg.setStatus(_A)
class _NbsRoadmCommonStagingAddCaps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_S,2)))
_NbsRoadmCommonStagingAddCaps_Type.__name__=_F
_NbsRoadmCommonStagingAddCaps_Object=MibTableColumn
nbsRoadmCommonStagingAddCaps=_NbsRoadmCommonStagingAddCaps_Object((1,3,6,1,4,1,629,235,10,2,1,13),_NbsRoadmCommonStagingAddCaps_Type())
nbsRoadmCommonStagingAddCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommonStagingAddCaps.setStatus(_A)
class _NbsRoadmCommonStagingDropCaps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_S,2)))
_NbsRoadmCommonStagingDropCaps_Type.__name__=_F
_NbsRoadmCommonStagingDropCaps_Object=MibTableColumn
nbsRoadmCommonStagingDropCaps=_NbsRoadmCommonStagingDropCaps_Object((1,3,6,1,4,1,629,235,10,2,1,14),_NbsRoadmCommonStagingDropCaps_Type())
nbsRoadmCommonStagingDropCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommonStagingDropCaps.setStatus(_A)
_NbsRoadmCommonStagingCommit_Type=NbsTcStagingCommit
_NbsRoadmCommonStagingCommit_Object=MibTableColumn
nbsRoadmCommonStagingCommit=_NbsRoadmCommonStagingCommit_Object((1,3,6,1,4,1,629,235,10,2,1,20),_NbsRoadmCommonStagingCommit_Type())
nbsRoadmCommonStagingCommit.setMaxAccess(_R)
if mibBuilder.loadTexts:nbsRoadmCommonStagingCommit.setStatus(_A)
class _NbsRoadmCommonCommittedGridType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('reserved',2),('customized',3),(_P,4),(_Q,5)))
_NbsRoadmCommonCommittedGridType_Type.__name__=_F
_NbsRoadmCommonCommittedGridType_Object=MibTableColumn
nbsRoadmCommonCommittedGridType=_NbsRoadmCommonCommittedGridType_Object((1,3,6,1,4,1,629,235,10,2,1,30),_NbsRoadmCommonCommittedGridType_Type())
nbsRoadmCommonCommittedGridType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommonCommittedGridType.setStatus(_A)
class _NbsRoadmCommonCommittedChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_NbsRoadmCommonCommittedChannels_Type.__name__=_F
_NbsRoadmCommonCommittedChannels_Object=MibTableColumn
nbsRoadmCommonCommittedChannels=_NbsRoadmCommonCommittedChannels_Object((1,3,6,1,4,1,629,235,10,2,1,40),_NbsRoadmCommonCommittedChannels_Type())
nbsRoadmCommonCommittedChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommonCommittedChannels.setStatus(_A)
_NbsRoadmFlexgridGrp_ObjectIdentity=ObjectIdentity
nbsRoadmFlexgridGrp=_NbsRoadmFlexgridGrp_ObjectIdentity((1,3,6,1,4,1,629,235,20))
if mibBuilder.loadTexts:nbsRoadmFlexgridGrp.setStatus(_A)
_NbsRoadmFlexgridTableSize_Type=Unsigned32
_NbsRoadmFlexgridTableSize_Object=MibScalar
nbsRoadmFlexgridTableSize=_NbsRoadmFlexgridTableSize_Object((1,3,6,1,4,1,629,235,20,1),_NbsRoadmFlexgridTableSize_Type())
nbsRoadmFlexgridTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridTableSize.setStatus(_A)
_NbsRoadmFlexgridTable_Object=MibTable
nbsRoadmFlexgridTable=_NbsRoadmFlexgridTable_Object((1,3,6,1,4,1,629,235,20,2))
if mibBuilder.loadTexts:nbsRoadmFlexgridTable.setStatus(_A)
_NbsRoadmFlexgridEntry_Object=MibTableRow
nbsRoadmFlexgridEntry=_NbsRoadmFlexgridEntry_Object((1,3,6,1,4,1,629,235,20,2,1))
nbsRoadmFlexgridEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:nbsRoadmFlexgridEntry.setStatus(_A)
_NbsRoadmFlexgridIfIndex_Type=InterfaceIndex
_NbsRoadmFlexgridIfIndex_Object=MibTableColumn
nbsRoadmFlexgridIfIndex=_NbsRoadmFlexgridIfIndex_Object((1,3,6,1,4,1,629,235,20,2,1,1),_NbsRoadmFlexgridIfIndex_Type())
nbsRoadmFlexgridIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridIfIndex.setStatus(_A)
class _NbsRoadmFlexgridCenterlineMin_Type(NbsTcMHz):defaultValue=190100000
_NbsRoadmFlexgridCenterlineMin_Type.__name__=_D
_NbsRoadmFlexgridCenterlineMin_Object=MibTableColumn
nbsRoadmFlexgridCenterlineMin=_NbsRoadmFlexgridCenterlineMin_Object((1,3,6,1,4,1,629,235,20,2,1,21),_NbsRoadmFlexgridCenterlineMin_Type())
nbsRoadmFlexgridCenterlineMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridCenterlineMin.setStatus(_A)
class _NbsRoadmFlexgridCenterlineMax_Type(NbsTcMHz):defaultValue=197250000
_NbsRoadmFlexgridCenterlineMax_Type.__name__=_D
_NbsRoadmFlexgridCenterlineMax_Object=MibTableColumn
nbsRoadmFlexgridCenterlineMax=_NbsRoadmFlexgridCenterlineMax_Object((1,3,6,1,4,1,629,235,20,2,1,22),_NbsRoadmFlexgridCenterlineMax_Type())
nbsRoadmFlexgridCenterlineMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridCenterlineMax.setStatus(_A)
class _NbsRoadmFlexgridCenterlineIncr_Type(NbsTcMHz):defaultValue=12500
_NbsRoadmFlexgridCenterlineIncr_Type.__name__=_D
_NbsRoadmFlexgridCenterlineIncr_Object=MibTableColumn
nbsRoadmFlexgridCenterlineIncr=_NbsRoadmFlexgridCenterlineIncr_Object((1,3,6,1,4,1,629,235,20,2,1,23),_NbsRoadmFlexgridCenterlineIncr_Type())
nbsRoadmFlexgridCenterlineIncr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridCenterlineIncr.setStatus(_A)
class _NbsRoadmFlexgridBandwidthMin_Type(NbsTcMHz):defaultValue=25000
_NbsRoadmFlexgridBandwidthMin_Type.__name__=_D
_NbsRoadmFlexgridBandwidthMin_Object=MibTableColumn
nbsRoadmFlexgridBandwidthMin=_NbsRoadmFlexgridBandwidthMin_Object((1,3,6,1,4,1,629,235,20,2,1,31),_NbsRoadmFlexgridBandwidthMin_Type())
nbsRoadmFlexgridBandwidthMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridBandwidthMin.setStatus(_A)
class _NbsRoadmFlexgridBandwidthMax_Type(NbsTcMHz):defaultValue=25000
_NbsRoadmFlexgridBandwidthMax_Type.__name__=_D
_NbsRoadmFlexgridBandwidthMax_Object=MibTableColumn
nbsRoadmFlexgridBandwidthMax=_NbsRoadmFlexgridBandwidthMax_Object((1,3,6,1,4,1,629,235,20,2,1,32),_NbsRoadmFlexgridBandwidthMax_Type())
nbsRoadmFlexgridBandwidthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridBandwidthMax.setStatus(_A)
class _NbsRoadmFlexgridBandwidthIncr_Type(NbsTcMHz):defaultValue=25000
_NbsRoadmFlexgridBandwidthIncr_Type.__name__=_D
_NbsRoadmFlexgridBandwidthIncr_Object=MibTableColumn
nbsRoadmFlexgridBandwidthIncr=_NbsRoadmFlexgridBandwidthIncr_Object((1,3,6,1,4,1,629,235,20,2,1,33),_NbsRoadmFlexgridBandwidthIncr_Type())
nbsRoadmFlexgridBandwidthIncr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmFlexgridBandwidthIncr.setStatus(_A)
_NbsRoadmStagingGrp_ObjectIdentity=ObjectIdentity
nbsRoadmStagingGrp=_NbsRoadmStagingGrp_ObjectIdentity((1,3,6,1,4,1,629,235,30))
if mibBuilder.loadTexts:nbsRoadmStagingGrp.setStatus(_A)
_NbsRoadmStagingTableSize_Type=Unsigned32
_NbsRoadmStagingTableSize_Object=MibScalar
nbsRoadmStagingTableSize=_NbsRoadmStagingTableSize_Object((1,3,6,1,4,1,629,235,30,1),_NbsRoadmStagingTableSize_Type())
nbsRoadmStagingTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmStagingTableSize.setStatus(_A)
_NbsRoadmStagingTable_Object=MibTable
nbsRoadmStagingTable=_NbsRoadmStagingTable_Object((1,3,6,1,4,1,629,235,30,2))
if mibBuilder.loadTexts:nbsRoadmStagingTable.setStatus(_A)
_NbsRoadmStagingEntry_Object=MibTableRow
nbsRoadmStagingEntry=_NbsRoadmStagingEntry_Object((1,3,6,1,4,1,629,235,30,2,1))
nbsRoadmStagingEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:nbsRoadmStagingEntry.setStatus(_A)
_NbsRoadmStagingIfIndex_Type=InterfaceIndex
_NbsRoadmStagingIfIndex_Object=MibTableColumn
nbsRoadmStagingIfIndex=_NbsRoadmStagingIfIndex_Object((1,3,6,1,4,1,629,235,30,2,1,1),_NbsRoadmStagingIfIndex_Type())
nbsRoadmStagingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmStagingIfIndex.setStatus(_A)
_NbsRoadmStagingCenterline_Type=NbsTcMHz
_NbsRoadmStagingCenterline_Object=MibTableColumn
nbsRoadmStagingCenterline=_NbsRoadmStagingCenterline_Object((1,3,6,1,4,1,629,235,30,2,1,2),_NbsRoadmStagingCenterline_Type())
nbsRoadmStagingCenterline.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmStagingCenterline.setStatus(_A)
class _NbsRoadmStagingBandwidth_Type(NbsTcMHz):defaultValue=100000
_NbsRoadmStagingBandwidth_Type.__name__=_D
_NbsRoadmStagingBandwidth_Object=MibTableColumn
nbsRoadmStagingBandwidth=_NbsRoadmStagingBandwidth_Object((1,3,6,1,4,1,629,235,30,2,1,10),_NbsRoadmStagingBandwidth_Type())
nbsRoadmStagingBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingBandwidth.setStatus(_A)
class _NbsRoadmStagingChannelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsRoadmStagingChannelName_Type.__name__=_G
_NbsRoadmStagingChannelName_Object=MibTableColumn
nbsRoadmStagingChannelName=_NbsRoadmStagingChannelName_Object((1,3,6,1,4,1,629,235,30,2,1,30),_NbsRoadmStagingChannelName_Type())
nbsRoadmStagingChannelName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingChannelName.setStatus(_A)
_NbsRoadmStagingAddPort_Type=InterfaceIndex
_NbsRoadmStagingAddPort_Object=MibTableColumn
nbsRoadmStagingAddPort=_NbsRoadmStagingAddPort_Object((1,3,6,1,4,1,629,235,30,2,1,41),_NbsRoadmStagingAddPort_Type())
nbsRoadmStagingAddPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingAddPort.setStatus(_A)
_NbsRoadmStagingDropPort_Type=InterfaceIndex
_NbsRoadmStagingDropPort_Object=MibTableColumn
nbsRoadmStagingDropPort=_NbsRoadmStagingDropPort_Object((1,3,6,1,4,1,629,235,30,2,1,42),_NbsRoadmStagingDropPort_Type())
nbsRoadmStagingDropPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingDropPort.setStatus(_A)
_NbsRoadmStagingSecondaryPort_Type=InterfaceIndex
_NbsRoadmStagingSecondaryPort_Object=MibTableColumn
nbsRoadmStagingSecondaryPort=_NbsRoadmStagingSecondaryPort_Object((1,3,6,1,4,1,629,235,30,2,1,43),_NbsRoadmStagingSecondaryPort_Type())
nbsRoadmStagingSecondaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingSecondaryPort.setStatus(_A)
class _NbsRoadmStagingSecondAttenu_Type(NbsTcMilliDb):defaultValue=-1000000
_NbsRoadmStagingSecondAttenu_Type.__name__=_H
_NbsRoadmStagingSecondAttenu_Object=MibTableColumn
nbsRoadmStagingSecondAttenu=_NbsRoadmStagingSecondAttenu_Object((1,3,6,1,4,1,629,235,30,2,1,44),_NbsRoadmStagingSecondAttenu_Type())
nbsRoadmStagingSecondAttenu.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingSecondAttenu.setStatus(_A)
class _NbsRoadmStagingAddAttenu_Type(NbsTcMilliDb):defaultValue=-1000000
_NbsRoadmStagingAddAttenu_Type.__name__=_H
_NbsRoadmStagingAddAttenu_Object=MibTableColumn
nbsRoadmStagingAddAttenu=_NbsRoadmStagingAddAttenu_Object((1,3,6,1,4,1,629,235,30,2,1,51),_NbsRoadmStagingAddAttenu_Type())
nbsRoadmStagingAddAttenu.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingAddAttenu.setStatus(_A)
class _NbsRoadmStagingDropAttenu_Type(NbsTcMilliDb):defaultValue=-1000000
_NbsRoadmStagingDropAttenu_Type.__name__=_H
_NbsRoadmStagingDropAttenu_Object=MibTableColumn
nbsRoadmStagingDropAttenu=_NbsRoadmStagingDropAttenu_Object((1,3,6,1,4,1,629,235,30,2,1,52),_NbsRoadmStagingDropAttenu_Type())
nbsRoadmStagingDropAttenu.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingDropAttenu.setStatus(_A)
class _NbsRoadmStagingItuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsRoadmStagingItuName_Type.__name__=_G
_NbsRoadmStagingItuName_Object=MibTableColumn
nbsRoadmStagingItuName=_NbsRoadmStagingItuName_Object((1,3,6,1,4,1,629,235,30,2,1,53),_NbsRoadmStagingItuName_Type())
nbsRoadmStagingItuName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmStagingItuName.setStatus(_A)
class _NbsRoadmStagingRowStatus_Type(RowStatus):defaultValue=1
_NbsRoadmStagingRowStatus_Type.__name__=_O
_NbsRoadmStagingRowStatus_Object=MibTableColumn
nbsRoadmStagingRowStatus=_NbsRoadmStagingRowStatus_Object((1,3,6,1,4,1,629,235,30,2,1,99),_NbsRoadmStagingRowStatus_Type())
nbsRoadmStagingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRoadmStagingRowStatus.setStatus(_A)
_NbsRoadmCommittedGrp_ObjectIdentity=ObjectIdentity
nbsRoadmCommittedGrp=_NbsRoadmCommittedGrp_ObjectIdentity((1,3,6,1,4,1,629,235,31))
if mibBuilder.loadTexts:nbsRoadmCommittedGrp.setStatus(_A)
_NbsRoadmCommittedTableSize_Type=Unsigned32
_NbsRoadmCommittedTableSize_Object=MibScalar
nbsRoadmCommittedTableSize=_NbsRoadmCommittedTableSize_Object((1,3,6,1,4,1,629,235,31,1),_NbsRoadmCommittedTableSize_Type())
nbsRoadmCommittedTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedTableSize.setStatus(_A)
_NbsRoadmCommittedTable_Object=MibTable
nbsRoadmCommittedTable=_NbsRoadmCommittedTable_Object((1,3,6,1,4,1,629,235,31,2))
if mibBuilder.loadTexts:nbsRoadmCommittedTable.setStatus(_A)
_NbsRoadmCommittedEntry_Object=MibTableRow
nbsRoadmCommittedEntry=_NbsRoadmCommittedEntry_Object((1,3,6,1,4,1,629,235,31,2,1))
nbsRoadmCommittedEntry.setIndexNames((0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:nbsRoadmCommittedEntry.setStatus(_A)
_NbsRoadmCommittedIfIndex_Type=InterfaceIndex
_NbsRoadmCommittedIfIndex_Object=MibTableColumn
nbsRoadmCommittedIfIndex=_NbsRoadmCommittedIfIndex_Object((1,3,6,1,4,1,629,235,31,2,1,1),_NbsRoadmCommittedIfIndex_Type())
nbsRoadmCommittedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedIfIndex.setStatus(_A)
_NbsRoadmCommittedCenterline_Type=NbsTcMHz
_NbsRoadmCommittedCenterline_Object=MibTableColumn
nbsRoadmCommittedCenterline=_NbsRoadmCommittedCenterline_Object((1,3,6,1,4,1,629,235,31,2,1,2),_NbsRoadmCommittedCenterline_Type())
nbsRoadmCommittedCenterline.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedCenterline.setStatus(_A)
class _NbsRoadmCommittedBandwidth_Type(NbsTcMHz):defaultValue=100000
_NbsRoadmCommittedBandwidth_Type.__name__=_D
_NbsRoadmCommittedBandwidth_Object=MibTableColumn
nbsRoadmCommittedBandwidth=_NbsRoadmCommittedBandwidth_Object((1,3,6,1,4,1,629,235,31,2,1,10),_NbsRoadmCommittedBandwidth_Type())
nbsRoadmCommittedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedBandwidth.setStatus(_A)
class _NbsRoadmCommittedChannelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsRoadmCommittedChannelName_Type.__name__=_G
_NbsRoadmCommittedChannelName_Object=MibTableColumn
nbsRoadmCommittedChannelName=_NbsRoadmCommittedChannelName_Object((1,3,6,1,4,1,629,235,31,2,1,30),_NbsRoadmCommittedChannelName_Type())
nbsRoadmCommittedChannelName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedChannelName.setStatus(_A)
_NbsRoadmCommittedAddPort_Type=InterfaceIndex
_NbsRoadmCommittedAddPort_Object=MibTableColumn
nbsRoadmCommittedAddPort=_NbsRoadmCommittedAddPort_Object((1,3,6,1,4,1,629,235,31,2,1,41),_NbsRoadmCommittedAddPort_Type())
nbsRoadmCommittedAddPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedAddPort.setStatus(_A)
_NbsRoadmCommittedDropPort_Type=InterfaceIndex
_NbsRoadmCommittedDropPort_Object=MibTableColumn
nbsRoadmCommittedDropPort=_NbsRoadmCommittedDropPort_Object((1,3,6,1,4,1,629,235,31,2,1,42),_NbsRoadmCommittedDropPort_Type())
nbsRoadmCommittedDropPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedDropPort.setStatus(_A)
_NbsRoadmCommittedSecondaryPort_Type=InterfaceIndex
_NbsRoadmCommittedSecondaryPort_Object=MibTableColumn
nbsRoadmCommittedSecondaryPort=_NbsRoadmCommittedSecondaryPort_Object((1,3,6,1,4,1,629,235,31,2,1,43),_NbsRoadmCommittedSecondaryPort_Type())
nbsRoadmCommittedSecondaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedSecondaryPort.setStatus(_A)
_NbsRoadmCommittedSecondAttenu_Type=NbsTcMilliDb
_NbsRoadmCommittedSecondAttenu_Object=MibTableColumn
nbsRoadmCommittedSecondAttenu=_NbsRoadmCommittedSecondAttenu_Object((1,3,6,1,4,1,629,235,31,2,1,44),_NbsRoadmCommittedSecondAttenu_Type())
nbsRoadmCommittedSecondAttenu.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedSecondAttenu.setStatus(_A)
_NbsRoadmCommittedAddAttenu_Type=NbsTcMilliDb
_NbsRoadmCommittedAddAttenu_Object=MibTableColumn
nbsRoadmCommittedAddAttenu=_NbsRoadmCommittedAddAttenu_Object((1,3,6,1,4,1,629,235,31,2,1,51),_NbsRoadmCommittedAddAttenu_Type())
nbsRoadmCommittedAddAttenu.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedAddAttenu.setStatus(_A)
_NbsRoadmCommittedDropAttenu_Type=NbsTcMilliDb
_NbsRoadmCommittedDropAttenu_Object=MibTableColumn
nbsRoadmCommittedDropAttenu=_NbsRoadmCommittedDropAttenu_Object((1,3,6,1,4,1,629,235,31,2,1,52),_NbsRoadmCommittedDropAttenu_Type())
nbsRoadmCommittedDropAttenu.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedDropAttenu.setStatus(_A)
class _NbsRoadmCommittedItuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsRoadmCommittedItuName_Type.__name__=_G
_NbsRoadmCommittedItuName_Object=MibTableColumn
nbsRoadmCommittedItuName=_NbsRoadmCommittedItuName_Object((1,3,6,1,4,1,629,235,31,2,1,60),_NbsRoadmCommittedItuName_Type())
nbsRoadmCommittedItuName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmCommittedItuName.setStatus(_A)
_NbsRoadmRedundantGrp_ObjectIdentity=ObjectIdentity
nbsRoadmRedundantGrp=_NbsRoadmRedundantGrp_ObjectIdentity((1,3,6,1,4,1,629,235,32))
if mibBuilder.loadTexts:nbsRoadmRedundantGrp.setStatus(_A)
_NbsRoadmRedundantTableSize_Type=Unsigned32
_NbsRoadmRedundantTableSize_Object=MibScalar
nbsRoadmRedundantTableSize=_NbsRoadmRedundantTableSize_Object((1,3,6,1,4,1,629,235,32,1),_NbsRoadmRedundantTableSize_Type())
nbsRoadmRedundantTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantTableSize.setStatus(_A)
_NbsRoadmRedundantTable_Object=MibTable
nbsRoadmRedundantTable=_NbsRoadmRedundantTable_Object((1,3,6,1,4,1,629,235,32,2))
if mibBuilder.loadTexts:nbsRoadmRedundantTable.setStatus(_A)
_NbsRoadmRedundantEntry_Object=MibTableRow
nbsRoadmRedundantEntry=_NbsRoadmRedundantEntry_Object((1,3,6,1,4,1,629,235,32,2,1))
nbsRoadmRedundantEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:nbsRoadmRedundantEntry.setStatus(_A)
_NbsRoadmRedundantIfIndex_Type=InterfaceIndex
_NbsRoadmRedundantIfIndex_Object=MibTableColumn
nbsRoadmRedundantIfIndex=_NbsRoadmRedundantIfIndex_Object((1,3,6,1,4,1,629,235,32,2,1,1),_NbsRoadmRedundantIfIndex_Type())
nbsRoadmRedundantIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantIfIndex.setStatus(_A)
_NbsRoadmRedundantCenterline_Type=NbsTcMHz
_NbsRoadmRedundantCenterline_Object=MibTableColumn
nbsRoadmRedundantCenterline=_NbsRoadmRedundantCenterline_Object((1,3,6,1,4,1,629,235,32,2,1,2),_NbsRoadmRedundantCenterline_Type())
nbsRoadmRedundantCenterline.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantCenterline.setStatus(_A)
class _NbsRoadmRedundantItuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsRoadmRedundantItuName_Type.__name__=_G
_NbsRoadmRedundantItuName_Object=MibTableColumn
nbsRoadmRedundantItuName=_NbsRoadmRedundantItuName_Object((1,3,6,1,4,1,629,235,32,2,1,10),_NbsRoadmRedundantItuName_Type())
nbsRoadmRedundantItuName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantItuName.setStatus(_A)
class _NbsRoadmRedundantChannelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsRoadmRedundantChannelName_Type.__name__=_G
_NbsRoadmRedundantChannelName_Object=MibTableColumn
nbsRoadmRedundantChannelName=_NbsRoadmRedundantChannelName_Object((1,3,6,1,4,1,629,235,32,2,1,20),_NbsRoadmRedundantChannelName_Type())
nbsRoadmRedundantChannelName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantChannelName.setStatus(_A)
_NbsRoadmRedundantMapPort_Type=InterfaceIndex
_NbsRoadmRedundantMapPort_Object=MibTableColumn
nbsRoadmRedundantMapPort=_NbsRoadmRedundantMapPort_Object((1,3,6,1,4,1,629,235,32,2,1,29),_NbsRoadmRedundantMapPort_Type())
nbsRoadmRedundantMapPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantMapPort.setStatus(_A)
_NbsRoadmRedundantSecondaryPort_Type=InterfaceIndex
_NbsRoadmRedundantSecondaryPort_Object=MibTableColumn
nbsRoadmRedundantSecondaryPort=_NbsRoadmRedundantSecondaryPort_Object((1,3,6,1,4,1,629,235,32,2,1,30),_NbsRoadmRedundantSecondaryPort_Type())
nbsRoadmRedundantSecondaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantSecondaryPort.setStatus(_A)
_NbsRoadmRedundantCurPort_Type=InterfaceIndex
_NbsRoadmRedundantCurPort_Object=MibTableColumn
nbsRoadmRedundantCurPort=_NbsRoadmRedundantCurPort_Object((1,3,6,1,4,1,629,235,32,2,1,40),_NbsRoadmRedundantCurPort_Type())
nbsRoadmRedundantCurPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantCurPort.setStatus(_A)
_NbsRoadmRedundantCurAttenu_Type=NbsTcMilliDb
_NbsRoadmRedundantCurAttenu_Object=MibTableColumn
nbsRoadmRedundantCurAttenu=_NbsRoadmRedundantCurAttenu_Object((1,3,6,1,4,1,629,235,32,2,1,41),_NbsRoadmRedundantCurAttenu_Type())
nbsRoadmRedundantCurAttenu.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantCurAttenu.setStatus(_A)
class _NbsRoadmRedundantCurState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switching',1),('active',2)))
_NbsRoadmRedundantCurState_Type.__name__=_F
_NbsRoadmRedundantCurState_Object=MibTableColumn
nbsRoadmRedundantCurState=_NbsRoadmRedundantCurState_Object((1,3,6,1,4,1,629,235,32,2,1,50),_NbsRoadmRedundantCurState_Type())
nbsRoadmRedundantCurState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsRoadmRedundantCurState.setStatus(_A)
_NbsRoadmTraps_ObjectIdentity=ObjectIdentity
nbsRoadmTraps=_NbsRoadmTraps_ObjectIdentity((1,3,6,1,4,1,629,235,100))
if mibBuilder.loadTexts:nbsRoadmTraps.setStatus(_A)
_NbsRoadmEvent_ObjectIdentity=ObjectIdentity
nbsRoadmEvent=_NbsRoadmEvent_ObjectIdentity((1,3,6,1,4,1,629,235,100,0))
if mibBuilder.loadTexts:nbsRoadmEvent.setStatus(_A)
nbsRoadmEventStageAreaCommitted=NotificationType((1,3,6,1,4,1,629,235,100,0,10))
nbsRoadmEventStageAreaCommitted.setObjects(*((_C,_J),(_M,_N),(_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:nbsRoadmEventStageAreaCommitted.setStatus(_A)
nbsRoadmEventRedundancyTriggered=NotificationType((1,3,6,1,4,1,629,235,100,0,20))
nbsRoadmEventRedundancyTriggered.setObjects(*((_C,_K),(_C,_L)))
if mibBuilder.loadTexts:nbsRoadmEventRedundancyTriggered.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nbsRoadmMib':nbsRoadmMib,'nbsRoadmCommonGrp':nbsRoadmCommonGrp,'nbsRoadmCommonTableSize':nbsRoadmCommonTableSize,'nbsRoadmCommonTable':nbsRoadmCommonTable,'nbsRoadmCommonEntry':nbsRoadmCommonEntry,_J:nbsRoadmCommonIfIndex,'nbsRoadmCommonStagingQuickCfg':nbsRoadmCommonStagingQuickCfg,'nbsRoadmCommonStagingAddCaps':nbsRoadmCommonStagingAddCaps,'nbsRoadmCommonStagingDropCaps':nbsRoadmCommonStagingDropCaps,'nbsRoadmCommonStagingCommit':nbsRoadmCommonStagingCommit,_Y:nbsRoadmCommonCommittedGridType,_Z:nbsRoadmCommonCommittedChannels,'nbsRoadmFlexgridGrp':nbsRoadmFlexgridGrp,'nbsRoadmFlexgridTableSize':nbsRoadmFlexgridTableSize,'nbsRoadmFlexgridTable':nbsRoadmFlexgridTable,'nbsRoadmFlexgridEntry':nbsRoadmFlexgridEntry,_T:nbsRoadmFlexgridIfIndex,'nbsRoadmFlexgridCenterlineMin':nbsRoadmFlexgridCenterlineMin,'nbsRoadmFlexgridCenterlineMax':nbsRoadmFlexgridCenterlineMax,'nbsRoadmFlexgridCenterlineIncr':nbsRoadmFlexgridCenterlineIncr,'nbsRoadmFlexgridBandwidthMin':nbsRoadmFlexgridBandwidthMin,'nbsRoadmFlexgridBandwidthMax':nbsRoadmFlexgridBandwidthMax,'nbsRoadmFlexgridBandwidthIncr':nbsRoadmFlexgridBandwidthIncr,'nbsRoadmStagingGrp':nbsRoadmStagingGrp,'nbsRoadmStagingTableSize':nbsRoadmStagingTableSize,'nbsRoadmStagingTable':nbsRoadmStagingTable,'nbsRoadmStagingEntry':nbsRoadmStagingEntry,_U:nbsRoadmStagingIfIndex,_V:nbsRoadmStagingCenterline,'nbsRoadmStagingBandwidth':nbsRoadmStagingBandwidth,'nbsRoadmStagingChannelName':nbsRoadmStagingChannelName,'nbsRoadmStagingAddPort':nbsRoadmStagingAddPort,'nbsRoadmStagingDropPort':nbsRoadmStagingDropPort,'nbsRoadmStagingSecondaryPort':nbsRoadmStagingSecondaryPort,'nbsRoadmStagingSecondAttenu':nbsRoadmStagingSecondAttenu,'nbsRoadmStagingAddAttenu':nbsRoadmStagingAddAttenu,'nbsRoadmStagingDropAttenu':nbsRoadmStagingDropAttenu,'nbsRoadmStagingItuName':nbsRoadmStagingItuName,'nbsRoadmStagingRowStatus':nbsRoadmStagingRowStatus,'nbsRoadmCommittedGrp':nbsRoadmCommittedGrp,'nbsRoadmCommittedTableSize':nbsRoadmCommittedTableSize,'nbsRoadmCommittedTable':nbsRoadmCommittedTable,'nbsRoadmCommittedEntry':nbsRoadmCommittedEntry,_W:nbsRoadmCommittedIfIndex,_X:nbsRoadmCommittedCenterline,'nbsRoadmCommittedBandwidth':nbsRoadmCommittedBandwidth,'nbsRoadmCommittedChannelName':nbsRoadmCommittedChannelName,'nbsRoadmCommittedAddPort':nbsRoadmCommittedAddPort,'nbsRoadmCommittedDropPort':nbsRoadmCommittedDropPort,'nbsRoadmCommittedSecondaryPort':nbsRoadmCommittedSecondaryPort,'nbsRoadmCommittedSecondAttenu':nbsRoadmCommittedSecondAttenu,'nbsRoadmCommittedAddAttenu':nbsRoadmCommittedAddAttenu,'nbsRoadmCommittedDropAttenu':nbsRoadmCommittedDropAttenu,'nbsRoadmCommittedItuName':nbsRoadmCommittedItuName,'nbsRoadmRedundantGrp':nbsRoadmRedundantGrp,'nbsRoadmRedundantTableSize':nbsRoadmRedundantTableSize,'nbsRoadmRedundantTable':nbsRoadmRedundantTable,'nbsRoadmRedundantEntry':nbsRoadmRedundantEntry,_K:nbsRoadmRedundantIfIndex,_L:nbsRoadmRedundantCenterline,'nbsRoadmRedundantItuName':nbsRoadmRedundantItuName,'nbsRoadmRedundantChannelName':nbsRoadmRedundantChannelName,'nbsRoadmRedundantMapPort':nbsRoadmRedundantMapPort,'nbsRoadmRedundantSecondaryPort':nbsRoadmRedundantSecondaryPort,'nbsRoadmRedundantCurPort':nbsRoadmRedundantCurPort,'nbsRoadmRedundantCurAttenu':nbsRoadmRedundantCurAttenu,'nbsRoadmRedundantCurState':nbsRoadmRedundantCurState,'nbsRoadmTraps':nbsRoadmTraps,'nbsRoadmEvent':nbsRoadmEvent,'nbsRoadmEventStageAreaCommitted':nbsRoadmEventStageAreaCommitted,'nbsRoadmEventRedundancyTriggered':nbsRoadmEventRedundancyTriggered})