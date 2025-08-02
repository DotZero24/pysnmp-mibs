_K='h3cDot11RdWmmAC'
_J='h3cDot11WMMRdId'
_I='h3cDot11WMMAPSerialID'
_H='h3cDot11StationWmmAC'
_G='h3cDot11RadioWmmAC'
_F='h3cDot11WmmRadioIndex'
_E='not-accessible'
_D='H3C-DOT11-QOS-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11ObjectIDType,H3cDot11QosAcType,H3cDot11RadioElementIndex,H3cDot11RadioScopeType,h3cDot11=mibBuilder.importSymbols('H3C-DOT11-REF-MIB','H3cDot11ObjectIDType','H3cDot11QosAcType','H3cDot11RadioElementIndex','H3cDot11RadioScopeType','h3cDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cDot11QoS=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,9))
if mibBuilder.loadTexts:h3cDot11QoS.setRevisions(('2008-07-23 12:00',))
class H3cDot11WMMSVPMapAC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('acbk',1),('acbe',2),('acvi',3),('acvo',4),('disable',5)))
class H3cDot11WMMCACPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('channelUtilization',1),('userNumber',2)))
_H3cDot11WmmCfgGroup_ObjectIdentity=ObjectIdentity
h3cDot11WmmCfgGroup=_H3cDot11WmmCfgGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,9,1))
_H3cDot11RadioWmmCfgTable_Object=MibTable
h3cDot11RadioWmmCfgTable=_H3cDot11RadioWmmCfgTable_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1))
if mibBuilder.loadTexts:h3cDot11RadioWmmCfgTable.setStatus(_A)
_H3cDot11RadioWmmCfgEntry_Object=MibTableRow
h3cDot11RadioWmmCfgEntry=_H3cDot11RadioWmmCfgEntry_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1))
h3cDot11RadioWmmCfgEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cDot11RadioWmmCfgEntry.setStatus(_A)
_H3cDot11WmmRadioIndex_Type=H3cDot11RadioElementIndex
_H3cDot11WmmRadioIndex_Object=MibTableColumn
h3cDot11WmmRadioIndex=_H3cDot11WmmRadioIndex_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1,1),_H3cDot11WmmRadioIndex_Type())
h3cDot11WmmRadioIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WmmRadioIndex.setStatus(_A)
_H3cDot11RadioWmmEnabled_Type=TruthValue
_H3cDot11RadioWmmEnabled_Object=MibTableColumn
h3cDot11RadioWmmEnabled=_H3cDot11RadioWmmEnabled_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1,2),_H3cDot11RadioWmmEnabled_Type())
h3cDot11RadioWmmEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWmmEnabled.setStatus(_A)
_H3cDot11RadioSVPMapToAC_Type=H3cDot11WMMSVPMapAC
_H3cDot11RadioSVPMapToAC_Object=MibTableColumn
h3cDot11RadioSVPMapToAC=_H3cDot11RadioSVPMapToAC_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1,3),_H3cDot11RadioSVPMapToAC_Type())
h3cDot11RadioSVPMapToAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioSVPMapToAC.setStatus(_A)
_H3cDot11RadioCacPolicy_Type=H3cDot11WMMCACPolicy
_H3cDot11RadioCacPolicy_Object=MibTableColumn
h3cDot11RadioCacPolicy=_H3cDot11RadioCacPolicy_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1,4),_H3cDot11RadioCacPolicy_Type())
h3cDot11RadioCacPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCacPolicy.setStatus(_A)
class _H3cDot11RadioCacChlUtlValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RadioCacChlUtlValue_Type.__name__=_C
_H3cDot11RadioCacChlUtlValue_Object=MibTableColumn
h3cDot11RadioCacChlUtlValue=_H3cDot11RadioCacChlUtlValue_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1,5),_H3cDot11RadioCacChlUtlValue_Type())
h3cDot11RadioCacChlUtlValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCacChlUtlValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCacChlUtlValue.setUnits('percent')
class _H3cDot11RadioCacUserNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,124))
_H3cDot11RadioCacUserNum_Type.__name__=_C
_H3cDot11RadioCacUserNum_Object=MibTableColumn
h3cDot11RadioCacUserNum=_H3cDot11RadioCacUserNum_Object((1,3,6,1,4,1,2011,10,2,75,9,1,1,1,6),_H3cDot11RadioCacUserNum_Type())
h3cDot11RadioCacUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCacUserNum.setStatus(_A)
_H3cDot11RadioWmmEdcaCfgTable_Object=MibTable
h3cDot11RadioWmmEdcaCfgTable=_H3cDot11RadioWmmEdcaCfgTable_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2))
if mibBuilder.loadTexts:h3cDot11RadioWmmEdcaCfgTable.setStatus(_A)
_H3cDot11RadioWmmEdcaCfgEntry_Object=MibTableRow
h3cDot11RadioWmmEdcaCfgEntry=_H3cDot11RadioWmmEdcaCfgEntry_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1))
h3cDot11RadioWmmEdcaCfgEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:h3cDot11RadioWmmEdcaCfgEntry.setStatus(_A)
_H3cDot11RadioWmmAC_Type=H3cDot11QosAcType
_H3cDot11RadioWmmAC_Object=MibTableColumn
h3cDot11RadioWmmAC=_H3cDot11RadioWmmAC_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1,1),_H3cDot11RadioWmmAC_Type())
h3cDot11RadioWmmAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11RadioWmmAC.setStatus(_A)
class _H3cDot11RadioWmmAifsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_H3cDot11RadioWmmAifsn_Type.__name__=_C
_H3cDot11RadioWmmAifsn_Object=MibTableColumn
h3cDot11RadioWmmAifsn=_H3cDot11RadioWmmAifsn_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1,2),_H3cDot11RadioWmmAifsn_Type())
h3cDot11RadioWmmAifsn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWmmAifsn.setStatus(_A)
class _H3cDot11RadioWmmEcwMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cDot11RadioWmmEcwMin_Type.__name__=_C
_H3cDot11RadioWmmEcwMin_Object=MibTableColumn
h3cDot11RadioWmmEcwMin=_H3cDot11RadioWmmEcwMin_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1,3),_H3cDot11RadioWmmEcwMin_Type())
h3cDot11RadioWmmEcwMin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWmmEcwMin.setStatus(_A)
class _H3cDot11RadioWmmEcwMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cDot11RadioWmmEcwMax_Type.__name__=_C
_H3cDot11RadioWmmEcwMax_Object=MibTableColumn
h3cDot11RadioWmmEcwMax=_H3cDot11RadioWmmEcwMax_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1,4),_H3cDot11RadioWmmEcwMax_Type())
h3cDot11RadioWmmEcwMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWmmEcwMax.setStatus(_A)
class _H3cDot11RadioWmmTxoplimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11RadioWmmTxoplimit_Type.__name__=_C
_H3cDot11RadioWmmTxoplimit_Object=MibTableColumn
h3cDot11RadioWmmTxoplimit=_H3cDot11RadioWmmTxoplimit_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1,5),_H3cDot11RadioWmmTxoplimit_Type())
h3cDot11RadioWmmTxoplimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWmmTxoplimit.setStatus(_A)
_H3cDot11RadioWmmNoAck_Type=TruthValue
_H3cDot11RadioWmmNoAck_Object=MibTableColumn
h3cDot11RadioWmmNoAck=_H3cDot11RadioWmmNoAck_Object((1,3,6,1,4,1,2011,10,2,75,9,1,2,1,6),_H3cDot11RadioWmmNoAck_Type())
h3cDot11RadioWmmNoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWmmNoAck.setStatus(_A)
_H3cDot11StationWmmEdcaTable_Object=MibTable
h3cDot11StationWmmEdcaTable=_H3cDot11StationWmmEdcaTable_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3))
if mibBuilder.loadTexts:h3cDot11StationWmmEdcaTable.setStatus(_A)
_H3cDot11StationWmmEdcaEntry_Object=MibTableRow
h3cDot11StationWmmEdcaEntry=_H3cDot11StationWmmEdcaEntry_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1))
h3cDot11StationWmmEdcaEntry.setIndexNames((0,_D,_F),(0,_D,_H))
if mibBuilder.loadTexts:h3cDot11StationWmmEdcaEntry.setStatus(_A)
_H3cDot11StationWmmAC_Type=H3cDot11QosAcType
_H3cDot11StationWmmAC_Object=MibTableColumn
h3cDot11StationWmmAC=_H3cDot11StationWmmAC_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1,1),_H3cDot11StationWmmAC_Type())
h3cDot11StationWmmAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11StationWmmAC.setStatus(_A)
class _H3cDot11StationWmmAifsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,15))
_H3cDot11StationWmmAifsn_Type.__name__=_C
_H3cDot11StationWmmAifsn_Object=MibTableColumn
h3cDot11StationWmmAifsn=_H3cDot11StationWmmAifsn_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1,2),_H3cDot11StationWmmAifsn_Type())
h3cDot11StationWmmAifsn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationWmmAifsn.setStatus(_A)
class _H3cDot11StationWmmEcwMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cDot11StationWmmEcwMin_Type.__name__=_C
_H3cDot11StationWmmEcwMin_Object=MibTableColumn
h3cDot11StationWmmEcwMin=_H3cDot11StationWmmEcwMin_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1,3),_H3cDot11StationWmmEcwMin_Type())
h3cDot11StationWmmEcwMin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationWmmEcwMin.setStatus(_A)
class _H3cDot11StationWmmEcwMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cDot11StationWmmEcwMax_Type.__name__=_C
_H3cDot11StationWmmEcwMax_Object=MibTableColumn
h3cDot11StationWmmEcwMax=_H3cDot11StationWmmEcwMax_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1,4),_H3cDot11StationWmmEcwMax_Type())
h3cDot11StationWmmEcwMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationWmmEcwMax.setStatus(_A)
class _H3cDot11StationWmmTxoplimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11StationWmmTxoplimit_Type.__name__=_C
_H3cDot11StationWmmTxoplimit_Object=MibTableColumn
h3cDot11StationWmmTxoplimit=_H3cDot11StationWmmTxoplimit_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1,5),_H3cDot11StationWmmTxoplimit_Type())
h3cDot11StationWmmTxoplimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationWmmTxoplimit.setStatus(_A)
_H3cDot11StationWmmCacEnabled_Type=TruthValue
_H3cDot11StationWmmCacEnabled_Object=MibTableColumn
h3cDot11StationWmmCacEnabled=_H3cDot11StationWmmCacEnabled_Object((1,3,6,1,4,1,2011,10,2,75,9,1,3,1,6),_H3cDot11StationWmmCacEnabled_Type())
h3cDot11StationWmmCacEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationWmmCacEnabled.setStatus(_A)
_H3cDot11WmmResetGroup_ObjectIdentity=ObjectIdentity
h3cDot11WmmResetGroup=_H3cDot11WmmResetGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,9,1,4))
_H3cDot11WmmResetRadioByAP_Type=Integer32
_H3cDot11WmmResetRadioByAP_Object=MibScalar
h3cDot11WmmResetRadioByAP=_H3cDot11WmmResetRadioByAP_Object((1,3,6,1,4,1,2011,10,2,75,9,1,4,1),_H3cDot11WmmResetRadioByAP_Type())
h3cDot11WmmResetRadioByAP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WmmResetRadioByAP.setStatus(_A)
_H3cDot11WmmResetStationByAP_Type=Integer32
_H3cDot11WmmResetStationByAP_Object=MibScalar
h3cDot11WmmResetStationByAP=_H3cDot11WmmResetStationByAP_Object((1,3,6,1,4,1,2011,10,2,75,9,1,4,2),_H3cDot11WmmResetStationByAP_Type())
h3cDot11WmmResetStationByAP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WmmResetStationByAP.setStatus(_A)
_H3cDot11RadioWmmEdcaCfg2Table_Object=MibTable
h3cDot11RadioWmmEdcaCfg2Table=_H3cDot11RadioWmmEdcaCfg2Table_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5))
if mibBuilder.loadTexts:h3cDot11RadioWmmEdcaCfg2Table.setStatus(_A)
_H3cDot11RadioWmmEdcaCfg2Entry_Object=MibTableRow
h3cDot11RadioWmmEdcaCfg2Entry=_H3cDot11RadioWmmEdcaCfg2Entry_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1))
h3cDot11RadioWmmEdcaCfg2Entry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:h3cDot11RadioWmmEdcaCfg2Entry.setStatus(_A)
_H3cDot11WMMAPSerialID_Type=H3cDot11ObjectIDType
_H3cDot11WMMAPSerialID_Object=MibTableColumn
h3cDot11WMMAPSerialID=_H3cDot11WMMAPSerialID_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,1),_H3cDot11WMMAPSerialID_Type())
h3cDot11WMMAPSerialID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WMMAPSerialID.setStatus(_A)
_H3cDot11WMMRdId_Type=H3cDot11RadioScopeType
_H3cDot11WMMRdId_Object=MibTableColumn
h3cDot11WMMRdId=_H3cDot11WMMRdId_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,2),_H3cDot11WMMRdId_Type())
h3cDot11WMMRdId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WMMRdId.setStatus(_A)
_H3cDot11RdWmmAC_Type=H3cDot11QosAcType
_H3cDot11RdWmmAC_Object=MibTableColumn
h3cDot11RdWmmAC=_H3cDot11RdWmmAC_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,3),_H3cDot11RdWmmAC_Type())
h3cDot11RdWmmAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11RdWmmAC.setStatus(_A)
class _H3cDot11RdWmmAifsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_H3cDot11RdWmmAifsn_Type.__name__=_C
_H3cDot11RdWmmAifsn_Object=MibTableColumn
h3cDot11RdWmmAifsn=_H3cDot11RdWmmAifsn_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,4),_H3cDot11RdWmmAifsn_Type())
h3cDot11RdWmmAifsn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RdWmmAifsn.setStatus(_A)
class _H3cDot11RdWmmEcwMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cDot11RdWmmEcwMin_Type.__name__=_C
_H3cDot11RdWmmEcwMin_Object=MibTableColumn
h3cDot11RdWmmEcwMin=_H3cDot11RdWmmEcwMin_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,5),_H3cDot11RdWmmEcwMin_Type())
h3cDot11RdWmmEcwMin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RdWmmEcwMin.setStatus(_A)
class _H3cDot11RdWmmEcwMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cDot11RdWmmEcwMax_Type.__name__=_C
_H3cDot11RdWmmEcwMax_Object=MibTableColumn
h3cDot11RdWmmEcwMax=_H3cDot11RdWmmEcwMax_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,6),_H3cDot11RdWmmEcwMax_Type())
h3cDot11RdWmmEcwMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RdWmmEcwMax.setStatus(_A)
class _H3cDot11RdWmmTxoplimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11RdWmmTxoplimit_Type.__name__=_C
_H3cDot11RdWmmTxoplimit_Object=MibTableColumn
h3cDot11RdWmmTxoplimit=_H3cDot11RdWmmTxoplimit_Object((1,3,6,1,4,1,2011,10,2,75,9,1,5,1,7),_H3cDot11RdWmmTxoplimit_Type())
h3cDot11RdWmmTxoplimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RdWmmTxoplimit.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'H3cDot11WMMSVPMapAC':H3cDot11WMMSVPMapAC,'H3cDot11WMMCACPolicy':H3cDot11WMMCACPolicy,'h3cDot11QoS':h3cDot11QoS,'h3cDot11WmmCfgGroup':h3cDot11WmmCfgGroup,'h3cDot11RadioWmmCfgTable':h3cDot11RadioWmmCfgTable,'h3cDot11RadioWmmCfgEntry':h3cDot11RadioWmmCfgEntry,_F:h3cDot11WmmRadioIndex,'h3cDot11RadioWmmEnabled':h3cDot11RadioWmmEnabled,'h3cDot11RadioSVPMapToAC':h3cDot11RadioSVPMapToAC,'h3cDot11RadioCacPolicy':h3cDot11RadioCacPolicy,'h3cDot11RadioCacChlUtlValue':h3cDot11RadioCacChlUtlValue,'h3cDot11RadioCacUserNum':h3cDot11RadioCacUserNum,'h3cDot11RadioWmmEdcaCfgTable':h3cDot11RadioWmmEdcaCfgTable,'h3cDot11RadioWmmEdcaCfgEntry':h3cDot11RadioWmmEdcaCfgEntry,_G:h3cDot11RadioWmmAC,'h3cDot11RadioWmmAifsn':h3cDot11RadioWmmAifsn,'h3cDot11RadioWmmEcwMin':h3cDot11RadioWmmEcwMin,'h3cDot11RadioWmmEcwMax':h3cDot11RadioWmmEcwMax,'h3cDot11RadioWmmTxoplimit':h3cDot11RadioWmmTxoplimit,'h3cDot11RadioWmmNoAck':h3cDot11RadioWmmNoAck,'h3cDot11StationWmmEdcaTable':h3cDot11StationWmmEdcaTable,'h3cDot11StationWmmEdcaEntry':h3cDot11StationWmmEdcaEntry,_H:h3cDot11StationWmmAC,'h3cDot11StationWmmAifsn':h3cDot11StationWmmAifsn,'h3cDot11StationWmmEcwMin':h3cDot11StationWmmEcwMin,'h3cDot11StationWmmEcwMax':h3cDot11StationWmmEcwMax,'h3cDot11StationWmmTxoplimit':h3cDot11StationWmmTxoplimit,'h3cDot11StationWmmCacEnabled':h3cDot11StationWmmCacEnabled,'h3cDot11WmmResetGroup':h3cDot11WmmResetGroup,'h3cDot11WmmResetRadioByAP':h3cDot11WmmResetRadioByAP,'h3cDot11WmmResetStationByAP':h3cDot11WmmResetStationByAP,'h3cDot11RadioWmmEdcaCfg2Table':h3cDot11RadioWmmEdcaCfg2Table,'h3cDot11RadioWmmEdcaCfg2Entry':h3cDot11RadioWmmEdcaCfg2Entry,_I:h3cDot11WMMAPSerialID,_J:h3cDot11WMMRdId,_K:h3cDot11RdWmmAC,'h3cDot11RdWmmAifsn':h3cDot11RdWmmAifsn,'h3cDot11RdWmmEcwMin':h3cDot11RdWmmEcwMin,'h3cDot11RdWmmEcwMax':h3cDot11RdWmmEcwMax,'h3cDot11RdWmmTxoplimit':h3cDot11RdWmmTxoplimit})