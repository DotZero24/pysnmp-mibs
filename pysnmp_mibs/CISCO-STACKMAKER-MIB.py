_J='ciscoStackMakerBasicGroup'
_I='csmStackIpAddress'
_H='csmClearStackTable'
_G='csmStackName'
_F='csmStackIndex'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='CISCO-STACKMAKER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ciscoStackMakerMIB=ModuleIdentity((1,3,6,1,4,1,9,9,59))
_CiscoStackMakerMIBObjects_ObjectIdentity=ObjectIdentity
ciscoStackMakerMIBObjects=_CiscoStackMakerMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,59,1))
_CiscoStackMakerConf_ObjectIdentity=ObjectIdentity
ciscoStackMakerConf=_CiscoStackMakerConf_ObjectIdentity((1,3,6,1,4,1,9,9,59,1,1))
class _CsmStackName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CsmStackName_Type.__name__=_D
_CsmStackName_Object=MibScalar
csmStackName=_CsmStackName_Object((1,3,6,1,4,1,9,9,59,1,1,1),_CsmStackName_Type())
csmStackName.setMaxAccess(_E)
if mibBuilder.loadTexts:csmStackName.setStatus(_A)
class _CsmClearStackTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clearTable',1),('noClearTable',2)))
_CsmClearStackTable_Type.__name__=_C
_CsmClearStackTable_Object=MibScalar
csmClearStackTable=_CsmClearStackTable_Object((1,3,6,1,4,1,9,9,59,1,1,2),_CsmClearStackTable_Type())
csmClearStackTable.setMaxAccess(_E)
if mibBuilder.loadTexts:csmClearStackTable.setStatus(_A)
_CsmStackTable_Object=MibTable
csmStackTable=_CsmStackTable_Object((1,3,6,1,4,1,9,9,59,1,1,3))
if mibBuilder.loadTexts:csmStackTable.setStatus(_A)
_CsmStackEntry_Object=MibTableRow
csmStackEntry=_CsmStackEntry_Object((1,3,6,1,4,1,9,9,59,1,1,3,1))
csmStackEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:csmStackEntry.setStatus(_A)
class _CsmStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CsmStackIndex_Type.__name__=_C
_CsmStackIndex_Object=MibTableColumn
csmStackIndex=_CsmStackIndex_Object((1,3,6,1,4,1,9,9,59,1,1,3,1,1),_CsmStackIndex_Type())
csmStackIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:csmStackIndex.setStatus(_A)
_CsmStackIpAddress_Type=IpAddress
_CsmStackIpAddress_Object=MibTableColumn
csmStackIpAddress=_CsmStackIpAddress_Object((1,3,6,1,4,1,9,9,59,1,1,3,1,2),_CsmStackIpAddress_Type())
csmStackIpAddress.setMaxAccess('read-create')
if mibBuilder.loadTexts:csmStackIpAddress.setStatus(_A)
_CiscoStackMakerMIBConformance_ObjectIdentity=ObjectIdentity
ciscoStackMakerMIBConformance=_CiscoStackMakerMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,59,3))
_CiscoStackMakerMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoStackMakerMIBCompliances=_CiscoStackMakerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,59,3,1))
_CiscoStackMakerMIBGroups_ObjectIdentity=ObjectIdentity
ciscoStackMakerMIBGroups=_CiscoStackMakerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,59,3,2))
ciscoStackMakerBasicGroup=ObjectGroup((1,3,6,1,4,1,9,9,59,3,2,1))
ciscoStackMakerBasicGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ciscoStackMakerBasicGroup.setStatus(_A)
ciscoStackMakerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,59,3,1,1))
ciscoStackMakerMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoStackMakerMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoStackMakerMIB':ciscoStackMakerMIB,'ciscoStackMakerMIBObjects':ciscoStackMakerMIBObjects,'ciscoStackMakerConf':ciscoStackMakerConf,_G:csmStackName,_H:csmClearStackTable,'csmStackTable':csmStackTable,'csmStackEntry':csmStackEntry,_F:csmStackIndex,_I:csmStackIpAddress,'ciscoStackMakerMIBConformance':ciscoStackMakerMIBConformance,'ciscoStackMakerMIBCompliances':ciscoStackMakerMIBCompliances,'ciscoStackMakerMIBCompliance':ciscoStackMakerMIBCompliance,'ciscoStackMakerMIBGroups':ciscoStackMakerMIBGroups,_J:ciscoStackMakerBasicGroup})