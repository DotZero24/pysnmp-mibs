_S='h3cIpaFWListIpDst'
_R='h3cIpaFWListIpSrc'
_Q='h3cIpaExtListProtocol'
_P='h3cIpaExtListIpDst'
_O='h3cIpaExtListIpSrc'
_N='h3cIpaIntListProtocol'
_M='h3cIpaIntListIpDst'
_L='h3cIpaIntListIpSrc'
_K='h3cIpaAccountListIndex'
_J='h3cIpaIfConfigIfIndex'
_I='read-create'
_H='enabled'
_G='disabled'
_F='read-write'
_E='not-accessible'
_D='A3COM-HUAWEI-IPA-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cIpa=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,25))
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpaGlobalStats_ObjectIdentity=ObjectIdentity
h3cIpaGlobalStats=_H3cIpaGlobalStats_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,25,1))
class _H3cIpaGlobalEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cIpaGlobalEnable_Type.__name__=_C
_H3cIpaGlobalEnable_Object=MibScalar
h3cIpaGlobalEnable=_H3cIpaGlobalEnable_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,1),_H3cIpaGlobalEnable_Type())
h3cIpaGlobalEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaGlobalEnable.setStatus(_A)
class _H3cIpaTimeOutSeconds_Type(Integer32):defaultValue=43200
_H3cIpaTimeOutSeconds_Type.__name__=_C
_H3cIpaTimeOutSeconds_Object=MibScalar
h3cIpaTimeOutSeconds=_H3cIpaTimeOutSeconds_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,2),_H3cIpaTimeOutSeconds_Type())
h3cIpaTimeOutSeconds.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaTimeOutSeconds.setStatus(_A)
class _H3cIpaIntListMaxItemNum_Type(Integer32):defaultValue=512
_H3cIpaIntListMaxItemNum_Type.__name__=_C
_H3cIpaIntListMaxItemNum_Object=MibScalar
h3cIpaIntListMaxItemNum=_H3cIpaIntListMaxItemNum_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,3),_H3cIpaIntListMaxItemNum_Type())
h3cIpaIntListMaxItemNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaIntListMaxItemNum.setStatus(_A)
class _H3cIpaExtListMaxItemNum_Type(Integer32):defaultValue=0
_H3cIpaExtListMaxItemNum_Type.__name__=_C
_H3cIpaExtListMaxItemNum_Object=MibScalar
h3cIpaExtListMaxItemNum=_H3cIpaExtListMaxItemNum_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,4),_H3cIpaExtListMaxItemNum_Type())
h3cIpaExtListMaxItemNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaExtListMaxItemNum.setStatus(_A)
_H3cIpaFWListMaxItemNum_Type=Integer32
_H3cIpaFWListMaxItemNum_Object=MibScalar
h3cIpaFWListMaxItemNum=_H3cIpaFWListMaxItemNum_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,5),_H3cIpaFWListMaxItemNum_Type())
h3cIpaFWListMaxItemNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaFWListMaxItemNum.setStatus(_A)
_H3cIpaAccountListMaxItemNum_Type=Integer32
_H3cIpaAccountListMaxItemNum_Object=MibScalar
h3cIpaAccountListMaxItemNum=_H3cIpaAccountListMaxItemNum_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,6),_H3cIpaAccountListMaxItemNum_Type())
h3cIpaAccountListMaxItemNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaAccountListMaxItemNum.setStatus(_A)
_H3cIpaAccountListNextIndex_Type=Integer32
_H3cIpaAccountListNextIndex_Object=MibScalar
h3cIpaAccountListNextIndex=_H3cIpaAccountListNextIndex_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,7),_H3cIpaAccountListNextIndex_Type())
h3cIpaAccountListNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaAccountListNextIndex.setStatus(_A)
class _H3cIpaListCleaningFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('cleaningAll',2),('cleaningIntList',3),('cleaningExtList',4),('cleaningFWList',5)))
_H3cIpaListCleaningFlag_Type.__name__=_C
_H3cIpaListCleaningFlag_Object=MibScalar
h3cIpaListCleaningFlag=_H3cIpaListCleaningFlag_Object((1,3,6,1,4,1,43,45,1,10,2,25,1,8),_H3cIpaListCleaningFlag_Type())
h3cIpaListCleaningFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaListCleaningFlag.setStatus(_A)
_H3cIpaIfConfigTable_Object=MibTable
h3cIpaIfConfigTable=_H3cIpaIfConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,25,2))
if mibBuilder.loadTexts:h3cIpaIfConfigTable.setStatus(_A)
_H3cIpaIfConfigEntry_Object=MibTableRow
h3cIpaIfConfigEntry=_H3cIpaIfConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,25,2,1))
h3cIpaIfConfigEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:h3cIpaIfConfigEntry.setStatus(_A)
_H3cIpaIfConfigIfIndex_Type=InterfaceIndex
_H3cIpaIfConfigIfIndex_Object=MibTableColumn
h3cIpaIfConfigIfIndex=_H3cIpaIfConfigIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,25,2,1,1),_H3cIpaIfConfigIfIndex_Type())
h3cIpaIfConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaIfConfigIfIndex.setStatus(_A)
class _H3cIpaIfConfigInEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cIpaIfConfigInEnable_Type.__name__=_C
_H3cIpaIfConfigInEnable_Object=MibTableColumn
h3cIpaIfConfigInEnable=_H3cIpaIfConfigInEnable_Object((1,3,6,1,4,1,43,45,1,10,2,25,2,1,2),_H3cIpaIfConfigInEnable_Type())
h3cIpaIfConfigInEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaIfConfigInEnable.setStatus(_A)
class _H3cIpaIfConfigOutEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cIpaIfConfigOutEnable_Type.__name__=_C
_H3cIpaIfConfigOutEnable_Object=MibTableColumn
h3cIpaIfConfigOutEnable=_H3cIpaIfConfigOutEnable_Object((1,3,6,1,4,1,43,45,1,10,2,25,2,1,3),_H3cIpaIfConfigOutEnable_Type())
h3cIpaIfConfigOutEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaIfConfigOutEnable.setStatus(_A)
class _H3cIpaIfConfigFWEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nodirection',1),('inbound',2),('outbound',3),('bidirection',4)))
_H3cIpaIfConfigFWEnable_Type.__name__=_C
_H3cIpaIfConfigFWEnable_Object=MibTableColumn
h3cIpaIfConfigFWEnable=_H3cIpaIfConfigFWEnable_Object((1,3,6,1,4,1,43,45,1,10,2,25,2,1,4),_H3cIpaIfConfigFWEnable_Type())
h3cIpaIfConfigFWEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpaIfConfigFWEnable.setStatus(_A)
_H3cIpaAccountListTable_Object=MibTable
h3cIpaAccountListTable=_H3cIpaAccountListTable_Object((1,3,6,1,4,1,43,45,1,10,2,25,3))
if mibBuilder.loadTexts:h3cIpaAccountListTable.setStatus(_A)
_H3cIpaAccountListEntry_Object=MibTableRow
h3cIpaAccountListEntry=_H3cIpaAccountListEntry_Object((1,3,6,1,4,1,43,45,1,10,2,25,3,1))
h3cIpaAccountListEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:h3cIpaAccountListEntry.setStatus(_A)
class _H3cIpaAccountListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpaAccountListIndex_Type.__name__=_C
_H3cIpaAccountListIndex_Object=MibTableColumn
h3cIpaAccountListIndex=_H3cIpaAccountListIndex_Object((1,3,6,1,4,1,43,45,1,10,2,25,3,1,1),_H3cIpaAccountListIndex_Type())
h3cIpaAccountListIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaAccountListIndex.setStatus(_A)
_H3cIpaAccountListIpAddr_Type=IpAddress
_H3cIpaAccountListIpAddr_Object=MibTableColumn
h3cIpaAccountListIpAddr=_H3cIpaAccountListIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,25,3,1,2),_H3cIpaAccountListIpAddr_Type())
h3cIpaAccountListIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cIpaAccountListIpAddr.setStatus(_A)
_H3cIpaAccountListIpMask_Type=IpAddress
_H3cIpaAccountListIpMask_Object=MibTableColumn
h3cIpaAccountListIpMask=_H3cIpaAccountListIpMask_Object((1,3,6,1,4,1,43,45,1,10,2,25,3,1,3),_H3cIpaAccountListIpMask_Type())
h3cIpaAccountListIpMask.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cIpaAccountListIpMask.setStatus(_A)
_H3cIpaAccountListRowStatus_Type=RowStatus
_H3cIpaAccountListRowStatus_Object=MibTableColumn
h3cIpaAccountListRowStatus=_H3cIpaAccountListRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,25,3,1,4),_H3cIpaAccountListRowStatus_Type())
h3cIpaAccountListRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cIpaAccountListRowStatus.setStatus(_A)
_H3cIpaIntListTable_Object=MibTable
h3cIpaIntListTable=_H3cIpaIntListTable_Object((1,3,6,1,4,1,43,45,1,10,2,25,4))
if mibBuilder.loadTexts:h3cIpaIntListTable.setStatus(_A)
_H3cIpaIntListEntry_Object=MibTableRow
h3cIpaIntListEntry=_H3cIpaIntListEntry_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1))
h3cIpaIntListEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:h3cIpaIntListEntry.setStatus(_A)
_H3cIpaIntListIpSrc_Type=IpAddress
_H3cIpaIntListIpSrc_Object=MibTableColumn
h3cIpaIntListIpSrc=_H3cIpaIntListIpSrc_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,1),_H3cIpaIntListIpSrc_Type())
h3cIpaIntListIpSrc.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaIntListIpSrc.setStatus(_A)
_H3cIpaIntListIpDst_Type=IpAddress
_H3cIpaIntListIpDst_Object=MibTableColumn
h3cIpaIntListIpDst=_H3cIpaIntListIpDst_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,2),_H3cIpaIntListIpDst_Type())
h3cIpaIntListIpDst.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaIntListIpDst.setStatus(_A)
class _H3cIpaIntListProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cIpaIntListProtocol_Type.__name__=_C
_H3cIpaIntListProtocol_Object=MibTableColumn
h3cIpaIntListProtocol=_H3cIpaIntListProtocol_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,3),_H3cIpaIntListProtocol_Type())
h3cIpaIntListProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaIntListProtocol.setStatus(_A)
_H3cIpaIntListInPackets_Type=Counter32
_H3cIpaIntListInPackets_Object=MibTableColumn
h3cIpaIntListInPackets=_H3cIpaIntListInPackets_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,4),_H3cIpaIntListInPackets_Type())
h3cIpaIntListInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaIntListInPackets.setStatus(_A)
_H3cIpaIntListInBytes_Type=Counter64
_H3cIpaIntListInBytes_Object=MibTableColumn
h3cIpaIntListInBytes=_H3cIpaIntListInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,5),_H3cIpaIntListInBytes_Type())
h3cIpaIntListInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaIntListInBytes.setStatus(_A)
_H3cIpaIntListOutPackets_Type=Counter32
_H3cIpaIntListOutPackets_Object=MibTableColumn
h3cIpaIntListOutPackets=_H3cIpaIntListOutPackets_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,6),_H3cIpaIntListOutPackets_Type())
h3cIpaIntListOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaIntListOutPackets.setStatus(_A)
_H3cIpaIntListOutBytes_Type=Counter64
_H3cIpaIntListOutBytes_Object=MibTableColumn
h3cIpaIntListOutBytes=_H3cIpaIntListOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,25,4,1,7),_H3cIpaIntListOutBytes_Type())
h3cIpaIntListOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaIntListOutBytes.setStatus(_A)
_H3cIpaExtListTable_Object=MibTable
h3cIpaExtListTable=_H3cIpaExtListTable_Object((1,3,6,1,4,1,43,45,1,10,2,25,5))
if mibBuilder.loadTexts:h3cIpaExtListTable.setStatus(_A)
_H3cIpaExtListEntry_Object=MibTableRow
h3cIpaExtListEntry=_H3cIpaExtListEntry_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1))
h3cIpaExtListEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:h3cIpaExtListEntry.setStatus(_A)
_H3cIpaExtListIpSrc_Type=IpAddress
_H3cIpaExtListIpSrc_Object=MibTableColumn
h3cIpaExtListIpSrc=_H3cIpaExtListIpSrc_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,1),_H3cIpaExtListIpSrc_Type())
h3cIpaExtListIpSrc.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaExtListIpSrc.setStatus(_A)
_H3cIpaExtListIpDst_Type=IpAddress
_H3cIpaExtListIpDst_Object=MibTableColumn
h3cIpaExtListIpDst=_H3cIpaExtListIpDst_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,2),_H3cIpaExtListIpDst_Type())
h3cIpaExtListIpDst.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaExtListIpDst.setStatus(_A)
class _H3cIpaExtListProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cIpaExtListProtocol_Type.__name__=_C
_H3cIpaExtListProtocol_Object=MibTableColumn
h3cIpaExtListProtocol=_H3cIpaExtListProtocol_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,3),_H3cIpaExtListProtocol_Type())
h3cIpaExtListProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaExtListProtocol.setStatus(_A)
_H3cIpaExtListInPackets_Type=Counter32
_H3cIpaExtListInPackets_Object=MibTableColumn
h3cIpaExtListInPackets=_H3cIpaExtListInPackets_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,4),_H3cIpaExtListInPackets_Type())
h3cIpaExtListInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaExtListInPackets.setStatus(_A)
_H3cIpaExtListInBytes_Type=Counter64
_H3cIpaExtListInBytes_Object=MibTableColumn
h3cIpaExtListInBytes=_H3cIpaExtListInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,5),_H3cIpaExtListInBytes_Type())
h3cIpaExtListInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaExtListInBytes.setStatus(_A)
_H3cIpaExtListOutPackets_Type=Counter32
_H3cIpaExtListOutPackets_Object=MibTableColumn
h3cIpaExtListOutPackets=_H3cIpaExtListOutPackets_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,6),_H3cIpaExtListOutPackets_Type())
h3cIpaExtListOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaExtListOutPackets.setStatus(_A)
_H3cIpaExtListOutBytes_Type=Counter64
_H3cIpaExtListOutBytes_Object=MibTableColumn
h3cIpaExtListOutBytes=_H3cIpaExtListOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,25,5,1,7),_H3cIpaExtListOutBytes_Type())
h3cIpaExtListOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaExtListOutBytes.setStatus(_A)
_H3cIpaFWListTable_Object=MibTable
h3cIpaFWListTable=_H3cIpaFWListTable_Object((1,3,6,1,4,1,43,45,1,10,2,25,6))
if mibBuilder.loadTexts:h3cIpaFWListTable.setStatus(_A)
_H3cIpaFWListEntry_Object=MibTableRow
h3cIpaFWListEntry=_H3cIpaFWListEntry_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1))
h3cIpaFWListEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:h3cIpaFWListEntry.setStatus(_A)
_H3cIpaFWListIpSrc_Type=IpAddress
_H3cIpaFWListIpSrc_Object=MibTableColumn
h3cIpaFWListIpSrc=_H3cIpaFWListIpSrc_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1,1),_H3cIpaFWListIpSrc_Type())
h3cIpaFWListIpSrc.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaFWListIpSrc.setStatus(_A)
_H3cIpaFWListIpDst_Type=IpAddress
_H3cIpaFWListIpDst_Object=MibTableColumn
h3cIpaFWListIpDst=_H3cIpaFWListIpDst_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1,2),_H3cIpaFWListIpDst_Type())
h3cIpaFWListIpDst.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpaFWListIpDst.setStatus(_A)
_H3cIpaFWListInPackets_Type=Counter32
_H3cIpaFWListInPackets_Object=MibTableColumn
h3cIpaFWListInPackets=_H3cIpaFWListInPackets_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1,3),_H3cIpaFWListInPackets_Type())
h3cIpaFWListInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaFWListInPackets.setStatus(_A)
_H3cIpaFWListInBytes_Type=Counter64
_H3cIpaFWListInBytes_Object=MibTableColumn
h3cIpaFWListInBytes=_H3cIpaFWListInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1,4),_H3cIpaFWListInBytes_Type())
h3cIpaFWListInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaFWListInBytes.setStatus(_A)
_H3cIpaFWListOutPackets_Type=Counter32
_H3cIpaFWListOutPackets_Object=MibTableColumn
h3cIpaFWListOutPackets=_H3cIpaFWListOutPackets_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1,5),_H3cIpaFWListOutPackets_Type())
h3cIpaFWListOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaFWListOutPackets.setStatus(_A)
_H3cIpaFWListOutBytes_Type=Counter64
_H3cIpaFWListOutBytes_Object=MibTableColumn
h3cIpaFWListOutBytes=_H3cIpaFWListOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,25,6,1,6),_H3cIpaFWListOutBytes_Type())
h3cIpaFWListOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpaFWListOutBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'InterfaceIndex':InterfaceIndex,'h3cIpa':h3cIpa,'h3cIpaGlobalStats':h3cIpaGlobalStats,'h3cIpaGlobalEnable':h3cIpaGlobalEnable,'h3cIpaTimeOutSeconds':h3cIpaTimeOutSeconds,'h3cIpaIntListMaxItemNum':h3cIpaIntListMaxItemNum,'h3cIpaExtListMaxItemNum':h3cIpaExtListMaxItemNum,'h3cIpaFWListMaxItemNum':h3cIpaFWListMaxItemNum,'h3cIpaAccountListMaxItemNum':h3cIpaAccountListMaxItemNum,'h3cIpaAccountListNextIndex':h3cIpaAccountListNextIndex,'h3cIpaListCleaningFlag':h3cIpaListCleaningFlag,'h3cIpaIfConfigTable':h3cIpaIfConfigTable,'h3cIpaIfConfigEntry':h3cIpaIfConfigEntry,_J:h3cIpaIfConfigIfIndex,'h3cIpaIfConfigInEnable':h3cIpaIfConfigInEnable,'h3cIpaIfConfigOutEnable':h3cIpaIfConfigOutEnable,'h3cIpaIfConfigFWEnable':h3cIpaIfConfigFWEnable,'h3cIpaAccountListTable':h3cIpaAccountListTable,'h3cIpaAccountListEntry':h3cIpaAccountListEntry,_K:h3cIpaAccountListIndex,'h3cIpaAccountListIpAddr':h3cIpaAccountListIpAddr,'h3cIpaAccountListIpMask':h3cIpaAccountListIpMask,'h3cIpaAccountListRowStatus':h3cIpaAccountListRowStatus,'h3cIpaIntListTable':h3cIpaIntListTable,'h3cIpaIntListEntry':h3cIpaIntListEntry,_L:h3cIpaIntListIpSrc,_M:h3cIpaIntListIpDst,_N:h3cIpaIntListProtocol,'h3cIpaIntListInPackets':h3cIpaIntListInPackets,'h3cIpaIntListInBytes':h3cIpaIntListInBytes,'h3cIpaIntListOutPackets':h3cIpaIntListOutPackets,'h3cIpaIntListOutBytes':h3cIpaIntListOutBytes,'h3cIpaExtListTable':h3cIpaExtListTable,'h3cIpaExtListEntry':h3cIpaExtListEntry,_O:h3cIpaExtListIpSrc,_P:h3cIpaExtListIpDst,_Q:h3cIpaExtListProtocol,'h3cIpaExtListInPackets':h3cIpaExtListInPackets,'h3cIpaExtListInBytes':h3cIpaExtListInBytes,'h3cIpaExtListOutPackets':h3cIpaExtListOutPackets,'h3cIpaExtListOutBytes':h3cIpaExtListOutBytes,'h3cIpaFWListTable':h3cIpaFWListTable,'h3cIpaFWListEntry':h3cIpaFWListEntry,_R:h3cIpaFWListIpSrc,_S:h3cIpaFWListIpDst,'h3cIpaFWListInPackets':h3cIpaFWListInPackets,'h3cIpaFWListInBytes':h3cIpaFWListInBytes,'h3cIpaFWListOutPackets':h3cIpaFWListOutPackets,'h3cIpaFWListOutBytes':h3cIpaFWListOutBytes})