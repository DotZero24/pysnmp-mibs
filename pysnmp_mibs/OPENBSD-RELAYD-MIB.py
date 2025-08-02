_N='relaydTableIndex'
_M='relaydSessionIndex'
_L='relaydSessionRelayIndex'
_K='relaydHostIndex'
_J='relaydNetRouteIndex'
_I='relaydRouterIndex'
_H='relaydRelayIndex'
_G='relaydRedirectIndex'
_F='active'
_E='disabled'
_D='OPENBSD-RELAYD-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
openBSD,=mibBuilder.importSymbols('OPENBSD-BASE-MIB','openBSD')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
relaydMIBObjects=ModuleIdentity((1,3,6,1,4,1,30155,3))
if mibBuilder.loadTexts:relaydMIBObjects.setRevisions(('2015-10-15 21:16','2015-10-14 00:00','2014-03-12 00:00'))
_RelaydInfo_ObjectIdentity=ObjectIdentity
relaydInfo=_RelaydInfo_ObjectIdentity((1,3,6,1,4,1,30155,3,2))
_RelaydRedirects_Object=MibTable
relaydRedirects=_RelaydRedirects_Object((1,3,6,1,4,1,30155,3,2,1))
if mibBuilder.loadTexts:relaydRedirects.setStatus(_A)
_RelaydRedirectEntry_Object=MibTableRow
relaydRedirectEntry=_RelaydRedirectEntry_Object((1,3,6,1,4,1,30155,3,2,1,1))
relaydRedirectEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:relaydRedirectEntry.setStatus(_A)
class _RelaydRedirectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydRedirectIndex_Type.__name__=_C
_RelaydRedirectIndex_Object=MibTableColumn
relaydRedirectIndex=_RelaydRedirectIndex_Object((1,3,6,1,4,1,30155,3,2,1,1,1),_RelaydRedirectIndex_Type())
relaydRedirectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectIndex.setStatus(_A)
class _RelaydRedirectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_E,1),('down',2),('backup',3)))
_RelaydRedirectStatus_Type.__name__=_C
_RelaydRedirectStatus_Object=MibTableColumn
relaydRedirectStatus=_RelaydRedirectStatus_Object((1,3,6,1,4,1,30155,3,2,1,1,2),_RelaydRedirectStatus_Type())
relaydRedirectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectStatus.setStatus(_A)
_RelaydRedirectName_Type=OctetString
_RelaydRedirectName_Object=MibTableColumn
relaydRedirectName=_RelaydRedirectName_Object((1,3,6,1,4,1,30155,3,2,1,1,3),_RelaydRedirectName_Type())
relaydRedirectName.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectName.setStatus(_A)
_RelaydRedirectCnt_Type=Counter64
_RelaydRedirectCnt_Object=MibTableColumn
relaydRedirectCnt=_RelaydRedirectCnt_Object((1,3,6,1,4,1,30155,3,2,1,1,4),_RelaydRedirectCnt_Type())
relaydRedirectCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectCnt.setStatus(_A)
_RelaydRedirectAvg_Type=Gauge32
_RelaydRedirectAvg_Object=MibTableColumn
relaydRedirectAvg=_RelaydRedirectAvg_Object((1,3,6,1,4,1,30155,3,2,1,1,5),_RelaydRedirectAvg_Type())
relaydRedirectAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectAvg.setStatus(_A)
_RelaydRedirectLast_Type=Gauge32
_RelaydRedirectLast_Object=MibTableColumn
relaydRedirectLast=_RelaydRedirectLast_Object((1,3,6,1,4,1,30155,3,2,1,1,6),_RelaydRedirectLast_Type())
relaydRedirectLast.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectLast.setStatus(_A)
_RelaydRedirectAvgHour_Type=Gauge32
_RelaydRedirectAvgHour_Object=MibTableColumn
relaydRedirectAvgHour=_RelaydRedirectAvgHour_Object((1,3,6,1,4,1,30155,3,2,1,1,7),_RelaydRedirectAvgHour_Type())
relaydRedirectAvgHour.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectAvgHour.setStatus(_A)
_RelaydRedirectLastHour_Type=Gauge32
_RelaydRedirectLastHour_Object=MibTableColumn
relaydRedirectLastHour=_RelaydRedirectLastHour_Object((1,3,6,1,4,1,30155,3,2,1,1,8),_RelaydRedirectLastHour_Type())
relaydRedirectLastHour.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectLastHour.setStatus(_A)
_RelaydRedirectAvgDay_Type=Gauge32
_RelaydRedirectAvgDay_Object=MibTableColumn
relaydRedirectAvgDay=_RelaydRedirectAvgDay_Object((1,3,6,1,4,1,30155,3,2,1,1,9),_RelaydRedirectAvgDay_Type())
relaydRedirectAvgDay.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectAvgDay.setStatus(_A)
_RelaydRedirectLastDay_Type=Gauge32
_RelaydRedirectLastDay_Object=MibTableColumn
relaydRedirectLastDay=_RelaydRedirectLastDay_Object((1,3,6,1,4,1,30155,3,2,1,1,10),_RelaydRedirectLastDay_Type())
relaydRedirectLastDay.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRedirectLastDay.setStatus(_A)
_RelaydRelays_Object=MibTable
relaydRelays=_RelaydRelays_Object((1,3,6,1,4,1,30155,3,2,2))
if mibBuilder.loadTexts:relaydRelays.setStatus(_A)
_RelaydRelayEntry_Object=MibTableRow
relaydRelayEntry=_RelaydRelayEntry_Object((1,3,6,1,4,1,30155,3,2,2,1))
relaydRelayEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:relaydRelayEntry.setStatus(_A)
class _RelaydRelayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydRelayIndex_Type.__name__=_C
_RelaydRelayIndex_Object=MibTableColumn
relaydRelayIndex=_RelaydRelayIndex_Object((1,3,6,1,4,1,30155,3,2,2,1,1),_RelaydRelayIndex_Type())
relaydRelayIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayIndex.setStatus(_A)
class _RelaydRelayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_RelaydRelayStatus_Type.__name__=_C
_RelaydRelayStatus_Object=MibTableColumn
relaydRelayStatus=_RelaydRelayStatus_Object((1,3,6,1,4,1,30155,3,2,2,1,2),_RelaydRelayStatus_Type())
relaydRelayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayStatus.setStatus(_A)
_RelaydRelayName_Type=OctetString
_RelaydRelayName_Object=MibTableColumn
relaydRelayName=_RelaydRelayName_Object((1,3,6,1,4,1,30155,3,2,2,1,3),_RelaydRelayName_Type())
relaydRelayName.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayName.setStatus(_A)
_RelaydRelayCnt_Type=Counter64
_RelaydRelayCnt_Object=MibTableColumn
relaydRelayCnt=_RelaydRelayCnt_Object((1,3,6,1,4,1,30155,3,2,2,1,4),_RelaydRelayCnt_Type())
relaydRelayCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayCnt.setStatus(_A)
_RelaydRelayAvg_Type=Gauge32
_RelaydRelayAvg_Object=MibTableColumn
relaydRelayAvg=_RelaydRelayAvg_Object((1,3,6,1,4,1,30155,3,2,2,1,5),_RelaydRelayAvg_Type())
relaydRelayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayAvg.setStatus(_A)
_RelaydRelayLast_Type=Gauge32
_RelaydRelayLast_Object=MibTableColumn
relaydRelayLast=_RelaydRelayLast_Object((1,3,6,1,4,1,30155,3,2,2,1,6),_RelaydRelayLast_Type())
relaydRelayLast.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayLast.setStatus(_A)
_RelaydRelayAvgHour_Type=Gauge32
_RelaydRelayAvgHour_Object=MibTableColumn
relaydRelayAvgHour=_RelaydRelayAvgHour_Object((1,3,6,1,4,1,30155,3,2,2,1,7),_RelaydRelayAvgHour_Type())
relaydRelayAvgHour.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayAvgHour.setStatus(_A)
_RelaydRelayLastHour_Type=Gauge32
_RelaydRelayLastHour_Object=MibTableColumn
relaydRelayLastHour=_RelaydRelayLastHour_Object((1,3,6,1,4,1,30155,3,2,2,1,8),_RelaydRelayLastHour_Type())
relaydRelayLastHour.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayLastHour.setStatus(_A)
_RelaydRelayAvgDay_Type=Gauge32
_RelaydRelayAvgDay_Object=MibTableColumn
relaydRelayAvgDay=_RelaydRelayAvgDay_Object((1,3,6,1,4,1,30155,3,2,2,1,9),_RelaydRelayAvgDay_Type())
relaydRelayAvgDay.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayAvgDay.setStatus(_A)
_RelaydRelayLastDay_Type=Gauge32
_RelaydRelayLastDay_Object=MibTableColumn
relaydRelayLastDay=_RelaydRelayLastDay_Object((1,3,6,1,4,1,30155,3,2,2,1,10),_RelaydRelayLastDay_Type())
relaydRelayLastDay.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRelayLastDay.setStatus(_A)
_RelaydRouters_Object=MibTable
relaydRouters=_RelaydRouters_Object((1,3,6,1,4,1,30155,3,2,3))
if mibBuilder.loadTexts:relaydRouters.setStatus(_A)
_RelaydRouterEntry_Object=MibTableRow
relaydRouterEntry=_RelaydRouterEntry_Object((1,3,6,1,4,1,30155,3,2,3,1))
relaydRouterEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:relaydRouterEntry.setStatus(_A)
class _RelaydRouterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydRouterIndex_Type.__name__=_C
_RelaydRouterIndex_Object=MibTableColumn
relaydRouterIndex=_RelaydRouterIndex_Object((1,3,6,1,4,1,30155,3,2,3,1,1),_RelaydRouterIndex_Type())
relaydRouterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRouterIndex.setStatus(_A)
_RelaydRouterTableIndex_Type=Integer32
_RelaydRouterTableIndex_Object=MibTableColumn
relaydRouterTableIndex=_RelaydRouterTableIndex_Object((1,3,6,1,4,1,30155,3,2,3,1,2),_RelaydRouterTableIndex_Type())
relaydRouterTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRouterTableIndex.setStatus(_A)
class _RelaydRouterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_RelaydRouterStatus_Type.__name__=_C
_RelaydRouterStatus_Object=MibTableColumn
relaydRouterStatus=_RelaydRouterStatus_Object((1,3,6,1,4,1,30155,3,2,3,1,3),_RelaydRouterStatus_Type())
relaydRouterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRouterStatus.setStatus(_A)
_RelaydRouterName_Type=OctetString
_RelaydRouterName_Object=MibTableColumn
relaydRouterName=_RelaydRouterName_Object((1,3,6,1,4,1,30155,3,2,3,1,4),_RelaydRouterName_Type())
relaydRouterName.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRouterName.setStatus(_A)
_RelaydRouterLabel_Type=OctetString
_RelaydRouterLabel_Object=MibTableColumn
relaydRouterLabel=_RelaydRouterLabel_Object((1,3,6,1,4,1,30155,3,2,3,1,5),_RelaydRouterLabel_Type())
relaydRouterLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRouterLabel.setStatus(_A)
_RelaydRouterRtable_Type=Integer32
_RelaydRouterRtable_Object=MibTableColumn
relaydRouterRtable=_RelaydRouterRtable_Object((1,3,6,1,4,1,30155,3,2,3,1,6),_RelaydRouterRtable_Type())
relaydRouterRtable.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydRouterRtable.setStatus(_A)
_RelaydNetRoutes_Object=MibTable
relaydNetRoutes=_RelaydNetRoutes_Object((1,3,6,1,4,1,30155,3,2,4))
if mibBuilder.loadTexts:relaydNetRoutes.setStatus(_A)
_RelaydNetRouteEntry_Object=MibTableRow
relaydNetRouteEntry=_RelaydNetRouteEntry_Object((1,3,6,1,4,1,30155,3,2,4,1))
relaydNetRouteEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:relaydNetRouteEntry.setStatus(_A)
class _RelaydNetRouteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydNetRouteIndex_Type.__name__=_C
_RelaydNetRouteIndex_Object=MibTableColumn
relaydNetRouteIndex=_RelaydNetRouteIndex_Object((1,3,6,1,4,1,30155,3,2,4,1,1),_RelaydNetRouteIndex_Type())
relaydNetRouteIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydNetRouteIndex.setStatus(_A)
_RelaydNetRouteAddr_Type=InetAddress
_RelaydNetRouteAddr_Object=MibTableColumn
relaydNetRouteAddr=_RelaydNetRouteAddr_Object((1,3,6,1,4,1,30155,3,2,4,1,2),_RelaydNetRouteAddr_Type())
relaydNetRouteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydNetRouteAddr.setStatus(_A)
_RelaydNetRouteAddrType_Type=InetAddressType
_RelaydNetRouteAddrType_Object=MibTableColumn
relaydNetRouteAddrType=_RelaydNetRouteAddrType_Object((1,3,6,1,4,1,30155,3,2,4,1,3),_RelaydNetRouteAddrType_Type())
relaydNetRouteAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydNetRouteAddrType.setStatus(_A)
_RelaydNetRoutePrefixLen_Type=Integer32
_RelaydNetRoutePrefixLen_Object=MibTableColumn
relaydNetRoutePrefixLen=_RelaydNetRoutePrefixLen_Object((1,3,6,1,4,1,30155,3,2,4,1,4),_RelaydNetRoutePrefixLen_Type())
relaydNetRoutePrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydNetRoutePrefixLen.setStatus(_A)
_RelaydNetRouteRouterIndex_Type=Integer32
_RelaydNetRouteRouterIndex_Object=MibTableColumn
relaydNetRouteRouterIndex=_RelaydNetRouteRouterIndex_Object((1,3,6,1,4,1,30155,3,2,4,1,5),_RelaydNetRouteRouterIndex_Type())
relaydNetRouteRouterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydNetRouteRouterIndex.setStatus(_A)
_RelaydHosts_Object=MibTable
relaydHosts=_RelaydHosts_Object((1,3,6,1,4,1,30155,3,2,5))
if mibBuilder.loadTexts:relaydHosts.setStatus(_A)
_RelaydHostEntry_Object=MibTableRow
relaydHostEntry=_RelaydHostEntry_Object((1,3,6,1,4,1,30155,3,2,5,1))
relaydHostEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:relaydHostEntry.setStatus(_A)
class _RelaydHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydHostIndex_Type.__name__=_C
_RelaydHostIndex_Object=MibTableColumn
relaydHostIndex=_RelaydHostIndex_Object((1,3,6,1,4,1,30155,3,2,5,1,1),_RelaydHostIndex_Type())
relaydHostIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostIndex.setStatus(_A)
_RelaydHostParentIndex_Type=Integer32
_RelaydHostParentIndex_Object=MibTableColumn
relaydHostParentIndex=_RelaydHostParentIndex_Object((1,3,6,1,4,1,30155,3,2,5,1,2),_RelaydHostParentIndex_Type())
relaydHostParentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostParentIndex.setStatus(_A)
_RelaydHostTableIndex_Type=Integer32
_RelaydHostTableIndex_Object=MibTableColumn
relaydHostTableIndex=_RelaydHostTableIndex_Object((1,3,6,1,4,1,30155,3,2,5,1,3),_RelaydHostTableIndex_Type())
relaydHostTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostTableIndex.setStatus(_A)
_RelaydHostName_Type=OctetString
_RelaydHostName_Object=MibTableColumn
relaydHostName=_RelaydHostName_Object((1,3,6,1,4,1,30155,3,2,5,1,4),_RelaydHostName_Type())
relaydHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostName.setStatus(_A)
_RelaydHostAddress_Type=InetAddress
_RelaydHostAddress_Object=MibTableColumn
relaydHostAddress=_RelaydHostAddress_Object((1,3,6,1,4,1,30155,3,2,5,1,5),_RelaydHostAddress_Type())
relaydHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostAddress.setStatus(_A)
_RelaydHostAddressType_Type=InetAddressType
_RelaydHostAddressType_Object=MibTableColumn
relaydHostAddressType=_RelaydHostAddressType_Object((1,3,6,1,4,1,30155,3,2,5,1,6),_RelaydHostAddressType_Type())
relaydHostAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostAddressType.setStatus(_A)
class _RelaydHostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('up',0),(_E,1),('down',2),('unknown',3)))
_RelaydHostStatus_Type.__name__=_C
_RelaydHostStatus_Object=MibTableColumn
relaydHostStatus=_RelaydHostStatus_Object((1,3,6,1,4,1,30155,3,2,5,1,7),_RelaydHostStatus_Type())
relaydHostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostStatus.setStatus(_A)
_RelaydHostCheckCnt_Type=Counter64
_RelaydHostCheckCnt_Object=MibTableColumn
relaydHostCheckCnt=_RelaydHostCheckCnt_Object((1,3,6,1,4,1,30155,3,2,5,1,8),_RelaydHostCheckCnt_Type())
relaydHostCheckCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostCheckCnt.setStatus(_A)
_RelaydHostUpCnt_Type=Counter64
_RelaydHostUpCnt_Object=MibTableColumn
relaydHostUpCnt=_RelaydHostUpCnt_Object((1,3,6,1,4,1,30155,3,2,5,1,9),_RelaydHostUpCnt_Type())
relaydHostUpCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostUpCnt.setStatus(_A)
class _RelaydHostErrno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('none',0),('abort',1),('intervalTimeout',2),('icmpOk',3),('icmpReadTimeout',4),('icmpWriteTimeout',5),('tcpSocketError',6),('tcpSocketLimit',7),('tcpSocketOption',8),('tcpConnectFail',9),('tcpConnectTimeout',10),('tcpConnectOk',11),('tcpWriteTimeout',12),('tcpWriteFail',13),('tcpReadTimeout',14),('tcpReadFail',15),('scriptOk',16),('scriptFail',17),('sslConnectError',18),('sslConnectFail',19),('sslConnectOk',20),('sslConnectTimeout',21),('sslReadTimeout',22),('sslWriteTimeout',23),('sslReadError',24),('sslWriteError',25),('sendExpectFail',26),('sendExpectOk',27),('httpCodeError',28),('httpCodeFail',29),('httpCodeOk',30),('httpDigestError',31),('httpDigestFail',32),('httpDigestOk',33)))
_RelaydHostErrno_Type.__name__=_C
_RelaydHostErrno_Object=MibTableColumn
relaydHostErrno=_RelaydHostErrno_Object((1,3,6,1,4,1,30155,3,2,5,1,10),_RelaydHostErrno_Type())
relaydHostErrno.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydHostErrno.setStatus(_A)
_RelaydSessions_Object=MibTable
relaydSessions=_RelaydSessions_Object((1,3,6,1,4,1,30155,3,2,6))
if mibBuilder.loadTexts:relaydSessions.setStatus(_A)
_RelaydSessionEntry_Object=MibTableRow
relaydSessionEntry=_RelaydSessionEntry_Object((1,3,6,1,4,1,30155,3,2,6,1))
relaydSessionEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:relaydSessionEntry.setStatus(_A)
class _RelaydSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydSessionIndex_Type.__name__=_C
_RelaydSessionIndex_Object=MibTableColumn
relaydSessionIndex=_RelaydSessionIndex_Object((1,3,6,1,4,1,30155,3,2,6,1,1),_RelaydSessionIndex_Type())
relaydSessionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionIndex.setStatus(_A)
class _RelaydSessionRelayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydSessionRelayIndex_Type.__name__=_C
_RelaydSessionRelayIndex_Object=MibTableColumn
relaydSessionRelayIndex=_RelaydSessionRelayIndex_Object((1,3,6,1,4,1,30155,3,2,6,1,2),_RelaydSessionRelayIndex_Type())
relaydSessionRelayIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionRelayIndex.setStatus(_A)
_RelaydSessionInAddr_Type=InetAddress
_RelaydSessionInAddr_Object=MibTableColumn
relaydSessionInAddr=_RelaydSessionInAddr_Object((1,3,6,1,4,1,30155,3,2,6,1,3),_RelaydSessionInAddr_Type())
relaydSessionInAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionInAddr.setStatus(_A)
_RelaydSessionInAddrType_Type=InetAddressType
_RelaydSessionInAddrType_Object=MibTableColumn
relaydSessionInAddrType=_RelaydSessionInAddrType_Object((1,3,6,1,4,1,30155,3,2,6,1,4),_RelaydSessionInAddrType_Type())
relaydSessionInAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionInAddrType.setStatus(_A)
_RelaydSessionOutAddr_Type=InetAddress
_RelaydSessionOutAddr_Object=MibTableColumn
relaydSessionOutAddr=_RelaydSessionOutAddr_Object((1,3,6,1,4,1,30155,3,2,6,1,5),_RelaydSessionOutAddr_Type())
relaydSessionOutAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionOutAddr.setStatus(_A)
_RelaydSessionOutAddrType_Type=InetAddressType
_RelaydSessionOutAddrType_Object=MibTableColumn
relaydSessionOutAddrType=_RelaydSessionOutAddrType_Object((1,3,6,1,4,1,30155,3,2,6,1,6),_RelaydSessionOutAddrType_Type())
relaydSessionOutAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionOutAddrType.setStatus(_A)
_RelaydSessionPortIn_Type=Integer32
_RelaydSessionPortIn_Object=MibTableColumn
relaydSessionPortIn=_RelaydSessionPortIn_Object((1,3,6,1,4,1,30155,3,2,6,1,7),_RelaydSessionPortIn_Type())
relaydSessionPortIn.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionPortIn.setStatus(_A)
_RelaydSessionPortOut_Type=Integer32
_RelaydSessionPortOut_Object=MibTableColumn
relaydSessionPortOut=_RelaydSessionPortOut_Object((1,3,6,1,4,1,30155,3,2,6,1,8),_RelaydSessionPortOut_Type())
relaydSessionPortOut.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionPortOut.setStatus(_A)
_RelaydSessionAge_Type=TimeTicks
_RelaydSessionAge_Object=MibTableColumn
relaydSessionAge=_RelaydSessionAge_Object((1,3,6,1,4,1,30155,3,2,6,1,9),_RelaydSessionAge_Type())
relaydSessionAge.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionAge.setStatus(_A)
_RelaydSessionIdle_Type=TimeTicks
_RelaydSessionIdle_Object=MibTableColumn
relaydSessionIdle=_RelaydSessionIdle_Object((1,3,6,1,4,1,30155,3,2,6,1,10),_RelaydSessionIdle_Type())
relaydSessionIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionIdle.setStatus(_A)
class _RelaydSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('running',0),('done',1)))
_RelaydSessionStatus_Type.__name__=_C
_RelaydSessionStatus_Object=MibTableColumn
relaydSessionStatus=_RelaydSessionStatus_Object((1,3,6,1,4,1,30155,3,2,6,1,11),_RelaydSessionStatus_Type())
relaydSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionStatus.setStatus(_A)
_RelaydSessionPid_Type=Integer32
_RelaydSessionPid_Object=MibTableColumn
relaydSessionPid=_RelaydSessionPid_Object((1,3,6,1,4,1,30155,3,2,6,1,12),_RelaydSessionPid_Type())
relaydSessionPid.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydSessionPid.setStatus(_A)
_RelaydTables_Object=MibTable
relaydTables=_RelaydTables_Object((1,3,6,1,4,1,30155,3,2,7))
if mibBuilder.loadTexts:relaydTables.setStatus(_A)
_RelaydTableEntry_Object=MibTableRow
relaydTableEntry=_RelaydTableEntry_Object((1,3,6,1,4,1,30155,3,2,7,1))
relaydTableEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:relaydTableEntry.setStatus(_A)
class _RelaydTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RelaydTableIndex_Type.__name__=_C
_RelaydTableIndex_Object=MibTableColumn
relaydTableIndex=_RelaydTableIndex_Object((1,3,6,1,4,1,30155,3,2,7,1,1),_RelaydTableIndex_Type())
relaydTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydTableIndex.setStatus(_A)
_RelaydTableName_Type=OctetString
_RelaydTableName_Object=MibTableColumn
relaydTableName=_RelaydTableName_Object((1,3,6,1,4,1,30155,3,2,7,1,2),_RelaydTableName_Type())
relaydTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydTableName.setStatus(_A)
class _RelaydTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('empty',1),(_E,2)))
_RelaydTableStatus_Type.__name__=_C
_RelaydTableStatus_Object=MibTableColumn
relaydTableStatus=_RelaydTableStatus_Object((1,3,6,1,4,1,30155,3,2,7,1,3),_RelaydTableStatus_Type())
relaydTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:relaydTableStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'relaydMIBObjects':relaydMIBObjects,'relaydInfo':relaydInfo,'relaydRedirects':relaydRedirects,'relaydRedirectEntry':relaydRedirectEntry,_G:relaydRedirectIndex,'relaydRedirectStatus':relaydRedirectStatus,'relaydRedirectName':relaydRedirectName,'relaydRedirectCnt':relaydRedirectCnt,'relaydRedirectAvg':relaydRedirectAvg,'relaydRedirectLast':relaydRedirectLast,'relaydRedirectAvgHour':relaydRedirectAvgHour,'relaydRedirectLastHour':relaydRedirectLastHour,'relaydRedirectAvgDay':relaydRedirectAvgDay,'relaydRedirectLastDay':relaydRedirectLastDay,'relaydRelays':relaydRelays,'relaydRelayEntry':relaydRelayEntry,_H:relaydRelayIndex,'relaydRelayStatus':relaydRelayStatus,'relaydRelayName':relaydRelayName,'relaydRelayCnt':relaydRelayCnt,'relaydRelayAvg':relaydRelayAvg,'relaydRelayLast':relaydRelayLast,'relaydRelayAvgHour':relaydRelayAvgHour,'relaydRelayLastHour':relaydRelayLastHour,'relaydRelayAvgDay':relaydRelayAvgDay,'relaydRelayLastDay':relaydRelayLastDay,'relaydRouters':relaydRouters,'relaydRouterEntry':relaydRouterEntry,_I:relaydRouterIndex,'relaydRouterTableIndex':relaydRouterTableIndex,'relaydRouterStatus':relaydRouterStatus,'relaydRouterName':relaydRouterName,'relaydRouterLabel':relaydRouterLabel,'relaydRouterRtable':relaydRouterRtable,'relaydNetRoutes':relaydNetRoutes,'relaydNetRouteEntry':relaydNetRouteEntry,_J:relaydNetRouteIndex,'relaydNetRouteAddr':relaydNetRouteAddr,'relaydNetRouteAddrType':relaydNetRouteAddrType,'relaydNetRoutePrefixLen':relaydNetRoutePrefixLen,'relaydNetRouteRouterIndex':relaydNetRouteRouterIndex,'relaydHosts':relaydHosts,'relaydHostEntry':relaydHostEntry,_K:relaydHostIndex,'relaydHostParentIndex':relaydHostParentIndex,'relaydHostTableIndex':relaydHostTableIndex,'relaydHostName':relaydHostName,'relaydHostAddress':relaydHostAddress,'relaydHostAddressType':relaydHostAddressType,'relaydHostStatus':relaydHostStatus,'relaydHostCheckCnt':relaydHostCheckCnt,'relaydHostUpCnt':relaydHostUpCnt,'relaydHostErrno':relaydHostErrno,'relaydSessions':relaydSessions,'relaydSessionEntry':relaydSessionEntry,_M:relaydSessionIndex,_L:relaydSessionRelayIndex,'relaydSessionInAddr':relaydSessionInAddr,'relaydSessionInAddrType':relaydSessionInAddrType,'relaydSessionOutAddr':relaydSessionOutAddr,'relaydSessionOutAddrType':relaydSessionOutAddrType,'relaydSessionPortIn':relaydSessionPortIn,'relaydSessionPortOut':relaydSessionPortOut,'relaydSessionAge':relaydSessionAge,'relaydSessionIdle':relaydSessionIdle,'relaydSessionStatus':relaydSessionStatus,'relaydSessionPid':relaydSessionPid,'relaydTables':relaydTables,'relaydTableEntry':relaydTableEntry,_N:relaydTableIndex,'relaydTableName':relaydTableName,'relaydTableStatus':relaydTableStatus})