_F='juniLicenseGroup'
_E='juniLicenseLineModuleIfLimitValue'
_D='juniLicenseLineModuleIfLimitKey'
_C='DisplayString'
_B='Juniper-LICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
juniLicenseMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,76))
if mibBuilder.loadTexts:juniLicenseMIB.setRevisions(('2004-09-14 19:24',))
_JuniLicenseObjects_ObjectIdentity=ObjectIdentity
juniLicenseObjects=_JuniLicenseObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,76,1))
class _JuniLicenseLineModuleIfLimitKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_JuniLicenseLineModuleIfLimitKey_Type.__name__=_C
_JuniLicenseLineModuleIfLimitKey_Object=MibScalar
juniLicenseLineModuleIfLimitKey=_JuniLicenseLineModuleIfLimitKey_Object((1,3,6,1,4,1,4874,2,2,76,1,1),_JuniLicenseLineModuleIfLimitKey_Type())
juniLicenseLineModuleIfLimitKey.setMaxAccess('read-write')
if mibBuilder.loadTexts:juniLicenseLineModuleIfLimitKey.setStatus(_A)
_JuniLicenseLineModuleIfLimitValue_Type=Integer32
_JuniLicenseLineModuleIfLimitValue_Object=MibScalar
juniLicenseLineModuleIfLimitValue=_JuniLicenseLineModuleIfLimitValue_Object((1,3,6,1,4,1,4874,2,2,76,1,2),_JuniLicenseLineModuleIfLimitValue_Type())
juniLicenseLineModuleIfLimitValue.setMaxAccess('read-only')
if mibBuilder.loadTexts:juniLicenseLineModuleIfLimitValue.setStatus(_A)
_JuniLicenseMIBConformance_ObjectIdentity=ObjectIdentity
juniLicenseMIBConformance=_JuniLicenseMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,76,2))
_JuniLicenseMIBCompliances_ObjectIdentity=ObjectIdentity
juniLicenseMIBCompliances=_JuniLicenseMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,76,2,1))
_JuniLicenseMIBGroups_ObjectIdentity=ObjectIdentity
juniLicenseMIBGroups=_JuniLicenseMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,76,2,2))
juniLicenseGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,76,2,2,1))
juniLicenseGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:juniLicenseGroup.setStatus(_A)
juniLicenseCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,76,2,1,1))
juniLicenseCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:juniLicenseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniLicenseMIB':juniLicenseMIB,'juniLicenseObjects':juniLicenseObjects,_D:juniLicenseLineModuleIfLimitKey,_E:juniLicenseLineModuleIfLimitValue,'juniLicenseMIBConformance':juniLicenseMIBConformance,'juniLicenseMIBCompliances':juniLicenseMIBCompliances,'juniLicenseCompliance':juniLicenseCompliance,'juniLicenseMIBGroups':juniLicenseMIBGroups,_F:juniLicenseGroup})