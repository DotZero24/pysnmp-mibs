_G='not-accessible'
_F='zyLayer3IpInbandMask'
_E='zyLayer3IpInbandIpAddress'
_D='Integer32'
_C='ZYXEL-L3-IP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelL3Ip=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,40))
_ZyxelLayer3IpSetup_ObjectIdentity=ObjectIdentity
zyxelLayer3IpSetup=_ZyxelLayer3IpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,40,1))
_ZyLayer3IpDnsIpAddress_Type=IpAddress
_ZyLayer3IpDnsIpAddress_Object=MibScalar
zyLayer3IpDnsIpAddress=_ZyLayer3IpDnsIpAddress_Object((1,3,6,1,4,1,890,1,15,3,40,1,1),_ZyLayer3IpDnsIpAddress_Type())
zyLayer3IpDnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer3IpDnsIpAddress.setStatus(_A)
class _ZyLayer3IpDefaultMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inBand',0),('outOfBand',1)))
_ZyLayer3IpDefaultMgmt_Type.__name__=_D
_ZyLayer3IpDefaultMgmt_Object=MibScalar
zyLayer3IpDefaultMgmt=_ZyLayer3IpDefaultMgmt_Object((1,3,6,1,4,1,890,1,15,3,40,1,2),_ZyLayer3IpDefaultMgmt_Type())
zyLayer3IpDefaultMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer3IpDefaultMgmt.setStatus(_A)
_ZyLayer3IpDefaultGateway_Type=IpAddress
_ZyLayer3IpDefaultGateway_Object=MibScalar
zyLayer3IpDefaultGateway=_ZyLayer3IpDefaultGateway_Object((1,3,6,1,4,1,890,1,15,3,40,1,3),_ZyLayer3IpDefaultGateway_Type())
zyLayer3IpDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer3IpDefaultGateway.setStatus(_A)
_ZyLayer3IpInbandMaxNumberOfInterfaces_Type=Integer32
_ZyLayer3IpInbandMaxNumberOfInterfaces_Object=MibScalar
zyLayer3IpInbandMaxNumberOfInterfaces=_ZyLayer3IpInbandMaxNumberOfInterfaces_Object((1,3,6,1,4,1,890,1,15,3,40,1,4),_ZyLayer3IpInbandMaxNumberOfInterfaces_Type())
zyLayer3IpInbandMaxNumberOfInterfaces.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyLayer3IpInbandMaxNumberOfInterfaces.setStatus(_A)
_ZyxelLayer3IpInbandTable_Object=MibTable
zyxelLayer3IpInbandTable=_ZyxelLayer3IpInbandTable_Object((1,3,6,1,4,1,890,1,15,3,40,1,5))
if mibBuilder.loadTexts:zyxelLayer3IpInbandTable.setStatus(_A)
_ZyxelLayer3IpInbandEntry_Object=MibTableRow
zyxelLayer3IpInbandEntry=_ZyxelLayer3IpInbandEntry_Object((1,3,6,1,4,1,890,1,15,3,40,1,5,1))
zyxelLayer3IpInbandEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:zyxelLayer3IpInbandEntry.setStatus(_A)
_ZyLayer3IpInbandIpAddress_Type=IpAddress
_ZyLayer3IpInbandIpAddress_Object=MibTableColumn
zyLayer3IpInbandIpAddress=_ZyLayer3IpInbandIpAddress_Object((1,3,6,1,4,1,890,1,15,3,40,1,5,1,1),_ZyLayer3IpInbandIpAddress_Type())
zyLayer3IpInbandIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:zyLayer3IpInbandIpAddress.setStatus(_A)
_ZyLayer3IpInbandMask_Type=IpAddress
_ZyLayer3IpInbandMask_Object=MibTableColumn
zyLayer3IpInbandMask=_ZyLayer3IpInbandMask_Object((1,3,6,1,4,1,890,1,15,3,40,1,5,1,2),_ZyLayer3IpInbandMask_Type())
zyLayer3IpInbandMask.setMaxAccess(_G)
if mibBuilder.loadTexts:zyLayer3IpInbandMask.setStatus(_A)
_ZyLayer3IpInbandVid_Type=Integer32
_ZyLayer3IpInbandVid_Object=MibTableColumn
zyLayer3IpInbandVid=_ZyLayer3IpInbandVid_Object((1,3,6,1,4,1,890,1,15,3,40,1,5,1,3),_ZyLayer3IpInbandVid_Type())
zyLayer3IpInbandVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zyLayer3IpInbandVid.setStatus(_A)
_ZyLayer3IpInbandRowStatus_Type=RowStatus
_ZyLayer3IpInbandRowStatus_Object=MibTableColumn
zyLayer3IpInbandRowStatus=_ZyLayer3IpInbandRowStatus_Object((1,3,6,1,4,1,890,1,15,3,40,1,5,1,4),_ZyLayer3IpInbandRowStatus_Type())
zyLayer3IpInbandRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyLayer3IpInbandRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelL3Ip':zyxelL3Ip,'zyxelLayer3IpSetup':zyxelLayer3IpSetup,'zyLayer3IpDnsIpAddress':zyLayer3IpDnsIpAddress,'zyLayer3IpDefaultMgmt':zyLayer3IpDefaultMgmt,'zyLayer3IpDefaultGateway':zyLayer3IpDefaultGateway,'zyLayer3IpInbandMaxNumberOfInterfaces':zyLayer3IpInbandMaxNumberOfInterfaces,'zyxelLayer3IpInbandTable':zyxelLayer3IpInbandTable,'zyxelLayer3IpInbandEntry':zyxelLayer3IpInbandEntry,_E:zyLayer3IpInbandIpAddress,_F:zyLayer3IpInbandMask,'zyLayer3IpInbandVid':zyLayer3IpInbandVid,'zyLayer3IpInbandRowStatus':zyLayer3IpInbandRowStatus})