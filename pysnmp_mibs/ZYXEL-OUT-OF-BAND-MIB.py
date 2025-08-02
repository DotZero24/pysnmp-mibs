_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelOutOfBand=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,58))
_ZyxelOutOfBandIpSetup_ObjectIdentity=ObjectIdentity
zyxelOutOfBandIpSetup=_ZyxelOutOfBandIpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,58,1))
_ZyOutOfBandIpAddress_Type=IpAddress
_ZyOutOfBandIpAddress_Object=MibScalar
zyOutOfBandIpAddress=_ZyOutOfBandIpAddress_Object((1,3,6,1,4,1,890,1,15,3,58,1,1),_ZyOutOfBandIpAddress_Type())
zyOutOfBandIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:zyOutOfBandIpAddress.setStatus(_B)
_ZyOutOfBandSubnetMask_Type=IpAddress
_ZyOutOfBandSubnetMask_Object=MibScalar
zyOutOfBandSubnetMask=_ZyOutOfBandSubnetMask_Object((1,3,6,1,4,1,890,1,15,3,58,1,2),_ZyOutOfBandSubnetMask_Type())
zyOutOfBandSubnetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:zyOutOfBandSubnetMask.setStatus(_B)
_ZyOutOfBandGateway_Type=IpAddress
_ZyOutOfBandGateway_Object=MibScalar
zyOutOfBandGateway=_ZyOutOfBandGateway_Object((1,3,6,1,4,1,890,1,15,3,58,1,3),_ZyOutOfBandGateway_Type())
zyOutOfBandGateway.setMaxAccess(_A)
if mibBuilder.loadTexts:zyOutOfBandGateway.setStatus(_B)
mibBuilder.exportSymbols('ZYXEL-OUT-OF-BAND-MIB',**{'zyxelOutOfBand':zyxelOutOfBand,'zyxelOutOfBandIpSetup':zyxelOutOfBandIpSetup,'zyOutOfBandIpAddress':zyOutOfBandIpAddress,'zyOutOfBandSubnetMask':zyOutOfBandSubnetMask,'zyOutOfBandGateway':zyOutOfBandGateway})