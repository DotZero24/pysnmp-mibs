_H='enable'
_G='disable'
_F='tunnelIfIndex'
_E='MAIPU-TUNNEL-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mpTunnelMib=ModuleIdentity((1,3,6,1,4,1,5651,3,37))
_TunnelConf_ObjectIdentity=ObjectIdentity
tunnelConf=_TunnelConf_ObjectIdentity((1,3,6,1,4,1,5651,3,37,1))
_TunnelIfConfTable_Object=MibTable
tunnelIfConfTable=_TunnelIfConfTable_Object((1,3,6,1,4,1,5651,3,37,1,1))
if mibBuilder.loadTexts:tunnelIfConfTable.setStatus(_A)
_TunnelIfConfEntry_Object=MibTableRow
tunnelIfConfEntry=_TunnelIfConfEntry_Object((1,3,6,1,4,1,5651,3,37,1,1,1))
tunnelIfConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tunnelIfConfEntry.setStatus(_A)
_TunnelIfIndex_Type=Integer32
_TunnelIfIndex_Object=MibTableColumn
tunnelIfIndex=_TunnelIfIndex_Object((1,3,6,1,4,1,5651,3,37,1,1,1,1),_TunnelIfIndex_Type())
tunnelIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelIfIndex.setStatus(_A)
_TunnelIfIpAddr_Type=IpAddress
_TunnelIfIpAddr_Object=MibTableColumn
tunnelIfIpAddr=_TunnelIfIpAddr_Object((1,3,6,1,4,1,5651,3,37,1,1,1,2),_TunnelIfIpAddr_Type())
tunnelIfIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelIfIpAddr.setStatus(_A)
_TunnelSrcAddr_Type=IpAddress
_TunnelSrcAddr_Object=MibTableColumn
tunnelSrcAddr=_TunnelSrcAddr_Object((1,3,6,1,4,1,5651,3,37,1,1,1,3),_TunnelSrcAddr_Type())
tunnelSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelSrcAddr.setStatus(_A)
_TunnelDestAddr_Type=IpAddress
_TunnelDestAddr_Object=MibTableColumn
tunnelDestAddr=_TunnelDestAddr_Object((1,3,6,1,4,1,5651,3,37,1,1,1,4),_TunnelDestAddr_Type())
tunnelDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelDestAddr.setStatus(_A)
class _TunnelSeqData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_TunnelSeqData_Type.__name__=_D
_TunnelSeqData_Object=MibTableColumn
tunnelSeqData=_TunnelSeqData_Object((1,3,6,1,4,1,5651,3,37,1,1,1,5),_TunnelSeqData_Type())
tunnelSeqData.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelSeqData.setStatus(_A)
class _TunnelKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TunnelKey_Type.__name__=_D
_TunnelKey_Object=MibTableColumn
tunnelKey=_TunnelKey_Object((1,3,6,1,4,1,5651,3,37,1,1,1,6),_TunnelKey_Type())
tunnelKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelKey.setStatus(_A)
class _TunnelChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_TunnelChecksum_Type.__name__=_D
_TunnelChecksum_Object=MibTableColumn
tunnelChecksum=_TunnelChecksum_Object((1,3,6,1,4,1,5651,3,37,1,1,1,7),_TunnelChecksum_Type())
tunnelChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelChecksum.setStatus(_A)
class _TunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_TunnelState_Type.__name__=_D
_TunnelState_Object=MibTableColumn
tunnelState=_TunnelState_Object((1,3,6,1,4,1,5651,3,37,1,1,1,8),_TunnelState_Type())
tunnelState.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelState.setStatus(_A)
_TunnelStatistic_ObjectIdentity=ObjectIdentity
tunnelStatistic=_TunnelStatistic_ObjectIdentity((1,3,6,1,4,1,5651,3,37,2))
_TunnelTooshort_Type=Counter32
_TunnelTooshort_Object=MibScalar
tunnelTooshort=_TunnelTooshort_Object((1,3,6,1,4,1,5651,3,37,2,1),_TunnelTooshort_Type())
tunnelTooshort.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelTooshort.setStatus(_A)
_TunnelBadhead_Type=Counter32
_TunnelBadhead_Object=MibScalar
tunnelBadhead=_TunnelBadhead_Object((1,3,6,1,4,1,5651,3,37,2,2),_TunnelBadhead_Type())
tunnelBadhead.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelBadhead.setStatus(_A)
_TunnelBadsum_Type=Counter32
_TunnelBadsum_Object=MibScalar
tunnelBadsum=_TunnelBadsum_Object((1,3,6,1,4,1,5651,3,37,2,3),_TunnelBadsum_Type())
tunnelBadsum.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelBadsum.setStatus(_A)
_TunnelHashmiss_Type=Counter32
_TunnelHashmiss_Object=MibScalar
tunnelHashmiss=_TunnelHashmiss_Object((1,3,6,1,4,1,5651,3,37,2,4),_TunnelHashmiss_Type())
tunnelHashmiss.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelHashmiss.setStatus(_A)
_TunnelBadbcast_Type=Counter32
_TunnelBadbcast_Object=MibScalar
tunnelBadbcast=_TunnelBadbcast_Object((1,3,6,1,4,1,5651,3,37,2,5),_TunnelBadbcast_Type())
tunnelBadbcast.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelBadbcast.setStatus(_A)
_TunnelBadkey_Type=Counter32
_TunnelBadkey_Object=MibScalar
tunnelBadkey=_TunnelBadkey_Object((1,3,6,1,4,1,5651,3,37,2,6),_TunnelBadkey_Type())
tunnelBadkey.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelBadkey.setStatus(_A)
_TunnelBadproto_Type=Counter32
_TunnelBadproto_Object=MibScalar
tunnelBadproto=_TunnelBadproto_Object((1,3,6,1,4,1,5651,3,37,2,7),_TunnelBadproto_Type())
tunnelBadproto.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelBadproto.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mpTunnelMib':mpTunnelMib,'tunnelConf':tunnelConf,'tunnelIfConfTable':tunnelIfConfTable,'tunnelIfConfEntry':tunnelIfConfEntry,_F:tunnelIfIndex,'tunnelIfIpAddr':tunnelIfIpAddr,'tunnelSrcAddr':tunnelSrcAddr,'tunnelDestAddr':tunnelDestAddr,'tunnelSeqData':tunnelSeqData,'tunnelKey':tunnelKey,'tunnelChecksum':tunnelChecksum,'tunnelState':tunnelState,'tunnelStatistic':tunnelStatistic,'tunnelTooshort':tunnelTooshort,'tunnelBadhead':tunnelBadhead,'tunnelBadsum':tunnelBadsum,'tunnelHashmiss':tunnelHashmiss,'tunnelBadbcast':tunnelBadbcast,'tunnelBadkey':tunnelBadkey,'tunnelBadproto':tunnelBadproto})