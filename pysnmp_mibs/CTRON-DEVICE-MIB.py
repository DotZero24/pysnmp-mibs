_C='mandatory'
_B='read-write'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDevice,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDevice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
_CommonDev_ObjectIdentity=ObjectIdentity
commonDev=_CommonDev_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,5,1))
_ComDeviceIPAddress_Type=IpAddress
_ComDeviceIPAddress_Object=MibScalar
comDeviceIPAddress=_ComDeviceIPAddress_Object((1,3,6,1,4,1,52,4,1,1,5,1,1),_ComDeviceIPAddress_Type())
comDeviceIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:comDeviceIPAddress.setStatus(_C)
class _ComDeviceTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6),ValueSizeConstraint(8,8))
_ComDeviceTime_Type.__name__=_A
_ComDeviceTime_Object=MibScalar
comDeviceTime=_ComDeviceTime_Object((1,3,6,1,4,1,52,4,1,1,5,1,2),_ComDeviceTime_Type())
comDeviceTime.setMaxAccess(_B)
if mibBuilder.loadTexts:comDeviceTime.setStatus(_C)
class _ComDeviceDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ComDeviceDate_Type.__name__=_A
_ComDeviceDate_Object=MibScalar
comDeviceDate=_ComDeviceDate_Object((1,3,6,1,4,1,52,4,1,1,5,1,3),_ComDeviceDate_Type())
comDeviceDate.setMaxAccess(_B)
if mibBuilder.loadTexts:comDeviceDate.setStatus(_C)
mibBuilder.exportSymbols('CTRON-DEVICE-MIB',**{'commonDev':commonDev,'comDeviceIPAddress':comDeviceIPAddress,'comDeviceTime':comDeviceTime,'comDeviceDate':comDeviceDate})