_M='zxr10CesId'
_L='zxr10CipId'
_K='zxr10UniId'
_J='enable'
_I='disable'
_H='read-create'
_G='down'
_F='not-accessible'
_E='ZXR10-IF-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxr10interfaces,=mibBuilder.importSymbols('ZXR10-SMI','zxr10interfaces')
class ListStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
class CipPriorityValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_Zxr10UniTable_Object=MibTable
zxr10UniTable=_Zxr10UniTable_Object((1,3,6,1,4,1,3902,3,103,4))
if mibBuilder.loadTexts:zxr10UniTable.setStatus(_A)
_Zxr10UniEntry_Object=MibTableRow
zxr10UniEntry=_Zxr10UniEntry_Object((1,3,6,1,4,1,3902,3,103,4,1))
zxr10UniEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:zxr10UniEntry.setStatus(_A)
_Zxr10UniId_Type=Integer32
_Zxr10UniId_Object=MibTableColumn
zxr10UniId=_Zxr10UniId_Object((1,3,6,1,4,1,3902,3,103,4,1,1),_Zxr10UniId_Type())
zxr10UniId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxr10UniId.setStatus(_A)
_Zxr10UniName_Type=DisplayString
_Zxr10UniName_Object=MibTableColumn
zxr10UniName=_Zxr10UniName_Object((1,3,6,1,4,1,3902,3,103,4,1,2),_Zxr10UniName_Type())
zxr10UniName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10UniName.setStatus(_A)
_Zxr10UniDesciption_Type=DisplayString
_Zxr10UniDesciption_Object=MibTableColumn
zxr10UniDesciption=_Zxr10UniDesciption_Object((1,3,6,1,4,1,3902,3,103,4,1,3),_Zxr10UniDesciption_Type())
zxr10UniDesciption.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10UniDesciption.setStatus(_A)
_Zxr10UniBindIfName_Type=DisplayString
_Zxr10UniBindIfName_Object=MibTableColumn
zxr10UniBindIfName=_Zxr10UniBindIfName_Object((1,3,6,1,4,1,3902,3,103,4,1,4),_Zxr10UniBindIfName_Type())
zxr10UniBindIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10UniBindIfName.setStatus(_A)
_Zxr10UniBindIfIndex_Type=Integer32
_Zxr10UniBindIfIndex_Object=MibTableColumn
zxr10UniBindIfIndex=_Zxr10UniBindIfIndex_Object((1,3,6,1,4,1,3902,3,103,4,1,5),_Zxr10UniBindIfIndex_Type())
zxr10UniBindIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10UniBindIfIndex.setStatus(_A)
_Zxr10UniLstStatus_Type=ListStatus
_Zxr10UniLstStatus_Object=MibTableColumn
zxr10UniLstStatus=_Zxr10UniLstStatus_Object((1,3,6,1,4,1,3902,3,103,4,1,6),_Zxr10UniLstStatus_Type())
zxr10UniLstStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10UniLstStatus.setStatus(_A)
_Zxr10UniRowStatus_Type=RowStatus
_Zxr10UniRowStatus_Object=MibTableColumn
zxr10UniRowStatus=_Zxr10UniRowStatus_Object((1,3,6,1,4,1,3902,3,103,4,1,7),_Zxr10UniRowStatus_Type())
zxr10UniRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10UniRowStatus.setStatus(_A)
_Zxr10CipTable_Object=MibTable
zxr10CipTable=_Zxr10CipTable_Object((1,3,6,1,4,1,3902,3,103,5))
if mibBuilder.loadTexts:zxr10CipTable.setStatus(_A)
_Zxr10CipEntry_Object=MibTableRow
zxr10CipEntry=_Zxr10CipEntry_Object((1,3,6,1,4,1,3902,3,103,5,1))
zxr10CipEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:zxr10CipEntry.setStatus(_A)
_Zxr10CipId_Type=Integer32
_Zxr10CipId_Object=MibTableColumn
zxr10CipId=_Zxr10CipId_Object((1,3,6,1,4,1,3902,3,103,5,1,1),_Zxr10CipId_Type())
zxr10CipId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxr10CipId.setStatus(_A)
_Zxr10CipName_Type=DisplayString
_Zxr10CipName_Object=MibTableColumn
zxr10CipName=_Zxr10CipName_Object((1,3,6,1,4,1,3902,3,103,5,1,2),_Zxr10CipName_Type())
zxr10CipName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipName.setStatus(_A)
_Zxr10CipDesciption_Type=DisplayString
_Zxr10CipDesciption_Object=MibTableColumn
zxr10CipDesciption=_Zxr10CipDesciption_Object((1,3,6,1,4,1,3902,3,103,5,1,3),_Zxr10CipDesciption_Type())
zxr10CipDesciption.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipDesciption.setStatus(_A)
_Zxr10CipType_Type=Integer32
_Zxr10CipType_Object=MibTableColumn
zxr10CipType=_Zxr10CipType_Object((1,3,6,1,4,1,3902,3,103,5,1,4),_Zxr10CipType_Type())
zxr10CipType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipType.setStatus(_A)
_Zxr10CipBindName_Type=DisplayString
_Zxr10CipBindName_Object=MibTableColumn
zxr10CipBindName=_Zxr10CipBindName_Object((1,3,6,1,4,1,3902,3,103,5,1,5),_Zxr10CipBindName_Type())
zxr10CipBindName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipBindName.setStatus(_A)
_Zxr10CipBindIdOrIfIndex_Type=Integer32
_Zxr10CipBindIdOrIfIndex_Object=MibTableColumn
zxr10CipBindIdOrIfIndex=_Zxr10CipBindIdOrIfIndex_Object((1,3,6,1,4,1,3902,3,103,5,1,6),_Zxr10CipBindIdOrIfIndex_Type())
zxr10CipBindIdOrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipBindIdOrIfIndex.setStatus(_A)
class _Zxr10CipAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_Zxr10CipAdminStatus_Type.__name__=_D
_Zxr10CipAdminStatus_Object=MibTableColumn
zxr10CipAdminStatus=_Zxr10CipAdminStatus_Object((1,3,6,1,4,1,3902,3,103,5,1,7),_Zxr10CipAdminStatus_Type())
zxr10CipAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zxr10CipAdminStatus.setStatus(_A)
class _Zxr10CipPhyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_Zxr10CipPhyStatus_Type.__name__=_D
_Zxr10CipPhyStatus_Object=MibTableColumn
zxr10CipPhyStatus=_Zxr10CipPhyStatus_Object((1,3,6,1,4,1,3902,3,103,5,1,8),_Zxr10CipPhyStatus_Type())
zxr10CipPhyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipPhyStatus.setStatus(_A)
class _Zxr10CipProStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_Zxr10CipProStatus_Type.__name__=_D
_Zxr10CipProStatus_Object=MibTableColumn
zxr10CipProStatus=_Zxr10CipProStatus_Object((1,3,6,1,4,1,3902,3,103,5,1,9),_Zxr10CipProStatus_Type())
zxr10CipProStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipProStatus.setStatus(_A)
class _Zxr10CipDetectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),('sf',1),('sd',2)))
_Zxr10CipDetectStatus_Type.__name__=_D
_Zxr10CipDetectStatus_Object=MibTableColumn
zxr10CipDetectStatus=_Zxr10CipDetectStatus_Object((1,3,6,1,4,1,3902,3,103,5,1,10),_Zxr10CipDetectStatus_Type())
zxr10CipDetectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipDetectStatus.setStatus(_A)
_Zxr10CipRowStatus_Type=RowStatus
_Zxr10CipRowStatus_Object=MibTableColumn
zxr10CipRowStatus=_Zxr10CipRowStatus_Object((1,3,6,1,4,1,3902,3,103,5,1,11),_Zxr10CipRowStatus_Type())
zxr10CipRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zxr10CipRowStatus.setStatus(_A)
_Zxr10CipServiceIndex_Type=Integer32
_Zxr10CipServiceIndex_Object=MibTableColumn
zxr10CipServiceIndex=_Zxr10CipServiceIndex_Object((1,3,6,1,4,1,3902,3,103,5,1,12),_Zxr10CipServiceIndex_Type())
zxr10CipServiceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipServiceIndex.setStatus(_A)
_Zxr10CipPriority_Type=CipPriorityValue
_Zxr10CipPriority_Object=MibTableColumn
zxr10CipPriority=_Zxr10CipPriority_Object((1,3,6,1,4,1,3902,3,103,5,1,13),_Zxr10CipPriority_Type())
zxr10CipPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipPriority.setStatus(_A)
_Zxr10CipStackId_Type=Integer32
_Zxr10CipStackId_Object=MibTableColumn
zxr10CipStackId=_Zxr10CipStackId_Object((1,3,6,1,4,1,3902,3,103,5,1,14),_Zxr10CipStackId_Type())
zxr10CipStackId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipStackId.setStatus(_A)
_Zxr10CipQingTerminal_Type=Integer32
_Zxr10CipQingTerminal_Object=MibTableColumn
zxr10CipQingTerminal=_Zxr10CipQingTerminal_Object((1,3,6,1,4,1,3902,3,103,5,1,15),_Zxr10CipQingTerminal_Type())
zxr10CipQingTerminal.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipQingTerminal.setStatus(_A)
class _Zxr10CipStructure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('agnostic',0),('aware',1)))
_Zxr10CipStructure_Type.__name__=_D
_Zxr10CipStructure_Object=MibTableColumn
zxr10CipStructure=_Zxr10CipStructure_Object((1,3,6,1,4,1,3902,3,103,5,1,16),_Zxr10CipStructure_Type())
zxr10CipStructure.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipStructure.setStatus(_A)
_Zxr10CipIdleCode_Type=Integer32
_Zxr10CipIdleCode_Object=MibTableColumn
zxr10CipIdleCode=_Zxr10CipIdleCode_Object((1,3,6,1,4,1,3902,3,103,5,1,17),_Zxr10CipIdleCode_Type())
zxr10CipIdleCode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipIdleCode.setStatus(_A)
class _Zxr10CipVcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('e1',0),('t1',1)))
_Zxr10CipVcType_Type.__name__=_D
_Zxr10CipVcType_Object=MibTableColumn
zxr10CipVcType=_Zxr10CipVcType_Object((1,3,6,1,4,1,3902,3,103,5,1,18),_Zxr10CipVcType_Type())
zxr10CipVcType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipVcType.setStatus(_A)
_Zxr10CipAu3_Type=Integer32
_Zxr10CipAu3_Object=MibTableColumn
zxr10CipAu3=_Zxr10CipAu3_Object((1,3,6,1,4,1,3902,3,103,5,1,19),_Zxr10CipAu3_Type())
zxr10CipAu3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipAu3.setStatus(_A)
_Zxr10CipAu4_Type=Integer32
_Zxr10CipAu4_Object=MibTableColumn
zxr10CipAu4=_Zxr10CipAu4_Object((1,3,6,1,4,1,3902,3,103,5,1,20),_Zxr10CipAu4_Type())
zxr10CipAu4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipAu4.setStatus(_A)
_Zxr10CipTug2_Type=Integer32
_Zxr10CipTug2_Object=MibTableColumn
zxr10CipTug2=_Zxr10CipTug2_Object((1,3,6,1,4,1,3902,3,103,5,1,21),_Zxr10CipTug2_Type())
zxr10CipTug2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipTug2.setStatus(_A)
_Zxr10CipTug3_Type=Integer32
_Zxr10CipTug3_Object=MibTableColumn
zxr10CipTug3=_Zxr10CipTug3_Object((1,3,6,1,4,1,3902,3,103,5,1,22),_Zxr10CipTug3_Type())
zxr10CipTug3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipTug3.setStatus(_A)
_Zxr10CipVcId_Type=Integer32
_Zxr10CipVcId_Object=MibTableColumn
zxr10CipVcId=_Zxr10CipVcId_Object((1,3,6,1,4,1,3902,3,103,5,1,23),_Zxr10CipVcId_Type())
zxr10CipVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipVcId.setStatus(_A)
_Zxr10CipTimeslots_Type=DisplayString
_Zxr10CipTimeslots_Object=MibTableColumn
zxr10CipTimeslots=_Zxr10CipTimeslots_Object((1,3,6,1,4,1,3902,3,103,5,1,24),_Zxr10CipTimeslots_Type())
zxr10CipTimeslots.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CipTimeslots.setStatus(_A)
_Zxr10CipClassMapName_Type=DisplayString
_Zxr10CipClassMapName_Object=MibTableColumn
zxr10CipClassMapName=_Zxr10CipClassMapName_Object((1,3,6,1,4,1,3902,3,103,5,1,25),_Zxr10CipClassMapName_Type())
zxr10CipClassMapName.setMaxAccess(_H)
if mibBuilder.loadTexts:zxr10CipClassMapName.setStatus(_A)
class _Zxr10CipBindVpnStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_Zxr10CipBindVpnStatus_Type.__name__=_D
_Zxr10CipBindVpnStatus_Object=MibTableColumn
zxr10CipBindVpnStatus=_Zxr10CipBindVpnStatus_Object((1,3,6,1,4,1,3902,3,103,5,1,26),_Zxr10CipBindVpnStatus_Type())
zxr10CipBindVpnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CipBindVpnStatus.setStatus(_A)
_Zxr10CesTable_Object=MibTable
zxr10CesTable=_Zxr10CesTable_Object((1,3,6,1,4,1,3902,3,103,6))
if mibBuilder.loadTexts:zxr10CesTable.setStatus(_A)
_Zxr10CesEntry_Object=MibTableRow
zxr10CesEntry=_Zxr10CesEntry_Object((1,3,6,1,4,1,3902,3,103,6,1))
zxr10CesEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:zxr10CesEntry.setStatus(_A)
_Zxr10CesId_Type=Integer32
_Zxr10CesId_Object=MibTableColumn
zxr10CesId=_Zxr10CesId_Object((1,3,6,1,4,1,3902,3,103,6,1,1),_Zxr10CesId_Type())
zxr10CesId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxr10CesId.setStatus(_A)
_Zxr10CesName_Type=DisplayString
_Zxr10CesName_Object=MibTableColumn
zxr10CesName=_Zxr10CesName_Object((1,3,6,1,4,1,3902,3,103,6,1,2),_Zxr10CesName_Type())
zxr10CesName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CesName.setStatus(_A)
_Zxr10CesDesciption_Type=DisplayString
_Zxr10CesDesciption_Object=MibTableColumn
zxr10CesDesciption=_Zxr10CesDesciption_Object((1,3,6,1,4,1,3902,3,103,6,1,3),_Zxr10CesDesciption_Type())
zxr10CesDesciption.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CesDesciption.setStatus(_A)
_Zxr10CesE1Name_Type=DisplayString
_Zxr10CesE1Name_Object=MibTableColumn
zxr10CesE1Name=_Zxr10CesE1Name_Object((1,3,6,1,4,1,3902,3,103,6,1,4),_Zxr10CesE1Name_Type())
zxr10CesE1Name.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CesE1Name.setStatus(_A)
_Zxr10CesE1IfIndex_Type=Integer32
_Zxr10CesE1IfIndex_Object=MibTableColumn
zxr10CesE1IfIndex=_Zxr10CesE1IfIndex_Object((1,3,6,1,4,1,3902,3,103,6,1,5),_Zxr10CesE1IfIndex_Type())
zxr10CesE1IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CesE1IfIndex.setStatus(_A)
_Zxr10CesAal1_Type=Integer32
_Zxr10CesAal1_Object=MibTableColumn
zxr10CesAal1=_Zxr10CesAal1_Object((1,3,6,1,4,1,3902,3,103,6,1,6),_Zxr10CesAal1_Type())
zxr10CesAal1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CesAal1.setStatus(_A)
_Zxr10CesRowStatus_Type=RowStatus
_Zxr10CesRowStatus_Object=MibTableColumn
zxr10CesRowStatus=_Zxr10CesRowStatus_Object((1,3,6,1,4,1,3902,3,103,6,1,7),_Zxr10CesRowStatus_Type())
zxr10CesRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10CesRowStatus.setStatus(_A)
_Zxr10CesServiceIndex_Type=Integer32
_Zxr10CesServiceIndex_Object=MibTableColumn
zxr10CesServiceIndex=_Zxr10CesServiceIndex_Object((1,3,6,1,4,1,3902,3,103,6,1,8),_Zxr10CesServiceIndex_Type())
zxr10CesServiceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10CesServiceIndex.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ListStatus':ListStatus,'CipPriorityValue':CipPriorityValue,'zxr10UniTable':zxr10UniTable,'zxr10UniEntry':zxr10UniEntry,_K:zxr10UniId,'zxr10UniName':zxr10UniName,'zxr10UniDesciption':zxr10UniDesciption,'zxr10UniBindIfName':zxr10UniBindIfName,'zxr10UniBindIfIndex':zxr10UniBindIfIndex,'zxr10UniLstStatus':zxr10UniLstStatus,'zxr10UniRowStatus':zxr10UniRowStatus,'zxr10CipTable':zxr10CipTable,'zxr10CipEntry':zxr10CipEntry,_L:zxr10CipId,'zxr10CipName':zxr10CipName,'zxr10CipDesciption':zxr10CipDesciption,'zxr10CipType':zxr10CipType,'zxr10CipBindName':zxr10CipBindName,'zxr10CipBindIdOrIfIndex':zxr10CipBindIdOrIfIndex,'zxr10CipAdminStatus':zxr10CipAdminStatus,'zxr10CipPhyStatus':zxr10CipPhyStatus,'zxr10CipProStatus':zxr10CipProStatus,'zxr10CipDetectStatus':zxr10CipDetectStatus,'zxr10CipRowStatus':zxr10CipRowStatus,'zxr10CipServiceIndex':zxr10CipServiceIndex,'zxr10CipPriority':zxr10CipPriority,'zxr10CipStackId':zxr10CipStackId,'zxr10CipQingTerminal':zxr10CipQingTerminal,'zxr10CipStructure':zxr10CipStructure,'zxr10CipIdleCode':zxr10CipIdleCode,'zxr10CipVcType':zxr10CipVcType,'zxr10CipAu3':zxr10CipAu3,'zxr10CipAu4':zxr10CipAu4,'zxr10CipTug2':zxr10CipTug2,'zxr10CipTug3':zxr10CipTug3,'zxr10CipVcId':zxr10CipVcId,'zxr10CipTimeslots':zxr10CipTimeslots,'zxr10CipClassMapName':zxr10CipClassMapName,'zxr10CipBindVpnStatus':zxr10CipBindVpnStatus,'zxr10CesTable':zxr10CesTable,'zxr10CesEntry':zxr10CesEntry,_M:zxr10CesId,'zxr10CesName':zxr10CesName,'zxr10CesDesciption':zxr10CesDesciption,'zxr10CesE1Name':zxr10CesE1Name,'zxr10CesE1IfIndex':zxr10CesE1IfIndex,'zxr10CesAal1':zxr10CesAal1,'zxr10CesRowStatus':zxr10CesRowStatus,'zxr10CesServiceIndex':zxr10CesServiceIndex})