_J='hpicfActivateConfigGroup1'
_I='hpicfActivateConfigGroup'
_H='hpicfActivateOverrideConfigCheck'
_G='deprecated'
_F='hpicfActivateProvisionMode'
_E='hpicfActivateSoftwareUpdateMode'
_D='read-write'
_C='TruthValue'
_B='current'
_A='HPICF-ACTIVATE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
hpicfActivateMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,129))
if mibBuilder.loadTexts:hpicfActivateMIB.setRevisions(('2020-06-20 00:00','2016-05-03 00:00'))
_HpicfActivateObjects_ObjectIdentity=ObjectIdentity
hpicfActivateObjects=_HpicfActivateObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,129,1))
class _HpicfActivateSoftwareUpdateMode_Type(TruthValue):defaultValue=1
_HpicfActivateSoftwareUpdateMode_Type.__name__=_C
_HpicfActivateSoftwareUpdateMode_Object=MibScalar
hpicfActivateSoftwareUpdateMode=_HpicfActivateSoftwareUpdateMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,129,1,1),_HpicfActivateSoftwareUpdateMode_Type())
hpicfActivateSoftwareUpdateMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfActivateSoftwareUpdateMode.setStatus(_B)
class _HpicfActivateProvisionMode_Type(TruthValue):defaultValue=1
_HpicfActivateProvisionMode_Type.__name__=_C
_HpicfActivateProvisionMode_Object=MibScalar
hpicfActivateProvisionMode=_HpicfActivateProvisionMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,129,1,2),_HpicfActivateProvisionMode_Type())
hpicfActivateProvisionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfActivateProvisionMode.setStatus(_B)
class _HpicfActivateOverrideConfigCheck_Type(TruthValue):defaultValue=2
_HpicfActivateOverrideConfigCheck_Type.__name__=_C
_HpicfActivateOverrideConfigCheck_Object=MibScalar
hpicfActivateOverrideConfigCheck=_HpicfActivateOverrideConfigCheck_Object((1,3,6,1,4,1,11,2,14,11,5,1,129,1,3),_HpicfActivateOverrideConfigCheck_Type())
hpicfActivateOverrideConfigCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfActivateOverrideConfigCheck.setStatus(_B)
_HpicfActivateConformance_ObjectIdentity=ObjectIdentity
hpicfActivateConformance=_HpicfActivateConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,129,2))
_HpicfActivateMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfActivateMIBCompliances=_HpicfActivateMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,129,2,1))
_HpicfActivateMIBGroups_ObjectIdentity=ObjectIdentity
hpicfActivateMIBGroups=_HpicfActivateMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,129,2,2))
hpicfActivateConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,129,2,2,1))
hpicfActivateConfigGroup.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:hpicfActivateConfigGroup.setStatus(_G)
hpicfActivateConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,129,2,2,2))
hpicfActivateConfigGroup1.setObjects(*((_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:hpicfActivateConfigGroup1.setStatus(_B)
hpicfActivateMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,129,2,1,1))
hpicfActivateMIBCompliance.setObjects((_A,_I))
if mibBuilder.loadTexts:hpicfActivateMIBCompliance.setStatus(_G)
hpicfActivateMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,129,2,1,2))
hpicfActivateMIBCompliance1.setObjects((_A,_J))
if mibBuilder.loadTexts:hpicfActivateMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfActivateMIB':hpicfActivateMIB,'hpicfActivateObjects':hpicfActivateObjects,_E:hpicfActivateSoftwareUpdateMode,_F:hpicfActivateProvisionMode,_H:hpicfActivateOverrideConfigCheck,'hpicfActivateConformance':hpicfActivateConformance,'hpicfActivateMIBCompliances':hpicfActivateMIBCompliances,'hpicfActivateMIBCompliance':hpicfActivateMIBCompliance,'hpicfActivateMIBCompliance1':hpicfActivateMIBCompliance1,'hpicfActivateMIBGroups':hpicfActivateMIBGroups,_I:hpicfActivateConfigGroup,_J:hpicfActivateConfigGroup1})