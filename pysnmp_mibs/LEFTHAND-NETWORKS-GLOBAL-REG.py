_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
leftHandNetworksGlobalRegistrationModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,1))
_LeftHandNetworks_ObjectIdentity=ObjectIdentity
leftHandNetworks=_LeftHandNetworks_ObjectIdentity((1,3,6,1,4,1,9804))
if mibBuilder.loadTexts:leftHandNetworks.setStatus(_A)
_LhnRegistrations_ObjectIdentity=ObjectIdentity
lhnRegistrations=_LhnRegistrations_ObjectIdentity((1,3,6,1,4,1,9804,1))
if mibBuilder.loadTexts:lhnRegistrations.setStatus(_A)
_LhnModules_ObjectIdentity=ObjectIdentity
lhnModules=_LhnModules_ObjectIdentity((1,3,6,1,4,1,9804,1,1))
if mibBuilder.loadTexts:lhnModules.setStatus(_A)
_LhnNusDevices_ObjectIdentity=ObjectIdentity
lhnNusDevices=_LhnNusDevices_ObjectIdentity((1,3,6,1,4,1,9804,1,2))
if mibBuilder.loadTexts:lhnNusDevices.setStatus(_A)
_LhnNusCommon_ObjectIdentity=ObjectIdentity
lhnNusCommon=_LhnNusCommon_ObjectIdentity((1,3,6,1,4,1,9804,1,2,1))
if mibBuilder.loadTexts:lhnNusCommon.setStatus(_A)
_LhnGeneric_ObjectIdentity=ObjectIdentity
lhnGeneric=_LhnGeneric_ObjectIdentity((1,3,6,1,4,1,9804,2))
if mibBuilder.loadTexts:lhnGeneric.setStatus(_A)
_LhnProducts_ObjectIdentity=ObjectIdentity
lhnProducts=_LhnProducts_ObjectIdentity((1,3,6,1,4,1,9804,3))
if mibBuilder.loadTexts:lhnProducts.setStatus(_A)
_LhnNusDevicesMIBs_ObjectIdentity=ObjectIdentity
lhnNusDevicesMIBs=_LhnNusDevicesMIBs_ObjectIdentity((1,3,6,1,4,1,9804,3,1))
if mibBuilder.loadTexts:lhnNusDevicesMIBs.setStatus(_A)
_LhnNusCommonMIB_ObjectIdentity=ObjectIdentity
lhnNusCommonMIB=_LhnNusCommonMIB_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1))
if mibBuilder.loadTexts:lhnNusCommonMIB.setStatus(_A)
_LhnCapabilities_ObjectIdentity=ObjectIdentity
lhnCapabilities=_LhnCapabilities_ObjectIdentity((1,3,6,1,4,1,9804,4))
if mibBuilder.loadTexts:lhnCapabilities.setStatus(_A)
_LhnRequirements_ObjectIdentity=ObjectIdentity
lhnRequirements=_LhnRequirements_ObjectIdentity((1,3,6,1,4,1,9804,5))
if mibBuilder.loadTexts:lhnRequirements.setStatus(_A)
_LhnExperimental_ObjectIdentity=ObjectIdentity
lhnExperimental=_LhnExperimental_ObjectIdentity((1,3,6,1,4,1,9804,6))
if mibBuilder.loadTexts:lhnExperimental.setStatus(_A)
mibBuilder.exportSymbols('LEFTHAND-NETWORKS-GLOBAL-REG',**{'leftHandNetworks':leftHandNetworks,'lhnRegistrations':lhnRegistrations,'lhnModules':lhnModules,'leftHandNetworksGlobalRegistrationModule':leftHandNetworksGlobalRegistrationModule,'lhnNusDevices':lhnNusDevices,'lhnNusCommon':lhnNusCommon,'lhnGeneric':lhnGeneric,'lhnProducts':lhnProducts,'lhnNusDevicesMIBs':lhnNusDevicesMIBs,'lhnNusCommonMIB':lhnNusCommonMIB,'lhnCapabilities':lhnCapabilities,'lhnRequirements':lhnRequirements,'lhnExperimental':lhnExperimental})