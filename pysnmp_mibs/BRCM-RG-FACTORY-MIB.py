_D='DisplayString'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataFactory,=mibBuilder.importSymbols('BRCM-CABLEDATA-FACTORY-MIB','cableDataFactory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
residentialGatewayFactory=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,7))
if mibBuilder.loadTexts:residentialGatewayFactory.setRevisions(('2007-02-05 00:00','2003-01-30 00:00'))
_RgFactoryBase_ObjectIdentity=ObjectIdentity
rgFactoryBase=_RgFactoryBase_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,7,1))
class _RgInitialMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('residentialGateway',2),('cableHome10',3),('cableHome11',4)))
_RgInitialMode_Type.__name__=_C
_RgInitialMode_Object=MibScalar
rgInitialMode=_RgInitialMode_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,1),_RgInitialMode_Type())
rgInitialMode.setMaxAccess(_A)
if mibBuilder.loadTexts:rgInitialMode.setStatus(_B)
_RgRipAuthEnabled_Type=TruthValue
_RgRipAuthEnabled_Object=MibScalar
rgRipAuthEnabled=_RgRipAuthEnabled_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,2),_RgRipAuthEnabled_Type())
rgRipAuthEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipAuthEnabled.setStatus(_B)
class _RgRipAuthKeyValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RgRipAuthKeyValue_Type.__name__=_D
_RgRipAuthKeyValue_Object=MibScalar
rgRipAuthKeyValue=_RgRipAuthKeyValue_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,3),_RgRipAuthKeyValue_Type())
rgRipAuthKeyValue.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipAuthKeyValue.setStatus(_B)
class _RgRipAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_RgRipAuthKeyId_Type.__name__=_C
_RgRipAuthKeyId_Object=MibScalar
rgRipAuthKeyId=_RgRipAuthKeyId_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,4),_RgRipAuthKeyId_Type())
rgRipAuthKeyId.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipAuthKeyId.setStatus(_B)
class _RgRipReportingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16535))
_RgRipReportingInterval_Type.__name__=_C
_RgRipReportingInterval_Object=MibScalar
rgRipReportingInterval=_RgRipReportingInterval_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,5),_RgRipReportingInterval_Type())
rgRipReportingInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipReportingInterval.setStatus(_B)
if mibBuilder.loadTexts:rgRipReportingInterval.setUnits('seconds')
_RgRipUnicastDestIpAddress_Type=IpAddress
_RgRipUnicastDestIpAddress_Object=MibScalar
rgRipUnicastDestIpAddress=_RgRipUnicastDestIpAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,6),_RgRipUnicastDestIpAddress_Type())
rgRipUnicastDestIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipUnicastDestIpAddress.setStatus(_B)
_RgRipSubnetMask_Type=IpAddress
_RgRipSubnetMask_Object=MibScalar
rgRipSubnetMask=_RgRipSubnetMask_Object((1,3,6,1,4,1,4413,2,99,1,1,2,7,1,7),_RgRipSubnetMask_Type())
rgRipSubnetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipSubnetMask.setStatus(_B)
mibBuilder.exportSymbols('BRCM-RG-FACTORY-MIB',**{'residentialGatewayFactory':residentialGatewayFactory,'rgFactoryBase':rgFactoryBase,'rgInitialMode':rgInitialMode,'rgRipAuthEnabled':rgRipAuthEnabled,'rgRipAuthKeyValue':rgRipAuthKeyValue,'rgRipAuthKeyId':rgRipAuthKeyId,'rgRipReportingInterval':rgRipReportingInterval,'rgRipUnicastDestIpAddress':rgRipUnicastDestIpAddress,'rgRipSubnetMask':rgRipSubnetMask})