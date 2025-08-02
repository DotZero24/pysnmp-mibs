_C='DisplayString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusCommonHwInfoModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonHwInfoModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ruckusHwInfoMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,2,1))
_RuckusHwInfoObjects_ObjectIdentity=ObjectIdentity
ruckusHwInfoObjects=_RuckusHwInfoObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,2,1,1))
_RuckusHwInfo_ObjectIdentity=ObjectIdentity
ruckusHwInfo=_RuckusHwInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,2,1,1,1))
class _RuckusHwInfoModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RuckusHwInfoModelNumber_Type.__name__=_C
_RuckusHwInfoModelNumber_Object=MibScalar
ruckusHwInfoModelNumber=_RuckusHwInfoModelNumber_Object((1,3,6,1,4,1,25053,1,1,2,1,1,1,1),_RuckusHwInfoModelNumber_Type())
ruckusHwInfoModelNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusHwInfoModelNumber.setStatus(_B)
class _RuckusHwInfoSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RuckusHwInfoSerialNumber_Type.__name__=_C
_RuckusHwInfoSerialNumber_Object=MibScalar
ruckusHwInfoSerialNumber=_RuckusHwInfoSerialNumber_Object((1,3,6,1,4,1,25053,1,1,2,1,1,1,2),_RuckusHwInfoSerialNumber_Type())
ruckusHwInfoSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusHwInfoSerialNumber.setStatus(_B)
class _RuckusHwInfoCustomerID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusHwInfoCustomerID_Type.__name__=_C
_RuckusHwInfoCustomerID_Object=MibScalar
ruckusHwInfoCustomerID=_RuckusHwInfoCustomerID_Object((1,3,6,1,4,1,25053,1,1,2,1,1,1,3),_RuckusHwInfoCustomerID_Type())
ruckusHwInfoCustomerID.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusHwInfoCustomerID.setStatus(_B)
_RuckusHwInfoHWMajorRevision_Type=Unsigned32
_RuckusHwInfoHWMajorRevision_Object=MibScalar
ruckusHwInfoHWMajorRevision=_RuckusHwInfoHWMajorRevision_Object((1,3,6,1,4,1,25053,1,1,2,1,1,1,4),_RuckusHwInfoHWMajorRevision_Type())
ruckusHwInfoHWMajorRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusHwInfoHWMajorRevision.setStatus(_B)
_RuckusHwInfoHWMinorRevision_Type=Unsigned32
_RuckusHwInfoHWMinorRevision_Object=MibScalar
ruckusHwInfoHWMinorRevision=_RuckusHwInfoHWMinorRevision_Object((1,3,6,1,4,1,25053,1,1,2,1,1,1,5),_RuckusHwInfoHWMinorRevision_Type())
ruckusHwInfoHWMinorRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusHwInfoHWMinorRevision.setStatus(_B)
class _RuckusHwInfoTemperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RuckusHwInfoTemperature_Type.__name__=_C
_RuckusHwInfoTemperature_Object=MibScalar
ruckusHwInfoTemperature=_RuckusHwInfoTemperature_Object((1,3,6,1,4,1,25053,1,1,2,1,1,1,10),_RuckusHwInfoTemperature_Type())
ruckusHwInfoTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusHwInfoTemperature.setStatus(_B)
_RuckusHwInfoEvents_ObjectIdentity=ObjectIdentity
ruckusHwInfoEvents=_RuckusHwInfoEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,2,1,2))
mibBuilder.exportSymbols('RUCKUS-HWINFO-MIB',**{'ruckusHwInfoMIB':ruckusHwInfoMIB,'ruckusHwInfoObjects':ruckusHwInfoObjects,'ruckusHwInfo':ruckusHwInfo,'ruckusHwInfoModelNumber':ruckusHwInfoModelNumber,'ruckusHwInfoSerialNumber':ruckusHwInfoSerialNumber,'ruckusHwInfoCustomerID':ruckusHwInfoCustomerID,'ruckusHwInfoHWMajorRevision':ruckusHwInfoHWMajorRevision,'ruckusHwInfoHWMinorRevision':ruckusHwInfoHWMinorRevision,'ruckusHwInfoTemperature':ruckusHwInfoTemperature,'ruckusHwInfoEvents':ruckusHwInfoEvents})