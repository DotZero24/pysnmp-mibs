_I='emergencyCallUrgentGatewayVer1'
_H='emergencyCallUrgentGatewayTargetAddress'
_G='emergencyCallUrgentGatewayDigitMap'
_F='emergencyCallUrgentGatewayEnable'
_E='MxEnableState'
_D='read-write'
_C='OctetString'
_B='MX-EMERGENCY-CALL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
emergencyCallMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,75))
if mibBuilder.loadTexts:emergencyCallMIB.setRevisions(('1903-03-03 00:00',))
_EmergencyCallMIBObjects_ObjectIdentity=ObjectIdentity
emergencyCallMIBObjects=_EmergencyCallMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,75,1))
_EmergencyCallUrgentGatewayCustomization_ObjectIdentity=ObjectIdentity
emergencyCallUrgentGatewayCustomization=_EmergencyCallUrgentGatewayCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,75,1,5))
class _EmergencyCallUrgentGatewayEnable_Type(MxEnableState):defaultValue=0
_EmergencyCallUrgentGatewayEnable_Type.__name__=_E
_EmergencyCallUrgentGatewayEnable_Object=MibScalar
emergencyCallUrgentGatewayEnable=_EmergencyCallUrgentGatewayEnable_Object((1,3,6,1,4,1,4935,15,75,1,5,5),_EmergencyCallUrgentGatewayEnable_Type())
emergencyCallUrgentGatewayEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:emergencyCallUrgentGatewayEnable.setStatus(_A)
class _EmergencyCallUrgentGatewayDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EmergencyCallUrgentGatewayDigitMap_Type.__name__=_C
_EmergencyCallUrgentGatewayDigitMap_Object=MibScalar
emergencyCallUrgentGatewayDigitMap=_EmergencyCallUrgentGatewayDigitMap_Object((1,3,6,1,4,1,4935,15,75,1,5,10),_EmergencyCallUrgentGatewayDigitMap_Type())
emergencyCallUrgentGatewayDigitMap.setMaxAccess(_D)
if mibBuilder.loadTexts:emergencyCallUrgentGatewayDigitMap.setStatus(_A)
class _EmergencyCallUrgentGatewayTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_EmergencyCallUrgentGatewayTargetAddress_Type.__name__=_C
_EmergencyCallUrgentGatewayTargetAddress_Object=MibScalar
emergencyCallUrgentGatewayTargetAddress=_EmergencyCallUrgentGatewayTargetAddress_Object((1,3,6,1,4,1,4935,15,75,1,5,15),_EmergencyCallUrgentGatewayTargetAddress_Type())
emergencyCallUrgentGatewayTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:emergencyCallUrgentGatewayTargetAddress.setStatus(_A)
_EmergencyCallConformance_ObjectIdentity=ObjectIdentity
emergencyCallConformance=_EmergencyCallConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,75,2))
_EmergencyCallCompliances_ObjectIdentity=ObjectIdentity
emergencyCallCompliances=_EmergencyCallCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,75,2,1))
_EmergencyCallGroups_ObjectIdentity=ObjectIdentity
emergencyCallGroups=_EmergencyCallGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,75,2,5))
emergencyCallUrgentGatewayVer1=ObjectGroup((1,3,6,1,4,1,4935,15,75,2,5,5))
emergencyCallUrgentGatewayVer1.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:emergencyCallUrgentGatewayVer1.setStatus(_A)
emergencyCallComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,75,2,1,1))
emergencyCallComplVer1.setObjects((_B,_I))
if mibBuilder.loadTexts:emergencyCallComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'emergencyCallMIB':emergencyCallMIB,'emergencyCallMIBObjects':emergencyCallMIBObjects,'emergencyCallUrgentGatewayCustomization':emergencyCallUrgentGatewayCustomization,_F:emergencyCallUrgentGatewayEnable,_G:emergencyCallUrgentGatewayDigitMap,_H:emergencyCallUrgentGatewayTargetAddress,'emergencyCallConformance':emergencyCallConformance,'emergencyCallCompliances':emergencyCallCompliances,'emergencyCallComplVer1':emergencyCallComplVer1,'emergencyCallGroups':emergencyCallGroups,_I:emergencyCallUrgentGatewayVer1})