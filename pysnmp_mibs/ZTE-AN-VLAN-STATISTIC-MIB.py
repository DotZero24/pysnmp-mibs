_P='zxAnCVlanId'
_O='zxAnSVlanId'
_N='zxAnUserVlanId'
_M='zxAnUserVlanPortIfIndex'
_L='zxAnSwVlanId'
_K='read-write'
_J='zxAnEnVlanId'
_I='DisplayString'
_H='read-create'
_G='Integer32'
_F='not-accessible'
_E='ZTE-AN-VLAN-STATISTIC-MIB'
_D='bytes'
_C='kbps'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention','TruthValue')
VlanId,ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','VlanId','ZxAnIfindex','zxAn')
zxAnVlanStatisticMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,191))
_ZxAnVlanPerfEnableTable_Object=MibTable
zxAnVlanPerfEnableTable=_ZxAnVlanPerfEnableTable_Object((1,3,6,1,4,1,3902,1015,191,1))
if mibBuilder.loadTexts:zxAnVlanPerfEnableTable.setStatus(_A)
_ZxAnVlanPerfEnableEntry_Object=MibTableRow
zxAnVlanPerfEnableEntry=_ZxAnVlanPerfEnableEntry_Object((1,3,6,1,4,1,3902,1015,191,1,1))
zxAnVlanPerfEnableEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:zxAnVlanPerfEnableEntry.setStatus(_A)
_ZxAnEnVlanId_Type=VlanId
_ZxAnEnVlanId_Object=MibTableColumn
zxAnEnVlanId=_ZxAnEnVlanId_Object((1,3,6,1,4,1,3902,1015,191,1,1,1),_ZxAnEnVlanId_Type())
zxAnEnVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEnVlanId.setStatus(_A)
class _ZxVlanPerfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxVlanPerfEnable_Type.__name__=_G
_ZxVlanPerfEnable_Object=MibTableColumn
zxVlanPerfEnable=_ZxVlanPerfEnable_Object((1,3,6,1,4,1,3902,1015,191,1,1,2),_ZxVlanPerfEnable_Type())
zxVlanPerfEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:zxVlanPerfEnable.setStatus(_A)
class _ZxVlanIDAllEnable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZxVlanIDAllEnable_Type.__name__=_I
_ZxVlanIDAllEnable_Object=MibTableColumn
zxVlanIDAllEnable=_ZxVlanIDAllEnable_Object((1,3,6,1,4,1,3902,1015,191,1,1,3),_ZxVlanIDAllEnable_Type())
zxVlanIDAllEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:zxVlanIDAllEnable.setStatus(_A)
_ZxAnSwVlanPerfTable_Object=MibTable
zxAnSwVlanPerfTable=_ZxAnSwVlanPerfTable_Object((1,3,6,1,4,1,3902,1015,191,2))
if mibBuilder.loadTexts:zxAnSwVlanPerfTable.setStatus(_A)
_ZxAnSwVlanPerfEntry_Object=MibTableRow
zxAnSwVlanPerfEntry=_ZxAnSwVlanPerfEntry_Object((1,3,6,1,4,1,3902,1015,191,2,1))
zxAnSwVlanPerfEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:zxAnSwVlanPerfEntry.setStatus(_A)
_ZxAnSwVlanId_Type=VlanId
_ZxAnSwVlanId_Object=MibTableColumn
zxAnSwVlanId=_ZxAnSwVlanId_Object((1,3,6,1,4,1,3902,1015,191,2,1,1),_ZxAnSwVlanId_Type())
zxAnSwVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSwVlanId.setStatus(_A)
_ZxAnSwVlanInOctets_Type=Counter64
_ZxAnSwVlanInOctets_Object=MibTableColumn
zxAnSwVlanInOctets=_ZxAnSwVlanInOctets_Object((1,3,6,1,4,1,3902,1015,191,2,1,2),_ZxAnSwVlanInOctets_Type())
zxAnSwVlanInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInOctets.setStatus(_A)
_ZxAnSwVlanOutOctets_Type=Counter64
_ZxAnSwVlanOutOctets_Object=MibTableColumn
zxAnSwVlanOutOctets=_ZxAnSwVlanOutOctets_Object((1,3,6,1,4,1,3902,1015,191,2,1,3),_ZxAnSwVlanOutOctets_Type())
zxAnSwVlanOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutOctets.setStatus(_A)
_ZxAnSwVlanInPkts_Type=Counter64
_ZxAnSwVlanInPkts_Object=MibTableColumn
zxAnSwVlanInPkts=_ZxAnSwVlanInPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,4),_ZxAnSwVlanInPkts_Type())
zxAnSwVlanInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInPkts.setStatus(_A)
_ZxAnSwVlanOutPkts_Type=Counter64
_ZxAnSwVlanOutPkts_Object=MibTableColumn
zxAnSwVlanOutPkts=_ZxAnSwVlanOutPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,5),_ZxAnSwVlanOutPkts_Type())
zxAnSwVlanOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutPkts.setStatus(_A)
_ZxAnSwVlanInBandwidth_Type=Integer32
_ZxAnSwVlanInBandwidth_Object=MibTableColumn
zxAnSwVlanInBandwidth=_ZxAnSwVlanInBandwidth_Object((1,3,6,1,4,1,3902,1015,191,2,1,6),_ZxAnSwVlanInBandwidth_Type())
zxAnSwVlanInBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInBandwidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnSwVlanInBandwidth.setUnits(_C)
_ZxAnSwVlanOutBandwidth_Type=Integer32
_ZxAnSwVlanOutBandwidth_Object=MibTableColumn
zxAnSwVlanOutBandwidth=_ZxAnSwVlanOutBandwidth_Object((1,3,6,1,4,1,3902,1015,191,2,1,7),_ZxAnSwVlanOutBandwidth_Type())
zxAnSwVlanOutBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutBandwidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnSwVlanOutBandwidth.setUnits(_C)
_ZxAnSwVlanInBandwidthUtility_Type=Integer32
_ZxAnSwVlanInBandwidthUtility_Object=MibTableColumn
zxAnSwVlanInBandwidthUtility=_ZxAnSwVlanInBandwidthUtility_Object((1,3,6,1,4,1,3902,1015,191,2,1,8),_ZxAnSwVlanInBandwidthUtility_Type())
zxAnSwVlanInBandwidthUtility.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInBandwidthUtility.setStatus(_A)
if mibBuilder.loadTexts:zxAnSwVlanInBandwidthUtility.setUnits('%')
_ZxAnSwVlanOutBandwidthUtility_Type=Integer32
_ZxAnSwVlanOutBandwidthUtility_Object=MibTableColumn
zxAnSwVlanOutBandwidthUtility=_ZxAnSwVlanOutBandwidthUtility_Object((1,3,6,1,4,1,3902,1015,191,2,1,9),_ZxAnSwVlanOutBandwidthUtility_Type())
zxAnSwVlanOutBandwidthUtility.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutBandwidthUtility.setStatus(_A)
if mibBuilder.loadTexts:zxAnSwVlanOutBandwidthUtility.setUnits('%')
_ZxAnSwVlanInCurrOctetRate_Type=Gauge32
_ZxAnSwVlanInCurrOctetRate_Object=MibTableColumn
zxAnSwVlanInCurrOctetRate=_ZxAnSwVlanInCurrOctetRate_Object((1,3,6,1,4,1,3902,1015,191,2,1,10),_ZxAnSwVlanInCurrOctetRate_Type())
zxAnSwVlanInCurrOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInCurrOctetRate.setStatus(_A)
_ZxAnSwVlanOutCurrOctetRate_Type=Gauge32
_ZxAnSwVlanOutCurrOctetRate_Object=MibTableColumn
zxAnSwVlanOutCurrOctetRate=_ZxAnSwVlanOutCurrOctetRate_Object((1,3,6,1,4,1,3902,1015,191,2,1,11),_ZxAnSwVlanOutCurrOctetRate_Type())
zxAnSwVlanOutCurrOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutCurrOctetRate.setStatus(_A)
_ZxAnSwVlanInCurrPktRate_Type=Gauge32
_ZxAnSwVlanInCurrPktRate_Object=MibTableColumn
zxAnSwVlanInCurrPktRate=_ZxAnSwVlanInCurrPktRate_Object((1,3,6,1,4,1,3902,1015,191,2,1,12),_ZxAnSwVlanInCurrPktRate_Type())
zxAnSwVlanInCurrPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInCurrPktRate.setStatus(_A)
_ZxAnSwVlanOutCurrPktRate_Type=Gauge32
_ZxAnSwVlanOutCurrPktRate_Object=MibTableColumn
zxAnSwVlanOutCurrPktRate=_ZxAnSwVlanOutCurrPktRate_Object((1,3,6,1,4,1,3902,1015,191,2,1,13),_ZxAnSwVlanOutCurrPktRate_Type())
zxAnSwVlanOutCurrPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutCurrPktRate.setStatus(_A)
_ZxAnSwVlanInUcastPkts_Type=Counter64
_ZxAnSwVlanInUcastPkts_Object=MibTableColumn
zxAnSwVlanInUcastPkts=_ZxAnSwVlanInUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,14),_ZxAnSwVlanInUcastPkts_Type())
zxAnSwVlanInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInUcastPkts.setStatus(_A)
_ZxAnSwVlanOutUcastPkts_Type=Counter64
_ZxAnSwVlanOutUcastPkts_Object=MibTableColumn
zxAnSwVlanOutUcastPkts=_ZxAnSwVlanOutUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,15),_ZxAnSwVlanOutUcastPkts_Type())
zxAnSwVlanOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutUcastPkts.setStatus(_A)
_ZxAnSwVlanInMulticastPkts_Type=Counter64
_ZxAnSwVlanInMulticastPkts_Object=MibTableColumn
zxAnSwVlanInMulticastPkts=_ZxAnSwVlanInMulticastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,16),_ZxAnSwVlanInMulticastPkts_Type())
zxAnSwVlanInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInMulticastPkts.setStatus(_A)
_ZxAnSwVlanOutMulticastPkts_Type=Counter64
_ZxAnSwVlanOutMulticastPkts_Object=MibTableColumn
zxAnSwVlanOutMulticastPkts=_ZxAnSwVlanOutMulticastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,17),_ZxAnSwVlanOutMulticastPkts_Type())
zxAnSwVlanOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutMulticastPkts.setStatus(_A)
_ZxAnSwVlanInNUcastPkts_Type=Counter64
_ZxAnSwVlanInNUcastPkts_Object=MibTableColumn
zxAnSwVlanInNUcastPkts=_ZxAnSwVlanInNUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,18),_ZxAnSwVlanInNUcastPkts_Type())
zxAnSwVlanInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInNUcastPkts.setStatus(_A)
_ZxAnSwVlanOutNUcastPkts_Type=Counter64
_ZxAnSwVlanOutNUcastPkts_Object=MibTableColumn
zxAnSwVlanOutNUcastPkts=_ZxAnSwVlanOutNUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,19),_ZxAnSwVlanOutNUcastPkts_Type())
zxAnSwVlanOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutNUcastPkts.setStatus(_A)
_ZxAnSwVlanInBroadcastPkts_Type=Counter64
_ZxAnSwVlanInBroadcastPkts_Object=MibTableColumn
zxAnSwVlanInBroadcastPkts=_ZxAnSwVlanInBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,20),_ZxAnSwVlanInBroadcastPkts_Type())
zxAnSwVlanInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInBroadcastPkts.setStatus(_A)
_ZxAnSwVlanOutBroadcastPkts_Type=Counter64
_ZxAnSwVlanOutBroadcastPkts_Object=MibTableColumn
zxAnSwVlanOutBroadcastPkts=_ZxAnSwVlanOutBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,21),_ZxAnSwVlanOutBroadcastPkts_Type())
zxAnSwVlanOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutBroadcastPkts.setStatus(_A)
_ZxAnSwVlanInDiscards_Type=Counter64
_ZxAnSwVlanInDiscards_Object=MibTableColumn
zxAnSwVlanInDiscards=_ZxAnSwVlanInDiscards_Object((1,3,6,1,4,1,3902,1015,191,2,1,22),_ZxAnSwVlanInDiscards_Type())
zxAnSwVlanInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInDiscards.setStatus(_A)
_ZxAnSwVlanOutDiscards_Type=Counter64
_ZxAnSwVlanOutDiscards_Object=MibTableColumn
zxAnSwVlanOutDiscards=_ZxAnSwVlanOutDiscards_Object((1,3,6,1,4,1,3902,1015,191,2,1,23),_ZxAnSwVlanOutDiscards_Type())
zxAnSwVlanOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutDiscards.setStatus(_A)
_ZxAnSwVlanInUndersizePkts_Type=Counter64
_ZxAnSwVlanInUndersizePkts_Object=MibTableColumn
zxAnSwVlanInUndersizePkts=_ZxAnSwVlanInUndersizePkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,24),_ZxAnSwVlanInUndersizePkts_Type())
zxAnSwVlanInUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInUndersizePkts.setStatus(_A)
_ZxAnSwVlanOutUndersizePkts_Type=Counter64
_ZxAnSwVlanOutUndersizePkts_Object=MibTableColumn
zxAnSwVlanOutUndersizePkts=_ZxAnSwVlanOutUndersizePkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,25),_ZxAnSwVlanOutUndersizePkts_Type())
zxAnSwVlanOutUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutUndersizePkts.setStatus(_A)
_ZxAnSwVlanInOversizePkts_Type=Counter64
_ZxAnSwVlanInOversizePkts_Object=MibTableColumn
zxAnSwVlanInOversizePkts=_ZxAnSwVlanInOversizePkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,26),_ZxAnSwVlanInOversizePkts_Type())
zxAnSwVlanInOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInOversizePkts.setStatus(_A)
_ZxAnSwVlanOutOversizePkts_Type=Counter64
_ZxAnSwVlanOutOversizePkts_Object=MibTableColumn
zxAnSwVlanOutOversizePkts=_ZxAnSwVlanOutOversizePkts_Object((1,3,6,1,4,1,3902,1015,191,2,1,27),_ZxAnSwVlanOutOversizePkts_Type())
zxAnSwVlanOutOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutOversizePkts.setStatus(_A)
_ZxAnSwVlanInCRCAlignErrors_Type=Counter64
_ZxAnSwVlanInCRCAlignErrors_Object=MibTableColumn
zxAnSwVlanInCRCAlignErrors=_ZxAnSwVlanInCRCAlignErrors_Object((1,3,6,1,4,1,3902,1015,191,2,1,28),_ZxAnSwVlanInCRCAlignErrors_Type())
zxAnSwVlanInCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInCRCAlignErrors.setStatus(_A)
_ZxAnSwVlanOutCRCAlignErrors_Type=Counter64
_ZxAnSwVlanOutCRCAlignErrors_Object=MibTableColumn
zxAnSwVlanOutCRCAlignErrors=_ZxAnSwVlanOutCRCAlignErrors_Object((1,3,6,1,4,1,3902,1015,191,2,1,29),_ZxAnSwVlanOutCRCAlignErrors_Type())
zxAnSwVlanOutCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutCRCAlignErrors.setStatus(_A)
_ZxAnSwVlanInFragments_Type=Counter64
_ZxAnSwVlanInFragments_Object=MibTableColumn
zxAnSwVlanInFragments=_ZxAnSwVlanInFragments_Object((1,3,6,1,4,1,3902,1015,191,2,1,30),_ZxAnSwVlanInFragments_Type())
zxAnSwVlanInFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInFragments.setStatus(_A)
_ZxAnSwVlanOutFragments_Type=Counter64
_ZxAnSwVlanOutFragments_Object=MibTableColumn
zxAnSwVlanOutFragments=_ZxAnSwVlanOutFragments_Object((1,3,6,1,4,1,3902,1015,191,2,1,31),_ZxAnSwVlanOutFragments_Type())
zxAnSwVlanOutFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutFragments.setStatus(_A)
_ZxAnSwVlanInJabbers_Type=Counter64
_ZxAnSwVlanInJabbers_Object=MibTableColumn
zxAnSwVlanInJabbers=_ZxAnSwVlanInJabbers_Object((1,3,6,1,4,1,3902,1015,191,2,1,32),_ZxAnSwVlanInJabbers_Type())
zxAnSwVlanInJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInJabbers.setStatus(_A)
_ZxAnSwVlanOutJabbers_Type=Counter64
_ZxAnSwVlanOutJabbers_Object=MibTableColumn
zxAnSwVlanOutJabbers=_ZxAnSwVlanOutJabbers_Object((1,3,6,1,4,1,3902,1015,191,2,1,33),_ZxAnSwVlanOutJabbers_Type())
zxAnSwVlanOutJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutJabbers.setStatus(_A)
_ZxAnSwVlanInCollisions_Type=Counter64
_ZxAnSwVlanInCollisions_Object=MibTableColumn
zxAnSwVlanInCollisions=_ZxAnSwVlanInCollisions_Object((1,3,6,1,4,1,3902,1015,191,2,1,34),_ZxAnSwVlanInCollisions_Type())
zxAnSwVlanInCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInCollisions.setStatus(_A)
_ZxAnSwVlanOutCollisions_Type=Counter64
_ZxAnSwVlanOutCollisions_Object=MibTableColumn
zxAnSwVlanOutCollisions=_ZxAnSwVlanOutCollisions_Object((1,3,6,1,4,1,3902,1015,191,2,1,35),_ZxAnSwVlanOutCollisions_Type())
zxAnSwVlanOutCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutCollisions.setStatus(_A)
_ZxAnSwVlanInUnknownProtos_Type=Counter64
_ZxAnSwVlanInUnknownProtos_Object=MibTableColumn
zxAnSwVlanInUnknownProtos=_ZxAnSwVlanInUnknownProtos_Object((1,3,6,1,4,1,3902,1015,191,2,1,36),_ZxAnSwVlanInUnknownProtos_Type())
zxAnSwVlanInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanInUnknownProtos.setStatus(_A)
_ZxAnSwVlanOutUnknownProtos_Type=Counter64
_ZxAnSwVlanOutUnknownProtos_Object=MibTableColumn
zxAnSwVlanOutUnknownProtos=_ZxAnSwVlanOutUnknownProtos_Object((1,3,6,1,4,1,3902,1015,191,2,1,37),_ZxAnSwVlanOutUnknownProtos_Type())
zxAnSwVlanOutUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSwVlanOutUnknownProtos.setStatus(_A)
_ZxAnUserVlanPerfTable_Object=MibTable
zxAnUserVlanPerfTable=_ZxAnUserVlanPerfTable_Object((1,3,6,1,4,1,3902,1015,191,3))
if mibBuilder.loadTexts:zxAnUserVlanPerfTable.setStatus(_A)
_ZxAnUserVlanPerfEntry_Object=MibTableRow
zxAnUserVlanPerfEntry=_ZxAnUserVlanPerfEntry_Object((1,3,6,1,4,1,3902,1015,191,3,1))
zxAnUserVlanPerfEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:zxAnUserVlanPerfEntry.setStatus(_A)
_ZxAnUserVlanPortIfIndex_Type=ZxAnIfindex
_ZxAnUserVlanPortIfIndex_Object=MibTableColumn
zxAnUserVlanPortIfIndex=_ZxAnUserVlanPortIfIndex_Object((1,3,6,1,4,1,3902,1015,191,3,1,1),_ZxAnUserVlanPortIfIndex_Type())
zxAnUserVlanPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnUserVlanPortIfIndex.setStatus(_A)
_ZxAnUserVlanId_Type=VlanId
_ZxAnUserVlanId_Object=MibTableColumn
zxAnUserVlanId=_ZxAnUserVlanId_Object((1,3,6,1,4,1,3902,1015,191,3,1,2),_ZxAnUserVlanId_Type())
zxAnUserVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnUserVlanId.setStatus(_A)
class _ZxAnUserVlanPerfReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('perfReset',1))
_ZxAnUserVlanPerfReset_Type.__name__=_G
_ZxAnUserVlanPerfReset_Object=MibTableColumn
zxAnUserVlanPerfReset=_ZxAnUserVlanPerfReset_Object((1,3,6,1,4,1,3902,1015,191,3,1,3),_ZxAnUserVlanPerfReset_Type())
zxAnUserVlanPerfReset.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnUserVlanPerfReset.setStatus(_A)
_ZxAnUserVlanRxPkts_Type=Counter64
_ZxAnUserVlanRxPkts_Object=MibTableColumn
zxAnUserVlanRxPkts=_ZxAnUserVlanRxPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,4),_ZxAnUserVlanRxPkts_Type())
zxAnUserVlanRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxPkts.setStatus(_A)
_ZxAnUserVlanTxPkts_Type=Counter64
_ZxAnUserVlanTxPkts_Object=MibTableColumn
zxAnUserVlanTxPkts=_ZxAnUserVlanTxPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,5),_ZxAnUserVlanTxPkts_Type())
zxAnUserVlanTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxPkts.setStatus(_A)
_ZxAnUserVlanRxOctetRate_Type=Gauge32
_ZxAnUserVlanRxOctetRate_Object=MibTableColumn
zxAnUserVlanRxOctetRate=_ZxAnUserVlanRxOctetRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,6),_ZxAnUserVlanRxOctetRate_Type())
zxAnUserVlanRxOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanRxOctetRate.setUnits(_C)
_ZxAnUserVlanTxOctetRate_Type=Gauge32
_ZxAnUserVlanTxOctetRate_Object=MibTableColumn
zxAnUserVlanTxOctetRate=_ZxAnUserVlanTxOctetRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,7),_ZxAnUserVlanTxOctetRate_Type())
zxAnUserVlanTxOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanTxOctetRate.setUnits(_C)
_ZxAnUserVlanRxOctetPeakRate_Type=Gauge32
_ZxAnUserVlanRxOctetPeakRate_Object=MibTableColumn
zxAnUserVlanRxOctetPeakRate=_ZxAnUserVlanRxOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,8),_ZxAnUserVlanRxOctetPeakRate_Type())
zxAnUserVlanRxOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanRxOctetPeakRate.setUnits(_C)
_ZxAnUserVlanTxOctetPeakRate_Type=Gauge32
_ZxAnUserVlanTxOctetPeakRate_Object=MibTableColumn
zxAnUserVlanTxOctetPeakRate=_ZxAnUserVlanTxOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,9),_ZxAnUserVlanTxOctetPeakRate_Type())
zxAnUserVlanTxOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanTxOctetPeakRate.setUnits(_C)
_ZxAnUserVlanRxUcastPkts_Type=Counter64
_ZxAnUserVlanRxUcastPkts_Object=MibTableColumn
zxAnUserVlanRxUcastPkts=_ZxAnUserVlanRxUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,10),_ZxAnUserVlanRxUcastPkts_Type())
zxAnUserVlanRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxUcastPkts.setStatus(_A)
_ZxAnUserVlanTxUcastPkts_Type=Counter64
_ZxAnUserVlanTxUcastPkts_Object=MibTableColumn
zxAnUserVlanTxUcastPkts=_ZxAnUserVlanTxUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,11),_ZxAnUserVlanTxUcastPkts_Type())
zxAnUserVlanTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxUcastPkts.setStatus(_A)
_ZxAnUserVlanRxMulticastPkts_Type=Counter64
_ZxAnUserVlanRxMulticastPkts_Object=MibTableColumn
zxAnUserVlanRxMulticastPkts=_ZxAnUserVlanRxMulticastPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,12),_ZxAnUserVlanRxMulticastPkts_Type())
zxAnUserVlanRxMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxMulticastPkts.setStatus(_A)
_ZxAnUserVlanTxMulticastPkts_Type=Counter64
_ZxAnUserVlanTxMulticastPkts_Object=MibTableColumn
zxAnUserVlanTxMulticastPkts=_ZxAnUserVlanTxMulticastPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,13),_ZxAnUserVlanTxMulticastPkts_Type())
zxAnUserVlanTxMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxMulticastPkts.setStatus(_A)
_ZxAnUserVlanRxBroadcastPkts_Type=Counter64
_ZxAnUserVlanRxBroadcastPkts_Object=MibTableColumn
zxAnUserVlanRxBroadcastPkts=_ZxAnUserVlanRxBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,14),_ZxAnUserVlanRxBroadcastPkts_Type())
zxAnUserVlanRxBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxBroadcastPkts.setStatus(_A)
_ZxAnUserVlanTxBroadcastPkts_Type=Counter64
_ZxAnUserVlanTxBroadcastPkts_Object=MibTableColumn
zxAnUserVlanTxBroadcastPkts=_ZxAnUserVlanTxBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,191,3,1,15),_ZxAnUserVlanTxBroadcastPkts_Type())
zxAnUserVlanTxBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxBroadcastPkts.setStatus(_A)
_ZxAnUserVlanRxDiscards_Type=Counter64
_ZxAnUserVlanRxDiscards_Object=MibTableColumn
zxAnUserVlanRxDiscards=_ZxAnUserVlanRxDiscards_Object((1,3,6,1,4,1,3902,1015,191,3,1,16),_ZxAnUserVlanRxDiscards_Type())
zxAnUserVlanRxDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxDiscards.setStatus(_A)
_ZxAnUserVlanTxDiscards_Type=Counter64
_ZxAnUserVlanTxDiscards_Object=MibTableColumn
zxAnUserVlanTxDiscards=_ZxAnUserVlanTxDiscards_Object((1,3,6,1,4,1,3902,1015,191,3,1,17),_ZxAnUserVlanTxDiscards_Type())
zxAnUserVlanTxDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxDiscards.setStatus(_A)
_ZxAnUserVlanRxErrors_Type=Counter64
_ZxAnUserVlanRxErrors_Object=MibTableColumn
zxAnUserVlanRxErrors=_ZxAnUserVlanRxErrors_Object((1,3,6,1,4,1,3902,1015,191,3,1,18),_ZxAnUserVlanRxErrors_Type())
zxAnUserVlanRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxErrors.setStatus(_A)
_ZxAnUserVlanTxErrors_Type=Counter64
_ZxAnUserVlanTxErrors_Object=MibTableColumn
zxAnUserVlanTxErrors=_ZxAnUserVlanTxErrors_Object((1,3,6,1,4,1,3902,1015,191,3,1,19),_ZxAnUserVlanTxErrors_Type())
zxAnUserVlanTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxErrors.setStatus(_A)
_ZxAnUserVlanRxUcastOctetRate_Type=Gauge32
_ZxAnUserVlanRxUcastOctetRate_Object=MibTableColumn
zxAnUserVlanRxUcastOctetRate=_ZxAnUserVlanRxUcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,20),_ZxAnUserVlanRxUcastOctetRate_Type())
zxAnUserVlanRxUcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxUcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanRxUcastOctetRate.setUnits(_C)
_ZxAnUserVlanTxUcastOctetRate_Type=Gauge32
_ZxAnUserVlanTxUcastOctetRate_Object=MibTableColumn
zxAnUserVlanTxUcastOctetRate=_ZxAnUserVlanTxUcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,21),_ZxAnUserVlanTxUcastOctetRate_Type())
zxAnUserVlanTxUcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxUcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanTxUcastOctetRate.setUnits(_C)
_ZxAnUserVlanRxUcastOctetPeakRate_Type=Gauge32
_ZxAnUserVlanRxUcastOctetPeakRate_Object=MibTableColumn
zxAnUserVlanRxUcastOctetPeakRate=_ZxAnUserVlanRxUcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,22),_ZxAnUserVlanRxUcastOctetPeakRate_Type())
zxAnUserVlanRxUcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxUcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanRxUcastOctetPeakRate.setUnits(_C)
_ZxAnUserVlanTxUcastOctetPeakRate_Type=Gauge32
_ZxAnUserVlanTxUcastOctetPeakRate_Object=MibTableColumn
zxAnUserVlanTxUcastOctetPeakRate=_ZxAnUserVlanTxUcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,23),_ZxAnUserVlanTxUcastOctetPeakRate_Type())
zxAnUserVlanTxUcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxUcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanTxUcastOctetPeakRate.setUnits(_C)
_ZxAnUserVlanRxMcastOctetRate_Type=Gauge32
_ZxAnUserVlanRxMcastOctetRate_Object=MibTableColumn
zxAnUserVlanRxMcastOctetRate=_ZxAnUserVlanRxMcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,24),_ZxAnUserVlanRxMcastOctetRate_Type())
zxAnUserVlanRxMcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxMcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanRxMcastOctetRate.setUnits(_C)
_ZxAnUserVlanTxMcastOctetRate_Type=Gauge32
_ZxAnUserVlanTxMcastOctetRate_Object=MibTableColumn
zxAnUserVlanTxMcastOctetRate=_ZxAnUserVlanTxMcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,25),_ZxAnUserVlanTxMcastOctetRate_Type())
zxAnUserVlanTxMcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxMcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanTxMcastOctetRate.setUnits(_C)
_ZxAnUserVlanRxMcastOctetPeakRate_Type=Gauge32
_ZxAnUserVlanRxMcastOctetPeakRate_Object=MibTableColumn
zxAnUserVlanRxMcastOctetPeakRate=_ZxAnUserVlanRxMcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,26),_ZxAnUserVlanRxMcastOctetPeakRate_Type())
zxAnUserVlanRxMcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanRxMcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanRxMcastOctetPeakRate.setUnits(_C)
_ZxAnUserVlanTxMcastOctetPeakRate_Type=Gauge32
_ZxAnUserVlanTxMcastOctetPeakRate_Object=MibTableColumn
zxAnUserVlanTxMcastOctetPeakRate=_ZxAnUserVlanTxMcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,3,1,27),_ZxAnUserVlanTxMcastOctetPeakRate_Type())
zxAnUserVlanTxMcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUserVlanTxMcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnUserVlanTxMcastOctetPeakRate.setUnits(_C)
_ZxAnUserVlanPerfRowStatus_Type=RowStatus
_ZxAnUserVlanPerfRowStatus_Object=MibTableColumn
zxAnUserVlanPerfRowStatus=_ZxAnUserVlanPerfRowStatus_Object((1,3,6,1,4,1,3902,1015,191,3,1,100),_ZxAnUserVlanPerfRowStatus_Type())
zxAnUserVlanPerfRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnUserVlanPerfRowStatus.setStatus(_A)
_ZxAnVlanStatTable_Object=MibTable
zxAnVlanStatTable=_ZxAnVlanStatTable_Object((1,3,6,1,4,1,3902,1015,191,4))
if mibBuilder.loadTexts:zxAnVlanStatTable.setStatus(_A)
_ZxAnVlanStatEntry_Object=MibTableRow
zxAnVlanStatEntry=_ZxAnVlanStatEntry_Object((1,3,6,1,4,1,3902,1015,191,4,1))
zxAnVlanStatEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:zxAnVlanStatEntry.setStatus(_A)
_ZxAnSVlanId_Type=VlanId
_ZxAnSVlanId_Object=MibTableColumn
zxAnSVlanId=_ZxAnSVlanId_Object((1,3,6,1,4,1,3902,1015,191,4,1,1),_ZxAnSVlanId_Type())
zxAnSVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSVlanId.setStatus(_A)
class _ZxAnCVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnCVlanId_Type.__name__=_G
_ZxAnCVlanId_Object=MibTableColumn
zxAnCVlanId=_ZxAnCVlanId_Object((1,3,6,1,4,1,3902,1015,191,4,1,2),_ZxAnCVlanId_Type())
zxAnCVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCVlanId.setStatus(_A)
_ZxAnVlanRxOctets_Type=Counter64
_ZxAnVlanRxOctets_Object=MibTableColumn
zxAnVlanRxOctets=_ZxAnVlanRxOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,3),_ZxAnVlanRxOctets_Type())
zxAnVlanRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxOctets.setStatus(_A)
_ZxAnVlanTxOctets_Type=Counter64
_ZxAnVlanTxOctets_Object=MibTableColumn
zxAnVlanTxOctets=_ZxAnVlanTxOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,4),_ZxAnVlanTxOctets_Type())
zxAnVlanTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxOctets.setStatus(_A)
_ZxAnVlanRxPkts_Type=Counter64
_ZxAnVlanRxPkts_Object=MibTableColumn
zxAnVlanRxPkts=_ZxAnVlanRxPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,5),_ZxAnVlanRxPkts_Type())
zxAnVlanRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxPkts.setStatus(_A)
_ZxAnVlanTxPkts_Type=Counter64
_ZxAnVlanTxPkts_Object=MibTableColumn
zxAnVlanTxPkts=_ZxAnVlanTxPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,6),_ZxAnVlanTxPkts_Type())
zxAnVlanTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxPkts.setStatus(_A)
_ZxAnVlanRxPktRate_Type=Gauge32
_ZxAnVlanRxPktRate_Object=MibTableColumn
zxAnVlanRxPktRate=_ZxAnVlanRxPktRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,7),_ZxAnVlanRxPktRate_Type())
zxAnVlanRxPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxPktRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxPktRate.setUnits('pps')
_ZxAnVlanTxPktRate_Type=Gauge32
_ZxAnVlanTxPktRate_Object=MibTableColumn
zxAnVlanTxPktRate=_ZxAnVlanTxPktRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,8),_ZxAnVlanTxPktRate_Type())
zxAnVlanTxPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxPktRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxPktRate.setUnits('pps')
_ZxAnVlanRxDiscardPkts_Type=Counter64
_ZxAnVlanRxDiscardPkts_Object=MibTableColumn
zxAnVlanRxDiscardPkts=_ZxAnVlanRxDiscardPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,9),_ZxAnVlanRxDiscardPkts_Type())
zxAnVlanRxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxDiscardPkts.setStatus(_A)
_ZxAnVlanTxDiscardPkts_Type=Counter64
_ZxAnVlanTxDiscardPkts_Object=MibTableColumn
zxAnVlanTxDiscardPkts=_ZxAnVlanTxDiscardPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,10),_ZxAnVlanTxDiscardPkts_Type())
zxAnVlanTxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxDiscardPkts.setStatus(_A)
_ZxAnVlanLackOfBufferDiscards_Type=Counter64
_ZxAnVlanLackOfBufferDiscards_Object=MibTableColumn
zxAnVlanLackOfBufferDiscards=_ZxAnVlanLackOfBufferDiscards_Object((1,3,6,1,4,1,3902,1015,191,4,1,11),_ZxAnVlanLackOfBufferDiscards_Type())
zxAnVlanLackOfBufferDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanLackOfBufferDiscards.setStatus(_A)
_ZxAnVlanDelayExceededDiscards_Type=Counter64
_ZxAnVlanDelayExceededDiscards_Object=MibTableColumn
zxAnVlanDelayExceededDiscards=_ZxAnVlanDelayExceededDiscards_Object((1,3,6,1,4,1,3902,1015,191,4,1,12),_ZxAnVlanDelayExceededDiscards_Type())
zxAnVlanDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanDelayExceededDiscards.setStatus(_A)
_ZxAnVlanErrorDiscards_Type=Counter64
_ZxAnVlanErrorDiscards_Object=MibTableColumn
zxAnVlanErrorDiscards=_ZxAnVlanErrorDiscards_Object((1,3,6,1,4,1,3902,1015,191,4,1,13),_ZxAnVlanErrorDiscards_Type())
zxAnVlanErrorDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanErrorDiscards.setStatus(_A)
_ZxAnVlanIngressFilterDiscards_Type=Counter64
_ZxAnVlanIngressFilterDiscards_Object=MibTableColumn
zxAnVlanIngressFilterDiscards=_ZxAnVlanIngressFilterDiscards_Object((1,3,6,1,4,1,3902,1015,191,4,1,14),_ZxAnVlanIngressFilterDiscards_Type())
zxAnVlanIngressFilterDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIngressFilterDiscards.setStatus(_A)
_ZxAnVlanRxOctetRate_Type=Gauge32
_ZxAnVlanRxOctetRate_Object=MibTableColumn
zxAnVlanRxOctetRate=_ZxAnVlanRxOctetRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,15),_ZxAnVlanRxOctetRate_Type())
zxAnVlanRxOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxOctetRate.setUnits(_C)
_ZxAnVlanTxOctetRate_Type=Gauge32
_ZxAnVlanTxOctetRate_Object=MibTableColumn
zxAnVlanTxOctetRate=_ZxAnVlanTxOctetRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,16),_ZxAnVlanTxOctetRate_Type())
zxAnVlanTxOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxOctetRate.setUnits(_C)
_ZxAnVlanRxOctetPeakRate_Type=Gauge32
_ZxAnVlanRxOctetPeakRate_Object=MibTableColumn
zxAnVlanRxOctetPeakRate=_ZxAnVlanRxOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,17),_ZxAnVlanRxOctetPeakRate_Type())
zxAnVlanRxOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxOctetPeakRate.setUnits(_C)
_ZxAnVlanTxOctetPeakRate_Type=Gauge32
_ZxAnVlanTxOctetPeakRate_Object=MibTableColumn
zxAnVlanTxOctetPeakRate=_ZxAnVlanTxOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,18),_ZxAnVlanTxOctetPeakRate_Type())
zxAnVlanTxOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxOctetPeakRate.setUnits(_C)
_ZxAnVlanRxUcastPkts_Type=Counter64
_ZxAnVlanRxUcastPkts_Object=MibTableColumn
zxAnVlanRxUcastPkts=_ZxAnVlanRxUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,19),_ZxAnVlanRxUcastPkts_Type())
zxAnVlanRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxUcastPkts.setStatus(_A)
_ZxAnVlanTxUcastPkts_Type=Counter64
_ZxAnVlanTxUcastPkts_Object=MibTableColumn
zxAnVlanTxUcastPkts=_ZxAnVlanTxUcastPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,20),_ZxAnVlanTxUcastPkts_Type())
zxAnVlanTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxUcastPkts.setStatus(_A)
_ZxAnVlanRxUcastOctets_Type=Counter64
_ZxAnVlanRxUcastOctets_Object=MibTableColumn
zxAnVlanRxUcastOctets=_ZxAnVlanRxUcastOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,21),_ZxAnVlanRxUcastOctets_Type())
zxAnVlanRxUcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxUcastOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxUcastOctets.setUnits(_D)
_ZxAnVlanTxUcastOctets_Type=Counter64
_ZxAnVlanTxUcastOctets_Object=MibTableColumn
zxAnVlanTxUcastOctets=_ZxAnVlanTxUcastOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,22),_ZxAnVlanTxUcastOctets_Type())
zxAnVlanTxUcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxUcastOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxUcastOctets.setUnits(_D)
_ZxAnVlanRxUcastOctetRate_Type=Gauge32
_ZxAnVlanRxUcastOctetRate_Object=MibTableColumn
zxAnVlanRxUcastOctetRate=_ZxAnVlanRxUcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,23),_ZxAnVlanRxUcastOctetRate_Type())
zxAnVlanRxUcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxUcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxUcastOctetRate.setUnits(_C)
_ZxAnVlanTxUcastOctetRate_Type=Gauge32
_ZxAnVlanTxUcastOctetRate_Object=MibTableColumn
zxAnVlanTxUcastOctetRate=_ZxAnVlanTxUcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,24),_ZxAnVlanTxUcastOctetRate_Type())
zxAnVlanTxUcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxUcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxUcastOctetRate.setUnits(_C)
_ZxAnVlanRxUcastOctetPeakRate_Type=Gauge32
_ZxAnVlanRxUcastOctetPeakRate_Object=MibTableColumn
zxAnVlanRxUcastOctetPeakRate=_ZxAnVlanRxUcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,25),_ZxAnVlanRxUcastOctetPeakRate_Type())
zxAnVlanRxUcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxUcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxUcastOctetPeakRate.setUnits(_C)
_ZxAnVlanTxUcastOctetPeakRate_Type=Gauge32
_ZxAnVlanTxUcastOctetPeakRate_Object=MibTableColumn
zxAnVlanTxUcastOctetPeakRate=_ZxAnVlanTxUcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,26),_ZxAnVlanTxUcastOctetPeakRate_Type())
zxAnVlanTxUcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxUcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxUcastOctetPeakRate.setUnits(_C)
_ZxAnVlanRxMcastPkts_Type=Counter64
_ZxAnVlanRxMcastPkts_Object=MibTableColumn
zxAnVlanRxMcastPkts=_ZxAnVlanRxMcastPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,27),_ZxAnVlanRxMcastPkts_Type())
zxAnVlanRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxMcastPkts.setStatus(_A)
_ZxAnVlanTxMcastPkts_Type=Counter64
_ZxAnVlanTxMcastPkts_Object=MibTableColumn
zxAnVlanTxMcastPkts=_ZxAnVlanTxMcastPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,28),_ZxAnVlanTxMcastPkts_Type())
zxAnVlanTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxMcastPkts.setStatus(_A)
_ZxAnVlanRxMcastOctets_Type=Counter64
_ZxAnVlanRxMcastOctets_Object=MibTableColumn
zxAnVlanRxMcastOctets=_ZxAnVlanRxMcastOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,29),_ZxAnVlanRxMcastOctets_Type())
zxAnVlanRxMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxMcastOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxMcastOctets.setUnits(_D)
_ZxAnVlanTxMcastOctets_Type=Counter64
_ZxAnVlanTxMcastOctets_Object=MibTableColumn
zxAnVlanTxMcastOctets=_ZxAnVlanTxMcastOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,30),_ZxAnVlanTxMcastOctets_Type())
zxAnVlanTxMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxMcastOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxMcastOctets.setUnits(_D)
_ZxAnVlanRxMcastOctetRate_Type=Gauge32
_ZxAnVlanRxMcastOctetRate_Object=MibTableColumn
zxAnVlanRxMcastOctetRate=_ZxAnVlanRxMcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,31),_ZxAnVlanRxMcastOctetRate_Type())
zxAnVlanRxMcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxMcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxMcastOctetRate.setUnits(_C)
_ZxAnVlanTxMcastOctetRate_Type=Gauge32
_ZxAnVlanTxMcastOctetRate_Object=MibTableColumn
zxAnVlanTxMcastOctetRate=_ZxAnVlanTxMcastOctetRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,32),_ZxAnVlanTxMcastOctetRate_Type())
zxAnVlanTxMcastOctetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxMcastOctetRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxMcastOctetRate.setUnits(_C)
_ZxAnVlanRxMcastOctetPeakRate_Type=Gauge32
_ZxAnVlanRxMcastOctetPeakRate_Object=MibTableColumn
zxAnVlanRxMcastOctetPeakRate=_ZxAnVlanRxMcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,33),_ZxAnVlanRxMcastOctetPeakRate_Type())
zxAnVlanRxMcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxMcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxMcastOctetPeakRate.setUnits(_C)
_ZxAnVlanTxMcastOctetPeakRate_Type=Gauge32
_ZxAnVlanTxMcastOctetPeakRate_Object=MibTableColumn
zxAnVlanTxMcastOctetPeakRate=_ZxAnVlanTxMcastOctetPeakRate_Object((1,3,6,1,4,1,3902,1015,191,4,1,34),_ZxAnVlanTxMcastOctetPeakRate_Type())
zxAnVlanTxMcastOctetPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxMcastOctetPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxMcastOctetPeakRate.setUnits(_C)
_ZxAnVlanRxBcastPkts_Type=Counter64
_ZxAnVlanRxBcastPkts_Object=MibTableColumn
zxAnVlanRxBcastPkts=_ZxAnVlanRxBcastPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,35),_ZxAnVlanRxBcastPkts_Type())
zxAnVlanRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxBcastPkts.setStatus(_A)
_ZxAnVlanTxBcastPkts_Type=Counter64
_ZxAnVlanTxBcastPkts_Object=MibTableColumn
zxAnVlanTxBcastPkts=_ZxAnVlanTxBcastPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,36),_ZxAnVlanTxBcastPkts_Type())
zxAnVlanTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxBcastPkts.setStatus(_A)
_ZxAnVlanRxBcastOctets_Type=Counter64
_ZxAnVlanRxBcastOctets_Object=MibTableColumn
zxAnVlanRxBcastOctets=_ZxAnVlanRxBcastOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,37),_ZxAnVlanRxBcastOctets_Type())
zxAnVlanRxBcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxBcastOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxBcastOctets.setUnits(_D)
_ZxAnVlanTxBcastOctets_Type=Counter64
_ZxAnVlanTxBcastOctets_Object=MibTableColumn
zxAnVlanTxBcastOctets=_ZxAnVlanTxBcastOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,38),_ZxAnVlanTxBcastOctets_Type())
zxAnVlanTxBcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxBcastOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxBcastOctets.setUnits(_D)
_ZxAnVlanRxFloodPkts_Type=Counter64
_ZxAnVlanRxFloodPkts_Object=MibTableColumn
zxAnVlanRxFloodPkts=_ZxAnVlanRxFloodPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,39),_ZxAnVlanRxFloodPkts_Type())
zxAnVlanRxFloodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxFloodPkts.setStatus(_A)
_ZxAnVlanTxFloodPkts_Type=Counter64
_ZxAnVlanTxFloodPkts_Object=MibTableColumn
zxAnVlanTxFloodPkts=_ZxAnVlanTxFloodPkts_Object((1,3,6,1,4,1,3902,1015,191,4,1,40),_ZxAnVlanTxFloodPkts_Type())
zxAnVlanTxFloodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxFloodPkts.setStatus(_A)
_ZxAnVlanRxFloodOctets_Type=Counter64
_ZxAnVlanRxFloodOctets_Object=MibTableColumn
zxAnVlanRxFloodOctets=_ZxAnVlanRxFloodOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,41),_ZxAnVlanRxFloodOctets_Type())
zxAnVlanRxFloodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRxFloodOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanRxFloodOctets.setUnits(_D)
_ZxAnVlanTxFloodOctets_Type=Counter64
_ZxAnVlanTxFloodOctets_Object=MibTableColumn
zxAnVlanTxFloodOctets=_ZxAnVlanTxFloodOctets_Object((1,3,6,1,4,1,3902,1015,191,4,1,42),_ZxAnVlanTxFloodOctets_Type())
zxAnVlanTxFloodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTxFloodOctets.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanTxFloodOctets.setUnits(_D)
_ZxAnVlanStatRowStatus_Type=RowStatus
_ZxAnVlanStatRowStatus_Object=MibTableColumn
zxAnVlanStatRowStatus=_ZxAnVlanStatRowStatus_Object((1,3,6,1,4,1,3902,1015,191,4,1,101),_ZxAnVlanStatRowStatus_Type())
zxAnVlanStatRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVlanStatRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxAnVlanStatisticMib':zxAnVlanStatisticMib,'zxAnVlanPerfEnableTable':zxAnVlanPerfEnableTable,'zxAnVlanPerfEnableEntry':zxAnVlanPerfEnableEntry,_J:zxAnEnVlanId,'zxVlanPerfEnable':zxVlanPerfEnable,'zxVlanIDAllEnable':zxVlanIDAllEnable,'zxAnSwVlanPerfTable':zxAnSwVlanPerfTable,'zxAnSwVlanPerfEntry':zxAnSwVlanPerfEntry,_L:zxAnSwVlanId,'zxAnSwVlanInOctets':zxAnSwVlanInOctets,'zxAnSwVlanOutOctets':zxAnSwVlanOutOctets,'zxAnSwVlanInPkts':zxAnSwVlanInPkts,'zxAnSwVlanOutPkts':zxAnSwVlanOutPkts,'zxAnSwVlanInBandwidth':zxAnSwVlanInBandwidth,'zxAnSwVlanOutBandwidth':zxAnSwVlanOutBandwidth,'zxAnSwVlanInBandwidthUtility':zxAnSwVlanInBandwidthUtility,'zxAnSwVlanOutBandwidthUtility':zxAnSwVlanOutBandwidthUtility,'zxAnSwVlanInCurrOctetRate':zxAnSwVlanInCurrOctetRate,'zxAnSwVlanOutCurrOctetRate':zxAnSwVlanOutCurrOctetRate,'zxAnSwVlanInCurrPktRate':zxAnSwVlanInCurrPktRate,'zxAnSwVlanOutCurrPktRate':zxAnSwVlanOutCurrPktRate,'zxAnSwVlanInUcastPkts':zxAnSwVlanInUcastPkts,'zxAnSwVlanOutUcastPkts':zxAnSwVlanOutUcastPkts,'zxAnSwVlanInMulticastPkts':zxAnSwVlanInMulticastPkts,'zxAnSwVlanOutMulticastPkts':zxAnSwVlanOutMulticastPkts,'zxAnSwVlanInNUcastPkts':zxAnSwVlanInNUcastPkts,'zxAnSwVlanOutNUcastPkts':zxAnSwVlanOutNUcastPkts,'zxAnSwVlanInBroadcastPkts':zxAnSwVlanInBroadcastPkts,'zxAnSwVlanOutBroadcastPkts':zxAnSwVlanOutBroadcastPkts,'zxAnSwVlanInDiscards':zxAnSwVlanInDiscards,'zxAnSwVlanOutDiscards':zxAnSwVlanOutDiscards,'zxAnSwVlanInUndersizePkts':zxAnSwVlanInUndersizePkts,'zxAnSwVlanOutUndersizePkts':zxAnSwVlanOutUndersizePkts,'zxAnSwVlanInOversizePkts':zxAnSwVlanInOversizePkts,'zxAnSwVlanOutOversizePkts':zxAnSwVlanOutOversizePkts,'zxAnSwVlanInCRCAlignErrors':zxAnSwVlanInCRCAlignErrors,'zxAnSwVlanOutCRCAlignErrors':zxAnSwVlanOutCRCAlignErrors,'zxAnSwVlanInFragments':zxAnSwVlanInFragments,'zxAnSwVlanOutFragments':zxAnSwVlanOutFragments,'zxAnSwVlanInJabbers':zxAnSwVlanInJabbers,'zxAnSwVlanOutJabbers':zxAnSwVlanOutJabbers,'zxAnSwVlanInCollisions':zxAnSwVlanInCollisions,'zxAnSwVlanOutCollisions':zxAnSwVlanOutCollisions,'zxAnSwVlanInUnknownProtos':zxAnSwVlanInUnknownProtos,'zxAnSwVlanOutUnknownProtos':zxAnSwVlanOutUnknownProtos,'zxAnUserVlanPerfTable':zxAnUserVlanPerfTable,'zxAnUserVlanPerfEntry':zxAnUserVlanPerfEntry,_M:zxAnUserVlanPortIfIndex,_N:zxAnUserVlanId,'zxAnUserVlanPerfReset':zxAnUserVlanPerfReset,'zxAnUserVlanRxPkts':zxAnUserVlanRxPkts,'zxAnUserVlanTxPkts':zxAnUserVlanTxPkts,'zxAnUserVlanRxOctetRate':zxAnUserVlanRxOctetRate,'zxAnUserVlanTxOctetRate':zxAnUserVlanTxOctetRate,'zxAnUserVlanRxOctetPeakRate':zxAnUserVlanRxOctetPeakRate,'zxAnUserVlanTxOctetPeakRate':zxAnUserVlanTxOctetPeakRate,'zxAnUserVlanRxUcastPkts':zxAnUserVlanRxUcastPkts,'zxAnUserVlanTxUcastPkts':zxAnUserVlanTxUcastPkts,'zxAnUserVlanRxMulticastPkts':zxAnUserVlanRxMulticastPkts,'zxAnUserVlanTxMulticastPkts':zxAnUserVlanTxMulticastPkts,'zxAnUserVlanRxBroadcastPkts':zxAnUserVlanRxBroadcastPkts,'zxAnUserVlanTxBroadcastPkts':zxAnUserVlanTxBroadcastPkts,'zxAnUserVlanRxDiscards':zxAnUserVlanRxDiscards,'zxAnUserVlanTxDiscards':zxAnUserVlanTxDiscards,'zxAnUserVlanRxErrors':zxAnUserVlanRxErrors,'zxAnUserVlanTxErrors':zxAnUserVlanTxErrors,'zxAnUserVlanRxUcastOctetRate':zxAnUserVlanRxUcastOctetRate,'zxAnUserVlanTxUcastOctetRate':zxAnUserVlanTxUcastOctetRate,'zxAnUserVlanRxUcastOctetPeakRate':zxAnUserVlanRxUcastOctetPeakRate,'zxAnUserVlanTxUcastOctetPeakRate':zxAnUserVlanTxUcastOctetPeakRate,'zxAnUserVlanRxMcastOctetRate':zxAnUserVlanRxMcastOctetRate,'zxAnUserVlanTxMcastOctetRate':zxAnUserVlanTxMcastOctetRate,'zxAnUserVlanRxMcastOctetPeakRate':zxAnUserVlanRxMcastOctetPeakRate,'zxAnUserVlanTxMcastOctetPeakRate':zxAnUserVlanTxMcastOctetPeakRate,'zxAnUserVlanPerfRowStatus':zxAnUserVlanPerfRowStatus,'zxAnVlanStatTable':zxAnVlanStatTable,'zxAnVlanStatEntry':zxAnVlanStatEntry,_O:zxAnSVlanId,_P:zxAnCVlanId,'zxAnVlanRxOctets':zxAnVlanRxOctets,'zxAnVlanTxOctets':zxAnVlanTxOctets,'zxAnVlanRxPkts':zxAnVlanRxPkts,'zxAnVlanTxPkts':zxAnVlanTxPkts,'zxAnVlanRxPktRate':zxAnVlanRxPktRate,'zxAnVlanTxPktRate':zxAnVlanTxPktRate,'zxAnVlanRxDiscardPkts':zxAnVlanRxDiscardPkts,'zxAnVlanTxDiscardPkts':zxAnVlanTxDiscardPkts,'zxAnVlanLackOfBufferDiscards':zxAnVlanLackOfBufferDiscards,'zxAnVlanDelayExceededDiscards':zxAnVlanDelayExceededDiscards,'zxAnVlanErrorDiscards':zxAnVlanErrorDiscards,'zxAnVlanIngressFilterDiscards':zxAnVlanIngressFilterDiscards,'zxAnVlanRxOctetRate':zxAnVlanRxOctetRate,'zxAnVlanTxOctetRate':zxAnVlanTxOctetRate,'zxAnVlanRxOctetPeakRate':zxAnVlanRxOctetPeakRate,'zxAnVlanTxOctetPeakRate':zxAnVlanTxOctetPeakRate,'zxAnVlanRxUcastPkts':zxAnVlanRxUcastPkts,'zxAnVlanTxUcastPkts':zxAnVlanTxUcastPkts,'zxAnVlanRxUcastOctets':zxAnVlanRxUcastOctets,'zxAnVlanTxUcastOctets':zxAnVlanTxUcastOctets,'zxAnVlanRxUcastOctetRate':zxAnVlanRxUcastOctetRate,'zxAnVlanTxUcastOctetRate':zxAnVlanTxUcastOctetRate,'zxAnVlanRxUcastOctetPeakRate':zxAnVlanRxUcastOctetPeakRate,'zxAnVlanTxUcastOctetPeakRate':zxAnVlanTxUcastOctetPeakRate,'zxAnVlanRxMcastPkts':zxAnVlanRxMcastPkts,'zxAnVlanTxMcastPkts':zxAnVlanTxMcastPkts,'zxAnVlanRxMcastOctets':zxAnVlanRxMcastOctets,'zxAnVlanTxMcastOctets':zxAnVlanTxMcastOctets,'zxAnVlanRxMcastOctetRate':zxAnVlanRxMcastOctetRate,'zxAnVlanTxMcastOctetRate':zxAnVlanTxMcastOctetRate,'zxAnVlanRxMcastOctetPeakRate':zxAnVlanRxMcastOctetPeakRate,'zxAnVlanTxMcastOctetPeakRate':zxAnVlanTxMcastOctetPeakRate,'zxAnVlanRxBcastPkts':zxAnVlanRxBcastPkts,'zxAnVlanTxBcastPkts':zxAnVlanTxBcastPkts,'zxAnVlanRxBcastOctets':zxAnVlanRxBcastOctets,'zxAnVlanTxBcastOctets':zxAnVlanTxBcastOctets,'zxAnVlanRxFloodPkts':zxAnVlanRxFloodPkts,'zxAnVlanTxFloodPkts':zxAnVlanTxFloodPkts,'zxAnVlanRxFloodOctets':zxAnVlanRxFloodOctets,'zxAnVlanTxFloodOctets':zxAnVlanTxFloodOctets,'zxAnVlanStatRowStatus':zxAnVlanStatRowStatus})