_R='read-only'
_Q='eqlTagObjectIndex'
_P='read-create'
_O='Unsigned32'
_N='eqliscsiVolumeIndex'
_M='eqliscsiLocalMemberId'
_L='eqlStorageGroupAdminAccountIndex'
_K='eqlGroupId'
_J='not-accessible'
_I='Integer32'
_H='EQLVOLUME-MIB'
_G='EQLGROUP-MIB'
_F='UTFString'
_E='eqlTagIndex'
_D='eqlTagType'
_C='read-write'
_B='EQLTAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
UTFString,eqlGroupId,eqlStorageGroupAdminAccountIndex=mibBuilder.importSymbols(_G,_F,_K,_L)
eqliscsiLocalMemberId,eqliscsiVolumeIndex=mibBuilder.importSymbols(_H,_M,_N)
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'enterprises','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
eqltagModule=ModuleIdentity((1,3,6,1,4,1,12740,23))
if mibBuilder.loadTexts:eqltagModule.setRevisions(('2011-10-02 00:00',))
_EqltagObjects_ObjectIdentity=ObjectIdentity
eqltagObjects=_EqltagObjects_ObjectIdentity((1,3,6,1,4,1,12740,23,1))
_EqlTagTable_Object=MibTable
eqlTagTable=_EqlTagTable_Object((1,3,6,1,4,1,12740,23,1,1))
if mibBuilder.loadTexts:eqlTagTable.setStatus(_A)
_EqlTagEntry_Object=MibTableRow
eqlTagEntry=_EqlTagEntry_Object((1,3,6,1,4,1,12740,23,1,1,1))
eqlTagEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:eqlTagEntry.setStatus(_A)
class _EqlTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('folder',1))
_EqlTagType_Type.__name__=_I
_EqlTagType_Object=MibTableColumn
eqlTagType=_EqlTagType_Object((1,3,6,1,4,1,12740,23,1,1,1,1),_EqlTagType_Type())
eqlTagType.setMaxAccess(_J)
if mibBuilder.loadTexts:eqlTagType.setStatus(_A)
_EqlTagIndex_Type=Unsigned32
_EqlTagIndex_Object=MibTableColumn
eqlTagIndex=_EqlTagIndex_Object((1,3,6,1,4,1,12740,23,1,1,1,2),_EqlTagIndex_Type())
eqlTagIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eqlTagIndex.setStatus(_A)
_EqlTagRowStatus_Type=RowStatus
_EqlTagRowStatus_Object=MibTableColumn
eqlTagRowStatus=_EqlTagRowStatus_Object((1,3,6,1,4,1,12740,23,1,1,1,3),_EqlTagRowStatus_Type())
eqlTagRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:eqlTagRowStatus.setStatus(_A)
class _EqlTagValue_Type(UTFString):defaultValue=OctetString('');subtypeSpec=UTFString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EqlTagValue_Type.__name__=_F
_EqlTagValue_Object=MibTableColumn
eqlTagValue=_EqlTagValue_Object((1,3,6,1,4,1,12740,23,1,1,1,4),_EqlTagValue_Type())
eqlTagValue.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlTagValue.setStatus(_A)
class _EqlTagAdminAccountKey_Type(Unsigned32):defaultValue=0
_EqlTagAdminAccountKey_Type.__name__=_O
_EqlTagAdminAccountKey_Object=MibTableColumn
eqlTagAdminAccountKey=_EqlTagAdminAccountKey_Object((1,3,6,1,4,1,12740,23,1,1,1,5),_EqlTagAdminAccountKey_Type())
eqlTagAdminAccountKey.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlTagAdminAccountKey.setStatus(_A)
class _EqlTagValueDescription_Type(UTFString):defaultValue=OctetString('');subtypeSpec=UTFString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EqlTagValueDescription_Type.__name__=_F
_EqlTagValueDescription_Object=MibTableColumn
eqlTagValueDescription=_EqlTagValueDescription_Object((1,3,6,1,4,1,12740,23,1,1,1,6),_EqlTagValueDescription_Type())
eqlTagValueDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlTagValueDescription.setStatus(_A)
_EqlTagObjectTable_Object=MibTable
eqlTagObjectTable=_EqlTagObjectTable_Object((1,3,6,1,4,1,12740,23,1,2))
if mibBuilder.loadTexts:eqlTagObjectTable.setStatus(_A)
_EqlTagObjectEntry_Object=MibTableRow
eqlTagObjectEntry=_EqlTagObjectEntry_Object((1,3,6,1,4,1,12740,23,1,2,1))
eqlTagObjectEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_Q))
if mibBuilder.loadTexts:eqlTagObjectEntry.setStatus(_A)
_EqlTagObjectIndex_Type=Unsigned32
_EqlTagObjectIndex_Object=MibTableColumn
eqlTagObjectIndex=_EqlTagObjectIndex_Object((1,3,6,1,4,1,12740,23,1,2,1,1),_EqlTagObjectIndex_Type())
eqlTagObjectIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eqlTagObjectIndex.setStatus(_A)
_EqlTagObjectTaggedObjectPointer_Type=RowPointer
_EqlTagObjectTaggedObjectPointer_Object=MibTableColumn
eqlTagObjectTaggedObjectPointer=_EqlTagObjectTaggedObjectPointer_Object((1,3,6,1,4,1,12740,23,1,2,1,2),_EqlTagObjectTaggedObjectPointer_Type())
eqlTagObjectTaggedObjectPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlTagObjectTaggedObjectPointer.setStatus(_A)
_EqlTagObjectRowStatus_Type=RowStatus
_EqlTagObjectRowStatus_Object=MibTableColumn
eqlTagObjectRowStatus=_EqlTagObjectRowStatus_Object((1,3,6,1,4,1,12740,23,1,2,1,3),_EqlTagObjectRowStatus_Type())
eqlTagObjectRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:eqlTagObjectRowStatus.setStatus(_A)
_EqlAdminAccountTagTable_Object=MibTable
eqlAdminAccountTagTable=_EqlAdminAccountTagTable_Object((1,3,6,1,4,1,12740,23,1,3))
if mibBuilder.loadTexts:eqlAdminAccountTagTable.setStatus(_A)
_EqlAdminAccountTagEntry_Object=MibTableRow
eqlAdminAccountTagEntry=_EqlAdminAccountTagEntry_Object((1,3,6,1,4,1,12740,23,1,3,1))
eqlAdminAccountTagEntry.setIndexNames((0,_G,_K),(0,_G,_L),(0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:eqlAdminAccountTagEntry.setStatus(_A)
class _EqlAdminAccountTagAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_C,2)))
_EqlAdminAccountTagAccess_Type.__name__=_I
_EqlAdminAccountTagAccess_Object=MibTableColumn
eqlAdminAccountTagAccess=_EqlAdminAccountTagAccess_Object((1,3,6,1,4,1,12740,23,1,3,1,1),_EqlAdminAccountTagAccess_Type())
eqlAdminAccountTagAccess.setMaxAccess(_R)
if mibBuilder.loadTexts:eqlAdminAccountTagAccess.setStatus(_A)
_EqlVolumeTagTable_Object=MibTable
eqlVolumeTagTable=_EqlVolumeTagTable_Object((1,3,6,1,4,1,12740,23,1,4))
if mibBuilder.loadTexts:eqlVolumeTagTable.setStatus(_A)
_EqlVolumeTagEntry_Object=MibTableRow
eqlVolumeTagEntry=_EqlVolumeTagEntry_Object((1,3,6,1,4,1,12740,23,1,4,1))
eqlVolumeTagEntry.setIndexNames((0,_H,_M),(0,_H,_N),(0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:eqlVolumeTagEntry.setStatus(_A)
class _EqlVolumeTagValue_Type(UTFString):subtypeSpec=UTFString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EqlVolumeTagValue_Type.__name__=_F
_EqlVolumeTagValue_Object=MibTableColumn
eqlVolumeTagValue=_EqlVolumeTagValue_Object((1,3,6,1,4,1,12740,23,1,4,1,1),_EqlVolumeTagValue_Type())
eqlVolumeTagValue.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlVolumeTagValue.setStatus(_A)
_EqltagNotifications_ObjectIdentity=ObjectIdentity
eqltagNotifications=_EqltagNotifications_ObjectIdentity((1,3,6,1,4,1,12740,23,2))
_EqltagConformance_ObjectIdentity=ObjectIdentity
eqltagConformance=_EqltagConformance_ObjectIdentity((1,3,6,1,4,1,12740,23,3))
mibBuilder.exportSymbols(_B,**{'eqltagModule':eqltagModule,'eqltagObjects':eqltagObjects,'eqlTagTable':eqlTagTable,'eqlTagEntry':eqlTagEntry,_D:eqlTagType,_E:eqlTagIndex,'eqlTagRowStatus':eqlTagRowStatus,'eqlTagValue':eqlTagValue,'eqlTagAdminAccountKey':eqlTagAdminAccountKey,'eqlTagValueDescription':eqlTagValueDescription,'eqlTagObjectTable':eqlTagObjectTable,'eqlTagObjectEntry':eqlTagObjectEntry,_Q:eqlTagObjectIndex,'eqlTagObjectTaggedObjectPointer':eqlTagObjectTaggedObjectPointer,'eqlTagObjectRowStatus':eqlTagObjectRowStatus,'eqlAdminAccountTagTable':eqlAdminAccountTagTable,'eqlAdminAccountTagEntry':eqlAdminAccountTagEntry,'eqlAdminAccountTagAccess':eqlAdminAccountTagAccess,'eqlVolumeTagTable':eqlVolumeTagTable,'eqlVolumeTagEntry':eqlVolumeTagEntry,'eqlVolumeTagValue':eqlVolumeTagValue,'eqltagNotifications':eqltagNotifications,'eqltagConformance':eqltagConformance})