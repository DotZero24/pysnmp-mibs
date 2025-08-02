_N='zyVrrpInfoVirtualId'
_M='zyVrrpInfoIpMaskBits'
_L='zyVrrpInfoIpAddress'
_K='zyVrrpUplinkGateway'
_J='zyVrrpVirtualId'
_I='Integer32'
_H='read-only'
_G='zyRouteDomainIpMaskBits'
_F='zyRouteDomainIpAddress'
_E='not-accessible'
_D='ZYXEL-IP-FORWARD-MIB'
_C='ZYXEL-VRRP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyRouteDomainIpAddress,zyRouteDomainIpMaskBits=mibBuilder.importSymbols(_D,_F,_G)
zyxelVrrp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,91))
_ZyxelVrrpSetup_ObjectIdentity=ObjectIdentity
zyxelVrrpSetup=_ZyxelVrrpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,91,1))
_ZyVrrpMaxNumberOfVirtualRouters_Type=Integer32
_ZyVrrpMaxNumberOfVirtualRouters_Object=MibScalar
zyVrrpMaxNumberOfVirtualRouters=_ZyVrrpMaxNumberOfVirtualRouters_Object((1,3,6,1,4,1,890,1,15,3,91,1,1),_ZyVrrpMaxNumberOfVirtualRouters_Type())
zyVrrpMaxNumberOfVirtualRouters.setMaxAccess(_H)
if mibBuilder.loadTexts:zyVrrpMaxNumberOfVirtualRouters.setStatus(_A)
_ZyxelVrrpTable_Object=MibTable
zyxelVrrpTable=_ZyxelVrrpTable_Object((1,3,6,1,4,1,890,1,15,3,91,1,2))
if mibBuilder.loadTexts:zyxelVrrpTable.setStatus(_A)
_ZyxelVrrpEntry_Object=MibTableRow
zyxelVrrpEntry=_ZyxelVrrpEntry_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1))
zyxelVrrpEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:zyxelVrrpEntry.setStatus(_A)
_ZyVrrpVirtualId_Type=Integer32
_ZyVrrpVirtualId_Object=MibTableColumn
zyVrrpVirtualId=_ZyVrrpVirtualId_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,1),_ZyVrrpVirtualId_Type())
zyVrrpVirtualId.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVrrpVirtualId.setStatus(_A)
_ZyVrrpUplinkGateway_Type=IpAddress
_ZyVrrpUplinkGateway_Object=MibTableColumn
zyVrrpUplinkGateway=_ZyVrrpUplinkGateway_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,2),_ZyVrrpUplinkGateway_Type())
zyVrrpUplinkGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVrrpUplinkGateway.setStatus(_A)
_ZyVrrpPreemptState_Type=EnabledStatus
_ZyVrrpPreemptState_Object=MibTableColumn
zyVrrpPreemptState=_ZyVrrpPreemptState_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,3),_ZyVrrpPreemptState_Type())
zyVrrpPreemptState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpPreemptState.setStatus(_A)
_ZyVrrpInterval_Type=Integer32
_ZyVrrpInterval_Object=MibTableColumn
zyVrrpInterval=_ZyVrrpInterval_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,4),_ZyVrrpInterval_Type())
zyVrrpInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpInterval.setStatus(_A)
_ZyVrrpPriority_Type=Integer32
_ZyVrrpPriority_Object=MibTableColumn
zyVrrpPriority=_ZyVrrpPriority_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,5),_ZyVrrpPriority_Type())
zyVrrpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpPriority.setStatus(_A)
_ZyVrrpPrimaryVirtualpAddress_Type=IpAddress
_ZyVrrpPrimaryVirtualpAddress_Object=MibTableColumn
zyVrrpPrimaryVirtualpAddress=_ZyVrrpPrimaryVirtualpAddress_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,6),_ZyVrrpPrimaryVirtualpAddress_Type())
zyVrrpPrimaryVirtualpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpPrimaryVirtualpAddress.setStatus(_A)
_ZyVrrpName_Type=DisplayString
_ZyVrrpName_Object=MibTableColumn
zyVrrpName=_ZyVrrpName_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,7),_ZyVrrpName_Type())
zyVrrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpName.setStatus(_A)
_ZyVrrpSecondaryVirtualIpAddress_Type=IpAddress
_ZyVrrpSecondaryVirtualIpAddress_Object=MibTableColumn
zyVrrpSecondaryVirtualIpAddress=_ZyVrrpSecondaryVirtualIpAddress_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,8),_ZyVrrpSecondaryVirtualIpAddress_Type())
zyVrrpSecondaryVirtualIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpSecondaryVirtualIpAddress.setStatus(_A)
_ZyVrrpPingState_Type=EnabledStatus
_ZyVrrpPingState_Object=MibTableColumn
zyVrrpPingState=_ZyVrrpPingState_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,9),_ZyVrrpPingState_Type())
zyVrrpPingState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpPingState.setStatus(_A)
_ZyVrrpRowStatus_Type=RowStatus
_ZyVrrpRowStatus_Object=MibTableColumn
zyVrrpRowStatus=_ZyVrrpRowStatus_Object((1,3,6,1,4,1,890,1,15,3,91,1,2,1,10),_ZyVrrpRowStatus_Type())
zyVrrpRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyVrrpRowStatus.setStatus(_A)
_ZyxelVrrpDomainTable_Object=MibTable
zyxelVrrpDomainTable=_ZyxelVrrpDomainTable_Object((1,3,6,1,4,1,890,1,15,3,91,1,3))
if mibBuilder.loadTexts:zyxelVrrpDomainTable.setStatus(_A)
_ZyxelVrrpDomainEntry_Object=MibTableRow
zyxelVrrpDomainEntry=_ZyxelVrrpDomainEntry_Object((1,3,6,1,4,1,890,1,15,3,91,1,3,1))
zyxelVrrpDomainEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:zyxelVrrpDomainEntry.setStatus(_A)
class _ZyVrrpDomainAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('simple',1)))
_ZyVrrpDomainAuthenticationType_Type.__name__=_I
_ZyVrrpDomainAuthenticationType_Object=MibTableColumn
zyVrrpDomainAuthenticationType=_ZyVrrpDomainAuthenticationType_Object((1,3,6,1,4,1,890,1,15,3,91,1,3,1,1),_ZyVrrpDomainAuthenticationType_Type())
zyVrrpDomainAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpDomainAuthenticationType.setStatus(_A)
_ZyVrrpDomainAuthenticationKey_Type=DisplayString
_ZyVrrpDomainAuthenticationKey_Object=MibTableColumn
zyVrrpDomainAuthenticationKey=_ZyVrrpDomainAuthenticationKey_Object((1,3,6,1,4,1,890,1,15,3,91,1,3,1,2),_ZyVrrpDomainAuthenticationKey_Type())
zyVrrpDomainAuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVrrpDomainAuthenticationKey.setStatus(_A)
_ZyxelVrrpStatus_ObjectIdentity=ObjectIdentity
zyxelVrrpStatus=_ZyxelVrrpStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,91,2))
_ZyxelVrrpInfoTable_Object=MibTable
zyxelVrrpInfoTable=_ZyxelVrrpInfoTable_Object((1,3,6,1,4,1,890,1,15,3,91,2,1))
if mibBuilder.loadTexts:zyxelVrrpInfoTable.setStatus(_A)
_ZyxelVrrpInfoEntry_Object=MibTableRow
zyxelVrrpInfoEntry=_ZyxelVrrpInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,91,2,1,1))
zyxelVrrpInfoEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:zyxelVrrpInfoEntry.setStatus(_A)
_ZyVrrpInfoIpAddress_Type=IpAddress
_ZyVrrpInfoIpAddress_Object=MibTableColumn
zyVrrpInfoIpAddress=_ZyVrrpInfoIpAddress_Object((1,3,6,1,4,1,890,1,15,3,91,2,1,1,1),_ZyVrrpInfoIpAddress_Type())
zyVrrpInfoIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVrrpInfoIpAddress.setStatus(_A)
_ZyVrrpInfoIpMaskBits_Type=Integer32
_ZyVrrpInfoIpMaskBits_Object=MibTableColumn
zyVrrpInfoIpMaskBits=_ZyVrrpInfoIpMaskBits_Object((1,3,6,1,4,1,890,1,15,3,91,2,1,1,2),_ZyVrrpInfoIpMaskBits_Type())
zyVrrpInfoIpMaskBits.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVrrpInfoIpMaskBits.setStatus(_A)
_ZyVrrpInfoVirtualId_Type=Integer32
_ZyVrrpInfoVirtualId_Object=MibTableColumn
zyVrrpInfoVirtualId=_ZyVrrpInfoVirtualId_Object((1,3,6,1,4,1,890,1,15,3,91,2,1,1,3),_ZyVrrpInfoVirtualId_Type())
zyVrrpInfoVirtualId.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVrrpInfoVirtualId.setStatus(_A)
_ZyVrrpInfoVirtualRouterStatus_Type=DisplayString
_ZyVrrpInfoVirtualRouterStatus_Object=MibTableColumn
zyVrrpInfoVirtualRouterStatus=_ZyVrrpInfoVirtualRouterStatus_Object((1,3,6,1,4,1,890,1,15,3,91,2,1,1,4),_ZyVrrpInfoVirtualRouterStatus_Type())
zyVrrpInfoVirtualRouterStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zyVrrpInfoVirtualRouterStatus.setStatus(_A)
_ZyVrrpInfoUplinkStatus_Type=DisplayString
_ZyVrrpInfoUplinkStatus_Object=MibTableColumn
zyVrrpInfoUplinkStatus=_ZyVrrpInfoUplinkStatus_Object((1,3,6,1,4,1,890,1,15,3,91,2,1,1,5),_ZyVrrpInfoUplinkStatus_Type())
zyVrrpInfoUplinkStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zyVrrpInfoUplinkStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelVrrp':zyxelVrrp,'zyxelVrrpSetup':zyxelVrrpSetup,'zyVrrpMaxNumberOfVirtualRouters':zyVrrpMaxNumberOfVirtualRouters,'zyxelVrrpTable':zyxelVrrpTable,'zyxelVrrpEntry':zyxelVrrpEntry,_J:zyVrrpVirtualId,_K:zyVrrpUplinkGateway,'zyVrrpPreemptState':zyVrrpPreemptState,'zyVrrpInterval':zyVrrpInterval,'zyVrrpPriority':zyVrrpPriority,'zyVrrpPrimaryVirtualpAddress':zyVrrpPrimaryVirtualpAddress,'zyVrrpName':zyVrrpName,'zyVrrpSecondaryVirtualIpAddress':zyVrrpSecondaryVirtualIpAddress,'zyVrrpPingState':zyVrrpPingState,'zyVrrpRowStatus':zyVrrpRowStatus,'zyxelVrrpDomainTable':zyxelVrrpDomainTable,'zyxelVrrpDomainEntry':zyxelVrrpDomainEntry,'zyVrrpDomainAuthenticationType':zyVrrpDomainAuthenticationType,'zyVrrpDomainAuthenticationKey':zyVrrpDomainAuthenticationKey,'zyxelVrrpStatus':zyxelVrrpStatus,'zyxelVrrpInfoTable':zyxelVrrpInfoTable,'zyxelVrrpInfoEntry':zyxelVrrpInfoEntry,_L:zyVrrpInfoIpAddress,_M:zyVrrpInfoIpMaskBits,_N:zyVrrpInfoVirtualId,'zyVrrpInfoVirtualRouterStatus':zyVrrpInfoVirtualRouterStatus,'zyVrrpInfoUplinkStatus':zyVrrpInfoUplinkStatus})