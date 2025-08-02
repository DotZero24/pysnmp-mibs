_R='etsysAppSignPatternGroup'
_Q='etsysAppSignDisplayNameGroup'
_P='etsysAppSignGroup'
_O='etsysAppSignPatternRowStatus'
_N='etsysAppSignPattern'
_M='etsysAppSignDisplayNameRowStatus'
_L='etsysAppSignDisplayName'
_K='etsysAppSignGroupName'
_J='etsysAppSignPatternIndex'
_I='DisplayString'
_H='SnmpAdminString'
_G='etsysAppSignDisplayId'
_F='not-accessible'
_E='etsysAppSignGroupId'
_D='read-create'
_C='Unsigned32'
_B='ENTERASYS-APPLICATION-SIGNATURE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
etsysApplicationSignatureMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,107))
if mibBuilder.loadTexts:etsysApplicationSignatureMIB.setRevisions(('2016-05-11 12:56',))
_EtsysApplicationSignatureMIBObjects_ObjectIdentity=ObjectIdentity
etsysApplicationSignatureMIBObjects=_EtsysApplicationSignatureMIBObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,107,1))
_EtsysAppSignGroupTable_Object=MibTable
etsysAppSignGroupTable=_EtsysAppSignGroupTable_Object((1,3,6,1,4,1,5624,1,2,107,1,1))
if mibBuilder.loadTexts:etsysAppSignGroupTable.setStatus(_A)
_EtsysAppSignGroupEntry_Object=MibTableRow
etsysAppSignGroupEntry=_EtsysAppSignGroupEntry_Object((1,3,6,1,4,1,5624,1,2,107,1,1,1))
etsysAppSignGroupEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:etsysAppSignGroupEntry.setStatus(_A)
class _EtsysAppSignGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysAppSignGroupId_Type.__name__=_C
_EtsysAppSignGroupId_Object=MibTableColumn
etsysAppSignGroupId=_EtsysAppSignGroupId_Object((1,3,6,1,4,1,5624,1,2,107,1,1,1,1),_EtsysAppSignGroupId_Type())
etsysAppSignGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysAppSignGroupId.setStatus(_A)
_EtsysAppSignGroupName_Type=SnmpAdminString
_EtsysAppSignGroupName_Object=MibTableColumn
etsysAppSignGroupName=_EtsysAppSignGroupName_Object((1,3,6,1,4,1,5624,1,2,107,1,1,1,2),_EtsysAppSignGroupName_Type())
etsysAppSignGroupName.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysAppSignGroupName.setStatus(_A)
_EtsysAppSignDisplayNameTable_Object=MibTable
etsysAppSignDisplayNameTable=_EtsysAppSignDisplayNameTable_Object((1,3,6,1,4,1,5624,1,2,107,1,2))
if mibBuilder.loadTexts:etsysAppSignDisplayNameTable.setStatus(_A)
_EtsysAppSignDisplayNameEntry_Object=MibTableRow
etsysAppSignDisplayNameEntry=_EtsysAppSignDisplayNameEntry_Object((1,3,6,1,4,1,5624,1,2,107,1,2,1))
etsysAppSignDisplayNameEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:etsysAppSignDisplayNameEntry.setStatus(_A)
class _EtsysAppSignDisplayId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5999))
_EtsysAppSignDisplayId_Type.__name__=_C
_EtsysAppSignDisplayId_Object=MibTableColumn
etsysAppSignDisplayId=_EtsysAppSignDisplayId_Object((1,3,6,1,4,1,5624,1,2,107,1,2,1,1),_EtsysAppSignDisplayId_Type())
etsysAppSignDisplayId.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysAppSignDisplayId.setStatus(_A)
class _EtsysAppSignDisplayName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysAppSignDisplayName_Type.__name__=_H
_EtsysAppSignDisplayName_Object=MibTableColumn
etsysAppSignDisplayName=_EtsysAppSignDisplayName_Object((1,3,6,1,4,1,5624,1,2,107,1,2,1,2),_EtsysAppSignDisplayName_Type())
etsysAppSignDisplayName.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAppSignDisplayName.setStatus(_A)
_EtsysAppSignDisplayNameRowStatus_Type=RowStatus
_EtsysAppSignDisplayNameRowStatus_Object=MibTableColumn
etsysAppSignDisplayNameRowStatus=_EtsysAppSignDisplayNameRowStatus_Object((1,3,6,1,4,1,5624,1,2,107,1,2,1,3),_EtsysAppSignDisplayNameRowStatus_Type())
etsysAppSignDisplayNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAppSignDisplayNameRowStatus.setStatus(_A)
_EtsysAppSignPatternTable_Object=MibTable
etsysAppSignPatternTable=_EtsysAppSignPatternTable_Object((1,3,6,1,4,1,5624,1,2,107,1,3))
if mibBuilder.loadTexts:etsysAppSignPatternTable.setStatus(_A)
_EtsysAppSignPatternEntry_Object=MibTableRow
etsysAppSignPatternEntry=_EtsysAppSignPatternEntry_Object((1,3,6,1,4,1,5624,1,2,107,1,3,1))
etsysAppSignPatternEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:etsysAppSignPatternEntry.setStatus(_A)
class _EtsysAppSignPatternIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000000,2000000))
_EtsysAppSignPatternIndex_Type.__name__=_C
_EtsysAppSignPatternIndex_Object=MibTableColumn
etsysAppSignPatternIndex=_EtsysAppSignPatternIndex_Object((1,3,6,1,4,1,5624,1,2,107,1,3,1,1),_EtsysAppSignPatternIndex_Type())
etsysAppSignPatternIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysAppSignPatternIndex.setStatus(_A)
class _EtsysAppSignPattern_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EtsysAppSignPattern_Type.__name__=_I
_EtsysAppSignPattern_Object=MibTableColumn
etsysAppSignPattern=_EtsysAppSignPattern_Object((1,3,6,1,4,1,5624,1,2,107,1,3,1,2),_EtsysAppSignPattern_Type())
etsysAppSignPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAppSignPattern.setStatus(_A)
_EtsysAppSignPatternRowStatus_Type=RowStatus
_EtsysAppSignPatternRowStatus_Object=MibTableColumn
etsysAppSignPatternRowStatus=_EtsysAppSignPatternRowStatus_Object((1,3,6,1,4,1,5624,1,2,107,1,3,1,3),_EtsysAppSignPatternRowStatus_Type())
etsysAppSignPatternRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAppSignPatternRowStatus.setStatus(_A)
_EtsysApplicationSignatureConformance_ObjectIdentity=ObjectIdentity
etsysApplicationSignatureConformance=_EtsysApplicationSignatureConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,107,2))
_EtsysAppSignGroups_ObjectIdentity=ObjectIdentity
etsysAppSignGroups=_EtsysAppSignGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,107,2,1))
_EtsysAppSignCompliances_ObjectIdentity=ObjectIdentity
etsysAppSignCompliances=_EtsysAppSignCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,107,2,2))
etsysAppSignGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,107,2,1,1))
etsysAppSignGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:etsysAppSignGroup.setStatus(_A)
etsysAppSignDisplayNameGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,107,2,1,2))
etsysAppSignDisplayNameGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:etsysAppSignDisplayNameGroup.setStatus(_A)
etsysAppSignPatternGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,107,2,1,3))
etsysAppSignPatternGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:etsysAppSignPatternGroup.setStatus(_A)
etsysAppSignCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,107,2,2,1))
etsysAppSignCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:etsysAppSignCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysApplicationSignatureMIB':etsysApplicationSignatureMIB,'etsysApplicationSignatureMIBObjects':etsysApplicationSignatureMIBObjects,'etsysAppSignGroupTable':etsysAppSignGroupTable,'etsysAppSignGroupEntry':etsysAppSignGroupEntry,_E:etsysAppSignGroupId,_K:etsysAppSignGroupName,'etsysAppSignDisplayNameTable':etsysAppSignDisplayNameTable,'etsysAppSignDisplayNameEntry':etsysAppSignDisplayNameEntry,_G:etsysAppSignDisplayId,_L:etsysAppSignDisplayName,_M:etsysAppSignDisplayNameRowStatus,'etsysAppSignPatternTable':etsysAppSignPatternTable,'etsysAppSignPatternEntry':etsysAppSignPatternEntry,_J:etsysAppSignPatternIndex,_N:etsysAppSignPattern,_O:etsysAppSignPatternRowStatus,'etsysApplicationSignatureConformance':etsysApplicationSignatureConformance,'etsysAppSignGroups':etsysAppSignGroups,_P:etsysAppSignGroup,_Q:etsysAppSignDisplayNameGroup,_R:etsysAppSignPatternGroup,'etsysAppSignCompliances':etsysAppSignCompliances,'etsysAppSignCompliance':etsysAppSignCompliance})