_U='mpGtsATMCfgRowIndex'
_T='mpGtsATMCfgVCI'
_S='mpGtsATMCfgVPI'
_R='mpGtsFRCfgRowIndex'
_Q='mpGtsFRCfgDLCI'
_P='packets'
_O='bits/second'
_N='accessList'
_M='all'
_L='mpGtsIFCfgRowIndex'
_K='DisplayString'
_J='Unsigned32'
_I='bits'
_H='not-accessible'
_G='ifIndex'
_F='Integer32'
_E='Octets'
_D='Packets'
_C='MAIPU-GTS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
maipuGtsMIB=ModuleIdentity((1,3,6,1,4,1,5651,6,2,3,5))
class Unsigned64(TextualConvention,Counter64):status=_A
_Maipu_ObjectIdentity=ObjectIdentity
maipu=_Maipu_ObjectIdentity((1,3,6,1,4,1,5651))
_MpMgmt2_ObjectIdentity=ObjectIdentity
mpMgmt2=_MpMgmt2_ObjectIdentity((1,3,6,1,4,1,5651,6))
_MpRouterTech_ObjectIdentity=ObjectIdentity
mpRouterTech=_MpRouterTech_ObjectIdentity((1,3,6,1,4,1,5651,6,2))
_MpRtQoSv2_ObjectIdentity=ObjectIdentity
mpRtQoSv2=_MpRtQoSv2_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3))
_MaipuGtsMIBObjects_ObjectIdentity=ObjectIdentity
maipuGtsMIBObjects=_MaipuGtsMIBObjects_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,5,1))
_MpGtsConfigs_ObjectIdentity=ObjectIdentity
mpGtsConfigs=_MpGtsConfigs_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,5,1,1))
_MpGtsInterfaceCfgTable_Object=MibTable
mpGtsInterfaceCfgTable=_MpGtsInterfaceCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1))
if mibBuilder.loadTexts:mpGtsInterfaceCfgTable.setStatus(_A)
_MpGtsInterfaceCfgEntry_Object=MibTableRow
mpGtsInterfaceCfgEntry=_MpGtsInterfaceCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1))
mpGtsInterfaceCfgEntry.setIndexNames((0,_C,_G),(0,_C,_L))
if mibBuilder.loadTexts:mpGtsInterfaceCfgEntry.setStatus(_A)
class _MpGtsIFCfgRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpGtsIFCfgRowIndex_Type.__name__=_F
_MpGtsIFCfgRowIndex_Object=MibTableColumn
mpGtsIFCfgRowIndex=_MpGtsIFCfgRowIndex_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,1),_MpGtsIFCfgRowIndex_Type())
mpGtsIFCfgRowIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mpGtsIFCfgRowIndex.setStatus(_A)
class _MpGtsIFCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_MpGtsIFCfgType_Type.__name__=_F
_MpGtsIFCfgType_Object=MibTableColumn
mpGtsIFCfgType=_MpGtsIFCfgType_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,2),_MpGtsIFCfgType_Type())
mpGtsIFCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFCfgType.setStatus(_A)
class _MpGtsIFCfgAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpGtsIFCfgAclName_Type.__name__=_K
_MpGtsIFCfgAclName_Object=MibTableColumn
mpGtsIFCfgAclName=_MpGtsIFCfgAclName_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,3),_MpGtsIFCfgAclName_Type())
mpGtsIFCfgAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFCfgAclName.setStatus(_A)
_MpGtsIFCfgRate64_Type=Unsigned64
_MpGtsIFCfgRate64_Object=MibTableColumn
mpGtsIFCfgRate64=_MpGtsIFCfgRate64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,4),_MpGtsIFCfgRate64_Type())
mpGtsIFCfgRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFCfgRate64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFCfgRate64.setUnits(_O)
_MpGtsIFCfgBurstSize_Type=Unsigned32
_MpGtsIFCfgBurstSize_Object=MibTableColumn
mpGtsIFCfgBurstSize=_MpGtsIFCfgBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,5),_MpGtsIFCfgBurstSize_Type())
mpGtsIFCfgBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFCfgBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFCfgBurstSize.setUnits(_I)
_MpGtsIFCfgExtBurstSize_Type=Unsigned32
_MpGtsIFCfgExtBurstSize_Object=MibTableColumn
mpGtsIFCfgExtBurstSize=_MpGtsIFCfgExtBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,6),_MpGtsIFCfgExtBurstSize_Type())
mpGtsIFCfgExtBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFCfgExtBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFCfgExtBurstSize.setUnits(_I)
_MpGtsIFCfgQueueLimit_Type=Unsigned32
_MpGtsIFCfgQueueLimit_Object=MibTableColumn
mpGtsIFCfgQueueLimit=_MpGtsIFCfgQueueLimit_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,1,1,7),_MpGtsIFCfgQueueLimit_Type())
mpGtsIFCfgQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFCfgQueueLimit.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFCfgQueueLimit.setUnits(_P)
_MpGtsFrameRelayVCCfgTable_Object=MibTable
mpGtsFrameRelayVCCfgTable=_MpGtsFrameRelayVCCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2))
if mibBuilder.loadTexts:mpGtsFrameRelayVCCfgTable.setStatus(_A)
_MpGtsFrameRelayVCCfgEntry_Object=MibTableRow
mpGtsFrameRelayVCCfgEntry=_MpGtsFrameRelayVCCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1))
mpGtsFrameRelayVCCfgEntry.setIndexNames((0,_C,_G),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:mpGtsFrameRelayVCCfgEntry.setStatus(_A)
class _MpGtsFRCfgDLCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1007))
_MpGtsFRCfgDLCI_Type.__name__=_J
_MpGtsFRCfgDLCI_Object=MibTableColumn
mpGtsFRCfgDLCI=_MpGtsFRCfgDLCI_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,1),_MpGtsFRCfgDLCI_Type())
mpGtsFRCfgDLCI.setMaxAccess(_H)
if mibBuilder.loadTexts:mpGtsFRCfgDLCI.setStatus(_A)
class _MpGtsFRCfgRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpGtsFRCfgRowIndex_Type.__name__=_F
_MpGtsFRCfgRowIndex_Object=MibTableColumn
mpGtsFRCfgRowIndex=_MpGtsFRCfgRowIndex_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,2),_MpGtsFRCfgRowIndex_Type())
mpGtsFRCfgRowIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mpGtsFRCfgRowIndex.setStatus(_A)
class _MpGtsFRCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_MpGtsFRCfgType_Type.__name__=_F
_MpGtsFRCfgType_Object=MibTableColumn
mpGtsFRCfgType=_MpGtsFRCfgType_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,3),_MpGtsFRCfgType_Type())
mpGtsFRCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRCfgType.setStatus(_A)
class _MpGtsFRCfgAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpGtsFRCfgAclName_Type.__name__=_K
_MpGtsFRCfgAclName_Object=MibTableColumn
mpGtsFRCfgAclName=_MpGtsFRCfgAclName_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,4),_MpGtsFRCfgAclName_Type())
mpGtsFRCfgAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRCfgAclName.setStatus(_A)
_MpGtsFRCfgRate64_Type=Unsigned64
_MpGtsFRCfgRate64_Object=MibTableColumn
mpGtsFRCfgRate64=_MpGtsFRCfgRate64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,5),_MpGtsFRCfgRate64_Type())
mpGtsFRCfgRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRCfgRate64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRCfgRate64.setUnits(_O)
_MpGtsFRCfgBurstSize_Type=Unsigned32
_MpGtsFRCfgBurstSize_Object=MibTableColumn
mpGtsFRCfgBurstSize=_MpGtsFRCfgBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,6),_MpGtsFRCfgBurstSize_Type())
mpGtsFRCfgBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRCfgBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRCfgBurstSize.setUnits(_I)
_MpGtsFRCfgExtBurstSize_Type=Unsigned32
_MpGtsFRCfgExtBurstSize_Object=MibTableColumn
mpGtsFRCfgExtBurstSize=_MpGtsFRCfgExtBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,7),_MpGtsFRCfgExtBurstSize_Type())
mpGtsFRCfgExtBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRCfgExtBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRCfgExtBurstSize.setUnits(_I)
_MpGtsFRCfgQueueLimit_Type=Unsigned32
_MpGtsFRCfgQueueLimit_Object=MibTableColumn
mpGtsFRCfgQueueLimit=_MpGtsFRCfgQueueLimit_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,2,1,8),_MpGtsFRCfgQueueLimit_Type())
mpGtsFRCfgQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRCfgQueueLimit.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRCfgQueueLimit.setUnits(_P)
_MpGtsATMPVCCfgTable_Object=MibTable
mpGtsATMPVCCfgTable=_MpGtsATMPVCCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3))
if mibBuilder.loadTexts:mpGtsATMPVCCfgTable.setStatus(_A)
_MpGtsATMPVCCfgEntry_Object=MibTableRow
mpGtsATMPVCCfgEntry=_MpGtsATMPVCCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1))
mpGtsATMPVCCfgEntry.setIndexNames((0,_C,_G),(0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:mpGtsATMPVCCfgEntry.setStatus(_A)
class _MpGtsATMCfgVPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpGtsATMCfgVPI_Type.__name__=_J
_MpGtsATMCfgVPI_Object=MibTableColumn
mpGtsATMCfgVPI=_MpGtsATMCfgVPI_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,1),_MpGtsATMCfgVPI_Type())
mpGtsATMCfgVPI.setMaxAccess(_H)
if mibBuilder.loadTexts:mpGtsATMCfgVPI.setStatus(_A)
class _MpGtsATMCfgVCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpGtsATMCfgVCI_Type.__name__=_J
_MpGtsATMCfgVCI_Object=MibTableColumn
mpGtsATMCfgVCI=_MpGtsATMCfgVCI_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,2),_MpGtsATMCfgVCI_Type())
mpGtsATMCfgVCI.setMaxAccess(_H)
if mibBuilder.loadTexts:mpGtsATMCfgVCI.setStatus(_A)
class _MpGtsATMCfgRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpGtsATMCfgRowIndex_Type.__name__=_F
_MpGtsATMCfgRowIndex_Object=MibTableColumn
mpGtsATMCfgRowIndex=_MpGtsATMCfgRowIndex_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,3),_MpGtsATMCfgRowIndex_Type())
mpGtsATMCfgRowIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mpGtsATMCfgRowIndex.setStatus(_A)
class _MpGtsATMCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_MpGtsATMCfgType_Type.__name__=_F
_MpGtsATMCfgType_Object=MibTableColumn
mpGtsATMCfgType=_MpGtsATMCfgType_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,4),_MpGtsATMCfgType_Type())
mpGtsATMCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMCfgType.setStatus(_A)
class _MpGtsATMCfgAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpGtsATMCfgAclName_Type.__name__=_K
_MpGtsATMCfgAclName_Object=MibTableColumn
mpGtsATMCfgAclName=_MpGtsATMCfgAclName_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,5),_MpGtsATMCfgAclName_Type())
mpGtsATMCfgAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMCfgAclName.setStatus(_A)
_MpGtsATMCfgRate64_Type=Unsigned64
_MpGtsATMCfgRate64_Object=MibTableColumn
mpGtsATMCfgRate64=_MpGtsATMCfgRate64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,6),_MpGtsATMCfgRate64_Type())
mpGtsATMCfgRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMCfgRate64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMCfgRate64.setUnits(_O)
_MpGtsATMCfgBurstSize_Type=Unsigned32
_MpGtsATMCfgBurstSize_Object=MibTableColumn
mpGtsATMCfgBurstSize=_MpGtsATMCfgBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,7),_MpGtsATMCfgBurstSize_Type())
mpGtsATMCfgBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMCfgBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMCfgBurstSize.setUnits(_I)
_MpGtsATMCfgExtBurstSize_Type=Unsigned32
_MpGtsATMCfgExtBurstSize_Object=MibTableColumn
mpGtsATMCfgExtBurstSize=_MpGtsATMCfgExtBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,8),_MpGtsATMCfgExtBurstSize_Type())
mpGtsATMCfgExtBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMCfgExtBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMCfgExtBurstSize.setUnits(_I)
_MpGtsATMCfgQueueLimit_Type=Unsigned32
_MpGtsATMCfgQueueLimit_Object=MibTableColumn
mpGtsATMCfgQueueLimit=_MpGtsATMCfgQueueLimit_Object((1,3,6,1,4,1,5651,6,2,3,5,1,1,3,1,9),_MpGtsATMCfgQueueLimit_Type())
mpGtsATMCfgQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMCfgQueueLimit.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMCfgQueueLimit.setUnits(_P)
_MpGtsStats_ObjectIdentity=ObjectIdentity
mpGtsStats=_MpGtsStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,5,1,2))
_MpGtsInterfaceStatTable_Object=MibTable
mpGtsInterfaceStatTable=_MpGtsInterfaceStatTable_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1))
if mibBuilder.loadTexts:mpGtsInterfaceStatTable.setStatus(_A)
_MpGtsInterfaceStatEntry_Object=MibTableRow
mpGtsInterfaceStatEntry=_MpGtsInterfaceStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1))
mpGtsInterfaceStatEntry.setIndexNames((0,_C,_G),(0,_C,_L))
if mibBuilder.loadTexts:mpGtsInterfaceStatEntry.setStatus(_A)
_MpGtsIFStatSentByte64_Type=Counter64
_MpGtsIFStatSentByte64_Object=MibTableColumn
mpGtsIFStatSentByte64=_MpGtsIFStatSentByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,1),_MpGtsIFStatSentByte64_Type())
mpGtsIFStatSentByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatSentByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatSentByte64.setUnits(_E)
_MpGtsIFStatSentPkt64_Type=Counter64
_MpGtsIFStatSentPkt64_Object=MibTableColumn
mpGtsIFStatSentPkt64=_MpGtsIFStatSentPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,2),_MpGtsIFStatSentPkt64_Type())
mpGtsIFStatSentPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatSentPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatSentPkt64.setUnits(_D)
_MpGtsIFStatDelayedByte64_Type=Counter64
_MpGtsIFStatDelayedByte64_Object=MibTableColumn
mpGtsIFStatDelayedByte64=_MpGtsIFStatDelayedByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,3),_MpGtsIFStatDelayedByte64_Type())
mpGtsIFStatDelayedByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatDelayedByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatDelayedByte64.setUnits(_E)
_MpGtsIFStatDelayedPkt64_Type=Counter64
_MpGtsIFStatDelayedPkt64_Object=MibTableColumn
mpGtsIFStatDelayedPkt64=_MpGtsIFStatDelayedPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,4),_MpGtsIFStatDelayedPkt64_Type())
mpGtsIFStatDelayedPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatDelayedPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatDelayedPkt64.setUnits(_D)
_MpGtsIFStatDropByte64_Type=Counter64
_MpGtsIFStatDropByte64_Object=MibTableColumn
mpGtsIFStatDropByte64=_MpGtsIFStatDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,5),_MpGtsIFStatDropByte64_Type())
mpGtsIFStatDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatDropByte64.setUnits(_E)
_MpGtsIFStatDropPkt64_Type=Counter64
_MpGtsIFStatDropPkt64_Object=MibTableColumn
mpGtsIFStatDropPkt64=_MpGtsIFStatDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,6),_MpGtsIFStatDropPkt64_Type())
mpGtsIFStatDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatDropPkt64.setUnits(_D)
_MpGtsIFStatActive_Type=TruthValue
_MpGtsIFStatActive_Object=MibTableColumn
mpGtsIFStatActive=_MpGtsIFStatActive_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,7),_MpGtsIFStatActive_Type())
mpGtsIFStatActive.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatActive.setStatus(_A)
_MpGtsIFStatCurrentQSize_Type=Gauge32
_MpGtsIFStatCurrentQSize_Object=MibTableColumn
mpGtsIFStatCurrentQSize=_MpGtsIFStatCurrentQSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,1,1,8),_MpGtsIFStatCurrentQSize_Type())
mpGtsIFStatCurrentQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsIFStatCurrentQSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsIFStatCurrentQSize.setUnits(_D)
_MpGtsFrameRelayVCStatTable_Object=MibTable
mpGtsFrameRelayVCStatTable=_MpGtsFrameRelayVCStatTable_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2))
if mibBuilder.loadTexts:mpGtsFrameRelayVCStatTable.setStatus(_A)
_MpGtsFrameRelayVCStatEntry_Object=MibTableRow
mpGtsFrameRelayVCStatEntry=_MpGtsFrameRelayVCStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1))
mpGtsFrameRelayVCStatEntry.setIndexNames((0,_C,_G),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:mpGtsFrameRelayVCStatEntry.setStatus(_A)
_MpGtsFRStatSentByte64_Type=Counter64
_MpGtsFRStatSentByte64_Object=MibTableColumn
mpGtsFRStatSentByte64=_MpGtsFRStatSentByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,1),_MpGtsFRStatSentByte64_Type())
mpGtsFRStatSentByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatSentByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatSentByte64.setUnits(_E)
_MpGtsFRStatSentPkt64_Type=Counter64
_MpGtsFRStatSentPkt64_Object=MibTableColumn
mpGtsFRStatSentPkt64=_MpGtsFRStatSentPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,2),_MpGtsFRStatSentPkt64_Type())
mpGtsFRStatSentPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatSentPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatSentPkt64.setUnits(_D)
_MpGtsFRStatDelayedByte64_Type=Counter64
_MpGtsFRStatDelayedByte64_Object=MibTableColumn
mpGtsFRStatDelayedByte64=_MpGtsFRStatDelayedByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,3),_MpGtsFRStatDelayedByte64_Type())
mpGtsFRStatDelayedByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatDelayedByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatDelayedByte64.setUnits(_E)
_MpGtsFRStatDelayedPkt64_Type=Counter64
_MpGtsFRStatDelayedPkt64_Object=MibTableColumn
mpGtsFRStatDelayedPkt64=_MpGtsFRStatDelayedPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,4),_MpGtsFRStatDelayedPkt64_Type())
mpGtsFRStatDelayedPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatDelayedPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatDelayedPkt64.setUnits(_D)
_MpGtsFRStatDropByte64_Type=Counter64
_MpGtsFRStatDropByte64_Object=MibTableColumn
mpGtsFRStatDropByte64=_MpGtsFRStatDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,5),_MpGtsFRStatDropByte64_Type())
mpGtsFRStatDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatDropByte64.setUnits(_E)
_MpGtsFRStatDropPkt64_Type=Counter64
_MpGtsFRStatDropPkt64_Object=MibTableColumn
mpGtsFRStatDropPkt64=_MpGtsFRStatDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,6),_MpGtsFRStatDropPkt64_Type())
mpGtsFRStatDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatDropPkt64.setUnits(_D)
_MpGtsFRStatActive_Type=TruthValue
_MpGtsFRStatActive_Object=MibTableColumn
mpGtsFRStatActive=_MpGtsFRStatActive_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,7),_MpGtsFRStatActive_Type())
mpGtsFRStatActive.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatActive.setStatus(_A)
_MpGtsFRStatCurrentQSize_Type=Gauge32
_MpGtsFRStatCurrentQSize_Object=MibTableColumn
mpGtsFRStatCurrentQSize=_MpGtsFRStatCurrentQSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,2,1,8),_MpGtsFRStatCurrentQSize_Type())
mpGtsFRStatCurrentQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsFRStatCurrentQSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsFRStatCurrentQSize.setUnits(_D)
_MpGtsATMPVCStatTable_Object=MibTable
mpGtsATMPVCStatTable=_MpGtsATMPVCStatTable_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3))
if mibBuilder.loadTexts:mpGtsATMPVCStatTable.setStatus(_A)
_MpGtsATMPVCStatEntry_Object=MibTableRow
mpGtsATMPVCStatEntry=_MpGtsATMPVCStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1))
mpGtsATMPVCStatEntry.setIndexNames((0,_C,_G),(0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:mpGtsATMPVCStatEntry.setStatus(_A)
_MpGtsATMStatSentByte64_Type=Counter64
_MpGtsATMStatSentByte64_Object=MibTableColumn
mpGtsATMStatSentByte64=_MpGtsATMStatSentByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,1),_MpGtsATMStatSentByte64_Type())
mpGtsATMStatSentByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatSentByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatSentByte64.setUnits(_E)
_MpGtsATMStatSentPkt64_Type=Counter64
_MpGtsATMStatSentPkt64_Object=MibTableColumn
mpGtsATMStatSentPkt64=_MpGtsATMStatSentPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,2),_MpGtsATMStatSentPkt64_Type())
mpGtsATMStatSentPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatSentPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatSentPkt64.setUnits(_D)
_MpGtsATMStatDelayedByte64_Type=Counter64
_MpGtsATMStatDelayedByte64_Object=MibTableColumn
mpGtsATMStatDelayedByte64=_MpGtsATMStatDelayedByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,3),_MpGtsATMStatDelayedByte64_Type())
mpGtsATMStatDelayedByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatDelayedByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatDelayedByte64.setUnits(_E)
_MpGtsATMStatDelayedPkt64_Type=Counter64
_MpGtsATMStatDelayedPkt64_Object=MibTableColumn
mpGtsATMStatDelayedPkt64=_MpGtsATMStatDelayedPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,4),_MpGtsATMStatDelayedPkt64_Type())
mpGtsATMStatDelayedPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatDelayedPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatDelayedPkt64.setUnits(_D)
_MpGtsATMStatDropByte64_Type=Counter64
_MpGtsATMStatDropByte64_Object=MibTableColumn
mpGtsATMStatDropByte64=_MpGtsATMStatDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,5),_MpGtsATMStatDropByte64_Type())
mpGtsATMStatDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatDropByte64.setUnits(_E)
_MpGtsATMStatDropPkt64_Type=Counter64
_MpGtsATMStatDropPkt64_Object=MibTableColumn
mpGtsATMStatDropPkt64=_MpGtsATMStatDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,6),_MpGtsATMStatDropPkt64_Type())
mpGtsATMStatDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatDropPkt64.setUnits(_D)
_MpGtsATMStatActive_Type=TruthValue
_MpGtsATMStatActive_Object=MibTableColumn
mpGtsATMStatActive=_MpGtsATMStatActive_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,7),_MpGtsATMStatActive_Type())
mpGtsATMStatActive.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatActive.setStatus(_A)
_MpGtsATMStatCurrentQSize_Type=Gauge32
_MpGtsATMStatCurrentQSize_Object=MibTableColumn
mpGtsATMStatCurrentQSize=_MpGtsATMStatCurrentQSize_Object((1,3,6,1,4,1,5651,6,2,3,5,1,2,3,1,8),_MpGtsATMStatCurrentQSize_Type())
mpGtsATMStatCurrentQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpGtsATMStatCurrentQSize.setStatus(_A)
if mibBuilder.loadTexts:mpGtsATMStatCurrentQSize.setUnits(_D)
mibBuilder.exportSymbols(_C,**{'Unsigned64':Unsigned64,'maipu':maipu,'mpMgmt2':mpMgmt2,'mpRouterTech':mpRouterTech,'mpRtQoSv2':mpRtQoSv2,'maipuGtsMIB':maipuGtsMIB,'maipuGtsMIBObjects':maipuGtsMIBObjects,'mpGtsConfigs':mpGtsConfigs,'mpGtsInterfaceCfgTable':mpGtsInterfaceCfgTable,'mpGtsInterfaceCfgEntry':mpGtsInterfaceCfgEntry,_L:mpGtsIFCfgRowIndex,'mpGtsIFCfgType':mpGtsIFCfgType,'mpGtsIFCfgAclName':mpGtsIFCfgAclName,'mpGtsIFCfgRate64':mpGtsIFCfgRate64,'mpGtsIFCfgBurstSize':mpGtsIFCfgBurstSize,'mpGtsIFCfgExtBurstSize':mpGtsIFCfgExtBurstSize,'mpGtsIFCfgQueueLimit':mpGtsIFCfgQueueLimit,'mpGtsFrameRelayVCCfgTable':mpGtsFrameRelayVCCfgTable,'mpGtsFrameRelayVCCfgEntry':mpGtsFrameRelayVCCfgEntry,_Q:mpGtsFRCfgDLCI,_R:mpGtsFRCfgRowIndex,'mpGtsFRCfgType':mpGtsFRCfgType,'mpGtsFRCfgAclName':mpGtsFRCfgAclName,'mpGtsFRCfgRate64':mpGtsFRCfgRate64,'mpGtsFRCfgBurstSize':mpGtsFRCfgBurstSize,'mpGtsFRCfgExtBurstSize':mpGtsFRCfgExtBurstSize,'mpGtsFRCfgQueueLimit':mpGtsFRCfgQueueLimit,'mpGtsATMPVCCfgTable':mpGtsATMPVCCfgTable,'mpGtsATMPVCCfgEntry':mpGtsATMPVCCfgEntry,_S:mpGtsATMCfgVPI,_T:mpGtsATMCfgVCI,_U:mpGtsATMCfgRowIndex,'mpGtsATMCfgType':mpGtsATMCfgType,'mpGtsATMCfgAclName':mpGtsATMCfgAclName,'mpGtsATMCfgRate64':mpGtsATMCfgRate64,'mpGtsATMCfgBurstSize':mpGtsATMCfgBurstSize,'mpGtsATMCfgExtBurstSize':mpGtsATMCfgExtBurstSize,'mpGtsATMCfgQueueLimit':mpGtsATMCfgQueueLimit,'mpGtsStats':mpGtsStats,'mpGtsInterfaceStatTable':mpGtsInterfaceStatTable,'mpGtsInterfaceStatEntry':mpGtsInterfaceStatEntry,'mpGtsIFStatSentByte64':mpGtsIFStatSentByte64,'mpGtsIFStatSentPkt64':mpGtsIFStatSentPkt64,'mpGtsIFStatDelayedByte64':mpGtsIFStatDelayedByte64,'mpGtsIFStatDelayedPkt64':mpGtsIFStatDelayedPkt64,'mpGtsIFStatDropByte64':mpGtsIFStatDropByte64,'mpGtsIFStatDropPkt64':mpGtsIFStatDropPkt64,'mpGtsIFStatActive':mpGtsIFStatActive,'mpGtsIFStatCurrentQSize':mpGtsIFStatCurrentQSize,'mpGtsFrameRelayVCStatTable':mpGtsFrameRelayVCStatTable,'mpGtsFrameRelayVCStatEntry':mpGtsFrameRelayVCStatEntry,'mpGtsFRStatSentByte64':mpGtsFRStatSentByte64,'mpGtsFRStatSentPkt64':mpGtsFRStatSentPkt64,'mpGtsFRStatDelayedByte64':mpGtsFRStatDelayedByte64,'mpGtsFRStatDelayedPkt64':mpGtsFRStatDelayedPkt64,'mpGtsFRStatDropByte64':mpGtsFRStatDropByte64,'mpGtsFRStatDropPkt64':mpGtsFRStatDropPkt64,'mpGtsFRStatActive':mpGtsFRStatActive,'mpGtsFRStatCurrentQSize':mpGtsFRStatCurrentQSize,'mpGtsATMPVCStatTable':mpGtsATMPVCStatTable,'mpGtsATMPVCStatEntry':mpGtsATMPVCStatEntry,'mpGtsATMStatSentByte64':mpGtsATMStatSentByte64,'mpGtsATMStatSentPkt64':mpGtsATMStatSentPkt64,'mpGtsATMStatDelayedByte64':mpGtsATMStatDelayedByte64,'mpGtsATMStatDelayedPkt64':mpGtsATMStatDelayedPkt64,'mpGtsATMStatDropByte64':mpGtsATMStatDropByte64,'mpGtsATMStatDropPkt64':mpGtsATMStatDropPkt64,'mpGtsATMStatActive':mpGtsATMStatActive,'mpGtsATMStatCurrentQSize':mpGtsATMStatCurrentQSize})