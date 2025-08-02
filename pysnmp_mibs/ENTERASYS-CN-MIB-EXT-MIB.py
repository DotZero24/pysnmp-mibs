_f='etsysCnMibExtCpGroup'
_e='etsysCnMibExtQpGroup'
_d='etsysCnMibExtGlobalGroup'
_c='etsysCnMibExtSysGroup'
_b='etsysCnMibExtQpTypeGroup'
_a='etsysCnMibExtCpQpIndex'
_Z='etsysCnMibExtCpQpTypeId'
_Y='etsysCnMibExtQpRowStatus'
_X='etsysCnMibExtQpMinHeaderOctets'
_W='etsysCnMibExtQpMinSampleBase'
_V='etsysCnMibExtQpFeedbackWeight'
_U='etsysCnMibExtQpSizeSetPoint'
_T='etsysCnMibExtGlobalActivePriVals'
_S='etsysCnMibExtMaxCompActivePriVals'
_R='etsysCnMibExtQptSupport'
_Q='etsysCnMibExtQptMaxQpEntries'
_P='etsysCnMibExtQptDesc'
_O='etsysCnMibExtGlobalEntry'
_N='etsysCnMibExtCpEntry'
_M='etsysCnMibExtQpIndex'
_L='etsysCnMibExtQpTypeId'
_K='etsysCnMibExtQpComponentId'
_J='etsysCnMibExtQptIdentifier'
_I='Integer32'
_H='SnmpAdminString'
_G='octets'
_F='not-accessible'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='ENTERASYS-CN-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ieee8021CnCpEntry,ieee8021CnGlobalEntry=mibBuilder.importSymbols('IEEE8021-CN-MIB','ieee8021CnCpEntry','ieee8021CnGlobalEntry')
IEEE8021PbbComponentIdentifier,=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PbbComponentIdentifier')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
etsysCnMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,95))
if mibBuilder.loadTexts:etsysCnMibExtMIB.setRevisions(('2012-07-20 12:21',))
_EtsysCnMibExtObjects_ObjectIdentity=ObjectIdentity
etsysCnMibExtObjects=_EtsysCnMibExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,95,1))
_EtsysCnMibExtSysBranch_ObjectIdentity=ObjectIdentity
etsysCnMibExtSysBranch=_EtsysCnMibExtSysBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,95,1,1))
_EtsysCnMibExtQpTypeTable_Object=MibTable
etsysCnMibExtQpTypeTable=_EtsysCnMibExtQpTypeTable_Object((1,3,6,1,4,1,5624,1,2,95,1,1,1))
if mibBuilder.loadTexts:etsysCnMibExtQpTypeTable.setStatus(_A)
_EtsysCnMibExtQpTypeEntry_Object=MibTableRow
etsysCnMibExtQpTypeEntry=_EtsysCnMibExtQpTypeEntry_Object((1,3,6,1,4,1,5624,1,2,95,1,1,1,1))
etsysCnMibExtQpTypeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:etsysCnMibExtQpTypeEntry.setStatus(_A)
_EtsysCnMibExtQptIdentifier_Type=Unsigned32
_EtsysCnMibExtQptIdentifier_Object=MibTableColumn
etsysCnMibExtQptIdentifier=_EtsysCnMibExtQptIdentifier_Object((1,3,6,1,4,1,5624,1,2,95,1,1,1,1,1),_EtsysCnMibExtQptIdentifier_Type())
etsysCnMibExtQptIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysCnMibExtQptIdentifier.setStatus(_A)
class _EtsysCnMibExtQptDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_EtsysCnMibExtQptDesc_Type.__name__=_H
_EtsysCnMibExtQptDesc_Object=MibTableColumn
etsysCnMibExtQptDesc=_EtsysCnMibExtQptDesc_Object((1,3,6,1,4,1,5624,1,2,95,1,1,1,1,2),_EtsysCnMibExtQptDesc_Type())
etsysCnMibExtQptDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysCnMibExtQptDesc.setStatus(_A)
_EtsysCnMibExtQptMaxQpEntries_Type=Unsigned32
_EtsysCnMibExtQptMaxQpEntries_Object=MibTableColumn
etsysCnMibExtQptMaxQpEntries=_EtsysCnMibExtQptMaxQpEntries_Object((1,3,6,1,4,1,5624,1,2,95,1,1,1,1,3),_EtsysCnMibExtQptMaxQpEntries_Type())
etsysCnMibExtQptMaxQpEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysCnMibExtQptMaxQpEntries.setStatus(_A)
class _EtsysCnMibExtQptSupport_Type(Bits):namedValues=NamedValues(*(('supportSizeSetPoint',0),('supportFeedbackWeight',1),('supportMinSampleBase',2),('supportMinHeaderOctets',3)))
_EtsysCnMibExtQptSupport_Type.__name__='Bits'
_EtsysCnMibExtQptSupport_Object=MibTableColumn
etsysCnMibExtQptSupport=_EtsysCnMibExtQptSupport_Object((1,3,6,1,4,1,5624,1,2,95,1,1,1,1,4),_EtsysCnMibExtQptSupport_Type())
etsysCnMibExtQptSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysCnMibExtQptSupport.setStatus(_A)
_EtsysCnMibExtMaxCompActivePriVals_Type=Unsigned32
_EtsysCnMibExtMaxCompActivePriVals_Object=MibScalar
etsysCnMibExtMaxCompActivePriVals=_EtsysCnMibExtMaxCompActivePriVals_Object((1,3,6,1,4,1,5624,1,2,95,1,1,2),_EtsysCnMibExtMaxCompActivePriVals_Type())
etsysCnMibExtMaxCompActivePriVals.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysCnMibExtMaxCompActivePriVals.setStatus(_A)
_EtsysCnMibExtCompBranch_ObjectIdentity=ObjectIdentity
etsysCnMibExtCompBranch=_EtsysCnMibExtCompBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,95,1,2))
_EtsysCnMibExtQpTable_Object=MibTable
etsysCnMibExtQpTable=_EtsysCnMibExtQpTable_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1))
if mibBuilder.loadTexts:etsysCnMibExtQpTable.setStatus(_A)
_EtsysCnMibExtQpEntry_Object=MibTableRow
etsysCnMibExtQpEntry=_EtsysCnMibExtQpEntry_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1))
etsysCnMibExtQpEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:etsysCnMibExtQpEntry.setStatus(_A)
_EtsysCnMibExtQpComponentId_Type=IEEE8021PbbComponentIdentifier
_EtsysCnMibExtQpComponentId_Object=MibTableColumn
etsysCnMibExtQpComponentId=_EtsysCnMibExtQpComponentId_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,1),_EtsysCnMibExtQpComponentId_Type())
etsysCnMibExtQpComponentId.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysCnMibExtQpComponentId.setStatus(_A)
_EtsysCnMibExtQpTypeId_Type=Unsigned32
_EtsysCnMibExtQpTypeId_Object=MibTableColumn
etsysCnMibExtQpTypeId=_EtsysCnMibExtQpTypeId_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,2),_EtsysCnMibExtQpTypeId_Type())
etsysCnMibExtQpTypeId.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysCnMibExtQpTypeId.setStatus(_A)
_EtsysCnMibExtQpIndex_Type=Unsigned32
_EtsysCnMibExtQpIndex_Object=MibTableColumn
etsysCnMibExtQpIndex=_EtsysCnMibExtQpIndex_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,3),_EtsysCnMibExtQpIndex_Type())
etsysCnMibExtQpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysCnMibExtQpIndex.setStatus(_A)
class _EtsysCnMibExtQpSizeSetPoint_Type(Unsigned32):defaultValue=26000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_EtsysCnMibExtQpSizeSetPoint_Type.__name__=_E
_EtsysCnMibExtQpSizeSetPoint_Object=MibTableColumn
etsysCnMibExtQpSizeSetPoint=_EtsysCnMibExtQpSizeSetPoint_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,4),_EtsysCnMibExtQpSizeSetPoint_Type())
etsysCnMibExtQpSizeSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCnMibExtQpSizeSetPoint.setStatus(_A)
if mibBuilder.loadTexts:etsysCnMibExtQpSizeSetPoint.setUnits(_G)
class _EtsysCnMibExtQpFeedbackWeight_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,10))
_EtsysCnMibExtQpFeedbackWeight_Type.__name__=_I
_EtsysCnMibExtQpFeedbackWeight_Object=MibTableColumn
etsysCnMibExtQpFeedbackWeight=_EtsysCnMibExtQpFeedbackWeight_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,5),_EtsysCnMibExtQpFeedbackWeight_Type())
etsysCnMibExtQpFeedbackWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCnMibExtQpFeedbackWeight.setStatus(_A)
class _EtsysCnMibExtQpMinSampleBase_Type(Unsigned32):defaultValue=150000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,4294967295))
_EtsysCnMibExtQpMinSampleBase_Type.__name__=_E
_EtsysCnMibExtQpMinSampleBase_Object=MibTableColumn
etsysCnMibExtQpMinSampleBase=_EtsysCnMibExtQpMinSampleBase_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,6),_EtsysCnMibExtQpMinSampleBase_Type())
etsysCnMibExtQpMinSampleBase.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCnMibExtQpMinSampleBase.setStatus(_A)
if mibBuilder.loadTexts:etsysCnMibExtQpMinSampleBase.setUnits(_G)
class _EtsysCnMibExtQpMinHeaderOctets_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_EtsysCnMibExtQpMinHeaderOctets_Type.__name__=_E
_EtsysCnMibExtQpMinHeaderOctets_Object=MibTableColumn
etsysCnMibExtQpMinHeaderOctets=_EtsysCnMibExtQpMinHeaderOctets_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,7),_EtsysCnMibExtQpMinHeaderOctets_Type())
etsysCnMibExtQpMinHeaderOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCnMibExtQpMinHeaderOctets.setStatus(_A)
if mibBuilder.loadTexts:etsysCnMibExtQpMinHeaderOctets.setUnits(_G)
_EtsysCnMibExtQpRowStatus_Type=RowStatus
_EtsysCnMibExtQpRowStatus_Object=MibTableColumn
etsysCnMibExtQpRowStatus=_EtsysCnMibExtQpRowStatus_Object((1,3,6,1,4,1,5624,1,2,95,1,2,1,1,8),_EtsysCnMibExtQpRowStatus_Type())
etsysCnMibExtQpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCnMibExtQpRowStatus.setStatus(_A)
_EtsysCnMibExtCpTable_Object=MibTable
etsysCnMibExtCpTable=_EtsysCnMibExtCpTable_Object((1,3,6,1,4,1,5624,1,2,95,1,2,2))
if mibBuilder.loadTexts:etsysCnMibExtCpTable.setStatus(_A)
_EtsysCnMibExtCpEntry_Object=MibTableRow
etsysCnMibExtCpEntry=_EtsysCnMibExtCpEntry_Object((1,3,6,1,4,1,5624,1,2,95,1,2,2,1))
if mibBuilder.loadTexts:etsysCnMibExtCpEntry.setStatus(_A)
_EtsysCnMibExtCpQpTypeId_Type=Unsigned32
_EtsysCnMibExtCpQpTypeId_Object=MibTableColumn
etsysCnMibExtCpQpTypeId=_EtsysCnMibExtCpQpTypeId_Object((1,3,6,1,4,1,5624,1,2,95,1,2,2,1,1),_EtsysCnMibExtCpQpTypeId_Type())
etsysCnMibExtCpQpTypeId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysCnMibExtCpQpTypeId.setStatus(_A)
_EtsysCnMibExtCpQpIndex_Type=Unsigned32
_EtsysCnMibExtCpQpIndex_Object=MibTableColumn
etsysCnMibExtCpQpIndex=_EtsysCnMibExtCpQpIndex_Object((1,3,6,1,4,1,5624,1,2,95,1,2,2,1,2),_EtsysCnMibExtCpQpIndex_Type())
etsysCnMibExtCpQpIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysCnMibExtCpQpIndex.setStatus(_A)
_EtsysCnMibExtGlobalTable_Object=MibTable
etsysCnMibExtGlobalTable=_EtsysCnMibExtGlobalTable_Object((1,3,6,1,4,1,5624,1,2,95,1,2,3))
if mibBuilder.loadTexts:etsysCnMibExtGlobalTable.setStatus(_A)
_EtsysCnMibExtGlobalEntry_Object=MibTableRow
etsysCnMibExtGlobalEntry=_EtsysCnMibExtGlobalEntry_Object((1,3,6,1,4,1,5624,1,2,95,1,2,3,1))
if mibBuilder.loadTexts:etsysCnMibExtGlobalEntry.setStatus(_A)
_EtsysCnMibExtGlobalActivePriVals_Type=Unsigned32
_EtsysCnMibExtGlobalActivePriVals_Object=MibTableColumn
etsysCnMibExtGlobalActivePriVals=_EtsysCnMibExtGlobalActivePriVals_Object((1,3,6,1,4,1,5624,1,2,95,1,2,3,1,1),_EtsysCnMibExtGlobalActivePriVals_Type())
etsysCnMibExtGlobalActivePriVals.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysCnMibExtGlobalActivePriVals.setStatus(_A)
_EtsysCnMibExtConformance_ObjectIdentity=ObjectIdentity
etsysCnMibExtConformance=_EtsysCnMibExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,95,2))
_EtsysCnMibExtGroups_ObjectIdentity=ObjectIdentity
etsysCnMibExtGroups=_EtsysCnMibExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,95,2,1))
_EtsysCnMibExtCompliances_ObjectIdentity=ObjectIdentity
etsysCnMibExtCompliances=_EtsysCnMibExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,95,2,2))
ieee8021CnCpEntry.registerAugmentions((_B,_N))
etsysCnMibExtCpEntry.setIndexNames(*ieee8021CnCpEntry.getIndexNames())
ieee8021CnGlobalEntry.registerAugmentions((_B,_O))
etsysCnMibExtGlobalEntry.setIndexNames(*ieee8021CnGlobalEntry.getIndexNames())
etsysCnMibExtQpTypeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,95,2,1,1))
etsysCnMibExtQpTypeGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:etsysCnMibExtQpTypeGroup.setStatus(_A)
etsysCnMibExtSysGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,95,2,1,2))
etsysCnMibExtSysGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:etsysCnMibExtSysGroup.setStatus(_A)
etsysCnMibExtGlobalGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,95,2,1,3))
etsysCnMibExtGlobalGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:etsysCnMibExtGlobalGroup.setStatus(_A)
etsysCnMibExtQpGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,95,2,1,4))
etsysCnMibExtQpGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:etsysCnMibExtQpGroup.setStatus(_A)
etsysCnMibExtCpGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,95,2,1,5))
etsysCnMibExtCpGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:etsysCnMibExtCpGroup.setStatus(_A)
etsysCnMibExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,95,2,2,1))
etsysCnMibExtCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:etsysCnMibExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysCnMibExtMIB':etsysCnMibExtMIB,'etsysCnMibExtObjects':etsysCnMibExtObjects,'etsysCnMibExtSysBranch':etsysCnMibExtSysBranch,'etsysCnMibExtQpTypeTable':etsysCnMibExtQpTypeTable,'etsysCnMibExtQpTypeEntry':etsysCnMibExtQpTypeEntry,_J:etsysCnMibExtQptIdentifier,_P:etsysCnMibExtQptDesc,_Q:etsysCnMibExtQptMaxQpEntries,_R:etsysCnMibExtQptSupport,_S:etsysCnMibExtMaxCompActivePriVals,'etsysCnMibExtCompBranch':etsysCnMibExtCompBranch,'etsysCnMibExtQpTable':etsysCnMibExtQpTable,'etsysCnMibExtQpEntry':etsysCnMibExtQpEntry,_K:etsysCnMibExtQpComponentId,_L:etsysCnMibExtQpTypeId,_M:etsysCnMibExtQpIndex,_U:etsysCnMibExtQpSizeSetPoint,_V:etsysCnMibExtQpFeedbackWeight,_W:etsysCnMibExtQpMinSampleBase,_X:etsysCnMibExtQpMinHeaderOctets,_Y:etsysCnMibExtQpRowStatus,'etsysCnMibExtCpTable':etsysCnMibExtCpTable,_N:etsysCnMibExtCpEntry,_Z:etsysCnMibExtCpQpTypeId,_a:etsysCnMibExtCpQpIndex,'etsysCnMibExtGlobalTable':etsysCnMibExtGlobalTable,_O:etsysCnMibExtGlobalEntry,_T:etsysCnMibExtGlobalActivePriVals,'etsysCnMibExtConformance':etsysCnMibExtConformance,'etsysCnMibExtGroups':etsysCnMibExtGroups,_b:etsysCnMibExtQpTypeGroup,_c:etsysCnMibExtSysGroup,_d:etsysCnMibExtGlobalGroup,_e:etsysCnMibExtQpGroup,_f:etsysCnMibExtCpGroup,'etsysCnMibExtCompliances':etsysCnMibExtCompliances,'etsysCnMibExtCompliance':etsysCnMibExtCompliance})