_n='iccpRgGroupV1'
_m='iccpNodeGroupV1'
_l='iccpRgCommunicationFailure'
_k='iccpRgCreateMcLag'
_j='iccpRgApplication'
_i='iccpRgInternalReference'
_h='iccpRgApplicationState'
_g='iccpRgState'
_f='iccpRgVlanId'
_e='iccpRgMegLevel'
_d='iccpRgMegGroupId'
_c='iccpRgMepId'
_b='iccpRgMepMaid'
_a='iccpRgMepName'
_Z='iccpRgPortId'
_Y='iccpRgPeerMacAddress'
_X='iccpRgRedundancyObjectId'
_W='iccpRgRedundancyGroupId'
_V='iccpRgDescr'
_U='iccpRgName'
_T='iccpNodeInternalReference'
_S='iccpNodeCreateIccpRg'
_R='iccpNodeSystemMacAddress'
_Q='iccpGeneralIccpNodeTableSize'
_P='iccpGeneralStateLastChangeTime'
_O='iccpGeneralLastChangeTime'
_N='undefined'
_M='operational'
_L='connecting'
_K='nonExistent'
_J='iccpRgIndex'
_I='iccpNodeIndex'
_H='Integer32'
_G='DisplayString'
_F='read-write'
_E='read-create'
_D='read-only'
_C='Unsigned32'
_B='LUM-ICCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIccpMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIccpMIB','lumModules')
CommandString,FaultStatus,MgmtNameString=mibBuilder.importSymbols('LUM-TC','CommandString','FaultStatus','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'MacAddress','PhysAddress','TextualConvention')
lumIccpMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,61))
if mibBuilder.loadTexts:lumIccpMIBModule.setRevisions(('2017-09-01 00:00','2017-06-15 00:00','2015-01-14 00:00','2014-11-05 00:00'))
class IccpLabel(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
class IccpIdentifier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LumIccpConfs_ObjectIdentity=ObjectIdentity
lumIccpConfs=_LumIccpConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,61,1))
_LumIccpGroups_ObjectIdentity=ObjectIdentity
lumIccpGroups=_LumIccpGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,61,1,1))
_LumIccpCompl_ObjectIdentity=ObjectIdentity
lumIccpCompl=_LumIccpCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,61,1,2))
_LumIccpMIBObjects_ObjectIdentity=ObjectIdentity
lumIccpMIBObjects=_LumIccpMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,61,2))
_IccpGeneral_ObjectIdentity=ObjectIdentity
iccpGeneral=_IccpGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,61,2,1))
_IccpGeneralLastChangeTime_Type=DateAndTime
_IccpGeneralLastChangeTime_Object=MibScalar
iccpGeneralLastChangeTime=_IccpGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,61,2,1,1),_IccpGeneralLastChangeTime_Type())
iccpGeneralLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpGeneralLastChangeTime.setStatus(_A)
_IccpGeneralStateLastChangeTime_Type=DateAndTime
_IccpGeneralStateLastChangeTime_Object=MibScalar
iccpGeneralStateLastChangeTime=_IccpGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,61,2,1,2),_IccpGeneralStateLastChangeTime_Type())
iccpGeneralStateLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpGeneralStateLastChangeTime.setStatus(_A)
_IccpGeneralIccpNodeTableSize_Type=Unsigned32
_IccpGeneralIccpNodeTableSize_Object=MibScalar
iccpGeneralIccpNodeTableSize=_IccpGeneralIccpNodeTableSize_Object((1,3,6,1,4,1,8708,2,61,2,1,3),_IccpGeneralIccpNodeTableSize_Type())
iccpGeneralIccpNodeTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpGeneralIccpNodeTableSize.setStatus(_A)
_IccpGeneralIccpRgTableSize_Type=Unsigned32
_IccpGeneralIccpRgTableSize_Object=MibScalar
iccpGeneralIccpRgTableSize=_IccpGeneralIccpRgTableSize_Object((1,3,6,1,4,1,8708,2,61,2,1,4),_IccpGeneralIccpRgTableSize_Type())
iccpGeneralIccpRgTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpGeneralIccpRgTableSize.setStatus(_A)
_IccpNodeList_ObjectIdentity=ObjectIdentity
iccpNodeList=_IccpNodeList_ObjectIdentity((1,3,6,1,4,1,8708,2,61,2,2))
_IccpNodeTable_Object=MibTable
iccpNodeTable=_IccpNodeTable_Object((1,3,6,1,4,1,8708,2,61,2,2,1))
if mibBuilder.loadTexts:iccpNodeTable.setStatus(_A)
_IccpNodeEntry_Object=MibTableRow
iccpNodeEntry=_IccpNodeEntry_Object((1,3,6,1,4,1,8708,2,61,2,2,1,1))
iccpNodeEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:iccpNodeEntry.setStatus(_A)
class _IccpNodeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IccpNodeIndex_Type.__name__=_C
_IccpNodeIndex_Object=MibTableColumn
iccpNodeIndex=_IccpNodeIndex_Object((1,3,6,1,4,1,8708,2,61,2,2,1,1,1),_IccpNodeIndex_Type())
iccpNodeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpNodeIndex.setStatus(_A)
_IccpNodeName_Type=MgmtNameString
_IccpNodeName_Object=MibTableColumn
iccpNodeName=_IccpNodeName_Object((1,3,6,1,4,1,8708,2,61,2,2,1,1,2),_IccpNodeName_Type())
iccpNodeName.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpNodeName.setStatus(_A)
class _IccpNodeSystemMacAddress_Type(DisplayString):defaultValue=OctetString('')
_IccpNodeSystemMacAddress_Type.__name__=_G
_IccpNodeSystemMacAddress_Object=MibTableColumn
iccpNodeSystemMacAddress=_IccpNodeSystemMacAddress_Object((1,3,6,1,4,1,8708,2,61,2,2,1,1,3),_IccpNodeSystemMacAddress_Type())
iccpNodeSystemMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpNodeSystemMacAddress.setStatus(_A)
_IccpNodeCreateIccpRg_Type=CommandString
_IccpNodeCreateIccpRg_Object=MibTableColumn
iccpNodeCreateIccpRg=_IccpNodeCreateIccpRg_Object((1,3,6,1,4,1,8708,2,61,2,2,1,1,4),_IccpNodeCreateIccpRg_Type())
iccpNodeCreateIccpRg.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpNodeCreateIccpRg.setStatus(_A)
class _IccpNodeInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IccpNodeInternalReference_Type.__name__=_C
_IccpNodeInternalReference_Object=MibTableColumn
iccpNodeInternalReference=_IccpNodeInternalReference_Object((1,3,6,1,4,1,8708,2,61,2,2,1,1,5),_IccpNodeInternalReference_Type())
iccpNodeInternalReference.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpNodeInternalReference.setStatus(_A)
_IccpRgList_ObjectIdentity=ObjectIdentity
iccpRgList=_IccpRgList_ObjectIdentity((1,3,6,1,4,1,8708,2,61,2,3))
_IccpRgTable_Object=MibTable
iccpRgTable=_IccpRgTable_Object((1,3,6,1,4,1,8708,2,61,2,3,1))
if mibBuilder.loadTexts:iccpRgTable.setStatus(_A)
_IccpRgEntry_Object=MibTableRow
iccpRgEntry=_IccpRgEntry_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1))
iccpRgEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:iccpRgEntry.setStatus(_A)
class _IccpRgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IccpRgIndex_Type.__name__=_C
_IccpRgIndex_Object=MibTableColumn
iccpRgIndex=_IccpRgIndex_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,1),_IccpRgIndex_Type())
iccpRgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpRgIndex.setStatus(_A)
_IccpRgName_Type=MgmtNameString
_IccpRgName_Object=MibTableColumn
iccpRgName=_IccpRgName_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,2),_IccpRgName_Type())
iccpRgName.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpRgName.setStatus(_A)
class _IccpRgDescr_Type(DisplayString):defaultValue=OctetString('')
_IccpRgDescr_Type.__name__=_G
_IccpRgDescr_Object=MibTableColumn
iccpRgDescr=_IccpRgDescr_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,3),_IccpRgDescr_Type())
iccpRgDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgDescr.setStatus(_A)
class _IccpRgRedundancyGroupId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IccpRgRedundancyGroupId_Type.__name__=_C
_IccpRgRedundancyGroupId_Object=MibTableColumn
iccpRgRedundancyGroupId=_IccpRgRedundancyGroupId_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,4),_IccpRgRedundancyGroupId_Type())
iccpRgRedundancyGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgRedundancyGroupId.setStatus(_A)
class _IccpRgRedundancyObjectId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IccpRgRedundancyObjectId_Type.__name__=_C
_IccpRgRedundancyObjectId_Object=MibTableColumn
iccpRgRedundancyObjectId=_IccpRgRedundancyObjectId_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,5),_IccpRgRedundancyObjectId_Type())
iccpRgRedundancyObjectId.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgRedundancyObjectId.setStatus(_A)
_IccpRgPeerMacAddress_Type=MacAddress
_IccpRgPeerMacAddress_Object=MibTableColumn
iccpRgPeerMacAddress=_IccpRgPeerMacAddress_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,6),_IccpRgPeerMacAddress_Type())
iccpRgPeerMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgPeerMacAddress.setStatus(_A)
class _IccpRgPortId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_IccpRgPortId_Type.__name__=_C
_IccpRgPortId_Object=MibTableColumn
iccpRgPortId=_IccpRgPortId_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,7),_IccpRgPortId_Type())
iccpRgPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgPortId.setStatus(_A)
class _IccpRgMepName_Type(DisplayString):defaultValue=OctetString('')
_IccpRgMepName_Type.__name__=_G
_IccpRgMepName_Object=MibTableColumn
iccpRgMepName=_IccpRgMepName_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,8),_IccpRgMepName_Type())
iccpRgMepName.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgMepName.setStatus(_A)
class _IccpRgMepMaid_Type(DisplayString):defaultValue=OctetString('')
_IccpRgMepMaid_Type.__name__=_G
_IccpRgMepMaid_Object=MibTableColumn
iccpRgMepMaid=_IccpRgMepMaid_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,9),_IccpRgMepMaid_Type())
iccpRgMepMaid.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgMepMaid.setStatus(_A)
class _IccpRgMepId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_IccpRgMepId_Type.__name__=_C
_IccpRgMepId_Object=MibTableColumn
iccpRgMepId=_IccpRgMepId_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,10),_IccpRgMepId_Type())
iccpRgMepId.setMaxAccess(_F)
if mibBuilder.loadTexts:iccpRgMepId.setStatus(_A)
class _IccpRgMegGroupId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_IccpRgMegGroupId_Type.__name__=_C
_IccpRgMegGroupId_Object=MibTableColumn
iccpRgMegGroupId=_IccpRgMegGroupId_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,11),_IccpRgMegGroupId_Type())
iccpRgMegGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgMegGroupId.setStatus(_A)
class _IccpRgMegLevel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IccpRgMegLevel_Type.__name__=_C
_IccpRgMegLevel_Object=MibTableColumn
iccpRgMegLevel=_IccpRgMegLevel_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,12),_IccpRgMegLevel_Type())
iccpRgMegLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgMegLevel.setStatus(_A)
class _IccpRgVlanId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IccpRgVlanId_Type.__name__=_C
_IccpRgVlanId_Object=MibTableColumn
iccpRgVlanId=_IccpRgVlanId_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,13),_IccpRgVlanId_Type())
iccpRgVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgVlanId.setStatus(_A)
class _IccpRgState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_IccpRgState_Type.__name__=_H
_IccpRgState_Object=MibTableColumn
iccpRgState=_IccpRgState_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,14),_IccpRgState_Type())
iccpRgState.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgState.setStatus(_A)
class _IccpRgApplicationState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),('reset',2),('connectSent',3),('connectReceive',4),(_L,5),(_M,6),(_N,7)))
_IccpRgApplicationState_Type.__name__=_H
_IccpRgApplicationState_Object=MibTableColumn
iccpRgApplicationState=_IccpRgApplicationState_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,15),_IccpRgApplicationState_Type())
iccpRgApplicationState.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgApplicationState.setStatus(_A)
class _IccpRgInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IccpRgInternalReference_Type.__name__=_C
_IccpRgInternalReference_Object=MibTableColumn
iccpRgInternalReference=_IccpRgInternalReference_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,16),_IccpRgInternalReference_Type())
iccpRgInternalReference.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgInternalReference.setStatus(_A)
class _IccpRgApplication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('mLacp',2),('pwRed',3),('mLacpAndIccp',4)))
_IccpRgApplication_Type.__name__=_H
_IccpRgApplication_Object=MibTableColumn
iccpRgApplication=_IccpRgApplication_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,17),_IccpRgApplication_Type())
iccpRgApplication.setMaxAccess(_E)
if mibBuilder.loadTexts:iccpRgApplication.setStatus(_A)
_IccpRgCreateMcLag_Type=CommandString
_IccpRgCreateMcLag_Object=MibTableColumn
iccpRgCreateMcLag=_IccpRgCreateMcLag_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,18),_IccpRgCreateMcLag_Type())
iccpRgCreateMcLag.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpRgCreateMcLag.setStatus(_A)
_IccpRgCommunicationFailure_Type=FaultStatus
_IccpRgCommunicationFailure_Object=MibTableColumn
iccpRgCommunicationFailure=_IccpRgCommunicationFailure_Object((1,3,6,1,4,1,8708,2,61,2,3,1,1,19),_IccpRgCommunicationFailure_Type())
iccpRgCommunicationFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:iccpRgCommunicationFailure.setStatus(_A)
iccpGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,61,1,1,1))
iccpGeneralGroupV1.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:iccpGeneralGroupV1.setStatus(_A)
iccpNodeGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,61,1,1,2))
iccpNodeGroupV1.setObjects(*((_B,_I),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:iccpNodeGroupV1.setStatus(_A)
iccpRgGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,61,1,1,3))
iccpRgGroupV1.setObjects(*((_B,_J),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:iccpRgGroupV1.setStatus(_A)
lumIccpBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,61,1,2,1))
lumIccpBasicComplV1.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:lumIccpBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IccpLabel':IccpLabel,'IccpIdentifier':IccpIdentifier,'lumIccpMIBModule':lumIccpMIBModule,'lumIccpConfs':lumIccpConfs,'lumIccpGroups':lumIccpGroups,'iccpGeneralGroupV1':iccpGeneralGroupV1,_m:iccpNodeGroupV1,_n:iccpRgGroupV1,'lumIccpCompl':lumIccpCompl,'lumIccpBasicComplV1':lumIccpBasicComplV1,'lumIccpMIBObjects':lumIccpMIBObjects,'iccpGeneral':iccpGeneral,_O:iccpGeneralLastChangeTime,_P:iccpGeneralStateLastChangeTime,_Q:iccpGeneralIccpNodeTableSize,'iccpGeneralIccpRgTableSize':iccpGeneralIccpRgTableSize,'iccpNodeList':iccpNodeList,'iccpNodeTable':iccpNodeTable,'iccpNodeEntry':iccpNodeEntry,_I:iccpNodeIndex,'iccpNodeName':iccpNodeName,_R:iccpNodeSystemMacAddress,_S:iccpNodeCreateIccpRg,_T:iccpNodeInternalReference,'iccpRgList':iccpRgList,'iccpRgTable':iccpRgTable,'iccpRgEntry':iccpRgEntry,_J:iccpRgIndex,_U:iccpRgName,_V:iccpRgDescr,_W:iccpRgRedundancyGroupId,_X:iccpRgRedundancyObjectId,_Y:iccpRgPeerMacAddress,_Z:iccpRgPortId,_a:iccpRgMepName,_b:iccpRgMepMaid,_c:iccpRgMepId,_d:iccpRgMegGroupId,_e:iccpRgMegLevel,_f:iccpRgVlanId,_g:iccpRgState,_h:iccpRgApplicationState,_i:iccpRgInternalReference,_j:iccpRgApplication,_k:iccpRgCreateMcLag,_l:iccpRgCommunicationFailure})