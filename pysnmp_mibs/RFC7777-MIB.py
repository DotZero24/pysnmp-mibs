_n='wfOspfDynNbrAddressLessIndex'
_m='wfOspfDynNbrIpAddr'
_l='wfOspfVirtNbrRtrId'
_k='wfOspfVirtNbrArea'
_j='wfOspfNbrAddressLessIndex'
_i='wfOspfNbrIpAddr'
_h='wfOspfVirtIfNeighbor'
_g='wfOspfVirtIfAreaID'
_f='wfOspfAddressLessIf'
_e='wfOspfIfIpAddress'
_d='wfOspfAreaRangeNet'
_c='wfOspfAreaRangeAreaID'
_b='wfOspfLsdbRouterId'
_a='wfOspfLsdbLSID'
_Z='wfOspfLsdbType'
_Y='wfOspfLsdbAreaId'
_X='wfOspfAreaId'
_W='full'
_V='loading'
_U='exchange'
_T='exchangstart'
_S='twoway'
_R='attempt'
_Q='pointtopoint'
_P='init'
_O='false'
_N='true'
_M='disabled'
_L='enabled'
_K='deleted'
_J='created'
_I='down'
_H='minimum'
_G='defval'
_F='maximum'
_E='RFC7777-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Wellfleet_ObjectIdentity=ObjectIdentity
wellfleet=_Wellfleet_ObjectIdentity((1,3,6,1,4,1,18))
_WfOspfGeneralGroup_ObjectIdentity=ObjectIdentity
wfOspfGeneralGroup=_WfOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,18,3,5,3,2,3,1))
class _WfOspfGeneralDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WfOspfGeneralDelete_Type.__name__=_C
_WfOspfGeneralDelete_Object=MibScalar
wfOspfGeneralDelete=_WfOspfGeneralDelete_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,1),_WfOspfGeneralDelete_Type())
wfOspfGeneralDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfGeneralDelete.setStatus(_A)
class _WfOspfGeneralDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfOspfGeneralDisable_Type.__name__=_C
_WfOspfGeneralDisable_Object=MibScalar
wfOspfGeneralDisable=_WfOspfGeneralDisable_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,2),_WfOspfGeneralDisable_Type())
wfOspfGeneralDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfGeneralDisable.setStatus(_A)
class _WfOspfGeneralState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),(_I,2),(_P,3),('notpresent',4)))
_WfOspfGeneralState_Type.__name__=_C
_WfOspfGeneralState_Object=MibScalar
wfOspfGeneralState=_WfOspfGeneralState_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,3),_WfOspfGeneralState_Type())
wfOspfGeneralState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfGeneralState.setStatus(_A)
_WfOspfRouterId_Type=IpAddress
_WfOspfRouterId_Object=MibScalar
wfOspfRouterId=_WfOspfRouterId_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,4),_WfOspfRouterId_Type())
wfOspfRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfRouterId.setStatus(_A)
_WfOspfVersionNumber_Type=Integer32
_WfOspfVersionNumber_Object=MibScalar
wfOspfVersionNumber=_WfOspfVersionNumber_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,5),_WfOspfVersionNumber_Type())
wfOspfVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVersionNumber.setStatus(_A)
class _WfOspfAreaBdrRtrStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_WfOspfAreaBdrRtrStatus_Type.__name__=_C
_WfOspfAreaBdrRtrStatus_Object=MibScalar
wfOspfAreaBdrRtrStatus=_WfOspfAreaBdrRtrStatus_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,6),_WfOspfAreaBdrRtrStatus_Type())
wfOspfAreaBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAreaBdrRtrStatus.setStatus(_A)
class _WfOspfASBdrRtrStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_WfOspfASBdrRtrStatus_Type.__name__=_C
_WfOspfASBdrRtrStatus_Object=MibScalar
wfOspfASBdrRtrStatus=_WfOspfASBdrRtrStatus_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,7),_WfOspfASBdrRtrStatus_Type())
wfOspfASBdrRtrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfASBdrRtrStatus.setStatus(_A)
class _WfOspfTOSSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_WfOspfTOSSupport_Type.__name__=_C
_WfOspfTOSSupport_Object=MibScalar
wfOspfTOSSupport=_WfOspfTOSSupport_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,8),_WfOspfTOSSupport_Type())
wfOspfTOSSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfTOSSupport.setStatus(_A)
class _WfOspfSpfHoldDown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10)));namedValues=NamedValues(*((_G,1),(_F,10)))
_WfOspfSpfHoldDown_Type.__name__=_C
_WfOspfSpfHoldDown_Object=MibScalar
wfOspfSpfHoldDown=_WfOspfSpfHoldDown_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,9),_WfOspfSpfHoldDown_Type())
wfOspfSpfHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfSpfHoldDown.setStatus(_A)
class _WfOspfSlotMask_Type(Integer32):defaultValue=4261150720;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(4261150720));namedValues=NamedValues(('slotmask',4261150720))
_WfOspfSlotMask_Type.__name__=_C
_WfOspfSlotMask_Object=MibScalar
wfOspfSlotMask=_WfOspfSlotMask_Object((1,3,6,1,4,1,18,3,5,3,2,3,1,10),_WfOspfSlotMask_Type())
wfOspfSlotMask.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfSlotMask.setStatus(_A)
_WfOspfAreaTable_Object=MibTable
wfOspfAreaTable=_WfOspfAreaTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,2))
if mibBuilder.loadTexts:wfOspfAreaTable.setStatus(_A)
_WfOspfAreaEntry_Object=MibTableRow
wfOspfAreaEntry=_WfOspfAreaEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1))
wfOspfAreaEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:wfOspfAreaEntry.setStatus(_A)
class _WfOspfAreaDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WfOspfAreaDelete_Type.__name__=_C
_WfOspfAreaDelete_Object=MibTableColumn
wfOspfAreaDelete=_WfOspfAreaDelete_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,1),_WfOspfAreaDelete_Type())
wfOspfAreaDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfAreaDelete.setStatus(_A)
class _WfOspfAreaDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfOspfAreaDisable_Type.__name__=_C
_WfOspfAreaDisable_Object=MibTableColumn
wfOspfAreaDisable=_WfOspfAreaDisable_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,2),_WfOspfAreaDisable_Type())
wfOspfAreaDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfAreaDisable.setStatus(_A)
class _WfOspfAreaState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_WfOspfAreaState_Type.__name__=_C
_WfOspfAreaState_Object=MibTableColumn
wfOspfAreaState=_WfOspfAreaState_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,3),_WfOspfAreaState_Type())
wfOspfAreaState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAreaState.setStatus(_A)
_WfOspfAreaId_Type=IpAddress
_WfOspfAreaId_Object=MibTableColumn
wfOspfAreaId=_WfOspfAreaId_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,4),_WfOspfAreaId_Type())
wfOspfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAreaId.setStatus(_A)
class _WfOspfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nopassword',1),('simplepassword',2)))
_WfOspfAuthType_Type.__name__=_C
_WfOspfAuthType_Object=MibTableColumn
wfOspfAuthType=_WfOspfAuthType_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,5),_WfOspfAuthType_Type())
wfOspfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfAuthType.setStatus(_A)
class _WfOspfImportASExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_WfOspfImportASExtern_Type.__name__=_C
_WfOspfImportASExtern_Object=MibTableColumn
wfOspfImportASExtern=_WfOspfImportASExtern_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,6),_WfOspfImportASExtern_Type())
wfOspfImportASExtern.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfImportASExtern.setStatus(_A)
class _WfOspfStubMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,16777215)));namedValues=NamedValues(*((_H,1),(_F,16777215)))
_WfOspfStubMetric_Type.__name__=_C
_WfOspfStubMetric_Object=MibTableColumn
wfOspfStubMetric=_WfOspfStubMetric_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,7),_WfOspfStubMetric_Type())
wfOspfStubMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfStubMetric.setStatus(_A)
class _WfOspfImportSum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_WfOspfImportSum_Type.__name__=_C
_WfOspfImportSum_Object=MibTableColumn
wfOspfImportSum=_WfOspfImportSum_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,8),_WfOspfImportSum_Type())
wfOspfImportSum.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfImportSum.setStatus(_A)
_WfOspfSpfCnt_Type=Counter32
_WfOspfSpfCnt_Object=MibTableColumn
wfOspfSpfCnt=_WfOspfSpfCnt_Object((1,3,6,1,4,1,18,3,5,3,2,3,2,1,9),_WfOspfSpfCnt_Type())
wfOspfSpfCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfSpfCnt.setStatus(_A)
_WfOspfLsdbTable_Object=MibTable
wfOspfLsdbTable=_WfOspfLsdbTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,3))
if mibBuilder.loadTexts:wfOspfLsdbTable.setStatus(_A)
_WfOspfLsdbEntry_Object=MibTableRow
wfOspfLsdbEntry=_WfOspfLsdbEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1))
wfOspfLsdbEntry.setIndexNames((0,_E,_Y),(0,_E,_Z),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:wfOspfLsdbEntry.setStatus(_A)
_WfOspfLsdbAreaId_Type=IpAddress
_WfOspfLsdbAreaId_Object=MibTableColumn
wfOspfLsdbAreaId=_WfOspfLsdbAreaId_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,1),_WfOspfLsdbAreaId_Type())
wfOspfLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbAreaId.setStatus(_A)
class _WfOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('routerlink',1),('networklink',2),('summarylink',3),('assummarylink',4),('asexternallink',5)))
_WfOspfLsdbType_Type.__name__=_C
_WfOspfLsdbType_Object=MibTableColumn
wfOspfLsdbType=_WfOspfLsdbType_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,2),_WfOspfLsdbType_Type())
wfOspfLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbType.setStatus(_A)
_WfOspfLsdbLSID_Type=IpAddress
_WfOspfLsdbLSID_Object=MibTableColumn
wfOspfLsdbLSID=_WfOspfLsdbLSID_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,3),_WfOspfLsdbLSID_Type())
wfOspfLsdbLSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbLSID.setStatus(_A)
_WfOspfLsdbRouterId_Type=IpAddress
_WfOspfLsdbRouterId_Object=MibTableColumn
wfOspfLsdbRouterId=_WfOspfLsdbRouterId_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,4),_WfOspfLsdbRouterId_Type())
wfOspfLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbRouterId.setStatus(_A)
_WfOspfLsdbSequence_Type=Integer32
_WfOspfLsdbSequence_Object=MibTableColumn
wfOspfLsdbSequence=_WfOspfLsdbSequence_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,5),_WfOspfLsdbSequence_Type())
wfOspfLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbSequence.setStatus(_A)
class _WfOspfLsdbAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3600));namedValues=NamedValues(('lsdbmaxage',3600))
_WfOspfLsdbAge_Type.__name__=_C
_WfOspfLsdbAge_Object=MibTableColumn
wfOspfLsdbAge=_WfOspfLsdbAge_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,6),_WfOspfLsdbAge_Type())
wfOspfLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbAge.setStatus(_A)
_WfOspfLsdbChecksum_Type=Integer32
_WfOspfLsdbChecksum_Object=MibTableColumn
wfOspfLsdbChecksum=_WfOspfLsdbChecksum_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,7),_WfOspfLsdbChecksum_Type())
wfOspfLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbChecksum.setStatus(_A)
_WfOspfLsdbAdvLen_Type=Integer32
_WfOspfLsdbAdvLen_Object=MibTableColumn
wfOspfLsdbAdvLen=_WfOspfLsdbAdvLen_Object((1,3,6,1,4,1,18,3,5,3,2,3,3,1,8),_WfOspfLsdbAdvLen_Type())
wfOspfLsdbAdvLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfLsdbAdvLen.setStatus(_A)
_WfOspfAreaRangeTable_Object=MibTable
wfOspfAreaRangeTable=_WfOspfAreaRangeTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,4))
if mibBuilder.loadTexts:wfOspfAreaRangeTable.setStatus(_A)
_WfOspfAreaRangeEntry_Object=MibTableRow
wfOspfAreaRangeEntry=_WfOspfAreaRangeEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1))
wfOspfAreaRangeEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:wfOspfAreaRangeEntry.setStatus(_A)
class _WfOspfAreaRangeDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WfOspfAreaRangeDelete_Type.__name__=_C
_WfOspfAreaRangeDelete_Object=MibTableColumn
wfOspfAreaRangeDelete=_WfOspfAreaRangeDelete_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1,1),_WfOspfAreaRangeDelete_Type())
wfOspfAreaRangeDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfAreaRangeDelete.setStatus(_A)
class _WfOspfAreaRangeDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfOspfAreaRangeDisable_Type.__name__=_C
_WfOspfAreaRangeDisable_Object=MibTableColumn
wfOspfAreaRangeDisable=_WfOspfAreaRangeDisable_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1,2),_WfOspfAreaRangeDisable_Type())
wfOspfAreaRangeDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfAreaRangeDisable.setStatus(_A)
class _WfOspfAreaRangeState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_WfOspfAreaRangeState_Type.__name__=_C
_WfOspfAreaRangeState_Object=MibTableColumn
wfOspfAreaRangeState=_WfOspfAreaRangeState_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1,3),_WfOspfAreaRangeState_Type())
wfOspfAreaRangeState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAreaRangeState.setStatus(_A)
_WfOspfAreaRangeAreaID_Type=IpAddress
_WfOspfAreaRangeAreaID_Object=MibTableColumn
wfOspfAreaRangeAreaID=_WfOspfAreaRangeAreaID_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1,4),_WfOspfAreaRangeAreaID_Type())
wfOspfAreaRangeAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAreaRangeAreaID.setStatus(_A)
_WfOspfAreaRangeNet_Type=IpAddress
_WfOspfAreaRangeNet_Object=MibTableColumn
wfOspfAreaRangeNet=_WfOspfAreaRangeNet_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1,5),_WfOspfAreaRangeNet_Type())
wfOspfAreaRangeNet.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAreaRangeNet.setStatus(_A)
_WfOspfAreaRangeMask_Type=IpAddress
_WfOspfAreaRangeMask_Object=MibTableColumn
wfOspfAreaRangeMask=_WfOspfAreaRangeMask_Object((1,3,6,1,4,1,18,3,5,3,2,3,4,1,6),_WfOspfAreaRangeMask_Type())
wfOspfAreaRangeMask.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfAreaRangeMask.setStatus(_A)
_WfOspfIfTable_Object=MibTable
wfOspfIfTable=_WfOspfIfTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,5))
if mibBuilder.loadTexts:wfOspfIfTable.setStatus(_A)
_WfOspfIfEntry_Object=MibTableRow
wfOspfIfEntry=_WfOspfIfEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1))
wfOspfIfEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:wfOspfIfEntry.setStatus(_A)
class _WfOspfIfDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WfOspfIfDelete_Type.__name__=_C
_WfOspfIfDelete_Object=MibTableColumn
wfOspfIfDelete=_WfOspfIfDelete_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,1),_WfOspfIfDelete_Type())
wfOspfIfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfDelete.setStatus(_A)
class _WfOspfIfDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfOspfIfDisable_Type.__name__=_C
_WfOspfIfDisable_Object=MibTableColumn
wfOspfIfDisable=_WfOspfIfDisable_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,2),_WfOspfIfDisable_Type())
wfOspfIfDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfDisable.setStatus(_A)
class _WfOspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),('loopback',2),('waiting',3),(_Q,4),('designatedrouter',5),('backupdesignatedrouter',6),('otherdesignatedrouter',7)))
_WfOspfIfState_Type.__name__=_C
_WfOspfIfState_Object=MibTableColumn
wfOspfIfState=_WfOspfIfState_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,3),_WfOspfIfState_Type())
wfOspfIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfState.setStatus(_A)
_WfOspfIfIpAddress_Type=IpAddress
_WfOspfIfIpAddress_Object=MibTableColumn
wfOspfIfIpAddress=_WfOspfIfIpAddress_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,4),_WfOspfIfIpAddress_Type())
wfOspfIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfIpAddress.setStatus(_A)
_WfOspfAddressLessIf_Type=Integer32
_WfOspfAddressLessIf_Object=MibTableColumn
wfOspfAddressLessIf=_WfOspfAddressLessIf_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,5),_WfOspfAddressLessIf_Type())
wfOspfAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfAddressLessIf.setStatus(_A)
_WfOspfIfAreaId_Type=IpAddress
_WfOspfIfAreaId_Object=MibTableColumn
wfOspfIfAreaId=_WfOspfIfAreaId_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,6),_WfOspfIfAreaId_Type())
wfOspfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfAreaId.setStatus(_A)
class _WfOspfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_Q,3)))
_WfOspfIfType_Type.__name__=_C
_WfOspfIfType_Object=MibTableColumn
wfOspfIfType=_WfOspfIfType_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,7),_WfOspfIfType_Type())
wfOspfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfType.setStatus(_A)
class _WfOspfIfRtrPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_G,1),(_F,255)))
_WfOspfIfRtrPriority_Type.__name__=_C
_WfOspfIfRtrPriority_Object=MibTableColumn
wfOspfIfRtrPriority=_WfOspfIfRtrPriority_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,8),_WfOspfIfRtrPriority_Type())
wfOspfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfRtrPriority.setStatus(_A)
class _WfOspfIfTransitDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3600)));namedValues=NamedValues(*((_H,1),(_F,3600)))
_WfOspfIfTransitDelay_Type.__name__=_C
_WfOspfIfTransitDelay_Object=MibTableColumn
wfOspfIfTransitDelay=_WfOspfIfTransitDelay_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,9),_WfOspfIfTransitDelay_Type())
wfOspfIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfTransitDelay.setStatus(_A)
class _WfOspfIfRetransInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,3600)));namedValues=NamedValues(*((_H,1),(_G,5),(_F,3600)))
_WfOspfIfRetransInterval_Type.__name__=_C
_WfOspfIfRetransInterval_Object=MibTableColumn
wfOspfIfRetransInterval=_WfOspfIfRetransInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,10),_WfOspfIfRetransInterval_Type())
wfOspfIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfRetransInterval.setStatus(_A)
class _WfOspfIfHelloInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,65535)));namedValues=NamedValues(*((_H,1),(_G,10),(_F,65535)))
_WfOspfIfHelloInterval_Type.__name__=_C
_WfOspfIfHelloInterval_Object=MibTableColumn
wfOspfIfHelloInterval=_WfOspfIfHelloInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,11),_WfOspfIfHelloInterval_Type())
wfOspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfHelloInterval.setStatus(_A)
class _WfOspfIfRtrDeadInterval_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,40,2147483647)));namedValues=NamedValues(*((_H,1),(_G,40),(_F,2147483647)))
_WfOspfIfRtrDeadInterval_Type.__name__=_C
_WfOspfIfRtrDeadInterval_Object=MibTableColumn
wfOspfIfRtrDeadInterval=_WfOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,12),_WfOspfIfRtrDeadInterval_Type())
wfOspfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfRtrDeadInterval.setStatus(_A)
class _WfOspfIfPollInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,120,2147483647)));namedValues=NamedValues(*((_H,1),(_G,120),(_F,2147483647)))
_WfOspfIfPollInterval_Type.__name__=_C
_WfOspfIfPollInterval_Object=MibTableColumn
wfOspfIfPollInterval=_WfOspfIfPollInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,13),_WfOspfIfPollInterval_Type())
wfOspfIfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfPollInterval.setStatus(_A)
_WfOspfIfDesignatedRouter_Type=IpAddress
_WfOspfIfDesignatedRouter_Object=MibTableColumn
wfOspfIfDesignatedRouter=_WfOspfIfDesignatedRouter_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,14),_WfOspfIfDesignatedRouter_Type())
wfOspfIfDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfDesignatedRouter.setStatus(_A)
_WfOspfIfBackupDesignatedRouter_Type=IpAddress
_WfOspfIfBackupDesignatedRouter_Object=MibTableColumn
wfOspfIfBackupDesignatedRouter=_WfOspfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,15),_WfOspfIfBackupDesignatedRouter_Type())
wfOspfIfBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfBackupDesignatedRouter.setStatus(_A)
class _WfOspfIfMetricCost_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_H,1),(_F,65535)))
_WfOspfIfMetricCost_Type.__name__=_C
_WfOspfIfMetricCost_Object=MibTableColumn
wfOspfIfMetricCost=_WfOspfIfMetricCost_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,16),_WfOspfIfMetricCost_Type())
wfOspfIfMetricCost.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfMetricCost.setStatus(_A)
_WfOspfIfAuthKey_Type=OctetString
_WfOspfIfAuthKey_Object=MibTableColumn
wfOspfIfAuthKey=_WfOspfIfAuthKey_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,17),_WfOspfIfAuthKey_Type())
wfOspfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfIfAuthKey.setStatus(_A)
_WfOspfIfTxHellos_Type=Counter32
_WfOspfIfTxHellos_Object=MibTableColumn
wfOspfIfTxHellos=_WfOspfIfTxHellos_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,18),_WfOspfIfTxHellos_Type())
wfOspfIfTxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfTxHellos.setStatus(_A)
_WfOspfIfTxDBDescripts_Type=Counter32
_WfOspfIfTxDBDescripts_Object=MibTableColumn
wfOspfIfTxDBDescripts=_WfOspfIfTxDBDescripts_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,19),_WfOspfIfTxDBDescripts_Type())
wfOspfIfTxDBDescripts.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfTxDBDescripts.setStatus(_A)
_WfOspfIfTxLinkStateReqs_Type=Counter32
_WfOspfIfTxLinkStateReqs_Object=MibTableColumn
wfOspfIfTxLinkStateReqs=_WfOspfIfTxLinkStateReqs_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,20),_WfOspfIfTxLinkStateReqs_Type())
wfOspfIfTxLinkStateReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfTxLinkStateReqs.setStatus(_A)
_WfOspfIfTxLinkStateUpds_Type=Counter32
_WfOspfIfTxLinkStateUpds_Object=MibTableColumn
wfOspfIfTxLinkStateUpds=_WfOspfIfTxLinkStateUpds_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,21),_WfOspfIfTxLinkStateUpds_Type())
wfOspfIfTxLinkStateUpds.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfTxLinkStateUpds.setStatus(_A)
_WfOspfIfTxLinkStateAcks_Type=Counter32
_WfOspfIfTxLinkStateAcks_Object=MibTableColumn
wfOspfIfTxLinkStateAcks=_WfOspfIfTxLinkStateAcks_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,22),_WfOspfIfTxLinkStateAcks_Type())
wfOspfIfTxLinkStateAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfTxLinkStateAcks.setStatus(_A)
_WfOspfIfRxHellos_Type=Counter32
_WfOspfIfRxHellos_Object=MibTableColumn
wfOspfIfRxHellos=_WfOspfIfRxHellos_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,23),_WfOspfIfRxHellos_Type())
wfOspfIfRxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfRxHellos.setStatus(_A)
_WfOspfIfRxDBDescripts_Type=Counter32
_WfOspfIfRxDBDescripts_Object=MibTableColumn
wfOspfIfRxDBDescripts=_WfOspfIfRxDBDescripts_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,24),_WfOspfIfRxDBDescripts_Type())
wfOspfIfRxDBDescripts.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfRxDBDescripts.setStatus(_A)
_WfOspfIfRxLinkStateReqs_Type=Counter32
_WfOspfIfRxLinkStateReqs_Object=MibTableColumn
wfOspfIfRxLinkStateReqs=_WfOspfIfRxLinkStateReqs_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,25),_WfOspfIfRxLinkStateReqs_Type())
wfOspfIfRxLinkStateReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfRxLinkStateReqs.setStatus(_A)
_WfOspfIfRxLinkStateUpds_Type=Counter32
_WfOspfIfRxLinkStateUpds_Object=MibTableColumn
wfOspfIfRxLinkStateUpds=_WfOspfIfRxLinkStateUpds_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,26),_WfOspfIfRxLinkStateUpds_Type())
wfOspfIfRxLinkStateUpds.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfRxLinkStateUpds.setStatus(_A)
_WfOspfIfRxLinkStateAcks_Type=Counter32
_WfOspfIfRxLinkStateAcks_Object=MibTableColumn
wfOspfIfRxLinkStateAcks=_WfOspfIfRxLinkStateAcks_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,27),_WfOspfIfRxLinkStateAcks_Type())
wfOspfIfRxLinkStateAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfRxLinkStateAcks.setStatus(_A)
_WfOspfIfDrops_Type=Counter32
_WfOspfIfDrops_Object=MibTableColumn
wfOspfIfDrops=_WfOspfIfDrops_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,28),_WfOspfIfDrops_Type())
wfOspfIfDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfIfDrops.setStatus(_A)
class _WfOspfMtuSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10000)));namedValues=NamedValues(*((_G,1),('min',2),(_F,10000)))
_WfOspfMtuSize_Type.__name__=_C
_WfOspfMtuSize_Object=MibTableColumn
wfOspfMtuSize=_WfOspfMtuSize_Object((1,3,6,1,4,1,18,3,5,3,2,3,5,1,29),_WfOspfMtuSize_Type())
wfOspfMtuSize.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfMtuSize.setStatus(_A)
_WfOspfVirtIfTable_Object=MibTable
wfOspfVirtIfTable=_WfOspfVirtIfTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,6))
if mibBuilder.loadTexts:wfOspfVirtIfTable.setStatus(_A)
_WfOspfVirtIfEntry_Object=MibTableRow
wfOspfVirtIfEntry=_WfOspfVirtIfEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1))
wfOspfVirtIfEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:wfOspfVirtIfEntry.setStatus(_A)
class _WfOspfVirtIfDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WfOspfVirtIfDelete_Type.__name__=_C
_WfOspfVirtIfDelete_Object=MibTableColumn
wfOspfVirtIfDelete=_WfOspfVirtIfDelete_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,1),_WfOspfVirtIfDelete_Type())
wfOspfVirtIfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfDelete.setStatus(_A)
class _WfOspfVirtIfDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfOspfVirtIfDisable_Type.__name__=_C
_WfOspfVirtIfDisable_Object=MibTableColumn
wfOspfVirtIfDisable=_WfOspfVirtIfDisable_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,2),_WfOspfVirtIfDisable_Type())
wfOspfVirtIfDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfDisable.setStatus(_A)
class _WfOspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_I,1),(_Q,4)))
_WfOspfVirtIfState_Type.__name__=_C
_WfOspfVirtIfState_Object=MibTableColumn
wfOspfVirtIfState=_WfOspfVirtIfState_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,3),_WfOspfVirtIfState_Type())
wfOspfVirtIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfState.setStatus(_A)
_WfOspfVirtIfAreaID_Type=IpAddress
_WfOspfVirtIfAreaID_Object=MibTableColumn
wfOspfVirtIfAreaID=_WfOspfVirtIfAreaID_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,4),_WfOspfVirtIfAreaID_Type())
wfOspfVirtIfAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfAreaID.setStatus(_A)
_WfOspfVirtIfNeighbor_Type=IpAddress
_WfOspfVirtIfNeighbor_Object=MibTableColumn
wfOspfVirtIfNeighbor=_WfOspfVirtIfNeighbor_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,5),_WfOspfVirtIfNeighbor_Type())
wfOspfVirtIfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfNeighbor.setStatus(_A)
class _WfOspfVirtIfTransitDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3600)));namedValues=NamedValues(*((_H,1),(_F,3600)))
_WfOspfVirtIfTransitDelay_Type.__name__=_C
_WfOspfVirtIfTransitDelay_Object=MibTableColumn
wfOspfVirtIfTransitDelay=_WfOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,6),_WfOspfVirtIfTransitDelay_Type())
wfOspfVirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfTransitDelay.setStatus(_A)
class _WfOspfVirtIfRetransInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,3600)));namedValues=NamedValues(*((_H,1),(_G,5),(_F,3600)))
_WfOspfVirtIfRetransInterval_Type.__name__=_C
_WfOspfVirtIfRetransInterval_Object=MibTableColumn
wfOspfVirtIfRetransInterval=_WfOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,7),_WfOspfVirtIfRetransInterval_Type())
wfOspfVirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfRetransInterval.setStatus(_A)
class _WfOspfVirtIfHelloInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,15,65535)));namedValues=NamedValues(*((_H,1),(_G,15),(_F,65535)))
_WfOspfVirtIfHelloInterval_Type.__name__=_C
_WfOspfVirtIfHelloInterval_Object=MibTableColumn
wfOspfVirtIfHelloInterval=_WfOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,8),_WfOspfVirtIfHelloInterval_Type())
wfOspfVirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfHelloInterval.setStatus(_A)
class _WfOspfVirtIfRtrDeadInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,60,2147483647)));namedValues=NamedValues(*((_H,1),(_G,60),(_F,2147483647)))
_WfOspfVirtIfRtrDeadInterval_Type.__name__=_C
_WfOspfVirtIfRtrDeadInterval_Object=MibTableColumn
wfOspfVirtIfRtrDeadInterval=_WfOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,9),_WfOspfVirtIfRtrDeadInterval_Type())
wfOspfVirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfRtrDeadInterval.setStatus(_A)
_WfOspfVirtIfAuthKey_Type=OctetString
_WfOspfVirtIfAuthKey_Object=MibTableColumn
wfOspfVirtIfAuthKey=_WfOspfVirtIfAuthKey_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,10),_WfOspfVirtIfAuthKey_Type())
wfOspfVirtIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfVirtIfAuthKey.setStatus(_A)
_WfOspfVirtIfTxHellos_Type=Counter32
_WfOspfVirtIfTxHellos_Object=MibTableColumn
wfOspfVirtIfTxHellos=_WfOspfVirtIfTxHellos_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,11),_WfOspfVirtIfTxHellos_Type())
wfOspfVirtIfTxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfTxHellos.setStatus(_A)
_WfOspfVirtIfTxDBDescripts_Type=Counter32
_WfOspfVirtIfTxDBDescripts_Object=MibTableColumn
wfOspfVirtIfTxDBDescripts=_WfOspfVirtIfTxDBDescripts_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,12),_WfOspfVirtIfTxDBDescripts_Type())
wfOspfVirtIfTxDBDescripts.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfTxDBDescripts.setStatus(_A)
_WfOspfVirtIfTxLinkStateReqs_Type=Counter32
_WfOspfVirtIfTxLinkStateReqs_Object=MibTableColumn
wfOspfVirtIfTxLinkStateReqs=_WfOspfVirtIfTxLinkStateReqs_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,13),_WfOspfVirtIfTxLinkStateReqs_Type())
wfOspfVirtIfTxLinkStateReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfTxLinkStateReqs.setStatus(_A)
_WfOspfVirtIfTxLinkStateUpds_Type=Counter32
_WfOspfVirtIfTxLinkStateUpds_Object=MibTableColumn
wfOspfVirtIfTxLinkStateUpds=_WfOspfVirtIfTxLinkStateUpds_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,14),_WfOspfVirtIfTxLinkStateUpds_Type())
wfOspfVirtIfTxLinkStateUpds.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfTxLinkStateUpds.setStatus(_A)
_WfOspfVirtIfTxLinkStateAcks_Type=Counter32
_WfOspfVirtIfTxLinkStateAcks_Object=MibTableColumn
wfOspfVirtIfTxLinkStateAcks=_WfOspfVirtIfTxLinkStateAcks_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,15),_WfOspfVirtIfTxLinkStateAcks_Type())
wfOspfVirtIfTxLinkStateAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfTxLinkStateAcks.setStatus(_A)
_WfOspfVirtIfRxHellos_Type=Counter32
_WfOspfVirtIfRxHellos_Object=MibTableColumn
wfOspfVirtIfRxHellos=_WfOspfVirtIfRxHellos_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,16),_WfOspfVirtIfRxHellos_Type())
wfOspfVirtIfRxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfRxHellos.setStatus(_A)
_WfOspfVirtIfRxDBDescripts_Type=Counter32
_WfOspfVirtIfRxDBDescripts_Object=MibTableColumn
wfOspfVirtIfRxDBDescripts=_WfOspfVirtIfRxDBDescripts_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,17),_WfOspfVirtIfRxDBDescripts_Type())
wfOspfVirtIfRxDBDescripts.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfRxDBDescripts.setStatus(_A)
_WfOspfVirtIfRxLinkStateReqs_Type=Counter32
_WfOspfVirtIfRxLinkStateReqs_Object=MibTableColumn
wfOspfVirtIfRxLinkStateReqs=_WfOspfVirtIfRxLinkStateReqs_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,18),_WfOspfVirtIfRxLinkStateReqs_Type())
wfOspfVirtIfRxLinkStateReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfRxLinkStateReqs.setStatus(_A)
_WfOspfVirtIfRxLinkStateUpds_Type=Counter32
_WfOspfVirtIfRxLinkStateUpds_Object=MibTableColumn
wfOspfVirtIfRxLinkStateUpds=_WfOspfVirtIfRxLinkStateUpds_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,19),_WfOspfVirtIfRxLinkStateUpds_Type())
wfOspfVirtIfRxLinkStateUpds.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfRxLinkStateUpds.setStatus(_A)
_WfOspfVirtIfRxLinkStateAcks_Type=Counter32
_WfOspfVirtIfRxLinkStateAcks_Object=MibTableColumn
wfOspfVirtIfRxLinkStateAcks=_WfOspfVirtIfRxLinkStateAcks_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,20),_WfOspfVirtIfRxLinkStateAcks_Type())
wfOspfVirtIfRxLinkStateAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfRxLinkStateAcks.setStatus(_A)
_WfOspfVirtIfDrops_Type=Counter32
_WfOspfVirtIfDrops_Object=MibTableColumn
wfOspfVirtIfDrops=_WfOspfVirtIfDrops_Object((1,3,6,1,4,1,18,3,5,3,2,3,6,1,21),_WfOspfVirtIfDrops_Type())
wfOspfVirtIfDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtIfDrops.setStatus(_A)
_WfOspfNbrTable_Object=MibTable
wfOspfNbrTable=_WfOspfNbrTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,7))
if mibBuilder.loadTexts:wfOspfNbrTable.setStatus(_A)
_WfOspfNbrEntry_Object=MibTableRow
wfOspfNbrEntry=_WfOspfNbrEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1))
wfOspfNbrEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:wfOspfNbrEntry.setStatus(_A)
class _WfOspfNbrDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WfOspfNbrDelete_Type.__name__=_C
_WfOspfNbrDelete_Object=MibTableColumn
wfOspfNbrDelete=_WfOspfNbrDelete_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,1),_WfOspfNbrDelete_Type())
wfOspfNbrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfNbrDelete.setStatus(_A)
class _WfOspfNbrDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfOspfNbrDisable_Type.__name__=_C
_WfOspfNbrDisable_Object=MibTableColumn
wfOspfNbrDisable=_WfOspfNbrDisable_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,2),_WfOspfNbrDisable_Type())
wfOspfNbrDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfNbrDisable.setStatus(_A)
class _WfOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_R,2),(_P,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8)))
_WfOspfNbrState_Type.__name__=_C
_WfOspfNbrState_Object=MibTableColumn
wfOspfNbrState=_WfOspfNbrState_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,3),_WfOspfNbrState_Type())
wfOspfNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrState.setStatus(_A)
_WfOspfNbrIpAddr_Type=IpAddress
_WfOspfNbrIpAddr_Object=MibTableColumn
wfOspfNbrIpAddr=_WfOspfNbrIpAddr_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,4),_WfOspfNbrIpAddr_Type())
wfOspfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrIpAddr.setStatus(_A)
_WfOspfNbrIfAddr_Type=IpAddress
_WfOspfNbrIfAddr_Object=MibTableColumn
wfOspfNbrIfAddr=_WfOspfNbrIfAddr_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,5),_WfOspfNbrIfAddr_Type())
wfOspfNbrIfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfNbrIfAddr.setStatus(_A)
_WfOspfNbrAddressLessIndex_Type=Integer32
_WfOspfNbrAddressLessIndex_Object=MibTableColumn
wfOspfNbrAddressLessIndex=_WfOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,6),_WfOspfNbrAddressLessIndex_Type())
wfOspfNbrAddressLessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrAddressLessIndex.setStatus(_A)
_WfOspfNbrRtrId_Type=IpAddress
_WfOspfNbrRtrId_Object=MibTableColumn
wfOspfNbrRtrId=_WfOspfNbrRtrId_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,7),_WfOspfNbrRtrId_Type())
wfOspfNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrRtrId.setStatus(_A)
_WfOspfNbrOptions_Type=Integer32
_WfOspfNbrOptions_Object=MibTableColumn
wfOspfNbrOptions=_WfOspfNbrOptions_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,8),_WfOspfNbrOptions_Type())
wfOspfNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrOptions.setStatus(_A)
class _WfOspfNbrPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_G,1),(_F,255)))
_WfOspfNbrPriority_Type.__name__=_C
_WfOspfNbrPriority_Object=MibTableColumn
wfOspfNbrPriority=_WfOspfNbrPriority_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,9),_WfOspfNbrPriority_Type())
wfOspfNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wfOspfNbrPriority.setStatus(_A)
_WfOspfNbrEvents_Type=Counter32
_WfOspfNbrEvents_Object=MibTableColumn
wfOspfNbrEvents=_WfOspfNbrEvents_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,10),_WfOspfNbrEvents_Type())
wfOspfNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrEvents.setStatus(_A)
_WfOspfNbrLSRetransQLen_Type=Gauge32
_WfOspfNbrLSRetransQLen_Object=MibTableColumn
wfOspfNbrLSRetransQLen=_WfOspfNbrLSRetransQLen_Object((1,3,6,1,4,1,18,3,5,3,2,3,7,1,11),_WfOspfNbrLSRetransQLen_Type())
wfOspfNbrLSRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfNbrLSRetransQLen.setStatus(_A)
_WfOspfVirtNbrTable_Object=MibTable
wfOspfVirtNbrTable=_WfOspfVirtNbrTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,8))
if mibBuilder.loadTexts:wfOspfVirtNbrTable.setStatus(_A)
_WfOspfVirtNbrEntry_Object=MibTableRow
wfOspfVirtNbrEntry=_WfOspfVirtNbrEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1))
wfOspfVirtNbrEntry.setIndexNames((0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:wfOspfVirtNbrEntry.setStatus(_A)
_WfOspfVirtNbrArea_Type=IpAddress
_WfOspfVirtNbrArea_Object=MibTableColumn
wfOspfVirtNbrArea=_WfOspfVirtNbrArea_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,1),_WfOspfVirtNbrArea_Type())
wfOspfVirtNbrArea.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrArea.setStatus(_A)
_WfOspfVirtNbrRtrId_Type=IpAddress
_WfOspfVirtNbrRtrId_Object=MibTableColumn
wfOspfVirtNbrRtrId=_WfOspfVirtNbrRtrId_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,2),_WfOspfVirtNbrRtrId_Type())
wfOspfVirtNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrRtrId.setStatus(_A)
_WfOspfVirtNbrIpAddr_Type=IpAddress
_WfOspfVirtNbrIpAddr_Object=MibTableColumn
wfOspfVirtNbrIpAddr=_WfOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,3),_WfOspfVirtNbrIpAddr_Type())
wfOspfVirtNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrIpAddr.setStatus(_A)
_WfOspfVirtNbrOptions_Type=Integer32
_WfOspfVirtNbrOptions_Object=MibTableColumn
wfOspfVirtNbrOptions=_WfOspfVirtNbrOptions_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,4),_WfOspfVirtNbrOptions_Type())
wfOspfVirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrOptions.setStatus(_A)
class _WfOspfVirtNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_R,2),(_P,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8)))
_WfOspfVirtNbrState_Type.__name__=_C
_WfOspfVirtNbrState_Object=MibTableColumn
wfOspfVirtNbrState=_WfOspfVirtNbrState_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,5),_WfOspfVirtNbrState_Type())
wfOspfVirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrState.setStatus(_A)
_WfOspfVirtNbrEvents_Type=Counter32
_WfOspfVirtNbrEvents_Object=MibTableColumn
wfOspfVirtNbrEvents=_WfOspfVirtNbrEvents_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,6),_WfOspfVirtNbrEvents_Type())
wfOspfVirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrEvents.setStatus(_A)
_WfOspfVirtNbrLSRetransQLen_Type=Gauge32
_WfOspfVirtNbrLSRetransQLen_Object=MibTableColumn
wfOspfVirtNbrLSRetransQLen=_WfOspfVirtNbrLSRetransQLen_Object((1,3,6,1,4,1,18,3,5,3,2,3,8,1,7),_WfOspfVirtNbrLSRetransQLen_Type())
wfOspfVirtNbrLSRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfVirtNbrLSRetransQLen.setStatus(_A)
_WfOspfDynNbrTable_Object=MibTable
wfOspfDynNbrTable=_WfOspfDynNbrTable_Object((1,3,6,1,4,1,18,3,5,3,2,3,9))
if mibBuilder.loadTexts:wfOspfDynNbrTable.setStatus(_A)
_WfOspfDynNbrEntry_Object=MibTableRow
wfOspfDynNbrEntry=_WfOspfDynNbrEntry_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1))
wfOspfDynNbrEntry.setIndexNames((0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:wfOspfDynNbrEntry.setStatus(_A)
class _WfOspfDynNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_R,2),(_P,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8)))
_WfOspfDynNbrState_Type.__name__=_C
_WfOspfDynNbrState_Object=MibTableColumn
wfOspfDynNbrState=_WfOspfDynNbrState_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,1),_WfOspfDynNbrState_Type())
wfOspfDynNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrState.setStatus(_A)
_WfOspfDynNbrIpAddr_Type=IpAddress
_WfOspfDynNbrIpAddr_Object=MibTableColumn
wfOspfDynNbrIpAddr=_WfOspfDynNbrIpAddr_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,2),_WfOspfDynNbrIpAddr_Type())
wfOspfDynNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrIpAddr.setStatus(_A)
_WfOspfDynNbrIfAddr_Type=IpAddress
_WfOspfDynNbrIfAddr_Object=MibTableColumn
wfOspfDynNbrIfAddr=_WfOspfDynNbrIfAddr_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,3),_WfOspfDynNbrIfAddr_Type())
wfOspfDynNbrIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrIfAddr.setStatus(_A)
_WfOspfDynNbrAddressLessIndex_Type=Integer32
_WfOspfDynNbrAddressLessIndex_Object=MibTableColumn
wfOspfDynNbrAddressLessIndex=_WfOspfDynNbrAddressLessIndex_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,4),_WfOspfDynNbrAddressLessIndex_Type())
wfOspfDynNbrAddressLessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrAddressLessIndex.setStatus(_A)
_WfOspfDynNbrRtrId_Type=IpAddress
_WfOspfDynNbrRtrId_Object=MibTableColumn
wfOspfDynNbrRtrId=_WfOspfDynNbrRtrId_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,5),_WfOspfDynNbrRtrId_Type())
wfOspfDynNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrRtrId.setStatus(_A)
_WfOspfDynNbrOptions_Type=Integer32
_WfOspfDynNbrOptions_Object=MibTableColumn
wfOspfDynNbrOptions=_WfOspfDynNbrOptions_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,6),_WfOspfDynNbrOptions_Type())
wfOspfDynNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrOptions.setStatus(_A)
_WfOspfDynNbrPriority_Type=Integer32
_WfOspfDynNbrPriority_Object=MibTableColumn
wfOspfDynNbrPriority=_WfOspfDynNbrPriority_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,7),_WfOspfDynNbrPriority_Type())
wfOspfDynNbrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrPriority.setStatus(_A)
_WfOspfDynNbrEvents_Type=Counter32
_WfOspfDynNbrEvents_Object=MibTableColumn
wfOspfDynNbrEvents=_WfOspfDynNbrEvents_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,8),_WfOspfDynNbrEvents_Type())
wfOspfDynNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrEvents.setStatus(_A)
_WfOspfDynNbrLSRetransQLen_Type=Gauge32
_WfOspfDynNbrLSRetransQLen_Object=MibTableColumn
wfOspfDynNbrLSRetransQLen=_WfOspfDynNbrLSRetransQLen_Object((1,3,6,1,4,1,18,3,5,3,2,3,9,1,9),_WfOspfDynNbrLSRetransQLen_Type())
wfOspfDynNbrLSRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wfOspfDynNbrLSRetransQLen.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wellfleet':wellfleet,'wfOspfGeneralGroup':wfOspfGeneralGroup,'wfOspfGeneralDelete':wfOspfGeneralDelete,'wfOspfGeneralDisable':wfOspfGeneralDisable,'wfOspfGeneralState':wfOspfGeneralState,'wfOspfRouterId':wfOspfRouterId,'wfOspfVersionNumber':wfOspfVersionNumber,'wfOspfAreaBdrRtrStatus':wfOspfAreaBdrRtrStatus,'wfOspfASBdrRtrStatus':wfOspfASBdrRtrStatus,'wfOspfTOSSupport':wfOspfTOSSupport,'wfOspfSpfHoldDown':wfOspfSpfHoldDown,'wfOspfSlotMask':wfOspfSlotMask,'wfOspfAreaTable':wfOspfAreaTable,'wfOspfAreaEntry':wfOspfAreaEntry,'wfOspfAreaDelete':wfOspfAreaDelete,'wfOspfAreaDisable':wfOspfAreaDisable,'wfOspfAreaState':wfOspfAreaState,_X:wfOspfAreaId,'wfOspfAuthType':wfOspfAuthType,'wfOspfImportASExtern':wfOspfImportASExtern,'wfOspfStubMetric':wfOspfStubMetric,'wfOspfImportSum':wfOspfImportSum,'wfOspfSpfCnt':wfOspfSpfCnt,'wfOspfLsdbTable':wfOspfLsdbTable,'wfOspfLsdbEntry':wfOspfLsdbEntry,_Y:wfOspfLsdbAreaId,_Z:wfOspfLsdbType,_a:wfOspfLsdbLSID,_b:wfOspfLsdbRouterId,'wfOspfLsdbSequence':wfOspfLsdbSequence,'wfOspfLsdbAge':wfOspfLsdbAge,'wfOspfLsdbChecksum':wfOspfLsdbChecksum,'wfOspfLsdbAdvLen':wfOspfLsdbAdvLen,'wfOspfAreaRangeTable':wfOspfAreaRangeTable,'wfOspfAreaRangeEntry':wfOspfAreaRangeEntry,'wfOspfAreaRangeDelete':wfOspfAreaRangeDelete,'wfOspfAreaRangeDisable':wfOspfAreaRangeDisable,'wfOspfAreaRangeState':wfOspfAreaRangeState,_c:wfOspfAreaRangeAreaID,_d:wfOspfAreaRangeNet,'wfOspfAreaRangeMask':wfOspfAreaRangeMask,'wfOspfIfTable':wfOspfIfTable,'wfOspfIfEntry':wfOspfIfEntry,'wfOspfIfDelete':wfOspfIfDelete,'wfOspfIfDisable':wfOspfIfDisable,'wfOspfIfState':wfOspfIfState,_e:wfOspfIfIpAddress,_f:wfOspfAddressLessIf,'wfOspfIfAreaId':wfOspfIfAreaId,'wfOspfIfType':wfOspfIfType,'wfOspfIfRtrPriority':wfOspfIfRtrPriority,'wfOspfIfTransitDelay':wfOspfIfTransitDelay,'wfOspfIfRetransInterval':wfOspfIfRetransInterval,'wfOspfIfHelloInterval':wfOspfIfHelloInterval,'wfOspfIfRtrDeadInterval':wfOspfIfRtrDeadInterval,'wfOspfIfPollInterval':wfOspfIfPollInterval,'wfOspfIfDesignatedRouter':wfOspfIfDesignatedRouter,'wfOspfIfBackupDesignatedRouter':wfOspfIfBackupDesignatedRouter,'wfOspfIfMetricCost':wfOspfIfMetricCost,'wfOspfIfAuthKey':wfOspfIfAuthKey,'wfOspfIfTxHellos':wfOspfIfTxHellos,'wfOspfIfTxDBDescripts':wfOspfIfTxDBDescripts,'wfOspfIfTxLinkStateReqs':wfOspfIfTxLinkStateReqs,'wfOspfIfTxLinkStateUpds':wfOspfIfTxLinkStateUpds,'wfOspfIfTxLinkStateAcks':wfOspfIfTxLinkStateAcks,'wfOspfIfRxHellos':wfOspfIfRxHellos,'wfOspfIfRxDBDescripts':wfOspfIfRxDBDescripts,'wfOspfIfRxLinkStateReqs':wfOspfIfRxLinkStateReqs,'wfOspfIfRxLinkStateUpds':wfOspfIfRxLinkStateUpds,'wfOspfIfRxLinkStateAcks':wfOspfIfRxLinkStateAcks,'wfOspfIfDrops':wfOspfIfDrops,'wfOspfMtuSize':wfOspfMtuSize,'wfOspfVirtIfTable':wfOspfVirtIfTable,'wfOspfVirtIfEntry':wfOspfVirtIfEntry,'wfOspfVirtIfDelete':wfOspfVirtIfDelete,'wfOspfVirtIfDisable':wfOspfVirtIfDisable,'wfOspfVirtIfState':wfOspfVirtIfState,_g:wfOspfVirtIfAreaID,_h:wfOspfVirtIfNeighbor,'wfOspfVirtIfTransitDelay':wfOspfVirtIfTransitDelay,'wfOspfVirtIfRetransInterval':wfOspfVirtIfRetransInterval,'wfOspfVirtIfHelloInterval':wfOspfVirtIfHelloInterval,'wfOspfVirtIfRtrDeadInterval':wfOspfVirtIfRtrDeadInterval,'wfOspfVirtIfAuthKey':wfOspfVirtIfAuthKey,'wfOspfVirtIfTxHellos':wfOspfVirtIfTxHellos,'wfOspfVirtIfTxDBDescripts':wfOspfVirtIfTxDBDescripts,'wfOspfVirtIfTxLinkStateReqs':wfOspfVirtIfTxLinkStateReqs,'wfOspfVirtIfTxLinkStateUpds':wfOspfVirtIfTxLinkStateUpds,'wfOspfVirtIfTxLinkStateAcks':wfOspfVirtIfTxLinkStateAcks,'wfOspfVirtIfRxHellos':wfOspfVirtIfRxHellos,'wfOspfVirtIfRxDBDescripts':wfOspfVirtIfRxDBDescripts,'wfOspfVirtIfRxLinkStateReqs':wfOspfVirtIfRxLinkStateReqs,'wfOspfVirtIfRxLinkStateUpds':wfOspfVirtIfRxLinkStateUpds,'wfOspfVirtIfRxLinkStateAcks':wfOspfVirtIfRxLinkStateAcks,'wfOspfVirtIfDrops':wfOspfVirtIfDrops,'wfOspfNbrTable':wfOspfNbrTable,'wfOspfNbrEntry':wfOspfNbrEntry,'wfOspfNbrDelete':wfOspfNbrDelete,'wfOspfNbrDisable':wfOspfNbrDisable,'wfOspfNbrState':wfOspfNbrState,_i:wfOspfNbrIpAddr,'wfOspfNbrIfAddr':wfOspfNbrIfAddr,_j:wfOspfNbrAddressLessIndex,'wfOspfNbrRtrId':wfOspfNbrRtrId,'wfOspfNbrOptions':wfOspfNbrOptions,'wfOspfNbrPriority':wfOspfNbrPriority,'wfOspfNbrEvents':wfOspfNbrEvents,'wfOspfNbrLSRetransQLen':wfOspfNbrLSRetransQLen,'wfOspfVirtNbrTable':wfOspfVirtNbrTable,'wfOspfVirtNbrEntry':wfOspfVirtNbrEntry,_k:wfOspfVirtNbrArea,_l:wfOspfVirtNbrRtrId,'wfOspfVirtNbrIpAddr':wfOspfVirtNbrIpAddr,'wfOspfVirtNbrOptions':wfOspfVirtNbrOptions,'wfOspfVirtNbrState':wfOspfVirtNbrState,'wfOspfVirtNbrEvents':wfOspfVirtNbrEvents,'wfOspfVirtNbrLSRetransQLen':wfOspfVirtNbrLSRetransQLen,'wfOspfDynNbrTable':wfOspfDynNbrTable,'wfOspfDynNbrEntry':wfOspfDynNbrEntry,'wfOspfDynNbrState':wfOspfDynNbrState,_m:wfOspfDynNbrIpAddr,'wfOspfDynNbrIfAddr':wfOspfDynNbrIfAddr,_n:wfOspfDynNbrAddressLessIndex,'wfOspfDynNbrRtrId':wfOspfDynNbrRtrId,'wfOspfDynNbrOptions':wfOspfDynNbrOptions,'wfOspfDynNbrPriority':wfOspfDynNbrPriority,'wfOspfDynNbrEvents':wfOspfDynNbrEvents,'wfOspfDynNbrLSRetransQLen':wfOspfDynNbrLSRetransQLen})