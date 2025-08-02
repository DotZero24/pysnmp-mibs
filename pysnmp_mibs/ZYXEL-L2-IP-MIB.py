_G='not-accessible'
_F='zyLayer2IpInbandVid'
_E='zyLayer2IpInbandIpAddress'
_D='ZYXEL-L2-IP-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelL2Ip=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,38))
_ZyxelLayer2IpSetup_ObjectIdentity=ObjectIdentity
zyxelLayer2IpSetup=_ZyxelLayer2IpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,38,1))
_ZyLayer2IpDnsIpAddress_Type=IpAddress
_ZyLayer2IpDnsIpAddress_Object=MibScalar
zyLayer2IpDnsIpAddress=_ZyLayer2IpDnsIpAddress_Object((1,3,6,1,4,1,890,1,15,3,38,1,1),_ZyLayer2IpDnsIpAddress_Type())
zyLayer2IpDnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpDnsIpAddress.setStatus(_A)
class _ZyLayer2IpDefaultMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inBand',0),('outOfBand',1)))
_ZyLayer2IpDefaultMgmt_Type.__name__=_C
_ZyLayer2IpDefaultMgmt_Object=MibScalar
zyLayer2IpDefaultMgmt=_ZyLayer2IpDefaultMgmt_Object((1,3,6,1,4,1,890,1,15,3,38,1,2),_ZyLayer2IpDefaultMgmt_Type())
zyLayer2IpDefaultMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpDefaultMgmt.setStatus(_A)
_ZyxelLayer2IpInbandDefaultSetup_ObjectIdentity=ObjectIdentity
zyxelLayer2IpInbandDefaultSetup=_ZyxelLayer2IpInbandDefaultSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,38,1,3))
class _ZyLayer2IpInbandDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dhcpClient',0),('staticIp',1)))
_ZyLayer2IpInbandDefaultType_Type.__name__=_C
_ZyLayer2IpInbandDefaultType_Object=MibScalar
zyLayer2IpInbandDefaultType=_ZyLayer2IpInbandDefaultType_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,1),_ZyLayer2IpInbandDefaultType_Type())
zyLayer2IpInbandDefaultType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultType.setStatus(_A)
_ZyLayer2IpInbandDefaultVid_Type=Integer32
_ZyLayer2IpInbandDefaultVid_Object=MibScalar
zyLayer2IpInbandDefaultVid=_ZyLayer2IpInbandDefaultVid_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,2),_ZyLayer2IpInbandDefaultVid_Type())
zyLayer2IpInbandDefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultVid.setStatus(_A)
_ZyLayer2IpInbandDefaultStaticIpAddress_Type=IpAddress
_ZyLayer2IpInbandDefaultStaticIpAddress_Object=MibScalar
zyLayer2IpInbandDefaultStaticIpAddress=_ZyLayer2IpInbandDefaultStaticIpAddress_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,3),_ZyLayer2IpInbandDefaultStaticIpAddress_Type())
zyLayer2IpInbandDefaultStaticIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultStaticIpAddress.setStatus(_A)
_ZyLayer2IpInbandDefaultStaticMask_Type=IpAddress
_ZyLayer2IpInbandDefaultStaticMask_Object=MibScalar
zyLayer2IpInbandDefaultStaticMask=_ZyLayer2IpInbandDefaultStaticMask_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,4),_ZyLayer2IpInbandDefaultStaticMask_Type())
zyLayer2IpInbandDefaultStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultStaticMask.setStatus(_A)
_ZyLayer2IpInbandDefaultStaticGateway_Type=IpAddress
_ZyLayer2IpInbandDefaultStaticGateway_Object=MibScalar
zyLayer2IpInbandDefaultStaticGateway=_ZyLayer2IpInbandDefaultStaticGateway_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,5),_ZyLayer2IpInbandDefaultStaticGateway_Type())
zyLayer2IpInbandDefaultStaticGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultStaticGateway.setStatus(_A)
_ZyLayer2IpInbandDefaultDhcpOption60State_Type=EnabledStatus
_ZyLayer2IpInbandDefaultDhcpOption60State_Object=MibScalar
zyLayer2IpInbandDefaultDhcpOption60State=_ZyLayer2IpInbandDefaultDhcpOption60State_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,6),_ZyLayer2IpInbandDefaultDhcpOption60State_Type())
zyLayer2IpInbandDefaultDhcpOption60State.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultDhcpOption60State.setStatus(_A)
_ZyLayer2IpInbandDefaultDhcpOption60ClassId_Type=DisplayString
_ZyLayer2IpInbandDefaultDhcpOption60ClassId_Object=MibScalar
zyLayer2IpInbandDefaultDhcpOption60ClassId=_ZyLayer2IpInbandDefaultDhcpOption60ClassId_Object((1,3,6,1,4,1,890,1,15,3,38,1,3,7),_ZyLayer2IpInbandDefaultDhcpOption60ClassId_Type())
zyLayer2IpInbandDefaultDhcpOption60ClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandDefaultDhcpOption60ClassId.setStatus(_A)
_ZyLayer2IpInbandMaxNumberOfInterfaces_Type=Integer32
_ZyLayer2IpInbandMaxNumberOfInterfaces_Object=MibScalar
zyLayer2IpInbandMaxNumberOfInterfaces=_ZyLayer2IpInbandMaxNumberOfInterfaces_Object((1,3,6,1,4,1,890,1,15,3,38,1,4),_ZyLayer2IpInbandMaxNumberOfInterfaces_Type())
zyLayer2IpInbandMaxNumberOfInterfaces.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyLayer2IpInbandMaxNumberOfInterfaces.setStatus(_A)
_ZyxelLayer2IpInbandTable_Object=MibTable
zyxelLayer2IpInbandTable=_ZyxelLayer2IpInbandTable_Object((1,3,6,1,4,1,890,1,15,3,38,1,5))
if mibBuilder.loadTexts:zyxelLayer2IpInbandTable.setStatus(_A)
_ZyxelLayer2IpInbandEntry_Object=MibTableRow
zyxelLayer2IpInbandEntry=_ZyxelLayer2IpInbandEntry_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1))
zyxelLayer2IpInbandEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:zyxelLayer2IpInbandEntry.setStatus(_A)
_ZyLayer2IpInbandIpAddress_Type=IpAddress
_ZyLayer2IpInbandIpAddress_Object=MibTableColumn
zyLayer2IpInbandIpAddress=_ZyLayer2IpInbandIpAddress_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1,1),_ZyLayer2IpInbandIpAddress_Type())
zyLayer2IpInbandIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:zyLayer2IpInbandIpAddress.setStatus(_A)
_ZyLayer2IpInbandMask_Type=IpAddress
_ZyLayer2IpInbandMask_Object=MibTableColumn
zyLayer2IpInbandMask=_ZyLayer2IpInbandMask_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1,2),_ZyLayer2IpInbandMask_Type())
zyLayer2IpInbandMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandMask.setStatus(_A)
_ZyLayer2IpInbandGateway_Type=IpAddress
_ZyLayer2IpInbandGateway_Object=MibTableColumn
zyLayer2IpInbandGateway=_ZyLayer2IpInbandGateway_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1,3),_ZyLayer2IpInbandGateway_Type())
zyLayer2IpInbandGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandGateway.setStatus(_A)
_ZyLayer2IpInbandVid_Type=Integer32
_ZyLayer2IpInbandVid_Object=MibTableColumn
zyLayer2IpInbandVid=_ZyLayer2IpInbandVid_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1,4),_ZyLayer2IpInbandVid_Type())
zyLayer2IpInbandVid.setMaxAccess(_G)
if mibBuilder.loadTexts:zyLayer2IpInbandVid.setStatus(_A)
_ZyLayer2IpInbandManageableState_Type=EnabledStatus
_ZyLayer2IpInbandManageableState_Object=MibTableColumn
zyLayer2IpInbandManageableState=_ZyLayer2IpInbandManageableState_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1,5),_ZyLayer2IpInbandManageableState_Type())
zyLayer2IpInbandManageableState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer2IpInbandManageableState.setStatus(_A)
_ZyLayer2IpInbandRowStatus_Type=RowStatus
_ZyLayer2IpInbandRowStatus_Object=MibTableColumn
zyLayer2IpInbandRowStatus=_ZyLayer2IpInbandRowStatus_Object((1,3,6,1,4,1,890,1,15,3,38,1,5,1,6),_ZyLayer2IpInbandRowStatus_Type())
zyLayer2IpInbandRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyLayer2IpInbandRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelL2Ip':zyxelL2Ip,'zyxelLayer2IpSetup':zyxelLayer2IpSetup,'zyLayer2IpDnsIpAddress':zyLayer2IpDnsIpAddress,'zyLayer2IpDefaultMgmt':zyLayer2IpDefaultMgmt,'zyxelLayer2IpInbandDefaultSetup':zyxelLayer2IpInbandDefaultSetup,'zyLayer2IpInbandDefaultType':zyLayer2IpInbandDefaultType,'zyLayer2IpInbandDefaultVid':zyLayer2IpInbandDefaultVid,'zyLayer2IpInbandDefaultStaticIpAddress':zyLayer2IpInbandDefaultStaticIpAddress,'zyLayer2IpInbandDefaultStaticMask':zyLayer2IpInbandDefaultStaticMask,'zyLayer2IpInbandDefaultStaticGateway':zyLayer2IpInbandDefaultStaticGateway,'zyLayer2IpInbandDefaultDhcpOption60State':zyLayer2IpInbandDefaultDhcpOption60State,'zyLayer2IpInbandDefaultDhcpOption60ClassId':zyLayer2IpInbandDefaultDhcpOption60ClassId,'zyLayer2IpInbandMaxNumberOfInterfaces':zyLayer2IpInbandMaxNumberOfInterfaces,'zyxelLayer2IpInbandTable':zyxelLayer2IpInbandTable,'zyxelLayer2IpInbandEntry':zyxelLayer2IpInbandEntry,_E:zyLayer2IpInbandIpAddress,'zyLayer2IpInbandMask':zyLayer2IpInbandMask,'zyLayer2IpInbandGateway':zyLayer2IpInbandGateway,_F:zyLayer2IpInbandVid,'zyLayer2IpInbandManageableState':zyLayer2IpInbandManageableState,'zyLayer2IpInbandRowStatus':zyLayer2IpInbandRowStatus})