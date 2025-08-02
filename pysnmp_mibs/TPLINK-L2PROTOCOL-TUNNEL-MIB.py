_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkL2protocolTunnelMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,81))
if mibBuilder.loadTexts:tplinkL2protocolTunnelMIB.setRevisions(('2009-08-27 00:00',))
_TplinkL2protocolTunnelMIBObjects_ObjectIdentity=ObjectIdentity
tplinkL2protocolTunnelMIBObjects=_TplinkL2protocolTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,81,1))
_TpL2ptGlobalCfg_ObjectIdentity=ObjectIdentity
tpL2ptGlobalCfg=_TpL2ptGlobalCfg_ObjectIdentity((1,3,6,1,4,1,11863,6,81,1,1))
class _TpL2ptEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpL2ptEnable_Type.__name__=_D
_TpL2ptEnable_Object=MibScalar
tpL2ptEnable=_TpL2ptEnable_Object((1,3,6,1,4,1,11863,6,81,1,1,1),_TpL2ptEnable_Type())
tpL2ptEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpL2ptEnable.setStatus(_A)
_TpL2ptPortCfg_ObjectIdentity=ObjectIdentity
tpL2ptPortCfg=_TpL2ptPortCfg_ObjectIdentity((1,3,6,1,4,1,11863,6,81,1,2))
_TpL2ptPortTable_Object=MibTable
tpL2ptPortTable=_TpL2ptPortTable_Object((1,3,6,1,4,1,11863,6,81,1,2,1))
if mibBuilder.loadTexts:tpL2ptPortTable.setStatus(_A)
_TpL2ptPortEntry_Object=MibTableRow
tpL2ptPortEntry=_TpL2ptPortEntry_Object((1,3,6,1,4,1,11863,6,81,1,2,1,1))
tpL2ptPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpL2ptPortEntry.setStatus(_A)
class _TpL2ptPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpL2ptPort_Type.__name__=_B
_TpL2ptPort_Object=MibTableColumn
tpL2ptPort=_TpL2ptPort_Object((1,3,6,1,4,1,11863,6,81,1,2,1,1,1),_TpL2ptPort_Type())
tpL2ptPort.setMaxAccess(_G)
if mibBuilder.loadTexts:tpL2ptPort.setStatus(_A)
class _TpL2ptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('uni',1),('nni',2)))
_TpL2ptType_Type.__name__=_D
_TpL2ptType_Object=MibTableColumn
tpL2ptType=_TpL2ptType_Object((1,3,6,1,4,1,11863,6,81,1,2,1,1,2),_TpL2ptType_Type())
tpL2ptType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpL2ptType.setStatus(_A)
class _TpL2ptProtocol_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpL2ptProtocol_Type.__name__=_B
_TpL2ptProtocol_Object=MibTableColumn
tpL2ptProtocol=_TpL2ptProtocol_Object((1,3,6,1,4,1,11863,6,81,1,2,1,1,3),_TpL2ptProtocol_Type())
tpL2ptProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:tpL2ptProtocol.setStatus(_A)
class _TpL2ptThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpL2ptThreshold_Type.__name__=_B
_TpL2ptThreshold_Object=MibTableColumn
tpL2ptThreshold=_TpL2ptThreshold_Object((1,3,6,1,4,1,11863,6,81,1,2,1,1,4),_TpL2ptThreshold_Type())
tpL2ptThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tpL2ptThreshold.setStatus(_A)
class _TpL2ptLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpL2ptLag_Type.__name__=_B
_TpL2ptLag_Object=MibTableColumn
tpL2ptLag=_TpL2ptLag_Object((1,3,6,1,4,1,11863,6,81,1,2,1,1,5),_TpL2ptLag_Type())
tpL2ptLag.setMaxAccess(_G)
if mibBuilder.loadTexts:tpL2ptLag.setStatus(_A)
_TplinkL2protocolTunnelNotifications_ObjectIdentity=ObjectIdentity
tplinkL2protocolTunnelNotifications=_TplinkL2protocolTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,81,2))
mibBuilder.exportSymbols('TPLINK-L2PROTOCOL-TUNNEL-MIB',**{'tplinkL2protocolTunnelMIB':tplinkL2protocolTunnelMIB,'tplinkL2protocolTunnelMIBObjects':tplinkL2protocolTunnelMIBObjects,'tpL2ptGlobalCfg':tpL2ptGlobalCfg,'tpL2ptEnable':tpL2ptEnable,'tpL2ptPortCfg':tpL2ptPortCfg,'tpL2ptPortTable':tpL2ptPortTable,'tpL2ptPortEntry':tpL2ptPortEntry,'tpL2ptPort':tpL2ptPort,'tpL2ptType':tpL2ptType,'tpL2ptProtocol':tpL2ptProtocol,'tpL2ptThreshold':tpL2ptThreshold,'tpL2ptLag':tpL2ptLag,'tplinkL2protocolTunnelNotifications':tplinkL2protocolTunnelNotifications})