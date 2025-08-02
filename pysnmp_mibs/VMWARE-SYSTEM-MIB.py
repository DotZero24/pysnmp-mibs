_I='vmwSystemGroup'
_H='vmwProdPatch'
_G='vmwProdUpdate'
_F='vmwProdBuild'
_E='vmwProdVersion'
_D='vmwProdName'
_C='read-only'
_B='VMWARE-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwSystem,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwSystem')
vmwSystemMIB=ModuleIdentity((1,3,6,1,4,1,6876,1,10))
if mibBuilder.loadTexts:vmwSystemMIB.setRevisions(('2010-08-02 00:00','2008-01-12 00:00','2007-12-27 00:00'))
_VmwProdName_Type=DisplayString
_VmwProdName_Object=MibScalar
vmwProdName=_VmwProdName_Object((1,3,6,1,4,1,6876,1,1),_VmwProdName_Type())
vmwProdName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwProdName.setStatus(_A)
_VmwProdVersion_Type=DisplayString
_VmwProdVersion_Object=MibScalar
vmwProdVersion=_VmwProdVersion_Object((1,3,6,1,4,1,6876,1,2),_VmwProdVersion_Type())
vmwProdVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwProdVersion.setStatus(_A)
_VmwProdBuild_Type=DisplayString
_VmwProdBuild_Object=MibScalar
vmwProdBuild=_VmwProdBuild_Object((1,3,6,1,4,1,6876,1,4),_VmwProdBuild_Type())
vmwProdBuild.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwProdBuild.setStatus(_A)
_VmwProdUpdate_Type=DisplayString
_VmwProdUpdate_Object=MibScalar
vmwProdUpdate=_VmwProdUpdate_Object((1,3,6,1,4,1,6876,1,5),_VmwProdUpdate_Type())
vmwProdUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwProdUpdate.setStatus(_A)
_VmwProdPatch_Type=DisplayString
_VmwProdPatch_Object=MibScalar
vmwProdPatch=_VmwProdPatch_Object((1,3,6,1,4,1,6876,1,6),_VmwProdPatch_Type())
vmwProdPatch.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwProdPatch.setStatus(_A)
_VmwSystemMIBConformance_ObjectIdentity=ObjectIdentity
vmwSystemMIBConformance=_VmwSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,1,10,2))
_VmwSystemMIBCompliances_ObjectIdentity=ObjectIdentity
vmwSystemMIBCompliances=_VmwSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,1,10,2,1))
_VmwSysMIBGroups_ObjectIdentity=ObjectIdentity
vmwSysMIBGroups=_VmwSysMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,1,10,2,2))
vmwSystemGroup=ObjectGroup((1,3,6,1,4,1,6876,1,10,2,2,1))
vmwSystemGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:vmwSystemGroup.setStatus(_A)
vmwSysMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,1,10,2,1,2))
vmwSysMIBBasicCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:vmwSysMIBBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_D:vmwProdName,_E:vmwProdVersion,_F:vmwProdBuild,_G:vmwProdUpdate,_H:vmwProdPatch,'vmwSystemMIB':vmwSystemMIB,'vmwSystemMIBConformance':vmwSystemMIBConformance,'vmwSystemMIBCompliances':vmwSystemMIBCompliances,'vmwSysMIBBasicCompliance':vmwSysMIBBasicCompliance,'vmwSysMIBGroups':vmwSysMIBGroups,_I:vmwSystemGroup})