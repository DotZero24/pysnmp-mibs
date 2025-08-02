_K='docsTestGroup'
_J='docsTestEnable'
_I='docsTestData'
_H='docsTestType'
_G='docsTestStatus'
_F='docsTestCapability'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='DOCS-TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
docsTestMIB=ModuleIdentity((1,3,6,1,4,1,4491,2,1,12))
_CableLabs_ObjectIdentity=ObjectIdentity
cableLabs=_CableLabs_ObjectIdentity((1,3,6,1,4,1,4491))
_ClabFunction_ObjectIdentity=ObjectIdentity
clabFunction=_ClabFunction_ObjectIdentity((1,3,6,1,4,1,4491,1))
_ClabFuncMib2_ObjectIdentity=ObjectIdentity
clabFuncMib2=_ClabFuncMib2_ObjectIdentity((1,3,6,1,4,1,4491,1,1))
_ClabFuncProprietary_ObjectIdentity=ObjectIdentity
clabFuncProprietary=_ClabFuncProprietary_ObjectIdentity((1,3,6,1,4,1,4491,1,2))
_ClabProject_ObjectIdentity=ObjectIdentity
clabProject=_ClabProject_ObjectIdentity((1,3,6,1,4,1,4491,2))
_ClabProjDocsis_ObjectIdentity=ObjectIdentity
clabProjDocsis=_ClabProjDocsis_ObjectIdentity((1,3,6,1,4,1,4491,2,1))
_DocsTestMibObjects_ObjectIdentity=ObjectIdentity
docsTestMibObjects=_DocsTestMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,12,1))
_DocsTestBaseObjects_ObjectIdentity=ObjectIdentity
docsTestBaseObjects=_DocsTestBaseObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,12,1,1))
_DocsTestCapability_Type=OctetString
_DocsTestCapability_Object=MibScalar
docsTestCapability=_DocsTestCapability_Object((1,3,6,1,4,1,4491,2,1,12,1,1,1),_DocsTestCapability_Type())
docsTestCapability.setMaxAccess(_E)
if mibBuilder.loadTexts:docsTestCapability.setStatus(_A)
_DocsTestStatus_Type=OctetString
_DocsTestStatus_Object=MibScalar
docsTestStatus=_DocsTestStatus_Object((1,3,6,1,4,1,4491,2,1,12,1,1,2),_DocsTestStatus_Type())
docsTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:docsTestStatus.setStatus(_A)
_DocsTestSetupObjects_ObjectIdentity=ObjectIdentity
docsTestSetupObjects=_DocsTestSetupObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,12,1,2))
class _DocsTestType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_DocsTestType_Type.__name__=_D
_DocsTestType_Object=MibScalar
docsTestType=_DocsTestType_Object((1,3,6,1,4,1,4491,2,1,12,1,2,1),_DocsTestType_Type())
docsTestType.setMaxAccess(_C)
if mibBuilder.loadTexts:docsTestType.setStatus(_A)
_DocsTestData_Type=OctetString
_DocsTestData_Object=MibScalar
docsTestData=_DocsTestData_Object((1,3,6,1,4,1,4491,2,1,12,1,2,2),_DocsTestData_Type())
docsTestData.setMaxAccess(_C)
if mibBuilder.loadTexts:docsTestData.setStatus(_A)
_DocsTestEnable_Type=TruthValue
_DocsTestEnable_Object=MibScalar
docsTestEnable=_DocsTestEnable_Object((1,3,6,1,4,1,4491,2,1,12,1,2,3),_DocsTestEnable_Type())
docsTestEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:docsTestEnable.setStatus(_A)
_DocsTestConformance_ObjectIdentity=ObjectIdentity
docsTestConformance=_DocsTestConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,1,12,2))
_DocsTestCompliances_ObjectIdentity=ObjectIdentity
docsTestCompliances=_DocsTestCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,1,12,2,1))
_DocsTestGroups_ObjectIdentity=ObjectIdentity
docsTestGroups=_DocsTestGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,1,12,2,2))
_ClabProjPacketCable_ObjectIdentity=ObjectIdentity
clabProjPacketCable=_ClabProjPacketCable_ObjectIdentity((1,3,6,1,4,1,4491,2,2))
_ClabProjOpenCable_ObjectIdentity=ObjectIdentity
clabProjOpenCable=_ClabProjOpenCable_ObjectIdentity((1,3,6,1,4,1,4491,2,3))
_ClabProjCableHome_ObjectIdentity=ObjectIdentity
clabProjCableHome=_ClabProjCableHome_ObjectIdentity((1,3,6,1,4,1,4491,2,4))
docsTestGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,12,2,2,1))
docsTestGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:docsTestGroup.setStatus(_A)
docsTestBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,12,2,1,1))
docsTestBasicCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:docsTestBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cableLabs':cableLabs,'clabFunction':clabFunction,'clabFuncMib2':clabFuncMib2,'clabFuncProprietary':clabFuncProprietary,'clabProject':clabProject,'clabProjDocsis':clabProjDocsis,'docsTestMIB':docsTestMIB,'docsTestMibObjects':docsTestMibObjects,'docsTestBaseObjects':docsTestBaseObjects,_F:docsTestCapability,_G:docsTestStatus,'docsTestSetupObjects':docsTestSetupObjects,_H:docsTestType,_I:docsTestData,_J:docsTestEnable,'docsTestConformance':docsTestConformance,'docsTestCompliances':docsTestCompliances,'docsTestBasicCompliance':docsTestBasicCompliance,'docsTestGroups':docsTestGroups,_K:docsTestGroup,'clabProjPacketCable':clabProjPacketCable,'clabProjOpenCable':clabProjOpenCable,'clabProjCableHome':clabProjCableHome})