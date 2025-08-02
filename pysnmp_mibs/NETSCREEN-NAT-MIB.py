_N='nsNatDipPPortIndex'
_M='nsNatVipServerIndex'
_L='weighted-least-conns'
_K='least-conns'
_J='weighted-round-robin'
_I='round-robin'
_H='nsNatVipCfgIndex'
_G='nsNatDipIndex'
_F='nsNatMipIndex'
_E='DisplayString'
_D='NETSCREEN-NAT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenNAT,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenNAT')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
netscreenNATMibModule=ModuleIdentity((1,3,6,1,4,1,3224,11,0))
if mibBuilder.loadTexts:netscreenNATMibModule.setRevisions(('2005-03-03 00:00','2004-05-03 00:00','2004-03-03 00:00','2003-06-03 00:00','2001-05-27 00:00'))
_NsNatMipTable_Object=MibTable
nsNatMipTable=_NsNatMipTable_Object((1,3,6,1,4,1,3224,11,1))
if mibBuilder.loadTexts:nsNatMipTable.setStatus(_A)
_NsNatMipEntry_Object=MibTableRow
nsNatMipEntry=_NsNatMipEntry_Object((1,3,6,1,4,1,3224,11,1,1))
nsNatMipEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:nsNatMipEntry.setStatus(_A)
class _NsNatMipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsNatMipIndex_Type.__name__=_C
_NsNatMipIndex_Object=MibTableColumn
nsNatMipIndex=_NsNatMipIndex_Object((1,3,6,1,4,1,3224,11,1,1,1),_NsNatMipIndex_Type())
nsNatMipIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipIndex.setStatus(_A)
_NsNatMipIp_Type=IpAddress
_NsNatMipIp_Object=MibTableColumn
nsNatMipIp=_NsNatMipIp_Object((1,3,6,1,4,1,3224,11,1,1,2),_NsNatMipIp_Type())
nsNatMipIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipIp.setStatus(_A)
_NsNatMipNetmask_Type=IpAddress
_NsNatMipNetmask_Object=MibTableColumn
nsNatMipNetmask=_NsNatMipNetmask_Object((1,3,6,1,4,1,3224,11,1,1,3),_NsNatMipNetmask_Type())
nsNatMipNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipNetmask.setStatus(_A)
_NsNatMipHost_Type=IpAddress
_NsNatMipHost_Object=MibTableColumn
nsNatMipHost=_NsNatMipHost_Object((1,3,6,1,4,1,3224,11,1,1,4),_NsNatMipHost_Type())
nsNatMipHost.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipHost.setStatus(_A)
_NsNatMipIfIp_Type=IpAddress
_NsNatMipIfIp_Object=MibTableColumn
nsNatMipIfIp=_NsNatMipIfIp_Object((1,3,6,1,4,1,3224,11,1,1,5),_NsNatMipIfIp_Type())
nsNatMipIfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipIfIp.setStatus(_A)
_NsNatMipIfNetmask_Type=IpAddress
_NsNatMipIfNetmask_Object=MibTableColumn
nsNatMipIfNetmask=_NsNatMipIfNetmask_Object((1,3,6,1,4,1,3224,11,1,1,6),_NsNatMipIfNetmask_Type())
nsNatMipIfNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipIfNetmask.setStatus(_A)
_NsNatMipVsys_Type=Integer32
_NsNatMipVsys_Object=MibTableColumn
nsNatMipVsys=_NsNatMipVsys_Object((1,3,6,1,4,1,3224,11,1,1,7),_NsNatMipVsys_Type())
nsNatMipVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatMipVsys.setStatus(_A)
_NsNatDipTable_Object=MibTable
nsNatDipTable=_NsNatDipTable_Object((1,3,6,1,4,1,3224,11,2))
if mibBuilder.loadTexts:nsNatDipTable.setStatus(_A)
_NsNatDipEntry_Object=MibTableRow
nsNatDipEntry=_NsNatDipEntry_Object((1,3,6,1,4,1,3224,11,2,1))
nsNatDipEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:nsNatDipEntry.setStatus(_A)
class _NsNatDipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsNatDipIndex_Type.__name__=_C
_NsNatDipIndex_Object=MibTableColumn
nsNatDipIndex=_NsNatDipIndex_Object((1,3,6,1,4,1,3224,11,2,1,1),_NsNatDipIndex_Type())
nsNatDipIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipIndex.setStatus(_A)
_NsNatDipId_Type=Integer32
_NsNatDipId_Object=MibTableColumn
nsNatDipId=_NsNatDipId_Object((1,3,6,1,4,1,3224,11,2,1,2),_NsNatDipId_Type())
nsNatDipId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipId.setStatus(_A)
_NsNatDipLow_Type=IpAddress
_NsNatDipLow_Object=MibTableColumn
nsNatDipLow=_NsNatDipLow_Object((1,3,6,1,4,1,3224,11,2,1,3),_NsNatDipLow_Type())
nsNatDipLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipLow.setStatus(_A)
_NsNatDipHigh_Type=IpAddress
_NsNatDipHigh_Object=MibTableColumn
nsNatDipHigh=_NsNatDipHigh_Object((1,3,6,1,4,1,3224,11,2,1,4),_NsNatDipHigh_Type())
nsNatDipHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipHigh.setStatus(_A)
_NsNatDipIfIp_Type=IpAddress
_NsNatDipIfIp_Object=MibTableColumn
nsNatDipIfIp=_NsNatDipIfIp_Object((1,3,6,1,4,1,3224,11,2,1,5),_NsNatDipIfIp_Type())
nsNatDipIfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipIfIp.setStatus(_A)
_NsNatDipIfNetmask_Type=IpAddress
_NsNatDipIfNetmask_Object=MibTableColumn
nsNatDipIfNetmask=_NsNatDipIfNetmask_Object((1,3,6,1,4,1,3224,11,2,1,6),_NsNatDipIfNetmask_Type())
nsNatDipIfNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipIfNetmask.setStatus(_A)
class _NsNatDipPTEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsNatDipPTEnable_Type.__name__=_C
_NsNatDipPTEnable_Object=MibTableColumn
nsNatDipPTEnable=_NsNatDipPTEnable_Object((1,3,6,1,4,1,3224,11,2,1,7),_NsNatDipPTEnable_Type())
nsNatDipPTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipPTEnable.setStatus(_A)
_NsNatDipVsys_Type=Integer32
_NsNatDipVsys_Object=MibTableColumn
nsNatDipVsys=_NsNatDipVsys_Object((1,3,6,1,4,1,3224,11,2,1,8),_NsNatDipVsys_Type())
nsNatDipVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipVsys.setStatus(_A)
_NsNatDipUtil_Type=Integer32
_NsNatDipUtil_Object=MibTableColumn
nsNatDipUtil=_NsNatDipUtil_Object((1,3,6,1,4,1,3224,11,2,1,9),_NsNatDipUtil_Type())
nsNatDipUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipUtil.setStatus(_A)
_NsNatVip_ObjectIdentity=ObjectIdentity
nsNatVip=_NsNatVip_ObjectIdentity((1,3,6,1,4,1,3224,11,3))
_NsNatVipCfgTable_Object=MibTable
nsNatVipCfgTable=_NsNatVipCfgTable_Object((1,3,6,1,4,1,3224,11,3,1))
if mibBuilder.loadTexts:nsNatVipCfgTable.setStatus(_A)
_NsNatVipCfgEntry_Object=MibTableRow
nsNatVipCfgEntry=_NsNatVipCfgEntry_Object((1,3,6,1,4,1,3224,11,3,1,1))
nsNatVipCfgEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:nsNatVipCfgEntry.setStatus(_A)
class _NsNatVipCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsNatVipCfgIndex_Type.__name__=_C
_NsNatVipCfgIndex_Object=MibTableColumn
nsNatVipCfgIndex=_NsNatVipCfgIndex_Object((1,3,6,1,4,1,3224,11,3,1,1,1),_NsNatVipCfgIndex_Type())
nsNatVipCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipCfgIndex.setStatus(_A)
_NsNatVipCfgIp_Type=IpAddress
_NsNatVipCfgIp_Object=MibTableColumn
nsNatVipCfgIp=_NsNatVipCfgIp_Object((1,3,6,1,4,1,3224,11,3,1,1,2),_NsNatVipCfgIp_Type())
nsNatVipCfgIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipCfgIp.setStatus(_A)
_NsNatVipCfgPort_Type=Integer32
_NsNatVipCfgPort_Object=MibTableColumn
nsNatVipCfgPort=_NsNatVipCfgPort_Object((1,3,6,1,4,1,3224,11,3,1,1,3),_NsNatVipCfgPort_Type())
nsNatVipCfgPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipCfgPort.setStatus(_A)
class _NsNatVipCfgService_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsNatVipCfgService_Type.__name__=_E
_NsNatVipCfgService_Object=MibTableColumn
nsNatVipCfgService=_NsNatVipCfgService_Object((1,3,6,1,4,1,3224,11,3,1,1,4),_NsNatVipCfgService_Type())
nsNatVipCfgService.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipCfgService.setStatus(_A)
class _NsNatVipCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-available',0),('available',1)))
_NsNatVipCfgStatus_Type.__name__=_C
_NsNatVipCfgStatus_Object=MibTableColumn
nsNatVipCfgStatus=_NsNatVipCfgStatus_Object((1,3,6,1,4,1,3224,11,3,1,1,5),_NsNatVipCfgStatus_Type())
nsNatVipCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipCfgStatus.setStatus(_A)
class _NsNatVipCfgLoadBalance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('null',0),(_I,1),(_J,2),(_K,3),(_L,4)))
_NsNatVipCfgLoadBalance_Type.__name__=_C
_NsNatVipCfgLoadBalance_Object=MibTableColumn
nsNatVipCfgLoadBalance=_NsNatVipCfgLoadBalance_Object((1,3,6,1,4,1,3224,11,3,1,1,6),_NsNatVipCfgLoadBalance_Type())
nsNatVipCfgLoadBalance.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipCfgLoadBalance.setStatus(_A)
_NsNatVipServerTable_Object=MibTable
nsNatVipServerTable=_NsNatVipServerTable_Object((1,3,6,1,4,1,3224,11,3,2))
if mibBuilder.loadTexts:nsNatVipServerTable.setStatus(_A)
_NsNatVipServerEntry_Object=MibTableRow
nsNatVipServerEntry=_NsNatVipServerEntry_Object((1,3,6,1,4,1,3224,11,3,2,1))
nsNatVipServerEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:nsNatVipServerEntry.setStatus(_A)
class _NsNatVipServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsNatVipServerIndex_Type.__name__=_C
_NsNatVipServerIndex_Object=MibTableColumn
nsNatVipServerIndex=_NsNatVipServerIndex_Object((1,3,6,1,4,1,3224,11,3,2,1,1),_NsNatVipServerIndex_Type())
nsNatVipServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerIndex.setStatus(_A)
_NsNatVipServerVIP_Type=IpAddress
_NsNatVipServerVIP_Object=MibTableColumn
nsNatVipServerVIP=_NsNatVipServerVIP_Object((1,3,6,1,4,1,3224,11,3,2,1,2),_NsNatVipServerVIP_Type())
nsNatVipServerVIP.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerVIP.setStatus(_A)
_NsNatVipServerService_Type=Integer32
_NsNatVipServerService_Object=MibTableColumn
nsNatVipServerService=_NsNatVipServerService_Object((1,3,6,1,4,1,3224,11,3,2,1,3),_NsNatVipServerService_Type())
nsNatVipServerService.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerService.setStatus(_A)
class _NsNatVipServerLoadBalance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('null',0),(_I,1),(_J,2),(_K,3),(_L,4)))
_NsNatVipServerLoadBalance_Type.__name__=_C
_NsNatVipServerLoadBalance_Object=MibTableColumn
nsNatVipServerLoadBalance=_NsNatVipServerLoadBalance_Object((1,3,6,1,4,1,3224,11,3,2,1,4),_NsNatVipServerLoadBalance_Type())
nsNatVipServerLoadBalance.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerLoadBalance.setStatus(_A)
_NsNatVipServerIp_Type=IpAddress
_NsNatVipServerIp_Object=MibTableColumn
nsNatVipServerIp=_NsNatVipServerIp_Object((1,3,6,1,4,1,3224,11,3,2,1,5),_NsNatVipServerIp_Type())
nsNatVipServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerIp.setStatus(_A)
_NsNatVipServerWeight_Type=Integer32
_NsNatVipServerWeight_Object=MibTableColumn
nsNatVipServerWeight=_NsNatVipServerWeight_Object((1,3,6,1,4,1,3224,11,3,2,1,6),_NsNatVipServerWeight_Type())
nsNatVipServerWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerWeight.setStatus(_A)
class _NsNatVipServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_NsNatVipServerStatus_Type.__name__=_C
_NsNatVipServerStatus_Object=MibTableColumn
nsNatVipServerStatus=_NsNatVipServerStatus_Object((1,3,6,1,4,1,3224,11,3,2,1,7),_NsNatVipServerStatus_Type())
nsNatVipServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatVipServerStatus.setStatus(_A)
_NsNatDipPPortTable_Object=MibTable
nsNatDipPPortTable=_NsNatDipPPortTable_Object((1,3,6,1,4,1,3224,11,4))
if mibBuilder.loadTexts:nsNatDipPPortTable.setStatus(_A)
_NsNatDipPPortEntry_Object=MibTableRow
nsNatDipPPortEntry=_NsNatDipPPortEntry_Object((1,3,6,1,4,1,3224,11,4,1))
nsNatDipPPortEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:nsNatDipPPortEntry.setStatus(_A)
class _NsNatDipPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsNatDipPPortIndex_Type.__name__=_C
_NsNatDipPPortIndex_Object=MibTableColumn
nsNatDipPPortIndex=_NsNatDipPPortIndex_Object((1,3,6,1,4,1,3224,11,4,1,1),_NsNatDipPPortIndex_Type())
nsNatDipPPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipPPortIndex.setStatus(_A)
_NsNatDipAllPort_Type=Integer32
_NsNatDipAllPort_Object=MibTableColumn
nsNatDipAllPort=_NsNatDipAllPort_Object((1,3,6,1,4,1,3224,11,4,1,2),_NsNatDipAllPort_Type())
nsNatDipAllPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipAllPort.setStatus(_A)
_NsNatDipAllocatedPort_Type=Integer32
_NsNatDipAllocatedPort_Object=MibTableColumn
nsNatDipAllocatedPort=_NsNatDipAllocatedPort_Object((1,3,6,1,4,1,3224,11,4,1,3),_NsNatDipAllocatedPort_Type())
nsNatDipAllocatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipAllocatedPort.setStatus(_A)
_NsNatDipAvailablePort_Type=Integer32
_NsNatDipAvailablePort_Object=MibTableColumn
nsNatDipAvailablePort=_NsNatDipAvailablePort_Object((1,3,6,1,4,1,3224,11,4,1,4),_NsNatDipAvailablePort_Type())
nsNatDipAvailablePort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipAvailablePort.setStatus(_A)
_NsNatDipAllocatedPairedPort_Type=Integer32
_NsNatDipAllocatedPairedPort_Object=MibTableColumn
nsNatDipAllocatedPairedPort=_NsNatDipAllocatedPairedPort_Object((1,3,6,1,4,1,3224,11,4,1,5),_NsNatDipAllocatedPairedPort_Type())
nsNatDipAllocatedPairedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipAllocatedPairedPort.setStatus(_A)
_NsNatDipAvailablePairedPort_Type=Integer32
_NsNatDipAvailablePairedPort_Object=MibTableColumn
nsNatDipAvailablePairedPort=_NsNatDipAvailablePairedPort_Object((1,3,6,1,4,1,3224,11,4,1,6),_NsNatDipAvailablePairedPort_Type())
nsNatDipAvailablePairedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsNatDipAvailablePairedPort.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'netscreenNATMibModule':netscreenNATMibModule,'nsNatMipTable':nsNatMipTable,'nsNatMipEntry':nsNatMipEntry,_F:nsNatMipIndex,'nsNatMipIp':nsNatMipIp,'nsNatMipNetmask':nsNatMipNetmask,'nsNatMipHost':nsNatMipHost,'nsNatMipIfIp':nsNatMipIfIp,'nsNatMipIfNetmask':nsNatMipIfNetmask,'nsNatMipVsys':nsNatMipVsys,'nsNatDipTable':nsNatDipTable,'nsNatDipEntry':nsNatDipEntry,_G:nsNatDipIndex,'nsNatDipId':nsNatDipId,'nsNatDipLow':nsNatDipLow,'nsNatDipHigh':nsNatDipHigh,'nsNatDipIfIp':nsNatDipIfIp,'nsNatDipIfNetmask':nsNatDipIfNetmask,'nsNatDipPTEnable':nsNatDipPTEnable,'nsNatDipVsys':nsNatDipVsys,'nsNatDipUtil':nsNatDipUtil,'nsNatVip':nsNatVip,'nsNatVipCfgTable':nsNatVipCfgTable,'nsNatVipCfgEntry':nsNatVipCfgEntry,_H:nsNatVipCfgIndex,'nsNatVipCfgIp':nsNatVipCfgIp,'nsNatVipCfgPort':nsNatVipCfgPort,'nsNatVipCfgService':nsNatVipCfgService,'nsNatVipCfgStatus':nsNatVipCfgStatus,'nsNatVipCfgLoadBalance':nsNatVipCfgLoadBalance,'nsNatVipServerTable':nsNatVipServerTable,'nsNatVipServerEntry':nsNatVipServerEntry,_M:nsNatVipServerIndex,'nsNatVipServerVIP':nsNatVipServerVIP,'nsNatVipServerService':nsNatVipServerService,'nsNatVipServerLoadBalance':nsNatVipServerLoadBalance,'nsNatVipServerIp':nsNatVipServerIp,'nsNatVipServerWeight':nsNatVipServerWeight,'nsNatVipServerStatus':nsNatVipServerStatus,'nsNatDipPPortTable':nsNatDipPPortTable,'nsNatDipPPortEntry':nsNatDipPPortEntry,_N:nsNatDipPPortIndex,'nsNatDipAllPort':nsNatDipAllPort,'nsNatDipAllocatedPort':nsNatDipAllocatedPort,'nsNatDipAvailablePort':nsNatDipAvailablePort,'nsNatDipAllocatedPairedPort':nsNatDipAllocatedPairedPort,'nsNatDipAvailablePairedPort':nsNatDipAvailablePairedPort})