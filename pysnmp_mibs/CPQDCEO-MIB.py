_J='NotificationType'
_I='mandatory'
_H='read-only'
_G='trapDeviceMgmtUrl'
_F='trapDeviceDetails'
_E='trapDescription'
_D='DisplayString'
_C='sysName'
_B='SNMPv2-MIB'
_A='CPQDCEO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ifDescr,ifIndex=mibBuilder.importSymbols('IF-MIB','ifDescr','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysContact,sysDescr,sysLocation,sysName=mibBuilder.importSymbols(_B,'sysContact','sysDescr','sysLocation',_C)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_CpqDceo_ObjectIdentity=ObjectIdentity
cpqDceo=_CpqDceo_ObjectIdentity((1,3,6,1,4,1,232,173))
_EnvironmentalDevice_ObjectIdentity=ObjectIdentity
environmentalDevice=_EnvironmentalDevice_ObjectIdentity((1,3,6,1,4,1,232,173,1))
_DceoTrapInfo_ObjectIdentity=ObjectIdentity
dceoTrapInfo=_DceoTrapInfo_ObjectIdentity((1,3,6,1,4,1,232,173,1,1))
class _TrapDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrapDescription_Type.__name__=_D
_TrapDescription_Object=MibScalar
trapDescription=_TrapDescription_Object((1,3,6,1,4,1,232,173,1,1,1),_TrapDescription_Type())
trapDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDescription.setStatus(_I)
class _TrapDeviceDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrapDeviceDetails_Type.__name__=_D
_TrapDeviceDetails_Object=MibScalar
trapDeviceDetails=_TrapDeviceDetails_Object((1,3,6,1,4,1,232,173,1,1,2),_TrapDeviceDetails_Type())
trapDeviceDetails.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDeviceDetails.setStatus(_I)
class _TrapDeviceMgmtUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrapDeviceMgmtUrl_Type.__name__=_D
_TrapDeviceMgmtUrl_Object=MibScalar
trapDeviceMgmtUrl=_TrapDeviceMgmtUrl_Object((1,3,6,1,4,1,232,173,1,1,3),_TrapDeviceMgmtUrl_Type())
trapDeviceMgmtUrl.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDeviceMgmtUrl.setStatus(_I)
trapDceoHighPriority=NotificationType((1,3,6,1,4,1,232,173,0,1))
trapDceoHighPriority.setObjects(*((_B,_C),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapDceoHighPriority.setStatus('')
trapDceoMediumPriority=NotificationType((1,3,6,1,4,1,232,173,0,2))
trapDceoMediumPriority.setObjects(*((_B,_C),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapDceoMediumPriority.setStatus('')
trapDceoLowPriority=NotificationType((1,3,6,1,4,1,232,173,0,3))
trapDceoLowPriority.setObjects(*((_B,_C),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapDceoLowPriority.setStatus('')
mibBuilder.exportSymbols(_A,**{'cpqDceo':cpqDceo,'trapDceoHighPriority':trapDceoHighPriority,'trapDceoMediumPriority':trapDceoMediumPriority,'trapDceoLowPriority':trapDceoLowPriority,'environmentalDevice':environmentalDevice,'dceoTrapInfo':dceoTrapInfo,_E:trapDescription,_F:trapDeviceDetails,_G:trapDeviceMgmtUrl})