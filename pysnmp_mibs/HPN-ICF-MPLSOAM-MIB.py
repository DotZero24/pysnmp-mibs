_O='hpnicfMplsOamEgrIndex'
_N='read-only'
_M='private'
_L='not-accessible'
_K='hpnicfMplsOamIgrIndex'
_J='read-write'
_I='hpnicfMplsOamEgrDefectType'
_H='hpnicfMplsOamEgrLspName'
_G='hpnicfMplsOamIgrDefectType'
_F='hpnicfMplsOamIgrLspName'
_E='TruthValue'
_D='Integer32'
_C='HPN-ICF-MPLSOAM-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
hpnicfMplsOam=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,79))
class HpnicfMplsOAMDefectType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('dServer',1),('dPeerMe',2),('dLOCV',3),('dTTSIMismatch',4),('dTTSIMismerge',5),('dExcess',6),('dUnknown',7),('dRlsnDown',8),('dLspDown',9),('dME',10),('noDefect',11)))
class HpnicfMplsOAMDetectFreq(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ffd10ms',1),('ffd20ms',2),('ffd50ms',3),('ffd100ms',4),('ffd200ms',5),('ffd500ms',6),('cv1000ms',7)))
_HpnicfMplsOamScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfMplsOamScalarGroup=_HpnicfMplsOamScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,79,1))
class _HpnicfMplsOamCapability_Type(TruthValue):defaultValue=2
_HpnicfMplsOamCapability_Type.__name__=_E
_HpnicfMplsOamCapability_Object=MibScalar
hpnicfMplsOamCapability=_HpnicfMplsOamCapability_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,1,1),_HpnicfMplsOamCapability_Type())
hpnicfMplsOamCapability.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfMplsOamCapability.setStatus(_A)
class _HpnicfMplsOamTrapOpen_Type(TruthValue):defaultValue=2
_HpnicfMplsOamTrapOpen_Type.__name__=_E
_HpnicfMplsOamTrapOpen_Object=MibScalar
hpnicfMplsOamTrapOpen=_HpnicfMplsOamTrapOpen_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,1,2),_HpnicfMplsOamTrapOpen_Type())
hpnicfMplsOamTrapOpen.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfMplsOamTrapOpen.setStatus(_A)
_HpnicfMplsOamTable_ObjectIdentity=ObjectIdentity
hpnicfMplsOamTable=_HpnicfMplsOamTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,79,2))
_HpnicfMplsOamIgrTable_Object=MibTable
hpnicfMplsOamIgrTable=_HpnicfMplsOamIgrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1))
if mibBuilder.loadTexts:hpnicfMplsOamIgrTable.setStatus(_A)
_HpnicfMplsOamIgrEntry_Object=MibTableRow
hpnicfMplsOamIgrEntry=_HpnicfMplsOamIgrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1))
hpnicfMplsOamIgrEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:hpnicfMplsOamIgrEntry.setStatus(_A)
_HpnicfMplsOamIgrIndex_Type=Unsigned32
_HpnicfMplsOamIgrIndex_Object=MibTableColumn
hpnicfMplsOamIgrIndex=_HpnicfMplsOamIgrIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,1),_HpnicfMplsOamIgrIndex_Type())
hpnicfMplsOamIgrIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfMplsOamIgrIndex.setStatus(_A)
_HpnicfMplsOamIgrLspName_Type=OctetString
_HpnicfMplsOamIgrLspName_Object=MibTableColumn
hpnicfMplsOamIgrLspName=_HpnicfMplsOamIgrLspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,2),_HpnicfMplsOamIgrLspName_Type())
hpnicfMplsOamIgrLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrLspName.setStatus(_A)
class _HpnicfMplsOamIgrDetectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cv',1),('ffd',2)))
_HpnicfMplsOamIgrDetectType_Type.__name__=_D
_HpnicfMplsOamIgrDetectType_Object=MibTableColumn
hpnicfMplsOamIgrDetectType=_HpnicfMplsOamIgrDetectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,3),_HpnicfMplsOamIgrDetectType_Type())
hpnicfMplsOamIgrDetectType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrDetectType.setStatus(_A)
_HpnicfMplsOamIgrDetectFreq_Type=HpnicfMplsOAMDetectFreq
_HpnicfMplsOamIgrDetectFreq_Object=MibTableColumn
hpnicfMplsOamIgrDetectFreq=_HpnicfMplsOamIgrDetectFreq_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,4),_HpnicfMplsOamIgrDetectFreq_Type())
hpnicfMplsOamIgrDetectFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrDetectFreq.setStatus(_A)
class _HpnicfMplsOamIgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('share',2)))
_HpnicfMplsOamIgrRevType_Type.__name__=_D
_HpnicfMplsOamIgrRevType_Object=MibTableColumn
hpnicfMplsOamIgrRevType=_HpnicfMplsOamIgrRevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,5),_HpnicfMplsOamIgrRevType_Type())
hpnicfMplsOamIgrRevType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrRevType.setStatus(_A)
_HpnicfMplsOamIgrRevLspName_Type=OctetString
_HpnicfMplsOamIgrRevLspName_Object=MibTableColumn
hpnicfMplsOamIgrRevLspName=_HpnicfMplsOamIgrRevLspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,6),_HpnicfMplsOamIgrRevLspName_Type())
hpnicfMplsOamIgrRevLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrRevLspName.setStatus(_A)
_HpnicfMplsOamIgrLspId_Type=Integer32
_HpnicfMplsOamIgrLspId_Object=MibTableColumn
hpnicfMplsOamIgrLspId=_HpnicfMplsOamIgrLspId_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,7),_HpnicfMplsOamIgrLspId_Type())
hpnicfMplsOamIgrLspId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrLspId.setStatus(_A)
class _HpnicfMplsOamIgrEnable_Type(TruthValue):defaultValue=2
_HpnicfMplsOamIgrEnable_Type.__name__=_E
_HpnicfMplsOamIgrEnable_Object=MibTableColumn
hpnicfMplsOamIgrEnable=_HpnicfMplsOamIgrEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,8),_HpnicfMplsOamIgrEnable_Type())
hpnicfMplsOamIgrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrEnable.setStatus(_A)
_HpnicfMplsOamIgrDefectType_Type=HpnicfMplsOAMDefectType
_HpnicfMplsOamIgrDefectType_Object=MibTableColumn
hpnicfMplsOamIgrDefectType=_HpnicfMplsOamIgrDefectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,9),_HpnicfMplsOamIgrDefectType_Type())
hpnicfMplsOamIgrDefectType.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfMplsOamIgrDefectType.setStatus(_A)
_HpnicfMplsOamIgrRowStatus_Type=RowStatus
_HpnicfMplsOamIgrRowStatus_Object=MibTableColumn
hpnicfMplsOamIgrRowStatus=_HpnicfMplsOamIgrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,1,1,10),_HpnicfMplsOamIgrRowStatus_Type())
hpnicfMplsOamIgrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamIgrRowStatus.setStatus(_A)
_HpnicfMplsOamEgrTable_Object=MibTable
hpnicfMplsOamEgrTable=_HpnicfMplsOamEgrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2))
if mibBuilder.loadTexts:hpnicfMplsOamEgrTable.setStatus(_A)
_HpnicfMplsOamEgrEntry_Object=MibTableRow
hpnicfMplsOamEgrEntry=_HpnicfMplsOamEgrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1))
hpnicfMplsOamEgrEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:hpnicfMplsOamEgrEntry.setStatus(_A)
_HpnicfMplsOamEgrIndex_Type=Unsigned32
_HpnicfMplsOamEgrIndex_Object=MibTableColumn
hpnicfMplsOamEgrIndex=_HpnicfMplsOamEgrIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,1),_HpnicfMplsOamEgrIndex_Type())
hpnicfMplsOamEgrIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfMplsOamEgrIndex.setStatus(_A)
_HpnicfMplsOamEgrLspName_Type=OctetString
_HpnicfMplsOamEgrLspName_Object=MibTableColumn
hpnicfMplsOamEgrLspName=_HpnicfMplsOamEgrLspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,2),_HpnicfMplsOamEgrLspName_Type())
hpnicfMplsOamEgrLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrLspName.setStatus(_A)
class _HpnicfMplsOamEgrDetectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cv',1),('ffd',2)))
_HpnicfMplsOamEgrDetectType_Type.__name__=_D
_HpnicfMplsOamEgrDetectType_Object=MibTableColumn
hpnicfMplsOamEgrDetectType=_HpnicfMplsOamEgrDetectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,3),_HpnicfMplsOamEgrDetectType_Type())
hpnicfMplsOamEgrDetectType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrDetectType.setStatus(_A)
_HpnicfMplsOamEgrDetectFreq_Type=HpnicfMplsOAMDetectFreq
_HpnicfMplsOamEgrDetectFreq_Object=MibTableColumn
hpnicfMplsOamEgrDetectFreq=_HpnicfMplsOamEgrDetectFreq_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,4),_HpnicfMplsOamEgrDetectFreq_Type())
hpnicfMplsOamEgrDetectFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrDetectFreq.setStatus(_A)
class _HpnicfMplsOamEgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('share',2)))
_HpnicfMplsOamEgrRevType_Type.__name__=_D
_HpnicfMplsOamEgrRevType_Object=MibTableColumn
hpnicfMplsOamEgrRevType=_HpnicfMplsOamEgrRevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,5),_HpnicfMplsOamEgrRevType_Type())
hpnicfMplsOamEgrRevType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrRevType.setStatus(_A)
_HpnicfMplsOamEgrRevLspName_Type=OctetString
_HpnicfMplsOamEgrRevLspName_Object=MibTableColumn
hpnicfMplsOamEgrRevLspName=_HpnicfMplsOamEgrRevLspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,6),_HpnicfMplsOamEgrRevLspName_Type())
hpnicfMplsOamEgrRevLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrRevLspName.setStatus(_A)
_HpnicfMplsOamEgrLsrId_Type=IpAddress
_HpnicfMplsOamEgrLsrId_Object=MibTableColumn
hpnicfMplsOamEgrLsrId=_HpnicfMplsOamEgrLsrId_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,7),_HpnicfMplsOamEgrLsrId_Type())
hpnicfMplsOamEgrLsrId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrLsrId.setStatus(_A)
_HpnicfMplsOamEgrLspId_Type=Integer32
_HpnicfMplsOamEgrLspId_Object=MibTableColumn
hpnicfMplsOamEgrLspId=_HpnicfMplsOamEgrLspId_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,8),_HpnicfMplsOamEgrLspId_Type())
hpnicfMplsOamEgrLspId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrLspId.setStatus(_A)
class _HpnicfMplsOamEgrEnable_Type(TruthValue):defaultValue=2
_HpnicfMplsOamEgrEnable_Type.__name__=_E
_HpnicfMplsOamEgrEnable_Object=MibTableColumn
hpnicfMplsOamEgrEnable=_HpnicfMplsOamEgrEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,9),_HpnicfMplsOamEgrEnable_Type())
hpnicfMplsOamEgrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrEnable.setStatus(_A)
_HpnicfMplsOamEgrDefectType_Type=HpnicfMplsOAMDefectType
_HpnicfMplsOamEgrDefectType_Object=MibTableColumn
hpnicfMplsOamEgrDefectType=_HpnicfMplsOamEgrDefectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,10),_HpnicfMplsOamEgrDefectType_Type())
hpnicfMplsOamEgrDefectType.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfMplsOamEgrDefectType.setStatus(_A)
_HpnicfMplsOamEgrRowStatus_Type=RowStatus
_HpnicfMplsOamEgrRowStatus_Object=MibTableColumn
hpnicfMplsOamEgrRowStatus=_HpnicfMplsOamEgrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,79,2,2,1,11),_HpnicfMplsOamEgrRowStatus_Type())
hpnicfMplsOamEgrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsOamEgrRowStatus.setStatus(_A)
_HpnicfMplsOamNotifications_ObjectIdentity=ObjectIdentity
hpnicfMplsOamNotifications=_HpnicfMplsOamNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,79,3))
hpnicfMplsOamIgrLSPOutDefect=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,79,3,1))
hpnicfMplsOamIgrLSPOutDefect.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfMplsOamIgrLSPOutDefect.setStatus(_A)
hpnicfMplsOamIgrLSPInDefect=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,79,3,2))
hpnicfMplsOamIgrLSPInDefect.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfMplsOamIgrLSPInDefect.setStatus(_A)
hpnicfMplsOamEgrLSPOutDefect=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,79,3,3))
hpnicfMplsOamEgrLSPOutDefect.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:hpnicfMplsOamEgrLSPOutDefect.setStatus(_A)
hpnicfMplsOamEgrLSPInDefect=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,79,3,4))
hpnicfMplsOamEgrLSPInDefect.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:hpnicfMplsOamEgrLSPInDefect.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfMplsOAMDefectType':HpnicfMplsOAMDefectType,'HpnicfMplsOAMDetectFreq':HpnicfMplsOAMDetectFreq,'hpnicfMplsOam':hpnicfMplsOam,'hpnicfMplsOamScalarGroup':hpnicfMplsOamScalarGroup,'hpnicfMplsOamCapability':hpnicfMplsOamCapability,'hpnicfMplsOamTrapOpen':hpnicfMplsOamTrapOpen,'hpnicfMplsOamTable':hpnicfMplsOamTable,'hpnicfMplsOamIgrTable':hpnicfMplsOamIgrTable,'hpnicfMplsOamIgrEntry':hpnicfMplsOamIgrEntry,_K:hpnicfMplsOamIgrIndex,_F:hpnicfMplsOamIgrLspName,'hpnicfMplsOamIgrDetectType':hpnicfMplsOamIgrDetectType,'hpnicfMplsOamIgrDetectFreq':hpnicfMplsOamIgrDetectFreq,'hpnicfMplsOamIgrRevType':hpnicfMplsOamIgrRevType,'hpnicfMplsOamIgrRevLspName':hpnicfMplsOamIgrRevLspName,'hpnicfMplsOamIgrLspId':hpnicfMplsOamIgrLspId,'hpnicfMplsOamIgrEnable':hpnicfMplsOamIgrEnable,_G:hpnicfMplsOamIgrDefectType,'hpnicfMplsOamIgrRowStatus':hpnicfMplsOamIgrRowStatus,'hpnicfMplsOamEgrTable':hpnicfMplsOamEgrTable,'hpnicfMplsOamEgrEntry':hpnicfMplsOamEgrEntry,_O:hpnicfMplsOamEgrIndex,_H:hpnicfMplsOamEgrLspName,'hpnicfMplsOamEgrDetectType':hpnicfMplsOamEgrDetectType,'hpnicfMplsOamEgrDetectFreq':hpnicfMplsOamEgrDetectFreq,'hpnicfMplsOamEgrRevType':hpnicfMplsOamEgrRevType,'hpnicfMplsOamEgrRevLspName':hpnicfMplsOamEgrRevLspName,'hpnicfMplsOamEgrLsrId':hpnicfMplsOamEgrLsrId,'hpnicfMplsOamEgrLspId':hpnicfMplsOamEgrLspId,'hpnicfMplsOamEgrEnable':hpnicfMplsOamEgrEnable,_I:hpnicfMplsOamEgrDefectType,'hpnicfMplsOamEgrRowStatus':hpnicfMplsOamEgrRowStatus,'hpnicfMplsOamNotifications':hpnicfMplsOamNotifications,'hpnicfMplsOamIgrLSPOutDefect':hpnicfMplsOamIgrLSPOutDefect,'hpnicfMplsOamIgrLSPInDefect':hpnicfMplsOamIgrLSPInDefect,'hpnicfMplsOamEgrLSPOutDefect':hpnicfMplsOamEgrLSPOutDefect,'hpnicfMplsOamEgrLSPInDefect':hpnicfMplsOamEgrLSPInDefect})