_F='zxAnPppoaIfIndex'
_E='ZTE-AN-PPPOA-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnPppoaMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,35))
_ZxAnPppoaGlobal_ObjectIdentity=ObjectIdentity
zxAnPppoaGlobal=_ZxAnPppoaGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,35,1))
class _ZxAnPppoaEchoTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1800))
_ZxAnPppoaEchoTimeout_Type.__name__=_C
_ZxAnPppoaEchoTimeout_Object=MibScalar
zxAnPppoaEchoTimeout=_ZxAnPppoaEchoTimeout_Object((1,3,6,1,4,1,3902,1015,35,1,1),_ZxAnPppoaEchoTimeout_Type())
zxAnPppoaEchoTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPppoaEchoTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnPppoaEchoTimeout.setUnits('sec')
_ZxAnPppoaInterfaceTable_Object=MibTable
zxAnPppoaInterfaceTable=_ZxAnPppoaInterfaceTable_Object((1,3,6,1,4,1,3902,1015,35,2))
if mibBuilder.loadTexts:zxAnPppoaInterfaceTable.setStatus(_A)
_ZxAnPppoaInterfaceEntry_Object=MibTableRow
zxAnPppoaInterfaceEntry=_ZxAnPppoaInterfaceEntry_Object((1,3,6,1,4,1,3902,1015,35,2,1))
zxAnPppoaInterfaceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnPppoaInterfaceEntry.setStatus(_A)
_ZxAnPppoaIfIndex_Type=ZxAnIfindex
_ZxAnPppoaIfIndex_Object=MibTableColumn
zxAnPppoaIfIndex=_ZxAnPppoaIfIndex_Object((1,3,6,1,4,1,3902,1015,35,2,1,1),_ZxAnPppoaIfIndex_Type())
zxAnPppoaIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnPppoaIfIndex.setStatus(_A)
class _ZxAnPppoaIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnPppoaIfAdminStatus_Type.__name__=_C
_ZxAnPppoaIfAdminStatus_Object=MibTableColumn
zxAnPppoaIfAdminStatus=_ZxAnPppoaIfAdminStatus_Object((1,3,6,1,4,1,3902,1015,35,2,1,2),_ZxAnPppoaIfAdminStatus_Type())
zxAnPppoaIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPppoaIfAdminStatus.setStatus(_A)
class _ZxAnPppoaIfMgmtOperstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('invalidState',1),('waitLcpCfgreq',2),('waitPado',3),('waitPads',4),('waitRetry',5),('pppoeConnnect',6)))
_ZxAnPppoaIfMgmtOperstatus_Type.__name__=_C
_ZxAnPppoaIfMgmtOperstatus_Object=MibTableColumn
zxAnPppoaIfMgmtOperstatus=_ZxAnPppoaIfMgmtOperstatus_Object((1,3,6,1,4,1,3902,1015,35,2,1,3),_ZxAnPppoaIfMgmtOperstatus_Type())
zxAnPppoaIfMgmtOperstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfMgmtOperstatus.setStatus(_A)
_ZxAnPppoaIfSessionId_Type=Integer32
_ZxAnPppoaIfSessionId_Object=MibTableColumn
zxAnPppoaIfSessionId=_ZxAnPppoaIfSessionId_Object((1,3,6,1,4,1,3902,1015,35,2,1,4),_ZxAnPppoaIfSessionId_Type())
zxAnPppoaIfSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfSessionId.setStatus(_A)
_ZxAnPppoaIfServerMac_Type=MacAddress
_ZxAnPppoaIfServerMac_Object=MibTableColumn
zxAnPppoaIfServerMac=_ZxAnPppoaIfServerMac_Object((1,3,6,1,4,1,3902,1015,35,2,1,5),_ZxAnPppoaIfServerMac_Type())
zxAnPppoaIfServerMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfServerMac.setStatus(_A)
_ZxAnPppoaIfLcpCfgReqPkts_Type=Counter32
_ZxAnPppoaIfLcpCfgReqPkts_Object=MibTableColumn
zxAnPppoaIfLcpCfgReqPkts=_ZxAnPppoaIfLcpCfgReqPkts_Object((1,3,6,1,4,1,3902,1015,35,2,1,6),_ZxAnPppoaIfLcpCfgReqPkts_Type())
zxAnPppoaIfLcpCfgReqPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfLcpCfgReqPkts.setStatus(_A)
_ZxAnPppoaIfEchoAckPkts_Type=Counter32
_ZxAnPppoaIfEchoAckPkts_Object=MibTableColumn
zxAnPppoaIfEchoAckPkts=_ZxAnPppoaIfEchoAckPkts_Object((1,3,6,1,4,1,3902,1015,35,2,1,7),_ZxAnPppoaIfEchoAckPkts_Type())
zxAnPppoaIfEchoAckPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfEchoAckPkts.setStatus(_A)
_ZxAnPppoaIfLcpTerminateReqPkts_Type=Counter32
_ZxAnPppoaIfLcpTerminateReqPkts_Object=MibTableColumn
zxAnPppoaIfLcpTerminateReqPkts=_ZxAnPppoaIfLcpTerminateReqPkts_Object((1,3,6,1,4,1,3902,1015,35,2,1,8),_ZxAnPppoaIfLcpTerminateReqPkts_Type())
zxAnPppoaIfLcpTerminateReqPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfLcpTerminateReqPkts.setStatus(_A)
_ZxAnPppoaIfPadoPkts_Type=Counter32
_ZxAnPppoaIfPadoPkts_Object=MibTableColumn
zxAnPppoaIfPadoPkts=_ZxAnPppoaIfPadoPkts_Object((1,3,6,1,4,1,3902,1015,35,2,1,9),_ZxAnPppoaIfPadoPkts_Type())
zxAnPppoaIfPadoPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfPadoPkts.setStatus(_A)
_ZxAnPppoaIfPadsPkts_Type=Counter32
_ZxAnPppoaIfPadsPkts_Object=MibTableColumn
zxAnPppoaIfPadsPkts=_ZxAnPppoaIfPadsPkts_Object((1,3,6,1,4,1,3902,1015,35,2,1,10),_ZxAnPppoaIfPadsPkts_Type())
zxAnPppoaIfPadsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfPadsPkts.setStatus(_A)
_ZxAnPppoaIfPadtPkts_Type=Counter32
_ZxAnPppoaIfPadtPkts_Object=MibTableColumn
zxAnPppoaIfPadtPkts=_ZxAnPppoaIfPadtPkts_Object((1,3,6,1,4,1,3902,1015,35,2,1,11),_ZxAnPppoaIfPadtPkts_Type())
zxAnPppoaIfPadtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPppoaIfPadtPkts.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxAnPppoaMib':zxAnPppoaMib,'zxAnPppoaGlobal':zxAnPppoaGlobal,'zxAnPppoaEchoTimeout':zxAnPppoaEchoTimeout,'zxAnPppoaInterfaceTable':zxAnPppoaInterfaceTable,'zxAnPppoaInterfaceEntry':zxAnPppoaInterfaceEntry,_F:zxAnPppoaIfIndex,'zxAnPppoaIfAdminStatus':zxAnPppoaIfAdminStatus,'zxAnPppoaIfMgmtOperstatus':zxAnPppoaIfMgmtOperstatus,'zxAnPppoaIfSessionId':zxAnPppoaIfSessionId,'zxAnPppoaIfServerMac':zxAnPppoaIfServerMac,'zxAnPppoaIfLcpCfgReqPkts':zxAnPppoaIfLcpCfgReqPkts,'zxAnPppoaIfEchoAckPkts':zxAnPppoaIfEchoAckPkts,'zxAnPppoaIfLcpTerminateReqPkts':zxAnPppoaIfLcpTerminateReqPkts,'zxAnPppoaIfPadoPkts':zxAnPppoaIfPadoPkts,'zxAnPppoaIfPadsPkts':zxAnPppoaIfPadsPkts,'zxAnPppoaIfPadtPkts':zxAnPppoaIfPadtPkts})