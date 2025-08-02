_a='dot1agCfmMepHighestPrDefect'
_Z='dot1agCfmMipSessionId'
_Y='dot1agCfmMepDbRSessionId'
_X='dot1agCfmLtrReceiveOrder'
_W='dot1agCfmLtrSeqNumber'
_V='Dot1agCfmLowestAlarmPri'
_U='Dot1agCfmFngState'
_T='dot1agCfmSessionId'
_S='dot1agCfmMaMepListSessionId'
_R='dot1agCfmMaVlanListIdentifier'
_Q='Dot1agCfmCcmInterval'
_P='Dot1agCfmMDLevel'
_O='Dot1agCfmMaintDomainName'
_N='Dot1agCfmMaintDomainNameType'
_M='charString'
_L='Dot1agCfmIdPermission'
_K='Dot1agCfmMhfCreation'
_J='OctetString'
_I='TruthValue'
_H='dot1agCfmMaIndex'
_G='d'
_F='not-accessible'
_E='dot1agCfmMdIndex'
_D='Unsigned32'
_C='ZXR10-CFM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
zxr10,=mibBuilder.importSymbols('ZXR10-SMI','zxr10')
zxr10cfmMIB=ModuleIdentity((1,3,6,1,4,1,3902,3,120))
if mibBuilder.loadTexts:zxr10cfmMIB.setRevisions(('2007-01-24 00:00',))
class InterfaceIndexOrZero(TextualConvention,Integer32):status=_A;displayHint=_G;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class VlanIdOrNone(TextualConvention,Integer32):status=_A;displayHint=_G;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
class VlanId(TextualConvention,Integer32):status=_A;displayHint=_G;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class Dot1agCfmMaintDomainNameType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('dnsLikeName',2),('macAddressAndUint',3),(_M,4)))
class Dot1agCfmMaintDomainName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
class Dot1agCfmMaintAssocNameType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primaryVid',1),(_M,2),('unsignedInt16',3),('rfc2865VpnId',4)))
class Dot1agCfmMaintAssocName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
class Dot1agCfmMDLevel(TextualConvention,Integer32):status=_A;displayHint=_G;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class Dot1agCfmMpDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
class Dot1agCfmHighestDefectPri(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('defRDICCM',1),('defMACstatus',2),('defRemoteCCM',3),('defErrorCCM',4),('defXconCCM',5)))
class Dot1agCfmLowestAlarmPri(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('allDef',1),('macRemErrXcon',2),('remErrXcon',3),('errXcon',4),('xcon',5),('noXcon',6)))
class Dot1agCfmSessionId(TextualConvention,Unsigned32):status=_A;displayHint=_G;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
class Dot1agCfmMhfCreation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('defMHFnone',1),('defMHFdefault',2),('defMHFexplicit',3),('defMHFdefer',4)))
class Dot1agCfmIdPermission(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sendIdNone',1),('sendIdChassis',2),('sendIdManage',3),('sendIdChassisManage',4),('sendIdDefer',5)))
class Dot1agCfmSpeed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fastSpeed',0),('slowSpeed',1)))
class Dot1agCfmCcmInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('intervalInvalid',0),('interval300Hz',1),('interval10ms',2),('interval100ms',3),('interval1s',4),('interval10s',5),('interval1min',6),('interval10min',7)))
class Dot1agCfmFngState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('fngReset',1),('fngDefect',2),('fngReportDefect',3),('fngDefectReported',4),('fngDefectClearing',5)))
class Dot1agCfmRelayActionFieldValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rlyHit',1),('rlyFdb',2),('rlyMpdb',3)))
class Dot1agCfmIngressActionFieldValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ingOk',1),('ingDown',2),('ingBlocked',3),('ingVid',4)))
class Dot1agCfmEgressActionFieldValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('egrOK',1),('egrDown',2),('egrBlocked',3),('egrVid',4)))
class Dot1afCfmIndexIntegerNextFree(TextualConvention,Unsigned32):status=_A;displayHint=_G;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class Dot1agCfmMepDefects(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('bDefRDICCM',0),('bDefMACstatus',1),('bDefRemoteCCM',2),('bDefErrorCCM',3),('bDefXconCCM',4)))
class Dot1agCfmLbrTransId(TextualConvention,Unsigned32):status=_A;displayHint=_G;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Dot1agNotifications_ObjectIdentity=ObjectIdentity
dot1agNotifications=_Dot1agNotifications_ObjectIdentity((1,3,6,1,4,1,3902,3,120,0))
_Dot1agMIBObjects_ObjectIdentity=ObjectIdentity
dot1agMIBObjects=_Dot1agMIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,3,120,1))
_Dot1agCfmMd_ObjectIdentity=ObjectIdentity
dot1agCfmMd=_Dot1agCfmMd_ObjectIdentity((1,3,6,1,4,1,3902,3,120,1,1))
_Dot1agCfmMdTableNextIndex_Type=Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdTableNextIndex_Object=MibScalar
dot1agCfmMdTableNextIndex=_Dot1agCfmMdTableNextIndex_Object((1,3,6,1,4,1,3902,3,120,1,1,1),_Dot1agCfmMdTableNextIndex_Type())
dot1agCfmMdTableNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdTableNextIndex.setStatus(_A)
_Dot1agCfmMdTable_Object=MibTable
dot1agCfmMdTable=_Dot1agCfmMdTable_Object((1,3,6,1,4,1,3902,3,120,1,1,2))
if mibBuilder.loadTexts:dot1agCfmMdTable.setStatus(_A)
_Dot1agCfmMdEntry_Object=MibTableRow
dot1agCfmMdEntry=_Dot1agCfmMdEntry_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1))
dot1agCfmMdEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:dot1agCfmMdEntry.setStatus(_A)
class _Dot1agCfmMdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Dot1agCfmMdIndex_Type.__name__=_D
_Dot1agCfmMdIndex_Object=MibTableColumn
dot1agCfmMdIndex=_Dot1agCfmMdIndex_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,1),_Dot1agCfmMdIndex_Type())
dot1agCfmMdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmMdIndex.setStatus(_A)
class _Dot1agCfmMdFormat_Type(Dot1agCfmMaintDomainNameType):defaultValue=4
_Dot1agCfmMdFormat_Type.__name__=_N
_Dot1agCfmMdFormat_Object=MibTableColumn
dot1agCfmMdFormat=_Dot1agCfmMdFormat_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,2),_Dot1agCfmMdFormat_Type())
dot1agCfmMdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdFormat.setStatus(_A)
class _Dot1agCfmMdName_Type(Dot1agCfmMaintDomainName):defaultValue=OctetString('DEFAULT')
_Dot1agCfmMdName_Type.__name__=_O
_Dot1agCfmMdName_Object=MibTableColumn
dot1agCfmMdName=_Dot1agCfmMdName_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,3),_Dot1agCfmMdName_Type())
dot1agCfmMdName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdName.setStatus(_A)
class _Dot1agCfmMdMdLevel_Type(Dot1agCfmMDLevel):defaultValue=0
_Dot1agCfmMdMdLevel_Type.__name__=_P
_Dot1agCfmMdMdLevel_Object=MibTableColumn
dot1agCfmMdMdLevel=_Dot1agCfmMdMdLevel_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,4),_Dot1agCfmMdMdLevel_Type())
dot1agCfmMdMdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdMdLevel.setStatus(_A)
class _Dot1agCfmMdMhfCreation_Type(Dot1agCfmMhfCreation):defaultValue=1
_Dot1agCfmMdMhfCreation_Type.__name__=_K
_Dot1agCfmMdMhfCreation_Object=MibTableColumn
dot1agCfmMdMhfCreation=_Dot1agCfmMdMhfCreation_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,5),_Dot1agCfmMdMhfCreation_Type())
dot1agCfmMdMhfCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdMhfCreation.setStatus(_A)
class _Dot1agCfmMdMhfIdPermission_Type(Dot1agCfmIdPermission):defaultValue=1
_Dot1agCfmMdMhfIdPermission_Type.__name__=_L
_Dot1agCfmMdMhfIdPermission_Object=MibTableColumn
dot1agCfmMdMhfIdPermission=_Dot1agCfmMdMhfIdPermission_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,6),_Dot1agCfmMdMhfIdPermission_Type())
dot1agCfmMdMhfIdPermission.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdMhfIdPermission.setStatus(_A)
_Dot1agCfmMdMaTableNextIndex_Type=Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdMaTableNextIndex_Object=MibTableColumn
dot1agCfmMdMaTableNextIndex=_Dot1agCfmMdMaTableNextIndex_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,7),_Dot1agCfmMdMaTableNextIndex_Type())
dot1agCfmMdMaTableNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdMaTableNextIndex.setStatus(_A)
_Dot1agCfmMdRowStatus_Type=RowStatus
_Dot1agCfmMdRowStatus_Object=MibTableColumn
dot1agCfmMdRowStatus=_Dot1agCfmMdRowStatus_Object((1,3,6,1,4,1,3902,3,120,1,1,2,1,8),_Dot1agCfmMdRowStatus_Type())
dot1agCfmMdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMdRowStatus.setStatus(_A)
_Dot1agCfmMa_ObjectIdentity=ObjectIdentity
dot1agCfmMa=_Dot1agCfmMa_ObjectIdentity((1,3,6,1,4,1,3902,3,120,1,2))
_Dot1agCfmMaTable_Object=MibTable
dot1agCfmMaTable=_Dot1agCfmMaTable_Object((1,3,6,1,4,1,3902,3,120,1,2,1))
if mibBuilder.loadTexts:dot1agCfmMaTable.setStatus(_A)
_Dot1agCfmMaEntry_Object=MibTableRow
dot1agCfmMaEntry=_Dot1agCfmMaEntry_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1))
dot1agCfmMaEntry.setIndexNames((0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:dot1agCfmMaEntry.setStatus(_A)
class _Dot1agCfmMaIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Dot1agCfmMaIndex_Type.__name__=_D
_Dot1agCfmMaIndex_Object=MibTableColumn
dot1agCfmMaIndex=_Dot1agCfmMaIndex_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,1),_Dot1agCfmMaIndex_Type())
dot1agCfmMaIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmMaIndex.setStatus(_A)
_Dot1agCfmMaPrimaryVlanId_Type=VlanIdOrNone
_Dot1agCfmMaPrimaryVlanId_Object=MibTableColumn
dot1agCfmMaPrimaryVlanId=_Dot1agCfmMaPrimaryVlanId_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,2),_Dot1agCfmMaPrimaryVlanId_Type())
dot1agCfmMaPrimaryVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaPrimaryVlanId.setStatus(_A)
_Dot1agCfmMaFormat_Type=Dot1agCfmMaintAssocNameType
_Dot1agCfmMaFormat_Object=MibTableColumn
dot1agCfmMaFormat=_Dot1agCfmMaFormat_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,3),_Dot1agCfmMaFormat_Type())
dot1agCfmMaFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaFormat.setStatus(_A)
_Dot1agCfmMaName_Type=Dot1agCfmMaintAssocName
_Dot1agCfmMaName_Object=MibTableColumn
dot1agCfmMaName=_Dot1agCfmMaName_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,4),_Dot1agCfmMaName_Type())
dot1agCfmMaName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaName.setStatus(_A)
class _Dot1agCfmMaMhfCreation_Type(Dot1agCfmMhfCreation):defaultValue=4
_Dot1agCfmMaMhfCreation_Type.__name__=_K
_Dot1agCfmMaMhfCreation_Object=MibTableColumn
dot1agCfmMaMhfCreation=_Dot1agCfmMaMhfCreation_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,5),_Dot1agCfmMaMhfCreation_Type())
dot1agCfmMaMhfCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaMhfCreation.setStatus(_A)
class _Dot1agCfmMaIdPermission_Type(Dot1agCfmIdPermission):defaultValue=5
_Dot1agCfmMaIdPermission_Type.__name__=_L
_Dot1agCfmMaIdPermission_Object=MibTableColumn
dot1agCfmMaIdPermission=_Dot1agCfmMaIdPermission_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,6),_Dot1agCfmMaIdPermission_Type())
dot1agCfmMaIdPermission.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaIdPermission.setStatus(_A)
class _Dot1agCfmMaCcmInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_Dot1agCfmMaCcmInterval_Type.__name__=_Q
_Dot1agCfmMaCcmInterval_Object=MibTableColumn
dot1agCfmMaCcmInterval=_Dot1agCfmMaCcmInterval_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,7),_Dot1agCfmMaCcmInterval_Type())
dot1agCfmMaCcmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaCcmInterval.setStatus(_A)
_Dot1agCfmMaRowStatus_Type=RowStatus
_Dot1agCfmMaRowStatus_Object=MibTableColumn
dot1agCfmMaRowStatus=_Dot1agCfmMaRowStatus_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,8),_Dot1agCfmMaRowStatus_Type())
dot1agCfmMaRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaRowStatus.setStatus(_A)
_Dot1agCfmMASpeed_Type=Dot1agCfmSpeed
_Dot1agCfmMASpeed_Object=MibTableColumn
dot1agCfmMASpeed=_Dot1agCfmMASpeed_Object((1,3,6,1,4,1,3902,3,120,1,2,1,1,9),_Dot1agCfmMASpeed_Type())
dot1agCfmMASpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMASpeed.setStatus(_A)
_Dot1agCfmMaVlanListTable_Object=MibTable
dot1agCfmMaVlanListTable=_Dot1agCfmMaVlanListTable_Object((1,3,6,1,4,1,3902,3,120,1,2,2))
if mibBuilder.loadTexts:dot1agCfmMaVlanListTable.setStatus(_A)
_Dot1agCfmMaVlanListEntry_Object=MibTableRow
dot1agCfmMaVlanListEntry=_Dot1agCfmMaVlanListEntry_Object((1,3,6,1,4,1,3902,3,120,1,2,2,1))
dot1agCfmMaVlanListEntry.setIndexNames((0,_C,_E),(0,_C,_H),(0,_C,_R))
if mibBuilder.loadTexts:dot1agCfmMaVlanListEntry.setStatus(_A)
_Dot1agCfmMaVlanListIdentifier_Type=VlanId
_Dot1agCfmMaVlanListIdentifier_Object=MibTableColumn
dot1agCfmMaVlanListIdentifier=_Dot1agCfmMaVlanListIdentifier_Object((1,3,6,1,4,1,3902,3,120,1,2,2,1,1),_Dot1agCfmMaVlanListIdentifier_Type())
dot1agCfmMaVlanListIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmMaVlanListIdentifier.setStatus(_A)
_Dot1agCfmMaVlanListRowStatus_Type=RowStatus
_Dot1agCfmMaVlanListRowStatus_Object=MibTableColumn
dot1agCfmMaVlanListRowStatus=_Dot1agCfmMaVlanListRowStatus_Object((1,3,6,1,4,1,3902,3,120,1,2,2,1,2),_Dot1agCfmMaVlanListRowStatus_Type())
dot1agCfmMaVlanListRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaVlanListRowStatus.setStatus(_A)
_Dot1agCfmMaMepListTable_Object=MibTable
dot1agCfmMaMepListTable=_Dot1agCfmMaMepListTable_Object((1,3,6,1,4,1,3902,3,120,1,2,3))
if mibBuilder.loadTexts:dot1agCfmMaMepListTable.setStatus(_A)
_Dot1agCfmMaMepListEntry_Object=MibTableRow
dot1agCfmMaMepListEntry=_Dot1agCfmMaMepListEntry_Object((1,3,6,1,4,1,3902,3,120,1,2,3,1))
dot1agCfmMaMepListEntry.setIndexNames((0,_C,_E),(0,_C,_H),(0,_C,_S))
if mibBuilder.loadTexts:dot1agCfmMaMepListEntry.setStatus(_A)
_Dot1agCfmMaMepListSessionId_Type=Dot1agCfmSessionId
_Dot1agCfmMaMepListSessionId_Object=MibTableColumn
dot1agCfmMaMepListSessionId=_Dot1agCfmMaMepListSessionId_Object((1,3,6,1,4,1,3902,3,120,1,2,3,1,1),_Dot1agCfmMaMepListSessionId_Type())
dot1agCfmMaMepListSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmMaMepListSessionId.setStatus(_A)
_Dot1agCfmMaMepListRowStatus_Type=RowStatus
_Dot1agCfmMaMepListRowStatus_Object=MibTableColumn
dot1agCfmMaMepListRowStatus=_Dot1agCfmMaMepListRowStatus_Object((1,3,6,1,4,1,3902,3,120,1,2,3,1,2),_Dot1agCfmMaMepListRowStatus_Type())
dot1agCfmMaMepListRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMaMepListRowStatus.setStatus(_A)
_Dot1agCfmMep_ObjectIdentity=ObjectIdentity
dot1agCfmMep=_Dot1agCfmMep_ObjectIdentity((1,3,6,1,4,1,3902,3,120,1,3))
_Dot1agCfmMepTable_Object=MibTable
dot1agCfmMepTable=_Dot1agCfmMepTable_Object((1,3,6,1,4,1,3902,3,120,1,3,1))
if mibBuilder.loadTexts:dot1agCfmMepTable.setStatus(_A)
_Dot1agCfmMepEntry_Object=MibTableRow
dot1agCfmMepEntry=_Dot1agCfmMepEntry_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1))
dot1agCfmMepEntry.setIndexNames((0,_C,_E),(0,_C,_H),(0,_C,_T))
if mibBuilder.loadTexts:dot1agCfmMepEntry.setStatus(_A)
_Dot1agCfmSessionId_Type=Dot1agCfmSessionId
_Dot1agCfmSessionId_Object=MibTableColumn
dot1agCfmSessionId=_Dot1agCfmSessionId_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,1),_Dot1agCfmSessionId_Type())
dot1agCfmSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmSessionId.setStatus(_A)
_Dot1agCfmMepIfIndex_Type=InterfaceIndexOrZero
_Dot1agCfmMepIfIndex_Object=MibTableColumn
dot1agCfmMepIfIndex=_Dot1agCfmMepIfIndex_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,2),_Dot1agCfmMepIfIndex_Type())
dot1agCfmMepIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepIfIndex.setStatus(_A)
_Dot1agCfmMepDirection_Type=Dot1agCfmMpDirection
_Dot1agCfmMepDirection_Object=MibTableColumn
dot1agCfmMepDirection=_Dot1agCfmMepDirection_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,3),_Dot1agCfmMepDirection_Type())
dot1agCfmMepDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepDirection.setStatus(_A)
class _Dot1agCfmMepPrimaryVid_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Dot1agCfmMepPrimaryVid_Type.__name__=_D
_Dot1agCfmMepPrimaryVid_Object=MibTableColumn
dot1agCfmMepPrimaryVid=_Dot1agCfmMepPrimaryVid_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,4),_Dot1agCfmMepPrimaryVid_Type())
dot1agCfmMepPrimaryVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepPrimaryVid.setStatus(_A)
class _Dot1agCfmMepActive_Type(TruthValue):defaultValue=2
_Dot1agCfmMepActive_Type.__name__=_I
_Dot1agCfmMepActive_Object=MibTableColumn
dot1agCfmMepActive=_Dot1agCfmMepActive_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,5),_Dot1agCfmMepActive_Type())
dot1agCfmMepActive.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepActive.setStatus(_A)
class _Dot1agCfmMepFngState_Type(Dot1agCfmFngState):defaultValue=1
_Dot1agCfmMepFngState_Type.__name__=_U
_Dot1agCfmMepFngState_Object=MibTableColumn
dot1agCfmMepFngState=_Dot1agCfmMepFngState_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,6),_Dot1agCfmMepFngState_Type())
dot1agCfmMepFngState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepFngState.setStatus(_A)
class _Dot1agCfmMepCciEnabled_Type(TruthValue):defaultValue=2
_Dot1agCfmMepCciEnabled_Type.__name__=_I
_Dot1agCfmMepCciEnabled_Object=MibTableColumn
dot1agCfmMepCciEnabled=_Dot1agCfmMepCciEnabled_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,7),_Dot1agCfmMepCciEnabled_Type())
dot1agCfmMepCciEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepCciEnabled.setStatus(_A)
class _Dot1agCfmMepCcmLtmPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1agCfmMepCcmLtmPriority_Type.__name__=_D
_Dot1agCfmMepCcmLtmPriority_Object=MibTableColumn
dot1agCfmMepCcmLtmPriority=_Dot1agCfmMepCcmLtmPriority_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,8),_Dot1agCfmMepCcmLtmPriority_Type())
dot1agCfmMepCcmLtmPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepCcmLtmPriority.setStatus(_A)
_Dot1agCfmMepMacAddress_Type=MacAddress
_Dot1agCfmMepMacAddress_Object=MibTableColumn
dot1agCfmMepMacAddress=_Dot1agCfmMepMacAddress_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,9),_Dot1agCfmMepMacAddress_Type())
dot1agCfmMepMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepMacAddress.setStatus(_A)
class _Dot1agCfmMepLowPrDef_Type(Dot1agCfmLowestAlarmPri):defaultValue=2
_Dot1agCfmMepLowPrDef_Type.__name__=_V
_Dot1agCfmMepLowPrDef_Object=MibTableColumn
dot1agCfmMepLowPrDef=_Dot1agCfmMepLowPrDef_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,10),_Dot1agCfmMepLowPrDef_Type())
dot1agCfmMepLowPrDef.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLowPrDef.setStatus(_A)
_Dot1agCfmMepHighestPrDefect_Type=Dot1agCfmHighestDefectPri
_Dot1agCfmMepHighestPrDefect_Object=MibTableColumn
dot1agCfmMepHighestPrDefect=_Dot1agCfmMepHighestPrDefect_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,11),_Dot1agCfmMepHighestPrDefect_Type())
dot1agCfmMepHighestPrDefect.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepHighestPrDefect.setStatus(_A)
_Dot1agCfmMepDefects_Type=Dot1agCfmMepDefects
_Dot1agCfmMepDefects_Object=MibTableColumn
dot1agCfmMepDefects=_Dot1agCfmMepDefects_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,12),_Dot1agCfmMepDefects_Type())
dot1agCfmMepDefects.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepDefects.setStatus(_A)
_Dot1agCfmMepCciSentCcms_Type=Counter32
_Dot1agCfmMepCciSentCcms_Object=MibTableColumn
dot1agCfmMepCciSentCcms=_Dot1agCfmMepCciSentCcms_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,13),_Dot1agCfmMepCciSentCcms_Type())
dot1agCfmMepCciSentCcms.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepCciSentCcms.setStatus(_A)
_Dot1agCfmMepId_Type=Unsigned32
_Dot1agCfmMepId_Object=MibTableColumn
dot1agCfmMepId=_Dot1agCfmMepId_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,14),_Dot1agCfmMepId_Type())
dot1agCfmMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepId.setStatus(_A)
_Dot1agCfmMepMEPAttachType_Type=Unsigned32
_Dot1agCfmMepMEPAttachType_Object=MibTableColumn
dot1agCfmMepMEPAttachType=_Dot1agCfmMepMEPAttachType_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,15),_Dot1agCfmMepMEPAttachType_Type())
dot1agCfmMepMEPAttachType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepMEPAttachType.setStatus(_A)
_Dot1agCfmMepTunnelId_Type=Unsigned32
_Dot1agCfmMepTunnelId_Object=MibTableColumn
dot1agCfmMepTunnelId=_Dot1agCfmMepTunnelId_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,16),_Dot1agCfmMepTunnelId_Type())
dot1agCfmMepTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepTunnelId.setStatus(_A)
class _Dot1agCfmMepLMFlage_Type(TruthValue):defaultValue=2
_Dot1agCfmMepLMFlage_Type.__name__=_I
_Dot1agCfmMepLMFlage_Object=MibTableColumn
dot1agCfmMepLMFlage=_Dot1agCfmMepLMFlage_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,17),_Dot1agCfmMepLMFlage_Type())
dot1agCfmMepLMFlage.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLMFlage.setStatus(_A)
class _Dot1agCfmMepDMFlage_Type(TruthValue):defaultValue=2
_Dot1agCfmMepDMFlage_Type.__name__=_I
_Dot1agCfmMepDMFlage_Object=MibTableColumn
dot1agCfmMepDMFlage=_Dot1agCfmMepDMFlage_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,18),_Dot1agCfmMepDMFlage_Type())
dot1agCfmMepDMFlage.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepDMFlage.setStatus(_A)
_Dot1agCfmMepPortName_Type=DisplayString
_Dot1agCfmMepPortName_Object=MibTableColumn
dot1agCfmMepPortName=_Dot1agCfmMepPortName_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,19),_Dot1agCfmMepPortName_Type())
dot1agCfmMepPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepPortName.setStatus(_A)
_Dot1agCfmMepLbrIn_Type=Counter32
_Dot1agCfmMepLbrIn_Object=MibTableColumn
dot1agCfmMepLbrIn=_Dot1agCfmMepLbrIn_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,20),_Dot1agCfmMepLbrIn_Type())
dot1agCfmMepLbrIn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLbrIn.setStatus(_A)
_Dot1agCfmMepLbrInOutOfOrder_Type=Counter32
_Dot1agCfmMepLbrInOutOfOrder_Object=MibTableColumn
dot1agCfmMepLbrInOutOfOrder=_Dot1agCfmMepLbrInOutOfOrder_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,21),_Dot1agCfmMepLbrInOutOfOrder_Type())
dot1agCfmMepLbrInOutOfOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLbrInOutOfOrder.setStatus(_A)
_Dot1agCfmMepLbrBadMsdu_Type=Counter32
_Dot1agCfmMepLbrBadMsdu_Object=MibTableColumn
dot1agCfmMepLbrBadMsdu=_Dot1agCfmMepLbrBadMsdu_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,22),_Dot1agCfmMepLbrBadMsdu_Type())
dot1agCfmMepLbrBadMsdu.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLbrBadMsdu.setStatus(_A)
_Dot1agCfmMepLtmNextSeqNumber_Type=Unsigned32
_Dot1agCfmMepLtmNextSeqNumber_Object=MibTableColumn
dot1agCfmMepLtmNextSeqNumber=_Dot1agCfmMepLtmNextSeqNumber_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,23),_Dot1agCfmMepLtmNextSeqNumber_Type())
dot1agCfmMepLtmNextSeqNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLtmNextSeqNumber.setStatus(_A)
_Dot1agCfmMepUnexpLtrIn_Type=Counter32
_Dot1agCfmMepUnexpLtrIn_Object=MibTableColumn
dot1agCfmMepUnexpLtrIn=_Dot1agCfmMepUnexpLtrIn_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,24),_Dot1agCfmMepUnexpLtrIn_Type())
dot1agCfmMepUnexpLtrIn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepUnexpLtrIn.setStatus(_A)
_Dot1agCfmMepLbrOut_Type=Counter32
_Dot1agCfmMepLbrOut_Object=MibTableColumn
dot1agCfmMepLbrOut=_Dot1agCfmMepLbrOut_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,25),_Dot1agCfmMepLbrOut_Type())
dot1agCfmMepLbrOut.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepLbrOut.setStatus(_A)
_Dot1agCfmMepRowStatus_Type=RowStatus
_Dot1agCfmMepRowStatus_Object=MibTableColumn
dot1agCfmMepRowStatus=_Dot1agCfmMepRowStatus_Object((1,3,6,1,4,1,3902,3,120,1,3,1,1,26),_Dot1agCfmMepRowStatus_Type())
dot1agCfmMepRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepRowStatus.setStatus(_A)
_Dot1agCfmLtrTable_Object=MibTable
dot1agCfmLtrTable=_Dot1agCfmLtrTable_Object((1,3,6,1,4,1,3902,3,120,1,3,2))
if mibBuilder.loadTexts:dot1agCfmLtrTable.setStatus(_A)
_Dot1agCfmLtrEntry_Object=MibTableRow
dot1agCfmLtrEntry=_Dot1agCfmLtrEntry_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1))
dot1agCfmLtrEntry.setIndexNames((0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:dot1agCfmLtrEntry.setStatus(_A)
class _Dot1agCfmLtrSeqNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Dot1agCfmLtrSeqNumber_Type.__name__=_D
_Dot1agCfmLtrSeqNumber_Object=MibTableColumn
dot1agCfmLtrSeqNumber=_Dot1agCfmLtrSeqNumber_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,1),_Dot1agCfmLtrSeqNumber_Type())
dot1agCfmLtrSeqNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmLtrSeqNumber.setStatus(_A)
class _Dot1agCfmLtrReceiveOrder_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Dot1agCfmLtrReceiveOrder_Type.__name__=_D
_Dot1agCfmLtrReceiveOrder_Object=MibTableColumn
dot1agCfmLtrReceiveOrder=_Dot1agCfmLtrReceiveOrder_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,2),_Dot1agCfmLtrReceiveOrder_Type())
dot1agCfmLtrReceiveOrder.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmLtrReceiveOrder.setStatus(_A)
class _Dot1agCfmLtrTtl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot1agCfmLtrTtl_Type.__name__=_D
_Dot1agCfmLtrTtl_Object=MibTableColumn
dot1agCfmLtrTtl=_Dot1agCfmLtrTtl_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,3),_Dot1agCfmLtrTtl_Type())
dot1agCfmLtrTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrTtl.setStatus(_A)
_Dot1agCfmLtrForwarded_Type=TruthValue
_Dot1agCfmLtrForwarded_Object=MibTableColumn
dot1agCfmLtrForwarded=_Dot1agCfmLtrForwarded_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,4),_Dot1agCfmLtrForwarded_Type())
dot1agCfmLtrForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrForwarded.setStatus(_A)
_Dot1agCfmLtrTerminalMep_Type=TruthValue
_Dot1agCfmLtrTerminalMep_Object=MibTableColumn
dot1agCfmLtrTerminalMep=_Dot1agCfmLtrTerminalMep_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,5),_Dot1agCfmLtrTerminalMep_Type())
dot1agCfmLtrTerminalMep.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrTerminalMep.setStatus(_A)
class _Dot1agCfmLtrLastEgressIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Dot1agCfmLtrLastEgressIdentifier_Type.__name__=_J
_Dot1agCfmLtrLastEgressIdentifier_Object=MibTableColumn
dot1agCfmLtrLastEgressIdentifier=_Dot1agCfmLtrLastEgressIdentifier_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,6),_Dot1agCfmLtrLastEgressIdentifier_Type())
dot1agCfmLtrLastEgressIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrLastEgressIdentifier.setStatus(_A)
class _Dot1agCfmLtrNextEgressIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Dot1agCfmLtrNextEgressIdentifier_Type.__name__=_J
_Dot1agCfmLtrNextEgressIdentifier_Object=MibTableColumn
dot1agCfmLtrNextEgressIdentifier=_Dot1agCfmLtrNextEgressIdentifier_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,7),_Dot1agCfmLtrNextEgressIdentifier_Type())
dot1agCfmLtrNextEgressIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrNextEgressIdentifier.setStatus(_A)
_Dot1agCfmLtrRelay_Type=Dot1agCfmRelayActionFieldValue
_Dot1agCfmLtrRelay_Object=MibTableColumn
dot1agCfmLtrRelay=_Dot1agCfmLtrRelay_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,8),_Dot1agCfmLtrRelay_Type())
dot1agCfmLtrRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrRelay.setStatus(_A)
_Dot1agCfmLtrIngress_Type=Dot1agCfmIngressActionFieldValue
_Dot1agCfmLtrIngress_Object=MibTableColumn
dot1agCfmLtrIngress=_Dot1agCfmLtrIngress_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,9),_Dot1agCfmLtrIngress_Type())
dot1agCfmLtrIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrIngress.setStatus(_A)
_Dot1agCfmLtrIngressMac_Type=MacAddress
_Dot1agCfmLtrIngressMac_Object=MibTableColumn
dot1agCfmLtrIngressMac=_Dot1agCfmLtrIngressMac_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,10),_Dot1agCfmLtrIngressMac_Type())
dot1agCfmLtrIngressMac.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrIngressMac.setStatus(_A)
_Dot1agCfmLtrEgress_Type=Dot1agCfmEgressActionFieldValue
_Dot1agCfmLtrEgress_Object=MibTableColumn
dot1agCfmLtrEgress=_Dot1agCfmLtrEgress_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,11),_Dot1agCfmLtrEgress_Type())
dot1agCfmLtrEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrEgress.setStatus(_A)
_Dot1agCfmLtrEgressMac_Type=MacAddress
_Dot1agCfmLtrEgressMac_Object=MibTableColumn
dot1agCfmLtrEgressMac=_Dot1agCfmLtrEgressMac_Object((1,3,6,1,4,1,3902,3,120,1,3,2,1,12),_Dot1agCfmLtrEgressMac_Type())
dot1agCfmLtrEgressMac.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLtrEgressMac.setStatus(_A)
_Dot1agCfmMepDbTable_Object=MibTable
dot1agCfmMepDbTable=_Dot1agCfmMepDbTable_Object((1,3,6,1,4,1,3902,3,120,1,3,3))
if mibBuilder.loadTexts:dot1agCfmMepDbTable.setStatus(_A)
_Dot1agCfmMepDbEntry_Object=MibTableRow
dot1agCfmMepDbEntry=_Dot1agCfmMepDbEntry_Object((1,3,6,1,4,1,3902,3,120,1,3,3,1))
dot1agCfmMepDbEntry.setIndexNames((0,_C,_E),(0,_C,_H),(0,_C,_Y))
if mibBuilder.loadTexts:dot1agCfmMepDbEntry.setStatus(_A)
_Dot1agCfmMepDbRSessionId_Type=Dot1agCfmSessionId
_Dot1agCfmMepDbRSessionId_Object=MibTableColumn
dot1agCfmMepDbRSessionId=_Dot1agCfmMepDbRSessionId_Object((1,3,6,1,4,1,3902,3,120,1,3,3,1,1),_Dot1agCfmMepDbRSessionId_Type())
dot1agCfmMepDbRSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1agCfmMepDbRSessionId.setStatus(_A)
_Dot1agCfmMepDbMacAddress_Type=MacAddress
_Dot1agCfmMepDbMacAddress_Object=MibTableColumn
dot1agCfmMepDbMacAddress=_Dot1agCfmMepDbMacAddress_Object((1,3,6,1,4,1,3902,3,120,1,3,3,1,2),_Dot1agCfmMepDbMacAddress_Type())
dot1agCfmMepDbMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepDbMacAddress.setStatus(_A)
_Dot1agCfmMepDbRdi_Type=TruthValue
_Dot1agCfmMepDbRdi_Object=MibTableColumn
dot1agCfmMepDbRdi=_Dot1agCfmMepDbRdi_Object((1,3,6,1,4,1,3902,3,120,1,3,3,1,3),_Dot1agCfmMepDbRdi_Type())
dot1agCfmMepDbRdi.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepDbRdi.setStatus(_A)
_Dot1agCfmMepDbId_Type=Unsigned32
_Dot1agCfmMepDbId_Object=MibTableColumn
dot1agCfmMepDbId=_Dot1agCfmMepDbId_Object((1,3,6,1,4,1,3902,3,120,1,3,3,1,4),_Dot1agCfmMepDbId_Type())
dot1agCfmMepDbId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMepDbId.setStatus(_A)
_Dot1agCfmLbrInfo_ObjectIdentity=ObjectIdentity
dot1agCfmLbrInfo=_Dot1agCfmLbrInfo_ObjectIdentity((1,3,6,1,4,1,3902,3,120,1,3,4))
_Dot1agCfmLbrTransId_Type=Dot1agCfmLbrTransId
_Dot1agCfmLbrTransId_Object=MibScalar
dot1agCfmLbrTransId=_Dot1agCfmLbrTransId_Object((1,3,6,1,4,1,3902,3,120,1,3,4,1),_Dot1agCfmLbrTransId_Type())
dot1agCfmLbrTransId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLbrTransId.setStatus(_A)
_Dot1agCfmLbrPrintInfo_Type=DisplayString
_Dot1agCfmLbrPrintInfo_Object=MibScalar
dot1agCfmLbrPrintInfo=_Dot1agCfmLbrPrintInfo_Object((1,3,6,1,4,1,3902,3,120,1,3,4,2),_Dot1agCfmLbrPrintInfo_Type())
dot1agCfmLbrPrintInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmLbrPrintInfo.setStatus(_A)
_Dot1agCfmMipTable_Object=MibTable
dot1agCfmMipTable=_Dot1agCfmMipTable_Object((1,3,6,1,4,1,3902,3,120,1,3,5))
if mibBuilder.loadTexts:dot1agCfmMipTable.setStatus(_A)
_Dot1agCfmMipEntry_Object=MibTableRow
dot1agCfmMipEntry=_Dot1agCfmMipEntry_Object((1,3,6,1,4,1,3902,3,120,1,3,5,1))
dot1agCfmMipEntry.setIndexNames((0,_C,_E),(0,_C,_H),(0,_C,_Z))
if mibBuilder.loadTexts:dot1agCfmMipEntry.setStatus(_A)
_Dot1agCfmMipSessionId_Type=Unsigned32
_Dot1agCfmMipSessionId_Object=MibTableColumn
dot1agCfmMipSessionId=_Dot1agCfmMipSessionId_Object((1,3,6,1,4,1,3902,3,120,1,3,5,1,1),_Dot1agCfmMipSessionId_Type())
dot1agCfmMipSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMipSessionId.setStatus(_A)
_Dot1agCfmMipName_Type=DisplayString
_Dot1agCfmMipName_Object=MibTableColumn
dot1agCfmMipName=_Dot1agCfmMipName_Object((1,3,6,1,4,1,3902,3,120,1,3,5,1,2),_Dot1agCfmMipName_Type())
dot1agCfmMipName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMipName.setStatus(_A)
_Dot1agCfmMipPortName_Type=DisplayString
_Dot1agCfmMipPortName_Object=MibTableColumn
dot1agCfmMipPortName=_Dot1agCfmMipPortName_Object((1,3,6,1,4,1,3902,3,120,1,3,5,1,3),_Dot1agCfmMipPortName_Type())
dot1agCfmMipPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmMipPortName.setStatus(_A)
_Dot1agCfmGloPara_ObjectIdentity=ObjectIdentity
dot1agCfmGloPara=_Dot1agCfmGloPara_ObjectIdentity((1,3,6,1,4,1,3902,3,120,1,4))
_Dot1agCfmGlobalIsEnable_Type=TruthValue
_Dot1agCfmGlobalIsEnable_Object=MibScalar
dot1agCfmGlobalIsEnable=_Dot1agCfmGlobalIsEnable_Object((1,3,6,1,4,1,3902,3,120,1,4,4),_Dot1agCfmGlobalIsEnable_Type())
dot1agCfmGlobalIsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agCfmGlobalIsEnable.setStatus(_A)
dot1agCfmFaultAlarm=NotificationType((1,3,6,1,4,1,3902,3,120,0,1))
dot1agCfmFaultAlarm.setObjects((_C,_a))
if mibBuilder.loadTexts:dot1agCfmFaultAlarm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'InterfaceIndexOrZero':InterfaceIndexOrZero,'VlanIdOrNone':VlanIdOrNone,'VlanId':VlanId,_N:Dot1agCfmMaintDomainNameType,_O:Dot1agCfmMaintDomainName,'Dot1agCfmMaintAssocNameType':Dot1agCfmMaintAssocNameType,'Dot1agCfmMaintAssocName':Dot1agCfmMaintAssocName,_P:Dot1agCfmMDLevel,'Dot1agCfmMpDirection':Dot1agCfmMpDirection,'Dot1agCfmHighestDefectPri':Dot1agCfmHighestDefectPri,_V:Dot1agCfmLowestAlarmPri,'Dot1agCfmSessionId':Dot1agCfmSessionId,_K:Dot1agCfmMhfCreation,_L:Dot1agCfmIdPermission,'Dot1agCfmSpeed':Dot1agCfmSpeed,_Q:Dot1agCfmCcmInterval,_U:Dot1agCfmFngState,'Dot1agCfmRelayActionFieldValue':Dot1agCfmRelayActionFieldValue,'Dot1agCfmIngressActionFieldValue':Dot1agCfmIngressActionFieldValue,'Dot1agCfmEgressActionFieldValue':Dot1agCfmEgressActionFieldValue,'Dot1afCfmIndexIntegerNextFree':Dot1afCfmIndexIntegerNextFree,'Dot1agCfmMepDefects':Dot1agCfmMepDefects,'Dot1agCfmLbrTransId':Dot1agCfmLbrTransId,'zxr10cfmMIB':zxr10cfmMIB,'dot1agNotifications':dot1agNotifications,'dot1agCfmFaultAlarm':dot1agCfmFaultAlarm,'dot1agMIBObjects':dot1agMIBObjects,'dot1agCfmMd':dot1agCfmMd,'dot1agCfmMdTableNextIndex':dot1agCfmMdTableNextIndex,'dot1agCfmMdTable':dot1agCfmMdTable,'dot1agCfmMdEntry':dot1agCfmMdEntry,_E:dot1agCfmMdIndex,'dot1agCfmMdFormat':dot1agCfmMdFormat,'dot1agCfmMdName':dot1agCfmMdName,'dot1agCfmMdMdLevel':dot1agCfmMdMdLevel,'dot1agCfmMdMhfCreation':dot1agCfmMdMhfCreation,'dot1agCfmMdMhfIdPermission':dot1agCfmMdMhfIdPermission,'dot1agCfmMdMaTableNextIndex':dot1agCfmMdMaTableNextIndex,'dot1agCfmMdRowStatus':dot1agCfmMdRowStatus,'dot1agCfmMa':dot1agCfmMa,'dot1agCfmMaTable':dot1agCfmMaTable,'dot1agCfmMaEntry':dot1agCfmMaEntry,_H:dot1agCfmMaIndex,'dot1agCfmMaPrimaryVlanId':dot1agCfmMaPrimaryVlanId,'dot1agCfmMaFormat':dot1agCfmMaFormat,'dot1agCfmMaName':dot1agCfmMaName,'dot1agCfmMaMhfCreation':dot1agCfmMaMhfCreation,'dot1agCfmMaIdPermission':dot1agCfmMaIdPermission,'dot1agCfmMaCcmInterval':dot1agCfmMaCcmInterval,'dot1agCfmMaRowStatus':dot1agCfmMaRowStatus,'dot1agCfmMASpeed':dot1agCfmMASpeed,'dot1agCfmMaVlanListTable':dot1agCfmMaVlanListTable,'dot1agCfmMaVlanListEntry':dot1agCfmMaVlanListEntry,_R:dot1agCfmMaVlanListIdentifier,'dot1agCfmMaVlanListRowStatus':dot1agCfmMaVlanListRowStatus,'dot1agCfmMaMepListTable':dot1agCfmMaMepListTable,'dot1agCfmMaMepListEntry':dot1agCfmMaMepListEntry,_S:dot1agCfmMaMepListSessionId,'dot1agCfmMaMepListRowStatus':dot1agCfmMaMepListRowStatus,'dot1agCfmMep':dot1agCfmMep,'dot1agCfmMepTable':dot1agCfmMepTable,'dot1agCfmMepEntry':dot1agCfmMepEntry,_T:dot1agCfmSessionId,'dot1agCfmMepIfIndex':dot1agCfmMepIfIndex,'dot1agCfmMepDirection':dot1agCfmMepDirection,'dot1agCfmMepPrimaryVid':dot1agCfmMepPrimaryVid,'dot1agCfmMepActive':dot1agCfmMepActive,'dot1agCfmMepFngState':dot1agCfmMepFngState,'dot1agCfmMepCciEnabled':dot1agCfmMepCciEnabled,'dot1agCfmMepCcmLtmPriority':dot1agCfmMepCcmLtmPriority,'dot1agCfmMepMacAddress':dot1agCfmMepMacAddress,'dot1agCfmMepLowPrDef':dot1agCfmMepLowPrDef,_a:dot1agCfmMepHighestPrDefect,'dot1agCfmMepDefects':dot1agCfmMepDefects,'dot1agCfmMepCciSentCcms':dot1agCfmMepCciSentCcms,'dot1agCfmMepId':dot1agCfmMepId,'dot1agCfmMepMEPAttachType':dot1agCfmMepMEPAttachType,'dot1agCfmMepTunnelId':dot1agCfmMepTunnelId,'dot1agCfmMepLMFlage':dot1agCfmMepLMFlage,'dot1agCfmMepDMFlage':dot1agCfmMepDMFlage,'dot1agCfmMepPortName':dot1agCfmMepPortName,'dot1agCfmMepLbrIn':dot1agCfmMepLbrIn,'dot1agCfmMepLbrInOutOfOrder':dot1agCfmMepLbrInOutOfOrder,'dot1agCfmMepLbrBadMsdu':dot1agCfmMepLbrBadMsdu,'dot1agCfmMepLtmNextSeqNumber':dot1agCfmMepLtmNextSeqNumber,'dot1agCfmMepUnexpLtrIn':dot1agCfmMepUnexpLtrIn,'dot1agCfmMepLbrOut':dot1agCfmMepLbrOut,'dot1agCfmMepRowStatus':dot1agCfmMepRowStatus,'dot1agCfmLtrTable':dot1agCfmLtrTable,'dot1agCfmLtrEntry':dot1agCfmLtrEntry,_W:dot1agCfmLtrSeqNumber,_X:dot1agCfmLtrReceiveOrder,'dot1agCfmLtrTtl':dot1agCfmLtrTtl,'dot1agCfmLtrForwarded':dot1agCfmLtrForwarded,'dot1agCfmLtrTerminalMep':dot1agCfmLtrTerminalMep,'dot1agCfmLtrLastEgressIdentifier':dot1agCfmLtrLastEgressIdentifier,'dot1agCfmLtrNextEgressIdentifier':dot1agCfmLtrNextEgressIdentifier,'dot1agCfmLtrRelay':dot1agCfmLtrRelay,'dot1agCfmLtrIngress':dot1agCfmLtrIngress,'dot1agCfmLtrIngressMac':dot1agCfmLtrIngressMac,'dot1agCfmLtrEgress':dot1agCfmLtrEgress,'dot1agCfmLtrEgressMac':dot1agCfmLtrEgressMac,'dot1agCfmMepDbTable':dot1agCfmMepDbTable,'dot1agCfmMepDbEntry':dot1agCfmMepDbEntry,_Y:dot1agCfmMepDbRSessionId,'dot1agCfmMepDbMacAddress':dot1agCfmMepDbMacAddress,'dot1agCfmMepDbRdi':dot1agCfmMepDbRdi,'dot1agCfmMepDbId':dot1agCfmMepDbId,'dot1agCfmLbrInfo':dot1agCfmLbrInfo,'dot1agCfmLbrTransId':dot1agCfmLbrTransId,'dot1agCfmLbrPrintInfo':dot1agCfmLbrPrintInfo,'dot1agCfmMipTable':dot1agCfmMipTable,'dot1agCfmMipEntry':dot1agCfmMipEntry,_Z:dot1agCfmMipSessionId,'dot1agCfmMipName':dot1agCfmMipName,'dot1agCfmMipPortName':dot1agCfmMipPortName,'dot1agCfmGloPara':dot1agCfmGloPara,'dot1agCfmGlobalIsEnable':dot1agCfmGlobalIsEnable})