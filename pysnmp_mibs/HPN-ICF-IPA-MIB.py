_S='hpnicfIpaFWListIpDst'
_R='hpnicfIpaFWListIpSrc'
_Q='hpnicfIpaExtListProtocol'
_P='hpnicfIpaExtListIpDst'
_O='hpnicfIpaExtListIpSrc'
_N='hpnicfIpaIntListProtocol'
_M='hpnicfIpaIntListIpDst'
_L='hpnicfIpaIntListIpSrc'
_K='hpnicfIpaAccountListIndex'
_J='hpnicfIpaIfConfigIfIndex'
_I='read-create'
_H='enabled'
_G='disabled'
_F='read-write'
_E='not-accessible'
_D='HPN-ICF-IPA-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfIpa=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,25))
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpaGlobalStats_ObjectIdentity=ObjectIdentity
hpnicfIpaGlobalStats=_HpnicfIpaGlobalStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,25,1))
class _HpnicfIpaGlobalEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpnicfIpaGlobalEnable_Type.__name__=_C
_HpnicfIpaGlobalEnable_Object=MibScalar
hpnicfIpaGlobalEnable=_HpnicfIpaGlobalEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,1),_HpnicfIpaGlobalEnable_Type())
hpnicfIpaGlobalEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaGlobalEnable.setStatus(_A)
class _HpnicfIpaTimeOutSeconds_Type(Integer32):defaultValue=43200
_HpnicfIpaTimeOutSeconds_Type.__name__=_C
_HpnicfIpaTimeOutSeconds_Object=MibScalar
hpnicfIpaTimeOutSeconds=_HpnicfIpaTimeOutSeconds_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,2),_HpnicfIpaTimeOutSeconds_Type())
hpnicfIpaTimeOutSeconds.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaTimeOutSeconds.setStatus(_A)
class _HpnicfIpaIntListMaxItemNum_Type(Integer32):defaultValue=512
_HpnicfIpaIntListMaxItemNum_Type.__name__=_C
_HpnicfIpaIntListMaxItemNum_Object=MibScalar
hpnicfIpaIntListMaxItemNum=_HpnicfIpaIntListMaxItemNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,3),_HpnicfIpaIntListMaxItemNum_Type())
hpnicfIpaIntListMaxItemNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaIntListMaxItemNum.setStatus(_A)
class _HpnicfIpaExtListMaxItemNum_Type(Integer32):defaultValue=0
_HpnicfIpaExtListMaxItemNum_Type.__name__=_C
_HpnicfIpaExtListMaxItemNum_Object=MibScalar
hpnicfIpaExtListMaxItemNum=_HpnicfIpaExtListMaxItemNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,4),_HpnicfIpaExtListMaxItemNum_Type())
hpnicfIpaExtListMaxItemNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaExtListMaxItemNum.setStatus(_A)
_HpnicfIpaFWListMaxItemNum_Type=Integer32
_HpnicfIpaFWListMaxItemNum_Object=MibScalar
hpnicfIpaFWListMaxItemNum=_HpnicfIpaFWListMaxItemNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,5),_HpnicfIpaFWListMaxItemNum_Type())
hpnicfIpaFWListMaxItemNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaFWListMaxItemNum.setStatus(_A)
_HpnicfIpaAccountListMaxItemNum_Type=Integer32
_HpnicfIpaAccountListMaxItemNum_Object=MibScalar
hpnicfIpaAccountListMaxItemNum=_HpnicfIpaAccountListMaxItemNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,6),_HpnicfIpaAccountListMaxItemNum_Type())
hpnicfIpaAccountListMaxItemNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaAccountListMaxItemNum.setStatus(_A)
_HpnicfIpaAccountListNextIndex_Type=Integer32
_HpnicfIpaAccountListNextIndex_Object=MibScalar
hpnicfIpaAccountListNextIndex=_HpnicfIpaAccountListNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,7),_HpnicfIpaAccountListNextIndex_Type())
hpnicfIpaAccountListNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaAccountListNextIndex.setStatus(_A)
class _HpnicfIpaListCleaningFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('cleaningAll',2),('cleaningIntList',3),('cleaningExtList',4),('cleaningFWList',5)))
_HpnicfIpaListCleaningFlag_Type.__name__=_C
_HpnicfIpaListCleaningFlag_Object=MibScalar
hpnicfIpaListCleaningFlag=_HpnicfIpaListCleaningFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,1,8),_HpnicfIpaListCleaningFlag_Type())
hpnicfIpaListCleaningFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaListCleaningFlag.setStatus(_A)
_HpnicfIpaIfConfigTable_Object=MibTable
hpnicfIpaIfConfigTable=_HpnicfIpaIfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,2))
if mibBuilder.loadTexts:hpnicfIpaIfConfigTable.setStatus(_A)
_HpnicfIpaIfConfigEntry_Object=MibTableRow
hpnicfIpaIfConfigEntry=_HpnicfIpaIfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,2,1))
hpnicfIpaIfConfigEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfIpaIfConfigEntry.setStatus(_A)
_HpnicfIpaIfConfigIfIndex_Type=InterfaceIndex
_HpnicfIpaIfConfigIfIndex_Object=MibTableColumn
hpnicfIpaIfConfigIfIndex=_HpnicfIpaIfConfigIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,2,1,1),_HpnicfIpaIfConfigIfIndex_Type())
hpnicfIpaIfConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaIfConfigIfIndex.setStatus(_A)
class _HpnicfIpaIfConfigInEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpnicfIpaIfConfigInEnable_Type.__name__=_C
_HpnicfIpaIfConfigInEnable_Object=MibTableColumn
hpnicfIpaIfConfigInEnable=_HpnicfIpaIfConfigInEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,2,1,2),_HpnicfIpaIfConfigInEnable_Type())
hpnicfIpaIfConfigInEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaIfConfigInEnable.setStatus(_A)
class _HpnicfIpaIfConfigOutEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpnicfIpaIfConfigOutEnable_Type.__name__=_C
_HpnicfIpaIfConfigOutEnable_Object=MibTableColumn
hpnicfIpaIfConfigOutEnable=_HpnicfIpaIfConfigOutEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,2,1,3),_HpnicfIpaIfConfigOutEnable_Type())
hpnicfIpaIfConfigOutEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaIfConfigOutEnable.setStatus(_A)
class _HpnicfIpaIfConfigFWEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nodirection',1),('inbound',2),('outbound',3),('bidirection',4)))
_HpnicfIpaIfConfigFWEnable_Type.__name__=_C
_HpnicfIpaIfConfigFWEnable_Object=MibTableColumn
hpnicfIpaIfConfigFWEnable=_HpnicfIpaIfConfigFWEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,2,1,4),_HpnicfIpaIfConfigFWEnable_Type())
hpnicfIpaIfConfigFWEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpaIfConfigFWEnable.setStatus(_A)
_HpnicfIpaAccountListTable_Object=MibTable
hpnicfIpaAccountListTable=_HpnicfIpaAccountListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,3))
if mibBuilder.loadTexts:hpnicfIpaAccountListTable.setStatus(_A)
_HpnicfIpaAccountListEntry_Object=MibTableRow
hpnicfIpaAccountListEntry=_HpnicfIpaAccountListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,3,1))
hpnicfIpaAccountListEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hpnicfIpaAccountListEntry.setStatus(_A)
class _HpnicfIpaAccountListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpaAccountListIndex_Type.__name__=_C
_HpnicfIpaAccountListIndex_Object=MibTableColumn
hpnicfIpaAccountListIndex=_HpnicfIpaAccountListIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,3,1,1),_HpnicfIpaAccountListIndex_Type())
hpnicfIpaAccountListIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaAccountListIndex.setStatus(_A)
_HpnicfIpaAccountListIpAddr_Type=IpAddress
_HpnicfIpaAccountListIpAddr_Object=MibTableColumn
hpnicfIpaAccountListIpAddr=_HpnicfIpaAccountListIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,3,1,2),_HpnicfIpaAccountListIpAddr_Type())
hpnicfIpaAccountListIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIpaAccountListIpAddr.setStatus(_A)
_HpnicfIpaAccountListIpMask_Type=IpAddress
_HpnicfIpaAccountListIpMask_Object=MibTableColumn
hpnicfIpaAccountListIpMask=_HpnicfIpaAccountListIpMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,3,1,3),_HpnicfIpaAccountListIpMask_Type())
hpnicfIpaAccountListIpMask.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIpaAccountListIpMask.setStatus(_A)
_HpnicfIpaAccountListRowStatus_Type=RowStatus
_HpnicfIpaAccountListRowStatus_Object=MibTableColumn
hpnicfIpaAccountListRowStatus=_HpnicfIpaAccountListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,3,1,4),_HpnicfIpaAccountListRowStatus_Type())
hpnicfIpaAccountListRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIpaAccountListRowStatus.setStatus(_A)
_HpnicfIpaIntListTable_Object=MibTable
hpnicfIpaIntListTable=_HpnicfIpaIntListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4))
if mibBuilder.loadTexts:hpnicfIpaIntListTable.setStatus(_A)
_HpnicfIpaIntListEntry_Object=MibTableRow
hpnicfIpaIntListEntry=_HpnicfIpaIntListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1))
hpnicfIpaIntListEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:hpnicfIpaIntListEntry.setStatus(_A)
_HpnicfIpaIntListIpSrc_Type=IpAddress
_HpnicfIpaIntListIpSrc_Object=MibTableColumn
hpnicfIpaIntListIpSrc=_HpnicfIpaIntListIpSrc_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,1),_HpnicfIpaIntListIpSrc_Type())
hpnicfIpaIntListIpSrc.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaIntListIpSrc.setStatus(_A)
_HpnicfIpaIntListIpDst_Type=IpAddress
_HpnicfIpaIntListIpDst_Object=MibTableColumn
hpnicfIpaIntListIpDst=_HpnicfIpaIntListIpDst_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,2),_HpnicfIpaIntListIpDst_Type())
hpnicfIpaIntListIpDst.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaIntListIpDst.setStatus(_A)
class _HpnicfIpaIntListProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfIpaIntListProtocol_Type.__name__=_C
_HpnicfIpaIntListProtocol_Object=MibTableColumn
hpnicfIpaIntListProtocol=_HpnicfIpaIntListProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,3),_HpnicfIpaIntListProtocol_Type())
hpnicfIpaIntListProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaIntListProtocol.setStatus(_A)
_HpnicfIpaIntListInPackets_Type=Counter32
_HpnicfIpaIntListInPackets_Object=MibTableColumn
hpnicfIpaIntListInPackets=_HpnicfIpaIntListInPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,4),_HpnicfIpaIntListInPackets_Type())
hpnicfIpaIntListInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaIntListInPackets.setStatus(_A)
_HpnicfIpaIntListInBytes_Type=Counter64
_HpnicfIpaIntListInBytes_Object=MibTableColumn
hpnicfIpaIntListInBytes=_HpnicfIpaIntListInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,5),_HpnicfIpaIntListInBytes_Type())
hpnicfIpaIntListInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaIntListInBytes.setStatus(_A)
_HpnicfIpaIntListOutPackets_Type=Counter32
_HpnicfIpaIntListOutPackets_Object=MibTableColumn
hpnicfIpaIntListOutPackets=_HpnicfIpaIntListOutPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,6),_HpnicfIpaIntListOutPackets_Type())
hpnicfIpaIntListOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaIntListOutPackets.setStatus(_A)
_HpnicfIpaIntListOutBytes_Type=Counter64
_HpnicfIpaIntListOutBytes_Object=MibTableColumn
hpnicfIpaIntListOutBytes=_HpnicfIpaIntListOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,4,1,7),_HpnicfIpaIntListOutBytes_Type())
hpnicfIpaIntListOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaIntListOutBytes.setStatus(_A)
_HpnicfIpaExtListTable_Object=MibTable
hpnicfIpaExtListTable=_HpnicfIpaExtListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5))
if mibBuilder.loadTexts:hpnicfIpaExtListTable.setStatus(_A)
_HpnicfIpaExtListEntry_Object=MibTableRow
hpnicfIpaExtListEntry=_HpnicfIpaExtListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1))
hpnicfIpaExtListEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:hpnicfIpaExtListEntry.setStatus(_A)
_HpnicfIpaExtListIpSrc_Type=IpAddress
_HpnicfIpaExtListIpSrc_Object=MibTableColumn
hpnicfIpaExtListIpSrc=_HpnicfIpaExtListIpSrc_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,1),_HpnicfIpaExtListIpSrc_Type())
hpnicfIpaExtListIpSrc.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaExtListIpSrc.setStatus(_A)
_HpnicfIpaExtListIpDst_Type=IpAddress
_HpnicfIpaExtListIpDst_Object=MibTableColumn
hpnicfIpaExtListIpDst=_HpnicfIpaExtListIpDst_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,2),_HpnicfIpaExtListIpDst_Type())
hpnicfIpaExtListIpDst.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaExtListIpDst.setStatus(_A)
class _HpnicfIpaExtListProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfIpaExtListProtocol_Type.__name__=_C
_HpnicfIpaExtListProtocol_Object=MibTableColumn
hpnicfIpaExtListProtocol=_HpnicfIpaExtListProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,3),_HpnicfIpaExtListProtocol_Type())
hpnicfIpaExtListProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaExtListProtocol.setStatus(_A)
_HpnicfIpaExtListInPackets_Type=Counter32
_HpnicfIpaExtListInPackets_Object=MibTableColumn
hpnicfIpaExtListInPackets=_HpnicfIpaExtListInPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,4),_HpnicfIpaExtListInPackets_Type())
hpnicfIpaExtListInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaExtListInPackets.setStatus(_A)
_HpnicfIpaExtListInBytes_Type=Counter64
_HpnicfIpaExtListInBytes_Object=MibTableColumn
hpnicfIpaExtListInBytes=_HpnicfIpaExtListInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,5),_HpnicfIpaExtListInBytes_Type())
hpnicfIpaExtListInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaExtListInBytes.setStatus(_A)
_HpnicfIpaExtListOutPackets_Type=Counter32
_HpnicfIpaExtListOutPackets_Object=MibTableColumn
hpnicfIpaExtListOutPackets=_HpnicfIpaExtListOutPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,6),_HpnicfIpaExtListOutPackets_Type())
hpnicfIpaExtListOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaExtListOutPackets.setStatus(_A)
_HpnicfIpaExtListOutBytes_Type=Counter64
_HpnicfIpaExtListOutBytes_Object=MibTableColumn
hpnicfIpaExtListOutBytes=_HpnicfIpaExtListOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,5,1,7),_HpnicfIpaExtListOutBytes_Type())
hpnicfIpaExtListOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaExtListOutBytes.setStatus(_A)
_HpnicfIpaFWListTable_Object=MibTable
hpnicfIpaFWListTable=_HpnicfIpaFWListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6))
if mibBuilder.loadTexts:hpnicfIpaFWListTable.setStatus(_A)
_HpnicfIpaFWListEntry_Object=MibTableRow
hpnicfIpaFWListEntry=_HpnicfIpaFWListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1))
hpnicfIpaFWListEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:hpnicfIpaFWListEntry.setStatus(_A)
_HpnicfIpaFWListIpSrc_Type=IpAddress
_HpnicfIpaFWListIpSrc_Object=MibTableColumn
hpnicfIpaFWListIpSrc=_HpnicfIpaFWListIpSrc_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1,1),_HpnicfIpaFWListIpSrc_Type())
hpnicfIpaFWListIpSrc.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaFWListIpSrc.setStatus(_A)
_HpnicfIpaFWListIpDst_Type=IpAddress
_HpnicfIpaFWListIpDst_Object=MibTableColumn
hpnicfIpaFWListIpDst=_HpnicfIpaFWListIpDst_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1,2),_HpnicfIpaFWListIpDst_Type())
hpnicfIpaFWListIpDst.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpaFWListIpDst.setStatus(_A)
_HpnicfIpaFWListInPackets_Type=Counter32
_HpnicfIpaFWListInPackets_Object=MibTableColumn
hpnicfIpaFWListInPackets=_HpnicfIpaFWListInPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1,3),_HpnicfIpaFWListInPackets_Type())
hpnicfIpaFWListInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaFWListInPackets.setStatus(_A)
_HpnicfIpaFWListInBytes_Type=Counter64
_HpnicfIpaFWListInBytes_Object=MibTableColumn
hpnicfIpaFWListInBytes=_HpnicfIpaFWListInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1,4),_HpnicfIpaFWListInBytes_Type())
hpnicfIpaFWListInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaFWListInBytes.setStatus(_A)
_HpnicfIpaFWListOutPackets_Type=Counter32
_HpnicfIpaFWListOutPackets_Object=MibTableColumn
hpnicfIpaFWListOutPackets=_HpnicfIpaFWListOutPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1,5),_HpnicfIpaFWListOutPackets_Type())
hpnicfIpaFWListOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaFWListOutPackets.setStatus(_A)
_HpnicfIpaFWListOutBytes_Type=Counter64
_HpnicfIpaFWListOutBytes_Object=MibTableColumn
hpnicfIpaFWListOutBytes=_HpnicfIpaFWListOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,25,6,1,6),_HpnicfIpaFWListOutBytes_Type())
hpnicfIpaFWListOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpaFWListOutBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'InterfaceIndex':InterfaceIndex,'hpnicfIpa':hpnicfIpa,'hpnicfIpaGlobalStats':hpnicfIpaGlobalStats,'hpnicfIpaGlobalEnable':hpnicfIpaGlobalEnable,'hpnicfIpaTimeOutSeconds':hpnicfIpaTimeOutSeconds,'hpnicfIpaIntListMaxItemNum':hpnicfIpaIntListMaxItemNum,'hpnicfIpaExtListMaxItemNum':hpnicfIpaExtListMaxItemNum,'hpnicfIpaFWListMaxItemNum':hpnicfIpaFWListMaxItemNum,'hpnicfIpaAccountListMaxItemNum':hpnicfIpaAccountListMaxItemNum,'hpnicfIpaAccountListNextIndex':hpnicfIpaAccountListNextIndex,'hpnicfIpaListCleaningFlag':hpnicfIpaListCleaningFlag,'hpnicfIpaIfConfigTable':hpnicfIpaIfConfigTable,'hpnicfIpaIfConfigEntry':hpnicfIpaIfConfigEntry,_J:hpnicfIpaIfConfigIfIndex,'hpnicfIpaIfConfigInEnable':hpnicfIpaIfConfigInEnable,'hpnicfIpaIfConfigOutEnable':hpnicfIpaIfConfigOutEnable,'hpnicfIpaIfConfigFWEnable':hpnicfIpaIfConfigFWEnable,'hpnicfIpaAccountListTable':hpnicfIpaAccountListTable,'hpnicfIpaAccountListEntry':hpnicfIpaAccountListEntry,_K:hpnicfIpaAccountListIndex,'hpnicfIpaAccountListIpAddr':hpnicfIpaAccountListIpAddr,'hpnicfIpaAccountListIpMask':hpnicfIpaAccountListIpMask,'hpnicfIpaAccountListRowStatus':hpnicfIpaAccountListRowStatus,'hpnicfIpaIntListTable':hpnicfIpaIntListTable,'hpnicfIpaIntListEntry':hpnicfIpaIntListEntry,_L:hpnicfIpaIntListIpSrc,_M:hpnicfIpaIntListIpDst,_N:hpnicfIpaIntListProtocol,'hpnicfIpaIntListInPackets':hpnicfIpaIntListInPackets,'hpnicfIpaIntListInBytes':hpnicfIpaIntListInBytes,'hpnicfIpaIntListOutPackets':hpnicfIpaIntListOutPackets,'hpnicfIpaIntListOutBytes':hpnicfIpaIntListOutBytes,'hpnicfIpaExtListTable':hpnicfIpaExtListTable,'hpnicfIpaExtListEntry':hpnicfIpaExtListEntry,_O:hpnicfIpaExtListIpSrc,_P:hpnicfIpaExtListIpDst,_Q:hpnicfIpaExtListProtocol,'hpnicfIpaExtListInPackets':hpnicfIpaExtListInPackets,'hpnicfIpaExtListInBytes':hpnicfIpaExtListInBytes,'hpnicfIpaExtListOutPackets':hpnicfIpaExtListOutPackets,'hpnicfIpaExtListOutBytes':hpnicfIpaExtListOutBytes,'hpnicfIpaFWListTable':hpnicfIpaFWListTable,'hpnicfIpaFWListEntry':hpnicfIpaFWListEntry,_R:hpnicfIpaFWListIpSrc,_S:hpnicfIpaFWListIpDst,'hpnicfIpaFWListInPackets':hpnicfIpaFWListInPackets,'hpnicfIpaFWListInBytes':hpnicfIpaFWListInBytes,'hpnicfIpaFWListOutPackets':hpnicfIpaFWListOutPackets,'hpnicfIpaFWListOutBytes':hpnicfIpaFWListOutBytes})