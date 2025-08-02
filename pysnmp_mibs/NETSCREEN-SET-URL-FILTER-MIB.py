_D='DisplayString'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenSetUrlFilterMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,4))
if mibBuilder.loadTexts:netscreenSetUrlFilterMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-12 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetURLFilter_ObjectIdentity=ObjectIdentity
nsSetURLFilter=_NsSetURLFilter_ObjectIdentity((1,3,6,1,4,1,3224,7,4))
class _NsSetUrlFilterViaWebsense_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsSetUrlFilterViaWebsense_Type.__name__=_C
_NsSetUrlFilterViaWebsense_Object=MibScalar
nsSetUrlFilterViaWebsense=_NsSetUrlFilterViaWebsense_Object((1,3,6,1,4,1,3224,7,4,1),_NsSetUrlFilterViaWebsense_Type())
nsSetUrlFilterViaWebsense.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlFilterViaWebsense.setStatus(_B)
class _NsSetUrlServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetUrlServerName_Type.__name__=_D
_NsSetUrlServerName_Object=MibScalar
nsSetUrlServerName=_NsSetUrlServerName_Object((1,3,6,1,4,1,3224,7,4,2),_NsSetUrlServerName_Type())
nsSetUrlServerName.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlServerName.setStatus(_B)
_NsSetUrlServerPort_Type=Integer32
_NsSetUrlServerPort_Object=MibScalar
nsSetUrlServerPort=_NsSetUrlServerPort_Object((1,3,6,1,4,1,3224,7,4,3),_NsSetUrlServerPort_Type())
nsSetUrlServerPort.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlServerPort.setStatus(_B)
class _NsSetUrlCommTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_NsSetUrlCommTimeout_Type.__name__=_C
_NsSetUrlCommTimeout_Object=MibScalar
nsSetUrlCommTimeout=_NsSetUrlCommTimeout_Object((1,3,6,1,4,1,3224,7,4,4),_NsSetUrlCommTimeout_Type())
nsSetUrlCommTimeout.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlCommTimeout.setStatus(_B)
class _NsSetUrlServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('not-applicable',0),('running',1),('down',2)))
_NsSetUrlServerStatus_Type.__name__=_C
_NsSetUrlServerStatus_Object=MibScalar
nsSetUrlServerStatus=_NsSetUrlServerStatus_Object((1,3,6,1,4,1,3224,7,4,5),_NsSetUrlServerStatus_Type())
nsSetUrlServerStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlServerStatus.setStatus(_B)
class _NsSetUrlSerLostHdlWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('block-all',0),('permit-all',1)))
_NsSetUrlSerLostHdlWay_Type.__name__=_C
_NsSetUrlSerLostHdlWay_Object=MibScalar
nsSetUrlSerLostHdlWay=_NsSetUrlSerLostHdlWay_Object((1,3,6,1,4,1,3224,7,4,6),_NsSetUrlSerLostHdlWay_Type())
nsSetUrlSerLostHdlWay.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlSerLostHdlWay.setStatus(_B)
class _NsSetUrlBlockMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('websense',0),('netscreen',1)))
_NsSetUrlBlockMsgType_Type.__name__=_C
_NsSetUrlBlockMsgType_Object=MibScalar
nsSetUrlBlockMsgType=_NsSetUrlBlockMsgType_Object((1,3,6,1,4,1,3224,7,4,7),_NsSetUrlBlockMsgType_Type())
nsSetUrlBlockMsgType.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlBlockMsgType.setStatus(_B)
class _NsSetUrlNsBlockMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,220))
_NsSetUrlNsBlockMsg_Type.__name__=_D
_NsSetUrlNsBlockMsg_Object=MibScalar
nsSetUrlNsBlockMsg=_NsSetUrlNsBlockMsg_Object((1,3,6,1,4,1,3224,7,4,8),_NsSetUrlNsBlockMsg_Type())
nsSetUrlNsBlockMsg.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetUrlNsBlockMsg.setStatus(_B)
mibBuilder.exportSymbols('NETSCREEN-SET-URL-FILTER-MIB',**{'netscreenSetUrlFilterMibModule':netscreenSetUrlFilterMibModule,'nsSetURLFilter':nsSetURLFilter,'nsSetUrlFilterViaWebsense':nsSetUrlFilterViaWebsense,'nsSetUrlServerName':nsSetUrlServerName,'nsSetUrlServerPort':nsSetUrlServerPort,'nsSetUrlCommTimeout':nsSetUrlCommTimeout,'nsSetUrlServerStatus':nsSetUrlServerStatus,'nsSetUrlSerLostHdlWay':nsSetUrlSerLostHdlWay,'nsSetUrlBlockMsgType':nsSetUrlBlockMsgType,'nsSetUrlNsBlockMsg':nsSetUrlNsBlockMsg})