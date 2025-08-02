_h='eoRelationStorageType'
_g='eoRelationStatus'
_f='eoRelationship'
_e='eoRelationID'
_d='eoMgmtDNSName'
_c='eoMgmtAddress'
_b='eoMgmtAddressType'
_a='eoMgmtMacAddress'
_Z='eoLldpPortNumber'
_Y='eoEthPortGrpIndex'
_X='eoEthPortIndex'
_W='eoPowerInterfaceType'
_V='eoPowerCategory'
_U='eoImportance'
_T='eoKeywords'
_S='eoAlternateKey'
_R='eoRoleDescription'
_Q='eoDomainName'
_P='eoRelationIndex'
_O='LldpPortNumberOrZero'
_N='PethPsePortGroupIndexOrZero'
_M='PethPsePortIndexOrZero'
_L='StorageType'
_K='energyObjectOptionalMIBTableGroup'
_J='energyObjectRelationTableGroup'
_I='energyObjectContextMIBTableGroup'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='read-create'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ENERGY-OBJECT-CONTEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
IANAEnergyRelationship,=mibBuilder.importSymbols('IANA-ENERGY-RELATION-MIB','IANAEnergyRelationship')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_L,'TextualConvention','TruthValue')
UUIDorZero,=mibBuilder.importSymbols('UUID-TC-MIB','UUIDorZero')
energyObjectContextMIB=ModuleIdentity((1,3,6,1,2,1,231))
if mibBuilder.loadTexts:energyObjectContextMIB.setRevisions(('2015-02-09 00:00',))
class PethPsePortIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class PethPsePortGroupIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class LldpPortNumberOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
class EnergyObjectKeywordList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_EnergyObjectContextMIBNotifs_ObjectIdentity=ObjectIdentity
energyObjectContextMIBNotifs=_EnergyObjectContextMIBNotifs_ObjectIdentity((1,3,6,1,2,1,231,0))
_EnergyObjectContextMIBObjects_ObjectIdentity=ObjectIdentity
energyObjectContextMIBObjects=_EnergyObjectContextMIBObjects_ObjectIdentity((1,3,6,1,2,1,231,1))
_EoTable_Object=MibTable
eoTable=_EoTable_Object((1,3,6,1,2,1,231,1,1))
if mibBuilder.loadTexts:eoTable.setStatus(_A)
_EoEntry_Object=MibTableRow
eoEntry=_EoEntry_Object((1,3,6,1,2,1,231,1,1,1))
eoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:eoEntry.setStatus(_A)
class _EoEthPortIndex_Type(PethPsePortIndexOrZero):defaultValue=0
_EoEthPortIndex_Type.__name__=_M
_EoEthPortIndex_Object=MibTableColumn
eoEthPortIndex=_EoEthPortIndex_Object((1,3,6,1,2,1,231,1,1,1,1),_EoEthPortIndex_Type())
eoEthPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eoEthPortIndex.setStatus(_A)
class _EoEthPortGrpIndex_Type(PethPsePortGroupIndexOrZero):defaultValue=0
_EoEthPortGrpIndex_Type.__name__=_N
_EoEthPortGrpIndex_Object=MibTableColumn
eoEthPortGrpIndex=_EoEthPortGrpIndex_Object((1,3,6,1,2,1,231,1,1,1,2),_EoEthPortGrpIndex_Type())
eoEthPortGrpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eoEthPortGrpIndex.setStatus(_A)
class _EoLldpPortNumber_Type(LldpPortNumberOrZero):defaultValue=0
_EoLldpPortNumber_Type.__name__=_O
_EoLldpPortNumber_Object=MibTableColumn
eoLldpPortNumber=_EoLldpPortNumber_Object((1,3,6,1,2,1,231,1,1,1,3),_EoLldpPortNumber_Type())
eoLldpPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eoLldpPortNumber.setStatus(_A)
_EoMgmtMacAddress_Type=MacAddress
_EoMgmtMacAddress_Object=MibTableColumn
eoMgmtMacAddress=_EoMgmtMacAddress_Object((1,3,6,1,2,1,231,1,1,1,4),_EoMgmtMacAddress_Type())
eoMgmtMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eoMgmtMacAddress.setStatus(_A)
_EoMgmtAddressType_Type=InetAddressType
_EoMgmtAddressType_Object=MibTableColumn
eoMgmtAddressType=_EoMgmtAddressType_Object((1,3,6,1,2,1,231,1,1,1,5),_EoMgmtAddressType_Type())
eoMgmtAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:eoMgmtAddressType.setStatus(_A)
_EoMgmtAddress_Type=InetAddress
_EoMgmtAddress_Object=MibTableColumn
eoMgmtAddress=_EoMgmtAddress_Object((1,3,6,1,2,1,231,1,1,1,6),_EoMgmtAddress_Type())
eoMgmtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eoMgmtAddress.setStatus(_A)
_EoMgmtDNSName_Type=OctetString
_EoMgmtDNSName_Object=MibTableColumn
eoMgmtDNSName=_EoMgmtDNSName_Object((1,3,6,1,2,1,231,1,1,1,7),_EoMgmtDNSName_Type())
eoMgmtDNSName.setMaxAccess(_C)
if mibBuilder.loadTexts:eoMgmtDNSName.setStatus(_A)
_EoDomainName_Type=SnmpAdminString
_EoDomainName_Object=MibTableColumn
eoDomainName=_EoDomainName_Object((1,3,6,1,2,1,231,1,1,1,8),_EoDomainName_Type())
eoDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:eoDomainName.setStatus(_A)
_EoRoleDescription_Type=SnmpAdminString
_EoRoleDescription_Object=MibTableColumn
eoRoleDescription=_EoRoleDescription_Object((1,3,6,1,2,1,231,1,1,1,9),_EoRoleDescription_Type())
eoRoleDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:eoRoleDescription.setStatus(_A)
_EoKeywords_Type=EnergyObjectKeywordList
_EoKeywords_Object=MibTableColumn
eoKeywords=_EoKeywords_Object((1,3,6,1,2,1,231,1,1,1,10),_EoKeywords_Type())
eoKeywords.setMaxAccess(_E)
if mibBuilder.loadTexts:eoKeywords.setStatus(_A)
class _EoImportance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EoImportance_Type.__name__=_D
_EoImportance_Object=MibTableColumn
eoImportance=_EoImportance_Object((1,3,6,1,2,1,231,1,1,1,11),_EoImportance_Type())
eoImportance.setMaxAccess(_E)
if mibBuilder.loadTexts:eoImportance.setStatus(_A)
class _EoPowerCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('consumer',0),('producer',1),('meter',2),('distributor',3),('store',4)))
_EoPowerCategory_Type.__name__=_D
_EoPowerCategory_Object=MibTableColumn
eoPowerCategory=_EoPowerCategory_Object((1,3,6,1,2,1,231,1,1,1,12),_EoPowerCategory_Type())
eoPowerCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:eoPowerCategory.setStatus(_A)
_EoAlternateKey_Type=SnmpAdminString
_EoAlternateKey_Object=MibTableColumn
eoAlternateKey=_EoAlternateKey_Object((1,3,6,1,2,1,231,1,1,1,13),_EoAlternateKey_Type())
eoAlternateKey.setMaxAccess(_E)
if mibBuilder.loadTexts:eoAlternateKey.setStatus(_A)
class _EoPowerInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inlet',0),('outlet',1),('both',2)))
_EoPowerInterfaceType_Type.__name__=_D
_EoPowerInterfaceType_Object=MibTableColumn
eoPowerInterfaceType=_EoPowerInterfaceType_Object((1,3,6,1,2,1,231,1,1,1,14),_EoPowerInterfaceType_Type())
eoPowerInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:eoPowerInterfaceType.setStatus(_A)
_EoRelationTable_Object=MibTable
eoRelationTable=_EoRelationTable_Object((1,3,6,1,2,1,231,1,2))
if mibBuilder.loadTexts:eoRelationTable.setStatus(_A)
_EoRelationEntry_Object=MibTableRow
eoRelationEntry=_EoRelationEntry_Object((1,3,6,1,2,1,231,1,2,1))
eoRelationEntry.setIndexNames((0,_G,_H),(0,_B,_P))
if mibBuilder.loadTexts:eoRelationEntry.setStatus(_A)
class _EoRelationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EoRelationIndex_Type.__name__=_D
_EoRelationIndex_Object=MibTableColumn
eoRelationIndex=_EoRelationIndex_Object((1,3,6,1,2,1,231,1,2,1,1),_EoRelationIndex_Type())
eoRelationIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eoRelationIndex.setStatus(_A)
_EoRelationID_Type=UUIDorZero
_EoRelationID_Object=MibTableColumn
eoRelationID=_EoRelationID_Object((1,3,6,1,2,1,231,1,2,1,2),_EoRelationID_Type())
eoRelationID.setMaxAccess(_F)
if mibBuilder.loadTexts:eoRelationID.setStatus(_A)
_EoRelationship_Type=IANAEnergyRelationship
_EoRelationship_Object=MibTableColumn
eoRelationship=_EoRelationship_Object((1,3,6,1,2,1,231,1,2,1,3),_EoRelationship_Type())
eoRelationship.setMaxAccess(_F)
if mibBuilder.loadTexts:eoRelationship.setStatus(_A)
_EoRelationStatus_Type=RowStatus
_EoRelationStatus_Object=MibTableColumn
eoRelationStatus=_EoRelationStatus_Object((1,3,6,1,2,1,231,1,2,1,4),_EoRelationStatus_Type())
eoRelationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:eoRelationStatus.setStatus(_A)
class _EoRelationStorageType_Type(StorageType):defaultValue=3
_EoRelationStorageType_Type.__name__=_L
_EoRelationStorageType_Object=MibTableColumn
eoRelationStorageType=_EoRelationStorageType_Object((1,3,6,1,2,1,231,1,2,1,5),_EoRelationStorageType_Type())
eoRelationStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:eoRelationStorageType.setStatus(_A)
_EnergyObjectContextMIBConform_ObjectIdentity=ObjectIdentity
energyObjectContextMIBConform=_EnergyObjectContextMIBConform_ObjectIdentity((1,3,6,1,2,1,231,2))
_EnergyObjectContextMIBCompliances_ObjectIdentity=ObjectIdentity
energyObjectContextMIBCompliances=_EnergyObjectContextMIBCompliances_ObjectIdentity((1,3,6,1,2,1,231,2,1))
_EnergyObjectContextMIBGroups_ObjectIdentity=ObjectIdentity
energyObjectContextMIBGroups=_EnergyObjectContextMIBGroups_ObjectIdentity((1,3,6,1,2,1,231,2,2))
energyObjectContextMIBTableGroup=ObjectGroup((1,3,6,1,2,1,231,2,2,1))
energyObjectContextMIBTableGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:energyObjectContextMIBTableGroup.setStatus(_A)
energyObjectOptionalMIBTableGroup=ObjectGroup((1,3,6,1,2,1,231,2,2,2))
energyObjectOptionalMIBTableGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:energyObjectOptionalMIBTableGroup.setStatus(_A)
energyObjectRelationTableGroup=ObjectGroup((1,3,6,1,2,1,231,2,2,3))
energyObjectRelationTableGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:energyObjectRelationTableGroup.setStatus(_A)
energyObjectContextMIBFullCompliance=ModuleCompliance((1,3,6,1,2,1,231,2,1,1))
energyObjectContextMIBFullCompliance.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:energyObjectContextMIBFullCompliance.setStatus(_A)
energyObjectContextMIBReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,231,2,1,2))
energyObjectContextMIBReadOnlyCompliance.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:energyObjectContextMIBReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:PethPsePortIndexOrZero,_N:PethPsePortGroupIndexOrZero,_O:LldpPortNumberOrZero,'EnergyObjectKeywordList':EnergyObjectKeywordList,'energyObjectContextMIB':energyObjectContextMIB,'energyObjectContextMIBNotifs':energyObjectContextMIBNotifs,'energyObjectContextMIBObjects':energyObjectContextMIBObjects,'eoTable':eoTable,'eoEntry':eoEntry,_X:eoEthPortIndex,_Y:eoEthPortGrpIndex,_Z:eoLldpPortNumber,_a:eoMgmtMacAddress,_b:eoMgmtAddressType,_c:eoMgmtAddress,_d:eoMgmtDNSName,_Q:eoDomainName,_R:eoRoleDescription,_T:eoKeywords,_U:eoImportance,_V:eoPowerCategory,_S:eoAlternateKey,_W:eoPowerInterfaceType,'eoRelationTable':eoRelationTable,'eoRelationEntry':eoRelationEntry,_P:eoRelationIndex,_e:eoRelationID,_f:eoRelationship,_g:eoRelationStatus,_h:eoRelationStorageType,'energyObjectContextMIBConform':energyObjectContextMIBConform,'energyObjectContextMIBCompliances':energyObjectContextMIBCompliances,'energyObjectContextMIBFullCompliance':energyObjectContextMIBFullCompliance,'energyObjectContextMIBReadOnlyCompliance':energyObjectContextMIBReadOnlyCompliance,'energyObjectContextMIBGroups':energyObjectContextMIBGroups,_I:energyObjectContextMIBTableGroup,_K:energyObjectOptionalMIBTableGroup,_J:energyObjectRelationTableGroup})