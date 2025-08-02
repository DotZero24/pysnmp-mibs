_E='snsifIndex'
_D='STORMSHIELD-IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsif=ModuleIdentity((1,3,6,1,4,1,11256,1,4))
if mibBuilder.loadTexts:snsif.setRevisions(('2017-02-20 00:00',))
_SnsifTable_Object=MibTable
snsifTable=_SnsifTable_Object((1,3,6,1,4,1,11256,1,4,1))
if mibBuilder.loadTexts:snsifTable.setStatus(_A)
_SnsifEntry_Object=MibTableRow
snsifEntry=_SnsifEntry_Object((1,3,6,1,4,1,11256,1,4,1,1))
snsifEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsifEntry.setStatus(_A)
class _SnsifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsifIndex_Type.__name__=_C
_SnsifIndex_Object=MibTableColumn
snsifIndex=_SnsifIndex_Object((1,3,6,1,4,1,11256,1,4,1,1,1),_SnsifIndex_Type())
snsifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifIndex.setStatus(_A)
_SnsifUserName_Type=SnmpAdminString
_SnsifUserName_Object=MibTableColumn
snsifUserName=_SnsifUserName_Object((1,3,6,1,4,1,11256,1,4,1,1,2),_SnsifUserName_Type())
snsifUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifUserName.setStatus(_A)
_SnsifName_Type=DisplayString
_SnsifName_Object=MibTableColumn
snsifName=_SnsifName_Object((1,3,6,1,4,1,11256,1,4,1,1,3),_SnsifName_Type())
snsifName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifName.setStatus(_A)
_SnsifAddr_Type=DisplayString
_SnsifAddr_Object=MibTableColumn
snsifAddr=_SnsifAddr_Object((1,3,6,1,4,1,11256,1,4,1,1,4),_SnsifAddr_Type())
snsifAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifAddr.setStatus(_A)
_SnsifMask_Type=DisplayString
_SnsifMask_Object=MibTableColumn
snsifMask=_SnsifMask_Object((1,3,6,1,4,1,11256,1,4,1,1,5),_SnsifMask_Type())
snsifMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifMask.setStatus(_A)
_SnsifType_Type=DisplayString
_SnsifType_Object=MibTableColumn
snsifType=_SnsifType_Object((1,3,6,1,4,1,11256,1,4,1,1,6),_SnsifType_Type())
snsifType.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifType.setStatus(_A)
_SnsifColor_Type=Integer32
_SnsifColor_Object=MibTableColumn
snsifColor=_SnsifColor_Object((1,3,6,1,4,1,11256,1,4,1,1,7),_SnsifColor_Type())
snsifColor.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifColor.setStatus(_A)
_SnsifMacThroughput_Type=Integer32
_SnsifMacThroughput_Object=MibTableColumn
snsifMacThroughput=_SnsifMacThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,8),_SnsifMacThroughput_Type())
snsifMacThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifMacThroughput.setStatus(_A)
_SnsifCurThroughput_Type=Integer32
_SnsifCurThroughput_Object=MibTableColumn
snsifCurThroughput=_SnsifCurThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,9),_SnsifCurThroughput_Type())
snsifCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifCurThroughput.setStatus(_A)
_SnsifMaxThroughput_Type=Integer32
_SnsifMaxThroughput_Object=MibTableColumn
snsifMaxThroughput=_SnsifMaxThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,10),_SnsifMaxThroughput_Type())
snsifMaxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifMaxThroughput.setStatus(_A)
_SnsifPktAccepted_Type=Counter64
_SnsifPktAccepted_Object=MibTableColumn
snsifPktAccepted=_SnsifPktAccepted_Object((1,3,6,1,4,1,11256,1,4,1,1,11),_SnsifPktAccepted_Type())
snsifPktAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifPktAccepted.setStatus(_A)
_SnsifPktBlocked_Type=Counter64
_SnsifPktBlocked_Object=MibTableColumn
snsifPktBlocked=_SnsifPktBlocked_Object((1,3,6,1,4,1,11256,1,4,1,1,12),_SnsifPktBlocked_Type())
snsifPktBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifPktBlocked.setStatus(_A)
_SnsifPktFragmented_Type=Counter64
_SnsifPktFragmented_Object=MibTableColumn
snsifPktFragmented=_SnsifPktFragmented_Object((1,3,6,1,4,1,11256,1,4,1,1,13),_SnsifPktFragmented_Type())
snsifPktFragmented.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifPktFragmented.setStatus(_A)
_SnsifPktTcp_Type=Counter64
_SnsifPktTcp_Object=MibTableColumn
snsifPktTcp=_SnsifPktTcp_Object((1,3,6,1,4,1,11256,1,4,1,1,14),_SnsifPktTcp_Type())
snsifPktTcp.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifPktTcp.setStatus(_A)
_SnsifPktUdp_Type=Counter64
_SnsifPktUdp_Object=MibTableColumn
snsifPktUdp=_SnsifPktUdp_Object((1,3,6,1,4,1,11256,1,4,1,1,15),_SnsifPktUdp_Type())
snsifPktUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifPktUdp.setStatus(_A)
_SnsifPktIcmp_Type=Counter64
_SnsifPktIcmp_Object=MibTableColumn
snsifPktIcmp=_SnsifPktIcmp_Object((1,3,6,1,4,1,11256,1,4,1,1,16),_SnsifPktIcmp_Type())
snsifPktIcmp.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifPktIcmp.setStatus(_A)
_SnsifTotalBytes_Type=Counter64
_SnsifTotalBytes_Object=MibTableColumn
snsifTotalBytes=_SnsifTotalBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,17),_SnsifTotalBytes_Type())
snsifTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifTotalBytes.setStatus(_A)
_SnsifTcpBytes_Type=Counter64
_SnsifTcpBytes_Object=MibTableColumn
snsifTcpBytes=_SnsifTcpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,18),_SnsifTcpBytes_Type())
snsifTcpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifTcpBytes.setStatus(_A)
_SnsifUdpBytes_Type=Counter64
_SnsifUdpBytes_Object=MibTableColumn
snsifUdpBytes=_SnsifUdpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,19),_SnsifUdpBytes_Type())
snsifUdpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifUdpBytes.setStatus(_A)
_SnsifIcmpBytes_Type=Counter64
_SnsifIcmpBytes_Object=MibTableColumn
snsifIcmpBytes=_SnsifIcmpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,20),_SnsifIcmpBytes_Type())
snsifIcmpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifIcmpBytes.setStatus(_A)
_SnsifTcpConn_Type=Counter64
_SnsifTcpConn_Object=MibTableColumn
snsifTcpConn=_SnsifTcpConn_Object((1,3,6,1,4,1,11256,1,4,1,1,21),_SnsifTcpConn_Type())
snsifTcpConn.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifTcpConn.setStatus(_A)
_SnsifUdpConn_Type=Counter64
_SnsifUdpConn_Object=MibTableColumn
snsifUdpConn=_SnsifUdpConn_Object((1,3,6,1,4,1,11256,1,4,1,1,22),_SnsifUdpConn_Type())
snsifUdpConn.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifUdpConn.setStatus(_A)
_SnsifTcpConnCount_Type=Integer32
_SnsifTcpConnCount_Object=MibTableColumn
snsifTcpConnCount=_SnsifTcpConnCount_Object((1,3,6,1,4,1,11256,1,4,1,1,23),_SnsifTcpConnCount_Type())
snsifTcpConnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifTcpConnCount.setStatus(_A)
_SnsifUdpConnCount_Type=Integer32
_SnsifUdpConnCount_Object=MibTableColumn
snsifUdpConnCount=_SnsifUdpConnCount_Object((1,3,6,1,4,1,11256,1,4,1,1,24),_SnsifUdpConnCount_Type())
snsifUdpConnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifUdpConnCount.setStatus(_A)
_SnsifInCurThroughput_Type=Integer32
_SnsifInCurThroughput_Object=MibTableColumn
snsifInCurThroughput=_SnsifInCurThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,25),_SnsifInCurThroughput_Type())
snsifInCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifInCurThroughput.setStatus(_A)
_SnsifOutCurThroughput_Type=Integer32
_SnsifOutCurThroughput_Object=MibTableColumn
snsifOutCurThroughput=_SnsifOutCurThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,26),_SnsifOutCurThroughput_Type())
snsifOutCurThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifOutCurThroughput.setStatus(_A)
_SnsifInMaxThroughput_Type=Integer32
_SnsifInMaxThroughput_Object=MibTableColumn
snsifInMaxThroughput=_SnsifInMaxThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,27),_SnsifInMaxThroughput_Type())
snsifInMaxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifInMaxThroughput.setStatus(_A)
_SnsifOutMaxThroughput_Type=Integer32
_SnsifOutMaxThroughput_Object=MibTableColumn
snsifOutMaxThroughput=_SnsifOutMaxThroughput_Object((1,3,6,1,4,1,11256,1,4,1,1,28),_SnsifOutMaxThroughput_Type())
snsifOutMaxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifOutMaxThroughput.setStatus(_A)
_SnsifInTotalBytes_Type=Counter64
_SnsifInTotalBytes_Object=MibTableColumn
snsifInTotalBytes=_SnsifInTotalBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,29),_SnsifInTotalBytes_Type())
snsifInTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifInTotalBytes.setStatus(_A)
_SnsifOutTotalBytes_Type=Counter64
_SnsifOutTotalBytes_Object=MibTableColumn
snsifOutTotalBytes=_SnsifOutTotalBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,30),_SnsifOutTotalBytes_Type())
snsifOutTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifOutTotalBytes.setStatus(_A)
_SnsifInTcpBytes_Type=Counter64
_SnsifInTcpBytes_Object=MibTableColumn
snsifInTcpBytes=_SnsifInTcpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,31),_SnsifInTcpBytes_Type())
snsifInTcpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifInTcpBytes.setStatus(_A)
_SnsifOutTcpBytes_Type=Counter64
_SnsifOutTcpBytes_Object=MibTableColumn
snsifOutTcpBytes=_SnsifOutTcpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,32),_SnsifOutTcpBytes_Type())
snsifOutTcpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifOutTcpBytes.setStatus(_A)
_SnsifInUdpBytes_Type=Counter64
_SnsifInUdpBytes_Object=MibTableColumn
snsifInUdpBytes=_SnsifInUdpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,33),_SnsifInUdpBytes_Type())
snsifInUdpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifInUdpBytes.setStatus(_A)
_SnsifOutUdpBytes_Type=Counter64
_SnsifOutUdpBytes_Object=MibTableColumn
snsifOutUdpBytes=_SnsifOutUdpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,34),_SnsifOutUdpBytes_Type())
snsifOutUdpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifOutUdpBytes.setStatus(_A)
_SnsifInIcmpBytes_Type=Counter64
_SnsifInIcmpBytes_Object=MibTableColumn
snsifInIcmpBytes=_SnsifInIcmpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,35),_SnsifInIcmpBytes_Type())
snsifInIcmpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifInIcmpBytes.setStatus(_A)
_SnsifOutIcmpBytes_Type=Counter64
_SnsifOutIcmpBytes_Object=MibTableColumn
snsifOutIcmpBytes=_SnsifOutIcmpBytes_Object((1,3,6,1,4,1,11256,1,4,1,1,36),_SnsifOutIcmpBytes_Type())
snsifOutIcmpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifOutIcmpBytes.setStatus(_A)
_SnsifProtected_Type=Integer32
_SnsifProtected_Object=MibTableColumn
snsifProtected=_SnsifProtected_Object((1,3,6,1,4,1,11256,1,4,1,1,37),_SnsifProtected_Type())
snsifProtected.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifProtected.setStatus(_A)
_SnsifDrvName_Type=DisplayString
_SnsifDrvName_Object=MibTableColumn
snsifDrvName=_SnsifDrvName_Object((1,3,6,1,4,1,11256,1,4,1,1,38),_SnsifDrvName_Type())
snsifDrvName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifDrvName.setStatus(_A)
_SnsifComment_Type=DisplayString
_SnsifComment_Object=MibTableColumn
snsifComment=_SnsifComment_Object((1,3,6,1,4,1,11256,1,4,1,1,39),_SnsifComment_Type())
snsifComment.setMaxAccess(_B)
if mibBuilder.loadTexts:snsifComment.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsif':snsif,'snsifTable':snsifTable,'snsifEntry':snsifEntry,_E:snsifIndex,'snsifUserName':snsifUserName,'snsifName':snsifName,'snsifAddr':snsifAddr,'snsifMask':snsifMask,'snsifType':snsifType,'snsifColor':snsifColor,'snsifMacThroughput':snsifMacThroughput,'snsifCurThroughput':snsifCurThroughput,'snsifMaxThroughput':snsifMaxThroughput,'snsifPktAccepted':snsifPktAccepted,'snsifPktBlocked':snsifPktBlocked,'snsifPktFragmented':snsifPktFragmented,'snsifPktTcp':snsifPktTcp,'snsifPktUdp':snsifPktUdp,'snsifPktIcmp':snsifPktIcmp,'snsifTotalBytes':snsifTotalBytes,'snsifTcpBytes':snsifTcpBytes,'snsifUdpBytes':snsifUdpBytes,'snsifIcmpBytes':snsifIcmpBytes,'snsifTcpConn':snsifTcpConn,'snsifUdpConn':snsifUdpConn,'snsifTcpConnCount':snsifTcpConnCount,'snsifUdpConnCount':snsifUdpConnCount,'snsifInCurThroughput':snsifInCurThroughput,'snsifOutCurThroughput':snsifOutCurThroughput,'snsifInMaxThroughput':snsifInMaxThroughput,'snsifOutMaxThroughput':snsifOutMaxThroughput,'snsifInTotalBytes':snsifInTotalBytes,'snsifOutTotalBytes':snsifOutTotalBytes,'snsifInTcpBytes':snsifInTcpBytes,'snsifOutTcpBytes':snsifOutTcpBytes,'snsifInUdpBytes':snsifInUdpBytes,'snsifOutUdpBytes':snsifOutUdpBytes,'snsifInIcmpBytes':snsifInIcmpBytes,'snsifOutIcmpBytes':snsifOutIcmpBytes,'snsifProtected':snsifProtected,'snsifDrvName':snsifDrvName,'snsifComment':snsifComment})