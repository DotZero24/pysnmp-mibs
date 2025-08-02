_K='mediaTerminalIntPort'
_J='mediaTerminalIntAddr'
_I='mediaConnIndex'
_H='delete'
_G='ipProxyDescr'
_F='DisplayString'
_E='BIANCA-BRICK-PROXY-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_IpProxyTable_Object=MibTable
ipProxyTable=_IpProxyTable_Object((1,3,6,1,4,1,272,4,5,50))
if mibBuilder.loadTexts:ipProxyTable.setStatus(_A)
_IpProxyEntry_Object=MibTableRow
ipProxyEntry=_IpProxyEntry_Object((1,3,6,1,4,1,272,4,5,50,1))
ipProxyEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ipProxyEntry.setStatus(_A)
class _IpProxyDescr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IpProxyDescr_Type.__name__=_F
_IpProxyDescr_Object=MibTableColumn
ipProxyDescr=_IpProxyDescr_Object((1,3,6,1,4,1,272,4,5,50,1,1),_IpProxyDescr_Type())
ipProxyDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyDescr.setStatus(_A)
class _IpProxyAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),(_H,3)))
_IpProxyAdminStatus_Type.__name__=_B
_IpProxyAdminStatus_Object=MibTableColumn
ipProxyAdminStatus=_IpProxyAdminStatus_Object((1,3,6,1,4,1,272,4,5,50,1,2),_IpProxyAdminStatus_Type())
ipProxyAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyAdminStatus.setStatus(_A)
class _IpProxyApplication_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8,15)));namedValues=NamedValues(*(('sip',1),('mgcp',2),('rtsp',3),('h323udp',4),('h323tcp',8),('none',15)))
_IpProxyApplication_Type.__name__=_B
_IpProxyApplication_Object=MibTableColumn
ipProxyApplication=_IpProxyApplication_Object((1,3,6,1,4,1,272,4,5,50,1,3),_IpProxyApplication_Type())
ipProxyApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyApplication.setStatus(_A)
class _IpProxyProtocol_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_IpProxyProtocol_Type.__name__=_B
_IpProxyProtocol_Object=MibTableColumn
ipProxyProtocol=_IpProxyProtocol_Object((1,3,6,1,4,1,272,4,5,50,1,4),_IpProxyProtocol_Type())
ipProxyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyProtocol.setStatus(_A)
class _IpProxyIntPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpProxyIntPort_Type.__name__=_B
_IpProxyIntPort_Object=MibTableColumn
ipProxyIntPort=_IpProxyIntPort_Object((1,3,6,1,4,1,272,4,5,50,1,5),_IpProxyIntPort_Type())
ipProxyIntPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyIntPort.setStatus(_A)
class _IpProxyExtPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpProxyExtPort_Type.__name__=_B
_IpProxyExtPort_Object=MibTableColumn
ipProxyExtPort=_IpProxyExtPort_Object((1,3,6,1,4,1,272,4,5,50,1,6),_IpProxyExtPort_Type())
ipProxyExtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyExtPort.setStatus(_A)
_IpProxyIntAddr_Type=IpAddress
_IpProxyIntAddr_Object=MibTableColumn
ipProxyIntAddr=_IpProxyIntAddr_Object((1,3,6,1,4,1,272,4,5,50,1,7),_IpProxyIntAddr_Type())
ipProxyIntAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyIntAddr.setStatus(_A)
class _IpProxyPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('default',1),('low-latency',2),('high',3),('medium',4),('low',5)))
_IpProxyPriority_Type.__name__=_B
_IpProxyPriority_Object=MibTableColumn
ipProxyPriority=_IpProxyPriority_Object((1,3,6,1,4,1,272,4,5,50,1,8),_IpProxyPriority_Type())
ipProxyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyPriority.setStatus(_A)
class _IpProxyTimeout_Type(Integer32):defaultValue=7200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_IpProxyTimeout_Type.__name__=_B
_IpProxyTimeout_Object=MibTableColumn
ipProxyTimeout=_IpProxyTimeout_Object((1,3,6,1,4,1,272,4,5,50,1,9),_IpProxyTimeout_Type())
ipProxyTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ipProxyTimeout.setStatus(_A)
_Media_ObjectIdentity=ObjectIdentity
media=_Media_ObjectIdentity((1,3,6,1,4,1,272,4,50))
_MediaConnTable_Object=MibTable
mediaConnTable=_MediaConnTable_Object((1,3,6,1,4,1,272,4,50,1))
if mibBuilder.loadTexts:mediaConnTable.setStatus(_A)
_MediaConnEntry_Object=MibTableRow
mediaConnEntry=_MediaConnEntry_Object((1,3,6,1,4,1,272,4,50,1,1))
mediaConnEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:mediaConnEntry.setStatus(_A)
class _MediaConnIndex_Type(Integer32):defaultValue=1
_MediaConnIndex_Type.__name__=_B
_MediaConnIndex_Object=MibTableColumn
mediaConnIndex=_MediaConnIndex_Object((1,3,6,1,4,1,272,4,50,1,1,1),_MediaConnIndex_Type())
mediaConnIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnIndex.setStatus(_A)
_MediaConnIntAddr_Type=IpAddress
_MediaConnIntAddr_Object=MibTableColumn
mediaConnIntAddr=_MediaConnIntAddr_Object((1,3,6,1,4,1,272,4,50,1,1,2),_MediaConnIntAddr_Type())
mediaConnIntAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnIntAddr.setStatus(_A)
_MediaConnIntPort_Type=Integer32
_MediaConnIntPort_Object=MibTableColumn
mediaConnIntPort=_MediaConnIntPort_Object((1,3,6,1,4,1,272,4,50,1,1,3),_MediaConnIntPort_Type())
mediaConnIntPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnIntPort.setStatus(_A)
_MediaConnExtAddr_Type=IpAddress
_MediaConnExtAddr_Object=MibTableColumn
mediaConnExtAddr=_MediaConnExtAddr_Object((1,3,6,1,4,1,272,4,50,1,1,4),_MediaConnExtAddr_Type())
mediaConnExtAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnExtAddr.setStatus(_A)
_MediaConnExtPort_Type=Integer32
_MediaConnExtPort_Object=MibTableColumn
mediaConnExtPort=_MediaConnExtPort_Object((1,3,6,1,4,1,272,4,50,1,1,5),_MediaConnExtPort_Type())
mediaConnExtPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnExtPort.setStatus(_A)
_MediaConnRemoteAddr_Type=IpAddress
_MediaConnRemoteAddr_Object=MibTableColumn
mediaConnRemoteAddr=_MediaConnRemoteAddr_Object((1,3,6,1,4,1,272,4,50,1,1,6),_MediaConnRemoteAddr_Type())
mediaConnRemoteAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnRemoteAddr.setStatus(_A)
_MediaConnRemotePort_Type=Integer32
_MediaConnRemotePort_Object=MibTableColumn
mediaConnRemotePort=_MediaConnRemotePort_Object((1,3,6,1,4,1,272,4,50,1,1,7),_MediaConnRemotePort_Type())
mediaConnRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnRemotePort.setStatus(_A)
_MediaConnAge_Type=TimeTicks
_MediaConnAge_Object=MibTableColumn
mediaConnAge=_MediaConnAge_Object((1,3,6,1,4,1,272,4,50,1,1,8),_MediaConnAge_Type())
mediaConnAge.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaConnAge.setStatus(_A)
_MediaTerminalTable_Object=MibTable
mediaTerminalTable=_MediaTerminalTable_Object((1,3,6,1,4,1,272,4,50,2))
if mibBuilder.loadTexts:mediaTerminalTable.setStatus(_A)
_MediaTerminalEntry_Object=MibTableRow
mediaTerminalEntry=_MediaTerminalEntry_Object((1,3,6,1,4,1,272,4,50,2,1))
mediaTerminalEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:mediaTerminalEntry.setStatus(_A)
_MediaTerminalIntAddr_Type=IpAddress
_MediaTerminalIntAddr_Object=MibTableColumn
mediaTerminalIntAddr=_MediaTerminalIntAddr_Object((1,3,6,1,4,1,272,4,50,2,1,1),_MediaTerminalIntAddr_Type())
mediaTerminalIntAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalIntAddr.setStatus(_A)
class _MediaTerminalIntPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MediaTerminalIntPort_Type.__name__=_B
_MediaTerminalIntPort_Object=MibTableColumn
mediaTerminalIntPort=_MediaTerminalIntPort_Object((1,3,6,1,4,1,272,4,50,2,1,2),_MediaTerminalIntPort_Type())
mediaTerminalIntPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalIntPort.setStatus(_A)
class _MediaTerminalExtPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MediaTerminalExtPort_Type.__name__=_B
_MediaTerminalExtPort_Object=MibTableColumn
mediaTerminalExtPort=_MediaTerminalExtPort_Object((1,3,6,1,4,1,272,4,50,2,1,3),_MediaTerminalExtPort_Type())
mediaTerminalExtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalExtPort.setStatus(_A)
class _MediaTerminalRemotePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MediaTerminalRemotePort_Type.__name__=_B
_MediaTerminalRemotePort_Object=MibTableColumn
mediaTerminalRemotePort=_MediaTerminalRemotePort_Object((1,3,6,1,4,1,272,4,50,2,1,4),_MediaTerminalRemotePort_Type())
mediaTerminalRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalRemotePort.setStatus(_A)
class _MediaTerminalLifetime_Type(Integer32):defaultValue=0
_MediaTerminalLifetime_Type.__name__=_B
_MediaTerminalLifetime_Object=MibTableColumn
mediaTerminalLifetime=_MediaTerminalLifetime_Object((1,3,6,1,4,1,272,4,50,2,1,5),_MediaTerminalLifetime_Type())
mediaTerminalLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalLifetime.setStatus(_A)
class _MediaTerminalAge_Type(Integer32):defaultValue=0
_MediaTerminalAge_Type.__name__=_B
_MediaTerminalAge_Object=MibTableColumn
mediaTerminalAge=_MediaTerminalAge_Object((1,3,6,1,4,1,272,4,50,2,1,6),_MediaTerminalAge_Type())
mediaTerminalAge.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaTerminalAge.setStatus(_A)
class _MediaTerminalProto_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_MediaTerminalProto_Type.__name__=_B
_MediaTerminalProto_Object=MibTableColumn
mediaTerminalProto=_MediaTerminalProto_Object((1,3,6,1,4,1,272,4,50,2,1,7),_MediaTerminalProto_Type())
mediaTerminalProto.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalProto.setStatus(_A)
class _MediaTerminalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,8)));namedValues=NamedValues(*(('client',1),('server',2),(_H,8)))
_MediaTerminalType_Type.__name__=_B
_MediaTerminalType_Object=MibTableColumn
mediaTerminalType=_MediaTerminalType_Object((1,3,6,1,4,1,272,4,50,2,1,8),_MediaTerminalType_Type())
mediaTerminalType.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaTerminalType.setStatus(_A)
class _MediaTerminalSessions_Type(Integer32):defaultValue=0
_MediaTerminalSessions_Type.__name__=_B
_MediaTerminalSessions_Object=MibTableColumn
mediaTerminalSessions=_MediaTerminalSessions_Object((1,3,6,1,4,1,272,4,50,2,1,10),_MediaTerminalSessions_Type())
mediaTerminalSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:mediaTerminalSessions.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'ipProxyTable':ipProxyTable,'ipProxyEntry':ipProxyEntry,_G:ipProxyDescr,'ipProxyAdminStatus':ipProxyAdminStatus,'ipProxyApplication':ipProxyApplication,'ipProxyProtocol':ipProxyProtocol,'ipProxyIntPort':ipProxyIntPort,'ipProxyExtPort':ipProxyExtPort,'ipProxyIntAddr':ipProxyIntAddr,'ipProxyPriority':ipProxyPriority,'ipProxyTimeout':ipProxyTimeout,'media':media,'mediaConnTable':mediaConnTable,'mediaConnEntry':mediaConnEntry,_I:mediaConnIndex,'mediaConnIntAddr':mediaConnIntAddr,'mediaConnIntPort':mediaConnIntPort,'mediaConnExtAddr':mediaConnExtAddr,'mediaConnExtPort':mediaConnExtPort,'mediaConnRemoteAddr':mediaConnRemoteAddr,'mediaConnRemotePort':mediaConnRemotePort,'mediaConnAge':mediaConnAge,'mediaTerminalTable':mediaTerminalTable,'mediaTerminalEntry':mediaTerminalEntry,_J:mediaTerminalIntAddr,_K:mediaTerminalIntPort,'mediaTerminalExtPort':mediaTerminalExtPort,'mediaTerminalRemotePort':mediaTerminalRemotePort,'mediaTerminalLifetime':mediaTerminalLifetime,'mediaTerminalAge':mediaTerminalAge,'mediaTerminalProto':mediaTerminalProto,'mediaTerminalType':mediaTerminalType,'mediaTerminalSessions':mediaTerminalSessions})