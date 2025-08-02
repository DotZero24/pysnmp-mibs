_K='fsPbbTeTeSidExtEntry'
_J='destroy'
_I='fsPbbTeEspVid'
_H='not-accessible'
_G='RowStatus'
_F='read-only'
_E='fsPbbTeContextId'
_D='ARICENT-PBB-TE-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,=mibBuilder.importSymbols('ARICENTQ-BRIDGE-MIB','VlanId')
IfIndexList,ieee8021PbbTeTeSidEntry=mibBuilder.importSymbols('IEEE8021-PBBTE-MIB','IfIndexList','ieee8021PbbTeTeSidEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress',_G,'TextualConvention')
fspbbte=ModuleIdentity((1,3,6,1,4,1,29601,2,11))
if mibBuilder.loadTexts:fspbbte.setRevisions(('2012-09-05 00:00',))
_FsPbbTeScalars_ObjectIdentity=ObjectIdentity
fsPbbTeScalars=_FsPbbTeScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,11,1))
_FsPbbTeGlobalTraceOption_Type=Unsigned32
_FsPbbTeGlobalTraceOption_Object=MibScalar
fsPbbTeGlobalTraceOption=_FsPbbTeGlobalTraceOption_Object((1,3,6,1,4,1,29601,2,11,1,1),_FsPbbTeGlobalTraceOption_Type())
fsPbbTeGlobalTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeGlobalTraceOption.setStatus(_A)
_FsPbbTeContext_ObjectIdentity=ObjectIdentity
fsPbbTeContext=_FsPbbTeContext_ObjectIdentity((1,3,6,1,4,1,29601,2,11,2))
_FsPbbTeContextTable_Object=MibTable
fsPbbTeContextTable=_FsPbbTeContextTable_Object((1,3,6,1,4,1,29601,2,11,2,1))
if mibBuilder.loadTexts:fsPbbTeContextTable.setStatus(_A)
_FsPbbTeContextEntry_Object=MibTableRow
fsPbbTeContextEntry=_FsPbbTeContextEntry_Object((1,3,6,1,4,1,29601,2,11,2,1,1))
fsPbbTeContextEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fsPbbTeContextEntry.setStatus(_A)
class _FsPbbTeContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPbbTeContextId_Type.__name__=_C
_FsPbbTeContextId_Object=MibTableColumn
fsPbbTeContextId=_FsPbbTeContextId_Object((1,3,6,1,4,1,29601,2,11,2,1,1,1),_FsPbbTeContextId_Type())
fsPbbTeContextId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPbbTeContextId.setStatus(_A)
class _FsPbbTeContextSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPbbTeContextSystemControl_Type.__name__=_C
_FsPbbTeContextSystemControl_Object=MibTableColumn
fsPbbTeContextSystemControl=_FsPbbTeContextSystemControl_Object((1,3,6,1,4,1,29601,2,11,2,1,1,2),_FsPbbTeContextSystemControl_Type())
fsPbbTeContextSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeContextSystemControl.setStatus(_A)
_FsPbbTeContextTraceOption_Type=Unsigned32
_FsPbbTeContextTraceOption_Object=MibTableColumn
fsPbbTeContextTraceOption=_FsPbbTeContextTraceOption_Object((1,3,6,1,4,1,29601,2,11,2,1,1,3),_FsPbbTeContextTraceOption_Type())
fsPbbTeContextTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeContextTraceOption.setStatus(_A)
_FsPbbTeContextNoOfActiveEsps_Type=Counter32
_FsPbbTeContextNoOfActiveEsps_Object=MibTableColumn
fsPbbTeContextNoOfActiveEsps=_FsPbbTeContextNoOfActiveEsps_Object((1,3,6,1,4,1,29601,2,11,2,1,1,4),_FsPbbTeContextNoOfActiveEsps_Type())
fsPbbTeContextNoOfActiveEsps.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbTeContextNoOfActiveEsps.setStatus(_A)
_FsPbbTeContextNoOfCreatedEsps_Type=Counter32
_FsPbbTeContextNoOfCreatedEsps_Object=MibTableColumn
fsPbbTeContextNoOfCreatedEsps=_FsPbbTeContextNoOfCreatedEsps_Object((1,3,6,1,4,1,29601,2,11,2,1,1,5),_FsPbbTeContextNoOfCreatedEsps_Type())
fsPbbTeContextNoOfCreatedEsps.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbTeContextNoOfCreatedEsps.setStatus(_A)
_FsPbbTeContextNoOfDeletedEsps_Type=Counter32
_FsPbbTeContextNoOfDeletedEsps_Object=MibTableColumn
fsPbbTeContextNoOfDeletedEsps=_FsPbbTeContextNoOfDeletedEsps_Object((1,3,6,1,4,1,29601,2,11,2,1,1,6),_FsPbbTeContextNoOfDeletedEsps_Type())
fsPbbTeContextNoOfDeletedEsps.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbTeContextNoOfDeletedEsps.setStatus(_A)
_FsPbbTeEspVidMapping_ObjectIdentity=ObjectIdentity
fsPbbTeEspVidMapping=_FsPbbTeEspVidMapping_ObjectIdentity((1,3,6,1,4,1,29601,2,11,3))
_FsPbbTeEspVidTable_Object=MibTable
fsPbbTeEspVidTable=_FsPbbTeEspVidTable_Object((1,3,6,1,4,1,29601,2,11,3,1))
if mibBuilder.loadTexts:fsPbbTeEspVidTable.setStatus(_A)
_FsPbbTeEspVidEntry_Object=MibTableRow
fsPbbTeEspVidEntry=_FsPbbTeEspVidEntry_Object((1,3,6,1,4,1,29601,2,11,3,1,1))
fsPbbTeEspVidEntry.setIndexNames((0,_D,_E),(0,_D,_I))
if mibBuilder.loadTexts:fsPbbTeEspVidEntry.setStatus(_A)
_FsPbbTeEspVid_Type=VlanId
_FsPbbTeEspVid_Object=MibTableColumn
fsPbbTeEspVid=_FsPbbTeEspVid_Object((1,3,6,1,4,1,29601,2,11,3,1,1,1),_FsPbbTeEspVid_Type())
fsPbbTeEspVid.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPbbTeEspVid.setStatus(_A)
class _FsPbbTeEspVidRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,6)));namedValues=NamedValues(*(('createAndGo',4),(_J,6)))
_FsPbbTeEspVidRowStatus_Type.__name__=_G
_FsPbbTeEspVidRowStatus_Object=MibTableColumn
fsPbbTeEspVidRowStatus=_FsPbbTeEspVidRowStatus_Object((1,3,6,1,4,1,29601,2,11,3,1,1,2),_FsPbbTeEspVidRowStatus_Type())
fsPbbTeEspVidRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsPbbTeEspVidRowStatus.setStatus(_A)
_FsPbbTeTeSidExtension_ObjectIdentity=ObjectIdentity
fsPbbTeTeSidExtension=_FsPbbTeTeSidExtension_ObjectIdentity((1,3,6,1,4,1,29601,2,11,4))
_FsPbbTeTeSidExtTable_Object=MibTable
fsPbbTeTeSidExtTable=_FsPbbTeTeSidExtTable_Object((1,3,6,1,4,1,29601,2,11,4,1))
if mibBuilder.loadTexts:fsPbbTeTeSidExtTable.setStatus(_A)
_FsPbbTeTeSidExtEntry_Object=MibTableRow
fsPbbTeTeSidExtEntry=_FsPbbTeTeSidExtEntry_Object((1,3,6,1,4,1,29601,2,11,4,1,1))
if mibBuilder.loadTexts:fsPbbTeTeSidExtEntry.setStatus(_A)
class _FsPbbTeTeSidExtContextId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_FsPbbTeTeSidExtContextId_Type.__name__=_C
_FsPbbTeTeSidExtContextId_Object=MibTableColumn
fsPbbTeTeSidExtContextId=_FsPbbTeTeSidExtContextId_Object((1,3,6,1,4,1,29601,2,11,4,1,1,1),_FsPbbTeTeSidExtContextId_Type())
fsPbbTeTeSidExtContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTeSidExtContextId.setStatus(_A)
_FsPbbTeTest_ObjectIdentity=ObjectIdentity
fsPbbTeTest=_FsPbbTeTest_ObjectIdentity((1,3,6,1,4,1,29601,2,11,5))
class _FsPbbTeTestApiContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPbbTeTestApiContextId_Type.__name__=_C
_FsPbbTeTestApiContextId_Object=MibScalar
fsPbbTeTestApiContextId=_FsPbbTeTestApiContextId_Object((1,3,6,1,4,1,29601,2,11,5,1),_FsPbbTeTestApiContextId_Type())
fsPbbTeTestApiContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiContextId.setStatus(_A)
_FsPbbTeTestApiTeSid_Type=Integer32
_FsPbbTeTestApiTeSid_Object=MibScalar
fsPbbTeTestApiTeSid=_FsPbbTeTestApiTeSid_Object((1,3,6,1,4,1,29601,2,11,5,2),_FsPbbTeTestApiTeSid_Type())
fsPbbTeTestApiTeSid.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiTeSid.setStatus(_A)
_FsPbbTeTestApiDestMacAddr_Type=MacAddress
_FsPbbTeTestApiDestMacAddr_Object=MibScalar
fsPbbTeTestApiDestMacAddr=_FsPbbTeTestApiDestMacAddr_Object((1,3,6,1,4,1,29601,2,11,5,3),_FsPbbTeTestApiDestMacAddr_Type())
fsPbbTeTestApiDestMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiDestMacAddr.setStatus(_A)
_FsPbbTeTestApiSourceMacAddr_Type=MacAddress
_FsPbbTeTestApiSourceMacAddr_Object=MibScalar
fsPbbTeTestApiSourceMacAddr=_FsPbbTeTestApiSourceMacAddr_Object((1,3,6,1,4,1,29601,2,11,5,4),_FsPbbTeTestApiSourceMacAddr_Type())
fsPbbTeTestApiSourceMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiSourceMacAddr.setStatus(_A)
_FsPbbTeTestApiEspVlanId_Type=VlanId
_FsPbbTeTestApiEspVlanId_Object=MibScalar
fsPbbTeTestApiEspVlanId=_FsPbbTeTestApiEspVlanId_Object((1,3,6,1,4,1,29601,2,11,5,5),_FsPbbTeTestApiEspVlanId_Type())
fsPbbTeTestApiEspVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiEspVlanId.setStatus(_A)
class _FsPbbTeTestApiEgressPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPbbTeTestApiEgressPort_Type.__name__=_C
_FsPbbTeTestApiEgressPort_Object=MibScalar
fsPbbTeTestApiEgressPort=_FsPbbTeTestApiEgressPort_Object((1,3,6,1,4,1,29601,2,11,5,6),_FsPbbTeTestApiEgressPort_Type())
fsPbbTeTestApiEgressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiEgressPort.setStatus(_A)
_FsPbbTeTestApiEgressPortList_Type=IfIndexList
_FsPbbTeTestApiEgressPortList_Object=MibScalar
fsPbbTeTestApiEgressPortList=_FsPbbTeTestApiEgressPortList_Object((1,3,6,1,4,1,29601,2,11,5,7),_FsPbbTeTestApiEgressPortList_Type())
fsPbbTeTestApiEgressPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiEgressPortList.setStatus(_A)
class _FsPbbTeTestApiAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('create',1),(_J,2)))
_FsPbbTeTestApiAction_Type.__name__=_C
_FsPbbTeTestApiAction_Object=MibScalar
fsPbbTeTestApiAction=_FsPbbTeTestApiAction_Object((1,3,6,1,4,1,29601,2,11,5,8),_FsPbbTeTestApiAction_Type())
fsPbbTeTestApiAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTeTestApiAction.setStatus(_A)
ieee8021PbbTeTeSidEntry.registerAugmentions((_D,_K))
fsPbbTeTeSidExtEntry.setIndexNames(*ieee8021PbbTeTeSidEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'fspbbte':fspbbte,'fsPbbTeScalars':fsPbbTeScalars,'fsPbbTeGlobalTraceOption':fsPbbTeGlobalTraceOption,'fsPbbTeContext':fsPbbTeContext,'fsPbbTeContextTable':fsPbbTeContextTable,'fsPbbTeContextEntry':fsPbbTeContextEntry,_E:fsPbbTeContextId,'fsPbbTeContextSystemControl':fsPbbTeContextSystemControl,'fsPbbTeContextTraceOption':fsPbbTeContextTraceOption,'fsPbbTeContextNoOfActiveEsps':fsPbbTeContextNoOfActiveEsps,'fsPbbTeContextNoOfCreatedEsps':fsPbbTeContextNoOfCreatedEsps,'fsPbbTeContextNoOfDeletedEsps':fsPbbTeContextNoOfDeletedEsps,'fsPbbTeEspVidMapping':fsPbbTeEspVidMapping,'fsPbbTeEspVidTable':fsPbbTeEspVidTable,'fsPbbTeEspVidEntry':fsPbbTeEspVidEntry,_I:fsPbbTeEspVid,'fsPbbTeEspVidRowStatus':fsPbbTeEspVidRowStatus,'fsPbbTeTeSidExtension':fsPbbTeTeSidExtension,'fsPbbTeTeSidExtTable':fsPbbTeTeSidExtTable,_K:fsPbbTeTeSidExtEntry,'fsPbbTeTeSidExtContextId':fsPbbTeTeSidExtContextId,'fsPbbTeTest':fsPbbTeTest,'fsPbbTeTestApiContextId':fsPbbTeTestApiContextId,'fsPbbTeTestApiTeSid':fsPbbTeTestApiTeSid,'fsPbbTeTestApiDestMacAddr':fsPbbTeTestApiDestMacAddr,'fsPbbTeTestApiSourceMacAddr':fsPbbTeTestApiSourceMacAddr,'fsPbbTeTestApiEspVlanId':fsPbbTeTestApiEspVlanId,'fsPbbTeTestApiEgressPort':fsPbbTeTestApiEgressPort,'fsPbbTeTestApiEgressPortList':fsPbbTeTestApiEgressPortList,'fsPbbTeTestApiAction':fsPbbTeTestApiAction})