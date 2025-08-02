_F='DisplayString'
_E='enabled'
_D='disable'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
netscreenSetGlbMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,10))
if mibBuilder.loadTexts:netscreenSetGlbMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetGlbMng_ObjectIdentity=ObjectIdentity
nsSetGlbMng=_NsSetGlbMng_ObjectIdentity((1,3,6,1,4,1,3224,7,10))
class _NsSetGlbMngVPNEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngVPNEnable_Type.__name__=_C
_NsSetGlbMngVPNEnable_Object=MibScalar
nsSetGlbMngVPNEnable=_NsSetGlbMngVPNEnable_Object((1,3,6,1,4,1,3224,7,10,1),_NsSetGlbMngVPNEnable_Type())
nsSetGlbMngVPNEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngVPNEnable.setStatus(_B)
class _NsSetGlbMngEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngEnable_Type.__name__=_C
_NsSetGlbMngEnable_Object=MibScalar
nsSetGlbMngEnable=_NsSetGlbMngEnable_Object((1,3,6,1,4,1,3224,7,10,2),_NsSetGlbMngEnable_Type())
nsSetGlbMngEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngEnable.setStatus(_B)
class _NsSetGlbProEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbProEnable_Type.__name__=_C
_NsSetGlbProEnable_Object=MibScalar
nsSetGlbProEnable=_NsSetGlbProEnable_Object((1,3,6,1,4,1,3224,7,10,3),_NsSetGlbProEnable_Type())
nsSetGlbProEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbProEnable.setStatus(_B)
_NsSetGlbManagerSetting_ObjectIdentity=ObjectIdentity
nsSetGlbManagerSetting=_NsSetGlbManagerSetting_ObjectIdentity((1,3,6,1,4,1,3224,7,10,4))
class _NsSetGlbMngSerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetGlbMngSerName_Type.__name__=_F
_NsSetGlbMngSerName_Object=MibScalar
nsSetGlbMngSerName=_NsSetGlbMngSerName_Object((1,3,6,1,4,1,3224,7,10,4,1),_NsSetGlbMngSerName_Type())
nsSetGlbMngSerName.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngSerName.setStatus(_B)
_NsSetGlbMngSerTCP_Type=Integer32
_NsSetGlbMngSerTCP_Object=MibScalar
nsSetGlbMngSerTCP=_NsSetGlbMngSerTCP_Object((1,3,6,1,4,1,3224,7,10,4,2),_NsSetGlbMngSerTCP_Type())
nsSetGlbMngSerTCP.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngSerTCP.setStatus(_B)
_NsSetGlbMngSerUDP_Type=Integer32
_NsSetGlbMngSerUDP_Object=MibScalar
nsSetGlbMngSerUDP=_NsSetGlbMngSerUDP_Object((1,3,6,1,4,1,3224,7,10,4,3),_NsSetGlbMngSerUDP_Type())
nsSetGlbMngSerUDP.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngSerUDP.setStatus(_B)
_NsSetGlbMngLocal_Type=Integer32
_NsSetGlbMngLocal_Object=MibScalar
nsSetGlbMngLocal=_NsSetGlbMngLocal_Object((1,3,6,1,4,1,3224,7,10,4,4),_NsSetGlbMngLocal_Type())
nsSetGlbMngLocal.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngLocal.setStatus(_B)
_NsSetGlbProManagerSetting_ObjectIdentity=ObjectIdentity
nsSetGlbProManagerSetting=_NsSetGlbProManagerSetting_ObjectIdentity((1,3,6,1,4,1,3224,7,10,5))
_NsSetGlbProPriSer_Type=IpAddress
_NsSetGlbProPriSer_Object=MibScalar
nsSetGlbProPriSer=_NsSetGlbProPriSer_Object((1,3,6,1,4,1,3224,7,10,5,1),_NsSetGlbProPriSer_Type())
nsSetGlbProPriSer.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbProPriSer.setStatus(_B)
_NsSetGlbProSecSer_Type=IpAddress
_NsSetGlbProSecSer_Object=MibScalar
nsSetGlbProSecSer=_NsSetGlbProSecSer_Object((1,3,6,1,4,1,3224,7,10,5,2),_NsSetGlbProSecSer_Type())
nsSetGlbProSecSer.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbProSecSer.setStatus(_B)
_NsSetGlbMngSetting_ObjectIdentity=ObjectIdentity
nsSetGlbMngSetting=_NsSetGlbMngSetting_ObjectIdentity((1,3,6,1,4,1,3224,7,10,6))
class _NsSetGlbMngProtDist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngProtDist_Type.__name__=_C
_NsSetGlbMngProtDist_Object=MibScalar
nsSetGlbMngProtDist=_NsSetGlbMngProtDist_Object((1,3,6,1,4,1,3224,7,10,6,1),_NsSetGlbMngProtDist_Type())
nsSetGlbMngProtDist.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngProtDist.setStatus(_B)
class _NsSetGlbMngEthStatis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngEthStatis_Type.__name__=_C
_NsSetGlbMngEthStatis_Object=MibScalar
nsSetGlbMngEthStatis=_NsSetGlbMngEthStatis_Object((1,3,6,1,4,1,3224,7,10,6,2),_NsSetGlbMngEthStatis_Type())
nsSetGlbMngEthStatis.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngEthStatis.setStatus(_B)
class _NsSetGlbMngAttStatis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngAttStatis_Type.__name__=_C
_NsSetGlbMngAttStatis_Object=MibScalar
nsSetGlbMngAttStatis=_NsSetGlbMngAttStatis_Object((1,3,6,1,4,1,3224,7,10,6,3),_NsSetGlbMngAttStatis_Type())
nsSetGlbMngAttStatis.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngAttStatis.setStatus(_B)
class _NsSetGlbMngPlyStatis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngPlyStatis_Type.__name__=_C
_NsSetGlbMngPlyStatis_Object=MibScalar
nsSetGlbMngPlyStatis=_NsSetGlbMngPlyStatis_Object((1,3,6,1,4,1,3224,7,10,6,4),_NsSetGlbMngPlyStatis_Type())
nsSetGlbMngPlyStatis.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngPlyStatis.setStatus(_B)
class _NsSetGlbMngFlowStatis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngFlowStatis_Type.__name__=_C
_NsSetGlbMngFlowStatis_Object=MibScalar
nsSetGlbMngFlowStatis=_NsSetGlbMngFlowStatis_Object((1,3,6,1,4,1,3224,7,10,6,5),_NsSetGlbMngFlowStatis_Type())
nsSetGlbMngFlowStatis.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngFlowStatis.setStatus(_B)
class _NsSetGlbMngTrafAlm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngTrafAlm_Type.__name__=_C
_NsSetGlbMngTrafAlm_Object=MibScalar
nsSetGlbMngTrafAlm=_NsSetGlbMngTrafAlm_Object((1,3,6,1,4,1,3224,7,10,6,6),_NsSetGlbMngTrafAlm_Type())
nsSetGlbMngTrafAlm.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngTrafAlm.setStatus(_B)
class _NsSetGlbMngAttAlm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngAttAlm_Type.__name__=_C
_NsSetGlbMngAttAlm_Object=MibScalar
nsSetGlbMngAttAlm=_NsSetGlbMngAttAlm_Object((1,3,6,1,4,1,3224,7,10,6,7),_NsSetGlbMngAttAlm_Type())
nsSetGlbMngAttAlm.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngAttAlm.setStatus(_B)
class _NsSetGlbMngEvtAlm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngEvtAlm_Type.__name__=_C
_NsSetGlbMngEvtAlm_Object=MibScalar
nsSetGlbMngEvtAlm=_NsSetGlbMngEvtAlm_Object((1,3,6,1,4,1,3224,7,10,6,8),_NsSetGlbMngEvtAlm_Type())
nsSetGlbMngEvtAlm.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngEvtAlm.setStatus(_B)
class _NsSetGlbMngCfgLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngCfgLog_Type.__name__=_C
_NsSetGlbMngCfgLog_Object=MibScalar
nsSetGlbMngCfgLog=_NsSetGlbMngCfgLog_Object((1,3,6,1,4,1,3224,7,10,6,9),_NsSetGlbMngCfgLog_Type())
nsSetGlbMngCfgLog.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngCfgLog.setStatus(_B)
class _NsSetGlbMngTrafLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngTrafLog_Type.__name__=_C
_NsSetGlbMngTrafLog_Object=MibScalar
nsSetGlbMngTrafLog=_NsSetGlbMngTrafLog_Object((1,3,6,1,4,1,3224,7,10,6,10),_NsSetGlbMngTrafLog_Type())
nsSetGlbMngTrafLog.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngTrafLog.setStatus(_B)
class _NsSetGlbMngInfoLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngInfoLog_Type.__name__=_C
_NsSetGlbMngInfoLog_Object=MibScalar
nsSetGlbMngInfoLog=_NsSetGlbMngInfoLog_Object((1,3,6,1,4,1,3224,7,10,6,11),_NsSetGlbMngInfoLog_Type())
nsSetGlbMngInfoLog.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngInfoLog.setStatus(_B)
class _NsSetGlbMngSelfLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetGlbMngSelfLog_Type.__name__=_C
_NsSetGlbMngSelfLog_Object=MibScalar
nsSetGlbMngSelfLog=_NsSetGlbMngSelfLog_Object((1,3,6,1,4,1,3224,7,10,6,12),_NsSetGlbMngSelfLog_Type())
nsSetGlbMngSelfLog.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGlbMngSelfLog.setStatus(_B)
mibBuilder.exportSymbols('NETSCREEN-SET-GLB-MIB',**{'netscreenSetGlbMibModule':netscreenSetGlbMibModule,'nsSetGlbMng':nsSetGlbMng,'nsSetGlbMngVPNEnable':nsSetGlbMngVPNEnable,'nsSetGlbMngEnable':nsSetGlbMngEnable,'nsSetGlbProEnable':nsSetGlbProEnable,'nsSetGlbManagerSetting':nsSetGlbManagerSetting,'nsSetGlbMngSerName':nsSetGlbMngSerName,'nsSetGlbMngSerTCP':nsSetGlbMngSerTCP,'nsSetGlbMngSerUDP':nsSetGlbMngSerUDP,'nsSetGlbMngLocal':nsSetGlbMngLocal,'nsSetGlbProManagerSetting':nsSetGlbProManagerSetting,'nsSetGlbProPriSer':nsSetGlbProPriSer,'nsSetGlbProSecSer':nsSetGlbProSecSer,'nsSetGlbMngSetting':nsSetGlbMngSetting,'nsSetGlbMngProtDist':nsSetGlbMngProtDist,'nsSetGlbMngEthStatis':nsSetGlbMngEthStatis,'nsSetGlbMngAttStatis':nsSetGlbMngAttStatis,'nsSetGlbMngPlyStatis':nsSetGlbMngPlyStatis,'nsSetGlbMngFlowStatis':nsSetGlbMngFlowStatis,'nsSetGlbMngTrafAlm':nsSetGlbMngTrafAlm,'nsSetGlbMngAttAlm':nsSetGlbMngAttAlm,'nsSetGlbMngEvtAlm':nsSetGlbMngEvtAlm,'nsSetGlbMngCfgLog':nsSetGlbMngCfgLog,'nsSetGlbMngTrafLog':nsSetGlbMngTrafLog,'nsSetGlbMngInfoLog':nsSetGlbMngInfoLog,'nsSetGlbMngSelfLog':nsSetGlbMngSelfLog})