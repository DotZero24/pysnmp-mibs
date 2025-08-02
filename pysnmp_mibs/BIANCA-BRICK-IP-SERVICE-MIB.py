_Y='localIcmpAllowType'
_X='localIcmpAllowAddr'
_W='localUdpLimitService'
_V='exceeded'
_U='inactive'
_T='active'
_S='localTcpLimitService'
_R='statmon'
_Q='bootps'
_P='localUdpAllowService'
_O='localUdpAllowAddr'
_N='rfc1086'
_M='telnet'
_L='localTcpAllowService'
_K='localTcpAllowAddr'
_J='Counter32'
_I='read-only'
_H='snmp'
_G='delete'
_F='verify'
_E='dont-verify'
_D='BIANCA-BRICK-IP-SERVICE-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_J,'Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_Biboipsrv_ObjectIdentity=ObjectIdentity
biboipsrv=_Biboipsrv_ObjectIdentity((1,3,6,1,4,1,272,4,5,14))
_LocalTcpAllowTable_Object=MibTable
localTcpAllowTable=_LocalTcpAllowTable_Object((1,3,6,1,4,1,272,4,5,14,1))
if mibBuilder.loadTexts:localTcpAllowTable.setStatus(_A)
_LocalTcpAllowEntry_Object=MibTableRow
localTcpAllowEntry=_LocalTcpAllowEntry_Object((1,3,6,1,4,1,272,4,5,14,1,1))
localTcpAllowEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:localTcpAllowEntry.setStatus(_A)
class _LocalTcpAllowAddrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_LocalTcpAllowAddrMode_Type.__name__=_C
_LocalTcpAllowAddrMode_Object=MibTableColumn
localTcpAllowAddrMode=_LocalTcpAllowAddrMode_Object((1,3,6,1,4,1,272,4,5,14,1,1,1),_LocalTcpAllowAddrMode_Type())
localTcpAllowAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpAllowAddrMode.setStatus(_A)
_LocalTcpAllowAddr_Type=IpAddress
_LocalTcpAllowAddr_Object=MibTableColumn
localTcpAllowAddr=_LocalTcpAllowAddr_Object((1,3,6,1,4,1,272,4,5,14,1,1,2),_LocalTcpAllowAddr_Type())
localTcpAllowAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpAllowAddr.setStatus(_A)
_LocalTcpAllowMask_Type=IpAddress
_LocalTcpAllowMask_Object=MibTableColumn
localTcpAllowMask=_LocalTcpAllowMask_Object((1,3,6,1,4,1,272,4,5,14,1,1,3),_LocalTcpAllowMask_Type())
localTcpAllowMask.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpAllowMask.setStatus(_A)
class _LocalTcpAllowIfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_LocalTcpAllowIfMode_Type.__name__=_C
_LocalTcpAllowIfMode_Object=MibTableColumn
localTcpAllowIfMode=_LocalTcpAllowIfMode_Object((1,3,6,1,4,1,272,4,5,14,1,1,4),_LocalTcpAllowIfMode_Type())
localTcpAllowIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpAllowIfMode.setStatus(_A)
_LocalTcpAllowIfIndex_Type=Integer32
_LocalTcpAllowIfIndex_Object=MibTableColumn
localTcpAllowIfIndex=_LocalTcpAllowIfIndex_Object((1,3,6,1,4,1,272,4,5,14,1,1,5),_LocalTcpAllowIfIndex_Type())
localTcpAllowIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpAllowIfIndex.setStatus(_A)
class _LocalTcpAllowService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_M,1),('trace',2),(_H,3),('capi',4),('tapi',5),(_N,6),('http',7),('https',8),('ssh',9)))
_LocalTcpAllowService_Type.__name__=_C
_LocalTcpAllowService_Object=MibTableColumn
localTcpAllowService=_LocalTcpAllowService_Object((1,3,6,1,4,1,272,4,5,14,1,1,6),_LocalTcpAllowService_Type())
localTcpAllowService.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpAllowService.setStatus(_A)
_LocalUdpAllowTable_Object=MibTable
localUdpAllowTable=_LocalUdpAllowTable_Object((1,3,6,1,4,1,272,4,5,14,2))
if mibBuilder.loadTexts:localUdpAllowTable.setStatus(_A)
_LocalUdpAllowEntry_Object=MibTableRow
localUdpAllowEntry=_LocalUdpAllowEntry_Object((1,3,6,1,4,1,272,4,5,14,2,1))
localUdpAllowEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:localUdpAllowEntry.setStatus(_A)
class _LocalUdpAllowAddrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_LocalUdpAllowAddrMode_Type.__name__=_C
_LocalUdpAllowAddrMode_Object=MibTableColumn
localUdpAllowAddrMode=_LocalUdpAllowAddrMode_Object((1,3,6,1,4,1,272,4,5,14,2,1,1),_LocalUdpAllowAddrMode_Type())
localUdpAllowAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpAllowAddrMode.setStatus(_A)
_LocalUdpAllowAddr_Type=IpAddress
_LocalUdpAllowAddr_Object=MibTableColumn
localUdpAllowAddr=_LocalUdpAllowAddr_Object((1,3,6,1,4,1,272,4,5,14,2,1,2),_LocalUdpAllowAddr_Type())
localUdpAllowAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpAllowAddr.setStatus(_A)
_LocalUdpAllowMask_Type=IpAddress
_LocalUdpAllowMask_Object=MibTableColumn
localUdpAllowMask=_LocalUdpAllowMask_Object((1,3,6,1,4,1,272,4,5,14,2,1,3),_LocalUdpAllowMask_Type())
localUdpAllowMask.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpAllowMask.setStatus(_A)
class _LocalUdpAllowIfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_LocalUdpAllowIfMode_Type.__name__=_C
_LocalUdpAllowIfMode_Object=MibTableColumn
localUdpAllowIfMode=_LocalUdpAllowIfMode_Object((1,3,6,1,4,1,272,4,5,14,2,1,4),_LocalUdpAllowIfMode_Type())
localUdpAllowIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpAllowIfMode.setStatus(_A)
_LocalUdpAllowIfIndex_Type=Integer32
_LocalUdpAllowIfIndex_Object=MibTableColumn
localUdpAllowIfIndex=_LocalUdpAllowIfIndex_Object((1,3,6,1,4,1,272,4,5,14,2,1,5),_LocalUdpAllowIfIndex_Type())
localUdpAllowIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpAllowIfIndex.setStatus(_A)
class _LocalUdpAllowService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('rip',2),(_Q,3),('dns',4),('nbns',5),(_R,6)))
_LocalUdpAllowService_Type.__name__=_C
_LocalUdpAllowService_Object=MibTableColumn
localUdpAllowService=_LocalUdpAllowService_Object((1,3,6,1,4,1,272,4,5,14,2,1,6),_LocalUdpAllowService_Type())
localUdpAllowService.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpAllowService.setStatus(_A)
_LocalTcpLimitTable_Object=MibTable
localTcpLimitTable=_LocalTcpLimitTable_Object((1,3,6,1,4,1,272,4,5,14,3))
if mibBuilder.loadTexts:localTcpLimitTable.setStatus(_A)
_LocalTcpLimitEntry_Object=MibTableRow
localTcpLimitEntry=_LocalTcpLimitEntry_Object((1,3,6,1,4,1,272,4,5,14,3,1))
localTcpLimitEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:localTcpLimitEntry.setStatus(_A)
class _LocalTcpLimitAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_U,2),(_G,3)))
_LocalTcpLimitAdminState_Type.__name__=_C
_LocalTcpLimitAdminState_Object=MibTableColumn
localTcpLimitAdminState=_LocalTcpLimitAdminState_Object((1,3,6,1,4,1,272,4,5,14,3,1,1),_LocalTcpLimitAdminState_Type())
localTcpLimitAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpLimitAdminState.setStatus(_A)
class _LocalTcpLimitService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_M,1),('trace',2),(_H,3),('capi',4),('tapi',5),(_N,6),('http',7),('https',8),('ssh',9)))
_LocalTcpLimitService_Type.__name__=_C
_LocalTcpLimitService_Object=MibTableColumn
localTcpLimitService=_LocalTcpLimitService_Object((1,3,6,1,4,1,272,4,5,14,3,1,2),_LocalTcpLimitService_Type())
localTcpLimitService.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpLimitService.setStatus(_A)
class _LocalTcpLimitMaxSessions_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_LocalTcpLimitMaxSessions_Type.__name__=_C
_LocalTcpLimitMaxSessions_Object=MibTableColumn
localTcpLimitMaxSessions=_LocalTcpLimitMaxSessions_Object((1,3,6,1,4,1,272,4,5,14,3,1,3),_LocalTcpLimitMaxSessions_Type())
localTcpLimitMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:localTcpLimitMaxSessions.setStatus(_A)
class _LocalTcpLimitCurSessions_Type(Counter32):defaultValue=0
_LocalTcpLimitCurSessions_Type.__name__=_J
_LocalTcpLimitCurSessions_Object=MibTableColumn
localTcpLimitCurSessions=_LocalTcpLimitCurSessions_Object((1,3,6,1,4,1,272,4,5,14,3,1,4),_LocalTcpLimitCurSessions_Type())
localTcpLimitCurSessions.setMaxAccess(_I)
if mibBuilder.loadTexts:localTcpLimitCurSessions.setStatus(_A)
class _LocalTcpLimitState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('below',1),(_V,2)))
_LocalTcpLimitState_Type.__name__=_C
_LocalTcpLimitState_Object=MibTableColumn
localTcpLimitState=_LocalTcpLimitState_Object((1,3,6,1,4,1,272,4,5,14,3,1,5),_LocalTcpLimitState_Type())
localTcpLimitState.setMaxAccess(_I)
if mibBuilder.loadTexts:localTcpLimitState.setStatus(_A)
_LocalUdpLimitTable_Object=MibTable
localUdpLimitTable=_LocalUdpLimitTable_Object((1,3,6,1,4,1,272,4,5,14,4))
if mibBuilder.loadTexts:localUdpLimitTable.setStatus(_A)
_LocalUdpLimitEntry_Object=MibTableRow
localUdpLimitEntry=_LocalUdpLimitEntry_Object((1,3,6,1,4,1,272,4,5,14,4,1))
localUdpLimitEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:localUdpLimitEntry.setStatus(_A)
class _LocalUdpLimitAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_U,2),(_G,3)))
_LocalUdpLimitAdminState_Type.__name__=_C
_LocalUdpLimitAdminState_Object=MibTableColumn
localUdpLimitAdminState=_LocalUdpLimitAdminState_Object((1,3,6,1,4,1,272,4,5,14,4,1,1),_LocalUdpLimitAdminState_Type())
localUdpLimitAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpLimitAdminState.setStatus(_A)
class _LocalUdpLimitService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('rip',2),(_Q,3),('dns',4),('nbns',5),(_R,6)))
_LocalUdpLimitService_Type.__name__=_C
_LocalUdpLimitService_Object=MibTableColumn
localUdpLimitService=_LocalUdpLimitService_Object((1,3,6,1,4,1,272,4,5,14,4,1,2),_LocalUdpLimitService_Type())
localUdpLimitService.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpLimitService.setStatus(_A)
class _LocalUdpLimitMaxRate_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_LocalUdpLimitMaxRate_Type.__name__=_C
_LocalUdpLimitMaxRate_Object=MibTableColumn
localUdpLimitMaxRate=_LocalUdpLimitMaxRate_Object((1,3,6,1,4,1,272,4,5,14,4,1,3),_LocalUdpLimitMaxRate_Type())
localUdpLimitMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:localUdpLimitMaxRate.setStatus(_A)
class _LocalUdpLimitCurRate_Type(Counter32):defaultValue=0
_LocalUdpLimitCurRate_Type.__name__=_J
_LocalUdpLimitCurRate_Object=MibTableColumn
localUdpLimitCurRate=_LocalUdpLimitCurRate_Object((1,3,6,1,4,1,272,4,5,14,4,1,4),_LocalUdpLimitCurRate_Type())
localUdpLimitCurRate.setMaxAccess(_I)
if mibBuilder.loadTexts:localUdpLimitCurRate.setStatus(_A)
class _LocalUdpLimitState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('below',1),(_V,2)))
_LocalUdpLimitState_Type.__name__=_C
_LocalUdpLimitState_Object=MibTableColumn
localUdpLimitState=_LocalUdpLimitState_Object((1,3,6,1,4,1,272,4,5,14,4,1,5),_LocalUdpLimitState_Type())
localUdpLimitState.setMaxAccess(_I)
if mibBuilder.loadTexts:localUdpLimitState.setStatus(_A)
_LocalIcmpAllowTable_Object=MibTable
localIcmpAllowTable=_LocalIcmpAllowTable_Object((1,3,6,1,4,1,272,4,5,14,5))
if mibBuilder.loadTexts:localIcmpAllowTable.setStatus(_A)
_LocalIcmpAllowEntry_Object=MibTableRow
localIcmpAllowEntry=_LocalIcmpAllowEntry_Object((1,3,6,1,4,1,272,4,5,14,5,1))
localIcmpAllowEntry.setIndexNames((0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:localIcmpAllowEntry.setStatus(_A)
class _LocalIcmpAllowAddrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_LocalIcmpAllowAddrMode_Type.__name__=_C
_LocalIcmpAllowAddrMode_Object=MibTableColumn
localIcmpAllowAddrMode=_LocalIcmpAllowAddrMode_Object((1,3,6,1,4,1,272,4,5,14,5,1,1),_LocalIcmpAllowAddrMode_Type())
localIcmpAllowAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:localIcmpAllowAddrMode.setStatus(_A)
_LocalIcmpAllowAddr_Type=IpAddress
_LocalIcmpAllowAddr_Object=MibTableColumn
localIcmpAllowAddr=_LocalIcmpAllowAddr_Object((1,3,6,1,4,1,272,4,5,14,5,1,2),_LocalIcmpAllowAddr_Type())
localIcmpAllowAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:localIcmpAllowAddr.setStatus(_A)
_LocalIcmpAllowMask_Type=IpAddress
_LocalIcmpAllowMask_Object=MibTableColumn
localIcmpAllowMask=_LocalIcmpAllowMask_Object((1,3,6,1,4,1,272,4,5,14,5,1,3),_LocalIcmpAllowMask_Type())
localIcmpAllowMask.setMaxAccess(_B)
if mibBuilder.loadTexts:localIcmpAllowMask.setStatus(_A)
class _LocalIcmpAllowIfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_LocalIcmpAllowIfMode_Type.__name__=_C
_LocalIcmpAllowIfMode_Object=MibTableColumn
localIcmpAllowIfMode=_LocalIcmpAllowIfMode_Object((1,3,6,1,4,1,272,4,5,14,5,1,4),_LocalIcmpAllowIfMode_Type())
localIcmpAllowIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:localIcmpAllowIfMode.setStatus(_A)
_LocalIcmpAllowIfIndex_Type=Integer32
_LocalIcmpAllowIfIndex_Object=MibTableColumn
localIcmpAllowIfIndex=_LocalIcmpAllowIfIndex_Object((1,3,6,1,4,1,272,4,5,14,5,1,5),_LocalIcmpAllowIfIndex_Type())
localIcmpAllowIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:localIcmpAllowIfIndex.setStatus(_A)
class _LocalIcmpAllowType_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6,9,12,13,14,15,18,19)));namedValues=NamedValues(*(('echoRep',1),('destUnreach',4),('srcQuench',5),('redirect',6),('echo',9),('timeExcds',12),('parmProb',13),('timestamp',14),('timestampRep',15),('addrMask',18),('addrMaskRep',19)))
_LocalIcmpAllowType_Type.__name__=_C
_LocalIcmpAllowType_Object=MibTableColumn
localIcmpAllowType=_LocalIcmpAllowType_Object((1,3,6,1,4,1,272,4,5,14,5,1,6),_LocalIcmpAllowType_Type())
localIcmpAllowType.setMaxAccess(_B)
if mibBuilder.loadTexts:localIcmpAllowType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'biboipsrv':biboipsrv,'localTcpAllowTable':localTcpAllowTable,'localTcpAllowEntry':localTcpAllowEntry,'localTcpAllowAddrMode':localTcpAllowAddrMode,_K:localTcpAllowAddr,'localTcpAllowMask':localTcpAllowMask,'localTcpAllowIfMode':localTcpAllowIfMode,'localTcpAllowIfIndex':localTcpAllowIfIndex,_L:localTcpAllowService,'localUdpAllowTable':localUdpAllowTable,'localUdpAllowEntry':localUdpAllowEntry,'localUdpAllowAddrMode':localUdpAllowAddrMode,_O:localUdpAllowAddr,'localUdpAllowMask':localUdpAllowMask,'localUdpAllowIfMode':localUdpAllowIfMode,'localUdpAllowIfIndex':localUdpAllowIfIndex,_P:localUdpAllowService,'localTcpLimitTable':localTcpLimitTable,'localTcpLimitEntry':localTcpLimitEntry,'localTcpLimitAdminState':localTcpLimitAdminState,_S:localTcpLimitService,'localTcpLimitMaxSessions':localTcpLimitMaxSessions,'localTcpLimitCurSessions':localTcpLimitCurSessions,'localTcpLimitState':localTcpLimitState,'localUdpLimitTable':localUdpLimitTable,'localUdpLimitEntry':localUdpLimitEntry,'localUdpLimitAdminState':localUdpLimitAdminState,_W:localUdpLimitService,'localUdpLimitMaxRate':localUdpLimitMaxRate,'localUdpLimitCurRate':localUdpLimitCurRate,'localUdpLimitState':localUdpLimitState,'localIcmpAllowTable':localIcmpAllowTable,'localIcmpAllowEntry':localIcmpAllowEntry,'localIcmpAllowAddrMode':localIcmpAllowAddrMode,_X:localIcmpAllowAddr,'localIcmpAllowMask':localIcmpAllowMask,'localIcmpAllowIfMode':localIcmpAllowIfMode,'localIcmpAllowIfIndex':localIcmpAllowIfIndex,_Y:localIcmpAllowType})