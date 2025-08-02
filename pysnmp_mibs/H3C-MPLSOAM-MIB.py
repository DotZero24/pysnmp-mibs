_O='h3cMplsOamEgrIndex'
_N='read-only'
_M='private'
_L='not-accessible'
_K='h3cMplsOamIgrIndex'
_J='read-write'
_I='h3cMplsOamEgrDefectType'
_H='h3cMplsOamEgrLspName'
_G='h3cMplsOamIgrDefectType'
_F='h3cMplsOamIgrLspName'
_E='TruthValue'
_D='Integer32'
_C='H3C-MPLSOAM-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
h3cMplsOam=ModuleIdentity((1,3,6,1,4,1,2011,10,2,79))
class H3cMplsOAMDefectType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('dServer',1),('dPeerMe',2),('dLOCV',3),('dTTSIMismatch',4),('dTTSIMismerge',5),('dExcess',6),('dUnknown',7),('dRlsnDown',8),('dLspDown',9),('dME',10),('noDefect',11)))
class H3cMplsOAMDetectFreq(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ffd10ms',1),('ffd20ms',2),('ffd50ms',3),('ffd100ms',4),('ffd200ms',5),('ffd500ms',6),('cv1000ms',7)))
_H3cMplsOamScalarGroup_ObjectIdentity=ObjectIdentity
h3cMplsOamScalarGroup=_H3cMplsOamScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,79,1))
class _H3cMplsOamCapability_Type(TruthValue):defaultValue=2
_H3cMplsOamCapability_Type.__name__=_E
_H3cMplsOamCapability_Object=MibScalar
h3cMplsOamCapability=_H3cMplsOamCapability_Object((1,3,6,1,4,1,2011,10,2,79,1,1),_H3cMplsOamCapability_Type())
h3cMplsOamCapability.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cMplsOamCapability.setStatus(_A)
class _H3cMplsOamTrapOpen_Type(TruthValue):defaultValue=2
_H3cMplsOamTrapOpen_Type.__name__=_E
_H3cMplsOamTrapOpen_Object=MibScalar
h3cMplsOamTrapOpen=_H3cMplsOamTrapOpen_Object((1,3,6,1,4,1,2011,10,2,79,1,2),_H3cMplsOamTrapOpen_Type())
h3cMplsOamTrapOpen.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cMplsOamTrapOpen.setStatus(_A)
_H3cMplsOamTable_ObjectIdentity=ObjectIdentity
h3cMplsOamTable=_H3cMplsOamTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,79,2))
_H3cMplsOamIgrTable_Object=MibTable
h3cMplsOamIgrTable=_H3cMplsOamIgrTable_Object((1,3,6,1,4,1,2011,10,2,79,2,1))
if mibBuilder.loadTexts:h3cMplsOamIgrTable.setStatus(_A)
_H3cMplsOamIgrEntry_Object=MibTableRow
h3cMplsOamIgrEntry=_H3cMplsOamIgrEntry_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1))
h3cMplsOamIgrEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:h3cMplsOamIgrEntry.setStatus(_A)
_H3cMplsOamIgrIndex_Type=Unsigned32
_H3cMplsOamIgrIndex_Object=MibTableColumn
h3cMplsOamIgrIndex=_H3cMplsOamIgrIndex_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,1),_H3cMplsOamIgrIndex_Type())
h3cMplsOamIgrIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cMplsOamIgrIndex.setStatus(_A)
_H3cMplsOamIgrLspName_Type=OctetString
_H3cMplsOamIgrLspName_Object=MibTableColumn
h3cMplsOamIgrLspName=_H3cMplsOamIgrLspName_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,2),_H3cMplsOamIgrLspName_Type())
h3cMplsOamIgrLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrLspName.setStatus(_A)
class _H3cMplsOamIgrDetectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cv',1),('ffd',2)))
_H3cMplsOamIgrDetectType_Type.__name__=_D
_H3cMplsOamIgrDetectType_Object=MibTableColumn
h3cMplsOamIgrDetectType=_H3cMplsOamIgrDetectType_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,3),_H3cMplsOamIgrDetectType_Type())
h3cMplsOamIgrDetectType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrDetectType.setStatus(_A)
_H3cMplsOamIgrDetectFreq_Type=H3cMplsOAMDetectFreq
_H3cMplsOamIgrDetectFreq_Object=MibTableColumn
h3cMplsOamIgrDetectFreq=_H3cMplsOamIgrDetectFreq_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,4),_H3cMplsOamIgrDetectFreq_Type())
h3cMplsOamIgrDetectFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrDetectFreq.setStatus(_A)
class _H3cMplsOamIgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('share',2)))
_H3cMplsOamIgrRevType_Type.__name__=_D
_H3cMplsOamIgrRevType_Object=MibTableColumn
h3cMplsOamIgrRevType=_H3cMplsOamIgrRevType_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,5),_H3cMplsOamIgrRevType_Type())
h3cMplsOamIgrRevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrRevType.setStatus(_A)
_H3cMplsOamIgrRevLspName_Type=OctetString
_H3cMplsOamIgrRevLspName_Object=MibTableColumn
h3cMplsOamIgrRevLspName=_H3cMplsOamIgrRevLspName_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,6),_H3cMplsOamIgrRevLspName_Type())
h3cMplsOamIgrRevLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrRevLspName.setStatus(_A)
_H3cMplsOamIgrLspId_Type=Integer32
_H3cMplsOamIgrLspId_Object=MibTableColumn
h3cMplsOamIgrLspId=_H3cMplsOamIgrLspId_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,7),_H3cMplsOamIgrLspId_Type())
h3cMplsOamIgrLspId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrLspId.setStatus(_A)
class _H3cMplsOamIgrEnable_Type(TruthValue):defaultValue=2
_H3cMplsOamIgrEnable_Type.__name__=_E
_H3cMplsOamIgrEnable_Object=MibTableColumn
h3cMplsOamIgrEnable=_H3cMplsOamIgrEnable_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,8),_H3cMplsOamIgrEnable_Type())
h3cMplsOamIgrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrEnable.setStatus(_A)
_H3cMplsOamIgrDefectType_Type=H3cMplsOAMDefectType
_H3cMplsOamIgrDefectType_Object=MibTableColumn
h3cMplsOamIgrDefectType=_H3cMplsOamIgrDefectType_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,9),_H3cMplsOamIgrDefectType_Type())
h3cMplsOamIgrDefectType.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cMplsOamIgrDefectType.setStatus(_A)
_H3cMplsOamIgrRowStatus_Type=RowStatus
_H3cMplsOamIgrRowStatus_Object=MibTableColumn
h3cMplsOamIgrRowStatus=_H3cMplsOamIgrRowStatus_Object((1,3,6,1,4,1,2011,10,2,79,2,1,1,10),_H3cMplsOamIgrRowStatus_Type())
h3cMplsOamIgrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamIgrRowStatus.setStatus(_A)
_H3cMplsOamEgrTable_Object=MibTable
h3cMplsOamEgrTable=_H3cMplsOamEgrTable_Object((1,3,6,1,4,1,2011,10,2,79,2,2))
if mibBuilder.loadTexts:h3cMplsOamEgrTable.setStatus(_A)
_H3cMplsOamEgrEntry_Object=MibTableRow
h3cMplsOamEgrEntry=_H3cMplsOamEgrEntry_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1))
h3cMplsOamEgrEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:h3cMplsOamEgrEntry.setStatus(_A)
_H3cMplsOamEgrIndex_Type=Unsigned32
_H3cMplsOamEgrIndex_Object=MibTableColumn
h3cMplsOamEgrIndex=_H3cMplsOamEgrIndex_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,1),_H3cMplsOamEgrIndex_Type())
h3cMplsOamEgrIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cMplsOamEgrIndex.setStatus(_A)
_H3cMplsOamEgrLspName_Type=OctetString
_H3cMplsOamEgrLspName_Object=MibTableColumn
h3cMplsOamEgrLspName=_H3cMplsOamEgrLspName_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,2),_H3cMplsOamEgrLspName_Type())
h3cMplsOamEgrLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrLspName.setStatus(_A)
class _H3cMplsOamEgrDetectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cv',1),('ffd',2)))
_H3cMplsOamEgrDetectType_Type.__name__=_D
_H3cMplsOamEgrDetectType_Object=MibTableColumn
h3cMplsOamEgrDetectType=_H3cMplsOamEgrDetectType_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,3),_H3cMplsOamEgrDetectType_Type())
h3cMplsOamEgrDetectType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrDetectType.setStatus(_A)
_H3cMplsOamEgrDetectFreq_Type=H3cMplsOAMDetectFreq
_H3cMplsOamEgrDetectFreq_Object=MibTableColumn
h3cMplsOamEgrDetectFreq=_H3cMplsOamEgrDetectFreq_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,4),_H3cMplsOamEgrDetectFreq_Type())
h3cMplsOamEgrDetectFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrDetectFreq.setStatus(_A)
class _H3cMplsOamEgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('share',2)))
_H3cMplsOamEgrRevType_Type.__name__=_D
_H3cMplsOamEgrRevType_Object=MibTableColumn
h3cMplsOamEgrRevType=_H3cMplsOamEgrRevType_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,5),_H3cMplsOamEgrRevType_Type())
h3cMplsOamEgrRevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrRevType.setStatus(_A)
_H3cMplsOamEgrRevLspName_Type=OctetString
_H3cMplsOamEgrRevLspName_Object=MibTableColumn
h3cMplsOamEgrRevLspName=_H3cMplsOamEgrRevLspName_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,6),_H3cMplsOamEgrRevLspName_Type())
h3cMplsOamEgrRevLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrRevLspName.setStatus(_A)
_H3cMplsOamEgrLsrId_Type=IpAddress
_H3cMplsOamEgrLsrId_Object=MibTableColumn
h3cMplsOamEgrLsrId=_H3cMplsOamEgrLsrId_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,7),_H3cMplsOamEgrLsrId_Type())
h3cMplsOamEgrLsrId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrLsrId.setStatus(_A)
_H3cMplsOamEgrLspId_Type=Integer32
_H3cMplsOamEgrLspId_Object=MibTableColumn
h3cMplsOamEgrLspId=_H3cMplsOamEgrLspId_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,8),_H3cMplsOamEgrLspId_Type())
h3cMplsOamEgrLspId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrLspId.setStatus(_A)
class _H3cMplsOamEgrEnable_Type(TruthValue):defaultValue=2
_H3cMplsOamEgrEnable_Type.__name__=_E
_H3cMplsOamEgrEnable_Object=MibTableColumn
h3cMplsOamEgrEnable=_H3cMplsOamEgrEnable_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,9),_H3cMplsOamEgrEnable_Type())
h3cMplsOamEgrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrEnable.setStatus(_A)
_H3cMplsOamEgrDefectType_Type=H3cMplsOAMDefectType
_H3cMplsOamEgrDefectType_Object=MibTableColumn
h3cMplsOamEgrDefectType=_H3cMplsOamEgrDefectType_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,10),_H3cMplsOamEgrDefectType_Type())
h3cMplsOamEgrDefectType.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cMplsOamEgrDefectType.setStatus(_A)
_H3cMplsOamEgrRowStatus_Type=RowStatus
_H3cMplsOamEgrRowStatus_Object=MibTableColumn
h3cMplsOamEgrRowStatus=_H3cMplsOamEgrRowStatus_Object((1,3,6,1,4,1,2011,10,2,79,2,2,1,11),_H3cMplsOamEgrRowStatus_Type())
h3cMplsOamEgrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsOamEgrRowStatus.setStatus(_A)
_H3cMplsOamNotifications_ObjectIdentity=ObjectIdentity
h3cMplsOamNotifications=_H3cMplsOamNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,79,3))
h3cMplsOamIgrLSPOutDefect=NotificationType((1,3,6,1,4,1,2011,10,2,79,3,1))
h3cMplsOamIgrLSPOutDefect.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cMplsOamIgrLSPOutDefect.setStatus(_A)
h3cMplsOamIgrLSPInDefect=NotificationType((1,3,6,1,4,1,2011,10,2,79,3,2))
h3cMplsOamIgrLSPInDefect.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cMplsOamIgrLSPInDefect.setStatus(_A)
h3cMplsOamEgrLSPOutDefect=NotificationType((1,3,6,1,4,1,2011,10,2,79,3,3))
h3cMplsOamEgrLSPOutDefect.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:h3cMplsOamEgrLSPOutDefect.setStatus(_A)
h3cMplsOamEgrLSPInDefect=NotificationType((1,3,6,1,4,1,2011,10,2,79,3,4))
h3cMplsOamEgrLSPInDefect.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:h3cMplsOamEgrLSPInDefect.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'H3cMplsOAMDefectType':H3cMplsOAMDefectType,'H3cMplsOAMDetectFreq':H3cMplsOAMDetectFreq,'h3cMplsOam':h3cMplsOam,'h3cMplsOamScalarGroup':h3cMplsOamScalarGroup,'h3cMplsOamCapability':h3cMplsOamCapability,'h3cMplsOamTrapOpen':h3cMplsOamTrapOpen,'h3cMplsOamTable':h3cMplsOamTable,'h3cMplsOamIgrTable':h3cMplsOamIgrTable,'h3cMplsOamIgrEntry':h3cMplsOamIgrEntry,_K:h3cMplsOamIgrIndex,_F:h3cMplsOamIgrLspName,'h3cMplsOamIgrDetectType':h3cMplsOamIgrDetectType,'h3cMplsOamIgrDetectFreq':h3cMplsOamIgrDetectFreq,'h3cMplsOamIgrRevType':h3cMplsOamIgrRevType,'h3cMplsOamIgrRevLspName':h3cMplsOamIgrRevLspName,'h3cMplsOamIgrLspId':h3cMplsOamIgrLspId,'h3cMplsOamIgrEnable':h3cMplsOamIgrEnable,_G:h3cMplsOamIgrDefectType,'h3cMplsOamIgrRowStatus':h3cMplsOamIgrRowStatus,'h3cMplsOamEgrTable':h3cMplsOamEgrTable,'h3cMplsOamEgrEntry':h3cMplsOamEgrEntry,_O:h3cMplsOamEgrIndex,_H:h3cMplsOamEgrLspName,'h3cMplsOamEgrDetectType':h3cMplsOamEgrDetectType,'h3cMplsOamEgrDetectFreq':h3cMplsOamEgrDetectFreq,'h3cMplsOamEgrRevType':h3cMplsOamEgrRevType,'h3cMplsOamEgrRevLspName':h3cMplsOamEgrRevLspName,'h3cMplsOamEgrLsrId':h3cMplsOamEgrLsrId,'h3cMplsOamEgrLspId':h3cMplsOamEgrLspId,'h3cMplsOamEgrEnable':h3cMplsOamEgrEnable,_I:h3cMplsOamEgrDefectType,'h3cMplsOamEgrRowStatus':h3cMplsOamEgrRowStatus,'h3cMplsOamNotifications':h3cMplsOamNotifications,'h3cMplsOamIgrLSPOutDefect':h3cMplsOamIgrLSPOutDefect,'h3cMplsOamIgrLSPInDefect':h3cMplsOamIgrLSPInDefect,'h3cMplsOamEgrLSPOutDefect':h3cMplsOamEgrLSPOutDefect,'h3cMplsOamEgrLSPInDefect':h3cMplsOamEgrLSPInDefect})