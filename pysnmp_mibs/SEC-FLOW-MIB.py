_M='nbsArFlowServicePortNumber'
_L='nbsArFlowServiceSpecsServiceId'
_K='nbsArFlowServiceFlowIndex'
_J='nbsArSecFlowIndex'
_I='NotificationType'
_H='modify'
_G='delete'
_F='add'
_E='none'
_D='SEC-FLOW-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1,=mibBuilder.importSymbols('NBASE-G1-MIB','nbSwitchG1')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbsAccelerouter_ObjectIdentity=ObjectIdentity
nbsAccelerouter=_NbsAccelerouter_ObjectIdentity((1,3,6,1,4,1,629,1,50,10))
_NbsArSecFlow_ObjectIdentity=ObjectIdentity
nbsArSecFlow=_NbsArSecFlow_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,8))
_NbsArSecFlowTable_Object=MibTable
nbsArSecFlowTable=_NbsArSecFlowTable_Object((1,3,6,1,4,1,629,1,50,10,8,1))
if mibBuilder.loadTexts:nbsArSecFlowTable.setStatus(_A)
_NbsArSecFlowEntry_Object=MibTableRow
nbsArSecFlowEntry=_NbsArSecFlowEntry_Object((1,3,6,1,4,1,629,1,50,10,8,1,1))
nbsArSecFlowEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:nbsArSecFlowEntry.setStatus(_A)
class _NbsArSecFlowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NbsArSecFlowIndex_Type.__name__=_C
_NbsArSecFlowIndex_Object=MibTableColumn
nbsArSecFlowIndex=_NbsArSecFlowIndex_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,1),_NbsArSecFlowIndex_Type())
nbsArSecFlowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowIndex.setStatus(_A)
_NbsArSecFlowValid_Type=Integer32
_NbsArSecFlowValid_Object=MibTableColumn
nbsArSecFlowValid=_NbsArSecFlowValid_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,2),_NbsArSecFlowValid_Type())
nbsArSecFlowValid.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowValid.setStatus(_A)
_NbsArSecFlowState_Type=Integer32
_NbsArSecFlowState_Object=MibTableColumn
nbsArSecFlowState=_NbsArSecFlowState_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,3),_NbsArSecFlowState_Type())
nbsArSecFlowState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowState.setStatus(_A)
class _NbsArSecFlowLastUsedTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NbsArSecFlowLastUsedTimestamp_Type.__name__=_C
_NbsArSecFlowLastUsedTimestamp_Object=MibTableColumn
nbsArSecFlowLastUsedTimestamp=_NbsArSecFlowLastUsedTimestamp_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,4),_NbsArSecFlowLastUsedTimestamp_Type())
nbsArSecFlowLastUsedTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowLastUsedTimestamp.setStatus(_A)
_NbsArSecFlowServTypes_Type=Integer32
_NbsArSecFlowServTypes_Object=MibTableColumn
nbsArSecFlowServTypes=_NbsArSecFlowServTypes_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,5),_NbsArSecFlowServTypes_Type())
nbsArSecFlowServTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowServTypes.setStatus(_A)
_NbsArSecFlowServId_Type=Integer32
_NbsArSecFlowServId_Object=MibTableColumn
nbsArSecFlowServId=_NbsArSecFlowServId_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,6),_NbsArSecFlowServId_Type())
nbsArSecFlowServId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowServId.setStatus(_A)
_NbsArFlowID_Type=OctetString
_NbsArFlowID_Object=MibTableColumn
nbsArFlowID=_NbsArFlowID_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,7),_NbsArFlowID_Type())
nbsArFlowID.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowID.setStatus(_A)
_NbsArFlowQoSSpec_Type=OctetString
_NbsArFlowQoSSpec_Object=MibTableColumn
nbsArFlowQoSSpec=_NbsArFlowQoSSpec_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,8),_NbsArFlowQoSSpec_Type())
nbsArFlowQoSSpec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowQoSSpec.setStatus(_A)
class _NbsArSecFlowNumOfServices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NbsArSecFlowNumOfServices_Type.__name__=_C
_NbsArSecFlowNumOfServices_Object=MibTableColumn
nbsArSecFlowNumOfServices=_NbsArSecFlowNumOfServices_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,9),_NbsArSecFlowNumOfServices_Type())
nbsArSecFlowNumOfServices.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowNumOfServices.setStatus(_A)
_NbsArSecFlowDriverData_Type=OctetString
_NbsArSecFlowDriverData_Object=MibTableColumn
nbsArSecFlowDriverData=_NbsArSecFlowDriverData_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,10),_NbsArSecFlowDriverData_Type())
nbsArSecFlowDriverData.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowDriverData.setStatus(_A)
_NbsArSecFlowActions_Type=OctetString
_NbsArSecFlowActions_Object=MibTableColumn
nbsArSecFlowActions=_NbsArSecFlowActions_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,11),_NbsArSecFlowActions_Type())
nbsArSecFlowActions.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowActions.setStatus(_A)
_NbsArSecFlowCounters_Type=OctetString
_NbsArSecFlowCounters_Object=MibTableColumn
nbsArSecFlowCounters=_NbsArSecFlowCounters_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,12),_NbsArSecFlowCounters_Type())
nbsArSecFlowCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowCounters.setStatus(_A)
class _NbsArSecFlowAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),('activate',5),('deactivate',6)))
_NbsArSecFlowAdminStatus_Type.__name__=_C
_NbsArSecFlowAdminStatus_Object=MibTableColumn
nbsArSecFlowAdminStatus=_NbsArSecFlowAdminStatus_Object((1,3,6,1,4,1,629,1,50,10,8,1,1,13),_NbsArSecFlowAdminStatus_Type())
nbsArSecFlowAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowAdminStatus.setStatus(_A)
_NbsArFlowServiceSpecTable_Object=MibTable
nbsArFlowServiceSpecTable=_NbsArFlowServiceSpecTable_Object((1,3,6,1,4,1,629,1,50,10,8,2))
if mibBuilder.loadTexts:nbsArFlowServiceSpecTable.setStatus(_A)
_NbsArFlowServiceSpecEntry_Object=MibTableRow
nbsArFlowServiceSpecEntry=_NbsArFlowServiceSpecEntry_Object((1,3,6,1,4,1,629,1,50,10,8,2,1))
nbsArFlowServiceSpecEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:nbsArFlowServiceSpecEntry.setStatus(_A)
_NbsArFlowServiceFlowIndex_Type=Integer32
_NbsArFlowServiceFlowIndex_Object=MibTableColumn
nbsArFlowServiceFlowIndex=_NbsArFlowServiceFlowIndex_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,1),_NbsArFlowServiceFlowIndex_Type())
nbsArFlowServiceFlowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceFlowIndex.setStatus(_A)
_NbsArFlowServiceSpecsServiceId_Type=Integer32
_NbsArFlowServiceSpecsServiceId_Object=MibTableColumn
nbsArFlowServiceSpecsServiceId=_NbsArFlowServiceSpecsServiceId_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,2),_NbsArFlowServiceSpecsServiceId_Type())
nbsArFlowServiceSpecsServiceId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsServiceId.setStatus(_A)
_NbsArFlowServiceSpecsServiceType_Type=Integer32
_NbsArFlowServiceSpecsServiceType_Object=MibTableColumn
nbsArFlowServiceSpecsServiceType=_NbsArFlowServiceSpecsServiceType_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,3),_NbsArFlowServiceSpecsServiceType_Type())
nbsArFlowServiceSpecsServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsServiceType.setStatus(_A)
_NbsArFlowServiceSpecsServiceFlowIndex_Type=Integer32
_NbsArFlowServiceSpecsServiceFlowIndex_Object=MibTableColumn
nbsArFlowServiceSpecsServiceFlowIndex=_NbsArFlowServiceSpecsServiceFlowIndex_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,4),_NbsArFlowServiceSpecsServiceFlowIndex_Type())
nbsArFlowServiceSpecsServiceFlowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsServiceFlowIndex.setStatus(_A)
_NbsArFlowServiceSpecsFlowIDExtension_Type=OctetString
_NbsArFlowServiceSpecsFlowIDExtension_Object=MibTableColumn
nbsArFlowServiceSpecsFlowIDExtension=_NbsArFlowServiceSpecsFlowIDExtension_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,5),_NbsArFlowServiceSpecsFlowIDExtension_Type())
nbsArFlowServiceSpecsFlowIDExtension.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsFlowIDExtension.setStatus(_A)
_NbsArFlowServiceSpecsFlowModifier_Type=OctetString
_NbsArFlowServiceSpecsFlowModifier_Object=MibTableColumn
nbsArFlowServiceSpecsFlowModifier=_NbsArFlowServiceSpecsFlowModifier_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,6),_NbsArFlowServiceSpecsFlowModifier_Type())
nbsArFlowServiceSpecsFlowModifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsFlowModifier.setStatus(_A)
_NbsArFlowServiceSpecsFlowSpec_Type=OctetString
_NbsArFlowServiceSpecsFlowSpec_Object=MibTableColumn
nbsArFlowServiceSpecsFlowSpec=_NbsArFlowServiceSpecsFlowSpec_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,7),_NbsArFlowServiceSpecsFlowSpec_Type())
nbsArFlowServiceSpecsFlowSpec.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsFlowSpec.setStatus(_A)
class _NbsArFlowServiceSpecsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_NbsArFlowServiceSpecsAdminStatus_Type.__name__=_C
_NbsArFlowServiceSpecsAdminStatus_Object=MibTableColumn
nbsArFlowServiceSpecsAdminStatus=_NbsArFlowServiceSpecsAdminStatus_Object((1,3,6,1,4,1,629,1,50,10,8,2,1,8),_NbsArFlowServiceSpecsAdminStatus_Type())
nbsArFlowServiceSpecsAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServiceSpecsAdminStatus.setStatus(_A)
_NbsArFlowServicePortTable_Object=MibTable
nbsArFlowServicePortTable=_NbsArFlowServicePortTable_Object((1,3,6,1,4,1,629,1,50,10,8,3))
if mibBuilder.loadTexts:nbsArFlowServicePortTable.setStatus(_A)
_NbsArFlowServicePortEntry_Object=MibTableRow
nbsArFlowServicePortEntry=_NbsArFlowServicePortEntry_Object((1,3,6,1,4,1,629,1,50,10,8,3,1))
nbsArFlowServicePortEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:nbsArFlowServicePortEntry.setStatus(_A)
_NbsArFlowServicePortNumber_Type=Integer32
_NbsArFlowServicePortNumber_Object=MibTableColumn
nbsArFlowServicePortNumber=_NbsArFlowServicePortNumber_Object((1,3,6,1,4,1,629,1,50,10,8,3,1,1),_NbsArFlowServicePortNumber_Type())
nbsArFlowServicePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServicePortNumber.setStatus(_A)
_NbsArFlowServicePortData_Type=OctetString
_NbsArFlowServicePortData_Object=MibTableColumn
nbsArFlowServicePortData=_NbsArFlowServicePortData_Object((1,3,6,1,4,1,629,1,50,10,8,3,1,2),_NbsArFlowServicePortData_Type())
nbsArFlowServicePortData.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServicePortData.setStatus(_A)
class _NbsArFlowServicePortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_NbsArFlowServicePortAdminStatus_Type.__name__=_C
_NbsArFlowServicePortAdminStatus_Object=MibTableColumn
nbsArFlowServicePortAdminStatus=_NbsArFlowServicePortAdminStatus_Object((1,3,6,1,4,1,629,1,50,10,8,3,1,3),_NbsArFlowServicePortAdminStatus_Type())
nbsArFlowServicePortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArFlowServicePortAdminStatus.setStatus(_A)
_NbsArSecFlowFwdStatus_Type=OctetString
_NbsArSecFlowFwdStatus_Object=MibScalar
nbsArSecFlowFwdStatus=_NbsArSecFlowFwdStatus_Object((1,3,6,1,4,1,629,1,50,10,8,4),_NbsArSecFlowFwdStatus_Type())
nbsArSecFlowFwdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsArSecFlowFwdStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'nbSwitchG1Il':nbSwitchG1Il,'nbsAccelerouter':nbsAccelerouter,'nbsArSecFlow':nbsArSecFlow,'nbsArSecFlowTable':nbsArSecFlowTable,'nbsArSecFlowEntry':nbsArSecFlowEntry,_J:nbsArSecFlowIndex,'nbsArSecFlowValid':nbsArSecFlowValid,'nbsArSecFlowState':nbsArSecFlowState,'nbsArSecFlowLastUsedTimestamp':nbsArSecFlowLastUsedTimestamp,'nbsArSecFlowServTypes':nbsArSecFlowServTypes,'nbsArSecFlowServId':nbsArSecFlowServId,'nbsArFlowID':nbsArFlowID,'nbsArFlowQoSSpec':nbsArFlowQoSSpec,'nbsArSecFlowNumOfServices':nbsArSecFlowNumOfServices,'nbsArSecFlowDriverData':nbsArSecFlowDriverData,'nbsArSecFlowActions':nbsArSecFlowActions,'nbsArSecFlowCounters':nbsArSecFlowCounters,'nbsArSecFlowAdminStatus':nbsArSecFlowAdminStatus,'nbsArFlowServiceSpecTable':nbsArFlowServiceSpecTable,'nbsArFlowServiceSpecEntry':nbsArFlowServiceSpecEntry,_K:nbsArFlowServiceFlowIndex,_L:nbsArFlowServiceSpecsServiceId,'nbsArFlowServiceSpecsServiceType':nbsArFlowServiceSpecsServiceType,'nbsArFlowServiceSpecsServiceFlowIndex':nbsArFlowServiceSpecsServiceFlowIndex,'nbsArFlowServiceSpecsFlowIDExtension':nbsArFlowServiceSpecsFlowIDExtension,'nbsArFlowServiceSpecsFlowModifier':nbsArFlowServiceSpecsFlowModifier,'nbsArFlowServiceSpecsFlowSpec':nbsArFlowServiceSpecsFlowSpec,'nbsArFlowServiceSpecsAdminStatus':nbsArFlowServiceSpecsAdminStatus,'nbsArFlowServicePortTable':nbsArFlowServicePortTable,'nbsArFlowServicePortEntry':nbsArFlowServicePortEntry,_M:nbsArFlowServicePortNumber,'nbsArFlowServicePortData':nbsArFlowServicePortData,'nbsArFlowServicePortAdminStatus':nbsArFlowServicePortAdminStatus,'nbsArSecFlowFwdStatus':nbsArSecFlowFwdStatus})