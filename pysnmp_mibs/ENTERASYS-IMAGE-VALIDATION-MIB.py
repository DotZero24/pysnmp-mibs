_Q='etsysImageValidationConfigGroup'
_P='etsysImageValidationSnmpAddress'
_O='etsysImageValidationSnmpAddressType'
_N='etsysImageValidationIcmpAddress'
_M='etsysImageValidationIcmpAddressType'
_L='etsysImageValidationOperations'
_K='etsysImageValidationPeriod'
_J='etsysImageValidationEnable'
_I='00000000'
_H='etsysImageValidationConfig'
_G='Unsigned32'
_F='EnabledStatus'
_E='InetAddressType'
_D='InetAddress'
_C='read-write'
_B='ENTERASYS-IMAGE-VALIDATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysImageValidationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,47))
if mibBuilder.loadTexts:etsysImageValidationMIB.setRevisions(('2004-04-02 21:34',))
_EtsysImageValidationObjects_ObjectIdentity=ObjectIdentity
etsysImageValidationObjects=_EtsysImageValidationObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,47,1))
_EtsysImageValidationConfig_ObjectIdentity=ObjectIdentity
etsysImageValidationConfig=_EtsysImageValidationConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,47,1,1))
class _EtsysImageValidationEnable_Type(EnabledStatus):defaultValue=2
_EtsysImageValidationEnable_Type.__name__=_F
_EtsysImageValidationEnable_Object=MibScalar
etsysImageValidationEnable=_EtsysImageValidationEnable_Object((1,3,6,1,4,1,5624,1,2,47,1,1,1),_EtsysImageValidationEnable_Type())
etsysImageValidationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationEnable.setStatus(_A)
class _EtsysImageValidationPeriod_Type(Unsigned32):defaultValue=600
_EtsysImageValidationPeriod_Type.__name__=_G
_EtsysImageValidationPeriod_Object=MibScalar
etsysImageValidationPeriod=_EtsysImageValidationPeriod_Object((1,3,6,1,4,1,5624,1,2,47,1,1,2),_EtsysImageValidationPeriod_Type())
etsysImageValidationPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationPeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysImageValidationPeriod.setUnits('seconds')
class _EtsysImageValidationOperations_Type(Bits):namedValues=NamedValues(*((_H,0),('etsysImageValidationIcmp',1),('etsysImageValidationSnmp',2)))
_EtsysImageValidationOperations_Type.__name__='Bits'
_EtsysImageValidationOperations_Object=MibScalar
etsysImageValidationOperations=_EtsysImageValidationOperations_Object((1,3,6,1,4,1,5624,1,2,47,1,1,3),_EtsysImageValidationOperations_Type())
etsysImageValidationOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationOperations.setStatus(_A)
class _EtsysImageValidationIcmpAddressType_Type(InetAddressType):defaultValue=1
_EtsysImageValidationIcmpAddressType_Type.__name__=_E
_EtsysImageValidationIcmpAddressType_Object=MibScalar
etsysImageValidationIcmpAddressType=_EtsysImageValidationIcmpAddressType_Object((1,3,6,1,4,1,5624,1,2,47,1,1,4),_EtsysImageValidationIcmpAddressType_Type())
etsysImageValidationIcmpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationIcmpAddressType.setStatus(_A)
class _EtsysImageValidationIcmpAddress_Type(InetAddress):defaultHexValue=_I
_EtsysImageValidationIcmpAddress_Type.__name__=_D
_EtsysImageValidationIcmpAddress_Object=MibScalar
etsysImageValidationIcmpAddress=_EtsysImageValidationIcmpAddress_Object((1,3,6,1,4,1,5624,1,2,47,1,1,5),_EtsysImageValidationIcmpAddress_Type())
etsysImageValidationIcmpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationIcmpAddress.setStatus(_A)
class _EtsysImageValidationSnmpAddressType_Type(InetAddressType):defaultValue=1
_EtsysImageValidationSnmpAddressType_Type.__name__=_E
_EtsysImageValidationSnmpAddressType_Object=MibScalar
etsysImageValidationSnmpAddressType=_EtsysImageValidationSnmpAddressType_Object((1,3,6,1,4,1,5624,1,2,47,1,1,6),_EtsysImageValidationSnmpAddressType_Type())
etsysImageValidationSnmpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationSnmpAddressType.setStatus(_A)
class _EtsysImageValidationSnmpAddress_Type(InetAddress):defaultHexValue=_I
_EtsysImageValidationSnmpAddress_Type.__name__=_D
_EtsysImageValidationSnmpAddress_Object=MibScalar
etsysImageValidationSnmpAddress=_EtsysImageValidationSnmpAddress_Object((1,3,6,1,4,1,5624,1,2,47,1,1,7),_EtsysImageValidationSnmpAddress_Type())
etsysImageValidationSnmpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysImageValidationSnmpAddress.setStatus(_A)
_EtsysImageValidationConformance_ObjectIdentity=ObjectIdentity
etsysImageValidationConformance=_EtsysImageValidationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,47,2))
_EtsysImageValidationGroups_ObjectIdentity=ObjectIdentity
etsysImageValidationGroups=_EtsysImageValidationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,47,2,1))
_EtsysImageValidationCompliances_ObjectIdentity=ObjectIdentity
etsysImageValidationCompliances=_EtsysImageValidationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,47,2,2))
etsysImageValidationConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,47,2,1,1))
etsysImageValidationConfigGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:etsysImageValidationConfigGroup.setStatus(_A)
etsysImageValidationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,47,2,2,1))
etsysImageValidationCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:etsysImageValidationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysImageValidationMIB':etsysImageValidationMIB,'etsysImageValidationObjects':etsysImageValidationObjects,_H:etsysImageValidationConfig,_J:etsysImageValidationEnable,_K:etsysImageValidationPeriod,_L:etsysImageValidationOperations,_M:etsysImageValidationIcmpAddressType,_N:etsysImageValidationIcmpAddress,_O:etsysImageValidationSnmpAddressType,_P:etsysImageValidationSnmpAddress,'etsysImageValidationConformance':etsysImageValidationConformance,'etsysImageValidationGroups':etsysImageValidationGroups,_Q:etsysImageValidationConfigGroup,'etsysImageValidationCompliances':etsysImageValidationCompliances,'etsysImageValidationCompliance':etsysImageValidationCompliance})