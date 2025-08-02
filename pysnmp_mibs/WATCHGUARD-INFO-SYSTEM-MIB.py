_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgInfoModule=ModuleIdentity((1,3,6,1,4,1,3097,6))
if mibBuilder.loadTexts:wgInfoModule.setRevisions(('2007-01-25 12:00',))
_WgInfoSystem_ObjectIdentity=ObjectIdentity
wgInfoSystem=_WgInfoSystem_ObjectIdentity((1,3,6,1,4,1,3097,6,1))
if mibBuilder.loadTexts:wgInfoSystem.setStatus(_A)
_WgInfoSystemCurrentTime_Type=DateAndTime
_WgInfoSystemCurrentTime_Object=MibScalar
wgInfoSystemCurrentTime=_WgInfoSystemCurrentTime_Object((1,3,6,1,4,1,3097,6,1,1),_WgInfoSystemCurrentTime_Type())
wgInfoSystemCurrentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wgInfoSystemCurrentTime.setStatus(_A)
class _WgInfoGavService_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WgInfoGavService_Type.__name__=_B
_WgInfoGavService_Object=MibScalar
wgInfoGavService=_WgInfoGavService_Object((1,3,6,1,4,1,3097,6,1,3),_WgInfoGavService_Type())
wgInfoGavService.setMaxAccess(_C)
if mibBuilder.loadTexts:wgInfoGavService.setStatus(_A)
class _WgInfoIpsService_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WgInfoIpsService_Type.__name__=_B
_WgInfoIpsService_Object=MibScalar
wgInfoIpsService=_WgInfoIpsService_Object((1,3,6,1,4,1,3097,6,1,4),_WgInfoIpsService_Type())
wgInfoIpsService.setMaxAccess(_C)
if mibBuilder.loadTexts:wgInfoIpsService.setStatus(_A)
mibBuilder.exportSymbols('WATCHGUARD-INFO-SYSTEM-MIB',**{'wgInfoModule':wgInfoModule,'wgInfoSystem':wgInfoSystem,'wgInfoSystemCurrentTime':wgInfoSystemCurrentTime,'wgInfoGavService':wgInfoGavService,'wgInfoIpsService':wgInfoIpsService})