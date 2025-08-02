_h='ntcTsDecConfGrpV1Standard'
_g='ntcTsDecMpeCrcVal'
_f='ntcTsDecDefEncProt'
_e='ntcTsDecChannelsAccessVlan'
_d='ntcTsDecChannelsVirualNetwork'
_c='ntcTsDecChannelsLabel'
_b='ntcTsDecChannelsInInstanceName'
_a='ntcTsDecChannelsInTypeName'
_Z='ntcTsDecChannelsEnable'
_Y='ntcTsDecChannelsRowStatus'
_X='ntcTsDecPidsProtocol'
_W='ntcTsDecPidsInInstanceName'
_V='ntcTsDecPidsInTypeName'
_U='ntcTsDecPidsPid'
_T='ntcTsDecPidsEnable'
_S='ntcTsDecPidsRowStatus'
_R='ntcTsDecIsisInInstanceName'
_Q='ntcTsDecIsisInTypeName'
_P='ntcTsDecIsisIsi'
_O='ntcTsDecIsisEnable'
_N='ntcTsDecIsisRowStatus'
_M='read-write'
_L='ntcTsDecChannelsName'
_K='ntcTsDecPidsName'
_J='ntcTsDecIsisName'
_I='NtcEnable'
_H='not-accessible'
_G='Unsigned32'
_F='Integer32'
_E='DisplayString'
_D='OctetString'
_C='read-create'
_B='NEWTEC-TSDECAPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
ntcTsDecaps=ModuleIdentity((1,3,6,1,4,1,5835,5,2,5900))
if mibBuilder.loadTexts:ntcTsDecaps.setRevisions(('2019-05-14 06:00','2015-09-25 11:00','2015-04-13 07:00','2015-01-30 08:00','2014-07-15 08:00','2014-02-03 12:00'))
_NtcTsDecObjects_ObjectIdentity=ObjectIdentity
ntcTsDecObjects=_NtcTsDecObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5900,1))
if mibBuilder.loadTexts:ntcTsDecObjects.setStatus(_A)
_NtcTsDecIsisTable_Object=MibTable
ntcTsDecIsisTable=_NtcTsDecIsisTable_Object((1,3,6,1,4,1,5835,5,2,5900,1,1))
if mibBuilder.loadTexts:ntcTsDecIsisTable.setStatus(_A)
_NtcTsDecIsisEntry_Object=MibTableRow
ntcTsDecIsisEntry=_NtcTsDecIsisEntry_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1))
ntcTsDecIsisEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ntcTsDecIsisEntry.setStatus(_A)
class _NtcTsDecIsisName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcTsDecIsisName_Type.__name__=_E
_NtcTsDecIsisName_Object=MibTableColumn
ntcTsDecIsisName=_NtcTsDecIsisName_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1,1),_NtcTsDecIsisName_Type())
ntcTsDecIsisName.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcTsDecIsisName.setStatus(_A)
_NtcTsDecIsisRowStatus_Type=RowStatus
_NtcTsDecIsisRowStatus_Object=MibTableColumn
ntcTsDecIsisRowStatus=_NtcTsDecIsisRowStatus_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1,2),_NtcTsDecIsisRowStatus_Type())
ntcTsDecIsisRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecIsisRowStatus.setStatus(_A)
_NtcTsDecIsisEnable_Type=NtcEnable
_NtcTsDecIsisEnable_Object=MibTableColumn
ntcTsDecIsisEnable=_NtcTsDecIsisEnable_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1,3),_NtcTsDecIsisEnable_Type())
ntcTsDecIsisEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecIsisEnable.setStatus(_A)
_NtcTsDecIsisIsi_Type=Unsigned32
_NtcTsDecIsisIsi_Object=MibTableColumn
ntcTsDecIsisIsi=_NtcTsDecIsisIsi_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1,4),_NtcTsDecIsisIsi_Type())
ntcTsDecIsisIsi.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecIsisIsi.setStatus(_A)
class _NtcTsDecIsisInTypeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecIsisInTypeName_Type.__name__=_D
_NtcTsDecIsisInTypeName_Object=MibTableColumn
ntcTsDecIsisInTypeName=_NtcTsDecIsisInTypeName_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1,5),_NtcTsDecIsisInTypeName_Type())
ntcTsDecIsisInTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecIsisInTypeName.setStatus(_A)
class _NtcTsDecIsisInInstanceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecIsisInInstanceName_Type.__name__=_D
_NtcTsDecIsisInInstanceName_Object=MibTableColumn
ntcTsDecIsisInInstanceName=_NtcTsDecIsisInInstanceName_Object((1,3,6,1,4,1,5835,5,2,5900,1,1,1,6),_NtcTsDecIsisInInstanceName_Type())
ntcTsDecIsisInInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecIsisInInstanceName.setStatus(_A)
_NtcTsDecPidsTable_Object=MibTable
ntcTsDecPidsTable=_NtcTsDecPidsTable_Object((1,3,6,1,4,1,5835,5,2,5900,1,2))
if mibBuilder.loadTexts:ntcTsDecPidsTable.setStatus(_A)
_NtcTsDecPidsEntry_Object=MibTableRow
ntcTsDecPidsEntry=_NtcTsDecPidsEntry_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1))
ntcTsDecPidsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ntcTsDecPidsEntry.setStatus(_A)
class _NtcTsDecPidsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcTsDecPidsName_Type.__name__=_E
_NtcTsDecPidsName_Object=MibTableColumn
ntcTsDecPidsName=_NtcTsDecPidsName_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,1),_NtcTsDecPidsName_Type())
ntcTsDecPidsName.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcTsDecPidsName.setStatus(_A)
_NtcTsDecPidsRowStatus_Type=RowStatus
_NtcTsDecPidsRowStatus_Object=MibTableColumn
ntcTsDecPidsRowStatus=_NtcTsDecPidsRowStatus_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,2),_NtcTsDecPidsRowStatus_Type())
ntcTsDecPidsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecPidsRowStatus.setStatus(_A)
_NtcTsDecPidsEnable_Type=NtcEnable
_NtcTsDecPidsEnable_Object=MibTableColumn
ntcTsDecPidsEnable=_NtcTsDecPidsEnable_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,3),_NtcTsDecPidsEnable_Type())
ntcTsDecPidsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecPidsEnable.setStatus(_A)
class _NtcTsDecPidsPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcTsDecPidsPid_Type.__name__=_G
_NtcTsDecPidsPid_Object=MibTableColumn
ntcTsDecPidsPid=_NtcTsDecPidsPid_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,4),_NtcTsDecPidsPid_Type())
ntcTsDecPidsPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecPidsPid.setStatus(_A)
class _NtcTsDecPidsInTypeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecPidsInTypeName_Type.__name__=_D
_NtcTsDecPidsInTypeName_Object=MibTableColumn
ntcTsDecPidsInTypeName=_NtcTsDecPidsInTypeName_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,5),_NtcTsDecPidsInTypeName_Type())
ntcTsDecPidsInTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecPidsInTypeName.setStatus(_A)
class _NtcTsDecPidsInInstanceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecPidsInInstanceName_Type.__name__=_D
_NtcTsDecPidsInInstanceName_Object=MibTableColumn
ntcTsDecPidsInInstanceName=_NtcTsDecPidsInInstanceName_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,6),_NtcTsDecPidsInInstanceName_Type())
ntcTsDecPidsInInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecPidsInInstanceName.setStatus(_A)
class _NtcTsDecPidsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('mpe',1),('ule',2)))
_NtcTsDecPidsProtocol_Type.__name__=_F
_NtcTsDecPidsProtocol_Object=MibTableColumn
ntcTsDecPidsProtocol=_NtcTsDecPidsProtocol_Object((1,3,6,1,4,1,5835,5,2,5900,1,2,1,7),_NtcTsDecPidsProtocol_Type())
ntcTsDecPidsProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecPidsProtocol.setStatus(_A)
_NtcTsDecChannelsTable_Object=MibTable
ntcTsDecChannelsTable=_NtcTsDecChannelsTable_Object((1,3,6,1,4,1,5835,5,2,5900,1,3))
if mibBuilder.loadTexts:ntcTsDecChannelsTable.setStatus(_A)
_NtcTsDecChannelsEntry_Object=MibTableRow
ntcTsDecChannelsEntry=_NtcTsDecChannelsEntry_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1))
ntcTsDecChannelsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ntcTsDecChannelsEntry.setStatus(_A)
class _NtcTsDecChannelsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcTsDecChannelsName_Type.__name__=_E
_NtcTsDecChannelsName_Object=MibTableColumn
ntcTsDecChannelsName=_NtcTsDecChannelsName_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,1),_NtcTsDecChannelsName_Type())
ntcTsDecChannelsName.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcTsDecChannelsName.setStatus(_A)
_NtcTsDecChannelsRowStatus_Type=RowStatus
_NtcTsDecChannelsRowStatus_Object=MibTableColumn
ntcTsDecChannelsRowStatus=_NtcTsDecChannelsRowStatus_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,2),_NtcTsDecChannelsRowStatus_Type())
ntcTsDecChannelsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsRowStatus.setStatus(_A)
_NtcTsDecChannelsEnable_Type=NtcEnable
_NtcTsDecChannelsEnable_Object=MibTableColumn
ntcTsDecChannelsEnable=_NtcTsDecChannelsEnable_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,3),_NtcTsDecChannelsEnable_Type())
ntcTsDecChannelsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsEnable.setStatus(_A)
class _NtcTsDecChannelsInTypeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecChannelsInTypeName_Type.__name__=_D
_NtcTsDecChannelsInTypeName_Object=MibTableColumn
ntcTsDecChannelsInTypeName=_NtcTsDecChannelsInTypeName_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,4),_NtcTsDecChannelsInTypeName_Type())
ntcTsDecChannelsInTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsInTypeName.setStatus(_A)
class _NtcTsDecChannelsInInstanceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecChannelsInInstanceName_Type.__name__=_D
_NtcTsDecChannelsInInstanceName_Object=MibTableColumn
ntcTsDecChannelsInInstanceName=_NtcTsDecChannelsInInstanceName_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,5),_NtcTsDecChannelsInInstanceName_Type())
ntcTsDecChannelsInInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsInInstanceName.setStatus(_A)
class _NtcTsDecChannelsLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTsDecChannelsLabel_Type.__name__=_E
_NtcTsDecChannelsLabel_Object=MibTableColumn
ntcTsDecChannelsLabel=_NtcTsDecChannelsLabel_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,6),_NtcTsDecChannelsLabel_Type())
ntcTsDecChannelsLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsLabel.setStatus(_A)
class _NtcTsDecChannelsVirualNetwork_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsDecChannelsVirualNetwork_Type.__name__=_D
_NtcTsDecChannelsVirualNetwork_Object=MibTableColumn
ntcTsDecChannelsVirualNetwork=_NtcTsDecChannelsVirualNetwork_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,7),_NtcTsDecChannelsVirualNetwork_Type())
ntcTsDecChannelsVirualNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsVirualNetwork.setStatus(_A)
class _NtcTsDecChannelsAccessVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NtcTsDecChannelsAccessVlan_Type.__name__=_G
_NtcTsDecChannelsAccessVlan_Object=MibTableColumn
ntcTsDecChannelsAccessVlan=_NtcTsDecChannelsAccessVlan_Object((1,3,6,1,4,1,5835,5,2,5900,1,3,1,8),_NtcTsDecChannelsAccessVlan_Type())
ntcTsDecChannelsAccessVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsDecChannelsAccessVlan.setStatus(_A)
class _NtcTsDecDefEncProt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mpe',0),('ule',1)))
_NtcTsDecDefEncProt_Type.__name__=_F
_NtcTsDecDefEncProt_Object=MibScalar
ntcTsDecDefEncProt=_NtcTsDecDefEncProt_Object((1,3,6,1,4,1,5835,5,2,5900,1,4),_NtcTsDecDefEncProt_Type())
ntcTsDecDefEncProt.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcTsDecDefEncProt.setStatus(_A)
class _NtcTsDecMpeCrcVal_Type(NtcEnable):defaultValue=1
_NtcTsDecMpeCrcVal_Type.__name__=_I
_NtcTsDecMpeCrcVal_Object=MibScalar
ntcTsDecMpeCrcVal=_NtcTsDecMpeCrcVal_Object((1,3,6,1,4,1,5835,5,2,5900,1,5),_NtcTsDecMpeCrcVal_Type())
ntcTsDecMpeCrcVal.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcTsDecMpeCrcVal.setStatus(_A)
_NtcTsDecConformance_ObjectIdentity=ObjectIdentity
ntcTsDecConformance=_NtcTsDecConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5900,2))
if mibBuilder.loadTexts:ntcTsDecConformance.setStatus(_A)
_NtcTsDecConfCompliance_ObjectIdentity=ObjectIdentity
ntcTsDecConfCompliance=_NtcTsDecConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5900,2,1))
if mibBuilder.loadTexts:ntcTsDecConfCompliance.setStatus(_A)
_NtcTsDecConfGroup_ObjectIdentity=ObjectIdentity
ntcTsDecConfGroup=_NtcTsDecConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5900,2,2))
if mibBuilder.loadTexts:ntcTsDecConfGroup.setStatus(_A)
ntcTsDecConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,5900,2,2,1))
ntcTsDecConfGrpV1Standard.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ntcTsDecConfGrpV1Standard.setStatus(_A)
ntcTsDecConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,5900,2,1,1))
ntcTsDecConfCompV1Standard.setObjects((_B,_h))
if mibBuilder.loadTexts:ntcTsDecConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTsDecaps':ntcTsDecaps,'ntcTsDecObjects':ntcTsDecObjects,'ntcTsDecIsisTable':ntcTsDecIsisTable,'ntcTsDecIsisEntry':ntcTsDecIsisEntry,_J:ntcTsDecIsisName,_N:ntcTsDecIsisRowStatus,_O:ntcTsDecIsisEnable,_P:ntcTsDecIsisIsi,_Q:ntcTsDecIsisInTypeName,_R:ntcTsDecIsisInInstanceName,'ntcTsDecPidsTable':ntcTsDecPidsTable,'ntcTsDecPidsEntry':ntcTsDecPidsEntry,_K:ntcTsDecPidsName,_S:ntcTsDecPidsRowStatus,_T:ntcTsDecPidsEnable,_U:ntcTsDecPidsPid,_V:ntcTsDecPidsInTypeName,_W:ntcTsDecPidsInInstanceName,_X:ntcTsDecPidsProtocol,'ntcTsDecChannelsTable':ntcTsDecChannelsTable,'ntcTsDecChannelsEntry':ntcTsDecChannelsEntry,_L:ntcTsDecChannelsName,_Y:ntcTsDecChannelsRowStatus,_Z:ntcTsDecChannelsEnable,_a:ntcTsDecChannelsInTypeName,_b:ntcTsDecChannelsInInstanceName,_c:ntcTsDecChannelsLabel,_d:ntcTsDecChannelsVirualNetwork,_e:ntcTsDecChannelsAccessVlan,_f:ntcTsDecDefEncProt,_g:ntcTsDecMpeCrcVal,'ntcTsDecConformance':ntcTsDecConformance,'ntcTsDecConfCompliance':ntcTsDecConfCompliance,'ntcTsDecConfCompV1Standard':ntcTsDecConfCompV1Standard,'ntcTsDecConfGroup':ntcTsDecConfGroup,_h:ntcTsDecConfGrpV1Standard})