_I='ruckusTunnelSoftGREStatusIndex'
_H='ruckusTunnelSoftGREIndex'
_G='DisplayString'
_F='Integer32'
_E='read-write'
_D='RUCKUS-TUNNEL-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusCommonTunnelModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonTunnelModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
ruckusTunnelMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,18,1))
_RuckusTunnelObjects_ObjectIdentity=ObjectIdentity
ruckusTunnelObjects=_RuckusTunnelObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,18,1,1))
_RuckusTunnelInfo_ObjectIdentity=ObjectIdentity
ruckusTunnelInfo=_RuckusTunnelInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,18,1,1,1))
_RuckusTunnelSoftGREConfigInfo_ObjectIdentity=ObjectIdentity
ruckusTunnelSoftGREConfigInfo=_RuckusTunnelSoftGREConfigInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,18,1,1,1,3))
_RuckusTunnelSoftGREConfigTable_Object=MibTable
ruckusTunnelSoftGREConfigTable=_RuckusTunnelSoftGREConfigTable_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,3,1))
if mibBuilder.loadTexts:ruckusTunnelSoftGREConfigTable.setStatus(_A)
_RuckusTunnelSoftGREEntry_Object=MibTableRow
ruckusTunnelSoftGREEntry=_RuckusTunnelSoftGREEntry_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,3,1,1))
ruckusTunnelSoftGREEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:ruckusTunnelSoftGREEntry.setStatus(_A)
class _RuckusTunnelSoftGREAdminEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RuckusTunnelSoftGREAdminEnable_Type.__name__=_F
_RuckusTunnelSoftGREAdminEnable_Object=MibTableColumn
ruckusTunnelSoftGREAdminEnable=_RuckusTunnelSoftGREAdminEnable_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,3,1,1,1),_RuckusTunnelSoftGREAdminEnable_Type())
ruckusTunnelSoftGREAdminEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusTunnelSoftGREAdminEnable.setStatus(_A)
class _RuckusTunnelSoftGREPrimaryGatewayAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusTunnelSoftGREPrimaryGatewayAddress_Type.__name__=_C
_RuckusTunnelSoftGREPrimaryGatewayAddress_Object=MibTableColumn
ruckusTunnelSoftGREPrimaryGatewayAddress=_RuckusTunnelSoftGREPrimaryGatewayAddress_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,3,1,1,2),_RuckusTunnelSoftGREPrimaryGatewayAddress_Type())
ruckusTunnelSoftGREPrimaryGatewayAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusTunnelSoftGREPrimaryGatewayAddress.setStatus(_A)
class _RuckusTunnelSoftGRESecondaryGatewayAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusTunnelSoftGRESecondaryGatewayAddress_Type.__name__=_C
_RuckusTunnelSoftGRESecondaryGatewayAddress_Object=MibTableColumn
ruckusTunnelSoftGRESecondaryGatewayAddress=_RuckusTunnelSoftGRESecondaryGatewayAddress_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,3,1,1,3),_RuckusTunnelSoftGRESecondaryGatewayAddress_Type())
ruckusTunnelSoftGRESecondaryGatewayAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusTunnelSoftGRESecondaryGatewayAddress.setStatus(_A)
_RuckusTunnelSoftGREIndex_Type=Unsigned32
_RuckusTunnelSoftGREIndex_Object=MibTableColumn
ruckusTunnelSoftGREIndex=_RuckusTunnelSoftGREIndex_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,3,1,1,200),_RuckusTunnelSoftGREIndex_Type())
ruckusTunnelSoftGREIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusTunnelSoftGREIndex.setStatus(_A)
_RuckusTunnelSoftGREStatusInfo_ObjectIdentity=ObjectIdentity
ruckusTunnelSoftGREStatusInfo=_RuckusTunnelSoftGREStatusInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,18,1,1,1,5))
_RuckusTunnelSoftGREStatusTable_Object=MibTable
ruckusTunnelSoftGREStatusTable=_RuckusTunnelSoftGREStatusTable_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1))
if mibBuilder.loadTexts:ruckusTunnelSoftGREStatusTable.setStatus(_A)
_RuckusTunnelSoftGREStatusEntry_Object=MibTableRow
ruckusTunnelSoftGREStatusEntry=_RuckusTunnelSoftGREStatusEntry_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1,1))
ruckusTunnelSoftGREStatusEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:ruckusTunnelSoftGREStatusEntry.setStatus(_A)
class _RuckusTunnelSoftGRECurrentActivePeerIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusTunnelSoftGRECurrentActivePeerIp_Type.__name__=_C
_RuckusTunnelSoftGRECurrentActivePeerIp_Object=MibTableColumn
ruckusTunnelSoftGRECurrentActivePeerIp=_RuckusTunnelSoftGRECurrentActivePeerIp_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1,1,1),_RuckusTunnelSoftGRECurrentActivePeerIp_Type())
ruckusTunnelSoftGRECurrentActivePeerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusTunnelSoftGRECurrentActivePeerIp.setStatus(_A)
class _RuckusTunnelSoftGREUptime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusTunnelSoftGREUptime_Type.__name__=_G
_RuckusTunnelSoftGREUptime_Object=MibTableColumn
ruckusTunnelSoftGREUptime=_RuckusTunnelSoftGREUptime_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1,1,2),_RuckusTunnelSoftGREUptime_Type())
ruckusTunnelSoftGREUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusTunnelSoftGREUptime.setStatus(_A)
_RuckusTunnelSoftGREKeepAliveDropCounter_Type=Counter32
_RuckusTunnelSoftGREKeepAliveDropCounter_Object=MibTableColumn
ruckusTunnelSoftGREKeepAliveDropCounter=_RuckusTunnelSoftGREKeepAliveDropCounter_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1,1,3),_RuckusTunnelSoftGREKeepAliveDropCounter_Type())
ruckusTunnelSoftGREKeepAliveDropCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusTunnelSoftGREKeepAliveDropCounter.setStatus(_A)
_RuckusTunnelSoftGRETunnelChangeCounter_Type=Counter32
_RuckusTunnelSoftGRETunnelChangeCounter_Object=MibTableColumn
ruckusTunnelSoftGRETunnelChangeCounter=_RuckusTunnelSoftGRETunnelChangeCounter_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1,1,4),_RuckusTunnelSoftGRETunnelChangeCounter_Type())
ruckusTunnelSoftGRETunnelChangeCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusTunnelSoftGRETunnelChangeCounter.setStatus(_A)
_RuckusTunnelSoftGREStatusIndex_Type=Unsigned32
_RuckusTunnelSoftGREStatusIndex_Object=MibTableColumn
ruckusTunnelSoftGREStatusIndex=_RuckusTunnelSoftGREStatusIndex_Object((1,3,6,1,4,1,25053,1,1,18,1,1,1,5,1,1,200),_RuckusTunnelSoftGREStatusIndex_Type())
ruckusTunnelSoftGREStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusTunnelSoftGREStatusIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ruckusTunnelMIB':ruckusTunnelMIB,'ruckusTunnelObjects':ruckusTunnelObjects,'ruckusTunnelInfo':ruckusTunnelInfo,'ruckusTunnelSoftGREConfigInfo':ruckusTunnelSoftGREConfigInfo,'ruckusTunnelSoftGREConfigTable':ruckusTunnelSoftGREConfigTable,'ruckusTunnelSoftGREEntry':ruckusTunnelSoftGREEntry,'ruckusTunnelSoftGREAdminEnable':ruckusTunnelSoftGREAdminEnable,'ruckusTunnelSoftGREPrimaryGatewayAddress':ruckusTunnelSoftGREPrimaryGatewayAddress,'ruckusTunnelSoftGRESecondaryGatewayAddress':ruckusTunnelSoftGRESecondaryGatewayAddress,_H:ruckusTunnelSoftGREIndex,'ruckusTunnelSoftGREStatusInfo':ruckusTunnelSoftGREStatusInfo,'ruckusTunnelSoftGREStatusTable':ruckusTunnelSoftGREStatusTable,'ruckusTunnelSoftGREStatusEntry':ruckusTunnelSoftGREStatusEntry,'ruckusTunnelSoftGRECurrentActivePeerIp':ruckusTunnelSoftGRECurrentActivePeerIp,'ruckusTunnelSoftGREUptime':ruckusTunnelSoftGREUptime,'ruckusTunnelSoftGREKeepAliveDropCounter':ruckusTunnelSoftGREKeepAliveDropCounter,'ruckusTunnelSoftGRETunnelChangeCounter':ruckusTunnelSoftGRETunnelChangeCounter,_I:ruckusTunnelSoftGREStatusIndex})