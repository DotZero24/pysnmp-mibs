_U='altigaFilterStatsGroup'
_T='alFilterStatsOutIcmpFragDiscard'
_S='alFilterStatsInIcmpFragDiscard'
_R='alFilterStatsOutTcpFragDiscard'
_Q='alFilterStatsInTcpFragDiscard'
_P='alFilterStatsOutShortUdpHdr'
_O='alFilterStatsInShortUdpHdr'
_N='alFilterStatsOutShortTcpHdr'
_M='alFilterStatsInShortTcpHdr'
_L='alFilterStatsOutPktsTx'
_K='alFilterStatsInPktsTx'
_J='alFilterStatsOutPktsRx'
_I='alFilterStatsInPktsRx'
_H='alFilterStatsOutPktsFiltered'
_G='alFilterStatsInPktsFiltered'
_F='alFilterStatsStartTime'
_E='Integer32'
_D='alFilterStatsInterfaceId'
_C='read-only'
_B='ALTIGA-FILTER-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alFilterMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alFilterMibModule')
alFilterGroup,alStatsFilter=mibBuilder.importSymbols('ALTIGA-MIB','alFilterGroup','alStatsFilter')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaFilterStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,14,2))
if mibBuilder.loadTexts:altigaFilterStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaFilterStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaFilterStatsMibConformance=_AltigaFilterStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,14,2,1))
_AltigaFilterStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaFilterStatsMibCompliances=_AltigaFilterStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,14,2,1,1))
_AlStatsFilterGlobal_ObjectIdentity=ObjectIdentity
alStatsFilterGlobal=_AlStatsFilterGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,9,1))
_AlFilterStatsTable_Object=MibTable
alFilterStatsTable=_AlFilterStatsTable_Object((1,3,6,1,4,1,3076,2,1,2,9,2))
if mibBuilder.loadTexts:alFilterStatsTable.setStatus(_A)
_AlFilterStatsEntry_Object=MibTableRow
alFilterStatsEntry=_AlFilterStatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1))
alFilterStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alFilterStatsEntry.setStatus(_A)
class _AlFilterStatsInterfaceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlFilterStatsInterfaceId_Type.__name__=_E
_AlFilterStatsInterfaceId_Object=MibTableColumn
alFilterStatsInterfaceId=_AlFilterStatsInterfaceId_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,1),_AlFilterStatsInterfaceId_Type())
alFilterStatsInterfaceId.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInterfaceId.setStatus(_A)
_AlFilterStatsStartTime_Type=TimeTicks
_AlFilterStatsStartTime_Object=MibTableColumn
alFilterStatsStartTime=_AlFilterStatsStartTime_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,2),_AlFilterStatsStartTime_Type())
alFilterStatsStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsStartTime.setStatus(_A)
_AlFilterStatsInPktsFiltered_Type=Counter32
_AlFilterStatsInPktsFiltered_Object=MibTableColumn
alFilterStatsInPktsFiltered=_AlFilterStatsInPktsFiltered_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,3),_AlFilterStatsInPktsFiltered_Type())
alFilterStatsInPktsFiltered.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInPktsFiltered.setStatus(_A)
_AlFilterStatsOutPktsFiltered_Type=Counter32
_AlFilterStatsOutPktsFiltered_Object=MibTableColumn
alFilterStatsOutPktsFiltered=_AlFilterStatsOutPktsFiltered_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,4),_AlFilterStatsOutPktsFiltered_Type())
alFilterStatsOutPktsFiltered.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutPktsFiltered.setStatus(_A)
_AlFilterStatsInPktsRx_Type=Counter32
_AlFilterStatsInPktsRx_Object=MibTableColumn
alFilterStatsInPktsRx=_AlFilterStatsInPktsRx_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,5),_AlFilterStatsInPktsRx_Type())
alFilterStatsInPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInPktsRx.setStatus(_A)
_AlFilterStatsOutPktsRx_Type=Counter32
_AlFilterStatsOutPktsRx_Object=MibTableColumn
alFilterStatsOutPktsRx=_AlFilterStatsOutPktsRx_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,6),_AlFilterStatsOutPktsRx_Type())
alFilterStatsOutPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutPktsRx.setStatus(_A)
_AlFilterStatsInPktsTx_Type=Counter32
_AlFilterStatsInPktsTx_Object=MibTableColumn
alFilterStatsInPktsTx=_AlFilterStatsInPktsTx_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,7),_AlFilterStatsInPktsTx_Type())
alFilterStatsInPktsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInPktsTx.setStatus(_A)
_AlFilterStatsOutPktsTx_Type=Counter32
_AlFilterStatsOutPktsTx_Object=MibTableColumn
alFilterStatsOutPktsTx=_AlFilterStatsOutPktsTx_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,8),_AlFilterStatsOutPktsTx_Type())
alFilterStatsOutPktsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutPktsTx.setStatus(_A)
_AlFilterStatsInShortTcpHdr_Type=Counter32
_AlFilterStatsInShortTcpHdr_Object=MibTableColumn
alFilterStatsInShortTcpHdr=_AlFilterStatsInShortTcpHdr_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,9),_AlFilterStatsInShortTcpHdr_Type())
alFilterStatsInShortTcpHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInShortTcpHdr.setStatus(_A)
_AlFilterStatsOutShortTcpHdr_Type=Counter32
_AlFilterStatsOutShortTcpHdr_Object=MibTableColumn
alFilterStatsOutShortTcpHdr=_AlFilterStatsOutShortTcpHdr_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,10),_AlFilterStatsOutShortTcpHdr_Type())
alFilterStatsOutShortTcpHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutShortTcpHdr.setStatus(_A)
_AlFilterStatsInShortUdpHdr_Type=Counter32
_AlFilterStatsInShortUdpHdr_Object=MibTableColumn
alFilterStatsInShortUdpHdr=_AlFilterStatsInShortUdpHdr_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,11),_AlFilterStatsInShortUdpHdr_Type())
alFilterStatsInShortUdpHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInShortUdpHdr.setStatus(_A)
_AlFilterStatsOutShortUdpHdr_Type=Counter32
_AlFilterStatsOutShortUdpHdr_Object=MibTableColumn
alFilterStatsOutShortUdpHdr=_AlFilterStatsOutShortUdpHdr_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,12),_AlFilterStatsOutShortUdpHdr_Type())
alFilterStatsOutShortUdpHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutShortUdpHdr.setStatus(_A)
_AlFilterStatsInTcpFragDiscard_Type=Counter32
_AlFilterStatsInTcpFragDiscard_Object=MibTableColumn
alFilterStatsInTcpFragDiscard=_AlFilterStatsInTcpFragDiscard_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,13),_AlFilterStatsInTcpFragDiscard_Type())
alFilterStatsInTcpFragDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInTcpFragDiscard.setStatus(_A)
_AlFilterStatsOutTcpFragDiscard_Type=Counter32
_AlFilterStatsOutTcpFragDiscard_Object=MibTableColumn
alFilterStatsOutTcpFragDiscard=_AlFilterStatsOutTcpFragDiscard_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,14),_AlFilterStatsOutTcpFragDiscard_Type())
alFilterStatsOutTcpFragDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutTcpFragDiscard.setStatus(_A)
_AlFilterStatsInIcmpFragDiscard_Type=Counter32
_AlFilterStatsInIcmpFragDiscard_Object=MibTableColumn
alFilterStatsInIcmpFragDiscard=_AlFilterStatsInIcmpFragDiscard_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,15),_AlFilterStatsInIcmpFragDiscard_Type())
alFilterStatsInIcmpFragDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsInIcmpFragDiscard.setStatus(_A)
_AlFilterStatsOutIcmpFragDiscard_Type=Counter32
_AlFilterStatsOutIcmpFragDiscard_Object=MibTableColumn
alFilterStatsOutIcmpFragDiscard=_AlFilterStatsOutIcmpFragDiscard_Object((1,3,6,1,4,1,3076,2,1,2,9,2,1,16),_AlFilterStatsOutIcmpFragDiscard_Type())
alFilterStatsOutIcmpFragDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:alFilterStatsOutIcmpFragDiscard.setStatus(_A)
altigaFilterStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,9,2))
altigaFilterStatsGroup.setObjects(*((_B,_D),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:altigaFilterStatsGroup.setStatus(_A)
altigaFilterStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,14,2,1,1,1))
altigaFilterStatsMibCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:altigaFilterStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaFilterStatsMibModule':altigaFilterStatsMibModule,'altigaFilterStatsMibConformance':altigaFilterStatsMibConformance,'altigaFilterStatsMibCompliances':altigaFilterStatsMibCompliances,'altigaFilterStatsMibCompliance':altigaFilterStatsMibCompliance,_U:altigaFilterStatsGroup,'alStatsFilterGlobal':alStatsFilterGlobal,'alFilterStatsTable':alFilterStatsTable,'alFilterStatsEntry':alFilterStatsEntry,_D:alFilterStatsInterfaceId,_F:alFilterStatsStartTime,_G:alFilterStatsInPktsFiltered,_H:alFilterStatsOutPktsFiltered,_I:alFilterStatsInPktsRx,_J:alFilterStatsOutPktsRx,_K:alFilterStatsInPktsTx,_L:alFilterStatsOutPktsTx,_M:alFilterStatsInShortTcpHdr,_N:alFilterStatsOutShortTcpHdr,_O:alFilterStatsInShortUdpHdr,_P:alFilterStatsOutShortUdpHdr,_Q:alFilterStatsInTcpFragDiscard,_R:alFilterStatsOutTcpFragDiscard,_S:alFilterStatsInIcmpFragDiscard,_T:alFilterStatsOutIcmpFragDiscard})